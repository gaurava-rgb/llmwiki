import unittest

import sync_to_notion


class SyncToNotionContractTests(unittest.TestCase):
    def test_supported_reader_categories_match_capture_bridge(self):
        self.assertEqual(
            sync_to_notion.READER_CATEGORIES,
            {"article", "rss", "tweet", "email", "video", "pdf", "epub"},
        )

    def test_source_type_for_prefers_explicit_field_then_source(self):
        self.assertEqual(
            sync_to_notion.source_type_for(
                {"source_type": "Reader RSS", "source": "Reader Share Sheet iOS"}
            ),
            "Reader RSS",
        )
        self.assertEqual(
            sync_to_notion.source_type_for({"source": "Readwise web highlighter"}),
            "Readwise web highlighter",
        )
        self.assertEqual(sync_to_notion.source_type_for({}), "")

    def test_reader_id_from_page_prefers_reader_id_property_then_reader_url(self):
        page = {
            "properties": {
                "Reader ID": {
                    "rich_text": [
                        {"plain_text": "01readerid", "text": {"content": "01readerid"}}
                    ]
                },
                "Reader URL": {"url": "https://read.readwise.io/read/01fallback"},
            }
        }
        self.assertEqual(sync_to_notion.reader_id_from_page(page), "01readerid")

        fallback_page = {
            "properties": {"Reader URL": {"url": "https://read.readwise.io/read/01fallback"}}
        }
        self.assertEqual(sync_to_notion.reader_id_from_page(fallback_page), "01fallback")

    def test_build_page_properties_include_sync_metadata(self):
        doc = {
            "id": "01abc",
            "title": "Tweet thread",
            "author": "Example Author",
            "source_url": "https://example.com/thread",
            "url": "https://read.readwise.io/read/01abc",
            "site_name": "X",
            "category": "tweet",
            "source": "Reader Share Sheet iOS",
            "source_type": "Reader Share Sheet iOS",
            "location": "new",
            "published_date": "2026-04-22T12:00:00Z",
            "saved_at": "2026-04-22T12:30:00Z",
            "reading_time": 2,
            "word_count": 180,
            "reading_progress": 50,
            "summary": "Quick source summary",
            "image_url": "https://example.com/image.jpg",
            "notes": "Captured locally",
            "tags": {"ai": {}, "agents": {}},
        }

        properties = sync_to_notion.build_page_properties(
            doc,
            synced_at="2026-04-22T13:00:00+00:00",
            run_id="sync-20260422T130000Z",
        )

        self.assertEqual(properties["Category"]["select"]["name"], "tweet")
        self.assertEqual(
            properties["Source Type"]["select"]["name"], "Reader Share Sheet iOS"
        )
        self.assertEqual(
            properties["Reader ID"]["rich_text"][0]["text"]["content"], "01abc"
        )
        self.assertEqual(properties["Status"]["select"]["name"], "captured")
        self.assertEqual(
            properties["Last Synced At"]["date"]["start"], "2026-04-22T13:00:00+00:00"
        )
        self.assertEqual(
            properties["Sync Run ID"]["rich_text"][0]["text"]["content"],
            "sync-20260422T130000Z",
        )

    def test_plan_sync_docs_skips_existing_ids_and_honors_max_items(self):
        docs = [
            {"id": "01a"},
            {"id": "01b"},
            {"id": "01c"},
        ]

        planned = sync_to_notion.plan_sync_docs({"01a"}, docs, max_items=1)

        self.assertEqual([doc["id"] for doc in planned], ["01b"])


if __name__ == "__main__":
    unittest.main()
