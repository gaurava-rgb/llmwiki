---
title: "Walter"
reader_id: "01k3c2yx3mmzed8qg7kqjzqcpc"
notion_page_id: "34a4ebe7-f118-816c-b151-c32f6fa45ead"
category: "email"
source_type: ""
reader_url: "https://read.readwise.io/read/01k3c2yx3mmzed8qg7kqjzqcpc"
source_url: "mailto:reader-forwarded-email/3282b84d3a297c0f3845cf2d0bbf778a"
author: "Rohit from Strange Loop Canon"
site: "Substack"
tags: []
published: "2025-08-23"
saved_at: "2025-08-23"
reading_time: "7 mins"
summary: "They trained a small model called Walter to write better tweet-sized takes by learning from social media engagement with reinforcement learning.  \nThey handled bias and sparsity by normalizing each author’s baseline and transferring from the single best similar post, plus light penalties and a KL leash.  \nSmall models expose reward hacking and force clearer reward design, and the same methods can apply to many other weak-signal tasks."
content_hash: "c862ad111c6d1ba02ca94e228292d720667f91899e4dbef5dbfb8591afb93de3"
---

Forwarded this email? [ Subscribe here ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cuc3RyYW5nZWxvb3BjYW5vbi5jb20vc3Vic2NyaWJlP3V0bV9zb3VyY2U9ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXN1YnNjcmliZSZyPTM4and2Jm5leHQ9aHR0cHMlM0ElMkYlMkZ3d3cuc3RyYW5nZWxvb3BjYW5vbi5jb20lMkZwJTJGd2FsdGVyIiwicCI6MTcxNzU0NzI5LCJzIjoyMzMwMTksImYiOnRydWUsInUiOjU0Mzc5MDMsImlhdCI6MTc1NTk3MjAwMiwiZXhwIjoyMDcxNTQ4MDAyLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.2tGLNkM-8GUybyyqZBtKe5IzLjkm0dtvnfekQBN4-0k?>) for more

#  [ Walter ](<https://substack.com/app-link/post?publication_id=233019&post_id=171754729&isFreemail=true&r=38jwv>)

###  experiments in rlnvr

[ Rohit Krishnan ](<https://substack.com/@strangeloopcanon>)

Aug 23

[ ![](https://substackcdn.com/image/fetch/$s_!69gL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aa4c22d-4b25-4bec-9587-3ec4d4dcce01_2228x2228.jpeg) ](<https://substack.com/@strangeloopcanon>)

[ ![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/app-link/post?publication_id=233019&post_id=171754729&isFreemail=true&submitLike=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/app-link/post?publication_id=233019&post_id=171754729&isFreemail=true&comments=true&r=38jwv&action=post-comment>)

[ ![](https://substackcdn.com/image/fetch/$s_!_L14!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideShare2%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/app-link/post?publication_id=233019&post_id=171754729&action=share&triggerShare=true&isFreemail=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvc3RyYW5nZWxvb3BjYW5vbi9wL3dhbHRlcj91dG1fc291cmNlPXN1YnN0YWNrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXJlc3RhY2stY29tbWVudCZhY3Rpb249cmVzdGFjay1jb21tZW50JnI9Mzhqd3YmdG9rZW49ZXlKMWMyVnlYMmxrSWpvMU5ETTNPVEF6TENKd2IzTjBYMmxrSWpveE56RTNOVFEzTWprc0ltbGhkQ0k2TVRjMU5UazNNakF3TWl3aVpYaHdJam94TnpVNE5UWTBNREF5TENKcGMzTWlPaUp3ZFdJdE1qTXpNREU1SWl3aWMzVmlJam9pY0c5emRDMXlaV0ZqZEdsdmJpSjkuSFRlYmlOQjJUZDl3SGdjaXpwY3B4WTFkWGwwcnhkMHcxTlpsd2J0dkYtayIsInAiOjE3MTc1NDcyOSwicyI6MjMzMDE5LCJmIjp0cnVlLCJ1Ijo1NDM3OTAzLCJpYXQiOjE3NTU5NzIwMDIsImV4cCI6MjA3MTU0ODAwMiwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.n1P9QeM7IWV1b1oEXRkxKxejE8OEpysRO0RkJjHIlqI>)

[ READ IN APP ![](https://substackcdn.com/image/fetch/$s_!ET-_!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideArrowUpRight%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://open.substack.com/pub/strangeloopcanon/p/walter?redirect=app-store>)

So, LLMs suck at Twitter. It’s kind of poetic, because twitter is full of bots. But despite sometimes trying to be naughty and sometimes trying to be nice they mostly still suck. It does remarkably well in some tasks and terribly in others. And writing is one of the hardest.

My friend [ Jon Evans ](<https://open.substack.com/users/54459-jon-evans>) and I were joking about this, considering words are at the very core of these miraculous machines, and thought hey wouldn’t it be nice if we could train a model to get better? We were first wondering if one could create an AI journalist that could actually write actual articles with actual facts and arguments and everything. Since we were thinking about an AI that could write, we called it Walter. Because of Bagehot. And Cronkite. We thought it had to be plausible, at least at a small scale. Which is why we tried the experiment ( [ paper here ](<https://substack.com/redirect/59ba902d-d129-46c2-a2b8-c73457bad363?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>) )¹.

This is particularly hard in a different way from math or coding, because how do you even know what the right answer is? Is there one? To get to a place where the training is easier and the rewards are richer, we thought of trying to write tweet sized takes on articles. So, Walter became a small, cranky, surprisingly competent engine that ingests social media data about articles, sees how people reacted, and trained itself via reinforcement learning to write better².

As Eliot once said, “Between the idea / And the reality / … falls the Shadow.” this was us trying to light a small lamp in there using RLNVR: our cheeky acronym for “reinforcement learning from non-verified rewards”.

Now, why small models? Well, a big reason, beyond being GPU poor, is that big models are resilient. They're like cars with particularly powerful shock absorbers, they are forgiving if you make silly assumptions. Small models are not. They are dumb. And precisely because they are dumb, you are forced to be smart.

> What I mean is that if you really want to understand something, the best way is to try and explain it to someone else. That forces you to sort it out in your own mind. And the more slow and dim-witted your pupil, the more you have to break things down into more and more simple ideas. And that’s really the essence of programming. By the time you’ve sorted out a complicated idea into little steps that even a stupid machine can deal with, you’ve certainly learned something about it yourself. The teacher usually learns more than the pupil  ³  .

This also makes reward modelling particularly interesting. Because anytime you think you have come up with a good reward model, if there is any weakness or flaw in how you measure your reward, a small model will find it and exploit it ruthlessly. Goodhart’s Law is not just for management.

This is not to say that only small models do that; of course we have seen large models [ reward hack ](<https://substack.com/redirect/b5e05825-328e-4358-b012-b4c67f8aaf8e?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>) and learn lessons they were not meant to. But it is fascinating to see a 500 million parameter model learn that it can trick your carefully designed evaluation rubric just by outputting tokens _just_ _so_ . It drives home just how powerful transformers actually are, because it doesn't matter how complicated a balanced scorecard you create; they will find a way to hack it. Tweaking specific weights given to different elements, fighting with a sampling bias towards articles with enough skeets, penalties and thresholds for similarities … all grist for their mill.

We should also say, social media engagement data is magnificently broken as a training signal. It’s sort of “well known”, but it’s hard to imagine exactly how bad until you try and use it. We first ingested Bluesky skeets plus their engagement signals (likes, reposts, replies). Since we wanted actual signal, we decided to use the URL as the organizer: we group all the skeets that point at the same URL, then ask the model to produce a fresh skeet for that article. For the reward, we use embeddings to calculate the most similar historic posts (this worked best), then sanity check, and then rank based on how well those posts did.

The outside world in this instance, as in many, has its problems. For instance:

  * Bias. Big accounts seem “better,” in that they get more and more interesting reactions, than small accounts who post very similar things. The Matthew Effect holds true in social media. To solve that, we had to do baseline normalization: Score a post relative to its author’s usual. Raw engagement minus the author’s baseline turns “how big is your account?” into “was this unusually good for you?”.
  * Sparsity. You get one post and one outcome, not ten A/B variants. And for that we tried max-based semantic transfer: For a new post, find the  _single most similar_ historical post about the same article and reward the similarity to that top performer. The max transfer mattered more than we expected. In this domain, the right teacher is a specific great prior, not the average of pretty‑good priors.



But this messy, biased, sparse signal is the only feedback that exists. The world doesn't hand out clean training labels. It hands you whatever people actually do, and you have to figure out how to learn from that.

Together, this turned a one-shot, messy outcome into a dense signal. We used GRPO first to train, though later we upgraded to train with GSPO with clipping and a KL leash to keep voice anchored⁴. We also added UED (Unsupervised Environment Design) so the curriculum self-organizes: to pick link targets where the policy shows regret/variance, and push there⁵.

Before training, the model usually hedged and link-dumped and added a comical number of hashtags. After training it was clearly much better. It proposed stakes, hinted at novelty, and tagged sparingly. When we A/B tested the same URL, the trained outcome is the one you’d actually post. Example:

  * Before (the base model): 🚀 SpaceX's Starship successfully landed at Cape Canaveral! 🚀 #SpaceX #Starship #CapeCanaveral Landing 🚀 #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX #SpaceX
  * After (the trained model): 🚀 SpaceX's Starship has successfully landed at Cape Canaveral, marking a key milestone toward future missions. #SpaceX #Starship #landing #Mars



LLMs love adding hashtags to tweets a lot. In the short runs, those didn’t entirely disappear, but did reduce a lot. And became better. Still, I admit I do have a soft spot for the first one for its sheer enthusiasm! Similarly, just for fun, here’s one about tariffs:

  * Before: A major retro handheld maker has stopped all U.S. shipments over tariffs… #retrohandheld #retrohandheld #retrohandheld #tariffs #trade
  * After: 🎮 A top retro handheld brand just paused U.S. shipments due to tariffs. Big ripple for imports, modders, and collectors. What’s your go-to alternative? #retrogaming #tariffs



But the most interesting part for us was that the pattern extends anywhere you have weak, messy signals, which is, well, most of real life. So the ideas here should theoretically also extend to other fields:

  * Creative writing: optimize for completion/saves; transfer from prior hits.
  * Education: optimize for retention/time-on-task; transfer from explanations that helped.
  * Product docs/UX: optimize for task completion/helpfulness; baseline by product area and release.
  * Research comms: optimize for expert engagement/citations; baseline by venue/community.



Take the raw data; normalize away obvious bias; transfer what worked via similarity however you want to calculate or analyse that; keep the loop numerically stable; and add small, legible penalties to deter degenerate strategies. And be extremely, extremely, vigilant about the model reward hacking. In subtle and obvious ways this will happen, it’s closer to crafting a story than writing a program. It also gives you a visceral appreciation of the bitter lesson, and makes you aware of the voracious appetite of these models to learn [ anything ](<https://substack.com/redirect/9565bd57-4a47-4ba5-bde3-3afd7a426dfd?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>) that you throw at them by any means necessary.

The next few years are going to see an absolute “managerial explosion” where we try to figure out better rubrics and rating systems, including using the smartest models to rate themselves, as we train models to do all sorts of tasks. This whole project is about the limits of current approaches and smaller models. When GPT-5 writes good social posts⁶, you can't tell if it learned general principles or just memorized patterns.

When a 500M model succeeds at a tiny task, all offline on your laptop where you mostly surf Twitter, it feels kind of amazing. Do check out the [ paper ](<https://substack.com/redirect/59ba902d-d129-46c2-a2b8-c73457bad363?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>) . Like intelligence truly can be unbounded, and you will soon have a cyberpunk world where models will be run anywhere and everywhere for tasks both mundane and magnificent.

1

After writing this we came across the recent Gemini 2.5 [ report ](<https://substack.com/redirect/ca5ecb87-27c8-4945-b8ae-27954a09f341?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>) , echoing the same instinct at a very different scale: tight loops that let models learn from imperfect, real interactions. Which was cool!

2

Note that “better” here does not only mean “optimize engagement at all costs.” Instead it’s the far more subtle “learn the latent rubric of what reads well and travels in this odd little medium.”

3

“It would be hard to learn much less than my pupils without undergoing a prefrontal lobotomy.”

4

Maybe an example can help. Ten people posted the same article about SpaceX. Normalize each author’s engagement by their baseline (e.g., 45 vs 20 → +25; 210 vs 200 → +10; 12 vs 5 → +7). Embed all posts. For a new candidate, compute cosine similarity to each and take max(similarity × normalized weight). If the best match has sim 0.82 and weight 0.9, reward ≈ 0.74. No live A/B; the signal comes from “be like the best thing that worked.”

5

Early training followed the classic arc: diverse exploration → partial convergence → collapse risk. With GSPO-style normalization, a small KL guardrail, and light penalties, the loop stays open and outputs nudge toward historical winners.

6

*If

_If you liked this essay from[ Strange Loop Canon ](<https://substack.com/redirect/811220ae-dcf6-40ad-bde0-5bcb5f749baa?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>) , please share it with someone you think might like it! Or, you know, post on Twitter I guess .. that works too! _

[ Share ](<https://substack.com/app-link/post?publication_id=233019&post_id=171754729&action=share&triggerShare=true&isFreemail=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) Like ](<https://substack.com/app-link/post?publication_id=233019&post_id=171754729&isFreemail=true&submitLike=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) Comment ](<https://substack.com/app-link/post?publication_id=233019&post_id=171754729&isFreemail=true&comments=true&r=38jwv&action=post-comment>)

[ ![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) Restack ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvc3RyYW5nZWxvb3BjYW5vbi9wL3dhbHRlcj91dG1fc291cmNlPXN1YnN0YWNrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXJlc3RhY2stY29tbWVudCZhY3Rpb249cmVzdGFjay1jb21tZW50JnI9Mzhqd3YmdG9rZW49ZXlKMWMyVnlYMmxrSWpvMU5ETTNPVEF6TENKd2IzTjBYMmxrSWpveE56RTNOVFEzTWprc0ltbGhkQ0k2TVRjMU5UazNNakF3TWl3aVpYaHdJam94TnpVNE5UWTBNREF5TENKcGMzTWlPaUp3ZFdJdE1qTXpNREU1SWl3aWMzVmlJam9pY0c5emRDMXlaV0ZqZEdsdmJpSjkuSFRlYmlOQjJUZDl3SGdjaXpwY3B4WTFkWGwwcnhkMHcxTlpsd2J0dkYtayIsInAiOjE3MTc1NDcyOSwicyI6MjMzMDE5LCJmIjp0cnVlLCJ1Ijo1NDM3OTAzLCJpYXQiOjE3NTU5NzIwMDIsImV4cCI6MjA3MTU0ODAwMiwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.n1P9QeM7IWV1b1oEXRkxKxejE8OEpysRO0RkJjHIlqI>)

© 2025 Strange Loop Canon
548 Market Street PMB 72296, San Francisco, CA 94104
[ Unsubscribe ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cuc3RyYW5nZWxvb3BjYW5vbi5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpvMU5ETTNPVEF6TENKd2IzTjBYMmxrSWpveE56RTNOVFEzTWprc0ltbGhkQ0k2TVRjMU5UazNNakF3TWl3aVpYaHdJam94TnpnM05UQTRNREF5TENKcGMzTWlPaUp3ZFdJdE1qTXpNREU1SWl3aWMzVmlJam9pWkdsellXSnNaVjlsYldGcGJDSjkuODJIVTJCVHBlSDlFWVJjVFpNU0ZkaThFSlppT2ozTklTbkJva1NsaFU4cyIsInAiOjE3MTc1NDcyOSwicyI6MjMzMDE5LCJmIjp0cnVlLCJ1Ijo1NDM3OTAzLCJpYXQiOjE3NTU5NzIwMDIsImV4cCI6MjA3MTU0ODAwMiwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.Y9VU64ygjsMAP7-lcllzKINpebDbMmHeTcYH_tgUVC8?>)

[ ![Start writing](https://substackcdn.com/image/fetch/$s_!LkrL!,w_270,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fpublish-button%402x.png) ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbnVwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290ZXImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9vdGVyJmZyZWVTaWdudXBFbWFpbD1nLmFyb3JhOTk1MzRAZ21haWwuY29tJnI9Mzhqd3YiLCJwIjoxNzE3NTQ3MjksInMiOjIzMzAxOSwiZiI6dHJ1ZSwidSI6NTQzNzkwMywiaWF0IjoxNzU1OTcyMDAyLCJleHAiOjIwNzE1NDgwMDIsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.C4AWFuPgSKKdo3AeGSILMJJMcMxjSd9iUOu53WsWAyc?>)
