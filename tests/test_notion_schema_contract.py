import unittest

import notion_schema


class NotionSchemaContractTests(unittest.TestCase):
    def test_schema_database_titles_are_stable(self):
        self.assertEqual(notion_schema.DEFAULT_RAW_DATABASE_TITLE, "Export via Reader")
        self.assertEqual(notion_schema.CONTROL_PAGE_TITLE, "LLM Wiki Control Center")
        self.assertEqual(notion_schema.WIKI_DB_TITLE, "LLM Wiki - Wiki Pages")
        self.assertEqual(notion_schema.CLAIMS_DB_TITLE, "LLM Wiki - Claims / Evidence")
        self.assertEqual(notion_schema.OPS_DB_TITLE, "LLM Wiki - Ops Log")

    def test_raw_source_properties_include_sync_contract(self):
        properties = notion_schema.raw_source_properties()

        for expected in [
            "Reader ID",
            "Source Type",
            "Status",
            "Local Markdown Path",
            "Local Asset Paths",
            "Content Hash",
            "Last Synced At",
            "Sync Run ID",
            "Processing Notes",
        ]:
            self.assertIn(expected, properties)

    def test_wiki_database_has_relation_to_raw_sources(self):
        properties = notion_schema.wiki_database_properties("raw-db-id")

        self.assertEqual(
            properties["Related Raw Sources"]["relation"]["database_id"],
            "raw-db-id",
        )
        self.assertEqual(properties["Related Raw Sources"]["relation"]["type"], "single_property")

    def test_claims_and_ops_databases_have_expected_relations(self):
        claims = notion_schema.claims_database_properties("raw-db-id", "wiki-db-id")
        ops = notion_schema.ops_database_properties("raw-db-id", "wiki-db-id")

        self.assertEqual(claims["Raw Source"]["relation"]["database_id"], "raw-db-id")
        self.assertEqual(claims["Wiki Page"]["relation"]["database_id"], "wiki-db-id")
        self.assertEqual(ops["Touched Sources"]["relation"]["database_id"], "raw-db-id")
        self.assertEqual(ops["Touched Wiki Pages"]["relation"]["database_id"], "wiki-db-id")
        self.assertEqual(claims["Raw Source"]["relation"]["type"], "single_property")
        self.assertEqual(ops["Touched Wiki Pages"]["relation"]["type"], "single_property")


if __name__ == "__main__":
    unittest.main()
