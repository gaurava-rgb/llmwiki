---
title: "An Interview with Substrate CEO James Proud About Building a Disruptive Foundry in America"
reader_id: "01k8v3khxtefe0qa73dk1j0tg7"
notion_page_id: "3484ebe7-f118-819e-882d-fc4d138f2d56"
reader_url: "https://read.readwise.io/read/01k8v3khxtefe0qa73dk1j0tg7"
source_url: "https://stratechery.com/2025/an-interview-with-substrate-ceo-james-proud-about-building-a-disruptive-foundry-in-america/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-10-30"
saved_at: "2025-10-30"
reading_time: "47 mins"
summary: "An interview with Substrate CEO James Proud about X-ray lithography, disrupting TSMC, and betting on American innovation."
content_hash: "4c4fce03bd06e4040360cb431de38361124a5824c740ba668b18aac71f6e3470"
---

An interview with Substrate CEO James Proud about X-ray lithography, disrupting TSMC, and betting on American innovation.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

This Stratechery interview is another installment of the Stratechery Founder series; as a reminder, one of the challenges in covering startups is the lack of available data. My solution is to go in the opposite direction and interview founders directly, letting them give their subjective overview of their companies, while pressing them on their business model, background, and long-term potential.

Today’s Stratechery Interview is with [Substrate](<https://substrate.com/>) Founder and CEO [James Proud](<https://x.com/jamesproud>). For context on Substrate, I recommend reading SemiAnalysis’s latest article, [How to Kill 2 Monopolies with 1 Tool](<https://newsletter.semianalysis.com/p/how-to-kill-2-monopolies-with-1-tool>):

> Substrate is a recently out-of-stealth Bay Area startup inventing “technology to power next-generation foundries” with the mission to substantially reduce the cost of advanced logic wafers. The first major step towards this mission is a new X-ray lithography (XRL) tool that the company has invented.
>
> The idea of x-ray lithography has been around for half a century. MIT researchers produced the first functioning devices using XRL in 1972. Most labs doing lithography research at least experimented with it — Bell Labs, IBM, and others. IBM even built chips using XRL in the 90s, but long wavelength (DUV and above) techniques kept scaling, so there was no need to overcome the numerous challenges facing XRL. Chief among them are (a) optics, since just like EUV, almost nothing bends nor reflects X-ray wavelengths and (b) sources, since generating a bright, isochromatic, and stable source of soft X-rays typically requires massive particle accelerators.
>
> The fields of spectroscopy and microscopy continued ahead with soft x-ray technology even after chip industry interest moved elsewhere. High quality research-grade optics and ‘tabletop’-scale sources have been a focus of intense research, but nothing resembling a leading edge lithography system has gone public.
>
> It appears Substrate has overcome these x-ray challenges at least partially, and their performance claims are stunning:
>
>   * Single-patterning capable for all layers at 2nm, 1nm, and possibly nodes beyond
>   * Equivalent resolution to high-NA EUV
>   * 12 nm features demonstrated
>   * Capable of complex, arbitrary patterns
>   * Overlay <= 1.6 nm, full-wafer CDU 0.25 nm, line edge roughness (LER) <= 1 nm, LCDU <= 1.5 nm
>   * Leading edge wafers will be produced at 50% less than existing options
>

>
> These are extraordinary claims and thus demand extraordinary evidence…Evidence so far is scarce, so we repeat these claims with some healthy skepticism. But we should also note, external contacts and 3rd party reports are all telling us the same story: the litho tool is legit…
>
> Substrate isn’t stopping there. They intend to run the tools in their own fabs rather than sell to 3rd parties. The mission isn’t just XRL, it’s a new American foundry. The goal is to develop an entire end-to-end chipmaking process, buying off-the-shelf when suitable options exist, inventing when they don’t.

I highly recommend reading the entire article for context, but this covers the gist: Substrate is claiming a breakthrough in an entirely new approach to lithography — displacing ASML — and sees that as the route to disrupt TSMC and the traditional foundry industry.

Proud — perhaps surprisingly, or perhaps not — does not have a background in the semiconductor manufacturing industry; he is a Thiel fellow, who was previously most well-known for founding Hello, a consumer hardware company that created the Sense sleep tracker. Proud also founded and remains the CEO of [Config](<https://config.com/>), which creates software for managing hardware development. What is tangible in this interview is the passion Proud has for returning the United States to technological leadership, and he is seeking to do so in the most intimidating field possible. In this interview we cover Proud’s background as a Thiel Fellow, what Substrate is and the technological breakthrough in X-ray lithography he believes they have achieved, why that requires a new foundry, and what the timing of that foundry is.

I don’t know if Proud and Substrate will succeed; I am certainly cheering for them.

As a reminder, all Stratechery content, including interviews, is available as a podcast; click the link at the top of this email to add Stratechery to your podcast player.

On to the Interview:

### An Interview with Substrate CEO James Proud About Building a Disruptive Foundry in America

_This interview is lightly edited for content and clarity._

**Topics:**

A Thiel Fellow | Substrate | X-Ray Lithography | First Principles Foundry | An American Foundry | Timelines | Ideological Chip-Making

#### A Thiel Fellow

**James Proud, welcome to Stratechery.**

**James Proud:** Thank you for having me.

**Well, we have some very exciting news to get to, but before that, because I think we could spend hours discussing it, I want to learn more about you. You are here today to discuss[reviving American chip manufacturing leadership](<https://substrate.com/our-purpose>). You told me on our initial call that I was going to think you were insane — I did not think you were insane, I actually sussed out exactly what you were doing, I think, pretty quickly, but probably because you said what you’re doing was insane. But if I may be so audacious, I think I detect a British accent, how does that connect to reviving American chip manufacturing? Tell me about your journey, starting with where you grew up.**

**JP:** Yeah, of course, and thank you for having me on. When we jumped on that call and I said, “You’re going to think I’m a maniac”, and you’re like, “Only if you’re doing this”, and then we both laughed and I was like, “Let’s get straight into it”, so you nailed it almost instantly. Well, literally, instantly, so that was fun.

So yeah, despite the British accent, now I only have an American passport, but I was born in South London, grew up in the UK, started using computers when I was I think five years old. My parents bought this old — well, it’s old now — but at the time it was brand new, this IBM Aptiva computer and when my mom wasn’t using it to learn how to touch type to go and change her career, I was breaking the thing and starting to build websites as a kid. So a very innate love of technology from early on, and then fast-forward, in 2011 when I was 19, I was given the opportunity and moved to the United States by Peter Thiel.

**You were a[Thiel fellow](<https://thielfellowship.org/>), correct?**

**JP:** I like to claim that I was actually, on a technicality, the very first Thiel fellow.

**Well, what is the technicality? I’m actually interested about this process. How did you even get connected? Did you just apply online? How did you get there?**

**JP:** When I finished high school, I’d already decided that I wasn’t going to go to college, and so I ended up living on basically California hours, I would be up until the early hours, and I remember watching [Peter speak live at this TechCrunch Disrupt conference where he announced the Thiel Fellowship](<https://techcrunch.com/2010/09/27/peter-thiel-drop-out-of-school/>), and I was like, “Well, I’m already not going to college and I’m under 20, so I guess I still count, all right, let me try and do this”. There was an online application and then I was lucky enough that close friends of mine were the founder of Spotify and they were a Founders Fund company, and so I think they put in a good word, which got me an interview and flew me out to the Bay Area.

I’ve never actually told this story publicly. The process was we were in San Francisco for two or three days, they have a bunch of things set up, but at the end of it, they had this interview pitch session where all of the potential candidates would get in front of this audience of people loosely associated with Peter World. I don’t think these were his closest friends, but loosely in the Thiel —

**Peter World is very extensive, I think, to say the least.**

**JP:** Yeah, like employees of portfolio companies, and so it was a broad audience, and then you’re supposed to pitch why you wanted to get the Thiel Fellowship. And at the time, there were people pitching that they’re going to mine asteroids, solve cancer, and I wasn’t doing any of that and so my pitch was like, “I really like building things, I just want to build stuff, can I come to the Bay Area?”, and so it was probably less impressive sounding.

**Well, maybe it was less impressive but more honest, and more humble. It could be a benefit.**

**JP:** And then at the end, they sat us in this room where you had these tables with a seat in front, and all of the candidates, they sat there and so it was sort of a speed dating thing where people would watch your presentations, could come up and speak to you.

So no one came and sat down to speak to me, I literally sat at this table on my own, except for one guy who walks over, places his hand on the table and says, “Hey, don’t feel too bad when you don’t get it, it’s only because you’re not doing anything big”, and I was like, “Thank you”.

And so at the end of that process, I was pretty dejected, I dreamt of coming to Silicon Valley and I was a historian of, I think similar to you, historian of the industry, reading up about these people, seeing them, and so it was like, “Ah, I had this one opportunity and I’m not going to get it”, and it was a bummer. It was around the time actually that _The Social Network_ came out, I think that film doesn’t get enough credit for—

**Inspiring an entire generation.**

**JP:** Completely, completely. I think there’s two films that deserve so much credit for this. One of course is _The Social Network_ and two is _Pirates of Silicon Valley_ , and so those are the two, I think, most important Silicon Valley inspirational films that there are.

And so yeah, this is at the time of The Social Network, so I’m depressively watching this thing in the UK saying, “Oh man, that looks so cool”.

**So the only feedback you got in person was this one guy that came to your table and said, “Too bad”. (laughing)**

**JP:** Yeah, yeah. Then it was a couple of months later, I get this email asking — it was at 1 AM, I was still in California time, at 1 AM saying, “Hey, are you free for a phone call in two hours?”, and I’m like, “Sure”, and so I stayed up to 3 AM, and then I got on the call with the staff over at the Thiel Foundation, and they said, “Congratulations, we want to offer you the Thiel Fellowship”.

**It was totally out of the blue. You had no expectations.**

**JP:** No expectations. I was so tired that I think my response was very lackluster, and I said to them, I was like, “Hey, don’t take me not being excited for a reflection on how excited I am or not, I’m very excited, I’m just very tired”, and so then at that point, I’m immediately like, “I’ve got to get out”.

**Is that where you decided, “I need to kiss my Britishness goodbye once and for all, I need to get some proper American enthusiasm here”?**

**JP:** I’ve got to get to San Francisco, I’ve got to got to get out there ASAP.

And a couple of weeks later, they actually sent out an email saying, “Hey, Peter is going to be in New York on this day, for the Fellowship’s first class, if any of you are in New York, he would love to get lunch with you in New York”. I literally had enough money to buy a plane ticket and then a little bit, and so I bought the plane ticket to New York because I was like, “I’m not going to miss this lunch with Peter”, and then I told the staff at the Foundation and they were like, “Do you have the money to afford to move to America in a week or two?”, and I was like, “No, I have enough for a plane ticket”, and they were like, “Well, I guess we’ve got to find a way to pay you”, and so they ended up paying me before they’d even set up the whole structure for the Thiel Fellowship, and so I was proudly the first recipient of some money, and it was in true Peter fashion, The Shire LLC. And so I felt very lucky, and that’s how I claim—

**Wait. Did you set up The Shire LLC or you got paid by The Shire LLC?**

**JP:** I got paid by The Shire LLC.

**Got it, okay. I was going to say, if you had started out, if you probably just went to that initial presentation and said, “Just to let you know, I’m going to receive funding via The Shire LLC”, you might’ve gotten hired on this spot, so I guess you didn’t realize the importance of the _Lord of the Rings_ connection quite yet.**

**JP:** Yeah. No, I think only Peter and Peter-adjacent people are able to use _Lord of the Rings_ branding from now on, he’s got a lock on that.

**You had the opportunity. You could have called your new startup something like[Moria](<https://en.wikipedia.org/wiki/Moria,_Middle-earth>) or something along those lines given the metallurgy angles, but we’re going to get to Substrate actually in a little bit, but what happened then? Looking back, what you’re doing is so insane and ambitious, it’s hard to think of even if you fail and we’ll get to the challenges and issues, this is certainly exactly what Peter had in mind when he was setting up the Fellowship. And so there was something that they saw in you that I think you’ve already paid back just with this announcement this week, again, even if it doesn’t work out. But it’s 2025, this is back in 2011. What was the path to get to where we’re at now?**

**JP:** Yeah, the path is I came out here and I had actually started this side project coming out of high school in the UK, which I ended up selling and so this was a website and I ended up selling that, and that gave me enough to go and file to get a green card.

**What was that project?**

**JP:** It was a live music-related search engine. I just built a crawler for my own purposes, because buying tickets from Ticketmaster, all these various services, before Ticketmaster truly took everything into one platform with Live Nation and all of these smaller ones, it was still a bit of a mess, and so I’d built this crawler and that was a fun side thing, and I guess it got enough SEO traffic that somebody was like, “I’ll buy that”, and so that was just a pure coincidence, and then I ended up taking the money from that and actually putting it into a startup called [Hello](<https://en.wikipedia.org/wiki/Hello_\(company\)>), which I ran for five years, which was building non-invasive health consumer electronics.

I’d never done hardware before and was like, “Well, this seems like a fun problem”, and ended up going through the whole thing, shipping hundreds of thousands of units. It was something that people truly loved, and that was a really fun experience.

**What did you learn from doing hardware?**

**JP:** I learned that despite it being very complex, you can still move at very high speed, and the fact that people think it’s so complex and so hard can actually give a kind of unfair advantage if you really do push very, very, very quickly. I was exposed to doing manufacturing in your previous homeland, well, temporary home, of Taiwan and then in China, and so I got a lot of exposure to that and what goes through that entire process, and learned a lot from that experience of where we find ourselves in the US vis-à-vis manufacturing and some of these other issues.

**So I think your most famous product was the[Sense Sleep Tracker](<https://www.kickstarter.com/projects/hello/sense-know-more-sleep-better>).**

**JP:** Correct.

**It’s quite a path from Sleep Tracker to chips, but to your point, I think that’s a really interesting insight. Number one, just manufacturing in general, but number two, not being intimidated by the space. I think, famously, hardware is considered a generally uninvestible space because you just get swamped by the big guys, it’s too hard, you’re dependent on China, XYZ, and basically, your takeaway was, “Actually, it’s not that hard, and because everyone thinks it’s hard, that’s good for me”.**

**JP:** Well, I got to be clear, I didn’t end up making money from that startup, but we did make a really beautiful product, and the IP actually got acquired and that went to Fitbit, and then ultimately, Google and lives in some products there. But yeah, I think the actually making a thing and shipping a thing, you can do that — you’ve got to be right on timing when it comes to hardware, and certainly on sleep, I think we were a little early. I think if we had been maybe six months to a year later, we probably would’ve, I’d still be running that company.

**Really? Why such a short amount of time? What changed?**

**JP:** Well, I think now, everyone realizes that actually, this is really important.

**Oh, it was just the market wasn’t ready for it.**

**JP:** Pure market, and I think that we helped to push that forward quite a lot. We were pushing sleep scores and all of this stuff and the [Bryan Johnson](<https://x.com/bryan_johnson>)‘s of the world are now really leading the way, and there’s a bunch of large consumer electronics companies who are very focused on sleep. And so I think macro correct, but maybe not super correct on timing.

**So tell me about[Config](<https://techcrunch.com/2023/06/06/config/>). This is basically a software tool to make hardware development easier.**

**JP:** Yeah, 100%, and that is my other company that I’ve been running for longer than Substrate, but really, the idea for both Config and Substrate basically came at the same time, but one was clearly a company before the other.

With Config, we are really just building the software that I always wanted to have when I was running a consumer electronics company. You’ve got EDA [Electronic Design Automation] tools, you’ve got ERP, you’ve got bill of materials, you’ve got all of these disparate functions, which all basically run off the same underlying CAD [Computer-Aided Design] data but are just transformed in lots of different ways. So because of those transformations, you end up having the same data represented in different data silos, which then leads to error. The number of times, and you’ll know this and know so many companies who have done this, you’re like, “Wait, which version did we build?”.

**(laughing) Yup. Is it v1.2.3 point edited point reviewed or whatever, yeah.**

**JP:** I saw that a lot of the slowness that came from hardware came from that problem and that’s, once again, a really hard product to build. To integrate deeply within those CAD tools, to really be able to free those files, that in itself has been a lot of work, but as we see when people use the product, you can move at much, much, much greater speed and so that is something that I came up with back then, and around the same time realized that our manufacturing dependence and concentration maybe wasn’t super great, but on the semiconductor side, I didn’t see a commercial way to go and really tackle that.

#### Substrate

**All right, well let’s get to Substrate, we’ll start at the top. Give me the overview of Substrate.[You just announced it this week](<https://www.bloomberg.com/news/articles/2025-10-28/what-is-substrate-a-thiel-backed-chip-startup-seeking-to-crack-asml-s-dominance>), but you have been working on it for a long time. What is the high level view of what you’re doing? And we did talk about this before and I know a bit about the space, but I’m going to play dumb here and do a ELI5 question and you explain it to me like I’m five. What’s the pitch?**

**JP:** So the pitch is, and it seems kind of simplistic, but the United States invented almost every major technology in semiconductors, and so it’s not an invention problem that the US has.

I think that maybe over the past 10 years or so, we might have had a commercialization problem and perhaps some missteps in some areas, but the timelines for the semiconductor industry, as you know better than anyone, you make a misstep, you might not see it till 5, 10 years later.

And so the belief really from Substrate was, “Hey, there’s probably a pathway for us re-onshoring this, but if we’re going to do this, we need to actually have a technology leap, because I think that we need to have something that’s very differentiated in terms of cost”.

**Right. Path dependencies are almost impossible to overcome.**

**JP:** Yeah, and that’s not to say that we shouldn’t be on-shoring and building domestic chip manufacturing as we are now. That is a national security imperative, so outside of cost, do that no matter what it takes. But hey, if these timelines do take five to 10 years, and if you think that there’s maybe a chance that China will figure out how to do this stuff, we need to be thinking of, “What does the next generation of semiconductor foundry look like today?”.

**When did you come up with the idea of Substrate and what inspired you to start pursuing this concept? You mentioned it was a similar timeline to Config. I think that goes back to what, 2015, somewhere around then? Or what’s the timeline here?**

**JP:** It’s around 2019, late 2019 going into the lost years of COVID. But that really around 2019 was just a sort of realization of, and this is pre-CHIPS Act, pre-COVID supply chain crunch — the US government needs to do something, we need to do something natural.

**So you came at it as, “Someone has to fix this chip problem, I’m not sure how”, but that was the impetus from the beginning?**

**JP:** Yeah, that was really the impetus.

**Yeah. Which is at the right time. I think that was around, I was writing a lot about this in[Chips and Geopolitics](<https://stratechery.com/2020/chips-and-geopolitics/>) and all that sort of thing.**

**JP:** 100%, and I know for this we’re pretending like ELI5, but yeah, a lot of your writing really went into a lot of this, and a lot of this thinking of like, “Okay, there’s a few people that see that this is an issue, are we doing anything about it? What is the plan?”, and then as time started to progress, it then became a case of, “Okay, if we were to do this as a private entity, how do you do it?” — as a new private entity that is, how do you do it so it’s not a suicide mission?

**Right. So just to give context here, I remember I was talking to someone somewhere around this timeline about this problem and this need and the issue is that to do a startup that is basically replicating the foundry model is impossible. Traditional foundries are too far down to go down the learning curve, the costs are too high, and you’re dealing with a effectively zero marginal cost product. The electricity is very expensive, but the sand is cheap, that the market’s going to get flooded if you’re trying to move down, especially you have to start at the trailing edge. So you have a ton of Chinese supply, you still have the remaining supply from old fabs that are still running in the US and Taiwan, and everywhere else, and it’s just not economically viable to make what is a 10-to-15 year journey. To your point, you almost are required, if something’s going to happen here, to have a new approach. And so you just set off on a search to find that new approach?**

**JP:** Yeah, it was really, I think understanding the history of how we got here.

**Well, tell me that history. What’s your history of how we got here?**

**JP:** Well, my telling of the history is that really two companies, IBM and Intel, invented the majority of the major innovations in semiconductors. American National Labs contributed to inventing some of the major manufacturing innovations in this, but due to technical choices made, which are well-known, I don’t need to go over them, we didn’t make the right choices, and investments in the US ended up transitioning overseas because Taiwan made the right bets, Europe made the right bets, and we didn’t.

So I think understanding that, I came as a complete outsider to the semiconductor industry, that just really just reinforced my view of, “Okay, the United States can actually do whatever we set our minds to, we do have the talent, we do have the scientists, the engineers. Is there actually a pathway and do we have the right north star to go and do something new?”, and that was sort of like, “I’m unsure if there is actually something new, maybe it’s what everyone says, there’s no other way, this is the hardest thing in the world and you cannot replicate or do anything differently and if that’s the case, then sure it is what it is and we can’t do anything new going forward”. But if there was something, I had a very strong belief that the United States would be able to do it.

**So what is the new approach? What is Substrate doing that you believe is fundamentally different than the way chips are made today?**

**JP:** When studying this, it was a kind of simplistic view of, “Okay, where is the cost and complexity coming from as we build more leading edge fabs?”, because I’ve had a belief very early on, if we’re going to do this, we have to, I think as you were intimating, be at the leading edge. Because to try and be trailing edge and catch up, yes, you could maybe technically do that, there is a pathway to do that.

**But it’s economically impossible.**

**JP:** 100%. And really I think that you’re betting against the progress in technology. The bet always needs to be, technology is going to shift and that is your starting point.

**Yup.**

**JP:** And if that’s that’s not your starting point, then you’re definitely going to get swamped, I think, by China as they march down towards leading edge, and I think do so faster than people expect.

**So the most complex part of the process is lithography and I think this is one of the challenges with chip controls and manufacturing is almost everyone else in the chain, from etching to deposition, to all these sorts of things, it’s the same technology that’s used for trailing edge to leading edge. The one piece that drives up the cost that is so astronomically complex and expensive, and which China is facing sort of a wall, is[leading edge lithography](<https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography>). So we had DUV immersion lithography, deep ultraviolet. We moved to EUV, this incredibly complex system of blowing up tin and with lasers and capturing the light, and going through these crazy mirrors and focusing and doing this, that’s the spot you’re working on. Was this a function of, “We found something that might work”, or I guess to your point, “This has to be the solution if there is going to be a solution”?**

**JP:** And just to give my full credit, the current EUV tools are incredible.

**Absolutely.**

**JP:** The fact that you can make that work at high throughput, that is incredible, it is a marvel of science and engineering. But my approach was these technology choices, like the major technology choices were decided in the early ’90s, and then it took decades to scale it up to the modern miracle that it is now. My naive approach was, “If we were starting afresh today, would we make the same technology choices?” — maybe we could do something a little differently. And really, I think that you can only do that differently if you’re building the foundry as well.

#### X-Ray Lithography

**We’ll get to that, but tell me what you’re doing differently. So you’re doing[X-ray lithography](<https://en.wikipedia.org/wiki/X-ray_lithography>). What is X-ray lithography and why is it possible in 2025 when it wasn’t possible before? The concept is not new.**

**JP:** Yeah, and once again, going back to IBM and giving them the credit — and to be clear, we’re using X-ray wavelengths similar to what IBM did in the ’80s and ’90s, but our implementation is quite a bit different.

**Well, walk me through it. Tell me what that is. What is X-ray lithography?**

**JP:** So at a very high level, as you said with DUV, EUV, deep ultraviolet, wavelength of light, extreme ultraviolet, as we want to print smaller and smaller features, there’s a couple of only major knobs you can tune in that equation. One, of course, is the numerical aperture of your optics as we’re going from low numerical to high numerical.

**Right. This is broadly optical lithography. You’re actually dealing with light and bouncing it around and using that.**

**JP:** Exactly, yes. So it’s the same photolithography, optical photons, photoresist onto a wafer as everyone does now. But as you go from EUV down to X-rays, you actually get that shorter wavelength of light, which enables you to have that increase in resolution, not relying on just changing the optics as well.

**Got it. So X-rays do away with the optics? Or what’s the best way to summarize that?**

**JP:** No, I wouldn’t say it does away with the optics. It’s more you have two things that you can change, how your optics are configured, and so really the size of your optics to capture more light and change your numerical aperture, or you can shrink the wavelength and you just default get higher resolution the shorter the wavelength, basically. It’s very simplistic, but when you’re fixed at 13.5, you can’t change the wavelength or you can change the optics. And what I’m saying is that if you go to a shorter wavelength in the X-ray spectrum, you’ve already, even if you had the same optics, you now already have a resolution boost there.

Really the big innovation, the big change of, “Okay, why didn’t this work in the ’80s and ’90s when IBM were looking at this?”, and the industry was really evaluating, “Are you going to extreme ultraviolet lithography, X-ray lithography?”, a lot of the things that were required around the light sources weren’t mature enough to really meet high volume production then.

**So the big breakthrough that Substrate is trumpeting this week is this particle accelerator generative source. What is that? How does that work?**

**JP:** Yeah, so particle accelerators are very, very cool.

**I hear particle accelerator, I think of the[CERN](<https://en.wikipedia.org/wiki/CERN>) multi-mile long sort of thing, which it doesn’t seem possible that this is the story to much cheaper lithography.**

**JP:** Well, you would think that, but when the tools themselves are costing $200 million to $400 million…

**That’s right, there’s a large price umbrella.**

**JP:** And you have to buy tens of them, what might have not made sense in the ’80s and ’90s actually begins to make sense now when you actually can amortize that across a lots of different tools using that one light source.

**Just to step back, because we’ve been referencing it in passing and just for the benefit of the audience, there was a real debate in the industry back in the ’80s and ’90s about X-ray lithography versus optical lithography. Optical lithography ended up being much more approachable — it basically ended up having way more runway than almost anyone expected. The leap to EUV was very, very difficult, but it did give us another 10, 15, 20 years of new ways of drawing these lines onto the wafers to broad terms, and the issue is it’s unbelievably expensive to do now. You have these machines that you just look at them, they look like 47 times over engineered. We’ve gotten a situation where the process of turning sand into processors requires this intervening step of like $30 billion and your bid is like, “Okay, that made sense, optical won out for good reasons in the ’80s and ’90s, we should come back to X-rays”.**

**But how do particle accelerators work in this regard? How big are they? How do you solve all the challenges that existed then? You just mentioned one, which is cost. Another one is throughput, coverage. There were a lot of good reasons that the industry went towards optical.**

**JP:** Yeah, so now a lot of those issues in terms of really the brightness and how many photons that you can actually provide with these accelerators, those have been solved.

**Who solved it?**

**JP:** US National Labs. They have done, once again, incredible work. The US National Labs are really the prime jewel of this country, the greatest science, and I feel very proud that our tax dollars go to them, because it’s these innovations where you don’t expect it to, 30 years later, end up being used for some completely different purpose and we’re sort of proving that out.

**Tell me about this particle accelerator. I’m still stuck on what I — again, I hear particle accelerator, I think CERN. What is a particle accelerator in this context?**

**JP:** Very simplistically, particle accelerators, you can take these electrons, you accelerate them, you bunch them up with magnets. As you bunch them up with magnets, they end up getting excited and end up releasing photons that you can go and use for doing lithography, and we can use them. There’s lots of different types, there’s long ones, there’s very large circular ones similar to what you see at CERN. But when you talk about size, these things are very large, but they don’t require a cleanroom.

**Interesting.**

**JP:** When you think about the cost of the land, if I’m able to shrink the size of my cleanroom for my high-end tooling, but I actually end up putting my accelerator structure, we have a lot of land here in the United States, then actually the price ends up working. But if it was a cleanroom space that we had to use, then yes, that would be incredibly expensive.

**Interesting. So basically, so you have this particle accelerator that focuses these electrons, you get these ions. One of the issues was throughput. How quickly does this work? Is this a consistent source? How does the power work?**

**JP:** There’s going to be a bunch of details that I’m probably going to have to gloss over because we want to not give a blueprint to other countries and people who’d be interested in this.

But really if I need a lot of photons, particle accelerators are now the best way to achieve that and then the other things that go into that throughput calculation, such as how your resist is going to act, the throughput of your mechatronics, these are things that we’ve gone and demonstrated and have actually constructed to show, hey, of the main constituent parts of this, my source, how it interacts with in doing a very fast exposure, how my mechatronics move at production throughput required, including things such as like my wafer exchange time, these are things that we’ve all gone and physically demonstrated.

**Right. The wafer exchange time is very underappreciated as to how ASML took the lead in general. When we went from 200mm wafers to 300mm wafers, Canon and Nikon and Intel were fine to just be like, “Okay, we’ll do a bigger wafer, we’ll just do it slower. Why not? We have monopoly profits, it doesn’t matter”. TSMC and ASML completely reworked the whole system to make — you think about physics, you’re flipping a 300mm wafer, it’s 150% larger than the smaller one, you have to change the complete handling of that wafer throughout, they achieve these massive throughput gains. That was really the key to — or not the key, a key — to those two leaping ahead and that’s all stuff that you’ve already been focused on and been thinking about as far as throughput goes.**

**JP:** 100%. And I think that, okay, maybe you could get a per-tool cost lower, but if your throughput is much worse, you’re going to destroy any gains that you’ve got on the individual tool. So we have been hyper, hyper-focused on this still needs to be on a per-tool basis. Incredibly high throughput.

**Yeah. Throughput was really why X-ray lithography died in the ’80s, it was like, “There’s no way we can do this at a high enough speed to make it viable”.**

**JP:** Exactly. So we’ve been very quiet for a long time because we need to feel confident that we can actually achieve these things. Because if you can’t, it doesn’t matter, that’s the end, it’s not going to be commercially viable. We’re publicly talking about this because for quite a while now, we’ve had very deep conviction from actual results that, hey, we know that this can be commercially viable.

#### First Principles Foundry

**There’s a couple angles I want to take here. Number one, just to go back to your background, I think an immediate critique that people might have is, look, there was this teenager, didn’t even go to college, guy from the UK who has renounced his UK citizenship, he’s a US citizen, he made a sleep tracker, who is he to be talking about semiconductors and lithography? On the other hand is basically the story that that’s what was required to say, “What if we rethink this whole process as opposed to seeking out minute gains on what the industry decided 30 years ago, 40 years ago?”.**

**JP:** Yeah, I mean it’s not been easy the past few years. You can only imagine if I did come from the semiconductor industry and I was talking to people about this, I would’ve had 100, 1000x time easier going with this. The level of belief that people, and I think rightly so, incredulity at what I’m talking about, that’s made it even harder, but it’s really that deeply held conviction that this is important.

I know it comes across as very simplistic, but I’m a very deep believer in the United States and what this country is able to do when it sets its mind to it. The only question is, “Do we think that it is important enough to do?”, as I would sit there reading this stuff with no background in this space, sort of being like, “Hey, I guess smarter people know about this”.

I’m told that on one hand, we potentially face the destruction of our economy and then on the other hand, I’m told it’s going to take decades and trillions of dollars, if even at that, and so our only thing we can do is hope and pray? Historically, the United States doesn’t sit there and hope and pray that something bad doesn’t happen. We hope nothing bad happens, we hope that we are never caught in that sort of situation, but the United States figures it out. Then it’s a question of, “Do we still have the smartest people, the best universities, the greatest companies in the world?”, I think that definitely, we still do. While we still do, we can attempt something as audacious as this.

I really think that it is, in some way, a sort of whole-of-nation effort that we want to have going towards this because right now, I do believe that there is a whole-of-nation effort going on in China because they realized the criticality and the importance of this.

I don’t know. I just thought, “Well, if no one’s trying, I at least want to try”, because if I believe that this is important enough and I think that I could raise the money, hire the people, figure out something here, and I don’t do it, then I think that I’m being a bad American. I want to be a good American, and so I’m willing to sacrifice my health, well-being, and sanity, and have people think that I’m insane just to even try because it’ll be fun just to even try.

**I want to stand up and clap, that’s fantastic.**

**Let’s get to the whole-of-nation bit. You talked about, and I cut you off because I wanted I want to get to it later, let’s zoom out. All things being equal, you’re czar of the world, you can control everything, is what you’re doing a drop-in replacement for ASML? You’re talking about actually not just replacing ASML, but replacing TSMC. What I’m curious about is there’s two reasons why you might want to do this. Number one is it’s technically necessary because this completely changes how chips are done from front to end. Number two is theoretically, it could be a drop-in, but the industry is so set on this particular path that to actually make it happen, we’re going to have to do it all ourselves and show people a better way. What is the balance there between A and B?**

**JP:** I think it’s closer to B, and it really goes back to that question of speed. What is the quickest way to do this? I’m always going to optimize for what is the quickest way that we can build the most advanced wafers and the lowest priced wafers in the United States. That might not always be what is the most likely to succeed over the long run, but if we believe that this is a national security imperative, then speed is the quickest pathway to do that.

Down the line, there will be lots of partnerships and ways that you could speed that up, and I hope that we can figure those out and do those. But to go back to your initial question of, “Okay, is this completely changed in the way things are done?” — no. We’ve believed that, “Hey, if you are going to replace this one step, everything else has to still work”.

**Right. Are the rest of the steps the same? Are you still doing etching, are you still doing washing of the wafers, are you still doing ion deposition, all these bits and pieces?**

**JP:** It still stays the same, yes.

**But the issue is if you want to go to a TSMC, of course, they’re going to say, “No, we’re working, we’re already in the lead”, I guess there’s this sort of an Intel question. Or is it also if you go to a Tokyo Electron or go to a Lam Research, or everyone else in this stack, they’re like, “You’re just a startup and led by this insane guy, we’re busy serving TSMC”, you’re just like, “I guess we have no choice, we have to do it all”.**

**JP:** No, no. I think that we will be buying tools from all of the incredible tool companies that exist. Really, our view when it comes to making our own tooling and vertically integrating in areas, is like does that actually give us a huge leap in cost and complexity reduction? If it doesn’t, work with the best person that do that thing.

We’re simply doing this because we think that cost and complexity reduction needs to be number one. If we think that Moore’s Law is slowing down, which of course as you get smaller, you will have some finite laws of physics and chemistry that make it so, then we really need to be focused on the second part of Moore’s Law, which is cost improvement. That’s where we really see, okay, cost and complexity, remove those things.

#### An American Foundry

**Walk me through this. Just give me the pitch why you need to replace not just ASML, but TSMC. Is it just because TSMC and ASML are inseparable?**

**JP:** No, I think that we want as many American foundries as we possibly can. It goes once again to if there is a country in the world where you possibly could make a new foundry business, it’s most likely actually going to be in the United States. I think that we can begin to look at not just lithography, but there’s a bunch of other areas and ideas that we have where we think, “Hey, if we did that a little differently”, and I say this not in a negative, if you didn’t have the baggage of being existing for decades, once again, the work that these existing foundries and everyone does, it’s incredible.

**Well, there’s a very simplistic view, these ASML machines are absolutely incredible, you also look at them and, just as a layperson, they look absurdly overengineered to a certain extent. There’s almost a bit where, and maybe this is the cleanroom angle, why is it so compact relatively speaking? Why is it so tightly tied together, and you have all this intricate tubing, wiring, and stuff like that? It feels like we could just spread this out a little bit. It’d be easier, more sustainable. Why do we need five, six 9s of yield?**

**I would think of something like Starship, and I can imagine Elon Musk is an inspiration for you, but the challenge is if the government is building the rocket, they can’t afford for it to blow up because then their funding’s going to get pulled. You end up dramatically overengineered, but you never find that line between just barely good enough and failure unless you’re willing to cross the line and fail. You need some Starships to blow up if you’re going to get it as cheap as possible, as simple as possible, because you won’t find the line otherwise. Have I just articulated your overall approach and view on this? You want to get in a position to fail a lot?**

**JP:** 100%. You completely nailed it. I think it’s really important to take that example of Elon. When he started SpaceX and those rockets were exploding, you had people lobbying Congress saying, “Only NASA should do this, who is this guy? Only NASA should do this” — if he hadn’t have started SpaceX then—

**We’d be screwed.**

**JP:** We’d be reliant on Russian launch capabilities right now, China would own space dominance against the United States. But instead, we are so far ahead because Elon was willing to do it when it was unpopular, [when he had Neil Armstrong lobbying Congress](<https://www.youtube.com/watch?v=8MoACklnnxk>), I can only imagine the pain for Elon to feel to have someone saying, “You can’t do this”, but he knew how important this was to do. I think most people, maybe rightly so, are like, “You’re insane, China’s not going to catch up”. My response would be, “What if they do?”, “What if they do figure out a way to do advanced lithography?”, then we’re in a really tough spot. The same way that you needed to start SpaceX when it didn’t seem like you needed to, I feel very, very similar about what we are doing.

**How does this actually manifest though? What is the spaceship blowing up of your approach in the way you’re trying to build a new fab?**

**JP:** Hopefully, we don’t have anything blowing up.

**(laughing) I think that for sure, a little bit of a difference. You’re not dealing with rocket fuel, fortunately.**

**JP:** The stakes are a little lower there. Look, I think it can manifest in there’ll be things that you do when you’re experimenting, where you might run a process, you might run a tool, it sounds simple and small, but you might not have it in a cleanroom. But traditionally, you’d have that in a really very, very, very clean space, but maybe where a startup—

**Right, that’s one reason why the EUV machines are so relatively compact, is they have to fit in a cleanroom. Part of your theory is actually, “We could build this entire accelerator outside the light source, and only the actual wafer handling portion needs to be in a cleanroom”.**

**JP:** Yeah. There’s these assumptions that will hold right now, but maybe you want to push them. On some of them, we’ll push them and we realize, “Hey, there is a reason why it’s done this way”, but maybe if you can do things a little differently, you can start to relax some requirements in certain areas. I think that we have a healthy dose of steps.

**This is why you need to take on TSMC, not just ASML, because the entire process needs to have this view.**

**JP:** I think that we will find that if you start to do it this way, things will begin to unlock that might not have been possible in the past, but rightly so. If you are running a trillion-dollar company where everyone relies upon you.

**It would be irresponsible for TSMC to be screwing around with these processes.**

**JP:** It’s completely irresponsible. I think it’ll be irresponsible for the United States to say, “This is our only bet and this is…” — no, we need to do everything. But the question is, “Are we at the stage where we need to throw everything against the wall?”, I believe firmly we are at the stage where we need to throw everything against the wall. I think having a sort of asymmetric bet here is one of those things, and that’s how we see ourselves.

#### Timelines

**Where are you exactly? Why are you announcing things this week? You mentioned that you feel you have some verifiable data that you can actually do this.[You just raised $100 million](<https://www.wsj.com/tech/peter-thiel-backed-startup-secures-100-million-to-make-chips-in-u-s-baff93ac>), which sounds like a lot of money until you realize a new fab costs $30 billion, that’s like a fifth of the cost of a UVNA machine. What are the next steps right now? Why now?**

**JP:** The previous money, the over $100 million that we’ve raised, that’s actually more historical. I think it’s now being reported because people are saying, “How much have you raised? Can you give us a ballpark?”.

**Oh, got it. Most of it’s already spent, even better.**

**JP:** I think the main reason for announcing is we’re incredibly proud of what we’ve been doing in secret the past few years. We’re incredibly proud of the results that we have to show. But also keeping a project of this scale under wraps, I think as you start to build big facilities, you build big particle accelerators, people are going to start asking questions. We’d rather put this together and tell people why we’re doing what we’re doing, what we believe versus somebody else trying to tell that story for us.

**What is next? Are we at the stage where we start reaching out to some of the semiconductor equipment manufacturers to bring them into the process, or is this still a self-contained, still inventing things sort of area?**

**JP:** That process has already been going on for a while now. We want to start building very big things very quickly, very soon.

**What timelines are we talking about here?**

**JP:** Our goal is by 2028, to have a full facility up and running, and be running wafers through. That’s a timeline we’re marching towards.

**Knowing that these are all marketing terms, 2nm, 3nm, 18a, 16a, what’s the target?**

**JP:** The target is basically, I would say, the sub-2nm class of node.

**Definitely on the leading edge. The idea is you are going to show up on the leading edge, but a fraction of the price. How is this going to manifest on the back end?**

**JP:** Yeah. You’ve got Moore’s Law, but we also have the one thing that has stayed constant, which is [Rock’s Law](<https://en.wikipedia.org/wiki/Moore%27s_second_law>) of how the cost of fabs is basically doubling every several years — that has held. When you chart this out, by the end of the decade, we’re going to be approaching $50 billion fabs going into wafers costing $100 thousand on the leading edge. I think that things are going to start to break once we get there.

**One of the underrated issues, and I think one of the big challenges facing TSMC in particular, is we already crossed the line of these wafers being so expensive that a huge portion of the industry just stopped at 28nm.[They’ve had to almost completely reinvent their business model](<https://stratechery.com/2024/tsmc-earnings-the-trailing-node-netflix-wwe-follow-up/>) to jack up prices on the front end because they’re not going to make the money back on the back end. This whole 7nm, they have a huge glut, it’s barely used, and it wasn’t engineered to be reused, unlike 5nm, 3nm, they started changing their approach to actually be more like the Intel of old, which Intel was always trying to stay in the front end so they’re trying to reuse equipment as much as possible. But that problem is only going to become more acute. You think about if we have to move to EUV-NA machines, what about all these EUV machines that aren’t going to be able to take advantage of the cost over time because it’s still just too expensive?**

**JP:** Yeah, I think that the opportunity here is: if we can begin to really bring the cost of leading edge much lower, you expand the aperture of the number of people who can afford advanced silicon, you increase the velocity of the numbers of wafers being produced and that is the virtuous cycle that the United States needs to unlock. If you can do that, then you actually have a huge market force — like you said, people beginning to move to the leading edge who previously couldn’t afford it. A huge market force that especially as wafers trend towards a $100k, is going to actually lead to volume capacity being built in the United States, that has always been so core to what we believe.

**So does your business plan require that you start achieving massive volumes? Are your fabs going to be this expensive but higher volume or are they relatively lower volume but they’re just so much cheaper that you can just build a bunch of them?**

**JP:** I would say that to operate in low volume, much lower cost, and so the sort of wafer-per-dollar spent on the fab will be actually lower.

**You don’t need to make up in volume, whereas that’s the Intel problem. They don’t have the volume to keep up with TSMC, even if they can do it in theory, the economics don’t pencil out.**

**JP:** Yeah. The barrier to entry both for us and for the end customer needs to be at a lower price. As I said, you own the key parts of the tooling chain where you can reduce cost and complexity, that then enables you at a much lower volume and a lower price point to be revenue accretive. But the goal is: we want to be building fabs that are huge, that are making hundreds of thousands, millions of wafers.

**You can actually ramp up to that without having to be huge from day one, which is sort of the challenge currently.**

**JP:** Exactly, that’s the key. That is the exact key.

**Okay. 2027, 2028, EUV, I think was invented in the late ’90s. It was projected that we would start using it in 2007, 2008, it took a lot longer than that, it took a lot more money. TSMC, Intel, Samsung had to basically rescue ASML back in the day to keep this going. This is fun, this is exciting, it’s 2025. Are you going to be on here in 2035 saying, “It’s definitely coming next year”?**

**JP:** So I think if you look at the history of the development of EUV, there were a few things that had to scale. One was scaling the power of the source and the other was really scaling down the number of defects on the optics. I can confidently say as of today, we are already there on the source and the scaling down problem of the optics, that’s no longer a problem either.

**It’s just an issue you just don’t need as good of optics as EUV because your wavelength is already smaller to start out with?**

**JP:** I don’t want to get into too many details on that.

**No, I know you don’t want to give away the secret sauce, but yes.**

**JP:** But if the problems have already been solved and you don’t have to solve them yourself, then you don’t have that scale up time, which takes multiple companies, multiple countries to go and go and do. But that doesn’t mean what we’re doing is easy. I think there’s a sweet spot where something can be incredibly, incredibly hard, but you can actually move quickly and then there’s a less sweet spot where something is incredibly hard but you cannot move quickly. We are occupying what we believe, and I think you have demonstrated is incredibly hard, but there is a pathway to move quickly.

**So I talked at the beginning that this is something that needs to be done, whether or not you succeed and you’ve already achieved, I think, this is what the Thiel Fellowship saw, is, “Hey, you’re willing to give it a shot whether it succeeds or not”. What is your confidence level of it succeeding?” Or is this, say, like, “Oh, we’re at a hundred percent we’re going to do it?”, or is there some sort of still a bit of humility here, “Nothing’s guaranteed”, where are you on that continuum right now?**

**JP:** Well, I’ve always been very, very open at how hard this is going to be. I remember with my brother [Oliver Proud] who’s also my co-founder, there was a moment where we were deciding to start the company and I leaned through a door and I said to him, “This is going to be incredibly, incredibly hard, are you sure you want to do this?”, and he said yes. And I said, “Okay then”, and then we both went to off.

**Maybe it had to be a brother because you can’t get divorced or anything. You’re stuck with him no matter what.**

**JP:** There’s a trust level.

**Unless you murder each other to try to avoid that.**

**JP:** That’s not going to happen! But then with investors, when I first started speaking to them, I was like, “I want to be very clear…”.

**When was this period? When were you speaking to investors just to give us some context of time?**

**JP:** So this was early 2022, and I said to them, “Our chances of success are about 1%. I want to be very clear: the chances of success are 1%, but I’m going to operate as if our chances of success are 100% and that we can’t fail”, and so I think that’s the sort of dual worlds that I try and operate in.

**It’s the classic venture bet.**

**JP:** Chances of success, still extremely low, but we have to succeed and so we’re going to do whatever it takes. And so I would say it’s still the same, that’s how we operate.

**It’s still a chance of 1%? Certainly, your evaluation is going to be higher.**

**JP:** The numbers are going up, but we still know that everything is still stacked against us. But as I said, I think this is important enough for the United States that we try and we give it our all.

**What’s stacked against you? Is it still technical challenges? Is it getting the ecosystem challenges? Is it a market challenge? If you start to go back to 2022, I would argue the technical challenge is sort of first and foremost. Is that still the case?**

**JP:** I would say that that sort of science and engineering, that technical challenge of, “Okay, this key enabler technology, can that work?” — yes, we feel very confident in that and by the results and the images that we’ve started to show, we feel high confidence in that. So that’s like, “Okay, now we can go”. I think really going from there, everything else, there’s an existence proof and so this goes back to my, “Does America have the talent, the engineers, the companies to do these things?” — yes.

**You think you’ve already shown that?**

**JP:** I think for the really crazy piece on the lithography, we feel that, yes, we can go and do this and we know how to scale this and we know the challenges there, that is tractable and then on the other pieces of really pulling this together, it’s always a question of, “Does the talent exist in the United States?”, “Do the companies exist?”, and I think that’s a resounding yes. So can we bring these things together? I believe the answer is yes. “Okay, now let’s go and tell the world that we exist and let’s run at this full speed”.

**So is it that you need the money now to make this happen, or are you ultimately going to be facing the Intel challenge, which is: are we going to have a market?**

**JP:** I think that if you can actually lower the costs so significant that, I think a different market will materialize.

**Right. Apple’s not leaving TSMC, but lots of other people would like to have that level of chip and can’t.**

**JP:** Yeah. I wouldn’t expect an Apple to say, “Hey, you know what, Substrate…” — I would revolt as a shareholder. I’d be like, “What are you guys doing? This is crazy”. I would love to work with Apple at one point, but that’s not the sort of founding belief of, “We need to land a huge whale on day one to make this thing work”.

**Yep.**

**JP:** When I sort of play out, “Okay, where is AI going? Where are these models going?”, when I look towards the end of this decade, I actually think that we’re going to be at the point where these models are able to design chips as good as humans. And if we get to that point, we’re going to have a proliferation of design. If we have a proliferation of design, then the key bottleneck is going to be the fabrication. Right now on the leading edge, you have bottlenecks of both fabrication and design so that limits the number of companies who can even play in that space. I think one of them through just the natural progression of AI is going to be removed and so how can we go and remove the second one? It’s really, as I said, a proliferation and a huge increase in volume.

#### Ideological Chip-Making

**How much of you talking about this — if we go back to those two problems, just say just money and market, how much of talking about this is about letting people know, “This is something that’s doable; you should come invest in this”, versus, “There is a burgeoning opportunity that’s going to show up in a few years and if you want to start that company and actually build something big that wasn’t possible previously, now’s the time to start thinking about it”?**

**JP:** Are you asking about starting a chip like fabless?

**Yeah, your motivation to talk about it. Well, I think there’s lots of companies that can potentially be started, right? If you’re talking about, “Actually, I understand and appreciate what TSMC does that entire chain, no one’s going to actually abandon that chain who has a good place in it because it’s stable and they’re large companies, they have to answer to shareholders. So we’re doing a different approach, but that means we’re going to need new partners at manufacturing equipment, in design software”. I don’t know what those might be, but that is one where, so there’s an opportunity in the overall supply chain.**

**There’s a potential opportunity in fabless, you can actually think about building a 1 nm chip that does XYZ knowing you can be low volume and there’s going to be this interesting opportunity that’s going to be relatively low cost. And then there’s the, “Hey, it’s not going to cost $30 billion for a fab, but it’s going to cost us a lot of money to get this done, and we need investors who believe in this vision”.**

**JP:** I think it’s more important when — like I said when we first spoke, “Hey, you’re going to think I’m probably insane in a maniac”, I think it’s important that to sort of tell the world, “Here’s what we believe”, and tell it in its totality. “Hey, we actually have very deep convictions that the world is going to look like this, and that’s what we’re building towards”, because today, if you are building towards today, some of the choices that we are making might not make any sense at all. And I think it’s important to say, “We think that things are going to change and that’s what we’re building towards and the timelines involved require you to build towards that future — I might be wrong, we might be wrong about that future, but that’s certainly what we are building towards”, and the people deserve to know.

**I think we’ve answered this question along the way, but to sort of tie this whole thing together — you grew up in the UK, we didn’t get the full story yet of you become a US citizen, renouncing UK citizenship. You’ve also written that[Substrate is deeply ideological](<https://substrate.com/our-purpose>), which I think we’ve gotten the ideology, but how would you tie that all together to Substrate being the manifestation of your own personal conviction and what you want to do?**

**JP:** It goes back to I think that we sometimes forget that the United States does consistently very, very hard things.

**When did you come to this conviction? Did you believe this when you were in the UK or is this when you came over to San Francisco?**

**JP:** I believed that when I was in the UK, I always wanted to be in Silicon Valley, that was ingrained from a young age, I just didn’t know that I could be there, and so that’s why I’m so deeply appreciative of Peter for giving me that opportunity. I wouldn’t be here and I wouldn’t be an American most likely if it wasn’t for him and so I had that deeply held conviction early on. Then just being in the United States and not just being in Silicon Valley, but having friends over in D.C., friends in the military, people who do very hard things every single day, and when you talk to them about why they do it, it’s like—

**“What else would I do?”**

**JP:** What else would I do? I can’t say where, but somewhere in D.C. there’s a building that when you walk out, above the doors, it says, “Somewhere in the world there’s an American counting on you”, and I read that and I sort of look around and I see the people who — they’re like, “This is obvious. Of course, that’s why I come into work every single day”, but sometimes I think in Silicon Valley and in tech, we forget about that.

So it goes back to what I said, we’re told that there’s really bad things that might happen if we don’t solve this problem, but it’s an impossible problem to solve and so if there’s a lot of Americans who walk out and see somewhere in the world, “There’s an American relying upon you”, what would that look like if we went and did that in tech and that’s how we see what we’re doing here or I see myself. And so as I said, chance of success, they’re always going to be very low, but we’re going to act as if we have to succeed.

**Well, there’s a reason why when we got on the phone line, you said, “You’re going to think I’m insane”, I’m like, “Oh, you’re building a foundry”, and I think you gave a very compelling reason why, and certainly I am cheering for you. It’s exciting for you to announce this.**

**I think it certainly speaks to something that I feel very deeply, particularly relative to this geopolitical competition with China. I think one of the contexts I always talked about, it was this question of censorship and controlling the information online and my take has always been, “You’re not going to do that better than China, you are going to succeed through innovation”. That’s how the US has done it in the past, and we need to be clear-eyed and honest about that and be okay with the “downsides” that come from that, from anyone be able to sort of say what they want.**

**And I think this is the physical manifestation of that. We’re not going to reproduce what’s been done before as well as China’s going to do and in many respects, you’re right, that’s the critique of so many of the “solutions” to the leading edge processes. “Can we do what TSMC did here?” — no, we’re not going to do it as well as they did, that’s the economic issue. In a nutshell, the best way to do it is to actually innovate and do something new. And I, for one, am glad that you’re here doing exactly that.**

**JP:** Thank you, Ben. As I said, we’ve been reading your thoughts and analysis on this for a very, very long time and yeah, very excited to finally speak to you and walk through this. You’ve been a part of this journey even if you didn’t know.

**Well, cheering for you. Thanks for coming on.**

**JP:** Thank you.

* * *

This Daily Update Interview is also available as a podcast. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Daily Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a supporter, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
