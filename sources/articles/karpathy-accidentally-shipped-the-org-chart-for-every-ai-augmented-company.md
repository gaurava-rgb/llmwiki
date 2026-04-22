---
title: "Karpathy accidentally shipped the org chart for every AI-augmented company..."
reader_id: "01kme9kqch95bs0hcv7wts7h5y"
notion_page_id: "34a4ebe7-f118-81a5-8b70-d306cfab03e9"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kme9kqch95bs0hcv7wts7h5y"
source_url: "https://x.com/i/status/2036006034729304175/?rw_tt_thread=True"
author: "Aakash Gupta"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-23"
saved_at: "2026-03-23"
reading_time: "3 mins"
summary: "Karpathy created a simple system that separates goal-setting from evaluation to ensure honest AI improvements. This method stops AI from faking results by locking the evaluation process. Many companies can use this idea to make better, trustworthy AI-driven decisions."
content_hash: "f41693a3c60a51113d5dea452c7c31ce3a20e44cf82f886a3542f386af1a86dc"
---

Karpathy accidentally shipped the org chart for every AI-augmented company in 2030.

Three files. [program.md](<http://program.md/>) is the human writing strategy in plain English. [train.py](<http://train.py/>) is the agent executing, iterating, and shipping code. [prepare.py](<http://prepare.py/>) is the locked evaluation layer that neither the human nor the agent can touch mid-run.

That third file is the one worth studying.

In most companies deploying AI agents today, the person who sets the goal also controls how success is measured. The marketing team picks the KPI, runs the campaign, and reports the results. The PM defines the metric, ships the feature, and presents the dashboard. The incentive to subtly shift the goalposts is built into the structure.

Karpathy separated goal-setting from evaluation by making [prepare.py](<http://prepare.py/>) immutable. The agent optimizes val_bpb. The agent cannot redefine val_bpb. The agent cannot swap in a friendlier dataset. The agent cannot adjust the tokenizer to make its numbers look better. It either improved on the locked metric or it gets reverted. No narrative. No context. No "well, if you look at it this way."

That's why the results held. 700 experiments, 20 kept, and when Karpathy applied those 20 improvements to a model twice the size, every single one transferred. The gains were real because the agent had zero ability to make fake gains look real.

Shopify's CEO ran the same architecture overnight. 37 experiments, 19% quality improvement, smaller model beating a larger one. The pattern transferred because the evaluation was trustworthy.

Now scale the principle. A sales team where the AI agent writes outbound sequences, an independent system scores reply quality, and a human sets the targeting criteria. A product team where the agent ships variants, a locked analytics pipeline measures retention, and a PM writes the experiment brief. A recruiting team where the agent screens candidates, a calibrated rubric scores them, and a hiring manager defines the role.

The separation Karpathy built into 630 lines of Python is the same separation every company will need when agents do the execution. Whoever controls the eval controls the outcome. Lock it down or the agent will find the shortest path to a number that means nothing.

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
