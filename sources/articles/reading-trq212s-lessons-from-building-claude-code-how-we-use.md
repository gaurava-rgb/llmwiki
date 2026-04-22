---
title: "Reading @trq212's \"Lessons from Building Claude Code: How We Use..."
reader_id: "01km13azcsxfeb0bx7e5mym03v"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01km13azcsxfeb0bx7e5mym03v"
source_url: "https://x.com/i/status/2034075011779109088/?rw_tt_thread=True"
author: "Muratcan Koylan"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-18"
saved_at: "2026-03-18"
reading_time: "2 mins"
summary: "Muratcan Koylan improved his open-source Agent Skills repo by making skills more practical and usable for AI agents like Claude. He added clear instructions, Gotchas sections, and composable code to help agents perform tasks better. The repo aims to teach context engineering as a skill set, not just provide tools, benefiting AI developers worldwide."
content_hash: "073217841c0fd9c26014c5616ae90df99de254efec1dd46b751e357fe081f5cb"
---

Reading [@trq212](<https://twitter.com/trq212>)'s "Lessons from Building Claude Code: How We Use Skills" made me rewrite my entire skills repository.

I maintain Agent Skills for Context Engineering, an open-source collection of 13 agent skills. It's been cited in peer-reviewed research and has contributors from around the world.

Skills in the repo were "textbooks"; they taught Claude about context engineering. Anthropic and some other industry research suggest that the best skills are "toolboxes," they help Claude do things.

The article also says the highest-signal content in any skill is the Gotchas section.

The scripts were reference implementations you'd read and learn from, but we need to give Claude composable code that it can actually import and use at runtime.

What we changed (v2.0):

  * Rewrote all 13 skills from descriptive ("X is Y") to hybrid instructional voice ("Do X because Y")
  * Added Gotchas sections to every skill (5-9 per skill, experience-derived, specific, actionable)
  * Made all 12 Python scripts composable: **all** exports, type hints, "Use when:" docstrings, **main** demo blocks
  * Added progressive disclosure triggers to all References ("Read when: [specific condition]")
  * Updated the skill template so every future skill gets Gotchas by default



So it's now a Context Engineering Skills repo that Claude, Codex, Cursor, OpenCode can actually use, instead of just reading and learning from it.

You will likely find the updated version more helpful. Let me know if you have any feedback.

![](https://pbs.twimg.com/profile_images/2017468785473548288/43nF1d1X.jpg)

[Muratcan Koylan](<https://twitter.com/koylanai>) [@koylanai](<https://twitter.com/koylanai>)

[ ](<https://twitter.com/koylanai/status/2002797649842331919>)

I’m excited to share a new repo: **Agent Skills for Context Engineering**

Instead of just offering a library of black-box tools, it acts as a "Meta-Agent" knowledge base. It provides a standard set of skills, written in markdown and code, that you can feed to an agent so it understands how to manage its own cognitive resources.

<https://t.co/vWwrYPAd8k>

Most agent failures are not model failures; they are context failures. This is still an experimental project. The goal is to establish a platform-agnostic standard for context engineering that can be used in Cursor, Claude Code, Copilot or Codex.

skills/

context-fundamentals: _What context is, why it matters_

context-degradation: _How context fails (lost-in-middle, poisoning)_

context-optimization: _Compaction, masking, caching_

multi-agent-patterns: _Orchestrator, swarm, hierarchical_

memory-systems:_Vector RAG, knowledge graphs, Zep_

tool-design: _Building tools agents can use_

evaluation: _Testing and measuring agent systems_

I believe this is a good start, showing developers how to approach context engineering rather than relying on ready-made tools.

You will also find the aggregated research documents I used to build these skills in the repo. The skills are synthesized from technical blogs on context and prompt engineering that I bookmarked, AI Labs' documentations, and Anthropic Skills examples.

Try the 7 Skills, created using Antrhopic's Skills template format. Experiment with the provided scripts and references, and feel free to contribute to the repo.

![](https://pbs.twimg.com/profile_images/1961793099031527424/Nt1ZvaJe.jpg)

[Muratcan Koylan](<https://twitter.com/koylanai>) [@koylanai](<https://twitter.com/koylanai>)

[ ](<https://twitter.com/koylanai/status/2002646195684991268>)

It’s actually a good question; the difference is subtle but structural.

I usually frame it like this:

AGENTS[.]md acts as the declarative context. You write this for every repo (and nested directories) to define the project structure, persona, and coding rules.

Skills are the functional protocols. They provide the agent with modular capabilities like advanced tool-use and multi-step chaining that are dynamically discovered only when needed.

If AGENTS[.]md defines the identity and environment (the body), Skills provide the specialized toolset (the capabilities) used to execute tasks autonomously.

![](https://pbs.twimg.com/profile_images/1656519795976687619/abuB5K8p.jpg)

[Adam Azzam](<https://twitter.com/AAAzzam>) [@AAAzzam](<https://twitter.com/AAAzzam>)

[ ](<https://twitter.com/AAAzzam/status/2002459788777783619>)

Okay I'll bite - what's the difference between [AGENTS.md](<http://AGENTS.md/>) and skills?

[Posted Dec 20, 2025 at 7:23PM](<https://twitter.com/AAAzzam/status/2002459788777783619>) [Posted Dec 21, 2025 at 7:43AM](<https://twitter.com/koylanai/status/2002646195684991268>)

[Posted Dec 21, 2025 at 5:45PM](<https://twitter.com/koylanai/status/2002797649842331919>)
