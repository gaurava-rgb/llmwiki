#!/usr/bin/env python3
"""Fetch 20 articles from Readwise Reader (10 Stratechery + 10 others) → markdown files."""

import os
import re
import sys
import time
import hashlib
import urllib.parse
from pathlib import Path
from typing import Optional

import requests
import html2text
from dotenv import dotenv_values

# ── Paths ──────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
ENV_FILE = Path(__file__).parent / ".env"
ARTICLES_DIR = REPO_ROOT / "sources" / "articles"
IMAGES_DIR = REPO_ROOT / "sources" / "images"

ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# ── Config ─────────────────────────────────────────────────────────────────────
API_BASE = "https://readwise.io/api/v3"
TARGET_STRATECHERY = 10
TARGET_OTHER = 10
STRATECHERY_DOMAIN = "stratechery.com"
CATEGORIES = {"article", "rss"}
REQUEST_TIMEOUT = 30
IMAGE_TIMEOUT = 20


def load_token() -> str:
    cfg = dotenv_values(ENV_FILE)
    token = cfg.get("readwise_token") or os.environ.get("READWISE_TOKEN", "")
    if not token:
        sys.exit("No readwise_token found in reader/.env")
    return token.strip()


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:80].strip("-")


def download_image(url: str, dest: Path, session: requests.Session) -> Optional[Path]:
    """Download image to dest, return path or None on failure."""
    if not url or not url.startswith("http"):
        return None
    try:
        r = session.get(url, timeout=IMAGE_TIMEOUT, stream=True)
        r.raise_for_status()
        content_type = r.headers.get("content-type", "")
        ext = {
            "image/jpeg": ".jpg", "image/jpg": ".jpg",
            "image/png": ".png", "image/gif": ".gif",
            "image/webp": ".webp", "image/svg+xml": ".svg",
        }.get(content_type.split(";")[0].strip(), "")
        if not ext:
            # guess from URL
            parsed_path = urllib.parse.urlparse(url).path
            url_ext = Path(parsed_path).suffix[:5].lower()
            ext = url_ext if url_ext in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"} else ".jpg"
        final = dest.with_suffix(ext)
        with open(final, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        return final
    except Exception as e:
        print(f"  ⚠ Image download failed {url[:60]}: {e}")
        return None


def process_html_images(html: str, article_id: str, session: requests.Session) -> str:
    """Download inline images, replace src with local relative paths."""
    img_pattern = re.compile(r'<img([^>]*?)src=["\']([^"\']+)["\']([^>]*?)/?>', re.IGNORECASE)
    counter = [0]

    def replace_img(m: re.Match) -> str:
        before, url, after = m.group(1), m.group(2), m.group(3)
        if not url.startswith("http"):
            return m.group(0)
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        dest_stem = IMAGES_DIR / f"{article_id}_{counter[0]}_{url_hash}"
        counter[0] += 1
        local = download_image(url, dest_stem, session)
        if local:
            rel = os.path.relpath(local, REPO_ROOT)
            return f'<img{before}src="{rel}"{after}>'
        return m.group(0)  # keep original on failure

    return img_pattern.sub(replace_img, html)


def html_to_markdown(html: str) -> str:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # no wrapping
    h.unicode_snob = True
    h.protect_links = True
    return h.handle(html)


def build_frontmatter(doc: dict, cover_local: Optional[Path]) -> str:
    title = doc.get("title", "Untitled").replace('"', '\\"')
    author = doc.get("author") or ""
    source_url = doc.get("source_url") or doc.get("url", "")
    site = doc.get("site_name") or ""
    tags_raw = doc.get("tags") or {}
    tags = list(tags_raw.keys()) if isinstance(tags_raw, dict) else list(tags_raw)
    published = doc.get("published_date") or ""
    saved_at = (doc.get("saved_at") or "")[:10]
    reading_time = doc.get("reading_time") or ""
    summary = (doc.get("summary") or "").replace('"', '\\"')
    cover = str(os.path.relpath(cover_local, REPO_ROOT)) if cover_local else ""

    lines = [
        "---",
        f'title: "{title}"',
        f'author: "{author}"',
        f'source_url: "{source_url}"',
        f'site: "{site}"',
        f"tags: {tags}",
        f'published: "{published}"',
        f'saved_at: "{saved_at}"',
        f'reading_time: "{reading_time}"',
        f'summary: "{summary}"',
    ]
    if cover:
        lines.append(f'image: "{cover}"')
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def fetch_documents(token: str, session: requests.Session):
    """Yield documents from Reader API, filtering by category and parent_id."""
    params = {
        "withHtmlContent": "true",
        "pageCursor": None,
    }
    headers = {"Authorization": f"Token {token}"}
    page = 0

    while True:
        p = {k: v for k, v in params.items() if v is not None}
        r = session.get(f"{API_BASE}/list/", headers=headers, params=p, timeout=REQUEST_TIMEOUT)
        r.raise_for_status()
        data = r.json()
        page += 1
        results = data.get("results", [])
        print(f"  Fetched page {page}: {len(results)} docs")

        for doc in results:
            if doc.get("parent_id") is not None:
                continue
            if doc.get("category") not in CATEGORIES:
                continue
            yield doc

        cursor = data.get("nextPageCursor")
        if not cursor:
            break
        params["pageCursor"] = cursor
        time.sleep(0.3)  # be nice to the API


def process_article(doc: dict, session: requests.Session) -> Path:
    article_id = doc["id"]
    title = doc.get("title") or "untitled"
    slug = slugify(title)
    out_path = ARTICLES_DIR / f"{slug}.md"

    # avoid duplicate filenames
    if out_path.exists():
        out_path = ARTICLES_DIR / f"{slug}-{article_id[:6]}.md"

    print(f"  Processing: {title[:60]}")

    # Download cover image
    cover_local = None
    cover_url = doc.get("image_url")
    if cover_url:
        cover_dest = IMAGES_DIR / f"{article_id}_cover"
        cover_local = download_image(cover_url, cover_dest, session)

    # Process HTML content
    html = doc.get("html_content") or ""
    if html:
        html = process_html_images(html, article_id, session)
        body = html_to_markdown(html)
    else:
        body = f"> *No content available — read at source: {doc.get('source_url', '')}*\n"

    fm = build_frontmatter(doc, cover_local)
    out_path.write_text(fm + body, encoding="utf-8")
    return out_path


def main():
    token = load_token()
    session = requests.Session()
    session.headers["User-Agent"] = "llmwikirepo-fetcher/1.0"

    stratechery: list[dict] = []
    others: list[dict] = []

    print("Fetching articles from Readwise Reader...")
    for doc in fetch_documents(token, session):
        source_url = doc.get("source_url") or ""
        is_strat = STRATECHERY_DOMAIN in source_url

        if is_strat and len(stratechery) < TARGET_STRATECHERY:
            stratechery.append(doc)
        elif not is_strat and len(others) < TARGET_OTHER:
            others.append(doc)

        if len(stratechery) >= TARGET_STRATECHERY and len(others) >= TARGET_OTHER:
            print(f"  Both buckets full — stopping early.")
            break

    all_docs = stratechery + others
    print(f"\nCollected: {len(stratechery)} Stratechery + {len(others)} others = {len(all_docs)} total\n")

    written = []
    failed = []

    for i, doc in enumerate(all_docs, 1):
        label = "stratechery" if STRATECHERY_DOMAIN in (doc.get("source_url") or "") else "other"
        print(f"[{i}/{len(all_docs)}] ({label})")
        try:
            path = process_article(doc, session)
            written.append(path)
            print(f"  → {path.relative_to(REPO_ROOT)}")
        except Exception as e:
            print(f"  ✗ Failed: {e}")
            failed.append(doc.get("title", "?"))

    print(f"\n✓ Done: {len(written)} articles written, {len(failed)} failed")
    if failed:
        print("  Failed:", failed)
    print(f"  Articles: {ARTICLES_DIR.relative_to(REPO_ROOT)}/")
    print(f"  Images:   {IMAGES_DIR.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()
