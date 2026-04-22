---
title: "Meta Earnings, Turning Dials, Zuckerberg's Motivation"
reader_id: "01kg5ac916jaqxyz37je672wv8"
notion_page_id: "3464ebe7-f118-8121-96d8-cf08b99bab43"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01kg5ac916jaqxyz37je672wv8"
source_url: "https://stratechery.com/?p=18182"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2026-01-29"
saved_at: "2026-01-29"
reading_time: "11 mins"
summary: "Meta is up, despite massive CapEx plans. The company is turning every dial to drive revenue, because Mark Zuckerberg thinks winning in AI is existential."
content_hash: "b44d67c30d16fc2d4de9ee7e9af89fbf7a7790440fe67ed40289b41597c98210"
---

Meta is up, despite massive CapEx plans. The company is turning every dial to drive revenue, because Mark Zuckerberg thinks winning in AI is existential.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

Jon at [Asianometry](<https://asianometry.passport.online/>) has a new video about the first commercially successful laptop PC: [The Toshiba T1100](<https://www.youtube.com/watch?v=qwGDfbyjegU>).

On to the Update:

### Meta Earnings

From [Bloomberg](<https://www.bloomberg.com/news/articles/2026-01-28/meta-says-2026-spending-will-blow-past-analysts-estimates>):

> Meta Platforms Inc.’s better-than-expected sales outlook helped ease Wall Street concerns about plans for unprecedented spending on artificial intelligence this year. The social networking giant topped projections for holiday quarter revenue and gave a strong forecast for the current period during its earnings report Wednesday. Improvements in its online advertising business are making it possible for Meta to spend hundreds of billions of dollars over the next few years on AI infrastructure. Meta’s shares jumped more than 11% in extended trading.
>
> Meta projected record spending for 2026, driven by Chief Executive Officer Mark Zuckerberg’s aggressive campaign to amass the infrastructure, computing power and talent that he deems necessary to win a competitive AI race. Zuckerberg has said his strategy centers on “front-loading” computing capacity in preparation for reaching the company’s goal of superintelligence, a theoretical milestone at which point AI can meet or outperform humans at many tasks. To get there, Meta is spending aggressively. The company estimated that full-year capital expenditures will be between $115 billion and $135 billion, exceeding the $110.6 billion average analyst estimate, according to data compiled by Bloomberg. If Meta hits the top-end of that range, it will mean a jump of roughly 87% from 2025, a record year in which cap-ex topped $72 billion.

The reaction to this earnings announcement was fascinating, particularly in comparison [to last quarter](<https://stratechery.com/2025/google-earnings-meta-earnings-the-cost-of-reality-labs/>). In that case Meta delivered excellent results, but warned it was going to ramp up infrastructure spending, and the market was not happy. This quarter the company again delivered excellent results, and an even more impressive outlook — potentially 30% revenue growth (26% on an equivalent currency basis) — but it also put a number to that infrastructure spending, and it was much higher than expected; overnight, however, the market was thrilled.

One thing that changed between last quarter and this quarter is that [Meta actually made cuts to Reality Labs](<https://stratechery.com/2026/meta-compute-the-meta-openai-battle-the-reality-labs-sacrifice/>); that not only will reduce losses — Zuckerberg said Reality Labs losses should peak this year — but also shows that Zuckerberg will in fact pull back spending eventually if an initiative isn’t generating the hoped-for return. That could always be done in AI.

Secondly, however, Meta continues to push the thesis they put forward last quarter, that spending on AI has a direct impact on top-line revenue. The most compelling articulation of this point came in CFO Susan Li’s prepared remarks on [the earnings call](<https://s21.q4cdn.com/399680738/files/doc_financials/2025/q4/META-Q4-2025-Earnings-Call-Transcript.pdf>):

> We’re seeing very strong results from the ad performance investments we made throughout 2025, with year-over-year conversion growth accelerating through the fourth quarter. We expect the set of investments we’re making in 2026 will enable us to drive further gains as we continue to integrate AI across all layers of the marketing and customer engagement funnel.
>
> The first area is our ads system, where we are continuing to scale the complexity and size of our models to better select which ads to show. In Q4, we doubled the number of GPUs we used to train our GEM model for ads ranking. We also adopted a new sequence learning model architecture, which is capable of using longer sequences of user behavior and processing much richer information about each piece of content. The GEM and sequence learning improvements together drove a 3.5% lift in ad clicks on Facebook and a more than 1% gain in conversions on Instagram in Q4.
>
> This new sequence learning architecture is significantly more efficient than our prior architectures, which should enable us to further scale up the data, complexity and compute we use in our future ranking models to deliver performance gains. As we scale up our foundational ads models like GEM, we are also developing more advanced models to use downstream of them at run-time for ads inference. In Q4, we launched a new runtime model across Instagram Feed, Stories, and Reels, resulting in a 3% increase in conversion rates in Q4.

Meta’s Generative Ads Model (GEM) is pretty interesting; the company’s engineering blog posted [an overview late last year](<https://engineering.fb.com/2025/11/10/ml-applications/metas-generative-ads-model-gem-the-central-brain-accelerating-ads-recommendation-ai-innovation/>). It’s not an LLM, although there are aspects of the model that use a transformer architecture; what’s compelling is that GEM scales with data and compute like LLMs do. Li said in response to a question:

> I’ll touch maybe specifically on GEM, in Q4, we extended GEM to cover Facebook Reels. Now it covers all major surfaces across Facebook and Instagram. We also doubled the size of the GPU cluster we used to train it. And in 2026, we’re expecting to meaningfully scale up GEM training to an even larger cluster, increasing the complexity of the model, expanding the data that we trained it on, leveraging new sequence learning architecture that we had begun deploying in Q4. And we’re also going to further improve how we transfer the learnings from our GEM foundation models to the runtime models that we’re using. So there’s a lot more headroom, I think, across many, many components of the stack. This is the first time we have found a recommendation model architecture that can scale with similar efficiency as LLMs. And we’re hoping that this will unlock the ability for us to significantly scale up the size of our ranking models while preserving an attractive ROI.

This right here, to the extent it is true, is by far the most compelling case for Meta’s investments, because Li is making the argument that more compute means better ad targeting, which directly translates into more revenue.

### Turning Dials

Last quarter I thought that the market’s reaction was wrong; this quarter, I think the market is right to make up for its previous excessive pessimism, but I also have to once again be a bit of a contrarian: I have questions about what exactly was driving these results, and if they were truly all down to Meta’s investments in AI.

Take a look at my usual Meta earnings chart:

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2026/01/meta-earnings-4q2025-1.png?resize=1330%2C684&ssl=1)

What made _last_ quarter so impressive to me is that both the impressions growth rate and price-per-ad growth rate increased. These almost always move in opposite directions, which makes intuitive sense: more impressions means more supply, which means if there is a steady-state in terms of demand prices should go down. If prices go up it’s because demand is increasing even more, which spoke to management’s argument that AI was really making ad targeting that much better.

That isn’t what happened this quarter: the impressions growth rate took another jump up, while the price-per-ad growth rate declined; this actually continued a trend that started in Q2 2025, which I picked up on at the time. From August’s [Facebook is Dead; Long Live Meta](<https://stratechery.com/2025/meta-earnings-meta-turns-the-dial-social-network-r-i-p/>):

> It turns out I was right last quarter that Meta had a lot of room to increase Reels monetization, but not just because they could target ads better (that was a part of it, as I noted above): rather, it turns out that short-form video is so addictive that Meta can simply drive more engagement — and thus more ad inventory — by pushing more of it. That’s impression driver number one — and the most important one. The second one is even more explicit: Meta simply started showing more ads to people (i.e. “ad load optimization”).
>
> All of this ties back to where I started, about how Meta learned that you have to give investors short term results to get permission for long term investments. I don’t think it’s a coincidence that, in the same quarter where Meta decided to very publicly up its investment in the speculative “Superintelligence”, users got pushed more Reels and Facebook users in particular got shown more ads. The positive spin on this is that Meta has dials to turn; by the same token, investors who have flipped from intrinsically doubting Meta to intrinsically trusting them should realize that it was the pre-2022 Meta, the one that [regularly voiced the importance of not pushing too many ads](<https://seekingalpha.com/article/4018524-facebook-fb-q3-2016-results-earnings-call-transcript?part=single>) in order to preserve the user experience, that actually deserved the benefit of the doubt for growth that was purely organic. This last quarter is, to my mind, a bit more pre-determined.

It seems to me that is exactly what happened this quarter: Reels viewing was up by an incredible 30% year-over-year, which means more inventory, and ad load continues to increase. I do appreciate that Vice President of Finance Chad Heaton was finally explicit about this last point on [the follow-up call](<https://s21.q4cdn.com/399680738/files/doc_financials/2025/q4/META-Q4-2025-Follow-Up-Call-Transcript.pdf>):

> And then to your question about impressions, so starting at the top, worldwide impressions grew 18% year-over-year in Q4. That was driven mainly by growth in users and engagement per user. Ad load increases were also a tailwind, although they contributed a minority of the year-over-year growth.
>
> On engagement, video was the largest driver of engagement gains in Q4, with particular strength on Instagram, where Reels time grew more than 30% yearover-year globally. I’d also note that Facebook saw healthy double-digit growth in video time in Q4 as well.
>
> On ad load, the tailwinds that we had in Q4 were driven by the higher levels of ad load on both feed and video surfaces on Facebook and Instagram. This was driven by some optimizations that we had made toward the end of Q3 and then continued into Q4. As Susan noted, we also had revenue gains from redistributing ad supply more optimally across users and sessions, though those show up in the reported pricing metrics rather than impressions since the optimizations don’t grow absolute ad load.
>
> The other thing I would note is we did see the three-point acceleration in worldwide impression growth. That was driven by ad load optimizations on Facebook and Instagram feed and video surfaces, in addition to the engagement strength on Instagram. The total year-over-year growth continues to be driven by growth in users and engagement, again, where ad load is a secondary contributor.

This isn’t necessarily bearish: as I noted six months ago, Meta has dials, and it appears it can turn them without losing customers. The reason to again highlight the actual drivers, however, is that I think that for now attributing increased revenue to AI gets the story backwards; Meta is increasing revenue so that it gets permission from investors to spend on AI.

### Zuckerberg’s Motivation

The most amusing part of the earnings call was Zuckerberg’s response to the very first analyst question:

> **Can you walk us through a little bit of how you think about the largest revenue or ROIC long-term opportunities you’re trying to unlock with those over the next, call it, 3, 5, 10 years through all the investment?**
>
> **Mark Zuckerberg:** Yes. I guess I can start with the first one. Although I have to say upfront that I think my answers to a lot of your questions on this particular call may be somewhat unfulfilling because we’re in this interesting period where we’ve been rebuilding our AI effort, and we’re six months into that, and I’m happy with how it’s going. But we are going to be rolling out our initial set of models and products and businesses around that over the coming months. And I will have a lot more to share on all of those fronts at that point. So I’m happy to offer kind of a high-level view of some of the stuff, but I apologize in advance that not much of this is going to be particularly detailed, but it will be exciting as we roll it out.

Zuckerberg’s answer went on a fair bit longer than that, but this was the honest part: his answers were in fact pretty unfulfilling, and he didn’t really answer the question. I don’t see any way you could read the full answer and come away thinking that Meta has any clearcut concrete plan for achieving a meaningful return on invested capital.

Instead, the real answer as to why the company is looking to spend up to $135 billion in CapEx this year — which is basically all of their projected free cash flow — came in Zuckerberg’s response to another question about whether Meta needed a general model:

> I think the question was around how important is it for us to have a general model. The way that I think about Meta is we’re a deep technology company. Some people think about us as we build these apps and experiences, but the thing that allows us to build all these things is that we build and control the underlying technology that allows us to integrate and design the experiences that we want and not just be constrained to what others in the ecosystem are building or allow us to build.
>
> So I think that this is a really fundamental thing where my guess is that frontier AI for many reasons, some competitive, some safety oriented, are not going to always be available through an API to everyone. So I think it’s very important, I think, to be able to have the capability to build the experiences that you want if you want to be one of the major companies in the world that helps to shape the future of these products.
>
> So that I think is — it’s going to be, I think, important from a business perspective. And I think it’s just important from like a creative and mission perspective to be able to actually design and build the experiences that we believe that we should be building for people. But yes, I mean I think it’s quite important. Otherwise, we wouldn’t be so focused on this. We’re clearly extremely focused on this.

This is the real motivation. Zuckerberg has come to believe that AI will be the critical technology for the future, which means that the question is not if Meta can have an acceptable return on invested capital, but actually whether or not Meta is a technology company that matters going forward. In other words, AI is existential.

That, by extension, strongly suggests that the link between Meta’s CapEx plans and its projected free cash flow is hardly an accident: Meta plans to invest literally every dollar it can into securing its future in an AI world. Moreover, this also explains the willingness to turn those ad load dials: if AI is going to replace everything, then what is there to preserve relative to the gain in cash flow and permission from investors that comes from generating more revenue in the short term?

To put it another way, investors may have decided that Zuckerberg can pursue his latest obsession as long as the core business keeps growing. I suspect Zuckerberg, however, has the inverse view: Meta must do what it takes to grow revenue such that the company can plow that much more money into AI.

And, I would add, it might not matter: Instagram ads are so good I hardly mind the (very noticeable) increased ad load; maybe Meta has been under-monetizing for years. Or, on the other hand, maybe the company will finally push it too far; one gets the impression Zuckerberg won’t mind as long as he gets enough money and permission to build on the frontier.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
