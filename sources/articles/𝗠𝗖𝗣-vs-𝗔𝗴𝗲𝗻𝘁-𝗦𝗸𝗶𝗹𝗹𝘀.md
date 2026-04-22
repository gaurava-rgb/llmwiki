---
title: "𝗠𝗖𝗣 vs 𝗔𝗴𝗲𝗻𝘁 𝗦𝗸𝗶𝗹𝗹𝘀"
reader_id: "01kj89z1tehbzc8s069rnwf9qp"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kj89z1tehbzc8s069rnwf9qp"
source_url: "https://x.com/i/status/2026299415179223480/?rw_tt_thread=True"
author: "Victoria Slocum"
site: "X (formerly Twitter)"
tags: []
published: "2026-02-24"
saved_at: "2026-02-24"
reading_time: "1 min"
summary: "MCP uses fixed API calls for clear and predictable coding, while Agent Skills let the agent decide how to solve problems using natural language. Both are useful: MCP is best for direct infrastructure tasks, and Skills guide agent behavior. A new Agent Skills repository helps build AI apps and improve Weaviate code."
content_hash: "7985b189f5b7fbe95b6a5858ee0620d3099d591e5d9f1d96d54588bbfa295a94"
---

𝗠𝗖𝗣 vs 𝗔𝗴𝗲𝗻𝘁 𝗦𝗸𝗶𝗹𝗹𝘀

(Is one actually better than the other?)

If you've been following the vibe coding movement, you've probably experienced your coding agent not being able to code well with specialized tools or infrastructure. Legacy syntax, wrong parameters, inefficient patterns, leading to tons of debugging that often feels like you're going in circles.

Two solutions have emerged: 𝗠𝗖𝗣 (𝗠𝗼𝗱𝗲𝗹 𝗖𝗼𝗻𝘁𝗲𝘅𝘁 𝗣𝗿𝗼𝘁𝗼𝗰𝗼𝗹) and 𝗔𝗴𝗲𝗻𝘁 𝗦𝗸𝗶𝗹𝗹𝘀. But which one should you use?

𝗠𝗖𝗣 is pretty much just a standardized API gateway. Your agent makes a deterministic API call with fixed input/output schemas and gets a deterministic response back. It's clean and predictable.

𝗦𝗸𝗶𝗹𝗹𝘀 are different. When an agent uses a skill, it's interpreting natural language instructions about 𝘩𝘰𝘸 to accomplish something. The agent decides which skill to use, when, 𝘢𝘯𝘥 𝘩𝘰𝘸 to execute it. Less "call this function" and more "here's how to think about this problem."

So they 𝗯𝗼𝘁𝗵 have a place in agentic coding. Skills are great for behavioral guidance, MCP works better for the direct infrastructure calls.

We just released our Agent Skills repository to help coding agents create end-to-end AI apps and write better [@weaviate_io](<https://twitter.com/weaviate_io>) code. It includes:

![1️⃣](https://abs-0.twimg.com/emoji/v2/svg/31-20e3.svg)

1️⃣ 𝗪𝗲𝗮𝘃𝗶𝗮𝘁𝗲 𝗦𝗸𝗶𝗹𝗹𝘀 (/skills/weaviate): Focused scripts for schema inspection, data ingestion, Query Agent integration, and search operations

2️⃣ 𝗖𝗼𝗼𝗸𝗯𝗼𝗼𝗸𝘀 (/skills/weaviate-cookbooks): End-to-end project blueprints for building complete applications (Query Agent chatbots, multivector PDF RAG, various RAG patterns, DSPy agents)

Check it out here: <https://t.co/BDSX2b6IOR>

![2️⃣](https://abs-0.twimg.com/emoji/v2/svg/32-20e3.svg)
