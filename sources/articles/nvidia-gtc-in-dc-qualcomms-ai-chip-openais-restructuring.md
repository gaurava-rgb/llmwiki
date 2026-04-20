---
title: "Nvidia GTC in DC, Qualcomm's AI Chip, OpenAI's Restructuring"
reader_id: "01k8rhzbhvrdq2anvpkytbeh1y"
notion_page_id: "3484ebe7-f118-8181-8c40-c72fe9069946"
reader_url: "https://read.readwise.io/read/01k8rhzbhvrdq2anvpkytbeh1y"
source_url: "https://stratechery.com/2025/nvidia-gtc-in-dc-qualcomms-ai-chip-openais-restructuring/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-10-29"
saved_at: "2025-10-29"
reading_time: "10 mins"
summary: "Nvidia makes its pitch to DC to preserve its CUDA moat, which also explains the challenges facing Qualcomm's new chip. Then, OpenAI's restructuring and Microsoft's collar trade."
content_hash: "94df88ed5e18b72a27f5b8ce6b20f80be24a794ba8c90c7af2ea5405beaf8640"
---

Nvidia makes its pitch to DC to preserve its CUDA moat, which also explains the challenges facing Qualcomm's new chip. Then, OpenAI's restructuring and Microsoft's collar trade.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On [this week’s episode of Sharp China](<https://sharpchina.fm/member/episode/a-basic-consensus-on-arrangements-to-address-us-china-concerns-the-new-five-year-plan-sounds-familiar-nexperia-as-an-object-lesson>), Andrew and Bill discuss the early outlines of a deal between the U.S. and China, and the scale of the challenge facing the U.S. and Europe in building secure supply chains.

In case you missed it, Andrew launched a new website, [Sharp Text](<https://sharptext.net/>), where he will write once a week on topics he covers across Sharp Tech, Sharp China, and Greatest of All Talk. Check out his first two articles: [Did Xi Jinping Just Have a Bad Moment?](<https://sharptext.net/2025/did-xi-jinping-just-have-a-bad-moment/>), about rare earths and the trade war, and [The NBA’s ESPN Problem Might Finally Be Over](<https://sharptext.net/2025/the-nbas-espn-problem-might-finally-be-over/>), about the NBA’s dramatically improved presentation with its newest broadcast partners. You can look for new Sharp Text Articles on Fridays; to receive them in your inbox you can [add Sharp Text to your Stratechery plan here](<https://stratechery.passport.online/>).

On to the Update:

### Nvidia GTC in DC

From the [Wall Street Journal](<https://www.wsj.com/tech/ai/nvidia-ceo-praises-trump-in-maga-themed-speech-ahead-of-trade-talks-f7684673>):

> Jensen Huang said Nvidia has helped reinvigorate U.S. manufacturing less than a year into President Trump’s second term and praised his policies days before a key trade meeting that could determine Nvidia’s access to the Chinese market. In a rollicking keynote speech at Nvidia’s first-ever technology conference in the nation’s capital, Huang highlighted a slew of partnerships with prominent American companies, including tech giants like Uber, Palantir, Amazon and Microsoft. Emphasizing themes of patriotism and U.S. national interests, Huang boasted about the computing capabilities of his company’s Blackwell graphics processing units, or GPUs, Nvidia’s most-advanced artificial-intelligence chips.
>
> He highlighted the Grace Blackwell NVL72, a powerful “thinking machine” made from components largely produced in U.S. factories that combines 72 GPUs in a single server rack, weighs 3,000 lbs. and costs several million dollars. Huang said Nvidia had shipped 6 million Blackwell chips — which were released last year — so far and had orders for 14 million more over the next five quarters, in total representing half a trillion dollars in sales. Nvidia’s stock rose 5% Tuesday.
>
> “We are manufacturing in America again. It is incredible,” he said. “The first thing that President Trump asked me for is, bring American manufacturing back…. Nine months later, we are now manufacturing, in full production, Blackwell in Arizona.” The claim builds on Nvidia’s recent announcement of the first silicon wafers for Blackwell GPUs rolling off manufacturing lines at Taiwan Semiconductor Manufacturing’s fabrication plant in Phoenix. The chips aren’t entirely completed on U.S. soil, however…
>
> Tuesday’s speech marked the latest instance of Huang praising Trump while the president contemplates export policies worth billions of dollars to Nvidia. Huang is expected to leave Washington to attend the Asia-Pacific Economic Cooperation meetings in South Korea, where Trump and Chinese leader Xi Jinping are set to meet Thursday. China’s access to Nvidia chips has been part of past negotiations and is seen as a potential bargaining chip for Trump. Huang is expected to meet with Trump in Asia but declined to say who else he would meet with. He said that the company originally planned its Washington summit hoping Trump would attend, but the president’s Asia trip conflicted.

This is a pretty cynical read about Nvidia’s latest GTC conference, held for the first time in Washington D.C., and, well, I think it’s also a very fair read. One thing I do admire about Huang is his directness and focus on solving the biggest problems facing Nvidia, and the biggest problem facing Nvidia is the combination of needing access to the Chinese market to maintain its CUDA software moat, and battling the perception amongst some in Washington that Huang in particular is insufficiently pro-America.

To that end, Huang started the keynote placing Nvidia squarely in the lineage of past American inventions from the telephone to the transistor and, as the excerpt notes, praised both American capabilities and Trump and his cabinet’s policies explicitly throughout the keynote — which again, was located in Washington D.C., not Silicon Valley.

There was also a section early in the keynote squarely focused on CUDA and its network effects. After talking about the slowdown in the performance of transistors and the need to change computing systems, Huang explained:

> Accelerated computing, its moment has now arrived. However, accelerated computing is a fundamentally different programming model. You can’t just take a CPU’s software, software written by hands, executing sequentially, and put it onto a GPU and have it run properly. In fact, if you just did that, it actually runs slower. And so you have to reinvent new algorithms. You have to create new libraries. You have to, in fact, rewrite the application, which is the reason why it’s taken so long. It’s taken us nearly 30 years to get here. But we did it one domain at a time.
>
> [CUDA-X Libraries are] the treasure of our company. Most people talk about the GPU. The GPU is important, but without a programming model that sits on top of it, and without dedication to that programming model, keeping it compatible over generations — we’re now at CUDA 13, coming up, CUDA 14 — hundreds of millions of GPUs in use, running in every single computer, perfectly compatible. If we didn’t do that, then developers wouldn’t target this computing platform. If we didn’t create these libraries, then developers wouldn’t know how to use the algorithm and use the architecture to its fullest, one application after another. This is really the treasure of our company.

Huang later talked about the virtuous cycle that attends the CUDA network: more developers using CUDA means more companies use CUDA, which drives more investment in CUDA and more developers, and so on. That is what Huang is desperate to preserve; the thing about virtuous cycles is that they are very hard to break, but straight up banning an entire ecosystem from participating is an excellent way to spur the creation of an alternative, and that alternative — which, at the end of the day, is just software — is likelier than not to spill over into Nvidia’s remaining core markets, destroying that treasure.

There was one other clip of Huang’s keynote I wanted to highlight, as I think it was an excellent articulation of the thesis that the AI market is orders of magnitude bigger than the software market:

> Software of the past, and this is a profound understanding, a profound observation of artificial intelligence, that the software industry of the past was about creating tools. Excel is a tool. Word is a tool. A web browser is a tool. The reason why I know these are tools is because you use them. The tools industry, just as screwdrivers and hammers, the tools industry is only so large. In the case of IT tools, they could be database tools, these IT tools is about a trillion dollars or so.
>
> But AI is not a tool. AI is work. That is the profound difference. AI is, in fact, workers that can actually use tools. One of the things I’m really excited about is the work that Aravind’s doing at Perplexity. Perplexity, using web browsers to book vacations or do shopping. Basically, an AI using tools. Cursor is an AI, an agentic AI system that we use at Nvidia. Every single software engineer at Nvidia uses Cursor. That’s improved our productivity tremendously. It’s basically a partner for every one of our software engineers to generate code, and it uses a tool, and the tool it uses is called VS Code. So Cursor is an AI, agentic AI system. that uses VS Code.
>
> Well, all of these different industries, these different industries, whether it’s chatbots or digital biology where we have AI assistant researchers, or what is a robotaxi? Inside a robotaxi, of course, it’s invisible, but obviously, there’s an AI chauffeur. That chauffeur is doing work, and the tool that it uses to do that work is the car, and so everything that we’ve made up until now, the whole world, everything that we’ve made up until now, are tools. Tools for us to use. For the very first time, technology is now able to do work and help us be more productive.

This distinction is one I’ve made in the past, including in [ChatGPT Gets a Computer](<https://stratechery.com/2023/chatgpt-learns-computing/>) and [Tech Philosophy and AI Opportunity](<https://stratechery.com/2025/tech-philosophy-and-ai-opportunity/>); what is compelling about Huang’s framing, however, is that it underlines why AI may be unique in terms how it is sold. Huang actually goes back to the Cursor example later on, pointing out that it’s worth paying for because it makes very expensive engineers more productive. It’s only a small step, however, to making the case that very expensive AI is much cheaper than far more expensive engineers, so why not simply ditch the latter entirely? In other words, AI’s value isn’t necessarily — or just — in its ability to grow top-line revenue, but in its ability to cut below the line costs. Usually revenue growth drivers are easier to sell; AI may be such a cost saver that it breaks the mold in that regard.

### Qualcomm’s AI Chip

From the [Wall Street Journal](<https://www.wsj.com/tech/qualcomm-stock-surges-on-ai-chip-launch-cc7a4590>):

> Shares in Qualcomm jumped as much as 20% early Monday after the company announced it was launching new artificial-intelligence accelerator chips to rival Nvidia. The AI200 will start shipping next year and the AI250 in 2027, the company said. Both will be available as stand-alone components or cards that can be added into existing machines. The move puts Qualcomm, which has so far mostly focused on semiconductors for mobile devices, in direct competition with Nvidia, which has dominated the market for AI chips. Qualcomm joins Intel and Advanced Micro Devices in trying to mount AI-chip competition against the semiconductor giant.

The market reaction to this announcement certainly speaks to a heightened level of frothiness; I have a hard time seeing the justification. First off, [Qualcomm released precious few details about these chips](<https://www.qualcomm.com/news/releases/2025/10/qualcomm-unveils-ai200-and-ai250-redefining-rack-scale-data-cent>). Secondly, however, even if the chips are awesome, Qualcomm faces a fundamental software challenge: anyone who wants a 3rd-party chip is likely to choose Nvidia; if they want an alternative, the obvious choice is a specially-designed ASIC tuned to their own software stack. And, if anyone is likely to win the tenuous middle ground between those two options, it seems more likely to be AMD than anyone else.

Indeed, this isn’t Qualcomm’s first AI chip; the previous A100 failed to find a market for exactly these factors. From [a 2022 report in The Information](<https://www.theinformation.com/articles/why-qualcomm-failed-to-land-meta-as-its-flagship-ai-chip-customer>):

> Qualcomm courted Meta Platforms in hopes of making Facebook’s owner the flagship customer for Qualcomm’s first AI data center chip, the AI 100, according to two people familiar with the matter. After Qualcomm released the chip in fall 2020, Meta tested it against a range of alternatives, including the chips Meta has been using and a specialized chip Meta developed internally to handle AI computing work. Qualcomm’s chip performed well, these people said, posting the best performance per watt of electricity used. That can have a big impact on operating costs for a company like Meta whose data centers support billions of users.
>
> But by spring of last year, Meta had declined to use Qualcomm’s chip, the people said. Meta questioned whether the software that accompanied the chip was mature enough to wring the best performance from the chip on future tasks, they said. Meta decided to stick with its existing chips as it evaluates its options, one of the people said.

Three years on and I’m skeptical that the software ecosystem has advanced to a point where simply making a good chip is enough; if Qualcomm wants to succeed in this space, they’re going to have to get very serious about software — which probably isn’t enough either, given the network effects at play — or, per the China point, hope that Nvidia’s software dominance is artificially interrupted.

### OpenAI’s Restructuring

From [OpenAI](<https://openai.com/index/built-to-benefit-everyone/>):

> OpenAI has completed its recapitalization, simplifying its corporate structure. The nonprofit remains in control of the for-profit, and now has a direct path to major resources before AGI arrives. The nonprofit, now called the OpenAI Foundation, holds equity in the for-profit currently valued at approximately $130 billion, making it one of the best resourced philanthropic organizations ever. The recapitalization also grants the Foundation additional ownership as OpenAI’s for-profit reaches a valuation milestone. The OpenAI mission — ensuring that AGI benefits all of humanity — will be advanced through both the business and the Foundation. The more OpenAI succeeds as a company, the more the non-profit’s equity stake will be worth, which the non-profit will use to fund its philanthropic work.

OpenAI shared more details of the restructure [here](<https://openai.com/our-structure/>), including:

  * The OpenAI Foundation will hold ~26% of the for-profit entity
  * Microsoft will hold ~27%
  * Employees and other investors will hold the remaining 47%



In addition, according to [Bloomberg](<https://www.bloomberg.com/news/articles/2025-10-28/microsoft-to-get-27-of-openai-access-to-ai-models-until-2032>):

  * Microsoft will have access to OpenAI technology until 2032, including models deemed as being AGI, but not for consumer hardware.
  * OpenAI will gain the right to develop products with 3rd parties.
  * Microsoft will continue to be entitled to 20% of OpenAI revenue until an expert panel deems OpenAI has reached AGI.
  * Microsoft gives up its right of first refusal on new OpenAI cloud infrastructure.
  * OpenAI will make an additional $250 billion commitment to use Azure infrastructure.



I’m not, [as I explained previously](<https://stratechery.com/2025/openai-restructuring-microsofts-rights-simo-and-windsurf/>), bothered by this restructuring; the reality is that most of OpenAI’s value was generated by the for-profit entity, and this formalizes that. In that same Update I also argued that Microsoft should prioritize continual access to OpenAI’s models over retaining its stake and profit share; the actual deal seems to have gone in the other direction: Microsoft keeps access for a while, but retains a long-term equity stake in OpenAI and a shorter-term revenue share.

This probably makes sense: Microsoft has put a collar on OpenAI’s future. The put is that OpenAI ends up being a commodity, in which case it will be easy enough to sub out OpenAI models for alternatives by the time 2032 rolls around. The call is that OpenAI is worth dramatically more than the value Microsoft can ever build on its own, which will make Microsoft’s equity stake worth more than continued access to the models. This certainly makes sense financially; it’s a bit of a bummer, however, to see a company ultimately decide that its biggest upside play is not betting on itself.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
