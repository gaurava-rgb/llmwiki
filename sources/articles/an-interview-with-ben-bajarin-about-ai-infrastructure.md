---
title: "An Interview with Ben Bajarin About AI Infrastructure"
reader_id: "01k6k0jcyj1gt21dc20dztj3ya"
notion_page_id: "3484ebe7-f118-81ca-a6fd-d81b3342ab87"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01k6k0jcyj1gt21dc20dztj3ya"
source_url: "https://stratechery.com/2025/an-interview-with-ben-bajarin-about-ai-infrastructure/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-10-02"
saved_at: "2025-10-02"
reading_time: "59 mins"
summary: "An Interview with Ben Bajarin about AI infrastructure, Nvidia, and Intel."
content_hash: "a3785422aa75df4a357747c40733bac2db34fc98b8c8f205f84e49a801d8d7bd"
---

An Interview with Ben Bajarin about AI infrastructure, Nvidia, and Intel.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

This week’s Stratechery Interview is with [Ben Bajarin](<https://x.com/BenBajarin>). Bajarin is the CEO and Principal Analyst for [Creative Strategies](<https://creativestrategies.com/>), one of the oldest technology-focused market research firms. Bajarin and Creative Strategies have a particular focus on semiconductors, and Bajarin also hosts [The Circuit Podcast](<https://thecircuit.fm/>) about the semiconductor industry with [previous Stratechery Interview subject Jay Goldberg](<https://stratechery.com/?s=jay+goldberg>). I previously spoke with Bajarin [last September](<https://stratechery.com/2024/an-interview-with-ben-bajarin-about-smartphones-ai-and-intel/>).

In this interview Ben and I try to wrap our heads around the flood of AI infrastructure news, including the power bottleneck, whether we are in a bubble, and if so, what the long-term payoff will be, as well as the flood of deals from OpenAI, Oracle, and Nvidia. Then we get into chips: how much should Nvidia fear ASICs, where is AMD, and the never-ending question of what should be done about Intel.

As a reminder, all Stratechery content, including interviews, is available as a podcast; click the link at the top of this email to add Stratechery to your podcast player.

On to the Interview:

### An Interview with Ben Bajarin About AI Infrastructure

_This interview is lightly edited for content and clarity._

**Topics:**

Apple and AI Video | Google and Video | The Search for Power | Bubble Productivity | Oracle | Nvidia Deal-Making | The ASIC Calculation | AMD | Nvidia and Intel | Saving Intel

#### Apple and AI Video

**Ben Bajarin, welcome back to Stratechery.**

**Ben Bajarin:** Hello Ben Thompson. Good to be here.

**We are here to talk infrastructure, AI, chips, all those sorts of things, but we did just bond over the fact that we are happy,[thrilled even](<https://dithering.passport.online/>), iPhone Air users.**

**BB:** It’s one of those things where I feel like [I wanted to tweet](<https://x.com/BenBajarin/status/1973486862846271527>), “This is the only acceptable iPhone”.

**I completely agree.**

**BB:** Then I would get so much hate, I’d get so much hate.

**I can’t imagine ever using a Pro ever again. It’s funny because, we’re here to talk about AI, [which Apple doesn’t really figure in]. I wrote, after WWDC, when they talked about Liquid Glass, “[Apple Retreats](<https://stratechery.com/2025/apple-retreats/>)“, they’re going back to what they’re good at, and I didn’t appreciate the extent to how true that is until I got the iPhone Air, which is sure, the smartphone era is considered dead and buried, old news, but they just dropped, by far, the greatest smartphone ever. It’s so good.**

**BB:** And I think it just doubles down, right? Two things that I think is interesting about that. One, Apple remains extremely good at miniaturization, which means that they will still have a lead in hardware going forward. What that means for them in AI software, fine, but all that stuff’s got to run on hardware, they’re not going away there.

**Well, we’re going to talk about — there were[all those AI video creation apps on iPhone](<https://stratechery.com/2025/sora-the-app-sonnet-4-5-and-the-question-of-models-as-processors/>), not on Android.**

**BB:** That’s where I first used it, and [made a video of me having coffee with Bigfoot](<https://x.com/BenBajarin/status/1973179637930012869>) on the beach talking like a surfer.

**Do you have any takes? What’s your favorite of the AI video creation apps so far?**

**BB:** I mean Sora is, but it’s because I think it gets the closest to the representation of myself, which I’m making a video of me or someone else that I’m friends with in my social circle, which just gets really, really entertaining and funny. AI slop being what it is, I get that and there’s a way to go, but just having something that you’re like, “Hey, I did the other one, I wanted to have a mullet in an ’80s gear rollerblading near the beach in LA”, and it did a really good job and I laughed, I thought it was funny. I was entertaining myself, Ben, with these things, but because that was the goal.

**Are you going to be entertaining yourself in a week or two weeks or a month?**

**BB:** Probably not. I certainly guarantee it will phase out. But the point being, at some point in time, this is both frightening and interesting, because what’s the future of creators? I don’t know if you saw this right away — well, in a turn of unfortunate events, the iPad, upcoming iPad, [got leaked by a person in Russia](<https://www.youtube.com/watch?v=XnzkC2q-iGI>) — and then a whole host of creators took that similarity of the iPad and made it look like they had the iPad.

**Oh, interesting.**

**BB:** You could tell it was AI, but you look at that and you’re like, “Man, what are the implications of this for content creation, original content, when really at this point it’s just your idea, not necessarily whether you have goods or not?”.

**Yep. The unbundling of the idea versus the actual substantiation of the idea, I think that’s something that[I wrote about a while ago when the first image generation apps first came along](<https://stratechery.com/2022/the-ai-unbundling/>). It’s interesting, because it’s one of those things that no one ever really thought about before. Of course the idea and the substantiation of the idea work together and turns out nope, they’re two distinct processes.**

**BB:** Yep, absolutely, so it’s been interesting. Like I said, I don’t think in a week or so, whatever, this has much stickiness, but more about like you and I like to think about things. Where does this go? What are the long-term implications of this in the next three to four years if this stuff keeps getting better and it’s indistinguishable to a large degree from real physical content?

**I think the optimistic outcome is that everything digital and online starts being treated as fake and we get a return to the real world and actually touching grass because we have no other choice.**

**BB:** Touching grass, that’s right. Go outside, go to the beach.

**Until you get AI-generated grass, I’m not sure how that’s going to work.**

**BB:** Some future simulations.

#### Google and Video

**Well, making these videos requires a lot of tokens. OpenAI claim that they’re releasing Sora using this invite system so that you were sure to join with friends, it’s more fun that way. Isn’t it more likely that they simply don’t have enough GPUs to launch this broadly?**

**BB:** Yeah, a hundred percent. And it’s funny, a lot of the initial memes that came out was these videos made of Sam Altman [running into stores to steal GPUs](<https://x.com/gabrielpeterss4/status/1973120058907041902?s=46>) saying, “Hey, we need GPUs”, or “I need more GPUs for OpenAI”, so we’re cooking these things, man, to be honest with you.

The infrastructure is hard in compute levels for this, let alone tokens. It’s also really expensive. So there’s got to be some business models that come along this before it can scale too far. You look at everybody, they’re limiting these to short-form videos, 10 seconds or less, because again, both compute can’t scale and it’s really, really expensive.

**Does this mean at the end of the day[that Google is just going to win](<https://stratechery.com/2025/the-youtube-tip-of-the-google-spear/>)? At least for video specifically? Set aside the tech space, LLMs, ChatGPT has so much penetration the consumer mindset, I think it’s going to be hard to overcome, but you get to video, they have infrastructure, they have the channel with YouTube. Is there any way they’re not the ultimate victors here?**

**BB:** I think they’re going to be a winner. I think the market’s big enough for a couple. I think OpenAI will be fine, but you’re right, Google’s ability to build compute, and a lot of these run on their own infrastructure. So TPUs and the scale that they have there, and they’re great at ads, right? This is going to have to be monetized to a large degree in some form of subsidy through ads, not paying users, and you have to believe that they’re extremely well positioned there.

My only thought for OpenAI is we read a bunch of research surveys on what people are doing, and the young demographic does skew very heavily right now to ChatGPT. Now that doesn’t mean that they’re not still using Google, but they’ve definitely moved a lot of that usage to ChatGPT.

**What I meant about Google, I mean video specifically, I think for consumer text-based LLMs, ChatGPT, I think they’ve already won. I think they actually won in November of 2022 or when they launched. But when it comes to video specifically, I guess this is a two part question. Number one, it does feel like Google’s in the driver’s seat and number two, is video for consumer going to be bigger and larger than text?**

**BB:** Yes. I don’t know the answer to two. I mean I do think there’s a ton of use cases across the spectrum where you working and working with an agent adds value. Video plays a role to the degree that, like we talked about, “Is it entertaining?”, “Is it something that can be used for the filler of content?”, “I can’t do this physically, so let’s use our imagination”, and I do think you’re right in terms of where Google will go there with their models and to monetize it.

Which one’s bigger? I don’t know. I think they both are equally large, but Google’s got the infra and I think the right business model, the trusted business model, to pull this off. I think you could extend that to the degree beyond video, to just what they’re doing with AI, [AI Mode](<https://search.google/ways-to-search/ai-mode/>), they’re going to be fine.

**Yeah, I’ve come around big time on Google as well, but let’s stick with OpenAI.**

#### The Search for Power

**So it’s hard to keep up with all their infrastructure announcements. Zooming out, every time they have[one of these announcements](<https://stratechery.com/2025/oracle-pops-from-databases-to-ai-oracle-and-openai/>) — it seems to be on a weekly basis — how much of this should we take seriously? There’s some aspect where these numbers are so large and these plans are so gargantuan, not just relative to OpenAI’s current revenue, which is exploding still, but just relative to the world economy, to all of chip production. Is this a, “We’re going to shoot for the moon, because at a minimum we’ll hit a streetlight”, sort of thing? Or are they actually going to pull these numbers off?**

**BB:** I think the monetization side of this is still, as you’re aware, the biggest question. I think the consensus is everybody believes that they need to own the AI highway. The AI highway will be paved with compute infrastructure, and we don’t know how much we need at this point. We know that we don’t have enough now, we know that everybody’s up against a constraint in every form of the stack. They can’t build fast enough. We don’t have buildings, we don’t have power, we don’t have networking, every bit is a bottleneck. The hope is if I keep building this out, that I’ll run these workloads for enterprises, for governments, for people doing these things.

**Build it and they will come?**

**BB:** Build it and they will come, I mean that’s literally where we’re at right now. Everybody who’s sitting on land with power and a shell has basically got a gold mine in some capacity, and some might monetize that better than others, but those people are going to make money, because those are scarcities in AI infrastructure.

You just look at where we want to go, agents are still the potential to — coding agents — Anthropic [came out the other day](<https://www.anthropic.com/news/claude-sonnet-4-5>) talking about Claude and something coding for 30 hours. That should be at some day, I would imagine, instantaneous. Maybe I’m wrong, maybe we’re always going to be okay with, “It takes an hour”. But I feel like people will be like, “You know what? I want this to be 10 minutes or less, if not instantaneous”, and that’s just, again, a tremendous amount of compute for these workloads.

I think that’s the hope — if we build this infrastructure, this is like railroads, right? The digging of canals, the paving of streets, that this is the future highway in which everybody will run and monetize and create economic upside. It’s like electricity too. What electricity did in infrastructure, lay wires in the ground, that’s the hope. It might be even more unprecedented than all of those things in terms of potential for GDP.

The monetization is the biggest part of this where we know businesses will pay for this. I think it’s unanimously now agreed upon that they have connected ROI to a handful of things, whether that’s coding, marketing, sales, customer support, low hanging fruit now. But across the entire business stack, I would imagine that companies will be paying a fee or some cost for each person in their organization to have some access to AI, so that’s going to monetize there.

The consumer side of it, like we talked about, might be different via ads, via commerce, via click throughs, whatever that is. But that’s build it, get the infrastructure, solve, compute. That’s going to take a number of years, quite a lot of time actually, and in the meantime, keep working out what those business models are that’s bringing that value and monetizing that infrastructure.

**You’ve always been focused on chips and that supply chain and what goes into the infrastructure. To what extent have you ever paid attention to power generation, or is that something you’ve had to brush up on and start to figure out in the way you didn’t before?**

**BB:** Right now, correct. I’ll tell you the weirdness of this is like one, it’s led me to the Bitcoin miners for better or worse, because they actually do have shells, they have capacity, they have long-term power contracts, so essentially the theory is a handful of them we’ll be able to turn into infrastructure providers for HPC workloads. CoreWeave sort of did this, right? CoreWeave mined Bitcoin, that was one of the main reasons Nvidia invested in, they’ve pivoted. Nebius is another one, they’ve pivoted. You hear people talk about IREN, Galaxy [Digital], Cipher [Mining], all these companies that again have power, they have land, they have access to more power going forward. Not just hundreds of megawatts but potentially gigawatts of power going forward, all things that are scarce. Now, whether they can pull that off and they’re just bare metal-

**Is it fair to that it’s actually widely underappreciated, the extent to which Bitcoin helped build out or get us in a better place than — in a world where Bitcoin didn’t come first, would we just be in much worse shape as far as an AI buildup goes?**

**BB:** We’d be behind, yes, I think that is exactly right, which is why when I started just trying to track power, initially it just came down to everybody in the hyperscalers we talked to is like, “I can’t get enough power”. So it was very clear to us a year or so ago that power is essentially one of the bigger scarce bottlenecks.

That was what led me to the Bitcoin miners, because you’ve got dozens of these who’ve done all of that. They’ve got capacity, they’ve got infrastructure, they have long-term power contracts, more access to land, abilities to leverage debt or assets to loan. So they’re well positioned, but let’s say that didn’t happen, we’d be starting from scratch, you’re going to go get land in Virginia, you’re going to start pouring concrete, stuff that’s happening now that Meta and xAI and others are doing. But that’s new infrastructure, being able to leverage existing infrastructure, which is why you [see Microsoft](<https://www.cnbc.com/2025/05/01/coreweave-stock-surges-after-microsoft-sticks-to-spending-plans.html>), [Meta, everybody](<https://finance.yahoo.com/news/coreweave-stock-surges-as-14-billion-deal-with-meta-signals-limitless-ai-demand-142356928.html>), doing deals with the CoreWeave’s or the Nebius’ alike is because they don’t have the physical capacity, they need to outsource some of that.

**So these deals, how much of these deals are what you just said, they have the physical capacity, they have the power contracts versus they have the Nvidia GPUs because Nvidia is very interested in selling GPUs to folks that aren’t going to build their own competitive GPUs?**

**BB:** It’s a mix of both, and I think what’s interesting here is we’re just starting to scale out the Grace Blackwell or the Blackwell era, and as you pointed out, Nvidia is kingmaker and it’s essentially distributing those so that they’re all sitting in one place. They don’t want any one company, even a hyperscaler. The case against them would be, “Don’t just give it all to one company, because you don’t want to essentially enable one company with the most valuable asset in the world right now, which is Nvidia GPUs”. And so for them, they’re distributing those things and I think they’re distributing them to the people who even aren’t — they aren’t investors yet.

I think that’s an important point. You get mixed up with CoreWeave’s saying, “Well, they invested in them, so they want them to win” — they’re actually giving allocation to others also that they’re not invested in. They just want to distribute these relatively fairly, but we’re just in the beginning stages of that ramp. As that ramps over time, it’ll continue to be some mix of that, they’ll give that to everybody.

But that doesn’t change the fact you’ve got to have a place to put them. You got to have power to run them, infrastructure to cool them and it just makes sense that while the hyperscalers would love a hundred percent to own all of this themselves, they just don’t have the buildings. Now what gets really interesting is from our conversations with the hyperscalers is what workloads they offload, and in some cases it might not be their AI workloads, it might be still needing to run on HPC compute, but it might be more complex web software that’s still doing agentic, but it’s not the training or the inference of a core model.

**Why does it matter what they outsource and what they don’t?**

**BB:** So they can prioritize their costs in a tokens-per-dollar per watt in areas where they have better deals. It is actually less economically viable, it’s a little bit more expensive to go to a CoreWeave or a Nebius in most cases. They’ll take their margins and what they’ll want to pass through, sometimes they don’t pass through the cooling costs, the water costs, sometimes they do, sometimes they don’t pass through all of power, so there’s just variables. But generally your hourly rate to rent from them is just more than yourself.

So then it comes down to, “Okay, well then what workloads might be cheaper for me to run there?”, then, “Which ones can I control and run in my own properties where I have a lot of power, which would tend to a training workload?”. You want upwards of 400, 500 megawatts for training workloads. Inference can get lower, but that’s, again, it’s expensive, so you want to control performance-per-dollar per watt as best you can for your margins and if that means you’ve decided that’s Tier 1/Tier 2 workloads for you and AI, and you’re okay outsourcing some of the other ones, because again, your cost metrics line up, that seems to be the way they’re thinking through this analysis right now and then that it impacts the deals that they strike with the Tier 2/Tier 3 neoclouds for outsourced equipment.

**So there’s a gazillion variables that go into this build out. But if we take the big three, let’s say that’s power, that’s the actual shell. And in shell, I’m looping in cooling and all the setup and wiring and ethernet, all that sort of bit, and then the GPUs themselves. What’s the stack ranking of what is the biggest bottleneck of those three?**

**BB:** Geez. I mean, it’s like it seems like it’s equal. I continually hear from those who are building out that when you just come down to the sheer bottleneck, power is it. Now, again, they’re not going to come in and say-

**Is power today, or they can see in three years power is going to be it? So as we build out, it’s a little nerve wracking.**

**BB:** No. Right now. Right now, and for the foreseeable future, because power contracts are largely set in stone for a long period of time. This is why, to your question, I started tracking power, because essentially if we know who has the gigawatts, you essentially can get a sense of who’s going to make money at this point in time, variable scales of money, but essentially it’s actually important to know who has how much power.

What further took me down this path was [Nvidia CEO] Jensen [Huang] to come out and say, “You can actually put a dollar number per megawatt”, and so if that’s true, and let’s say that’s true of Nvidia GPUs — I don’t know if that’s true of housing TPUs there, or housing tranium, if Amazon has to do this — but let’s just use Jensen’s number, he’d give a range of numbers of how many billions you can make per megawatt or even per gigawatt. So if that’s the case, then you essentially can say, “If I know somebody has 5 gigawatts of power total, or 10 gigawatt or whatever, you can get a sense of what their upside is just in revenue to monetize that in tokens”, and I’m making that point that that’s an AI factory state point.

When we say AI factories, we mean those are people who are trying to monetize tokens. If you’re a Walmart and you aren’t monetizing tokens, you’re just running infrastructure for your employees, that’s not monetizing tokens, that’s just using it for efficiency. And so you would lump that right into your operating expenses just as a cost versus making money on tokens, which is what we define AI factories as and that’s turning that infrastructure into dollars on margins over your performance-per-dollar per watt.

**So one of the things I’ve been meaning to write about is, when the last inflation numbers came out, one of the reasons why inflation was relatively low at that time was because energy costs were down. However, if you clicked into energy costs, that’s because gas was down significantly and electricity was up a lot, and it has actually been up report after report after report. Is this directly applicable to AI? Electricity costs are skyrocketing all over the country, and it’s just a matter of you have these build outs that have guaranteed contracts, and so consumers are the ones actually bearing the costs here.**

**BB:** It is, and I think that gets more drastic over time. The degree that that’s impacting costs now is a factor, I think the concern is that this goes up over time. Like you’ve heard people essentially say it’s just infeasible that consumers power bills go up that much more because they’re eating the costs for AI, and you’ve got really smart grid stuff that’s happening.

**But that’s what’s happening, isn’t it?**

**BB:** It is what’s happening. It is what’s happening.

**Consumers are actually helping pay for AI right now.**

**BB:** Correct, and there are elements of this where you’re seeing these sort of smart grid AI management of workloads in these data centers that do use things like coal and whatnot that’s generally for consumer power and they’re trying to figure out, “Well, what if I run these workloads at night when nobody uses these things?”, just to try to keep costs down. But again, that’s what we’re up against, is we are up against an [increasing demand of power](<https://x.com/DKThomp/status/1973418106669105248>), really an unprecedented demand of power, to be honest with you, that we’ve just not seen before and that has all sorts of implications about who passes those through, who’s bearing the costs for that, because it is the most expensive bill to the hyperscalers, is power.

#### Bubble Productivity

**[The bubble talk](<https://sharptech.fm/member/episode/videos-ongoing-victory-over-text-google-and-you-tubes-abundance-of-opportunity-six-questions-about-an-ai-bubble>) is obviously inescapable at this point. We have vendor financing, we have lots of money starting to be borrowed for this sort of stuff, but the question is, you go back to bubbles, are they a productive bubble, [to use the Carlota Perez framing](<https://stratechery.com/2021/the-death-and-birth-of-technological-revolutions/>)? All the railroad build out, they all went bankrupt, but we got railroads, a lot of the electricity stuff, they went bankrupt, we got electricity. Dot Com era, great example, we got a huge fiber build out, all the builders went bankrupt, but we still got something afterwards. I think the big question right now is GPUs, spending a lot on GPUs, not very useful for the long run. What is your current estimate of the useful lifetime of a GPU?**

**BB:** Yeah. I think you’ve got two ways to look at this. People will say that first and foremost, as long as you can monetize that hardware, there’s no reason to take that offline. Now again, if you’re limited in space, meaning that I’ve got a million square feet — which would be a gigantic data center, and only a hyperscaler would have that — but let’s just use that number, and I have to keep returning or moving my infrastructure in a way that makes me the best. Again, performance-per-dollar per watt, and they’d run that analysis, they have to shift some of that infrastructure.

So you hear three years, you hear four years, you have five years. But the bottom line is if they can keep making money on it, they will. The question will always be, “What’s that churn for new infrastructure?”, and then, “Is there a tipping point where next year’s GPUs are only 10% gain”, and then you’re like, “Well, I might as well just use what I have, there’s no reason to replace that infrastructure”.

Now, I do think we’re a long ways off from just a small 10% in gain, but that would be one way I think they factor, “Do I take something offline?”, or, “Do I refresh a third of my infrastructure to the newest because it’s the best bang for my buck?”.

**Where are we at right now? Are we still in the, “Use stuff for as long as you can?”. Yes, they start to break down for three years, but that’s only a big deal in training, if it’s inference, whatever, we can handle burnouts, there’s not much of a blast radius. Or are we still in the, “Time to tear off the A100s, we could use this space much more efficiently”?**

**BB:** Yes, we are in that phase and we are at the phase where I would argue the vast majority of existing infrastructure needs to be turned over and that includes general cloud purpose software as well.

**Okay, well that’s my next question. Are we going to face a scenario where general cloud computing actually starts to get more expensive because CPUs are being torn out for GPUs and so there’s more competition for the CPUs that remain?**

**BB:** I believe it’s trending in that direction. I even believe the CPUs that are needed to run agentic AI in a cloud, just cloud-native workloads actually will become more expensive. Now you might need less of them, to your point. I might need, let’s say one CPU to four GPUs in a agentic database cloud workflow, but I think that CPU itself gets bigger, gets more complex. These are architectural things that I think Nvidia and Intel will look at because they do need to keep — those agents that run your web database software need to keep up with the agent that’s running on the AI factory to go operate that software.

**Oh that’s interesting, because the AI is hitting it so much faster than humans ever do.**

**BB:** Than humans, absolutely.

**Yeah, that’s a great point.**

**BB:** And that’s why I think this point of all infrastructure needs to be refreshed, just completely rebuilt from the inside out and that’s really how you get to Jensen’s trillions of dollars a year is you basically say all of it needs to go and all of it needs to be rebuilt from the ground up for AI first and there’s a lot of logic to that for what I said, but that’s how you get to those numbers.

**So my view, just to wrap up one of the bubble angles is, as long as all the money’s going to GPUs, I feel like it’s not a productive bubble, I feel like we will have a productive bubble if we’re actually building new power generation at scale, and I think to your point, actually, God bless Bitcoin, it helped us get to where we are. We had a real problem in the early part of this decade where tons and tons of power generation was killed by regulators. Has there been a reversal there? Are we getting a power build out at scale in a way that even if this all went kaput, at least, hey, now we have excess power for the next 50 years? I like a 50 year depreciation schedule better than a 3 year one or a 5 year one.**

**BB:** Absolutely, and I think that’s what you’re seeing with, again, people are looking at nuclear, but that takes time, and that’s happening. That will happen. You will have innovation there in small and large-sized nuclear reactors over the next 10 years, it’s inevitable.

**Are we going to actually build them though? There’s this sclerosis around building anything, or is this a story where actually the biggest story of the year is this[big trip to the Middle East](<https://sharptech.fm/member/episode/the-u-s-partners-with-the-middle-east-in-ai-why-open-ai-is-acquiring-windsurf-googles-side-of-the-platform-wars>), and that’s actually where all this stuff is going to get built?**

**BB:** In terms of a large giant nuclear, probably not. If you look at a lot of the research papers, there is trending breakthroughs towards these small micro-reactors which could fuel one or two of these. If that happens, that’s productive. You could use that for cities like you said in some other areas, so it’s forcing this innovation function, that’s what’s happening.

Everybody’s like, “We’ve got to figure out how to solve this problem”, it is helping natural gas, we’re seeing lots of natural gas power companies start to get piped in. [Meta is using this now](<https://techcrunch.com/2025/07/14/mark-zuckerberg-says-meta-is-building-a-5gw-ai-data-center/>), almost I think two gigawatts I think. They’re all running natural gas, so you’re seeing that boom. We’ve got to power this stuff. Again, part of the AI highway. So I would agree with you, I think that’s productive.

**I agree it’s productive. I guess my question is, is anything actually happening? Is this getting moved down the road?**

**BB:** Yes, and it has to. We have to solve power, we have to build to plant this with renewables of some forest. So again, you’re going to see more solar implementations start to happen in these areas.

**Yeah, but renewables aren’t a great match for compute.**

**BB:** So what you do is when renewables, it’s using the residual, so you need to have backups to backups. This needs to be a [six/nine scenario](<https://en.wikipedia.org/wiki/High_availability>) and so, those are supplementing and, or augmenting whatever you’ll put in in core infrastructure. Largely, whether that’s coal or natural gas or something, you need to have all of your redundancies in place and so you’ll see them put more of that in place. And again, that’s just building out more of that infrastructure capacity, maybe that gets used somewhere else, that’s great. More solar farms can be productive across the board. So yes, that’s happening because it is a problem, so it’s a known problem, it’s just that’s going to move slow. That’s not a 3, 4 year solution problem, this is a 5, 7, 10 year problem that we’ll keep dealing with in terms power.

But my other point, I think this is really interesting, and I’ll lay this on you for the first time, I’ve said this to others, but my point about other bubbles is that was not computationally complex software and even if you just want to use networking and fiber, packet switching data bits is very different than agentic AI and so my theory is you can look at this two ways.

**Is it different this time, is that the theory?**

**BB:** But it’s only different if you follow the second part of what I’m going to say.

**Okay.**

**BB:** So if your first logic is, “This is more like desktop software or mobile software apps or web software”, then it runs its course, Absolutely. If this is more like graphics, then in the history of graphic and game development, they have never had enough compute. That’s the one category of software who every time you put something new out, they’re chasing pixels, they’re chasing lifelike reality, that’s computationally complex software.

If this is more like graphics, then this goes for a long time and I think Jensen would agree more with that. This is the whole reason he’s pivoted the GPU to these workloads, is because they’re very much like graphics and that’s just an era of software. It won’t be all software, but let’s say the big software houses who build this will build that compute and that reality — I think that’s where, if you believe that, that angle of viewing software, this goes on for much longer than people think.

**What if anything would pop the bubble if it were to be the case? And maybe it’s not this year, maybe it’s in 5 years, maybe it’s in 10 years. Or are you putting forth the possibility that actually no, this is just the way it’s going to be?**

**BB:** In the second scenario, that’s my position, this would go for a long period of time and software will outstrip compute capacity. If the first scenario happens, then a number of things. None of these Tier 2/Tier 3 neoclouds survive because you have an overbuild of capacity.

**What do you think would trigger this? Is it just a matter of, it just ends up not working?**

**BB:** No, I think it works, I think it’s more that we’ve just realized we have enough compute, whatever we have built out is enough. Again, the best analogy, remember, you were with me with this. 2000s, you open Office and it took a minute and a half and you’re like, “Man, this is slow”, and then the next year, Pentium II comes out and it takes a minute or 45 seconds. There was a pain point to you, it was slow, and so as long as it’s slow, slow within a measurable distance, that’s why I said if coding agents take 30 hours, what should we expect them to do someday? So until it’s fast enough, good enough, that’s when I think we would realize, “Okay, we might have enough compute, it’s not progressing at a weight that makes us feel slow, I’m happy with my experience, I’m getting my work done, slow is not a pain point anymore”, and we could be very far from that, we could be closer than we think. It just depends on what you view AI software as.

#### Oracle

**How many hyperscalers are there?**

**BB:** Well, Meta’s considered one, right? So, there’s four, and then Oracle is the great question, which is probably where you’re going.

**That was the exact question. Has[Oracle graduated to being a hyperscaler](<https://stratechery.com/2025/oracle-pops-from-databases-to-ai-oracle-and-openai/>)?**

**BB:** Should we consider Oracle a hyperscaler? I tend to think, yes. It’s interesting that this is debated, and I think you got a couple other things. First of all, if we’re just talking about — and I actually even debate this — should we consider them a neocloud or should we consider them a hyperscaler? This all depends on your division. I would lean toward, yes, they’re a hyperscaler and I would also lean toward, I would not put it against that company’s management or Larry Ellison to achieve that goal, if they aren’t that yet. But a lot of that also includes, what’s your differentiation? It can’t just be infrastructure. It’s got to be a layer of the stack of value that I add somewhere that’s different than everybody else with my peers or competitors.

**Do they have that?**

**BB:** I mean that has historically just been their database software, I don’t know if they have that for AI. I think right now they are basically just using their infrastructure, will build out infrastructure, and run whatever the deal, Microsoft or Amazon or whoever gives them, or Meta gives them.

**But someone like Microsoft doesn’t. What differentiators do they have in the cloud at the end of the day?**

**BB:** They have a good bit of software in the stack. Yes, they rely a ton on OpenAI, but it’s just like Amazon or GCP.

**Here’s my case on why they are a hyperscaler and not a neocloud, that is because they have another cash generating business that is not infrastructure. To me — I just came up with this on the fly — I’m not sure if it holds, but Microsoft obviously is a big company including Azure, Amazon is a big company including AWS, Google is a big company including GCP, Meta is a big company. Well, they’re completely self-contained, so they’re kind of their own category. Oracle still has a cash generating business. Now, is it generating enough cash to fund everything they’re building?**

**BB:** No.

**No. But it is different than a neocloud where all they do is infrastructure, period. So I guess they’re not quite there because their cash isn’t big enough, but at least they have a cash generating engine.**

**BB:** Yeah, I like that logic. I think when you look at where businesses go, so this is the question, does a business-not-named running on Microsoft, Amazon, or Google go to Oracle as a primary host of their workloads? And they have historically, their databases have been fantastic. Do they have that in AI? I think that’s kind of the bigger question.

**So Oracle would say, “Actually, we’ve made some really important investments in our networking stack in particular downstream from Sun, it was really important for databases, so it actually translates very well to AI”. Do you buy any of that?**

**BB:** Yes-ish. I think again, it depends, is that how much core compute? They don’t own that computer, that’s not first party compute to the same degree, and I think there’s an argument that they might start making some of their own silicon the way that the others do. But a lot of those assets they just don’t have to do North-South, East-West cluster networking, to build those racks, they’re going to use other people’s stuff. That’s just the bottom line. They might have slivers that make that better or parts of it but again, that’s a point of, I’m just making my infrastructure better, I’m not getting first parties to come to me for primary workloads, I’m making my infrastructure better to run somebody else’s workloads.

**Right. Well, but isn’t that an advantage? I put this analogy of like the TSMC of data centers in that they do have a side business, but it’s not really core to their cloud business, they’re not competing with model providers, they’re not competing with chip makers, and so if you’re from an Nvidia perspective or an OpenAI perspective, aren’t they the ideal partner?**

**BB:** I think, yes. Again, because I think, who would you bet on to keep funding this capacity built out to secure power?

**Well, that’s the question. Where is the money coming from? When[the Stargate announcement](<https://stratechery.com/2025/stargate-the-end-of-microsoft-and-openai/>) happened in January, Elon Musk is immediately like, “**[They don’t have the money](<https://twitter.com/elonmusk/status/1881923570458304780>)**.” Now we have this Oracle announcement. Also, not clear, where’s the money coming from? Where’s the money coming from, Ben?**

**BB:** Well, two things. One, who do you believe’s got the best chance to get that money? I would bet on Larry and I do think there’s a part of this leverage debt because I do think the lenders — and you’re also hearing about a lot of private equity wanting to get into this too, because they know this is picks and shovels, “I will make money if you have a shell and infrastructure and power”, and I think people would trust Larry, they’re going to give them money differently than others. So, I do think, and to answer the question. Yes, we can talk about where it’s going to come from, to me it’s, “Who do you trust the most?”, “Who would you rather bet on?”, and I find it very hard to say, “I would not bet on Larry Ellison”.

**That’s interesting. So almost like that is their advantage more than anything, is people know who Oracle is, they know who Larry is. He’s pulled it off before, and so he’s going to get the loans that other people might not.**

**BB:** He’s made lots of people lots of money and I think he’s been doing this long enough and is savvy enough. And you’re exactly right, they’ve got the scale opportunity to secure that infrastructure and I wouldn’t, again, rule out that they do some interesting things in the stack.

If you look at everybody else, Nebius, IREN, those other I talked about, they are, CoreWeave, they try their own style, they wouldn’t tell you that they’re just a second horse and that their primary business is relying on others — they’ll tell you, “No, I’ve got startups, I’ve got healthcare, I’ve got X, Y, and Z who come to me”. Fine, that’s great, but that is not your cash cow. Your money is that you’re just that you’ve got power and you’ve got infrastructure and that’s why they get those deals.

I think Oracle’s got an opportunity to make either acquisitions or build some parts of the stack, but they’re not going to be the first party of choice like Amazon, Google or Microsoft is for the vast majority of enterprises to run their public workloads.

#### Nvidia Deal-Making

**So, Nvidia is making lots of deals. The largest one obviously[is this investment in OpenAI](<https://openai.com/index/openai-nvidia-systems-partnership/>), they also made a deal to guarantee [buying compute capacity from CoreWeave](<https://www.reuters.com/business/coreweave-nvidia-sign-63-billion-cloud-computing-capacity-order-2025-09-15/>), they made other investments. How much of these deals, and maybe they differ with the OpenAI one from the other ones, is a matter of Nvidia actually trying to fill that Larry Ellison role for these companies, helping them actually get access to capital, get lower rates? Because it’s like if you’re a CoreWeave and we’re doing this build out, say, “Hey, we have a guaranteed buyer through 2030 or 2032, we should get a lower interest rate”. How much of is this just sort of the most convoluted high stakes financial engineering that there might be?**

**BB:** I think there’s a lot of it, I think there’s ways where Jensen, again obviously has, he’s incentivized to distribute his pool of GPUs, he realizes that some people don’t have the same cash as others, and so there’s deals to be had, other money to be made in terms of either interest, revenue share or just backing the capital, I do think there’s a part of that.

I don’t read into any of this that there’s artificial demand, we can’t find a person building this out that doesn’t contingently say they just don’t have enough compute. But yeah, if you’re building something, and this is again a 5 to 10 year timeline, there’s believing that Jensen is right in his number. Which is like, “Oh, it’s going to be $4 trillion a year in CapEx”, there’s believing that and then there’s like, “When will it actually happen?”, so somebody’s got to help capitalize and finance it.

I think the broader strategic point here, as I think everybody can appreciate who follows Nvidia is, he just wants GPUs everywhere, he wants to be the dominant GPU provider. And so, anything that does that, that helps him have the largest installed base of the most important compute backend in the world, he’s going to do those deals because he realizes how sticky that is, and you see him negotiate these things and do those deals on the base of that strategy.

**Is this[vendor financing](<https://en.wikipedia.org/wiki/Vendor_finance>)? And if it is vendor financing, I need [your dad’s](<https://en.wikipedia.org/wiki/Tim_Bajarin>) take on what he thinks about vendor financing.**

**BB:** From the bubble days?

**From the bubble days. We’ve been here before.**

**BB:** I think you could answer this a couple of ways. If they had the cash, would they buy it and believe it? Probably. But you’re sitting here dealing with, like we talked about, amounts of money that no one actually has, so now you have to come up with creative ways because we all believe that this infrastructure AI highway is valuable. You’ve got to find ways to CapEx this and run faster than others because, he who controls the power, he who controls the GPUs, he who controls that infrastructure is poised to make a lot of money over the long haul.

So that’s why I think people believe financing this is worth it, but it’s going to come from a variety of areas. And if the vendor has to help do that, why not? I think the other case you’d make, if they wouldn’t be absolutely sued for monopoly practices, Nvidia should have just become a first party host of their own GPUs and sold that as a service. What a great recurring business model, right? But then they’re just vendor-choicing their GPUs. That would be a subject of an antitrust-

**Well, I could push back and say, all these folks building out these data centers and sourcing this power is like the telecoms building out all the infrastructure to support iPhone traffic, and people wanted Apple to get into becoming a telecom carrier for years and years. I always push back on that, and say, “No way, the riskiest most expensive part of using an iPhone is being undertaken by everyone else on Apple’s behalf”, it’s phenomenal.**

**BB:** Yes. The same way people said, “Apple should just buy a fab”, why? Let TSMC own all that CapEx, you just run on the back of their infrastructure. So, I get it. But at the end of the day, there is a lot of money that will come from providing compute as a recurring business model, so that’s where I think they’re incentivized to make a lot of this happen. And again, it just comes back to dollars or dollars, they’ve got a lot of it, and if they can keep making GPUs indisposable to the infrastructure side, all software, all AI software running, that keeps them in a very strong position.

#### The ASIC Calculation

**Just to go back to OpenAI for a moment, Nvidia recently invested in them, Sam Altman was just in Seoul yesterday[signing deals](<https://openai.com/index/samsung-and-sk-join-stargate/>) with Samsung and SK hynix for memory.**

**BB:** Memory, yeah.

**I assume he’s not acquiring memory on Nvidia’s behalf? You would do that if you’re building your own chips, is that going to happen? How real is it?**

**BB:** Yeah, we believe they’re building their own chips. I think the consensus view, and I believe this too, is that they are the fourth “secret customer” of Broadcom looking to build some of their own sort of custom ASICs. Whether that’s a CPU and an AI accelerator, I don’t know. I think Broadcom would suggest it’s mostly an AI accelerator, even though they do some of the Arm CPU stuff.

But it makes a lot of sense in the same vein as to why TPUs make a lot of sense for Google. When you can optimize silicon for your specific workloads, you will have performance-per-dollar per watt benefits and so it makes a lot of sense that they’ll do something. How big of a scale this is, I don’t know. But I agree with you, this is not for a friendly customer, this is because they are building infrastructure, I have no doubt about that at this point.

**So how much should Nvidia fear ASICs? And by ASICs, I broadly mean all this, the TPUs, the Trainiums, whatever OpenAI is doing, basically anything that’s not — we’ll have an AMD question in a moment — but anything that’s not Nvidia?**

**BB:** Yeah, I think this is the question that keeps coming up to Jensen, and it’s the concern of most people, which is, do you lose business? Do you lose share to the TPUs, to Trainiums, to what Meta does in terms of their ASIC strategy, Microsoft with Maia, which is starting to scale? Right now what we see is that those are largely internal workloads optimized for first party software, so Amazon software, Google software, Microsoft software, is how they’re using the ASICs. Now that may change over time.

**Is that just because they push their employees to use it as opposed to developers that actually have to have something they want?**

**BB:** Yes, but there is again, like I said, performance-per-dollar per watt benefits to run Gemini, for example on TPUs, they’ve optimized the software for the silicon stack, for the architecture that they have built. You get better performance-per-dollar per watt compared to what you’d spend on, in this case, $3 or $4 million dollar Blackwell Rack, so it makes a lot of sense for them, but you’re optimizing.

Getting your customer, your CSP customer is a whole different strategy, they’ve got to migrate away from CUDA, that’s a huge lift and shift, we’re not seeing that happen at scale. Again, I’m not saying it won’t someday, this is just the view of the market today. Most third party workloads on their CSP stacks are still running on x86 and broadly Nvidia software or Nvidia hardware for their AI workloads.

**This is the question of what is the actual bottleneck?[If it’s power](<https://stratechery.com/2025/nvidia-gtc-and-asics-the-power-constraint-the-pareto-frontier/>), is the equation that matters how much performance-per-watt, the cost per performance-per-watt, or is it simply performance-per-watt, period? Because the cost actually, if your demand exceeds your capacity, you actually have to get an absolute value out of your watt.**

**BB:** Yes, correct.

**And that still favors Nvidia, correct?**

**BB:** Yes, yes, correct. It still favors Nvidia today.

**So does this mean basically that the worse we do at building out power, the better the business case for Nvidia?**

**BB:** Yes, 100%, that is true. Because you look at it, in terms of you use performance-per-watt, and we have historically talked about that, is you want to use it in a mobile form factor, you want the most compute in something that’s 10 watts or 20 watts. The difference here is, you actually want the most performance-per-watt within your wattage guidelines. So if that’s a hundred megawatts, you want to get the most compute for a hundred megawatts and so that absolutely favors Nvidia at this point.

Again, there comes a point where the cost to develop your own chip, which is somewhere in the billion dollars each cycle, plus the time to tape out, which is two years, Nvidia is on a one-year cycle, and then your margins above that. It’s never going to perform — I won’t say never — right now, it does not perform across the variety of workloads as well as a GPU.

Now, in five years maybe. And so, I think there’s a longer lead question of how workloads evolve into that matrix that I just explained to you on how they do the analysis on their chip. Where again, more third parties might say, “Yes, it makes sense for me to run that”. But as long as, exactly right, like you said, I am power-constrained, I need the most performance in that power budget, and that just is going to continually favor Nvidia, and the other part about Nvidia’s GPUs that are good right now is they’re actually better at just general purpose workflows, I don’t know what next year’s model’s going to be yet.

**That’s right, exactly.**

**BB:** It’s more flexible than the TPUs. But again, in five or seven years that may not be the case. But in the short run, I don’t see any concern to Nvidia over, call it, the five-year horizon.

**What is the difference, if any, between Google’s TPU strategy and AWS’ Trainium strategy?**

**BB:** I think it’s the same, different architectures. What is interesting is Google’s been at this longer. I think this is a fascinating model and even a lot of the ways that you model things. So AWS started doing a lot of custom silicon early, earlier than a lot of people, but they did CPUs, because to them that’s what they saw, cloud-native workloads, that was the predominant thing, people were just coming to run their basic cloud software. Google on the other hand was like, “We see AI, we see these AI workloads, that’s what we need to solve for”. So for them, TPUs have been going — they’re on, what, version six now I think, or seven.

**Yeah, 2016 I think it was the first one.**

**BB:** Yeah, exactly. So it’s just interesting to see that Amazon doubled down on CPUs because that’s where they saw the workload compute constraints were and the opportunity, where Google focused on TPUs and now Amazon’s now coming right on version 2, they’re on version 2 of Trainium. They’re just behind because for them, AI workloads weren’t the priority like it was with Google. And so, they need more time to scale, but the strategy is the same, keep my costs down, have better performance-per-dollar, control my variables in my software and give me better unit economics on my compute with my silicon. That’s essentially the strategy.

**Are they at risk of losing a lot of workloads while they’re trying to catch up?**

**BB:** Yes.

**And instead of spending all that time and space on Trainium, they could have just bought more Nvidia GPUs?**

**BB:** That’s correct, and it has already been wildly publicly known that they were underserved and under-bought GPU capacity.

**Were they underserved and under-bought by their choice or by Nvidia’s choice?**

**BB:** I mean, their choice. Honestly, I think they’re late, they’re late and behind in AI. I think they’re catching up, Anthropic is a great partner of theirs for a lot of enterprise APIs.

**To that point, how much does it matter that Google — you mentioned they can marry Gemini to TPUs and they could co-design the architecture in that regard. How much does it matter that Amazon doesn’t have their own model, or is Anthropic sufficient to fill that role for them?**

**BB:** I think Anthropic’s sufficient to fill that role. The question is, does Anthropic remain exclusive? If they’re not exclusive, then again, how are you differentiated? Google is the only one, back to the, “Why should we be optimistic at Google?”, that owns their own infrastructure and owns their own primary world-class model and that should be, any of us who are in favor of vertical integration, that should be a lot of checkboxes to the positive because they own the critical IP across the stack that we all are optimistic about for AI workloads. So it is, I think, a strategic deficit for Amazon and for Microsoft, because they don’t have one. They’re using OpenAI versus Google in just the basis of “Who’s best advantaged competitively?”.

**Should we be more bearish on Microsoft? Where are they?**

**BB:** They’re still growing as a primary. I think right now they’re still the leading choice for IT and for companies to move their AI workloads to, Google is the second and Amazon catching up right there with Anthropic, but it’s because of OpenAI, that’s the thing. I don’t think people can appreciate that if it wasn’t for OpenAI, if OpenAI had chosen Amazon, for example, this would be a very different story, it’s as simple as that.

But Microsoft and OpenAI are very close, and that relationship appears to still be solid for the foreseeable future. Because really the only two models right now you’re seeing third-party enterprises tied to is Claude (Anthropic) and OpenAI. Vast majority of businesses are just hooking into one of those models and that’s Amazon and Microsoft.

**Who has more leverage: OpenAI over Microsoft or Microsoft over OpenAI? Or is this sort of like a marriage that is going to go on forever because they just can’t afford to leave?**

**BB:** Right now, Microsoft does, to be honest with you, because they have the capacity, they have the infrastructure. Now we talk about Oracle, what if Oracle becomes-

**They don’t want to fund the leading edge models which have an economic problem — you pay a ton to run a model that is commoditized six months later and you don’t make your money back.**

**BB:** Exactly, and you have to keep chasing the new training paradigms, the new economics of that for model advancement, which is just really, really expensive. So because Microsoft is basically the backend for OpenAI, OpenAI needs that. Where else are they going to go? They can’t just create their own. They would be years away, if ever, to create the kind of infrastructure they need internally and to your point, should they even own that? Maybe they shouldn’t. Maybe they should always work with somebody else who owns that infrastructure, but there’s only a handful of companies who could meet OpenAI’s compute demands. And Microsoft has that, continues to have that, and is spending hundreds of billions of dollars, and will do so over the next few years in CapEx in order to maintain that they have that infrastructure to run OpenAI’s compute.

**Do you have any insight what happened with Microsoft where six, nine months ago, it’s like they’re[backing off on some of this investment](<https://www.bloomberg.com/news/articles/2025-04-03/microsoft-pulls-back-on-data-centers-from-chicago-to-jakarta>) that they’re doing? And then you hear a month or two ago, “Nope, they’re back in, back in the market”, [they signed another deal with a neocloud](<https://www.forbes.com/sites/tiriasresearch/2025/09/30/massive-leap-for-ai-neoclouds-with-deal-between-nebius-and-microsoft/>). Was that just when you take a breath here, or was this all overwrought and not a big deal?**

**BB:** Yeah, I don’t think it was a big deal, there really wasn’t much of a pause. Again, we can’t find anybody who was not like, “We just don’t have enough and we’ve got to keep spending hundreds of billions of dollars to make this”, including inside Azure. So it could have just been more-

**It was really about the training runs for OpenAI. They’re like, “Actually, you should go do those somewhere else”. Is that the easiest way to put it?**

**BB:** Yes. Training runs, and I’ve heard, to be honest with you, it’s actually not uncommon, and you have kind of a Tier 2/Tier 3 contract to just tear those up, even if it’s expensive, to just cancel those leases and then decide to go somewhere else with them or move that workload back internally when you have space. Just because, again, you’re looking at your tokenomics here across the board. And so, if it’s just worth it to just tear up that contract, to use a sports analogy, just let the guy go, just option him, because it’s not working out anymore. That’s actually not uncommon, it just doesn’t normally get the press that some of those contract cancellations did.

#### AMD

**Where is AMD?**

**BB:** AMD is a challenger. They are building out what I think will be a competitive rack solution and I think to preface this, we have to make the point about, “Where is this going?”. The industry is moving to tightly integrated compute cluster racks, that’s what Grace Blackwell is. It is the CPU, the GPU, NVLink, north-south with east-west networking so that you could have 10,000 of these function together as one brain with almost no latency. So that’s a shift from just it’s one rack by itself to 10,000 racks working, so that’s where we’re moving to, and we’re in the very early stages of that.

AMD does not have that solution, this is what’s coming next year [with Helios](<https://www.amd.com/en/blogs/2025/amd-delivering-open-rack-scale-ai-infrastructure-to-unlock-agentic-ai.html>), is a full rack, put these in a cluster and start to now build your infrastructure out with 10,000’s of these, or whatever, functioning as one unit. So they are positioning themselves to go and do that, to compete with these tightly integrated racks that Nvidia is making and put themselves as a position to be really the second option here, because there isn’t one of these for TPUs the same way yet that I’m talking about.

I believe there will be. Google, Amazon to the degree that Microsoft builds their own silicon, you need to be building clusters of these things. TPUs do a good job, they are clustered, but this needs to go to a whole nother level of scale. So AMD wants to be that second choice for these large compute clusters, which is good for training and really for inference at scale, but that doesn’t ship till next year.

So if you just look at where they’re at right now, they’re a tiny percentage of these hundreds of billions of dollars in GPUs, but that number’s going up, this is an increasing pie. Depending on whose numbers you look at, GPUs could be anywhere from $500 to $700 billion dollars in a year in 2030, so AMD wants a piece of that.

**Isn’t there a possibility though that for inference — actually inference is mostly run on a single GPU just with there’s a lot of memory — you could house the model, and maybe they should just leave the highly parallelizable stacks to Nvidia, because they’re not going to catch up?**

**BB:** You could make the argument, and I do think they will, that they’re going to focus on inference. I don’t think that changes the cluster need and able to serve an agentic model.

**The reality of you’re doing that, you’re just asking to take it out by ASICs, that’s the real problem.**

**BB:** Yeah, correct. And again, I emphasize this idea that to serve an agentic model to hundreds of millions of people at the exact same time is also still a very computationally complex problem, and so you need zero latency and these clusters of compute to do that for inference as well, not just training. The degree of how many, fine, but that doesn’t change the dynamic of what’s needed for inference.

So anyway, main point is there’s a lot of dollars up for grab in GPU, and AMD wants a piece of that, and it’s optimistic. People are optimistic that they could get to $10, $15, $20, $30 billion dollars of revenue for just their [Instinct line](<https://www.amd.com/en/products/accelerators/instinct.html>).

**There is this oddity though, where at the end of the day, AMD and Nvidia have the same supplier, which is TSMC. So, if you sort of zoom out, is the actual natural state of affairs in a power-limited world with network effects, that actually all that capacity that’s going to AMD would be better spent just going to Nvidia in the long run, and there’s not actually a role for AMD?**

**BB:** I mean, obviously, TSMC wouldn’t do that, right? Even though Nvidia’s estimated revenue to them is $20-ish something billion dollars, probably moving closer to $30 in the next couple of years, and AMD’s is around $10 or more than $10. In the same way, TSMC doesn’t want lock-in to be beholden to one dominant vendor, so they wouldn’t do that.

**AMD is a much more loyal customer than Nvidia has been.**

**BB:** Loyal customer, and I do think AMD has a lot of parts of the stack that they’re doing with TSMC, where I think there’s some interesting things that Nvidia might do with Intel over the long haul.

#### Nvidia and Intel

**What about Intel? So we have[this Nvidia-Intel deal](<https://stratechery.com/2025/nvidia-and-intel-tans-earnings-call-negotiation-deal-specifics/>). What’s your take on it, high level? And is Gaudi dead? Is Arc dead? How many casualties are going to be downstream of this?**

**BB:** Yeah, it’s unclear if it’s dead yet. I think you could make the argument that it should be, or at least Gaudi should be.

**Which should be dead, Arc or both of them? Gaudi being Intel’s AI accelerator.**

**BB:** AI accelerator, yeah.

**And then Arc being their GPU.**

**BB:** Their GPU, right. I think there’s two facets to this. So the high level is essentially these companies have basically been like, “We could use each other, so let’s figure out what that looks like”, and they essentially have decided that Intel is going to be the CPU and Nvidia is going to be the GPU, both in premium client parts and in these future racks that, like I talked about, are cluster x86 racks.

**Is the Arm processor in like a Grace Blackwell, is that going to go away and that’s just going to be x86 in the long run?**

**BB:** No, I don’t think so, I think it will remain both. There’s different reasons to have different workloads.

**Why? Because it’s extra complexity. If people just want tokens, why do they care if there’s an x86 steering the ship or Arm?**

**BB:** Well, I mean right now, if you look at the vast majority of those workloads, they’re moving to a Grace Blackwell workload. So OpenAI and other models, they’re training that and because that is a much more, back to the custom tuned part, Nvidia is designing that chip. They will co-design with Intel, but they’re not designing that chip for x86, so there will be some advantages.

**Why would there be any x86 ones then? Or is this just sort of a token announcement that’s not going to really matter because Nvidia is still is going to need to control the whole thing?**

**BB:** It comes back to legacy software, and I think that’s the root here. This is essentially what Jensen said, and this has been true with any ISVs [independent software vendors] you talked to, whether that’s data center or a client, is essentially that there is a lot of software that is still Intel, not even x86, Intel-run software.

**That’s why you see them bleeding in the hyperscalers for years and years, and their enterprise share, just rock solid.**

**BB:** Yeah, stays the same, exactly, and I think this is essentially what Jensen said. He said, “Customers came to us and was like, ‘I want a version of Grace Blackwell, but I want it running x86, because that’s where my software runs.'” Now that’s not OpenAI, that’s not the future AI workloads.

**But does software have to be rewritten to take advantage of GPUs and parallelism? At this point, I get the general idea that enterprise, and government is the other big client, that’s just locked on Intel. But if you’re going to rewrite the software to take advantage of GPUs and parallelism, can’t you just address the issue at that point?**

**BB:** Well, I mean that’s what CUDA does, right? So CUDA essentially gives them a lot of flexibility in terms of where they want to run those workloads, and it’s really just more, “What’s the CPU doing?”, the CPU is an orchestrator layer, the CPU isn’t really running the high-value workloads, it’s just helping organize and orchestrate and decide what goes to which block of the GPU.

Now, again, I’m not saying that’s not complex or important, but there’s a software component of those APIs that has historically been in enterprise x86. CUDA gives you some variabilities of that, but the bottom line is I think he’s dealing with the customer that is, to some degree, AMD was going to stand one of these up, which is an x86 plus accelerator, and having a response to that in an enterprise deployment makes a lot of sense.

Now, whenever this happens, two or three years from now, the biggest question on everybody’s mind will be, “What’s the mix of your Arm GPU plus your Intel GPU?”, and that will be very, very telling. But I think the customer demand is there. Intel continues to see this, which is why they’re doing this deal.

**Well, Intel made this deal because get $5 billion and a vote — how did Jensen pull off a vote of confidence in Intel without actually doing anything for Intel Foundry, it’s amazing.**

**BB:** Yes. But I would say there’s a strategic nut here that I think is [most interesting for Jensen is NVLink](<https://www.nvidia.com/en-us/data-center/nvlink/>). I think he wants that networking everywhere and he’ll do whatever it takes to get NVLink across the board because he wants networking to be $100-billion-dollar business someday or more for them. So Intel adopting this strategy with NVLink and maybe other things that they agree and build products together on just deepens NVLink’s value and solidifies it as a AI architecture for networking that just makes more valuable parts of his networking business. So NVLink to me is actually the real strategic nut here.

**So when is AMD going to incorporate NVLink?**

**BB:** Never. They have their own thing, that would be like hell froze over, right?

**Who is the one that says no when it comes to that question?**

**BB:** [AMD CEO Dr.] Lisa [Su]. Jensen would be like, “100%. Here you go”.

**I know, I think that’s right.**

**BB:** “You want this? Take it.”

**I think that’s right.**

**BB:** He wants everything. But they are on the [UALink standard](<https://en.wikipedia.org/wiki/UALink>). It’s good, I don’t think there’s anything wrong with this.

**Was Jensen, do you think, was surprised at how ethernet stood up against InfiniBand and that he’s trying to avoid a similar thing with NVLink?**

**BB:** Yeah. I think InfiniBand itself and ethernet, everybody knew, it had runway. It wasn’t like we didn’t have what we need, it’s really its ability to move those bits with less latency across that stack, that’s sort of the nut. And again, we’re both fond of integration, the most tightly integrated rack is probably going to outperform one that’s a little bit more cobbled together. But to the degree that it outperforms, we don’t know, that’s the question. But I would always just err toward integration and that’s what an NVLink situation does, is it’s a more tightly coupled, tightly integrated rack with every bit of that stack optimized for that workload and that’s just going to yield you efficiencies than one that’s using less integrated components. Even if they might be somewhat integrated, they’re less integrated, you just might not get as much efficiency.

#### Saving Intel

**The last time you were on, we were here basically saying Intel, it’s dire, something needs to be done. Something has been done,[the US government is now a part owner of Intel](<https://stratechery.com/2025/u-s-intel/>), Intel has gotten now two cash infusions, one from the US, one from Nvidia, I guess you would include SoftBank in there as well. How do you feel? And do you approve you? Or are you a principled objector?**

**BB:** Yeah, so I’ll do this two ways. Obviously this has gone from “Hope?” to “Hope!”. It’s still hope, but there is no — for Foundry particularly — there is no, “We’re comfortable to know that this is going forward”. The money that they’ve gotten does not solve their problem, that’s it at the end of the day.

For Intel Foundry to succeed and for 14A to go forward, they need a wafer customer and I make that distinction because I actually think the deal with Intel is a packaging deal for the client part, not the data center part and if these rumors around something [Apple might do is true](<https://www.bloomberg.com/news/articles/2025-09-24/intel-is-seeking-an-investment-from-apple-as-part-of-its-comeback-bid>), that’s also packaging, not process. They can’t go forward with packaging-only deals. They need wafer deals and they need a wafer-scale customer.

Now, there’s a small number of people who could do that. The most common names you would list off today are not leaving TSMC. So that leaves you with, “Would Google do this with TPUs and their Axion Arm CPUs?”, I think that’s an interesting option. But we don’t know. They need one of those customers, the money itself is not going to solve the problem. The thing on the government that I’m curious about is have they decided that Intel is just too big to fail?

**It seems yes, that’s the real value of this investment.**

**BB:** So then what do they do? Let’s say that Intel — and I’m making this up, I don’t know this for certain, I have my own ideas as well — but let’s say they need between $15 and $20 billion to go forward with 14A. Let’s say that they get a customer and it’s $7 billion, does the government give them the rest of that? Where does that extra money come from if they can’t get the customer that fuels this to go forward? That’s why I say this money’s got to come from somewhere. And even if a customer just can’t commit to the same dollar that they need, does that mean the government steps in? And that goes back to that question, is that what they’ll do? Are they too big to fail, so they’ll subsidize what’s left if they can’t get a customer?

**I sort of mentioned this in passing, but how much was Jensen making this deal with Intel just to say, “Look, I made the deal, go talk to Apple and AMD and all those guys, I’m already in the door”?**

**BB:** Yes, and I think it’s also too, there’s good favor with this administration to be investing and giving money in United States companies.

**[Particularly important for Nvidia](<https://stratechery.com/2025/nvidia-earnings-moats-and-china-nvidia-vs-the-ai-labs/>)?**

**BB:** For Nvidia, and part of me also thought that this is also him wanting this deal for him to just sell to China to come faster and show good faith in American economy. But again, none of that changes that for Foundry to go forward, there needs to be a wafer-scale customer and where does that money come from? That, we don’t know, that is still a wait-and-see situation.

**Should every fabless customer be forced to pay Intel? And they could decide whether they want to take wafers or not, but they’re going to pay for them regardless?**

**BB:** No, that’s not fair. I think you need to, and here’s my other-

**Well,[isn’t it more fair if everyone has to do it](<https://stratechery.com/2025/an-interview-with-dan-kim-about-intel-nvidia-and-the-u-s-government/>)?**

**BB:** Maybe, but here’s my take, and this is just coming from the technologist in me. You want them to choose on merit.

**I know, but no one’s going to choose Intel on merit, that’s the whole problem.**

**BB:** Maybe, I’m not ruling that out. I think they have some very good IP in 18A and future in 14A [with PowerVia](<https://newsroom.intel.com/client-computing/powervia-intel-achieves-chipmaking-breakthrough>) and [RibbonFET, right](<https://newsroom.intel.com/intel-foundry/intel-18a-process-technology-simply-explained>)? Transistor process and backside power.

**Right, but[PowerVia in particular makes it a worse mobile part](<https://stratechery.com/2025/tsmc-earnings-a16-and-tsmcs-approach-to-backside-power-intel-earnings-architecture-and-ai/>). So what workloads are they going to get?**

**BB:** I don’t think mobile is an option for them anyway, to be honest with you, I’m happy to be wrong. Dude, if somebody comes to them, Qualcomm, I don’t know, whoever and is like, “Yeah, we’re going to get 40,000 wafers” — great, I’m happy to be wrong. I don’t particularly believe that their process is right now well positioned for a monolithic SOC.

**No, it’s not.**

**BB:** I think it makes a lot of sense for a disaggregated, chiplet-based architecture, which I do think the TPUs of the world and the Trainiums of the world and their future CPUs could move to, but there’s not a lot of time to make these decisions. Intel does not have a year or more to secure whether or not 14A goes forward because that impacts the timelines of a whole slew of other people in the ecosystem.

**How many high-NA EUV machines does Intel have now?**

**BB:** (laughing) Enough?

**This is the problem. At what point does someone get their accelerators made for free because they went to Intel and the US is like, “We’re paying for them, good for you”?**

**BB:** Maybe. Again, that’s the thing. But I’m sensitive, as I’m sure you are, to this idea like we’re forced to use Intel out of our own will versus they actually have something that gives us a competitive advantage.

**Do you have insurance?**

**BB:** I do have insurance.

**Who pays for it?**

**BB:** The company.

**Which you own.**

**BB:** This is your analogy? Subsidies, yeah.

**Well, I think, well, this is what I come. I don’t like any of this, to be clear, as I hope I’ve made clear regularly. This is all terrible, you should have to win on merit.**

**BB:** Right.

**At the end of the day, Intel existing is the single most important piece of insurance for an Apple, for an AMD, for an Nvidia, for a Qualcomm for basically every single US fabless chip company, and the reason why insurance is the right analogy is because in any normal state of affairs, they don’t need Intel. TSMC meets their needs, they meet their needs better, and that’s why they’re not signing deals with Intel. But the point of insurance is you don’t need it until you need it and if they don’t want to go out of business, if something happens to TSMC, then they need to buy insurance. As gross as it is, and it’s very gross.**

**BB:** Right. But does that come again in the form of an investment? Or like you said, we secure wafers and maybe we don’t need them. Great, but that doesn’t fill your fab, that doesn’t fill your capacity with active using manufacturing of wafers, which is really what you need to keep this thing going forward.

**Right, but how is Intel ever going to get good at making wafers if no one’s paying them to make wafers? It’s all a Catch-22. This is the whole problem, someone has to jump in and force it.**

**BB:** It is. And again, this is the question of 14A, and 18A is ramping now. Intel is the product of 18A, so they’ll flesh that out and bear in mind, any 14A customer’s also going to use 18A because these are not monolithic tiles. So you’ll use some 14A, some 18A, probably all the way back to some Intel 3, which is a mature process scaling at volume.

**Well, you can still make some of your chiplets at TSMC, just some of them at Intel as well.**

**BB:** You could, you’re correct, you’re right. And Intel, again, is the only foundry that will let you do that, make somewhere else and bring to them so you’re absolutely right, you can mix and match process there. But you’re right and I think the question is, again, comes back to Intel product is the hope would be that some future product Intel makes is on 14A, but there comes a time where you got to make that call, right? That’s my broader point here. And at some point they got to go, “No, I’ve got to go back to TSMC”.

**Well, I guess that’s part two. We talked about this a year ago, we’ve talked about it in person offline for years, does Intel need to be split up? On one hand, yes, you need the design side’s volume. On the other hand, how much of a hang-up and obstacle, above and beyond all the other issues, is the fact that, “We don’t trust Intel, we don’t want our IP going over there as long as it’s one integrated company”?**

**BB:** Yeah. Actually, I say, I laugh at the, “We don’t trust Intel”, part when, I hate to say this, but there’s no secrets in Taiwan and China either. So I get it, I get the sentiment, but everybody knows everybody’s roadmaps, I don’t care who you are.

**Okay, fine. Everybody hates Intel, how’s that? (laughing)**

**BB:** (laughing) There you go, that’s one I’ll accept, Ben. But I think the point though being, they will say that product group has autonomy, can make whatever decision they want, can make mix and match tiles, absolutely. But I think there’s a lot of merit to, and if they got said investment, let’s say all the people we’re talking about decide to instead of invest in Intel, invest in Intel Foundry. Intel Foundry’s going to raise $40 billion, or whatever.

**Right. But that’s the whole point. Because of this Nvidia deal, for example, they get painted as, “We’re doing Intel a solid”, but actually this is all about the design side. Yes, there’s a small amount of packaging deal in here for high-end laptop chips or whatever, but this is really, they are on the design side. It’s the design side that at least has a viable reason to exist.**

**BB:** Yes.

**Wouldn’t it be better and cleaner if it was just super explicit that, look — foundry is not pulling up by its bootstraps, it’s being pulled up by Uncle Sam, but it’s going to happen and this is where the money is going?**

**BB:** Correct, and the other argument I’ve made for this is, and I think anybody who’s, you know this and then anybody who heard our last time, I was never really a giant fan of the splitting, but I think what’s convinced me more of this is I don’t particularly love Intel’s current board and I would love the idea of—

**[It’s atrocious](<https://stratechery.com/2024/intels-death-and-potential-revival/>). It’s unbelievable.** **They’re in the ditch because of decisions made years/decades ago. Why are there members of the board that have been there the whole time that are still there? It’s unbelievable.**

**BB:** Yes, I don’t know. But to further that point, so we all agree on that, what if an entity existed whose board consisted of some of the best and brightest minds in American semiconductor manufacturing from the entirety of the supply chain, even in every facet of that, and you had just the rock star of the board to manufacture semiconductors? That, to me, would be a very promising and a very healthy environment for Foundry execution going forward, both in process, in procedure and packaging, in execution. Plus, like you said, having the right firewalls in place so that there isn’t any question. I just think how could you not set that up as a great promising American semi story when you’ve assembled a rock star of that board just in a foundry capacity?

**Yeah, I hate this solution, I’m not in favor of state-controlled aspects of the economy. But to me, it’s like right now we’re muddling, at least we’re generally muddling, I think in some sort of good direction, let’s just rip the Band-Aid off and commit to this, let’s force a split. Everyone has to invest, from Apple to AMD to Nvidia, it’s like what Nvidia is doing with OpenAI to a certain extent.**

**BB:** Yeah.

**You might not get the upside, you might not want to fab there, but it matters. You’re paying for insurance and it’s government-mandated insurance and it sucks and it might not work out. You might have all the issues that come with government control of these sort of institutions but to your point, the board should have someone from Apple on it, someone from Nvidia on it. Intel needs to exist to serve those companies at the end of the day, and we should just be explicit about it and stop beating around the bush and muddling to a solution.**

**BB:** Yeah, agree. And I think in every capacity, there’s the trade-offs. Even in this Nvidia deal, like you talked about, if the future of Intel’s GPUs are at stake, so be it, but this is a trade-off you make, you do whatever you need to do, and if that means partnering with who was once your archenemy, you do it, because it’s just we do what we can to survive.

**What is unfair is Intel’s design business being propped up with all these sorts of deals. They’re their own hot mess and they deserve to suffer the consequences of that.**

**BB:** Yeah, agreed. I think there’s some corner turning coming in product, but you’re right. That’s why I said I would prefer all this investment dollar actually go to Foundry, that would be my preference and having a separate entity makes that happen. Just build this out. Have Apple, like you said, have Google, have Microsoft invest.

**They all should be, yeah.**

**BB:** Because they need them. Right, and then just raise, like I said, X number of dollars, $50 billion for Foundry. Because the other point I want to make about 14A is this can’t just be about go/no-go for 14A, this has to mean 10A and beyond.

**Oh, for sure. If you’re going to tape out for just the Intel process in general, you need not a 2-year roadmap, you need a 10-year roadmap at minimum, and one you can actually count on.**

**BB:** Exactly, and that’s where this astronomical number of dollars comes from. To move 14A is not as much as you need to go 10A and whatever’s beyond. You need $50, $70, $100 billion to do that, and I think that could be doable, I think the structure of that could happen. But you’re right, if the government has to intervene and go, “Look, let’s just split this, let’s open this up, let’s do a capital raise, let people invest, let Americans invest in this, put the board together”, I just think it’s clean. And again, to be quite honest with you, I think it presents not just the insurance, but this story around an American foundry that’s not really quite there today when it’s Product and Foundry together, if you know what I mean.

**Or should we let the market, should just let Intel go out of business and TSMC and Samsung will build fabs in the US and that’s good enough?**

**BB:** No. I think you and I agree — even that’s a risk. Those aren’t American companies and if you believe that this is a geopolitical issue some way down the road or that you have to have an American company with American IP, that just can’t happen. So there’s still a risk that these are not American companies.

**Yep. Obviously, I agree. It’s not about the fabs that are being built right now, it’s the capacity and ability to build the fabs in the future. [TSMC’s headquarters in] Hsinchu gets blown up, doesn’t matter. Doesn’t matter how many TSMC fabs you have in the US.**

**BB:** Yeah, you’re right. The process of just what it takes to build, to manufacture there, can it even be leading edge? You need these to be leading edge. That’s the thing, it can’t be two gens behind, you need somebody on the cutting edge in foundry and right now that is only Intel.

**Ben, good talking to you. We’ll see what disasters befall us so we can talk again in the future.**

**BB:** Yes. Good to see you and chat with you again, Ben. Always happy to come on.

* * *

This Daily Update Interview is also available as a podcast. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Daily Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a supporter, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
