---
name: pre-mortem
description: "Prevent failure by imagining the project has failed, then working backward to identify what went wrong."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [pre-mortem, risk, failure, planning, prevention, strategy]
    related_skills: [five-whys, force-field-analysis, swot]
---

# Pre-Mortem

## Overview

A pre-mortem is a prospective risk technique developed by Gary Klein. Before a project launches, the team imagines it is some future date and the project has already failed — then works backward to explain why. This "prospective hindsight" surfaces risks that standard risk registers and optimism bias routinely suppress.

```
NOW ──────────────────────────────────────────► FUTURE

  [Project              [Imagined          [Real
   Kickoff]              Failure Date]      Launch]
       │                      │                │
       │   Pre-Mortem         │                │
       │   runs HERE ◄────────┘                │
       │   "It failed. Why?"                   │
       │                                       │
       └──── fixes applied ───────────────────►│
```

Unlike a risk register (which lists vague probabilities), a pre-mortem produces a ranked, narrative list of specific failure stories that teams can act on immediately.

## Core Concepts

### Prospective Hindsight
Psychologically, people generate more and better reasons for an outcome when they treat it as having already happened rather than as a possibility. Declaring "it failed" — not "it might fail" — unlocks this effect. The team switches from defending their plan to explaining a known outcome.

### Individual Brainstorm Before Group Discussion
Group dynamics suppress minority views. Each participant writes their own failure narrative silently before any sharing. This prevents anchoring on the first idea voiced and ensures quieter team members contribute genuine concerns.

### Failure Categories
Structure the brainstorm across four domains to avoid blind spots:

```
┌─────────────────┬──────────────────────────────────────────┐
│ CATEGORY        │ EXAMPLES                                 │
├─────────────────┼──────────────────────────────────────────┤
│ Execution       │ missed deadlines, scope creep, key       │
│                 │ person leaves, quality shortcuts         │
├─────────────────┼──────────────────────────────────────────┤
│ Assumptions     │ market size wrong, customer need         │
│                 │ misunderstood, tech feasibility off      │
├─────────────────┼──────────────────────────────────────────┤
│ External        │ competitor moves, regulation change,     │
│                 │ economic shift, dependency failure       │
├─────────────────┼──────────────────────────────────────────┤
│ Team/Process    │ misaligned incentives, unclear ownership,│
│                 │ communication breakdown, wrong metrics   │
└─────────────────┴──────────────────────────────────────────┘
```

### Prioritization by Impact × Likelihood
After collecting failure modes, rank them. You cannot fix everything — focus mitigation effort on the top 3–5 risks that are both plausible and high-impact.

## How to Apply

### Step 1 — Set the scene
Open the session with a single sentence: "It is [specific future date] and the project has completely failed. We did not achieve [the stated goal]. Now explain why." Do not soften this. Keeping the failure hypothetical ("might fail") defeats the technique.

### Step 2 — Silently write failure narratives (5–10 minutes)
Each participant independently writes as many specific failure reasons as they can think of. Encourage concrete, story-form entries: "We launched three weeks late because the integration with the payment API took four times longer than estimated and no one escalated until week six." Vague entries like "technical risk" are not useful.

### Step 3 — Round-robin sharing and clustering
Go around the group, each person reading one item at a time until all unique items are on the board. Cluster duplicates. Aim for breadth — do not debate or evaluate during this step.

### Step 4 — Vote and rank
Each participant allocates 3–5 votes (dot-voting or similar) to the failure modes they find most credible. Rank the consolidated list by votes. The top items represent the team's collective assessment of the highest-risk failure paths.

### Step 5 — Assign mitigations and owners
For each top-ranked failure mode, define: (a) a concrete change to the plan that reduces the risk, and (b) a named owner who is accountable. Update the project plan before the session ends — insights not embedded in the plan are lost.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  PRE-MORTEM  ►  [Project or initiative name]                                         ║
╠════════════════════════════════════════╦═════════════════════════════════════════════╣
║  Session date : [date]                 ║  Imagined failure date : [date]             ║
╚════════════════════════════════════════╩═════════════════════════════════════════════╝

  ▼  FAILURE NARRATIVES — all submissions, clustered by category  ▼

  ┌───────────────────────────────────────────┬───────────────────────────────────────────┐
  │  EXECUTION                                │  ASSUMPTIONS                              │
  ├───────────────────────────────────────────┼───────────────────────────────────────────┤
  │  ● [specific failure story 1 — concrete   │  ● [specific failure story 3 — concrete   │
  │    account of what went wrong]            │    account of what went wrong]            │
  │  ● [specific failure story 2]             │  ● [specific failure story 4]             │
  ├───────────────────────────────────────────┼───────────────────────────────────────────┤
  │  EXTERNAL                                 │  TEAM / PROCESS                           │
  ├───────────────────────────────────────────┼───────────────────────────────────────────┤
  │  ● [specific failure story 5]             │  ● [specific failure story 6]             │
  │  ● [add more as collected]                │  ● [add more as collected]                │
  └───────────────────────────────────────────┴───────────────────────────────────────────┘

  ▼  RANKED RISKS — ordered by team vote  ▼

  ╔═════╦══════════════════════════════════════════════════════╦═══════╦════════════╗
  ║  #  ║  Failure Mode                                        ║ Votes ║  Severity  ║
  ╠═════╬══════════════════════════════════════════════════════╬═══════╬════════════╣
  ║  1  ║  [highest-voted failure mode]                        ║  [n]  ║  High      ║
  ╠═════╬══════════════════════════════════════════════════════╬═══════╬════════════╣
  ║  2  ║  [second failure mode]                               ║  [n]  ║  High/Med  ║
  ╠═════╬══════════════════════════════════════════════════════╬═══════╬════════════╣
  ║  3  ║  [third failure mode]                                ║  [n]  ║  Med/Low   ║
  ╚═════╩══════════════════════════════════════════════════════╩═══════╩════════════╝

  ▼  MITIGATION ACTIONS — one block per top-ranked risk  ▼

  ┌─ Risk #1 ─────────────────────────────────────────────────────────────────────────┐
  │  Failure   ► [highest-voted failure mode]                                         │
  │  Mitigation► [specific change to the plan that reduces this risk]                 │
  │  Owner     ► [name]                                                               │
  │  Done when ► [measurable condition confirming the risk is addressed]              │
  └───────────────────────────────────────────────────────────────────────────────────┘
  ┌─ Risk #2 ─────────────────────────────────────────────────────────────────────────┐
  │  Failure   ► [second failure mode]                                                │
  │  Mitigation► [specific change to the plan that reduces this risk]                 │
  │  Owner     ► [name]                                                               │
  │  Done when ► [measurable condition confirming the risk is addressed]              │
  └───────────────────────────────────────────────────────────────────────────────────┘
```

The 2×2 failure-narrative grid ensures coverage across all four blind-spot categories before any group discussion begins. The ranked risks table reflects the team's collective vote — only the top items (typically 3–5) should have mitigation blocks, keeping the action list focused and owned.

## Common Mistakes

- **Softening the premise.** Saying "imagine we might struggle" produces weak risk lists. Say "it failed" and commit to the fiction. Psychological distance kills the technique.
- **Letting the project lead dominate.** The person most invested in the plan is least likely to voice its fatal flaws. Enforce the silent individual write before any group discussion, and collect all inputs anonymously if needed.
- **Listing symptoms, not causes.** "The project was late" is a symptom. "The project was late because we had a single-threaded dependency on one senior engineer who also owned three other initiatives" is a cause worth acting on.
- **Skipping Step 5.** A pre-mortem that produces a ranked list but no plan changes is an anxiety exercise, not a risk tool. Every top-ranked failure mode must map to a concrete mitigation with an owner before the session closes.
- **Running it only once.** Pre-mortems are most valuable at project kickoff, but also at major pivots, scope changes, or team transitions. A single session at the start does not cover risks that emerge later.
