---
title: "OpenClaw has 186K GitHub stars and 1.5M compromised API keys"
reader_id: "01khbvnqgnfvbmcavtvqeb21th"
notion_page_id: "34a4ebe7-f118-815d-94bf-f97d54fcd447"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01khbvnqgnfvbmcavtvqeb21th"
source_url: "https://x.com/i/status/2021943985216819419/?rw_tt_thread=True"
author: "Paweł Huryn"
site: "X (formerly Twitter)"
tags: []
published: "2026-02-12"
saved_at: "2026-02-13"
reading_time: "2 mins"
summary: "OpenClaw is popular but has serious security problems with leaked API keys. The author built a safer AI agent using strong sandboxing and strict permissions. This new tool runs securely, respects user control, and needs no coding to use."
content_hash: "989db57aec172c7626db5323c1ae3ef0f422d014b9f571b95f0511d2b36d5c0f"
---

OpenClaw has 186K GitHub stars and 1.5M compromised API keys. I needed a secure alternative.

So, I built it with n8n and Claude Opus 4.6.

It can already:



  * Reply to your Telegram messages


  * Access selected folders from your laptop


  * Access Gmail, Drive, Notion, Linear, etc.


  * Install new local tools in a sandbox


  * Run autonomously for hours


  * Create multiple subagents


  * Learn from experience


  * Wake up regularly



But, unlike OpenClaw, it:



  * Can't access your API keys


  * Can't modify its environment


  * Can't access folders you haven't shared


  * Can't access tools you haven't approved


  * Must get your confirmation, e.g., when sending emails



These aren’t prompt instructions. They’re hard architectural boundaries — Docker isolation, mounted folder permissions, n8n’s tool approval system.

Key components:

✅ The VPS on Hostinger hosts n8n and a sandbox container. Agents can also connect to my laptop's sandbox via a Claudeflare tunnel + Desktop Commander MCP.

✅ The Manager agent is the brain. It plans, decides, delegates, and talks to the user. It never touches files. It never runs scripts. It works entirely from executor summaries.

✅ The Executor agents are the hands. Each receives a task (what to do + why it matters), decides how to execute it, and reports back. They can install new tools and execute code only in their dedicated sandboxes.

✅ Data Tables in n8n store both memories and sessions — no external database, no vector store, no infrastructure. Just rows in a table. Turns out, that's enough.

Two memory types:



  * Manager memory: user preferences, facts, corrections, relationship, skills, context


  * Executor memory: what tools are installed, what’s broken, workarounds



✅ Sessions are short-term state for multi-step tasks. Original request, plan, assumptions, and what happened so far. When the Manager loops with fresh context, the session is all it gets. That's a Ralph Wiggum loop.

I've been using it for 5 days. And already can't imagine not having it on my phone.

What's next:



  * Heartbeat via Cron (a scheduled prompt)


  * Civic Nexus governance + MCPs


  * Supermemory integration


  * WhatsApp as an additional surface


  * Hardening



The architecture supports all of it.

OpenClaw proved people want personal AI agents.

It also proved that 'just trust the prompt' isn't a security model.

Docker isolation, mounted folder permissions, tool approval — none of this is new technology. It's just discipline.

You can easily do this even with n8n — no coding required.

* * *


Want to try it or read more?

More, what I learned, and a setup guide: productcompass[.]pm


Your browser does not support the video tag.
