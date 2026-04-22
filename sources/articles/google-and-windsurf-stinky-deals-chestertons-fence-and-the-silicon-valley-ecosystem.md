---
title: "Google and Windsurf, Stinky Deals, Chesterton's Fence and the Silicon Valley Ecosystem"
reader_id: "01k050mvk1nvsjtf8ndtk3nesk"
notion_page_id: "3484ebe7-f118-81cf-9eb4-c9c07bee8abd"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01k050mvk1nvsjtf8ndtk3nesk"
source_url: "https://stratechery.com/2025/google-and-windsurf-stinky-deals-chestertons-fence-and-the-silicon-valley-ecosystem/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-07-14"
saved_at: "2025-07-14"
reading_time: "11 mins"
summary: "Windsurf's founders and IP are going to Google in the latest stinky deal that is downstream of regulator's recklessly messing the startup ecosystem."
content_hash: "c478ca6b3054450531a61f12008fc058a1803eba0d7073b5095232d28e63862a"
---

Windsurf's founders and IP are going to Google in the latest stinky deal that is downstream of regulator's recklessly messing the startup ecosystem.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On [Thursday’s episode of Sharp Tech](<https://sharptech.fm/member/episode/apple-searches-for-an-ai-partner-a-second-fair-use-ruling-and-reckoning-with-reality-the-f-1-movie-and-related-matters>), we discussed Apple’s potential search for an AI partner, fair use and AI training, and the recent F1 movie.

On to the Update:

### Google and Windsurf

From [The Information](<https://www.theinformation.com/articles/openai-windsurf-break-acquisition-talks-microsoft-ip-concerns>):

> OpenAI’s discussions to buy Windsurf, the maker of a popular artificial intelligence coding assistant formerly known as Codeium, have ended. Instead, Google will hire Windsurf’s CEO, Varun Mohan, and some of the startup’s staff, both Google and Windsurf said. The months-long talks between OpenAI to buy the startup for $3 billion ended in recent days. Among the reasons: Windsurf’s team raised concerns over how the coding assistant would fit into the OpenAI and Microsoft agreement, which requires OpenAI to share its technology with Microsoft, according to two people familiar with the company’s discussions. Google is paying $2.4 billion for an nonexclusive licensing fee that will pay for Windsurf’s technology and multiple years of compensation for Windsurf staff coming to the company, according to a person with direct knowledge. It will not take a stake in the company, Google said.

The first-order effects of this news are notable, although not the biggest takeaway from this deal (which I will get to in a moment). First, Cursor is firmly established as the independent AI-empowered integrated development environment (IDE) contender; Cursor relies on foundational models from the big AI labs, including Anthropic, OpenAI, Google, and xAI, and also develops its own models using data it gets from users (see the [Stratechery Interview with Cursor CEO Michael Truell](<https://stratechery.com/2025/an-interview-with-cursor-co-founder-and-ceo-michael-truell-about-coding-with-ai/>)). Frankly, however, I think this was mostly already the case: while it’s impossible to get clear data on usage, anecdotally I know a lot of people who use Cursor, and didn’t really know anyone using Windsurf (which I think is an important factor for the discussion below).

Anthropic, meanwhile, has their Claude Code product, which I discussed in passing in last week’s [Tech Philosophy and AI Opportunity](<https://stratechery.com/2025/tech-philosophy-and-ai-opportunity/>); I think the AI startup is primarily focused on making a coding agent, while Cursor is a bet on continued human involvement (i.e. more on the “tool” side of this graph):

[![A drawing of Apple, Microsoft, OpenAI, Anthropic, Meta, and Google on the AI Tech Philosophy Opportunity Graph](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/07/tech-philosophy-ai-opportunity-4-1.png?resize=1330%2C928&ssl=1)](<https://stratechery.com/2025/tech-philosophy-and-ai-opportunity/>)

In this framing Windsurf, to the extent it was a tool for using AI in coding, aligned with my placement of OpenAI, which is primarily about ChatGPT’s role in users’ lives; acquiring Windsurf made sense in terms of making a ChatGPT subscription that much more of a full-service offering for end users. OpenAI also has [Codex](<https://openai.com/index/introducing-codex/>); Codex was originally a code-focused LLM that powered the original GitHub Copilot; that model was retired in 2023 when general-purpose LLMs started out-performing it. The new Codex is more akin to Claude Code: it uses a finetuned o3-based model, and is available both in the terminal and also ChatGPT. It’s unclear if Windsurf was going to be folded into Codex, or if OpenAI planned to also offer a full-fledged IDE; my guess is the latter, [given OpenAI’s (appropriate) drive to control all user touchpoints](<https://stratechery.com/2025/openai-restructuring-microsofts-rights-simo-and-windsurf/>).

However, that is a moot point now: Windsurf’s founders and some number of their engineers are headed to Google, along with a license to Windsurf’s IP, presumably to work on Google’s own coding offerings. At a very high level this isn’t abnormal: Big Tech companies make aquihires all the time, and sometimes they acquire companies out from under the noses of their competitors. However, what has much of Silicon Valley up-in-arms is that this wasn’t an acquisition; it was a gutting.

### Stinky Deals

Continuing from _The Information_ :

> The deal will generate a return for at least some of the startup’s investors, according to a person familiar with the deal. Employees with vested shares will receive cash, but those without vested equity — many of whom joined in the past year — will not receive a payout, according to a person who spoke to leadership at Windsurf…
>
> Other large tech companies have paid huge sums of money as part of similar transactions, in which they hire much sought-after AI talent without outright acquiring their companies. Last month, Meta invested $14.3 billion in Scale AI while also hiring the startup’s CEO Alexandr Wang and several of its top employees. Last year, Google hired Character AI co-founders Noam Shazeer and Daniel De Freitas while paying the startup a $2.7 billion licensing fee, which was used to pay out shareholders. And also last year, Microsoft paid a roughly $650 million licensing fee to Inflection to hire most of its staff, including its co-founders. The unconventional agreements have allowed the big tech companies to quickly hire top AI researchers without going through the lengthy review process of a formal merger.

All of these deals stink, although the stinkiness factor varies:

  * Scale AI is a real business. Meta’s investment hurts the company’s ability to supply other foundational AI labs, but Scale AI has other customers like the U.S. Defense Department; you could argue that this business is in fact much better off being independent from Meta.
  * Character.ai hasn’t yet proven itself as a real business, but (1) it does have an independent userbase, (2) it is not competitive with Google, and (3) it made sense for the company to pivot away from training its own models to building on top of foundational AI model offerings, which in turn meant it wasn’t illogical for the company’s model-building talent to decamp for Google.
  * Inflection was basically a failed startup with a lot of GPUs; this was the most obvious candidate for an acquihire, but Microsoft simply hired (almost) everyone instead and paid off the investors.



Inflection seems to be the closest analogy for what happened with Windsurf; what appears to be different — stinkier, if you will — about this Windsurf deal is the extent to which a large portion of Windsurf employees appear to have been left out to dry, or rather, remain employed with a company that appeared to already be losing and now lost a huge portion of its talent. Congratulations?

There remains a lot of dispute over the details of this deal, and given the disgust expressed across the ecosystem about the treatment of the remaining employees I expect that this will ultimately resolve with some sort of payout for the employees that remain; Windsurf reportedly retained $100 million that could be paid out to those not hired by Google if the company shuts down in the near future. Whatever happens, however, is clearly much worse than the old model, wherein big tech companies acquired the entire company, giving everyone who took the risk of joining a startup at minimum a job.

### Chesterton’s Fence and the Silicon Valley Ecosystem

There is [a famous quote from G.K. Chesterton](<https://www.chesterton.org/taking-a-fence-down/>) you have probably heard:

> In the matter of reforming things, as distinct from deforming them, there is one plain and simple principle; a principle which will probably be called a paradox. There exists in such a case a certain institution or law; let us say, for the sake of simplicity, a fence or gate erected across a road. The more modern type of reformer goes gaily up to it and says, “I don’t see the use of this; let us clear it away.” To which the more intelligent type of reformer will do well to answer: “If you don’t see the use of it, I certainly won’t let you clear it away. Go away and think. Then, when you can come back and tell me that you do see the use of it, I may allow you to destroy it.”

Back in February 2020, during my last pre-COVID trip, [I appeared on a panel](<https://stratechery.com/2020/doj-public-workshop-on-venture-capital-and-antitrust/>) for a [Public Workshop on Venture Capital and Antitrust](<https://www.justice.gov/opa/pr/department-justice-antitrust-division-co-host-workshop-venture-capital-investment-and>) hosted by the Department of Justice. What I learned that day alarmed me so much that I wrote an article entitled [First, Do No Harm](<https://stratechery.com/2020/first-do-no-harm/>). Here is the opening of that Article:

> While _primum non nocere_ — Latin for “First, do no harm” — is commonly associated with the [Hippocratic Oath](<https://en.wikipedia.org/wiki/Hippocratic_Oath>) taken by physicians, its actual provenance is uncertain; the phrase [likely originated](<https://accp1.onlinelibrary.wiley.com/doi/abs/10.1177/0091270004273680>) with the English doctor [Thomas Sydenham](<https://en.wikipedia.org/wiki/Thomas_Sydenham>) in the 1600s, but didn’t appear in writing until 1860. The uncertainty is just as well: core to the idea of _primum non nocere_ is the danger of unintended consequences; sometimes it is better for a doctor to not do anything than to risk causing more harm than good.
>
> I was reminded of this phrase yesterday when [the FTC announced](<https://www.ftc.gov/news-events/press-releases/2020/02/ftc-examine-past-acquisitions-large-technology-companies>) it was requesting data from the Big Tech companies about small scale acquisitions made over the last decade…I am all for the Federal Trade Commission being better informed about the tech industry; what increasingly concerns me is the potential unintended consequences of the government getting involved in tech acquisitions, particularly the small-scale ones implicated in this investigation.

My contention in that Article is that small-scale acquisitions of primarily failed startups by Big Tech companies was essential to how the Silicon Valley ecosystem worked:

> The first group that benefits from large tech company acquisitions is end users. The fastest possible way for a new technology or feature to be diffused to users broadly is for it to be incorporated by one of the large platforms or Aggregators. Suddenly, instead of reaching a few thousand or even a few million people, a new technology can reach billions of people. It’s difficult to overstate how compelling this point is from a consumer welfare perspective: banning acquisitions means denying billions of people access to a particular technology for years, if not forever.
>
> The second group that benefits from large tech company acquisitions is investors. If one of their startups creates something useful, that investment can earn a return even if said startup does not have a clear business model or user acquisition strategy. To put it another way, investors have the freedom to be more speculative in their investments, and pay more attention to technological breakthroughs and less to monetization, because there is always the possibility of exiting via acquisition. This benefit accrues broadly: more money going to more initiatives is ultimately good for society.
>
> The third group that benefits from large tech company acquisitions is entrepreneurs and startup employees. Trying to build something new is difficult and draining; it makes the effort — which will likely fail — far more palatable knowing that if it doesn’t work out an acquihire acquisition is a likely outcome. Sure, it might have been easier to simply apply for a job at Google or Facebook, but being handed one because you worked for a failed startup reduces the risk of going to work for that startup in the first place.
>
> It’s important to note that the sort of acquisitions the FTC is looking at almost certainly fall predominantly in this third group. Acquihires of failed startups is arguably the most tangible way that Big Tech companies contribute to Silicon Valley’s durable startup culture: there is more reason for entrepreneurs, early employees, and investors to take a chance on new ideas because the Big Tech companies provide a backstop.

Unfortunately, regulators didn’t listen. The effort to indiscriminately throw sand in the gears of the Silicon Valley machine — which, it should be noted, started under the first Trump administration, but was dramatically accelerated under the Biden administration — is undoubtedly the biggest driver of these stinky deals. Big Tech, starting with Microsoft, realized that the easiest way to avoid regulatory annoyance around acquihires was to separate the acquisition from the hiring; what has happened as these deals have evolved is that tech companies increasingly realize that if they are simply hiring and not acquiring then they don’t have to hire everyone. That, however, breaks the implicit social contract that made startup employment significantly less risky for rank-and-file employees.

What is frustrating about this development is that there is a good chance we will never go back. The fact of the matter is that picking-and-choosing who to hire from a failed startup is great for Big Tech: they get the IP they want and the employees that matter, and get to jettison everyone else without having to do a future layoff. That they never thought to do so previously was, in retrospect, downstream of “the way things are done”, not some sort of legal requirement; once the law, in the form of over-eager regulators who didn’t understand what they were regulating, gave them no choice, it’s not at all clear why they would go back to the old model.

This, in the long run, is very bad for startups. The incentives for founding a company do still remain; the founders of all four of the companies in the stinky list are doing very well for themselves. The people who are getting screwed, however, are the folks who were never necessarily going to get rich — that’s reserved for founders, and appropriately so — but who could justify rolling the dice on a positive outcome as long as they had downside protection in the form of guaranteed employment with a Big Tech company if things didn’t work out. Now, however, the best route for any non-founder is simply to pursue employment with a Big Tech company directly; the alternative, if the downside is unemployment or a contract with a hollowed-out doomed company, isn’t worth the risk (which, ultimately, again favors Big Tech, as it lowers competition for rank-and-file employees).

It is, in the end, one of the clearest examples of a Chesterton Fence you can come up with: regulators didn’t understand the role that seamless small acquisitions played in making Silicon Valley work, so they made them undesirable and untenable; the end result is a diminished ecosystem that further entrenches the biggest players, reduces long-term innovation and risk-taking, and destroys individual employees’ opportunity and bargaining power with big companies and their chances of earning a nice payday if things worked out.

One more note on this deal specifically: one of the reasons that the OpenAI deal fell through is because of questions around how the Windsurf acquisition intersected with OpenAI’s Microsoft deal and the requirement to share IP. That deal, meanwhile, is downstream from another oddity, which is OpenAI’s non-profit structure. I was very skeptical of that structure from the beginning; from [a 2015 Update](<https://stratechery.com/2015/openai-artificial-intelligence-and-data-data-and-recruiting/>):

> Elon Musk and Sam Altman, who head organizations (Tesla and YCombinator, respectively) that look a lot like the two examples I just described of companies threatened by Google and Facebook’s data advantage, have done exactly that with OpenAI, with the added incentive of making the entire thing a non-profit; I say “incentive” because being a non-profit is almost certainly a lot less about being altruistic and a lot more about the line I highlighted at the beginning: “We hope this is what matters most to the best in the field.” In other words, OpenAI may not have the best data, but at least it has a mission structure that may help idealist researchers sleep better at night. That OpenAI may help balance the playing field for Tesla and YCombinator is, I guess we’re supposed to believe, a happy coincidence.

In fact, what Altman (and Musk) did was tear down a Chesterton fence of their own; setting up a normal corporation with a normal cap table, ultimately governed by the profit incentive, was “the way things were done”. If OpenAI had such a normal structure from the beginning they wouldn’t have had to enter into this bizarre relationship with Microsoft in the first place. That they ultimately lost out on this deal because of their convoluted corporate structure, itself speaks to the wisdom of not messing with what works, without truly understanding what you are losing with utopian ideas like a non-profit tech company.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
