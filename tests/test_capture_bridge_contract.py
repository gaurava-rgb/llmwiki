import contextlib
import io
import os
import tempfile
import unittest
from unittest import mock
from pathlib import Path

from reader import capture_reader_to_markdown as capture


class CaptureBridgeContractTests(unittest.TestCase):
    class FakeResponse:
        def __init__(self, payload):
            self._payload = payload
            self.status_code = 200
            self.headers = {}

        def json(self):
            return self._payload

        def raise_for_status(self):
            return None

    def test_env_value_supports_local_aliases(self):
        local_env = {"readwise_token": "reader-token", "database_id": "raw-db"}

        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(capture.env_value("READWISE_TOKEN", local_env, "readwise_token"), "reader-token")
            self.assertEqual(capture.env_value("NOTION_DATABASE_ID", local_env, "database_id"), "raw-db")

    def test_sanitize_url_strips_private_access_token(self):
        url = "https://stratechery.com/2026/example/?access_token=secret&utm_source=x#frag"

        self.assertEqual(capture.sanitize_url(url), "https://stratechery.com/2026/example/")

    def test_sanitize_url_collapses_private_member_urls(self):
        url = "https://stratechery.passport.online/member/login?email=gaurav_a%40tamu.edu"

        self.assertEqual(capture.sanitize_url(url), "https://stratechery.passport.online/")

    def test_sanitize_text_urls_removes_private_markers(self):
        text = (
            "Read https://example.com/a?access_token=secret and "
            "https://stratechery.passport.online/member/podcast?url=secret"
        )

        sanitized = capture.sanitize_text_urls(text)

        self.assertNotIn("access_token=", sanitized)
        self.assertNotIn("passport.online/member", sanitized)

    def test_sanitize_private_text_removes_member_footer(self):
        text = "body\nMember: Gaurav Arora  \nEmail: gaurav_a@tamu.edu  \n"

        sanitized = capture.sanitize_private_text(text)

        self.assertNotIn("Gaurav Arora", sanitized)
        self.assertNotIn("gaurav_a@tamu.edu", sanitized)

    def test_sanitize_url_handles_malformed_url_without_private_query(self):
        url = "https://[broken.example/path?access_token=secret"

        self.assertEqual(capture.sanitize_url(url), "https://[broken.example/path")

    def test_content_hash_is_stable(self):
        first = capture.content_hash_for("title: example\n", "body\n")
        second = capture.content_hash_for("title: example\n", "body\n")

        self.assertEqual(first, second)

    def test_normalize_markdown_removes_trailing_whitespace(self):
        self.assertEqual(capture.normalize_markdown("line  \r\n\nnext \n"), "line\n\nnext\n")

    def test_reader_id_from_url(self):
        self.assertEqual(
            capture.reader_id_from_url("https://read.readwise.io/read/01abc123"),
            "01abc123",
        )

    def test_manifest_round_trip_uses_reader_id_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "manifest.jsonl"
            records = {
                "01abc": {
                    "reader_id": "01abc",
                    "category": "tweet",
                    "source_type": "Reader Share Sheet iOS",
                    "path": "sources/articles/example.md",
                    "content_hash": "hash",
                }
            }

            capture.write_manifest(records, path)

            self.assertEqual(capture.load_manifest(path), records)

    def test_dry_run_capture_does_not_write_files(self):
        doc = {
            "id": "01abc",
            "url": "https://read.readwise.io/read/01abc",
            "title": "Example Article",
            "source_url": "https://stratechery.com/2026/example/?access_token=secret",
            "html_content": "",
            "category": "article",
            "saved_at": "2026-04-20T00:00:00+00:00",
        }
        with tempfile.TemporaryDirectory() as tmp:
            articles_dir = Path(tmp) / "articles"
            manifest_path = articles_dir / "manifest.jsonl"

            with contextlib.redirect_stdout(io.StringIO()):
                stats = capture.capture_docs(
                    [doc],
                    notion_page_map={"01abc": "notion-page"},
                    apply=False,
                    download_images=False,
                    articles_dir=articles_dir,
                    manifest_path=manifest_path,
                )

            self.assertEqual(stats["planned"], 1)
            self.assertFalse((articles_dir / "example-article.md").exists())
            self.assertFalse(manifest_path.exists())

    def test_fetch_reader_docs_includes_supported_top_level_categories(self):
        payloads = [
            {
                "results": [
                    {"id": "01a", "category": "article", "parent_id": None},
                    {"id": "01b", "category": "tweet", "parent_id": None},
                    {"id": "01c", "category": "highlight", "parent_id": None},
                    {"id": "01d", "category": "pdf", "parent_id": "child"},
                ],
                "nextPageCursor": "next",
            },
            {
                "results": [
                    {"id": "01e", "category": "email", "parent_id": None},
                    {"id": "01f", "category": "video", "parent_id": None},
                    {"id": "01g", "category": "epub", "parent_id": None},
                    {"id": "01h", "category": "rss", "parent_id": None},
                    {"id": "01i", "category": "note", "parent_id": None},
                ],
                "nextPageCursor": None,
            },
        ]

        with mock.patch.object(capture, "request_with_retry", side_effect=[self.FakeResponse(p) for p in payloads]):
            docs = capture.fetch_reader_docs("reader-token", session=object())

        self.assertEqual(
            [doc["id"] for doc in docs],
            ["01a", "01b", "01e", "01f", "01g", "01h"],
        )

    def test_build_article_frontmatter_includes_category_and_source_type(self):
        doc = {
            "id": "01abc",
            "url": "https://read.readwise.io/read/01abc",
            "title": "Thread Example",
            "source_url": "https://x.com/example/status/123?rw_tt_thread=True",
            "category": "tweet",
            "source": "Reader Share Sheet iOS",
            "saved_at": "2026-04-20T00:00:00+00:00",
        }

        article, _, _ = capture.build_article(
            doc,
            notion_page_id="notion-page",
            session=object(),
            apply=False,
            download_images=False,
        )

        self.assertIn('category: "tweet"', article)
        self.assertIn('source_type: "Reader Share Sheet iOS"', article)

    def test_capture_docs_manifest_preserves_category_and_source_type(self):
        doc = {
            "id": "01abc",
            "url": "https://read.readwise.io/read/01abc",
            "title": "Video Example",
            "source_url": "https://youtube.com/watch?v=abc123&si=tracking",
            "category": "video",
            "source": "Reader Share Sheet iOS",
            "saved_at": "2026-04-20T00:00:00+00:00",
        }
        with tempfile.TemporaryDirectory() as tmp:
            articles_dir = Path(tmp) / "articles"
            manifest_path = articles_dir / "manifest.jsonl"

            with contextlib.redirect_stdout(io.StringIO()):
                stats = capture.capture_docs(
                    [doc],
                    notion_page_map={"01abc": "notion-page"},
                    apply=True,
                    download_images=False,
                    articles_dir=articles_dir,
                    manifest_path=manifest_path,
                )

            manifest = capture.load_manifest(manifest_path)

        self.assertEqual(stats["created"], 1)
        self.assertEqual(manifest["01abc"]["category"], "video")
        self.assertEqual(manifest["01abc"]["source_type"], "Reader Share Sheet iOS")
        self.assertEqual(manifest["01abc"]["source_url"], "https://youtube.com/watch?v=abc123")

    def test_manifest_skip_requires_file_content_hash_match(self):
        doc = {
            "id": "01abc",
            "url": "https://read.readwise.io/read/01abc",
            "title": "Example Article",
            "source_url": "https://example.com/article",
            "html_content": "",
            "category": "article",
            "saved_at": "2026-04-20T00:00:00+00:00",
        }
        with tempfile.TemporaryDirectory() as tmp:
            articles_dir = Path(tmp) / "articles"
            articles_dir.mkdir()
            article_path = articles_dir / "example-article.md"
            article_path.write_text('---\nreader_id: "01abc"\ncontent_hash: "stale"\n---\n\nold\n', encoding="utf-8")
            _, expected_hash, _ = capture.build_article(
                doc,
                notion_page_id="notion-page",
                session=object(),
                apply=False,
                download_images=False,
            )
            manifest_path = articles_dir / "manifest.jsonl"
            capture.write_manifest(
                {
                    "01abc": {
                        "reader_id": "01abc",
                        "path": str(article_path),
                        "content_hash": expected_hash,
                    }
                },
                manifest_path,
            )

            with contextlib.redirect_stdout(io.StringIO()):
                stats = capture.capture_docs(
                    [doc],
                    notion_page_map={"01abc": "notion-page"},
                    apply=False,
                    download_images=False,
                    articles_dir=articles_dir,
                    manifest_path=manifest_path,
                )

            self.assertEqual(stats["updated"], 1)

    def test_source_type_for_prefers_explicit_field_then_source(self):
        self.assertEqual(
            capture.source_type_for({"source_type": "Reader RSS", "source": "Reader Share Sheet iOS"}),
            "Reader RSS",
        )
        self.assertEqual(
            capture.source_type_for({"source": "Readwise web highlighter"}),
            "Readwise web highlighter",
        )


if __name__ == "__main__":
    unittest.main()
