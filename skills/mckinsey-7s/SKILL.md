---
name: mckinsey-7s
description: "Align organizations across Strategy, Structure, Systems, Shared Values, Skills, Style, and Staff."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [mckinsey, 7s, organization, alignment, change, strategy, structure]
    related_skills: [balanced-scorecard, swot, force-field-analysis]
---

# McKinsey 7-S Framework

## Overview

Diagnostic tool for organizational alignment. It maps seven interdependent elements that must all pull in the same direction for a strategy to succeed. Misalignment in any element undermines the others — this is a system, not a checklist.

```
                    ┌─────────────┐
                    │   STRATEGY  │
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
    ┌──────┴──────┐  ┌─────┴──────┐  ┌────┴────────┐
    │  STRUCTURE  │  │  SYSTEMS   │  │    STAFF    │
    └──────┬──────┘  └─────┬──────┘  └────┬────────┘
           │         ┌─────┴──────┐        │
           └─────────┤   SHARED   ├────────┘
                     │   VALUES   │
           ┌─────────┤  (center)  ├────────┐
    ┌──────┴──────┐  └────────────┘  ┌─────┴───────┐
    │   SKILLS    │                  │    STYLE    │
    └─────────────┘                  └─────────────┘
```

Hard elements (tangible, manageable): Strategy, Structure, Systems
Soft elements (culture-driven, harder to change): Shared Values, Skills, Style, Staff

## The Seven Elements

### Strategy
The plan for competitive advantage: what you will do and what you will not do. Must be explicit, time-bound, and traceable to resource allocation decisions. Vague mission statements are not strategy.

### Structure
How the organization is divided — reporting lines, team topology, centralization vs. decentralization. Structure should follow strategy, but often ossifies and constrains it instead.

### Systems
Formal and informal processes that govern daily work: budgeting cycles, hiring pipelines, performance reviews, data flows, approval chains. Systems are where strategy either executes or dies.

### Shared Values
The core beliefs and culture that shape behavior when no one is watching. Not the values on the wall — the ones that actually drive decisions under pressure. The center of the model because they influence all other elements.

### Skills
Capabilities that exist in the organization as a whole, not just in individuals. Includes institutional knowledge, tooling proficiency, and the ability to learn. Ask: what does this org do distinctively well?

### Style
Leadership behavior and management culture as demonstrated by actions, not words. How leaders spend time, what they reward, how they handle failure. Sets the tone for the rest of the organization.

### Staff
Headcount composition, talent density, diversity, and the mechanisms used to attract, develop, and retain people. Distinct from Skills — this is about who is here, not what they can do.

## How to Apply

### Step 1 — Define the scope and trigger
Name the unit of analysis (whole company, division, team) and the reason for the assessment: merger, strategy pivot, underperformance, restructuring, or culture change. This anchors what "aligned" means.

### Step 2 — Describe the current state of each element
For each of the 7 elements, write 2–4 sentences describing what actually exists today, not what is intended. Pull from org charts, process docs, exit interviews, culture surveys, and firsthand observation.

### Step 3 — Describe the required future state
For each element, define what it needs to look like to support the target strategy. Be specific: "matrix structure with product-line P&L ownership" is useful; "more collaborative structure" is not.

### Step 4 — Identify misalignments
Compare current vs. required state for each element. Then check cross-element alignment: a new strategy with an unchanged incentive system (part of Systems) is a classic misalignment. Mark every gap.

### Step 5 — Sequence interventions
Hard elements are faster to change (restructure, redesign a process). Soft elements take longer. Sequence changes so hard-element moves don't outpace soft-element readiness — reorganizing before culture shifts causes thrashing.

## Output Format

```
McKINSEY 7-S ASSESSMENT: [organization / unit]
TRIGGER: [why this analysis is being done]

ELEMENT        | CURRENT STATE                          | REQUIRED STATE                         | GAP
---------------|----------------------------------------|----------------------------------------|--------------------
Strategy       | [what the strategy actually is today]  | [what it must become]                  | [gap description]
Structure      | [reporting lines, topology today]      | [required structure]                   | [gap description]
Systems        | [key processes governing daily work]   | [required processes]                   | [gap description]
Shared Values  | [observed cultural behaviors]          | [required cultural behaviors]          | [gap description]
Skills         | [org-level capabilities today]         | [capabilities needed]                  | [gap description]
Style          | [actual leadership behaviors]          | [required leadership behaviors]        | [gap description]
Staff          | [headcount composition, talent gaps]   | [required talent profile]              | [gap description]

KEY MISALIGNMENTS:
1. [element A] ↔ [element B]: [description of conflict and business impact]
2. ...

INTERVENTION PLAN:
Hard elements (start now):
- [action] — owner: [role], timeline: [date]

Soft elements (start now, expect 6–18 months):
- [action] — owner: [role], signal of progress: [observable indicator]
```

## Common Mistakes

- Treating Shared Values as aspirational — assess actual behavior, not stated values; interview people who recently left
- Skipping cross-element misalignment checks — the table is not enough; explicitly ask "does element X contradict element Y?"
- Changing Structure without touching Systems — reorganizing reporting lines while leaving old incentive and budget systems intact guarantees the old behavior continues
- Confusing Staff (who) with Skills (what they can do) — a team of senior engineers (Staff) may still lack ML expertise (Skills)
- Using the framework as a one-time snapshot — 7-S is most valuable as a recurring diagnostic during multi-year transformations, not a one-off audit
