---
title: "Hardik Tiwari’s Post"
reader_id: "01kkxtrtpggnhqm8jhww6b2t6q"
notion_page_id: "3464ebe7-f118-8119-ae8e-ebb01b71cd51"
reader_url: "https://read.readwise.io/read/01kkxtrtpggnhqm8jhww6b2t6q"
source_url: "https://www.linkedin.com/posts/hardik-tiwari_our-product-team-has-been-using-llms-to-assist-share-7439466110468603904-Q5r5"
author: "Hardik Tiwari"
site: "linkedin.com"
tags: []
published: ""
saved_at: "2026-03-17"
reading_time: "2 mins"
summary: "Hardik Tiwari’s team built a tool that connects their work apps and shares strategy with AI to help manage projects better. The tool uses a context graph to remember all decisions, plans, and documents, so the AI can assist without repeating information. This system makes tasks like writing documents or planning days faster and more accurate for the whole team."
content_hash: "fd5bf80045f98518a6dd647c447d5d74fe11ab24920d78763a053ded0b3db303"
---

[ Hardik Tiwari ](<https://www.linkedin.com/in/hardik-tiwari?trk=public_post_feed-actor-name>)

Our product team has been using LLMs to assist with work. However, every session started with managing/writing prompts, re-explaining our strategy and seeding context .

So we natively moved to claude/cursor. And setup our framework to use/contribute.

PM Operating System — a repo you clone into Cursor/Claude code that gives your AI full PM context, once. Strategy, segments, metrics, decisions. Connect your apps— Slack, Jira, Drive, Figma, Databricks… anything you use — and integrate context from them. That context makes every conversation/work with LLM informed

It has 15+ PM skills baked in: PRDs, working backwards, launch posts, exec updates, weekly planning and updating memory layer and referencing relevant tools/MCPs.

With Shared context across the team. Everyone is working with same strategy and shared context that compounds. Under the hood, the repo builds a context graph (which updates with every session and every tool that you connect) — strategy, segments, metrics, decisions, feedback, and plans all linked together. Every artifact you create adds a node. Every decision you log adds an edge. The graph is what lets the AI reason across your product, not just within a single prompt.

What that looks like in practice:

1\. Drop a strategy doc into the knowledge layer. Agent derives key metrics. A subagent builds the Databricks dashboard. Strategy → metrics → dashboard — same graph, no re-typing.

2\. I say "write a PRD for X." The AI already has our segments, positioning, and strategic pillars from the graph. I edit and push — not rewrite from scratch.

3\. Monday: "plan my week." The agent reads my goals, quarterly priorities, and last 24 hours of Slack. Out comes a daily plan — P0s, P1s, P2s. Tuesday: "plan my day" — it reshuffles based on what actually happened. The graph keeps it grounded in real commitments.

Clone the repo, open in Cursor, say "onboard." A few questions later you're set up — knowledge layer, skills, agents, rules. MCPs are optional. You can also contribute to the repo

[Github Repo] [https://lnkd.in/gaDrQgqs](<https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd.in%2FgaDrQgqs&urlhash=pxlB&trk=public_post-text>)

Message me or [Sachin G.](<https://www.linkedin.com/in/sachinkgupta1?trk=public_post-text>) if you want to talk about context graphs or PM OS.

  * ![No alternative text description for this image](https://media.licdn.com/dms/image/v2/D5622AQHFQXk8gc3tqQ/feedshare-shrink_2048_1536/B56Zz5LAaIKsAg-/0/1773706938634?e=2147483647&v=beta&t=2aU7gxbCJZUMO1M3nZm50NC9O5gOhfz7ZPSejKnA7W0)
