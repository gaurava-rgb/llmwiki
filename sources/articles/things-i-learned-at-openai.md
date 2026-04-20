---
title: "Things I learned at OpenAI"
reader_id: "01kpgqyj3f6ewb4a522k1tb42x"
notion_page_id: "3464ebe7-f118-8111-96c9-e6d60c63bf0b"
reader_url: "https://read.readwise.io/read/01kpgqyj3f6ewb4a522k1tb42x"
source_url: "https://semaphore.substack.com/p/things-i-learned-at-openai?r=38jwv"
author: "Karina Nguyen"
site: "substack.com"
tags: []
published: "2026-03-28"
saved_at: "2026-04-18"
reading_time: "5 mins"
summary: "Karina Nguyen shares lessons from her time at OpenAI about building better AI through thoughtful evaluation, creative post-training, and smart research. She believes the future of AI depends on teaching models empathy, humor, and judgment, which is still a new challenge. She emphasizes the importance of alignment, adaptability, and working on bold ideas that truly matter for people and society."
content_hash: "ad5505e0ed9ec28f218b3a68174d8d8299636fc8cfdfb9455e719597593f942b"
---

### With deep gratitude to the collaborators, mentors, and friends who shaped how I think about the world.

[![](https://substackcdn.com/image/fetch/$s_!_ZLj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24b565dd-a8b7-4cad-9901-02ed12809933_4032x3024.heic)](<https://substackcdn.com/image/fetch/$s_!_ZLj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24b565dd-a8b7-4cad-9901-02ed12809933_4032x3024.heic>)My first day at Anthropic started in this NYC apartment in 2022

When I wrote a similar post about [Anthropic](<https://semaphore.substack.com/p/things-i-learned-at-anthropic>) around two years ago, Claude Code didn’t exist and AI’s coding skills were far more limited. The world was about to experience models that could finally think deeply to solve hard things that were previously out of reach.

I joined OpenAI precisely because I wanted to contribute to the [paradigm shift](<https://openai.com/index/learning-to-reason-with-llms/>) as it happened. Much has changed, but I've always dreamed of building optimistic visions of the future with AI (_[new terminal Mesh](<https://autumn-detective-45e.notion.site/Mesh-Reimagining-a-more-Humane-Command-Line-42140fd0338f47b19b9d365ecf7cce56>), [visual AI recsys InterAlia](<https://x.com/karinanguyen/status/1587217615885406213>)_). What’s different now is timing. If AGI arrives in 2-5 years, and I believe it will, the returns to high agency are unprecedented.

There has never been a better moment to build new things and work on the hardest and most ambitious challenges of our time. The economics of value creation are being repriced because the best builders can do more than was previously possible _(due to tools like Claude Code)_ , and capture more of the upside _(leverage compounds)_. The spread between average outcomes and exceptional ones is widening, and the upside is increasingly asymmetric.

### **Lessons**

**Evals & benchmarks**

  * Good evaluations are surprisingly hard to design. The best ones are simple enough to become ubiquitous but specific enough to actually measure meaningful things. Clear outputs, fast feedback, obvious signals. Most evals fail on one of these. The friction of setting up infrastructure, interpreting results, or debugging failures determines whether researchers actually use it in their iteration loops. (We wrote more about this in [SimpleQA](<https://arxiv.org/pdf/2411.04368>) paper)

  * A great benchmark becomes a Schelling point. Once it exists, the entire field orients around it because everyone wants to claim they beat it. You move the field by incentivizing everyone to optimize against them. This is why creating the right eval is sometimes more impactful than creating the model that scores well on it.

    * E.g. we recently released [PostTrainBench](<https://posttrainbench.thoughtfullab.com/>) because of this




**Post-training & product **

  * Designing post-training data mixtures is closer to art than engineering. The same is true for inventing methods that teach models new capabilities. Human taste and creativity matter enormously here.

  * Alignment failures are sometimes failures of abstraction, not intent. Many bad behaviors arise because the model can’t correctly abstract a principle across contexts.

  * I’ve come to believe that post-training is where the next frontier of AI progress happens, especially for subjective / hard-to-measure capabilities like emotional intelligence, taste, humor, creative judgment. Base models are increasingly capable. The question is whether we know how to unlock what’s already in them and how to invent entirely new behaviors to teach them. Objective capabilities have clear benchmarks. Subjective ones require a different craft: intuition about data, feel for what’s working, methods we’re still inventing. This is the frontier that matters, and almost nobody is working on it yet.

  * I’ve started to look at products from the perspective of training signals. [ChatGPT canvas](<https://openai.com/index/introducing-canvas/>), for example, wasn’t just a writing interface. It was a mechanism for collecting user signals on how people want to collaborate with models. The product shapes the data, the data shapes the model, the model shapes what the product can become.




**Act of AI research**

  * Internal tooling is an underrated competitive advantage. The lab with the best eval and training UX iterates faster and catches problems earlier. That compounds.

  * The skill is designing experiments that give you maximum information per FLOP because not all experiments are worth the compute they burn. Knowing when a small ablation tells you everything you need, versus when you genuinely need to run at scale. There’s also a meta-skill here: recognizing when the field’s conventional wisdom about what requires scale is actually wrong, and you can learn what you need at a fraction of the cost.

  * A result nobody understands doesn’t spread. Distill to one clear claim, one good visual, one memorable number.

  * The gap between “trying random things” and “systematically narrowing hypotheses” separates okay researchers from effective ones. Debugging intuition is learnable and comes with running hundreds of experiments.

  * The most durable skill in AI research isn’t any particular technical contribution, but the ability to repeatedly identify what matters now and execute quickly. Choosing the right problems to work on is as important as executing them with care.

  * Audacious ideas get higher buy-in. Talented people have options; they won’t spend them on incrementalism. If you’re asking for someone’s time, you owe them a mission worth the risk.

  * Some discoveries are downstream of infrastructure—you can’t have certain ideas until you have the systems that make them possible to test. The tooling comes first, then the insight. That’s why often researchers spend time on engineering problems.

  * That’s said, some findings are infrastructure-dependent, not infrastructure-agnostic. They emerge from a particular stack and setup. Different systems might have surfaced entirely different discoveries.

  * Sometimes starting from scratch is more effective than incremental fix. For example, retrofitting personality onto an existing model means fighting patterns optimized for something else.

  * Model personality is a reflection of the people who trained it. This is more literal than most realize.




**Environment**

  * Human politics/misalignment might be one of the core bottlenecks to making more progress on AGI

  * In fast-moving environments, things change constantly: people will leave, projects shift, priorities get reshuffled. It’s natural to feel destabilized by this and I certainly was. Care deeply about the work and the people, but try not to anchor your sense of stability to any particular configuration, be adaptable. The person you’re collaborating with today might be somewhere else next month. That’s not a reason to care less, but a reason to be present while it lasts.




**Alignment, societal impacts**

  * One of the more significant updates to my thinking is that greater capability correlates with better alignment. More capable models can be less inclined to deceive because they understand better that deception erodes trust and can reason about long-term consequences. Values like “be helpful” or “be honest” are abstract; applying them correctly across contexts requires sophisticated reasoning.

  * Risks become real only once they’re legible, but waiting for incidents is almost too late. We built [sycophancy evals](<https://arxiv.org/pdf/2212.09251>) at Anthropic years before [real-world incidents of ChatGPT](<https://openai.com/index/sycophancy-in-gpt-4o/>) made the risk legible to everyone else.

  * Alignment is a cultural problem. The societal harms of AGI like [psychological dependency,](<https://en.wikipedia.org/wiki/Chatbot_psychosis>) [disempowerment](<https://www.nytimes.com/2025/12/28/opinion/artificial-intelligence-jobs.html>), [erosion of agency](<https://www.theguardian.com/technology/2025/may/31/the-workers-who-lost-their-jobs-to-ai-chatgpt>) are closer than most people realize. That’s deeply concerning. What’s particularly unfortunate is seeing parts of the entertainment industry resist this moment. Few people have more power to shape how humanity imagines the future. Instead of pushing back, they could be telling the stories that help billions of people understand what’s coming and how to navigate it with agency and care.




I spent the first half of my twenties working on Claude and ChatGPT. Billions of people now wake up to systems that carry a tiny piece of my love in them. After that, there is no other way to live.

I'm 25 now, and I know that I want to give my life to the types of hard problems no one has tackled yet. Teaching intelligence empathy, storytelling, creative judgment, modelcrafting and aligning AI systems to what actually matters to us, humans. Imagining products for humans and AI to interact in novel ways. That’s the work worth doing.

If any of this excites you, I’d love to talk (my email is karina@thoughtfullab.com or shoot me a [DM](<https://x.com/karinanguyen_>), [our website](<https://www.thoughtfullab.com/>)). The best work I've ever done happened alongside people who cared deeply about getting it right.

### Ready for more?

Subscribe
