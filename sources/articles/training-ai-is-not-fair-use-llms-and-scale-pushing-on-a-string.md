---
title: "Training AI is Not Fair Use?, LLMs and Scale, Pushing on a String"
reader_id: "01jzk0w17wrb0twcrfn3pc5fe8"
notion_page_id: "3484ebe7-f118-810e-949b-fa30febd0d13"
reader_url: "https://read.readwise.io/read/01jzk0w17wrb0twcrfn3pc5fe8"
source_url: "https://stratechery.com/2025/training-ai-is-not-fair-use-llms-and-scale-pushing-on-a-string/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-07-07"
saved_at: "2025-07-07"
reading_time: "13 mins"
summary: "Meta won another fair use case, even though the judge wanted to rule against LLMs; he'll have a hard time doing so."
content_hash: "11e38d5e668ea5a8b12fb4a36b6954cf230c35b978e0728aceb3127cdb888fc6"
---

Meta won another fair use case, even though the judge wanted to rule against LLMs; he'll have a hard time doing so.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

Happy July 4th! I had a great summer break, and I hope you all had the same. And, at the same time, I’m happy to be back.

It is, however, summer, which means [the usual summer schedule](<https://stratechery.com/stratechery-plus/schedule/>) through August. Namely, while there will still be three Updates and/or Articles a week, there will be no Stratechery Interviews; in addition, there will be one extended episode of [Sharp Tech](<https://sharptech.fm/member>) a week, along with the usual two episodes of [Dithering](<https://dithering.passport.online/>).

On to the Update:

### Training AI is Not Fair Use?

A day after the Anthropic fair use decision that [I wrote about just before the break](<https://stratechery.com/2025/training-ai-is-fair-use-product-protection-versus-llm-liability-piracy-and-competition/>) came down, the same federal circuit delivered a strikingly different ruling in reasoning, but not outcome. From [Bloomberg Law](<https://news.bloomberglaw.com/legal-ops-and-tech/meta-beats-copyright-suit-from-authors-over-ai-training-on-books>):

> Meta Platforms Inc. escaped a first-of-its-kind copyright lawsuit from a group of authors who alleged the tech giant hoovered up millions of copyrighted books without permission to train its generative AI model called Llama. San Francisco federal Judge Vince Chhabria ruled Wednesday that Meta’s decision to use the books for training is protected under copyright law’s fair use defense, but he cautioned that his opinion is more a reflection on the authors’ failure to litigate the case effectively.
>
> “This ruling does not stand for the proposition that Meta’s use of copyrighted materials to train its language models is lawful,” Chhabria said. “It stands only for the proposition that these plaintiffs made the wrong arguments and failed to develop a record in support of the right one”…The ruling comes two days after a judge in the same court ruled largely in favor of AI competitor Anthropic PBC, which was similarly accused of illegally using books to train its models.

As a quick refresher, here is the [Stanford Library’s summary of the fair use test](<https://fairuse.stanford.edu/overview/fair-use/four-factors/>):

> The only way to get a definitive answer on whether a particular use is a fair use is to have it resolved in federal court. Judges use four factors to resolve fair use disputes, as discussed in detail below. It’s important to understand that these factors are only guidelines that courts are free to adapt to particular situations on a case‑by‑case basis. In other words, a judge has a great deal of freedom when making a fair use determination, so the outcome in any given case can be hard to predict.
>
> The four factors judges consider are:
>
>   * The purpose and character of your use
>   * The nature of the copyrighted work
>   * The amount and substantiality of the portion taken, and
>   * The effect of the use upon the potential market.
>


Judge William Alsup of the Northern District of California ruled that using copyrighted works to train AI was tranformative (factor one, in favor of fair use), commercial (factor two, against fair use), total but no individual work was necessary or reproducible (factor three, in favor of fair use), and an increase in competition for writing generally, but not for the books in question specifically (factor four, in favor of fair use).

Judge Chhabria, also of the Northern District of California, also found that using copyrighted works to train AI was transformative (factor one, in favor of fair use), commercial (factor two, against fair use), total but no individual work was necessary or reproducible (factor three, in favor of fair use). Where Judge Chhabria differed from Judge Alsup was in his evaluation of factor four.

In this Update I’m going to quote extensively from the case, as it’s an obvious counter to [my previous Update entitled “Training AI is Fair Use”](<https://stratechery.com/2025/training-ai-is-fair-use-product-protection-versus-llm-liability-piracy-and-competition/>); I’ll get into a bit of analysis, but expect more on this topic soon.

### LLMs and Scale

Here is the key section of [Judge Chhabria’s opinion](<https://storage.courtlistener.com/recap/gov.uscourts.cand.415175/gov.uscourts.cand.415175.598.0.pdf>) about the fourth factor:

> The Supreme Court has said that the “only harm” that matters under the fourth factor “is the harm of market substitution.” But indirect substitution is still substitution: If someone bought a romance novel written by an LLM instead of a romance novel written by a human author, the LLM-generated novel is substituting for the human-written one. This is different from the (non-cognizable) harm caused by criticism or commentary, which can harm demand for an original work without serving as a replacement for it.
>
> Relatedly, Meta argues that “legitimate” competition from noninfringing secondary works is not cognizable under the fourth factor. It cites the intermediate copying cases for this proposition. But key to those cases’ reasoning was the fact that the secondary users’ competing products did not benefit from the creative expression in the works they copied. By contrast, as discussed, LLMs are better able to generate text (including competing works) because they are trained on the creative expression in copyrighted books. So this competition is not “legitimate” within the meaning of those cases.
>
> It’s true that, in many copyright cases, this concept of market dilution or indirect substitution is not particularly important. That’s because, in a more typical case, an original work is being compared to a single secondary work. If the secondary work is somewhat similar, but not so similar as to effectively be a copy, it still might have a small indirect effect on the market for the original work. But that likely won’t matter. Recall that the fourth factor looks to whether “conduct of the sort engaged in by the defendant” would have a “substantially adverse impact on the potential market for the original.” The existence of some harm from indirect substitution isn’t dispositive of the fourth factor or the fair use inquiry. Where, for instance, the first factor cuts in favor of the secondary user, the law might tolerate a little bit of competition. In cases involving a single secondary work that’s similar-but-not-too-similar, it’s unlikely that harm from market dilution would be significant enough to matter. Even considering the effect of “widespread conduct of the sort engaged in by the defendant,” creating one indirectly substitutional work at a time could only have so great an effect on the market for the original.
>
> This case is different. This is not a case where an original work is being compared to one secondary work. Nor is this case like the previous fair use cases involving creation of a digital tool. In those cases, like Google Books and Perfect 10, the tool could at most be used to access part or all of the original works. This case, unlike any of those cases, involves a technology that can generate literally millions of secondary works, with a miniscule fraction of the time and creativity used to create the original works it was trained on. No other use — whether it’s the creation of a single secondary work or the creation of other digital tools — has anything near the potential to flood the market with competing works the way that LLM training does. And so the concept of market dilution becomes highly relevant.
>
> In arguing that this sort of harm doesn’t count just because it’s never made a difference in a case before, Meta makes the mistake the Supreme Court instructs parties and courts to avoid: robotically applying concepts from previous cases without stepping back to consider context. Fair use is meant to be a flexible doctrine that takes account of “significant changes in technology.” Courts can’t stick their heads in the sand to an obvious way that a new technology might severely harm the incentive to create, just because the issue has not come up before. Indeed, it seems likely that market dilution will often cause plaintiffs to decisively win the fourth factor — and thus win the fair use question overall — in cases like this.

Judge Chhabria’s argument is in many respects a logical extension of the argument both he and Judge Alsup make about factor three: in that case, both (correctly, in my mind) argue that while LLMs use the entirety of a copyrighted work in their training set, this is not necessarily a violation because the scale of data necessary to train an LLM means that any one work is not critical to the LLM, and besides, both Anthropic and Meta take care to ensure their models do not output exact copies of copyrighted work. In other words, Anthropic and Meta are not necessarily violating the individual copyright for a work because the scale of copyrighted work necessary is so large that the relative contribution of any one work renders the violation immaterial.

Judge Alsup’s dismissal of factor four, however, ignores scale; [from his opinion](<https://www.documentcloud.org/documents/25982111-bartz/>):

> Authors contend generically that training LLMs will result in an explosion of works competing with their works — such as by creating alternative summaries of factual events, alternative examples of compelling writing about fictional events, and so on. This order assumes that is so. But Authors’ complaint is no different than it would be if they complained that training school children to write well would result in an explosion of competing works. This is not the kind of competitive or creative displacement that concerns the Copyright Act. The Act seeks to advance original works of authorship, not to protect authors against competition.

Judge Chhabria says this is absurd:

> In a recent ruling on this topic, Judge Alsup focused heavily on the transformative nature of generative AI while brushing aside concerns about the harm it can inflict on the market for the works it gets trained on. Such harm would be no different, he reasoned, than the harm caused by using the works for “training schoolchildren to write well,” which could “result in an explosion of competing works.” According to Judge Alsup, this “is not the kind of competitive or creative displacement that concerns the Copyright Act.” But when it comes to market effects, using books to teach children to write is not remotely like using books to create a product that a single individual could employ to generate countless competing works with a miniscule fraction of the time and creativity it would otherwise take. This inapt analogy is not a basis for blowing off the most important factor in the fair use analysis.

As I noted before the break, I’m sympathetic to Judge Chhabria’s argument generally; using human analogies for computers ignores the fact that the speed and comprehensiveness with which computers can undertake human-like actions — like reading a book — makes for a fundamental difference in practical effects. To that end, just as computers can ingest books at far greater scale than humans can, so can they output text at a far greater scale; that, in Judge Chhabria’s mind, means that using copyrighted material to train LLMs fails the fair use test because the end result is an overwhelming amount of competition for copyrighted authors that is not at all analogous to a human reading a lot of books and subsequently writing one of his or her own.

### Pushing on a String

And yet, despite the fact that Judge Chhabria spent the first four pages of his opinion making this case — even before he got to the legal analysis — he ultimately ruled in Meta’s favor. Again from his opinion:

> Courts can’t decide cases based on what they think will or should happen in other cases. They must decide cases based on the arguments presented and the evidence submitted by the parties. The question, then, is whether these particular thirteen plaintiffs in this particular case have presented enough evidence to win on this factor. Or, to put it more precisely given the procedural posture of this case, whether these plaintiffs have presented enough evidence to raise a genuine dispute of material fact sufficient to give the question of market dilution to a jury. The answer is no.

Judge Chhabria is clearly frustrated with the plaintiffs in this case, practically begging them to come up with even a shred of evidence that LLMs have harmed the plaintiff’s market opportunities.

> Where a defendant introduces evidence of a lack of market harm, “and the plaintiff fails to introduce empirical evidence countering such a showing, the fourth factor should be weighed in the defendant’s favor.” That is exactly what happened here. Meta introduced evidence that its copying hasn’t caused market harm. The plaintiffs presented no empirical evidence to the contrary — no evidence that the copying has already caused market harm, and no evidence that the copying is likely to cause market harm in the future. All the plaintiffs presented is speculation, and speculation is insufficient to raise a genuine issue of fact and defeat summary judgment.

Here’s my observation: Judge Chhabria thinks he is criticizing the plaintiffs, but actually that last sentence characterizes his entire opinion. Judge Chhabria goes on and on about the the speculative harms of AI, but ultimately rules for Meta because “speculation is insufficient to raise a genuine issue of fact and defeat summary judgment”; what I would argue is that this isn’t a failure of the plaintiffs to present evidence, but is in fact the flip-side of the scale argument that Judge Chhabria says makes Meta guilty. I’ll let Judge Chhabria make the case for me:

> The plaintiffs argue that they didn’t need to present empirical evidence because market harm can be inferred. For this argument, they cite to Hachette, in which the Second Circuit inferred market harm — even though the plaintiffs had not provided “empirical data” showing any and the secondary user presented expert testimony that there was none — because it was “self-evident” that the secondary use would cause such harm if widespread. In Hachette, the secondary user maintained a database that let internet users “download an identical copy of” the plaintiffs’ books for free. The secondary use therefore offered a directly “competing substitute” for the original books.
>
> While it made sense to infer market harm in Hachette, it doesn’t make sense to do so here. First, the Supreme Court has stated that no “inference of market harm . . . is applicable to a case involving something beyond mere duplication for commercial purposes.” In Hachette, the secondary use was basically “mere duplication.” Here, by contrast, Meta’s use is highly transformative and has a purpose well beyond that. Second, unlike in Hachette, Meta’s use does not let users access any significant portion of the plaintiffs’ books, so it isn’t self-evident that Meta’s use would create harm via direct substitution. Nor is it self-evident that Llama will harm the book sale market by enabling users to create a flood of competing books. It’s possible, even likely, that Llama will harm the book sale market. But to conclude that it will requires inferring that Llama (and not just any LLM) can be used to create such books, that it will be used to create such books, that consumers will purchase those books instead of books written by human authors, that consumers will buy those books instead of the plaintiffs’ books in particular, and that Llama is meaningfully better at creating those books because it was trained on copyrighted material. In Hachette, on the other hand, the only necessary inference was that readers might choose to download the plaintiffs’ books for free instead of paying for them — a much shorter (and more obvious) inferential leap.
>
> On this record, then, Meta has defeated the plaintiffs’ half-hearted argument that its copying causes or threatens significant market harm. That conclusion may be in significant tension with reality, but it’s dictated by the choice the plaintiffs made to put forward two flawed theories of market harm while failing to present meaningful evidence on the effect of training LLMs like Llama with their books on the market for those books.

I disagree; that conclusion is dictated by the fact that measuring the market harm of LLMs to an individual author is effectively impossible, for the same reasons that any one copyrighted work are inconsequential to an LLM (i.e. Judge Chhabria’s factor three analysis). These authors may amend their case — Judge Chhabria clearly hopes they will, as he couldn’t be more clear that he wished he could rule in their favor — but they will face the fundamental problem of figuring out how to measure the buying decisions of individuals; actually, it’s worse than that, because the harm Judge Chhabria wants to find is the measurement of buying decisions _not_ made.

In this there is a strong similarity to the challenges faced by those seeking to use traditional antitrust arguments to constrain Aggregators; I refer to it as “pushing on a string”; from 2020’s [Anti-Monopoly vs. Antitrust](<https://stratechery.com/2020/anti-monopoly-vs-antitrust/>):

> So much modern antitrust action against tech companies is like pushing on a string: the reason these companies have power is because so many customers choose to use them, and it is both difficult and probably unwise to try and regulate the individual choices of billions of users. At the same time, as I noted, I am sympathetic to the issue of just how much power these companies have: constraining that power, though, needs new laws that start with Internet assumptions, and anti-monopoly advocates would do well to focus on solutions that, instead of retracting privileges, extend them (a la incorporations in the 1800s).
>
> These aren’t idle words: I have previously laid out ideas for **[regulating competition on the Internet](<https://stratechery.com/2019/a-framework-for-regulating-competition-on-the-internet/>)**. One thing that is critical is understanding that not all tech companies are the same: Apple and Android are traditional platforms, relatively well-served by traditional antitrust law (except for the fact that their duopoly helps both escape scrutiny together); Google and Facebook, though, are Aggregators, which require a different approach, which I laid out in 2019’s **[Where Warren’s Wrong](<https://stratechery.com/2019/where-warrens-wrong/>)**. These include a focus on acquisitions and anticompetitive contracts, which I was glad to see were also a focus of the committee (although I think the focus on small-scale acquisitions **[missed why acquisitions can be a good thing](<https://stratechery.com/2020/first-do-no-harm/>)**).

Judge Chhabria wants to push on a similar string: he can imagine the harms that LLMs cause to copyright holders broadly, and he’s probably right; a finding of copyright infringement, however, requires explicit harm, and it’s not clear at all how that can be measured. To that end, I suspect the eventual prevailing ruling on copyright and AI — which, given the conflict that is already emerging within a single court, seems inevitably headed for the Supreme Court — will ultimately come down in favor of the AI companies; if copyright advocates want a different result they will need to pass new laws (which, for the record, I would oppose, but I’m trying to not let that influence my analysis).

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
