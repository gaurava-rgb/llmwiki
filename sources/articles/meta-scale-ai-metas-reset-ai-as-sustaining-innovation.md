---
title: "Meta + Scale AI?, Meta's Reset, AI as Sustaining Innovation"
reader_id: "01jxg0qa1f4c7vbehwx1630ya9"
notion_page_id: "3484ebe7-f118-8186-9b74-e2a4bd285b04"
reader_url: "https://read.readwise.io/read/01jxg0qa1f4c7vbehwx1630ya9"
source_url: "https://stratechery.com/2025/meta-scale-ai-metas-reset-ai-as-sustaining-innovation/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-06-11"
saved_at: "2025-06-11"
reading_time: "9 mins"
summary: "Meta is reportedly buying 49% of Scale AI and hiring CEO Alexandr Wang; this seems to be deal about fixing Llama, not about Scale AI."
content_hash: "10b77288526f5c7a4f41e1e8890848a0b17d1d806575faf73872ebfafc10ed67"
---

Meta is reportedly buying 49% of Scale AI and hiring CEO Alexandr Wang; this seems to be deal about fixing Llama, not about Scale AI.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On [Tuesday’s episode of Dithering](<https://dithering.passport.online/>) — recorded on John’s side from a bench outside the Steve Jobs Theater! — we discussed [Apple’s Retreat](<https://stratechery.com/2025/apple-retreats/>) to its safe space: working overtime on new user interfaces, while it resets its approach to AI.

On to the Update:

### Meta + Scale AI?

From the [New York Times](<https://www.nytimes.com/2025/06/10/technology/meta-new-ai-lab-superintelligence.html>):

> Meta is preparing to unveil a new artificial intelligence research lab dedicated to pursuing “superintelligence,” a hypothetical A.I. system that exceeds the powers of the human brain, as the tech giant jockeys to stay competitive in the technology race, according to four people with knowledge of the company’s plans.
>
> Meta has tapped Alexandr Wang, 28, the founder and chief executive of the A.I. start-up Scale AI, to join the new lab, the people said, and has been in talks to invest billions of dollars in his company as part of a deal that would also bring other Scale AI employees to the company. Meta has offered seven- to nine-figure compensation packages to dozens of researchers from leading A.I. companies such as OpenAI and Google, with some agreeing to join, according to the people.
>
> The new lab is part of a larger reorganization of Meta’s A.I. efforts, the people said. The company, which owns Facebook, Instagram and WhatsApp, has recently grappled with internal management struggles over the technology, as well as employee churn and several product releases that fell flat, two of the people said.

This news, particularly the Scale AI piece, is very odd in isolation. First off there is the structure of this deal; from [The Information](<https://www.theinformation.com/articles/meta-pay-nearly-15-billion-scale-ai-stake-startups-28-year-old-ceo>):

> Meta has agreed to take a 49% stake in data labeling firm Scale AI for $14.8 billion, two people familiar with the matter said. The unusual deal will be structured so Meta will send the cash to Scale’s existing shareholders and place the startup’s CEO, Alexandr Wang, in a top position inside Meta, the people said.

The most obvious explanation for the structure is that Meta wants to avoid the sort of antitrust scrutiny that would attend to an acquisition. This explanation applies broadly — big tech generally and Meta specifically are under massive scrutiny in terms of acquisitions, including Meta going to trial for acquisitions it made over a decade ago — and narrowly: Scale AI is a supplier for not just Meta but also Meta’s competitors, including Google and OpenAI. Vertical mergers are generally allowed under U.S. antitrust law, but things could definitely be dicier in the E.U., and Meta probably just doesn’t want to risk it.

The problem, however, is that just because Meta isn’t acquiring Scale AI doesn’t mean the deal can’t be scrutinized. Indeed, Section 7 of the Clayton Act is explicit about covering only partial acquisitions:

> No person engaged in commerce or in any activity affecting commerce shall acquire, directly or indirectly, the whole or any part of the stock or other share capital and no person subject to the jurisdiction of the Federal Trade Commission shall acquire the whole or any part of the assets of another person engaged also in commerce or in any activity affecting commerce, where in any line of commerce or in any activity affecting commerce in any section of the country, the effect of such acquisition may be substantially to lessen competition, or to tend to create a monopoly.

Of course there are a lot of things that are theoretically illegal under these century-old statutes, but this specific question was a part of the Biden administration’s [new merger guidelines](<https://www.ftc.gov/system/files/ftc_gov/pdf/2023_merger_guidelines_final_12.18.2023.pdf>):

> **Guideline 11: When an Acquisition Involves Partial Ownership or Minority Interests, the Agencies Examine Its Impact on Competition.** The Agencies apply the frameworks in Guidelines 1-6 to assess if an acquisition of partial control or common ownership may substantially lessen competition.

These guidelines were [reaffirmed by the Trump administration](<https://www.ftc.gov/news-events/news/press-releases/2025/02/ftc-chairman-andrew-n-ferguson-announces-ftc-dojs-joint-2023-merger-guidelines-are-effect>) earlier this year, so it certainly seems reasonable to assume there will be some sort of scrutiny.

Even beyond that, however — and perhaps this makes the regulators’ point — it seems likely that this will kill Scale AI’s business with the big labs in particular, who would be concerned about their data ending up in the hands of Meta, which is to say this is a deal that would destroy the enterprise value that Meta is theoretically investing in.

As it is, many of the labs, particularly OpenAI, have been bringing more of their data work in-house, which helped to contribute to Scale AI missing its revenue targets last year. From [The Information in April](<https://www.theinformation.com/articles/scale-ai-missed-revenue-profit-targets-ahead-share-sale>):

> Scale AI, the fast-growing data-labeling startup, missed its revenue and profit targets last year, but its investors are undeterred. The company is close to finalizing about a $150 million share sale, largely to existing investors, that values it at around $25 billion, up about 80% from a year ago…
>
> In an investor presentation, Scale AI is stressing its move into building AI apps for a broader set of companies, not just helping to refine large language models for big tech firms and AI labs. It said last year it netted more than a dozen new corporate customers, with over $200 million in annual contract value. That list includes Morgan Stanley; the U.S. Army; Marc Benioff’s media firm, Time; and Cisco, which is also a Scale investor. Scale forecast its apps business would generate $1.3 billion, one-fifth of its sales, by 2027.
>
> Scale’s larger business of using a network of human experts to provide data for top AI companies has more competition now. OpenAI has moved to bring more of its data-labeling efforts in-house. Other Scale rivals, like Turing and Invisible, have raised new funding in recent months.

That enterprise segment is interesting, and is a potential match with Meta’s open-source Llama efforts, but there is no reason for Meta to pay a premium to own 49% of that business, even if, [according to Semafor](<https://www.semafor.com/article/06/10/2025/metas-15-billion-investment-in-scale-ai-comes-with-a-hidden-perk>), a big portion of the company’s investment is actually payment for future services.

### Meta’s Reset

In fact, the more pertinent angle to discuss this deal is probably Llama. Llama 4 was widely viewed as a disappointing model, and [a big portion of the original Llama team has long since left Meta](<https://www.businessinsider.com/meta-llama-ai-talent-mistral-2025-5>). [I noted on Sharp Tech](<https://sharptech.fm/member/episode/meta-and-its-many-plans-in-ai-apple-gets-hammered-in-court-the-costs-of-waiting-to-do-the-right-thing>) after [my recent interview with Meta CEO Mark Zuckerberg](<https://stratechery.com/2025/an-interview-with-meta-ceo-mark-zuckerberg-about-ai-and-the-evolution-of-social-media/>) that his media tour about AI seemed a bit forced and unfocused, and have heard through the grapevine that Zuckerberg was considering a wholesale reset of the company’s AI efforts, with the biggest priority being the search for a new AI chief to take firmer control of the company’s efforts.

That, in the end, may be the Occam’s Razor explanation of this deal: this is a very expensive acquihire of Alexandr Wang, Scale AI’s co-founder and CEO, with the price softened a bit by virtue of paying Scale AI for work that Meta was going to have the company do anyways. Wang isn’t a researcher, but he is an executive and leader who is familiar with the space, and Meta needs leadership in addition to talent. That’s also [Casey Newton’s read of the situation at Platformer](<https://www.platformer.news/meta-scale-investment-zuckerberg-wang/?ref=platformer-newsletter>):

> The company lost last year to the Llama 4 dysfunction. Zuckerberg is determined not to lose this one, too. And so talk of mere AGI is out, and a new “superintelligence” team is on its way in. In coming weeks, Meta is set to announce several key hires for the team, I’m told. At least one will be a relatively high-profile departure from DeepMind. All will be making pro-athlete money or better; I heard one credible story of a researcher being offered $75 million to join Meta. (The Times reports that some offers stretch into nine figures.) That may sound like a lot for one person, and it is. But in some real sense Meta’s future depends on hiring and retaining those people, and Meta has already committed $65 billion to AI infrastructure this year. What’s a few hundred million more?
>
> Zuckerberg led the recruiting effort himself — something he has done before in high-stakes situations. He reaches out to people directly; sometimes they first assume it is spam. They have dinner at his homes in Palo Alto and Lake Tahoe. They go on long walks to talk about the future. More than a decade ago, he recruited Yann LeCun in this way; LeCun, a pioneering AI researcher, would go on to become the company’s chief AI scientist. The pitch: come work with the best in the industry. At Meta you’ll have unlimited compute to realize your dreams of superintelligence. Billions of people will use what you make. And you’ll work directly with Zuckerberg — this team will sit next to him, I’m told.

As Newton notes, that last detail cuts both ways: if your dream is to create AGI, or SuperIntelligence, or whatever it’s called these days, then do you really want to do it in ultimate service to Meta?

On the other hand, the fact that the one hire Newton mentioned is a DeepMind employee speaks to a potential lane for this new Meta AI lab: if you’re a true believer in AGI, you probably want to work for Anthropic; if you want to work on a consumer business from scratch then you want to work for OpenAI. However, if you don’t want to work for OpenAI — and there are clearly a lot of AI folks that don’t at this point — then Meta might be preferable to Google, given the latter’s bureaucracy and inability to build products. At least at Meta you’ll have the best possible ally to cut through the red tape — the founder and CEO — and Meta generally still seems less sclerotic than Google if your goal is real world applications (and, as an aside, the dollar figures being discussed here to speak to how difficult it will be for Apple to catch up, if it wanted to).

### AI as Sustaining Innovation

The other reason to believe in Meta versus Google comes down to the difference between disruptive and sustaining innovations. The late Professor Clayton Christensen described the difference in [The Innovator’s Dilemma](<https://www.amazon.com/Innovators-Dilemma-Technologies-Management-Innovation-ebook/dp/B00E257S86/ref=sr_1_1?s=digital-text&ie=UTF8&qid=1443170772&sr=1-1&keywords=innovator%27s+dilemma>):

> Most new technologies foster improved product performance. I call these sustaining technologies. Some sustaining technologies can be discontinuous or radical in character, while others are of an incremental nature. What all sustaining technologies have in common is that they improve the performance of established products, along the dimensions of performance that mainstream customers in major markets have historically valued. Most technological advances in a given industry are sustaining in character. An important finding revealed in this book is that rarely have even the most radically difficult sustaining technologies precipitated the failure of leading firms.
>
> Occasionally, however, disruptive technologies emerge: innovations that result in worse product performance, at least in the near-term. Ironically, in each of the instances studied in this book, it was disruptive technology that precipitated the leading firms’ failure. Disruptive technologies bring to a market a very different value proposition than had been available previously. Generally, disruptive technologies underperform established products in mainstream markets. But they have other features that a few fringe (and generally new) customers value. Products based on disruptive technologies are typically cheaper, simpler, smaller, and, frequently, more convenient to use.

The question of whether generative AI is a sustaining or disruptive innovation for Google remains uncertain [two years after I raised it](<https://stratechery.com/2023/more-on-google-and-ai-openai-integration-and-microsoft/>). Obviously Google has tremendous AI capabilities both in terms of infrastructure and research, and generative AI is a sustaining innovation for its display advertising business and its cloud business; at the same time, the long-term questions around search monetization remain as pertinent as ever.

Meta, however, does not have a search business to potentially disrupt, and [a whole host of ways to leverage generative AI across its business](<https://stratechery.com/2024/metas-ai-abundance/>); for Zuckerberg and company I think that AI is absolutely a sustaining technology, which is why it ultimately makes sense to spend whatever is necessary to get the company moving in the right direction.

It’s also worth noting that Meta doesn’t really have any alternatives other than continuing to invest: Google is a competitor for advertising, the most financially compelling use case today; OpenAI is a competitor for consumer attention, Meta’s most important scarce resource; I suppose Anthropic would be a potential partner, but per the point above, that seems like the ultimate culture clash. If anything the most compatible partners for Meta would be Microsoft and Apple, but the former is obviously tied up with OpenAI, and the former, well, never say never forever, but definitely never for now.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
