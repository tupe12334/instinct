---
name: SMEAC
description: "Structure briefings as Situation, Mission, Execution, Administration/Logistics, Command/Communications."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [briefing, planning, military, execution, communication, SMEAC, operations, team]
    related_skills: [SMART, the-GROW-model, the-eisenhower-matrix]
---

# SMEAC Briefing Format

## Overview

SMEAC is a military operations briefing structure used to communicate complex plans clearly and completely. Adapted for business, project management, and high-stakes operational contexts.

| Section | What it covers |
|---------|---------------|
| **S** | Situation | Context — what's happening in the environment |
| **M** | Mission | The objective — what we must accomplish and why |
| **E** | Execution | How we'll do it — the plan, tasks, and phases |
| **A** | Administration/Logistics | Resources, supplies, support |
| **C** | Command/Communications | Who's in charge, how we communicate |

SMEAC ensures every participant has full context (Situation), clear purpose (Mission), a concrete plan (Execution), the resources they need (Administration), and knows who to contact and who decides (Command).

## Section Breakdowns

### S — Situation

Set the full context so everyone understands *why* this matters and what environment they're operating in.

Include:
- **What's happening** in the broader environment (market, product, org)
- **What the problem or opportunity is**
- **Key constraints or external pressures** (time, competition, regulations)
- **What we know vs what's uncertain**

Goal: no one should need to ask "why are we doing this?" after reading Situation.

### M — Mission

One clear sentence (or short paragraph) stating what must be accomplished and why. The mission is the single most important element — everything else serves it.

Formula: *[Who] will [what action] in order to [why / intended effect] by [when].*

Example: "The product team will ship the new onboarding flow by [date] in order to reduce Day-1 churn by 20%."

Rules:
- One mission — if you have two, run two briefings
- State both the **task** (what) and the **purpose** (why)
- Everyone in the room should be able to recite the mission from memory after the briefing

### E — Execution

The plan. How the mission gets accomplished.

Structure for complex missions:
1. **Commander's intent** (or leader's intent): the end state if the plan breaks down — what does success look like, even if we deviate from the plan?
2. **Concept of operations**: overview of the approach (phases, sequence)
3. **Task assignments**: who does what, with specific assignments per person or team
4. **Coordinating instructions**: timing, rules of engagement, cross-team dependencies, shared standards

For simpler missions:
- Phase 1: [what, who, by when]
- Phase 2: [what, who, by when]
- Contingencies: [if X happens, then Y]

### A — Administration / Logistics

Resources, support, and infrastructure needed to execute.

Cover:
- **Resources**: budget, tools, access, headcount
- **Timeline / Schedule**: key dates and milestones
- **Support**: who provides it, how to request it
- **Risk and contingencies**: what could fail, what's the fallback

### C — Command / Communications

Who's in charge and how everyone stays connected.

Cover:
- **Command hierarchy**: who decides what, escalation path
- **Primary contact**: who to go to for what
- **Communication channels**: where updates are posted, what cadence
- **Meeting / sync cadence**: standups, check-ins, reviews
- **Reporting requirements**: what metrics or status gets reported, to whom, how often

## How to Apply

### Use SMEAC when:
- Kicking off a project or operation with multiple teams
- Running a war room / incident response
- Onboarding a new team to an initiative
- Any situation where misalignment or information gaps would be costly

### Step 1 — Fill each section in order
Start with Mission (the anchor), then Situation (context), then Execution, Admin, Command.

### Step 2 — Brief the team
Read or present each section. Pause for questions at each section, not just at the end.

### Step 3 — Mission check
At the end, ask: "What is our mission?" One person states it. If they can't, the briefing failed.

### Step 4 — Distribute written record
SMEAC briefings should be written and distributed — verbal-only briefings lose fidelity.

## Output Format

```
SMEAC BRIEFING: [operation/project name]
Date: [YYYY-MM-DD]
Briefed by: [name/role]

─────────────────────────────────────────────
S — SITUATION
[Context: what's happening, the problem/opportunity, key constraints, known unknowns]

─────────────────────────────────────────────
M — MISSION
[One sentence: who + what + why + by when]

─────────────────────────────────────────────
E — EXECUTION
Commander's Intent:
  [End state — what success looks like even if the plan breaks down]

Concept of Operations:
  [High-level approach and phases]

Task Assignments:
  - [Team/Person]: [task] by [date]
  - [Team/Person]: [task] by [date]

Coordinating Instructions:
  - [Dependencies, timing rules, shared standards]

Contingencies:
  - If [condition]: [response]

─────────────────────────────────────────────
A — ADMINISTRATION / LOGISTICS
Resources: [budget, tools, access]
Timeline: [key dates]
Support: [who provides what]
Risks: [top risks and mitigations]

─────────────────────────────────────────────
C — COMMAND / COMMUNICATIONS
Decision authority: [who decides what]
Escalation path: [steps]
Primary contacts: [role → person → channel]
Update cadence: [frequency and format]
Reporting: [what, to whom, how often]
```

## Common Mistakes

- Writing a mission that's actually a task ("deploy the app" not "deliver [outcome] by [date] to [effect]")
- Skipping Situation — teams execute better when they understand the "why"
- Vague task assignments without named owners and dates
- No contingency plan — execution rarely follows the plan exactly
- Briefing verbally without written record
