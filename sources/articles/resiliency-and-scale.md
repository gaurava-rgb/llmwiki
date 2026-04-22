---
title: "Resiliency and Scale"
reader_id: "01k86gp1w8cf9bhqnnwxqtdsam"
notion_page_id: "3484ebe7-f118-81bd-bf87-e8421f27dc61"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01k86gp1w8cf9bhqnnwxqtdsam"
source_url: "https://stratechery.com/2025/resiliency-and-scale/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-10-22"
saved_at: "2025-10-22"
reading_time: "12 mins"
summary: "Decreasing transportation and communications costs increases resiliency in theory, but destroys it in practice. The only way to have resiliency is through less efficiency."
content_hash: "7e85fd43bab634e5b57ba9ea43dee3e3042260a55d02b22a7a54180def9c9440"
---

Decreasing transportation and communications costs increases resiliency in theory, but destroys it in practice. The only way to have resiliency is through less efficiency.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

There seems, at first glance, to be little in common between the two big stories of the last two weeks. On October 9, China announced expansive export controls on rare earths, which are critical to nearly all tech products; then, on October 20, US-East-1, the oldest and largest region of Amazon Web Services, suffered a DNS issue that impacted cloud services that people didn’t even know they used, until they were no longer available.

There is, however a commonality, one that cuts to the heart of accepted wisdom about both the Internet and international trade, and serves as a reminder that what actually happens in reality matters more than what should happen in theory.

### US-East-1 and the End of Resiliency

The Internet story is easier to tell. While the initial motivation for ARPANET, the progenitor of the Internet, was to share remote computing resources, the more famous motivation of surviving a nuclear attack did undergird a critical Internet technology: [packet switching](<https://www.rand.org/pubs/articles/2018/paul-baran-and-the-origins-of-the-internet.list.html>). Knocking out one node of the Internet should not break the whole thing, and, technically, it doesn’t. And yet we have what happened this week: US-East-1 is but one node on the Internet, but it is so critical to so many applications that it effectively felt like the Internet was broken.

The reasoning is straightforward: scale and inertia. Start with the latter: Northern Virginia was a place that, in the 1990s, had relatively cheap and reliable power, land, and a fairly benign natural-disaster profile; it also had one of the first major Internet exchange points, thanks to its proximity to Washington D.C., and was centrally located between the west coast and Europe. That drew AOL, the largest Internet Service Provider of the 1990s, which established the region as data center central, leading to an even larger buildout of critical infrastructure, and making it the obvious location to place AWS’s first data center in 2006.

That data center became what is known as US-East-1, and from the beginning it has been the location with the most capacity, the widest variety of instance types, and the first region to get AWS’s newest features. It’s so critical that AWS itself has repeatedly been shown to have dependencies on US-East-1; it’s also the default location in tutorials and templates used by developers around the world. You might make the case that “no one got fired for using US-East-1”, at least until now.

Amazon, meanwhile, has invested billions of dollars into AWS over the last two decades, making the case that enterprises ought not waste their time and money building out and maintaining their own servers: even if the costs penciled out similarly, the flexibility of being able to scale up and scale down instantly was worth shifting capital costs to operational ones.

The fact that this was not only a winning argument but an immensely profitable one became clear with [The AWS IPO](<https://stratechery.com/2015/the-aws-ipo/>), which is how I described the Amazon earnings where they first broke out AWS’s financials. For the first decade of AWS’ existence the conventional wisdom was that only Amazon, with its famous appetite for tiny margins, would be able to stomach similarly narrow margins in the cloud; in fact it turned out that AWS was extremely profitable, and that profitability increased with scale.

And, nestled within AWS’s scale, was US-East-1: that was the place with the cheapest instances, because it had the most, and that is where both startups and established businesses started as they moved to the cloud. Sure, best practices meant you had redundancy, but best practices are not always followed practices, and when it comes to networking, things can break in weird ways, particularly if DNS is involved.

The larger lesson, however, is that while the Internet provided resiliency in theory, it also dramatically reduced the costs of putting your data and applications anywhere; then, once you could put your data and applications anywhere, everyone put their data and applications in the place that was both the easiest and the cheapest. That, by extension, only increased the scale of the place where everyone put their data and applications, making it even cheaper and easier. The end result is that, as we saw this week, the Internet in practice is less resilient than it was 20 years ago. Back then data centers went down all of the time, but if that data center served a single customer in an office park it didn’t really matter; now one data center in Northern Virgina is a failure point that affects nearly everyone.

### Rare Earths and China Dependency

Rare earths are very different from packets that move with the speed of light. You have to build massive mines, separate trace minerals from mounds of dirt, then process and refine them to get something useful. It’s a similar story for physical goods generally: you have to get the raw materials, refine and process them, manufacture components, do final assembly, and then ship them to stores and warehouses until they reach their final destination in workplaces and homes.

This process was so onerous that, midway through the last century, only a portion of the world’s countries had ever managed to industrialize, and those that did trod similar paths and developed similar capabilities. Geography mattered tremendously, which is why, to take some classic examples, every country had their own car companies, their own chemical companies, etc. Yes, countries did search and colonize the planet in pursuit of raw materials, but the industrial base was firmly established in the homeland.

Technology of another sort changed this equation; from 2016’s [The Brexit Possibility](<https://stratechery.com/2016/the-brexit-possibility/>):

> In the years leading up to the 1970s, three technological advances completely transformed the meaning of globalization:
>
>   * In 1963, Boeing produced the 707-320B, the first jet airliner capable of non-stop service from the continental United States to Asia; in 1970 the 747 made this routine.
>   * In 1964, the first transpacific telephone cable between the United States and Japan was completed; over the next several years it would be extended throughout Asia.
>   * In 1968, ISO 668 standardized shipping containers, dramatically increasing the efficiency with which goods could be shipped over the ocean in particular.
>

>
> These three factors in combination, for the first time, enabled a new kind of trade. Instead of manufacturing products in the United States (or Europe or Japan or anywhere else) and trading them to other countries, multinational corporations could invert themselves: design products in their home markets, then communicate those designs to factories in other countries, and ship finished products back to their domestic market. And, thanks to the dramatically lower wages in Asia (supercharged by China’s opening in 1978), it was immensely profitable to do just that.

What followed over the last several decades was the same establishment of scale and inertia that led to a dependency on US-East-1 on the Internet, only in this case the center of gravity was China. Once the cost of communication and transportation plummeted it suddenly became viable to shift industry across the globe in pursuit of lower labor costs, looser environmental laws, and governments eager to support factory build-outs. Then, over time, scale and inertia took over: if everyone else was building a factory in China, it was easier to build your factory there; if all of the factories for your components were there, it was easier to do final assembly there.

[This pattern applied to rare earths just as much as anything else](<https://stratechery.com/2025/an-interview-with-gracelin-baskaran-about-rare-earths/>). China identified rare earths as a strategic priority even as [the United States made it increasingly untenable](<https://stratechery.com/2025/china-and-rare-earth-metals-chips-and-rare-earths-the-u-s-s-self-inflicted-challenge/>) to maintain, much less expand, rare earth mining and processing here; over time nearly every part of the rare earth production chain, from separation to processing to refining to actual usage in final products became centered in China, and [any attempts to build out an alternative saw their market flooded by Chinese supply](<https://www.wsj.com/economy/trade/how-china-took-over-the-worlds-rare-earths-industry-fb668839>), driving down prices and dooming projects. Not that end users cared: they could just buy from China, just like everyone everywhere increasingly bought everything from China.

One of the critiques I’ve previously leveled at classical free trade arguments is that they ignore the importance of learning curves; from [A Chance to Build](<https://stratechery.com/2024/a-chance-to-build/>):

> The story to me seems straightforward: the big loser in the post World War 2 reconfiguration I described above was the American worker; yes, we have all of those service jobs, but what we have much less of are traditional manufacturing jobs. What happened to chips in the 1960s happened to manufacturing of all kinds over the ensuing decades. Countries like China started with labor cost advantages, and, over time, moved up learning curves that the U.S. dismantled; that is how you end up with this from Walter Isaacson in his [Steve Jobs biography](<https://www.simonandschuster.com/books/Steve-Jobs/Walter-Isaacson/9781982176860>) about a dinner with then-President Obama:
>
>> When Jobs’s turn came, he stressed the need for more trained engineers and suggested that any foreign students who earned an engineering degree in the United States should be given a visa to stay in the country. Obama said that could be done only in the context of the “Dream Act,” which would allow illegal aliens who arrived as minors and finished high school to become legal residents — something that the Republicans had blocked. Jobs found this an annoying example of how politics can lead to paralysis. “The president is very smart, but he kept explaining to us reasons why things can’t get done,” he recalled. “It infuriates me.”
>>
>> Jobs went on to urge that a way be found to train more American engineers. Apple had 700,000 factory workers employed in China, he said, and that was because it needed 30,000 engineers on-site to support those workers. “You can’t find that many in America to hire,” he said. These factory engineers did not have to be PhDs or geniuses; they simply needed to have basic engineering skills for manufacturing. Tech schools, community colleges, or trade schools could train them. “If you could educate these engineers,” he said, “we could move more manufacturing plants here.” The argument made a strong impression on the president. Two or three times over the next month he told his aides, “We’ve got to find ways to train those 30,000 manufacturing engineers that Jobs told us about.”
>
> I think that Jobs had cause-and-effect backwards: there are not 30,000 manufacturing engineers in the U.S. because there are not 30,000 manufacturing engineering jobs to be filled. That is because the structure of the world economy — choices made starting with Bretton Woods in particular, and cemented by the removal of tariffs over time — made them nonviable. Say what you will about the viability or wisdom of Trump’s tariffs, the motivation — to undo eighty years of structural changes — is pretty straightforward!
>
> The other thing about Jobs’ answer is how ultimately self-serving it was. This is not to say it was wrong: Apple could not only not manufacture an iPhone in the U.S. because of cost, it also can’t do so because of capability; that capability is downstream of an ecosystem that has developed in Asia and a long learning curve that China has traveled and that the U.S. has abandoned. Ultimately, though, the benefit to Apple has been profound: the company has the best supply chain in the world, centered in China, that gives it the capability to build computers on an unimaginable scale with maximum quality for not that much money at all.

The [Apple-China story is so compelling](<https://stratechery.com/2025/an-interview-with-apple-in-china-author-patrick-mcgee/>) because it is so representative of how the U.S. has become dependent on China. What is notable, however, is that this dependency points to another flaw in classic free trade formulations: while in theory free trade and globalization make supply chains more resilient because you can source from anywhere, in practice free trade has destroyed resiliency. Apple CEO Tim Cook famously said in what became known as [The Tim Cook Doctrine](<https://asymco.com/2011/01/17/the-cook-doctrine/>):

> We believe that we need to own and control the primary technologies behind the products we make, and participate only in markets where we can make a significant contribution.

The fact of the matter, however, is that Apple’s most important technology — the one architected by Cook himself — is its unmatched capability to make the most sophisticated and profitable devices at astronomical scale, and Apple ultimately does not own and control it: China does.

So it goes for nearly everything else in the industrial supply chain, including rare earths. Rare earths are not, in fact, rare, but China’s scale and the inertia of the last forty years has led to total dependence on a country that is a geopolitical foe of the United States. And so, once again, removing or reducing the costs of transportation and communication — this time for atoms — did not increase resiliency but rather, thanks to the pursuit of lower costs enabled by scale, destroyed it.

### COVID and Information Resiliency

There is a happier story to be told about overcoming resiliency collapse, but I should warn you up front, this might be a controversial take. It has to do with the current state of information, the earliest and most popular Internet content.

Back in March 2020 I wrote an Article entitled [Zero Trust Information](<https://stratechery.com/2020/zero-trust-information/>) that made the case that the Internet was under-appreciated as a medium for conveying information that cut against the prevailing wisdom; my go-to example was the Seattle Flu Study, which heroically traced the spread of COVID in the United States at the beginning of 2020, making the (correct) case that the virus was far more widespread in the U.S. than the CDC in particular was willing to admit.

In truth, however, my optimism was misplaced, or at least early. What followed in the weeks and months and even years afterwards was one of the greatest failures in information discovery and propagation maybe ever. I actually wrote an Update on [March 2, 2020](<https://stratechery.com/2020/covid-19-cancellations-apple-china-and-data-what-we-might-know/>) that included a huge amount of relevant COVID information — including the fact that it was both going to infect everyone, and that it was much less fatal than initially assumed — that only became widely accepted years later (and still isn’t accepted by a big chunk of the population).

It’s hard not to think about how much differently we might have handled the ensuing months and years if just those two facts were widely accepted, much less other banal observations like the fact that of course natural immunity is a real thing, or that airborne viruses are all-but-inescapable indoors, but much less of an issue outdoors. Unfortunately what happened is that by 2020 information distribution was highly centralized on Facebook, Twitter, and YouTube, and all three companies went to extraordinary lengths to limit the aperture of acceptable discourse on topics that contained a great deal of unknowns; indeed, it’s possible that that March 2 Update, had it been posted on one of those platforms, would have at one point earned me a ban. In short, our resiliency in terms of information propagation was by 2020 completely destroyed, and we all suffered the consequences.

Then Elon Musk bought Twitter.

What is fascinating about what has happened in the years since Musk’s purchase is not that Twitter has become a fountain of truth, even if it did in some respects become considerably freer. More importantly, Musk’s purchase and ensuing political advocacy provided the impetus for a number of Twitter alternatives, including Threads, Mastodon, and BlueSky.

Each of these networks has its own focus and mores and overall culture. What is critical about their existence, however, is not that any one of them has a monopoly on the truth: rather, given that such a monopoly is impossible, it’s heartening that there is more than one forum. To that end, should a COVID-like episode arise today, there may be an easily distinguishable and widely-held-on-the-platform X truth, and Threads truth, and Mastodon truth, and BlueSky truth; the fact that none of those truths will be completely right — and in come cases completely at odds — is not a bug not a feature: that’s actual resiliency, because it increases the likelihood that we collectively arrive at the right answer sooner than we did in the COVID era.

### The Costs of Resiliency

What is worth noting is that the only way we arrived at this point is through a fair bit of value destruction: Musk overpaid for Twitter, and losing a monopoly on short-form text communication diminished the value further. I think, however, that the collective outcome was positive.

Unwinding US-East-1 dependencies will also take a similar sort of pain: businesses will need to spend money to truly understand their stack, and build actual resiliency into their systems, such that one region on one cloud provider going down doesn’t screw up their business; it can be done, it just needs the budget.

And, in the end, we can do something similar with China. There, though, the difference between atoms and bits is very profound, and exceptionally costly. Overcoming the advantages of scale and decades-long learning curves will be very painful and very expensive; the only solution to the inevitable destruction of resiliency that comes from decreased transportation and communications costs is to increase costs elsewhere, even if those costs are artificial and lead to deadweight loss.

I am, needless to say, much more optimistic about our willingness to accept the costs of moving some bits around than I am the willingness to accept the drastically larger and longer costs of moving atoms. If we don’t, however, then we need to be clear that the true price being paid for global efficiency is national resiliency. Pursuing the former led to the destruction of the latter; there’s no way back other than destroying some value along the way.

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
