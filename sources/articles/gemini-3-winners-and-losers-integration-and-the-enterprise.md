---
title: "Gemini 3, Winners and Losers, Integration and the Enterprise"
reader_id: "01kaekrksbjjmadcsggf7n25aj"
notion_page_id: "3484ebe7-f118-811a-b4fd-fc02ce323a3d"
reader_url: "https://read.readwise.io/read/01kaekrksbjjmadcsggf7n25aj"
source_url: "https://stratechery.com/2025/gemini-3-winners-and-losers-integration-and-the-enterprise/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-11-19"
saved_at: "2025-11-19"
reading_time: "11 mins"
summary: "Gemini 3 is out, and looks to be state of the art. What does that mean for everyone else in the AI space, and what markets might Google win?"
content_hash: "7d279b2002915851cb40d1d27ecfe65ff9820ee5fe215b10c8dc1f076612d394"
---

Gemini 3 is out, and looks to be state of the art. What does that mean for everyone else in the AI space, and what markets might Google win?

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

Next week is the Thanksgiving holiday in the U.S.; there will be Stratechery Updates on Monday and Tuesday, and then I will be off the rest of the week.

Three points of clarification and/or corrections:

  * First, [there is a Microsoft 365 Copilot app](<https://www.microsoft.com/en-us/microsoft-365-copilot/download-copilot-app>), that is distinct from the Copilot app; it’s nothing more than a webview of the exact same page you get in the browser. So, from my perspective, it’s pretty worthless, but I guess this is a correction, because it does exist.
  * Second, [on last week’s Sharp Tech](<https://sharptech.fm/member/episode/how-apple-changed-the-cellular-economy-what-space-x-wants-to-do-with-spectrum-airlines-and-carriers-yann-le-cun-departs-meta>), I said that Spectrum (and Comcast’s) service on Verizon was deprioritized; this is not true, as both services operate on the same priority level as Verizon’s services.
  * Third, with regards to yesterday’s Article [Robotaxis and Suburbia](<https://stratechery.com/2025/robotaxis-and-suburbia/>), I should have noted that [Waymo and DoorDash have partnered to launch a pilot delivery service](<https://about.doordash.com/en-us/news/waymo>).



On to the Update:

### Gemini 3

From the Wall Street Journal, in an Article entitled [Google Seeks to Shake Up Chatbot Race With New Gemini Version](<https://www.wsj.com/tech/ai/google-seeks-to-shake-up-chatbot-race-with-new-gemini-version-9a393172>):

> Alphabet’s Google has been playing catch-up in artificial intelligence ever since OpenAI introduced ChatGPT in 2022. The Tuesday launch of Gemini 3, an updated version of its own large language model, offers a chance to narrow that gap — and perhaps bring its considerable advantages to bear in the race for AI supremacy. The company said Gemini 3 will improve the sophistication of answers to queries in its Gemini app, as well as those made using AI Mode in the Google search engine. The new model is also significantly more skilled at coding, developing applications and generating images, the company said…
>
> Google has already gained significant traction this year, in part because of an image-generation tool called Nano Banana. The company in August uploaded it to a public platform that ranks AI models, and within days, it was topping the leaderboard, trending on X and overwhelming Google’s expectations for usage. Since its launch, people have used it to create more than five billion images, Google said. With Nano Banana, growth in Gemini usage is on its fastest trajectory to date. Gemini now has 650 million monthly active users, up from 450 million in July. The company says queries on the app have tripled since this spring, and that since Nano Banana was introduced, users who try out the Gemini app are more than twice as likely to come back as they had been before.
>
> ChatGPT still far outpaces usage of Gemini. The company said this month that it now has 800 million active users each week, up from 700 million in July. But Nano Banana took off in part because it generates images much more quickly than other AI models. Unlike ChatGPT, which can take a minute or longer to produce images, Nano Banana does so within seconds. Many users say the images they create are significantly more lifelike as well, with fewer imperfections such as extra fingers or distorted features.

Gemini 3, at least on day one, appears to live up to the hype. It [dominates benchmarks](<https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini_3_table_final_HLE_Tools_on.gif>) (with the exception of SWE-Bench Verified, a coding benchmark, which Claude Sonnet 4.5 still leads), and the [early](<https://www.oneusefulthing.org/p/three-years-from-gpt-3-to-gemini>) [reviews](<https://simonwillison.net/2025/Nov/18/gemini-3/>) are very positive. The most effusive came from [Matt Shumer](<https://shumer.dev/gemini3review>):

> Let’s start with the creative writing, because that’s where Gemini 3 first floored me. GPT-5.1, which dropped last week, was already a noticeable jump from previous frontier models. But Gemini 3? It wrote book chapters I had to double-check weren’t plagiarized from a real book. The voice was coherent. The pacing natural, the turns of phrase genuinely surprising. But most importantly, it didn’t feel like the “AI slop” writing we all know just a little too well. It’s really impressive… Gemini 3 doesn’t just put out “good for AI” writing, it puts out genuinely good writing.
>
> The improvements feels fundamental. Previous models had a certain spikiness… their quality varied wildly depending on the task. You could get brilliance on one task, followed by just-okay results on another. Gemini 3 is more consistent, less prone to those jarring spikes. My hunch is that Google has cracked something about reinforcement learning on non-verifiable tasks… creative work where you can’t just check if the answer is right. The result is a model that feels more like a skilled collaborator than anything we’ve had before.
>
> That said, here’s an important note: for 80% of your daily work, you might not even notice the difference. Current models are already “good enough” for writing emails or making small changes to your webapp. So at first glance, Gemini 3 doesn’t always feel like a massive leap. But that feeling is deceptive. The jump is there, it’s just hiding in the difficult 20%… the complex reasoning, the subtle creative choices, the edge cases where other models fall apart. When you really need that extra brainpower, it’s there.
>
> Another standout feature: it’s fast for how smart it is. To understand this, we can think of a metric like “intelligence per second”, and Gemini 3 is fantastic in this regard.

Shumer concludes:

> If GPT-5.1 is a solid junior engineer, Gemini 3 is a senior engineer who says “got it, done”, and you better check that it’s actually done. I keep reaching for it, not because it’s perfect, but because when it’s right, it’s brilliantly, almost humanly right. This is, without a doubt, my new daily driver. And with Google’s computing power and ability to serve this cheaply and stably I’d bet this is going to be a winner.

The most interesting thing that Shumer highlights is speed; I gave ChatGPT’s auto-router a try for a while, but I’m back on the Thinking model exclusively, just because the answers are so consistently better; having to always wait for said answer, however, is pretty annoying. A meaningful speed increase with even equivalent quality answers would be awesome, and a reason to change, much less _better_ answers. That said, I’ll reserve judgment; for what it’s worth one of my first questions to Gemini was a networking question that ChatGPT frankly gave a far more accurate and more useful answer to. That could be luck of the draw, but it’s a reminder that a model’s quality reveals itself over time.

There is one specific Gemini feature I want to call out:

![](https://pbs.twimg.com/profile_images/935325968280907776/AcBo6zJc.jpg)

[Jeff Dean](<https://twitter.com/JeffDean>) [@JeffDean](<https://twitter.com/JeffDean>)

[ ](<https://twitter.com/JeffDean/status/1990817283589943594>)

As an example of how we are building on top of Gemini 3, AI Mode in Search now uses Gemini 3 to enable new generative UI experiences, all generated completely on the fly based on your query. Here’s how you might use this to learn a complex topic like how RNA polymerase works.

Your browser does not support the video tag. [Posted Nov 18, 2025 at 4:20PM](<https://twitter.com/JeffDean/status/1990817283589943594>)

I can’t embed this tweet, because while X still has the “Embed post” option, it goes to the Twitter domain and doesn’t work, but if you click through there is a video of Gemini generating UI on the fly in response to a query; in other words, [The Gen AI Bridge to the Future](<https://stratechery.com/2024/the-gen-ai-bridge-to-the-future/>) is very much being built.

### Winners and Losers

Let’s assume, however, that the benchmarks are right, and Gemini is, in every respect but perhaps coding, state of the art; what does that mean for the other players in the AI ecosystem?

**Google:** The biggest winner, it goes without saying, is Google. The company may have been caught napping by OpenAI and ChatGPT, but clearly the behemoth — the company whose resources were so vast that it drove Elon Musk and Sam Altman together in the first place in an attempt to avoid a future where Google won AI by default — is very much awake. Moreover, the company is well-positioned to push its advantage:

  * Google is fully integrated from TPUs to models to applications; this is the structure that you would expect to win in the beginning stages of a new technology, and that is — finally — exactly what they appear to be doing, at least as far as model capability is concerned.
  * Google has massive cash flow to fund continued AI development, obvious owned-and-operated applications for its models, and a rapidly growing cloud service that is gaining a significant differentiator.
  * Google has the lowest cost structure of any of the leading model makers, thanks to their dependence on their own in-house TPUs, on which Gemini was trained.



To date Google has leveraged its cash flow and cost advantage to offer Gemini at a lower price than OpenAI or Anthropic’s models; what is notable about Gemini 3, however — and perhaps the strongest evidence that Google itself believes that Gemini 3 is superior to the alternatives — is that its pricing is more expensive than GPT-5.1 (although still less expensive than GPT-5.1-Pro and Anthropic’s leading models). Google appears to not yet be ready to accept that models are commodities; to the extent they are right is very good for the company’s long-term margins (alternatively, this might be a really expensive model to serve, which is more bearish).

**Anthropic:** I think that Anthropic is a winner from this announcement as well: whatever secret sauce that Anthropic figured out with regards to coding appears to be a durable advantage; as I noted above that is the one benchmark that Gemini didn’t win. It’s that coding prowess that is driving Claude’s penetration into the enterprise, and Anthropic’s own sky-rocketing valuation (more on this in a moment).

**OpenAI:** There were lots of people on X yesterday pronouncing doom and gloom for OpenAI: if Google has the best model, and Anthropic the best coding, then what does OpenAI have? The answer — the importance of which should be obvious to Stratechery readers — is around 800 million weekly active users of ChatGPT. I am going to give Gemini a try as my primary AI model (although the lack of a Mac app continues to be a real frustration); most people will not, particularly as the gains are increasingly imperceptible to most consumers. That leads to a possible market structure of — actually, hold that one, because I’m going to come back to it in a moment as well.

**Nvidia:** This is maybe the most interesting one. Nvidia, which reports earnings later today (and which I’ll cover next week), is on one hand a loser, because the best model in the world was not trained on their chips, proving once and for all that it is possible to be competitive without paying Nvidia’s premiums.

On the other hand, there are two reasons for Nvidia optimism. The first is that everyone needs to respond to Gemini, and they need to respond now, not at some future date when their chips are good enough. Google started its work on TPUs a decade ago; everyone else is better off sticking with Nvidia, at least if they want to catch up.

Secondly, and relatedly, Gemini re-affirms that the most important factor in catching up — or moving ahead — is more compute. This post is from the Vice-President of Research at DeepMind:

![](https://pbs.twimg.com/profile_images/677499217993007104/Uartsv8s.jpg)

[Oriol Vinyals](<https://twitter.com/OriolVinyalsML>) [@OriolVinyalsML](<https://twitter.com/OriolVinyalsML>)

[ ](<https://twitter.com/OriolVinyalsML/status/1990854455802343680>)

The secret behind Gemini 3?

Simple: Improving pre-training & post-training 🤯

P**re-training:** Contra the popular belief that scaling is over—which we discussed in our NeurIPS '25 talk with [@ilyasut](<https://twitter.com/ilyasut>) and [@quocleix](<https://twitter.com/quocleix>)—the team delivered a drastic jump. The delta between 2.5 and 3.0 is as big as we've ever seen. No walls in sight!

P**ost-training:** Still a total greenfield. There's lots of room for algorithmic progress and improvement, and 3.0 hasn't been an exception, thanks to our stellar team.

Congratulations to the whole team 💙💙💙


![](https://pbs.twimg.com/media/G6DraPpWMAAMJFY.jpg) [Posted Nov 18, 2025 at 6:47PM](<https://twitter.com/OriolVinyalsML/status/1990854455802343680>)

This is of course good for Google — [the GPU-Rich in a world of GPU-Poors](<https://newsletter.semianalysis.com/p/google-gemini-eats-the-world-gemini>) — but, just like the last point, it’s good for Nvidia, because more GPUs mean better models.

**Apple:** [White-labeling Gemini](<https://stratechery.com/2025/apple-earnings-siri-white-labels-gemini-short-term-gains-and-long-term-risk/>) is looking like a pretty good option!

### Integration and the Enterprise

I said above I wanted to come back to market structure, and I’ll start with another big news story from yesterday; from [a joint press release](<https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/>) from Microsoft, Nvidia, and Anthropic:

> Today Microsoft, Nvidia and Anthropic announced new strategic partnerships. Anthropic is scaling its rapidly-growing Claude AI model on Microsoft Azure, powered by Nvidia, which will broaden access to Claude and provide Azure enterprise customers with expanded model choice and new capabilities. Anthropic has committed to purchase $30 billion of Azure compute capacity and to contract additional compute capacity up to one gigawatt.
>
> For the first time, Nvidia and Anthropic are establishing a deep technology partnership to support Anthropic’s future growth. Anthropic and Nvidia will collaborate on design and engineering, with the goal of optimizing Anthropic models for the best possible performance, efficiency, and TCO, and optimizing future Nvidia architectures for Anthropic workloads. Anthropic’s compute commitment will initially be up to one gigawatt of compute capacity with Nvidia Grace Blackwell and Vera Rubin systems.
>
> Microsoft and Anthropic are also expanding their existing partnership to provide broader access to Claude for businesses. Customers of Microsoft Foundry will be able to access Anthropic’s frontier Claude models including Claude Sonnet 4.5, Claude Opus 4.1, and Claude Haiku 4.5. This partnership will make Claude the only frontier model available on all three of the world’s most prominent cloud services. Azure customers will gain expanded choice in models and access to Claude-specific capabilities.
>
> Microsoft has also committed to continuing access for Claude across Microsoft’s Copilot family, including GitHub Copilot, Microsoft 365 Copilot, and Copilot Studio. As part of the partnership, Nvidia and Microsoft are committing to invest up to $10 billion and up to $5 billion respectively in Anthropic.

On one hand, yes, this is another circular investment: Anthropic is getting funding from Microsoft and Nvidia to buy GPUs from the latter and run its models on the former’s Azure cloud service. It’s also a totally reasonable and expected response to Google. No one is going to catch up to Google’s integrated advantages (pour one out for AWS and Trainium, perhaps the most clear-cut loser yesterday, particularly in light of this news); the most logical competitive response is to lean into modularity.

This is clearly Microsoft’s strategy, as [I discussed after their earnings](<https://stratechery.com/2025/microsoft-earnings-coreai-mantleai-additional-notes/>); adding Anthropic to Azure is the best possible option right now to decrease dependence on OpenAI ahead of the loss of exclusive access to OpenAI’s models in a few years. Anthropic, meanwhile, is now on all three major clouds, a big selling point for enterprises. Nvidia, of course, wants to maintain its position as the most important and irreplaceable part of the value chain for everyone who isn’t Google.

This is where it really gets interesting: if you look at past computing paradigms, including both PCs and the smartphone, you would expect the integrated option to get the most traction in the consumer space, while the modular alternative is preferred by enterprises eager to avoid lock-in. OpenAI, however, still has that significant lead in consumer; that would seem to suggest that Google’s biggest opportunity is in enterprise, but to what extent will the company be hampered by the fact that enterprises may be reluctant to go all-in with Google, knowing that means they could be locked in to the Google stack?

This is where the extent of Google’s lead — and, to the extent it exists, their ability to extend it — is going to matter a great deal. If Gemini is truly better at agentic workflows, to take the most pertinent example, then enterprises, eager for the potential cost savings that AI represents, may decide the lock-in risk is worth it; if the lead is less than it seems now, or is fleeting, then Google’s integration may have its downsides in terms of finding as big of a market as you might expect.

Of course that isn’t all that matters: Gemini will power all of Google’s own apps and services, and impressively, launched first day in Google Search’s AI Mode. Moreover, [as I noted in the context of YouTube](<https://stratechery.com/2025/the-youtube-tip-of-the-google-spear/>), just because consumer AI is mostly text now doesn’t mean it will be mostly text forever, and Google’s lead in images and video has already been established. Indeed, that is the ultimate Google bull case: as the saying goes, AI is the worst it will ever be; we could look back sooner rather than later and say that this was as small as Google’s lead ever was.

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
