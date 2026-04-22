---
title: "The backstory on Superpowers is wild"
reader_id: "01km13ap99jmpe1270actp5xhr"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01km13ap99jmpe1270actp5xhr"
source_url: "https://x.com/i/status/2034118864313725242/?rw_tt_thread=True"
author: "Aakash Gupta"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-18"
saved_at: "2026-03-18"
reading_time: "2 mins"
summary: "Jesse Vincent created Superpowers, a system that helps AI coding agents work carefully and follow strict steps. It stops the AI from guessing, makes detailed plans, enforces testing, and produces reliable code. Superpowers quickly gained huge popularity because it solves the main problem in AI coding: lack of discipline."
content_hash: "e725efcbb4f23e2aafb2891811f9fdfd2106437bf0be460ddea8ebd9fa44405f"
---

The backstory on Superpowers is wild.

Jesse Vincent created Request Tracker in 1994. It became the most widely used open-source ticket tracking system on Earth. Then he ran the Perl programming language for three years. Then he co-founded Keyboardio and shipped custom ergonomic keyboards to 78 countries. Then he co-founded VaccinateCA during COVID and helped millions of Americans find vaccine appointments.

Every single one of those projects was about the same thing: building systems that help people organize complex work they can’t hold in their heads.

Now look at what he built. Superpowers makes your AI agent stop, ask what you’re actually building, write a spec in chunks small enough to read, break implementation into 2-5 minute tasks with exact file paths, and delete any code written before tests exist.

91,000 GitHub stars in five months. That’s 18,000 stars per month. For a repo that is literally just markdown files telling your coding agent to slow down.

The growth rate tells you something the AI labs don’t want to admit. The bottleneck in AI-assisted development right now is not model capability. The models are smart enough. The problem is they have zero discipline. They guess at specs, skip tests, and produce code you spend the next hour babysitting.

A guy who spent 30 years building systems for how humans organize work just built the system for how AI agents organize work. The career arc makes perfect sense in retrospect.

![](https://pbs.twimg.com/profile_images/2020520446500950016/jZ9Kdk79.jpg)

[Ihtesham Ali](<https://twitter.com/ihtesham2005>) [@ihtesham2005](<https://twitter.com/ihtesham2005>)

[ ](<https://twitter.com/ihtesham2005/status/2033679744219418710>)

🚨 Holy shit...A developer on GitHub just built a full development methodology for AI coding agents and it has 40.9K stars on GitHub.

It's called Superpowers, and it completely changes how your AI agent writes code.

Right now, most people fire up Claude Code or Codex and just… let it go. The agent guesses what you want, writes code before understanding the problem, skips tests, and produces spaghetti you have to babysit.

Superpowers fixes all of that.

Here's what happens when you install it:

→ Before writing a single line, the agent stops and brainstorms with you. It asks what you're actually trying to build, refines the spec through questions, and shows it to you in chunks short enough to read.

→ Once you approve the design, it creates an implementation plan so detailed that "an enthusiastic junior engineer with poor taste and no judgement" could follow it.

→ Then it launches subagent-driven development. Fresh subagents per task. Two-stage code review after each one (spec compliance, then code quality). The agent can run autonomously for hours without deviating from your plan.

→ It enforces true test-driven development. Write failing test → watch it fail → write minimal code → watch it pass → commit. It literally deletes code written before tests.

→ When tasks are done, it verifies everything, presents options (merge, PR, keep, discard), and cleans up.

The philosophy is brutal: systematic over ad-hoc. Evidence over claims. Complexity reduction. Verify before declaring success.

Works with Claude Code (plugin install), Codex, and OpenCode.

This isn't a prompt template. It's an entire operating system for how AI agents should build software.

100% Opensource. MIT License.

[Posted Mar 16, 2026 at 11:00PM](<https://twitter.com/ihtesham2005/status/2033679744219418710>)
