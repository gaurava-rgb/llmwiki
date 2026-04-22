---
title: "Three Years from GPT-3 to Gemini 3"
reader_id: "01kabyhcwxyyzcpz08pa87kh1z"
notion_page_id: ""
category: "email"
source_type: ""
reader_url: "https://read.readwise.io/read/01kabyhcwxyyzcpz08pa87kh1z"
source_url: "mailto:reader-forwarded-email/e0ba198dc734da5bb35d48029b9b6937"
author: "Ethan Mollick from One Useful Thing"
site: "Substack"
tags: []
published: "2025-11-18"
saved_at: "2025-11-18"
reading_time: "7 mins"
summary: "Three years after GPT-3, Google’s Gemini 3 shows AI can not only write but build, code, and act like a digital coworker. It creates websites, runs analyses, and even produced a near-PhD-level research paper with human guidance. This marks a shift from chatbots to agentic tools that need managers, not fixers."
content_hash: "03b953effbde2e0a93c69a5aa29f44295152403d33e94ef0abfbcd2f1a36d17b"
---

###  From chatbots to agents

I’ve been testing Google’s new Gemini 3 model. It is very good. But rather than give you benchmark numbers, I’m going to show you how far AI has come in three years by asking the AI to demonstrate it.

It has been slightly less than three years since the release of ChatGPT. A few days before that launch, I wrote my [ first post on this Substack about OpenAI’s earlier GPT-3 model. ](<https://substack.com/redirect/aaa61d32-f2fd-44a8-8f08-dd50c391bdaa?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) Then ChatGPT came out, and I [ wrote ](<https://substack.com/redirect/d766755c-ab75-4ce6-a483-776147684eeb?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) immediately afterwards that “I am usually pretty hesitant to make technology predictions, but I think that this is going to change our world much sooner than we expect, and much more drastically. Rather than automating jobs that are repetitive & dangerous, there is now the prospect that the first jobs that are disrupted by AI will be more analytic; creative; and involve more writing and communication.”

I think I got that one right.

[ ![](https://substackcdn.com/image/fetch/$s_!L1NO!,w_548,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ac6903e-8339-49df-b41f-ff9848694f9f_1239x1166.png) ](<https://substack.com/redirect/310e679b-c933-4aa9-ade0-45d0a7f0fc0d?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) My first post after using GPT-3.5 three years ago

I could explain the difference between the original ChatGPT and the new AI model from Google, Gemini 3, that launched today. But I don’t have to. Instead, I gave the screenshot above to Gemini 3 with a single prompt:

**Me:** “show how far AI has come since this post by doing stuff.”

**Gemini:** “I can definitely show you the difference. The tweet you shared is from November 2022—right on the cusp of the modern AI boom. Back then, the “wow factor” was that an AI could write a coherent _paragraph_ or a simple poem about a silly concept like a “candy-powered FTL drive escaping otters.”

To demonstrate how far we’ve come, I’m not just going to write text about it. I have built you a **fully interactive, playable Candy-Powered FTL Starship Simulator** .

In 2022, AI could describe the engine. In 2025, AI can code the engine, design the interface, and let you pilot the ship yourself.”

[ ![](https://substackcdn.com/image/fetch/$s_!3f20!,w_466,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F349214f1-3e41-459d-ac2f-24574f1c75c9_1878x1706.png) ](<https://substack.com/redirect/c2a0ce61-f3f9-4eb0-8021-8127b5f60264?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>)

And, indeed, it built me a tiny game where I had to use the power of candy to escape otters, featuring small poems and an ongoing set of amusing updates. If you’re reading this blog, you probably knew AI could do that. What’s more interesting is what else Gemini 3 can do when you stop thinking of it as a chatbot and start thinking of it as something else entirely

#  Coding tools that aren’t just coding tools

Along with Gemini 3, Google has launched Antigravity. For programmers, Antigravity should be familiar territory, it is similar to Claude Code and OpenAI Codex, specialized tools that can be given access to your computer and which can autonomously write computer programs with guidance. If you aren’t a programmer, you may dismiss Antigravity and similar tools. I think that is a mistake because the ability to code isn’t just about programming, it’s about being able to do anything that happens on a computer. And that changes what these tools actually are.

Gemini 3 is very good at coding, and this matters to you even if you don’t think of what you do as programming. A fundamental perspective powering AI development is that everything you do on a computer is, ultimately, code, and if AI can work with code it can do anything someone with a computer can: build you dashboards, work with websites, create PowerPoint, read your files, and so on. This makes agents that can code general purpose tools. Antigravity embraces this idea, with the concept of an Inbox, a place where I can send AI agents off on assignments and where they can ping me when they need permission or help.

[ ![](https://substackcdn.com/image/fetch/$s_!g_pi!,w_436,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d46f934-2f6b-4db4-8ec6-90db72a96fb4_1342x1093.png) ](<https://substack.com/redirect/b20cb0c6-766e-472b-b8dc-2613b093e7a7?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) You can see I am working with four different agents right now, one is working and another needs my help to proceed.

I don’t communicate with these agents in code, I communicate with them in English and they use code to do the work. Because Gemini 3 is good at planning, it is capable of figuring out what to do, and also when to ask my approval. For example, I gave Antigravity access to a directory on my computer containing all of my posts for this newsletter.¹ I then asked Gemini 3,0: “I would like an attractive list of predictions I have made about AI in a single site, also do a web search to see which I was right and wrong about.” It then read through all the files, executing code, until it gave me a plan which I could edit or approve. The screenshot below is the first time the AI asked me anything about the project, and its understanding of what I wanted was impressive. I made a couple of small changes and let the AI work.

[ ![](https://substackcdn.com/image/fetch/$s_!iw2C!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F748a5067-4fed-449a-bac8-46dfaf5a00b2_2223x1538.png) ](<https://substack.com/redirect/6049f5bf-95e0-4ae1-a0f4-f62c9dec3f44?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>)

It then did web research, created a site, took over my browser to confirm the site worked, and presented me the results. Just as I would have with a human, I went through the results and made a few suggestions for improvement. It then packaged up the results so I could [ deploy them here. ](<https://substack.com/redirect/1080efb8-6fad-4223-a559-24859c37de6e?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>)

[ ![](https://substackcdn.com/image/fetch/$s_!wv8T!,w_158,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d9bc5fc-2520-4877-9637-4d9d55a63bd4_909x1492.png) ](<https://substack.com/redirect/4a2beab8-35b9-4083-b4be-9c4f1080099c?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>)

It was not that Gemini 3.0 was capable of doing everything correctly without human intervention — agents aren’t there yet. There were no hallucinations I spotted, but there were things I corrected, though those errors were more about individual judgement calls or human-like misunderstandings of my intentions than traditional AI problems. Importantly, I felt that I was in control of the choices AI was making because the AI checked in and its work was visible. It felt much more like managing a teammate than prompting an AI through a chat interface.

#  PhD Level Intelligence?

But Antigravity isn’t the only way Gemini 3 surprised me. The other was in how it handled work that required genuine judgment. As I have mentioned many times on this site, benchmarking AI progress is a mess. Gemini 3 takes a definitive benchmark lead on most stats, (although it may still not be able to beat the $200 GPT-5 Pro Model, but I suspect that might change when Gemini 3’s inevitable Deep Think version comes out). But you will hear one phrase repeated a lot in the AI world - that a model has “PhD level intelligence.”

I decided to put that to the test. I gave Gemini 3 access to a directory of old files I had used for research into crowdfunding a decade ago. It was a mishmash of files labelled things like “project_final_seriously_this_time_done.xls” and data in out-of-date statistical formats. I told the AI to “figure out the data and the structure and the initial cleaning from the STATA files and get it ready to do a new analysis to find new things.” And it did, recovering corrupted data and figuring out the complexities of the environment.

Then I gave it a typical assignment that you would expect from a second year PhD student, doing minor original research. With no further hints I wrote: “great, now i want you to write an original paper using this data. do deep research on the field, make the paper not just about crowdfunding but about an important theoretical topic of interest in either entrepreneurship or business strategy. conduct a sophisticated analysis, write it up as if for a journal.” I gave it no suggestions beyond that and yet the AI considered the data, generated original hypotheses, tested them statistically, and gave me formatted output in the form of a document. The most fascinating part was that I did not give it any hints about what to research, it walked the tricky tightrope of figuring out what might be an interesting topic and how to execute it with the data it had - one of the hardest things to teach. After a couple of vague commands (“build it out more, make it better”) I got a 14 page paper.

[ ![](https://substackcdn.com/image/fetch/$s_!vJvs!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e997e6a-f569-43e0-addc-f97f4c760208_2325x1404.png) ](<https://substack.com/redirect/8716d946-2a6f-49ba-8422-003d4067472c?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) The first two pages of the paper

Aside from this, I was impressed that the AI came up with its own measure, a way of measuring how unique a crowdfunding idea was by using natural language processing tools to compare its description mathematically to other descriptions. It wrote the code, executed it and checked the results.

[ ![](https://substackcdn.com/image/fetch/$s_!lbO3!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9c0c03a-1306-4e1a-8200-8aa41890418b_2202x1362.png) ](<https://substack.com/redirect/44f89822-d863-4756-b1fa-0451ea6b3653?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>)

So is this a PhD-level intelligence? In some ways, yes, if you define a PhD level intelligence as doing the work of a competent grad student at a research university. But it also had some of the weaknesses of a grad student. The idea was good, as were many elements of the execution, but there were also problems: some of its statistical methods needed more work, some of its approaches were not optimal, some of its theorizing went too far given the evidence, and so on. Again, we have moved past hallucinations and errors to more subtle, and often human-like, concerns. Interestingly, when I gave it suggestions with a lot of leeway, the way I would a student: (“make sure that you cover the crowdfunding research more to establish methodology, etc.”) it improved tremendously, so maybe more guidance would be all that Gemini needed. We are not there yet, but “PhD intelligence” no longer seems that far away.

#  Gemini 3

Gemini 3 is a very good thinking and doing partner that is available to billions of people around the world. It is also a sign of many things: the fact that we have not yet seen a significant slowdown in AI’s continued development, the rise of agentic models, the need to figure out better ways to manage smart AIs, and more. It shows how far AI has come.

Three years ago, we were impressed that a machine could write a poem about otters. Less than 1,000 days later, I am debating statistical methodology with an agent that built its own research environment. The era of the chatbot is turning into the era of the digital coworker. To be very clear, Gemini 3 isn’t perfect, and it still needs a manager who can guide and check it. But it suggests that “human in the loop” is evolving from “human who fixes AI mistakes” to “human who directs AI work.” And that may be the biggest change since the release of ChatGPT.

[ ![](https://substackcdn.com/image/fetch/$s_!f-5x!,w_302,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe20744fc-7146-409d-8eff-519e9a2d13d7_2181x1296.png) ](<https://substack.com/redirect/852641f0-2eae-4e33-891c-89607a2a6c6b?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) I asked Gemini “using code alone create a really good cover image for my post about Gemini 3.0 in Substack, look up what size those images are” and the AI was able to use a combination of tools, from web browsing to coding, to create an image using math alone.

1Obligatory warning: Giving an AI agent access to your computer can be risky if you don’t know what you are doing. They can move or delete files without asking you and can potentially present a security risk as well by exposing your documents to others. I suspect many of these problems will be addressed as these tools are adapted to non-coders, but, for now, be very careful.

_You’re currently a free subscriber to One Useful Thing. Subscriptions are optional but help support my work._

[ View in app ](<https://substack.com/app-link/post?publication_id=1180644&post_id=178246604&isFreemail=true&r=6fumam>)
