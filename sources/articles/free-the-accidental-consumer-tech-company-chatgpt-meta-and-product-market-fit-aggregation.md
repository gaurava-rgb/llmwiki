---
title: "[FREE] The Accidental Consumer Tech Company; ChatGPT, Meta, and Product-Market Fit; Aggregation and APIs"
reader_id: "01jzqta7n0cx2n8bjnexdw944w"
notion_page_id: "3484ebe7-f118-8192-a761-cf0c0ec2ed71"
category: "article"
source_type: "Reader add from clipboard"
reader_url: "https://read.readwise.io/read/01jzqta7n0cx2n8bjnexdw944w"
source_url: "https://stratechery.com/2023/the-accidental-consumer-tech-company-chatgpt-meta-and-product-market-fit-aggregation-and-apis/?scroll_to_last=1"
author: "Stratechery by Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2023-03-28"
saved_at: "2025-07-09"
reading_time: "10 mins"
summary: "OpenAI's ChatGPT rapidly grew to over 100 million users, transforming from a research-focused company into a major consumer tech platform. This success highlights the importance of product-market fit, where user demand drives growth and ambition. As ChatGPT evolves, it competes effectively against established players like Microsoft, emphasizing the value of superior products and customer acquisition strategies."
content_hash: "4f0081c68ddf82109ec0a3b6ca0eaf30b9c596e4876f81346f64da426f232a50"
---

Good morning,

Yesterday’s episode of [Sharp Tech](<https://sharptech.fm/member/episode/evaluating-ai-risk-and-entering-an-era-of-incredible-unknowns>) discussed AI risk and the incredibly uncertain environment we are entering. You can listen at the above link, or add Sharp Tech to your podcast player using the link at the bottom of this email.

On to the update:

### The Accidental Consumer Tech Company

In yesterday’s Article [ChatGPT Gets a Computer](<https://stratechery.com/2023/chatgpt-learns-computing/>) I primarily wanted to explore the nature of AI and how the addition of Wolfram|Alpha in particular highlighted how the experience of using an LLM was fundamentally different from that of what we usually think of as computing. There are, though, more traditional strategic questions that I wanted to touch on today.

Last November, OpenAI was an exciting [fat startup](<https://a16z.com/2010/03/17/the-case-for-the-fat-startup/>) making an audacious bet on an AI future (albeit with a [very unconventional structure](<https://stratechery.com/2022/dall-e-open-to-all-openai-and-openness-openai-opportunities-and-threats/>)). The most obvious business model for the research-focused company was the OpenAI API, access to which was sold on a usage basis.

Then came ChatGPT. Within a matter of weeks ChatGPT had over 100 million users, marking the fastest growth of a consumer app ever, and by all accounts [it’s still growing rapidly](<https://aibusiness.com/nlp/chatgpt-passes-1b-page-views>); OpenAI, whether they intended to or not, suddenly found itself a consumer tech company.

Go back to [the first interview I conducted with Nat Friedman and Daniel Gross last October](<https://stratechery.com/2022/an-interview-with-daniel-gross-and-nat-friedman-about-the-democratization-of-ai/>); Friedman said of his search for AI product companies:

> I left GitHub thinking, “Well, the AI revolution’s here and there’s now going to be an immediate wave of other people tinkering with these models and developing products”, and then there kind of wasn’t and I thought that was really surprising. So the situation that we’re in now is the researchers have just raced ahead and they’ve delivered this bounty of new capabilities to the world in an accelerating way, they’re doing it every day. So we now have this capability overhang that’s just hanging out over the world and, bizarrely, entrepreneurs and product people have only just begun to digest these new capabilities and to ask the question, “What’s the product you can now build that you couldn’t build before that people really want to use?” I think we actually have a shortage.
>
> Interestingly, I think one of the reasons for this is because people are mimicking OpenAI, which is somewhere between the startup and a research lab. So there’s been a generation of these AI startups that style themselves like research labs where the currency of status and prestige is publishing and citations, not customers and products. We’re just trying to, I think, tell the story and encourage other people who are interested in doing this to build these AI products, because we think it’ll actually feed back to the research world in a useful way. We keep hearing these narratives about how AI is going to solve reasoning over time. I think a very good test for whether it’s actually doing that is something like Copilot, where if it is doing that, it’s going to start writing close to 100% of your code in time.

There are not, needless to say, a shortage of people paying attention to products now, a topic I touch on in another interview with Friedman and Gross that will publish on Thursday. The bit about OpenAI, though, is an important one: this really isn’t an entity that was created to be a consumer tech company, and not just because of its weird corporate structure; Friedman’s point is that the culture wasn’t that of a consumer tech company either.

This is the first reason why I thought last week’s launch of [ChatGPT plugins](<https://openai.com/blog/chatgpt-plugins>) was so important: to me it signaled a major shift in ambition. ChatGPT may have started out as a fun demo, but now it is well on its way to being the next major consumer tech _platform_. And yes, that may have been obvious — those usage numbers don’t lie — but I think this launch was meaningful for what it signaled about OpenAI’s acceptance of that reality.

### ChatGPT, Meta, and Product-Market Fit

There is another interesting meta observation to make: there is no one in tech who desires a traditional platform more than Meta’s Mark Zuckerberg. As far back as 2013 [I was arguing that mobile saved Facebook from Zuckerberg’s platform obsession](<https://stratechery.com/2013/mobile-makes-facebook-just-an-app-thats-great-news/>) by forcing the company to focus on simply being an advertising platform instead of a developer platform; a year later [I was very critical of Facebook’s acquisition of Oculus](<https://stratechery.com/2014/face-future/>) because I thought Zuckerberg’s desire for a platform was making him overlook VR’s fundamental shortcomings:

> The power of computing, at least in my world view, was best articulated by — who else — Steve Jobs, years ago:
>
> What is so powerful about this analogy — that the computer is a bicycle for the mind — is that it elevates the humanity of a desired action, in this case transportation, and inserts the computer as an aid. This is exactly what the iPhone and the smartphones that followed have done for people: instead of a computer being a destination, it’s something that is always with us, ready to call up a map, or a restaurant recommendation, or simply fill time with a flapping bird. To put it another way, mobile is a big deal not because we use computers more, but because a computer is with us in more places.
>
> Envisioning a future in which Oculus’ technology is the dominant platform is diametrically opposed: it’s a reality where humans _retreat_ from day-to-day activities in favor of computers. This idea — a life lived in computers — is something that appeals to the technically predisposed; who among us spends all day in front a glowing screen, and then goes home to do the exact same? I’m sure Zuckerberg is in that boat. But it’s a much smaller boat than many technologists realize.
>
> For most people, computers are a means, not an end. Computers help them create music, or write novels, communicate, wayfind, or hookup. To use Jobs’ analogy, it’s not that people want to ride a bicycle for a bicycle’s sake, but because they want to go from Point A to Point B; offering such a person a full-featured massage chair simply misses the point.

This is, admittedly, a pretty unrealistically idealized view of how people use their phones; in fact, plenty of people go from work on a big screen to leisure on small one, and retreat from the real world in favor of computers — maybe that is a reason to be more bullish about VR experiences than I was at the time (and, of course, Meta will emphasize that their long-run goal is AR).

At the same time, the explosive growth of OpenAI’s ChatGPT — which, it must be noted, has raised less money in its existence than Meta lost on its Reality Labs division last year (albeit with massive Microsoft discounts on computing), and has a subscription business that I’ve heard is already at a 9-figure run rate — suggests that the overall paradigm still holds: people are incredibly excited about an AI _Assistant_ which, as the name suggests, helps them, as opposed to immerses them (although [that’s definitely going to be a market](<https://stratechery.com/2023/from-bing-to-sydney-search-as-distraction-sentient-ai/>)!).

This takes me back to Marc Andreessen’s famous essay about [Product-Market Fit](<https://pmarchive.com/guide_to_startups_part4.html>):

> I’ll assert that market is the most important factor in a startup’s success or failure. Why? In a great market — a market with lots of real potential customers — the market pulls product out of the startup.

As I noted above, the market didn’t so much pull ChatGPT out of OpenAI as they pulled the ambition to be a consumer tech company out of a group of researchers.

> The only thing that matters is getting to product/market fit. Product/market fit means being in a good market with a product that can satisfy that market.
>
> You can always feel when product/market fit isn’t happening. The customers aren’t quite getting value out of the product, word of mouth isn’t spreading, usage isn’t growing that fast, press reviews are kind of “blah”, the sales cycle takes too long, and lots of deals never close.
>
> And you can always feel product/market fit when it’s happening. The customers are buying the product just as fast as you can make it — or usage is growing just as fast as you can add more servers. Money from customers is piling up in your company checking account. You’re hiring sales and customer support staff as fast as you can. Reporters are calling because they’ve heard about your hot new thing and they want to talk to you about it. You start getting entrepreneur of the year awards from Harvard Business School. Investment bankers are staking out your house. You could eat free for a year at Buck’s.

Obviously ChatGPT has product-market fit; what is notable is this bit where Andreessen notes that product quality _usually_ isn’t enough:

> Can’t great products sometimes create huge new markets? Absolutely. This is a best case scenario, though.
>
> VMWare is the most recent company to have done it — VMWare’s product was so profoundly transformative out of the gate that it catalyzed a whole new movement toward operating system virtualization, which turns out to be a monster market. And of course, in this scenario, it also doesn’t really matter how good your team is, as long as the team is good enough to develop the product to the baseline level of quality the market requires and get it fundamentally to market.
>
> Understand I’m not saying that you should shoot low in terms of quality of team, or that VMWare’s team was not incredibly strong—it was, and is. I’m saying, bring a product as transformative as VMWare’s to market and you’re going to succeed, full stop. Short of that, I wouldn’t count on your product creating a new market from scratch.

This is obviously the route OpenAI has taken, and I think I would amend Andreessen’s observation slightly: when it comes to meaningful consumer tech companies, the product is actually the most important. The key to consumer products is efficient customer acquisition, which means word-of-mouth and/or network effects; ChatGPT doesn’t really have the latter (yes, it gets feedback), but it has an astronomical amount of the former (and, for what it’s worth, playing around with [Friedman’s compare tool](<https://nat.dev/compare>) definitely leaves the impression that OpenAI currently has the best product). Indeed, the product that ChatGPT’s emergence most reminds me of is Google: it simply was better than anything else on the market, which meant it didn’t matter that it came from a couple of university students (the origin stories are not dissimilar!).

Moreover, just like Google — and in opposition to Zuckerberg’s obsession with hardware — ChatGPT is so good people find a way to use it. There isn’t even an app! And yet there is now, a mere four months in, a platform.

### Aggregation and APIs

I wrote near the end of yesterday’s Article:

> Wolfram|Alpha isn’t the only plugin, of course: right now there are 11 plugins in categories like Travel (Expedia and Kayak), restaurant reservations (OpenTable), and Zapier, which opens the door to 5,000+ other apps (the plugin to search the web isn’t currently available); they are all presented in what is being called the “Plugin store.” The Instacart integration was particularly delightful…
>
> ChatGPT isn’t actually delivering me groceries — but it’s not far off! One limitation is I actually had to select the Instacart plugin; you can only have 3 loaded at a time. Still, that is a limitation that will be overcome, and it seems certain that there will be many more plugins to come; one could certainly imagine OpenAI both allowing customers to choose and also selling default plugin status for certain categories on an auction basis, using the knowledge it gains about users.

That is the business model of an Aggregator; an Aggregator is a company that controls demand; a company controls demand by building a compelling product that customers choose to use of their own volition; a massive customer base drives the creation of a platform; a platform gives the company power over supply. ChatGPT, needless to say, is an Aggregator, and plug-ins are perfectly aligned with this reality: they both make the product significantly better and make for an obvious business model, above and beyond ChatGPT’s subscription offering.

That noted, in this world, what exactly is the point of having an API that is completely disconnected from the consumer user experience, and which implies support and backwards compatibility for a usage-based consumption model that actually makes your core product worse (by using up GPUs)? That’s why I wasn’t surprised when OpenAI [killed support for the Codex API](<https://twitter.com/goodside/status/1638064664046186496>); after an outcry CEO Sam Altman [said that OpenAI would preserve the API for researchers](<https://twitter.com/sama/status/1638576434485825536>), which I guess is in line with whatever remains of OpenAI’s mission.

However, from a cold-blooded business analysis perspective, OpenAI didn’t go far enough: yes, the company has had an API for a long time, and once thought it was its business model; ChatGPT, though, made it a consumer tech company, and the next step after accepting that reality is making the hard business decisions that entails — including not wasting precious time and resources, including GPU capacity — on maintaining APIs that other companies depend on.

I doubt OpenAI will kill its API, to be clear, at least not for now, but another way to state this analysis more gently is that any startup building on OpenAI’s API would do well to consider [the Azure alternative](<https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview>): supporting APIs forever is what the Microsoft monopoly was built on, and I’m sure the company is eager to lock in the next generation of companies on Azure.

On the flip side, I think that ChatGPT + plugins means that Bing might not make the ultimate market share progress that Microsoft hopes: while OpenAI withdrew the web plugin at some point over the weekend, I’m sure it’s coming back, and the reality is that in the consumer space ChatGPT already has the mindshare and, in my estimation, the better user experience.

Of course we have seen clearly compatible companies fight on each other’s turf to their collective detriment (e.g. Apple and Google), but the fact that Microsoft and OpenAI are joined at the hip will perhaps make their coopetition tilt more towards the “cooperate” part than the “competition” part. That’s for them to decide, though; its customers who are the big winners, which is always the origin story of a new Aggregator.

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!
