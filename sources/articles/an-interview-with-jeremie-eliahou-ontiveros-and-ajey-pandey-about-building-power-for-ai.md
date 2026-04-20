---
title: "An Interview with Jeremie Eliahou Ontiveros and Ajey Pandey About Building Power for AI"
reader_id: "01kefbq5by9hz6xnnje3x7fcy3"
notion_page_id: "3464ebe7-f118-8139-b0bb-fb4aa1767771"
reader_url: "https://read.readwise.io/read/01kefbq5by9hz6xnnje3x7fcy3"
source_url: "https://stratechery.com/2026/an-interview-with-jeremie-eliahou-ontiveros-and-ajey-pandey-about-building-power-for-ai/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2026-01-08"
saved_at: "2026-01-08"
reading_time: "58 mins"
summary: "An Interview with Jeremie Eliahou Ontiveros and Ajey Pandey about how AI labs and hyperscalers are leveraging demand to build out entirely new electrical infrastructure for AI."
content_hash: "9caab4ae81b2e03bc77bce637ba838dea14690f8c57abaebb89739d8beec4659"
---

An Interview with Jeremie Eliahou Ontiveros and Ajey Pandey about how AI labs and hyperscalers are leveraging demand to build out entirely new electrical infrastructure for AI.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

This week’s Stratechery Interview is with [Jeremie Eliahou Ontiveros](<https://x.com/JeremieEO>) and [Ajey Pandey](<https://x.com/GridGodAjey>) from SemiAnalysis. Eliahou Ontiveros is the [Head of Datacenter & Energy Infrastructure Research](<https://semianalysis.com/jeremie-eliahou-ontiveros/>) at SemiAnalysis. Eliahou Ontiveros, who resides in Paris, was previously an equity analyst before joining SemiAnalysis to build out a research team focused on energy for AI data centers; Pandey is [an analyst](<https://semianalysis.com/ajey-pandey/>) at SemiAnalysis focused on energy infrastructure. Pandey, who resides in Vermont, previously worked in municipal utilities.

Over the winter break Eliahou Ontiveros and Pandey wrote [a fascinating report](<https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power>) about how AI Labs are leading the way in building new data centers with on-site power. This report covered, and referenced previous reports, about the unique load that AI is putting on the grid, and how companies — inspired by Elon Musk and xAI — are increasingly doing power generation themselves. In this interview we discuss this evolution, and what it means for U.S. electrical generation going forward; what surprised and delighted me is the extent to which this interview left me feeling pretty optimistic about the U.S. and our ability to innovate, and to leverage demand to enact long-standing necessary evolutions to our electrical grid. Or, to put it another way, [bubbles really do have benefits](<https://stratechery.com/2025/the-benefits-of-bubbles/>).

As a reminder, all Stratechery content, including interviews, is available as a podcast; click the link at the top of this email to add Stratechery to your podcast player.

On to the Interview:

### An Interview with Jeremie Eliahou Ontiveros and Ajey Pandey About Building Power for AI

_This interview is lightly edited for clarity._

**Topics:**

Backing Into Power | The Power Shortage | Grid Challenges | Behind the Meter | The Market Response to Power Demand | Energy Sources | Bubble Dynamics

#### Backing Into Power

**Jeremie Eliahou Ontiveros and Ajey Pandey, welcome to Stratechery.**

**Ajey Pandey:** Yeah, thanks for having us.

**Jeremie Elio Ontiveros:** Thanks for having us.

**As I was setting up interviews over the winter break, I actually had two goals. Number one, I wanted to do something about power generation generally. I think it’s super interesting and so that has been top of mind for 2026. I also needed to get an interview for the first week, and you guys dropped[this absolute gem of an article on SemiAnalysis](<https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power>). I immediately [messaged Dylan](<https://x.com/dylan522p>). I’m like, “Your name’s number three on this, who actually wrote this article?”, and it turns out, it was you two. So I’m super excited to talk to you about this. But before we get into [How AI Labs Are Solving the Power Crisis: The Onsite Gas Deep Dive](<https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power>) — that’s the title of the article — I want to hear more about you guys. Where’d you get started? How did you come to analyze this space? How’d you arrive at SemiAnalysis? Tell me your story. Ajey, why don’t you go first?**

**AP:** Sure. My name’s Ajey, I got my start in the municipal electric utility industry. So I was doing resource planning, Net Zero type work, program management for these very small utilities, “50-megawatt peak load, wow!”.

**You sound like me talking about money. I remember[I was talking to a guy who works in DC](<https://stratechery.com/2024/an-interview-with-gregory-allen-about-transforming-u-s-defense/>). He’s like, “Oh, they have this huge budget”, and he’s like, “$6 billion or something”, I’m like, “Wait, is $6 billion a lot of money?”, just totally warped by tech. It sounds like that’s happened to you with power.**

**AP:** Yeah. Every once in a while, if I want to wig out my friends, I tell them that the peak load of the city I live in, Burlington, Vermont, it’s 50 megawatts, and a normal data center is 10 Burlingtons, bam! So it’s a lot of fun. But I was also working [on a Substack](<https://www.energycrystals.io/>) on what is going on with the grid, it was very focused on New England, and Dylan found the blog. So from there, the scope of my research has expanded dramatically to really dig into the details of what is actually happening with the electric grid and I am learning an incredible amount at an incredible rate.

**Oh, that’s super interesting. Were you always interested in power? Has that been your career all the way through? Did you study that in university?**

**AP:** Yeah, I went to school for electrical engineering. And for me, the real turning point was seeing the news coverage for Hurricane Maria back in 2017. I was still on college, I have no connection to Puerto Rico, but I saw, “Oh, they’re pulling people out of retirement to get the lights back on, someone should do something about this”, and that was how I ended up in industry.

**Super interesting. Jeremie, tell me your story. You’ve been with SemiAnalysis a little bit longer, you have a great collection of articles. How did you get there? What is your background?**

**JEO:** Yeah, sure. I started in the finance industry, I started as a buy-side analyst, so used to basically cover equities on the loan-only side with the typical purpose for buy-side analysts, which is, “Let’s try to find stocks that are undervalued that have a high potential for long-term investments”, all the typical stock picking stuff. As a buy-sider, I was covering mostly industrials energy, it was pretty broad-based, I was mostly a generalist, but over the last, I would say roughly three to four years, I’ve been covering increasingly the semiconductor space.

In Europe, we have a few champions, we have STMicroelectronics, we have Infineon, we have Soitec and just as part of my research, I discovered SemiAnalysis, which I was like, “Whoa”, this guy is really good at the detail stuff we don’t see on typical sales side reports when you’re on the other side. That was mid-2023, and so basically I saw Dylan post on Twitter saying, “Hey, now I want to build a real business”, back in ’23, he was basically alone, was still a personal blog. I think he just had hired his first person mid-’23, [that was Myron](<https://semianalysis.com/myron-xie/>). And yeah, so he posted on Twitter, “I’m looking for people”, I reached out, joined the company early 2024. We were just seven when I joined, now we’re over 50, so it’s been a pretty crazy ride.

Here at SemiAnalysis, I launched a little research team on all the physical infra side of things. SemiAnalysis historically has really focused on the chip side, obviously, SemiAnalysis, semiconductors. We’re the best at understanding what’s the architecture of GPUs, TPUs, Nvidia, Dylan has been following the industry for a while. But what we realized pretty early on, so early ’24, we had this article called [AI Energy Dilemma](<https://newsletter.semianalysis.com/p/ai-datacenter-energy-dilemma-race>) where we actually quantified what’s the energy demand related to AI data centers and we took a pretty different methodology from what you typically see on this industry.

Oftentimes you see people making just CAGRs like, “Hey, let’s assume 10% or 15% year-over-year growth”, what we thought is, “Hey, let’s wait a second, all of this is driven by a completely new technology and their growth curve is not linear, it’s not progressive, it’s actually all at once”. It’s Nvidia doing whatever, $5 billion of GPU sales per quarter and suddenly saying, “I’m going to do 14 next quarter”, that was the famous quarter in May 2023 or something and so that growth curve looks exponential. So we thought, “Hey, let’s multiply our proprietary forecast of how many chips are shipping in industry and look at what’s the power for each one of these chips”.

**Right, back that into the power requirements, that makes sense.**

**JEO:** And back that into the power requirements, and the figures were just astonishing.

So I’ll give you a bit of context. If you analyze the historical trends on the data center side, you’re looking at roughly 2019 to 2022, roughly four to five gigawatts of capacity added per year, that’s all-inclusive. Social media, cloud computing, internationally. So Europe, US, China, all of it, four to five gigs a year and when you back out the math I just described earlier, 2024, Nvidia alone shipped five gigawatts, Nvidia alone doubled the size of the industry.

Essentially that’s when we thought, “Hey, we need to actually track down the physical supply chains to understand if this is even possible from an infra perspective”. The first step was, “Let’s track the individual data centers”, so we went on this crazy journey of tracking thousands of data centers. And today, this is the [data center model](<https://semianalysis.com/datacenter-industry-model/>) where we have this intelligence of where the hyperscaler was building, how fast, “How many megawatts are they building each quarter?”, the neoclouds as well. We look at all the major players building infrastructure, we look at the end users, our goal is to understand who is also deploying that power, who needs that power, try to quantify how much does OpenAI want, Anthropic, Google, DeepMind, all of that.

And the thing is, once you start going through that rabbit hole, it just never stops, because everything is interconnected. So after begin tracking the data centers, we though, “Hey, we need to get smarter on electrical and cooling systems”, so about a year-and-a-half ago, you saw on SemiAnalysis, I wrote a pretty comprehensive [piece on electrical systems](<https://newsletter.semianalysis.com/p/datacenter-anatomy-part-1-electrical>), then on [cooling systems](<https://newsletter.semianalysis.com/p/datacenter-anatomy-part-2-cooling-systems>). What we realized is, “Hey, just by looking at satellite pictures, you can actually tell a lot about a data center”, there’s a lot of things you can tell, and we just kept going deeper and deeper and deeper. Then we thought, “Okay, there’s just too many things we got to track, let’s build a real team”, so now our data center energy industrial team, we’re what, seven people. We’re lucky to have five analysts full-time and also two persons on the data side helping us track all of those indicators, it just never stops. And so the goal for us is really to expand that team as much as possible and to basically help people in those traditional industries that have nothing to do with tech understand what’s actually driving their business.

**I’m just curious, just from a business perspective, who are the customers for this group that either are reading you or need to be reading you?**

**JEO:** Half investors, half corporations. Look, at the SemiAnalysis level, the first customers that we found obviously were on the tech side because we come from the tech side. Hyperscalers, they want competitive intel, they want to understand what their competitors are doing, they come to us, AI labs as well.

And then over time, we started getting more and more new types of customers. On the investor side, we used to have only the semiconductor investors, then we started to have the overall tech investors because we realized by tracking the data centers, we can actually have the best intel on what Microsoft is doing, what Amazon is doing, what Oracle is doing and we’ve had some successful bankers where we predicted, for example, the Amazon growth rate acceleration in Q3, or we talked about the Microsoft path way before anyone, because by looking at all of these indicators one by one, data center by data center, you get the best intel on what’s going on in the market, and now we’re increasingly getting into the industrial space.

**Quick question on that. So this makes me think of, I remember the early iPhone years, Apple was super predictable in their results and the reason they were super predictable is because as they were signing up new carriers around the world, those carriers all had guaranteed purchase amounts, and so they actually knew exactly how much capacity they were adding quarter on quarter. Then I remember, I think it was the first quarter after China Mobile and NTT Docomo came on where they basically had everyone, their forecasts were totally wrong and they were all over the place for a while because they had to realize, actually, we don’t know how to forecast this very well because it’s not as predictable as it could be.**

**The reason I think about this is you talk about this looking at data centers coming online, has it been a situation where actually results are very closely tied to that? And is it just a situation where as long as it’s a validation that demand does exceed supply because you can measure the outcomes by knowing the supply and that’s just going to be the case until that sort of balances out?**

**JEO:** Yeah, exactly. So if you take a side step back, how do people typically forecast growth for Amazon’s cloud business or Microsoft’s cloud business? The typical way is doing surveys. It’s doing a survey to a hundred CIOs and be like, “Hey, this year, do you plan to increase your spending on Microsoft Azure or lower your spending?”, typical Gartner service. That works decently, sometimes it works, sometimes it doesn’t. But now we’re in a different world where essentially anytime you have a shell that is powered, and that’s important because when we think about the power shortage, we’re going to talk about that in more detail, of course, but it’s not just the power itself, not just the energy, it’s actually building an operational data center, that matters a lot and at least in this context, once you have a power data center, you can actually have a very clear sense of how much revenue that can generate.

And look, to be perfectly clear, the reason we can do that is because SemiAnalysis, we track all aspects of the supply chain and because we understand a bit of materials of a chip, we understand how much it costs, because we understand at the value add layer what the different clouds are doing, what are the different services that are offered by the industry, you can understand the revenue-per-chip, you can understand the revenue-per-megawatts. So we love to do these indicators in terms of many different things, so per chip or megawatt or whatever but essentially, anytime you have power, you can predict what’s going to happen with revenue, at least in this current market shape.

So far, that has played out very well, we’ll see. Currently, we don’t have a way to think that this is going to change the next few quarters, next few years, but obviously at some point, this is going to get solved.

**Well, for it to change, the supply is going to have to exceed the demand and I think a big theme that we’re talking about is that’s nowhere close to happening just because there’s so many constraints on the supply side.**

**JEO:** And an interesting caveat on this is that you could argue, hey, maybe the constraint is going to shift, maybe it could shift to chips.

**Yeah, I have a question about that. Memory or CoWoS, or whatever might it be.**

**JEO:** And memory, storage, all of that, so the constraint could shift definitely. But what’s really interesting here is that on the data center side, you have the longest lead time, it takes much longer to procure a chip. This changes if we get to a constraint where we need to build a new fab, that would be the next level, we’re not there yet. So currently, the constraint is data center or energy, and those are very long-time items, so we can have a very good sense by tracking those one by one of what’s going to happen next year, what’s going to happen in the next 18 months. Currently, it’s working out pretty well.

#### The Power Shortage

**You mentioned the expanding beyond tech into other sorts of investors. When did this become an issue in that not just they’re subscribed to SemiAnalysis, but just in general, people started to wake up to this fact that there is this real crunch coming and we need to start thinking about it. And what are the drivers in terms of thinking about it? How does supply/demand work when it comes to power generally? What is the response, and is that response happening?**

**JEO:** I’ll give you a data point I think is quite interesting. If you think about the chip side, the first time you saw that massive acceleration was Q1 2023 when Nvidia basically shocked the world by saying, “I’m going to accelerate by whatever”.

**Right. ChatGPT, yeah.**

**JEO:** Yeah, that was crazy. Then investors were starting to think about, “What are the other things that are going to be impacted by this?”. I would say it really started in ’24. In ’23, Q3, ’23, actually, you had Vertiv, so it’s a data center equipment company, they sell electrical equipment for data centers, cooling equipment for data centers, they’re a critical piece of building a data center, and they reported a surge in orders quarter over quarter, and a surge not as extreme as Nvidia, but something in that order and so that gives you a sense of the lag.

So initially it happened with the chips, then it started impacting on the data center side and I think 2024 is when over time, people really realized that there are a whole bunch of other areas. So if you look at the stock market, you can just see the stock prices of GE Vernova exploded in 2024, Talen Energy on the utility side, this is an interesting one as well, but basically the asset owners in the regulated markets that are not fully hedged are benefiting tremendously because power prices are going up because the value of their assets are going up. And so you saw Talen Energy, Constellation, Vistra, the IPPs, as we say, independent power producers, their stock went up tremendously as well in 2024. So over the course of ’24, it began to happen.

I think generally speaking, some of us were pretty early. So early 24, we had [that big paper quantifying the surge in demand](<https://newsletter.semianalysis.com/p/ai-datacenter-energy-dilemma-race>) and to us, it’s been interesting to see how the other organizations have changed their forecast over time. The forecast we put out early ’24 looked crazy. We we’re saying, “Hey, AI is going to be this way in two years”, people were saying, “You’re crazy, it’s not going to happen because my model says it’s going to be 20% year-over-year growth”, but no, it’s a new trend that really is net new essentially. It’s just this new buying of Nvidia, it’s not incremental to buying Intel chips that make up cloud data centers and social media data centers and if you look at Nvidia revenue growth, it just went up so fast, so part of the money went up also incredibly fast.

**Which of the cloud providers was earliest to seeing this?**

**JEO:** Microsoft.

**Interesting, tell me about that.**

**JEO:** Microsoft, no doubt whatsoever. The one way you can think about this. So first of all, Microsoft did a billion-dollar investment in OpenAI in 2020, so you could argue they were really early, but then early 2023, Microsoft signed that $10 billion investment check with OpenAI so that was already a sign that Microsoft was betting pretty hard on this.

**Right, and so they saw it from the usage of OpenAI, they were first to see what’s happening with ChatGPT. So they just go out and start buying power everywhere?**

**JEO:** Yes. So one indicator that I think is really fascinating, if you think about leading indicators that you can gather from the data center side, there’s two things you can think about. One is a data center can be self-built, self-operated, or you can rent a data center from another operator, it’s called the leasing market for data centers.

On the self-built side, we track construction stocks, so who’s starting to build new data centers? Again, takes a year, a bit more than a year to build it from first stone until you think operational. 2023, Microsoft really began to start construction everywhere, all around the US and internationally as well, other folks were a bit slower to react.

On the leasing side, I think it’s even more shocking. So leasing, maybe you’re familiar with folks like QTS, Digital Realty, Equinix, these people that have been building data center for a while, been working with the hyperscalers for a while. The leasing market in 2023 had an essentially insane year. To give you some numbers, and Microsoft was essentially the single driver of this, Microsoft alone leased over 60% of the total capacity in 2023. In Q3 2023, Microsoft leased two gigawatts, that’s as much as the total amount leased in the whole year 2022 in North America.

So really, the scale of what Microsoft did in 2023 was absolutely astonishing. And if you think about it from, let’s say revenue perspective, you can also see that they were the first to really accelerate on the cloud side. You saw Microsoft Azure really accelerate towards the end of ’24 and early ’25, and that’s because of the decisions they took in ’23 and ’24.

**So who was the laggard, if anything? I guess the other ones to think about would be Meta, Amazon, and Google. Oracle’s obviously coming along, trying to make a big play here. Are the rest of them all in the same boat or are there any of them that were late to the game and are going to have problems now?**

**JEO:** They all recognized the issue at the same time if you just look at whatever official statements and CapEx projections and things like that. But in practice, they were later.

So Meta is interesting, Meta was really caught by surprise and this is really interesting from the data center side because traditionally the Meta data center, it looks like an H, it’s the thing they’ve been building for the last 10 years. First one in Prineville, Oregon, they’ve repeated that design in many other locations. 150 megawatt per campus, five buildings, big stuff. But the problem with that data center is one, it’s fully air cooled, it’s really tough to do liquid cooling in that data center. A second thing, more important, takes over two years to build, two to two-and-a-half years to build, it’s a complex structure, three stories, takes a while.

So basically they realized they have to make a hot pivot if they want to accommodate all of that GPU load that is suddenly coming and so [we had a report about that](<https://newsletter.semianalysis.com/p/meta-superintelligence-leadership-compute-talent-and-data>) where we showed they had a data center under construction early stages, they demolished that data center and they completely changed the design to build a new one. But because they were so late with regards to the state of their infrastructure compatibility with AI, it took them a while to get that capacity operational.

So you really started seeing Meta get more capacity towards the second half of ’24 and be much more active towards second half of ’24, generally speaking. So now they’re very much in, but they were late. Amazon, generally speaking, was also late. Google, I would say, was slightly late as well, but less than the others, that’s your rough ranking.

**Tell me more about why it’s hard to, you referenced it with the air cooled versus liquid cooled, but why is it hard to repurpose data centers from traditional serving to AI serving and why the AI data centers actually end up being new ones?**

**JEO:** So we can use that Meta example, I think it’s a pretty interesting one. The design pattern with their old data center was let’s make it as cheap as possible, essentially, especially from an energy efficiency side. So there’s this ratio, it’s called PUE [[Power Usage Effectiveness](<https://en.wikipedia.org/wiki/Power_usage_effectiveness>)], it multiplies the amount of power that you need for cooling and all of that. So the total amount of power that you need, including cooling, divided by the IT load. Anyways, that ratio for Meta was the lowest in the industry. They built the most energy efficient data centers in the world, but the drawback was that they had to build this fairly complex structure.

The way they do it essentially is they take air from the outside — you could argue they open the window, that’s their cooling system — they open the window, they spray some water in the hottest summer days, there’s no compressor, there’s nothing and then the exhaust is basically also opening the window with a bunch of fans. Super efficient but if you need to cool a liquid cooled chip, well, you have no piping, you have no fluid cooling system. It’s opening the window, closing the window so if you need liquid cooling, you just can’t do it, essentially, so that was the main issue.

The second issue is also because they were prioritizing efficiency, they build this complex structure and so it’s not about the data center itself, in this case, it’s more about the time to build. In AI, everything goes so fast so you just need to change your design order to be able to build it faster. If you have 500 megawatts sitting idle, you’d rather be able to build a shell in nine months than in two years.

#### Grid Challenges

**You wrote at the beginning of the article, in Texas alone, tens of gigawatts of data center load requests pour in each month. Yet, in the past 12 months, barely more than a gigawatt has been approved, the grid is sold out. Texas is interesting because they have their own grid, but I assume, Ajey, that this statement holds everywhere, this is a universal problem. But then again, you also mentioned this gridlock issue. Is there no more power or there’s a gridlock in getting it hooked up? What’s the balance there in bureaucratic holdup versus there literally is just no power available?**

**AP:** I’ll start with the interconnection, then we can get to the underlying infrastructure. With the interconnection queue, when you’re applying for interconnection to the electric grid, it often starts with the distribution utility. So in a Texan case, it’s CenterPoint or AEP Texas, and then that gets run through a process of, “Okay, is there going to be generation capacity, transmission capacity to serve this load at this point if we run these simulations on worst case scenario A, B, C?”, and that load study is coordinated between the distribution utility and the transmission utility and the grid operator, which are in some cases, three different organizations.

And so that process, quite complicated, a lot of math, requires a proprietary model to put together and sometimes with the current pace of interconnections, by the time you have that interconnection study done, a few more projects have already come online and you have to redo the interconnection. Additionally, with the particular graph on our site in terms of tens of gigawatts of new load coming in per month, a lot of that new load request is speculative.

**That sounds like a similar issue in semiconductors. People are just ordering a gazillion chips and they may or may not take them.**

**AP:** Yes. And the specific structure I’ve heard is you’ll get, for lack of a better of a term, a yokel with a hundred acres of land. Yeah, there’s a transmission line near there, there’s a gas pipeline here, sure you can put a data center here, just someone else bring the capital and technical expertise. And so there’s a lot of noise in, especially the Texas interconnection queue because it’s the gold rush and we have not yet found the process for clearing out a lot of that noise. That legislation is coming, for example, there is the [Texas SB6](<https://legiscan.com/TX/bill/SB6/2025>), which covers a lot of pieces, but one of them is in requiring some extra disclosures on the interconnection side to weed out a lot of these speculative or uninformed interconnection requests.

**Got it. But is the long and short of it that there is power out there, it’s just right now we’re stuck in actually getting stuff hooked up because of the application system’s getting overloaded.**

**AP:** There is also constraints on the hardware side.

**JEO:** The way we put it is it’s sort of a prisoner’s dilemma. If everyone could coordinate, we could all find power in a more easy way, but because everyone is spamming the utilities all around the country, actually all around the world, it creates this vicious circle where because you have requests everywhere, you need to put requests elsewhere because you don’t know if you’re going to get one in this location, and so it just only gets worse. And so that’s why you’ve seen this crazy behavior where every state has seen tens of gigawatts of data center requests for every month, which is insane because if you aggregate the number or total number of data center requests close to a terawatt in the US alone, which for context, the peak load in the US is 750 gigawatts, so we’re saying we are requesting more than double that!

**So a lot of those are fake, yeah.**

**JEO:** Yeah, they’re fake, and it’s just not possible, the US is not going to be able to handle all of that. But the reason they’re fake is that prisoner’s dilemma where because of that behavior, and it goes back to the way the grid is designed where we have these transmission constraints, it’s very complicated to interconnect. And also the fact that the grid is meant to serve all of us, all the people that live in the US, 300 and whatever million people, we got to make sure they’ll have lights always on and because of AC power, everything has to be always perfectly in sync. So if somehow a disruption happens at the point of interconnection, especially at gigawatt scale, you can have a blackout.

**Well, tell me about this. You wrote a really interesting article about this, about how[training in particular causes problems for the grid](<https://newsletter.semianalysis.com/p/ai-training-load-fluctuations-at-gigawatt-scale-risk-of-power-grid-blackout>). Can you explain that?**

**JEO:** That was the first collaboration between Ajey and I a few months ago. Yeah, so it’s two things. So on the training side, what happens is that the load is very volatile. You can think of it this way, a training job is going to be synchronous typically, especially when you think about pre-training a huge model. Where you’re talking about a massive supercomputer basically running calculations at the same time, which means there’s moments where you’re running MatMuls, you’re running matrix multiplications, you’re at peak power and then suddenly you do the checkpoints or you just sync because you have to sync all of these machines to sync the gradients and all of that.

So you have these millisecond periods where you can basically go from 100% load to zero. If you do that at gigawatt scale, you go from one gigawatt to zero in less than a second, that can blow up a whole grid, essentially. And we can give you the example of what happened in Spain last year, so I’ll let Ajey comment on this one because I think it’s a pretty interesting one.

**AP:** Yeah. So with Spain, so for context for everyone, back in April 27th, I believe it was, there was [a very sudden blackout for all of Spain and Portugal](<https://en.wikipedia.org/wiki/2025_Iberian_Peninsula_blackout>) and the ultimate takeaway from that is that the blackout started because there was an imbalance in supply and demand.

**And with renewables, that’s a real challenge because if you’re dependent on variable factors, wasn’t that part of the driving factor what happened in Spain?**

**AP:** It was part of the driving factor, but it was more a matter of the imbalance of you have one or two or have a small network of distributed solar sites kick offline, and all of a sudden there is more demand than supply. And because of the dynamics of the grid, that sends voltage on the overall grid up, up, up and then because there are over voltage faults on a whole bunch of new sets of generators, those trip offline. And then because the voltage keeps going, you get one more, one more, one more, and you get a cascade failure because supply and demand were not in balance. The initial spark could have been anything really and going back to the reports I read about that blackout, the initial snowball wasn’t recorded on the transmission grids or the grid operators systems, they didn’t see the initial trips offline.

**The point being it was pretty small. It wasn’t unusual.**

**AP:** It started small, and that blackout started with an imbalance in supply and demand. It can be caused by distributed renewable systems that are not tuned properly, but it can also, and this is what we argued in that report, is it could also be kicked off by either one of these large fluctuations for a data center, which in practice, if you’re looking at a gigawatt scale data center, you’re looking at fluctuations 10, 15%, that’s a hundred megawatts. That is two Burlingtons of Vermont on, off, on, off within milliseconds and so that’s one way you can get all of these imbalances and voltage, imbalances and frequency, and that can send cascade failures outward.

Or, and this is one thing that the grid operator in [Texas ERCOT](<https://en.wikipedia.org/wiki/Electric_Reliability_Council_of_Texas>) flagged, is that if you have what they call a low voltage ride-through event of classic outage, a squirral touches the wrong part of a wire, gets fried, and you’ll see an entire line go offline, and then an automatic switch will try and effectively zap the fault off, just bam, bam, bam. What loads in that area will see is the voltage on their meter just go down, down, down, and back and so a lot of these uninterruptible power supplies are designed to, if they see these dips in succession, they’ll click offline, go to their backup generators, “Clearly there’s something wrong with the electric grid, let’s stay out of this for a little bit”. If you are a gigawatt scale data center, all of a sudden you’re losing 600 megawatts, 800 megawatts, a gigawatt. And what ERCOT would see, and this is that their worry, is that if the wrong outage happened at the wrong time in the wrong part of Texas, you might see two-and-a-half gigawatts, 2.6 gigawatts of load trip off all at once and if all of that trips off at once, you see a spike in frequency that cascades across Texas.

**Oh, interesting, that makes sense. Yeah, because they’re like, “We’re backing out of the line, it’s unreliable right now” — actually that’s its own sort of acceleration event.**

**AP:** Exactly, and then you would have that same cascade effect similar to how it was in Spain of you have one fault, it propagates to two to four to eight, and then you lose the entire grid network, and a lot of these are engineering challenges. So in ERCOT, there is a dedicated working group to large loads, and that includes both AI data centers and also crypto miners, there’s increase in commonality between these two players now.

**Well, the crypto miners ended up being in a great position because they came in to take care of all this excess power capacity, they could monetize it and now it turns out that that’s really valuable to have some of those contracts.**

**AP:** Not only do they have existing powered land, existing interconnections that from jump were sized for a full-tilled system and not the variable load that a crypto miner usually is, but also a lot of these companies have staff who their energy person on staff used to work for ERCOT. They know the underlying grid infrastructure and they have people on the inside as well and so those crypto miners are really well positioned from a infrastructure basis from a tacit knowledge basis to interact with their local grid topographies.

#### Behind the Meter

**Well, we’ve been talking about the grid, but your article was about behind the meter. Give me an overview. What does behind the meter mean? Why is it so important? Why is this a huge deal? Why did this article, why was it so interesting that it made me want to talk to you?**

**AP:** So the electric meter is the point of division between what the electric utility owns and manages and responsible for and what the customer is responsible for.

So if we look at your house, for example, let’s say you have a house and you have an electric car and you have a solar system attached to your house. The solar system is behind your meter, it is not the responsibility of the electric utility and if your solar system generates power for your house, that is run directly to your house, the power does not cross the electric meter by default. And so when that solar panel is generating, what the electric meter sees is just a loss in demand. It can’t tell the difference between the solar panel generating and you just having an outage in your house and so at a house level, that’s the structure and you’re talking about solar panels and cars and power walls.

At an industrial scale, what you’re looking at is onsite generators and typically that’s been diesel generators as backup. But in this case, what we’re looking at is full scale power plants, gas turbines, reciprocating engine cells.

**JEO:** So the context here, and this is, if you read the intro of the paper, you’ll notice we talked about xAI many times, [they were pioneers here](<https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter>).

**That was one of my questions, was anyone doing this or thinking about this to the extent they are today before xAI suddenly showed up out of nowhere? We have this massive data center running[in Memphis](<https://x.ai/memphis>).**

**JEO:** No.

**AP:** It was Elon.

**Well, tell me about that. What did he do and how has that been the inspiration for this explosion that’s happening now?**

**JEO:** Yeah, so Elon basically thought from first principles like, “Hey, I want to be in the AI race, I’m behind, how can I build a data center faster than anyone else?”, and so it’s interesting because at that time, so that was early ’24, maybe late ’23, he was talking to a bunch of the cloud companies. He was talking to Oracle, for example, initially xAI was in touch with Oracle to take the Stargate site in Abilene, Texas.

People were telling him, “You’re going to get power in mid-2025”, so xAI thought, “I got to do something about this”, and they basically rethought the whole thing from first principles. Data center site selection, let’s not build a new data center, let’s find an existing site. So it’s an old, I think it’s like washing machine or appliance factory or something like that in Memphis, and then in terms of energy, they thought, “Hey, the grid is going to be too slow, so we got to generate our own power, we’ve got to do this fast”, so they thought about what is the best way to get power fast. It’s not going to be to use the utility scale turbines, those take a while to deploy, so he just talked to all of the vendors and he found a turbine rental company that had inventory, they had a bunch of turbines available. They wanted to rent them, told them, “Hey, can I get those? They’re pretty fast to deploy. Takes a few weeks. If you have them deploying them onsite and generating powers really fast”. He just thought that’s the simple fastest way to get energy on a new site, so that’s essentially the story, it’s just first principle, how can I build a data center, a GPU cluster of the 200, 300 megawatt scale as fast as possible, he did it in just four months and that was a playbook, self-made energy, [brownfield site](<https://en.wikipedia.org/wiki/Brownfield_land>).

**And now everyone’s like, “We should do that too, especially if we can’t even get power”.**

**JEO:** Exactly. So the funny thing is that you had two reactions to this. On one end, you had the traditional data center people who thought, “No, it’s crazy, my industry doesn’t work this way”, and so by that time I was going to a bunch of conferences and everyone was saying, “No, no one should do this, from a real estate perspective, it’s not the way to do it”.

But you had the other world, which is now taking an increasing share of the market is the AI world, the OpenAIs of the world, the Anthropics, all the AI labs, bveryone in the AI community thought, “Hey, Elon is a genius, that’s just the way we should be building data centers from now on”, and so what’s interesting is that as a share of, I guess the new build outs, AI labs went up tremendously and so now you’re seeing them being in the decision-making seats and them being the ones that are telling people how to do things, and that’s why you’re seeing the whole industry now adapt to that mindset.

**So what’s the downside of doing your own power onsite as opposed to connecting to the grid?**

**JEO:** Number one is cost. The great thing about the grid is that if you think about redundancy, about the uptime, in the US, you have four-nines, so 99.99% of uptime. And the way this is done is via the grid, is via one generator here, another one 20 miles away, another one 50 miles away, it’s all interconnected. When you do everything onsite, you have to build your own redundancy, it’s more expensive.

**And how important is redundancy for AI?**

**JEO:** Actually, that’s a great debate. In theory, for AI training, it doesn’t matter much. I would say it doesn’t matter because the GPUs themselves are actually unreliable so when you run a GPU cluster, you’re going to be at maybe two-nines of uptime so in theory, you don’t need it.

But the problem is, if you want to do something else with it, say you want to maximize utilization of your GPU cluster because as a company, that’s your single largest expense, then you want to be sure you can do as many use cases as possible with your data center. So maybe sometimes it’s processing some peak inference requests, maybe sometimes is doing some other type of training jobs.

As a general rule, if you manage a huge infrastructure, gigawatt scale, think like a Meta or like a Google, it’s best to have large computing centers that have high availability and can do many things at the same time. Anyways, all of that to say, uptime doesn’t matter as much as it used to in the cloud era, but it still matters, it’s still good to have more than two-nines.

**When Elon built this in Memphis, was his goal to connect it to the grid eventually? And is that still the goal for all these build outs that are happening, sort of mimicking his approach? Is the idea we just need to get it started because we can make money now or because the race is so intense, but this is not sustainable in the long run? Or is there a shift to actually, this is just the way we’re going to build data centers going forward?**

**JEO:** Yes, he had a path to the grid from the beginning, he requested to the utility the amount of power, which was 300 megawatts, he got it, but after a year. So this is called bridge power in this world, which is generating power onsite off-grid for a given amount of time and then, when you have a grid connection, you use the grid as main power source.

**How does that impact your choice of power for that bridge power?**

**JEO:** What you see in that case is traditional data centers for uptime have diesel generators as backup. And so, when you forego grid power, you don’t buy diesel backups typically. So for a while, you just operate without backup and whenever you get the grid connection, your turbines that you have on-site can operate as backup power.

In terms of equipment that you want to buy, you want to buy stuff that is useful for backup purposes. So, you cannot be too big, you’re not going to use a 500 megawatt turbine as backup, it just doesn’t make any sense and you want something that is fast, that is able to react to surges in demand. So if the grid has an issue and you need to turn on your backup generators or turbines, they need to be able to react fast, which we also do for certain types of systems. So, we talk about aeroderivatives or industrials.

**There’s a tradeoff here, right, between the efficiency of your power versus how fast it can turn on and be useful as a backup in the long run? But if that’s the case, you start out and you’re like, “Okay, we’re just going to get bridge power, in the long run, this power is going to be backup, so we want to prioritize this”. Is there a shift where it’s like, actually we’re not going to get grid power for a long time, so maybe we need to think about what this bridge power looks like in the meantime?**

**JEO:** That’s the conversation now, if you go back to that shot where you have the approval to energize and large loop requests, the worry is that it only goes one way, which is the grids get increasingly constrained. Increasingly, you’re saying, folks that were thinking we’re going to have utility power by late ’27, say, and suddenly they’ve been told now it’s going to be late ’28 or late ’29 or 2035 — the grid is increasingly unreliable, which leads people to essentially plan fully behind the meter data center.

**So, what is a fully behind the meter data center, what does the plan look like as compared to say what Elon did with xAI?**

**JEO:** Well, in theory, we want to have cheaper power costs, you want to have machines that can last for a long time so you’re going to use primarily utility scale turbines. So you go from those small modular turbines or engines to those large scale systems that we know for many, many years can run for whatever, 20, 30 years, generate power very cheap. So, H-class CCGT [Combined Cycle Gas Turbine], as we say, over 60% efficiency, that’s ideally what you want for base load power. And you’re going to need to manage your redundancy, and then the system is going to be a bit more complex.

To be perfectly clear, it remains to be seen because we haven’t seen any of those in practice today. All of the on-site gas power deployments today are for bridge power purposes, but from what we can tell here, our analysis of site plans, of permitting and all of that, we can already see that some data centers for say 2027 or 2028 are planning to just forego the grid and plan their own power plant on-site.

#### The Market Response to Power Demand

**When you talk about shortages, so okay, the grid’s running short, we can’t interconnect, there’s a shortage of bureaucratic ease, maybe is one way to put it. Does all this talk, if we’re shifting behind the meter, does that mean we now have a completely new vector of potential shortages, which is in these gas turbines or these utility turbines as people think, “Well, I’m just going to plan for the long run”?**

**AP:** Yes, there is increasing constraints on the production of all kinds of generating systems. So, the lead times for these H-class gas turbines is we’re seeing orders that will ship in 2029, for example. And then we’re also seeing lead times on these smaller modular turbines also go longer and longer and longer and also, the prices for these are going higher and higher and higher because the manufacturers, GE Vernova, Siemens Energy, know where they are and know they can take the extra margin. Those shortages are coming and we’re going to track them down further from not only the gas turbines and the engines, but also the material inputs and the switch gear and the transformers and there are all of these other bottlenecks on time to power.

**JEO:** There’s something that’s really fascinating on this topic, which is when we started talking about self-generation, about the need for more gas turbines, people were starting to freak out because GE Vernova was saying, “Yeah, I’m booked out in 2029”. So then the question was, “Where are we going to find even those systems? How are we going to generate the power?”.

Then came the engines. So, we’re starting using those low speed engines, medium speed engines, four context medium speed engines are based on the same ones that we use for ships, container ships or cruise ships. And what’s really interesting is that over the last year or so, we’re witnessing a huge wave of new entrants because everyone who can supply hardware to generate power, now this is an opportunity.

So, a few months ago, we had [Boom Supersonic and a 1.2 gigawatt deal with Crusoe](<https://boomsupersonic.com/press-release/boom-supersonic-to-power-ai-data-centers-with-superpower-natural-gas-turbines-adds-300-million-in-new-funding>), and it’s like, okay, this company that builds turbines for supersonic jets now thinks they can in play in the AI data center game, and this is just getting started. There’s a bunch of other companies that are, that we fully expect to get some orders and that are also leveraging new techniques.

**Right, that’s what I was curious about because this whole chain, it’s like there’s massive demand so you would expect sort of a response in supply and that’s sort of where the initial wave is coming from. It’s people who make engines that weren’t usually used for power generation, it’s like, look, an engine is an engine, it could be used for this.**

**JEO:** Yeah, exactly, that’s the supply response. So, you have, Pro Energy is an interesting one, they’re basically finding old jets of Boeing 747, if I remember correctly, and they’re retrofitting the turbines that you have on these jets and using them for power generation. That’s just one example. And if you think about where are we going next? Hey, there’s other sources of power. Maybe someday we’re going to be using car engines. Or maybe that’s too crazy, but big trucks or trains, there’s still a lot of sources of power that we can use to generate power.

**Well, the 747 is retired, amazing plane, but by-and-large gone because it wasn’t sufficiently efficient. Now, some of that efficiency comes down to the design of the plane itself, but a lot of it is about the engines and is that just not a concern at this point? It’s like, look, we’ll take power however it comes, it doesn’t have to be the most efficient. Of course, ideally we would want something different, but the demand and the opportunity is just so large that all those concerns are sort of by the wayside.**

**AP:** The dirty secret is that the turbines that GE Vernova sells, those small modular turbines, are the exact same engine class.

**I have a friend that works in the energy in this space and the first time he described to me, he’s like, “Yeah, I basically work on the same jet engine that is in planes”, it blew my mind. I’m like, “Oh, that’s amazing”.**

**AP:** It is the exact same thing.

**It makes a lot of sense once I think about it.**

**JEO:** So look, the way to think about this is, what’s the revenue you can make per megawatt? And when you look at the folks like the Oracle’s, the CoreWeave’s of the world, they buy a bunch of GPUs, they rent them through the cloud, the revenue they’re making is roughly $12 billion per gigawatt per year. It’s just such an amount of money that you can make so if you can get that six months earlier, there’s basically no impact if your power costs are higher.

And so, another way to think about this is what’s the cost to run one of these GPU clouds? And the cost is basically, it’s all about hardware, it’s Nvidia’s gross margin, it’s basically your Nvidia system, if you increase your power cost by 2x, it’s not that much of a problem.

**That’s super interesting. So, should we expect to see a knock-on effect going forward in, say, container ship building or in jet engine building? I mean, there’s massive backlogs for jets as it is, is that going to get worse?**

**JEO:** Yeah, I think that’s sort of the next step, which is at what moment does all of the crazy stuff that we do for AI infra impact the broad economy? It’s already starting to happen.

Another example, we haven’t talked about the labor shortages, that’s a pretty common issue in the data center. People talk about we cannot find electricians, we cannot find plumbers, then the flip side of this is if data center operators are basically taking all of that labor pool, then who’s going to be building houses, hospitals or industrial facilities? So, yes, that’s sort of the same direction, which is stuff that is going to be used for other purposes, now we want it for AI, and people in the world of AI have more money so it’s the arbitrage here.

**AP:** And for me, this is where it gets exciting as an ex-grid guy is that when I was working on the utility side, I was thinking a lot about how do you make Net Zero happen? And that’s a very expensive proposition. What we were starting to get a sense of by year 2020, 2021 was that it was not going to happen with current spending and so a lot of these transformations of the electric grid just weren’t going to happen in time.

Enter AI, and all of a sudden you have this new influx of not only capital, but willingness to try new things, and all of a sudden, all of these hopes about rebuilding the electric grid in a way that solves 40 years of deferred maintenance, it’s happening now. And that for me is the very, very exciting side of things of all of these really cool new technologies, really cool new ways of approaching things, new institutional designs, this is happening.

Going back to these models of on-site power, we’re building what would’ve been called micro-grids, but at a much larger scale than the Net Zero guys were really talking about. This is exciting to me, this is the new stuff.

**Right. But the question is, does that ever actually — is the long-run future, you have all these individual islands and powers sort of very dispersed as opposed to the current system that you were talking about before where it’s all centralized, and you get the benefit of everyone sort of helps each other and you get a lot of redundancy for free, is that world just disappearing and we’re going to end up with all these islands? Or do we end up with all these islands and maybe in the future the islands sort of reconnect to each other?**

**AP:** Potentially. We’re now seeing a lot of development on, for example, DC connections between — so for example, a lot of the interconnection between larger grids so between say New England and Quebec, those are DC lines, in many cases. That’s a newer technology that didn’t exist 40 years ago that now is usable and you can use it to connect otherwise de-synchronized grids.

**They don’t need to be in perfectly in balance if it’s DC.**

**AP:** They don’t need to be in perfect balance, although it helps. There are a lot of these new technologies, and I don’t know necessarily if a whole bunch of islands connected together with DC lines will work as well, but it is worth a shot. And from my personal experience, the utility industry has been very slow to adopt new ideas and challenges.

**Well, that’s the big thing, right? It’s like, maybe it’s not perfect, but at least it’s getting done. I think people worry about the power question — it’s like, well, to the extent that this requires bureaucracy and regulatory bodies, there’s despair that nothing’s going to happen. But it sounds like what’s basically happening is wherever there is space, whether it be sort of at a Memphis refrigerator plant or whatever it might be, stuff is going to happen and we’ll sort of back into whatever’s next. Is that how the hope that there’s a massive new electrical build out because of AI that is broadly beneficial, that that’s going to happen?**

**AP:** Yeah, and also it’s going to be a matter of seeing which institutions, which organizations really step up. We’re seeing a lot of good work coming out of some companies, especially Georgia Power or AEP and Dominion, they are really showing they’re up to the game and they have good forecasting, they have good capital plans, they’re showing what is possible. And to the extent that these plans work out, okay, here’s a new model or here’s a revised model to follow and so for me, it’s exciting being at the laboratory of new ideas in electrical service, and some of the ideas are a little wackier than others, but it’s exciting to see even the wacky ideas get tested out.

**JEO:** One thing I would say, Ben, is I think it’s interesting to compare US and China for a bit. One meme that often comes up is that China is way better than the US as building power because if you analyze transmission build out, the number of transmission lines on a mile basis has been going down for a while in the US, whereas it only goes up in China. And if you think about why is that happening, it’s because in China, it’s much easier to invest in a huge transmission project because the country is still very early, so it’s easy to project rise in energy demand.

**Right.**

**JEO:** Whereas in the US, it’s just not possible to build a massive transmission project that is going to help everyone just because there’s no uptick. Over the last 20 years, power hasn’t grown. It hasn’t been powerful.

**They actually slightly decreased, right?**

**JEO:** Actually slightly decreased.

**Yeah.**

**JEO:** This is one way you can think of it, there’s two ways you could see this playing out. One is, okay, data centers, let them do their own thing, let them bring their own power.

But another way you could think about this is, data centers could actually contribute to making a grid better for everyone because now you have uptick. I would argue it’s already starting to happen to some extent. You’re seeing in Texas, it’s been a while, but we now have a 765 kV project so ultra-high voltage projects, the first 765 kV line we’re building since, I don’t know how many decades. It’s pretty exciting to see that we’re starting to see, again, some huge scale transmission projects getting built that’s going to enable a lot of new things.

Because if you think about, for example, let’s imagine at some point the question of the energy transition is going to come back. One of the big issues you had when we’re talking about building more renewables was transmission, there’s no transmission, it cannot interconnect, and now if we start building that next generation transmission system at much higher voltages, it’s going to be much easier for these new types of generation to come in and to rethink the whole thing. So I think there’s actually a future where the grid is really part of it, and data centers benefit everyone on that side.

**Is this going to be one of those things where, is this sort of going to happen — let’s say[there is a bubble](<https://stratechery.com/2025/the-benefits-of-bubbles/>) and the bubble bursts, and now you have all these stranded power units sort of over the place that are not necessarily being utilized. Is that then going to really kick into gear this idea of building new transmission because there’s power deployed, but it wasn’t ever connected, and now it’s like we get free power if we can just build a transmission line?**

**AP:** Potentially.

**JEO:** Historically, when you look at these cycles, it’s always this way, right? It goes up a lot initially, then it goes down quite a bit. But if this is really a mega trend, which obviously we think it is at SemiAnalysis, it’s going to keep going up and up and up, it’s going to have cycles, there are going to be a down cycle in whatever, two years, three years, four years, five years, who knows? But there’s going to be an upcycle again and it’s going to be way stronger.

So the point is, yes, maybe there’s going to be some struggles to build more infrastructure at some point, and there’s going to be a period where our existing assets are underutilized. There’s going to be this digestion period where people are going to be happy to find existing assets but the long-term solution, if this is real as we think it is, is only going to be to build more infrastructure.

As we go, and if we think about what’s the next upcycle going to look like, this industry is going to be much more established, but we’re going to have much more visibility into who are the big players, how much capital do they have, what are they financial resources? So for everyone in the market, it’s going to be way easier to finance a multi-year transmission projects. Whereas today, that’s always the issue is when you want to build these massive upgrades, a lot of people just don’t understand this on the utility side.

**I think it’s so interesting, I think you tell a very compelling story, because you think about how do you increase electricity and increase the grid, most people start from a supply side mindset. We have to build the plant and we have to build the transmission line, and what’s happening here is you have this massive increase in demand such that the people who are generating demand are taking it on themselves to bring on their own supply and then, once that supply is on, that will naturally lead to, well, look, we could build redundancy for our one gigawatt data center, or the data center providers are thinking we should work together because we can actually help each other out in this redundancy perspective, and suddenly you’re building a new grid and it’s all coming from the demand side as opposed to the supply side.**

**JEO:** You could argue, I guess to some extent, history of humanity, that’s how we built the railroads, that’s how we built all our infrastructure. I would personally think that’s the way it’s going to happen because at some point, we’re just going to realize now that we understand that industry better, it’s just way easier to pour capital into it and to coordinate and to create the best outcome for everyone. So, yeah, pretty optimistic.

#### Energy Sources

**It is exciting, but everything in your article is mostly about natural gas. Where do other energy sources fit in this, or are all those just too slow to even matter?**

**JEO:** First of all, our article is mostly about what’s happening in the next roughly two to three years, it’s shorter, what are people actually doing right now to power their big data centers next year or in two years? If you think about that, there’s actually no alternative — this is a bit of an exaggeration. You can do more geothermal or whatever, but generally speaking, you need base loads, you’re not going to have base load with solar. You could, but it’s going to be super expensive, you have to be a monster solar power plant, overbuilt, whatever.

Anyways, the point being, gas for these next two years is the best. Then what’s going to happen next, you have nuclear, a lot of people are excited about nuclear, the problem is that no one knows if nuclear is going to be a 2029 story or 2035. There’s a hope, but the one thing that we know pretty much for sure is that it’s not going to be next year, it’s not going to be in two years, so in that short term window, nuclears aren’t there. Solar is the one that some folks are pretty excited about, but we need base load, we’re adding net new base load, we need power that is always on. Solar is in West Texas, best case scenario, 30% on, on average.

**Right, you need battery installations or some sort of storage mechanism.**

**JEO:** Yeah, gigantic batteries, or a massive overbuilt of solar. And another way to think about this as well is, if you want to build solar to power a data center, the complexity of that is actually pretty high because, say one gigawatt data center, typically what you see on acres-per-megawatt for solar is like five to six so you need to find 6,000 acres of land, or even more if you’re going to overbuild, so it can be over 10K, it’s just complicated. It’s just easier to just build turbines on-site and get started in the next couple of months or a couple of years.

**Is it better for solar, if you’re thinking back or just thinking about how the grid is going to develop — you mentioned actually at the very beginning, houses with solar on the roofs, is it one of those things where that is actually going to be where solar plays a role in this overall build out, that it makes more sense for a consumer, it matches the energy consumption cycle of a typical house by and large. And this baseline, there’s going to be a separation between consumer and industry, or is that really not viable? Everything needs to be all together?**

**AP:** I would argue that solar doesn’t necessarily fit the use case of a house. If you look at a load curve of a house with a solar system on it, you see it goes low, high, low but with the solar system on that, you get low, a peak around 8:00 AM, 9:00 AM, then a dip, and then it spikes again around 5:00 or 6:00 so it doesn’t exactly meet it. And even with the battery, you still have that same issue of getting enough solar and storage to match your whole home load without having outages for 1% of the time, 2% of the time. That last 1%, 2%, getting from one nine to two nine, to three nine, that’s really the hard and expensive part, and it’s the same issue on the consumer side.

I think eventually we’ll get there, but it’s a much harder optimization problem, because you also have to model out — it really depends on how much sun you have, how much precipitation you have, how much that changes year over year and it becomes a much more challenging modeling problem to get it down pat. Versus with gas, you have to check if you have enough gas in the nearby pipeline.

**Yep, a much simpler problem. You mentioned the US-China link up here. Is all these issues, are they common around the world? Is there a story where actually a lot of these data centers are going to end up in, say, in the Middle East, just because it’s easier to get this to market? Or are there different stories in different places or is it the same story everywhere?**

**AP:** It’s a little bit different everywhere.

**JEO:** I would say there’s different stories in different places. There’s one overarching theme, which is all of the places where we’ve typically seen a lot of data center load, they’re all increasingly constrained. So in Europe, you typically see data centers in Paris and London, Frankfurt, Amsterdam. In Asia, you see that in Tokyo or in Seoul, or in Singapore. All of these areas, the grid is basically overwhelmed. They’re not growing particularly fast either because demand is also fairly strong so the overall theme, which is to build a data center, you need to go closer to the energy source, that’s happening worldwide.

Now, going down the path of onsite gas, I would say today is still very US specific, there’s a few other examples. Ireland is an interesting example where they also do on-site gas but in the macro scheme of things, in terms of large scale build outs, it’s really USA is very specific on that onsite gas part of things.

**And is that because our demand is so strong, people are more aggressive or because we have a lot of natural gas?**

**AP:** It’s a shale story, I would say. One thing about West Texas in particular is that a lot of the gas production you have in that area is what’s called [associated gas](<https://en.wikipedia.org/wiki/Associated_petroleum_gas>).

**Right, you get the oil and gas coming out together.**

**AP:** You have a shale oil well and you get the gas coming out and it’s so cheap that in some places it is actually more cost-effective, it’s burned off the top, it’s not worth bottling up. There’s a particular hub in West Texas, the Waha Hub, which for a few years now has sometimes traded at negative prices, you’ve literally been paid to take gas out of their hands because they can’t get it out fast enough.

And so, in that context, this is why natural gas prices in much of the US have been very, very cheap, is because in many cases that gas is a waste product, US storage is a very specifically West Texas story. That is why you see especially a lot of focus on on-site gas in Texas, because you’re right where the permeant shale fields are, you can get extremely cheap gas even by American standards. Whereas, for example, in Ireland or in Asia, you’re looking at liquefied natural gas and it is three, four, five times as expensive.

**JEO:** Before talking about gas, and I think you were right talking about demand, because that’s actually the main thing is the people who want to build data center, they build in the US first. If you think about why, it’s the largest market on Earth by far. Nowhere else in the world do you have as many data centers as in the US, the companies are all American, they like the country and so, generally speaking, you just see people building much larger stuff.

There’s also an interesting thing, which is from a training point of view, the infrastructure build out today is still more training weighted than inference and from a training point of view, it’s advantageous to have data centers that can be connected through earth, because across Atlantic or across Pacific fiber is very, very expensive, whereas laying out fiber on earth is much, much cheaper. You can basically have unlimited bandwidth between location A and location B. So there’s actually a flywheel effect, where because big training data centers are in the US, it’s easier to put new big training data centers in the US.

**Interesting. And those big training centers, I mean, when does the shift happen to inference being the primary driver and does that change? You talked about how training has these weird cycles in terms of power usage, does that change any of this story or not really?**

**JEO:** You have to go back to what’s the underlying driver, which is the famous scaling laws. Why are we doing all of this investment? It’s because we think the more we invest, the better the product’s going to be. There’s very strong empirical evidence that that’s happening. In other words, if you invest today, next year you’re going to have a real revenue accelerate because your product is better, because you’re investing today.

So if you apply that mindset, I think it just only goes one way, which is until we’ve reached the limits of scaling laws or until we reach a point where we cannot monetize the investments that we’ve made on a certain year, no one has any incentive to store their own training. This is basically the way this has the bubble unfolds, is at some point we all invest like crazy in training because we have an incentive to do that, because we think the more we invest, the better it is.

#### Bubble Dynamics

**Got it. What would pop this bubble and what would happen if it pops?**

**JEO:** Well, you can think of it this way. There’s five major players today investing a lot of money to try to win a market. It remains to be seen how large is the market and whether it can accommodate those five players investing that amount of money, and if you extrapolate what’s happening today, you have arguably three players that are really making — they’re not making money, but they’re generating a lot of revenue at least. OpenAI, Anthropic and Google. And then you have two other players, Meta and xAI, they’re investing a lot, but they’re really not seeing the benefits yet.

From their perspective, that means they need to invest more in training, because that’s how they’re going to get a shot by winning, so I think that’s the main issue is how big is actually the market and can it handle these five players. And at some point, these things, I would say, if you look at this from a historical perspective, it’s generally macro. Who knows what exactly is going to unfold, you never really know what is the exact thing that breaks it, but you can suddenly have a vibe shift and suddenly everyone realize, okay, I cannot be supporting financial at this company, it could also be just driven by revenue growth slowdown.

Today, we are just extrapolating the growth curve that we see for OpenAI, Anthropic, which is whatever, 3x year-over-year for OpenAI, 10x year-over-year for Anthropic, we’ll extrapolate this into the future, but at some point you run into human issues. Maybe the next phase of growth at some point is going to be driven by enterprise and maybe enterprises have a lot of bureaucracy. Maybe they need some time to adopt these new products and revenue growth slows down temporarily, not because the technology is not good enough, but just because you need human time to actually make this technology be adopted at a rate that justifies the spending.

**How much of this power is being financed by debt?**

**JEO:** How much of this part is being financed by debt? Great question. I don’t have the best answer for you.

**It’s a very logical thing to build out with debt, given there should be a long-lived asset that is used for a long time. The reason I ask is people will say, “Oh, don’t worry about the AI bubble, it’s mostly the hyperscalers, they’re funding it from free cash flows”. But if it’s inspiring this massive response in power generation, and these new entrants, and all the sort of things that we’re talking about, is this where the actual debt bubble to be worried about might be?**

**JEO:** Let me give you some input, because super interesting theme. On the power side, on the data center side, so if you think about it on a per megawatt basis, data centers are more expensive. You can think about it this way, building a power plant, whatever, $2 million per megawatt, roughly speaking, building a data center, roughly $8 to $15 million per megawatts. Building a GPU cluster, over $30. If you add that up, you’re at whatever, $50 billion per gigawatt, $50 million per megawatt so the GPU is really the most worrying thing. But on the power plant, obviously you have some financing on the data center side as well.

Today, I guess one way to think about this is you’re increasingly seeing balance sheets take some of that risk to enable the build out. I think the most obvious one is in Nvidia, it’s really fascinating to see them — obviously, they’re the most successful company at this era — it’s really fascinating to see them using their balance sheet and providing credit backstop or credit warranties, or basically signing off on either a power contract or a data center contract or whatever to help this being financed. Because if you do that on CoreWeave risk or on OpenAI risk, your debt rate is going to be whatever, 20% or more, if you do that on investment grade, Nvidia is going to be below 10%.

It’s going to be interesting to see what is the limit of the investment grade credit and I think what you’re seeing on the debt side, where you saw Oracle debt sold off pretty aggressively, is a tell that at some point, even if you’re investment grade, you have limits. Now, to be fair, Oracle was already in debt before even starting this, they didn’t have the cleanest balance sheet of everyone. They were a BBB investment grade, but not the cleanest. Microsoft is AAA, so they’re all sort of under the US government, we’ll still have some runway before Microsoft becomes in a financially complicated position.

**It just makes sense that you would assume it’s going to happen in power, but you also want it to happen in power because you want all this built out. Well, I think the most surprising thing for this conversation with you guys, and actually it kind of makes perfect sense, is I think in general, the US always engenders senses of pessimism but there’s a bit where actually the US, it feels like is doing better in many regards than lots of other places and the reason is the reason it always is with the US, it’s because demand. Demand just rules all, and it sounds like that’s exactly what’s happening again in this space, as difficult and complicated as it might be.**

**JEO:** I want to give you the European example, it’s really interesting to me. I feel like in Europe, what comes first is the chicken or the egg, because we have this problem where there’s not demand because there’s no supply, essentially. It’s like, hey, I’m looking for 100 megawatt data center, liquid cooled, high density for AI, there’s nothing available, but the reason there’s nothing available is because from the people that build the supply, they have the hyperscalers, but they don’t see yet the AI demand so you need someone to take the risk first.

And so, I would say America’s greatest strengths is capital markets. These people actually are okay going speculative and taking some risk in order to enable things, and in Europe, because we don’t have those capital markets, things are just way slower. It’s starting to pick up finally, but a few years after the US. So demand side, capital markets, overall just I guess willingness to take risk is always one of the greatest strengths.

**Ajey, one final question. People hear all these stories and you sort of mentioned the — we’ve talked about the house bit a little bit, but you started out at a small utility and everyone I think is like, “Okay, this sounds great, it’s great the US is leading, what about me? What about my electrical bills? Not just is AI benefiting me, is AI actively harming me?”.**

**AP:** Well, it very much depends on the structure of the rate case. Every single rate case, they have the ultimate question of, “How do you convert all of your costs into all of your rates?”, and there’s always an argument of how much of your costs come from commercial, and should be paid by commercial, and how much come from low-income customers, and should be paid by them, is perpetually an argument.

The big kicker with a lot of these AI scale data centers is that they’re just massive. So even if you are a very, very large electric utility that covers a city, a massive city and all the suburbs, you can have a new data center and it’s a gigawatt scale thing and that’s immediately 20% a year load, and that changes a lot of the math. We’re seeing a lot of innovation on these, what’s called large low tariffs to try and focus on, “Okay, how do you handle rate design for a singular large customer that requires its own infrastructure and that will automatically become 10, 20% of your revenue?”, or if you’re a small utility, that takes you from a small utility that doesn’t have to do all this reporting to one that now FERC wants you to do a whole bunch of extra reporting that requires three extra staff. Oops.

So there’s a lot of those open questions, it really depends on the specifics of the rate design. It really depends on the specifics of the utility and how smart they are about it and so, it very much is a matter of check with your local public utility commission.

**Well, is there a bit where you say Microsoft comes in — Microsoft came in, no one knew what was going on, they got a bunch of great deals and now going forward, everyone that’s coming in is like, “No, you are paying for this, we’re not going to offload this to gconsumers” — so, basically, is the offload to customers to the extent they’re feeling it going to be the most right now, because it’s downstream of deals that were made two, three years ago before people knew what was going on? Whereas going forward, utilities are going to be much smarter about these deals and there’ll be less of a broad-based impact.**

**AP:** I’ve been reading about what power prices did in the ’70s, I don’t necessarily assume smart decision-making from every utility.

**(laughing) The ’70s did not have a lot of smart decision-making in general, so that tracks.**

**AP:** And there are a lot of factors beyond just the data center growth, it’s also a matter of do the input prices go to the moon for transformers, for example, or natural gas turbines. It also is about the price of the natural gas itself, there’s a lot of new demand of natural gas, not only from data centers, but also from exports. A lot of things can go, and not all of it is predictable, and not all of it is necessarily stuff that will be handled competently. So, it’s very specific to where you are and who you’re dealing with.

**Very good. Well, this was super interesting, this is actually even more interesting than I thought. Do you have any final thoughts? Because actually, we didn’t even get to — we’ll put a link to the article that you wrote, put a link to the reports that you do on SemiAnalysis, it’s all great stuff, but is there any key factors that we missed? Ajey, I’ll let you go first, then Jeremie, I’ll let you close it out.**

**AP:** This is where the action is. This is the opportunity for new ideas on electric servers to come in. And if you have one, make it happen pretty quick because this is the opportunity.

**Right. This is the fervor, the bubble that’s happening. What do you think, Jeremie?**

**JEO:** (laughing) I thought you were going to ask us about data centers in space

**It is on my list, but we’ve already gone 25 minutes over, but if you have a data center in space take — I mean,[my take on data centers in space](<https://sharptech.fm/member/episode/an-open-ai-reminder-netflixs-expanding-appetite-q-a-on-remote-work-taco-bell-and-data-centers-in-space>) is that theoretically possible, makes no sense, unless we’re in a world where we literally can’t build anything. What I’m hearing from you guys is we’re actually doing a decent job of building, it’s not what you expected as far as building, but it is sort of happening.**

**AP:** And we have not yet run out of innovation on this front.

**JEO:** Yeah, but the overarching theme is we try to do things fast. And to do things fast, you have to, I guess, take the path of known stuff to some extent. Most of the technologies we’re using are actually well-established. Turbines, engines, that’s all stuff, we’re not doing anything crazy so far in the form we’re using new technologies. So, going to space, why not? It’s the extreme way of going through the source of energy. I was saying earlier, there’s this trend of going near the energy source that’s going near the sun. Why not?

**Yeah. Literally getting closer.**

**JEO:** Why not? But it’s a bit complicated from a logistics perspective, I guess to say the least. So, yeah, probably not anytime soon. Interesting to watch, though, and the energy case makes sense. I think it’s more of a question of, “Can we actually build things and does it make sense from a supply chain perspective?”, “Can we build all of these components so that they can work together in space?”, “Can we network a 1,000K GPU cluster as efficiently in space as on Earth?”, “Can we service it?”, there’s still a lot of constraints that are a bit complicated.

**Well, I think it’s interesting though, because clearly SpaceX is the only company that could do this, because they can fully integrate so many of those pieces. On Earth, it needs to be that market-based response of all these aspects up and down the stack. Is there one critical choke point to be worried about? You guys mentioned turbine blades, for example, in your article. Is that the one or is there just a bunch of them or we’re actually not sure what’s going to be the worst one?**

**JEO:** There’s another one, that’s the big theme. Who was predicting NAND shortage a few months ago? I think no one. Now it’s NAND, now it’s DRAM, there’s always a new shortage. At some point it’s going to be fabs, maybe if we keep this trend. So, at some point it could shift from data centers to something else. In the data service space, if I had to say what’s the biggest one, I would say it’s on the labor side, but there are also ways to work around this with prefabricated stuff and more in factory to reduce the number of workers on-site, that kind of stuff. So, there’s no other one, it’s all of the above.

**Ajey, Jeremie, super interesting. The great thing is, I know I’m going to have you on again because this stuff’s changing so fast, that who knows where we’re going to be in six months to a year. Thank you very much, this is a great report, we’ll link to it and I look forward to talking to you guys soon.**

**AP:** Awesome, thank you so much.

**JEO:** Thanks for having us.

* * *

This Daily Update Interview is also available as a podcast. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Daily Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a supporter, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
