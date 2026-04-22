---
title: "I forked AutoResearch and adapted it to run on macOS..."
reader_id: "01kk6xek94d5x08j7dcpz32154"
notion_page_id: "34a4ebe7-f118-8165-a39d-c39ece3f4ae2"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kk6xek94d5x08j7dcpz32154"
source_url: "https://x.com/i/status/2030402705374728218/?rw_tt_thread=True"
author: "Artem Andreenko"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-07"
saved_at: "2026-03-08"
reading_time: "1 min"
summary: "I forked AutoResearch and adapted it to run on macOS using Metal. Welcome!"
content_hash: "ff57a16512f326eccea73d947c4dfda950149b8a2ac8fc0afb8a5753a0c8ba64"
---

I forked AutoResearch and adapted it to run on macOS using Metal. Welcome!

[github.com/miolini/autore…](<https://github.com/miolini/autoresearch-macos>)

![Image](https://pbs.twimg.com/media/HC1wd73aYAA643Q.png?name=orig)

![](https://pbs.twimg.com/profile_images/1296667294148382721/9Pr6XrPB.jpg)

[Andrej Karpathy](<https://twitter.com/karpathy>) [@karpathy](<https://twitter.com/karpathy>)

[ ](<https://twitter.com/karpathy/status/2030371219518931079>)

I packaged up the "autoresearch" project into a new self-contained minimal repo if people would like to play over the weekend. It's basically nanochat LLM training core stripped down to a single-GPU, one file version of ~630 lines of code, then:

  * the human iterates on the prompt (.md)
  * the AI agent iterates on the training code (.py)



The goal is to engineer your agents to make the fastest research progress indefinitely and without any of your own involvement. In the image, every dot is a complete LLM training run that lasts exactly 5 minutes. The agent works in an autonomous loop on a git feature branch and accumulates git commits to the training script as it finds better settings (of lower validation loss by the end) of the neural network architecture, the optimizer, all the hyperparameters, etc. You can imagine comparing the research progress of different prompts, different agents, etc.

<https://t.co/YCvOwwjOzF>

Part code, part sci-fi, and a pinch of psychosis :)

[Posted Mar 7, 2026 at 7:53PM](<https://twitter.com/karpathy/status/2030371219518931079>)
