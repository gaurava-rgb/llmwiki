---
title: "1/4 LLMs solve research grade math problems but struggle with..."
reader_id: "01kksg03ppdd3zhpa3v8dr9mqf"
notion_page_id: "34a4ebe7-f118-818f-a827-ccc719781cb7"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kksg03ppdd3zhpa3v8dr9mqf"
source_url: "https://x.com/i/status/2031845134577406426/?rw_tt_thread=True"
author: "Christos Tzamos"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-11"
saved_at: "2026-03-15"
reading_time: "1 min"
summary: "A quarter of large language models can solve hard math problems but struggle with simple calculations. The authors built a computer inside a transformer to run programs quickly and accurately. This new method lets the model do all computations itself, making it much faster and more efficient."
content_hash: "57e9c389406912b410e86e53c324b11a6334425863efc725da51e16afa34e80e"
---

1/4 LLMs solve research grade math problems but struggle with basic calculations. We bridge this gap by turning them to computers.

We built a computer INSIDE a transformer that can run programs for millions of steps in seconds solving even the hardest Sudokus with 100% accuracy

Your browser does not support the video tag.

* * *

2/4 The key limitation of LLMs is that standard attention is too slow for any practical computation.

We bypass this limitation with a new decoding path that allows for exponentially faster attention enabling almost constant work per token generation.

Your browser does not support the video tag.

* * *

3/4 Instead of using an external tool, the model executes the program directly via its transformer weights, producing an execution trace token by token and streaming results at more than 30k tokens/sec on a CPU.

All computation is done autoregressively inside the transformer!

Your browser does not support the video tag.

* * *

4/4 Read more at our blog post:

[percepta.ai/blog/can-llms-…](<https://www.percepta.ai/blog/can-llms-be-computers>)
