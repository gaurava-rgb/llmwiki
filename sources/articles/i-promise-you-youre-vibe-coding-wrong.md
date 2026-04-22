---
title: "I promise you you’re vibe coding wrong"
reader_id: "01jyx4q5vxyywkx2h1crskr119"
notion_page_id: "34a4ebe7-f118-81b9-85b4-d7437a16af71"
category: "tweet"
source_type: "Wisereads discovery"
reader_url: "https://read.readwise.io/read/01jyx4q5vxyywkx2h1crskr119"
source_url: "https://x.com/vasumanmoza/status/1923912878370980115/?rw_tt_thread=True"
author: "Vasuman Moza"
site: "X (formerly Twitter)"
tags: []
published: "2025-05-18"
saved_at: "2025-06-29"
reading_time: "2 mins"
summary: "The author, Vasuman Moza, shares a structured approach to coding that avoids chaos and confusion. By using ChatGPT to outline a detailed product architecture and a step-by-step plan, developers can maintain control and produce clean, testable code. This method emphasizes small, focused tasks to streamline the development process."
content_hash: "e19bf5f29e24423a387e6de8dede81448fe19af72d9d93c30b1665f5e08d918b"
---

I promise you you’re vibe coding wrong

as someone who has built multiple production-ready applications, with thousands of users, from just Cursor with minimum intervention.

But first here's you (probably):

You open Cursor. Type “build me X.”
It spirals. Nothing works. You start over.
That’s not development. That’s chaos.

I have an incredibly simple system that works every single time:

* * *

Step 1: <https://t.co/7LNl6vlaMZ>

Open ChatGPT (4o, not o1/o3/o4) and say:

“ I’m building a [description of your product - the more detailed the better]. Use Next.js for frontend, Supabase for DB + auth.
Give me the full architecture:
\- File + folder structure
\- What each part does
\- Where state lives, how services connect
Format this entire document in markdown.”

Save its output as <https://t.co/7LNl6vlaMZ> and throw it in an empty folder where your project will live.

* * *

Step 2: <https://t.co/QyJvN76ZPH>

Now say:

“ Using that architecture, write a granular step-by-step plan to build the MVP.
Each task should:
\- Be incredibly small + testable
\- Have a clear start + end
\- Focus on one concern
I’ll be passing this off to an engineering LLM that will be told to complete one task at a time, allowing me to test in between. "

Save it as <https://t.co/QyJvN76ZPH>. Again, throw it in the folder.

* * *

Step 3: In Cursor/Windsurf

“ You’re an engineer building this codebase.
You've been given <https://t.co/7LNl6vlICx> and <https://t.co/QyJvN76ZPH>.
\- Read both carefully. There should be no ambiguity about what we’re building.
\- Follow <https://t.co/QyJvN76ZPH> and complete one task at a time.
\- After each task, stop. I’ll test it. If it works, commit to GitHub and move to the next. "

Include this as well - this is crucial:

### CODING PROTOCOL ###
" Coding Instructions

\- Write the absolute minimum code required
\- No sweeping changes
\- No unrelated edits - focus on just the task you're on
\- Make code precise, modular, testable
\- Don’t break existing functionality
\- If I need to do anything (e.g. Supabase/AWS config), tell me clearly "

* * *

This system fixes the biggest problem with vibe coding:

You’re not dumping everything into the IDE and praying.
You’re giving it a roadmap.
You’re keeping it on rails.
You stay in control.

This workflow lets you ship clean, testable AI-assisted code - without the spiral.

Normally I'd ask you to follow me for the playbook but this is literally it. Good luck
