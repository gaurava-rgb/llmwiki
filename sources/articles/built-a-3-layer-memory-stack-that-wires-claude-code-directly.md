---
title: "Built a 3-layer Memory Stack that wires Claude Code directly..."
reader_id: "01kn79aa2magpjn3zmevdgzjt7"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kn79aa2magpjn3zmevdgzjt7"
source_url: "https://x.com/i/status/2039481184078409769/?rw_tt_thread=True"
author: "WorldofAI"
site: "X (formerly Twitter)"
tags: []
published: "2026-04-01"
saved_at: "2026-04-02"
reading_time: "5 mins"
summary: "WorldofAI built a 3-layer Memory Stack that connects Claude AI directly to Obsidian, so it remembers your project details and goals. This system cuts time spent re-explaining context by 85% and makes Claude a smart collaborator. It organizes information clearly and uses tools to turn all your knowledge into a searchable brain."
content_hash: "d8d4737601693faa1a0296c542233a7e8064e561246ff0e83baf4dfc547882c2"
---

Built a 3-layer Memory Stack that wires Claude Code directly into Obsidian with skills so it never forgets your project DNA, your notes, your standards, or your goals.

Fixes most of Claude Code's memory issues.

Your browser does not support the video tag.

![](https://pbs.twimg.com/profile_images/1656792400163921921/Z46Yn67p.jpg)

[WorldofAI](<https://twitter.com/intheworldofai>) [@intheworldofai](<https://twitter.com/intheworldofai>)

[ ](<https://twitter.com/intheworldofai/status/2039255561280057794>)

![Claude + Obsidian: Solving The Memory Issue! \(Walkthrough\)](https://pbs.twimg.com/media/HEzilABa0AAvhIv.jpg)

Most development teams waste **30 - 40 minutes per session** simply re-explaining context to Claude.

I call this **Context Amnesia** \- that frustrating moment when you open a fresh chat or terminal and your AI greets you like it’s the first date all over again. No memory of the architecture decisions you made yesterday, the bug you fixed last night, or the exact naming conventions you agreed on.

The knee-jerk reaction is “we just need a bigger context window.”

That’s wrong.

The real fix is a **3-layer compounding memory stack** that permanently wires your project DNA, personal knowledge graph, and external research into one living, searchable brain.

I’ve been running this exact system for the last nine months. It has cut my context-rebuilding time by ~85% and turned Claude from a clever autocomplete into a genuine senior collaborator that actually _knows_ my stack, my standards, and my long-term goals.

Here is the complete, battle-tested blueprint.

  1. The File Structure - Separation of Concerns (The Foundation)



Never throw AI-generated noise into your Obsidian vault. It dilutes the quality of your knowledge graph and makes semantic search noisy.

Instead, maintain **two parallel worlds** :


    ~/
    ├── claude/                          # ← The "Work" Folder (AI-heavy)
    │   ├── github/                      # Repos, PRDs, architecture decision records, skill matrices
    │   ├── meeting-notes/               # Raw transcripts from Zoom, Granola, Fireflies, etc.
    │   └── .claude/                     # Hidden per-project memory (auto-managed)
    │       └── projects/<hash>/
    │           └── memory/
    │               └── [MEMORY.md](<http://MEMORY.md/>)        # Claude’s own evolving learnings
    └── obsidian-vault/                  # ← The "Brain" (human-first, high-signal only)
        ├── 01-polaris/                  # Strategy, goals, Life Razors
        ├── 02-logs/                     # Daily scratchpads & weekly reviews
        ├── 03-commonplace/              # Atomic notes, evergreen ideas, tech deep-dives
        ├── 04-outputs/                  # Published drafts, blog posts, X threads
        └── inbox/                       # Temporary landing zone for ingested content


**Why this separation matters** :

  * Your Obsidian graph stays pristine and human-curated.
  * Claude still gets full read/write access to _both_ folders via the Model Context Protocol (MCP).
  * You keep the signal-to-noise ratio extremely high.


  2. Layer 1 - Session Memory ([CLAUDE.md](<http://CLAUDE.md/>) \+ Auto-Memory)



[CLAUDE.md](<http://CLAUDE.md/>) lives at the root of every repo and is the very first file Claude reads in every new session.

**How to bootstrap it** :

  1. Run the /init command inside your repo (I have a custom Claude command for this).
  2. Claude automatically scans the entire codebase and generates ~80% of the document.
  3. You manually enrich it with three sections:

**Nouns** \- Tech stack, folder structure, key abstractions, architecture patterns.

**Verbs** \- Exact build commands, test scripts, deployment flows, linting rules.

**Boundaries & Principles** \- Hard rules like “Never use default exports in React components”, “Always use Zod for schema validation”, “All API responses must be typed with TypeScript interfaces”.




Once Auto-Memory is enabled in Claude’s project settings, Claude begins writing its own learnings to ~/.claude/projects/<project-hash>/memory/[MEMORY.md](<http://MEMORY.md/>).

Example entry it might write after a session:

“Fixed race condition in useWebSocket hook by moving subscription logic into a useEffect with proper cleanup. Confirmed that reconnect logic now survives hot reloads. Do not re-introduce the old setInterval pattern.”

That single line saves you 10+ minutes next week.

  3. Layer 2 - The Knowledge Graph (Obsidian + MCP Bridge)



This is where the system becomes superhuman.

You connect Claude directly to your Obsidian vault using the **Model Context Protocol (MCP)**. Two tools make this magical:

  * **Smart-Connections MCP** : Semantic/vector search across your entire vault. Claude can ask “find every note related to authentication patterns” and get meaningful results even if you never used the exact keyword.
  * **QMD (Query Markup Documents)** : Lightning-fast hybrid search that understands wikilinks, aliases, and exact code snippets. Perfect when you need the _precise_ Docker Compose config from six months ago.



**MCP config file** (~/.claude/mcp-servers.json):


    {
      "mcpServers": {
        "qmd": {
          "command": "qmd",
          "args": ["mcp"]
        },
        "smart-connections": {
          "command": "node",
          "args": ["/absolute/path/to/smart-connections-mcp/dist/index.js"],
          "env": {
            "SMART_VAULT_PATH": "~/obsidian-vault",
            "OBSIDIAN_API_KEY": "your-key-if-needed"
          }
        }
      }
    }


With this bridge active, Claude can traverse your entire second brain in real time. It’s no longer guessing - it’s _reading your mind_.

  4. Layer 3 - Ingestion Pipeline (Turning Noise into Signal)



Most high-value knowledge arrives as a YouTube video, PDF, podcast, or research paper. I refuse to let it stay unstructured.

I use a local tool called brain-ingest (privacy-first, runs entirely offline after download):

Bash

brain-ingest "<https://youtube.com/watch?v=VIDEO_ID>" --enrich --vault ~/obsidian-vault

What happens under the hood:

  * Local transcription (Whisper-based)
  * LLM extraction of **Claims** , **Frameworks** , **Action Items** , and **Open Questions**
  * Automatic wikilinking to existing notes
  * Clean Markdown file dropped into inbox/ with proper frontmatter and tags



I review the note in < 60 seconds and move it into 03-commonplace/ if it’s evergreen. The compounding effect here is insane — every hour of content I consume becomes permanently searchable by Claude.

  5. The Polaris Strategy - Turning Claude into an Accountability Partner



In 01-polaris/Top of [Mind.md](<http://Mind.md/>) I keep one living document that contains:

  * Current quarterly goals (Q2 2026)
  * Active projects with success criteria
  * “Life Razors” - non-negotiable principles (e.g., “Ship before perfect”, “Write the docs first”, “Never add tech debt on purpose”)



Every time I start a new feature or refactor, I open with:

“Read my Top of Mind note first. Evaluate how this new auth flow aligns with my Q2 goals around reducing cognitive load and shipping velocity. Flag any misalignments and suggest adjustments.”

Claude now pushes back when I’m about to make a decision that contradicts my own stated direction. It’s like having a co-founder who never forgets what we agreed on in January.

  6. Full Setup Checklist (Copy-Paste Ready)

  7. **Repo level** Run /init → generates [CLAUDE.md](<http://CLAUDE.md/>)

Enable Auto-Memory in project settings

  8. **System level** npm install -g @tobilu/qmd

Install Smart-Connections MCP

Configure ~/.claude/mcp-servers.json

  9. **Vault level** Create the 01-polaris / 02-logs / 03-commonplace / 04-outputs structure

Add Top of [Mind.md](<http://Mind.md/>) and populate it

  10. **Advanced harness (optional but powerful)** Set up LACP (Local Agent Control Plane) for automated verification loops and policy gates
  11. **Daily rhythmOrient** → Open Top of Mind

**Work** → Code in the repo with full memory stack

**Persist** → Let Claude update [MEMORY.md](<http://MEMORY.md/>) and ingest any new learnings




Here is my full video on it: <https://youtu.be/srqWFT_TUec>

![Image](https://pbs.twimg.com/media/HEzj6VEaMAA0O3a.jpg)

**The Compounding Payoff**

After three months you’ll notice something wild: Claude starts _anticipating_ your needs. It references notes you wrote six weeks ago without you prompting it. It catches architectural drift before it happens. It becomes the most knowledgeable person on your team - because it literally has access to everything you’ve ever thought, built, or learned.

Memory is no longer a feature. It is the **operating system for your attention**.

In 2026 the developers who win won’t be the ones who prompt the fastest. They will be the ones who built a graph worth traversing.

If you’re running Claude + Obsidian today, drop your current memory setup in the comments. I’m always looking to steal better ideas.

What part of this stack are you going to implement first?

[Posted Apr 1, 2026 at 8:16AM](<https://twitter.com/intheworldofai/status/2039255561280057794>)
