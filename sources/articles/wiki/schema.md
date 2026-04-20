# Wiki Schema

This file defines the structure and conventions for this knowledge base wiki. It is generated on first compile and co-evolved between human and LLM on subsequent runs.

**Human:** You can edit this file to rename topics, merge them, add conventions, or change the article structure. The compiler will respect your changes on the next run.

**Compiler:** Read this file before classifying sources. Follow its conventions. Add new topics here when discovered. Never remove topics without human approval.

## Topics

- `anthropic-strategy`: Anthropic's compute procurement, enterprise growth, model releases (Mythos), and strategic positioning
- `openai-strategy`: OpenAI's Frontier platform, enterprise aggregation, TBPN acquisition, and competitive positioning
- `apple`: Apple's 50-year hardware/software integration thesis, satellite strategy, and AI access point positioning
- `ai-lab-competition`: Competitive dynamics between OpenAI, Anthropic, Google, and Meta — compute race, model releases, distillation attacks
- `ai-security`: NPM supply chain attacks, Claude Code source map leak, AI-powered offensive security (Project Glasswing)
- `ai-industry-economics`: European VC funding trends, compute opportunity cost framework, aggregation economics in AI
- `media-publishing`: NYT's human-expertise bet, The Athletic acquisition, AI licensing strategy, journalism vs. AI-generated content
- `claude-code-tools`: Claude Code extension architecture (CLAUDE.md, subagents, hooks, MCP), CCA certification, enterprise adoption
- `ai-literacy`: Core AI vocabulary — tokens, context window, temperature, hallucination, RAG — for non-technical practitioners
- `product-management-ai`: PM role transformation from 638-voice analysis: evals, NLX design, prototyping fluency as net-new competencies
- `ai-craft-quality`: Vibe coding critique, slop economics, Minimum Viable Precision, craft vs. convenience argument
- `snowflake-data`: Snowflake's 7 database type taxonomy, architect decision framework, Native Apps via Streamlit/Snowpark

## Concepts

Cross-cutting patterns that span 3+ topics. Interpretive, not just factual.

- `compute-as-strategic-moat`: The shift from marginal cost to opportunity cost framing for GPU capacity; compute access as positional advantage with a closing window — connects [anthropic-strategy, openai-strategy, ai-lab-competition, ai-industry-economics]
- `craft-vs-speed`: Speed is table stakes; craft is the differentiator — quality-differentiated work becoming the growth strategy as AI lowers barriers to shipping — connects [ai-craft-quality, product-management-ai, media-publishing, claude-code-tools]
- `aggregation-theory-applied`: Thompson's Aggregation Theory applied to AI — demand aggregators (enterprises, devices) capture margin as models commoditize — connects [apple, openai-strategy, anthropic-strategy, ai-industry-economics]

## Article Structure

Each topic article follows this format:
- **Summary** [coverage] — standalone briefing, 2-3 paragraphs
- **Key Thesis** [coverage] — central argument or claim the author makes
- **Key Insights** [coverage] — 3-5 concrete takeaways
- **Industry Context** [coverage] — where this fits in the broader tech/AI landscape
- **Implications** [coverage] — what practitioners and builders should act on
- **Sources** — backlinks to every contributing raw file

Coverage tags: `[coverage: high -- N sources]`, `[coverage: medium -- N sources]`, `[coverage: low -- N sources]`

## Naming Conventions

- Topic slugs: lowercase-kebab-case (e.g., `anthropic-strategy`, `ai-craft-quality`)
- Files: `{topic-slug}.md` in `topics/`, `{concept-slug}.md` in `concepts/`
- Dates: YYYY-MM-DD format everywhere
- Links: Obsidian `[[wikilinks]]` with relative paths from `topics/` or `concepts/`

## Unclassified Sources

- `untitled.md` — no usable content (empty stub from León.Stop); skipped
- `karthik-vinay-kumar-adari.md` — LinkedIn post on staffing firms; thin content, no standalone topic warranted

## Evolution Log

- 2026-04-16: Initial schema generated from 12 topics, 3 concepts (20 source files scanned, 18 classified)
