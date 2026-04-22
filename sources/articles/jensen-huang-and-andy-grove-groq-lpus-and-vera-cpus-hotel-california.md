---
title: "Jensen Huang and Andy Grove, Groq LPUs and Vera CPUs, Hotel California"
reader_id: "01km13hx2262xreq659rjdad91"
notion_page_id: "3464ebe7-f118-8107-a736-c563e85f10d6"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01km13hx2262xreq659rjdad91"
source_url: "https://stratechery.com/?p=18560"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2026-03-18"
saved_at: "2026-03-18"
reading_time: "11 mins"
summary: "GTC 2026 marked an important inflection point for Nvidia, as the company is selling multiple architectures, instead of focusing on just one GPU. The motivation is serve all needs and keep all customers."
content_hash: "ea7f605359e2b2d0816c0816fc3ecd8bdf1ed1774b82112883d468e20d0c92e1"
---

GTC 2026 marked an important inflection point for Nvidia, as the company is selling multiple architectures, instead of focusing on just one GPU. The motivation is serve all needs and keep all customers.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

It’s about that time for my annual spring vacation, but instead of taking an entire week off, I’m spreading it out to accommodate my travel schedule. Specifically, this is the last post of the week, and then [my posting schedule](<https://stratechery.com/stratechery-plus/schedule/>) will look like this:

  * Monday and Tuesday, March 23–24, no Update
  * Wednesday, March 25, Update
  * Thursday, March 26, Interview
  * Monday, March 30, no Update



I’ll be back on a normal schedule starting on Tuesday, March 31. In addition, Dithering and Sharp Tech episodes will stay on schedule (at least that’s the plan!). To that end, see you on those podcasts, and with another Update a week from today.

On to the Update:

### Jensen Huang and Andy Grove

Andy Grove, the co-founder and third CEO of Intel, wrote one of the canonical tech industry books that was entitled “[Only the Paranoid Survive](<https://www.penguinrandomhouse.com/books/72469/only-the-paranoid-survive-by-andrew-grove/>)“. He wrote in the Preface:

> I’m often credited with the motto, “Only the paranoid survive.” I have no idea when I first said this, but the fact remains that, when it comes to business, I believe in the value of paranoia. Business success contains the seeds of its own destruction. The more successful you are, the more people want a chunk of your business and then another chunk and then another until there is nothing left. I believe that the prime responsibility of a manager is to guard constantly against other people’s attacks and to inculcate this guardian attitude in the people under his or her management.

It was Grove and his exhortation of paranoia that I was reminded of this week while watching Nvidia CEO Jensen Huang’s [GTC Keynote](<https://www.youtube.com/watch?v=jw_o0xr8MWU>) and [interviewing him immediately afterwards](<https://stratechery.com/2026/an-interview-with-nvidia-ceo-jensen-huang-about-accelerated-computing/>). There was, as I noted in that interview, an aspect of the keynote that had a back-to-the-future component, particularly the discussion of CUDA and how it enabled a wide array of accelerated computing applications via a vertical Nvidia stack. That reminded me of pre-ChatGPT GTCs, where Nvidia would launch a host of new CUDA libraries, which were, at the end of the day, all bespoke manifestations of parallel computing on a common GPU architecture. I wrote in [a 2021 Update](<https://stratechery.com/2021/nvidias-gtc-keynote-the-nvidia-stack-the-omniverse/>):

> This is a useful way to think about Nvidia’s stack: writing shaders is like writing assembly, as in it’s really hard and very few people can do it well. CUDA abstracted that away into a universal API that was much more generalized and approachable — it’s the operating system in this analogy. Just like with operating systems, though, it is useful to have libraries that reduce duplicative work amongst programmers, freeing them to focus on their own programs. So it is with CUDA and all of those SDKs that Huang referenced: those are libraries that make it much simpler to implement programs that run on Nvidia GPUs.
>
> This is how it is that a single keynote can cover “Robots and digital twins and games and machine learning accelerators and data-center-scale computing and cybersecurity and self-driving cars and computational biology and quantum computing and metaverse-building-tools and trillion-parameter AI models”; most of those are new or updated libraries on top of CUDA, and the more that Nvidia makes, the more they can make.

The most momentous announcements from this year’s GTC, however, were not new libraries for leveraging a common GPU architecture: rather, they were two new racks with two entirely new kinds of chips. That strikes me as a pretty big shift — a strategic inflection point, if you will. And, to return to Grove, it was in a chapter about navigating strategic inflection points that he returned to his titular phrase:

> If competition is chasing you (and they always are — this is why “only the paranoid survive”), you only get out of the valley of death by outrunning the people who are after you. And you can only outrun them if you commit yourself to a particular direction and go as fast as you can. You could argue that, since they are chasing you, you should give yourself all sorts of alternative directions — in other words, hedge. I say, “No.” Hedging is expensive and dilutes commitment. Without exquisite focus, the resources and energy of the organization will be spread a mile wide — and they will be an inch deep.
>
> Second, while you’re going through the valley of death, you may think you see the other side, but you can’t be sure whether it’s truly the other side or just a mirage. Yet you have to commit yourself to a certain course and a certain pace, otherwise you will run out of water and energy before long. If you’re wrong, you will die. But most companies don’t die because they are wrong; most die because they don’t commit themselves. They fritter away their momentum and their valuable resources while attempting to make a decision. The greatest danger is in standing still.

One year ago at GTC 2025 Huang gave a full-throated defense of Nvidia’s one-GPU-to-do-it-all approach in the face of increased concern about the threat that ASICs represented to Nvidia’s massive margins. [I highly suggest reading the Update I wrote at the time](<https://stratechery.com/2025/nvidia-gtc-and-asics-the-power-constraint-the-pareto-frontier/>), which includes a long transcription of Huang’s argument, but to summarize:

  * As inference came to dominate overall workloads there would be a strong push by the hyperscalers in particular to design ASICs (application-specific integrated circuits) that could theoretically be faster than more general-purpose GPUs, and also cheaper because they avoided Nvidia’s margins.
  * Huang’s first argument against this future was that as long as power was the limiting factor, maximizing revenue would depend on having the highest performance-per-watt, which Nvidia would continue to maintain thanks to its lead in not just chips but also systems design.
  * Huang’s second argument was that maximizing efficiency would require balancing throughput and latency (which are fundamentally at odds), and that (1) the generalizable nature of GPUs were better suited to covering the Pareto Frontier and (2) Nvidia’s new Dynamo software would disaggregate inference into component parts, leveraging different GPUs optimized in different ways to deliver superior performance-per-watt. ASICs, on the other hand, would, by their nature, only be able to target one spot on that frontier.



Huang brought back some of the same slides from last year to this year, but for a very different reason: Nvidia was announcing an entirely new kind of architecture thanks to [their don’t-call-it-an-acquisition of Groq](<https://stratechery.com/2026/nvidia-and-groq-a-stinkily-brilliant-deal-why-this-deal-makes-sense/>). In other words, the slides were the same but the thesis was the opposite: Huang was saying that for some workloads, one-GPU-to-do-it-all was _not_ enough. This strikes me as a strategic inflection point!

And, for good measure — and adhering to Grove’s advice — Groq wasn’t the only chip Nvidia announced it would be selling by the rack: you can now buy Vera CPU chips from Nvidia as well. Nvidia has, for the entire 20 year history of CUDA, been predicated on being a one architecture company; yes, the company actually sells a multitude of other chips, from various networking chips to storage management to CPUs paired to its GPUs, but that was all in the service of one GPU architecture that undergirded everything. Now, however, Nvidia is selling three distinct architectures, and I think the motivation is clear: Huang isn’t going to give up Nvidia’s dominant position without a fight; he’s certainly not going to stand still.

### Groq LPUs and Vera CPUs

I wrote about Groq’s unique architecture [in this 2024 Update](<https://stratechery.com/2026/nvidia-and-groq-a-stinkily-brilliant-deal-why-this-deal-makes-sense/>), but to summarize, by using on-die SRAM and defining scheduling and data movement at compiler time, instead of dynamically, Groq chips can use much simpler computation units to execute the token-by-token steps of LLM inference with much lower latency and far more determinism — an especially valuable advantage given that generation is serial at the dependency level.

The downside of Groq’s approach is that because SRAM is actually transistors on the same die as the processors, its chips don’t have much memory _and_ that memory is extremely expensive; Cerebras, which in broad strokes uses a similar architecture, solves that problem by making wafer-sized chips, which are exceptionally expensive. On the flipside, to get a usable Groq system required multiple chips networked together, which carried its own high costs and much more complexity.

The problem, however, is that while you need memory to hold the model weights, you also need memory to hold the KV cache — where the context is stored — and KV cache grows linearly with each token, which means the memory requirements increase. That means reasoning models significantly increase the amount of memory needed for KV cache, above and beyond the push for ever larger context windows.

The way Nvidia is solving this issue is very clever. To restate [Huang’s explanation in yesterday’s interview](<https://stratechery.com/2026/an-interview-with-nvidia-ceo-jensen-huang-about-accelerated-computing/>):

  * Vera Rubin chips — i.e. Nvidia’s regular GPU architecture — will handle prefill. This is the part of the process where everything the LLM needs to understand is encoded into a state the model can read. This includes the request, a relevant codebase, documents, the results of web searches, etc. This process is highly parallelizable and well-suited to traditional GPUs.
  * The first part of decode (where tokens are actually produced) entails reading the KV cache to make the attention calculation. A Groq-like architecture can do this extremely quickly, but this is where the memory limitations in the face of a large KV cache are a problem. To that end, while traditional GPUs have higher latency, Vera Rubin not only has much more memory but also is [designed to control an entire memory hierarchy to manage KV cache specifically](<https://stratechery.com/2026/nvidia-at-ces-vera-rubin-and-ai-native-storage-infrastructure-alpamayo/>). That’s why Nvidia is using Vera Rubin for this part of decode.
  * The second part of decode is the feed-forward computation over the model weights to produce logits (basically scores over vocabulary that will go into final token selection). Here the memory requirements are bounded and predictable, since it is defined by the size of the relevant model weight shards, which is to say this is the best place to take advantage of Groq’s approach without blowing through its memory limitations.



After this process, the model considers the logits, selects the next token, appends its K/V state to the cache, and starts all over again — the fact this happens for every single token explains why significantly speeding up even one part of the process ends up with significant overall gains.

Nvidia’s approach is probably not the absolute lowest-latency path for pure token generation; a more specialized Groq- or Cerebras-like design might be faster for narrower decode workloads, but only if the KV cache could fit within the available memory. That, however, is why Nvidia’s approach is much more usable, particularly for very high context workflows like coding, where KV cache management is actually the biggest challenge — assuming, of course, you can handle the complexity of passing this information at extremely high speeds between different architectures. That, though, is exactly what Nvidia is good at.

The other new chip — which is not technically new — is the Vera CPU. Nvidia previously announced the Vera CPU in the same context that it introduced the Grace CPU: the latter was paired with first Hopper and then Blackwell GPUs, and the former with the Rubin GPU. The reason why GPUs need CPUs is because the CPU manages the actual flow of data in and out of the GPU as well as overall orchestration; the reason why Nvidia designed their own CPUs is because the most important thing in terms of maximizing their GPU’s performance is minimizing the amount of time they are waiting for data, and Nvidia wanted to design a CPU focused on that exact use case.

However, just as the rise of reasoning models necessitated new approaches to memory hierarchies to manage KV cache, the rise of agents — which aren’t models, but rather software that uses models, along with other deterministic tools — is potentially a limiting factor in how often GPUs are utilized. I wrote about how [agents were a big opportunity for Intel and AMD](<https://stratechery.com/2026/intel-earnings-the-agentic-opportunity-intels-mistaken-pessimism/>) earlier this year, but as Huang told me yesterday, even if there were enough CPUs to satisfy demand, he doesn’t think CPUs designed for web serving are good for agents, particularly if the goal is to keep your GPUs busy. Thus the new Vera rack offering.

I suspect Huang is right. I also think that Huang is paranoid that fully realizing the performance-per-watt advantages of Nvidia chips means taking on this question of idle GPUs head-on. If the actual limiting factor for AI is CPUs, then that means there is a performance umbrella for not-as-fast-but-much-cheaper ASICs; maintaining Nvidia margins means doing everything possible to realize that increased efficiency, just as maintaining Nvidia margins means selling an entirely new architecture for a very specific inference use case.

### Hotel California

I asked Huang at the end of the Interview if the company was being stretched too thin, and this was how he answered:

> The reason why Nvidia can move so fast is because we always have a unifying theory for the company, and that’s my job, I need to come up with a unifying theory for what’s important and why things connect together and how they connect together and then create an organization, an organism that’s really, really good at delivering on that unifying theory.
>
> And so the unifying theory for Nvidia is actually fairly simple. On the one hand, we have the computing platform, the software platform that’s related to CUDA-X. On the other hand, we’re a computing systems company, we optimize things vertically, we apply extreme co-design across the stack and all the different components of a computer and now that computer is a platform of ours and we integrate that platform into all the clouds and to all the OEMs and then we have another platform that’s now the data center platform, or the AI factory platform.
>
> So once you have a unifying theory about what Nvidia builds and how it goes about doing it — and I used the keynote to kind of tell that story even partly to our own employees.

The funny thing about that answer is that there really wasn’t a unifying theory presented, unless the answer is that we do everything, which doesn’t really address the “stretched too thin” concerns. And, honestly, I think that’s probably correct: the unifying theory that I took away from yesterday’s presentation was Huang’s determination to leave no openings for alternatives.

If Nvidia GPUs are not fast enough for some inference use cases, then Nvidia will offer a new architecture; if CPUs aren’t fast enough to realize the speed of Nvidia’s offerings, then Nvidia will sell CPUs. If China — [which apparently will now allow the sale of H200s](<https://www.reuters.com/world/china/chinese-authorities-approve-nvidias-h200-ai-chip-sales-source-says-2026-03-18/>) — is threatening to build an alternative stack, then Nvidia will lobby Washington and allocate capacity to serve that market and prevent an alternative software to CUDA to gain traction.

Nvidia, thanks to their relentless chip development, investment in CUDA, and acquisition of Mellanox, has had by far the best offering for AI; everyone checked in, and Nvidia became the most valuable company in the world. Huang, however, is paranoid about anyone checking out, and will do whatever is necessary to make sure no one can leave.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *
