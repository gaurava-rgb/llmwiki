---
title: "Karpathy's autoresearch isn't just for AI research"
reader_id: "01kkfay47zj26736677gj035pg"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kkfay47zj26736677gj035pg"
source_url: "https://x.com/i/status/2031046227333443609/?rw_tt_thread=True"
author: "ericosiu"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-09"
saved_at: "2026-03-11"
reading_time: "3 mins"
summary: "Karpathy's autoresearch uses AI to run thousands of experiments automatically, speeding up learning in marketing and business. This system tests and improves things like emails and ads much faster than humans can. Companies using it gain a big advantage by continuously learning what works best while others move slowly."
content_hash: "cdf1a1b08a2916539f3ff318712db30416e49249b9b7a869d41349088a2ce04f"
---

Karpathy's autoresearch isn't just for AI research. You can use it for business.

Imagine running 700x more experiments:

  * Landing pages
  * Creatives
  * AEO/SEO
  * Pricing
  * E-mails
  * Cold outreach
  * Warm outreach
  * AP/AR
  * Procurement



Revenues: 📈

![](https://pbs.twimg.com/profile_images/1855481085595156480/wKSpzEkj.jpg)

[ericosiu](<https://twitter.com/ericosiu>) [@ericosiu](<https://twitter.com/ericosiu>)

[ ](<https://twitter.com/ericosiu/status/2030758253395951958>)

![Karpathy's Autonomous AI Can Make You 701x Faster. It's The Future of Business.](https://pbs.twimg.com/media/HC6m0yAbIAArqSF.jpg)

Most marketing teams run ~30 experiments a year. The next generation will run 36,500+. Easily.

They'll run experiments while they sleep.

Current marketing teams run 20-30 experiments a year. Maybe 52 if they're 'good'.

New landing page.

New ad creative.

Maybe a subject line test.

That's considered "data-driven marketing."

But the next generation of marketing systems will run 36,500+ experiments per year.

And most of them will run automatically.

The shift comes from a simple pattern.

More on the math below.

## The Experiment Loop

Every growth channel follows the same structure:





content missing


Modify a variable.

Deploy it.

Measure one metric.

Keep or discard.

Repeat forever.

Cold email.

Ad creative.

Landing pages.

Job postings.

YouTube thumbnails.

Discovery call scripts.

They all follow the same loop.

## AI Just Learned How to Run This Loop

Andrej Karpathy released autoresearch.

An AI agent that runs ML experiments autonomously. Modifies code, trains a model for 5 minutes, checks whether results improved, keeps or discards the change, repeats.

You wake up to 100 experiments completed overnight.

Multiply 100 * 365 days = 36,500 experiments completed in a year.

I looked at it and realized this pattern works for anything with a feedback signal and a variable to optimize.

Including marketing.

## The Marketing Version

Karpathy's system has three files:

  * [prepare.py](<http://prepare.py/>): fixed constraints, never touched

  * [train.py](<http://train.py/>): the thing being optimized

  * [program.md](<http://program.md/>): instructions for the agent




The marketing equivalent:

[baseline.md](<http://baseline.md/>)

Your ICP, positioning, brand rules, guardrails. The stuff that doesn't change.

template.json

The asset being optimized. Email, ad, landing page, script.

[program.md](<http://program.md/>)

Campaign goal + scoring rule.

Once those exist, the system runs the loop automatically.

**Example: Cold Outreach**

We're building the first test loop right now.

Setup:

  * 15 inboxes

  * ~300 emails per day

  * Agent modifies one variable per experiment

  * Sends 100 emails

  * Waits 72 hours

  * Scores positive reply rate

  * Keeps or discards

  * Repeats




Variables tested: subject line, opener, CTA, personalization depth, framing angle.

Current baseline: 1% positive reply rate.

Target after 30 days of autonomous testing: 2%+.

That sounds small.

But at 9,000 sends per month, that's the difference between 90 interested replies and 180 interested replies.

At our close rates, that's roughly $500K+ in additional pipeline.

And the agent never stops testing.

## The Real Power: Multiple Loops

The same engine runs across every growth surface.





content missing


Different scoring speeds. Same engine.

In our case: 17 loops running simultaneously.

## The Compounding Effect

Each loop produces learning. But the learning spreads.





content missing


Now your marketing system is building a knowledge graph of what resonates with your ICP.

Each experiment makes every channel smarter.

Humans can't do this. Most teams run 2-3 experiments per month per channel. These loops run 2-3 per week per channel.

Across 17 channels: 170+ experiments per month.

In one year: ~2,000 experiments.

Your competitor ran 30.

## The Cost Difference Is Ridiculous

Running these loops costs roughly $100-150/month. Compute, sending infrastructure, scoring scripts.

One junior marketer costs $5,000/month and runs fewer experiments.

The machine replaces slow learning cycles. Marketers still matter. Speed of learning matters more.

## Where the Moat Actually Comes From

Agents may very well become commodities. Everyone will have access to the same models.

The real moat is experiment history.

A system that runs 2,000 experiments per year across 17 channels for a specific ICP builds a proprietary map of which hooks work, which numbers convert, which angles resonate, which objections appear.

Switching vendors means losing that entire learning history.

The moat is the experiment graph.

## What This Means

Marketing teams historically optimized campaigns.

The next generation will optimize learning velocity.

The companies that win won't have better marketers. They'll have faster experiment loops.

And once those loops start running, they never stop.

Your competitors will still be launching campaigns.

You'll be running a system that learns while you sleep.

If you're AI-obsessed and want to work with me, you can apply by beating AI at <https://www.singlegrain.com/apply>

For more like this, level up your marketing with 14,000+ marketers and founders in my Leveling Up newsletter here for free: <https://levelingup.beehiiv.com/subscribe>

[Posted Mar 8, 2026 at 9:31PM](<https://twitter.com/ericosiu/status/2030758253395951958>)
