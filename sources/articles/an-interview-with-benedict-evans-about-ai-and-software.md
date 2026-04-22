---
title: "An Interview with Benedict Evans About AI and Software"
reader_id: "01kgqfh4jpgfqt6sp88nz52b0b"
notion_page_id: "3464ebe7-f118-81fc-9051-ffcdc8531fee"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01kgqfh4jpgfqt6sp88nz52b0b"
source_url: "https://stratechery.com/2026/an-interview-with-benedict-evans-about-ai-and-software/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2026-02-05"
saved_at: "2026-02-05"
reading_time: "50 mins"
summary: "An interview with Benedict Evans about the crisis facing software, the future of the corporation, OpenAI, and the struggle to define the LLM paradigm."
content_hash: "dcaf8e85575389e8aaa4433176fb1a865fc4eba16239d56b652b6786974bed13"
---

An interview with Benedict Evans about the crisis facing software, the future of the corporation, OpenAI, and the struggle to define the LLM paradigm.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

This week’s Stratechery Interview is with [Benedict Evans](<https://www.ben-evans.com/>). Evans is an independent tech analyst based in New York. Evans started his career in investment banking with a focus on the telecom sector, before his first stint as an independent analyst focused on mobile. In 2014 Evans joined Andreessen Horowitz as partner and analyst, before departing in 2020; he is once again an [independent analyst](<https://www.ben-evans.com/newsletter>) and [speaker](<https://www.ben-evans.com/presentations>). Evans was an inspiration for me when I started Stratechery, and it’s an honor that these interviews have become a bit of a tradition: we talked previously in [2024](<https://stratechery.com/2024/an-interview-with-benedict-evans-about-regulation-and-ai/>) and [2025](<https://stratechery.com/2025/an-interview-with-benedict-evans-about-ai-unknowns/>).

In this interview we start with the topic on everyone’s mind: is software dead? That necessitates understanding what role software actually plays in enterprises, which raises the question of what corporations will look like in the future. Then we discuss OpenAI and its desperate search for a moat, the peaks and valleys of LLM knowledge, and the fact that consumers both want new paradigms, and the fact that those paradigms take a long time to emerge. At the end we discuss the future of devices and the supply chain, and whether the smartphone can ever be displaced.

Evans’ website is located at [ben-evans.com](<https://www.ben-evans.com/>), where he both posts long-form essays and hosts subscriptions for his newsletter. Evans has written about many of the topics we discuss in this Interview; I strongly suggest you subscribe.

As a reminder, all Stratechery content, including interviews, is available as a podcast; click the link at the top of this email to add Stratechery to your podcast player.

On to the Interview:

### An Interview with Benedict Evans About AI and Software

_This interview is lightly edited for clarity._

**Topics:**

Is Software Dead? | AI and Coordination Costs | The OpenAI Cargo Cult | LLM Knowledge Gaps | New Paradigms | Smartphones and Supply Chains

#### Is Software Dead?

**Benedict Evans, welcome back to Stratechery.**

**Benedict Evans:** Thanks for having me.

**[Is software dead](<https://stratechery.com/2026/microsoft-and-software-survival/>)?**

**BE:** Good topic. I was just thinking about this, well, in various ways over the last few weeks. I just think there’s a starting point, there’s three or four building blocks to put on the table and kick around.

Obviously, it’s an order of magnitude, maybe two orders of magnitude, quicker and cheaper to make any given piece of software, which for a couple of years, I compared to AWS that suddenly you get an order of magnitude quicker and cheaper and easier to build software. Okay, great. Step two is, okay, now that software can do a whole bunch of stuff that you couldn’t do three years ago, you’ll have new features and new companies and new software and new tools. Step three is, how far up the stack do the foundation models go? So do you discover tomorrow that the thing that was your product is now just something that ChatGPT does? Or probably a more interesting conversation is, does your set of capabilities no longer make sense of something separate from one of your competitors? The demarcations between different software categories and different functions shift around, you were solving a thing that that thing couldn’t do and now that thing does it.

And then the fourth one, which to me I said on Threads and LinkedIn a while ago, seems to me delusional is — oh, no, no, no, wait, there won’t be software companies, random middle managers and accounts payable inside big companies will just make this tool to do their thing for them.

**Yep, that one’s ridiculous. But I think your number three, that’s the one that I’ve been anchored on. I analogized it to content back in the day, where it’s like if you are a local newspaper and you’re like, “I’m constrained by geography, now I can reach the whole world because the Internet came along” — that’s not so great because everyone else can also reach the whole world now and your competition has increased basically infinitely. This is a similar case where all these little SaaS companies, they just identified one business function, they followed the playbook, followed the recipe, built a startup around that, got to tell themselves they’re changing the world and all those walls, where’s the way to leverage the fact you can make more software? It’s to expand horizontally, particularly if you’re selling into organizations that they’re diverting all their budget to AI as it is.**

**BE:** It’s interesting. So [I’ve published data](<https://www.ben-evans.com/benedictevans/2023/7/2/working-with-ai>) from Productiv and Okta that says that the typical big US company has something between 350 to 450 separate SaaS apps.

**It’s amazing.**

**BE:** Which sounds crazy until you realize it’s like if you’re married or I got married — planning a wedding and you think, “We’ll have a small wedding, we’ll have 10 people”, and then you start making a list and it’s like, “Well, I’ve got a brother and my brother’s married and she’s got two sisters and then there’s an aunt and the aunt has children”, and you realize you can have 5 people or 150 people and it’s kind of nothing in between — it’s kind of the same with enterprise software.

Well, how much software have you got? Well, we’ve got Office and Salesforce and SAP and Workday, and then you realize that the HR team has got seven different things just doing different kinds of training, and you’ve got the graduate recruit hiring thing, and you’ve got the compliance management thing, and the other compliance management thing. And yeah, you’ve got 450 apps.

What each of them are doing is unbundling something — again, building blocks. Firstly, what all they’re doing is they’re unbundling something that theoretically you could do in Excel or Oracle or Salesforce or something or email and it’s a thing that you were doing in email and Google Sheets and you didn’t realize that you could automate it. Then an entrepreneur finds this problem and finds you and comes to you and says, “Hey, I’ve got this thing, it’s $200 a seat, and did you realize you were spending a day a week on doing this thing? Now it’s a button.” That’s what gets you those 400 or 500 apps.

But the thing that I was thinking about that what each of those apps are doing is, I don’t remember if we had this conversation before, but what any GUI is doing is two things. One of them is it’s surfacing out all the things that the app could do, which is why Office has 500 buttons and 500 menu items, and it’s possible to have that much stuff and find it because you’ve got a GUI, you don’t need to memorize keyboard commands. Same with Photoshop, same with AutoCAD, any of these things. But the other side of it is you’re on the screen and there’s five buttons because there’s a bunch of institutional knowledge of working out what those buttons should be and what the steps in the workflow here should be in a predetermined, standardized way that someone has sat down and decided what it should look like.

And that’s the problem both with the middle manager creating software and it’s also the problem with the software becoming much more generalized, because what is the process for working out, “This is how you institutionalize this workflow or solve its problem”? Do you want that to be improvised? Do you want it to be generalized or is it suddenly solved if one entrepreneur works out, “This is the way that you solve that specific problem”?

And so obviously there’s two pathways here. There’s one pathway that says we’re just going to have another thousand people using LLMs to solve some problem that couldn’t be solved before and software companies will end up with — some of those SaaS companies will go away, there’ll be a whole bunch of new SaaS companies. The more weird, fuzzy, speculative one is this kind of changes what software is, and that’s a much harder thing to think about and understand because if you change what software is, who is it that decides that?

**The software is stored processes and just the way something is done.**

**BE:** Yes. Software is somebody sat down and designed a workflow and said this is the right way of doing this. And what’s his name? The manager in The Office, what’s the character called?

**I don’t remember.**

**BE:** The Ricky Gervais character, they are not the right person to sit down and work out what is the right way to do accounts payable for a paper company, and so that’s the entrepreneur or it’s a CIO or it’s a compliance department or something, so improvising software seems like an interesting way of thinking about this. Do you improvise software or do you institutionalize it?

I had this conversation with someone at Walmart six months ago, and the thing that occurred to me was if you’re trying to solve some task somewhere inside a big company, you’ve got the tool in SAP, you’ve got the vertical SaaS tool and you’ve got Excel or Tableau or something. So you either do it in the dedicated horizontal tool or you do it in the dedicated vertical tool or you export it to a CSV and you do it in Tableau or Excel, you write a script or something.

Now ChatGPT or LLMs generically are like, are they a fourth option in there? Is it like I get ChatGPT to do this for me instead of getting Excel to do it for me instead of doing it inside SAP? Is it like another step in that continuum of how structured and systematized do you want to do this? Because if you’re doing the same process three days, three times a day every day and it’s a billion dollars, you’re not going to do that in Excel. You’re going to do that in either SAP or a vertical tool, but you’re going to do it in a tool that somebody else has built and designed. But if it’s just a kind of random one-off thing that you need to solve today, then you won’t have a dedicated tool for it, so you’ll either do it in Excel or you won’t be able to do it.

Now an LLM solves a big class of, “You won’t be able to do it” — maybe, I’m sort of thinking out loud here. There are these sort of liminal spaces between the big LLM stuff and the improvisatory space of “Well, we’ll make an Excel, we’ll make a script, we’ll do a one-off project around this”, and it seems more interesting to think about how LLMs change and expand that space than to say, well, obviously every big company is just going to dump SAP and improvise something in Gemini tomorrow.

**Right. Is this a case where, I think what you’re articulating is very compelling, where there is an embedded value in software that is very hard to articulate, which is you mentioned you do it three times a day and it’s a billion dollars. That’s really worth spending the money to get the right button to make sure that that billion dollars goes down the pike correctly. And maybe that means a lot of these software companies actually retain real world value, but never have stock market value, and the analogy I’m thinking of is Microsoft from basically 2001 to 2015, where the company generated astronomical profits year after year after year, and the stock price was totally flat the entire time. It was stuck at $40 or $45 basically for 15 years — is that maybe the future of software generally where it lasts longer than we think, but no one actually believes that it’s valuable?**

**BE:** That’s funny, what should SaaS multiples be? What should profit margins be for a software company? What do you charge? Well, it’s value-based charging, so what’s it worth? What’s the customer willing to pay for it? How many competitors might you have for this thing? I don’t know. I never thought that the hard part of building a piece of software that manages the thing for the other thing in the thing deep inside a big company was writing the code.

**Right. Completely agree.**

**BE:** That’s not the hard part. The hard part is working out that that problem exists and then working out the right way of solving it and then going out and building a go-to-market and working out how to get your customers to buy it. It’s the implementation, the execution, the route to market, the right way of solving the problem. You remember this phrase that was going around a couple of years ago about thin GPT wrappers, well every one of those 400 apps is a thin SQL wrapper.

**That’s right.**

**BE:** Those 400 SaaS apps, they’re all a thin SQL wrapper, they’re all just databases. It’s like the dumb Hacker News comment, “Airbnb is just a CMS”. But yeah, every social network is just a CMS. Well, great, but Tinder, I mean, even that, Tinder and Hinge aren’t the same at all, and those really are just the same thing and they’re just a database with a social network on top.

Obviously there are exceptions and there are some things where you’ve had to build something very clever around the actual technology. But I always remember when I was at Andreessen Horowitz, we invest in a company called Everlaw, which is cloud legal discovery. You see someone, they send you a truck full of paper, you want software to manage that, and you can immediately start thinking of all the stuff you might want. They run on the cloud, I guess. Which cloud? Does it matter?

**Nope.**

**BE:** Are they worried that AWS is going to come out and compete with them? No. Microsoft, maybe. AWS, no way. And they’re just a database and a user management system and a file management system, but that’s not what they are. They’re a solution for lawyers and no lawyer is going to go and buy an AWS API key for sentiment analysis or translation, they’re going to buy a product with a Salesforce and a support team and a throat to choke — that’s a great phrase.

**It feels like the throat to choke is actually going to become ever more valuable in the age of AI, not less.**

#### AI and Coordination Costs

**BE:** I suppose there’s another way you can think about this because I was at an event, speaking at an event for an insurance company this morning instead of thinking about — I’m sure you know I do [an annual presentation](<https://www.ben-evans.com/presentations>) once a year and I’m now shifting to doing it.

**I was going to ask about it, yes.**

**BE:** Well, I’m now doing it twice a year because stuff is changing so fast. And one of the framings that I’ve been thinking about is that, which I mentioned very briefly in the deck I did last year, [end of last year](<https://www.ben-evans.com/s/2025-Autumn-AI.pdf>), is that the Internet unbundled a whole bunch of things where you had a physical asset and then you had a business that was based on anything, the physical asset, but it never occurred to anybody that that was what you were.

**This is the story of the publishing industry. They were a light manufacturing industry, no one knew.**

**BE:** Yeah, exactly. So it didn’t really occur to anyone in the newspaper that they were a light manufacturing and a trucking company.

**Yep.**

**BE:** And then the Internet comes along and suddenly you don’t need to have stores in every city in the country to run a bank, you don’t need to own a cable network in order to do a TV station and so on. You remember the joke two years ago, Airbnb owns no hotels, Uber owns no car, has no cars, SVB has no money — but the point being though, can you think about LLMs as unbundling in that sense that you’ve got a great chunk of you’ve got a building full of people doing something super boring and that was actually what your business was, although it didn’t occur to you that that was your business. And now you don’t need that building full of people doing something really boring.

**You’re going to be a company that has no employees. Is that the end state here?**

**BE:** Well, it’s not so much that. It’s more like, can you separate out all of the work that was being done to deliver the product from the product? How can you separate that apart? And do you realize now that those are two different, slightly separate things?

I was giving this presentation a couple of months ago, and somebody came up to me who just retired from one of the big four accounting firms, and she said her first job, sometime in the 80s, was intercompany audit. So you’ve got, I don’t know, say it’s BP and they’ve got 75 legal entities and they want to check, “BP Denmark says that they pay BP Morocco this much money, does BP Morocco say that they agree?”, and the way they do this is they get a big meeting room with no furniture and a create a graph paper, and they lay 75 sheets of graph paper along one side, and then 75 group sheets of graph paper down the left-hand side, and then they spend the next three months filling in the floor with graph paper. It’s literally how you did intercompany audits in 1985.

**It’s amazing.**

**BE:** And yet there are more auditors now than there were then.

**Yep.**

**BE:** So a lot of this sort of fuzziness of what was the job, what were you using the software for? What was the software doing? Does the software get broken apart? Does it get combined in completely different ways?

**What occurs to me, and this just came to mind when you were saying that, is one of the great fallacies about the Internet is that the Internet was going to widen the playing field, let a thousand flowers bloom, distribute everything. In fact,[it was very centralizing](<https://stratechery.com/2015/aggregation-theory/>) and you had these big companies, you had so much supply that someone needed to sort of find it, discovery became more important than distribution. Is the analogy for AI that if you think about — an assumption is, “With AI, anyone can start a company, you could have a bunch of tiny little enterprises”, because one entrepreneur can—**

**BE:** Well, look at the two of us.

**Right, exactly, that’s the optimistic case. But what is the limiting function of a corporation? It’s coordination costs, right? At some point you get so large, you just can’t, it sort of falls under its own weight.**

**BE:** You trip over yourself.

**That’s right. But what if AI actually eliminates coordination costs, that actually the net result is we end up with way much larger companies than we ever thought possible, not just in tech, but actually across the economy?**

**BE:** It’s funny, this was a conversation that the Russians had, the Soviets had because what they discover or don’t want to admit or encounter in the ’60s and ’70s is that you can kind of make central planning work when all you’re trying to do is build railway and locomotive and tractors.

**Right.**

**BE:** But once you are trying to make a sophisticated, complex, modern industrial economy, you can’t. It’s just not possible to have one office building in Moscow that’s deciding what everybody in the entire country is going to be doing all day, this is this organization [called Gosplan](<https://en.wikipedia.org/wiki/Gosplan>). Central planning doesn’t work because you just can’t manage that level of information and a free market economy is a decentralized system where every individual person is making those decisions and pricing is the information system where people decide what they’re going to do.

So you could propose that with a computer, you could solve that and of course that didn’t work with mainframes. You could propose that you could do this with LLMs, that you could have a more — you could certainly change a lot of those information flows.

Now, I don’t think anybody in a big company, opening their copy of Outlook at 9 o’clock in the morning and seeing 7,500 emails thinks that the Internet solves this problem. No more memos anymore, we’ll have free flow of information. And then of course Slack, Slack solves the problem-

**Yeah, I was going to say the 750 Slack messages is even worse.**

**BE:** Yeah, Slack solved the problem, didn’t it? Every organization can communicate freely now, so maybe AI solves this.

It did occur to me, I was just thinking out loud that I was looking at all these meeting note takers and thinking, okay, what happens if those meeting notes aren’t just being emailed to everybody, but if they’re actually in a central repository, can you turn those recording into structured data? Can you actually have some sense of what the hell everybody’s talking about and what people are working on and what’s going on? If you can combine that with actually analyzing the entire corpus of internal email all the time and all the calendars and all the meeting notes, would that give you some — I don’t know, I don’t know enough about the history of CRM, but is this what happened with CRM, that before CRM software, nobody knew what the sales process was, and then with CRM, suddenly you could measure what sales calls were.

**Right.**

**BE:** I might be completely wrong, I don’t know, but something vaguely interesting, what would happen if a company actually knew everything that was happening? Going back to your point about supply, it’s something I’ve been talking about for years, that the problem with the Internet is that you have infinite content, infinite media, infinite retailer space, infinite product. Amazon has 700 or 800 million SKUs. So on the one hand, if you want to find that widget and you know the part number, you can get it. But you can’t go to Amazon or Google, and say, “I want a new winter coat”, it’s not going to give you any remotely personalized answer.

In principle, with an LLM, you’re going to solve two parts of this, because on the one side, the LLM could in principle — well, there’s two parts to this. The first of these is that the way that Google and Facebook, and Amazon addressed it is as a [giant mechanical turk](<https://www.ben-evans.com/benedictevans/2025/11/23/ai-networks-and-mechanical-turks>). They see everything that you’ve bought, and everything that everybody else has bought, and they do well. And that’s a network effect, and a winner-takes-all effect, and a barrier to entry.

I wrote something about this at the end of last year, that in principle, an LLM would know those same things without having using any users, because it’s got it from the training data. We got it pre-baked from the training data, which is also a mechanical turk, but a mechanical turk at a different level of abstraction. Theoretically, if you get an LLM as an API, and you can say to it, “Hey, people who bought this, what else might they like to buy?”, you might know that without needing that data. I mean, you wouldn’t have Amazon’s internal data, but you would have a level of, “If people buy this, they might also buy that”, without needing to be Amazon and indeed, you might know things that Amazon doesn’t know.

The other side of it is, you might know what you as an individual might like without necessarily needing to be massively pre-populated, or you might be able to pre-populate it in other ways, which is kind of a roundabout way of saying, I can go to an LLM, and say, “Go look at my Instagram, and then tell me what coat I might like”, and that’s a different way of getting to those recommendations, and those suggestions. You don’t necessarily need the same user base, or maybe not at the same time in the same way, you may be able to suggest different things, and have a different view of the user. The problem with that is if you’re OpenAI, you don’t actually have any view of the user today.

#### The OpenAI Cargo Cult

**Well, I was just going to ask you, are you attempting to articulate a bull case for[OpenAI and advertising](<https://stratechery.com/2026/ads-in-chatgpt-why-openai-needs-ads-the-long-road-to-instagram/>), and whatever it might be?**

**BE:** So there’s a funny thing here that I thought everyone knew what a cargo cult is. Do you know what a [cargo cult](<https://en.wikipedia.org/wiki/Cargo_cult>) is?

**Now I’m nervous that I’m not sure.**

**BE:** The point of a cargo cult is it’s something that happens in the Pacific after the war, which is that you’ve got these people who haven’t really had any exposure to it. They’re not uncontacted, but they don’t have exposure to modern mass manufacturing society. The war comes, Americans built these airfields, these planes land every day, all this stuff comes out. Americans handed out spam, and food, and cooking pots, and all sorts of stuff, all this great stuff, war ends, planes just disappear one day. One day there’s just no planes, and there’s no Americans in the airfield. So, what do you do? Well, maybe if we run the flag up the flagpole again, and salute it, they’ll come back. Maybe if we stand on parade the way the Americans did, maybe that will make the planes come back. Now, I’m not making this up, you can go and see there were studies of this, this is the thing that happens.

**I’m glad I didn’t try to answer, I did not know the answer, that’s good to know.**

**BE:** It’s fascinating. And the reason I mention this is it’s like you’ve—

**So Cargo Cult, they were a cult hoping for the cargo from the Americans.**

**BE:** For the cargo to come back, “How do we get a cargo back?”.

**Got it. Okay.**

**BE:** And so the question is, you’ve got all these people from the Meta team who all joined 10 years after Meta had product-market fit. You’ve now gone to work at OpenAI, and they’re like, “Well, how do we get growth?”. Well, what happened before? Oh, you need an app store. If you have an app store, then you’ll have defensibility.

**Yep.**

**BE:** We need ads.

**Right, and they tried to GPTs, yup.**

**BE:** Yeah. If you have ads, then what do platforms do? Well, they have ads, they have an app store, they have a developer conference. And it’s like, but why is it that the app store, what problem was the app store solving? What problem was it that the developer conference was solving? Well, that’s not a problem that anyone has now.

And well, obviously we’re going off in lots of different directions, but to me, the defining question for OpenAI this year is that the models remain fundamentally commodities, which is a statement that a lot of people in tech really struggle with, because if you use them every day, you see them as different, and this is better at code, and that’s better at images, but 80 to 90% of people who use ChatGPT use it once a week, or twice a week, and don’t see those differences. There’s not any apparent reason why one of these models would be defensively sustainably better than all the others, there’s no winner-takes-all effect yet. Maybe there will be, but right now there isn’t.

So, you’ve got fundamentally an undifferentiated technology, or differentiated except at the margins, and you don’t really have product-market fit. And you’ve got 800, or 900 million users, but they’re weekly active users, not daily active users, they haven’t really formed a habit. And so you are frantically trying on the one hand to get infrastructure, and on the other hand, to get product, and defensibility, and experience on top of the model so that you have something defensible. So you build an app store, and you build a video sharing thing, and you build a developer platform, and you try, and build all this stuff so that you can compete on top of the model because the model itself doesn’t have competitive differentiation in any kind of systematic, sustainable, strategic way.

Part of that is building APIs for developers. Going back to the cargo cult thing, Sam Altman did this livestream towards the end of last year that I thought was fascinating in that he used the Bill Gates quote about the definition of a platform is that it produces more value for the people building on it than the platform in it, and he showed this classic stack diagram of, “Well, you have the hole of the bottom, and as you go up, there’s more, and more independent stuff, and third parties”, and so on. And like, well, we’re going to be like Windows, we’re going to be the Windows of AI, he didn’t say it explicitly, but that was clearly the point.

I kind of looked at this, and said, “But you’re not Windows, you’re AWS” — if I use a third-party app, any of the apps that we were talking about at the beginning of this podcast, whatever they are, whoever they are, what their margins are. As an enterprise, I don’t care if that runs on Anthropic, or Google, or OpenAI, any more than I care whether it runs on AWS, or GCP. As a law firm, I don’t buy a subscription to Everlaw, and log into it with my AWS account, that’s not how any of this works. And as a law firm, I’m not going to buy an AI-powered legal tool, and log into it with our corporate OpenAI account, that’s not how this works either, that’s their problem, that’s the software company’s problem.

**It’s interesting, you might worry about it if you’re doing coding, so you’ll put in your API key because you prefer one model over the other, but you’re very tuned into the differences. Is there a bit where coding seems so well-suited to probabilistic AI models in that it’s a deterministic outcome and so you have this sort of virtuous cycle where it can check itself, correct itself, it either runs, or it doesn’t, it can write its own unit tests, all these sorts of pieces, and is there a bit where actually the entire industry is over-extrapolating from this specific use case to all these other use cases, both in terms of how viable they are, but also in the terms of to what extent people care about what’s underneath it?**

**BE:** And you could possibly, suggesting that people in the tech industry have a slight tendency to being self-involved because that would be a really radical suggestion.

**(laughing) I mean, imagine not only could you code, but you could also have your LLM choose your flights for you. What are the chances?**

**BE:** Yeah, my LLM will just choose my wardrobe because the defaults are fine. And what do you mean there are different clothes? Why would you care?

**That’s right. Black turtleneck, jeans.**

**BE:** Yeah, exactly, the hoodie. So I think absolutely, for whatever reason, the things where generative AI works really, really well out of the box without any kind of wrapping, or tooling, or evolution, or anything, is software development and marketing.

**Yep and one of my questions later on is, Google and Meta are really just the only winners here, but continue.**

**BE:** And one of those is, and [I did a podcast last summer with Balaji](<https://youtu.be/ne2MF-mTpLg>) in Singapore, [Balaji Srinivasan](<https://x.com/balajis>), who used to be a partner at A16Z when I was there, just as institutionally challenged as I am.

**In the same boat.**

**BE:** We kind of combined our two framings, because the framing I was thinking about was, there are questions that don’t have right answers, or don’t have precisely right answers. “Suggest 10 ideas for this”, generally doesn’t have a precisely right answer and his point was, and the other side of it is, is it tactical? So can you mechanistically test whether the outcome is correct? Is there not really such a thing as a wrong answer? And my point was, is it easier to check it than to make it? So, at your marketing team, you want 300 images, you get ChatGPT to make 500, you pick 50 that are good, that’s still way more efficient than making 50 yourself.

**Especially when you could just automate the checking by running actually A/B tests, all of which the failures don’t matter.**

**BE:** Well, but the first step is checking that you haven’t got Chinese Nazis, or something in your pictures. You’ve got to make sure that the pictures are like, you’ve got to have the human in the loop, just to look at the images to make sure you haven’t got a cat with six legs, or something first, but it’s very easy to check that. It’s a lot easier to see, “Does that cat have six legs?”, than to make a fairly realistic image of a cat.

**Yep.**

**BE:** That’s kind of my point. Then as you get away from that, then progressively it becomes harder to see what you do with this and it needs more tooling and more use cases, and more people sitting down and saying, “Well, we’re going to wrap it in this product for you”.

Meanwhile, software developers are generally quite free to decide how they’re going to do their job and so yes, absolutely, the place where this really, really works for software development, and entrepreneurial, and for entrepreneurs, it’s also like the people who use Notion, using Notion as an archetype, people who use no-code, the certain kind of person that thinks about how they can optimize their job. And for that, this is life-changing.

But the analogy, and I’m sure that I used this analogy last time we spoke, is imagine you are a lawyer seeing the first spreadsheet, the first software spreadsheet, and you would think, “Well, I’m sure that’s life-changing for an accountant, but I don’t use spreadsheets, maybe I’ll use this for my time sheet next week, but that’s not what I do all day”, and that’s almost literally what a lot of people do when they see ChatGPT. They say, “Well, I’m sure that’s great if you’re a marketer, or a coder, maybe I’ll use it for my time sheet next week, but that’s not what I do today”.

**Well, I was going to ask you, you do your[AI Eats the World presentation](<https://www.ben-evans.com/s/2025-Autumn-AI.pdf>), and I was going to ask you what’s the biggest change that has happened? Because I asked you about the same presentation last year, but you said you’re updating it twice a year, but what you’re actually saying right now is there’s actually a very core question that hasn’t changed at all.**

**BE:** I think from end of 2021 through to well into 2025, nothing had really changed. This stuff, the models are scaling, it became clear very quickly that it wasn’t just going to be OpenAI, and then what? And now we have much more of a sense of divergence of okay, “Google’s now in the game”, and going back to OpenAI, you’ve got, “If the model’s a good commodity, how do you differentiate?” — well, you can make the chatbot itself different, but how would you make a chatbot different? That’s kind of like saying, how would you make a web browser different? It’s got an input box, an output box. What would you do that would make yours different from anybody else’s? Or you make dedicated vertical features around it like Sora, but then you are competing with the entire tech industry to make dedicated vertical apps.

**Or you’re going to make a device, and now you’re competing with Apple out of nowhere.**

**BE:** And you are trying to invent something better than a smartphone, which is, well, that’s worth a try, but that’s not a strategy that you can plan for success in.

I remember 10 years ago, let’s try, and build a DCF value for Apple’s next product, but we don’t know what it is, how did you value that? All you can do is you can think about this as adding features, and capabilities to existing products, which is obviously what Google and Meta, and Apple are doing, etc., except as OpenAI, you don’t have existing products, you can’t add AI Overviews to Search, you don’t have Search.

And I think if you look at the usage right now, what you see clearly is Google and — it’s very fascinating to me is that Meta AI is almost as big as Google, as big as Gemini, and in tech, Meta AI has been written off as the laughing stock, but the model isn’t bad, and it’s got distribution. So you’re ChatGPT, you’re OpenAI, you’ve got a commodity technology, knowing when it takes all of that, it’s very, very shallow usage. And you’ve got all these people who’ve got basically the same product, but they’ve got distribution. So what are you going to do? Are you going to compete with Y Combinator at inventing cool consumer apps? Are you going to compete with Y Combinator at making 50 cool new enterprise use cases? Are you going to try and be the best API solution? Fine, but you can have a whole conversation about why AWS beat Google, but that’s a very different kind of strategy. Are you going to build an ad business? Well, the ad business, I mean, I think you’ve talked about this before — on the one hand, can you lock in a big user base by making it free and sustainable, and giving everybody the full fat product. You saw [DeepMind CEO] Demis Hassabis [throwing shade at Davos](<https://www.youtube.com/watch?v=tDSDR7QILLg>) saying, “Well, it seems a bit early to be degrading the user experience like that.”

**Right. Especially — Demis, what sort of business model funds your model?**

**BE:** Yeah, it’s easy to say that when you’ve got the cashflow to pay for this and clearly a lot of the OpenAI story is you’re trying to get to the point that you can compete with companies that have cashflow when you don’t, or you don’t have the same kind of cashflow, but you’ve got this question of, “What would the experience be?”. The challenge for the ad model is, how much does OpenAI really know about you, compared to how much Google knows about you, or Meta knows about you?

**The initial ad product is so bad. To your point, it sort of stuns me with having all these Meta AI, but I thought your cargo quote was very compelling, you would think people coming from Meta would have a better point of view on this than when you put out your ad principles, and your ad principle is, “Our ads are not influenced by the conversation”, and your ad is explicitly influenced by the conversation, it’s like my T-shirt is disputing the thing that my T-shirt is, or whatever the phrasing is.**

**BE:** The thing I always think about, and it’s going back to what I was saying earlier about because the LLM can both understand things and suggest things in ways that Google and Amazon couldn’t do, All of these kind of companies are like the story of the blind men feeLing the elephant, and one person feels the legs and says it’s a tree, and somebody else feels the tail and says it’s a snake. Meta, Amazon, and Google have a different view of who you are, and what you’re doing And Amazon doesn’t really know why you bought that And even if you were like — this is what the Chinese Android companies do is scrape everything into, that’s happening inside the app, you still don’t know why.

So, remember when OpenAI launched a web browser, what happened to that? But imagine you were using that web browser to access Instagram. Well, maybe it would kind of know what the pictures you were seeing in Instagram were, but it wouldn’t know the graph behind that, it wouldn’t know why Meta was showing you those pictures. Each of these companies gets this very different view of who you are and if you’re the 80 to 90%, there’s a cash point too here that just occurred to me as I’m talking about this, if you’re only using this once a week, so you’re not paying for it, and you’re getting the ad-funded product, then you’re not using it enough for the ads to be any good. The only way that the ads are going to be any good is if you’re using it enough that you pay for it, and don’t have any ads, does that make sense?

#### LLM Knowledge Gaps

**Totally. It’s funny because this is almost like the LLM problem generally. A friend of mine made this observation ages ago, which is, “It’s all well and good to get all the text on the Internet” — what you’re missing are all of the thought processes that went into generating that text, you’re fundamentally training on finished products.**

**BE:** Oh, yeah. There’s so many different places where we can say this. So just put two, or three of these on the table. Firstly, they don’t have anything from inside any enterprise SaaS app, they have no idea what’s inside Salesforce, they have no idea what’s inside MasterCard, they have no idea what’s inside Amazon, or inside Meta. They don’t know any of the stuff that any enterprise software company knows about what the product is, how it works, what people do with it. They kind of can read the public API docs, but they’ve got no idea how that relates to anything. Same thing for your e-commerce purchasing.

This was a thing that was amusing me looking on social media a few weeks ago, is all these idiots who say that LLMs will destroy McKinsey — you have no idea what McKinsey does, McKinsey’s business is not making slides, that is not the job.

**Yep.**

**BE:** That’s not what they do.

**That’s an output.**

**BE:** That is a work product, that is not why you hire them, that’s not what they’re doing all day. And you have no idea what those conversations inside those companies are, which is actually the point I was making earlier about the note-taker. Maybe the note-taker means that the company does know what the internal conversations are. And yeah, absolutely, the LLM doesn’t know why you made that slide, it doesn’t know why you made that model, it doesn’t know why that purchase happened, but it knows a bunch of other stuff.

I’m kind of circling around this again, I did an imaginative slide in a deck I’ve been using lately, where I said, “Look, Amazon knows that if you bought packing tape, you might want bubble wrap”, it should know that you might also want light bulbs and smoke alarms, you’re moving home. It probably doesn’t, but it probably should know that.

**Right.**

**BE:** But they won’t show you home insurance ads, because they do not know what packing tape and bubble wrap are, they’re just SKUs, this is the thing I keep thinking about.

**[My Meta bull case](<https://stratechery.com/2024/metas-ai-abundance/>) from a while ago is every pixel on the screen is now understandable. To this point, they should know what bubble wrap is, they should know what packing tape is, that’s now possible.**

**BE:** They don’t, here’s the thing, Amazon doesn’t know what that thing is, it knows it’s a SKU, it’s got the metadata from the manufacturer, it doesn’t know what bubble wrap is, and it doesn’t know why people buy it. It just knows that people who bought this, bought that. I mean, you get all the jokes about, “Dear Amazon, I bought a toilet seat, I’m not collecting toilet seats”, you ought to be able to fix that with frequency analysis. Nobody buys five toilet seats, you should know that. That’s like database analysis, and yet they don’t, but there’s a sort of profound shift here with an LLM, and the LLM should know that, and it should know that without needing the user base. You shouldn’t have to be Amazon and have all that transaction data to know that people that buy packing tape by bubble wrap, and you shouldn’t need that user base to know that, therefore, you could show them that sell them a home insurance ad.

I think that shift in how is it that managing the infinite has worked for 30 years, you have to have an enormous user base and do a shit-load of correlation analysis on it, that’s the only way you can work out what those billions of webpages and billions of screws are. Now LLMs might change that. I mean, their system would actually know what the pixels are, and not just know it’s a code, but know what kind of code and why.

**Exactly. The thing I always go back to is, what’s the core user interface of the web that underscores the Internet’s business model, which is advertising?[It’s the feed](<https://stratechery.com/2015/facebook-and-the-feed/>), and the feed wasn’t invented until 2008 or whatever it might be, a solid 15 years after they came along.**

**BE:** Yeah, it’s a Facebook thing.

**Right, and there’s a bit where, no matter how fast the technology progresses, the fundamental limiter is the human imagination for what this can be used for, and maybe it requires a generational change. It requires the sort of 23, 24-year-old Harvard dropouts that weren’t stuck in any old paradigms and, definitionally speaking, we’re not at the LLM-optimized business model stage, because everyone who’s working on LLMs is just functionally incapable of figuring out what they’re actually good for.**

**BE:** Yeah, going back to my unbundling framing, one of the things I wonder about is, do you separate out the function from the experience? Which I haven’t quite worked out, what’s the right word to describe this? But on one side you have, “I want the logistics of getting the product from Amazon, I just want the answer, I want to know what time that flight is, I want to know the weather tomorrow, I want an output from a database or some physical logistics fulfillment product of some kind, just give me the response, and give me the answer”. On the other side is, “I want to be entertained, I want authenticity, I want experience and curation and suggestion and help and amusement”, which is why is it that I go to a bookshop rather than go up ordering something on Amazon?

Shopping for books, shopping is a leisure activity, which is one of these things that engineers in Silicon Valley don’t really understand, which is also, what is it that you’re buying from McKinsey? You’re not buying the slides, you’re buying something else. It’s not the same thing in music. You’re driving an Uber all day, do you just want generic, soft jazz to fill your time, or do you care about Taylor Swift’s authentic human experience? Do you want utility, or do you want experience, authenticity, personalization, specificity? Do you want self-actualization? Throwing all of these words out there, all sort of too fuzzy.

**Maslow’s Hierarchy, we’re never getting away from it.**

**BE:** Yeah, exactly, but there’s two fuzzy clouds of what it is that you want here, which is why we have Amazon and Walmart, and yet we also have boutiques and we have independent retailers, because they’re serving different purposes. A retailer is not just the endpoint to a logistics system, and the LLM unbundles those capabilities for a whole bunch of stuff where you couldn’t do that before, and changes how those recommendations and discoveries and suggestions might work.

I mean, I remember way back in the early days of the Internet. Do you remember [Jakob Nielsen](<https://en.wikipedia.org/wiki/Jakob_Nielsen_\(usability_consultant\)>)? You remember all that stuff? This was like a thing in the 90s.

**It sounds familiar, remind me.**

**BE:** There was this whole argument about, is the Internet an information system or an interactive experience? Should your website basically be black-and-white and have three things that just say, “Here is the information you want”, or should it be about brand and experience and emotion? Which is the argument, the answer that Google won. What is it, and why am I looking at that webpage? Why am I scrolling? What am I looking at? Why am I doing this? Do I just want the answer from ChatGPT, or am I going to enjoy looking at stuff for half an hour? That’s been the tension in the Internet for the last 30 years, it’s why people get angry about feeds.

#### New Paradigms

**On the feed point, and this goes back to the software bit, where both of us poo-poo immediately, this idea that middle managers should be running their little bits of software, XYZ. You could go back to 1993 and poo-poo with the idea that user-generated content is going to be what people look for on the Internet. It actually just took 30 years — a lot of this, there’s a time horizon aspect to lots of this, you mentioned, you go back to the Facebook and the feed and advertising. I remember early on in Stratechery, people would be blaming Facebook for destroying the advertising model for newspapers and things along those lines. I put a graph up ages ago that showed, actually, Facebook’s revenue ramped well after all the newspaper advertising revenue was destroyed, and I think there’s an aspect of these new paradigm shifts when they’re as large as this one is. You mentioned the unbundling and the bundling, it’s like the destruction happens first, the destruction and the value creation are not simultaneous in time. First, there’s a lot of destruction that happens, the unbundling aspect of this, and then people are freed up to figure out the new thing, and that’s when the value creation happens. Maybe this goes to the software bit, we’re just looking at a lot of value destruction right now, the actual value creation is TBD, but it definitionally is going to happen in the future.**

**BE:** Yeah, it’s amazing, we’ve got over 45 minutes into this and haven’t mentioned [OpenClaw or whatever it’s called today](<https://www.macstories.net/stories/clawdbot-showed-me-what-the-future-of-personal-ai-assistants-looks-like/>).

**[OpenClaw, that’s a good name](<https://dithering.passport.online/>), I think they’re going to stick with this one.**

**BE:** It’s funny how open source projects always run to anthropomorphic names. I think there’s a lot of things you could say about it. As a comparison, with the urge to homebrew, like the [Homebrew Computing Club](<https://en.wikipedia.org/wiki/Homebrew_Computer_Club>), the desire to build your own thing to host it yourself, the desire to break out of all the silos of the individual cloud models, just build your own thing, and connect them altogether however you want. It’s also like a pent-up demand for an AI assistant of a kind that, as we have both talked about, [Apple showed this brilliant concept](<https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/>).

**Is OpenClaw actually very bullish for Apple and Google at the end of the day?**

**BE:** I still think that Apple showed this almost unmatched concept for what an AI assistant could be. Then, we realized, “Wait a minute, you are proposing a multimodal, agentic tool using, dynamic, real-time, on-device LLM assistant that’s completely immune from prompt injection”. Okay, Apple hasn’t shipped this, we’re what? Two-and-a-half years later, it’s not like Google’s got that working either. It was just way, way harder than I think Apple realized.

**But it also doesn’t mean they were wrong, maybe that’s the answer.**

**BE:** But this is the thing about OpenClaw, is then everyone starts pointing to the security questions and the usability and the safety questions — I was throwing out scenarios, but imagine if you tell it to go look at Salesforce email in your calendar and print out a really neat, elegant, beautifully designed infographic every morning. So, it would install these APIs, and it would plug into each of these tools, and it would go to Nano Banana, it would make you a cute infographic. You would say, “Can you make it a bit tidier, because those names don’t fit?”, they would say, “Absolutely”, and it would cancel all those plans.

**Delete everyone with a name longer than 13 characters.**

**BE:** Yeah, exactly. It sounds like a joke, but no, it would do that, it could very easily do that, and that’s the difference between the fun open source project that you install by typing into the command line on your Mac, which I would be willing to bet 95% of people with a Mac have no idea there is a command line, I’ve never used it, like you said, out of curiosity. An actual product that you can give to billions of people is way, way harder.

There’s a sort of generic problem with LLMs, is they give an amazing demo, the demo is always absolutely mind-blowing, and then you’re like, “Yeah, but okay, I’ll ask this okay, that didn’t work”, but it shows the pent-up demand for something that strands through our conversation, it shows the pent-up demand for new computing paradigms. This is the thing I talk about a lot, is each of these new things, step one, is you do the old thing, but with the new tech. Yahoo has a mobile app, Flickr has a mobile app, and it takes a while to get to Instagram and to work out, “No, this is the new thing that’s native to the new form, that isn’t just the old thing on the new thing”.

Then, it takes even longer. It’s like, step one is Flickr’s mobile app, step two is Instagram, step three is Snapchat where you actually say, “No, we’ve got a camera and a touch screen”, because Instagram didn’t use the touch screen at all. You really start thinking about what is truly native to this experience and right now what everybody is doing is doing the old thing, but with new thing. We’re doing software development, but faster, we’re making more ads. I mean, you remember the joke, “Half of AI will be turning three bullet points into email, and the other half will be turning emails into three bullet points”.

**That’s right.**

**BE:** What’s actually happening is, half of AI is turning three bullet points into 300 ads, and then the other half is, “Wait, who’s looking at the ads? How does that work?”.

**Is there a structural ad problem in the long run? Because the more transparency, everyone’s like, “Oh, look, I did all this research, the LMM matched it”, It’s like, yes, that’s basically it, but now if that’s available to everyone, I’m obviously one of the world’s biggest ad advocates, everyone’s always bearish on it, I get a lot of traction saying, “No, actually ads work very well, they’re not going anywhere”, is this the time that the ad bears are finally right?**

**BE:** I think you could make a list of litmus tests for idiots like, “Consultants are all stupid, equity analysts are all idiots, private equity is evil, facebook sells your data, advertising is evil”.

**“It doesn’t work”.**

**BE:** “It doesn’t work”, yes. Well, there, you’re just delusional. but there’s clearly a bunch of questions around what is it that the ad is doing, and clearly Google advertising was this completely new conception of what advertising would be. Then, Instagram and interest-targeted advertising like that was also a completely new conception of what advertising could be — also, of course, unlocked massive audience and massive base of people who couldn’t advertise before.

Again, there’s a step one, step two. Step one, I go to an LLM and ask for advice on life insurance, and I get a lot of insurance ad, easy. Step two is I ask the LLM, “Talk me through how life insurance works”. Step three is, “Yeah, okay, ask me some questions, and then just buy me the life insurance”.

**Right, and step three is you’re researching skydiving and then you get a life insurance ad.**

**BE:** Well, yeah, I’d expect that life insurance companies probably don’t want to sell you life insurance.

**(laughing) Good point, fair point.**

**BE:** That’s on all the exclusion lists.

**I’ll tell you what step in though is, where these platforms, the most successful platforms, Meta’s the best example of this, create their own advertisers, because they make possible all these sorts of businesses. In the long tail, you talked about the self-serve ads and reaching the entire world as your audience, but the problem is that it’s a very long path to get there.**

**BE:** I think, again, this would come back to the engineer’s fallacy of there’s the right product. Why would you go to a bookstore? Just get it on Amazon. Well, because I go to a bookstore, I don’t know what book I’m going to buy, I spend an hour looking, it’s the difference between, “Do I want the answer, or do I want the experience? Do I want to know about something I didn’t know existed?” — I buy lots of things that I see in Instagram ads, because they’re very personalized to start to me, and they’re stuff I wouldn’t know about. The ad buying mechanic is a filtering system that surfaces stuff of sufficient value and sufficient interest and sufficient relevance to me, that it’s effective as a discovery system. Again, you have people who install ad blockers, they say, “Well, I just don’t want to see all that garbage, it’s a herpes of the Internet”, you think, “Okay, I don’t know what websites you’re on, but I don’t see ads with malware, which place exactly are you looking at?”.

**Instagram ads are amazing, number one, and number two, my biggest realization since moving back to the US is US Instagram’s are especially amazing. It turns out being the largest consumer market in the world gets you some amazing stuff, and I spend way too much money on it.**

**BE:** It does. I used to tease people at Google that, if Google really worked, it wouldn’t need advertising, because I would just always have the right result at the top of the feed anyway.

**It turns out they could sell that too!**

**BE:** It turns out they can sell that too. Of course, now AI-generated video means there’ll be a whole new wave of advertising as well, and that will be more effective or more immersive or something, because now anybody can have video for free or for cheap in ways that weren’t possible in the past.

You go and look at the numbers, and the global ad industry is a bit over $1 trillion dollars, and outside of China it’s, I don’t know, $800 or $900 million, and half of that is Google and Amazon, and Amazon, of course, and better. The thing I always used to think about looking at advertising was that, these are charts I made a couple of years ago, is that you should put advertising in the same TAM as retail rent and shipping and returns and credit card processing. It’s everything that you spend to each customer, should we open stores there or just advertise? And of course, that wasn’t a question you could ask before the Internet.

How much will AI change how I find these things? Well, it will change how you find things the way search did or the way social did, but that doesn’t mean that people aren’t going to have budget to reach you and to put themselves in front of you, and that there aren’t going to be people who’ll say, “Well, we’ll take that money, because the alternative is subscription”. We know it’s like the Churchill quote, “Advertising is the worst business model, except for all of the others”. Here were are where hilariously, here’s ChatGPT, this amazing transformative thing — only 5% of people are paying for it.

**I just want to double down on that point, because I think it’s a super important one. I had this discussion with someone who works in a CPG industry, broadly defined, and I urged on him strongly, as he was organizing a new business, I’m like, “Your advertising should be a COGS item, it should not be in sales and marketing, because if you’re selling through online channels, it’s just a part of every item that’s sold”, and when you’re in internal discussions in your company, actually the accounting really matters in terms of where that slot’s in, and I just think it’s a super important point, that people don’t think about advertising or they don’t think about accounting and where stuff winds up, but when it comes to internal turf battles, it matters. If you’re selling online, it’s a COGS, it’s not S &M.**

**BE:** The generalized point here, that you have to consider all of those things as one budget and all of them is interchangeable, it’s no longer, “Well, we have to have a store, and we have to have advertising, and how do we allocate them in different places?”, they’re all part of, “How is it that you tell your customer that you exist”, and, “Do we do free shipping, or do we do have more ads, or do we do free returns, or do we open a store?”. Well, that all becomes one question, and how the LLM thinks about you, suggests you to people, suggest to people that look at you, surfaces you in different ways, they all flow together.

#### Smartphones and Supply Chains

**Circling back to, we first talked, years and years ago, about smartphones, and there’s like 47 questions on here, but I think one of the most interesting things is, as AI in the infrastructure build out is taking over the entire supply chain, how much spillover do you think there’s going to be on consumer electronics on smartphones? We see memory prices going to the moon, and for Apple specifically, how do you think they’re going to handle not calling the shots in the supply chain, or are they still going to call shots in the supply chain?**

**BE:** [I was listening](<https://thecircuit.fm/>) to our old podcast companion, [Ben Bajarin](<https://x.com/BenBajarin>), and talking about this with [Jay Goldberg](<https://x.com/jaygoldberg>), and now we’ve gone from a power generation crunch to a memory crunch in the deployment of data centers.

So look, right now, AI is not a reason to change your device, because it doesn’t run on the device and you don’t have enough consumer awareness, it doesn’t run on the device anyway. Apple has put a few things onto the iPhone, some image editing stuff that runs on the device, but there’s not stuff there that’s a reason why you would upgrade your computer or upgrade your phone. If and when the new Siri launches and it’s a big deal as we get — Google’s been edging stuff onto Android, but Google has this fragmentation problem where you really know what the device is, and what it’s going to run, and how fast it is and so they’ll say, “Google Assistant (or whatever it’s called) is on this many Android devices”.

**What does that mean?**

**BE:** Yeah, what does that mean? If I buy an Android phone, am I going to have this Google feature, yes or no? Which is of course the problem that Microsoft had 30 years ago. I suppose the point is right now there’s not a reason for AI to drive you a new device, that might change dramatically this year. Part of the point of OpenClaw is you’ve got stuff on the device and you’ve got the stuff on the device that’s deciding which giant model in the cloud you should use and how do you move stuff back and forth.

Apple’s vision of Siri is the same, stuff on the device and stuff in the cloud, it’s going back to what I was saying about this is the year for OpenAI. They’ve got to go beyond just having a model like everybody else’s model, because if that’s all they are in a year’s time, they’re screwed. This is a year of product, as opposed to models perhaps and product may well in part mean stuff running on device. So that might be a reason to upgrade the device, that’s one device conversation.

**Right. But how much is the device going to cost? If it’s going to run on a device, you need more memory.**

**BE:** Yeah. What’s the memory going to cost? I don’t know. I’m writing something about OpenAI at the moment, and I’ve done a version of the bell curve IQ meme of there’s a genius, and the idiot, and the guy in the middle. And the way I did it was the guy on the left-hand side is saying, “Computers get faster and cheaper”, and the guy on the right is saying, “Computers get faster and cheaper”, and the guy in the middle is like, “Data centers, water cooling, EUV, memory bandwidth”, and I feel slightly guilty, because there’s lots of really, really clever people working on EUV, and memory bandwidth, and stuff. But for everybody else, who cares? So computers get faster and cheaper. What happens this year? I’m not a TSMC shareholder, I don’t care. I’m not an Apple shareholder, I don’t care. Yeah, yeah, this year there’s an awful lot of supply crunch stuff going on. This year, next year, we could see a lot more breakout consumer stuff that’s actually a reason to buy a faster phone, so there’s one piece. There’s the glasses and VR piece where there’s nothing we can say that we didn’t say five years ago and that may be the case in five years as well. [Meta CEO] Mark [Zuckerberg] is still spending $5 billion a quarter.

**Yeah.**

**BE:** $4 billion a quarter, $20 billion a year, nothing to show for it. That’s unfair, but it’s also true. Sorry, boss. Then there’s the wearable stuff, which apparently is going to ship the second half of this year. How can you judge a thing that you haven’t seen that doesn’t exist yet? There’s a view here that says, “What if the computer just knew way more?” — if the computer was ambient, if it was with you watching, and hearing, and listening, and then you could just say, “I met somebody at a party two weeks ago who was an SVP at Disney, what was their name?”, “What language do my doormen speak? I keep hearing them speaking something, it sounds vaguely Slavic, what language is that?”, “I saw a poster for a thing yesterday, what was it?”. Is that a microphone? Is it a wearable camera? It’s this ambient, this computer? Is it outsourced memory? What is it? Is there some vision in there of something that could solve problems? I don’t know.

You could come over all cynical here and say, “Look, Jony Ive made hardware, he didn’t do the services, or the software, or the UX, or any of that stuff, he made a brilliant, beautifully engineered box to put Craig Federighi’s software inside”. That’s not true, but it’s kind of true. There’s a whole bunch of other people at LoveFrom who were building beautiful experiences in software and so on. But, look at the Watch, the Watch is brilliantly successful, it’s a couple of hundred million unit install base, it’s a smartphone accessory, it’s very tough to replace, and go back and look [at the pin](<https://en.wikipedia.org/wiki/Humane_Inc.>) from the couple from Apple.

**Yeah, Humane.**

**BE:** The problem here is your vision that you are going to replace the phone? You can’t. Certainly not yet. Maybe in N year’s time, but right now, no. I’m still going to need my Uber app, and my Instacart app, and my web browser and someone sends me a picture and I need to see the picture. I mean, at the core of it, someone sends me a text message with a picture of their dog, I want to see the picture, I need a screen, and then I’m going to need WhatsApp and I’m going to need the whole app ecosystem and you can’t just go and get rid of that by hand-waving and say, “Oh, it’ll be an app inside ChatGPT” — shut the fuck up. So then it’s a smartphone accessory and so then it’s a partner to my iPhone or my Android, and immediately now we’re having a different conversation, aren’t we?

**Yep. You could say the counter would be people said that about the PC and the phone came along, but there’s a physicality to it, which was the PC by definition could not be with you everywhere. Is the phone basically sufficiently mobile that everything in the future is going to be a phone accessory, and that’s just the reality of it?**

**BE:** There’s a line here that something like history teaches you nothing, or history doesn’t repeat, but it rhymes or something. One goes back and looks at the phone and you still find people who don’t accept that the phone has replaced a PC as a center of the tech industry who still don’t get it. But, for any consumer, yes, they used Excel at Salesforce or Oracle at work, but there was nothing that they did on their PC that they couldn’t do on an iPhone 3 or an iPhone 4, literally nothing that a normal consumer did on a PC that they could not do on their phone. Maybe filing your taxes once a year, or making a complicated plane purchase, flight purchase, but there was almost literally nothing that you did not do on your phone and your phone was better on a whole bunch of other axis. A device with no screen?

**It’s worse.**

**BE:** That’s a completely different conversation.

**Yeah.**

**BE:** Okay, so it’s got a screen, maybe it’s got a roll-up screen. So now you’re trying to compete with the iPhone or Android ecosystem, I think it’s a bit tough to do that.

**This is the most full circle possible conclusion I think for us. It’s not going full circle under the 3 years we’ve done this, it’s going back to 15 years, when we first started writing on the Internet.**

**BE:** I mean, remember the Windows Phone people who would say, “Well, we don’t have all the apps, but we’ve got the ones that matter” — no, you don’t.

**Yep.**

**BE:** And then they would say, “Oh, but we’ll have all the Windows apps because people with Windows apps will write them for Windows Phone” — but Uber doesn’t have a Windows app, what are you talking about? There was an awful lot of wishful thinking there.

Beyond this, what can we say? We’re speculating about a thing that we haven’t seen, maybe it will be magical, maybe it will be completely orthogonal and it will change how we think about something that we hadn’t thought about before. There has to be something in there, it’s what we keep coming back to of the step two of how do you instantiate these capabilities into new software experiences, not just better dictation and a button that lets me edit the picture better. How do you really shift those experiences?

It’s funny, we’re talking about user experience in SaaS, it’s hilarious looking at, again, ChatGPT is open on its public comments, they started talking about a capability gap, which is the model can do way more than you realize. When I was a kid, we called that not having product-market fit, that’s what you’re there, you’re saying you don’t have product-market fit.

**This is when they were bragging about their revenue scales with compute — I as a tech company[would not be bragging that my revenue is gated](<https://stratechery.com/2026/ads-in-chatgpt-why-openai-needs-ads-the-long-road-to-instagram/>) by my costs.**

**BE:** Yeah. That’s like Walmart saying, “If we build more stores, we have more sales”. Well, yeah, but that’s not a winner-takes-all effect, that’s not a virtuous circle. Like, “We built a bigger pipeline, now we’re shipping more gasoline” — okay?

**That’s not demonstrating scalability.**

**BE:** But, going back to the device, there is a fundamental UX challenge in that most people can’t think of anything to do with this most of the time or only occasionally and that is the entrepreneur’s job, the engineer’s job, the software developer’s job. It’s not the user’s job to work out what the technology is for. Some of that is new app and new experiences, some of that’s new features. It might be a new device, but the device has to be built around a really coherent vision of what it is that this is doing that you couldn’t do before that makes your life better.

**Well, Benedict Evans, this is great, and we got through four of my questions, but that’s exactly what I like.**

**BE:** Yeah, I’m sorry, I talk too much.

**No, it’s fantastic, this was really fun, we should talk again soon. Everyone should go to[ben-evans.com](<https://www.ben-evans.com/>) and subscribe to your newsletter. Subscriptions still work on a small scale, just not for big companies.**

**BE:** They do, yes.

**Very good. And, check out his[AI Eats the World](<https://www.ben-evans.com/presentations>) presentation, you’re updating it twice a year, instead of once a year, does presentations all over the world, you can check out his website. Great to talk to you.**

**BE:** Good to chat.

* * *

This Daily Update Interview is also available as a podcast. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Daily Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a supporter, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
