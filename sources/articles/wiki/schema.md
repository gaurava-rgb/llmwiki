# Wiki Schema

This file defines the structure and conventions for this knowledge base wiki. It is generated on first compile and co-evolved between human and LLM on subsequent runs.

**Human:** You can edit this file to rename topics, merge them, add conventions, or change the article structure. The compiler will respect your changes on the next run.

**Compiler:** Read this file before classifying sources. Follow its conventions. Add new topics here when discovered. Never remove topics without human approval.

## Topics

- `anthropic-strategy`: Anthropic's enterprise coding wedge, Claude product line, TPU supply, and trust posture.
- `openai-strategy`: OpenAI's platform expansion, ChatGPT monetization, Microsoft tension, and Frontier ambitions.
- `apple`: Apple's AI strategy through integration, device distribution, Siri, Vision Pro, and platform control.
- `ai-lab-competition`: The wider competitive field around AI labs: hyperscalers, chips, clouds, China, and supply chains.
- `ai-security`: Prompt injection, exploit generation, source leaks, and operational risk around AI tooling.
- `ai-industry-economics`: Funding, valuation, pricing, ads, aggregation, and business-model structure in AI.
- `media-publishing`: Streaming, creators, journalism, and the interaction between AI abundance and trusted media.
- `claude-code-tools`: Claude Code, Cowork, Codex/OpenClaw comparisons, MCP, skills, memory, and workflow design.
- `ai-literacy`: Operational AI vocabulary: models, apps, harnesses, limits, and practical tool selection.
- `product-management-ai`: How PM work shifts under AI: evals, prototyping, adoption, and judgment.
- `ai-craft-quality`: Vibe coding, slop, design systems, taste, and quality as a differentiator.
- `snowflake-data`: Snowflake and the data-architecture layer underneath AI workflows.
- `ai-agent-workflows`: Agent orchestration, automation loops, memory, and harness design.
- `open-source-ai-builder-stack`: GitHub repos, local tools, OCR, voice, CLI/browser tooling, and open-source builder leverage.
- `knowledge-systems`: Readwise, Obsidian, knowledge graphs, NotebookLM, and externalized memory systems.
- `ai-learning-careers`: Learning loops, roadmaps, jobs, student leverage, and career signal-building in the AI era.
- `personal-systems-and-execution`: Attention, ADHD, listening, questions, and the personal operating systems behind consistent work.
- `quant-finance-and-markets`: Fundamental analysis, quant prep, prediction markets, bitcoin, and finance research workflows.
- `startup-growth`: Distribution, bootstrapping, creator channels, AI content factories, and founder operating choices.
- `builder-feed-notes`: A high-volume short-form radar topic for fast-moving builder notes, demos, and tactics.
- `general-tech-essays`: Long-form overflow essays and adjacent tech/business material awaiting sharper topicization.

## Concepts

Cross-cutting patterns that span 3+ topics. Interpretive, not just factual.

- `compute-as-strategic-moat`: Compute access and allocation as the binding strategic constraint across labs, clouds, and products.
- `craft-vs-speed`: AI lowers the cost of shipping, which increases the value of quality judgment and finish.
- `aggregation-theory-applied`: Distribution owners and demand aggregators capture outsized leverage over upstream capability providers.
- `agentic-compounding`: Agents improve when context, skills, memory, and tools persist between runs.
- `learning-loop-as-moat`: Fast learn-build-test-revise cycles become a durable advantage when AI accelerates iteration.

## Article Structure

Each topic article follows this format:
- **Summary** [coverage] — standalone briefing of the topic and why it matters now
- **Key Thesis** [coverage] — the central argument that best explains the cluster
- **Key Insights** [coverage] — 3-5 concrete takeaways from the source set
- **Industry Context** [coverage] — how the topic fits into the wider market or workflow landscape
- **Implications** [coverage] — what to do, watch, or change
- **Sources** — backlinks to every contributing raw file

Coverage tags remain qualitative: use **high** for broad, coherent coverage; **medium** for narrower or more heterogeneous coverage; **low** when the topic is still thin.

## Naming Conventions

- Topic slugs: lowercase-kebab-case
- Topic files live in `topics/` and concept files live in `concepts/`
- Dates use YYYY-MM-DD format
- Links use Obsidian-style wikilinks

## Unclassified Sources

- None in this rebuild; the schema now includes explicit overflow buckets for short-form builder notes and adjacent long-form essays.

## Evolution Log

- 2026-04-16: Initial schema generated from 12 topics, 3 concepts (20 source files scanned, 18 classified)
- 2026-04-22: Full rebuild from 750 raw sources. Kept the original topic set, refreshed all existing topics, and added ai-agent-workflows, open-source-ai-builder-stack, knowledge-systems, ai-learning-careers, personal-systems-and-execution, quant-finance-and-markets, startup-growth, builder-feed-notes, and general-tech-essays. Added concepts agentic-compounding and learning-loop-as-moat.
