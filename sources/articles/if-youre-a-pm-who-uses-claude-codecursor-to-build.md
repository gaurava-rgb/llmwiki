---
title: "If you're a PM who uses Claude Code/Cursor to build..."
reader_id: "01kkj8rsh9p1ws9pknnnnt92g7"
notion_page_id: "34a4ebe7-f118-8153-b469-e2679854a303"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kkj8rsh9p1ws9pknnnnt92g7"
source_url: "https://x.com/i/status/2032124503330058696/?rw_tt_thread=True"
author: "George from 🕹prodmgmt.world"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-12"
saved_at: "2026-03-13"
reading_time: "2 mins"
summary: "This tool stack helps product managers quickly find and use past research and decisions without manual copying. It uses Obsidian to store notes locally and qmd to search them with advanced methods, keeping data private. This saves time and makes each new note more valuable for future work."
content_hash: "ba0394c934cc36b67c4fe320598c9808d4624b6ba7a7a00accd360e86830434f"
---

If you're a PM who uses Claude Code/Cursor to build and execute research, strategy, and discovery work, this stack cuts context setup from 15 minutes of pasting to under a minute.

Obsidian solves the storage problem: every note you write becomes a local markdown file, yours permanently, readable by any tool, locked to no platform.

The second piece is qmd, a CLI tool built by Tobi Lütke (Shopify's CEO) specifically for searching markdown files, now at 14.5k GitHub stars.

It combines three search approaches running entirely on your machine: BM25 full-text retrieval, vector semantic search via a locally-running 300MB embedding model, and LLM re-ranking for final relevance scoring. No data leaves your laptop.

You point it at a folder, run `qmd embed` to index your entire collection.

What this means in practice: I can open Claude Code and ask it to find every decision I've made about a particular product area, or pull every research note that mentions a specific problem, without manually copying anything.

Claude runs the search, reads the relevant files, and starts from that context rather than from scratch. The time I used to spend pasting background into chat windows before each session now goes into the actual work.

What I didn't expect was how much it compounds. I'm not sure how to quantify it precisely, but every note I add increases the usefulness of future sessions without any extra effort on my part.

Setup to replicate this:

  1. Install Obsidian and import all your notes from wherever you used to store them
  2. Install QMD (<https://t.co/3FtFXnMdcn>)



Works perfectly with <https://t.co/ngCnvp77SD> of course
