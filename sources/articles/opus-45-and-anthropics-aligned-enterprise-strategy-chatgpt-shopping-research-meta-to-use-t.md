---
title: "Opus 4.5 and Anthropic's Aligned Enterprise Strategy, ChatGPT Shopping Research, Meta to Use TPUs?"
reader_id: "01kaxqd7af35q8t7k0xj644mha"
notion_page_id: "3464ebe7-f118-81fe-be58-c268bd354cbd"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01kaxqd7af35q8t7k0xj644mha"
source_url: "https://stratechery.com/2025/opus-4-5-and-anthropics-aligned-enterprise-strategy-chatgpt-shopping-research-meta-to-use-tpus/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-11-25"
saved_at: "2025-11-25"
reading_time: "9 mins"
summary: "Anthropic's Opus 4.5 appears to be a big breakthrough that slots into Anthropic's enterprise strategy, while ChatGPT gets new consumer features, and Meta might use Google's TPUs"
content_hash: "1b9b9f82730d1bed1a913e9db3598e358520b9a39e2e702263005e3d0ebba951"
---

Anthropic's Opus 4.5 appears to be a big breakthrough that slots into Anthropic's enterprise strategy, while ChatGPT gets new consumer features, and Meta might use Google's TPUs

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

After today Stratechery will be on break for the Thanksgiving holiday; today is also this week’s [only episode of Dithering](<https://dithering.passport.online/>), and tomorrow will have a special holiday episode of [Sharp Tech](<https://sharptech.fm/member>). I’ll be back on Monday, and there is certainly a lot of news to digest before then!

On to the Update:

### Opus 4.5 and Anthropic’s Aligned Enterprise Strategy

From [Bloomberg](<https://www.bloomberg.com/news/articles/2025-11-24/anthropic-says-its-new-ai-model-is-better-at-coding-and-office-work>):

> Anthropic PBC is rolling out a new version of its most powerful artificial intelligence model that is designed to be better at automating coding and office tasks, part of an effort to compete with OpenAI and Alphabet Inc.’s Google for business customers. The new model, Claude Opus 4.5, is more capable than previous versions at software engineering work, like fixing bugs, without needing a user’s help, Anthropic said. Opus 4.5, released Monday, is also intended to be better at carrying out complicated multistep tasks on a user’s computer and the internet.
>
> Founded in 2021 by former employees of OpenAI, San Francisco-based Anthropic now has more than 300,000 business customers who use its models to streamline workplace tasks — particularly in the field of computer programming, where the startup has emerged as a market leader. But Anthropic faces intense competition from OpenAI and Google, the latter of which impressed the AI community and investors last week with the release of Gemini 3. Google’s new model is designed to be better at coding, among other jobs.
>
> Anthropic’s new model has hit a new coding milestone of sorts, according to Scott White, head of product for Claude AI models. Opus 4.5 is the first to score higher than any of the company’s human candidates on a challenging take-home engineering assignment that prospective employees are asked to complete, he said. White declined to explain the specific assignment but said it’s meant to take a qualified candidate many hours while using Anthropic’s Claude model.

I had a feeling this was coming, but it’s important to keep in mind the state of play before this announcement: Claude Sonnet 4.5 — a smaller model — was already better than Gemini 3 at coding benchmarks, and, according to engineers I talked to, significantly better in practice; that gap in performance is, [as I noted last week](<https://stratechery.com/2025/gemini-3-winners-and-losers-integration-and-the-enterprise/>), one that has persisted for a couple of years now. And now there is Opus 4.5, which appears to be a considerable leap in coding in particular. The benchmarks certainly agree; from [Anthropic’s announcement post](<https://www.anthropic.com/news/claude-opus-4-5>):

[![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/11/anthropic-1.png?resize=1330%2C748&ssl=1)](<https://www.anthropic.com/news/claude-opus-4-5>)

What is interesting is what Opus 4.5 is not. While Opus — like all Claude models — can ingest images and understand them, it does not generate them (other than code-defined formats like SVG). To put it another way, Claude is multi-modal in, but not out; it can, however, use tools — or even program them — while saving a lot of tokens along the way.

This point speaks to a larger one. One angle is that Anthropic, more than any other lab, remains laser-focused on AGI, and believes that building a model tuned for coding in particular is the shortest path to getting there; after all, once the model can develop itself, we have take-off. What is convenient — and impressive to me — is how much sense this makes as a business strategy.

The fact of the matter is that Anthropic missed the consumer market; Claude came out in March 2023, and was really good from the get-go, but ChatGPT had already won. Winning, though, is its own curse: OpenAI went through two years of wrenching change to make itself into a consumer tech company, and the journey is far from over, [as I lamented yesterday](<https://stratechery.com/2025/nvidia-earnings-power-scarcity-and-marginal-costs-openai-hand-wringing/>) (you’re not a consumer tech company if you don’t have ads!). That change — and the drama that resulted — is a massive distraction, both in terms of employee attention and also resources. It also made it both necessary and incredibly difficult for OpenAI to divorce itself from Microsoft, a process that won’t be completed until 2030 (in terms of exclusive access to OpenAI IP).

Anthropic, meanwhile, came out with Claude 3.5 Sonnet in the summer of 2024, which was — even more clearly in retrospect — a massive breakthrough in terms of coding. That laid the foundation for Anthropic’s enterprise push and the explosion in revenue that followed. That offering, meanwhile, was married to a very smart distribution strategy: Claude was available directly from Anthropic, but also on Amazon and Google’s cloud services; now, [as of last week](<https://stratechery.com/2025/gemini-3-winners-and-losers-integration-and-the-enterprise/>), it is also available on Azure. That is exactly the right way to reach enterprise customers — on their terms, and their cloud of choice — and Anthropic is following that up by proving it still leads the pack on the precise vector enterprises care about.

It’s also notable (and unsurprising) that coding appears to be highly correlated to agentic capabilities, at least in terms of benchmark scores. Agents are, of course, where AI expands beyond development teams to every part of the organization; Anthropic is, once again, the best placed of the labs to capture that opportunity, and is laser-focused on it.

One other note: Opus has always been better than Sonnet, but it’s been cost-prohibitive to use. What makes this release a particularly big deal, then, is that it is considerably cheaper; from [Simon Willison](<https://simonwillison.net/2025/Nov/24/claude-opus/>):

> The pricing is a big relief: $5/million for input and $25/million for output. This is a lot cheaper than the previous Opus at $15/$75 and keeps it a little more competitive with the GPT-5.1 family ($1.25/$10) and Gemini 3 Pro ($2/$12, or $4/$18 for >200,000 tokens). For comparison, Sonnet 4.5 is $3/$15 and Haiku 4.5 is $1/$5.

A 66% decrease in token pricing is a big deal; I look forward to learning more about how this was achieved. Per token pricing, however, is only a proxy: what actually matters is how much you spend to actually get something done. To that end, the even bigger breakthrough with Opus 4.5 is that it appears to use tokens far more efficiently; from Claude’s Jeremy Hadfield [on X](<https://x.com/jerhadf/status/1993069510660854201>):

![](https://pbs.twimg.com/profile_images/1753838696225267712/PWxOikdC.jpg)

[jeremy](<https://twitter.com/jerhadf>) [@jerhadf](<https://twitter.com/jerhadf>)

[ ](<https://twitter.com/jerhadf/status/1993069510660854201>)

one fact people won't realize immediately about opus 4.5: it's remarkably token-efficient. all-in it's often **_cheaper_ than sonnet 4.5 and other models for cost-per-task-success**. glad sourcegraph is seeing this early in Amp!

we find that opus 4.5 with medium effort is pareto dominant over sonnet 4.5 on swe-bench verified - outperforming it at 77.4% w/ 4x fewer tokens and 35% of the cost. it's smart about using only the optimal time & tokens it needs to solve the problem. sonnet is still great and this may not hold for other use cases, but many agentic coding use cases are seeing remarkable efficiency. curious what you all find!

check out this interactive chart opus 4.5 made about it: <https://t.co/jSJtvrRQmL>

sticker prices aren't everything!


![](https://pbs.twimg.com/media/G6jNTdEXkAAoDQ4.jpg)

![](https://pbs.twimg.com/profile_images/1519180377604034560/NxI03WYE.jpg)

[Quinn Slack](<https://twitter.com/sqs>) [@sqs](<https://twitter.com/sqs>)

[ ](<https://twitter.com/sqs/status/1993057357958681017>)

Opus is worth it, and maybe cheaper all-in than Sonnet?

Early rough non-representative numbers, for our own internal [@AmpCode](<https://twitter.com/AmpCode>) usage (avg cost $ per thread):

\- Sonnet 4.5: $1.83
\- Opus 4.5: $1.30 (earlier checkpoint last week was $1.55)
\- Gemini 3 Pro: $1.21

[twitter.com/i...](<https://twitter.com/i/web/status/1993039601301393786>)

[Posted Nov 24, 2025 at 8:41PM](<https://twitter.com/sqs/status/1993057357958681017>) [Posted Nov 24, 2025 at 9:29PM](<https://twitter.com/jerhadf/status/1993069510660854201>)

This creates the conditions for a third leg of the Anthropic enterprise stool: distribution is one, capability is the second, and the 3rd is a predictable business model where jobs can be priced on the cost of achieving them, instead of usage; the latter is better than a per-seat model (which is completely archaic in an agent world), but is still a proxy for what a company actually wants, which is to complete a given task for a predictable price.

### ChatGPT Shopping Research

From [Bloomberg](<https://www.bloomberg.com/news/articles/2025-11-24/openai-debuts-chatgpt-shopping-research-tool-ahead-of-the-holidays>):

> OpenAI unveiled a free artificial intelligence-powered shopping research tool that it says can generate a personalized buyer’s guide for ChatGPT users during the holiday season. While ChatGPT has always been able to respond to shopping-related questions, OpenAI has trained a version of its GPT-5 mini model that asks clarifying questions and draws its answers from reviews published on what the company considers higher-quality websites, it said in a blog post Monday. For example, user experiences shared on Reddit may be considered more trustworthy than paid marketing or reviews posted on a product page, OpenAI representatives told reporters ahead of the announcement. The tool does not prioritize specific websites when citing links to products, they added.
>
> The new tool is different from the regular text interaction that ChatGPT users have grown accustomed to. People can use a dedicated “shopping research” button in the chat interface and describe what they’re looking for using instructions like “find a small couch for a studio apartment” or “I need a gift for my 4-year-old niece who loves art.” Instead of immediately generating a text response, the research tool will ask for more information in a quiz format, taking into consideration possible factors such as budget, color preferences and the desired size of the item. As it gathers information from the web, it will suggest 10 to 15 items along the way, and users will be prompted to click “more like this” or “not interested” to refine the final list.

It’s hard to imagine a more perfect example to accentuate the point I made above: this is a great idea, that I expect to be well executed, that is perfectly suited for a clear consumer use case. Moreover, note that this is more than just fancy UI: OpenAI post-trained a special version of GPT-5 mini to specialize in shopping. It’s also a great way to gather more information about users to fuel a future ad product. And, to complete my point, it’s basically impossible to imagine Anthropic ever doing anything like this (and neither company is wrong!).

### Meta to Use TPUs?

From [The Information](<https://www.theinformation.com/articles/google-encroaches-nvidias-turf-new-ai-chip-push>):

> Google is picking up the pace of its efforts to compete directly with Nvidia in the AI chip business. For years, the search giant has rented its own AI chips, known as tensor processing units, to cloud customers who use them in its Google Cloud data centers. Now, though, Google has begun pitching some of those customers — including Meta Platforms and big financial institutions — on the idea of using TPUs in their own data centers, according to people involved in the talks.
>
> Meta, the parent company of Facebook and Instagram, is currently in talks with Google about spending billions of dollars to use TPUs in Meta’s data centers in 2027, as well as to rent Google chips from Google Cloud next year, according to a person involved in the talks. Meta currently relies on Nvidia’s graphics processing units.

This is one of those shocking but not surprising tidbits: a deal between Google and Meta specifically makes a lot of sense.

Start with the pricing discussion in [yesterday’s Update](<https://stratechery.com/2025/nvidia-earnings-power-scarcity-and-marginal-costs-openai-hand-wringing/>): while Nvidia GPUs may be cheaper on a marginal basis, the upfront cost still matters, particularly when you are buying at Meta’s scale. That scale, however, means that it is worth what would certainly be a considerable engineering investment to tune specific applications to a new chip architecture, significantly closing whatever performance delta may exist, allowing the lower upfront cost to tilt the overall cost of ownership lower. Moreover, this tilting is easier to achieve if you can skip over the very expensive cost of actually developing the chip itself (even if that means paying Google a margin).

If you’re Google, meanwhile, any incremental sales of TPUs spreads out the cost of developing the TPUs over that many more chips, which actually reduces the cost of your own infrastructure build-out, in addition to the incremental revenue. You also gain a very capable customer who can contribute to the development of libraries that run on your TPUs, further reducing your costs. Moreover, that customer isn’t actually a competitor: Meta doesn’t have a cloud business.

What I am more skeptical about is a TPU deal with basically anyone else. Few other companies have the resources and scale to make the level of investment necessary to achieve the upside of such a deal, and the ones that do are Google competitors. I suspect that Nvidia will still remain the best choice for basically everyone else — and Nvidia is leveraging its burgeoning war chest to make sure they agree. From the The Information report:

> Whether Google succeeds in its TPU efforts, the mere specter of a powerful alternative to Nvidia may have already yielded benefits for big Nvidia customers like Anthropic and OpenAI that don’t want to rely on a single AI chip provider.
>
> Last month, following a Google deal to provide up to 1 million TPUs to Anthropic, Huang announced another deal to invest billions of dollars into Anthropic. He also got a commitment from the AI startup to use Nvidia GPUs.
>
> Similarly, after it became publicly known OpenAI was planning to rent TPUs from Google Cloud, Huang struck a tentative deal to invest up to $100 billion in the ChatGPT maker so it could develop its own data centers, and has discussed leasing out Nvidia GPUs to the company.

This certainly provides useful context as to why OpenAI could be so brash as to make a deal with AMD just weeks after the Nvidia investment (which isn’t finalized); competition is good, and it’s fascinating that it’s Google of all companies who might be helping cut the bills — or up the investment — for some of its own biggest competitors.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
