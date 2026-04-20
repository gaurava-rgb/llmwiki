---
title: "Anthropic cuts AI productivity forecasts in half after analyzing Claude's real-world failure rates"
reader_id: "01kfdsfzvceazcja7kv1c7z74b"
notion_page_id: "3464ebe7-f118-810d-b525-e542565ff98e"
reader_url: "https://read.readwise.io/read/01kfdsfzvceazcja7kv1c7z74b"
source_url: "https://share.google/D3db9i8CXmER3fqbd"
author: "Maximilian Schreiner"
site: "Forbes.com"
tags: []
published: "2026-01-15"
saved_at: "2026-01-20"
reading_time: "4 mins"
summary: "Anthropic found that Claude AI struggles more with complex tasks, cutting their productivity forecasts in half. They also noticed AI use may lower skill levels in some jobs while boosting collaboration between users and AI. Usage is growing fast in the US but still varies widely worldwide based on wealth and education."
content_hash: "82c1c524e96d0d37533cb452af1b3b579a9f0c8bd05c3ba183a40900f91cde2e"
---

![Image description](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMzc2IiBoZWlnaHQ9Ijc2OCIgdmlld0JveD0iMCAwIDEzNzYgNzY4Ij48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBzdHlsZT0iZmlsbDojZjJmMmYyO2ZpbGwtb3BhY2l0eTogMC4xOyIvPjwvc3ZnPg==)Image description

**Anthropic's first systematic analysis of Claude's task failure rates reveals a clear pattern: the more complex the work, the lower the success rate. The company has cut its productivity forecasts roughly in half.**

Anthropic has released its fourth "Economic Index Report," marking the first systematic look at how often Claude actually succeeds at different tasks. The analysis draws from one million Claude.ai conversations and one million API transcripts from November 2025, just before the release of Opus 4.5.

At the heart of the report are five new "economic primitives" - basic metrics that Anthropic generates by having Claude analyze anonymized transcripts. These capture task complexity (how long a human would need without AI), the education level required for inputs and outputs, use case (work, study, or personal), the AI's level of autonomy, and task success.

## Complex tasks mean bigger gains but more failures

The data reveals a clear tradeoff: complex tasks offer greater time savings, but Claude fails at them more often. According to the report, Claude achieves roughly 60 percent success on API requests for tasks under one hour, dropping to about 45 percent for tasks over five hours. The 50 percent threshold sits at an estimated 3.5 hours of work.

Claude.ai tells a different story: success rates decline much more slowly as tasks get longer. Anthropic estimates Claude.ai wouldn't drop below 50 percent until around 19 hours. The researchers attribute this gap to the multi-turn nature of conversations, where users can course-correct and iterate.

## Productivity estimates fall by half

The new success rate data forced Anthropic to revise its earlier projections. In a previous analysis, the company estimated that broad AI adoption could boost annual US labor productivity growth by 1.8 percentage points. Adjusted for success rates, that estimate falls to roughly 1.0 to 1.2 percentage points.

Factor in bottleneck effects - tasks essential to a job that AI can't speed up - and the estimated impact drops further to 0.6 to 0.8 percentage points. Still, Anthropic points out that even one percentage point annually over ten years would bring US productivity growth back to late 1990s and early 2000s levels. The company also expects future models to achieve higher success rates.

## AI adoption could "deskill" certain jobs

One key finding concerns the impact on job profiles. According to the data, Claude tends to be used for tasks requiring higher education - an average of 14.4 years (equivalent to an associate's degree), compared to 13.2 years for all tasks across the US economy.

When AI takes over these tasks, humans are left with less skilled work - a net "deskilling" effect. Anthropic offers concrete examples: travel agents would lose planning tasks to AI and mainly handle ticketing and payment processing. Property managers, on the other hand, would experience "upskilling" as accounting tasks disappear, leaving contract negotiations and stakeholder management.

## Better prompts lead to better answers

The analysis also reveals a tight link between the education level of user inputs and the quality of Claude's responses. Anthropic measures both sides: how many years of formal education are needed to understand a user prompt, and how many years are needed to understand Claude's response. The correlation coefficient between these values exceeds 0.92 - both at the country level and across US states.

In practical terms, users who craft complex, technically precise requests get correspondingly sophisticated answers. Those who ask simple questions get simple answers. Claude dynamically adjusts its response level to match the input level. According to Anthropic, this has far-reaching implications: countries with higher education levels could benefit more from AI regardless of raw adoption rates, simply because their populations can better tap into the models' potential through skilled prompting.

## Users shift back to collaboration over delegation

Since the last report in August 2025, usage patterns on Claude.ai have shifted. Anthropic distinguishes between two basic usage types: "augmentation," where users work collaboratively with Claude (iterating on tasks together, getting concepts explained, or seeking feedback) and "automation," where users fully delegate a task to Claude, which completes it with minimal back-and-forth.

In August 2025, automated usage had overtaken augmented usage for the first time, a sign that users were increasingly willing to hand tasks off entirely to Claude. That trend has now reversed: augmented usage climbed to 52 percent while automated usage fell to 45 percent. The share of "directive" conversations where users give Claude a task and it completes without follow-up questions dropped from 39 to 32 percent.

Anthropic suspects that product updates like file creation, persistent memory, and customizable "skills" have driven more collaborative interactions. These features enable more complex workflows that keep users more involved. This distinction only loosely relates to agentic usage, where AI systems independently execute multi-step tasks: agents would fall more into the automation category but aren't separately tracked in the analyzed data.

Usage remains highly concentrated: the ten most common tasks account for 24 percent of all Claude.ai conversations. Code and math tasks continue to dominate at 34 percent on Claude.ai and 46 percent for API usage.

## Fast convergence in the US, global inequality persists

Within the US, early signs of rapid regional convergence are emerging: states with lower usage are catching up relatively faster. Anthropic estimates per capita usage could equalize within two to five years, roughly ten times faster than the diffusion of economically significant technologies in the 20th century.

Globally, however, there's no convergence. The US, India, Japan, the UK, and South Korea lead in Claude.ai usage, and inequality still correlates strongly with GDP per capita - a one percent increase correlates with 0.7 percent more Claude usage. In lower-income countries, coursework and education use cases are relatively more common, while Claude is predominantly used for work overall.

Anthropic is publishing the [data on Hugging Face](<https://huggingface.co/datasets/Anthropic/EconomicIndex>) to enable external researchers to study AI's economic impact. The [full report is available here](<https://www.anthropic.com/research/anthropic-economic-index-january-2026-report>).

### AI News Without the Hype – Curated by Humans


As a **THE DECODER subscriber** , you get ad-free reading, our **weekly AI newsletter** , the exclusive **"AI Radar" Frontier Report 6× per year** , access to comments, and our **complete archive.**

[ Subscribe now ](<https://the-decoder.com/subscription/>)
