---
title: "The most in-demand skill in AI just shifted, and most..."
reader_id: "01kmnwjtdxwtnzcj178zp82mj0"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kmnwjtdxwtnzcj178zp82mj0"
source_url: "https://x.com/i/status/2037059475375624343/?rw_tt_thread=True"
author: "Aakash Gupta"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-26"
saved_at: "2026-03-26"
reading_time: "3 mins"
summary: "The most important skill in AI now is writing clear instructions for AI agents, called program.md files. This skill controls how well the AI experiments improve results, making it more valuable than coding itself. Companies that master this will gain the biggest advantage in AI development."
content_hash: "3fbab1a42f282d4fc3a5b3707707e9154fa9cc4126f5789f58ab291465046b84"
---

The most in-demand skill in AI just shifted, and most people won't notice for two years.

Autoresearch has three files. [program.md](<http://program.md/>) is the only one the human writes. It contains research directions, constraints, and goals in plain English. The agent reads it, forms hypotheses, writes code, runs experiments, evaluates results, and iterates. 700 times in 2 days during Karpathy's first run.

[program.md](<http://program.md/>) is a new kind of artifact. It reads like a strategy memo, but it functions as executable software. The quality of the directions you write determines the quality of the experiments the agent runs. Vague constraints produce scattered results. Precise constraints with clear evaluation criteria produce the 20 improvements out of 700 that Karpathy kept.

This maps to a skill that already exists but has never been the bottleneck: writing the brief.

In advertising, the brief is the single page that determines whether a $10 million campaign produces results or waste. Agencies with world-class creative departments still fail when the brief is weak. The brief writer has always been undervalued because the visible work happened downstream.

In product management, the PRD serves the same function. Teams with strong engineers ship mediocre products when the spec is vague. The spec writer is the constraint that determines output quality, but the engineer gets the credit because the code is the visible artifact.

Autoresearch makes this dynamic explicit and measurable. Karpathy can see exactly which [program.md](<http://program.md/>) instructions produced improvements and which produced noise. The feedback loop between brief quality and outcome quality is 5 minutes long instead of 6 months.

Shopify's CEO pointed the same architecture at an internal model. 37 experiments overnight. 19% quality gain. The variable was the directions he wrote, not the compute, not the model size, not the framework.

Every company deploying AI agents will discover this same bottleneck. The person who can write a precise, well-constrained [program.md](<http://program.md/>), whether they call it a prompt, a spec, a PRD, or a research direction, becomes the highest-leverage role on the team. The execution layer is now infinite. The strategy layer is still scarce.

Karpathy called this "engineering your agents." The job title that emerges from it will be something nobody's coined yet. The skill underneath it is the oldest one in management: writing a clear brief.

![](https://pbs.twimg.com/profile_images/2021355466216062976/8MDXp7vR.jpg)

[Aakash Gupta](<https://twitter.com/aakashgupta>) [@aakashgupta](<https://twitter.com/aakashgupta>)

[ ](<https://twitter.com/aakashgupta/status/2034851259442749909>)

For $25 and a single GPU, you can now run 100 experiments overnight without designing any of them.

Karpathy open-sourced autoresearch. 42,000 GitHub stars in a week. Fortune called it "The Karpathy Loop."

Every article about it focused on the ML angle. They all missed the bigger story. The pattern underneath works on anything you can score with a number. Ad copy, cold emails, video scripts, job posts, skill files.

Three files. One the agent edits. One it can never touch. One instruction file from you. Each cycle takes 5 minutes. Score went up? Git commit. Score went down? Git reset. Twelve cycles per hour. A hundred overnight.

Karpathy ran it on code he'd already optimized by hand for months. The agent found 20 improvements he'd missed. 11% faster. Tobi Lutke pointed it at Shopify's Liquid templating engine. 53% faster rendering from 93 automated commits.

I spent two weeks pulling the system apart. Today's guide shows you how to use it on the things you actually make every day. Six use cases, the three-step setup, and the eval mistakes that kill runs before they start.

Full guide: <https://t.co/CbJSXRXRKh>

[Posted Mar 20, 2026 at 4:35AM](<https://twitter.com/aakashgupta/status/2034851259442749909>)
