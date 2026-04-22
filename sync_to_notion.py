#!/usr/bin/env python3
"""Incremental sync: fetch Reader docs and push new ones to Notion. Logs each run."""

import argparse
import re
import sys
import time
import logging
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString

import requests

ENV_FILE = Path(__file__).parent / "reader" / ".env"
DEFAULT_RAW_DATABASE_TITLE = "Export via Reader"
NOTION_VERSION = "2022-06-28"
REQUEST_TIMEOUT = 30
LOG_DIR = Path(__file__).parent / "logs"

READER_CATEGORIES = {"article", "rss", "tweet", "email", "video", "pdf", "epub"}


def load_local_env(path):
    if not path.exists():
        return {}
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def env_value(name, local_env, fallback_name=None):
    return (
        os.environ.get(name)
        or local_env.get(name)
        or (local_env.get(fallback_name) if fallback_name else "")
        or ""
    ).strip()


def load_runtime_config():
    local_env = load_local_env(ENV_FILE)
    return {
        "notion_token": env_value("NOTION_TOKEN", local_env, "notion_api"),
        "readwise_token": env_value("READWISE_TOKEN", local_env, "readwise_token"),
        "database_id": env_value("NOTION_DATABASE_ID", local_env, "database_id"),
        "database_title": env_value("NOTION_DATABASE_TITLE", local_env, "notion_database_title")
        or DEFAULT_RAW_DATABASE_TITLE,
    }


RUNTIME_CONFIG = load_runtime_config()
NOTION_TOKEN = RUNTIME_CONFIG["notion_token"]
READWISE_TOKEN = RUNTIME_CONFIG["readwise_token"]
DATABASE_ID = RUNTIME_CONFIG["database_id"]
DATABASE_TITLE = RUNTIME_CONFIG["database_title"]

NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": NOTION_VERSION,
}
READER_HEADERS = {"Authorization": f"Token {READWISE_TOKEN}"}


def require_config():
    missing = [
        name for name, value in {
            "NOTION_TOKEN": NOTION_TOKEN,
            "READWISE_TOKEN": READWISE_TOKEN,
        }.items()
        if not value
    ]
    if missing:
        sys.exit(f"Missing required environment variables: {', '.join(missing)}")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Plan Notion creates without writing any pages.",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        help="Limit how many new Reader docs are pushed in this run.",
    )
    args = parser.parse_args()
    if args.max_items is not None and args.max_items <= 0:
        parser.error("--max-items must be a positive integer")
    return args


# ── Logging setup ──────────────────────────────────────────────────────────────

def setup_logging():
    LOG_DIR.mkdir(exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    log_file = LOG_DIR / f"sync_{ts}.log"

    fmt = "%(asctime)s  %(levelname)-7s %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        datefmt=datefmt,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout),
        ],
    )
    logging.info(f"Log file: {log_file}")
    return log_file


# ── Rich text builder ──────────────────────────────────────────────────────────

def valid_url(href):
    if not href:
        return None
    href = href.strip()
    if href.startswith(("http://", "https://")):
        return href[:2000]
    return None


def make_rich_text(text, href=None, bold=False, italic=False, code=False):
    obj = {
        "type": "text",
        "text": {"content": text[:2000]},
        "annotations": {
            "bold": bold,
            "italic": italic,
            "code": code,
            "strikethrough": False,
            "underline": False,
            "color": "default",
        },
    }
    url = valid_url(href)
    if url:
        obj["text"]["link"] = {"url": url}
    return obj


def parse_inline(node, bold=False, italic=False, code=False):
    results = []
    if isinstance(node, NavigableString):
        text = str(node)
        if text:
            results.append(make_rich_text(text, bold=bold, italic=italic, code=code))
        return results

    tag = node.name.lower() if node.name else ""
    if tag in ("script", "style", "noscript"):
        return []
    if tag == "br":
        results.append(make_rich_text("\n", bold=bold, italic=italic))
        return results

    new_bold = bold or tag in ("b", "strong")
    new_italic = italic or tag in ("i", "em")
    new_code = code or tag in ("code",)

    if tag == "a":
        href = node.get("href") or ""
        inner = []
        for child in node.children:
            inner.extend(parse_inline(child, bold=new_bold, italic=new_italic, code=new_code))
        if not inner:
            link_text = node.get_text(strip=True) or href
            inner = [make_rich_text(link_text, href=href, bold=new_bold, italic=new_italic)]
        else:
            url = valid_url(href)
            for seg in inner:
                if url:
                    seg["text"]["link"] = {"url": url}
        results.extend(inner)
        return results

    for child in node.children:
        results.extend(parse_inline(child, bold=new_bold, italic=new_italic, code=new_code))
    return results


def merge_rich_text(segments):
    merged = []
    for seg in segments:
        if (merged and
                merged[-1]["annotations"] == seg["annotations"] and
                merged[-1]["text"].get("link") == seg["text"].get("link") and
                len(merged[-1]["text"]["content"]) + len(seg["text"]["content"]) <= 2000):
            merged[-1]["text"]["content"] += seg["text"]["content"]
        else:
            merged.append(seg)
    return merged


def rt_from_node(node):
    return merge_rich_text(parse_inline(node))


def chunk_rich_text(rt_list, max_chars=2000):
    chunks = []
    current = []
    total = 0
    for seg in rt_list:
        seg_len = len(seg["text"]["content"])
        if total + seg_len > max_chars and current:
            chunks.append(current)
            current = []
            total = 0
        current.append(seg)
        total += seg_len
    if current:
        chunks.append(current)
    return chunks or [[]]


# ── Block builders ─────────────────────────────────────────────────────────────

def make_paragraph(rt):
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": rt}}

def make_heading(rt, level):
    t = f"heading_{level}"
    return {"object": "block", "type": t, t: {"rich_text": rt}}

def make_quote(rt):
    return {"object": "block", "type": "quote", "quote": {"rich_text": rt}}

def make_bullet(rt):
    return {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": rt}}

def make_numbered(rt):
    return {"object": "block", "type": "numbered_list_item", "numbered_list_item": {"rich_text": rt}}

def make_code(text, language="plain text"):
    return {"object": "block", "type": "code",
            "code": {"rich_text": [make_rich_text(text[:2000])], "language": language}}

def make_divider():
    return {"object": "block", "type": "divider", "divider": {}}

def make_plain_paragraph(text):
    return make_paragraph([make_rich_text(text[:2000])])


def clean_select_name(value):
    """Notion select/multi_select option names cannot contain commas."""
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).replace(",", " -")[:100].strip()


def source_type_for(doc):
    return str(doc.get("source_type") or doc.get("source") or "")


def rich_text_property(text, limit=1900):
    return {"rich_text": [make_rich_text(str(text)[:limit])]}


def plain_rich_text(prop):
    segments = prop.get("rich_text") or []
    values = []
    for seg in segments:
        plain = seg.get("plain_text")
        if plain is None:
            plain = seg.get("text", {}).get("content", "")
        values.append(plain)
    return "".join(values).strip()


def reader_id_from_page(page):
    props = page.get("properties", {})
    reader_id = plain_rich_text(props.get("Reader ID", {}))
    if reader_id:
        return reader_id

    reader_url_prop = props.get("Reader URL", {})
    url = reader_url_prop.get("url") or ""
    if not url:
        return None

    match = re.search(r"/(01\w+)/?$", url)
    return match.group(1) if match else None


def build_page_properties(doc, synced_at=None, run_id=None):
    title = (doc.get("title") or "Untitled")[:2000]
    author = doc.get("author") or ""
    source_url = doc.get("source_url") or ""
    reader_url = doc.get("url") or ""
    site = doc.get("site_name") or ""
    category = doc.get("category") or ""
    source = doc.get("source") or ""
    source_type = source_type_for(doc)
    reader_id = str(doc.get("id") or "")
    location = doc.get("location") or ""
    published = iso_date(doc.get("published_date"))
    saved_at = iso_date(doc.get("saved_at"))
    reading_time = str(doc.get("reading_time") or "")
    word_count = doc.get("word_count")
    progress = doc.get("reading_progress")
    summary = doc.get("summary") or ""
    image_url = doc.get("image_url") or ""
    notes = doc.get("notes") or ""
    tags_raw = doc.get("tags") or {}
    tags = list(tags_raw.keys()) if isinstance(tags_raw, dict) else list(tags_raw)

    properties = {
        "Name": {"title": [{"type": "text", "text": {"content": title}}]},
        "Status": {"select": {"name": "captured"}},
    }
    if reader_id:
        properties["Reader ID"] = rich_text_property(reader_id)
    if source_type:
        properties["Source Type"] = {"select": {"name": clean_select_name(source_type)}}
    if author:
        properties["Author"] = rich_text_property(author)
    if site:
        properties["Site"] = {"select": {"name": clean_select_name(site)}}
    if category:
        properties["Category"] = {"select": {"name": clean_select_name(category)}}
    if source:
        properties["Source"] = rich_text_property(source)
    if valid_url(source_url):
        properties["Source URL"] = {"url": valid_url(source_url)}
    if valid_url(reader_url):
        properties["Reader URL"] = {"url": valid_url(reader_url)}
    if published:
        properties["Published Date"] = {"date": {"start": published}}
    if saved_at:
        properties["Saved At"] = {"date": {"start": saved_at}}
    if reading_time:
        properties["Reading Time"] = rich_text_property(reading_time)
    if word_count is not None:
        properties["Word Count"] = {"number": word_count}
    if progress is not None:
        properties["Reading Progress"] = {"number": progress / 100 if progress > 1 else progress}
    if location:
        properties["Location"] = {"select": {"name": clean_select_name(location)}}
    if tags:
        properties["Tags"] = {
            "multi_select": [{"name": clean_select_name(t)} for t in tags if clean_select_name(t)]
        }
    if summary:
        properties["Summary"] = rich_text_property(summary)
    if valid_url(image_url):
        properties["Cover Image URL"] = {"url": valid_url(image_url)}
    if notes:
        properties["Notes"] = rich_text_property(notes)
    if synced_at:
        properties["Last Synced At"] = {"date": {"start": synced_at}}
    if run_id:
        properties["Sync Run ID"] = rich_text_property(run_id)

    return properties


def is_sync_candidate(doc):
    return doc.get("parent_id") is None and doc.get("category") in READER_CATEGORIES


def plan_sync_docs(existing_ids, docs, max_items=None):
    planned = [doc for doc in docs if str(doc.get("id") or "") not in existing_ids]
    if max_items is not None:
        planned = planned[:max_items]
    return planned


# ── HTML → Notion blocks ───────────────────────────────────────────────────────

def html_to_notion_blocks(html):
    soup = BeautifulSoup(html, "html.parser")
    blocks = []

    def process(node):
        if isinstance(node, NavigableString):
            text = str(node).strip()
            if text:
                blocks.append(make_plain_paragraph(text))
            return

        tag = (node.name or "").lower()
        if tag in ("script", "style", "noscript", "meta", "head"):
            return
        if tag == "hr":
            blocks.append(make_divider())
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = min(int(tag[1]), 3)
            rt = rt_from_node(node)
            if rt:
                for chunk in chunk_rich_text(rt):
                    blocks.append(make_heading(chunk, level))
            return
        if tag == "blockquote":
            for child in node.children:
                if isinstance(child, NavigableString):
                    t = str(child).strip()
                    if t:
                        blocks.append(make_quote([make_rich_text(t)]))
                else:
                    rt = rt_from_node(child)
                    if rt:
                        for chunk in chunk_rich_text(rt):
                            blocks.append(make_quote(chunk))
            return
        if tag == "pre":
            code_node = node.find("code")
            text = (code_node or node).get_text()
            if text.strip():
                lines = text.split("\n")
                chunk = []
                for line in lines:
                    chunk.append(line)
                    if len("\n".join(chunk)) > 1900:
                        blocks.append(make_code("\n".join(chunk[:-1])))
                        chunk = [line]
                if chunk:
                    blocks.append(make_code("\n".join(chunk)))
            return
        if tag in ("ul", "ol"):
            maker = make_bullet if tag == "ul" else make_numbered
            for li in node.find_all("li", recursive=False):
                rt = rt_from_node(li)
                if rt:
                    for chunk in chunk_rich_text(rt):
                        blocks.append(maker(chunk))
                else:
                    for child in li.children:
                        process(child)
            return
        if tag == "p":
            rt = rt_from_node(node)
            if rt:
                for chunk in chunk_rich_text(rt):
                    blocks.append(make_paragraph(chunk))
            return
        if tag == "img":
            src = node.get("src", "").strip()
            alt = node.get("alt", "")
            url = valid_url(src)
            if url:
                blocks.append({"object": "block", "type": "image",
                                "image": {"type": "external", "external": {"url": url}}})
            elif alt:
                blocks.append(make_plain_paragraph(f"[Image: {alt}]"))
            return
        if tag == "figure":
            img = node.find("img")
            caption = node.find("figcaption")
            if img:
                process(img)
            if caption:
                rt = rt_from_node(caption)
                if rt:
                    blocks.append(make_quote(rt))
            return
        if tag in ("table", "tr", "td", "th"):
            text = node.get_text(separator=" | ", strip=True)
            if text:
                blocks.append(make_plain_paragraph(text[:2000]))
            return
        for child in node.children:
            process(child)

    body = soup.find("body") or soup
    for child in body.children:
        process(child)
    return [b for b in blocks if b]


# ── Notion API ────────────────────────────────────────────────────────────────

def get_all_db_pages():
    pages = []
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {"page_size": 100}
    while True:
        r = requests.post(url, headers=NOTION_HEADERS, json=payload)
        r.raise_for_status()
        data = r.json()
        pages.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        payload["start_cursor"] = data["next_cursor"]
    return pages


def notion_title_text(parts):
    return "".join(part.get("plain_text", "") for part in parts)


def find_notion_database_id(title):
    if not title:
        return ""
    payload = {
        "query": title,
        "filter": {"property": "object", "value": "database"},
        "page_size": 20,
    }
    response = requests.post(
        "https://api.notion.com/v1/search",
        headers=NOTION_HEADERS,
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    for result in response.json().get("results", []):
        if notion_title_text(result.get("title", [])) == title:
            return result.get("id", "")
    return ""


def get_existing_doc_ids():
    """Return set of Reader doc IDs already in Notion."""
    pages = get_all_db_pages()
    doc_ids = set()
    for page in pages:
        reader_id = reader_id_from_page(page)
        if reader_id:
            doc_ids.add(reader_id)
    return doc_ids


def push_blocks(page_id, blocks):
    for i in range(0, len(blocks), 100):
        batch = blocks[i:i+100]
        for attempt in range(3):
            try:
                r = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children",
                                   headers=NOTION_HEADERS, json={"children": batch}, timeout=30)
                if r.ok:
                    break
                logging.warning(f"Block append failed: {r.status_code} {r.text[:200]}")
                break
            except Exception as e:
                logging.warning(f"Attempt {attempt+1} failed: {e}")
                time.sleep(2 ** attempt)
        time.sleep(0.3)


def post_notion_json_with_retry(url, payload, attempts=3):
    retry_statuses = {429, 500, 502, 503, 504}
    last_response = None
    for attempt in range(1, attempts + 1):
        try:
            response = requests.post(url, headers=NOTION_HEADERS, json=payload, timeout=30)
        except requests.RequestException as exc:
            if attempt == attempts:
                raise
            logging.warning(f"POST attempt {attempt} failed: {exc}")
            time.sleep(2 ** (attempt - 1))
            continue

        if response.status_code not in retry_statuses:
            return response

        last_response = response
        if attempt == attempts:
            return response

        retry_after = response.headers.get("Retry-After")
        delay = int(retry_after) if retry_after and retry_after.isdigit() else 2 ** (attempt - 1)
        logging.warning(f"POST attempt {attempt} returned {response.status_code}; retrying in {delay}s")
        time.sleep(delay)

    return last_response


def iso_date(val):
    if not val:
        return None
    s = str(val)[:10]
    return s if len(s) == 10 else None


def create_notion_page(doc, synced_at=None, run_id=None):
    summary = doc.get("summary") or ""
    html_content = doc.get("html_content") or ""
    properties = build_page_properties(doc, synced_at=synced_at, run_id=run_id)

    header_blocks = []
    if summary:
        header_blocks.append(make_quote(rich_text_property(summary)["rich_text"]))
    header_blocks.append(make_divider())

    if html_content:
        content_blocks = html_to_notion_blocks(html_content)
    else:
        content_blocks = [make_plain_paragraph("No content available — read at source.")]

    all_blocks = header_blocks + content_blocks

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": properties,
        "children": all_blocks[:100],
    }

    r = post_notion_json_with_retry("https://api.notion.com/v1/pages", payload)
    if (not r.ok) and (r.status_code == 403 or "Cloudflare" in r.text[:1000]):
        logging.warning("Create page rejected with full content; retrying metadata-only fallback")
        fallback_blocks = header_blocks + [
            make_plain_paragraph("Full article body omitted because Notion rejected the original HTML payload. Use Source URL or Reader URL for the full source.")
        ]
        fallback_payload = {
            "parent": {"database_id": DATABASE_ID},
            "properties": properties,
            "children": fallback_blocks[:100],
        }
        r = post_notion_json_with_retry("https://api.notion.com/v1/pages", fallback_payload)
    if not r.ok:
        logging.error(f"Create page failed {r.status_code}: {r.text[:400]}")
        return None

    page_id = r.json().get("id")
    remaining = all_blocks[100:]
    if remaining and page_id:
        push_blocks(page_id, remaining)

    return page_id


# ── Readwise ───────────────────────────────────────────────────────────────────

def fetch_all_reader_docs():
    """Yield all supported top-level Reader docs from the paginated API."""
    params = {"withHtmlContent": "true"}
    cursor = None
    page = 0
    while True:
        if cursor:
            params["pageCursor"] = cursor
        r = requests.get("https://readwise.io/api/v3/list/",
                         headers=READER_HEADERS, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        page += 1
        results = data.get("results", [])
        logging.info(f"  Reader page {page}: {len(results)} docs")
        for doc in results:
            if is_sync_candidate(doc):
                yield doc
        cursor = data.get("nextPageCursor")
        if not cursor:
            break
        time.sleep(0.3)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    args = parse_args()
    require_config()
    log_file = setup_logging()
    start = time.time()
    run_id = datetime.now(timezone.utc).strftime("sync-%Y%m%dT%H%M%SZ")
    synced_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    logging.info("=== Notion sync started ===")

    global DATABASE_ID
    if not DATABASE_ID:
        logging.info("Resolving Notion Raw Sources database by title...")
        DATABASE_ID = find_notion_database_id(DATABASE_TITLE)
        if not DATABASE_ID:
            sys.exit(
                "Missing NOTION_DATABASE_ID/database_id and could not resolve "
                f"{DATABASE_TITLE!r} via Notion search"
            )
        logging.info(f"  Resolved database: {DATABASE_TITLE} ({DATABASE_ID})")

    logging.info("Fetching existing doc IDs from Notion...")
    existing_ids = get_existing_doc_ids()
    logging.info(f"  {len(existing_ids)} articles already in Notion.")

    logging.info("Fetching all docs from Reader API...")
    new_docs = plan_sync_docs(existing_ids, fetch_all_reader_docs(), max_items=args.max_items)
    logging.info(f"  {len(new_docs)} new articles to push.")
    if new_docs:
        breakdown = Counter(str(doc.get("category") or "unknown") for doc in new_docs)
        logging.info(
            "  New doc breakdown: %s",
            ", ".join(f"{category}={count}" for category, count in sorted(breakdown.items())),
        )

    if args.dry_run:
        for idx, doc in enumerate(new_docs[:10], 1):
            title = (doc.get("title") or "?")[:60]
            logging.info(
                "[plan %s/%s] %r (id=%s, category=%s, source_type=%s)",
                idx,
                len(new_docs),
                title,
                doc.get("id"),
                doc.get("category") or "",
                source_type_for(doc),
            )
        logging.info("DRY RUN: no Notion writes performed.")
        logging.info(f"=== Done in {time.time()-start:.1f}s ===")
        return

    if not new_docs:
        logging.info("Nothing to do. Exiting.")
        logging.info(f"=== Done in {time.time()-start:.1f}s ===")
        return

    success = 0
    failed = 0
    for idx, doc in enumerate(new_docs, 1):
        title = (doc.get("title") or "?")[:60]
        html = doc.get("html_content") or ""
        logging.info(f"[{idx}/{len(new_docs)}] {title!r} (id={doc['id']}, html={len(html)} chars)")

        try:
            page_id = create_notion_page(doc, synced_at=synced_at, run_id=run_id)
        except Exception as e:
            logging.error(f"  Exception: {e}")
            page_id = None

        if page_id:
            logging.info(f"  -> pushed {page_id}")
            success += 1
        else:
            logging.error(f"  -> failed")
            failed += 1

        time.sleep(0.4)

    elapsed = time.time() - start
    logging.info(f"=== Done: {success} pushed, {failed} failed, {len(existing_ids)} skipped (already present). {elapsed:.1f}s ===")


if __name__ == "__main__":
    main()
