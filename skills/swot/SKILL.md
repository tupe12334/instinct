---
name: swot
description: "Analyze Strengths, Weaknesses, Opportunities, Threats for a subject to guide strategy."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [swot, strategy, analysis, strengths, weaknesses, opportunities, threats, planning]
    related_skills: [bcg-matrix, the-project-portfolio-matrix, feedback-analysis]
---

# SWOT Analysis

## Overview

Structured strategic assessment across four dimensions:

```
              HELPFUL           HARMFUL
         ┌──────────────┬──────────────────┐
INTERNAL │  STRENGTHS   │   WEAKNESSES     │
         │  (leverage)  │   (address)      │
         ├──────────────┼──────────────────┤
EXTERNAL │ OPPORTUNITIES│    THREATS       │
         │  (exploit)   │   (mitigate)     │
         └──────────────┴──────────────────┘
```

- **Internal factors**: within your control (Strengths, Weaknesses)
- **External factors**: in the environment (Opportunities, Threats)

## Dimension Definitions

### Strengths (Internal, Helpful)
Competitive advantages and capabilities you possess:
- Resources, skills, IP, brand, relationships
- What you do better than competitors
- What others see as your advantage

### Weaknesses (Internal, Harmful)
Limitations that put you at a disadvantage:
- Gaps in capability, resources, or knowledge
- What competitors do better
- Factors that limit your options

### Opportunities (External, Helpful)
External conditions you can exploit:
- Market trends, regulatory changes, competitor weaknesses
- Unmet customer needs
- Emerging technologies

### Threats (External, Harmful)
External conditions that could harm you:
- Competitor actions, market shifts, regulation
- Economic downturns, supply chain risk
- Disruptive technologies

## How to Apply

### Step 1 — Define scope
What are you analyzing? (Company, product, career, decision, project)

### Step 2 — Brainstorm each quadrant
For each dimension, generate 3–7 specific, concrete items. Avoid vague generalities ("good team" → "senior engineering team with 5 years avg domain experience").

### Step 3 — Prioritize within quadrants
Rank items by impact. Top 3 per quadrant is ideal for focus.

### Step 4 — Cross-analyze (TOWS)
The real value: match quadrants to generate strategic options.

| | Opportunities | Threats |
|---|---|---|
| **Strengths** | SO: Use strengths to exploit opportunities | ST: Use strengths to counter threats |
| **Weaknesses** | WO: Fix weaknesses to capture opportunities | WT: Minimize weaknesses, avoid threats |

### Step 5 — Derive actions
Each cross-analysis cell should yield 1–3 concrete strategic actions.

## Output Format

```
SWOT ANALYSIS: [subject]

STRENGTHS
1. [strength] — [why it matters]
2. ...

WEAKNESSES
1. [weakness] — [impact if unaddressed]
2. ...

OPPORTUNITIES
1. [opportunity] — [window/timeline]
2. ...

THREATS
1. [threat] — [likelihood and severity]
2. ...

STRATEGIC OPTIONS (TOWS)
SO (Leverage): [action exploiting S+O]
ST (Defend): [action using S to counter T]
WO (Improve): [action addressing W to capture O]
WT (Survive): [action minimizing exposure]

PRIORITY ACTIONS:
1. [highest-impact action]
2. [second action]
```

## Common Mistakes

- Listing aspirations as strengths (must be actual current capabilities)
- Conflating weaknesses with threats (internal vs external)
- Skipping TOWS — the raw quadrants without cross-analysis are half the value
- Too many items — depth beats breadth; focus on the critical few
