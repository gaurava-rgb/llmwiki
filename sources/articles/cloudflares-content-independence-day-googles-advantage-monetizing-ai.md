---
title: "Cloudflare's Content Independence Day, Google's Advantage, Monetizing AI"
reader_id: "01k0a86vgxgte5bd6neb39j5nv"
notion_page_id: "3484ebe7-f118-8114-ba7f-d79c7d2adf2a"
reader_url: "https://read.readwise.io/read/01k0a86vgxgte5bd6neb39j5nv"
source_url: "https://stratechery.com/2025/cloudflares-content-independence-day-googles-advantage-monetizing-ai/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-07-16"
saved_at: "2025-07-16"
reading_time: "10 mins"
summary: "Cloudflare is unilaterally blocking AI crawlers unless they are willing to pay"
content_hash: "b107c2729ffa0eae7346bfee1c854de199c7b9ca24c27529de22c32f9905e14b"
---

Cloudflare is unilaterally blocking AI crawlers unless they are willing to pay

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

Here’s an unexpected area of coverage for the Stratechery Plus bundle: while [Greatest of All Talk](<https://goat.passport.online/>) is a podcast about basketball, primarily the NBA, the first part of [this week’s episode](<https://goat.passport.online/>) is about Ben Golliver’s time at Chesstival, a cross-over event in Las Vegas featuring Magnus Carlsen and Derrick Rose.

On to the Update:

### Cloudflare’s Content Independence Day

From the [New York Times](<https://www.nytimes.com/2025/07/01/technology/cloudflare-ai-data.html>):

> Cloudflare, a tech company that helps websites secure and manage their internet traffic, said on Tuesday that it had rolled out a new permission-based setting that allows customers to automatically block artificial intelligence companies from collecting their digital data, a move that has implications for publishers and the race to build A.I. With Cloudflare’s new setting, websites can block — by default — online bots that scrape their data, requiring the website owner to grant access for a bot to collect the content, the company said. In the past, those whom Cloudflare did not flag as a hacker or malicious actor could get through to a website to gather its information.
>
> “We’re changing the rules of the internet across all of Cloudflare,” said Matthew Prince, the chief executive of the company, which provides tools that protect websites from cyberattacks and helps them load content more efficiently. “If you’re a robot, now you have to go on the toll road in order to get the content of all of these publishers.” Cloudflare is making the change to protect original content on the internet, Mr. Prince said. If A.I. companies freely use data from various websites without permission or payment, people will be discouraged from creating new digital content, he said. The company, which says its network of servers handles about 20 percent of internet traffic, has seen a sharp increase in A.I. data crawlers on the web.

More from [Prince’s post on Cloudflare’s blog](<https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/>):

> The problem is whether you create content to sell ads, sell subscriptions, or just to know that people value what you’ve created, an AI-driven web doesn’t reward content creators the way that the old search-driven web did. And that means the deal that Google made to take content in exchange for sending you traffic just doesn’t make sense anymore. Instead of being a fair trade, the web is being stripmined by AI crawlers with content creators seeing almost no traffic and therefore almost no value.
>
> That changes today, July 1, what we’re calling Content Independence Day. Cloudflare, along with a majority of the world’s leading publishers and AI companies, is changing the default to block AI crawlers unless they pay creators for their content. That content is the fuel that powers AI engines, and so it’s only fair that content creators are compensated directly for it.

Cloudflare’s core product, which has undergirded their growth strategy from the beginning, is protecting sites from distributed denial-of-service attacks; this is not only immensely valuable to websites, but also to ISPs, which are happy to let Cloudflare co-locate their servers on the edge of the Internet. Moreover, as Cloudflare became more popular, they became economically critical to ISPs, who could serve websites from their own facilities without having to pay transit fees to fetch the protected websites elsewhere, further increasing Cloudflare’s position on the edge, which made their products — including an increasing array of paid services that have long since extended beyond reverse proxying and content delivery — even more valuable to websites. It’s a brilliant virtuous cycle that I wrote about in 2021’s [Cloudflare on the Edge](<https://stratechery.com/2021/cloudflare-on-the-edge/>).

What this means in terms of this news is that Cloudflare defaults are a big deal, and this is a pretty audacious display of power. Cloudflare launched an “easy button” to block AI crawlers [a year ago](<https://blog.cloudflare.com/declaring-your-aindependence-block-ai-bots-scrapers-and-crawlers-with-a-single-click/>), and says [more than 1 million customers have enabled this feature since then](<https://blog.cloudflare.com/declaring-your-aindependence-block-ai-bots-scrapers-and-crawlers-with-a-single-click/>). That, however, was an affirmative choice; now tens of millions of websites will block AI crawlers with immediate effect, unless they affirmatively agree to be crawled.

### Google’s Advantage

There is one important exception to these new defaults: Google, which has two crawlers. `Googlebot` crawls the web for Google search, while `Google-Extended` crawls the web to capture data for Gemini. What is critical to understand, however, is that data for Google Search AI products — including AI Overviews and AI Mode (i.e. [the search funnel](<https://stratechery.com/2025/google-i-o-the-search-funnel-product-possibilities/>)) — is gathered by `Googlebot`; that means that if you want your website to show up in Google Search you have no choice but to have that data also be used by any AI products that are under the Search umbrella. [I wrote about this reality in 2024](<https://stratechery.com/2024/perplexity-and-robots-txt-perplexitys-defense-google-and-competition/>) when some websites were upset about Perplexity:

> The key thing to understand for this Update is that no website can afford to exclude Google’s crawler from `robots.txt` because it would be economically ruinous. Google does have [an exclusion for Gemini](<https://searchengineland.com/google-extended-crawler-432636>), announced a couple of months after OpenAI, but [that exclusion does not extend to Search Generative Experiences](<https://searchengineland.com/google-extended-does-not-stop-google-search-generative-experience-from-using-your-sites-content-433058>), i.e. those AI-generated snippets in search that are Google’s most important defense against AI-chatbot incursion into their search dominance; if you want your content available to Google Search — and any publisher must — then your content will go into Google’s most important AI product as well.
>
> I think this casts Perplexity’s position — and OpenAI and Anthropic, which are also being [accused](<https://www.reuters.com/technology/artificial-intelligence/multiple-ai-companies-bypassing-web-standard-scrape-publisher-sites-licensing-2024-06-21/>) of [ignoring](<https://www.reuters.com/technology/artificial-intelligence/multiple-ai-companies-bypassing-web-standard-scrape-publisher-sites-licensing-2024-06-21/>) `robots.txt` — in a much more sympathetic light. Insisting that `robots.txt` is a law, the violation of which is unethical, is to insist that Google be granted an overwhelming advantage in terms of search for the rest of time, simply because they established economic power over publishers first.

Just to be clear, what Cloudflare is doing is not simply amending `robots.txt`; rather, they are straight-up denying access to AI crawlers — again, except for `Googlebot`, which a Google executive confirmed in court captured data for use in Search AI products; from [Bloomberg](<https://www.bloomberg.com/news/articles/2025-05-03/google-can-train-search-ai-with-web-content-even-after-opt-out>):

> Google can train its search-specific AI products, like AI Overviews, on content across the web even when the publishers have chosen to opt out of training Google’s AI products, a vice-president of product at the company testified in court on Friday. That’s because Google’s controls for publishers to opt out of AI training covers work by Google DeepMind, the company’s AI lab, said Eli Collins, a DeepMind vice president. Other organizations at the company can further train the models for their products. “Once you take the Gemini” AI model “and put it inside the search org, the search org has the ability to train on the data that publishers had opted out of training, correct?” asked Diana Aguilar, a Department of Justice lawyer. “Correct — for use in search,” Collins responded.

In short, Cloudflare is actively helping Google’s competitive position, insomuch as Google’s most important AI product is in fact Search; perhaps that is why [Prince’s post](<https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/>) opens with a paean to Search specifically:

> Almost 30 years ago, two graduate students at Stanford University — Larry Page and Sergey Brin — began working on a research project they called Backrub. That, of course, was the project that resulted in Google. But also something more: it created the business model for the web.
>
> The deal that Google made with content creators was simple: let us copy your content for search, and we’ll send you traffic. You, as a content creator, could then derive value from that traffic in one of three ways: running ads against it, selling subscriptions for it, or just getting the pleasure of knowing that someone was consuming your stuff.
>
> Google facilitated all of this. Search generated traffic. They acquired DoubleClick and built AdSense to help content creators serve ads. And acquired Urchin to launch Google Analytics to let you measure just who was viewing your content at any given moment in time.
>
> For nearly thirty years, that relationship was what defined the web and allowed it to flourish.
>
> But that relationship is changing. For the first time in more than a decade, the percentage of searches run on Google is [declining](<https://searchengineland.com/google-search-market-share-drops-2024-450497>). What’s taking its place? AI.

This reality makes me intrinsically uncomfortable with Cloudflare’s move, both in terms of the original “easy button” and especially now with the change in defaults: it’s not just the flexing of Cloudflare’s power, but also the fact that the primary beneficiary is the biggest and most important incumbent.

### Monetizing AI

And yet, at the same time, I’ve actually already made the argument as to why Cloudflare’s heavy-handed approach is a good thing. Specifically, from May’s [The Agentic Web and Original Sin](<https://stratechery.com/2025/the-agentic-web-and-original-sin/>):

> The original web was the human web, and advertising was and is one of the best possible ways to monetize the only scarce resource in digital: human attention. The incentives all align:
>
>   * Users get to access a vastly larger amount of content and services because they are free.
>   * Content makers get to reach the largest possible audience because access is free.
>   * Advertisers have the opportunity to find customers they would have been never able to reach otherwise.
>

>
> Yes, there are the downsides to advertising Zuckerman fretted about, but everything is a trade-off, and the particular set of trade-offs that led to the advertising-centric web were, on balance, a win-win-win that generated an astronomical amount of economic value…
>
> The center of this world for the last twenty years has been Google.
>
> ![A drawing of Google and the Ad Supported Web](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/05/agentic-web-original-sin-2.png?resize=1330%2C860&ssl=1)
>
> Google in its most idealized form Aggregated content consumers by mastering discovery in this world of abundance, directing users to exactly the site they were looking for, which was monetized through ads that were sold and served by Google.

This world, however, is rapidly being overwhelmed by AI:

> The problem, as both I and Patel noted, is that this ecosystem depends on humans seeing those webpages, not impersonal agents impervious to advertising, which destroys the economics of ad-supported content sites, which, in the long run, dries up the supply of new content for AI. OpenAI and Google in particular are clumsily addressing the supply issue by cutting deals with news providers and user-generated content sites like Reddit; this, however, is bad for the sort of competition Microsoft wants to engender, and ultimately won’t scale to the amount of new content that needs to be generated.

My proposed solution was a new marketplace for content:

> What is possible — not probable, but at least possible — is to in the long run build an entirely new marketplace for content that results in a new win-win-win equilibrium.
>
> ![A drawing of A New AI Content Marketplace](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/05/agentic-web-original-sin-1.png?resize=1330%2C266&ssl=1)
>
> First, the protocol layer should have a mechanism for payments via digital currency, i.e. stablecoins. Second, AI providers like ChatGPT should build an auction mechanism that pays out content sources based on the frequency with which they are cited in AI answers. The result would be a new universe of creators who will be incentivized to produce high quality content that is more likely to be useful to AI, competing in a marketplace a la the open web; indeed, this would be the new open web, but one that operates at even greater scale than the current web given the fact that human attention is a scarce resource, while the number of potential agents is infinite.

This is in fact the other part of Cloudflare’s actions; Prince wrote:

> Next, we’ll work on a marketplace where content creators and AI companies, large and small, can come together. Traffic was always a poor proxy for value. We think we can do better. Let me explain. Imagine an AI engine like a block of swiss cheese. New, original content that fills one of the holes in the AI engine’s block of cheese is more valuable than repetitive, low-value content that unfortunately dominates much of the web today. We believe that if we can begin to score and value content not on how much traffic it generates, but on how much it furthers knowledge — measured by how much it fills the current holes in AI engines “swiss cheese” — we not only will help AI engines get better faster, but also potentially facilitate a new golden age of high-value content creation. We don’t know all the answers yet, but we’re working with some of the leading economists and computer scientists to figure them out.

Specifically, Cloudflare is introducing [pay per crawl](<https://blog.cloudflare.com/introducing-pay-per-crawl/>):

> [Pay per crawl](<http://www.cloudflare.com/paypercrawl-signup/>), in private beta, is our first experiment in this area. Pay per crawl integrates with existing web infrastructure, leveraging HTTP status codes and established authentication mechanisms to create a framework for paid content access. Each time an AI crawler requests content, they either present payment intent via request headers for successful access (HTTP response code 200), or receive a 402 Payment Required response with pricing. Cloudflare acts as the Merchant of Record for pay per crawl and also provides the underlying technical infrastructure…
>
> At its core, pay per crawl begins a technical shift in how content is controlled online. By providing creators with a robust, programmatic mechanism for valuing and controlling their digital assets, we empower them to continue creating the rich, diverse content that makes the Internet invaluable…The true potential of pay per crawl may emerge in an agentic world. What if an agentic paywall could operate entirely programmatically? Imagine asking your favorite deep research program to help you synthesize the latest cancer research or a legal brief, or just help you find the best restaurant in Soho — and then giving that agent a budget to spend to acquire the best and most relevant content. By anchoring our first solution on HTTP response code 402, we enable a future where intelligent agents can programmatically negotiate access to digital resources.

This really casts my discomfort in stark relief: isn’t this exactly what I asked for? And, by extension, wouldn’t such a fundamental shift only be possible if it were imposed by an entity with the sort of power over the web that Cloudflare has?

Of course this will potentially be quite lucrative for Cloudflare:

> Crawler operators and content owners must configure pay per crawl payment details in their Cloudflare account. Billing events are recorded each time a crawler makes an authenticated request with payment intent and receives an HTTP 200-level response with a crawler-charged header. Cloudflare then aggregates all the events, charges the crawler, and distributes the earnings to the publisher.

Cloudflare has not, to my knowledge, announced any specifics as to what they will charge for this service, but even fractions of a cent per transaction could amount to a tremendous amount of money. Ultimately, however, I wouldn’t begrudge Cloudflare the windfall: Google supported the advertising-based web, while also taking the preponderance of advertising dollars [thanks to its Aggregator position](<https://stratechery.com/2015/popping-the-publishing-bubble/>); a potential Cloudflare commission fee would simply make this sort of value capture explicit.

What is more interesting to me is the more fundamental reality that undergirds this announcement: it’s one thing to have an idea for monetization in the age of AI; what Cloudflare’s announcement — and Google’s Advantage — makes clear is that actually enacting change requires power and the willingness to exercise it.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
