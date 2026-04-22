---
title: "The quality of your vibecoded slop is horrible"
reader_id: "01kpa3hfshx8wnfh36ska7exry"
notion_page_id: "34a4ebe7-f118-81c2-9826-ed6c7a97def6"
category: "tweet"
source_type: "Reader Share Sheet iOS"
reader_url: "https://read.readwise.io/read/01kpa3hfshx8wnfh36ska7exry"
source_url: "https://x.com/shawmakesmagic/status/2044269097647779990/?s=12&rw_tt_thread=True"
author: "Shaw (spirit/acc)"
site: "X (formerly Twitter)"
tags: []
published: "2026-04-15"
saved_at: "2026-04-16"
reading_time: "2 mins"
summary: "The current code quality is very poor and needs major improvement. The author suggests using eight specialized subagents to clean, simplify, and strengthen the codebase. Each subagent will research, assess, and fix specific issues like duplication, weak types, unused code, and unclear comments."
content_hash: "7729ca183260339303724446f00bc9b1e205b956989308b0eb20701c66a558aa"
---

The quality of your vibecoded slop is horrible. I've seen it. Absolute dogshit.

Fortunately, there is a fix.

Use this prompt:

I want to clean up my codebase and improve code quality. This is a complex task, so we'll need 8 subagents. Make a sub agent for each of the following:

1\. Deduplicate and consolidate all code, and implement DRY where it reduces complexity

2\. Find all type definitions and consolidate any that should be shared

3\. Use tools like knip to find all unused code and remove, ensuring that it's actually not referenced anywhere

4\. Untangle any circular dependencies, using tools like madge

5\. Remove any weak types, for example 'unknown' and 'any' (and the equivalent in other languages), research what the types should be, research in the codebase and related packages to make sure that the replacements are strong types and there are no type issues

6\. Remove all try catch and equivalent defensive programming if it doesn't serve a specific role of handling unknown or unsanitized input or otherwise has a reason to be there, with clear error handling and no error hiding or fallback patterns

7\. Find any deprecated, legacy or fallback code, remove, and make sure all code paths are clean, concise and as singular as possible

8\. Find any AI slop, stubs, larp, unnecessary comments and remove. Any comments that describe in-motion work, replacements of previous work with new work, or otherwise are not helpful should be either removed or replaced with helpful comments for a new user trying to understand the codebase-- but if you do edit, be concise

I want each to do detailed research on their task, write a critical assessment of the current code and recommendations, and then implement all high confidence recommendations.
