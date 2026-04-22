---
title: "Holy shit… Your anonymous internet identity can now be unmasked..."
reader_id: "01kjcyfnevg6xhx4dp6nbqnavv"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kjcyfnevg6xhx4dp6nbqnavv"
source_url: "https://x.com/i/status/2026951395753213970/?rw_tt_thread=True"
author: "Alex Prompter"
site: "X (formerly Twitter)"
tags: []
published: "2026-02-26"
saved_at: "2026-02-26"
reading_time: "2 mins"
summary: "New research shows that AI can reveal the real identities behind anonymous internet posts with high accuracy and low cost. This method works automatically, using tools like ChatGPT to link users to their online profiles. As AI gets better, staying truly anonymous online is becoming nearly impossible."
content_hash: "013a84961055d52715082c18c0edb42b41cee5e5dcae7d8236639d9452b9fe15"
---

Holy shit… Your anonymous internet identity can now be unmasked for $1 😳

![😳](https://abs-0.twimg.com/emoji/v2/svg/1f633.svg)

Not by the FBI. By anyone with access to Claude or ChatGPT and a few of your Reddit comments.

ETH Zurich and Anthropic just dropped a paper called “Large-Scale Online Deanonymization with LLMs” and the results are the most alarming privacy research I’ve read this year.

They built an automated pipeline that takes your anonymous posts, extracts identity signals, searches the web, and figures out who you are.

No human investigator needed. Fully autonomous. Works on Hacker News, Reddit, LinkedIn, even redacted interview transcripts.

Here’s how bad the numbers are.

On Hacker News users: 67% identified correctly.

When the system made a guess, it was right 90% of the time.

On Reddit academics posting under pseudonyms: 52%.

On scientists whose interview transcripts were explicitly redacted for privacy: 9 out of 33 still got unmasked.

The pipeline works in four steps they call ESRC. Extract identity signals from your posts using LLMs.

Search for candidate matches using embeddings across thousands of profiles.

Reason over top candidates with models like GPT-5.2. Calibrate confidence so when it does guess, it’s almost never wrong.

The classical deanonymization method from the famous Netflix Prize attack? Nearly 0% recall across every test.

LLMs didn’t just improve on old techniques. They made old techniques look like toys.

When they scaled to temporally split Reddit profiles, matching a user’s old posts to their newer ones across a full year gap, the pipeline hit 67% recall at 90% precision and 38% recall at 99% precision.

Meaning even a year of changed interests and different conversations wasn’t enough to hide.

More reasoning compute = better deanonymization. High reasoning effort doubled recall at 99% precision in some tests. As frontier models get smarter, this attack strengthens automatically. Every model upgrade is a privacy downgrade.

What makes it nearly impossible to defend against: the pipeline splits into subtasks that all look benign. Summarize a profile.

Compute embeddings. Rank candidates. No single API call screams “deanonymization.” The researchers themselves say they’re pessimistic that safety guardrails or rate limits can stop it.

Their conclusion is blunt: “Users who post under persistent usernames should assume that adversaries can link their accounts to real identities.” And it extrapolates.

Log-linear projections suggest roughly 35% recall at 90% precision even at one million candidates.

Every throwaway account. Every anonymous forum post. Every “nobody will connect this to me” comment.

It’s all searchable micro-data now. And the cost to run the full agent on one target is less than a cup of coffee.

Practical anonymity on the internet just died. The paper killed it with math.

* * *

TL;DR:

LLMs can now unmask your anonymous accounts. 67% accuracy, 90% precision, $1-4 per target.

Classical methods scored nearly 0%. LLMs turned a theoretical privacy attack into something anyone can run from an API.

Your Reddit throwaways. Your anonymous forum accounts. Your

![Image](https://pbs.twimg.com/media/HCEtkRTagAAoZI7.jpg?name=orig)

* * *

Full paper: [arxiv.org/pdf/2602.16800](<https://arxiv.org/pdf/2602.16800>)

* * *

Your premium AI bundle to 10x your business

→ Prompts for marketing & business

→ Unlimited custom prompts

→ n8n automations

→ Weekly updates

Start your free trial👇

[godofprompt.ai/complete-ai-bu…](<https://godofprompt.ai/complete-ai-bundle>)
