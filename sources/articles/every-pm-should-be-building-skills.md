---
title: "Every PM Should Be Building Skills"
reader_id: "01kk0w30g67610bkmf5vkzgbff"
notion_page_id: "3464ebe7-f118-81f7-b4e9-eeef742e292c"
reader_url: "https://read.readwise.io/read/01kk0w30g67610bkmf5vkzgbff"
source_url: "https://amankhan1.substack.com/p/every-pm-should-be-building-skills?r=38jwv"
author: "Aman Khan"
site: "substack.com"
tags: []
published: "2026-03-05"
saved_at: "2026-03-06"
reading_time: "11 mins"
summary: "Skills are simple markdown files that teach AI assistants how to help you with tasks by following your personal workflow. They save time by automatically applying your preferences without repeating instructions. Building your own skills helps you work smarter and share useful methods with others."
content_hash: "ef34e9b598891a32ca23f369ace7d9dd3798980baea96cf1281d2651faf62f9e"
---

### What skills are, why you should be using them, and how to get started - all in one simple prompt

_Quick Note: Eric Xiao and I are excited to launch a second cohort of our coding agent course called[ Claude Code for PMs. ](<https://maven.com/aman-khan/claude-code-for-product-managers?promoCode=aman250>)We have a **[free](<https://maven.com/p/9762b4/open-claw-for-product-managers>)**[ lightning lesson on OpenClaw next week](<https://maven.com/p/9762b4/open-claw-for-product-managers>) \- feel free to join! We’d love to see you there _

_Now on to the post!_

**TL;DR:**

  * **Start here:** copy paste this into Claude Code/Cursor/Your favorite coding agent:

    * `“Go to https://aman.md/ (url) and set me up”`

  * **Get my full setup here:**[amans-skills](<https://github.com/amanaiproduct/amans-skills>)


[![](https://substackcdn.com/image/fetch/$s_!bMal!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac487c14-59a4-4940-abf6-74c0b4e31753_1600x916.png)](<https://substackcdn.com/image/fetch/$s_!bMal!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac487c14-59a4-4940-abf6-74c0b4e31753_1600x916.png>)

I’ve spent the last few months using [Claude Code’s skill](<https://code.claude.com/docs/en/skills>) and plugin system. At first I thought it was just another way to add prompts - they seem like just instructions in a markdown file. How valuable could this be? As I’ve been using skills more, I’ve realized that skills and plugins are how you turn a coding assistant into something that actually knows your codebase, your workflow, and your preferences. And an underappreciated benefit of this simplicity is that skills are a peek into your mind as a builder, which creates a unique distribution approach.

You’ve probably seen more companies starting to add skills to use their products. As a product builder or specialist in some way, one of the highest leverage things you could do right now is find ways to encode your knowledge into an agent for it to be used to take action. Skills are the perfect method of doing this.

If you just want to get started with my setup (and have skills loaded next time you use claude code), I’ve packaged my plugins, skills, and config into a guided installer you can paste into any Claude Code session:

> `“Go to aman.md (url) and set me up.”`

That walks you through installing 6 plugins and 2 custom skills interactively - you pick which ones you want as it goes. The full repo is at [amans-skills](<https://github.com/amanaiproduct/amans-skills>) if you want to look before you install. I’ll continue to add skills here as I find use with them and think they’re worth sharing.

Something I didn’t expect: **skills are a peek into your mind as a builder.** A well-written skill encodes how you think about a problem, what conventions you follow, what mistakes you’ve learned to avoid. My writing voice skill is 200+ lines of patterns, anti-patterns, and calibration sentences that encode years of figuring out what works. When I share that skill, I’m sharing my judgment, not just a prompt. More companies are starting think this way, by shipping skills alongside their products, and if you have domain expertise, encoding it into a skill that agents can act on is one of the most useful things you can do right now.

The documentation for all of this exists, but practical guidance is scattered. In this post, I’m going to cover: what are skills, where to find good ones, how to make Claude invoke them reliably, and what my actual daily setup looks like.

If you want to understand what you just installed and why any of this matters, keep reading.

## **What’s a Skill? What’s a Plugin? What’s a CLI?**

I went back and forth on these distinctions for a while, so let me save you the confusion.

**A skill is a markdown file that teaches Claude how to do something.** You create a SKILL.md file with instructions, drop it in .claude/skills/my-skill/, and Claude adds it to its toolkit. Skills follow the [Agent Skills](<https://agentskills.io/>) open standard, which means they work across multiple AI coding tools, not just Claude Code. When you type /my-skill, Claude loads those instructions and follows them. That’s it.

Here’s the part that makes skills more interesting than plain prompts: Claude reads the description field in your skill’s frontmatter and decides when to apply it **automatically** , without you invoking it. If you write a skill with:
description: “Use when reviewing code for quality issues”
Claude will load that skill whenever you ask it to review code, even if you never type the slash command. The description is always in context, but the full skill body only loads on demand. This keeps your context window clean.

**A plugin is a package that bundles skills, agents, hooks, and MCP servers together.** Plugins are distributed through marketplaces (Git repos or npm packages) and installed with /plugin install. All components get a namespace prefix like /compound-engineering:workflows:plan. A skill teaches Claude one thing; a plugin teaches Claude many things and wires up the infrastructure to support them.

There’s another layer worth naming: **the CLI or agent harness itself.** Claude Code, Cursor, Windsurf, Cline, aider, or a custom wrapper built on the Agent SDK. The harness is the execution environment that loads your skills, connects to MCP servers, manages context, and decides how tool calls actually run. Skills and plugins are portable across harnesses (that’s the point of the Agent Skills standard), but the harness determines what’s possible at runtime: how many sub-agents you can spawn, whether hooks exist, how context compression works, what permission model governs tool use. When people ask “should I use Claude Code or Cursor?”, they’re really asking which harness fits their workflow. (I’ll be sharing more on this layer in a future post)

## **Why Skills Matters If You’re a PM**

Most of the conversation around Claude Code assumes you’re an engineer writing application code. I’m a product person, and I use Claude Code every day. Each of the skills I use encodes my preferences and ways of working. Without skills, I was re-explaining these preferences every session.

I went from spending the first five minutes of every session re-establishing context to just having Claude load my voice profile, anti-slop rules, and format-specific structure automatically.

If you’re a PM who uses coding agents for more than just code (writing, prototyping, diagramming, analysis), skills are how you stop repeating yourself and start compounding what you’ve learned about how you work best. Skills also matter from a distribution perspective, which I cover more below.

## **CLAUDE.md vs Skills: What Goes Where**

CLAUDE.md and skills are both markdown files that tell Claude how to behave, but they load at different times, and that difference matters more than I expected.

**CLAUDE.md is always on.** Claude reads your CLAUDE.md files (global ~/.claude/CLAUDE.md and project-level in your repo root) at the start of every conversation and keeps them in context the entire time. These are rules that apply to everything: coding conventions, commit message formats, communication preferences, things Claude should never do. My project CLAUDE.md has anti-slop writing rules because I want those enforced whether I’m drafting an email, reviewing a PR, or writing a Substack post.

**Skills load on demand.** Only the short description field sits in context between invocations. The full skill body loads when you type the slash command or when Claude decides it’s relevant based on matching the description to your message. My Excalidraw skill is 300 lines of diagram layout rules, quality gates, and arrow routing instructions. Those 300 lines only enter context when I’m actually making a diagram.

The practical rule: if it should apply to every interaction, put it in CLAUDE.md. If it only applies to a specific task, make it a skill. “Never use em dashes in my writing” goes in CLAUDE.md. “How to create architecture diagrams on an Excalidraw canvas” is a skill.

### **What actually happens when a skill fires**

Understanding this lifecycle changed how I structured my skills:

  1. **Session starts.** Claude loads your CLAUDE.md files and reads every installed skill’s description field. The descriptions collectively eat about 2% of your context window. The full skill bodies are not loaded yet.

  2. **You send a message.** Either /my-skill explicitly, or something natural like “review this code for quality issues.”

  3. **Claude decides what to load.** Explicit slash command loads that skill directly. Natural language gets matched against all skill descriptions, and Claude picks the relevant ones and loads their full bodies. This is why the description field is the most important line in any skill file.

  4. **References load progressively.** If the skill body says “read references/voice-dna.md”, Claude reads that file with the Read tool. This gives you three tiers of loading: description (always in context), skill body (loaded on invocation), and reference files (loaded when the skill needs them).

  5. **Claude executes.** Follows the instructions: calls tools, asks clarifying questions, launches sub-agents, generates output.




This is why I moved my writing voice rules out of CLAUDE.md. The full voice profile is 200+ lines. In CLAUDE.md, that burns 200 lines of context on every turn, including turns where I’m debugging a Python script and don’t need voice rules at all. As a skill with progressive loading, it costs 30 words normally and the full 200+ lines only when I’m actually writing.

## **What I Actually Run Day to Day**

Here’s what’s in my setup and why each piece earns its place:

**[Compound Engineering](<https://github.com/EveryInc/compound-engineering-plugin>)** (/workflows:plan, /workflows:work, /workflows:review, /workflows:compound) changed how I approach complex features. Before this plugin, I would just start prompting Claude and hope for the best. This workflow spins up parallel research agents to understand the codebase before generating an implementation plan. The review workflow launches 15 specialized agents (security, performance, architecture, pattern consistency, and more) that each analyze your code from a different angle. After I finish a feature, /workflows:compound documents what I learned so the next session starts smarter.

The compound loop is the real value: each unit of work makes the next one easier, and it feels like your agent is actually learning

**Plugin Dashboard** (my plugin) renders a compact summary after every Claude Code response showing exactly which tools and plugins were used on that turn. Something like `MCP:manager-ai` · `File:Read,Grep` · `Agent:Explore`. This is how I discovered that Claude was doing twelve file reads on turns where it should have been using a single Grep, and why certain responses took 30+ seconds.

**Ralph Loop** is Geoffrey Huntley’s approach to autonomous agent work, now an official Anthropic plugin. Claude exits normally each iteration, the loop starts a fresh session, and all state persists on disk through files and git history. From my own experience, Ralph works well for greenfield projects with clear specs and automated success criteria like tests passing.

**Frontend Design** generates distinctive UI implementations instead of the generic Bootstrap-looking output you get from a base Claude prompt. I use it for rapid prototyping when I need something that looks intentional.

**Excalidraw Skill** connects to a running Excalidraw MCP server and lets Claude create, edit, and iteratively refine diagrams on a live canvas. The part that makes this useful is the iterative refinement loop: Claude creates elements, takes a screenshot of its own work, evaluates against the quality checklist, and fixes issues before proceeding. **Fun fact:** the image for my skill setup at the top of this page was made by this Excalidraw skill!

## **How to Install Skills**

**For a single skill you found online:**

I recommend just prompting Claude/your agent to install the skill by copy-pasting a github repo link of the skill or plugin and saying:

> `“Install this skill <link to the skill>, tell me what it does and how I would use it.”`

Depending on where the skill is stored, it will either be accessible in only that project, or across your entire Claude setup. Skills in `~/.claude/skills/` are available in all your projects. Skills in `.claude/skills/ `are project-specific.

## **Making Claude Actually Use Your Skills**

[![](https://substackcdn.com/image/fetch/$s_!kKEP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda0350e4-bb99-40f8-8de1-eb932b1e36c2_1844x2304.png)](<https://substackcdn.com/image/fetch/$s_!kKEP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda0350e4-bb99-40f8-8de1-eb932b1e36c2_1844x2304.png>)

Having installed a bunch of skills, I discovered that half the battle is getting Claude to invoke them reliably. Here’s what I learned:

**The description field is important.** Claude reads skill descriptions to decide when to apply them automatically. A vague description like “helps with code” will never fire. A specific one like “Use when reviewing Python code for type safety, Pythonic patterns, and maintainability” will fire every time you ask Claude to review Python. Write the description as if you’re telling a coworker when to hand someone a specific reference sheet.

**Just call it directly when it matters.** If you need a skill to run, type /skill-name or tell your agent to utilize that skill in the prompt. Relying on automatic invocation is fine for convenience, but for anything important, explicit beats implicit.

**Check what’s actually loaded.** Run /skills to see your currently loaded skills. If something isn’t showing up, check the path (it must be SKILL.md, not skill.md), verify the directory structure, and restart Claude Code. I’ve lost time debugging skills that simply weren’t being found because they were saved in the wrong place.

**Understand the context budget.** Skill descriptions eat ~2% of your context window. If you install forty plugins with verbose descriptions, some will get silently dropped. [The Compound Engineering team](<https://github.com/EveryInc/compound-engineering-plugin>) learned this firsthand when their plugin was consuming 316% of Claude Code’s context description budget, causing components to silently get excluded. Their fix in v2.31.0 reduced agent descriptions from an average of 1,400 characters to 180 characters each, cutting context consumption by 79%. The lesson here is to keep descriptions short, and move details into the skill body where they only load on demand.

## **Building Your Own**

The best skills are the ones you write yourself, because nobody else knows your conventions. Here is an example prompt you can paste into Claude:

> “I write a weekly stakeholder update every Monday. Create a skill for it. It should include what shipped and the user impact, what’s in progress with timelines, blockers that need exec attention, and next week’s priorities. I want it to lead with outcomes, not tasks. No jargon.”

Claude created the SKILL.md, put it in ~/.claude/skills/stakeholder-update/, set the description field so it triggers automatically when I say things like “draft my weekly update,” and I was done. The whole thing took about 30 seconds. If you have the plugin-dev plugin installed, you can also run /create-plugin for a guided walkthrough that scaffolds the full directory structure for you.

A few things I’ve learned from writing my own:

**Start with one convention you repeat constantly.** PR descriptions, commit messages, code review checklists, deployment steps. If you find yourself typing the same instructions into Claude more than twice, that’s a skill, and you can just prompt claude to create the skill.

**Structure complex skills as routers.** The skill loads, asks one clarifying question, figures out intent, then loads only the relevant sub-instructions. This is how the Compound Engineering brainstorming skill works. It doesn’t dump all possible brainstorming frameworks into context up front. That means you’re treating skills like pointers for other skills

**Keep the description short and the body detailed.** The description burns context on every turn. The body only loads when invoked. Two sentences max for the description; put the real instructions in the body.

**Test the description trigger.** After writing a skill, try asking Claude to do the thing your skill covers without using the slash command. If Claude doesn’t load the skill automatically, your description isn’t specific enough. Iterate on the wording until it fires reliably for the right prompts.

## **Skills as Distribution**

Skills are markdown files, making them the simplest possible packaging for knowledge. And because of that simplicity, they’re the most honest representation of how someone actually thinks about a problem.

When I look at someone’s skill files, I can see exactly what conventions they follow, what mistakes they’ve learned to avoid, what their workflow looks like in practice. That accumulated operational knowledge, packaged in a format that any agent can use, is what makes skills worth sharing.

Companies are starting to figure this out. Product teams are shipping skills alongside their APIs so that Claude (and other agents that support the Agent Skills standard) can use their product correctly without the user reading any documentation. If you have domain expertise worth sharing, publishing a skill is a good place to start. You’re encoding your judgment in a format that works at the point of action.

## **Where to Find More Skills and Plugins**

**The official marketplace** comes built into Claude Code. Run /plugin and you’ll see a tabbed interface with Discover, Installed, Marketplaces, and Errors tabs. The official claude-plugins-official marketplace includes plugins maintained by Anthropic and vetted community contributors, including ralph-loop, frontend-design, and plugin-dev.

**Community GitHub repos** are where the most interesting stuff lives, and you have to know where to look:

  * [claude-code-plugins-plus-skills](<https://github.com/jeremylongshore/claude-code-plugins-plus-skills>) has 270+ plugins with 739 skills, plus a CLI package manager (ccpi) for searching and installing them.

  * My friend [Hamel Husain](<https://open.substack.com/users/2260358-hamel-husain>) just launched a great set of skills for evals! Check them out [here](<https://hamel.dev/blog/posts/evals-skills/>)




To add any third-party marketplace, you just tell Claude Code where the Git repo lives:

/plugin marketplace add https://github.com/EveryInc/compound-engineering-plugin

/plugin install compound-engineering

**People worth following:** Tom Doerr ([@tom_doerr](<https://x.com/tom_doerr>)) curates Claude Code tools constantly and maintains [MAGI//ARCHIVE](<https://tom-doerr.github.io/repo_posts/>), which catalogs hundreds of repos.

If you want to get started, pick one convention you repeat all the time and write a skill for it. Save it as ~/.claude/skills/my-thing/SKILL.md with a clear description. Use it for a week.

Or just paste this into Claude Code and let it set you up:

> Go to [aman.md](<https://aman.md/>) and set me up.

If you build your own skills, I want to hear about it!

### Ready for more?

Subscribe
