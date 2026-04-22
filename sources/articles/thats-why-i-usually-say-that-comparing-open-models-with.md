---
title: "That’s why I usually say that comparing open models with..."
reader_id: "01kn5drw60gjpdk8gwbnhq2st6"
notion_page_id: "34a4ebe7-f118-81b0-90cd-e5fad8c83851"
category: "tweet"
source_type: "Readwise web highlighter"
reader_url: "https://read.readwise.io/read/01kn5drw60gjpdk8gwbnhq2st6"
source_url: "https://x.com/ClementDelangue/status/2039194611118190866/?rw_tt_thread=True"
author: "clem 🤗"
site: "X (formerly Twitter)"
tags: []
published: "2026-04-01"
saved_at: "2026-04-01"
reading_time: "3 mins"
summary: "Comparing open models to closed-source APIs is unfair because APIs have extra tools and tricks that open models lack. Claude Code works better than a simple chat interface due to smart context handling, caching, and specialized tools. These improvements help Claude Code manage code efficiently and provide stronger performance."
content_hash: "da3ecdfda3dd93928578d76c866690386bab0bde83afc1550e40c6c21e71fcf2"
---

That’s why I usually say that comparing open models with closed-source APIs or products is like comparing apples and oranges. Or comparing an engine with a full car. Or comparing an ingredient with a Michelin dinner (missing ingredients, prep and chef).

There’s a lot of scaffolding and tricks that is done behind APIs that make it unfair to compare to a raw open-source model! However that also means that if you put the work to really try to make open-source models work, they can give you much better results than what benchmark suggests (and that’s without even post-training/fine-tuning)

![](https://pbs.twimg.com/profile_images/1661187442043486209/a3E4t1eV.jpg)

[Sebastian Raschka](<https://twitter.com/rasbt>) [@rasbt](<https://twitter.com/rasbt>)

[ ](<https://twitter.com/rasbt/status/2038980345316413862>)

![Claude Code's Real Secret Sauce \(Probably\) Isn't the Model](https://pbs.twimg.com/media/HEvpqRWbQAA6JKt.jpg)

Turns out Claude Code source code was leaked today. I saw several snapshots of the TypeScript code base on GitHub. I don't want to link here for legal reasons, but there are some interesting educational tidbits that can be learned here.

Of course, it's probably common knowledge that Claude Code works better for coding than the Claude web chat because it is not just a chat interface with a shell added to it but more of a carefully designed tool with some nice prompt and context optimizations.

I should also say that while a lot of the qualitative coding performance comes from the model itself, I believe the reason why Claude Code is so good is this software harness, meaning that if we were to drop in other models (say DeepSeek, MiniMax, or Kimi) and optimize this a bit for these models, we would also have very strong coding performance.

Anyways, below are some interesting tidbits for educational purposes to better understand how coding agents work.

# 1\. Claude Code Builds a Live Repo Context

This is maybe most obvious, but when you start prompting, Claude loads the main git branch, current git branch, recent commits, etc. in addition to [CLAUDE.md](<http://CLAUDE.md/>) for context.

# 2\. Aggressive Prompt Cache Reuse

There seems to be something like a boundary marker that separates static and dynamic content. Meaning the static sections are globally cached for stability so that the expensive parts do not need to be rebuilt and reprocessed every time.

# 3\. The Tooling Is Better Than "Chat With Uploaded Files"

The prompt seems to tell the model to uses a dedicated Grep tool instead of invoking grep or rg through Bash, presumably because the dedicated tool has better permission handling and (perhaps?) better result collection.

There is also a dedicated Glob tool for file discovery. And finally it also has a LSP (Language Server Protocol) tool for call hierarchy, finding references etc. That should be a big "power up" compared to the Chat UI, which (I think) sees the code more as static text.

# 4\. Minimizing Context Bloat

One of the biggest problems is, of course, the limited context size when working with code repos. This is especially true if we have back-and-forths with the agent and repeated file reads, log files, long shell outputs etc.

There is a lot of plumbing in Claude Code to minimize that. For example, they do have file-read deduplication that checks whether a file is unchanged and then doesn't reprocess these unchanged files.

Also, if tool results do get too large, they are written to disk, and the context only uses a preview plus a file reference.

And, of course, similar to any modern LLM UI, it would automatically truncate long contexts and run autocompaction (/summarization) if needed.

# 5\. Structured Session Memory

Claude Code keeps a structured markdown file for the current conversation with sections like:

  * Session Title
  * Current State
  * Task specification
  * Files and Functions
  * Workflow
  * Errors & Corrections
  * Codebase and System Documentation
  * Learnings
  * Key results
  * Worklog



It's kind of how we humans code, I'd say, where we keep notes and summaries.

# 6\. It Uses Forks and Subagents

This is probably no surprise that Claude Code parallizes work with subagents. That was basically one of the selling points over Codex for a long time (until Codex recently also added subagent support).

Here, forked agents reuse the parent's cache while being aware or mutable states. So, that lets the system do side work such as summarization, memory extraction, or background analysis without contaminating the main agent loop.

# Why This Probably Feels And Works Better Than Coding in the Web UI

All in all, the reason why Claude Code works better than the plain web UI is not prompt engineering or a better model. It's all these little performance and context handling improvement listed above. And there is the convenience, of course, too, in having everything nice and organized on your computer versus uploading files to a Chat UI.

[Posted Mar 31, 2026 at 2:02PM](<https://twitter.com/rasbt/status/2038980345316413862>)
