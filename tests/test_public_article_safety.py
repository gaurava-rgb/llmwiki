import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIVATE_MARKERS = (
    "access_token=",
    "passport.online/member",
    "member/login?email=",
    "gaurav_a@tamu.edu",
    "gaurav_a%40tamu.edu",
)


class PublicArticleSafetyTests(unittest.TestCase):
    def test_tracked_article_markdown_has_no_private_url_material(self):
        offenders = []
        for path in sorted((ROOT / "sources" / "articles").glob("*.md")):
            text = path.read_text(encoding="utf-8").lower()
            for marker in PRIVATE_MARKERS:
                if marker in text:
                    offenders.append(f"{path.relative_to(ROOT)} contains {marker}")

        self.assertEqual(offenders, [])

    def test_manifest_has_no_private_url_material(self):
        manifest_path = ROOT / "sources" / "articles" / "manifest.jsonl"
        if not manifest_path.exists():
            self.skipTest("manifest not present")

        text = manifest_path.read_text(encoding="utf-8").lower()
        offenders = [marker for marker in PRIVATE_MARKERS if marker in text]

        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
