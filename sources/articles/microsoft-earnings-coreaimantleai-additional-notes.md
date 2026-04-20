---
title: "Microsoft Earnings, CoreAI/MantleAI, Additional Notes"
reader_id: "01k9wf5wj59tafkkhhve5x7k5z"
notion_page_id: "3484ebe7-f118-81ef-a229-ed78ef0052c9"
reader_url: "https://read.readwise.io/read/01k9wf5wj59tafkkhhve5x7k5z"
source_url: "https://stratechery.com/2025/microsoft-earnings-coreai-mantleai-additional-notes/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-11-12"
saved_at: "2025-11-12"
reading_time: "12 mins"
summary: "Microsoft declares independence from OpenAI and sketches out its future role building scaffolding for AI. Plus, Windows is tiny now."
content_hash: "313f66cf1cb24e73325653355c405868572db8a6975847e3689d7f336af54b5e"
---

Microsoft declares independence from OpenAI and sketches out its future role building scaffolding for AI. Plus, Windows is tiny now.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On [this week’s episode of Sharp China](<https://sharpchina.fm/member/episode/us-china-follow-through-new-xi-textbooks-and-a-new-aircraft-carrier-a-wolf-warrior-greets-japans-pm-more-setbacks-for-nvidia>), Andrew and Bill discuss the implementation of the U.S.-China trade deal, and more setbacks for Nvidia.

On to the Update:

### Microsoft Earnings

From the [Wall Street Journal](<https://www.wsj.com/tech/ai/microsoft-msft-q1-earnings-report-2026-b342eefd>):

> Microsoft is seeing more demand for its cloud computing and AI services than it can keep up with, a challenge that is supercharging the company’s income. Demand for the tech giant’s cloud services is so great that Microsoft will boost its AI capacity by more than 80% this year and double its total data-center footprint in the next two years, Chief Executive Satya Nadella told investors late Wednesday. That outlook means Microsoft now expects to spend more than previously projected on its AI infrastructure this fiscal year — and still be short of the capacity it will need to meet demand.
>
> Companies have been eager to host and train their artificial-intelligence models on Microsoft’s wide array of services. That keeps paying off for Microsoft, which reported revenue of $77.7 billion for its first fiscal quarter. The figure exceeded Wall Street expectations. The company’s closely watched Azure cloud business grew by about 40%, also topping expectations. Operating income increased 24% to $38 billion, more than consensus projections. The company said its net income was $27.7 billion, or $3.72 per diluted share.
>
> Despite beating Wall Street’s projections, Microsoft shares ticked lower by nearly 4% in after-hours trading, as the company reported substantial spending on cloud and AI infrastructure. The company took a $3.1 billion charge from its massive investment in Open AI. Some investors are worried there is overreliance on cloud contracts from OpenAI, reflecting a broader industry concern.

I’m a bit late on these earnings, but Microsoft’s stock is still down a bit, and CEO Satya Nadella seemed to anticipate investor concerns. His message on [the earnings call](<https://seekingalpha.com/article/4835092-microsoft-corporation-msft-q1-2026-earnings-call-transcript>) came down to one word: “fungibility”, which he repeated in some variation eight times. From his prepared remarks:

> We have the most expansive data center fleet for the AI era, and we are adding capacity at an unprecedented scale. We will increase our total AI capacity by over 80% this year and roughly double our total data center footprint over the next 2 years, reflecting the demand signals we see. Just this quarter, we announced the world’s most powerful AI data center, Fairwater in Wisconsin, which will go online next year and scale to 2 gigawatts alone. And we have deployed the world’s first large-scale cluster of Nvidia GB300s.
>
> We are building a fungible fleet that’s been continuously modernized and spans all stages of the AI life cycle, from pretraining to post training, to synthetic data generation and inference. And it also goes beyond GenAI workloads to recommendation engines, databases and streaming. We’re optimizing this fleet across silicon systems and software to maximize performance and efficiency.
>
> It’s this combination of fungibility and continuous optimization that allows us to deliver the best ROI and TCO for us and our customers. For example, during the quarter, we increased the token throughput for GPT-4.1 and GPT-5, two of the most widely used models, by over 30% per GPU.

This is, in many respects, the same argument that [Meta CEO Mark Zuckerberg was trying to make on Meta’s earnings call](<https://stratechery.com/2025/google-earnings-meta-earnings-the-cost-of-reality-labs/>): there are so many applications for GPUs that Microsoft would in fact be derelict in not buying more; moreover, the way to gain maximum leverage on its R&D is to have an ever larger fleet from which to wring continual efficiency gains.

What is interesting is the pecking order when it comes to using those GPUs. CFO Amy Hood was asked about how much more money Azure could have made if it had more supply, and whether or not Microsoft risked losing customers to other hyperscalers, and she was very clear that Microsoft came first:

> It’s always hard to quantify precisely what would have been the revenue impact in quarter. But I would offer a way to think about it is Azure probably does bear most of the revenue impact. Because when you think about real priorities that you have to fill first, it’s obviously the increasing usage and adoption and sales we’ve seen of M365 Copilot and the usage of Copilot chat, which we’ve seen very different patterns, which we’re encouraged by. It’s the adoption of security features. It’s the GitHub momentum. And so when you’re thinking about it, that is where it is a priority for us to allocate resourcing there first. And so you are right to ask how do I think about that.
>
> We’ve worked very hard to try to mitigate it as best we can, but we have been short in Azure, and we’ve been clear on it. And I would say the other 2 priorities that I haven’t mentioned maybe as much before is also just making sure our product teams and the AI talent that we’ve been able to hire into the company really over the past 1.5 years have access also to significant capacity because we’re seeing it make the product better in a loop that is adding great benefit today into products people are using today for real-world work. And so we are making that a priority to make sure our research teams have that as well as our product engineering teams. And yes, it does impact Azure directly. That is the place where you see that prioritization. But I think it’s probably hard for me to give an exact number, but it is safe to say that the number could be higher.

Nadella doubled down on this point in response to the next question:

> I mean for us, again, just always goes back to, I think, the core principle, which is build a fleet that is fungible across the planet and works for third-party and first-party and research. So that’s essentially what we have done. And so when some demand comes in shape, that don’t fit that goal, where it’s too concentrated, not just by customer, by location, by type of skewing, right?
>
> I think Amy mentioned some very key things. When you think about the margin profile of a hyperscaler, you’ve got to remember this, the AI accelerator piece, but there’s compute, there’s storage. And so if all of the demand just comes for just one meter, that’s really not a long-term business we want to be in. That’s even from a third party. We have to balance it with all of our first-party stuff because that’s after all a different margin stack for us. And then we have to fund our own R&D and model capability because in the long run, that’s what’s going to differentiate us.
>
> And so I look at all of those. We sort of use all of that to make sure we are saying yes to all the demand that we want, we say no to some of the demand that may be something that we could serve, but it’s not in our long-term interest. And so that’s sort of the decision-making we have done, and we feel very, very good about the decisions. In some sense, I feel even each time we say no to, the day after, I feel better.

Nadella and Hood both opened the call celebrating Microsoft’s deal with OpenAI; these answers seemed to be a declaration of independence. It’s fair to question how valid that is — OpenAI did just commit to buying another $250 billion worth of compute — but clearly Nadella and Hood wanted to communicate that (1) they were buying a lot of broadly useful compute, (2) that compute was first and foremost for Microsoft, and (3) the company has said no to some 3rd-party requests — almost certainly OpenAI — because they exposed the company to too much risk without broad-based benefit or utility.

### CoreAI/MantleAI

That raises another question: if Microsoft is willing to let OpenAI buy compute elsewhere, and set itself up to lose IP access in a few years, then what is the long-term value it is providing? Nadella’s answer was scaffolding:

> I think there are 2 parts. We feel very, very good about even this, I’d say, the new agreement that we now have with OpenAI because I think even, it just creates more certainty to all of the IP relationship we have as it relates to even this definition of AGI. But beyond that, I think your question touches on something that’s pretty important, which is how are these AI systems going to truly be deployed in the real world and make a real difference and make a return for both the customers who are deploying them and then obviously, the providers of these systems.
>
> And I think the best way to characterize the situation is that even as the intelligence capability increases, let’s even say, exponentially like model version over model version, the problem is it’s always going to still be jagged, right? I think the term people use is the jagged intelligence, even — or spiky intelligence, right? So you may even have a capability that’s fantastic at a particular task, but it may not uniformly grow. So what is required is in fact, these systems, whether it is GitHub Agent HQ or the M365 Copilot system. Don’t think of this as a product. Think of it as a system that in some sense smooths out those jagged edges, and really helps the capability…
>
> The reason I say all of that is because that’s the type of construction that will be needed even when the model is magical, all powerful. I think we will be in this jagged intelligence phase for a long time. So one of the fundamental things that these — whether it’s GitHub, whether it’s security, whether it’s M365, the 3 main domains we’re in — we feel very, very good about building these as organizing layers for agents to help customers.

This gets at the collar trade [I wrote about previously](<https://stratechery.com/2025/nvidia-gtc-in-dc-qualcomms-ai-chip-openais-restructuring/>) in the context of the deal with OpenAI. If OpenAI makes Microsoft obsolete, well, Microsoft owns a big chunk of OpenAI; on the other hand, if OpenAI ends up being one model of many, all of which have their strengths and weaknesses, then Microsoft is positioning itself to be the entity that makes it all useful. The actual team dedicated to building this is called “CoreAI”, which Nadella introduced in [a January blog post](<https://blogs.microsoft.com/blog/2025/01/13/introducing-core-ai-platform-and-tools/>):

> We will build agentic applications with memory, entitlements, and action space that will inherit powerful model capabilities. And we will adapt these capabilities for enhanced performance and safety across roles, business processes, and industry domains. Further, how we build, deploy, and maintain code for these AI applications is also fundamentally changing and becoming agentic.
>
> This is leading to a new AI-first app stack — one with new UI/UX patterns, runtimes to build with agents, orchestrate multiple agents, and a reimagined management and observability layer. In this world, Azure must become the infrastructure for AI, while we build our AI platform and developer tools — spanning Azure AI Foundry, GitHub, and VS Code — on top of it. In other words, our AI platform and tools will come together to create agents, and these agents will come together to change every SaaS application category, and building custom applications will be driven by software (i.e. “service as software”).
>
> The good news is that we have been working at this for more than two years and have learned a lot in terms of the systems, app platform, and tools required for the AI era. To more rapidly and boldly advance our roadmap across each of these layers, we are creating a new engineering organization: CoreAI – Platform and Tools.

I actually find the name “CoreAI” confusing, because, as I understand this organization’s goals, it is actually more akin to “MantleAI”:

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/11/Microsoft-core-1.png?resize=1330%2C1140&ssl=1)

What Microsoft is seeking to do is, in some respects, what it did with the PC. The “core” of a PC was an Intel processor; the actual interface layer for applications and users, however — the mantle, if you will — was Windows. That was where the user interface was, and the APIs that developers used to make apps; no one wrote directly to the CPU.

In this case, Microsoft is making the case that users and application developers and agents need something more stable to build on than just the models, and that something is exactly what the CoreAI-should-be-called-MantleAI team is seeking to build; I can certainly see the value today, and Nadella’s bet is that the value will persist even if/when models continue to increase in capabilities.

And, if the real core swallows everything, Microsoft still wins (at least if it’s OpenAI).

### Additional Notes

**The Short-Lived Asset Paradox:** Hood emphasized that half of Microsoft’s planned spending was for short-lived assets — GPUs and CPUs — and that that spending roughly matched revenue that was already booked; in other words, Microsoft wasn’t spending speculatively. This, however, is in tension with [the argument that Microsoft’s real shortage is power](<https://stratechery.com/2025/the-benefits-of-bubbles/>), which requires much longer-term agreements, and well in advance of GPU purchases. To put it another way, it’s fine to say that half of your planned capex is relatively risk-free, but that doesn’t change the fact that that means the other half is riskier.

**Expansive Revenue Streams:** Nadella noted that AI is actually increasing the revenue opportunity for Microsoft:

> The other aspect, which Amy spoke to is we have some of the best agent systems that matter in the high-value domains, right? It’s in information work. That’s the Copilot system. Coding, I mean, I should also say one of the things I like about Copilot is, I mean, Copilot ARPU is compared to M365 ARPUs, right? It’s expansive. The same thing that happened between server and cloud, like we used to always say, well, is it zero-sum, it turned out that the cloud was so much more expansive to the server market.
>
> The same thing is happening in AI because first, you could say, hey, our ARPUs are too low when it comes to M365 or you could say, we have the opportunity with AI to be much more expansive. Same thing with tools, right? I mean, the tools business was not like a leading business, whereas coding business is going to be one of the most expansive AI systems. And so we feel very good about being in that category. Same thing with security, same thing with health.
>
> So we have – and in consumer, one of the things is it’s not just about ads, it’s ads plus subscriptions that also opens up opportunity for us. So when I look at the entirety of these high-value agent systems and when we look at the efficiency of and fungibility of our fleet, that’s what gives us the confidence to invest, both the capital and the R&D talent to go after this opportunity.

That GitHub CoPilot ARPU number is very interesting. When Microsoft bought GitHub [I wrote in an Update](<https://stratechery.com/2018/microsoft-to-buy-github-a-win-for-github-facebooks-data-sharing-deals-with-device-makers/>):

> GitHub has a freemium business model: the vast majority of the company’s 24 million users don’t pay to host their code, which is public (that number, by the way, is likely higher than the total number of developers in the world); individual users can pay for private accounts (I have one for Stratechery’s WordPress theme files), but the biggest moneymaker is enterprise subscriptions, which of course offer privacy as well as a whole host of collaboration and security features, as well as versions of GitHub that run on private clouds. The company at last reports was doing about $200 million in revenue.
>
> That is certainly attractive to Microsoft, to an extent, but I suspect this is will be a purchase — presuming it goes through! — in which revenue is a bit beside the point. The implication of GitHub being used by basically all developers, if not at work than at least for their private projects, is that Microsoft now has a connection to all developers with a service that is generally beloved. That’s a big deal.

In fact, AI is turning GitHub into a real revenue driver via direct payments from developers, just like — as Nadella noted — chatbots are driving actual subscription revenue from users, even as ads are as valuable as ever.

**Tiny Windows:** One thing that jumped out to me is just how tiny Windows is these days; from Hood:

> Now to More Personal Computing. Revenue was $13.8 billion and grew 4%. Windows OEM and Devices revenue increased 6% year-over-year, significantly ahead of expectations, driven by strong demand ahead of Windows 10 end of support as well as a benefit from inventory levels that remain elevated.

To put that number in perspective, Microsoft Cloud revenue increased by $10 billion year-over-year, to $49 billion; in other words, Microsoft Cloud grew by 73.8% of the entire Windows division!

Small wonder that, in late September, [Microsoft reunified Windows internally](<https://www.theverge.com/report/787796/microsoft-windows-reorg-single-engineering-team-changes>); when the organization was split back in 2018 I wrote about [The End of Windows](<https://stratechery.com/2018/the-end-of-windows/>), which recounted how Nadella broke the product’s hold over the company and its strategy. Putting Windows back together internally doesn’t invalidate the take; rather, these revenue numbers prove how impactful and beneficial Nadella’s actions were.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
