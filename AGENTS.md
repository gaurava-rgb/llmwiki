# v1april Knowledge Base Operating Manual

This is the canonical operating file for Codex and Claude. Keep `CLAUDE.md`
pointing here so both agents follow one workflow.

## Current Architecture

- Raw article markdown lives in `sources/articles/`.
- Raw downloaded images live in `sources/images/`.
- The compiled LLM wiki lives in `sources/articles/wiki/`.
- The wiki index is `sources/articles/wiki/INDEX.md`.
- The wiki schema is `sources/articles/wiki/schema.md`.
- Notion sync scripts are `sync_to_notion.py` and `push_to_notion.py`.
- Sprint planning and run logs live in `docs/sprints/`.

## Goal

Build a cloud-backed LLM Wiki flow:

1. Notion is the online capture and review layer for raw articles, images,
   metadata, and source status.
2. GitHub is the versioned source of truth for durable markdown, assets,
   compiled wiki pages, tests, and rollback history.
3. Codex/Claude maintain the wiki through explicit sprints with measurable
   outcomes, tests, rollback steps, and run logs.

## Agent Rules

1. Treat `sources/articles/` and `sources/images/` as raw source material.
   Do not rewrite or delete raw files unless the user asks for that.
2. Treat `sources/articles/wiki/` as LLM-maintained compiled knowledge.
   Update it through `/wiki-compile`, `/wiki-ingest`, or explicit edits that
   cite source files.
3. Read `sources/articles/wiki/INDEX.md` before answering questions about
   companies, topics, themes, or saved articles.
4. Never commit or paste live credentials. Use environment variables:
   `NOTION_TOKEN`, `NOTION_DATABASE_ID`, and `READWISE_TOKEN`.
5. Do not run destructive Notion operations, including archive/delete/rebuild
   pushes, without an explicit user confirmation for that run.
6. Prefer dry-run/idempotent sync behavior before touching external services.
7. Before and after each sprint, update `docs/sprints/RUN_LOG.md`.
8. Keep sprint outcomes testable with `python3 -m unittest discover -s tests`.
9. If a test cannot run because a dependency or credential is missing, log the
   blocker rather than guessing.
10. Do not create a GitHub remote until the user provides the target repo or
    confirms the repo name/visibility.

## Commands

- Rebuild the wiki: `/wiki-compile`
- Query the wiki: `/wiki-query [topic]`
- Local contract tests: `python3 -m unittest discover -s tests`
- Read sprint plan: `docs/sprints/SPRINTS.md`
- Read test plan: `docs/sprints/TEST_PLAN.md`
- Read run log: `docs/sprints/RUN_LOG.md`

## Current Sprint State

- Sprint 0 is complete: baseline audit, credential cleanup, sprint plan, and
  local test harness.
- Sprint 1 baseline GitHub versioning is complete: root Git is initialized,
  `origin` points to `https://github.com/gaurava-rgb/llmwiki.git`, and the
  rollback tag is `baseline/notion-github-start`.
- Notion integration exists as scripts, but needs schema hardening,
  idempotency tests, and confirmed credentials before external runs.
