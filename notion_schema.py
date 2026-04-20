#!/usr/bin/env python3
"""Create or update the Notion schema for the LLM Wiki.

This script uses the existing Readwise export database as the Raw Sources
database, then creates a control page inside it and child databases for:

- Wiki Pages
- Claims / Evidence
- Ops Log

Credentials are loaded from environment variables or ignored local env files.
No secrets are printed.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


NOTION_VERSION = "2022-06-28"
DEFAULT_RAW_DATABASE_TITLE = "Export via Reader"
CONTROL_PAGE_TITLE = "LLM Wiki Control Center"
WIKI_DB_TITLE = "LLM Wiki - Wiki Pages"
CLAIMS_DB_TITLE = "LLM Wiki - Claims / Evidence"
OPS_DB_TITLE = "LLM Wiki - Ops Log"


def load_local_env() -> dict[str, str]:
    env: dict[str, str] = {}
    for path in [Path(".env"), Path("reader/.env")]:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip("\"'")
    return env


def env_value(key: str, local_env: dict[str, str], *fallbacks: str) -> str:
    for name in (key, *fallbacks):
        value = os.environ.get(name) or local_env.get(name)
        if value:
            return value.strip()
    return ""


@dataclass
class Notion:
    token: str
    dry_run: bool = False

    def request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        if self.dry_run and method in {"POST", "PATCH"}:
            print(f"DRY-RUN {method} {path}")
            return {}

        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(
            f"https://api.notion.com/v1/{path}",
            data=data,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Notion-Version": NOTION_VERSION,
                "Content-Type": "application/json",
            },
            method=method,
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Notion API {method} {path} failed: {exc.code} {body}") from exc


def title_text(parts: list[dict[str, Any]]) -> str:
    return "".join(part.get("plain_text", "") for part in parts)


def title_property(text: str) -> dict[str, Any]:
    return {"title": [{"type": "text", "text": {"content": text}}]}


def rich_text_property(text: str) -> dict[str, Any]:
    return {"rich_text": [{"type": "text", "text": {"content": text}}]}


def find_database_by_title(notion: Notion, title: str) -> dict[str, Any] | None:
    payload = {
        "query": title,
        "filter": {"property": "object", "value": "database"},
        "page_size": 20,
    }
    data = notion.request("POST", "search", payload)
    for result in data.get("results", []):
        if title_text(result.get("title", [])) == title:
            return result
    return None


def find_page_in_database(notion: Notion, database_id: str, title: str) -> dict[str, Any] | None:
    payload = {
        "filter": {"property": "Name", "title": {"equals": title}},
        "page_size": 1,
    }
    data = notion.request("POST", f"databases/{database_id}/query", payload)
    results = data.get("results", [])
    return results[0] if results else None


def ensure_control_page(notion: Notion, raw_database_id: str) -> str:
    existing = find_page_in_database(notion, raw_database_id, CONTROL_PAGE_TITLE)
    if existing:
        print(f"reuse page: {CONTROL_PAGE_TITLE}")
        return existing["id"]

    payload = {
        "parent": {"database_id": raw_database_id},
        "properties": {
            "Name": title_property(CONTROL_PAGE_TITLE),
            "Category": {"select": {"name": "system"}},
            "Summary": rich_text_property("Control page for LLM Wiki schema databases."),
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Child databases below define the LLM Wiki schema."
                            },
                        }
                    ]
                },
            }
        ],
    }
    data = notion.request("POST", "pages", payload)
    print(f"create page: {CONTROL_PAGE_TITLE}")
    return data["id"]


def raw_source_properties() -> dict[str, Any]:
    return {
        "Reader ID": {"rich_text": {}},
        "Source Type": {
            "select": {
                "options": [
                    {"name": "article", "color": "blue"},
                    {"name": "rss", "color": "green"},
                    {"name": "paper", "color": "purple"},
                    {"name": "note", "color": "gray"},
                    {"name": "transcript", "color": "orange"},
                    {"name": "system", "color": "red"},
                ]
            }
        },
        "Status": {
            "select": {
                "options": [
                    {"name": "queued", "color": "yellow"},
                    {"name": "captured", "color": "blue"},
                    {"name": "processed", "color": "green"},
                    {"name": "needs review", "color": "orange"},
                    {"name": "archived", "color": "gray"},
                ]
            }
        },
        "Local Markdown Path": {"rich_text": {}},
        "Local Asset Paths": {"rich_text": {}},
        "Content Hash": {"rich_text": {}},
        "Last Synced At": {"date": {}},
        "Sync Run ID": {"rich_text": {}},
        "Processing Notes": {"rich_text": {}},
    }


def relation_property(database_id: str) -> dict[str, Any]:
    return {
        "relation": {
            "database_id": database_id,
            "type": "single_property",
            "single_property": {},
        }
    }


def wiki_database_properties(raw_database_id: str) -> dict[str, Any]:
    return {
        "Name": {"title": {}},
        "Page Type": {
            "select": {
                "options": [
                    {"name": "source summary", "color": "blue"},
                    {"name": "topic", "color": "green"},
                    {"name": "entity", "color": "purple"},
                    {"name": "concept", "color": "orange"},
                    {"name": "synthesis", "color": "red"},
                    {"name": "comparison", "color": "yellow"},
                    {"name": "question", "color": "gray"},
                ]
            }
        },
        "Slug": {"rich_text": {}},
        "Summary": {"rich_text": {}},
        "Lifecycle": {
            "select": {
                "options": [
                    {"name": "draft", "color": "yellow"},
                    {"name": "reviewed", "color": "blue"},
                    {"name": "verified", "color": "green"},
                    {"name": "stale", "color": "red"},
                ]
            }
        },
        "Confidence": {
            "select": {
                "options": [
                    {"name": "low", "color": "red"},
                    {"name": "medium", "color": "yellow"},
                    {"name": "high", "color": "green"},
                ]
            }
        },
        "Related Raw Sources": relation_property(raw_database_id),
        "Local Path": {"rich_text": {}},
        "GitHub URL": {"url": {}},
        "Last Updated": {"date": {}},
        "Tags": {"multi_select": {}},
    }


def claims_database_properties(raw_database_id: str, wiki_database_id: str) -> dict[str, Any]:
    return {
        "Claim": {"title": {}},
        "Evidence Quote": {"rich_text": {}},
        "Confidence": {
            "select": {
                "options": [
                    {"name": "low", "color": "red"},
                    {"name": "medium", "color": "yellow"},
                    {"name": "high", "color": "green"},
                ]
            }
        },
        "Raw Source": relation_property(raw_database_id),
        "Wiki Page": relation_property(wiki_database_id),
        "Entity / Concept": {"rich_text": {}},
        "Image Reference": {"rich_text": {}},
        "Source URL": {"url": {}},
        "Date Observed": {"date": {}},
    }


def ops_database_properties(raw_database_id: str, wiki_database_id: str) -> dict[str, Any]:
    return {
        "Name": {"title": {}},
        "Timestamp": {"date": {}},
        "Operation": {
            "select": {
                "options": [
                    {"name": "capture", "color": "blue"},
                    {"name": "schema", "color": "purple"},
                    {"name": "ingest", "color": "green"},
                    {"name": "compile", "color": "orange"},
                    {"name": "publish", "color": "red"},
                    {"name": "query", "color": "yellow"},
                    {"name": "lint", "color": "gray"},
                ]
            }
        },
        "Status": {
            "select": {
                "options": [
                    {"name": "planned", "color": "gray"},
                    {"name": "running", "color": "yellow"},
                    {"name": "passed", "color": "green"},
                    {"name": "failed", "color": "red"},
                    {"name": "partial", "color": "orange"},
                ]
            }
        },
        "Run ID": {"rich_text": {}},
        "Summary": {"rich_text": {}},
        "Notes": {"rich_text": {}},
        "Touched Sources": relation_property(raw_database_id),
        "Touched Wiki Pages": relation_property(wiki_database_id),
        "Git Commit": {"rich_text": {}},
    }


def create_database(
    notion: Notion,
    parent_page_id: str,
    title: str,
    properties: dict[str, Any],
) -> str:
    existing = find_database_by_title(notion, title)
    if existing:
        print(f"reuse database: {title}")
        return existing["id"]

    payload = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": [{"type": "text", "text": {"content": title}}],
        "properties": properties,
    }
    data = notion.request("POST", "databases", payload)
    print(f"create database: {title}")
    return data["id"]


def update_database_properties(notion: Notion, database_id: str, properties: dict[str, Any], label: str) -> None:
    notion.request("PATCH", f"databases/{database_id}", {"properties": properties})
    print(f"update database properties: {label}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply changes to Notion.")
    parser.add_argument("--raw-database-title", default=DEFAULT_RAW_DATABASE_TITLE)
    parser.add_argument("--raw-database-id", default="")
    args = parser.parse_args()

    local_env = load_local_env()
    token = env_value("NOTION_TOKEN", local_env, "notion_api")
    if not token:
        print("Missing NOTION_TOKEN or reader/.env notion_api", file=sys.stderr)
        return 2

    notion = Notion(token=token, dry_run=not args.apply)

    raw_database_id = args.raw_database_id or env_value("NOTION_DATABASE_ID", local_env, "database_id")
    if not raw_database_id:
        raw_database = find_database_by_title(notion, args.raw_database_title)
        if not raw_database:
            print(f"Could not find raw database titled {args.raw_database_title!r}", file=sys.stderr)
            return 2
        raw_database_id = raw_database["id"]

    if not args.apply:
        print("Dry run only. Re-run with --apply to write to Notion.")

    control_page_id = ensure_control_page(notion, raw_database_id)
    update_database_properties(notion, raw_database_id, raw_source_properties(), "Raw Sources")

    wiki_database_id = create_database(
        notion,
        control_page_id,
        WIKI_DB_TITLE,
        wiki_database_properties(raw_database_id),
    )
    claims_database_id = create_database(
        notion,
        control_page_id,
        CLAIMS_DB_TITLE,
        claims_database_properties(raw_database_id, wiki_database_id),
    )
    ops_database_id = create_database(
        notion,
        control_page_id,
        OPS_DB_TITLE,
        ops_database_properties(raw_database_id, wiki_database_id),
    )

    update_database_properties(
        notion,
        raw_database_id,
        {"Related Wiki Pages": relation_property(wiki_database_id)},
        "Raw Sources relation",
    )

    print("Schema ready:")
    print(f"- Raw Sources: {raw_database_id}")
    print(f"- Control Page: {control_page_id}")
    print(f"- Wiki Pages: {wiki_database_id}")
    print(f"- Claims / Evidence: {claims_database_id}")
    print(f"- Ops Log: {ops_database_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
