---
title: "\"yo Hermes, learn what the goat Professor Jiang said here..."
reader_id: "01km1311zymrdgzghx95z46aev"
notion_page_id: "34a4ebe7-f118-8181-b049-f86870b50396"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01km1311zymrdgzghx95z46aev"
source_url: "https://x.com/i/status/2034043483313275148/?rw_tt_thread=True"
author: "We"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-17"
saved_at: "2026-03-18"
reading_time: "1 min"
summary: "Professor Jiang shared important insights in a video for Hermes. We built a tool that transcribes videos from many sources quickly. This helps agents analyze and simulate markets using those transcripts."
content_hash: "911e93315e0640ac95cc0037dc01a9832e916d0a3464d41012d44e9188004f56"
---

"yo Hermes, learn what the goat Professor Jiang said here [VideoUrl] find markets that could be influeced and setup a simulation using predihermes (40 rounds 50 agents)."

[@NousResearch](<https://twitter.com/NousResearch>)

I built video-url-transcriber for Hermes

URL -> media fetch (yt-dlp) -> audio normalize (ffmpeg) -> local ASR (faster-whisper) -> timestamped JSON transcripts.

Now agents can transcribe YouTube/X/+any (not limited to yt like it used to) supported sources and feed transcripts straight into analysis/sim pipelines.

Skill below ;)
