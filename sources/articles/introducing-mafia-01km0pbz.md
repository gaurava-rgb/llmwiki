---
title: "Introducing Mafia!"
reader_id: "01km0pbzpeq5nb4w8w14e30sap"
notion_page_id: "34a4ebe7-f118-8130-b646-cef94db2f254"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01km0pbzpeq5nb4w8w14e30sap"
source_url: "https://x.com/i/status/2033958434631258152/?rw_tt_thread=True"
author: "Elliot Arledge"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-17"
saved_at: "2026-03-18"
reading_time: "1 min"
summary: "Elliot Arledge created a game called Mafia! using language models. He trained a model named Qwen3-8B on special hardware. The game includes roles like Mafia, Villager, Doctor, Detective, and Troll."
content_hash: "fc298b25e961d84b0da8291ee2c57e34667847af51d466050667b3de845d58b5"
---

Introducing Mafia!

[github.com/Infatoshi/mafia](<https://github.com/Infatoshi/mafia>)

After playing a bunch of Mafia in real life with friends and family, I figured I just had to kick off an RL run to see how language models would evolve and potentially reward hack.

I trained Qwen3-8B on H100s with the following roles:

>
>
>
> Mafia
>
> Villager
>
> Doctor
>
> Detective
>
> Troll




One file. One GPU. No frameworks beyond PyTorch + HuggingFace Transformers.
