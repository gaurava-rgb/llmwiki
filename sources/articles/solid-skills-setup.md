---
title: "Solid Skills setup"
reader_id: "01kjb0c43stndy4vdeyp04wc5n"
notion_page_id: "34a4ebe7-f118-814c-9c22-f65a177efacc"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kjb0c43stndy4vdeyp04wc5n"
source_url: "https://x.com/i/status/2026076069602939131/?rw_tt_thread=True"
author: "Morgan"
site: "X (formerly Twitter)"
tags: []
published: "2026-02-23"
saved_at: "2026-02-25"
reading_time: "5 mins"
summary: "Claude Code skills are special instruction sets that help automate tasks and improve workflows. Morgan uses skills for app design, user research, and finding new app ideas, which save time and boost quality. He encourages others to start simple by turning repetitive tasks into skills to see the benefits."
content_hash: "21e01fa8d6d100d37eb4333e32f154f6fb4ee0b38336b0714383aac4443d9e4a"
---

Solid Skills setup.

![](https://pbs.twimg.com/profile_images/1649670410848333825/yNqgk-ys.jpg)

[✌︎ frederik ✌︎](<https://twitter.com/froessell>) [@froessell](<https://twitter.com/froessell>)

[ ](<https://twitter.com/froessell/status/2025833621299351613>)

![My Claude Code Skills Setup](https://pbs.twimg.com/media/HB0z3YZXMAAIliB.jpg)## I've been writing a lot about Claude Code and a lot of people have asked about my Claude Code setup so let's talk about it.

I'll show you mine and you show me yours. Deal?

Before we start, let me just preface to say that I'm by no means an expert in this.

I haven't touched OpenClaw or the more advanced agent stuff yet. That's a beehive I don't want to stick my hand into right now. I just make things for myself out of curiosity and see what sticks.

I've only scratched the surface with skills but a few of them have genuinely changed how I work on a daily basis.

**WTF are skills?**

Skills are basically instruction sets you can give Claude Code. You can either download them from [skills.sh](<http://skills.sh/>) or create your own, depending on what you need. Skills tell Claude how to approach specific tasks: what to look for, what patterns to follow, what output to create.

Think of them as saved prompts on steroids. Instead of explaining what you want every time, you invoke a skill and Claude knows the playbook… if only my kids could do the same and learn how to stop throwing their clothes on the floor.

But I digress.

**The one that started it all: mobile-ios-design**

Recently I had a workflow problem and was experimenting with different tools. I was testing a flow where I'd create a PRD using Claude, paste that PRD into Superdesign.dev to generate a design, export that design into Figma (because of the MCP), then feed the design and PRD to Claude Code to build the app in SwiftUI.

The app worked. But it wasn't great. It felt off. Hard coded text styles. Spacing was good, but inconsistent. Navigation worked but looked like a hybrid app, not a native one.

I came across the mobile-ios-design skill and decided to try it. The skill goes through your app and enforces iOS Human Interface Guidelines. Proper system colors. Native navigation patterns. Correct text styles.

I ran it after the initial build and suddenly the app felt native.

Yay.

![Image](https://pbs.twimg.com/media/HB0z-4nWMAAiwGr.jpg)

**Impeccable: A design toolkit in skill form**

**Get it here: impeccable.style**

This is a collection of skills for design refinement. I don't use all of them, but a few have become regulars:

impeccable:critique

Gets UX feedback on your design. I run this when something feels off but I can't pinpoint why.

impeccable:polish

Final pass for alignment, spacing, consistency. The stuff I'd normally do manually in Figma but now Claude handles it in code.

impeccable:simplify

Strips designs down to essentials. Useful when I've overdesigned something and need to pull back or just want a fresh perspective on the design.

impeccable:normalize

Matches the design to your existing design system. Good for when AI-generated components don't follow your tokens.

The full list has maybe 15+ skills. I haven't tried them all. But having them available means I can invoke specific design thinking on demand instead of prompting from scratch every time.

**Feature Discovery: Enterprise UX research on autopilot**

This one I built for my day job. I work at an ecommerce company and we work across four platforms: iOS, Android, desktop web, mobile web. It's a big machine so we have to do a lot of research before making new features and that research can take forever if done correctly. But sometimes I just want to test an assumption, not roll out the big processes with sprint planning, jira tickets and OKR meetings.

Just a quick: "Is that a good idea or not?"

So I made a skill that can do that for me. Or at least give me a better idea if my assumption is worth pursuing further or not.

You give it a feature idea or optimization brief and mr. Claude then runs through six phases:

  1. Brief & Audit: Structures your idea and critiques the current state
  2. Competitor Research: Pulls patterns from Mobbin, analyzes competitors etc.
  3. Edge Cases & Flows: Maps user flows and inventories edge cases across all platforms
  4. Recommendations: Prioritizes quick wins, medium-term fixes, roadmap items
  5. Prototypes: Generates interactive React/Tailwind prototypes you can share including before & after versions and annotations for easy sharing
  6. Report: Packages everything into a markdown report with a summary for leadership



It can either do everything in succession or stop and reevaluate after each step. It's up to you. Run one phase, review, decide if you want to continue.

I've used it for things like "Is having a hamburger menu in the navigation on desktop a good idea" and "Should we add a new single column view on listings on iOS". It doesn't replace thinking, but it can help me evaluate an idea quicker.

**App Niche Hunter: From market gap to prototype while I sleep**

This one is for my side projects. My hobby projects. This is my play time.

It's simpler and more fun.

I give Claude Code a niche I want to create an app in, like "sleep apps", and it goes to work:

  1. Searches the App Store for top apps in that category, free and paid
  2. Scrapes 1 and 2 star reviews from the biggest ones
  3. Finds patterns in what people complain about
  4. Identifies gaps that could be filled by a new app
  5. Opens Rork in the browser and builds a prototype. This is an insane thing to watch
  6. Sends me a test link



I can set Claude to work and come back to a prototype based on real user frustrations, not my assumptions. Is it stylish and without the vibecode "feel"?

No, but it works and I can always improve the branding myself later if I want to continue with it.

It doesn't always find gold. But it's turned "I wonder if there's an opportunity in X" from a weekend research project into something I can run while I do something else.

**The point**

Claude Code on its own is powerful. You can build apps, fix bugs, ship projects.

But Claude Code with skills is a different tool. It's not just "build this". It's "build this the way I would if I had unlimited time."

The mobile-ios-design skill knows HIG better than I do. The Impeccable toolkit catches design issues I'd miss. Feature Discovery does research I'd skip because I suck at doing research and prefer to design (I usually just hand that stuff over to the experts in the company). The niche hunter explores ideas I'd never get around to.

But as I said earlier, I'm still figuring this out. There's a whole world of agents and orchestration I haven't touched yet. But even these basic skills have changed how I work.

If you're using Claude Code and haven't explored skills yet, start simple. Find one repetitive task you hate. Turn it into a skill. See what happens.

[Posted Feb 23, 2026 at 7:22AM](<https://twitter.com/froessell/status/2025833621299351613>)
