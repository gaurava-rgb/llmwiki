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
