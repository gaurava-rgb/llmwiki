---
title: "Claude Dispatch and the Power of Interfaces"
reader_id: "01kn30rqjr9qpc064dznw8ats2"
notion_page_id: "34a4ebe7-f118-81eb-bb55-ce0c393acce0"
category: "email"
source_type: ""
reader_url: "https://read.readwise.io/read/01kn30rqjr9qpc064dznw8ats2"
source_url: "mailto:reader-forwarded-email/2267e8e44115d8ce561b6c8438cec91f"
author: "Ethan Mollick from One Useful Thing"
site: "Substack"
tags: []
published: "2026-03-31"
saved_at: "2026-03-31"
reading_time: "6 mins"
summary: "AI is very smart but hard to use because chatbots make work confusing and overwhelming. New tools like Claude Cowork and Dispatch let AI work with your real files and apps, making it feel like a helpful assistant. The future will have AI that creates the right interface for each task, so more people can easily benefit from AI's power."
content_hash: "d6050fe8dee0a323b8ba1d0db1da199261c2be54789ddd0d6b3515a64f0bc8d5"
---

###  We often lack the tools for the job, even if the AI is capable enough

AIs are already far more capable than most people realize. A large part of this so-called capability overhang comes not from the limits of AI (though, of course, they still have many limits), but from how people interact with it. The vast majority of people access AI through chatbots, and usually the free versions with less capable models. A chatbot is fine for a quick question, but it is a bad way to get real work done.

In fact, recent research suggests that we pay a mental tax when using chatbot interfaces for work. A [ new paper ](<https://substack.com/redirect/5a5a4aa5-739c-45f9-aed5-7ef02025e0ed?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) had a small group of financial professionals do a complex valuation task with GPT-4o¹ and measured their cognitive load from the transcripts, turn by turn. People did see a productivity gain from using AI, but some of that seemed to be offset by the fact that the AI presented information in a way that completely overwhelmed people: giant walls of text, offers to pursue new topics, and sprawling discussions. The chatbot interface appeared to be the obstacle, not the work. And once a conversation got messy, it stayed messy. The AI, optimized to be helpful, just mirrored back whatever disorganized structure the user provided while the user, overwhelmed, didn’t reorganize. Both sides kept compounding the problem. The people hurt most were less experienced workers, exactly the people who could benefit the most from AI… if they could keep track of what they were doing with it

[ ![](https://substackcdn.com/image/fetch/$s_!mhah!,w_543,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e6b8117-702a-4acf-aa4c-c6f68db7d545_2814x1536.jpeg) ](<https://substack.com/redirect/39c985b6-ba1b-4417-9728-1e6ed73ee5fa?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>)

This shouldn’t be a surprise to you if you have used a chatbot to get things done. You ask a specific question and get five paragraphs that contain the answer (somewhere!) while the AI also offers three new things you didn’t ask about. The interface itself creates cognitive costs that overwhelm the benefits of the AI’s intelligence. So what does a better interface look like?

#  Specialized interfaces

One option is to build specific interfaces for specific jobs or tasks. Of all the specialized AI interfaces, the only really complete ones are for programming. This is exactly what you would expect, the AI labs are staffed by programmers, the models are trained extensively on code, and the people building these tools are often building them for themselves.

I’ve [ written before ](<https://substack.com/redirect/cd717f55-6842-4525-b21b-acecce26c142?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) about Claude Code, Anthropic’s coding agent that can work for hours autonomously. OpenAI’s Codex and Google’s Antigravity do similar things. I have used Claude Code for everything from [ making (a small amount of) money ](<https://substack.com/redirect/51f57fcb-e9ec-48f7-9232-96c46e5cce09?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) to [ making games ](<https://substack.com/redirect/8072a462-3d72-43e6-bf40-14fb102c7a72?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) , never touching any code at all. I also find Codex incredibly useful as well, with a similar level of capability. These tools are terrific, but they are _really_ built for programmers. They assume you know Python and Git. Their interfaces look like a 1980s computer lab. For the 99% of knowledge workers who are not developers, these powerful AI tools are not optimized for them.

[ ![](https://substackcdn.com/image/fetch/$s_!q5Uz!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b00d345-c3f5-4fc2-8837-75073b845c32_2356x528.png) ](<https://substack.com/redirect/f6dc302a-4df4-408a-8fba-5dc38f6fccfb?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) Pomelli, Stitch, and NotebookLM

Of all the AI labs, Google seems to be experimenting the most with building specialized interfaces for other professions. All are a bit rough around the edges, but they show how the future might look when AI tools are built for other types of knowledge professionals. Google’s [ Stitch ](<https://substack.com/redirect/5c961224-f653-4fa5-970c-4070c32b9196?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) hints at what AI-native design could look like — an infinite canvas where you describe an app in natural language and get back multiple interconnected screens with consistent design systems. In a similar vein, [ Pomelli ](<https://substack.com/redirect/e4549aca-97e9-4e7a-a38c-e9741ae4e207?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) lets you paste your website URL and automatically generates on-brand social media campaigns, taking the language of marketing, not prompting, to make this feel less technical. And, most well-known, [ NotebookLM ](<https://substack.com/redirect/c43457fe-dd6d-43a2-98ad-d10839819356?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>) provides a way of researching, displaying, and working with diverse information sources. Each of these show where things might be heading, but it’s not yet the kind of transformative tool that Claude Code is for programmers. But there is another interface that has seen explosive growth, the personal agent.

#  Using the interfaces you already have

If you haven’t heard of it, OpenClaw is an open-source AI agent, its symbol is a red lobster, it is a security nightmare, and it has become the fastest-growing open source project in history. OpenClaw is a so successful because it is a genuine personal agent. The system is designed so that you can talk to your AI agent through WhatsApp or Telegram or Slack, the same apps you use to text people. You tell it to check your email, book a table, find a file, and it goes and does those things on your computer. It solved the interface problem in a way that felt obvious in retrospect: instead of a chatbot or a command line, it let you talk to an AI in the way that you would a person, using interfaces, like WhatsApp, that are already very familiar.

[ ![](https://substackcdn.com/image/fetch/$s_!bhGJ!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42236cb8-55bd-4bb3-a0e8-2671ce9a2f05_2391x1283.png) ](<https://substack.com/redirect/e5e31bce-dd1e-4212-806a-28aa714e39a1?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>)

OpenClaw, however, is hard to use and provides a lot of security risks. Anthropic’s answer is Claude Cowork with Dispatch. Cowork, which launched in January, is a version of Claude Code for knowledge workers. It gives Claude access to your local files and applications through a desktop workspace. It also connects to dozens of apps through connectors, and when no connector exists, it falls back to directly controlling your mouse and keyboard. Dispatch, which came in the last couple weeks, adds the key piece: you can message Claude from your phone while it works on your desktop. You scan a QR code, and your phone becomes a remote control for an AI agent sitting at your computer.

Using a combination of Dispatch and Claude Code creates an interface that feels like talking to a competent assistant. For example, I asked Claude from my phone to prepare a morning briefing, and it reads from my calendars, emails, and online channels, then gives me a report on what I need to do next. But Cowork also does more complex work. From my phone, I asked it to look at a recent presentation I made and see if the graph in Slide 3 was up-to-date, and, if not, to update it. You can see that it got slightly stuck at one place (a site blocked it from downloading a file), but, aside from that, the results were very impressive. It opened and “viewed” the PowerPoint and investigated my entire computer for more up-to-date data. When I gave it a link to a more updated online paper, it downloaded the PDF, located the newer graph, clipped out the image of the graph, and updated my PowerPoint for me. This is sophisticated and complicated work, that, even if not always seamless, is usually close enough to save a lot of time.

[ ![](https://substackcdn.com/image/fetch/$s_!c3Lr!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21982406-3d63-459e-bcf5-4f3731c7dec2_1693x1113.png) ](<https://substack.com/redirect/0bbd0c0f-61fa-4367-8732-2871b661fe46?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>)

Is this as flexible as OpenClaw? No. Cowork is sandboxed, safer but more limited (but that doesn’t mean there aren’t security risks). The connector ecosystem is growing but incomplete. And the idea that Cowork can use your computer is impressive as a concept and error-prone in practice. But the core insight is the same one OpenClaw stumbled onto. People don’t want a chatbot. They want an agent that works on their actual files, with their actual tools, accessible the way they talk to people.

#  Interfaces on Demand

All of this assumes that we need to decide our interfaces in advance. But the latest AI systems can actually build an interface for you. For example, over the past few weeks, Claude gained the ability to generate visualizations directly in the conversation. These aren’t static images. They’re interactive, adjustable, and Claude can modify them as you ask follow-up questions.

[ ![](https://substackcdn.com/image/fetch/$s_!tmFI!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45e99e6d-10df-4f09-90c9-c34ed3eebf44_2102x1593.png) ](<https://substack.com/redirect/e77f048c-17e1-4174-94c1-abd300a43d28?j=eyJ1IjoiNmZ1bWFtIn0.GyHcZoDE-MxbdQ2qPakLa5PwtJvSjuuMfwOXdUaTNWw>)

This is a different approach to the interface problem. Instead of having companies build a specialized interface for every kind of work, the AI generates the right interface on the fly. I suspect the future isn’t one interface to rule them all. It’s AI that generates the right interface for the moment, an agent on your desktop, a chart in a conversation, a custom app to solve a problem. We’re moving from adapting to the AI’s interface to the AI adapting its interface to you.

AI capability has been running ahead of AI accessibility. The models have been smart enough to do extraordinary things for a while now, but we’ve been making people access that intelligence through chatbots. And, as that cognitive load research shows, the chatbot format is actively working against them. As interfaces improve, we’re going to see what happens when a much larger number of people can actually use what AI is capable of. Every new interface that closes even part of that gap will feel like a leap in AI capability, even when the models haven’t changed (though they are still changing). My guess is that a lot of the “AI disappointment” people sometimes express comes not from the AI being bad, but from the interfaces being wrong. We built one of the most powerful technologies in recent history and then made people access it by typing into a chat window. That will change soon.

1It is always good to be cautious about papers that make claims based on older AI models, but, in this case, I doubt there has been much change between the now obsolete GPT-4o and GPT-5.4 or whatever, since they both show walls of text.

_You’re currently a free subscriber to One Useful Thing. Subscriptions are optional but help support my work._

[ View in app ](<https://substack.com/app-link/post?publication_id=1180644&post_id=192379643&isFreemail=true&r=6fumam>)
