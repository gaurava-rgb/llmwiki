---
title: "What 638 Practitioner Voices Reveal About Product Manager’s AI Transformation"
author: "David Haberlah"
source_url: "https://medium.com/@haberlah/what-638-practitioner-voices-reveal-about-pms-ai-transformation-7d2fd16be10d"
site: "Medium"
tags: []
published: "2026-03-18"
saved_at: "2026-04-08"
reading_time: "15 mins"
summary: "AI is changing how product managers work, adding new skills like prompt engineering and AI evaluation. Experts say great product managers still need strong people skills and high standards. Overall, AI reshapes product management but keeps its core values intact."
image: "sources/images/01knqfa01p5t1khb4jt6bb44t1_cover.png"
---

## Lessons from 7 years of Lenny’s Newsletter & Podcast

In December 2024, I published a theoretical analysis mapping AI’s expected impact on every product management task using the ISPMA Software Product Management Reference Architecture ([Haberlah, 2024](<https://medium.com/@haberlah/the-future-of-product-management-in-an-age-of-artificial-general-intelligence-agi-4a19ceb54451>)). The prediction: operational work would automate; strategic judgement, stakeholder influence, and user empathy would appreciate in value.

15 months later, the evidence is in. This article draws on 349 newsletters and 289 podcast transcripts from [_Lenny’s Newsletter_](<https://www.lennysnewsletter.com/>) and [_Lenny’s Podcast_](<https://www.lennysnewsletter.com/podcast>) published this week on Github from <https://www.lennysdata.com/>, spanning June 2019 to March 2026. AI-related content rose from 4% of output in early 2023 to 67% by the first quarter of 2026. Conversations that once centred on growth loops and A/B testing now orbit evaluations, agentic architectures, and non-deterministic systems. What follows is an empirical examination of those shifts, drawn from the voices of practitioners living through the transformation.

### **Methodology**

This research was conducted using Anthropic’s Claude Opus 4.6 1M context model, orchestrated as a multi-agent team within Claude Code. I directed 5 specialised AI agents covering traditional PM analysis, AI-native practice, forward-looking synthesis, copy editing, and reference verification.

The full _Lenny’s Newsletter_ repository was cloned from GitHub and systematically analysed. All 638 pieces were evaluated for relevance: 96 rated high, 165 medium, and 377 low. The 25 most relevant received close reading. Statistical analysis of metadata produced the data visualisations presented throughout.

**This article is itself an artefact of the human-AI collaboration it describes**. I provided direction, editorial judgement, and domain expertise; AI agents handled systematic analysis, pattern identification, and drafting at a scale that would have taken weeks of manual work.

### **The Evidence Base**

_Lenny’s Newsletter_ occupies a distinctive position in the product management landscape. Founded by Lenny Rachitsky, a former Airbnb product lead, it has grown into a community whose reach and editorial rigour make it an unusually reliable barometer of practitioner sentiment. The 638 pieces published over the last 7 years analysed here, represent the **most comprehensive longitudinal record of how the PM profession talks to itself about its own evolution**.

The clearest finding is the speed of the discourse shift. Figure 1 traces AI content as a proportion of total output over time, resembling a classic adoption curve compressed into roughly thirty months. In the second half of 2022, AI-tagged content accounted for less than 4% of output. By the first quarter of 2026, that figure had reached 67%. From Q2 2024 onward, AI ceased to be a specialist topic and became the dominant lens through which product management is discussed.

Figure 1. AI content as a percentage of Lenny’s Newsletter and Podcast output, Q3 2022 — Q1 2026. Based on analysis of 638 items.

The second figure reveals a complementary pattern in topic composition. As AI and engineering tags surged, traditional mainstays (growth, strategy, general management) declined in relative prominence. Those topics did not become irrelevant, but AI became the centre around which they were increasingly organised. A growth article in 2024 was likely to discuss AI-augmented experimentation; a strategy piece in 2025 almost certainly addressed agentic architectures.

Figure 2. Topic landscape evolution across Lenny’s Newsletter and Podcast, 2020–2026. Colour intensity represents the percentage of content carrying each tag within each half-year period.

The relevance evaluation reinforces the temporal acceleration. Of the 96 pieces rated as highly relevant to this analysis, 10 were published across all of 2022 and 2023 combined, while 14 appeared in the first quarter of 2026 alone. These patterns confirm that the conversation is grounded in operational experience and deepening rather than merely expanding.

## **What Changes: The New Operating Model**

### **Speed Replaces Perfection**

Every creative and planning cycle has compressed. Jenny Wen quantified the shift: “ _A few years ago, 60 to 70% of it was mocking and prototyping, but now I feel the mocking up part of it is 30 to 40%”_ ([Wen as cited in Rachitsky, 2026](<https://podcasts.apple.com/us/podcast/design-rewritten-how-ai-broke-the-process-lennys-podcast/id1848404899?i=1000752316217>)). Strategic horizons have collapsed alongside production timelines: “ _We used to go off and make this two-year, five-year, 10-year vision even. Now it becomes a vision that’s three to six months out, and isn’t necessarily creating this beautiful deck, sometimes just creating a prototype that points people in the right direction_ ”. The shift is from polished artefacts to navigational prototypes. The traditional design process, Wen argued, has become untenable:

> “This design process that designers have been taught, we sort of treat it as gospel. That’s basically dead” ([Wen as cited in Rachitsky, 2026](<https://podcasts.apple.com/us/podcast/design-rewritten-how-ai-broke-the-process-lennys-podcast/id1848404899?i=1000752316217>)).

The evidence extends beyond individual practice. Duolingo went from producing 100 courses in 12 years to 150 courses in 12 months with AI’s help ([Rachitsky & Yang, 2025](<https://www.lennysnewsletter.com/p/25-proven-tactics-to-accelerate-ai-adoption-at-your-company>)). Colin Matthews demonstrated that PMs could convert a PRD into a working interactive prototype in under 10 minutes, a workflow that previously consumed weeks of engineering effort ([Matthews, 2025](<https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product-managers>)). Kevin Weil, OpenAI’s Chief Product Officer, identified the underlying cause: “ _Every two months, computers can do something they’ve never been able to do before and you need to completely think differently about what you’re doing_ ” ([Weil as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=scsW6_2SPC4>)). Speed raises the bar for where rigour is applied, rather than lowering it.

### **Non-Determinism as a Design Constraint**

Conventional software is deterministic: identical inputs yield identical outputs. AI products shatter this assumption. Aishwarya Naresh Reganti, co-creator of the Continuous Calibration / Continuous Development (CC/CD) framework, identified the foundational challenge:

> “Most people tend to ignore the non-determinism. You don’t know how the user might behave with your product, and you also don’t know how the LLM might respond to that” ([Reganti as cited in Rachitsky, 2026](<https://podcasts.apple.com/us/podcast/why-most-ai-products-fail-lessons-from-50-ai-deployments/id1627920305?i=1000744678894>)).

This double indeterminacy means that product managers can no longer design for guaranteed behaviour; they must design for probable behaviour.

Reganti introduced a second concept: the agency-control tradeoff. “ _Every time you hand over decision-making capabilities to agentic systems, you’re kind of relinquishing some amount of control on your end_ ”. The CC/CD framework proposes that agency must be earned incrementally: scoped capability first, calibrated through evaluation, expanded only once the system has demonstrated reliability. Joshua Xu of HeyGen reinforced the point: “ _Demo value isn’t user value. Building a cool AI demo doesn’t mean we have a product that customers love and is useful_ ” ([Xu as cited in Rachitsky & Poyar, 2024](<https://www.lennysnewsletter.com/p/counterintuitive-advice-for-building-ai-products>)). Products built on probabilistic foundations are better understood as probability distributions to be shaped than as blueprints to be executed.

### **From Artefacts to Organisms**

The shift from deterministic to probabilistic systems has a deeper ontological consequence: the nature of the product itself is changing. Asha Sharma, Corporate Vice President of AI Platform at Microsoft, described a world in which

> “ _[products]_ aren’t just like these static artifacts … [but have become] … living organisms that just get better with the more interactions that happen,” _arguing that_ “this is the new IP of every single company” _[…]_ “products that think and live and learn” ([Sharma as cited in Rachitsky, 2025)](<https://www.youtube.com/watch?v=J9UWaltU-7Q>).

This reconceptualisation has immediate implications for business models. Bret Taylor, chairman of the board at OpenAI and co-founder of Sierra, predicted a structural endpoint:

> _“The whole market is going to go towards agents. I think the whole market is going to go towards outcomes-based pricing. It’s just so obviously the correct way to build and sell software” (_[_Taylor as cited in Rachitsky, 2025_](<https://www.youtube.com/watch?v=qImgGtnNbx0>) _)._

Dan Shipper’s company Every provides a living case study: a 15-person team running 5 products generating 7-figure revenue with, as Shipper put it, “ _no one is manually coding anymore_ ” ([Shipper as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=crMrVozp_h8>)). Under this model, PMs cultivate adaptive systems rather than build features: shaping incentives, designing feedback loops, and stewarding data flywheels.

### **The Shifting Planning Horizon**

If products are organisms rather than artefacts, traditional planning methodologies need radical revision. Kevin Weil was blunt: “ _We do quarterly roadmapping. We laid out a year-long strategy. I don’t for a second believe that what we write down in these documents is what we’re going to actually ship three months from now, let alone six or nine_ ” ([Weil as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=scsW6_2SPC4>)). He invoked Eisenhower’s dictum (Plans are useless. Planning is helpful) and described roadmapping reconceived as rolling bets rather than a fixed itinerary.

Albert Cheng, who led growth at Duolingo and Grammarly, extended this logic to organisational culture, arguing that the velocity of change has inverted the relationship between experience and effectiveness:

> “Sometimes experience could be a crutch, especially in this world where the grounds are shifting so fast with AI. A lot of your learned habits actually need to be intentionally discarded” ([Cheng as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=2BKmNmnEj9w>)).

Howie Liu, CEO of Airtable, took the most dramatic structural action of any leader surveyed, restructuring the company’s entire organisation into “fast thinking” and “slow thinking” groups. Liu went further, questioning whether incumbents could survive without reinvention:

> “If you were literally founding a new company from scratch with the same mission, how would you execute on that mission using a fully AI-native approach? If you can’t, then you should find a buyer” ([Liu as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=GT0jtVjRy2E>)).

The planning horizon has become structurally different: iterative, experimental, and designed to accommodate the possibility that the underlying technology undergoes a step change before your current sprint concludes.

## **What Stays the Same: The Enduring PM Core Capabilies**

The enduring core of product management resides in qualities no large language model can easily replicate: conviction, taste, influence, and an unwavering orientation towards outcomes.

### **Conviction and User-Centric Thinking**

Every consequential product decision rests on personal conviction that cannot be delegated to a model. Tomer Cohen, Chief Product Officer at LinkedIn, observed that:

> “in products, in building product, if you’re not genuinely excited about what you want to build, you don’t have conviction about it, it’s going to be very hard for you to make a big impact” ([Cohen as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=R-zCfLQD_84>)).

Conviction shapes every downstream decision from research framing to trade-off resolution. Rachitsky’s survey of nearly 1,000 respondents across more than 600 companies found that execution was highlighted by 75% of organisations and communication by over 60% as the most valued PM hiring attributes, both fundamentally human capabilities that resist automation ([Rachitsky, 2020](<https://www.lennysnewsletter.com/p/a-comprehensive-survey-of-product-management>)). Karina Nguyen, a researcher at OpenAI, identified “creative thinking,” “prioritization, communication, management” and “people skills like empathy, understanding people, collaboration” as the competencies that will appreciate in value as models grow more capable ([Nguyen as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=DeskgjrLxxs>)).

### **Taste, Craft, and First Principles**

If conviction provides the fuel, taste provides the steering. Aparna Chennapragada, CPO at Microsoft, warned that without editorial judgement and taste at the heart of the process, the result is inevitably “ _a Frankenstein product_ ” ([Chennapragad aas cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=HbbfXAWcuUo>)). More prototypes do not automatically produce better products, they merely raise the threshold at which discernment becomes indispensable. Stewart Butterfield, co-founder of Slack, offered a complementary lens through his concept of utility curves, arguing that:

> “you can create a real advantage for yourself, for your product, for your company by leaning into it because most people don’t have good taste and don’t invest” ([Butterfield as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=kLe-zy5r0Mk>)).

Rachitsky’s 14 habits of highly effective product managers similarly emphasised that great PMs “ _hold the bar high for the work they, and their teammates, do_ ” and “ _always have a point of view, but loosely held_ ,” habits rooted in craft rather than analytical processing ([Rachitsky, 2021](<https://www.lennysnewsletter.com/p/14-habits-of-highly-effective-product-managers>)).

### **Influence and Strategic Narrative**

The right insight matters little if a PM cannot marshal organisational support behind it. Jules Walter, a product leader at Google, put it plainly:

> “your ability to influence others can move your career forward or keep you stuck,” _noting that influence requires understanding_ “how each person makes decisions — what they value, who they consult, and what they’re afraid of” ([Walter, 2024](<https://www.lennysnewsletter.com/p/a-pms-guide-to-influence>)).

This is relational work: mapping power structures, reading emotional cues, constructing tailored arguments. Andy Raskin articulated the narrative dimension, describing how compelling product stories frame “ _the shift from the old game to a new game_ ” rather than reciting feature advantages ([Raskin as cited in Rachitsky, 2023](<https://www.youtube.com/watch?v=dkVJnaxDlXE>)). Naomi Gleit, Head of Product at Meta, employed the metaphor of the conductor: “ _as a PM, your job is to make sure everyone’s playing their part correctly, every section in the orchestra is playing their part, but at the same time, they’re playing together, they’re unified in the music that they’re producing_ ” ([Gleit as cited in Rachitsky, 2024](<https://www.youtube.com/watch?v=sTYuKgzZoL8>)).

### **Outcome-Based Thinking**

The final enduring attribute is the orientation towards outcomes rather than outputs, a distinction that AI sharpens. If agents deliver measurable results autonomously, as Taylor predicted, the PM’s value shifts from shipping features to defining the outcomes those features must achieve. Marty Cagan has long advocated this distinction, arguing that:

> “in a real product team, you celebrate when you actually solve the problem, when you accomplish those results. That’s why we say product teams are about outcomes, they’re not about output” ([Cagan as cited in Rachitsky, 2022](<https://www.youtube.com/watch?v=h-KVGHoQ_98>)).

Christian Idiodi grounded this in an almost artisanal ethic: “ _the real essence of this job is that you wake up on behalf of someone else to solve a problem for them, and you have to do it well enough that they give you something back in return_ ” ([Idiodi as cited in Rachitsky, 2023](<https://www.youtube.com/watch?v=SXYc5RoU3Lg>)). That exchange (value delivered in return for trust, revenue, and loyalty) remains the core of product management, whether the tools are spreadsheets or autonomous agents.

## **The New Competency Stack**

The operational shifts documented earlier demand a corresponding evolution in PM skills. The evidence points to **3 specific AI-literate additions to the PM toolkit** :

  1. evaluations
  2. prototyping fluency, and
  3. natural language experience design



### **Evals as the Defining New Skill**

If non-determinism is the central design constraint of AI products, evals (the systematic measurement of how well an AI system performs against defined quality criteria) are the central response. Aman Khan, Director of Product at Arize AI, articulated the stakes:

> “Prompts may make headlines, but evals quietly decide whether your product thrives or dies” _and argues that_ “the ability to write great evals isn’t just important, it’s rapidly becoming the defining skill for AI PMs in 2025 and beyond” ([Khan, 2025](<https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete-guide-to-evals>))

This claim is substantiated by both OpenAI and Anthropic’s product leaders independently identifying evals as the most critical emerging competency.

Hamel Husain and Shreya Shankar, whose evals course has trained teams across every major AI lab, described a methodology grounded in error analysis and open coding: reviewing real user interactions, writing free-form critiques, and categorising failure patterns into a prioritised taxonomy ([Husain & Shankar, 2025](<https://www.lennysnewsletter.com/p/building-eval-systems-that-improve-your-ai-product>)). Husain emphasised the necessity of product involvement: “ _When you’re doing this open coding, a lot of teams get bogged down in having a committee do this. For a lot of situations, that’s wholly unnecessary._ […] _You can appoint one person whose taste that you trust. It should be the person with domain expertise. Oftentimes, it is the product manager_ ” ([Husain & Shankar, 2025](<https://www.lennysnewsletter.com/p/building-eval-systems-that-improve-your-ai-product>)). Mastering evaluations means developing the capacity to define what “good” looks like for a probabilistic system, a competency with no real precedent in the pre-AI toolkit.

### **The PM-Prototyper Hybrid**

The second competency is prototyping fluency. Aparna Chennapragada stated the expectation bluntly: “ _If you’re not prototyping and building to see what you want to build, I think you’re doing it wrong_ ” ([Chennapragada as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=HbbfXAWcuUo>)). Howie Liu reinforced this:

> “There’s a strong advantage to any of those three roles who can kind of cross over into the other two. As a PM, you need to start looking more like a hybrid PM prototyper, who has some good design sensibilities” ([Liu as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=GT0jtVjRy2E>)).

Lazar Jovanovic, the first professional vibe coder at Lovable, represents the extreme end of this spectrum: a non-technical builder shipping production software entirely through AI tools. As Jovanovic explained, “ _I’m optimizing 100% of my time today on good judgment, clarity, quality, taste_ ” rather than on coding itself ([Jovanovic as cited in Rachitsky, 2026](<https://www.youtube.com/watch?v=0XNkUdzxiZI>)). PMs need not become engineers, but moving from concept to interactive prototype in minutes rather than weeks is becoming a baseline expectation.

### **NLX and Prompt Craft**

The third competency concerns designing natural language experiences, which Aparna Chennapragada framed as a new design discipline: “ _Natural language interface. NLX is the new UX_ ”. Chennapragada argued that conversations, like graphical interfaces, have “grammars” and “structures” and “UI elements” that are “invisible” but must be deliberately designed ([Chennapragada as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=HbbfXAWcuUo>)). Design is not eliminated; it is transformed into a domain requiring understanding of both human conversation and model behaviour.

Mike Taylor demonstrated that effective prompting is a structured skill with validated techniques including role-playing, few-shot learning, and chain-of-thought reasoning ([Taylor, 2024](<https://www.lennysnewsletter.com/p/five-proven-prompt-engineering-techniques-and-a-few-more-advanced-tactics>)). Tal Raviv extended this by arguing that the real gains emerge from sustained, context-rich partnerships: “ _When LLMs have this valuable and ongoing context about our goals, our role, our projects, our team, and our wider org, they become our ‘AI copilot’ — a real thinking partner for long-term, complex work_ ” ([Raviv, 2025](<https://www.lennysnewsletter.com/p/build-your-personal-ai-copilot>)). The PM of the near future will need fluency in a new triad: evaluating probabilistic systems, prototyping with AI-assisted tools, and designing the natural language experiences through which humans and AI agents collaborate. These are additions to the existing competency stack, and they may define the competitive boundary between PMs who thrive in the era of powerful AI and those who do not.

Figure 3. Tag co-occurrence differential: AI-tagged content vs. non-AI content (in percentage points). Positive values indicate enrichment in AI content.

## **Synthesis: The PM Compass**

In my earlier ISPMA overlay ([Haberlah, 2024](<https://medium.com/@haberlah/the-future-of-product-management-in-an-age-of-artificial-general-intelligence-agi-4a19ceb54451>)), I mapped which tasks would be reshaped by advancing AI and to what degree. That analysis answered the question of _what will change_. The PM Compass framework, presented in Figure 4, addresses _where practitioners should invest_ as those shifts take hold.

The PM Compass organises the landscape along two axes. The horizontal axis distinguishes what endures from what changes; the vertical axis separates mindset from skills. Together, these yield four quadrants.

**Timeless Principles** (top-left): captures the enduring mindset commitments (user empathy first, outcome over output, strong opinions loosely held) that guests repeatedly foregrounded as non-negotiable regardless of tooling paradigm.

**New Mental Models** (top-right): houses the cognitive reorientations the evidence demands: treating AI as a team member rather than a tool, adopting probabilistic thinking, and conducting continuous capability audits. Weil’s observation that the frontier shifts every 2 months renders static mental models inadequate.

**Foundational Craft** (bottom-left): preserves the enduring skill base (prioritisation frameworks, stakeholder communication, problem definition) that remains essential even when execution velocity accelerates dramatically.

**Emerging Capabilities** (bottom-right): catalogues the new competencies surfaced most consistently: prompt and context engineering, AI evaluation and benchmarking, and technical prototyping.

Figure 4. The PM Compass: a framework for navigating what endures and what changes in AI-era product management.

**The framework’s utility is diagnostic. Practitioners can locate their strengths across the four quadrants and identify where deliberate investment is needed**. No single quadrant is sufficient. Liu’s characterisation of the modern PM as “ _a hybrid PM prototyper, who has some good design sensibilities_ ” ([Liu as cited in Rachitsky, 2025](<https://www.youtube.com/watch?v=GT0jtVjRy2E>)) suggests that quadrant boundaries are intentionally porous, and the most effective practitioners will cultivate capability across all four.

## **Conclusion**

Across 638 practitioner voices, the pattern is consistent: AI is reshaping the operating model of product management while reinforcing its enduring core. Planning cycles have compressed. Non-determinism has become a first-order design constraint. Entirely new competencies have emerged. Yet conviction, taste, influence, and outcome orientation are growing more valuable, not less, as AI handles an expanding share of operational execution. The speed of transformation has exceeded even the forecasts I offered fifteen months ago ([Haberlah, 2024](<https://medium.com/@haberlah/the-future-of-product-management-in-an-age-of-artificial-general-intelligence-agi-4a19ceb54451>)).

The PM practitioners who will thrive are those who cultivate capability across all four quadrants of the PM Compass: enduring principles, new mental models, foundational craft, and emerging capabilities. The profession is being rewritten. We are the authors.

— -

## **References**

Haberlah, D. (2024, December 7). Product management in the age of artificial general intelligence (AGI). _Medium_. <https://medium.com/@haberlah/the-future-of-product-management-in-an-age-of-artificial-general-intelligence-agi-4a19ceb54451>

Husain, H., & Shankar, S. (2025, September 9). Building eval systems that improve your AI product. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/building-eval-systems-that-improve-your-ai-product>

Khan, A. (2025, April 8). Beyond vibe checks: A PM’s complete guide to evals. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete-guide-to-evals>

Matthews, C. (2025, January 7). A guide to AI prototyping for product managers. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product-managers>

Rachitsky, L. (2020, December 22). A comprehensive survey of product management. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/a-comprehensive-survey-of-product-management>

Rachitsky, L. (2021, May 4). 14 habits of highly effective product managers. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/14-habits-of-highly-effective-product-managers>

Rachitsky, L. (Host). (2022, August 21). The nature of product (Marty Cagan) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=h-KVGHoQ_98>

Rachitsky, L. (Host). (2023, May 28). The power of strategic narrative (Andy Raskin) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=dkVJnaxDlXE>

Rachitsky, L. (Host). (2023, December 21). The essence of product management (Christian Idiodi) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=SXYc5RoU3Lg>

Rachitsky, L. (Host). (2024, October 27). Meta’s Head of Product on working with Mark Zuckerberg, early growth tactics, why PMs are like conductors, and more (Naomi Gleit) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=sTYuKgzZoL8>

Rachitsky, L. (Host). (2025, February 9). OpenAI researcher on why soft skills are the future of work (Karina Nguyen) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=DeskgjrLxxs>

Rachitsky, L. (Host). (2025, April 10). OpenAI’s CPO on how AI changes must-have skills, moats, coding, startup playbooks, more (Kevin Weil) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=scsW6_2SPC4>

Rachitsky, L. (Host). (2025, May 18). Microsoft CPO: If you aren’t prototyping with AI, you’re doing it wrong (Aparna Chennapragada) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=HbbfXAWcuUo>

Rachitsky, L. (Host). (2025, July 17). The AI-native startup: 5 products, 7-figure revenue, 100% AI-written code (Dan Shipper) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=crMrVozp_h8>

Rachitsky, L. (Host). (2025, July 31). He saved OpenAI, invented the “Like” button, and built Google Maps (Bret Taylor) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=qImgGtnNbx0>

Rachitsky, L. (Host). (2025, August 28). How 80,000 companies build with AI: Products as organisms, the death of org charts, and why agents will outnumber employees by 2026 (Asha Sharma) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=J9UWaltU-7Q>

Rachitsky, L. (Host). (2025, August 31). How we restructured Airtable’s entire org for AI (Howie Liu) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=GT0jtVjRy2E>

Rachitsky, L. (Host). (2025, September 25). Why AI evals are the hottest new skill for product builders (Hamel Husain & Shreya Shankar) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=BsWxPI9UM4c>

Rachitsky, L. (Host). (2025, October 5). How to find hidden growth opportunities in your product (Albert Cheng) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=2BKmNmnEj9w>

Rachitsky, L. (Host). (2025, November 20). Slack founder: Mental models for building products people love ft. Stewart Butterfield (Stewart Butterfield) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=kLe-zy5r0Mk>

Rachitsky, L. (Host). (2025, December 4). Why LinkedIn is turning PMs into AI-powered “full stack builders” (Tomer Cohen) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=R-zCfLQD_84>

Rachitsky, L. (Host). (2026, January 11). Aishwarya Naresh Reganti + Kiriti Badam [Audio podcast episode]. In _Lenny’s Podcast_. <https://podcasts.apple.com/us/podcast/why-most-ai-products-fail-lessons-from-50-ai-deployments/id1627920305?i=1000744678894>

Rachitsky, L. (Host). (2026, February 8). The rise of the professional vibe coder (Lazar Jovanovic) [Audio podcast episode]. In _Lenny’s Podcast_. <https://www.youtube.com/watch?v=0XNkUdzxiZI>

Rachitsky, L. (Host). (2026, March 1). Jenny Wen [Audio podcast episode]. In _Lenny’s Podcast_. <https://podcasts.apple.com/us/podcast/design-rewritten-how-ai-broke-the-process-lennys-podcast/id1848404899?i=1000752316217>

Rachitsky, L., & Poyar, K. (2024, July 2). Counterintuitive advice for building AI products. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/counterintuitive-advice-for-building-ai-products>

Rachitsky, L., & Yang, P. (2025, August 5). 25 proven tactics to accelerate AI adoption at your company. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/25-proven-tactics-to-accelerate-ai-adoption-at-your-company>

Raviv, T. (2025, July 22). Build your personal AI copilot. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/build-your-personal-ai-copilot>

Reganti, A. N., & Badam, K. (2025, August 19). Why your AI product needs a different development lifecycle. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different-development-lifecycle>

Taylor, M. (2024, October 29). Five proven prompt engineering techniques (and a few more-advanced tactics). _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/five-proven-prompt-engineering-techniques-and-a-few-more-advanced-tactics>

Walter, J. (2024, October 1). A PM’s guide to influence. _Lenny’s Newsletter_. <https://www.lennysnewsletter.com/p/a-pms-guide-to-influence>
