---
title: "AWS re:Invent, Agents for AWS, Nova Forge"
reader_id: "01kbjn7gwxsr27xkpm0vp5etye"
notion_page_id: "3464ebe7-f118-81de-9358-d5436da351b3"
reader_url: "https://read.readwise.io/read/01kbjn7gwxsr27xkpm0vp5etye"
source_url: "https://stratechery.com/2025/aws-reinvent-agents-for-aws-nova-forge/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-12-03"
saved_at: "2025-12-03"
reading_time: "10 mins"
summary: "AWS re:Invent sought to present AI solutions in the spirit of AWS' original impact on startups; the real targets may be the startups from that era, not the current one."
content_hash: "927da7dd67a067f805d018d11075af0168b0d2e900f227afcd8372e62ba47d96"
---

AWS re:Invent sought to present AI solutions in the spirit of AWS' original impact on startups; the real targets may be the startups from that era, not the current one.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On [this week’s episode of Sharp China](<https://sharpchina.fm/member/episode/trump-takaichi-and-a-game-of-telephone-japan-jawboning-continues-an-internet-governance-study-session-china-making-trade-impossible>), Bill and Andrew discuss the recent phone call between Presidents Trump and Xi, Trump and Japan’s prime minister, and the PRC’s ongoing tensions with Japan.

On to the Update:

### AWS re:Invent

From [Bloomberg](<https://www.bloomberg.com/news/articles/2025-12-02/amazon-rushes-latest-ai-chip-to-market-to-take-on-nvidia-google>):

> Amazon.com Inc.’s cloud unit raced to get the latest version of its artificial intelligence chip to market, renewing efforts to sell hardware capable of rivaling products from Nvidia Corp. and Google. The accelerator, called Trainium3, was recently installed in a few data centers and will be available for customers beginning on Tuesday, Dave Brown, a vice president with Amazon Web Services, said in an interview. “As we get into early next year we’ll start to scale out very, very quickly,” he said.
>
> The chip push is a key element of Amazon’s strategy to stand out in AI. AWS is the largest seller of rented computing power and data storage. But it has struggled to replicate that dominance among leading developers of AI tools, as some companies opt instead to rely on Microsoft Corp., which has close ties to ChatGPT maker OpenAI, or Alphabet Inc.’s Google…
>
> Amazon hopes to entice companies looking for a bargain. Trainium chips are capable of powering the intensive calculations behind AI models more cheaply and efficiently than Nvidia’s market-leading graphics processing units, according to the company. “We’ve been very pleased with our ability to get the right price performance with Trainium,” Brown said.

Stratechery Updates follow a usual template: I post a snippet from a news provider — usually the Wall Street Journal or Bloomberg — about the topic I want to discuss, and then I discuss it. However, this is always a challenge when it comes to big keynotes, particularly enterprise-focused ones like yesterday’s [AWS’ re:Invent opening keynote](<https://www.youtube.com/live/rpsh_UBQY14>): there are so many different announcements that my usual sources usually just pick one to focus on, and if it fits into a juicy ongoing narrative, all the better!

So it is with this Bloomberg article about Trainium taking on Nvidia (which was the same focus of the [Wall Street Journal](<https://www.wsj.com/tech/ai/amazons-custom-chips-pose-another-threat-to-nvidia-8aa19f5b>)), and to be clear, I get it. Trainium 3 is a real announcement, and of course the goal is for AWS to gain cost control over its AI offerings and not be subject to Nvidia’s margins. We’ll see how Trainium 3 does in the real world, but the fact that Anthropic reportedly has had much better results with TPUs, and recently signed a deal with Nvidia, isn’t exactly encouraging (although the work that Anthropic has put into being able to run across different chips is very smart, and in-line with the company’s [smart approach to the enterprise](<https://stratechery.com/2025/opus-4-5-and-anthropics-aligned-enterprise-strategy-chatgpt-shopping-research-meta-to-use-tpus/>)).

What is ultimately more productive, in my mind, is actually watching the keynotes, particularly the framing that the company itself puts on their announcements, and I thought AWS CEO Matt Garman’s introduction was quite interesting.

> So why do we do this? What motivates us? Why are we just as passionate today as we were 20 years ago when we first launched AWS? What drives us every day is giving you all the freedom to invent. This has been our motivation since when we started AWS at the very beginning. We wanted to make it possible for every developer or inventor in her dorm room or garage to access the technology infrastructure and capabilities so that they could build whatever they could imagine. 20 years ago, it just wasn’t possible for developers or builders to get the servers or compute capacity that they needed without investing significant capital and time. Developers were spending way too much of their time procuring servers, managing infrastructure, and not enough of that time building. We’ve actually felt this ourselves inside of Amazon. We had a company full of builders who had these incredible ideas of how they could make our customers’ lives better, but they couldn’t move as fast as they wanted. So we asked ourselves, “Why not?” Why couldn’t developers focus on building instead of on infrastructure? Why couldn’t we bring the time and the cost of experimentation down to zero? Why not make every idea possible? And we’ve spent the last two decades innovating towards those goals. Giving all of you the freedom to keep inventing is why we’re here today.
>
> Right now we’re witnessing an explosion of invention with AI. Every single customer experience, every single company, frankly, every single industry is in the process right now of being reinvented, and we’re still in the early days of what AI is going to deliver, and the technology is iterating faster than anything any of us have ever witnessed before. It wasn’t that long ago that we were all testing and experimenting with chatbots, and now it seems like there’s something new every day. But when I speak to customers, and many of you out there, you haven’t yet seen the returns that match up to the promise of AI. The true value of AI has not yet been unlocked, but a lot of that is changing fast too. AI assistants are starting to give way to AI agents that can perform tasks and automate on your behalf. This is where we’re starting to see material business returns from your AI investments.
>
> I believe that the advent of AI agents has brought us to an inflection point in AI’s trajectory. It’s turning from a technical wonder into something that delivers us real value. This change is going to have as much impact on your business as the Internet or the cloud. I believe that in the future there’s going to be billions of agents inside of every company, and across every imaginable field. Already we see agents accelerating health care discoveries, improving customer service, making payroll processing more efficient, and agents are also starting to scale people’s impact, up by 10x in some cases, so they have more time to invent more. Wouldn’t it be awesome if everyone could see that level of impact? We think so, and that’s why we ask the question, “Why not?” Getting to a future of billions of agents, where every organization is getting real-world value and results from AI, is going to require us to push the limits of what’s possible with the infrastructure. We’re going to have to invent new building blocks for agentic systems and applications. We want to reimagine every single process in the way that all of us work. At AWS we’ve been innovating at all of the layers of the stack to give you all the freedom to invent what’s next.

I did admittedly chuckle about the invocation of passion in terms of motivation; I’m pretty sure what motivates Amazon is making a lot of money and seeing the stock price go up-and-to-the-right. But if I can get past that moment of cynicism, everything Garman said about the genesis of AWS is pretty much true. I wrote in 2015’s [Venture Capital and the Internet’s Impact](<https://stratechery.com/2015/venture-capital-and-the-internets-impact/>):

> In 2006, though, something changed, and that something was the launch of Amazon Web Services. Because a company pays for AWS resources as they use them, it is possible to create an entirely new app for basically $0 in your spare time. Or, alternately, if you want to make a real go of it, a founder’s only costs are his or her forgone salary and the cost of hiring whomever he or she deems necessary to get a minimum viable product out the door. In dollar terms that means the cost of building a new idea has plummeted from the millions to the (low) hundreds of thousands.

It’s difficult to overstate what a big deal AWS specifically and the cloud generally has been to the startup ecosystem; that Article specifically was about how AWS transformed the venture capital industry, giving rise to angels in particular, and moving the barrier of company viability away from idea to actual market traction (how venture capital has continued to transform into an intense focus on growth and winner-take-all markets is the subject of another Article).

The point Garman is making in this segment, however, has to do with abstraction: AWS abstracted away infrastructure from being an up-front capital expenditure that was a pre-requisite to building something new to an operational cost that scaled in line with success; the pitch he is making is that AWS wants to do the same with AI. Instead of having to build infrastructure for an agent, you can just build an agent — or hire one of AWS’s (more on this is in a moment). And this, by extension, is where the Trainium story actually matters. In this vision, companies don’t actually need to care about what chip is powering their infrastructure; what matters is that Amazon provides a service that has an operational cost that scales in line with success. Amazon’s business is in providing that service at the lowest cost possible, which is to say that the real target customer for Trainium’s lower costs is Amazon and its AI service margins.

### Agents for AWS

There are two specific announcements Garman made that I want to highlight, and the first is Agents from AWS. Garman said in the keynote:

> Now with the tools and services we’re providing, we know that our customers and partners out there are going to build a huge number of incredibly impactful agents. But you can also expect that some of the most capable, powerful, agentic solutions are going to come direct from AWS…as we thought about what agents should we build and which experiences could we build reimagined, we focused on areas where we thought we could bring some differentiated expertise to our customers.

The agents Garman announced included:

  * Amazon Quick, a consumer AI experience that delivers insights from across a company’s various data sources
  * Amazon Connect, a contact center AI experience that resolves issues and recommends solutions to customer service agents
  * AWS Transform, which modernizes code bases
  * AWS Kiro, for structured AI coding
  * AWS Security Agent, for continually securing systems, scanning them, and testing them
  * AWS DevOps Agent, for proactively identifying and resolving incidents for production applications



What is so compelling about these offerings is that the first, best customer for all of them is Amazon itself:

  * Amazon has huge amounts of data across its business that needs to be analyzed
  * Amazon has a massive customer service burden in its e-commerce business
  * Amazon has old code that needs to be modernized
  * Amazon is continuously generating new code
  * Amazon is one of the biggest targets in the world
  * Amazon has a plethora of services that need continual support



If you sign up for these agents, you’re getting the same service that Amazon built for itself; that’s always been one of the selling points for AWS as a whole, and it’s a powerful one for these agents.

### Nova Forge

From [CNBC](<https://www.cnbc.com/2025/12/02/amazon-nova-forge-lets-clients-customize-ai-models-for-100000-a-year.html>):

> Amazon has found a way to let cloud clients extensively customize generative AI models. The catch is that the system costs $100,000 per year. The Nova Forge offering from Amazon Web Services gives organizations access to Amazon’s AI models in various stages of training so they can incorporate their own data earlier in the process. Already, companies can fine-tune large language models after they’ve been trained. The results with Nova Forge will lean more heavily on the data that customers supply. Nova Forge customers will also have the option to refine open-weight models, but training data and computing infrastructure are not included.

Right now you have two ways to incorporate your company’s data into an AI model: first, you can use RAG to basically have a model search your company’s data in the context of providing an answer. Second, you can post-train a model on your company’s data. The shortcoming in both approaches is that your company’s data isn’t actually in the model, which can lead to unsatisfying results.

Nova Forge is an offering built on AWS’s internally produced AI models; because they own the Nova models, they own the training checkpoints. What you can do with Nova Forge is choose a checkpoint — say, when the model is 80% trained — and infuse your company’s data at that point, so that the data is integrated into the model itself, and not simply searched or trained-in after-the-fact.

I think this is a really compelling offering, even if Nova is fairly middling as a model. After all, what is more useful: an OK model that actually knows your company, or a leading-edge model that is hacking around the edges to give relevant answers?

What this offering also speaks to, however, is a broader observation about AWS in the age of AI. Whereas AWS in the beginning was the greatest possible gift to startups, AWS in the age of AI seems solidly focused on helping established enterprises utilize AI in the most effective way possible. So many of these offerings are compelling when you already have established data and processes and code bases; AWS might have made a lot of startups possible over the last 20 years, but its most compelling AI offerings may in the end be focused on the same companies, which are now established enterprises. If you’re starting from scratch, is this where you would go?

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
