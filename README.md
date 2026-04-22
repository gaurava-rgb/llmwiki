# llmwiki

Cloud-backed LLM Wiki for saved articles.

## Architecture

- `sources/articles/` contains raw article markdown.
- `sources/images/` contains downloaded article images.
- `sources/articles/wiki/` contains the compiled LLM-maintained wiki.
- Notion is the intended online capture/review layer.
- GitHub is the versioned source of truth for markdown, assets, scripts, tests,
  and rollback history.

## Pipeline, Plainly

Think of the system as five layers:

1. **Reader is the inbox.**
   This is where saved links, emails, tweets, PDFs, and other source items
   start out.
2. **Notion is the review table.**
   The raw-source database in Notion is where source records can be tracked,
   reviewed, and annotated.
3. **This repo is the durable file copy.**
   The capture bridge pulls supported top-level Reader items and writes
   normalized markdown files into `sources/articles/` so the source layer is
   versioned in Git.
4. **The wiki compiler turns raw files into knowledge pages.**
   It reads `sources/articles/` and writes synthesized topic/concept pages into
   `sources/articles/wiki/`.
5. **Queries read the compiled wiki, not the whole inbox.**
   That keeps later agent work smaller, faster, and more consistent.

## Where Outputs Go

- **Reader -> Notion sync logs:** `logs/sync_*.log`
- **Raw captured source files:** `sources/articles/*.md`
- **Capture manifest:** `sources/articles/manifest.jsonl`
- **Downloaded images when opted in:** `sources/images/`
- **Compiled wiki index:** `sources/articles/wiki/INDEX.md`
- **Compiled wiki topic pages:** `sources/articles/wiki/topics/`
- **Compiled wiki concepts:** `sources/articles/wiki/concepts/`
- **Wiki compile state/logs:** `sources/articles/wiki/.compile-state.json` and
  `sources/articles/wiki/compile-log.md`

## Typical Flow

1. Save something in Reader.
2. Optionally sync Reader items into the Notion Raw Sources database.
   `sync_to_notion.py` now mirrors the same supported top-level Reader set as
   the capture bridge: `article`, `rss`, `tweet`, `email`, `video`, `pdf`, and
   `epub`. Use `--dry-run` first to preview what would be created:

```bash
python3 sync_to_notion.py --dry-run
python3 sync_to_notion.py
```

3. Materialize the broader supported Reader set in versioned markdown in this
   repo. The capture bridge currently handles top-level `article`, `rss`,
   `tweet`, `email`, `video`, `pdf`, and `epub` items, and stores `category`
   plus `source_type` in frontmatter and the manifest:

```bash
python3 reader/capture_reader_to_markdown.py --apply
```

4. Rebuild the compiled knowledge base:

```text
/wiki-compile
```

5. Browse or query the compiled result at
   `sources/articles/wiki/INDEX.md` or with:

```text
/wiki-query [topic]
```

## Operating Files

- `AGENTS.md` is the canonical Codex/Claude operating manual.
- `CLAUDE.md` points Claude to `AGENTS.md`.
- `docs/sprints/SPRINTS.md` defines the measurable sprint backlog.
- `docs/sprints/TEST_PLAN.md` defines local and future integration tests.
- `docs/sprints/RUN_LOG.md` records sprint execution.

## Local Setup

```bash
python3 -m unittest discover -s tests
```

Create/update the Notion schema:

```bash
python3 notion_schema.py --apply
```

Capture Reader/Notion raw sources into local markdown:

```bash
python3 reader/capture_reader_to_markdown.py --apply
```

Image downloads are opt-in because they can create a large binary diff:

```bash
python3 reader/capture_reader_to_markdown.py --apply --download-images
```

Notion and Readwise credentials are local only. Copy the examples and fill them
outside Git:

```bash
cp .env.example .env
cp reader/.env.example reader/.env
```

Required environment variables:

- `NOTION_TOKEN`
- `READWISE_TOKEN`

The Reader capture bridge and `sync_to_notion.py` also accept `reader/.env`
aliases:

- `readwise_token`
- `notion_api`
- `database_id` for `NOTION_DATABASE_ID`; optional when the Raw Sources
  database is still named `Export via Reader`.

## Safety Notes

This repository is public. Do not commit `.env`, `reader/.env`, Claude local
settings, sync logs, or generated caches.
