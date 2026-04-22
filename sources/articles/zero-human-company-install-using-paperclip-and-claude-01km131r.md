---
title: "Zero human company install using Paperclip and Claude"
reader_id: "01km131r6kbd1s9k1hzpyszmqz"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01km131r6kbd1s9k1hzpyszmqz"
source_url: "https://x.com/i/status/2034224042023239773/?rw_tt_thread=True"
author: "Nick Spisak"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-18"
saved_at: "2026-03-18"
reading_time: "4 mins"
summary: "Paperclip is a free tool that organizes AI coding agents into a virtual company with roles, budgets, and goals. It helps users manage many agents easily and prevents losing work or overspending. You can set it up quickly and control everything from one dashboard on your computer or phone."
content_hash: "aeca556dbdc55b7f9ca109be51ef167c076caf01e71234873a4470f6fc4e0a3a"
---

Zero human company install using Paperclip and Claude

Your browser does not support the video tag.

![](https://pbs.twimg.com/profile_images/1614514579098275840/6dgPShU3.jpg)

[Nick Spisak](<https://twitter.com/NickSpisak_>) [@NickSpisak_](<https://twitter.com/NickSpisak_>)

[ ](<https://twitter.com/NickSpisak_/status/2033518072724705437>)

![How to build a company run entirely by AI agents \(free, open source, 5-minute setup\)](https://pbs.twimg.com/media/HDiB4w1XAAAt8xi.jpg)

If you use Claude Code, OpenClaw, Codex, OpenCode, Cursor, or any other AI coding agent - Paperclip was built for you.

It's a free, open-source tool that just launched on GitHub and hit 1.6 million views in its first week. It takes every AI agent you already use and organizes them into an actual company - with an org chart, job titles, budgets, goals, and one dashboard to manage all of them.

You're already using the workers. Paperclip gives them a company to work in.

Real quick ...

If you're non-technical and want to learn how to build systems like this, join our Build With AI community:<http://return-my-time.kit.com/1bd2720397>

## Here's everything it does and exactly how to get started...

## The Problem It Solves

Right now you probably have Claude Code in one terminal, maybe Codex in another, Cursor open somewhere else. You're copying outputs between them. You lose track of who's doing what. Your computer restarts and you lose everything.

Paperclip fixes all of that. Every agent gets a role, a boss, and a budget. Tasks persist across reboots. And you can check on everything from your phone.

Created by @dotta. Completely open source under the MIT license. No account required. No subscription. Self-hosted on your own machine.

## The 8 Features That Matter Most

  1. **Org Charts** \- Your AI Company Has a Structure



You create roles just like a real company. CEO, CTO, engineers, designers, marketers. Each agent gets a title, a job description, and a boss they report to. This isn't cosmetic - the reporting structure determines how work flows between agents.

  2. **Goal Alignment** \- Every Task Connects to the Mission



You set one big company goal (like "Build an AI note-taking app to $1M MRR"). That goal breaks into projects. Projects break into tasks. Every agent working on a task can see exactly why it matters - not just what to do, but what the bigger picture is.

  3. **Heartbeats** \- Agents Work on a Schedule



Agents don't run 24/7 burning money. They wake up on a schedule (called a "heartbeat"), check if there's work to do, do it, and go back to sleep. You control how often each agent checks in. This keeps costs predictable.

  4. **Budget Controls** \- No More Surprise Bills



Every agent gets a monthly spending limit. When they hit it, they stop. Period. Paperclip tracks every dollar spent on AI tokens in real time. You'll never wake up to a $300 surprise bill because an agent got stuck in a loop.

  5. **Ticket System** \- Every Decision Has a Paper Trail



All work happens through tickets. Every conversation is threaded. Every tool call is traced. Every decision is logged. If something goes wrong, you can trace back exactly what happened, when, and why.

  6. Works With the **Tools You Already Use**



Paperclip doesn't lock you into one AI provider. It works with Claude Code, OpenClaw, Codex, OpenCode, Cursor, plain Bash scripts, or any agent that can receive a signal over HTTP. You can even mix and match - your CEO agent could run on Claude while your engineering agents run on Codex. Paperclip doesn't care. It just organizes them into a team.

  7. **Multi-Company Support**



One Paperclip installation can run multiple companies. Each one has completely separate data, separate budgets, and separate audit trails. If you want to run an AI marketing agency and an AI SaaS company at the same time, one dashboard handles both.

  8. **Governance** \- You're the Board of Directors



You approve hires. You review strategy changes. You can pause or shut down any agent at any time. Configuration changes are versioned, so if something breaks, you can roll it back. You stay in control.

## How to Set It Up (5 Minutes)

The One-Command Method

Open your terminal and run:


    npx paperclipai onboard --yes


That's it. Paperclip installs, creates a database automatically, and launches a dashboard at [http://localhost:3100](<http://localhost:3100/>). No separate database setup needed.

The Manual Method

If you prefer to do it step by step:


    git clone <https://github.com/paperclipai/paperclip.git>
    cd paperclip
    pnpm install
    pnpm dev


Requirements: Node.js 20+ and pnpm 9.15+.

What Happens Next

Once the dashboard is running:

  1. You'll create your first company and set the mission
  2. You'll hire your first agent (it starts with a CEO)
  3. The CEO will recommend hiring more agents (like a coder)
  4. You approve the hires and set budgets
  5. Agents start working on tasks toward your goal



You manage everything from the dashboard. On your laptop or your phone.

## What's Coming Next: ClipMart

The team is building ClipMart - a marketplace where you can download entire pre-built companies with one click. Imagine browsing a template library: marketing agency, SaaS builder, content studio. Pick one, import it into Paperclip, and you have a fully staffed AI company ready to go.

This hasn't launched yet, but it's on the roadmap.

## Who This Is For

Paperclip isn't for someone who uses one AI tool for one task. It's for people who are already running multiple agents and need a way to coordinate them.

If you've ever had 10+ Claude Code terminals open and lost track of what each one was doing, this is your answer. If you've ever had an AI agent burn through $200 in tokens because nobody was watching, this is your answer.

One dashboard. One org chart. One budget system. Every agent accounted for.

## The GitHub repo is live. It's free. And it takes 5 minutes to set up.

**PS: If you like this starter pack, you'll love what's coming.**

**_I'm building a community where I break down exactly how to turn custom agents into a real employee: custom skills, scheduled workflows, and systems that run while you sleep._**

**_Join the waitlist here:<https://return-my-time.kit.com/1bd2720397>_**

[Posted Mar 16, 2026 at 12:17PM](<https://twitter.com/NickSpisak_/status/2033518072724705437>)
