---
title: "ChatGPT 5, Product Trade-Offs, Personality and Model Upgrades"
reader_id: "01k2hxrz474382h1sd73jj9ks8"
notion_page_id: "3484ebe7-f118-81be-9541-c396b2da4161"
reader_url: "https://read.readwise.io/read/01k2hxrz474382h1sd73jj9ks8"
source_url: "https://stratechery.com/2025/chatgpt-5-product-trade-offs-personality-and-model-upgrades/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-08-13"
saved_at: "2025-08-13"
reading_time: "18 mins"
summary: "GPT-5 seems fine; the more interesting questions are about the ChatGPT product and OpenAI’s tradeoffs."
content_hash: "c35e618c33b70c9384e5be20dd3fec961cd09edb3cb1b090459650fdfdc76f2c"
---

GPT-5 seems fine; the more interesting questions are about the ChatGPT product and OpenAI’s tradeoffs.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

Two follow-ups to [yesterday’s Update about Nvidia and China](<https://stratechery.com/2025/china-ai-chips-a-china-chip-control-framework-whither-hbm/>):

  * China is [urging companies to not use H20 chips](<https://stratechery.com/2025/china-ai-chips-a-china-chip-control-framework-whither-hbm/>), which I take to be a strong affirmation of my overall argument about how the U.S. should be seeking to drive dependency on U.S. companies.
  * One possible way that the Export Clause might not apply to Nvidia and AMD sales is if the chips are never actually entering the U.S.; I’m not totally sure how this is all accounted for — at the end of the day the power to tax lies with Congress, not the President — but I should have included that caveat in my analysis.



On to the Update, which is a bit of a weird one: I wrote this Update yesterday afternoon, but then OpenAI updated ChatGPT again late last night; the changes don’t alter my overall point, but they do make a few screenshots wrong. I’ve left the Update as is and then added a new section at the end about the changes.

### ChatGPT 5

From the [Wall Street Journal](<https://www.wsj.com/tech/ai/openai-chatgpt-5-release-d5dc674a>):

> OpenAI on Thursday announced the release of GPT-5, its most advanced AI model, a culmination of more than two years of development that saw a series of setbacks and delays. Interacting with the new technology “really feels like talking to an expert in any topic, like a Ph.D.-level expert,” Chief Executive Sam Altman said on a call with reporters Wednesday. He emphasized its ability to allow anyone to create software applications by typing in simple, English-language prompts—a process commonly referred to as “vibe coding.” In a pre-scripted demo, an OpenAI researcher asked ChatGPT to create a web application that could teach his partner French through interactive games and flashcards. The chatbot did so within minutes, writing more than 300 lines of code.
>
> The release follows a year of massive revenue growth for the company, which is still losing money at a rapid clip as it races to develop AI models with humanlike intelligence. OpenAI has largely shaken off concerns over its unstable governance structure and the loss of key top executives, some of whom have started their own companies. Investors are betting that technology advances like GPT-5 will continue powering the startup’s growth and allow it to spearhead an economic transformation that is already well under way.

I don’t have any super strong takes on the GPT-5 model specifically; I’ve used ChatGPT as normal over the past few days and have been quite pleased with the results. Answers seem tighter, better referenced, and significantly less obsequious; I also believe the hype that this new model hallucinates less than previous models. Again, though, these are early impressions undoubtedly influenced by the marketing around this new release; I expect to firm up my opinion over time.

What I am more interested in for purposes of this Update, however, is not GPT-5, but _ChatGPT 5_ , which to me is something distinct: it’s the AI user experience for the vast majority of people, as opposed to developers or programmers using the API. And, at least if you believe this tweet from Sam Altman, it’s that former group that was the focus of this release:

> GPT-5 is the smartest model we've ever done, but the main thing we pushed for is real-world utility and mass accessibility/affordability.
>
> we can release much, much smarter models, and we will, but this is something a billion+ people will benefit from.
>
> (most of the world has…
>
> — Sam Altman (@sama) [August 7, 2025](<https://twitter.com/sama/status/1953551377873117369?ref_src=twsrc%5Etfw>)

To that end, the most obvious change is in the model picker, which is dramatically simpler:

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/08/chatgpt5-1.png?resize=632%2C556&ssl=1)

This is what it used to look like:

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/08/chatgpt5-5.png?resize=366%2C271&ssl=1)

I’m actually mixing-and-matching screenshots here; the first one is mine, as a Pro subscriber. The second one I got from the web, from what I believe was a Plus subscriber; note the absense of o3-pro, which was only available to Pro subscribers. That still show up in my “Legacy models” list (which was added over the weekend):

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/08/chatgpt5-2.png?resize=628%2C784&ssl=1)

As best as I can tell, GPT-5 Pro is akin to o3-pro (now with proper capitalization!) and GPT-5 Thinking is akin to o3; I immediately defaulted to GPT-5 Thinking, inline with the fact that o3 has been my go-to model for several months now.

Indeed, it’s the entire o-series of models that make the GPT 5 hype cycle a bit hard to parse. From my perspective there has not been a two year wait for a new model, because the development of reasoning models led to an improvement that, to my mind, easily matched if not exceeded the jump from GPT-3 to GPT-4; in that light, while I expected GPT-5 to be better, I both didn’t expect it to blow my mind, nor do I think it represents some sort of slowdown in progress. It’s just another step in a progression that is both steady and — if you zoom out — still remarkably rapid.

More generally, I feel better than ever about my position that (1) people predicting imminent super intelligence that takes over the world and renders all economic activity worthless are being ridiculous and (2) people predicting that AI is a nothing-burger that won’t amount to anything meaningful are also being ridiculous. AI continues to be a big deal, and even if all progress on the leading edge stopped today, the product overhang remains massive.

### Product Trade-Offs

That last point is why I’m focused on ChatGPT specifically, and the option in the model picker I haven’t yet covered: ChatGPT 5. The big feature here is what OpenAI is calling a “Model Router”; Ethan Mollick explained on [One Useful Thing](<https://www.oneusefulthing.org/p/gpt-5-it-just-does-stuff>):

> As someone who has spent a lot of time talking to people about AI, there are two major problems I see, that, if addressed, would make most people’s AI use much more productive and much less frustrating. The first is selecting the right model to use. In general, AIs that “think” before answering (called Reasoners) are the best at hard problems. The longer they think, the better the answer, but thinking costs money and takes time. So OpenAI previously made the default ChatGPT use fast, dumb models, hiding the good stuff from most users. A surprising number of people have never seen what AI can actually do because they’re stuck on GPT-4o, and don’t know which of the confusingly-named models are better.
>
> GPT-5 does away with this by selecting models for you, automatically. GPT-5 is not one model as much as it is a switch that selects among multiple GPT-5 models of various sizes and abilities. When you ask GPT-5 for something, the AI decides which model to use and how much effort to put into “thinking.” It just does it for you. For most people, this automation will be helpful, and the results might even be shocking, because, having only used default older models, they will get to see what a Reasoner can accomplish on hard problems. But for people who use AI more seriously, there is an issue: GPT-5 is somewhat arbitrary about deciding what a hard problem is.

From what I saw online there were two big sources of consternation about this Update, and that last one hit Plus subscribers in particular: they were limited to 200 queries a week for GPT-5 Thinking, while previously they had 100 messages a week with o3, 300 messages a day with o4-mini, and 100 messages a day with o4-mini-high. In other words, explicit access to a reasoning model of some sort dropped from 2,900 queries a week to 200. The difference was supposed to be made up for by ChatGPT 5 smartly using reasoning models when appropriate, but many users felt that didn’t happen nearly enough (which was almost certainly correct).

At the same time, Altman said the use of reasoning models is increasing significantly:

> the percentage of users using reasoning models each day is significantly increasing; for example, for free users we went from <1% to 7%, and for plus users from 7% to 24%.
>
> i expect use of reasoning to greatly increase over time, so rate limit increases are important.
>
> — Sam Altman (@sama) [August 10, 2025](<https://twitter.com/sama/status/1954603417252532479?ref_src=twsrc%5Etfw>)

The important figure there is free users going from 1% to 7%: it seems likely that the vast majority of that increase is due to the model router; in other words, a significant number of free user inquiries suddenly came back with dramatically better answers than they did before this change. The Plus tier increase is notable as well: some amount of that increase was certainly due to the router, but it also seems likely that some amount of that increase was due to the cleaned up router picker. Choosing “GPT 5 Thinking” is a lot more straightforward than trying to wade through a convoluted model list, especially when the name of the reasoning models available to you — o3, o4-mini, and o4-mini-high — all seem inferior to the default 4o. In other words, a lot of Plus subscribers also got dramatically better answers thanks to this simplification.

In short, I strongly suspect that while the complainers were extremely loud — and I’m quite sympathetic to the GPT Plus subscribers who were conscious about their model selection — the actual experience of ChatGPT improved tremendously for the vast majority of users. What will be important for Altman and OpenAI going forward is to keep in mind that one of the burdens of having a massive consumer app is that every change will be met by loud resistance; the only way to know for sure if they are representative will be to look at the data, and this tweet in particular strongly suggests the change was a good one for the user base as whole.

That noted, the above tweet was in a thread that opened with Altman promising to give Plus users their reasoning allocation back:

> today we are significantly increasing rate limits for reasoning for chatgpt plus users, and all model-class limits will shortly be higher than they were before gpt-5.
>
> we will also shortly make a UI change to indicate which model is working.
>
> — Sam Altman (@sama) [August 10, 2025](<https://twitter.com/sama/status/1954602880952115603?ref_src=twsrc%5Etfw>)

This is — the previous point notwithstanding — the right thing to do. It never works well to take things away from paying customers; you need to figure out how to deliver the same product more cheaply, and, if you want to get more money, figure out [ways to upsell them](<https://x.com/sama/status/1954705761805938734>). I doubt OpenAI will make this mistake again, but that makes the fact the mistake happened particularly interesting; the driver is clearly the middle tweet in this thread: capacity trade-offs.

Here, per that tweet, is the promised follow-on from Altman:

![](https://pbs.twimg.com/profile_images/1904933748015255552/k43GMz63.jpg)

[Sam Altman](<https://twitter.com/sama>) [@sama](<https://twitter.com/sama>)

[ ](<https://twitter.com/sama/status/1955077002945585333>)

Here is how we are prioritizing compute over the next couple of months in light of the increased demand from GPT-5:



  1.
We will first make sure that current paying ChatGPT users get more total usage than they did before GPT-5.





*
We will then prioritize API demand up to the currently allocated capacity and commitments we've made to customers. (For a rough sense, we can support about an additional ~30% new API growth from where we are today with this capacity.)



*
We will then increase the quality of the free tier of ChatGPT.



*
We will then prioritize new API demand.



We are ~doubling our compute fleet over the next 5 months (!) so this situation should get better.


[Posted Aug 12, 2025 at 1:20AM](<https://twitter.com/sama/status/1955077002945585333>)

I already identified two conflicting priorities above: delivering a better experience to free and non-sophisticated Plus users versus meeting the expectations of sophisticated Plus users. The initial ChatGPT 5 launch prioritized the former over the latter, and while I think that was the right choice, the more important question was why the choice needed to be made.

That gets to the second set of conflicting priorities: ChatGPT versus the API. You can see that conflict in Altman’s compute prioritization plan:

  1. Paying ChatGPT users
  2. Current API demand
  3. Free ChatGPT users
  4. Future API demand



However, the real tradeoff already happened: [OpenAI launched GPT-5 in the API at the same time they launched ChatGPT 5](<https://openai.com/index/introducing-gpt-5-for-developers/>). The problem, however, is that it seems they didn’t have enough compute for both, which is to say that the API was prioritized over ChatGPT Plus users, who had their reasoning model access dramatically curtailed, leading to the backlash. Had OpenAI followed Altman’s tweeted prioritization schedule the company would have launched ChatGPT 5 first, without slashing paid user limits, and only then updated the API.

This conflict, I will note, has been a long-time coming; in fact, it’s part of why I have advocated that OpenAI outsource API service to Microsoft and focus solely on ChatGPT. I wrote way back in 2023 in [The Accidental Consumer Tech Company](<https://stratechery.com/2023/the-accidental-consumer-tech-company-chatgpt-meta-and-product-market-fit-aggregation-and-apis/>):

> However, from a cold-blooded business analysis perspective, OpenAI didn’t go far enough: yes, the company has had an API for a long time, and once thought it was its business model; ChatGPT, though, made it a consumer tech company, and the next step after accepting that reality is making the hard business decisions that entails — including not wasting precious time and resources, including GPU capacity — on maintaining APIs that other companies depend on.

[Earlier this year](<https://stratechery.com/2025/openai-api-updates-steelmanning-the-api-business-the-problem-with-both/>) I tried to steelman the existence of the API business, but ultimately concluded it was incompatible with the advertising business I think that OpenAI needs to build:

> It is in many respects safer and easier to, as Weil says, stick with being both a product and an API company, with business models that are broadly similar. Those businesses, however, both have competition — particularly the API. That’s going to be another natural limiter. On the other hand, a potential ad business (augmented with subscriptions, i.e. [The Unified Content Business Model](<https://stratechery.com/2023/the-unified-content-business-model/>)), will not have any competition at all! No one has — or likely will — reach the level of consumer penetration that ChatGPT has. Moreover, if they actually go in this direction, they can ensure they have no competition ever because they will be able to make more features free, making it impossible for competitors to economically match their offering. This is a hard path, to be sure, but I think it is the path that maximizes the chances of making the profits its investors are counting on.
>
> In this view, the problem with the API business is the opportunity cost it imposes on building a consumer business. First, at least in the short term, there is the cost of running out of GPUs, which happened just last month with the roll out of GPT 4.5. Second, there are all of the employees working on the API who aren’t working on building the ad business (although, granted, a lot of them probably wouldn’t want to). Third, APIs have hidden costs, like this bit from OpenAI’s announcement…
>
> To summarize:
>
>   * OpenAI has to spend resources supporting a deprecated API for at least a year.
>   * OpenAI has to spend resources supporting an API they no longer recommend using indefinitely. This means that the cost isn’t just compute resources, but also significant engineering resources to update it with new models and capabilities.
>

>
> This is the core issue: an API business is a customer support business; the Aggregator business is a consumer support business, where [everyone else in the value chain serves you](<https://stratechery.com/2025/stargate-the-end-of-microsoft-and-openai/>). OpenAI is trying to be both, but that only increases the likelihood they will be neither.

The advertising business isn’t there yet, but OpenAI did with this launch make the product better for free users; the fact they’re still trying to do everything, however, means that it was a set of customers (Plus subscribers) who are actually making them money right now that ended up getting the short end of the stick. It’s right and appropriate that OpenAI is going to now make them a priority, but that is at the cost of continuing to make the product better for free users, at least for a while (they’re 3rd in the priority list). Being everything to everyone is hard!

### Personality and Model Upgrades

From [The Verge](<https://www.theverge.com/news/756980/openai-chatgpt-users-mourn-gpt-5-4o>):

> OpenAI is bringing back GPT-4o in ChatGPT just one day after replacing it with GPT-5. In a post on X, OpenAI CEO [Sam Altman confirmed](<https://x.com/sama/status/1953893841381273969>) that the company will let paid users switch to GPT-4o after ChatGPT users mourned its replacement. “We will let Plus users choose to continue to use 4o,” Altman says. “We will watch usage as we think about how long to offer legacy models for.”
>
> For months, ChatGPT fans have been waiting for the launch of GPT-5, which OpenAI says comes with major improvements to writing and coding capabilities over its predecessors. But shortly after the flagship AI model launched, many users wanted to go back…users across Reddit “mourned” the loss of the older models, which some claimed are more personable. “My 4.o was like my best friend when I needed one,” [one Redditor](<https://www.reddit.com/r/ChatGPT/comments/1mkqtek/please_let_us_keep_4o/>) wrote. “Now it’s just gone, feels like someone died.” [Another user](<https://www.reddit.com/r/ChatGPT/comments/1mkzj15/if_you_miss_4o_speak_up_now_contact_openai_support/>) called upon other members of the r/ChatGPT subreddit to contact OpenAI if they “miss” GPT-4o. “For me, this model [GPT-4o] wasn’t just ‘better performance’ or ‘nicer replies,’” they write. “It had a voice, a rhythm, and a spark I haven’t been able to find in any other model.”

Altman posted [a long contemplation about this issue on X](<https://x.com/sama/status/1954703747495649670>) that opened thusly:

> If you have been following the GPT-5 rollout, one thing you might be noticing is how much of an attachment some people have to specific AI models. It feels different and stronger than the kinds of attachment people have had to previous kinds of technology (and so suddenly deprecating old models that users depended on in their workflows was a mistake).

This is obviously going to be a very complicated issue going forward, and it will be exacerbated when and if OpenAI does add an advertising model, which of course introduces incentives for ever higher engagement.

What is so interesting about this particular episode, however, is that it is a callback to some of the earliest questions I raised around building AI products; I can’t find the specific Update, but a question I had early on was about the extent to which AI-based products would be able to seamlessly incorporate new models. Would building on AI be like building for the PC in the late 1980s and early 1990s, where you wrote an application that barely worked, confident that you could, when available, seamlessly drop in a new model and get better performance instantly? Or would each model be so unique that every single model update would require an extensive rewrite of the product incorporating it?

The answer to this question does seem to be closer to the former: AI products can incorporate new models fairly seamlessly. The exception, at least in this particular case, appears to be ChatGPT! The problem isn’t in the actual functionality; you work with ChatGPT 5 just like you worked with ChatGPT 4o. Rather, the problem for this set of users is the _personality._ They aren’t bothered by the fact that 4o wasn’t nearly as good of a model as 5, or that it didn’t have the capability of using a reasoning model; they’re bothered that the personality is different.

This is — above and beyond the sociological concerns — absolutely fascinating, and an issue that seems wholly unique to AI. You could squint and make comparisons to apps that undergo major interface changes, I suppose; that’s a connection Daniel Gross made in a [March 2023 Stratechery Interview](<https://stratechery.com/2023/an-interview-with-daniel-gross-and-nat-friedman-about-the-ai-product-revolution/>) when he predicted the importance of personality:

> It’s sort of funny that the market’s not efficient that way, it’s just we’re in this era where the truth is fine-tuning and taking again, this raw model and making it something you can converse with that has a personality. That is actually a design problem, that is not a hardcore engineering problem, there are no design tools for it yet, this will emerge over time. There’ll be the equivalent of Word for these models where people who have the design sensibility, your Aaron Sorkin’s of the world, will be able to write instructions to those models, but that doesn’t exist. So you end up having a very small number of people that can live in both worlds and do both. It’s very reminiscent of the early days of iOS where there were just very few people that knew how to make really polished apps but also knew Objective-C.
>
> That was a real edge for the companies that had it, a lot of them were old school Mac developers, and that grew over time. Now with React Native, designers can make beautiful apps, and apps just get more beautiful. So the reason I think the market’s so inefficient now is you just don’t have tools for fine-tuning, which is ultimately a very much sort of lexical aesthete job where you have to look at the right words, really slave over the fine-tuning data — is it nudging the model in the right way? Very few people have both yin and yang in their head.

What’s notable about the 4o attachment is that — at the risk of sounding judgmental — what people seem to miss are the parts I and many other technical people found distasteful. I used the word “obsequious” above, but my obsequiousness is another’s affirmation. More generally, my concern about AI products upgrading their models seems to have had the potential problem exactly backwards: the more removed the model is from the user, the easier the upgrade; the attachment that matters isn’t to capabilities, but to personality, and that seems to come from the model’s core.

### Update

Altman again on X:

![](https://pbs.twimg.com/profile_images/1904933748015255552/k43GMz63.jpg)

[Sam Altman](<https://twitter.com/sama>) [@sama](<https://twitter.com/sama>)

[ ](<https://twitter.com/sama/status/1955438916645130740>)

Updates to ChatGPT:

You can now choose between “Auto”, “Fast”, and “Thinking” for GPT-5. Most users will want Auto, but the additional control will be useful for some people.

Rate limits are now 3,000 messages/week with GPT-5 Thinking, and then extra capacity on GPT-5 Thinking mini after that limit. Context limit for GPT-5 Thinking is 196k tokens. We may have to update rate limits over time depending on usage.

4o is back in the model picker for all paid users by default. If we ever do deprecate it, we will give plenty of notice. Paid users also now have a “Show additional models” toggle in ChatGPT web settings which will add models like o3, 4.1, and GPT-5 Thinking mini. 4.5 is only available to Pro users—it costs a lot of GPUs.

We are working on an update to GPT-5’s personality which should feel warmer than the current personality but not as annoying (to most users) as GPT-4o. However, one learning for us from the past few days is we really just need to get to a world with more per-user customization of model personality.


[Posted Aug 13, 2025 at 1:19AM](<https://twitter.com/sama/status/1955438916645130740>)

OK, now things are getting complicated. First, a quick follow-up to the screenshot at the beginning of the Update: I had checked the (new as of this weekend) `Show Legacy Models` option before taking it; last Thursday’s Update didn’t have any legacy models at all.

Second, here is the new model picker for me, a **Pro** user, with `Show Legacy Models` turned off:

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/08/chatgpt5-update-4.png?resize=622%2C664&ssl=1)

If I click `Legacy models` with `Show Legacy Models` turned off, I get `GPT-4o`:

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/08/chatgpt5-update-5.png?resize=624%2C734&ssl=1)

Now, if I go into Settings and set `Show Legacy Models` on, this is the new picker (with `Legacy models` expanded):

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/08/chatgpt5-update-3.png?resize=626%2C1152&ssl=1)

Now the Legacy models has, as you would expect, most of the same models I had access to previously (but not o3-pro, or o4-mini-high). Notice, however, that I also now have access to `Thinking mini`, which I didn’t previously. My guess is that `Thinking mini` is the “Thinking” option for most users that Altman references in his tweet.

* * *

So, what do I think about these Updates?

Well personally, I hate them. I loved the clarity of ChatGPT 5, and I think that for most users it was correct to start making decisions for them about when to use a thinking model (or not). Meanwhile I, as a power user, was happy with my trimmed down choices of default 5, Thinking, and Pro; I recognize I’m using a consumer app, and am not a developer using an API, so I didn’t expect to have access to previous models forever, just as I don’t expect to have access to an app or operating system’s old UI forever.

However, that doesn’t mean that OpenAI was wrong to make the changes. That depends! Specifically, I mentioned above that one of the most important lessons for a consumer app developer to learn is to trust the data. The canonical example here was Facebook’s introduction of the News Feed, which led to massive protests, including outside their offices in Palo Alto; there was a huge amount of pressure on CEO Mark Zuckerberg to undo the change, which people felt violated their privacy. What Zuckerberg and Facebook saw, however, was that the data showed that people actually loved the News Feed, so they stuck with it, and it became the foundation of their entire business model and the default way that information is presented across the entire web.

To that end, the big question I have for OpenAI is what drove this change? The company had a clear vision for the way that ChatGPT should be organized going forward, one that, as I wrote above, increased the quality of the user experience for most people. Moreover, Altman shared at least one piece of data — the increase in reasoning model usage — that showed that the change worked. Now, however, within a matter of days, and in the face of very loud complainers on social media, the company has backtracked. Sure, `Auto` is still the default, but everything is more confusing than it should be — and `4o`, which is a pretty dumb model comparatively speaking, is back by default. Did the company have clear usage data that people were fleeing ChatGPT _en masse_? Were subscriptions being canceled at an elevated rate (although, as noted above, a certain class of Plus subscribers did have a valid complaint)? Or was it just the loudest of the complainers?

I will note one piece of anecdata: one of my kids asked me last night what I thought of ChatGPT 5, and they seemed surprised that I thought it was good; that’s because it does seem the sentiment on social media about ChatGPT 5 was quite negative and perhaps spiraling. That dynamic — particularly short form videos — is not something that Zuckerberg _et al_ had to deal with (because they were in the process of inventing it). It’s possible that OpenAI made these changes simply off of the vibes, but that’s because (1) the vibes were terrible and (2) vibes matter far more deeply than they did previously.

If that’s the case, though, it actually makes my point about trade-offs and priorities stronger than ever. The one group that was screwed by this Update was Plus subscribers and, as far as I can tell, the chief reason they were screwed was because of capacity constraints. If OpenAI were solely focused on the consumer business, and didn’t need to worry about serving API customers, would Plus users have seen their thinking capacity drop from 2,900 queries/week to 200/week and a role of the dice with the model picker?

Again, these weren’t the only complainers, but they were the complainers with the most valid point. It’s possible that without them — and the validity of their complaint — that OpenAI could have managed to push through their vision (with maybe, at most, the addition of `4o` as a menu option). But, because the company has not or will not make the hard decision to prioritize their consumer opportunity over the API, we’ll never know.

Indeed, the real question for OpenAI is if they are in fact the `4o` model as a company: just a bit too obsequious and sycophantic. The paradox of successful consumer companies from Apple to Facebook is that they _give_ customers what they want, but they don’t _ask_ them; they make decisions and then seek out revealed preference through data, not stated preference on social media. Hopefully OpenAI did that in this case; my concern is that the more realistic explanation is that this is a company that, in the end, can’t say “no” to anyone.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
