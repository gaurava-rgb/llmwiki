---
title: "Super interesting way to use autoresearch"
reader_id: "01kkfb3c0svydyxneatp841emn"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kkfb3c0svydyxneatp841emn"
source_url: "https://x.com/i/status/2031566709291888693/?rw_tt_thread=True"
author: "Morgan"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-11"
saved_at: "2026-03-11"
reading_time: "1 min"
summary: "Autonomous agents can now improve machine learning models by running many experiments on their own. Andrej Karpathy showed that this approach made his model better and faster without manual tuning. This method could help researchers optimize many tasks efficiently in the future."
content_hash: "9a8c6d68606b436d7fb331f0227d7582ae7a9b37465fa30f5e457eea67a00c64"
---

Super interesting way to use autoresearch.

![](https://pbs.twimg.com/profile_images/1984693297840111616/wpQy5aKy.jpg)

[snwy](<https://twitter.com/snwy_me>) [@snwy_me](<https://twitter.com/snwy_me>)

[ ](<https://twitter.com/snwy_me/status/2031347002773221673>)

autoresearch really interested me, despite me not being "all-in" on agents yet. i wanted to get started with running auto experiments

i looked to existing tools to serve as a harness but each one had its problems. so i made one

introducing Helios for autonomous ML research

![Image](https://pbs.twimg.com/media/HDCu7nuaMAUp3yT.jpg?name=orig)

![](https://pbs.twimg.com/profile_images/1296667294148382721/9Pr6XrPB.jpg)

[Andrej Karpathy](<https://twitter.com/karpathy>) [@karpathy](<https://twitter.com/karpathy>)

[ ](<https://twitter.com/karpathy/status/2031135152349524125>)

Three days ago I left autoresearch tuning nanochat for ~2 days on depth=12 model. It found ~20 changes that improved the validation loss. I tested these changes yesterday and all of them were additive and transferred to larger (depth=24) models. Stacking up all of these changes, today I measured that the leaderboard's "Time to GPT-2" drops from**2.02 hours to 1.80 hours** (~11% improvement), this will be the new leaderboard entry. So yes, these are real improvements and they make an actual difference. I am mildly surprised that my very first naive attempt already worked this well on top of what I thought was already a fairly manually well-tuned project.

This is a first for me because I am very used to doing the iterative optimization of neural network training manually. You come up with ideas, you implement them, you check if they work (better validation loss), you come up with new ideas based on that, you read some papers for inspiration, etc etc. This is the bread and butter of what I do daily for 2 decades. Seeing the agent do this entire workflow end-to-end and all by itself as it worked through approx. 700 changes autonomously is wild. It really looked at the sequence of results of experiments and used that to plan the next ones. It's not novel, ground-breaking "research" (yet), but all the adjustments are "real", I didn't find them manually previously, and they stack up and actually improved nanochat. Among the bigger things e.g.:

  * It noticed an oversight that my parameterless QKnorm didn't have a scaler multiplier attached, so my attention was too diffuse. The agent found multipliers to sharpen it, pointing to future work.
  * It found that the Value Embeddings really like regularization and I wasn't applying any (oops).
  * It found that my banded attention was too conservative (i forgot to tune it).
  * It found that AdamW betas were all messed up.
  * It tuned the weight decay schedule.
  * It tuned the network initialization.




This is on top of all the tuning I've already done over a good amount of time. The exact commit is here, from this "round 1" of autoresearch. I am going to kick off "round 2", and in parallel I am looking at how multiple agents can collaborate to unlock parallelism.

<https://t.co/WAz8aIztKT>

All LLM frontier labs will do this. It's the final boss battle. It's a lot more complex at scale of course - you don't just have a single train. py file to tune. But doing it is "just engineering" and it's going to work. You spin up a swarm of agents, you have them collaborate to tune smaller models, you promote the most promising ideas to increasingly larger scales, and humans (optionally) contribute on the edges.

And more generally, _any_ metric you care about that is reasonably efficient to evaluate (or that has more efficient proxy metrics such as training a smaller network) can be autoresearched by an agent swarm. It's worth thinking about whether your problem falls into this bucket too.

[Posted Mar 9, 2026 at 10:28PM](<https://twitter.com/karpathy/status/2031135152349524125>)

[Posted Mar 10, 2026 at 12:30PM](<https://twitter.com/snwy_me/status/2031347002773221673>)
