---
title: "At this rate Andrej is going to make his own..."
reader_id: "01kjjazgabzbxeqgsb04wj7ye3"
notion_page_id: "34a4ebe7-f118-8196-8339-e37c41b117d1"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kjjazgabzbxeqgsb04wj7ye3"
source_url: "https://x.com/i/status/2027522318872789245/?rw_tt_thread=True"
author: "Numman Ali"
site: "X (formerly Twitter)"
tags: []
published: "2026-02-27"
saved_at: "2026-02-28"
reading_time: "2 mins"
summary: "Andrej Karpathy is experimenting with using AI agents to run a research lab. The agents can follow instructions but struggle to create good ideas or designs on their own. This setup shows promise but still needs improvement to work well."
content_hash: "1e792a5965fcf85ca8a800f50f89002f4be354e8f4d962c11b3f1eec4a527cf7"
---

At this rate Andrej is going to make his own AI Lab

His current set up has

\- 1 chief scientist

\- 8 independent solo researchers

\- 8 junior researchers

He clearly says not great but with someone of his caliber who says he can't make it work?

![](https://pbs.twimg.com/profile_images/1296667294148382721/9Pr6XrPB.jpg)

[Andrej Karpathy](<https://twitter.com/karpathy>) [@karpathy](<https://twitter.com/karpathy>)

[ ](<https://twitter.com/karpathy/status/2027521323275325622>)

I had the same thought so I've been playing with it in nanochat. E.g. here's 8 agents (4 claude, 4 codex), with 1 GPU each running nanochat experiments (trying to delete logit softcap without regression). The TLDR is that it doesn't work and it's a mess... but it's still very pretty to look at :)

I tried a few setups: 8 independent solo researchers, 1 chief scientist giving work to 8 junior researchers, etc. Each research program is a git branch, each scientist forks it into a feature branch, git worktrees for isolation, simple files for comms, skip Docker/VMs for simplicity atm (I find that instructions are enough to prevent interference). Research org runs in tmux window grids of interactive sessions (like Teams) so that it's pretty to look at, see their individual work, and "take over" if needed, i.e. no -p.

But ok the reason it doesn't work so far is that the agents' ideas are just pretty bad out of the box, even at highest intelligence. They don't think carefully though experiment design, they run a bit non-sensical variations, they don't create strong baselines and ablate things properly, they don't carefully control for runtime or flops. (just as an example, an agent yesterday "discovered" that increasing the hidden size of the network improves the validation loss, which is a totally spurious result given that a bigger network will have a lower validation loss in the infinite data regime, but then it also trains for a lot longer, it's not clear why I had to come in to point that out). They are very good at implementing any given well-scoped and described idea but they don't creatively generate them.

But the goal is that you are now programming an organization (e.g. a "research org") and its individual agents, so the "source code" is the collection of prompts, skills, tools, etc. and processes that make it up. E.g. a daily standup in the morning is now part of the "org code". And optimizing nanochat pretraining is just one of the many tasks (almost like an eval). Then - given an arbitrary task, how quickly does your research org generate progress on it?

![](https://pbs.twimg.com/profile_images/1629469939860946946/WUyBolSu.jpg)

[Thomas Wolf](<https://twitter.com/Thom_Wolf>) [@Thom_Wolf](<https://twitter.com/Thom_Wolf>)

[ ](<https://twitter.com/Thom_Wolf/status/2027421947999506722>)

How come the NanoGPT speedrun challenge is not fully AI automated research by now?

![](https://pbs.twimg.com/profile_images/1959245933268672512/oAdbl4gC.jpg)

[Larry Dial](<https://twitter.com/classiclarryd>) [@classiclarryd](<https://twitter.com/classiclarryd>)

[ ](<https://twitter.com/classiclarryd/status/2027228782483182059>)

New NanoGPT Speedrun WR at 88.1 (-1s) from [@ChrisJMcCormick](<https://twitter.com/ChrisJMcCormick>) , by optimizing kernels for transposed weights, removing the Block() abstraction, and tuning the prior PR on partitioned hyperconnections by reducing the lambda count. [github.com/KellerJordan/m…](<https://github.com/KellerJordan/modded-nanogpt/pull/233>)

![Image](https://pbs.twimg.com/media/HCIpVPFbcAAZETU.png?name=orig)

[Posted Feb 27, 2026 at 3:46AM](<https://twitter.com/classiclarryd/status/2027228782483182059>) [Posted Feb 27, 2026 at 4:33PM](<https://twitter.com/Thom_Wolf/status/2027421947999506722>)

[Posted Feb 27, 2026 at 11:08PM](<https://twitter.com/karpathy/status/2027521323275325622>)
