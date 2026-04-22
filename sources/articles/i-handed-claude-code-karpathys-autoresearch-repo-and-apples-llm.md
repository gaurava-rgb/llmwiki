---
title: "I handed Claude Code @karpathy's autoresearch repo and Apple's \"LLM..."
reader_id: "01km3cvp8m03ykftshjkpk9v4c"
notion_page_id: "34a4ebe7-f118-81c2-bd3b-e77240eddecb"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01km3cvp8m03ykftshjkpk9v4c"
source_url: "https://x.com/i/status/2033940227736100873/?rw_tt_thread=True"
author: "Dan Woods"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-17"
saved_at: "2026-03-19"
reading_time: "2 mins"
summary: "Dan Woods got the Qwen3.5-397B model running on his M3 Max with some custom optimizations, reaching about 6 tokens per second. He replaced Python with metal shaders to improve speed and reduce memory use. There is still room to optimize, especially with caching and hardware advantages."
content_hash: "57509088ad34f291efb23f7ba3ccc72bcf16a24e64a5e178707de9c971a4ebda"
---

I handed Claude Code [@karpathy](<https://twitter.com/karpathy>)'s autoresearch repo and Apple's "LLM in a Flash" paper, told it to get Qwen3.5-397B running on my M3 Max 48GB... it did!

![Image](https://pbs.twimg.com/media/HDoBdQPXAAAf448.png?name=orig)

* * *

It ran for ~5 hours and got 1 tok/s. Another ~3 hours of optimizing and it's at 4.74 tok/s using 5.9GB RAM

* * *

[@karpathy](<https://twitter.com/karpathy>) btw [@awnihannun](<https://twitter.com/awnihannun>) \- wouldn't have been possible without MLX

* * *

[@karpathy](<https://twitter.com/karpathy>) Chat is very stable at about 4 tok/s, which isn't unusable except to say that Qwen3.5-397B-A17B really likes to think a lot, so some system prompt tuning was important... we had to dump python entirely, the GIL was killing us, so we have custom metal shaders now.

![Image](https://pbs.twimg.com/media/HDp-6d7bEAYloJb.jpg?name=orig)

* * *

Importantly, there's a ton of optimization yet to do w/ the end-to-end lifecycle... as you can see, prefill doesn't cache at all rn, so even if 4 tok/s is usable generally, in multi-turn it gets decimated by the prefill.

* * *

I'm not gonna do that right away though, because I think there's some Apple hardware advantages still on the table. Time to see how far we can push the NVMe controller!

* * *

Here's a short, simple demo of it running. We've landed at ~6tok/s, which is extremely usable. Minimal GPU pressure, minimal memory (between 6-10GB). Disk and page cache aren't saturated yet. There's still room to go. But, I decided to spend more of last night working on the

Your browser does not support the video tag.

* * *

In hindsight, it should’ve been obvious that the MoE would be worst case scenario for this since the layers are non-deterministic and cannot be made contiguous on disk, so page caching and readahead hints aren’t fully optimized. A fat, dense, 400B model can easily run 4x speed.

* * *

Article published [x.com/danveloper/sta…](<https://x.com/danveloper/status/2034353876753592372?s=20>)
