---
title: "Trump Allows H200 Sales to China, The Sliding Scale, A Good Decision"
reader_id: "01kc4pfc66f11xv222pn82szxn"
notion_page_id: "3464ebe7-f118-810e-91ee-d9293c7ba89f"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01kc4pfc66f11xv222pn82szxn"
source_url: "https://stratechery.com/2025/trump-allows-h200-sales-to-china-the-sliding-scale-a-good-decision/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-12-10"
saved_at: "2025-12-10"
reading_time: "10 mins"
summary: "The Trump administration has effectively unwound the Biden era chip controls by selling the H200 to China; I agree with the decision, which is a return to longstanding U.S. policy."
content_hash: "f5ac9aec8ef20fa592406cfd83806b46bd48f99e9e5e9cde83a7c979ebf1d23d"
---

The Trump administration has effectively unwound the Biden era chip controls by selling the H200 to China; I agree with the decision, which is a return to longstanding U.S. policy.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

On [Thursday’s episode of Sharp Tech](<https://sharptech.fm/member/episode/open-ai-declares-a-code-red-alan-dye-leaves-apple-for-meta-questions-on-tranium-3-substack-and-f-1>) we discussed my angst about OpenAI and the looming Google threat, as well as Apple executive changes, Trainium 3, and Substack.

Then, on [this week’s episode of Sharp China](<https://sharpchina.fm/member/episode/trumps-plan-to-sell-advanced-chips-to-china-u-s-concessions-piling-up-amid-a-push-for-stability-macron-and-the-eu-conundrum>), Bill and Andrew discussed President Trump’s plan to let Nvidia sell H200 chips to China.

On to the Update:

### Trump Allows H200 Sales to China

From [Bloomberg](<https://www.bloomberg.com/news/articles/2025-12-08/nvidia-set-to-win-us-approval-to-export-h200-ai-chips-to-china>):

> President Donald Trump granted Nvidia Corp. permission to ship its H200 artificial intelligence chip to China in exchange for a 25% surcharge, a move that lets the world’s most valuable company potentially regain billions of dollars in lost business from a key global market. The decision was announced by Trump in a post on his Truth Social network, capping weeks of deliberations with advisers about whether to allow H200 exports to China. Trump said he informed Chinese President Xi Jinping about the move and that Xi had responded favorably. He added that shipments would only go to “approved customers,” and that chipmakers such as Intel Corp. and Advanced Micro Devices Inc. would also be eligible.
>
> The move represents a victory for Nvidia in its push to get Trump and Congress to relax export controls that have kept the company from selling its AI chips to the world’s largest semiconductor arena. Chief Executive Officer Jensen Huang has forged a close relationship with Trump since the November 2024 election and has used those ties to make his case that restrictions only boost Chinese domestic champions like Huawei Technologies Co.

At first glance, this seems in line with the Trump administration’s [earlier reversal](<https://stratechery.com/2025/china-ai-chips-a-china-chip-control-framework-whither-hbm/>) of its [initial ban on the sale of H20 chips](<https://stratechery.com/2025/nvidia-h20-restricted-in-china-the-huawei-cloudmatrix-384-whither-chip-controls/>). That, however, was actually restoring the status quo the Trump administration inherited from the Biden administration.

To fully understand this decision, you actually have to go back to 2022 and the initial Biden chip ban. The key parameter the initial ban focused on was memory bandwidth; from a [November 2022 Update](<https://stratechery.com/2022/china-chip-ban-clarifications-nvidias-a800-china-intel-and-tower/>) (quoting an [October 2022 Update](<https://stratechery.com/2022/more-on-the-china-chip-ban-the-ai-focus-apple-and-ymtc/>)):

> I don’t think it is a coincidence that the rules specify 600 Gb/s given the fact that Nvidia’s A100 chip has 600 Gb/s interconnects. I explained why this matters in a [Daily Update](<https://stratechery.com/2022/more-on-the-china-chip-ban-the-ai-focus-apple-and-ymtc/>):
>
>> Nvidia’s data center chips, like the current top-of-the-line A100 and upcoming H100, have the same architecture as its gaming chips (Ampere in the case of the A100 and 3000 line of gaming chips; Ada Lovelace in the case of the H100 and 4000 line of gaming chips); the biggest difference (beyond clock speed and the allocation of cores amongst shaders, tensors, etc.) is memory: data center chips not only have more of it, they also have much higher speed memory buses, both in terms of on-board memory and also interconnects for working with other chips. This, by extension, gets at the difference between training and inference: while inference (i.e. the application of machine learning models) can run on single GPUs, training (i.e. the creation of those models) is done on fleets of them; the training of AI models specifically appears to have been the primary target of the Biden administration.
>
> As I further explained in that Update, maximizing compute is increasingly a matter of system design, not just chips; this is particularly important in terms of AI training, which is an “embarrassingly parallel” task: the speed of processing increases basically linearly with the amount of processors available, but the trick is keeping all of those processors busy, which is where the memory bandwidth comes in. In other words, the A800 chip, which is limited to 400 Gb/s interconnects, will operate as fast as the A100, but it will more likely be sitting idle more often because the interconnect is saturated moving data around.

The A800 I’m referring to was Nvidia’s response to the chip ban: the company quickly came out with a variation of the A100 chip that had lower chip-to-chip bandwidth, thus fitting into that particular iteration of export controls. The H20, then was the successor to the A800, but in the meantime, the Biden administration had released a new set of rules that not only restricted memory bandwidth but also placed limits on actual computational performance. In other words, the H20 was, relative to the H200, a worse chip than the A800 was relative to the A100.

The reason to retrace this history is that what the Trump administration is doing is basically unwinding the Biden chip controls almost completely. Of course the H200 can be used for inference; more critically, it was, until the release of the GB200, the go-to chip for training, thanks not only to its performance, but also because of the way tens of thousands of chips could be linked together in a coherent manner to handle the massive amount of data necessary to train large models.

Note that I say “almost completely”; before the Biden chip ban Chinese companies could buy the exact same chips as American companies. Today, however, American companies are buying GB200 chips, which are a significant leap forward from H200s; the implication of this policy is that China is allowed to be on the same technology curve as the U.S., but a generation (or two) behind.

### The Sliding Scale

This, I would note, is not that extraordinary; it’s actually a return to the way the U.S. managed technological exports for decades, under what was known as the “Sliding Scale”. This paragraph from a Clinton administration fact sheet about [Export Controls on Computers](<https://www.bis.doc.gov/index.php/documents/product-guidance/340-7-1-99-fact-sheet/file>) explains the concept succinctly:

> Today’s announcement is President Clinton’s third revision to U.S. export control parameters since 1993. Today’s announcement reflects this Administration’s efforts to ensure effective controls on militarily sensitive technology while taking into account the increased availability of commodity products, such as servers and workstations, of which millions are manufactured and sold worldwide every year.
>
> When controls were last revised in 1995, we knew computer technology would continue to advance rapidly — and that we would need to update control levels periodically. Accordingly, for the past year, the Administration has conducted a review of our computer export controls that took into account (1) the rapid advance of computing technology since 1995, (2) our security, nonproliferation and other national security interests, and (3) the need for a policy that would remain effective for at least six months.
>
> The Administration’s computer export controls are designed to permit the government to calibrate control levels and licensing conditions depending upon the national security or proliferation risk posed at a specific destination, and to enhance U.S. national security and preserve the technological lead of the U.S. computer industrial base by ensuring controls on computer exports are effective and do not unnecessarily impede legitimate computer exports.

This fact sheet is one of many running across multiple administrations; the overarching goal has traditionally been to preserve U.S. dominance on the leading edge without creating the conditions for that dominance to be superceded by alternatives created elsewhere, which is not only a national security threat, but also reduces the competitiveness of U.S. firms by denying them the revenue that fuels R&D.

The best evidence that this framework is at play was [this story from Bloomberg](<https://www.bloomberg.com/news/articles/2025-12-09/trump-s-reprieve-for-nvidia-s-h200-spurred-by-huawei-s-ai-gains>):

> President Donald Trump decided to let Nvidia Corp. sell its H200 artificial intelligence chips to China after concluding the move carried a lower security risk because the company’s Chinese archrival, Huawei Technologies Co., already offers AI systems with comparable performance, according to a person familiar with the deliberations.
>
> Administration officials who weighed whether to clear Nvidia’s H200 had considered multiple possible scenarios, factoring in the views of national security hawks in Washington, said the person. Options ranged from exporting zero AI chips to China to allowing exports of everything to flood the Chinese market and overwhelm Huawei. Ultimately the policy backed by Trump called for clearing H200s to China while holding back the latest Nvidia chips for American customers, the person said.
>
> The move would give the US an 18-month advantage over China in terms of what AI chips customers in each market receive, with American buyers retaining exclusive access to the latest products, the person said. White House officials concluded that pushing the H200 into China would prod Chinese AI developers into building on the US tech ecosystem rather than turning to offerings from Huawei or other local chipmakers…
>
> Underpinning the move was an assessment that Huawei can compete far more closely with Nvidia than the US has acknowledged. White House officials focused on a Huawei AI platform known as CloudMatrix 384 that relies on the company’s newer Ascend chips, the person said. Officials found that CloudMatrix 384 performed as well as a similar Nvidia system known as NVL72 that uses the US company’s most advanced Blackwell-design chips, according to the person, who spoke on condition of anonymity to discuss sensitive matters. Adding a sense of urgency, the person said, was a conclusion by US officials that Huawei would be capable in 2026 of producing a few million of its Ascend 910C accelerators, a chip designed specifically to compete with Nvidia’s product line. That compares with a US estimate, given in June, that the Shenzhen-based company would be able to make just 200,000 of the Ascend line this year.

I wrote about the CloudMatrix 384 in [this Update](<https://stratechery.com/2025/nvidia-h20-restricted-in-china-the-huawei-cloudmatrix-384-whither-chip-controls/>) — the same Update where I criticized the Trump administration for banning the H20 — and concluded:

> The reality is that right now we are in the messy middle: we’re not actually stopping Huawei from building a system that is capable of doing large language model training (albeit inefficiently), but we are hurting the fortunes of a U.S. AI champion and limiting their long-term competitiveness. And, of course, we are incentivizing everyone in China, from the government to private enterprise, to ultimately remove the point of leverage that we can’t even wield properly.

We aren’t in the messy middle anymore! More generally, what this move signals is an overall decision to not treat AI like it’s something special — the Biden administration was, I thought, [overly influenced](<https://stratechery.com/2023/attenuating-innovation-ai/>) by the doomer wing of AI — but rather like the latest iteration of American-developed technology.

### A Good Decision

My position on this decision will not surprise long-time readers: I think it’s a good one.

First, as I laid out in [AI Promise and Chip Precariousness](<https://stratechery.com/2025/ai-promise-and-chip-precariousness/>), I think that the vast majority of discussions about the national security implications of AI are too narrow. Ban proponents limit their consideration to AI itself and its military applications, and imagine a world where the U.S. develops extraordinary capabilities that maintain and/or restore our military dominance generally, and over China specifically.

However, there are three big problems with this point of view.

  * First, I think that one country having a massive military advantage results in an unstable equilibrium; to reach back to the Cold War and nuclear as an obvious analogy, mutually assured destruction actually ended up being much more stable.
  * Second, while the U.S. did have such an enviable position after the dissolution of the Soviet Union, that technological advantage was married to a production advantage; today, however, it is China that has the production advantage, which I think would make the situation even more unstable.
  * Third, U.S. AI capabilities are dependent on fabs in Taiwan, [which are trivial for China to destroy](<https://stratechery.com/2020/chips-and-geopolitics/>), at massive cost to the entire world, particularly the United States.



If there were an alternate universe where the U.S. (1) had a clear technological edge in warfare and (2) had the best production capacity and (3) made the components that undergirded that edge in the United States, then that would be one thing — it would be the situation in the world circa 1990. But that simply isn’t the case, which I think should force considerably more modesty on those who dream of AI being a long-term military differentiator.

Second, I continue to think it is worth it and — despite the protestations of the Chinese government — possible to maintain the U.S.’s relative advantage and ecosystem dominance. Even if we grant that the CloudMatrix 384 has comparable performance to an Nvidia NVL72 server — which I’m not completely prepared to do, but will for purposes of this point — performance isn’t all that matters. Ecosystems are far more than just chips: they are software, and developers, and libraries, and APIs, all of which are dependent on the voluntary choices of the most talented people in the world to use. You can pass a law and pay out a subsidy to build a chip; you can’t use the same blunt tools to align the talent necessary to overcome the massive multi-faceted moat that Nvidia has built around their chips. This is a point that I think that people in technology get intuitively, and which completely escapes most people in Washington, who view everything as a commodity; the talent to actually build AI is anything but.

That, by extension, is why I don’t see the Trump administration’s offering as some sort of unilateral giveaway; rather, they are calling the Chinese government’s bluff. That’s how I read [this story in the Financial Times](<https://www.ft.com/content/c4e81a67-cd5b-48b4-9749-92ecf116313d>):

> Beijing is set to limit access to Nvidia’s advanced H200 chips despite Donald Trump’s decision to allow the export of the technology to China as it pushes to achieve self-sufficiency in semiconductor production. According to two people with knowledge of the matter, regulators in Beijing have been discussing ways to permit limited access to the H200, Nvidia’s second-best generation of artificial intelligence chips. Buyers would probably be required to go through an approval process, the people said, submitting requests to purchase the chips and explaining why domestic providers were unable to meet their needs. The people added that no final decision had been made yet.

China has limited access to H20 chips, and you could spin this news as the country successfully holding the line until they got the real deal — and doing so successfully; note that the story doesn’t say the H200 will be banned on the China side. That, however, is why the H200 offer is an effective counteroffer: the real ecosystem payoff is in training, and there’s no question that the best Chinese talent is going to want to work with the H200, not the Huawei alternative. To that end, the choice facing China is continued progress on AI, or a multi-year pause and stringent _import_ controls, which I’m skeptical will be effective. It was one thing to align the necessary ingredients for an indigenous AI ecosystem when the U.S. was doing you the favor of not selling you chips; it’s another thing entirely to make fetch happen on your own from the top down.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
