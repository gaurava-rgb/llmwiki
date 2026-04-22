---
title: "Nvidia Earnings, Moats and China, Nvidia vs. the AI Labs"
reader_id: "01k3rwyw678pnp8vbyxwf76kz5"
notion_page_id: "3484ebe7-f118-81e3-9c66-eb585c178b9d"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01k3rwyw678pnp8vbyxwf76kz5"
source_url: "https://stratechery.com/2025/nvidia-earnings-moats-and-china-nvidia-vs-the-ai-labs/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-08-28"
saved_at: "2025-08-28"
reading_time: "11 mins"
summary: "Nvidia's earning continue to be governed by supply — and reasoning models make that even more the case. Plus, why Nvidia is so desperate to get back into China."
content_hash: "7c943dc59baf3f3a93070edfee2e641b2d7304479de689323fa535532ffc7e40"
---

Nvidia's earning continue to be governed by supply — and reasoning models make that even more the case. Plus, why Nvidia is so desperate to get back into China.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

Sharp Tech will be back with a new episode tomorrow; in the meantime, and apropos this Update, [Sharp China covered Nvidia and China last week](<https://sharpchina.fm/member/episode/two-weeks-of-nvidia-angst-stocks-and-real-estate-warming-relations-with-india-labubu-and-soft-power-exports>).

Next Monday is the Labor Day holiday in the U.S.; there will be no Update.

On to the Update:

### Nvidia Earnings

From the [Wall Street Journal](<https://www.wsj.com/business/earnings/nvidia-nvda-q2-earnings-report-2026-2939143b>):

> Nvidia sales set a fresh record on Wednesday, as the world’s most valuable public company continued to capitalize on strong demand for AI computing, but the company’s lackluster outlook stoked jitters about future demand, sending its share price lower. Sales in the July quarter hit $46.7 billion, roughly in line with analyst estimates. Revenue from the important data-center segment, which includes sales of the company’s most powerful chips, used to train and refine artificial-intelligence models, rose 56% to $41.1 billion, but came in slightly lower than the $41.3 billion analysts had expected. Quarterly net income was $26.4 billion, 59% higher than a year earlier. The company predicted revenue of $54 billion for the third quarter, slightly higher than consensus estimates by Wall Street analysts. After several blockbuster quarters, the revenue projection was seen as underwhelming and stoked worries that growth in demand for AI chips might be hitting a plateau.

It is always dangerous to invoke the mythical law of large numbers, but the most important place to start with Nvidia earnings is to check the supply-demand balance; here’s the answer from CEO Jensen Huang on [the earnings call](<https://seekingalpha.com/article/4817296-nvidia-corporation-nvda-q2-2026-earnings-call-transcript>):

> Right now, the buzz is, I’m sure all of you know about the buzz out there. The buzz is everything sold out. H100 sold out. H200s are sold out. Large CSPs are coming out renting capacity from other CSPs. And so the AI-native start-ups are really scrambling to get capacity so that they could train their reasoning models. And so the demand is really, really high.

I made this point [a year-and-a-half ago](<https://stratechery.com/2024/nvidia-earnings-inference-and-meta/>), and it still holds: as long as demand for Nvidia GPUs exceeds supply, then Nvidia sales are governed by the number of GPUs they can make. That supply is certainly increasing — which is why Nvidia’s sales continue to climb — but assuming that supply increases are linear then, by definition, Nvidia’s growth rate is going to slow as it laps ever larger revenue numbers that themselves grew exponentially.

The big complicating factor is China. CFO Colette Kress said in response to an investor question:

> So let me first answer your question regarding what will it take for the H20s to be shipped. There is interest in our H20s. There is the initial set of license that we received. And then additionally, we do have supply that we are ready, and that’s why we communicated that somewhere in the range of about $2 billion to $5 billion this quarter, we could potentially ship.
>
> We’re still waiting on several of the geopolitical issues going back and forth between the governments and the companies trying to determine their purchases and what they want to do. So it’s still open at this time, and we’re not exactly sure what that full amount will be this quarter. However, if more interest arrives, more licenses arrives, again, we can also still build additional H20 and ship more as well.

Nvidia cleared one hurdle when the Trump administration, [after pausing H20 sales](<https://stratechery.com/2025/nvidia-h20-restricted-in-china-the-huawei-cloudmatrix-384-whither-chip-controls/>), [allowed them to resume](<https://stratechery.com/2025/china-ai-chips-a-china-chip-control-framework-whither-hbm/>); the Chinese government, however, [then told Chinese companies to not buy the H20](<https://www.theinformation.com/articles/china-demands-companies-halt-nvidia-chip-orders-security-concerns>). From the [Financial Times](<https://www.ft.com/content/b8e30c54-b71c-4113-8b3e-8f54bc36587d>) as to why:

> According to people with knowledge of the regulatory action, the Cyberspace Administration of China (CAC), the National Development and Reform Commission (NDRC) and the Ministry of Industry and Information Technology (MIIT) moved in response to comments made by Lutnick last month. “We don’t sell them our best stuff, not our second-best stuff, not even our third-best,” Lutnick told CNBC on July 15, the day after the Trump administration lifted export controls, implemented in April, on H20 sales. “You want to sell the Chinese enough that their developers get addicted to the American technology stack, that’s the thinking,” he added.
>
> Some of China’s senior leaders found the comments “insulting”, leading the policymakers to seek ways to restrict Chinese tech groups from buying the processors, according to two people with knowledge of the latest regulatory decision-making. As a result, Chinese tech groups held off or significantly downsized their H20 orders, according to those with knowledge of their plans.

I’m always wary of falling into the trap of blaming the U.S. for Chinese decisions; this overly solipsistic view of the world is the root of a lot of bad analysis, beyond being insulting to the intelligence and volition of the U.S.’s chief geopolitical rival. At the same time, it would be nice to see the counterfactual of Lutnick keeping his mouth shut, or better yet, the Trump administration not raising a ruckus about the H20 in the first place.

The problem, of course, is that Lutnick is right: Chinese companies using Nvidia chips preserves U.S. dominance of the dominant AI software stack; on the flipside, Chinese companies not using Nvidia both diminishes U.S. control and, for Nvidia specifically, theatens not just their China sales but, in the long run, their sales everywhere, not just from Chinese competitors but from competition generally should a Chinese-pioneered open-source CUDA alternative gain scale. And, by extension, the fact that Nvidia isn’t assuming it will sell any H20s at all should be the real reason for investor concern.

One note while I’m here: when the Trump administration [first put a pause](<https://stratechery.com/2025/nvidia-h20-restricted-in-china-the-huawei-cloudmatrix-384-whither-chip-controls/>) on H20 sales, I said that no one outside of China would want them; several folks noted that actually several would-be customers would be happy to buy H20s for the prices Nvidia was selling them to China, specifically for inference workloads, but Nvidia refused.

### Moats and China

One interesting way to think about Nvidia and China — and why Huang is so desperate to sell into the country — is the nature of their moat. Huang said in answer to a question about ASICs:

> Let’s talk about ASICs first. A lot of projects are started. Many start-up companies are created. Very few products go into production. And the reason for that is it’s really hard. Accelerated computing is unlike general-purpose computing. You don’t write software and just compile it into a processor. Accelerated computing is a full-stack co-design problem. And AI factories in the last several years have become so much more complex because of the scale of the problems have grown so significantly. It is really the ultimate, the most extreme computer science problem the world’s ever seen obviously. And so the stack is complicated. The models are changing incredibly fast from generative based on auto regressive to degenerative based on diffusion to mixed models to multi-modality. The number of different models that are coming out that are either derivatives of transformers or evolutions of transformers is just daunting.
>
> One of the advantages that we have is that Nvidia is available in every cloud. We’re available from every computer company. We’re available from the cloud to on-prem to edge to robotics on the same programming model. And so it’s sensible that every framework in the world supports Nvidia. When you’re building a new model architecture, releasing it on Nvidia is most sensible. And so the diversity of our platform, both in the ability to evolve into any architecture, the fact that we’re everywhere, and also, we accelerate the entire pipeline, everything from data processing to pretraining to post training with reinforcement learning, all the way out to inference. And so when you build a data center with NVIDIA platform in it, the utility of it is best. The lifetime usefulness is much, much longer.

This answer captures two parts of the moat. The first is CUDA, Nvidia’s software stack for controlling Nvidia GPUs, which is the default option. The second is that CUDA is everywhere, which means you can go to any cloud provider, hire developers familiar with CUDA, etc.

> And then I would just say that in addition to all of that, it’s just a really extremely complex systems problem anymore. People talk about the chip itself. There’s one ASIC, the GPU that many people talk about. But in order to build Blackwell the platform and Rubin the platform, we had to build CPUs that connect fast memory, extremely energy-efficient memory for large KB caching necessary for agentic AI to the GPU to a SuperNIC to a scale up switch, we call NVLink, completely revolutionary, we’re in our fifth generation now, to a scale out switch, whether it’s Quantum or Spectrum-X Ethernet, to now scale across switches so that we could prepare for these AI super factories with multiple gigawatts of computing all connected together. We call that Spectrum-XGS. We just announced that at Hot Chips this week. And so the complications, the complexity of everything that we do is really quite extraordinary. It’s just done at a really, really extreme scale now.

This is the third part, which is networking; I keep referring to Nvidia GPUs, but in reality, GPUs work at the system level, particularly for training, and Nvidia’s ability to link GPUs together into a single coherent system is unmatched. This is a big revenue driver, too: this quarter networking revenue was $7.3 billion, which is [more than Nvidia paid for Mellanox](<http://nvidianews.nvidia.com/news/nvidia-to-acquire-mellanox-for-6-9-billion>) (which is the foundation of their networking offering) in 2019. It’s truly one of the greatest acquisitions of all time.

> And then lastly, if I could just say one more thing, we’re in every cloud for a good reason. Not only are we the most energy efficient. Our perf per watt is the best of any computing platform. And in a world of power-limited data centers, perf per watt drives directly to revenues. And you’ve heard me say before that, in a lot of ways, the more you buy, the more you grow. And because our perf per dollar, the performance per dollar is so incredible, you also have extremely great margins.
>
> So the growth opportunity with NVIDIA’s architecture and the gross margins opportunity with NVIDIA’s architecture is absolutely the best. And so there’s a lot of reasons why NVIDIA is chosen by every cloud and every start-up and every computer company. We’re really a holistic full-stack solution for AI factories.

This last one — [which I wrote about after Huang’s most recent GTC](<https://stratechery.com/2025/nvidia-gtc-and-asics-the-power-constraint-the-pareto-frontier/>) — is maybe the most important piece of Nvidia’s long-term moat in the West. If AI companies are ultimately limited by power than they must maximize performance per watt; as long as Nvidia leads in that specific metric, their sky-high prices are well worth paying.

Power, however, is much less likely to be a limiting factor in China than in the West; that, by extension, means that Nvidia’s moat is much more dependent on CUDA, but that depends on China actually building on Nvidia chips. Huang’s long-term fear is that China is one of the most important countries for AI chips in the long run, and that Nvidia has no sustainable differentiation even if they were free to sell.

### Nvidia vs. the AI Labs

There was [an excellent blog post from Ethan Ding](<https://ethanding.substack.com/p/ai-subscriptions-get-short-squeezed>) in July about the challenging economics of AI:

> Imagine you start a company knowing that consumers won’t pay more than $20/month. Fine, you think, classic VC playbook – charge at cost, sacrifice margins for growth. you’ve done the math on CAC, LTV, all that. But here’s where it gets interesting: you’ve seen the a16z chart showing LLM costs dropping 10x every year.
>
> ![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/08/nvidia-earnings-1.png?resize=1330%2C982&ssl=1)
>
> So you think: I’ll break even today at $20/month, and when models get 10x cheaper next year, boom – 90% margins. The losses are temporary. The profits are inevitable.

Ding points out two big problems with this view. First is the fact that no one wants to use cheap models when better models exist:

> Demand exists for “the best language model,” period. And the best model always costs about the same, because that’s what the edge of inference costs today…When you’re spending time with an AI — whether coding, writing, or thinking — you always max out on quality. Nobody opens Claude and thinks, “You know what? Let me use the shitty version to save my boss some money.” We’re cognitively greedy creatures. We want the best brain we can get, especially if we’re balancing the other side with our time.

Second, the way that models have improved is by using way more tokens:

> While it’s true each generation of frontier model didn’t get more expensive per token, something else happened. Something worse. The number of tokens they consumed went absolutely nuclear. ChatGPT used to reply to a one sentence question with a one sentence reply. Now deep research will spend 3 minutes planning, and 20 minutes reading, and another 5 minutes re-writing a report for you while o3 will just run for 20-minutes to answer “Hello There”. The explosion of RL and test-time compute has resulted in something nobody saw coming: the length of a task that AI can complete has been doubling every six months. What used to return 1,000 tokens is now returning 100,000.

This is a critical insight in its own right, and it’s particularly notable when it comes to evaluating Nvidia’s long-term opportunity. I talked about the supply-demand balance earlier in the context of demand for Nvidia GPUs; another way to think about the same question is demand for tokens. The implication of Ding’s argument is that Nvidia, despite the ramp-up in supply, is actually exponentially further away from meeting demand because demand itself has increased exponentially, not just because more people and companies are using AI, but because those using AI consume dramatically more tokens.

Huang certainly recognizes this is the case. He said in an answer to an investor question about future growth:

> At the highest level of growth drivers would be the evolution, the introduction, if you will, of reasoning agentic AI. Where chatbots used to be one shot, you give it a prompt and it would generate the answer, now the AI does research. It thinks and does a plan, and it might use tools. And so it’s called long thinking; and the longer it thinks, oftentimes, it produces better answers. And the amount of computation necessary for 1 shot versus reasoning agentic AI models could be 100x, 1,000x and potentially even more as the amount of research and basically reading and comprehension that it goes off to do. And so the amount of computation that has resulted in agentic AI has grown tremendously. And of course, the effectiveness has also grown tremendously. Because of agentic AI, the amount of hallucination has dropped significantly. You can now use tools and perform tasks. Enterprises have been opened up. As a result of agentic AI and vision language models, we now are seeing a breakthrough in physical AI, in robotics, autonomous systems. So the last year, AI has made tremendous progress and agentic systems, reasoning systems is completely revolutionary.

This presents a fascinating paradox in terms of who captures value from AI. To the extent that reasoning produces better results — which is the primary thrust of research of the major AI labs — is the extent that Nvidia captures more profits, because the demand for tokens skyrockets; on the flipside, if reasoning showed diminishing returns, the quality of models from AI labs would arguably plateau, but their ability to capture profits would actually increase!

AI labs are stuck in a bit of a prisoner’s dilemma: they all feel the need to improve model performance to stay ahead of the competition, but the way in which they do that actually destroys their profitability; Nvidia, meanwhile, is the warden, making ever more money the more that AI labs lose it.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
