# llmwiki

Cloud-backed LLM Wiki for saved articles.

## Architecture

- `sources/articles/` contains raw article markdown.
- `sources/images/` contains downloaded article images.
- `sources/articles/wiki/` contains the compiled LLM-maintained wiki.
- Notion is the intended online capture/review layer.
- GitHub is the versioned source of truth for markdown, assets, scripts, tests,
  and rollback history.

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

The Reader capture bridge also accepts `reader/.env` aliases:

- `readwise_token`
- `notion_api`
- `database_id` for `NOTION_DATABASE_ID`; optional when the Raw Sources
  database is still named `Export via Reader`.

## Safety Notes

This repository is public. Do not commit `.env`, `reader/.env`, Claude local
settings, sync logs, or generated caches.
