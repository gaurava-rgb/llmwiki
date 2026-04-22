---
title: "elvis (@elvissaravia): \"Agentic Context Engineering Great paper on agentic context engineering. The recipe: Treat your system prompts and agent memory as a living playbook. Log trajectories, reflect to extract actionable bullets (strategies, tool schemas, failure modes), then merge as append-only…\""
reader_id: "01k7a69eymxyet4gfxsh1fwfr2"
notion_page_id: "3484ebe7-f118-81e1-9df5-d1bf3aafb908"
category: "article"
source_type: "Reader Share Sheet iOS"
reader_url: "https://read.readwise.io/read/01k7a69eymxyet4gfxsh1fwfr2"
source_url: "https://substack.com/@elvissaravia/note/c-165115004?r=38jwv"
author: "Substack"
site: "Substack"
tags: []
published: "2025-10-11"
saved_at: "2025-10-11"
reading_time: "1 min"
summary: "Agentic Context Engineering treats prompts and agent memory as a living playbook. It logs runs, extracts actionable bullets, and appends deduplicated updates to improve agents. Using tests and online updates, ACE outperforms baselines in adaptation."
content_hash: "5dc1111ff21945a7a183e203a59dfd4f37bbc11b41c00c8204e60280f73f0999"
---

[![](https://substackcdn.com/image/fetch/$s_!k_mw!,w_520,h_272,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d285455-461b-44ac-ae33-79fc301d4d5a_500x310.jpeg)](<https://jmarriott.substack.com/p/the-dawn-of-the-post-literate-society-aa1>)[![Cultural Capital](https://substackcdn.com/image/fetch/$s_!Yg17!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c790cf3-5cd4-4ab6-bde4-e19b87ad08aa_1024x1024.png)](<https://jmarriott.substack.com/p/the-dawn-of-the-post-literate-society-aa1>)[Cultural Capital](<https://jmarriott.substack.com/>)The dawn of the post-literate society ![](https://substackcdn.com/image/fetch/$s_!u9e1!,w_100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Fapp_page%2Fhighlight-2-v5.png)

Agentic Context Engineering

Great paper on agentic context engineering.

The recipe:

Treat your system prompts and agent memory as a living playbook.

Log trajectories, reflect to extract actionable bullets (strategies, tool schemas, failure modes), then merge as append-only deltas with periodic semantic de-dupe.

Use execution signals and unit tests as supervision. Start offline to warm up a seed playbook, then continue online to self-improve.

On AppWorld, ACE consistently beats strong baselines in both offline and online adaptation. Example: ReAct+ACE (offline) lifts average score to 59.4% vs 46.0–46.4% for ICL/GEPA. Online, ReAct+ACE reaches 59.5% vs 51.9% for Dynamic Cheatsheet.

Track top AI papers here: [nlp.elvissaravia.com](<https://nlp.elvissaravia.com/>)
