---
title: "infinite alpha in this article, but this tops them all..."
reader_id: "01km3cs0fwh6ktnvxdt0jh9nmv"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01km3cs0fwh6ktnvxdt0jh9nmv"
source_url: "https://x.com/i/status/2034280589411455107/?rw_tt_thread=True"
author: "Ole Lehmann"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-18"
saved_at: "2026-03-19"
reading_time: "11 mins"
summary: "Anthropic created a system where AI skills learn from your corrections to improve automatically over time. The more you use it, the better it adapts to your real preferences without extra effort. This saves time by producing drafts and outputs that fit your style with minimal editing."
content_hash: "c83d59ac34c42b6b29f2a8152ddf3a0e6cfa725697d8082d894321c7340b8970"
---

infinite alpha in this article, but this tops them all IMO (i'm adding this to all my skills):

anthropic found a way to make their skills compound on autopilot.

every session gets memorized (what it produced, what you corrected, what you preferred)

so the skill learns _exactly_ how you want things done, and the output gets closer to perfect every single session

meaning the more you use claude, the better it adapts to you.

over time you barely have to edit anything because it already knows your preferences from every previous session

here's how it works:

you add a feedback log to any skill.

every time you correct claude during a session ("too formal," "shorter subject lines," "i'd never phrase it like that"), it saves your correction to the log

next session it reads the log before doing anything else.

session 1 through 5 feel normal. you're still correcting things, still adjusting tone, still saying "not like this, more like this"

by session 10 the corrections start dropping off. because claude already absorbed the patterns from your previous feedback

by session 20 the first drafts are coming back close to done.

because the skill now carries 20 sessions worth of your real preferences

(and not your imagined preferences from when you first wrote the instructions, your real ones that only surface when you're editing live output)

this works across everything:

  * content: "too formal" / "never use that word" / "always put the cta before the sign-off" → drafts start sounding like you actually wrote them

  * outreach: "shorter subject lines" / "reference something specific about their business" / "don't open with the company name" → sequences stop reading like templates

  * client reports: "bar charts, never pie charts" / "recommendation before the data" / "my clients hate jargon" → reports come out ready to send

  * proposals: "lead with the problem statement" / "pricing on its own page" / "less formal in the intro" → first drafts you'd actually put your name on




here's the setup. paste this into cowork:

"add a feedback log to my [skill name] skill. create a feedback.log file inside the skill folder. update the skill instructions to: (1) read feedback.log at the start of every session before doing anything. (2) whenever i give a correction or preference during a session, immediately append it to feedback.log. use your judgment on how much detail to include per entry, some preferences are one line, others need a sentence or two of context to be useful. only log general preferences that apply to future sessions, skip anything specific to the current task"

cowork handles the rest. takes about 30 seconds

it's like onboarding an assistant who takes perfect notes.

30 seconds of setup, and a month in they already know how you think (with unreal precision)

run that prompt for every skill you have and give it a few weeks.

![](https://pbs.twimg.com/profile_images/1976939058741039104/r3GgzqRh.jpg)

[Thariq](<https://twitter.com/trq212>) [@trq212](<https://twitter.com/trq212>)

[ ](<https://twitter.com/trq212/status/2033949937936085378>)

![Lessons from Building Claude Code: How We Use Skills ](https://pbs.twimg.com/media/HDl2jn9a0AAZkyz.jpg)

Skills have become one of the most used extension points in Claude Code. They’re flexible, easy to make, and simple to distribute.

But this flexibility also makes it hard to know what works best. What type of skills are worth making? What's the secret to writing a good skill? When do you share them with others?

We've been using skills in Claude Code extensively at Anthropic with hundreds of them in active use. These are the lessons we've learned about using skills to accelerate our development.

## What are Skills?

If you’re new to skills, I’d recommend [reading our docs](<https://code.claude.com/docs/en/skills>) or watching our newest course on [new Skilljar on Agent Skills](<https://anthropic.skilljar.com/introduction-to-agent-skills>), this post will assume you already have some familiarity with skills.

A common misconception we hear about skills is that they are “just markdown files”, but the most interesting part of skills is that they’re not just text files. They’re folders that can include scripts, assets, data, etc. that the agent can discover, explore and manipulate.

In Claude Code, skills also have a [wide variety of configuration options](<https://code.claude.com/docs/en/skills>) including registering dynamic hooks.

We’ve found that some of the most interesting skills in Claude Code use these configuration options and folder structure creatively.

# Types of Skills

[Posted Mar 17, 2026 at 4:53PM](<https://twitter.com/trq212/status/2033949937936085378>)

* * *

if you want to learn how to use claude cowork to create the output of a 5 person marketing team, i'm hosting a workshop in 2 weeks

last time 180 people joined

[tally.so/r/LZbxKl](<https://tally.so/r/LZbxKl>)

* * *

If you want more AI workflows that help you get more customers, more attention, and more done (without working more hours)...

I send them to 35k readers every week for free.

Plus you get a free Claude Cowork masterclass when you join: [aisolo.beehiiv.com/subscribe](<http://aisolo.beehiiv.com/subscribe>)
