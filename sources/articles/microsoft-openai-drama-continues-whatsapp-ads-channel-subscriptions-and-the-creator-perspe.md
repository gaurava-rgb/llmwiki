---
title: "Microsoft-OpenAI Drama Continues, WhatsApp Ads, Channel Subscriptions and the Creator Perspective"
reader_id: "01jxzkq1thcja28bfmrds0836g"
notion_page_id: "3484ebe7-f118-8127-92aa-c992f936a533"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01jxzkq1thcja28bfmrds0836g"
source_url: "https://stratechery.com/2025/microsoft-openai-drama-continues-whatsapp-ads-channel-subscriptions-and-the-creator-perspective/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-06-17"
saved_at: "2025-06-17"
reading_time: "11 mins"
summary: "Microsoft and AI continue to fight, and WhatsApp adds ads and subscriptions (and I explain why as a creator I'm not interested)."
content_hash: "76f114c58357ae62e004b6828ac864963b73db262b548fccfc2fceeb7ac04342"
---

Microsoft and AI continue to fight, and WhatsApp adds ads and subscriptions (and I explain why as a creator I'm not interested).

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

Jon at [Asianometry](<https://asianometry.passport.online/>) has another great historical video, this time about [Lisp Machines](<https://www.youtube.com/watch?v=sV7C6Ezl35A>).

On to the Update:

### Microsoft-OpenAI Drama Continues

From the [Wall Street Journal](<https://www.wsj.com/tech/ai/openai-and-microsoft-tensions-are-reaching-a-boiling-point-4981c44f>):

> Tensions between OpenAI and Microsoft over the future of their famed AI partnership are flaring up. OpenAI wants to loosen Microsoft’s grip on its AI products and computing resources, and secure the tech giant’s blessing for its conversion into a for-profit company. Microsoft’s approval of the conversion is key to OpenAI’s ability to raise more money and go public. But the negotiations have been so difficult that in recent weeks, OpenAI’s executives have discussed what they view as a nuclear option: accusing Microsoft of anticompetitive behavior during their partnership, people familiar with the matter said. That effort could involve seeking federal regulatory review of the terms of the contract for potential violations of antitrust law, as well as a public campaign, the people said.
>
> Such a move could threaten the companies’ six-year-old relationship, widely seen as one of the most successful partnerships in tech history. For years, Microsoft fueled OpenAI’s rise in exchange for early access to its technology, but the two sides have since turned into competitors, making it more difficult to find common ground…OpenAI and Microsoft are at a standoff over the terms of the startup’s $3 billion acquisition of the coding startup Windsurf, the people said. Microsoft currently has access to all of OpenAI’s IP, according to their agreement. It offers its own AI coding product, GitHub Copilot, that competes with OpenAI. OpenAI doesn’t want Microsoft to have access to Windsurf’s intellectual property.
>
> The companies continue to be at odds over how much of OpenAI Microsoft would own if it converts into a public-benefit corporation. Microsoft is currently asking for a larger stake in the new company than OpenAI is willing to give, people familiar with the matter said. OpenAI has to complete the conversion by the end of the year, or it risks losing $20 billion in funding…The startup is trying to renegotiate elements of that deal alongside its planned conversion. It wants to join with other cloud providers so it can sell its technology to more customers and access additional computing resources. Microsoft, meanwhile, wants access to OpenAI’s technology even after the startup declares its models have achieved humanlike intelligence, which would end the current partnership.

[The Information came out with a story a few hours later](<https://www.theinformation.com/articles/openai-seeks-new-financial-concessions-microsoft-top-shareholder>) corroborating much of The Wall Street Journal story, particularly in terms of the points of conflict, with a very telling line:

> OpenAI wants Microsoft, the startup’s biggest outside shareholder, to have a roughly 33% stake in the reshaped unit in exchange for foregoing its rights to future profits, according to a person who spoke to OpenAI executives.

The Wall Street Journal doesn’t indicate who its sources are, but there’s little doubt in my mind they too are on the OpenAI side, and I get why: my biggest takeaway from this story is that I have underestimated the amount of leverage that Microsoft has over OpenAI. I most recently wrote about this slow motion train wreck last month and said:

> Here’s the big question: what is more valuable to Microsoft in the long run? Those rights to $100 billion in profits, along with the revenue share they now enjoy, or perpetual rights to OpenAI’s models? I think it has to be the latter (to put $100 billion in context, that is $17 billion short of Microsoft’s total operating income last year). Of course OpenAI — and the rest of its investors — almost certainly doesn’t want to give up so valuable an asset, but I’m not sure if they will have a choice; the fact of the matter is that Microsoft put in the money to make OpenAI an entity worth fighting for, and they would do well to give up future profits from OpenAI to secure profits of their own.

I still think that this is broadly correct — and note that the right to make OpenAI models available to other cloud providers is one of the points of contention in this story — but the fact that OpenAI (in my interpretation) seems to be reduced to issuing fantastical threats through the press suggests that the decision about the endpoint of these negotiations is almost entirely up to Microsoft. To that end, I can understand if the company is pushing for more than I suggested; indeed, if anything these threats through the press might make Microsoft want to hold onto more, since they’ll probably have to fight OpenAI again in a few years. I still think, however, that this is all the more reason to give more ground now, in exchange for an iron-clad agreement securing Microsoft’s exclusive Azure access to OpenAI models in perpetuity.

As for the Windsurf angle, [my interview with Cursor CEO Michael Truell](<https://stratechery.com/2025/an-interview-with-cursor-co-founder-and-ceo-michael-truell-about-coding-with-ai/>) made clear just how important the data generated by these IDEs are:

> **Is that a real sustainable advantage for you going forward, where you can really dominate the space because you have the usage data, it’s not just calling out to an LLM, that got you started, but now you’re training your own models based on people using Cursor. You started out by having the whole context of the code, which is the first thing you need to do to even accomplish this, but now you have your own data to train on.**
>
> **MT:** Yeah, I think it’s a big advantage, and I think these dynamics of high ceiling, you can kind of pick between products and then this kind of third dynamic of distribution then gets your data, which then helps you make the product better. I think all three of those things were shared by search at the end of the 90s and early 2000s, and so in many ways I think that actually, the competitive dynamics of our market mirror search more than normal enterprise software markets.

Anthropic executives have made similar comments about the importance of this data feedback loop in terms of creating Claude Code; to that end, you can see why OpenAI would not want to share this sort of data with Microsoft to use to improve GitHub Copilot, even if their contract mandates that _all_ IP is available to Redmond. And, frankly, I think OpenAI has a point; the spirit of the agreement is about AI models, not products or product usage data, which Microsoft has had plenty of opportunities to harvest on its own (a separate but related question I have is if OpenAI shares ChatGPT usage data with Microsoft? It would seem so?).

Again, it does seem that Microsoft holds all of the cards for now, and relinquishing any of their rights would be a big short to medium term sacrifice. And, along those lines, I’m just an analyst sitting at my computer; I don’t have a fiduciary responsibility to shareholders. I continue to think, however, that Microsoft should be focused on securing long-term rights to capabilities that align with its existing business, which is model access and exclusive rights to sell OpenAI models; let the product stuff go, including Windsurf data.

This is still a bitter pill to swallow for OpenAI: not only would they get more leverage on their training spend if other cloud providers could sell OpenAI models, but they would also have a better chance of monopolizing the market; as it stands existing AWS and GCP users are probably not going to switch to Azure just to get OpenAI models, but will instead use Anthropic or Gemini. The bitterness of that pill, however, is directly correlated to [the cynicism/naiveté entailed in setting up the non-profit structure in the first place](<https://stratechery.com/2015/openai-artificial-intelligence-and-data-data-and-recruiting/>).

### WhatsApp Ads

From the [New York Times](<https://www.nytimes.com/2025/06/16/technology/whatsapp-ads.html>):

> On Monday, WhatsApp said it would start showing ads inside its app for the first time. The promotions will appear only in an area of the app called Updates, which is used by around 1.5 billion people a day. WhatsApp will collect some data on users to target the ads, such as location and the device’s default language, but it will not touch the contents of messages or whom users speak with. The company added that it had no plans to place ads in chats and personal messages…
>
> WhatsApp, which unveiled the changes at the Cannes Lions advertising industry conference, also said it was introducing paid monthly subscriptions for content creators, similar to offerings from competitors like X, YouTube and Twitch. The app will also let users and businesses advertise their “channels,” which are one-way broadcasts that can be sent to large groups of people…
>
> The introduction of ads may call attention to WhatsApp’s previous stumbles with privacy. In 2021, the company proposed changes to its terms of service that some users interpreted as more data sharing. The revisions incited a global backlash. This time, WhatsApp braced for pushback, saying any data sharing with other Meta-owned apps for ad targeting was optional. Users can choose to link their WhatsApp, Instagram and Facebook accounts, so ads on WhatsApp can be based on data collected from those platforms, Ms. Srinivasan said.

WhatsApp has always been a bit of a funny app in that it has always had a tab bar at the bottom that I personally have only ever interacted with by accident; these new ads are going in the “Updates” tab, which is an evolution of “Status”, which has been there from the beginning and is, I think, a hangover from AOL Instant Messaging (I’m not sure who made this graphic — it looks like its from WhatsApp? — but I found it [on Reddit](<https://www.reddit.com/r/coolguides/comments/1cos43d/a_cool_guide_to_whatsapps_interface_design/>)):

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2025/06/whatsapp-1.png?resize=1330%2C602&ssl=1)

I’ll take Meta’s word for it that Updates are used in some markets; it has continued to be a part of the UI for a reason, I suppose (perhaps because it has always been a natural place to put advertising). That, by extension, is certainly a reason to not be bothered by this news: I’m not going to see the ads anyways! Even if I did, however, I wouldn’t begrudge Meta this move: WhatsApp provides me tremendous utility, that utility is connected to WhatsApp being free-to-use (because it has network effects), so of course it makes sense that there would be ads at some point (but I hope that there is eventually a subscribe-for-no-ads option).

What is interesting is that WhatsApp just yesterday pushed me to add my email address for security; maybe this is just a coincidence, and Meta wouldn’t also want to use that email address to identify me, but given that I haven’t linked my WhatsApp account to my other Meta accounts, or registered my WhatsApp phone number with Facebook, the company will probably be reduced to using something like IP addresses to target data, for ads that I probably won’t see (Meta is emphasizing that they don’t sell your data to advertisers, which of course they don’t; it’s too valuable. What is useful is being able to link accounts for targeting purposes).

Again, I don’t begrudge them these attempts, to the extent they are true; indeed, when and if advertising gains a greater presence in the app I would be tempted to link the accounts just to get better ads. And, of course, I appreciate WhatsApp’s end-to-end encryption, which means that Meta couldn’t use message content to target even if they wanted to; in that light, have at my other Meta data.

### Channel Subscriptions and the Creator Perspective

What is more interesting to me are the new subscription options; from the [WhatsApp blog](<https://blog.whatsapp.com/helping-you-find-more-channels-and-businesses-on-whatsapp>):

> Today we’re introducing some new features for our Updates tab, which is home to both Channels and Status. We’ve worked over the last two years to make this tab the place for you to discover something new on WhatsApp and it’s now used by 1.5 billion people a day. We’re encouraged by the enthusiasm and also want to help admins, organizations, and businesses grow on WhatsApp.
>
> We’re going to do this in three ways:
>
>   * **Channel subscriptions:** You’ll be able to support your favorite channel by subscribing to receive exclusive updates for a monthly fee.
>   * **Promoted Channels:** We’ll help you discover new channels that might be interesting to you when you’re looking through the directory. For the first time, admins have a way to increase their Channel’s visibility.
>   * **Ads in Status:** You’ll be able to find a new business and easily start a conversation with them about a product or service they’re promoting in Status.
>

>
> These new features will appear only on the Updates tab, away from your personal chats. This means if you only use WhatsApp to chat with friends and loved ones there is no change to your experience at all.

I had a chat with a WhatsApp executive about the Channels subscriptions and Promoted Channels items in the context of my being a creator, and this was my feedback:

  * First, I’m certainly always in favor of new ways to monetize, but more importantly, am interested in new ways to connect to my subscribers.
  * Second, what I am not interested in is having new channels to monitor or manage; a critical component of the creator business model is managing scarce resources, which is not just money, but also time.
  * Third, what I need most is better ways to acquire and retain customers; what I am not worried about is marginal costs that drive revenue.



What I thought was interesting about this conversation was the initial disconnect we had on point three. Specifically, I personally have no issue paying 30% or whatever fee a platform wants to charge for acquiring customers; I would be happy to pay Apple or YouTube or Meta or whomever else for access to new channels. After all, every customer is incremental zero marginal cost revenue; if I have to pay $3 to get $10 of revenue that’s still $7 I wouldn’t have had otherwise.

What I don’t want to do is have to manage the complexity of individual silos, or only give my subscribers a portion of what they are entitled to; my ideal relationship to a scaled platform is [the one I have with Spotify](<https://stratechery.com/2021/spotifys-surprise/>). I’m able to manage my subscribers via Passport, which connects with Spotify on the back-end to unlock Stratechery Plus content on Spotify. Right now there is no cost for this connection, but if Spotify ever wanted to start selling subscriptions on my behalf — and taking a fee, naturally — that would be ok with me too. The key difference from, say, YouTube subscriptions, or this WhatsApp product, is that I still ultimately own the connection with the subscriber, and can give them everything they are entitled to: not just podcasts, but also emails, website access, etc.

This remains one of the core concepts of Passport: of course I sell subscriptions directly using Stripe, but Passport can accept any front-end for payments, whether that be the App Store, WhatsApp, YouTube, etc., just as it can link to any back-end for distribution, from email to SMS to RSS to Spotify. Unfortunately nearly all of those other payment options completely intermediate the customer — I can’t even get an email address. What I need is scalability of my management time and the ability to be multimodal; if I get that, I’m happy to pay fees on incremental revenue.

Anyhow, what that means in terms of this announcement is that I’m not interested in setting up Channel subscriptions; I am seling subscribers more than just WhatsApp updates. If, however, I can tie that into my broader offering, then I’d be happy to pay Meta to help me acquire customers through WhatsApp or any of their other properties.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
