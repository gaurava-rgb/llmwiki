import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class RepoContractTests(unittest.TestCase):
    def test_instruction_files_point_to_sprint_controls(self):
        agents = read_text("AGENTS.md")

        self.assertIn("docs/sprints/SPRINTS.md", agents)
        self.assertIn("docs/sprints/TEST_PLAN.md", agents)
        self.assertIn("docs/sprints/RUN_LOG.md", agents)
        self.assertIn("python3 -m unittest discover -s tests", agents)

    def test_claude_delegates_to_agents(self):
        claude = read_text("CLAUDE.md")

        self.assertIn("AGENTS.md", claude)
        self.assertIn("canonical operating manual", claude)

    def test_gitignore_protects_local_secrets_and_noise(self):
        gitignore = read_text(".gitignore")

        for expected in [
            ".env",
            "reader/.env",
            ".claude/settings.local.json",
            "logs/",
            ".venv/",
            "__pycache__/",
            ".DS_Store",
        ]:
            self.assertIn(expected, gitignore)

    def test_no_obvious_hardcoded_service_tokens(self):
        scanned_paths = [
            "sync_to_notion.py",
            "push_to_notion.py",
            ".claude/settings.local.json",
        ]
        notion_token = re.compile("ntn" + r"_[A-Za-z0-9]+")
        readwise_auth = re.compile("Authorization:" + r"\s*Token\s+[A-Za-z0-9]{20,}")

        for path in scanned_paths:
            text = read_text(path)
            self.assertIsNone(notion_token.search(text), path)
            self.assertIsNone(readwise_auth.search(text), path)

    def test_wiki_index_links_resolve(self):
        index = read_text("sources/articles/wiki/INDEX.md")
        links = re.findall(r"\[\[((?:topics|concepts)/[^\]]+)\]\]", index)

        self.assertGreater(len(links), 0)
        for link in links:
            target = ROOT / "sources/articles/wiki" / f"{link}.md"
            self.assertTrue(target.exists(), f"Missing wiki link target: {link}")

    def test_article_local_image_references_resolve(self):
        image_refs = []
        for article in (ROOT / "sources/articles").glob("*.md"):
            text = article.read_text(encoding="utf-8")
            image_refs.extend(
                (article, match.group(1))
                for match in re.finditer(r'image:\s*"([^"]+)"', text)
                if match.group(1).startswith("sources/images/")
            )
            image_refs.extend(
                (article, match.group(1))
                for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text)
                if match.group(1).startswith("sources/images/")
            )

        for article, image_path in image_refs:
            self.assertTrue(
                (ROOT / image_path).exists(),
                f"{article.relative_to(ROOT)} references missing image {image_path}",
            )


if __name__ == "__main__":
    unittest.main()
