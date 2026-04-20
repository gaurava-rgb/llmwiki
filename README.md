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

Notion and Readwise credentials are local only. Copy the examples and fill them
outside Git:

```bash
cp .env.example .env
cp reader/.env.example reader/.env
```

Required environment variables:

- `NOTION_TOKEN`
- `NOTION_DATABASE_ID`
- `READWISE_TOKEN`

## Safety Notes

This repository is public. Do not commit `.env`, `reader/.env`, Claude local
settings, sync logs, or generated caches.
