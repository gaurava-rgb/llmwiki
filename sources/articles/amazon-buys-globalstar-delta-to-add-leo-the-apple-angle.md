---
title: "Amazon Buys Globalstar, Delta to Add Leo, The Apple Angle"
reader_id: "01kp95k2gfkpggsz3sgzt5jbcc"
notion_page_id: "3464ebe7-f118-8105-af69-e2d00d82d80e"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01kp95k2gfkpggsz3sgzt5jbcc"
source_url: "https://stratechery.com/2026/amazon-buys-globalstar-delta-to-add-leo-the-apple-angle/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2026-04-15"
saved_at: "2026-04-15"
reading_time: "10 mins"
summary: "Apple's Globalstar acquisition is being framed as Apple versus SpaceX, but I think the real story is about Apple."
content_hash: "1999dde72910f835edb3a2a0d0fd2a6985e0c5750d4c86f9a34bf02fca6161ea"
---

Apple's Globalstar acquisition is being framed as Apple versus SpaceX, but I think the real story is about Apple.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

The NBA postseason is here, which means this is an excellent time to add [The Greatest of All Talk](<https://goat.passport.online/>), hosted by Andrew Sharp and Ben Golliver, to your podcast player; also make sure you are subscribed to [Andrew’s writing on Sharp Text](<https://sharptext.net/>), and check out [Golliver’s new Substack](<https://bengolliver.substack.com/>).

On to the Update:

### Amazon Buys Globalstar

From [Bloomberg](<https://www.bloomberg.com/news/articles/2026-04-14/amazon-s-11-6-billion-globalstar-deal-amps-up-rivalry-with-musk>):

> Amazon.com Inc.’s $11.6 billion deal to buy Globalstar Inc. ramps up competition with Elon Musk’s Starlink in satellite communications, a market predicted to double to $200 billion in the coming years. On Tuesday, Amazon announced plans to buy the satellite operator for a mix of stock and up to $90 a share and said that in 2028 it will launch a direct-to-device service, offering connectivity straight to people’s mobile devices as an alternative to traditional cell towers.
>
> Through Globalstar, Amazon will gain radio frequency licenses that are key to the company advancing its satellite-to-mobile services. The e-commerce giant has been trying for years to break into satellite services to gain new sources of growth beyond its enormous retail and cloud-computing businesses. But its efforts have been hampered by delays from rocket builders and a slow start to its manufacturing operations. Meanwhile, Musk’s Starlink, a division of SpaceX, has sprinted ahead with a network of 10,000 satellites in orbit serving 10 million people and developing a reputation for reliable internet service in hard-to-reach areas.

Framing this acquisition in terms of Leo versus Starlink is the most obvious thing in the world. After all, Amazon is the only company really challenging SpaceX when it comes to low earth orbit satellite constellations, which, to be honest, sometimes feels a little quixotic and tied up in the Jeff Bezos versus Elon Musk rivalry than in any real business case, particularly given SpaceX’s big head start.

Still, you can see why Amazon in particular is making the investment in Leo. The first thing that I think about is logistics: Amazon has, over the last decade, built up one of if not the largest logistics business in the world, with mobile assets all over the world that need connectivity; what is particularly interesting to think about, however, is a future of drone delivery, where satellite connectivity and control actually is superior to cellular and, thanks to the fact that drones fly, avoids many of the satellite downsides in terms of needing line-of-sight. There are also some niche AWS use cases, particularly in terms of very low latency connectivity between far-flung regions, and of course the possibility of building data centers in space.

Amazon, meanwhile, is a company whose specialty is making massive long-term capital investments to give itself a durable price advantage; building a satellite constellation definitely fits the massive long-term capital investment part of that, and ensuring they are not dependent on SpaceX fits the second part. And, of course, [Amazon will be Leo’s first customer](<https://stratechery.com/2017/amazons-new-customer/>), but the ultimate goal will be to sell Leo’s services to third parties as well.

Here’s what is weird about this deal, however: I don’t really see how acquiring Globalstar really makes a difference to these goals. Globalstar’s assets are, all things considered, pretty middling:

  * 24 satellites nearing the end of their 15-year lifespan with a bent-pipe architecture (i.e. signal relaying only, no onboard processing), and 24 ground gateway stations across six continents; there are some new satellites on the way to keep the constellation going, but it seems likely that still-on-the-drawing-board higher-capability satellites will be scrapped.
  * Approximately 8 MHz of L-band satellite uplink, and approximately 16.5 MHz of S-band satellite downlink
  * n53 terrestrial spectrum (i.e. for private cellular networks, not phone-to-satellite communication) that is licensed out



Moreover, those assets by-and-large serve one customer: Apple. Apple owned a 20% equity stake in Globalstar and had rights to 85% of Globalstar’s network capacity for the satellite service it provides to iPhones and Apple Watches. That is certainly a valuable relationship, but it also meant that Apple had a de facto veto on any Globalstar acquisition. What I suspect, however, is that Apple’s role went further than having — or declining to use — their veto. I think they made this deal happen — but first, a (related) digression.

### Delta to Add Leo

From the [Wall Street Journal late last month](<https://www.wsj.com/business/airlines/delta-to-tap-amazon-satellite-internet-service-for-in-flight-wi-fi-583a3c09>):

> Amazon.com struck a deal to provide internet access on Delta Air Lines flights, the tech giant’s highest-profile victory in the race to supply in-flight Wi-Fi. Delta said it plans to use Amazon’s nascent Leo satellite-internet business to provide Wi-Fi on an initial 500 aircraft starting in 2028. With Leo, Delta is planning for internet speeds that will be three to five times faster than what the airline currently offers.
>
> Delta’s choice intensifies competition in the satellite-internet industry. JetBlue Airways last year announced plans to use Amazon’s service on a portion of its fleet. But Starlink, the service operated by Elon Musk’s SpaceX, has become a dominant provider for airlines, signing up customers including United Airlines, Southwest Airlines and Alaska Air Group.

I don’t think it’s a surprise that United went with Starlink while Delta went with Leo, and the analogy I would draw is to the iPhone. Apple famously first offered the iPhone to Verizon, the leading carrier in the U.S., but the latter balked at granting Apple total control of the device and user interface; Apple instead went with AT&T, née Cingular, which was willing to take a chance on leveraging the iPhone to catch up. That same strategy repeated itself throughout the world: leading carriers didn’t want to make a deal on Apple’s terms, so Apple would launch with second place carriers, and then leverage [the unprecedented willingness of customers to change carriers just to get an iPhone](<https://stratechery.com/2013/why-do-carriers-subsidize-the-iphone/>) to eventually come to terms with the market leader.

In this case, Starlink has unquestionably the best satellite Internet service. I also strongly suspect it’s the most expensive, and comes with a lot of terms and conditions, reportedly including the requirement that it be free to customers, and that [it be installed across an airline’s entire fleet](<https://x.com/TMFAssociates/status/2000272938227159342>), which means that a carrier is completely dependent on Starlink. That’s a price that United, [which has had its sights set on challenging Delta for premium passengers](<https://stratechery.com/2026/an-interview-with-united-ceo-scott-kirby-about-tech-transformation/>), is willing to pay; by the same token, it’s one that Delta, the most profitable U.S. airline and long acknowledged leader, isn’t. They would rather maintain power over their suppliers — Leo won’t be on all of their aircraft — and Amazon is willing to play ball (American, meanwhile, [is also talking to Amazon](<https://www.bloomberg.com/news/articles/2025-12-10/american-airlines-in-talks-with-amazon-for-leo-in-flight-wi-fi>), mostly because they’re cheap).

This isn’t the only example of leading companies wanting to avoid being at the mercy of SpaceX: Verizon is at it again in terms of their own satellite service, [doubling-down on their investment in AST SpaceMobile](<https://stratechery.com/2025/the-openai-hype-cycle-microsofts-game-pass-failure-verizons-satellites/>) instead of coming to a deal with Starlink for not just better service, but service that actually exists today (AST SpaceMobile is years behind).

And, to that end, what is another company that is the clear leader in their space? Well, it’s the one that I expressed hope [late last year](<https://stratechery.com/2025/spacex-buys-more-spectrum-spacexs-pivot-why-apple-and-spacex-should-partner/>) would lean into a SpaceX partnership:

> Satellite connectivity, however, is a different market. Carriers were well-established by the time the iPhone came around; that meant the conditions were in place for Apple to commoditize the market, but that also meant that there was no room for Apple to differentiate itself in the market. It’s the opposite in this case: satellite functionality is new, and it’s not good enough; that means there are real benefits to integration, wherein the satellite connectivity piece is developed hand-in-hand with handsets to deliver a differentiated experience.
>
> The problem for Apple is that GlobalStar, their long-time satellite partner, simply doesn’t have the resources to keep up with Apple. Apple already had to give the company an infusion of cash, and that was simply to maintain an experience that is worse than what you get from SpaceX; SpaceX, meanwhile, has an unassailable launch advantage that it is leveraging to cover the sky with cellular-capable satellites.
>
> The problem SpaceX is having, meanwhile, is that they lost out on their gambit to be the provider for every cellular carrier, which means the best way to bring their advantages to bear is to also pursue an integrated strategy, but they don’t have the handset expertise or go-to-market capabilities necessary to build a fully integrated experience of their own.
>
> In short, Apple and SpaceX can solve each other’s problem/opportunity: SpaceX could allow Apple to push the envelope in terms of satellite capability on iPhones, capability that could exist on top of existing carrier services; Apple, meanwhile, could bring SpaceX’s potential mobile service to market in a far more effective and compelling way than SpaceX could on its own. It’s not pure integration — I’m talking about a partnership here — but there is a real path to delivering a truly differentiated experience to the benefit of both companies.

The problem, as I noted in that Update, is that it was hard to see Apple and SpaceX ever resolving who would actually be in charge; Apple clearly agrees, because not only are they declining to work with SpaceX, I actually think they were the driving force in this GlobalStar deal.

### The Apple Angle

[Amazon’s press release about the acquisition](<https://www.aboutamazon.com/news/company-news/amazon-globalstar-apple>) is pretty interesting if you read between the lines. Here’s the opening paragraph:

> Today Amazon.com, Inc. and Globalstar, Inc. announced that they have entered into a definitive merger agreement under which Amazon will acquire Globalstar, enabling Amazon Leo to add direct-to-device (D2D) services to its low Earth orbit satellite network and extend cellular coverage to customers beyond the reach of terrestrial networks. In addition, Amazon and Apple announced an agreement for Amazon Leo to power satellite services for iPhone and Apple Watch, including Emergency SOS via satellite. The new capabilities are part of Amazon’s long-term vision for space-based connectivity, and Amazon plans to work with mobile network operators (MNOs) and additional partners to deliver on that vision and extend reliable, high-speed connectivity to customers, no matter where they are in the world.

Amazon isn’t really talking about being a cellular provider, and for good reason: first, [as I have explained in the context of Starlink](<https://stratechery.com/2025/spacex-buys-spectrum-spectrum-specifics-spacexs-big-bet/>), there are fundamental physical limitations in terms of providing cellular service solely through satellites; you need terrestrial service as well. Second, Globalstar only has around 25 MHz of spectrum, far less than the 65 MHz that [SpaceX has acquired](<https://stratechery.com/2025/spacex-buys-more-spectrum-spacexs-pivot-why-apple-and-spacex-should-partner/>). To that end, note that Amazon is leading with the Apple partnership, and then back-filling with future carrier partnerships.

Next, read the section of the press release about Apple specifically:

> In addition to the agreement with Globalstar, Amazon and Apple signed an agreement to provide satellite connectivity for current and future iPhone and Apple Watch features. Globalstar currently partners with Apple to power satellite service on iPhone 14 or later, as well as Apple Watch Ultra 3, allowing users to text emergency services, message friends and family, request roadside assistance, and share their location. With the new Amazon-Apple agreement, Amazon will continue to support iPhone and Apple Watch models currently using Globalstar’s existing and planned upcoming low Earth orbit satellite constellations, being manufactured by MDA Space, and collaborate with Apple on future satellite services using Amazon Leo’s expanded satellite network.
>
> “Since launching more than three years ago, our groundbreaking safety service Emergency SOS via satellite has helped save many lives around the world—from a scout troop stranded on a winter hike in British Columbia, to a woman who was airlifted to safety in Colorado after her car rolled down a 250-foot cliff,” said Greg Joswiak, Senior Vice President of Worldwide Product Marketing, Apple. “Apple and Amazon have a long and proven track record of working together through Amazon’s core infrastructure services, and we look forward to building on that collaboration with Amazon Leo. This ensures our users will continue to have access to the vital satellite features they have come to rely on, including Emergency SOS, Messages, Find My, and Roadside Assistance via satellite, so they can stay safe and connected while off the grid.”

Apple isn’t talking about exciting new features, but rather maintaining what they have — which is exactly what Amazon is promising. This, by extension, leads me to my conclusion that this deal is about _Apple_ versus Starlink, not _Amazon_.

Specifically, I don’t think that Apple wants to partner with Starlink, for the reasons I noted above. At the same time, the Globalstar partnership was failing, which meant that Apple was stuck. I wouldn’t be surprised if they made a deal with Amazon: acquire Globalstar, keep it running for now, and in the long run add Globalstar’s capabilities to the satellites that Amazon is going to launch anyways. In return, Amazon can have a nice side business selling that capability to mobile network operators around the world, and Apple will continue to — using Greg Joswiak’s words — to build on its “long and proven track record of working together through Amazon’s core infrastructure services.” Apple already spends an estimated $1–$1.5 billion/year on AWS, which means there is plenty of latitude to make this acquisition well worth Amazon’s while, and ensure that the iPhone maker isn’t answering to Elon Musk.

This is, to be clear, speculation. It is, however, speculation that explains this deal much more satisfactorily than the default explanation of Amazon getting into the direct-to-device satellite business with a worse offering that doesn’t directly benefit their core reasons for launching satellites in the first place.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *
