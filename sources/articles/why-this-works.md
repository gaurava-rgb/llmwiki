---
title: "Why this works:"
reader_id: "01km6g3mzfqsv041jt6hk2m40h"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01km6g3mzfqsv041jt6hk2m40h"
source_url: "https://x.com/i/status/2034343368977961146/?rw_tt_thread=True"
author: "Corey Ganim"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-18"
saved_at: "2026-03-20"
reading_time: "3 mins"
summary: "Breaking a large AI skill file into smaller, focused files helps Claude stay focused and remember important details. Each file loads only what Claude needs at each step, improving quality and making fixes easier. This modular approach is like how developers organize code into modules for better results."
content_hash: "44f0e9626ff8cf63da33c796a959497cb739b29ead0239f926355e523abe7309"
---

Why this works:

Single-file skills force Claude to hold everything in working memory at once. Voice rules compete with formatting rules. Examples get buried under instructions. The longer the file, the more Claude "forgets" what matters for the current step.

Folder-based skills fix this by loading context just-in-time.

Writing the intro? Load only [voice.md](<http://voice.md/>) and examples/good/.

Running eval? Load only [checklist.md](<http://checklist.md/>).

Claude's attention stays focused on what matters RIGHT NOW.

The outcome:

→ Less drift mid-document (Claude doesn't lose the voice halfway through)

→ Easier debugging (bad output? Check which file it loaded)

→ Faster iteration (fix one file without breaking others)

→ More consistent quality across runs

This is the same reason developers split code into modules instead of writing one giant file.

Same principle. Applied to prompts.

![](https://pbs.twimg.com/profile_images/2020688928215646208/w1dcfnp3.jpg)

[JJ Englert](<https://twitter.com/JJEnglert>) [@JJEnglert](<https://twitter.com/JJEnglert>)

[ ](<https://twitter.com/JJEnglert/status/2034329261960475086>)

I just finished restructuring all my skills based on [@AnthropicAI](<https://twitter.com/AnthropicAI>) 's latest recommendations for how to build them.

Here's what's different, why it matters, and how you can do it too.

Our #1 AI newsletter ([tenex.co/ultrathink](<https://www.tenex.co/ultrathink>)) skill used to be one long file. Voice rules, examples, subject line logic — all crammed into one document.

It worked pretty well. But Claude would drift every now and again. It would nail the tone in one section and lose it in another. And every time I wanted to fix one thing, I risked breaking something else.

The problem isn't Claude. It's how you feed it information.

When everything lives in one file, Claude tries to hold it all at once. Rules compete with each other. Examples get buried. The longer the file, the worse the output.

The fix: break one file into a folder of specialized files.

  1. [SKILL.md](<http://SKILL.md/>) is the boss. It doesn't contain any rules itself — it just tells Claude which files to read and when. Like a playbook.

  2. instructions/ holds the actual rules. One file for voice. One for subject lines. One for section-specific guidance. They never compete because Claude only loads what it needs for the current step.

  3. examples/ is where Claude learns what good and bad look like. Good examples from real shipped work. Bad examples showing 12 common AI writing patterns to avoid. Claude reads these right before writing so the voice is fresh.

  4. eval/ is the quality check. After every draft, two things run automatically:

  5. A checklist with 9 pass/fail tests

  6. An advisory board — 3 AI personas (Exec, Builder, Lurker) review the draft in parallel and give feedback




The workflow it runs:

  * Load the rules
  * Gather inputs
  * Read relevant examples
  * Write the draft
  * Run the checklist + eval (9 tests)
  * Run the advisory board (3 reviewers in parallel)
  * Revise based on feedback
  * Save and queue for human preview / review



Every step loads only what it needs, when it needs it.

Want to restructure your own skills? Paste this into Claude Code:

\--

I want to restructure my Claude Code skill files. Right now my skills are single files that try to do everything. I want to break them into a folder system like this:

[SKILL.md](<http://SKILL.md/>) — the orchestrator that tells Claude which files to read and when

instructions/ — one file per set of rules (voice, formatting, section guides)

examples/good/ — annotated examples of great output

examples/bad/ — anti-patterns to avoid

eval/[checklist.md](<http://checklist.md/>) — pass/fail tests that run after every draft

eval/[advisory-board.md](<http://advisory-board.md/>) — AI reviewer personas that evaluate drafts in parallel

templates/ — output format templates

Phase 1: Read my existing skill files and identify every distinct concern (voice rules, formatting, examples, evaluation criteria, templates). Show me the audit before building anything.

Phase 2: Create the folder structure and move each concern into its own file.

Phase 3: Build [SKILL.md](<http://SKILL.md/>) as the orchestrator — it should contain no rules, just the step-by-step workflow pointing to the right files.

Phase 4: Build the eval layer with a checklist and 2-3 reviewer personas.

Phase 5: Run the skill on a real task and verify everything works.

Start with Phase 1.

[Posted Mar 18, 2026 at 6:01PM](<https://twitter.com/JJEnglert/status/2034329261960475086>)
