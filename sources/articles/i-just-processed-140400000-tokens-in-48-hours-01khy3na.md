---
title: "I just processed 140,400,000 tokens in 48 hours"
reader_id: "01khy3nancac4cv8ra6b8ps8ah"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01khy3nancac4cv8ra6b8ps8ah"
source_url: "https://x.com/i/status/2024881546365112590/?rw_tt_thread=True"
author: "Ziwen"
site: "X (formerly Twitter)"
tags: []
published: "2026-02-20"
saved_at: "2026-02-20"
reading_time: "8 mins"
summary: "Ziwen processed over 140 million tokens in 48 hours using a self-hosted OpenClaw agent and only spent $50 instead of $1,677. He advises routing routine checks to a free local model to save costs and avoiding switching AI models mid-task to keep context. The key is to use a stable paid plan with fallback models for efficient, affordable AI work."
content_hash: "d594e3186414d83cce428de1987171337b279c356140f99a3166e858bc7cf418"
---

I just processed 140,400,000 tokens in 48 hours.

Raw API bill: $1,677.82

My actual cost: $50.00

I’m moving my entire life into a self-hosted OpenClaw agent.

If you aren't using this "cheat code" setup, you're just donating money to Big Tech.

The 30x leverage setup:

  * Flat-rate loophole: Stop paying per token. Hook OpenClaw into a flat-rate coding plan for heavy lifting.
  * Local heartbeats: OpenClaw pings 48×/day. Route these to a local Llama 3.2 via Ollama. Cost: $0.
  * The 2-agent rule: Killed my 9-agent fleet ($100/night money pit). One for code. One for ops.
  * Plan > chat: If you don't use a [ https://t.co/3gN0tX6fNj ](<https://t.co/3gN0tX6fNj>) , you’re just burning cash in a chat box.



I burned $100 in one night so you don't have to.

The Day 1 manual for infinite scale:

![](https://pbs.twimg.com/profile_images/2009704432674426880/Q29hAGJR.jpg)

[ Ziwen ](<https://twitter.com/ziwenxu_>) [ @ziwenxu_ ](<https://twitter.com/ziwenxu_>)

[ ](<https://twitter.com/ziwenxu_/status/2024682444335497220>)

![10 Things I Wish I Knew Before Using OpenClaw](https://pbs.twimg.com/media/HBkcd1kWIAADBoc.jpg)

OpenClaw is a god-tier AI Assistant, but it’s a double-edged sword. I’ve burned over $100 in a single night and spend the time to learn so you don’t have to.

If you’re moving your life into a self-hosted agent, you need a strategy, not just an API key. This is the Day 1 manual I wish someone had handed me.

**1\. Localize Your Heartbeat (Save Your Budget)**

By default, your agent "wakes up" every 30 minutes to check for tasks. That’s 48 API calls a day even if you're doing absolutely nothing. If you are paying raw API rates for those checks, you are literally burning cash while you sleep.

  * **The Fix:** The _very first thing_ you should do after installing OpenClaw is set up your own Local LLM specifically for heartbeats. Or leave your heartbeats to empty.
  * **The Pro Move:** Install Ollama and pull a lightweight model like llama3.2:1b. It only takes up about 1.3GB of space, runs 100% offline, and costs exactly zero dollars.
  * **The Setup:** Tell OpenClaw to route all routine heartbeat checks to your local llama3.2:1b instance. Save your expensive, premium API tokens for the actual heavy-lifting coding tasks. And as a general rule, keep your [ HEARTBEAT.md ](<http://HEARTBEAT.md/>) file empty unless you have an active automation running.



**2\. Stop "Model-Hopping" (And Dodging Rate Limits)**

"Free API credits" from Google AI or Anthropic sound like a cheat code, and switching models mid-chat with /model feels like a superpower. In reality, it’s a massive trap that will ruin your context—and probably get you banned.

  * **The Trap (Free Tier Bans):** Free tiers have incredibly low rate limits designed for humans. OpenClaw is an agent; it fires massive bursts of prompts to check skills, read files, and think. If you hook OpenClaw up to a free Gemini or Claude tier, you will hit the rate limit in 5 minutes, and providers _will_ ban or suspend your API key for abuse.
  * **The Problem:** Every time you hit a limit and manually switch models to keep working, you break the "vibe." Different models process context differently, and mid-task switching causes severe context rot.
  * **The Fix:** Upgrade to a stable paid tier. Pick one "Brain" (Claude 3.5 Sonnet) and one "Worker" (Gemini Flash). Stick to them.
  * **The Hack:** Stop manually switching. Set up **fallback models** in your config. If your primary API hangs or rate-limits, OpenClaw automatically swaps to the backup in the background so you never lose your flow.



[ Posted Feb 20, 2026 at 3:08AM ](<https://twitter.com/ziwenxu_/status/2024682444335497220>)
