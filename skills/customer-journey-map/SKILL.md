---
name: customer-journey-map
description: "Visualize every touchpoint a customer has with a product or service — stages, actions, emotions, pain points, opportunities."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [customer-journey, touchpoints, experience, ux, empathy, mapping]
    related_skills: [jobs-to-be-done, value-proposition-canvas, aarrr-pirate-metrics]
---

# Customer Journey Map

## Overview

A Customer Journey Map (CJM) is a structured visualization of every interaction a specific customer persona has with a product or service — from first awareness through to advocacy or churn. It externalizes what customers do, think, and feel at each stage so that friction and opportunity become visible to the whole team, not just to whoever talked to customers last.

```
STAGE       │ Awareness │ Consideration │ Decision  │ Onboarding │ Usage     │ Advocacy
────────────┼───────────┼───────────────┼───────────┼────────────┼───────────┼──────────
Actions     │ searches, │ reads reviews,│ signs up, │ completes  │ core task │ refers,
            │ sees ad   │ compares      │ pays      │ setup      │ loops     │ reviews
────────────┼───────────┼───────────────┼───────────┼────────────┼───────────┼──────────
Touchpoints │ Google,   │ G2, blog,     │ pricing   │ welcome    │ app, docs,│ NPS email,
            │ social    │ sales call    │ page      │ email      │ support   │ community
────────────┼───────────┼───────────────┼───────────┼────────────┼───────────┼──────────
Emotion     │ curious   │ interested    │ anxious   │ confused   │ confident │ loyal
curve       │ (+)       │ (+)           │ (-)       │ (--)       │ (++)      │ (+++)
────────────┼───────────┼───────────────┼───────────┼────────────┼───────────┼──────────
Pain Points │ irrelevant│ no clear      │ pricing   │ setup too  │ feature   │ no easy
            │ results   │ differentiator│ unclear   │ long       │ gap       │ share path
────────────┼───────────┼───────────────┼───────────┼────────────┼───────────┼──────────
Opportunity │ SEO /     │ stronger case │ trial /   │ guided     │ proactive │ referral
            │ targeting │ studies       │ guarantee │ checklist  │ nudges    │ program
```

## Core Dimensions

**Stages** — The distinct phases of the customer's experience from their own perspective. Common arc: Awareness → Consideration → Decision → Onboarding → Usage → Advocacy (or Churn). Adjust stages to match your actual product — a B2B sales cycle has different phases than a consumer app.

**Actions** — Concrete things the customer does at each stage. Use active verbs and customer-observable behavior: "searches 'project management tool'", "books a demo", "invites a teammate." Not "becomes aware" — that is internal state, not an action.

**Touchpoints** — The specific channels or interfaces where the interaction happens: Google search results, pricing page, onboarding email, Slack notification, support ticket. One stage can have multiple touchpoints.

**Thoughts** — What the customer is actively thinking at each stage. Pulled from interviews, support transcripts, and reviews. Written in first person: "I just need to know if this will work for my team."

**Emotion Curve** — The customer's emotional state at each stage, rated on a spectrum (frustrated → neutral → delighted). Drawn as a line across stages. Dips reveal moments of friction; peaks reveal moments of value.

**Pain Points** — Specific obstacles, confusions, or failures at each stage. Not vague ("bad experience") — concrete: "pricing page has no annual vs. monthly toggle," "setup wizard requires admin credentials they don't have."

**Opportunities** — One or two specific interventions per stage that would reduce friction or amplify a positive moment. Must be actionable: "add a 10-minute quick-start template to reduce time-to-first-value."

## How to Apply

### Step 1 — Fix the scope before you start
Choose one persona and one end-to-end journey. Do not mix personas (the SMB buyer and the enterprise buyer have different journeys) and do not map every possible path in one canvas. One map = one persona + one primary job.

### Step 2 — Define the stages from the customer's perspective
Draft 4–7 stages that reflect how the customer experiences the journey — not your internal funnel. Validate stage names by asking: "Would a real customer recognize this phase?" Rename "Acquisition" to "Researching options" if that is what it feels like from their side.

### Step 3 — Fill actions and touchpoints from real data
Use interview notes, session recordings, support tickets, NPS verbatims, and analytics — not internal assumptions. For each stage, answer: "What did they actually do, and where did they do it?" If you don't have data for a stage, mark it explicitly as assumed.

### Step 4 — Map the emotion curve
For each stage, give an emotion label and a valence score: negative (--), neutral (~), positive (++). Draw the curve across the map. The biggest dips are your highest-priority design problems. Moments that are already strongly positive are candidates for amplification (referral triggers, share prompts).

### Step 5 — Extract pain points and assign opportunities
For each stage, write the single worst pain point — the one with the highest frequency or severity in your data. Then write one specific opportunity that addresses it. Assign an owner and a priority. A journey map with no owners and no next actions is a poster, not a tool.

## Output Format

```
CUSTOMER JOURNEY MAP
Persona: [name / role / situation]
Journey: [e.g. "First-time user from signup to first successful export"]
Date: [date] | Data sources: [interviews / analytics / support tickets / assumed]

STAGE         [Stage 1]        [Stage 2]        [Stage 3]        [Stage 4]
────────────────────────────────────────────────────────────────────────────
Actions       [what they do]   [what they do]   [what they do]   [what they do]

Touchpoints   [channel/UI]     [channel/UI]     [channel/UI]     [channel/UI]

Thoughts      "[quote or       "[quote or       "[quote or       "[quote or
               paraphrase]"     paraphrase]"     paraphrase]"     paraphrase]"

Emotion       [label] (--)     [label] (~)      [label] (++)     [label] (+)

Pain Point    [specific        [specific        [specific        [specific
               obstacle]        obstacle]        obstacle]        obstacle]

Opportunity   [action item]    [action item]    [action item]    [action item]
Owner         [name]           [name]           [name]           [name]
Priority      [H/M/L]          [H/M/L]          [H/M/L]         [H/M/L]

SUMMARY
Biggest friction point: [stage + pain]
Most positive moment: [stage + what drives it]
Top 3 opportunities ranked by impact:
1. [opportunity] — Owner: [name] — By: [date]
2. [opportunity] — Owner: [name] — By: [date]
3. [opportunity] — Owner: [name] — By: [date]
Assumed stages (need validation): [list]
```

## Common Mistakes

- **Mapping from the inside out.** The most common failure: stages named after internal departments ("Marketing hands off to Sales"), actions described as what your team does, touchpoints listed as your own systems. Every cell should describe the customer's experience, not your process.
- **Building the map in a workshop without data.** A room full of well-intentioned assumptions is not a journey map — it is a group fiction exercise. Run at least 5 customer interviews before the workshop; use the workshop to synthesize, not to invent.
- **Skipping the emotion curve.** The emotion row is not decoration. It is the signal that separates stages that feel good but have hidden friction from stages that look fine in analytics but make customers feel stupid. If you remove it, you lose the empathy the whole tool is designed to generate.
- **Using it as a one-time deliverable.** A journey map built for a Q1 strategy deck and never updated becomes wrong within months. Treat it as a living document: revisit it after significant product changes, after customer research rounds, and when key metrics shift.
- **Too many stages at too high an altitude.** "Customer uses product" is not a stage — it contains an entire journey inside it. If a stage does not have specific, different actions and emotions from the adjacent stages, collapse it or split it into concrete sub-stages.
