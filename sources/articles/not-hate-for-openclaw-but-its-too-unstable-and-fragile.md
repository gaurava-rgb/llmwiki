---
title: "not hate for openclaw, but it's too unstable and fragile..."
reader_id: "01kj89sk1g4xfscdxm1qnwtrcr"
notion_page_id: "34a4ebe7-f118-813b-989e-e74d83827699"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kj89sk1g4xfscdxm1qnwtrcr"
source_url: "https://x.com/i/status/2025980742522786211/?rw_tt_thread=True"
author: "4nzn"
site: "X (formerly Twitter)"
tags: []
published: "2026-02-23"
saved_at: "2026-02-24"
reading_time: "2 mins"
summary: "The author finds OpenClaw too unstable and prefers a simpler agent with smart memory and skill access. They created a system that mirrors graph memory in editable markdown files for easy control and visualization. Skills are stored in the memory graph and activated only when relevant to avoid confusion and keep the agent smart."
content_hash: "55a630b9ebb0da78b38d1485d082da04598d588725972b277548fd92b999a877"
---

not hate for openclaw, but it's too unstable and fragile for my liking. i don't need overly complex multi-agent coordination, and i don't need to be able to text my agent from my samsung smart fridge...

i only need: SMART memory, skill access, and an agent that is not braindead & lobotomized if i plug a less intelligent model like minimax-2.5 into it

RAG graph memory by default. and i want to be able to not just visualize the agent memory, but also edit and modify it to make sure it's correct, and even add/fix connections manually over time

so i came up with a 1:1 mirroring system between a neo4j graph memory backend and markdown notes in the filesystem with wiki links. you can open the memory system in Obsidian (if you want) and visualize the memories and the graph

you NEVER touch the actual neo4j db. you work on markdown files. you edit memory content. you add or remove links, etc

whatever you do and edit in the markdown notes is instantly and automatically synced and re-indexed in the actual graph memory backend. it's like a mirror to give you human readable and editable access to the agent memory

one more BIG problem: when you load a shit ton of skills into your agent, it gets stupid. too many skills loaded in context create ambiguity and reduce activation accuracy

so: SKILLS now live in the memory graph along with memories. they can connect to memories. they can connect to other skills. and they are discovered ONLY when relevant. the right memory might connect to the right skill

example: when talking with your agent about the backend of a specific coding project, your postgres SQL might be automatically pulled into context and then fully discoverable by the agent

you can have 100s of skills in your graph, but they will only be discovered when relevant and NOT all in context by default. and of course, the skill in the graph can be a proxy to a standard claude format skill folder somewhere, so it's compatible with the legacy skill system

cron and HEARTHBEAT operations support just copied from openclaw because it's just a good system

* * *

[t.me/theaimafia](<http://t.me/theaimafia>)
