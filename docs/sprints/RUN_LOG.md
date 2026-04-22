# Sprint Run Log

## 2026-04-20 - Sprint 0 Kickoff

Requested outcome:

- Audit what already exists in the repo.
- Build measurable sprints toward a Notion + GitHub LLM Wiki.
- Add testable, reversible, versioned working conventions.
- Keep progress and checks in a durable project file.

Actions completed:

- Audited root files, wiki output, source/article/image folders, Notion scripts,
  compiler plugin, and existing logs.
- Confirmed root folder is not currently a git repository.
- Confirmed compiled wiki exists with 12 topics, 3 concepts, and 18 classified
  sources out of 20 scanned.
- Identified existing Notion sync scripts and one prior Notion sync log. The
  prior log reaches item 172 of 338 and does not include a final completion
  summary, so the previous Notion sync should be treated as partial.
- Moved Notion/Readwise script configuration to environment variables.
- Removed explicit service-token curl allowances from local Claude settings.
- Added `.gitignore`, `.env.example`, and `reader/.env.example`.
- Added `requirements.txt` for the Python sync/capture scripts.
- Added `README.md` for the public GitHub repository.
- Added `.gitmodules` so `llm-wiki-compiler/` is tracked as an upstream
  submodule.
- Configured the compiler submodule to ignore untracked local files so root
  status stays clean.
- Initialized root Git repository and added remote
  `https://github.com/gaurava-rgb/llmwiki.git`.
- Staged baseline files for the first commit. Ignored files include `.env`,
  `reader/.env`, `.claude/settings.local.json`, logs, caches, and `.DS_Store`.
- Replaced duplicated short `AGENTS.md`/`CLAUDE.md` instructions with one
  canonical operating manual.
- Added this sprint plan, test plan, and run log.
- Added no-network contract tests under `tests/`.

Open blockers:

- GitHub remote provided: `https://github.com/gaurava-rgb/llmwiki.git`.
- The selected repository is public. Raw articles, images, and compiled wiki
  pages should be treated as public after push.
- Existing exposed service credentials should be rotated in Notion and Readwise
  even though local `.env` files are ignored.
- Python dependencies for the sync scripts are not installed in the current
  environment (`bs4` was missing during audit). `requirements.txt` now lists
  the needed packages.

Checks run:

```bash
python3 -m unittest discover -s tests
```

Result: passed, 6 tests.

Token-pattern scan:

Result: passed by direct `rg` scan; no live Notion/Readwise tokens matched in
non-cache project files.

```bash
git status --short
```

Initial result: failed before Sprint 1 setup because the root folder was not a
git repository yet.

Current result: root Git repository initialized and baseline files staged.

Additional GitHub setup:

- Created baseline commit `Baseline LLM wiki setup`.
- Created follow-up commit `Configure compiler submodule`.
- Moved `baseline/notion-github-start` to the current baseline state.
- Pushed `main` to `https://github.com/gaurava-rgb/llmwiki.git`.
- Pushed `baseline/notion-github-start` to GitHub.
- Root working tree was clean after the baseline tag.

Final Sprint 1 checks:

```bash
python3 -m unittest discover -s tests
```

Result: passed, 6 tests.

Token-pattern scan:

Result: passed by direct `rg` scan excluding logs, caches, the compiler `.git`,
and the saved Readwise API documentation page containing placeholder examples.

## 2026-04-20 - Sprint 2 Notion Schema Start

Requested outcome:

- Use the local Notion token to create the Notion-side schema.

Actions completed:

- Found local Notion token in ignored `reader/.env` under `notion_api`.
- Confirmed root `.env` is not present.
- Queried Notion search and found existing database `Export via Reader`.
- Confirmed existing database properties before applying schema changes.
- Added `notion_schema.py` to make schema creation repeatable and idempotent.
- First schema apply created the control page and updated Raw Sources, then
  failed because Notion required explicit relation type metadata.
- Patched relation properties to use `single_property` and reran successfully.
- Created Notion databases:
  - Raw Sources: `3464ebe7-f118-8086-ae21-fa8b46f294ec`
  - Control Page: `3484ebe7-f118-81cf-aa1e-c87efef41174`
  - Wiki Pages: `3484ebe7-f118-81b6-b8b4-ff8291b5ddd2`
  - Claims / Evidence: `3484ebe7-f118-812f-a0fd-d1e1bd372cd2`
  - Ops Log: `3484ebe7-f118-81c0-ab3f-e64b6707979b`
- Created Notion Ops Log entry for the schema run:
  `3484ebe7-f118-8158-87ba-c9d7d4ed2587`
- Added `docs/sprints/NOTION_SCHEMA.md`.
- Added no-network schema contract tests.

Planned Notion layout:

- Use `Export via Reader` as Raw Sources.
- Create or reuse `LLM Wiki Control Center` page in Raw Sources.
- Create or reuse child databases:
  - `LLM Wiki - Wiki Pages`
  - `LLM Wiki - Claims / Evidence`
  - `LLM Wiki - Ops Log`

Checks run:

```bash
python3 -m py_compile notion_schema.py
python3 -m unittest discover -s tests
```

Result: passed, 10 tests.

## 2026-04-20 - Sprint 2 Incremental Notion Sync

Requested outcome:

- Sync the remaining Readwise Reader articles into Notion.
- Do not repeat articles already pushed.
- Use parallel agent execution if useful, while keeping the run logged.

Actions completed:

- Spawned a worker agent for the Notion sync. The worker stalled without a
  useful process/log, so it was closed and the sync was completed directly in
  this thread.
- Confirmed `reader/.env` is ignored and used it only as local runtime config.
- Created local `.venv/` and installed `requirements.txt` there because the
  system Python environment is externally managed and did not have `bs4`.
- Added `.venv/` to `.gitignore`.
- Ran the incremental sync against Raw Sources database
  `3464ebe7-f118-8086-ae21-fa8b46f294ec`.
- Hardened `sync_to_notion.py` so Notion select and multi-select values replace
  commas, which Notion rejects in option names.
- Added a metadata-only fallback when Notion/Cloudflare rejects full HTML page
  creation.
- Added retry handling for transient Notion page creation failures.
- Added a repository contract assertion that `.venv/` remains ignored.

Run details:

- `logs/sync_20260420_152926.log`: found 188 articles already in Notion and
  150 new articles to push. The run was manually stopped after two early
  failures and 21 successful pushes so the sync script could be hardened.
- `logs/sync_20260420_153053.log`: found 209 articles already in Notion and
  129 new articles to push. Result: 128 pushed, 1 failed, 209 skipped.
- `logs/sync_20260420_153550.log`: found 337 articles already in Notion and
  1 new article to push. Result: 1 pushed, 0 failed, 337 skipped.
- `logs/sync_20260420_153616.log`: final no-op verification found 338 articles
  already in Notion and 0 new articles to push.

Measurable outcome:

- Raw Sources in Notion is caught up for the current Reader API result set:
  338 Reader article/rss documents present and 0 remaining new documents.
- Re-running the sync is idempotent for the current dataset because Reader IDs
  are extracted from the `Reader URL` property before creating pages.

Checks run:

```bash
.venv/bin/python -m py_compile sync_to_notion.py
python3 -m unittest discover -s tests
```

Result: passed, 10 tests.

## 2026-04-20 - Sprint 3A/3B Public Capture Bridge

Requested outcome:

- Run Sprint 3A and Sprint 3B in parallel where practical.
- Sanitize public article markdown.
- Build the Reader/Notion to GitHub capture bridge.
- Keep outcomes measurable, idempotent, and logged.

Actions completed:

- Started two parallel worker agents:
  - Sprint 3A public markdown cleanup.
  - Sprint 3B capture bridge scaffold.
- Both workers stalled without returning final summaries, so they were shut
  down and the implementation was completed in this thread.
- Sanitized tracked markdown under `sources/articles/*.md` so public files no
  longer contain `access_token=`, Passport member links, member login email
  URLs, source-site membership footer lines, or the known account email.
- Added public article safety tests.
- Added `reader/capture_reader_to_markdown.py`.
- Added capture bridge contract tests for:
  - environment alias handling.
  - URL sanitization.
  - private footer sanitization.
  - markdown trailing-whitespace normalization.
  - malformed URL handling.
  - Reader URL ID extraction.
  - stable content hashes.
  - manifest round-trip.
  - dry-run no-write behavior.
  - stale local file detection when manifest hash and file hash diverge.
- Added Notion database title resolution for fresh shells where
  `reader/.env` has `notion_api` but no `NOTION_DATABASE_ID`.
- Synced the one Reader article that appeared after the previous Notion run.
  Log: `logs/sync_20260420_200230.log`.
- Ran the capture bridge against Reader and the Notion Raw Sources database.

Run details:

- Notion catch-up:
  - Existing Notion articles: 338.
  - New Reader articles found: 1.
  - Result: 1 pushed, 0 failed, 338 skipped.
- Capture dry-run before apply:
  - Reader docs selected: 339.
  - Notion page IDs mapped: 338 before catch-up, 339 after catch-up.
  - Planned local writes before first apply: 319 created, 20 updated.
- Capture apply:
  - `319` new markdown files created under `sources/articles/`.
  - `20` existing markdown files updated with Reader/Notion metadata and
    sanitized URLs.
  - `sources/articles/manifest.jsonl` written with 339 records.
- Image materialization check:
  - A full image-materializing run was started, then stopped after it generated
    hundreds of image files and made `sources/images/` too large for a prudent
    single public GitHub commit.
  - Generated untracked images from that aborted run were removed.
  - The text/metadata capture was rerun with external image URLs preserved.
  - Asset materialization remains a separate future sprint or opt-in run.
- Final idempotency check:
  - Capture dry-run selected 339 Reader docs.
  - Notion page IDs mapped: 339.
  - Result: 0 created, 0 updated, 339 skipped, 0 planned writes.

Measurable outcome:

- `sources/articles/` now contains 339 raw markdown article files.
- `sources/articles/manifest.jsonl` contains 339 records.
- Manifest uniqueness checks:
  - 339 unique Reader IDs.
  - 339 unique paths.
  - 339 records with Notion page IDs.
- Public-safety scan found no remaining matches for:
  - `access_token=`
  - `passport.online/member`
  - `member/login?email=`
  - `gaurav_a@tamu.edu`
  - `gaurav_a%40tamu.edu`

Checks run:

```bash
.venv/bin/python -m py_compile reader/capture_reader_to_markdown.py sync_to_notion.py notion_schema.py
python3 -m unittest discover -s tests
rg -n "access_token=|passport\\.online/member|member/login\\?email=|gaurav_a@tamu\\.edu|gaurav_a%40tamu\\.edu" sources/articles/*.md sources/articles/manifest.jsonl
env -u NOTION_DATABASE_ID -u READWISE_TOKEN -u NOTION_TOKEN .venv/bin/python reader/capture_reader_to_markdown.py
```

Result:

- Compile passed.
- Unit tests passed, 23 tests.
- Public-safety scan returned no matches.
- Capture idempotency dry-run returned 339 skipped and 0 planned writes.

## 2026-04-22 - Sprint 3C Expanded Reader Capture Types

Requested outcome:

- Broaden the capture bridge beyond article/rss.
- Preserve source format metadata so downstream wiki compilation can treat
  tweets, emails, videos, PDFs, and EPUBs differently later.
- Explain the pipeline plainly and keep the sprint logged.

Actions completed:

- Started a parallel worker agent for the bridge code and focused tests.
- Reviewed and integrated the worker changes in this thread.
- Expanded supported top-level Reader categories in
  `reader/capture_reader_to_markdown.py` to:
  - `article`
  - `rss`
  - `tweet`
  - `email`
  - `video`
  - `pdf`
  - `epub`
- Kept child records excluded by preserving the `parent_id` filter, so
  highlights and notes are still not materialized as standalone source files.
- Added `category` and `source_type` to raw markdown frontmatter.
- Added `category` and `source_type` to manifest records.
- Updated README with a plain-English pipeline explanation and explicit output
  locations.
- Materialized the widened Reader set into `sources/articles/`.

Run details:

- Pre-change audit against the live Reader API:
  - Total Reader API docs returned: 824.
  - Top-level docs: 747.
  - Child docs: 77.
  - Existing capture scope before this sprint: 339 (`article` + `rss`).
- Widened-capture dry-run:
  - Reader docs selected: 750.
  - Notion page IDs mapped: 339.
  - Planned writes: 411 created, 339 updated, 0 skipped.
- Widened-capture apply:
  - Reader docs selected: 750.
  - Result: 411 created, 339 updated, 0 skipped.
- Final idempotency check after apply:
  - Reader docs selected: 750.
  - Notion page IDs mapped: 339.
  - Result: 0 created, 0 updated, 750 skipped, 0 planned writes.

Measurable outcome:

- `sources/articles/` now contains 750 raw source markdown files.
- `sources/articles/manifest.jsonl` now contains 750 records.
- Manifest uniqueness checks:
  - 750 unique Reader IDs.
  - 750 unique paths.
  - 339 records with Notion page IDs.
  - 411 records without Notion page IDs.
- Manifest category breakdown:
  - `tweet`: 371
  - `rss`: 176
  - `article`: 166
  - `email`: 25
  - `video`: 6
  - `pdf`: 5
  - `epub`: 1

Current gap:

- The Git capture bridge now materializes the broader Reader set directly from
  Reader.
- `sync_to_notion.py` is still the narrower lane and mirrors the
  `article`/`rss` subset into the Notion Raw Sources database.
- That is why 411 captured files currently have blank `notion_page_id` values.

Checks run:

```bash
python3 -m unittest discover -s tests
.venv/bin/python -m py_compile reader/capture_reader_to_markdown.py sync_to_notion.py notion_schema.py
rg -n "access_token=|passport\\.online/member|member/login\\?email=|gaurav_a@tamu\\.edu|gaurav_a%40tamu\\.edu" sources/articles/*.md sources/articles/manifest.jsonl
env -u NOTION_DATABASE_ID -u READWISE_TOKEN -u NOTION_TOKEN .venv/bin/python reader/capture_reader_to_markdown.py
env -u NOTION_DATABASE_ID -u READWISE_TOKEN -u NOTION_TOKEN .venv/bin/python reader/capture_reader_to_markdown.py --apply
env -u NOTION_DATABASE_ID -u READWISE_TOKEN -u NOTION_TOKEN .venv/bin/python reader/capture_reader_to_markdown.py
```

Result:

- Compile passed.
- Unit tests passed, 28 tests.
- Public-safety scan returned no matches.
- Final capture dry-run returned 750 skipped and 0 planned writes.

## 2026-04-22 - Sprint 3D Widen Notion Sync Types

Requested outcome:

- Choose the next bounded sprint after raw capture expansion.
- Widen the incremental Notion sync lane to match the broader raw capture set.
- Keep the run measurable, testable, and logged.

Actions completed:

- Expanded `sync_to_notion.py` from the `article`/`rss` subset to the same
  supported top-level Reader categories used by the capture bridge:
  `article`, `rss`, `tweet`, `email`, `video`, `pdf`, and `epub`.
- Added `Source Type` mapping based on Reader `source_type` or fallback
  `source`.
- Added `Reader ID`, `Status`, `Last Synced At`, and `Sync Run ID` properties
  to new Notion page creates so Raw Sources rows stay aligned with the local
  manifest/frontmatter contract.
- Added `--dry-run` and `--max-items` to the incremental Notion sync script so
  the sync can be previewed before any external write.
- Added no-network sync contract tests for supported categories, `Source Type`
  behavior, Reader ID extraction, and dry-run planning.

Run details:

- `logs/sync_20260422_183304.log`: dry-run against the widened category set.
  Result: 412 new docs planned, 339 existing docs detected in Notion.
  Planned category breakdown: 371 tweets, 25 emails, 6 videos, 5 PDFs,
  2 articles, 2 RSS items, and 1 EPUB.
- `logs/sync_20260422_183328.log`: first full widened sync run.
  Result: 411 pushed, 1 failed, 339 skipped.
- The single failed item was Reader document `01kk6xdvtqv3awdgc7p0k5ywec`
  (`"Someone built a full virtual computer that runs inside..."`), caused by
  Notion counting one summary field as 2001 characters and then one quote block
  as 2001 characters.
- `logs/sync_20260422_184551.log`: post-fix dry-run. Result: 1 remaining tweet
  planned.
- `logs/sync_20260422_184618.log`: first retry after tightening property
  truncation. Result: 0 pushed, 1 failed because the summary quote block still
  used the untrimmed string.
- `logs/sync_20260422_184658.log`: second retry after tightening the summary
  quote block. Result: 1 pushed, 0 failed.
- `logs/sync_20260422_184722.log`: final dry-run verification. Result: 0 new
  docs to push.

Measurable outcome:

- `sync_to_notion.py` is now aligned with the broader raw-capture source set:
  `article`, `rss`, `tweet`, `email`, `video`, `pdf`, and `epub`.
- Raw Sources in Notion is caught up for the current supported Reader dataset:
  751 existing Reader docs detected and 0 remaining new docs in the final
  dry-run.
- The widened backfill required 412 planned creates in the initial dry-run and
  completed as 411 successful creates in the first run plus 1 successful retry.
- No-network verification now passes with 33 tests.
- One newer supported Reader doc appeared after the previous local raw-capture
  run, so Notion is now current at 751 while the local raw markdown layer from
  the earlier capture sprint remains at 750 until capture is rerun.

Checks run:

```bash
python3 -m unittest discover -s tests
.venv/bin/python -m py_compile sync_to_notion.py
```

## 2026-04-22 - Sprint 4 Wiki Rebuild Refresh

Requested outcome:

- Rebuild the compiled wiki from the current raw Reader corpus.
- Keep the result measurable, testable, and logged.

Actions completed:

- Confirmed the earlier full wiki rebuild had already regenerated the compiled
  wiki from the then-current 750 raw source files.
- Detected a one-item gap between the local raw capture layer and Notion's
  current Raw Sources state.
- Reran `reader/capture_reader_to_markdown.py --apply` to refresh the local raw
  corpus from Reader.
- Captured 1 new raw source file:
  `john-ternus-and-apples-hardware-defined-future-spacexai-and-cursor.md`.
- Refreshed raw-source frontmatter and manifest metadata so Notion page IDs are
  now carried through the local raw layer.
- Incrementally updated the compiled wiki instead of regenerating every topic
  again:
  - bumped the corpus totals from 750 to 751 sources,
  - added the new Stratechery source to the Apple topic,
  - updated compile state and wiki logs.

Measurable outcome:

- Local raw corpus now contains 751 captured source markdown files.
- Compiled wiki now reflects 751 classified sources.
- Topic count remains 21.
- Concept count remains 5.
- Apple topic source count increased from 21 to 22.

Checks run:

```bash
.venv/bin/python reader/capture_reader_to_markdown.py --apply
python3 -m unittest discover -s tests
git diff --check
```
