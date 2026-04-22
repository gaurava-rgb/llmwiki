---
title: "Introducing Mafia!"
reader_id: "01km0pbzpeq5nb4w8w14e30sap"
notion_page_id: ""
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
content_hash: "b5a2ccb6dbf5ab6d69b5d39e9a33a29266b669c1d664c9fd7c028a5dcbf80e45"
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
