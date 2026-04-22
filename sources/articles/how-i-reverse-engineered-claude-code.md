---
title: "How I Reverse Engineered Claude Code "
reader_id: "01kkwfnqec0122tsx0jn6jj736"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kkwfnqec0122tsx0jn6jj736"
source_url: "https://x.com/i/status/2033488305191616875/?rw_tt_thread=True"
author: "Arinjay Wyawhare"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-16"
saved_at: "2026-03-16"
reading_time: "5 mins"
summary: "The author spent a week reverse engineering Claude Code, a large closed binary that bundles JavaScript code and serves as a prompt delivery system for Anthropic's AI. Inside, many hidden features are controlled by flags and telemetry, showing Anthropic ships code early but enables features later. The main product is the complex prompt that guides the AI, while the binary is just the container."
content_hash: "7dad5a1a02b4883099550099167e00d938b9faffddd5c280807cea8c54ca1ba0"
---

![How I Reverse Engineered Claude Code ](https://pbs.twimg.com/media/HDhQXuLbMAA7Vt1.jpg)

Caude Code is Anthropic's CLI tool. It ships as a 213 MB binary with no source code. I spent a week taking it apart.

## Why

I'd just wrapped up two projects, [C-ML](<https://github.com/jaywyawhare/C-ML>) \- a machine learning library in C, and [GigaVector](<https://github.com/jaywyawhare/GigaVector>), a vector database engine. There's always this restless period after finishing something. You need the next thing.

I'd been using Claude Code. It worked well. But it's a closed binary that talks to an API on my behalf, and I didn't know what it was actually doing. That's not a complaint, it's a starting condition. I have a security background and I know how to look inside things. So I did.

The immediate trigger was dumber than that, though. I don't update my packages. I was running v2.1.33 from mid-February while the world had moved on. Instead of updating last weekend, I started pulling the binary apart. In retrospect this was more productive than updating would have been.

## What's inside

You always start with file and readelf.


    $ file /opt/claude-code/bin/claude


*ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked
*

213 MB for a CLI tool is absurd. But strings told the story immediately:


    Bun v1.3.5 (Linux x64 baseline)


It's a [Bun](<https://bun.sh/>) single executable application - the entire JavaScriptCore runtime bundled with the app code into one ELF binary. Most of the 213 MB is runtime. The application itself is small.

This is the best case for reverse engineering. JavaScript, even minified, is much easier to read than compiled code.

## Getting the code out

Bun SEAs have a trailer at the end of the binary:


    $ strings -t x /opt/claude-code/bin/claude | grep "Bun!"


_d4c370a ---- Bun! ----_

The trailer points to a table of contents - 15 embedded files. The one that matters is the JavaScript bundle at offset 0x62DA02B.


    $ dd if=/opt/claude-code/bin/claude bs=1 skip=103700011 count=10357830 of=claude-code.js


 _9.88 MB of minified JavaScript. 7,493 lines. That's the whole application._

## Reading it

10 MB of minified JavaScript is unpleasant. Every variable is tC or sC1 or HY1. But minification can't rename string literals, and that's the way in.

Search for "You are Claude" and you land in the system prompt. Search for "tengu_" and you find 597 references to their internal feature flag namespace. These are your anchor points. From there you trace outward.

I used Claude Code to help analyze its own source. You feed it chunks of minified JS and ask what the functions do. It's good at this. There's something funny about a tool reverse engineering itself, but it works.

## The prompt architecture

The system prompt isn't a static string. It's assembled at runtime from 15+ modular sections:


    Identity layer          → "You are Claude Code..."
    Tone and style          → be concise, no emojis, etc.
    Task management         → how to track work
    Tool usage policy       → which tool when
    Security policy         → hardcoded constant, can't be overridden
    Code references         → formatting rules
    Dynamic sections        → memory, environment, MCP servers


The security policy is hardcoded. Everything else shifts based on the tools available, the model running, and the user's configuration.

There's also a hidden minimal mode: set CLAUDE_CODE_SIMPLE=true and the entire prompt collapses to one sentence. Probably exists for testing.

I'm not including the actual prompt text here. I don't know where Anthropic draws the line on this, and I'm not in a position to find out the hard way.

## Tengu

Buried in the code is a feature flag and telemetry system called "Tengu" -after mountain spirits from Japanese folklore. Nobody explains these naming choices. They just happen.

37 feature flags. About 560 telemetry events. Flags are evaluated through GrowthBook on Anthropic's infrastructure, with Statsig as a fallback. Telemetry goes through OpenTelemetry to Datadog plus Anthropic's own analytics endpoint. That's serious instrumentation for a CLI tool.

The interesting part: many flags were gating features that clearly existed in the code but weren't turned on. Extended thinking modes, alternative model routing, experimental UI, cost optimization experiments. The code was there. The switches were off.

## The version diff

By Sunday night I'd mapped enough to have a theory: these gated features aren't dead code. They're upcoming releases, already in the binary, waiting to be enabled.

To test this I grabbed v2.1.76, which Anthropic had just released. Extracted the new bundle (11 MB, larger), diffed it against v2.1.33.

The diff confirmed it. Features behind flags in the old version were live in the new one. New tools added. Prompts restructured. The agent system expanded significantly. Anthropic ships features into the binary weeks before turning them on publicly.

That's the payoff of reverse engineering. Not the extraction - that's mechanical. It's when your model of the system, built from days of reading mangled code, predicts something correctly. That's how you know you understand it.

## Things I didn't expect

The prompt uses 10,000+ tokens before the user says anything. With tool descriptions, [CLAUDE.md](<http://CLAUDE.md/>) files, memory, and system reminders, you're at 15-20k tokens of scaffolding per turn. That explains the cost.

The bash sandbox is real. I assumed it would be theater. It's not - there's a genuine allow/deny mechanism with network restrictions.

560 telemetry events is a lot for a CLI tool. They're measuring everything: tool usage patterns, error rates, performance, flag evaluations.

The prompt contains instructions about handling prompt injection, and also instructions about interpreting the tags that contain its own instructions. It's recursive in a way that makes you stop and think.

## Tools

  1. file, readelf, strings - Binary identification
  2. dd - Extracting the JS bundle
  3. grep, ripgrep - Pattern search through minified JS
  4. Claude Code - Analyzing its own source
  5. diff, meld - Version comparison



## If you want to try this

  * Install Claude Code




    yay -S claude-code


  * Find the binary - which claude
  * Look for the Bun trailer:




    strings -t x $(which claude) | grep "Bun!"


  * Extract the JS bundle from .rodata
  * Start with string searches



There's no encryption, no integrity checking, no anti-tamper. It's minified but not obfuscated. The door is open.

## Prior work

Others have approached this differently:

  1. [Kir Shatrov](<https://kirshatrov.com/posts/claude-code-internals>) intercepted API calls with mitmproxy - good for runtime behavior, misses the prompt architecture.
  2. [Reid Barber](<https://reidbarber.com/blog/reverse-engineering-claude-code>) found source maps in an early release - clean code, but Anthropic removed them.
  3. [Vrungta](<https://vrungta.substack.com/p/claude-code-architecture-reverse>) reconstructed architecture from runtime behavior - thorough but speculative.
  4. [Yuyz0112](<https://github.com/Yuyz0112/claude-code-reverse>) monkey-patched the SDK to log API calls.



Direct binary extraction gives you the most complete picture but the least readable one. Tradeoffs everywhere.

## What it actually is

After a week inside the binary: Claude Code is a prompt delivery system. The code is plumbing. It handles tools, manages context, talks to the API. The product is the prompt - thousands of carefully written tokens that tell the model how to behave.

The binary is packaging. The prompt is the product.

_All analysis was performed on locally installed software for educational purposes. No network interception or authentication bypass was involved._
