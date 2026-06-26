---
name: force-field-analysis
description: "Map driving forces (pushing toward change) vs restraining forces (resisting change) to plan change management."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [force-field, change-management, driving-forces, restraining-forces, lewin]
    related_skills: [pre-mortem, swot, mckinsey-7s]
---

# Force Field Analysis

## Overview

Developed by Kurt Lewin, Force Field Analysis maps every significant force acting on a proposed change — forces pushing toward it (driving) and forces pushing against it (restraining). The goal is not to list them but to act on them: strengthen drivers, weaken restrainers, or both.

```
                        PROPOSED CHANGE
                              │
   DRIVING FORCES             │          RESTRAINING FORCES
   (push toward change)       │          (push against change)
                              │
   Cost savings ──────────►   │   ◄────── Staff retraining cost
   Regulatory pressure ─────► │   ◄────── Loss of familiar workflow
   Competitor pressure ──────►│   ◄────── Union resistance
   Leadership mandate ───────►│   ◄────── Budget constraints
                              │
                   ◄──── EQUILIBRIUM ────►
                   (change happens when driving
                    forces outweigh restraining ones)
```

Change occurs when the sum of driving forces exceeds the sum of restraining forces. The model reveals where to intervene — not just whether to proceed.

## Core Concepts

### Driving Forces
Pressures, motivations, or conditions that push toward the desired change. Sources include:
- External pressure (regulation, market, competition)
- Internal pull (leadership vision, cost reduction, quality goals)
- Opportunity forces (technology, growth, new capability)

### Restraining Forces
Resistances that oppose or slow the change. Sources include:
- Resource constraints (budget, time, headcount)
- Cultural or behavioral inertia (habit, fear of loss)
- Structural blockers (existing contracts, legacy systems, org design)
- Stakeholder opposition (unions, customers, adjacent teams)

### Force Strength
Each force has a relative strength — rate it on a consistent scale (e.g., 1–5). This prevents treating all forces as equal and reveals where small interventions yield the largest shift in equilibrium.

### Equilibrium
The current stable state. Change fails when restraining forces reassert. Lewin's Change Model pairs with this: Unfreeze (weaken restrainers) → Change (act) → Refreeze (embed the new state).

## How to Apply

### Step 1 — Define the change precisely
Write one sentence: "We will [specific action] by [date/milestone]." Vague changes produce vague force maps. "Improve culture" is not a change; "migrate all customer support to a new CRM by Q3" is.

### Step 2 — Brainstorm forces independently before grouping
Have each participant silently list driving and restraining forces. Group discussion before individual input anchors everyone to the first ideas voiced — silent brainstorm prevents this.

### Step 3 — Consolidate and rate each force
Cluster duplicates. For each remaining force, assign a strength score (1 = weak, 5 = strong). Be honest: a 5-rated restraining force that goes unaddressed will kill the change regardless of the number of driving forces listed.

### Step 4 — Score the equilibrium
Sum driving force scores. Sum restraining force scores. If driving > restraining, the change is viable but not guaranteed — identify the highest-rated restrainers and address them specifically. If restraining > driving, the change will fail without deliberate intervention.

### Step 5 — Build an action plan per force
For each restraining force rated 3 or higher: name a specific action to reduce it, an owner, and a deadline. For each driving force rated 3 or higher: name a specific action to amplify it. Do not leave the session without owners on the top forces.

## Output Format

```
FORCE FIELD ANALYSIS: [change statement]
Date: [date]  |  Owner: [name]

DRIVING FORCES                         RESTRAINING FORCES
Force                     Score │ Score  Force
─────────────────────────────── │ ──────────────────────────────
[driving force 1]           [n] │  [n]   [restraining force 1]
[driving force 2]           [n] │  [n]   [restraining force 2]
[driving force 3]           [n] │  [n]   [restraining force 3]
[driving force 4]           [n] │  [n]   [restraining force 4]
                                │
TOTAL DRIVING SCORE:        [n] │  [n]   TOTAL RESTRAINING SCORE
                                │
VERDICT: [Proceed / Proceed with conditions / Do not proceed]

ACTION PLAN
Restrainers to weaken:
1. Force: [restraining force]
   Action: [specific intervention]
   Owner: [name]  |  Due: [date]

2. Force: [restraining force]
   Action: [specific intervention]
   Owner: [name]  |  Due: [date]

Drivers to amplify:
1. Force: [driving force]
   Action: [specific intervention]
   Owner: [name]  |  Due: [date]
```

## Common Mistakes

- **Listing forces without scoring them.** An unweighted list makes every force look equal. A low-cost restrainer and an existential one appear identical — scoring forces is not optional.
- **Only addressing drivers.** Adding more driving forces rarely overcomes strong restrainers. The lever is almost always on the restraining side: find the 1–2 highest-rated blockers and remove them rather than piling on more reasons to change.
- **Generic forces.** "Resistance to change" is not a force — it is a category. "The sales team loses commission on legacy contracts for 90 days post-migration" is a force with an owner and a specific mitigation.
- **Treating the analysis as a one-time snapshot.** Forces shift during implementation. Re-run or update the map at major milestones; a restrainer that weakened may revive, and new driving forces may emerge.
- **Skipping the action plan.** The map has no value unless each high-rated force maps to a named action with an owner before the session ends. Insight without assignment is just documentation.
