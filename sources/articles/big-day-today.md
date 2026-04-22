---
title: "Big day today"
reader_id: "01kpa8nnx2a8gv4q2j8d7jn89w"
notion_page_id: "34a4ebe7-f118-81f2-81c7-d96e43d9746b"
category: "tweet"
source_type: "Reader Share Sheet iOS"
reader_url: "https://read.readwise.io/read/01kpa8nnx2a8gv4q2j8d7jn89w"
source_url: "https://x.com/kwindla/status/2044268295692661069/?s=12&rw_tt_thread=True"
author: "kwindla"
site: "X (formerly Twitter)"
tags: []
published: "2026-04-15"
saved_at: "2026-04-16"
reading_time: "2 mins"
summary: "Pipecat version 1.0 is a popular AI framework for real-time, multi-modal applications. The new Pipecat Subagents library helps run many AI tasks in parallel with shared context. A fun game called Gradient Bang uses this tech and lets players manage multiple AI models in a space trading setting."
content_hash: "962c2580565e54bae73d596860bc1750bf7ce3d81769d875844db4aa5574ce55"
---

Big day today. Pipecat version 1.0. Two years in the making. The most widely used framework for voice agents, but not just voice agents. Pipecat is a framework for realtime, multi-modal, multi-model AI applications. Contributions from NVIDIA, all the foundation labs, AWS, GCP, and Azure. Used by thousands of startups, scale-ups, and enterprises.

Pipecat Subagents v0.1.0. A new library for sub-agent orchestration. Which is just a fancy way of saying running lots of inference loops in parallel, with partially shared context. The basic architecture of Pipecat Subagents is an event bus that works locally, and over the network.

And Gradient Bang. The side project that broke containment. Built with Pipecat and Pipecat Subagents. Gradient Bang was actually the proving ground for the early Subagents work. But ... it's also a really fun game.

![Image](https://pbs.twimg.com/media/HF6y2G4bwAArvIg.jpg?name=orig)

![Image](https://pbs.twimg.com/media/HF6y29xasAAydpn.jpg?name=orig)

![](https://pbs.twimg.com/profile_images/1790772534914551808/YpwkVUIl.jpg)

[kwindla](<https://twitter.com/kwindla>) [@kwindla](<https://twitter.com/kwindla>)

[ ](<https://twitter.com/kwindla/status/2044106314612408437>)

Sub-agents in (latent) space!

We’ve been working on a side project.

As far as I know, this is the first massively multiplayer, completely LLM-driven game. Come play Gradient Bang with us. See if you can catch me on the leaderboard.

This whole thing started because I wanted to explore a bunch of things I’m currently obsessed with, in an application of non-trivial size, that felt both new and old at the same time.

So … a retro-style space trading game built entirely around interacting with and managing multiple LLMs. Factorio, but instead of clicking, you cajole your ship AI into tasking other AIs to do things for you.

Some of the things we’ve been thinking about as we hack on Gradient Bang:

  * Sub-agent orchestration
  * Partial context sharing between multiple LLM inference loops
  * Managing very long contexts, and episodic memory across user sessions
  * World events and large volumes of structured data input as part of human/agent conversations
  * Dynamic user interfaces, driven/created on the fly by LLMs
  * And, of course, voice as primary input



If you’ve been building coding harnesses, or writing Open Claw agents, or doing pretty much anything that pushes the boundaries of AI-native development these days, you’re probably thinking about these things too!

This is all built with [@pipecat_ai](<https://twitter.com/pipecat_ai>), the back end is [@supabase](<https://twitter.com/supabase>), the React front end is deployed to [@vercel](<https://twitter.com/vercel>), and all the code is open source.

Your browser does not support the video tag.

[Posted Apr 14, 2026 at 5:31PM](<https://twitter.com/kwindla/status/2044106314612408437>)

* * *

Pipecat 1.0 Changelog: [github.com/pipecat-ai/pip…](<https://github.com/pipecat-ai/pipecat/blob/main/CHANGELOG.md>)

Pipecat Subagents: [github.com/pipecat-ai/pip…](<https://github.com/pipecat-ai/pipecat-subagents>)

Play the game: [gradient-bang.com](<https://www.gradient-bang.com/>)

Gradient Bang code: [github.com/pipecat-ai/gra…](<https://github.com/pipecat-ai/gradient-bang>)
