---
title: "This guy built a distributed web crawler on Hetzner for..."
reader_id: "01kmh1zt4s759gr0snn6qttxzt"
notion_page_id: "34a4ebe7-f118-8197-8295-de711c38b6fb"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kmh1zt4s759gr0snn6qttxzt"
source_url: "https://x.com/i/status/2036283379432477018/?rw_tt_thread=True"
author: "Michael"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-24"
saved_at: "2026-03-24"
reading_time: "2 mins"
summary: "A developer built a distributed web crawler on Hetzner for $200 per month. He scaled it from 200 to 1,600 workers and faced challenges along the way. He will share his code and insights soon for others to learn from."
content_hash: "59911f7271fa0415540013bae9d65d3e5b3e1b8f30ab313abf63c9120987fdd9"
---

This guy built a distributed web crawler on Hetzner for $200/mo and wrote about exactly he did it.

Banger.

![](https://pbs.twimg.com/profile_images/1975716857337569280/PFDynq_3.jpg)

[hrishikesh kamath](<https://twitter.com/kamathhrishi>) [@kamathhrishi](<https://twitter.com/kamathhrishi>)

[ ](<https://twitter.com/kamathhrishi/status/2036278842344779973>)

Lately, I have been trying to beat Google.

Ok not really xD

I have been building a search engine over niche web data and it's been one of the most fun projects I've ever worked on.

The idea of querying the internet exactly the way I want, at scale, has always fascinated me. Especially what I could do with it: look at 1,000 companies' job postings and find hiring trends using natural language, map competitive landscapes including the lesser known players, find alternative data for investing. Or just a personalized corner of the web, curated for me.

It's been an interesting journey.

Started out with 200 workers on localhost, rewrote the crawler from Python to Rust to get up to 1,600 workers in parallel. Moved it to the cloud. Hit challenges that made the whole Rust rewrite useless xD

Then I woke up to an abuse report from a French website with the words "European Commission", "appeal", "court" in it. For a second I genuinely thought I was about to have legal proceedings against me. Phew. Nevertheless it's been the most fun project I've worked on. It's surprising how you can cover a lot of information starting from a modest number of seed URLs.

I'll be sharing everything I learned in the open. Code will be open sourced soon and the search engine will be live too.

If you're curious how to build a distributed web crawler that covers 10M+ pages under $200/month, do read my blogpost.

Blogpost Link: <https://t.co/nmsMR1l6Rx>

[Posted Mar 24, 2026 at 3:08AM](<https://twitter.com/kamathhrishi/status/2036278842344779973>)
