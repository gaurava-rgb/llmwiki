---
title: "OpenAI Code Red, AWS and Google Cloud Networking"
reader_id: "01kbfd3y1dz8axqab5vsr0r0na"
notion_page_id: "3464ebe7-f118-8173-9503-d2ac10c1c688"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01kbfd3y1dz8axqab5vsr0r0na"
source_url: "https://stratechery.com/2025/openai-code-red-aws-and-google-cloud-networking/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-12-02"
saved_at: "2025-12-02"
reading_time: "7 mins"
summary: "OpenAI is declaring code red and doubling down on ChatGPT, highlighting the company's bear case. Then, AWS makes it easier to run AI workloads on other clouds."
content_hash: "edeb7774b9610356bfaccf32eb8046588b206343a27a7726eec3f3ffc65cf847"
---

OpenAI is declaring code red and doubling down on ChatGPT, highlighting the company's bear case. Then, AWS makes it easier to run AI workloads on other clouds.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On a special [Thanksgiving week episode of Sharp Tech](<https://sharptech.fm/member/episode/how-tech-is-transforming-the-suburbs-q-a-on-gemini-llm-use-cases-working-with-your-in-laws-ua-ps-and-more>), Andrew and I discussed how tech is transforming the suburbs, and then answered a whole grab bag of mailbox questions — many of which had nothing to do with tech. These are always some of my favorite episodes!

On to the Update:

### OpenAI Code Red

From [The Information](<https://www.theinformation.com/articles/openai-ceo-declares-code-red-combat-threats-chatgpt-delays-ads-effort>):

> OpenAI CEO Sam Altman on Monday told employees he was declaring a “code red” to marshall more resources to improve ChatGPT as threats rise from Google and other artificial intelligence competitors, according to an internal memo. As a result, OpenAI plans to delay other initiatives, such as advertising, Altman said. “We are at a critical time for ChatGPT,” he said.
>
> OpenAI hasn’t publicly acknowledged it is working on selling ads, but it is testing different types of ads, including those related to online shopping, according to a person with knowledge of its plans. Millions of people already use ChatGPT to search for products to buy. Altman said the code red “surge” to improve ChatGPT meant OpenAI would also delay progress with other products such as AI agents, which aim to automate tasks related to shopping and health, and Pulse, which generates personalized reports for ChatGPT users to read each morning.
>
> He didn’t specify what was going wrong with ChatGPT, but Google said this fall that its Gemini chatbot had gained ground in terms of usage. Altman recently warned employees privately that Google’s AI resurgence could cause “temporary economic headwinds” for OpenAI. In a call with OpenAI investors last month, CFO Sarah Friar alluded to a slowdown in ChatGPT growth, though it wasn’t clear what growth metric she was referring to, according to a person with knowledge of her remarks.

I’ll get to this snippet in a moment, but stepping back, I had a difficult time writing [yesterday’s Article](<https://stratechery.com/2025/google-nvidia-and-openai/>), not because I didn’t know what I wanted to say, but because I lacked my usual level of conviction. On one hand, I think that a lot of the “OpenAI is doomed” talk went too far over the last few weeks; ChatGPT is, by all accounts, the vast majority of actual AI usage, and the sheer scale of the userbase puts the app in the pole position in the consumer space. Moreover, I still have serious reservations about Google’s product chops — the Gemini app just isn’t as good on the phone, and the desktop/browser situation is a bit of a mess — and the company’s structural challenge in terms of being incentivized to defend search remains.

On the other hand — and I hope I conveyed this in the Article — I really do think that OpenAI has seriously erred by not aggressively building out an advertising model. Google and Meta are years ahead of OpenAI in this regard, which lets them compete with ChatGPT using cash flow today; OpenAI is promising revenues in the future, but from what? Subscriptions are great, and it’s legitimately amazing how large the OpenAI subscription business is, but any subscription model is fundamentally limited by the challenges of price elasticity: higher prices mean fewer users, while lower prices for a product that has real marginal costs means a worse user experience.

I think that YouTube is a good comparison here. I continue to think it is a violation of SEC rules that Google doesn’t report YouTube costs, but it’s safe to assume that video costs a fair bit to serve; that has certainly come down over time, of course, but it’s more than text. Because YouTube has an advertising model, however, the costs of serving are directly correlated with the revenue opportunity: the more videos you watch, the more ads you see. That also gives an easy way to calculate the appropriate YouTube Premium price: simply charge users what you would have earned for showing them ads (granted, this gets a little tricky if Premium users watch more YouTube videos than a free user, but you at least have a ballpark idea of what the right price is). A similar approach to ChatGPT would make it possible to not just give free users a better experience, but also align costs to revenue (and give more leeway to introduce usage pricing to account for expensive users).

So surely — to return to The Information article — I must be dismayed by this news? Well, no, not necessarily. The foundation of everything — as is the case for any consumer business — is customer usage. If OpenAI is seeing serious issues in terms of growth or engagement time, they have to be fixed; everything else pales in comparison, and that includes an advertising product that could, particularly at introduction, be a bit of a turn-off.

What is dismaying is that things have gotten to this point in 2025 without the ad product existing. Way back when there used to be a saying about about how Netflix was trying to become HBO before HBO became Netflix (neither of which happened, but it was a nice turn of phrase); in this case, ChatGPT needed to build an advertising-supported model before Gemini got good. The fact they didn’t is the real issue here.

And, I would add, Altman’s declaration raises another long-standing Stratechery concern about OpenAI: the lack of focus. I wanted the company for years to give up their enterprise business and focus on ChatGPT; I eventually conceded on this point, but there sure do seem to be some focus issues at play with this news!

Meanwhile, I noted in my conclusion yesterday that Google is the one company that has won consumer markets with nothing but a better product. I was thinking about Search, but John Gruber made the excellent point on [this morning’s Dithering](<https://dithering.passport.online/>), that actually Google has come to dominate multiple markets without being first, including smartphones (Android), browsers (Chrome), and email (Gmail). Of all the companies in tech to have on your tail, Google, with their tremendous infrastructure, distribution, and relentless iteration, is probably the scariest.

### AWS and Google Cloud Networking

From [Reuters](<https://www.reuters.com/business/retail-consumer/amazon-google-launch-multicloud-service-faster-connectivity-2025-12-01/>):

> Amazon and Google introduced a jointly developed multicloud networking service on Sunday to meet growing demand for reliable connectivity the companies said in a statement, at a time when even brief internet disruptions can cause major outages. The initiative will enable customers to establish private, high-speed links between the two companies’ computing platforms in minutes instead of weeks.

Reuters and other news sources framed this announcement in the context of last month’s AWS outage, but that seems unlikely to be the motivation. What is perhaps more telling is that [Google Cloud wrote a long blog post](<https://cloud.google.com/blog/products/networking/extending-cross-cloud-interconnect-to-aws-and-partners/>) about this, and AWS issued [a very short press release](<https://aws.amazon.com/about-aws/whats-new/2025/11/preview-aws-interconnect-multicloud/>). First from Google:

> Today, we announced a significant collaboration with Amazon Web Services (AWS) to offer a managed, private and secure, on-demand, solution for cross-cloud connectivity. This solution is designed to enable customers to easily build enterprise-grade applications that span both Google Cloud and AWS environments. This collaboration is particularly timely, as the adoption of multicloud applications is rapidly accelerating, driven in part by the rise of AI. A Forbes survey highlighted that 82% of respondents anticipate that the arrival of AI services will increase the demand for multicloud networking due to the scarcity of specialized accelerator resources and the availability of diverse AI agents across different vendors. The surge in multicloud adoption is a strategic imperative for organizations looking to build agentic AI applications, optimize workloads, access best-of-breed services, meet data residency requirements, and ensure the necessary resiliency for modern hybrid and multicloud applications.
>
> To address the inherent network infrastructure challenges introduced by multicloud deployments, we designed the Cross-Cloud Network to simplify and optimize networking between Google Cloud and other providers. This commitment to multicloud integration has led to over 50% of the Fortune 500 currently using the Cross-Cloud Network, and this collaboration provides a significant boost. Importantly, this new jointly engineered solution with AWS is being published under an open specification, creating an opportunity to expand the reach, allowing other providers to contribute and implement this solution in their own environments, further benefiting mutual customers.

Next from Amazon:

> AWS announces preview of AWS Interconnect – multicloud, providing simple, resilient, high-speed private connections to other cloud service providers (CSPs), starting in preview with Google Cloud as the first launch partner and then with Microsoft Azure later in 2026.
>
> Customers have been adopting multicloud strategies while migrating more applications to the cloud. They do so for many reasons including interoperability requirements, the freedom to choose technology that best suits their needs, and the ability to build and deploy applications on any environment with greater ease and speed. Previously, when interconnecting workloads across multiple cloud providers, customers had to go the route of a ‘do-it-yourself’ multicloud approach, leading to complexities of managing global multi-layered networks at scale. AWS Interconnect – multicloud is the first purpose-built product of its kind and a new way of how clouds connect and talk to each other. It enables customers to quickly establish private, secure, high-speed network connections with dedicated bandwidth and built-in resiliency between their Amazon VPCs and other cloud environments. Interconnect – multicloud makes it easy to connect AWS networking services such as AWS Transit Gateway, AWS Cloud WAN, and Amazon VPC to other Cloud Service Providers (CSPs) quickly, instead of weeks or months.

At the risk of reading too deeply into press release tea leaves, it’s notable that:

  * Google immediately mentions AI
  * AWS doesn’t mention AI at all
  * Only AWS announced that they will also be interconnecting with Azure



AWS has the largest cloud and the weakest AI offerings; Google, meanwhile, is heavily invested in AI as a cloud differentiator, and Microsoft has exclusive rights to OpenAI IP. What this reads like to me is that AWS is increasingly concerned about losing not just AI workloads to Google and Microsoft, but also that the rest of the data will follow; building easy interconnects for sharing data gives a much easier and attractive alternative for customers already on AWS who want to run AI elsewhere: simply send what you need for AI, easily, to Google and Microsoft if you wish, but keep your data and applications on AWS. And it will probably work!

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
