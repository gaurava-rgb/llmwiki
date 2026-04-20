---
title: "ChatGPT Group Chats, Meta and the Encryption Trade-off, Network Effects and Ad Models"
reader_id: "01ka9avbj218g2081hz3z0eajw"
notion_page_id: "3484ebe7-f118-8167-a84b-eb690ef108ff"
reader_url: "https://read.readwise.io/read/01ka9avbj218g2081hz3z0eajw"
source_url: "https://stratechery.com/2025/chatgpt-group-chats-meta-and-the-encryption-trade-off-network-effects-and-ad-models/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-11-17"
saved_at: "2025-11-17"
reading_time: "8 mins"
summary: "ChatGPT is getting group chats, a long-standing Stratechery feature request. It's also a clear attach against Meta, who can't respond because of encryption, while Google looms."
content_hash: "06aaf25070fca1e42d756be87581265f387272594ed49190007b266cda5a0663"
---

ChatGPT is getting group chats, a long-standing Stratechery feature request. It's also a clear attach against Meta, who can't respond because of encryption, while Google looms.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On [Thursday’s episode of Sharp Tech](<https://sharptech.fm/member/episode/how-apple-changed-the-cellular-economy-what-space-x-wants-to-do-with-spectrum-airlines-and-carriers-yann-le-cun-departs-meta>), Andrew and I recounted the history of Apple and the carriers, and what might be both similar and different to SpaceX and Apple’s efforts to build out satellite cellular capabilities.

On to the Update:

### ChatGPT Group Chats

From [OpenAI](<https://openai.com/index/group-chats-in-chatgpt/>):

> Today, we’re beginning to pilot a new experience in a few regions that makes it easy for people to collaborate with each other — and with ChatGPT — in the same conversation. With group chats, you can bring friends, family, or coworkers into a shared space to plan, make decisions, or work through ideas together. Whether you’re organizing a group dinner or drafting an outline with coworkers, ChatGPT can help. Group chats are separate from your private conversations, and your personal ChatGPT memory is never shared with anyone in the chat.
>
> Group chats are starting to roll out on mobile and web for logged-in ChatGPT users on ChatGPT Free, Go, Plus and Pro plans in Japan, New Zealand, South Korea and Taiwan. This pilot is a small first step toward shared experiences in ChatGPT, and we expect to learn from early user feedback to inform how we expand to more regions and ChatGPT plans.

This is a fascinating announcement for lots of reasons, not least of all because this is a direct Stratechery feature request! From [an Update back in May](<https://stratechery.com/2025/claude-4-anthropic-agents-human-ai-agents/>):

> It remains to be seen how far away we truly are from agents that are reliable enough to be left alone to do work, and, needless to say, there are major second-order effects that will result from this being the case. In the meantime, however, I think there is a massive AI-enabled opportunity that is currently being missed by all of the major model-makers, or at least their product teams: human-AI agents.
>
> Right now all of the consumer-focused AI interfaces — i.e. the chatbots — are built for a single user (ChatGPT’s Teams subscription just refers to billing and administration, not usage). There is a huge productivity unlock, however, that happens when you make them multiuser. The following is a personal example that I discovered last week…

You can read the post for the specifics of the example, but I concluded:

> In fact, this is so effective that I wonder if enterprises everywhere are thinking about AI all wrong, at least in the short-term. There is a lot of focus on one person having a lot of agents under their control, and the allure of that — both financially and in terms of productivity — are clear. It’s possible, however, that a lot of the productivity gains are available now. A team leader can direct people (1) who use the same tools as them with a similar effectiveness (2) in an auditable way (3) and seamlessly extend or augment their work while retaining context. That’s pretty powerful!
>
> The reason why I think this is novel and worth writing about is because none of the chatbots support multi-user. Daman and I hacked this together using the “Share Chat” feature, but this would be better if multi-user chats were possible by default. And, more broadly, the real unlocks from AI are not going to come from working the way we do but better; it will come from changing the way we work, and here at Stratechery we have started doing exactly that.

I don’t think that my use case is the focus of this new feature; I’m optimistic, however, that it will be useful for our work all the same.

We could, I should note, use Copilot, which [just added Teams mode](<https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-teams-mode-for-microsoft-365-copilot/4463259>). Copilot, however, still doesn’t have a proper Mac app for enterprise accounts (there is a Mac app, but it only works with personal accounts), and I don’t want to chat in Teams, which is overkill for our needs. It just makes sense for us to work with AI jointly where we already work with AI individually.

### Meta and the Encryption Trade-off

Where we do communicate currently, by the way, is iMessage and WhatsApp, and, in the wake of this announcement, lots of people are wondering how it is that OpenAI beat Meta to the punch. In fact, you can access Meta AI in WhatsApp group chats, but it’s severely limited — and for a very good reason. From the [WhatsApp Help Center](<https://faq.whatsapp.com/203220822537614/>):

> You can use Meta AI in your WhatsApp individual or group chats to ask questions or get advice. Others in the chat will be able to see your messages to Meta AI as well as Meta AI’s response. Meta AI is an optional service offered and managed by Meta.
>
> Messages from Meta AI are generated by artificial intelligence (AI), using a service from Meta, in response to the prompts and messages you send to the AI.
>
> Meta can only read messages that mention @Meta AI or that people choose to share with it, not any others. As always, your personal messages and calls are protected with end-to-end encryption, meaning no one outside of the chat, not even WhatsApp or Meta, can read, listen to, or share them.

I actually strongly disliked the addition of Meta AI to WhatsApp group chats, because I think that even placing the possibility that Meta could see your messages in people’s minds wasn’t worth it; rest assured, however, that MetaAI cannot read your group chats. That, though, is precisely the problem for Meta: MetaAI can’t read your group chats! ChatGPT Group Chats are not and will not be end-to-end encrypted, because how could they be? To actually gain the benefit you have to share context, which means that encryption actually hurts the experience.

This, in some respects, harkens back to what [I wrote last year about Telegram’s non-encrypted advantage](<https://stratechery.com/2024/telegram-ceo-arrested-telegrams-non-encrypted-advantage-telegram-complexities/>):

> Here is the important takeaway with regards to Telegram, though: Telegram didn’t do any of that [end-to-end encryption], which has arguably been a feature, not a bug. Two of the biggest Telegram features that have helped fuel its popularity are Channels and Groups:
>
>   * Channels are one-way broadcasts, that may also allow for reactions and comments. This is more akin to a blog or a Facebook page. Channels can have an unlimited number of subscribers.
>   * Groups are, well, group chats, but they can scale to 200,000 members. Note that that is a two orders of magnitude increase in capacity compared to WhatsApp and Signal; this is directly related to the fact that Telegram groups are not end-to-end encrypted.
>

>
> I think that this point is crucial to understanding Telegram and its place in the market. Yes, the company has played extremely fast-and-easy with how it characterizes its product, to the extent that most users and media (i.e. the excerpt above) mistakenly believe the product has more inherent security than it does. What is also true, though, is that Telegram’s specific feature set are integral to the product-market fit it obtained: there is a place in the market for large scalable group discussion, and filling that hole in the market does depend on an absence of end-to-end encryption.

End-to-end encryption is, in nearly every respect, an excellent example of how everything is a trade-off. Yes, you get privacy and security, and obviously that is valuable; it’s not cost-free, however, and not being able to seamlessly include AI is one of the costs.

This is also the second example in just the last two months of Meta finding itself threatened by OpenAI in the social space because of constraints it didn’t fully realize it faced. [The first one was Sora](<https://stratechery.com/2025/sora-ai-bicycles-and-meta-disruption/>) and the — admittedly speculative — theory that it won’t be so easy to just shove AI-generated content front-and-center in Instagram, along with the fact that Instagram no longer being a social networking app means there is a social umbrella for actual social networking. ChatGPT group chats, meanwhile, are exploiting a technical constraint; the extent to which both are successful is the extent to which Meta’s hold on the only scarce resource on the web — user time and attention — is diminished.

### Network Effects and Ad Models

This is expected to be Gemini 3 week, confirmed by none other than CEO Sundar Pichai:

![](https://pbs.twimg.com/profile_images/1710036756731510784/FyfFgM-B.jpg)

[Sundar Pichai](<https://twitter.com/sundarpichai>) [@sundarpichai](<https://twitter.com/sundarpichai>)

[ ](<https://twitter.com/sundarpichai/status/1989481514393121239>)

🤔🤔

![](https://pbs.twimg.com/profile_images/1382355312036958211/C-W8CIB8.png)

[Alphabetting](<https://twitter.com/wintermoat>) [@wintermoat](<https://twitter.com/wintermoat>)

[ ](<https://twitter.com/wintermoat/status/1989360965801201734>)

Prediction markets are betting on Gemini 3 release next week $goog

![](https://pbs.twimg.com/media/G5uhQQhacAAl58m.jpg) [Posted Nov 14, 2025 at 3:53PM](<https://twitter.com/wintermoat/status/1989360965801201734>) [Posted Nov 14, 2025 at 11:52PM](<https://twitter.com/sundarpichai/status/1989481514393121239>)

The hype machine is high for this release (as well as Google’s stock after [Berkshire Hathaway disclosed an investment](<https://www.cnbc.com/2025/11/14/warren-buffetts-berkshire-hathaway-reveals-new-position-in-alphabet.html>)); more broadly, I can’t help but think back to what OpenAI CEO Sam Altman told me in [a February 2023 Stratechery Interview](<https://stratechery.com/2023/new-bing-and-an-interview-with-kevin-scott-and-sam-altman-about-the-microsoft-openai-partnership/>) after the release of “New Bing”:

> I think it’s fabulous for both of us. I think there’s so much upside for both of us here. We’re going to discover what these new models can do, but if I were sitting on a lethargic search monopoly and had to think about a world where there was going to be a real challenge to the way that monetization of this works and new ad units, and maybe even a temporary downward pressure, I would not feel great about that.

Google seems to be doing pretty well! More generally, one increasingly gets the sense that the search giant has shifted from being the hunted to being the hunter: if Gemini 3 blows away the competition, is OpenAI doomed?

Well, no, I don’t think so, because OpenAI is already ingrained into the lives of hundreds of millions of people, and those habits are hard to break (and also, while I’m here, Mac Gemini app with app integrations, please?). What would certainly help, moreover, would be to extend the habit advantage ChatGPT has to a network advantage as well. That’s why I think it’s notable that, unlike with Sora, these group chats are going into the ChatGPT app. I do think this is a more natural fit — I think of group chats as another means of “doing AI”, which for most people means ChatGPT — but there is a clear strategic imperative as well.

This is also a good reason to make Group Chats available to everyone, not just paid users; one shouldn’t have to know the paying status of potential collaborators to start a group chat, or limit one’s market in any way if the goal is a network effect. Still, there is some weird complexity; back to the OpenAI post:

> Group chats work much like your usual ChatGPT conversations — only now, others can join in. Responses are powered by GPT‑5.1 Auto, which chooses the best model to respond with based on the prompt and the models available to the user that ChatGPT is responding to based on their Free, Go, Plus or Pro plan. Search, image and file upload, image generation, and dictation are enabled. Rate limits only apply when ChatGPT responds – not to messages between users in the group chat – and responses from ChatGPT count toward the limit available of the person ChatGPT is responding to. For more details, you can visit the help center⁠

Speaking of limitations, you can really start to see the seams of the paid subscription model starting to show in this paragraph. Answers may differ in quality based on the subscription level of whoever asked ChatGPT a question, and some users in a chat may have rate limits, while others do not. What this says to me — unsurprisingly — is that ChatGPT really needs to get going on that ad-supported model! Seeking to build a network effect is a worthwhile line of defense against Google, and line of attack against Meta; more broadly, massive penetration and awareness is already ChatGPT’s biggest defense. All of this is dramatically enhanced if the best possible product is “free” to use.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
