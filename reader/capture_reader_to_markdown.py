#!/usr/bin/env python3
"""Capture Readwise Reader docs into versioned local markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = Path(__file__).parent / ".env"
ARTICLES_DIR = REPO_ROOT / "sources" / "articles"
IMAGES_DIR = REPO_ROOT / "sources" / "images"
MANIFEST_PATH = ARTICLES_DIR / "manifest.jsonl"
API_BASE = "https://readwise.io/api/v3"
READER_CATEGORIES = {"article", "rss"}
REQUEST_TIMEOUT = 30
IMAGE_TIMEOUT = 20
NOTION_VERSION = "2022-06-28"
DEFAULT_RAW_DATABASE_TITLE = "Export via Reader"

PRIVATE_URL_MARKERS = (
    "access_token=",
    "passport.online/member",
    "member/login?email=",
    "member/podcast?",
    "gaurav_a@tamu.edu",
    "gaurav_a%40tamu.edu",
)

DROP_QUERY_KEYS = {
    "access_token",
    "token",
    "email",
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "utm_id",
    "triedredirect",
    "rcm",
    "si",
    "lc",
}


def env_value(name: str, local_env: dict[str, str | None], fallback_name: str | None = None) -> str:
    return (
        os.environ.get(name)
        or local_env.get(name)
        or (local_env.get(fallback_name) if fallback_name else "")
        or ""
    ).strip()


def load_runtime_config() -> dict[str, str]:
    local_env = load_local_env(ENV_FILE)
    return {
        "readwise_token": env_value("READWISE_TOKEN", local_env, "readwise_token"),
        "notion_token": env_value("NOTION_TOKEN", local_env, "notion_api"),
        "notion_database_id": env_value("NOTION_DATABASE_ID", local_env, "database_id"),
        "notion_database_title": env_value("NOTION_DATABASE_TITLE", local_env, "notion_database_title")
        or DEFAULT_RAW_DATABASE_TITLE,
    }


def load_local_env(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def slugify(text: str, limit: int = 90) -> str:
    text = (text or "untitled").lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:limit].strip("-") or "untitled"


def safe_date(value: Any) -> str:
    if not value:
        return ""
    value = str(value)
    return value[:10] if len(value) >= 10 else value


def sanitize_url(url: str | None) -> str:
    if not url:
        return ""
    raw = str(url).strip().strip("<>").strip()
    if not raw:
        return ""
    try:
        parsed = urllib.parse.urlsplit(raw)
    except ValueError:
        return re.split(r"[?#]", raw, maxsplit=1)[0]
    if parsed.scheme not in {"http", "https"}:
        return raw

    host = parsed.netloc.lower()
    path = parsed.path or "/"
    query_pairs = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query_pairs = [
        (key, value)
        for key, value in query_pairs
        if key.lower() not in DROP_QUERY_KEYS and not key.lower().startswith("utm_")
    ]

    if "passport.online" in host and path.startswith("/member"):
        return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, "/", "", ""))
    if path.startswith("/member/login") or path.startswith("/member/podcast"):
        return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, "/", "", ""))

    query = urllib.parse.urlencode(query_pairs, doseq=True)
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, path, query, ""))


URL_RE = re.compile(r"https?://[^\s<>)\"']+")


def sanitize_text_urls(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        value = match.group(0)
        trailing = ""
        while value and value[-1] in ".,;:!?]":
            trailing = value[-1] + trailing
            value = value[:-1]
        return sanitize_url(value) + trailing

    return URL_RE.sub(replace, text)


PRIVATE_FOOTER_LINE_RE = re.compile(
    r"(?im)^\s*(?:Member:\s*Gaurav Arora|Email:\s*gaurav_a@tamu\.edu)\s*$\n?"
)


def sanitize_private_text(text: str) -> str:
    text = PRIVATE_FOOTER_LINE_RE.sub("", text)
    return text.replace("gaurav_a%40tamu.edu", "")


def has_private_url_material(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in PRIVATE_URL_MARKERS)


def normalize_markdown(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in normalized.split("\n")]
    return "\n".join(lines).strip() + "\n"


def yaml_string(value: Any) -> str:
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def yaml_list(values: list[str]) -> str:
    return "[" + ", ".join(json.dumps(str(value), ensure_ascii=False) for value in values) + "]"


def normalize_tags(tags_raw: Any) -> list[str]:
    if isinstance(tags_raw, dict):
        return sorted(str(key) for key in tags_raw.keys())
    if isinstance(tags_raw, list):
        return sorted(str(value) for value in tags_raw)
    return []


def html_to_markdown(html: str) -> str:
    import html2text

    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    converter.body_width = 0
    converter.unicode_snob = True
    converter.protect_links = True
    return normalize_markdown(sanitize_private_text(sanitize_text_urls(converter.handle(html or ""))))


def content_hash_for(frontmatter_without_hash: str, body: str) -> str:
    digest = hashlib.sha256()
    digest.update(frontmatter_without_hash.encode("utf-8"))
    digest.update(b"\n")
    digest.update(body.encode("utf-8"))
    return digest.hexdigest()


def build_frontmatter(doc: dict[str, Any], body: str, notion_page_id: str = "", image_path: str = "") -> tuple[str, str]:
    reader_id = str(doc.get("id") or "")
    reader_url = sanitize_url(doc.get("url") or f"https://read.readwise.io/read/{reader_id}")
    source_url = sanitize_url(doc.get("source_url") or "")
    tags = normalize_tags(doc.get("tags") or {})

    fields: list[tuple[str, str]] = [
        ("title", yaml_string(doc.get("title") or "Untitled")),
        ("reader_id", yaml_string(reader_id)),
        ("notion_page_id", yaml_string(notion_page_id)),
        ("reader_url", yaml_string(reader_url)),
        ("source_url", yaml_string(source_url)),
        ("author", yaml_string(doc.get("author") or "")),
        ("site", yaml_string(doc.get("site_name") or "")),
        ("tags", yaml_list(tags)),
        ("published", yaml_string(safe_date(doc.get("published_date")))),
        ("saved_at", yaml_string(safe_date(doc.get("saved_at")))),
        ("reading_time", yaml_string(doc.get("reading_time") or "")),
        ("summary", yaml_string(sanitize_private_text(sanitize_text_urls(doc.get("summary") or "")))),
    ]
    if image_path:
        fields.append(("image", yaml_string(image_path)))

    frontmatter_without_hash = "---\n" + "\n".join(f"{key}: {value}" for key, value in fields) + "\n"
    content_hash = content_hash_for(frontmatter_without_hash, body)
    fields.append(("content_hash", yaml_string(content_hash)))
    frontmatter = "---\n" + "\n".join(f"{key}: {value}" for key, value in fields) + "\n---\n\n"
    return frontmatter, content_hash


FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return {}
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] == '"':
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                value = value.strip('"')
        data[key.strip()] = str(value)
    return data


def index_existing_articles(articles_dir: Path) -> dict[str, dict[str, Path]]:
    index = {"reader_id": {}, "source_url": {}, "slug": {}}
    for path in sorted(articles_dir.glob("*.md")):
        if path.name == "manifest.jsonl":
            continue
        meta = parse_frontmatter(path)
        if meta.get("reader_id"):
            index["reader_id"][meta["reader_id"]] = path
        if meta.get("source_url"):
            index["source_url"][sanitize_url(meta["source_url"])] = path
        index["slug"][path.stem] = path
    return index


def choose_article_path(
    doc: dict[str, Any],
    existing_index: dict[str, dict[str, Path]],
    used_paths: set[Path],
    articles_dir: Path = ARTICLES_DIR,
) -> Path:
    reader_id = str(doc.get("id") or "")
    source_url = sanitize_url(doc.get("source_url") or "")
    slug = slugify(doc.get("title") or "untitled")

    for candidate in (
        existing_index["reader_id"].get(reader_id),
        existing_index["source_url"].get(source_url),
        existing_index["slug"].get(slug),
    ):
        if candidate and candidate not in used_paths:
            return candidate

    candidate = articles_dir / f"{slug}.md"
    if candidate not in used_paths and not candidate.exists():
        return candidate

    suffix = reader_id[:8] if reader_id else hashlib.sha1(slug.encode()).hexdigest()[:8]
    candidate = articles_dir / f"{slug}-{suffix}.md"
    counter = 2
    while candidate in used_paths or candidate.exists():
        candidate = articles_dir / f"{slug}-{suffix}-{counter}.md"
        counter += 1
    return candidate


def extension_from_response(url: str, response: requests.Response) -> str:
    content_type = response.headers.get("content-type", "").split(";")[0].strip().lower()
    by_type = {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/svg+xml": ".svg",
    }
    if content_type in by_type:
        return by_type[content_type]
    suffix = Path(urllib.parse.urlsplit(url).path).suffix.lower()
    return suffix if suffix in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"} else ".jpg"


def download_image(url: str, dest_stem: Path, session: requests.Session, apply: bool) -> str:
    sanitized = sanitize_url(url)
    if not sanitized.startswith(("http://", "https://")):
        return sanitized
    if not apply:
        return sanitized
    try:
        response = session.get(sanitized, timeout=IMAGE_TIMEOUT, stream=True)
        response.raise_for_status()
        final_path = dest_stem.with_suffix(extension_from_response(sanitized, response))
        final_path.parent.mkdir(parents=True, exist_ok=True)
        with final_path.open("wb") as handle:
            for chunk in response.iter_content(8192):
                if chunk:
                    handle.write(chunk)
        return os.path.relpath(final_path, REPO_ROOT)
    except Exception as exc:
        print(f"  image download failed: {sanitized[:80]} ({exc})")
        return sanitized


def localize_images(html: str, reader_id: str, session: requests.Session, apply: bool, download_images: bool) -> tuple[str, list[str]]:
    if not html:
        return "", []

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html or "", "html.parser")
    assets: list[str] = []
    for index, img in enumerate(soup.find_all("img")):
        src = img.get("src") or ""
        if not src:
            continue
        sanitized = sanitize_url(src)
        if download_images:
            url_hash = hashlib.sha256(sanitized.encode("utf-8")).hexdigest()[:12]
            replacement = download_image(sanitized, IMAGES_DIR / f"{reader_id}_{index}_{url_hash}", session, apply)
        else:
            replacement = sanitized
        img["src"] = replacement
        if replacement.startswith("sources/images/"):
            assets.append(replacement)
    return str(soup), assets


def load_manifest(path: Path = MANIFEST_PATH) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    records: dict[str, dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        records[str(record["reader_id"])] = record
    return records


def write_manifest(records: dict[str, dict[str, Any]], path: Path = MANIFEST_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        json.dumps(record, ensure_ascii=False, sort_keys=True)
        for record in sorted(records.values(), key=lambda item: str(item.get("path", "")))
    ]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def request_with_retry(
    session: requests.Session,
    method: str,
    url: str,
    attempts: int = 5,
    **kwargs: Any,
) -> requests.Response:
    retry_statuses = {429, 500, 502, 503, 504}
    for attempt in range(1, attempts + 1):
        response = session.request(method, url, **kwargs)
        if response.status_code not in retry_statuses or attempt == attempts:
            return response
        retry_after = response.headers.get("Retry-After")
        delay = int(retry_after) if retry_after and retry_after.isdigit() else min(30, 2 ** attempt)
        print(f"  {method.upper()} {url} returned {response.status_code}; retrying in {delay}s")
        time.sleep(delay)
    return response


def fetch_reader_docs(token: str, session: requests.Session, max_items: int | None = None) -> list[dict[str, Any]]:
    headers = {"Authorization": f"Token {token}"}
    params: dict[str, str] = {"withHtmlContent": "true"}
    docs: list[dict[str, Any]] = []
    page = 0
    while True:
        response = request_with_retry(
            session,
            "get",
            f"{API_BASE}/list/",
            headers=headers,
            params=params,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()
        page += 1
        print(f"  Reader page {page}: {len(data.get('results', []))} docs")
        for doc in data.get("results", []):
            if doc.get("parent_id") is not None:
                continue
            if doc.get("category") not in READER_CATEGORIES:
                continue
            docs.append(doc)
            if max_items and len(docs) >= max_items:
                return docs
        cursor = data.get("nextPageCursor")
        if not cursor:
            break
        params["pageCursor"] = cursor
        time.sleep(0.6)
    return docs


def reader_id_from_url(url: str) -> str:
    match = re.search(r"/(01\w+)/?$", url or "")
    return match.group(1) if match else ""


def notion_title_text(parts: list[dict[str, Any]]) -> str:
    return "".join(part.get("plain_text", "") for part in parts)


def find_notion_database_id(token: str, title: str, session: requests.Session) -> str:
    if not token or not title:
        return ""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }
    payload = {
        "query": title,
        "filter": {"property": "object", "value": "database"},
        "page_size": 20,
    }
    response = request_with_retry(
        session,
        "post",
        "https://api.notion.com/v1/search",
        headers=headers,
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    for result in response.json().get("results", []):
        if notion_title_text(result.get("title", [])) == title:
            return result.get("id", "")
    return ""


def fetch_notion_page_map(token: str, database_id: str, session: requests.Session) -> dict[str, str]:
    if not token or not database_id:
        return {}
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    payload: dict[str, Any] = {"page_size": 100}
    page_map: dict[str, str] = {}
    while True:
        response = request_with_retry(session, "post", url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        for page in data.get("results", []):
            props = page.get("properties", {})
            reader_url = props.get("Reader URL", {}).get("url") or ""
            reader_id = reader_id_from_url(reader_url)
            if reader_id:
                page_map[reader_id] = page.get("id", "")
        if not data.get("has_more"):
            break
        payload["start_cursor"] = data.get("next_cursor")
    return page_map


def build_article(doc: dict[str, Any], notion_page_id: str, session: requests.Session, apply: bool, download_images: bool) -> tuple[str, str, list[str]]:
    reader_id = str(doc.get("id") or "")
    cover_path = ""
    assets: list[str] = []
    if doc.get("image_url") and download_images:
        cover_hash = hashlib.sha256(sanitize_url(doc["image_url"]).encode("utf-8")).hexdigest()[:12]
        cover_path = download_image(doc["image_url"], IMAGES_DIR / f"{reader_id}_cover_{cover_hash}", session, apply)
        if cover_path.startswith("sources/images/"):
            assets.append(cover_path)

    html, inline_assets = localize_images(doc.get("html_content") or "", reader_id, session, apply, download_images)
    assets.extend(inline_assets)
    if html:
        body = html_to_markdown(html)
    else:
        source = sanitize_url(doc.get("source_url") or doc.get("url") or "")
        body = f"> *No content available. Read at source: {source}*\n"
    frontmatter, content_hash = build_frontmatter(doc, body, notion_page_id=notion_page_id, image_path=cover_path)
    article = frontmatter + body
    if has_private_url_material(article):
        raise ValueError(f"private URL material remained in {doc.get('id')}: {doc.get('title')}")
    return article, content_hash, sorted(set(assets))


def capture_docs(
    docs: list[dict[str, Any]],
    notion_page_map: dict[str, str],
    apply: bool,
    download_images: bool,
    articles_dir: Path = ARTICLES_DIR,
    manifest_path: Path = MANIFEST_PATH,
) -> dict[str, int]:
    import requests

    articles_dir.mkdir(parents=True, exist_ok=True)
    if download_images and apply:
        IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    existing_index = index_existing_articles(articles_dir)
    manifest = load_manifest(manifest_path)
    used_paths: set[Path] = set()
    now = datetime.now(timezone.utc).isoformat()
    stats = {"created": 0, "updated": 0, "skipped": 0, "planned": 0}
    session = requests.Session()
    session.headers["User-Agent"] = "llmwikirepo-capture/1.0"

    for doc in docs:
        reader_id = str(doc.get("id") or "")
        path = choose_article_path(doc, existing_index, used_paths, articles_dir=articles_dir)
        used_paths.add(path)
        notion_page_id = notion_page_map.get(reader_id, "")
        article, content_hash, assets = build_article(doc, notion_page_id, session, apply=apply, download_images=download_images)
        rel_path = os.path.relpath(path, REPO_ROOT)
        prior = manifest.get(reader_id)

        current_meta = parse_frontmatter(path) if path.exists() else {}
        current_hash = current_meta.get("content_hash", "")
        if prior and prior.get("content_hash") == content_hash and current_hash == content_hash and path.exists():
            stats["skipped"] += 1
            continue

        action = "created" if not path.exists() else "updated"
        stats[action] += 1
        stats["planned"] += 1

        record = {
            "reader_id": reader_id,
            "notion_page_id": notion_page_id,
            "path": rel_path,
            "reader_url": sanitize_url(doc.get("url") or f"https://read.readwise.io/read/{reader_id}"),
            "source_url": sanitize_url(doc.get("source_url") or ""),
            "title": doc.get("title") or "Untitled",
            "saved_at": safe_date(doc.get("saved_at")),
            "content_hash": content_hash,
            "assets": assets,
            "captured_at": prior.get("captured_at", now) if prior and prior.get("content_hash") == content_hash else now,
        }
        manifest[reader_id] = record

        if apply:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(article, encoding="utf-8")
        print(f"  {action}: {rel_path}")

    if apply:
        write_manifest(manifest, manifest_path)
    return stats


def main() -> int:
    import requests

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write markdown files and manifest")
    parser.add_argument("--max-items", type=int, default=None, help="limit Reader docs for testing")
    parser.add_argument("--download-images", action="store_true", help="download cover and inline images into sources/images")
    parser.add_argument("--no-image-download", action="store_true", help="deprecated; external image URLs are preserved by default")
    args = parser.parse_args()

    config = load_runtime_config()
    if not config["readwise_token"]:
        print("Missing READWISE_TOKEN or reader/.env readwise_token", file=sys.stderr)
        return 2

    session = requests.Session()
    session.headers["User-Agent"] = "llmwikirepo-capture/1.0"
    print("Fetching Reader docs...")
    docs = fetch_reader_docs(config["readwise_token"], session, max_items=args.max_items)
    print(f"Reader docs selected: {len(docs)}")

    notion_database_id = config["notion_database_id"]
    if config["notion_token"] and not notion_database_id:
        notion_database_id = find_notion_database_id(config["notion_token"], config["notion_database_title"], session)
        if notion_database_id:
            print(f"Resolved Notion database: {config['notion_database_title']}")

    notion_page_map = fetch_notion_page_map(config["notion_token"], notion_database_id, session)
    if notion_page_map:
        print(f"Notion page IDs mapped: {len(notion_page_map)}")
    else:
        print("Notion page ID mapping skipped or empty")

    stats = capture_docs(
        docs,
        notion_page_map,
        apply=args.apply,
        download_images=args.download_images and not args.no_image_download,
    )
    mode = "applied" if args.apply else "dry-run"
    print(
        f"Capture {mode}: {stats['created']} created, {stats['updated']} updated, "
        f"{stats['skipped']} skipped, {stats['planned']} planned writes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
