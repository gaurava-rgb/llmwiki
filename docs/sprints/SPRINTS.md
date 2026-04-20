# Notion + GitHub LLM Wiki Sprint Plan

This plan turns the current local article wiki into a cloud-backed, versioned
Notion + GitHub system. Each sprint must be measurable, testable, reversible,
and logged in `docs/sprints/RUN_LOG.md`.

## Baseline Audit

Current state as of 2026-04-20:

| Area | Status | Evidence |
| --- | --- | --- |
| Raw article layer | Present | `sources/articles/*.md` |
| Raw image layer | Present | `sources/images/*` |
| Compiled wiki | Present | `sources/articles/wiki/INDEX.md` |
| Wiki compiler | Present | `llm-wiki-compiler/` submodule |
| Notion sync scripts | Present | `sync_to_notion.py`, `push_to_notion.py` |
| Local tests | Added in Sprint 0 | `tests/test_repo_contracts.py` |
| Root Git repository | Present | branch `main` |
| GitHub remote | Pushed | `https://github.com/gaurava-rgb/llmwiki.git` |
| Secrets hygiene | Partially remediated | env files ignored; token rotation still required |
| Notion schema contract | Created | `docs/sprints/NOTION_SCHEMA.md` |
| Reversible sync | Incomplete | destructive archive script still exists and needs safeguards |

## Sprint 0 - Baseline, Safety, and Operating Manual

Objective: make the repo safe enough to put under GitHub and give agents one
consistent way to plan, run, test, and log work.

Deliverables:

- Canonical `AGENTS.md` operating manual.
- `CLAUDE.md` points to `AGENTS.md` to avoid drift.
- `.gitignore` protects local secrets and generated noise.
- `.env.example` and `reader/.env.example` document required credentials.
- Notion/Readwise credentials are loaded from environment variables.
- Local no-network contract tests exist.
- Sprint plan, test plan, and run log exist.

Measurable outcomes:

- `python3 -m unittest discover -s tests` passes.
- The local token-safety contract test does not find live Notion/Readwise
  service tokens in project files that would be committed.
- `AGENTS.md`, `CLAUDE.md`, sprint docs, and tests are internally linked.

Rollback:

- Restore modified files from Git once Sprint 1 initializes versioning.
- Before Git exists, use the run log plus file paths listed in final summaries
  to manually revert edits if needed.

## Sprint 1 - GitHub Versioning and Reversibility

Objective: make the repository versioned, private, and recoverable.

Deliverables:

- Initialize root git repository after credentials are removed.
- Create or connect to a user-provided GitHub repository.
- First commit contains source markdown, images, wiki, scripts, docs, and tests.
- The wiki compiler is tracked as a submodule pinned to the upstream compiler
  commit instead of vendoring its internal `.git` history into this repo.
- Add a `main` branch baseline tag such as `baseline/notion-github-start`.
- Document rollback commands in `docs/sprints/RUN_LOG.md`.

Measurable outcomes:

- `git status --short` is clean after the baseline commit.
- `git remote -v` shows the selected GitHub remote.
- `git tag --list` includes the baseline tag.
- A fresh clone can run `python3 -m unittest discover -s tests`.

Rollback:

- Use `git restore <path>` for file-level rollback.
- Use `git switch -c rescue/<date>` before risky changes.
- Use the baseline tag to return to the pre-sync state.

Blocked decisions:

- Whether to track `sources/images/` directly or move large assets to Git LFS.

Public repo note:

- The selected GitHub repository is public. Do not commit `.env`,
  `reader/.env`, `.claude/settings.local.json`, generated logs, or local caches.
  Raw articles, images, and compiled wiki pages should be assumed publicly
  readable once pushed.

Sprint 1 status:

- Root Git repository initialized.
- `main` pushed to GitHub.
- `baseline/notion-github-start` pushed as rollback tag.
- Local tests passed before push.

## Sprint 2 Status

- Started: Notion schema creation via `notion_schema.py`.
- Schema created and verified in Notion.
- Existing `Export via Reader` database is the Raw Sources database.
- Script creates/reuses a control page and child schema databases.

## Sprint 2 - Notion Raw Source Schema

Objective: make Notion the online capture and review layer for raw articles and
images without replacing GitHub as the durable source of truth.

Deliverables:

- Define Notion databases: Raw Sources, Wiki Pages, Claims/Evidence, Ops Log.
- Map required properties to local frontmatter and sync manifests.
- Add schema validation before pushing to Notion.
- Add dry-run mode that prints intended Notion writes without external changes.
- Add fixture-based tests for representative article metadata and image fields.

Measurable outcomes:

- A schema check reports all required Notion properties before sync.
- A dry-run for 3 fixture articles reports create/update/skip decisions.
- Test fixtures cover article with cover image, article with inline images, and
  article with no content.
- No external Notion write happens during tests.

Rollback:

- Notion changes are limited to a test database until approved.
- Every pushed page records source file path and Reader document ID for cleanup.
- Use Notion database filters to archive pages from a single test run.

## Sprint 3 - Readwise/Notion to GitHub Capture Bridge

Objective: make capture idempotent from Readwise/Notion into local markdown and
assets that can be committed to GitHub.

Deliverables:

- A manifest maps Reader ID, Notion page ID, markdown path, and asset paths.
- Capture code skips already-seen sources unless content changed.
- Image downloads are content-addressed or uniquely named and path-checked.
- New sources land as raw files first; wiki compile happens as a separate step.

Measurable outcomes:

- Running capture twice against the same fixtures creates no duplicate files.
- Deleted local image fixture is detected and restored or reported.
- Manifest diff shows exactly what changed.
- Network sync has a dry-run and a max-item limit for safe testing.

Rollback:

- Revert the manifest and files in the same Git commit.
- Keep raw capture commits separate from wiki compilation commits.

## Sprint 4 - Wiki Compile and Query Quality Gate

Objective: make the compiled wiki reliable as the agent-facing knowledge layer.

Deliverables:

- Define query use cases for saved articles, companies, themes, and comparisons.
- Add link-health checks for `[[topics/...]]` and `[[concepts/...]]`.
- Add source-coverage checks for each topic page.
- Add a recurring unclassified-source review checklist.
- Update `schema.md` only with logged rationale.

Measurable outcomes:

- Every topic in `INDEX.md` resolves to an existing file.
- Every source referenced by a topic exists.
- At least 5 canonical queries have expected source/topic coverage.
- `wiki/log.md` and `docs/sprints/RUN_LOG.md` both record compile runs.

Rollback:

- Compile outputs are committed separately from raw source changes.
- Revert a bad compile commit without losing raw captures.

## Sprint 5 - Publish Compiled Wiki Back to Notion

Objective: publish the durable wiki layer into Notion for browsing while keeping
GitHub as the versioned source of truth.

Deliverables:

- Notion Wiki Pages database mirrors `sources/articles/wiki/`.
- Relations connect Wiki Pages to Raw Sources and Claims/Evidence.
- Publish script is idempotent and updates existing pages by stable ID.
- Ops Log records every publish run.

Measurable outcomes:

- Publishing the same wiki twice produces zero duplicate Notion pages.
- A sample topic page in Notion links back to its source article pages.
- A failed publish can be retried from the same manifest.

Rollback:

- Use run ID metadata to archive only pages created by a bad publish.
- Revert the Git commit that produced the published wiki state.

## Sprint 6 - Automation and Observability

Objective: make the system maintainable without silent failures.

Deliverables:

- Scheduled or manually triggered sync workflow.
- Per-run logs for capture, compile, test, and publish.
- Failure summary with counts, skipped items, and retry instructions.
- Health check command suitable for local and CI runs.

Measurable outcomes:

- A run produces one human-readable log and one machine-readable summary.
- Failed items are listed with source IDs and reasons.
- CI or local test command catches broken links and unsafe credentials.

Rollback:

- Disable automation without deleting local data.
- Keep each automation run isolated by run ID.

## Definition of Done for Every Sprint

- Scope is documented before implementation.
- Acceptance tests are listed and run.
- Results are logged in `docs/sprints/RUN_LOG.md`.
- External writes require explicit user approval.
- Changes are small enough to revert in one commit once Git is initialized.
