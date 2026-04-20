---
title: "OpenAI and Broadcom, ChatGPT and XPUs, AMD and Nvidia"
reader_id: "01k7hxafzfxxep9e7awqm5t2m3"
notion_page_id: "3484ebe7-f118-81dc-9d48-ddb719f8f8ef"
reader_url: "https://read.readwise.io/read/01k7hxafzfxxep9e7awqm5t2m3"
source_url: "https://stratechery.com/2025/openai-and-broadcom-chatgpt-and-xpus-amd-and-nvidia/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-10-14"
saved_at: "2025-10-14"
reading_time: "7 mins"
summary: "OpenAI's deal with Broadcom makes perfect sense, because OpenAI already knows exactly what workloads it needs to optimize."
content_hash: "969b7ce55556f037a2614f0f6de2f04c7035ad84fbbc0f75c799b852d552f7ac"
---

OpenAI's deal with Broadcom makes perfect sense, because OpenAI already knows exactly what workloads it needs to optimize.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On [today’s episode of Dithering](<https://dithering.passport.online/>), John and I preview the National League Championship Series (Go Brewers!), and discuss Apple TV dropping the plus.

On to the Update:

### OpenAI and Broadcom

From the [Wall Street Journal](<https://www.wsj.com/tech/ai/openai-broadcom-forge-multibillion-dollar-chip-development-deal-58d930d1>):

> OpenAI and Broadcom are working together to develop and deploy 10 gigawatts of custom AI chips and computing systems over the next four years, a high-profile partnership aimed at satisfying some of the startup’s immense computing needs. OpenAI plans to design its own graphics processing units, or GPUs, which will allow it to integrate what it has learned from developing powerful artificial-intellligence models into the hardware that underpins future systems. As part of the agreement announced Monday, the chips will be co-developed by OpenAI and Broadcom and deployed by the chip company starting in the second half of next year. The new agreement will be worth multiple billions of dollars, people familiar with the matter said. The companies didn’t disclose financial terms.

Another day, another OpenAI deal, but this is one of the more interesting ones. Start with a mistake in this excerpt: this deal is almost certainly not for _GPUs_ , but _XPUs_. Now this is a tricky distinction to make, because a GPU _is_ an XPU, technically speaking; the term actually started with Intel and was used to describe basically any sort of processor beyond the CPU, which of course includes GPUs (Graphical Processing Units), but also TPUs (Tensor Processing Units), NPUs (Neural Processing Units), DPUs (Data Processing Units), VPUs (Vision Processing Units)…you get the idea.

Today, however, it is worth distinguishing GPUs from the rest of their XPU cohort, particularly since the graphical component is only a minor use case. You could actually keep the same acronym, and call it a generalizable parallel unit: what makes a GPU different from a CPU is that it is made up of a huge number of cores operating in parallel, but what makes it different from other XPUs is that it is programmable, which means it can be used across many different use cases — including use cases that haven’t yet been invented. Just look at CUDA: Nvidia released the first version of their GPU programming framework in 2007, a decade before LLMs were invented, but because of its programmability it was and remains essential to AI development today.

That, by extension, means that the best way to think about non-GPU XPUs is that they are much closer to ASICs — Application-Specific Integration Circuits. These are chips that are custom-built for a specific job; pure ASICs are not programmable at all, but XPUs as a broader category sit along a spectrum of flexibility and programmability. Ultimately, however, they are much less flexible than GPUs (which themselves are much less flexible than CPUs); the trade-off is that because they are custom-built for a specific use-case they are often much faster at that specific use-case, and also much simpler which makes them cheaper to manufacture (less complexity means smaller chips and higher yields). And, critically, there isn’t an Nvidia in the middle taking margin; Broadcom takes a cut of XPU sales, but a relatively small one, and then beyond that you just have to pay TSMC to make them.

Now, I don’t begrudge the Wall Street Journal the error; being pedantic about the precise definition of a “GPU” is probably a doomed enterprise, and again, it’s not like these are being used for graphics (although the fact they still are used for graphics speaks to their flexibility, as long as the job to be done is highly parallelizable). It’s probably inevitable that all AI chips will be referred to as GPUs in the long run, particularly in the mass media. Still, the distinction matters when it comes to this news item, and what it says about some of OpenAI’s other recent announcements.

### ChatGPT and XPUs

I wrote about ASICs in the context of Nvidia in March; from that [Update](<https://stratechery.com/2025/nvidia-gtc-and-asics-the-power-constraint-the-pareto-frontier/>):

> The concern for Nvidia is that while they have a lock on training, thanks to the scalability of their offerings, large cloud providers in particular will see the value in paying a lot less for ASICs for inference, particularly as inference becomes a larger and larger share of the AI market.
>
> The argument for inference a year ago was pretty straightforward: transformers are nearly a decade old, and appear to be the foundational architecture for AI for the foreseeable future. Everyone will load a model, put in a prompt, and get an answer out; you can design a chip that does exactly that for a lot less than you’ll pay Nvidia for a more generalized solution.
>
> The big change over the last year is the rise of reasoning models, starting with OpenAI’s o1, and for Huang reasoning formed the foundation of two arguments he put forward as to why Nvidia GPUs were a better option than ASICs.

Huang’s two arguments were power and flexibility. First, if the constraint on token output was power, than the most efficient solution would be worth more, even if that solution cost more up front; Huang obviously believes that Nvidia will win the efficiency game. Second, there is a trade-off between bandwidth and speed: generating tokens for many users means slower speeds for one user, and vice-versa. Nvidia GPUs, thanks to their flexibility and software layer, can handle both use cases, which makes their chips more useful and more likely to be fully utilized (and higher utilization means more leverage on your upfront costs).

I think that Huang’s arguments make sense in a vacuum, and apply to most Nvidia customers. OpenAI, however, is different, for one very obvious reason: they aren’t planning for theoretical use cases; they already have them, at scale. ChatGPT is by a massive margin the most-used AI application on earth, which means that OpenAI both knows exactly the type of workloads it needs to deliver, how often they are used, and, thanks to the router architecture that was a key component of GPT-5, the ability to decide which jobs are run where.

In other words, OpenAI, more than just about any other company, is well-placed and eminently justified in building their own custom chip. Moreover, [this tweet from OpenAI’s Clive Chan](<https://x.com/itsclivetime/status/1977772728850817263>) makes clear that OpenAI sees reasoning as the key use case for these chips:

![](https://pbs.twimg.com/profile_images/1783368343619252224/BzPPFLQt.jpg)

[Clive Chan](<https://twitter.com/itsclivetime>) [@itsclivetime](<https://twitter.com/itsclivetime>)

[ ](<https://twitter.com/itsclivetime/status/1977772728850817263>)

Really happy to be announcing the chips we’ve been cooking the past 18 months! OpenAI kicked off the reasoning wave with o1, but months before that we’d already started designing a chip tuned precisely for reasoning inference of OpenAI models.

In January 2024, I joined OpenAI as a hybrid gpu programmer & custom chip designer, the first IC on an oddly positioned hardware team that hadn’t yet committed to the idea of custom chips. These past 21 months I’m so lucky to have gotten the chance to learn from this incredibly talented and tiny team, accelerated by tight codesign with our ML team, Broadcom, and a few really cool new AI tools ;)

Now we’re 9 months away from what is I think the fastest and largest volume ramp of any first time chip. Looking forward to pushing the cost and latency of intelligence to zero.


![](https://pbs.twimg.com/profile_images/1885410297101381632/3Gs7_1gs.jpg)

[OpenAI Newsroom](<https://twitter.com/OpenAINewsroom>) [@OpenAINewsroom](<https://twitter.com/OpenAINewsroom>)

[ ](<https://twitter.com/OpenAINewsroom/status/1977724753705132314>)

We're partnering with Broadcom to deploy 10GW of chips designed by OpenAI.

Building our own hardware, in addition to our other partnerships, will help all of us meet the world’s growing demand for AI.

[openai.com/index/openai-a…](<https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/>)

[Posted Oct 13, 2025 at 1:15PM](<https://twitter.com/OpenAINewsroom/status/1977724753705132314>) [Posted Oct 13, 2025 at 4:25PM](<https://twitter.com/itsclivetime/status/1977772728850817263>)

Reasoning is amazing; it’s also way too slow. It also dramatically increases the amount of tokens necessary for an answer. It’s the most obvious thing to improve to bring down costs and increase usage, and I think it’s very plausible that OpenAI can build something custom to reason better.

Now of course OpenAI and Broadcom have to deliver, but this isn’t Broadcom’s first go-around: the company has worked with Google, Meta, and ByteDance on chips, and is even rumored to be working with Apple on a custom AI chip for its servers; OpenAI meanwhile, has those real workloads that should give very useful guidance on exactly what needs to be built.

### AMD and Nvidia

What should be clear by now is that this announcement is not a surprise; it does, however, raise the question about what exactly was the deal with that announcement OpenAI made with AMD?

In fact, I think I got it right in [OpenAI’s Windows Play](<https://stratechery.com/2025/openais-windows-play/>): OpenAI’s deal with AMD is ultimately about keeping Nvidia in check, helping OpenAI capture the most value from the AI value chain. AMD is like Nvidia in that they make GPUs; they are less like Nvidia in that they don’t have nearly the same software stack, networking infrastructure, etc. AMD’s strategy is to build out open consortiums to solve those issues, and it would very much be in OpenAI’s long-term interest that they succeed and offer a credible alternative to Nvidia, both in case the XPUs don’t work out, but also even if they do.

The fact of the matter is that GPUs will still absolutely be critical for OpenAI, and not just for training. AI is not and will not be a monolithic thing, particularly in the age of reasoners; even if this XPU effort succeeds in accelerating a critical type of token generation, there will still remain many other ones for different use cases, and here the GPU’s flexibility will be essential.

Moreover, OpenAI has all of the option value on AMD: the latter has to actually deliver for OpenAI to take its stake, the value of which will roughly mirror what OpenAI will pay AMD; if it doesn’t work out — and even if it does — OpenAI will still be Nvidia’s biggest customer, it would just prefer that they are locked in to the minimum extent possible.

This also explains why Nvidia’s investment into OpenAI was ultimately a smart move for both sides. Nvidia still benefits financially even if OpenAI becomes the Windows to its Intel (which is still a very good place to be!); OpenAI, meanwhile, further incentivizes Nvidia to support them even as they bring on other chip makers and architectures, although truthfully, their userbase is incentive enough.

What remains unresolved is the power generation for all of these chips, and the fact that chips from Nvidia, AMD, and Broadcom are all made by TSMC. Altman brushed aside questions about the latter in [his latest Stratechery Interview](<https://stratechery.com/2025/an-interview-with-openai-ceo-sam-altman-about-devday-and-the-ai-buildout/>); he hinted about the former in terms of more announcements that may be upcoming. One angle I would keep an eye on is the Middle East: it’s possible that one of the incentives for peace in the region is the potential for a massive commitment to build AI data centers in a place that has sufficient capability and insufficient compunction about building power generation.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
