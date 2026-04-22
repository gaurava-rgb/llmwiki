---
title: "Spot on"
reader_id: "01kmnwhx96b7h14tgwy47skk8p"
notion_page_id: "34a4ebe7-f118-8148-9f85-d5fdf2574974"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kmnwhx96b7h14tgwy47skk8p"
source_url: "https://x.com/i/status/2036968353072357773/?rw_tt_thread=True"
author: "Jeremy S. Pollock"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-26"
saved_at: "2026-03-26"
reading_time: "10 mins"
summary: "The Agentic EHR is a new kind of medical record system where AI agents do most of the work and doctors just approve it. This system saves time by automating tasks like coding, prescriptions, and insurance approvals. It will help small clinics and virtual providers give better care at lower cost than today’s EHRs."
content_hash: "5b05196003a4ff9018f429340049f01451ee3f50d51a56d5bd50ea3610e6d8de"
---

Spot on.

This is a Trillion dollar idea that will transform healthcare delivery.

![](https://pbs.twimg.com/profile_images/1821247539506524160/OetIQjpg.jpg)

[Colton Ortolf](<https://twitter.com/ColtonOrtolf>) [@ColtonOrtolf](<https://twitter.com/ColtonOrtolf>)

[ ](<https://twitter.com/ColtonOrtolf/status/2036800456769392652>)

![Rise of the Agentic EHR](https://pbs.twimg.com/media/HEM2cDSaIAECSSd.jpg)

The "Headless EHR" is dead. Its successor doesn't need a head at all.

It's 7:42 AM on a Tuesday. Dr. Sarah Chen pulls into the parking lot at her primary care practice. She hasn't opened a chart yet. She doesn't need to.

**Overnight, her agents worked.** Three lab results came back from Quest. A metabolic panel for James Okafor flagged a creatinine of 1.8, up from 1.3 six months ago. Her renal monitoring agent caught it, calculated the eGFR trajectory (68 > 52 > 41, now CKD stage 3b), traversed James's medication list, and drafted a recommendation:

  * **Hold metformin** per FDA guidance for eGFR below 45
  * **Continue lisinopril** for its renoprotective benefit
  * **Order cystatin C** to confirm the decline
  * **Refer to nephrology:** prior auth pre-submitted to UnitedHealthcare at 3 AM with supporting documentation already attached



No human initiated any of this. The lab result arrived at 2:14 AM. The agent caught it, reasoned about it, and acted while Dr. Chen slept.

![Image](https://pbs.twimg.com/media/HEQk7K3bIAAhpqs.jpg)

Sarah walks in, coffee in hand, and opens her morning briefing. Not a chart. Not an inbox. A briefing: three patients flagged for action, ranked by clinical urgency.

James Okafor is at the top. She sees the agent's reasoning laid out: the creatinine trend, the eGFR trajectory, the specific KDIGO guideline citation, and the proposed action plan. She doesn't need to look up the lab, find the trend, remember the medications, check the guidelines, or call the insurance company. She needs to decide one thing: **does this plan make sense?**

It does. She taps approve. **One tap.** The hold goes on the metformin. The cystatin C order routes to Quest. The nephrology referral transmits. A patient message goes out in plain language. The follow-up is scheduled.

**45 seconds. One clinical decision.** In a traditional EHR, this would have been 15-20 minutes (or more) of chart review, order entry, phone calls to insurance, and inbox management.

![Image](https://pbs.twimg.com/media/HENBDIxXIAAjj8u.jpg)

Her first patient arrives at 8:00. Maria Gutierrez, here for a diabetes follow-up. Sarah walks in and starts talking. **She doesn't touch a computer.**

The encounter agent listens, not just transcribing, but reasoning. When Sarah says "let's think about adding a GLP-1," the formulary agent checks Maria's Blue Cross plan in the background. By the time Sarah finishes her sentence, a notification appears:

  * **Semaglutide** covered on Tier 2, prior auth required
  * **Step therapy criteria met** Maria has been on metformin for 14 months
  * **Prior auth documentation** ready to submit on approval



Sarah says "let's do it." The agent drafts the prescription, generates the prior auth, codes the encounter, and queues everything for her sign-off. Between patients, she reviews the approval queue: note, orders, codes, prior auth, all presented as a single package with confidence scores and an evidence trail. Two small edits to the note. Approve the rest. Move on.

**By noon,** Sarah has seen 14 patients. She has signed every note, approved every order, and made every clinical decision. But she hasn't manually entered a single diagnosis code, typed a prescription, navigated a chart, or called an insurance company. Her documentation is done. **There is no pajama time.**

## What is an Agentic EHR?

Around 2021, the digital health world got excited about the "Headless EHR": an API-first system where you rip off the UI and let builders create their own front-end. The right idea at the right time, but most implementations hit a wall. Five years later, the question has changed. It's no longer "can I build my own UI on top of the EHR?" It's: **why is a human operating the EHR at all?**

![Image](https://pbs.twimg.com/media/HEMzBzfaIAAbXbX.jpg)

An Agentic EHR is a clinical data and workflow system designed from the ground up for AI agents as its primary operators, with human clinicians as supervisors, not button-clickers. The agent reads, writes, reasons, and acts within the clinical record. The physician reviews, approves, and intervenes. The entire system ( data model, APIs, permissioning, audit trails ) is built around this assumption.

This is not "an EHR with AI features bolted on." Epic is doing that with AI Charting, Penny, and Emmie: automating individual tasks within a system still designed for humans. The human is still the user. The AI is a feature. The Agentic EHR flips that relationship.

## Here's the key test: **if you removed the clinician from the room for 10 minutes, would the system keep working?** In an EHR with AI features, nothing happens until a human clicks. In an Agentic EHR, agents continue processing lab results, triaging inbox messages, pre-submitting prior authorizations, and preparing for the next patient. The system has agency. The clinician provides judgment.

# The Agentic EHR Architecture

Dr. Chen's morning felt simple. One briefing, a few approvals, conversations with patients. But underneath Sarah's 45-second approval, seven systems coordinated: a lab result triggered an agent, which traversed a knowledge graph, which generated a clinical action plan, which passed through a permission framework, which pre-submitted a prior auth through a payer integration, which logged the full reasoning chain for audit, all before routing to her approval queue.

None of that is possible with today's EHR architecture. CRUD APIs can't resolve clinical intent. Relational databases can't support graph-based reasoning. Role-based permissions don't account for agent confidence. Audit logs don't capture why.

Building an Agentic EHR requires seven systems working together. Some exist in pieces today. None exist as a coherent stack.

![Image](https://pbs.twimg.com/media/HEM5KsRW0AAW3V_.jpg)

## Agent Orchestrator

The brain of the system. A stateful workflow engine that manages a directed acyclic graph (DAG) of agent tasks for every clinical encounter and between-encounter workflow. A single patient visit might spawn five agents running concurrently (documentation, coding, formulary checking, safety monitoring, and prior auth) each consuming the same event stream but producing different outputs. The orchestrator manages lifecycle, priority, and conflict resolution.

Think of it as a hybrid between Temporal (durable workflow orchestration) and LangGraph (LLM agent graphs), purpose-built for clinical workflows. The key design choice: agents don't call each other directly. They publish to the event backbone and subscribe to events they care about. This means you can swap, upgrade, and A/B test individual agents without rewiring the system.

## **Intent Resolution Layer**

![Image](https://pbs.twimg.com/media/HEM4jOnawAAtARw.jpg)

This replaces CRUD APIs. Today's EHR APIs are database operations: POST /orders/medications with NDC codes, SIG strings, and pharmacy identifiers. Miss a field, get a 400 error. These APIs were built for developers writing deterministic code.

An Agentic EHR exposes intent-based endpoints. Instead of constructing a medication order object, an agent sends: "Prescribe lisinopril 10mg daily for hypertension." The intent layer decomposes this into a validated action plan: drug lookup, dose check, interaction screening, formulary verification, pharmacy routing, prior auth pre-check. The agent gets back a structured, verified plan ready for physician approval.

Under the hood, this is an LLM-driven intent parser wrapped in deterministic validators. The probabilistic part is understanding what the clinician wants. Everything downstream (drug interactions, formulary checks, dosing) is rule-based. The intent layer is the bridge between natural language clinical reasoning and structured system operations.

## **Event Backbone**

The nervous system of the architecture. Traditional EHRs are request-response: nothing happens until a human clicks. An Agentic EHR is event-driven: every state change (lab filed, insurance verified, vitals recorded, message received) emits a typed event to a durable stream (Kafka-pattern). Agents subscribe to event types and react autonomously. This is why Dr. Chen's creatinine scenario works at 2 AM with no human in the loop.

## **Clinical Knowledge Graph**

![Image](https://pbs.twimg.com/media/HEM6J26aIAA_X5l.jpg)

Agents don't reason in table joins. They reason in relationships. A knowledge graph stores clinical entities (conditions, medications, labs) as nodes with typed, weighted edges: "This patient has hypertension, treated by lisinopril, which interacts with potassium supplements, ordered because of hypokalemia, detected by a lab drawn because of their diuretic, prescribed for the same hypertension." That's a graph traversal. It's also exactly how clinicians think. Implementation: a property graph with FHIR resources as canonical node representations, clinical ontologies (SNOMED, RxNorm, LOINC) as vocabulary, and vector embeddings for semantic similarity search across populations.

## **Trust and Permission Framework**

The make-or-break layer. Every agent gets a permission manifest; OAuth scopes with clinical semantics. The framework defines four tiers:

![Image](https://pbs.twimg.com/media/HEM5RLfWIAA4BV-.jpg)

  * **Tier 1 - Autonomous:** Agent executes without approval. Chart reads, summarization, pre-visit prep, inbox triage. Low-risk, high-frequency.
  * **Tier 2 - Propose + Approve:** Agent generates an action plan, physician approves. Medication orders, referrals, note signing. This is the core workflow loop.
  * **Tier 3 - Propose + Confirm + Approve:** High-risk actions requiring the physician to explicitly review supporting evidence. Controlled substances, diagnosis changes, etc.
  * **Tier 4 - Human-only:** Agent cannot act or propose. Goals-of-care conversations, breaking bad news, capacity determinations. Irreducibly human.



Each manifest also includes confidence thresholds (i.e., below 0.90, escalate one tier), temporal constraints (proposals expire after 24 hours), and contextual gates (pediatric patients automatically elevate one tier regardless of confidence).

The hard technical problem: agents reason probabilistically, but permissions must be enforced deterministically. The solution is a post-reasoning policy engine (OPA/Cedar-style) that validates every proposed agent action against its manifest after the agent reasons but before anything executes. Agents never write directly to the clinical record. They write to a staging area. The policy engine validates. Then it either commits (Tier 1), routes to approval (Tier 2-3), or blocks (Tier 4).

## **Reasoning Audit Trail**

When the "who" in a HIPAA audit log is an AI agent, you also need "why." Every agent action logs the input state observed, reasoning chain, confidence scores, alternatives considered, proposed action, and the physician's approval or override decision. This gives you reproducibility, counterfactual analysis, and a training dataset for continuous improvement. It's expensive to store. It's also the most valuable dataset in the system.

## **Integration Adapters**

## Surescripts, clearinghouses, HIE networks, reference labs: the same external systems, but invoked by agents through events and intent resolution instead of human clicks. This is where the headless EHR infrastructure wave pays dividends. Companies like Photon Health (prescribing APIs), Particle Health (clinical data), Candid Health (billing), and Availity (payer connectivity) already built the API-first plumbing. An Agentic EHR composes from these APIs rather than rebuilding them.

# Why Agentic Will Happen

The Headless EHR was a sound idea that largely failed in practice. Why would the Agentic EHR be different?

**The Headless EHR solved a real problem, but the execution cost killed it. The Agentic EHR changes the economics.**

The original headless insight was correct: builders wanted to create clinical interfaces tailored to their unique care models (behavioral health workflows, DPC visit flows, virtual-first triage) and the generic EHR UI was actively getting in the way of better care. The problem wasn't the vision. The problem was that building a custom clinical UI on top of a headless EHR meant hiring healthcare-specialized engineers, navigating ONC certification, reimplementing workflows the EHR already handled (badly, but completely), and maintaining all of it indefinitely. The build cost was enormous, and for most organizations, the ceiling of what they could create was still constrained by the EHR's API surface.

The Agentic EHR sidesteps this entirely. You don't need to build a better UI. You need a thinner one. The agent does the work; the physician approves it. The massive engineering effort that sank headless projects is replaced by a supervisory interface that's fundamentally simpler to build and maintain. And the ROI isn't "a better interface for our care model." It's measurable P&L impact. The average primary care physician spends nearly two hours on EHR tasks for every one hour of direct patient care. If agents reclaim even half of that administrative time, a 15-provider practice could see the equivalent of 3-4 additional providers' worth of patient-facing capacity, without hiring anyone. That's a CFO conversation, not a product roadmap conversation.

**The technology wasn't ready in 2021. It is now.**

In 2026, the AI layer that makes the Agentic EHR possible actually exists. Ambient documentation is proven at scale: Abridge processes 80M+ clinical conversations per year, and DAX Copilot is deployed across 600+ healthcare organizations. LLM reliability for structured clinical tasks has crossed utility thresholds: studies show AI-generated clinical notes match or exceed physician-authored notes in completeness and accuracy for routine encounters. Agent frameworks (LangGraph, CrewAI) provide orchestration primitives that didn't exist three years ago. Foundation models can reason over clinical data with sufficient accuracy that t**he Tier 1/Tier 2 permission model is viable today** , not in five years. The headless movement asked builders to construct entire clinical interfaces from scratch. The agentic movement asks them to orchestrate agents: a fundamentally different (and smaller) engineering surface.

**The buyer has evolved.**

In 2021, the customer for a Headless EHR was a digital health startup that wanted to build on top of it. The market was small, the budgets were VC-funded, and when funding dried up, so did the customer base.

The Agentic EHR's customer is every ambulatory practice, retail clinic, and virtual-first provider that's currently spending $150+/provider/month on an EHR plus $50-100/provider/month on ambient AI plus the hidden cost of administrative staff doing work that agents could handle. The average physician practice spends roughly $100K per year per physician on billing and administrative staff alone. The total cost of the current stack (software, AI add-ons, and the human labor compensating for what the software doesn't do) is the budget the Agentic EHR competes against. And that's before you count the revenue upside.

The greenfield market is expanding every quarter. Procedures continue migrating from inpatient to ambulatory at an accelerating rate, with ambulatory surgery centers growing 6-7% annually. Retail health is growing. Telehealth and DPC are scaling. Every new ambulatory site that opens is a potential Agentic EHR customer: a setting with no legacy EHR to rip out, where the AI-native option wins on both cost and experience.

**The incumbents can't build this.**

Epic makes money selling software to human users. Epic will keep bolting AI features onto their existing architecture and for inpatient settings, that's probably enough. But they won't build a system whose design premise is that humans shouldn't be the primary operators. The incentives don't allow it.

## This is the classic innovator's dilemma. The Agentic EHR starts in the segment Epic cares least about (small ambulatory, retail, virtual-first), proves itself where switching costs are lowest, and expands as the share of care delivered outside Epic's domain grows year over year. For this to work, the Agentic EHR has to be meaningfully better than what's already in the ambulatory market: not just Epic, but athenahealth, eClinicalWorks, and the rest of the mid-market incumbents. These systems are entrenched, well-integrated with billing workflows, and "good enough" for practices that aren't in active pain. The Agentic EHR doesn't win by being incrementally better at the same game. It wins by changing the game entirely, by delivering an operating model where a 5-provider practice runs with the administrative overhead of a 2-provider practice. That delta has to be real and demonstrable from day one.

The Headless EHR asked: can we give the EHR a better head? The Agentic EHR asks: does it need a head at all?

Someone's going to build this. The architecture is clear. The buyer is identified. The technology is ready. The incumbents are structurally unable to do it. The only question is who gets there first.

[Posted Mar 25, 2026 at 1:40PM](<https://twitter.com/ColtonOrtolf/status/2036800456769392652>)
