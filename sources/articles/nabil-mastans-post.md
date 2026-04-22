---
title: "Nabil Mastan’s Post"
reader_id: "01kn8c4pv731whtgs145ff1ht5"
notion_page_id: "3464ebe7-f118-8179-ab0a-fd36a072cf4f"
category: "article"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kn8c4pv731whtgs145ff1ht5"
source_url: "https://www.linkedin.com/posts/nabil-mastan_github-namastanresume-tailoring-agents-share-7444773315589652480-srQr"
author: "Nabil Mastan"
site: "linkedin.com"
tags: []
published: ""
saved_at: "2026-04-03"
reading_time: "2 mins"
summary: "Nabil Mastan built an AI tool that helps you see if a job fits you instead of just making your resume look good. The tool keeps your words but asks questions to improve weak resume points based on real experience. This saves time by showing which jobs match you well and which don’t."
content_hash: "60e72b3657db59232909bd5b413cc6fdf8ece5273a07cfa7be6fee00cbf86289"
---

[ Nabil Mastan ](<https://www.linkedin.com/in/nabil-mastan?trk=public_post_feed-actor-name>)

The Profit Clinic AI•979 followers

A tool that tells you 'this role isn't a fit' is more valuable than one that makes your resume look good for every role.

I learned that by building one.

I'm a strategic PM obsessing over how AI is changing how we work. While exploring my next career move, I got frustrated with AI resume tools that rewrite your bullets and invent outcomes you'd never survive an interview defending.

So I built a different kind of system.

It has three components:
1) A parser that turns your resume into a structured YAML file. Your exact words, never changed.
2) A job analyst that strips generic JD requirements before scoring your bullets against what actually differentiates candidates.
3) A coaching agent that interrogates weak bullets instead of rewriting them.

The coaching part is where it got interesting.

When the analyst flags a weak bullet, the coach asks you 3 questions. You answer with what actually happened. It sharpens the bullet using only what you give it.

Here's a real example from my own resume:

Original (weak, pre-coaching):
"Led template and workflow strategy for Mailchimp's email product, improving adoption and retention metrics."

After 3 questions:
"Owned end-to-end template strategy for Mailchimp's flagship email product — diagnosed the cold-start problem, overhauled discovery UX, personalized templates by business use case, doubled the library in 90 days, and resolved nearly 1 in 5 email-related VOC complaints."

Same experience. Nothing invented. Completely different signal.

Then I ran the system against two real roles I was considering.

A cardiovascular health PM role at a wearable company: 0.15 alignment. The system correctly flagged that I have zero domain background in physiological sensing. Easy pass.

A Senior Staff AI PM role at a platform I know deeply: 0.67 with a clean gap analysis showing exactly where I'm strong and where I'm not.

The 0.15 saved me hours of tailoring an application I had no business submitting.

While the architecture and design decisions are mine, having [Anthropic](<https://www.linkedin.com/company/anthropicresearch?trk=public_post-text>)'s Claude Code as an AI pair programmer compressed weeks of work into days. That's the meta-lesson underneath all of this.

The whole thing is open-source: [https://lnkd.in/e8E6GP62](<https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd.in%2Fe8E6GP62&urlhash=T4h7&trk=public_post-text>)

Python + Claude API. No database. Your career history lives in a YAML file you own and version control.

If you're in a job search or building agent workflows, I'd love to hear what you think - drop a comment or star the repo if it's useful.

[#ProductManagement](<https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fproductmanagement&trk=public_post-text>) [#AIAgents](<https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Faiagents&trk=public_post-text>) [#JobSearch](<https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fjobsearch&trk=public_post-text>) [#OpenSource](<https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fopensource&trk=public_post-text>)

[![GitHub - namastan/resume-tailoring-agents: A multi-component Python framework for tailoring resumes using a persistent career data structure and an interactive coaching agent](https://media.licdn.com/dms/image/sync/v2/D4E27AQFFOC2kSWC0LQ/articleshare-shrink_1280_800/B4EZ1EkBb6HYAU-/0/1774971787882?e=2147483647&v=beta&t=1E7R_anydDwfUENSFvj7cMj2De3j0oHdBlPG2s1mwko) GitHub - namastan/resume-tailoring-agents: A multi-component Python framework for tailoring resumes using a persistent career data structure and an interactive coaching agent github.com ](<https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgithub.com%2Fnamastan%2Fresume-tailoring-agents&urlhash=EOLZ&trk=public_post_feed-article-content>)
