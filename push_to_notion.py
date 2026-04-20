#!/usr/bin/env python3
"""Delete existing Notion pages + push articles from Readwise Reader API with proper formatting."""

import re
import time
import os
import sys
import requests
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
READWISE_TOKEN = os.environ.get("READWISE_TOKEN", "")
DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "")
ARTICLES_DIR = Path(__file__).parent / "sources" / "articles"

NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}
READER_HEADERS = {"Authorization": f"Token {READWISE_TOKEN}"}


def require_config():
    missing = [
        name for name, value in {
            "NOTION_TOKEN": NOTION_TOKEN,
            "READWISE_TOKEN": READWISE_TOKEN,
            "NOTION_DATABASE_ID": DATABASE_ID,
        }.items()
        if not value
    ]
    if missing:
        sys.exit(f"Missing required environment variables: {', '.join(missing)}")


# ── Rich text builder ──────────────────────────────────────────────────────────

def valid_url(href):
    """Return href only if Notion will accept it (absolute http/https)."""
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
    """Recursively extract rich_text objects from an inline HTML node."""
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
        # Apply href to all segments, or use link text if empty
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
    """Merge adjacent segments with identical annotations to reduce block count."""
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
    """Split rich_text list into chunks where total char count <= max_chars."""
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
    return {"object": "block", "type": "paragraph",
            "paragraph": {"rich_text": rt}}


def make_heading(rt, level):
    t = f"heading_{level}"
    return {"object": "block", "type": t, t: {"rich_text": rt}}


def make_quote(rt):
    return {"object": "block", "type": "quote",
            "quote": {"rich_text": rt}}


def make_bullet(rt):
    return {"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": rt}}


def make_numbered(rt):
    return {"object": "block", "type": "numbered_list_item",
            "numbered_list_item": {"rich_text": rt}}


def make_code(text, language="plain text"):
    return {"object": "block", "type": "code",
            "code": {"rich_text": [make_rich_text(text[:2000])], "language": language}}


def make_divider():
    return {"object": "block", "type": "divider", "divider": {}}


def make_plain_paragraph(text):
    return make_paragraph([make_rich_text(text[:2000])])


# ── HTML → Notion blocks ───────────────────────────────────────────────────────

BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
              "blockquote", "pre", "hr", "div", "section", "article",
              "header", "footer", "figure", "figcaption", "table", "tr", "td", "th"}


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
            # Recurse inside but wrap paragraphs as quote blocks
            inner_blocks = []
            for child in node.children:
                if isinstance(child, NavigableString):
                    t = str(child).strip()
                    if t:
                        inner_blocks.append(make_quote([make_rich_text(t)]))
                elif child.name in ("p", "div"):
                    rt = rt_from_node(child)
                    if rt:
                        for chunk in chunk_rich_text(rt):
                            inner_blocks.append(make_quote(chunk))
                else:
                    rt = rt_from_node(child)
                    if rt:
                        for chunk in chunk_rich_text(rt):
                            inner_blocks.append(make_quote(chunk))
            blocks.extend(inner_blocks)
            return

        if tag == "pre":
            code_node = node.find("code")
            text = (code_node or node).get_text()
            if text.strip():
                # split long code into multiple code blocks
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
                    # recurse deeper
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
                blocks.append({
                    "object": "block",
                    "type": "image",
                    "image": {"type": "external", "external": {"url": url}},
                })
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
            # flatten table rows to paragraphs
            text = node.get_text(separator=" | ", strip=True)
            if text:
                blocks.append(make_plain_paragraph(text[:2000]))
            return

        # Generic container — recurse
        for child in node.children:
            process(child)

    body = soup.find("body") or soup
    for child in body.children:
        process(child)

    # Filter empty blocks
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


def archive_page(page_id):
    r = requests.patch(f"https://api.notion.com/v1/pages/{page_id}",
                       headers=NOTION_HEADERS, json={"archived": True})
    return r.ok


def push_blocks(page_id, blocks):
    """Append blocks in batches of 100 with retry."""
    for i in range(0, len(blocks), 100):
        batch = blocks[i:i+100]
        for attempt in range(3):
            try:
                r = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children",
                                   headers=NOTION_HEADERS, json={"children": batch}, timeout=30)
                if r.ok:
                    break
                print(f"  WARN block append failed: {r.status_code} {r.text[:200]}")
                break
            except Exception as e:
                print(f"  WARN attempt {attempt+1} failed: {e}")
                time.sleep(2 ** attempt)
        time.sleep(0.3)


def iso_date(val):
    if not val:
        return None
    s = str(val)[:10]
    if len(s) == 10:
        return s
    return None


def create_notion_page(doc):
    title       = (doc.get("title") or "Untitled")[:2000]
    author      = doc.get("author") or ""
    source_url  = doc.get("source_url") or ""
    reader_url  = doc.get("url") or ""
    site        = doc.get("site_name") or ""
    category    = doc.get("category") or ""
    source      = doc.get("source") or ""
    location    = doc.get("location") or ""
    published   = iso_date(doc.get("published_date"))
    saved_at    = iso_date(doc.get("saved_at"))
    reading_time = str(doc.get("reading_time") or "")
    word_count  = doc.get("word_count")
    progress    = doc.get("reading_progress")
    summary     = doc.get("summary") or ""
    image_url   = doc.get("image_url") or ""
    notes       = doc.get("notes") or ""
    tags_raw    = doc.get("tags") or {}
    tags        = list(tags_raw.keys()) if isinstance(tags_raw, dict) else list(tags_raw)
    html_content = doc.get("html_content") or ""

    properties = {
        "Name": {"title": [{"type": "text", "text": {"content": title}}]},
    }
    if author:
        properties["Author"] = {"rich_text": [{"type": "text", "text": {"content": author[:2000]}}]}
    if site:
        properties["Site"] = {"select": {"name": site[:100]}}
    if category:
        properties["Category"] = {"select": {"name": category[:100]}}
    if source:
        properties["Source"] = {"rich_text": [{"type": "text", "text": {"content": source[:2000]}}]}
    if valid_url(source_url):
        properties["Source URL"] = {"url": valid_url(source_url)}
    if valid_url(reader_url):
        properties["Reader URL"] = {"url": valid_url(reader_url)}
    if published:
        properties["Published Date"] = {"date": {"start": published}}
    if saved_at:
        properties["Saved At"] = {"date": {"start": saved_at}}
    if reading_time:
        properties["Reading Time"] = {"rich_text": [{"type": "text", "text": {"content": reading_time}}]}
    if word_count is not None:
        properties["Word Count"] = {"number": word_count}
    if progress is not None:
        properties["Reading Progress"] = {"number": progress / 100 if progress > 1 else progress}
    if location:
        properties["Location"] = {"select": {"name": location[:100]}}
    if tags:
        properties["Tags"] = {"multi_select": [{"name": t[:100]} for t in tags]}
    if summary:
        properties["Summary"] = {"rich_text": [{"type": "text", "text": {"content": summary[:2000]}}]}
    if valid_url(image_url):
        properties["Cover Image URL"] = {"url": valid_url(image_url)}
    if notes:
        properties["Notes"] = {"rich_text": [{"type": "text", "text": {"content": notes[:2000]}}]}

    # Content blocks
    header_blocks = []
    if summary:
        header_blocks.append(make_quote([make_rich_text(summary)]))
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

    r = requests.post("https://api.notion.com/v1/pages", headers=NOTION_HEADERS, json=payload)
    if not r.ok:
        print(f"  ERROR {r.status_code}: {r.text[:400]}")
        return None

    page_id = r.json().get("id")

    # Append remaining
    remaining = all_blocks[100:]
    if remaining and page_id:
        push_blocks(page_id, remaining)

    return page_id


# ── Readwise ───────────────────────────────────────────────────────────────────

def get_article_ids_from_md():
    ids = []
    for f in sorted(ARTICLES_DIR.glob("*.md")):
        if f.name == "untitled.md":
            continue
        text = f.read_text(encoding="utf-8")
        m = re.search(r'image:.*?/(01\w+)_cover', text)
        if m:
            ids.append(m.group(1))
    return ids


def fetch_reader_doc(doc_id):
    r = requests.get(
        f"https://readwise.io/api/v3/list/?id={doc_id}&withHtmlContent=true",
        headers=READER_HEADERS, timeout=30,
    )
    r.raise_for_status()
    results = r.json().get("results", [])
    return results[0] if results else None


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    require_config()
    print("Step 1: Archiving existing Notion pages...")
    pages = get_all_db_pages()
    print(f"  {len(pages)} pages to archive.")
    for p in pages:
        ok = archive_page(p["id"])
        print(f"  {'✓' if ok else '✗'} {p['id']}")
        time.sleep(0.15)

    print(f"\nStep 2: Loading article IDs from MD files...")
    ids = get_article_ids_from_md()
    print(f"  {len(ids)} articles.\n")

    print("Step 3: Fetch from Reader + push to Notion with rich formatting...")
    success = 0
    for i, doc_id in enumerate(ids, 1):
        doc = fetch_reader_doc(doc_id)
        if not doc:
            print(f"[{i}/{len(ids)}] SKIP {doc_id}")
            continue

        title = (doc.get("title") or "?")[:60]
        html = doc.get("html_content") or ""
        print(f"[{i}/{len(ids)}] {title} (html={len(html)} chars)")

        try:
            page_id = create_notion_page(doc)
        except Exception as e:
            print(f"  ✗ exception: {e}")
            page_id = None
        if page_id:
            print(f"  ✓ {page_id}")
            success += 1
        else:
            print(f"  ✗ failed")
        time.sleep(0.4)

    print(f"\nDone: {success}/{len(ids)} pushed.")


if __name__ == "__main__":
    main()
