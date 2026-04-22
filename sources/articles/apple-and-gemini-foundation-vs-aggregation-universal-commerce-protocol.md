---
title: "Apple and Gemini, Foundation vs. Aggregation, Universal Commerce Protocol"
reader_id: "01kew7z6nkmjz7k4ebcr53b4c1"
notion_page_id: "3464ebe7-f118-8166-b9f0-d8fdd0cf8f85"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01kew7z6nkmjz7k4ebcr53b4c1"
source_url: "https://stratechery.com/2026/apple-and-gemini-foundation-vs-aggregation-universal-commerce-protocol/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2026-01-13"
saved_at: "2026-01-13"
reading_time: "9 mins"
summary: "The deal to put Gemini at the heart of Siri is official, and it makes sense for both sides; then Google runs its classic playbook with Universal Commerce Protocol."
content_hash: "bf60d49793289e9ad7605de91a9084f77578d62e4a98e6759ab2b3ce3c2c94e1"
---

The deal to put Gemini at the heart of Siri is official, and it makes sense for both sides; then Google runs its classic playbook with Universal Commerce Protocol.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

As part of my [one-man crusade to resuscitate the Apple Vision Pro](<https://stratechery.com/2026/apple-you-still-dont-understand-the-vision-pro/>) (“Live in Your Living Room”), I ranted about Apple’s unnecessary production on [Dithering](<https://dithering.passport.online/>), and then on [TBPN](<https://www.youtube.com/live/bnjUhCxt9tw?t=2070s>) explained why I think that making the Vision Pro about live events could, in the long run, make the device a much more compelling productivity tool as well.

On to the Update:

### Apple and Gemini

From [CNBC](<https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html>):

> Apple is joining forces with Google to power its artificial intelligence features, including a major Siri upgrade expected later this year. The multiyear partnership will lean on Google’s Gemini and cloud technology for future Apple foundational models, according to a joint statement obtained by CNBC’s Jim Cramer. “After careful evaluation, we determined that Google’s technology provides the most capable foundation for Apple Foundation Models and we’re excited about the innovative new experiences it will unlock for our users,” Apple said in a statement Monday. The models will continue to run on Apple devices and the company’s private cloud compute, the companies added. Apple declined to comment on the terms of the deal. Google referred CNBC to the joint statement.

Google added in a statement [on X](<https://x.com/NewsFromGoogle/status/2010746083170046376>):

> Apple and Google have entered into a multi-year collaboration under which the next generation of Apple Foundation Models will be based on Google’s Gemini models and cloud technology. These models will help power future Apple Intelligence features, including a more personalized Siri coming this year.
>
> After careful evaluation, Apple determined that Google’s Al technology provides the most capable foundation for Apple Foundation Models and is excited about the innovative new experiences it will unlock for Apple users. Apple Intelligence will continue to run on Apple devices and Private Cloud Compute, while maintaining Apple’s industry-leading privacy standards.

I analyzed this partnership in depth when Mark Gurman reported it was coming [in November](<https://stratechery.com/2025/apple-earnings-siri-white-labels-gemini-short-term-gains-and-long-term-risk/>):

> Start with the implications of Apple white-labeling a model for Siri in the first place. First off, I think this is the right move; there is no evidence, either from history or from the company’s capital expenditure numbers, that Apple has the capability to compete on the leading edge of AI model development. At the same time, Apple doesn’t need to be highly differentiated in this regard, at least not now: we just saw that the company’s products are as popular as ever; what the company needs is to have something that is “good enough”. In other words, what is “best” actually doesn’t have much to do with “better”; “good enough” is sufficient.

The context of that paragraph was Gurman’s reporting that Apple chose Gemini over Anthropic’s Claude, which, at that time, was regarded as a better model; I made the case that Apple didn’t necessarily need the best model, and it was reasonable to consider things like price, infrastructure, familiarity, etc., because Apple simply needed to be in the game. Therefore, Gemini made sense.

However, I probably should have realized that Apple was almost certainly getting access to upcoming models at that point, which means they were evaluating Gemini 3, which is obviously very strong and arguably state of the art. Regardless, the points about price, infrastructure, and familiarity all hold — if that comes with the best model, all the better!

### Foundation vs. Aggregation

It’s also worth specifying what exactly Apple is getting: this is not a replacement for the OpenAI partnership, wherein Siri bounces some queries to ChatGPT; rather, this deal is about the foundational model undergirding Siri itself. The game that Apple is bowing out of is pre-training, where you ingest astronomical amounts of data to create a foundation model; that foundation model is a token-generation engine.

Simply spitting out tokens, however, is not a product: the product aspect of models comes from post-training, where you make that token generation coherent, you provide guardrails, you add specific skills, and where you give the model a personality. In other words, this is the step where you make the model Siri. To that end, I’m not surprised that this announcement was so low key: I don’t expect the name “Gemini” to appear anywhere in the Siri product, at least outside of a product credits page where they list things like open source licenses. Siri will still very much be an Apple creation, it will just rest on a Gemini foundation.

There is, as I noted last November, long-term risk here; Apple didn’t say anything about continuing to develop their own foundational models, but I think this seals their fate:

> Still, Apple’s plans are a bit like the alcoholic who admits that they have a drinking problem, but promises to limit their intake to social occasions. Namely, how exactly does Apple plan on replacing Gemini with its own models when (1) Google has more talent, (2) Google spends far more on infrastructure, and (3) Gemini will be continually increasing from the current level, where it is far ahead of Apple’s efforts? Moreover, there is now a new factor working against Apple: if this white-labeling effort works, then the bar for “good enough” will be much higher than it is currently. Will Apple, after all of the trouble they are going through to fix Siri, actually be willing to tear out a model that works so that they can once again roll their own solution, particularly when that solution hasn’t faced the market pressure of actually working, while Gemini has?
>
> In short, I think Apple has made a good decision here for short term reasons, but I don’t think it’s a short-term decision: I strongly suspect that Apple, whether it has admitted it to itself or not, has just committed itself to depending on 3rd-parties for AI for the long run. And, I might add, this could work out very well. Just look at the Services revenue example above: Apple’s position as the most desirable hardware platform means it is benefiting massively from AI revenue growth; similarly, Apple’s ownership of the user experience on the most important platform means it can treat model builders as suppliers — and cleverly, by not advertising who makes the model, it retains the option to switch suppliers in the future if necessary.
>
> The real risk happens much further down the road, if AI actually disrupts the smartphone paradigm, or becomes the UI of the future. Apple surely is telling itself that it will keep building models just in case such a future comes to pass, but again, I struggle to see how the company will keep up. Google is going to be so much better at this, and is charging so little, probably to ensure that Apple never truly tries. [It’s the exact same strategy as search](<https://stratechery.com/2024/friendly-google-and-enemy-remedies/>)…
>
> Apple is in a desperate enough position that they aren’t getting paid to use Gemini; they are an attractive enough customer, however, that Google is putting in real work to make Gemini run on Apple’s infrastructure for a mere $1 billion a year. Maybe Apple can simply ask that the money be taken out of the search deal! And, by the way, the lack of branding works for Google too: if Siri still stinks Gemini’s brand isn’t hurt.

In fact, there is a way that Apple might have its cake and eat it too. Remember, this deal does not replace OpenAI; that, though, means there is potentially another deal to be made. From [Alex Heath at Sources](<https://sources.news/p/google-wants-gemini-in-ios-like-chatgpt>):

> Sources say that Sundar Pichai and Google’s other leaders hope this initial deal on underlying model technology will lead to the same kind of product integration that ChatGPT currently enjoys on iOS and macOS. Even though it recently won its search antitrust case, Google would not dare try to fully replace ChatGPT as the only third-party assistant on Apple devices, of course. Such a move is still too risky, given how closely governments around the world are still scrutinizing Google and any big AI deal. But Google would love to make Gemini available as an alternative to ChatGPT on Apple’s billions of devices.

Back when Apple first announced Apple Intelligence [I was optimistic that Apple could Aggregate AI](<https://stratechery.com/2024/wwdc-apple-intelligence-apple-aggregates-ai/>):

> To put it another way, and in Stratechery terms, Apple is positioning itself as an AI Aggregator: the company owns users and, by extension, generative AI demand by virtue of owning its platforms, and it is deepening its moat through Apple Intelligence, which only Apple can do; that demand is then being brought to bear on suppliers who probably have to eat the costs of getting privileged access to Apple’s userbase.

The big problem with this vision is that it assumed that Apple Intelligence would be competent, and it simply wasn’t; just as the iPhone search deal wouldn’t be worth much if the iPhone sucked, Siri chatbot integration isn’t worth much if Siri sucks. Now, however, Google is selling the underlying model to make Siri good, and their biggest hope is that they can pay Apple all of their money back — and more! — to have a money-making Gemini sit on top.

### Universal Commerce Protocol

From [TechCrunch](<https://techcrunch.com/2026/01/11/google-announces-a-new-protocol-to-facilitate-commerce-using-ai-agents/>):

> Google on Sunday announced a new open standard called the Universal Commerce Protocol (UCP) for AI agent-based shopping, at the National Retail Federation (NRF) conference. The standard, developed with companies like Shopify, Etsy, Wayfair, Target, and Walmart, lets agents work across different parts of customer buying processes, including discovery and post-purchase support.
>
> The core idea is that the standard could facilitate these various parts of the process instead of requiring connections with different agents. Google said that it also works with other agentic protocols, such as Agent Payments Protocol (AP2) — which Google announced last year — Agent2Agent (A2A), and Model Context Protocol (MCP). The company specified that Agents and Businesses can pick and choose specific extensions of the protocol that suits their needs.
>
> The company said that it will soon use UCP for eligible Google product listings in AI mode in search and the Gemini apps to let shoppers check out directly from U.S.-based retailers while researching a product. Users will be able to pay using Google Pay and pass on the shipping information saved in the Google Wallet. Google said that it will soon support PayPal as a payment option.

This announcement is a bit in the weeds, particularly as it follows on to OpenAI’s announcement of the [Agentic Commerce Protocol](<https://developers.openai.com/commerce/>) last [September](<https://stratechery.com/2025/openai-instant-checkout-ai-and-long-tail-e-commerce-is-ai-different/>). Broadly speaking, both protocols enable instant checkout type of experiences within AI workflows; there are, however, subtle differences that speak to how OpenAI and Google view their relative positions.

In short, to dramatically simplify, the OpenAI and Stripe pioneered Agentic Commerce Protocol is about enabling purchases from within ChatGPT (yes, it’s an open standard, but it was clearly built for ChatGPT). Merchants provide a formatted list of their goods to ChatGPT, and then Stripe facilitates a purchase that keeps the 3rd-party as the merchant of record. More generally, Agentic Commerce Protocol is focused on a world where the commerce journey exists entirely within ChatGPT.

The Universal Commerce Protocol, on the other hand, is much more ambitious (and complicated). You can define every aspect of the e-commerce funnel, from discovery to catalog to checkout to order history to returns to loyalty etc.; those aspects can then be consumed by anything, whether that be a chatbot, an agent, etc. This is much more work, but, if done well, both preserves more control for the merchant and also makes the entirety of their experience much more broadly available than just in a chatbot.

This is very much classic Google. Google, particularly early Google, doesn’t want walled gardens; rather, it wants to tear down all walls and make everything generally accessible. Yes, in theory that creates the conditions for competition, but in reality Google can bring to bear its massive user base to most efficiently and effectively harvest and wield broadly available digital abundance — think Google Search leveraging the open web versus, say, Yahoo and its portal, or AOL and its walled garden.

In other words, the point of the Universal Commerce Protocol is right there in the name: Google wants all information and potential activities everywhere to be universally accessible, because when no one has a structural advantage or a wall around their garden then Google actually has the biggest advantage of everyone. That, by extension, will create the conditions for Gemini to actually make money — and outbid OpenAI for the actual branded spot atop Siri.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
