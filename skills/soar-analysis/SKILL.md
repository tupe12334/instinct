---
name: soar-analysis
description: "Appreciative alternative to SWOT: Strengths, Opportunities, Aspirations, Results — focuses on possibility over deficit."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [soar, strengths, opportunities, aspirations, results, strategy, appreciative]
    related_skills: [swot, okr, clear]
---

# SOAR Analysis

## Overview

SOAR is an appreciative strategic framework that replaces deficit-hunting with possibility-building. Where SWOT surfaces weaknesses and threats, SOAR asks: what is already working, where can we go, what do we want, and how will we know we succeeded?

```
         PRESENT STATE            FUTURE STATE
       ┌──────────────────┬──────────────────────┐
INNER  │   STRENGTHS      │    ASPIRATIONS       │
       │  (what we have)  │  (what we want)      │
       ├──────────────────┼──────────────────────┤
OUTER  │  OPPORTUNITIES   │      RESULTS         │
       │ (what's possible)│  (how we measure it) │
       └──────────────────┴──────────────────────┘
```

Use SOAR when you need energy and alignment around a future state, not a forensic audit of what's broken.

## Dimension Definitions

### Strengths
What you genuinely do well right now — proven capabilities, assets, and advantages:
- Validated skills, IP, processes, or resources
- What your customers, users, or stakeholders already praise
- Competitive differentiators that are real today, not projected

### Opportunities
External conditions you can act on — trends, gaps, or changes that align with your strengths:
- Market or technology shifts opening new doors
- Underserved segments or unmet needs
- Partnerships, platforms, or channels available but not yet used

### Aspirations
The bold future you want to create — your shared vision expressed concretely:
- Where do you want to be in 1–3 years?
- What impact do you want to have on customers, the market, or your team?
- What would "remarkable success" look like in plain language?

### Results
Measurable outcomes that signal you have reached your aspirations:
- Specific metrics with targets and timeframes (not directions, actual numbers)
- Leading and lagging indicators that track progress
- Milestones that make the aspiration feel real and achievable

## How to Apply

### Step 1 — Set the scope
Name the subject: a product launch, a team, a business unit, a career decision, or an initiative. Write it at the top so every participant is answering the same question.

### Step 2 — Surface Strengths through positive inquiry
Ask "When are we at our best?" and "What is working that we should do more of?" Collect 4–8 concrete items. Reject vague claims — "strong culture" is not a strength until you can point to a behavior or outcome that proves it.

### Step 3 — Map Opportunities to your Strengths
For each strength, ask "What external condition could amplify this?" and "What doors are open right now that this strength can walk through?" Aim for 3–5 high-leverage opportunities, ranked by impact and feasibility.

### Step 4 — Draft Aspirations as vivid future statements
Write 2–4 statements in present tense as if the future has arrived: "We are the go-to platform for X", "Our team ships weekly with zero critical incidents." Avoid abstract language — if you cannot picture it, sharpen it.

### Step 5 — Define Results with numbers
Translate each aspiration into 1–3 measurable outcomes. Attach a target value and a date. If you cannot measure it, the aspiration is still too vague — go back and refine.

## Output Format

```
╔═══════════════════════════════════════════════════════════════════════════════════════════╗
║  SOAR ANALYSIS  ▸  [subject]                                                              ║
╠═══════════════════════════════════╦═══════════════════════════════════════════════════════╣
║  S  STRENGTHS                     ║  A  ASPIRATIONS                                       ║
║     what we have today            ║     where we want to be                               ║
║  ─────────────────────────────    ║  ──────────────────────────────────────────────────   ║
║  ● [strength 1]                   ║  ● [future-state statement, present tense]             ║
║    └─ [evidence / proof point]    ║  ● [future-state statement, present tense]             ║
║  ● [strength 2]                   ║  ● [future-state statement, present tense]             ║
║    └─ [evidence / proof point]    ║                                                       ║
║  ● [strength 3]                   ║                                                       ║
║    └─ [evidence / proof point]    ║                                                       ║
╠═══════════════════════════════════╬═══════════════════════════════════════════════════════╣
║  O  OPPORTUNITIES                 ║  R  RESULTS                                           ║
║     what's possible now           ║     how we know we succeeded                          ║
║  ─────────────────────────────    ║  ──────────────────────────────────────────────────   ║
║  ● [opportunity 1]                ║  Asp 1 ─► [metric] = [target] by [date]               ║
║    └─ [why now / time window]     ║  Asp 2 ─► [metric] = [target] by [date]               ║
║  ● [opportunity 2]                ║  Asp 3 ─► [metric] = [target] by [date]               ║
║    └─ [which strength amplified]  ║                                                       ║
║  ● [opportunity 3]                ║                                                       ║
║    └─ [why now / time window]     ║                                                       ║
╚═══════════════════════════════════╩═══════════════════════════════════════════════════════╝

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│  PRIORITY ACTIONS                                                                         │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│  1 ▸ [concrete next step that moves toward Result 1]                                      │
│  2 ▸ [concrete next step that moves toward Result 2]                                      │
│  3 ▸ [concrete next step that moves toward Result 3]                                      │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

Each quadrant follows the 2×2 SOAR grid: left column captures the present state (Strengths, Opportunities), right column captures the future state (Aspirations, Results). Every Aspiration in the top-right must trace directly to at least one measurable Result in the bottom-right via the `Asp N ─►` arrows, and every Opportunity should name the Strength it amplifies in its `└─` sub-bullet.

## Common Mistakes

- Listing wishes as strengths — a strength must be demonstrable today, not something you hope to build; if it does not exist yet, it belongs in Aspirations
- Vague aspirations with no visual anchor — "be a leader in the space" is not an aspiration, it is a slogan; rewrite until a newcomer could draw a picture of the outcome
- Results without numbers — "improve customer satisfaction" is not a result; "NPS above 50 by Q4" is
- Ignoring weaknesses entirely — SOAR does not pretend problems do not exist; it just does not lead with them; factor known risks into Opportunities (can this strength offset the risk?) or Results (set a floor metric)
- Using SOAR to avoid hard conversations — appreciative inquiry accelerates momentum, but unresolved conflicts or resource constraints still need to be named; if a real blocker exists, surface it in the Results section as a risk threshold
