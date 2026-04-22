---
title: "TSMC Earnings; A16 and TSMC's Approach to Backside Power; Intel Earnings, Architecture, and AI"
reader_id: "01k192q3k13a5dgj1173gge32h"
notion_page_id: "3484ebe7-f118-8191-b81b-fd90b4765de6"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01k192q3k13a5dgj1173gge32h"
source_url: "https://stratechery.com/2025/tsmc-earnings-a16-and-tsmcs-approach-to-backside-power-intel-earnings-architecture-and-ai/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-07-28"
saved_at: "2025-07-28"
reading_time: "13 mins"
summary: "TSMC and Intel's approach to backside power are downstream of their cultures: customer-centric versus self-serving. It may doom the latter."
content_hash: "89ec64a7bd678a6ee5f22df1a8441d92ba9a04e9c5ac40c80b460b5b36c15496"
---

TSMC and Intel's approach to backside power are downstream of their cultures: customer-centric versus self-serving. It may doom the latter.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On [last week’s episode of Sharp Tech](<https://sharptech.fm/member/episode/the-post-ai-internet-realities-how-future-creators-can-succeed-mail-on-startups-f-1-rights-and-alternative-rock>), Andrew and I discussed the future of the web in a world of AI, and then dived into an expansive mailbag section covering startups, F1, 90s music, and more.

On to the Update:

### TSMC Earnings

From [Bloomberg](<https://www.bloomberg.com/news/articles/2025-07-17/tsmc-profit-surges-again-after-ai-drives-big-jump-in-sales>):

> Taiwan Semiconductor Manufacturing Co. raised its outlook for 2025 revenue growth, shoring up investors’ confidence in the momentum of the global AI spending spree. The world’s biggest contract chipmaker on Thursday forecast sales growth of about 30% in US dollar terms this year, up from mid-20% previously. That reinforced expectations that tech firms from Meta Platforms Inc. to Google will keep spending to build the data centers essential to artificial intelligence development. TSMC’s American depositary receipts gained as much as 4.3% after markets opened in New York, while top supplier ASML Holding NV rose as much as 3.5%.
>
> TSMC’s move underscores resilient demand for high-end chips from the likes of Nvidia Corp. and Advanced Micro Devices Inc., which is outpacing its production capacity. Chief Executive Officer C.C. Wei affirmed on Thursday that AI orders still run hot — seeking to dispel persistent speculation that tech firms may curtail spending. While he stressed that underlying AI demand is strengthening, the uncertainty around the Trump administration’s tariffs merited caution…
>
> TSMC upgraded its forecast after reporting a better-than-expected 61% jump in net income for the June quarter to NT$398.3 billion ($13.5 billion), keeping intact a streak of beating estimates every quarter since 2021. The company previously posted a 39% surge in revenue. Revenue from high-performance computing — which includes chips for servers and data centers — now accounts for three-fifths of the company’s revenue, a major change from when TSMC primarily rode the smartphone market. It remains the main chipmaker to Apple Inc.

TSMC’s [earnings call](<https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2025-07/1f4f86c935f1de837672a6973154e64b26bdae57/TSMC%202Q25%20Transcript.pdf>) was before the Google earnings call that [I wrote about last week](<https://stratechery.com/2025/google-earnings-google-flips-the-switch-on-cloud-search-notes/>), where the company increased its planned capex by $10 billion; needless to say TSMC’s optimism was clearly justified.

TSMC did have lower margins, for two reasons: first, there was a big move in the Taiwanese dollar relative to the U.S. dollar in the second quarter, which goes straight to the bottom line (TSMC’s revenue is in dollars and its costs are in NTD, so a strong NTD means margin compression). Second is the fact that the first Arizona fab is on line, and it’s more expensive to operate. CFO Wendell Huang said:

> We have just guided our third-quarter gross margin to decrease by 210 basis points to 56.5% at the midpoint, primarily due to the continued unfavorable foreign exchange rate and more pronounced dilution from overseas fabs, as we ramp up further in Kumamoto and Arizona. We continue to forecast the gross margin dilution from the ramp-up of our overseas fabs in the next five years, starting from 2025, to be between 2% to 3% every year in the early stages and widen to 3% to 4% in the latter stages. Despite the higher cost of overseas fabs, we will leverage our increasing size in Arizona and work on our operations to improve the cost structure. We will also continue to work closely with our customers and suppliers to manage the impact.

“Working closely with our customers” certainly includes raising prices, and CEO C.C. Wei was clear that the upcoming N2 node will be substantially more expensive than N3 (which I believe [was very underpriced](<https://stratechery.com/2024/tsmc-earnings-tsmcs-pricing-mistake-intel-v-tsmc/>)).

### A16 and TSMC’s Approach to Backside Power

What is interesting about N2 — which will start shipping in volume this fall with Apple’s new iPhone — is that ([as expected](<https://stratechery.com/2024/tsmc-earnings-the-ai-milestone/>)) smartphones won’t have the most expensive chips. Here is Wei during the question-and-answer portion of the call talking about the A16 variant:

> **You highlighted A16, which would be very applicable for high performance compute. Is that the node where AI and HPC would actually be at par with smartphone as an end market that would drive demand for the most leading edge node?**
>
> **C.C. Wei:** You are right. Usually, the HPC’s customers are always one step behind using N plus 1 or N plus 2 technologies. Now because of AI demand is so strong, that’s one thing. But the most important thing is they need some kind of performance, but the power consumption is very, very important. And when we talk about A16, we have another power efficiency improvement close to 20%. That’s a big value for all the AI data centers applications. So that help my customer moving faster because of every time when we talk about the AI data center, if you notice that the first thing they talk about is power supply, electricity, right? So they did not tell you, say the power efficiency is very important, but they tell you that we had to build a very big electricity power plant to support the AI data center. So that tells you how important it is. And TSMC is a technology, by the way. A16 is a further improvement of the N2 node, so it’s not a surprise for TSMC to expect for those people in AI datacenter industry, they want to use A16.

A16 is very interesting. Chips are constructed with multiple layers; traditionally the most delicate layers are logic layers that are at the bottom of the chip, for a very simple reason: because they are the easiest to screw up, it makes sense to lay them down first so that you can discard the wafer if you screw up without throwing away too much work. The challenge, however, is that that means that the power layers are higher up in the stack, which means you need to get power down from the top to the bottom, which both causes congestion and interference. Backside power is a way to solve this problem: if you put power on the bottom, then you can easily wire up the logic layer from the backside, leaving the topside free for communication. The problem, however, is that the complicated stuff is now in the middle of the chip.

Intel and TSMC have taken two fundamentally different approaches to this problem. Intel starts by laying down all of the power layers and then builds the logic on top. This is challenging for yields but, if yields can be managed, is overall a more cost-effective solution. TSMC, on the other hand, is building one wafer for power and another layer for logic and then bonding them together. This is much more expensive, but on the flipside, TSMC can take the same logic layer and build traditional chips with power on top. In other words, N2 and A16 have the same logic layers, but the former puts power on top, and the latter bonds it to the bottom.

What this means in practice is that N2 is much more suitable for smartphones in particular, where the overall power draw is the gating factor; that means that there is much less of a concern about congestion and interference issues because the power draw never gets that high (because it would destroy battery life). A16 chips, meanwhile, can absolutely guzzle power, driving superior performance. To put it another way, while both mobile and AI needs power efficiency, their constraints are different: mobile needs performance-per-watt with a capped amount of wattage; AI needs performance-per-watt but has no a much higher limit in the amount of watts it can consume as long as the performance gained is worth it. That’s what A16 will specialize in, and why the significant extra costs will be worth it.

More generally, TSMC’s approach to backside power makes sense for the sort of company that TSMC is: they want to service everyone, and they want to give them choice. Apple doesn’t want to pay more for iPhone chips to get backside power given that mobile won’t really see the benefits, and they won’t have to; Nvidia absolutely will see the benefits, however, and they certainly have the margins to pay TSMC’s premium for the more expensive bonded solution.

### Intel Earnings, Architecture, and AI

From [Bloomberg](<https://www.bloomberg.com/news/articles/2025-07-24/intel-gives-upbeat-sales-forecast-after-pc-demand-picks-up>):

> Shares of Intel Corp. tumbled 8.5% on Friday after Chief Executive Officer Lip-Bu Tan sparked concerns that he was more focused on cost cutting than restoring the chipmaker’s technological edge. As part of Intel’s second-quarter report, Tan said the company will cancel some factory projects and take a more conservative approach to future spending. Tan called the investments begun under his predecessor, Pat Gelsinger, excessive and unwise. “I do not subscribe to the belief that if you build it, they will come,” he said on a conference call with analysts.
>
> At the same time, Tan struggled to give a clear picture of how he’ll make the company more competitive again. Gelsinger had embarked on an ambitious plan to turn Intel into a chip foundry, a business that makes products for outside clients. A key part of that was moving toward a more advanced production technique called 14A. But Tan signaled Thursday that Intel will only roll out that technology tentatively. The company will add large-scale capacity for 14A when Tan is convinced he has enough customers committed to using it, he said on the call. That didn’t sit well with investors, who sent the shares down to $20.70 in New York on Friday, the stock’s biggest single-day decline in more than three months.

There was a lot to unpack from [this earnings call](<https://seekingalpha.com/article/4804322-intel-corporation-intc-q2-2025-earnings-call-transcript>), including Tan’s only-slightly-veiled explanation as to why Intel failed to acquire any meaningful 3rd-party customers for the 18A process on which Gelsinger staked the company’s future; from his prepared remarks:

> The foundry business is a service business that relies on foundational principle of trust. We need to demonstrate to our customers that we can deliver wafers on time with high quality, reliability and yield that we can manufacture their products at scale. We need to have process and packaging technology that is not only competitive but, more importantly, is designed to meet the needs of our customers. In addition, we also need to develop a rich and diverse ecosystem of IP and EDA partners who will enable our customers to seamlessly design chips using our process.

Tan added later in the question-and-answer section:

> So I think as you mentioned, 18A is a foundation for at least 3 generation of our Intel client and server business products, and we are committed to ramp that and so far, give me the confidence as we’re engaging with external ecosystem partners to help us to look at the yield and how can we improve. And that, in the past, we didn’t engage that. So I really see that the feedback from the partners that, hey, the culture, the intensity for our team is really focused on the yield performance and they really like the attitude on that.

And later about 14A:

> So I think on the 14A, first of all, I think the team is laser-focused on building up the basic building blocks, technology definition, transistor architecture, process flow, design enablement, PDK and foundation IP and the test chip to verify and improve the performance and the defect density. Saying that, clearly, we learned quite a lot on the mistake we made on the 18A, and now we’re applying it to the 14A. So I think we learned a lot.
>
> And secondly, we also reach out to the outside partners to help us, show them the data and how can we improve the yield and per month, and so that we can drive — that gives me a lot of confidence we can get there. But even more important, we are engaging with customers that are going to enable us and then with a clear milestone to execute in terms of process development and with PDK, with all the different IP that we need to really put it together. So I think that gives me a lot of more confidence that this time, we have customers who are engaging early enough in the inception. And also we learned from our mistake and we can learn quicker and then get a better result.
>
> So I think all in all, I think I have a lot of more confidence. The team is laser-focused, and the feedback from the partners and outside is that, “Wow, the culture is changing and you guys are really focused on the yield rather than just the performance.” So I think that part, I think, will be able to enable us. Plus, the other part is we really engage with all the external EDA and IP provider and make sure that we have the whole program together to do the pattern matching for the customer. And the good news is customers are excited. The 14A is a process node. But clearly, I want to make sure that until I see the internal customer, external customer volume commitment before I put CapEx into the operation. So that is something that needs to meet my requirement in terms of performance and yield. It’s a lot of responsibility to be serving our customer, make sure that we can deliver the result, consistent, reliable result to them, so that the revenue can depend on us.

In short, it seems clear that 18A yields are very poor and the reason why 3rd-party customers weren’t interested. Worse, what Tan is suggesting is that previous leadership didn’t care about yields, just performance. I’m sure Gelsinger, if he had a say, would push back against that, but I’m inclined to believe Tan, because prioritizing performance over everything else sounds exactly like the Intel modus operandi — and [Gelsinger’s most fundamental failing](<https://stratechery.com/2025/intels-new-ceo-reevaluating-gelsinger-lip-bu-tan-and-cadence/>) is that he was Intel to the core at a time when Intel needed a fundamental cultural reset.

What was perhaps the most surprising part of the call, however, was Tan’s AI plan:

> Finally, turning to AI. In the past, we approached AI with a traditional silicon and training-centric mindset without a cohesive silicon systems software stack and strategy. While we do need to build and consolidate upon our silicon franchise based upon our x86 CPU and our Xe GPUs, we recognize the need to move up the abstraction stack into system and software. This is the area where Intel has traditionally been weak or entirely absent. But we intend to incubate and grow these important skill sets and capabilities under my leadership. This will take time, but it will be vital for Intel to stay relevant in the next wave of computing. In addition, we see the AI market continuing to evolve, and we are concentrating our efforts on areas we believe we can disrupt and differentiate like inference and agentic AI. We need to start by first understanding emerging and real AI workloads, then work backwards to design software, systems and silicon to enable best outcome for those particular workloads. We will strive to become the compute platform of choice, but we will also work towards a full stack AI solution, and I look forward to sharing more on our strategy in the coming months.

My first thought was that this seems fairly delusional; Nvidia is the dominant AI solution, with AMD as a distant second; the true alternative, however, is hyperscalers building their own ASICS. It’s not clear where Intel fits, and the idea that the company is going to suddenly become a compelling software provider seems delusional.

I wonder, however, if this plan is downstream from another Gelsinger decision that was very much classic Intel: I mentioned above that Intel’s approach to backside power is to build all their chips that way from the get-go. The power layer is laid down, then the logic layer, which is bad for yields — see Tan’s frustration with 18A — but, in the future, could be more cost-effective but less flexible than TSMC’s approach. That is the classic Intel part, in that the company pursued the more technologically challenging but theoretically superior option that benefits Intel’s products most of all.

The problem with this approach is that [it does handicap Intel’s foundry efforts, because 18A really isn’t compelling for mobile](<https://semianalysis.com/2025/07/21/vlsi2025/>). Mobile chips don’t benefit from backside power, which means the extra cost and lower yields aren’t worth it; all 18A chips, however, have backside power. What this does mean, however, is that Intel could, at least in theory, build very high-performance monolithic chips at a considerable cost advantage to TSMC. A16 chips will almost exclusively be used in a chiplet configuration, where a lot of the chip’s functionality is fabbed on much cheaper processes; this is fine in a training scenario where you are linking together massive numbers of these chips in pursuit of throughput and system-wide coherence and much less concerned about latency and on-chip coherence.

However, inference is different. While consumer applications like ChatGPT can be relatively high-latency, more-and-more workloads will require low latency and high coherence, and here a monolithic chip could be better, which Intel is better placed to provide. The key, however, will be the software to take advantage of that architectural difference, which is exactly what Tan is talking about. In other words, what I think Tan is driving at is that Gelsinger’s architectural choices actually made a foundry model harder to pull off, which means that for all of his attempts to change the culture, the company’s best chance might be in doubling down on the integrated model.

We’ll see! None of this matters if Intel gives up on manufacturing, which Tan raised as a possibility. From his prepared remarks:

> Up to and through Intel 18A, we could generate a reasonable return on our investments with only Intel Products. The increase in capital cost at Intel 14A, make it clear that we need both Intel products, and a meaningful external customer to drive acceptable returns on our deployed capital, and I will only invest when I’m confident those returns exist.

That Intel’s products would not be enough to fund the leading edge was the exact worry I raised [back in 2013](<https://stratechery.com/2013/the-intel-opportunity/>), and now we’re here. And, honestly, the AI plan — if I’m right about architecture driving it — makes me pretty pessimistic about this outcome. Intel needed to become a foundry to survive, but the company just might have never had it in them to truly be customer-centric a la TSMC, which is why the AI plan — an integrated chip and software solution — is in many respects back to the future.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
