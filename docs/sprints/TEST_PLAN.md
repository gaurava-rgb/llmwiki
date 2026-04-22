# Test Plan

Tests are split into no-network contract tests and later integration tests.
No-network tests must run without Notion, Readwise, GitHub, or installed API
credentials.

## How to Run

```bash
python3 -m unittest discover -s tests
```

## Current No-Network Test Cases

| Test case | Use case | Expected result |
| --- | --- | --- |
| Instruction files are linked | Codex and Claude use one operating manual | `AGENTS.md` names sprint/test/run-log docs and `CLAUDE.md` points to `AGENTS.md` |
| Git ignore protects local files | Repo can become a GitHub repo safely | `.env`, `reader/.env`, `.claude/settings.local.json`, logs, caches are ignored |
| No obvious hardcoded service tokens | GitHub commits do not include live Notion/Readwise tokens | token-like Notion/Readwise auth literals are absent from tracked project files |
| No private article access URLs | Public article markdown is safe to push | tracked article markdown does not contain private access tokens, Passport member URLs, or account email markers |
| Wiki index links resolve | Agents can navigate compiled topics/concepts | all `[[topics/...]]` and `[[concepts/...]]` links in `INDEX.md` resolve |
| Article image references resolve | Raw markdown can preserve local images when materialized | any local image paths in article frontmatter/body exist |
| Capture bridge contracts | Reader/Notion capture is idempotent and public-safe | URL sanitizer, supported Reader categories, `category`/`source_type` metadata, manifest, content hashes, dry-run behavior, and stale-file detection work without network |
| Notion sync contracts | Reader -> Notion sync stays aligned with capture metadata | supported Reader categories, `Reader ID` / `Source Type` mapping, and dry-run planning work without network |

## Planned Fixture Tests

| Sprint | Fixture | Expected behavior |
| --- | --- | --- |
| Sprint 2 | article with cover image | dry-run maps cover image to Notion field and page block |
| Sprint 2 | article with inline images | dry-run preserves all image blocks or records skipped images |
| Sprint 2 | article with no content | dry-run creates source page with no-content warning |
| Sprint 3 | repeated Reader document | second capture is a no-op |
| Sprint 3 | changed Reader document | manifest records update and changed markdown path |
| Sprint 4 | broken wiki link | health check fails with missing target path |
| Sprint 5 | repeated wiki publish | second publish updates pages, creates zero duplicates |

## Integration Tests Requiring Approval

These tests touch external services and must not run without explicit user
approval for the run:

- Readwise fetch against a max of 3 documents.
- Notion schema validation against the target database.
- Notion test publish into a temporary/test database.
- GitHub remote push after the private repository is selected.
