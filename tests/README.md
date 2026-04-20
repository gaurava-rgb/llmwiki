# Tests

Run the local contract tests with:

```bash
python3 -m unittest discover -s tests
```

These tests intentionally avoid network calls and third-party Python packages.
They check the repo contract that must be true before GitHub versioning and
Notion integration work becomes safe.
