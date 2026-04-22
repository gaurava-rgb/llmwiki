---
title: "Nvidia and Groq, A Stinkily Brilliant Deal, Why This Deal Makes Sense"
reader_id: "01kea752j17d51rn2628q6kxd8"
notion_page_id: "3464ebe7-f118-81d0-bccb-c1ded718b563"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01kea752j17d51rn2628q6kxd8"
source_url: "https://stratechery.com/2026/nvidia-and-groq-a-stinkily-brilliant-deal-why-this-deal-makes-sense/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2026-01-06"
saved_at: "2026-01-06"
reading_time: "8 mins"
summary: "Nvidia is licensing Groq's technology and hiring most of its employees; it's the most potent application of tech's don't-call-it-an-acquisition deal model yet."
content_hash: "df7df157135209a973a2306e7e239feb8537bf8f8c9c437c7e063f6666b9b8fb"
---

Nvidia is licensing Groq's technology and hiring most of its employees; it's the most potent application of tech's don't-call-it-an-acquisition deal model yet.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

Happy New Year! It’s good to be back. There was one big piece of news over the break that I definitely wanted to get to first thing.

On to the Update:

### Nvidia and Groq

From [Bloomberg](<https://www.bloomberg.com/news/articles/2025-12-24/nvidia-reaches-licensing-deal-with-chip-startup-groq>) on Christmas Eve:

> Nvidia Corp. agreed to a licensing deal with artificial intelligence startup Groq, furthering its investments in companies connected to the AI boom and gaining the right to add a new type of technology to its products. The world’s largest publicly traded company has paid for the right to use Groq’s technology and will integrate its chip design into future products. Some of the startup’s executives are leaving to join Nvidia to help with that effort, the companies said. Groq will continue as an independent company with a new chief executive, it said Wednesday in a post on its website.
>
> Nvidia’s technology already dominates data centers that are at the heart of the explosion in spending on new computing needed for AI software and services. The popularity of its existing offerings has made Nvidia by far the richest company in the chip industry and it has said it will use some of that cash to advance the uptake of AI across the economy. Groq is among the startups and companies such as Alphabet Inc.’s Google that are developing their own AI chips to rival Nvidia. The startup, which was founded in 2016, raised $750 million at a post-funding valuation of $6.9 billion in September. At the time, Groq said it would use the funds to expand its data center capacity. Its data center business, which offers outsourced computing, will continue, the company said in the post.

[I wrote about Groq in February 2024](<https://stratechery.com/2024/sora-groq-and-virtual-reality/>), and explained what made their chip different:

> Groq was founded in 2016 by Jonathan Ross, who created Google’s first Tensor Processing Unit; Ross’s thesis was that chips should take their cue from software-defined networking: instead of specialized hardware for routing data, a software-defined network uses commodity hardware with a software layer to handle the complexity of routing. Indeed, [Groq’s paper](<https://wow.groq.com/wp-content/uploads/2023/05/GroqISCAPaper2022_ASoftwareDefinedTensorStreamingMultiprocessorForLargeScaleMachineLearning-1.pdf>) explaining their technology is entitled “A Software-defined Tensor Streaming Multiprocessor for Large-scale Machine Learning.”
>
> To that end Groq started with the compiler, the software that translates code into machine language that can be understood by chips; the goal was to be able to reduce machine-learning algorithms into a format that could be executed on dramatically simpler processors that could operate at very high speed, without expensive memory calls and prediction misses that make modern processors relatively slow.
>
> The end result is that Groq’s chips are purely deterministic: instead of the high-bandwidth memory (HBM) used for modern GPUs or Dynamic Random Access Memory (DRAM) used in computers, both of which need to be refreshed regularly to function (which introduces latency and uncertainty about the location of data at a specific moment in time), Groq uses SRAM — Static Random Access Memory. SRAM stores data in what is called a bistable latching circuitry; this, unlike the transistor/capacitor architecture undergirding DRAM (and by extension, HBM), stores data in a stable state, which means that Groq always knows exactly where every piece of data is at any particular moment in time. This allows the Groq compiler to, in an ideal situation, pre-define every memory call, enabling extremely rapid computation with a relatively simple architecture.
>
> It turns out that running inference on transformer-based models is an extremely ideal situation, because the computing itself is extremely deterministic. An LLM like GPT-4 processes text through a series of layers which have a predetermined set of operations, which is perfectly suited to Groq’s compiler. Meanwhile, token-based generation is a purely serial operation: every single token generated depends on knowing the previous token; there is zero parallelism for any one specific answer, which means the speed of token calculation is at an absolute premium.

Groq was and remains extremely fast thanks to its architecture, but everything is a trade-off: Groq chips were built on Global Foundries 14nm process and only had 230MB of SRAM, which means that serving even a relatively basic model [required linking together hundreds of chips](<https://stratechery.com/2024/groq-costs-gemini-pro-1-5-googles-timidity/>). At the same time, that also meant there was a lot of room for Groq chips to be even better: SRAM is directly on the chip, which meant that moving to a smaller process size would allow for a lot more memory and, of course even faster speeds. Groq 2 — which unlike Groq 1, was designed for LLMs — was scheduled to be built on Samsung’s 4nm process, but hasn’t yet shipped.

### A Stinkily Brilliant Deal

First off, it’s important to note that this isn’t an acquisition: it’s another one of those [“stinky deals” I wrote about last summer](<https://stratechery.com/2025/google-and-windsurf-stinky-deals-chestertons-fence-and-the-silicon-valley-ecosystem/>). In that Article I placed the blame for these hire-and-license arrangements squarely at the feet of regulators:

> The effort to indiscriminately throw sand in the gears of the Silicon Valley machine — which, it should be noted, started under the first Trump administration, but was dramatically accelerated under the Biden administration — is undoubtedly the biggest driver of these stinky deals. Big Tech, starting with Microsoft, realized that the easiest way to avoid regulatory annoyance around acquihires was to separate the acquisition from the hiring; what has happened as these deals have evolved is that tech companies increasingly realize that if they are simply hiring and not acquiring then they don’t have to hire everyone. That, however, breaks the implicit social contract that made startup employment significantly less risky for rank-and-file employees.
>
> What is frustrating about this development is that there is a good chance we will never go back. The fact of the matter is that picking-and-choosing who to hire from a failed startup is great for Big Tech: they get the IP they want and the employees that matter, and get to jettison everyone else without having to do a future layoff. That they never thought to do so previously was, in retrospect, downstream of “the way things are done”, not some sort of legal requirement; once the law, in the form of over-eager regulators who didn’t understand what they were regulating, gave them no choice, it’s not at all clear why they would go back to the old model.

It’s worth noting that there are two aspects of this deal that make it considerably less stinky — or, perhaps, give it a different odor. The first is that Nvidia and Groq appear to have done very well by existing employees. From [Axios](<https://www.axios.com/2025/12/28/nvidia-groq-shareholders>):

> Around 90% of Groq employees are said to be joining Nvidia, and they will be paid cash for all vested shares. Their unvested shares will be paid out at the $20 billion valuation, but via Nvidia stock that vests on a schedule. There are also around 50 members of that group whose entire stock packages are being accelerated and paid out in cash. Remaining Groq employees will also be paid for vested shares, plus will receive a package that includes economic participation in the ongoing company. Any Groq employee — staying or leaving — with the company for less than one year will have their vesting cliff dropped, so they can get some up-front liquidity.

The second smell, if you will, is that there are actual anticompetitive concerns with this deal. Groq chips are not by any means a substitute for Nvidia chips, which rely on slower but significantly higher capacity memory, which is essential for training, larger language models, big context windows, etc.; however, they are highly differentiated in terms of high speed inference specifically, which will be a portion of the inference market (think highly interactive voice models, for example, or highly-personalized ad serving, or model routing). Nvidia is buying capability that they didn’t have, and which threatened to take some amount of their market share.

Except that they didn’t buy, remember? This is a case where this deal structure really is brilliant: Nvidia isn’t avoiding unfair indiscriminate scrutiny; they’re avoiding reasonable deal scrutiny! Moreover, that by extension is the first obvious signal that this deal makes a lot of sense — potentially anticompetitive deals usually do! — and there really isn’t anything that can be done about it. I would be strictly opposed to restricting the freedom of movement for individual employees, and the licensing is non-exclusive; if anyone can license it, why can’t Nvidia?

Indeed, the question those overzealous regulators should be asking is if Nvidia would have even thought of this deal structure absent the precedent that was established across Big Tech. To what extent did going after deals that didn’t deserve the scrutiny create the conditions to make scrutiny impossible on a deal that does?

### Why This Deal Makes Sense

The fact that Nvidia has a non-exclusive license doesn’t diminish this deal’s upside in the slightest. Groq’s software-first approach slides very nicely, at least in theory, into Nvidia’s CUDA ecosystem; Nvidia will be able to build systems that use the right chips for the right inference, and do so in a way that abstracts the complexity away from customers. Moreover, Groq will benefit from NVLink and Nvidia’s overall network stack, particularly given the importance of tying multiple chips together to serve sufficiently-sized models.

And, of course, there is simply the question of talent: Ross is a superstar, and now he works for Nvidia; or perhaps more importantly, he doesn’t work for anyone else. Now those future Groq chips will be Nvidia chips — oh, and there’s a good chance they’ll now be made at TSMC, on a leading edge process that Nvidia will get access to before anyone else. That’s another way that Nvidia can make Groq far more valuable than it would have been on its own.

Of course Nvidia is paying through the nose: $20 billion is a lot of money for a license and people, and no business (that stays behind). I don’t have any problem with the number, however. First off, Nvidia can certainly afford it: the company had $22 billion in free cash flow _last quarter_. Second, as I noted, Nvidia is uniquely capable of increasing the value of Groq’s IP. Third, Nvidia is trying to win _now_ ; counting dollars and cents, or waiting a few years to develop your own version of Groq’s approach, is a losing strategy given Nvidia’s massive opportunity. Speed matters, not just in inference, but in market opportunities.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
