---
title: "You can use Claude Code to clean your Mac"
reader_id: "01kn5djhw0w5bpgtd3p139ga3q"
notion_page_id: "34a4ebe7-f118-8100-9c39-e41754959e65"
category: "tweet"
source_type: "Readwise web highlighter"
reader_url: "https://read.readwise.io/read/01kn5djhw0w5bpgtd3p139ga3q"
source_url: "https://x.com/dani_avila7/status/2007588161984118874/?rw_tt_thread=True"
author: "Daniel San"
site: "X (formerly Twitter)"
tags: []
published: "2026-01-03"
saved_at: "2026-04-01"
reading_time: "1 min"
summary: "Claude Code cleaned my Mac and freed 7.3GB by removing caches (NPM, Yarn) and old Homebrew packages.  \nIt acted like CleanMyMac or CCleaner using a single prompt.  \nThis shows prompts can replace some app functions."
content_hash: "b6bf1b3a3a492813ee555e02d1cb51a6f145f709215b8697abf13581f2e85891"
---

You can use Claude Code to clean your Mac

Running out of disk space. Opened Claude Code and asked it to find and clean temporary files.
One prompt... Done

What it cleaned:
\- NPM cache: 5.5GB
\- Homebrew old packages: 456MB
\- Yarn cache: 2.3GB

Recovered 7.3GB total.

This replaces some of the functionality you'd find in apps like CleanMyMac or CCleaner.

It's pretty incredible that we're starting to replace entire applications with Claude Code prompts.

What other app or functionality do you think could be replaced by a Claude Code prompt?

![](https://pbs.twimg.com/media/G9xhZoCWsAATibC.jpg)![](https://pbs.twimg.com/media/G9xhZoEWoAAIXIB.jpg)

* * *

Install with:

npx claude-code-templates@latest --command=utilities/cleanup-cache --yes

More info:
[aitmpl.com/component/comm…](<https://www.aitmpl.com/component/command/cleanup-cache>)

![](https://pbs.twimg.com/media/G9xiltDXoAM6MNN.jpg)
