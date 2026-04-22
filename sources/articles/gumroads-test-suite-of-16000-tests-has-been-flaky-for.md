---
title: "Gumroad’s test suite of 16,000 tests has been flaky for..."
reader_id: "01kmr4r0rmq1h9t2dch5jy0xs3"
notion_page_id: "34a4ebe7-f118-8106-b812-dc733fdd9eef"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kmr4r0rmq1h9t2dch5jy0xs3"
source_url: "https://x.com/i/status/2037366443906330826/?rw_tt_thread=True"
author: "Sahil Lavingia"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-27"
saved_at: "2026-03-27"
reading_time: "3 mins"
summary: "Gumroad’s large test suite was flaky and slowed down work for years. A new AI tool named Gumclaw fixed many flaky tests automatically overnight. This tool is open source and helps teams save time by handling repetitive test debugging."
content_hash: "35876907504c6b5f02180759420621f079b675695f71944e212c50032af93ac0"
---

Gumroad’s test suite of 16,000 tests has been flaky for years. This slowed down shipping tremendously.

This week, Gianfranco used [@karpathy](<https://twitter.com/karpathy>)’s autoresearch and [@steipete](<https://twitter.com/steipete>)’s OpenClaw to stabilize our test suite overnight.

And his code is open source, so you can (have your agent) do it too.

(And our code is open source too so you can see every single fix on GitHub.)

![](https://pbs.twimg.com/profile_images/1963590044469411840/h2NRmpcU.jpg)

[Gianfranco](<https://twitter.com/gianfrancopiana>) [@gianfrancopiana](<https://twitter.com/gianfrancopiana>)

[ ](<https://twitter.com/gianfrancopiana/status/2037199814694228187>)

Last week Gumclaw made 206 commits to our repo while I slept. It fixed 13 flaky tests. I didn't write a single line of test code.

Gumclaw is Gumroad's team AI assistant. It runs on [OpenClaw](<https://openclaw.ai/>) on a Mac mini at our Brooklyn office. It answers questions, reviews PRs, and now, apparently, fixes flaky tests.

Flaky tests are detective work with a 20-minute feedback loop. They pass locally, fail in CI, and after enough false alarms the team starts ignoring red builds. Nobody wants to fix them. So nobody does.

I wanted to see if Gumclaw could do the grinding for me.

Spoiler alert: it did.

![Image](https://pbs.twimg.com/media/HEWV5ydWsAE7MoP.jpg)

**This freed me to do my job.** My highest-value work is building product, not debugging why a tax test fails 1 in 20 runs. Gumclaw ran overnight while I shipped features.

Here's how you can setup the same system for yourself.

## The tool

I built [openclaw-autoresearch](<https://github.com/gianfrancopiana/openclaw-autoresearch>), a plugin for [OpenClaw](<https://openclaw.ai/>). It's a port of [pi-autoresearch](<https://github.com/davebcn87/pi-autoresearch>) (by Tobi Lutke) to the OpenClaw plugin system.

The idea is simple. You give it a command that measures something. Gumclaw runs it, gets a baseline, makes a change, runs it again. If the numbers improve, it commits. If they don't, it logs what it learned and what to try next. Then it loops.

All state lives in plain files. If the session crashes, you type `/autoresearch resume` and Gumclaw picks up where it left off.

## What happened

I pointed Gumclaw at our test suite on March 18. One week later: 206 commits, 94 CI runs, 13 merged PRs. Race conditions, timing issues, browser session corruption, test cleanup hooks leaking between tests.

The best find wasn't even a flaky test. It was a real bug: when remapping file IDs, A became B, then B became C, silently corrupting file references. The flake was just the symptom.

## What the agent found

It was methodical. Fix a class of failures, trigger CI, log the results, move to the next class.

When a fix didn't hold, it wrote down why and what to try next. Those notes fed an ideas backlog that kept it from repeating failed approaches. By experiment 20, it had built a map of which tests were flaky and why.

Some fixes took multiple iterations. One tax input field went through four different approaches before Gumclaw found one that held across CI runs.

## What I learned

**Flaky tests are a perfect target for this.** Green or red. Pass or fail. The agent ran 30+ CI cycles overnight without getting bored.

**The ideas backlog is the killer feature**. Every failed experiment forces Gumclaw to write down what it tried. It stops repeating mistakes.

**It takes time: 206 commits for 13 PRs**. Fixing a flaky test is easy. Proving it's fixed means running CI enough times to trust the flake is gone and not hiding. The loop handles that grind.

## Try it now:


    openclaw plugin install @gianfrancopiana/openclaw-autoresearch
    /autoresearch setup


[openclaw-autoresearch](<https://github.com/gianfrancopiana/openclaw-autoresearch>) is open source, and we would love your contributions!

[Posted Mar 26, 2026 at 4:07PM](<https://twitter.com/gianfrancopiana/status/2037199814694228187>)

* * *

[github.com/gianfrancopian…](<https://github.com/gianfrancopiana/openclaw-autoresearch>)
