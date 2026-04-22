---
title: "If you missed this article when it first came out..."
reader_id: "01khbwqbqs5xm4cg9mp150mm16"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01khbwqbqs5xm4cg9mp150mm16"
source_url: "https://x.com/i/status/2022156484264833537/?rw_tt_thread=True"
author: "Morgan"
site: "X (formerly Twitter)"
tags: []
published: "2026-02-13"
saved_at: "2026-02-13"
reading_time: "6 mins"
summary: "Claude Code with Obsidian creates a powerful system for thinking by linking markdown notes like building blocks. Each vault has its own rules and philosophy, taught to the AI through a special file so it can help organize and find connections. This approach changes note-taking into managing a living knowledge network where the human guides and edits the AI's work."
content_hash: "8e336e4196620037b237a5350f6e8af2db8e85c9fa2f6190160cc97688c39963"
---

If you missed this article when it first came out, don't miss it twice.

Especially now that Opus 4.6 is here.

Claude Code + Obsidian is insanely powerful.

And no, you can't do the same thing with Notion or Notes.

![](https://pbs.twimg.com/profile_images/2012958446891536384/neq1Tu46.jpg)

[Heinrich](<https://twitter.com/arscontexta>) [@arscontexta](<https://twitter.com/arscontexta>)

[ ](<https://twitter.com/arscontexta/status/2013045749580259680>)

ive spent the last year building an operating system for thinking with ai. claude code runs my obsidian vaults

it extracts the key concepts, connects them to what you already figured out, and builds a living representation of your thinking

i find myself only working in the vault now

the markdown files know everything ive discovered, nicely structured and with automatic situational context injection for in-context learning

i use a vault index that helps the agent decide what notes to pull in, same pattern as how claude code decides which skills to load

(if you think about it, every note is basically a skill in some sense... highly curated knowledge that gets injected when relevant)

the deeper thing is that a vault encodes how you think, not just what you thought about. the methodology becomes part of the system

its all just markdown files, you own it completely. this is ai as thinking partner, not as a writing assistant

## knowledge = code?


i realized: knowledge bases and codebases have a lot in common

theyre both folders of text files with relationships between them, they both have conventions and patterns, and they both benefit from agents that can navigate and operate them

vibe coding changed how we write software by letting ai handle implementation while you focus on direction, and the same shift applies to knowledge work

you dont take notes anymore. you operate a system that takes notes

## what is a vault?


a vault is a folder of markdown files that link to each other:

files connect using [[wiki links]] which build a network of ideas

when you write [[quality is the hard part]] in one note, it creates a clickable link to another note with that title

the agent can follow these links to jump between related ideas, discovering connections you forgot existed

## how to write good notes


how you write those links matters

most people put references at the bottom like footnotes. instead, weave links into your sentences

dont write "this relates to quality, see: quality-note". write "because [[quality is the hard part]] we need to focus on curation"

the link becomes part of your thought, and the agent can follow your reasoning by following the links

also write notes that stand alone and are composable

if someone lands on a note from a link, they shouldnt need to read five other notes first to understand it

think of notes like lego blocks

each one is complete on its own, but they connect to build bigger structures

when your notes work this way, the network itself becomes valuable

the thing is, ai doesnt automatically understand your philosophy. you have to teach it

watching an ai completely disrespect my philosophies taught me this the hard way

when you need to teach claude how you think, you realize how much implicit knowledge you carry around. suddenly you have to textualize everything

my claudemd is around 2000 lines now because i keep refining what works and what doesnt

## every vault needs its own philosophy


heres what most guides get wrong. they give you a system and say follow this but every vault serves a different purpose and needs different principles

same as codebases really

you wouldnt use the same folder structure for a cli tool and a web app

i run multiple vaults. one is for thinking about ai and knowledge management, which is the example ill share

another is for work, which tracks projects and clients with completely different rules. the philosophy changes based on purpose

same underlying pattern, different rules. the pattern is:

1\. markdown files with links that any ai can read

1\. a [CLAUDE.md](<http://CLAUDE.md/>) file that teaches the agent your specific system

1\. structure that lets the agent orient quickly

1\. conventions written as instructions so the ai stays consistent

what goes in those instructions depends entirely on your purpose

## what this could be


a work vault might emphasize:

\- capture first, structure later

\- project folders with meetings and outputs

\- client context for ai consumption

a research vault might emphasize:

\- source tracking and citations

\- literature notes

\- claim verification

a creative vault might emphasize:

\- idea capture and incubation

\- draft progression

\- reference organization

## the thinking vault example


the vault im sharing focuses on developing understanding. the philosophy comes from the claude md file:

i can feel the difference when the vault is well maintained versus full of noise. depth matters more than breadth

here is a snippet from the claude md to emphasize on this:

## how claude finds things


when claude starts a session it needs to understand what exists without reading every file

thats impossible with thousands of notes. so my system has layers that let the agent orient quickly:



  1. claude sees the folder structure. a hook automatically shows what folders and files exist at session start


  2. an index file that lists every note with a one sentence description. claude can scan 50 notes in seconds without opening them


  3. topic pages (MOCs) that link to related notes these act like tables of contents for each subject



they also contain notes that claude leaves for itself about what it learned while traversing the graph, leaving breadcrumbs for future sessions

the ai starts broad, narrows to whats relevant, then follows links to build understanding



## core principles


these are the rules that work for my thinking vault. other vault types might need different ones:

1\. can this note be linked from elsewhere and still make sense? if linking to it forces you to explain three other things first, split it up. thats composability

1\. i stopped naming notes like topics and started naming them like claims. instead of "thoughts on ai slop" you write "quality is the hard part". when you link to it, the title becomes part of your sentence naturally (this also forces claude to think differently when building sentences, which i believe is beneficial because it requires understanding)

1\. insight that individual notes matter less than their relationships. a note with many incoming links is more valuable than an isolated note because every link creates a new reading path. the network is the knowledge

## how the agent operates


every task starts with orientation. claude scans the structure, checks the index for relevant notes, reads the topic page before making changes

it follows links to build understanding and makes no changes without context

when claude discovers something useful about navigating a topic, it records that in the topic page

future sessions read those notes and learn from past navigation. this is how the vault remembers how to think through itself

sometimes two notes interact in interesting ways. claude creates a new note capturing the insight that emerges from combining them

every new capture triggers a search for related notes. claude adds links with context

## folder architecture


this structure works for a personal thinking vault. a work vault might have projects and clients

the point isnt the specific folders but that folder location tells you what something is

markdown is the system. tools like obsidian are just windows into it. the vault could survive any app disappearing

everything is plain text that any editor can read and any ai can process. you own your data completely

## how to start






  1. create a folder with subfolders that match your purpose. think about what you actually need to organize


  2. write a claude md that explains your system. start simple and evolve it as you learn what works


  3. let claude operate. capture something and ask claude to find connections. let it navigate and discover relationships and suggest where things belong



ALWAYS review what it produces and edit for quality

youre not taking notes anymore but directing a system that takes notes. your job becomes judgment, which means deciding what matters

the human role evolves from writer to editor and from creator to curator



## tldr






  * vibe coding changed how we write software. vibe note taking changes how we think


  * a vault is just markdown files that link to each other


  * llms have no memory, so vaults give them one


  * claude md teaches the ai how your system works


  * every vault needs its own philosophy based on purpose


  * what stays constant: markdown, links, ai operates while you provide judgment



if you want to see how this evolves, follow along. im open sourcing my notes soon

heinrich


[Posted Jan 19, 2026 at 12:28AM](<https://twitter.com/arscontexta/status/2013045749580259680>)
