---
title: "Agent Skills are everywhere - Claude Code, Gemini CLI, Codex..."
reader_id: "01khr9yrhbchsr79k221mnm02x"
notion_page_id: "34a4ebe7-f118-81fc-8577-c9e06df3611a"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01khr9yrhbchsr79k221mnm02x"
source_url: "https://x.com/i/status/2022409507826213048/?rw_tt_thread=True"
author: "Xiangyi Li"
site: "X (formerly Twitter)"
tags: []
published: "2026-02-13"
saved_at: "2026-02-18"
reading_time: "1 min"
summary: "Agent Skills help AI perform better in many tasks, especially when created by experts. Models struggle to generate their own Skills, so expert-made Skills improve results more than bigger models. SkillsBench is an open-source project that tests Skills across many domains and shows these findings."
content_hash: "1abeacc9d74f5600de5f6110fb3baa4910e3fcf814e7459e8991076088b0f658"
---

Agent Skills are everywhere - Claude Code, Gemini CLI, Codex all support them. But do they actually work?
105 domain experts from Stanford, CMU, Berkeley, Oxford, Amazon, ByteDance & more built SkillsBench to find that out.
86 tasks. 11 domains. 7,308 trajectories. 🧵👇

![](https://pbs.twimg.com/media/HBEKuqobUAApJck.jpg)

* * *

Every task is human-authored by domain experts - clinical data harmonization, manufacturing, financial analysis, robotic control, CTF challenges etc
322 submissions. 86 accepted. 26.7% acceptance rate. 100% human-verified and verifiable. No toy problems.

![](https://pbs.twimg.com/media/HBEKvoYbsAAshRX.jpg)

* * *

✅ Curated Skills: +16.2pp average improvement across all 7 agent configs
❌ Self-generated Skills: -1.3pp — models can't write their own procedural knowledge

Agents know that they need domain expertise. They just can't generate it.

* * *

Less is more:

• 2-3 focused Skills: +18.6pp
• 4+ Skills: +5.9pp
• Comprehensive docs: -2.9pp

And Skills substitute for model scale — Haiku 4.5 with Skills (27.7%) beats Opus 4.5 without (22.0%).

The right procedural knowledge can be worth more than a bigger model.

* * *

SkillsBench is fully open-source.

📄 Blog and paper: [skillsbench.ai/blogs/introduc…](<https://www.skillsbench.ai/blogs/introducing-skillsbench>)
💻 Code: [github.com/benchflow-ai/s…](<http://github.com/benchflow-ai/skillsbench>)
🌐 Website: [skillsbench.ai](<http://skillsbench.ai/>)

Massive thanks to all 41 co-authors and 105 contributors who made this possible.
