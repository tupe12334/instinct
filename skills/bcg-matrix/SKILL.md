---
name: bcg-matrix
description: "Classify portfolio items as Stars, Cash Cows, Question Marks, or Dogs by market share and growth."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [portfolio, strategy, growth, market-share, bcg, business, products]
    related_skills: [swot, the-project-portfolio-matrix]
---

# BCG Matrix (Boston Consulting Group Matrix)

## Overview

Portfolio strategy tool. Plot business units, products, or initiatives on two axes:
- **Market Growth Rate** (vertical): how fast is the market expanding?
- **Relative Market Share** (horizontal): your share vs largest competitor

```
              HIGH SHARE        LOW SHARE
             ┌─────────────┬─────────────┐
HIGH GROWTH  │    STARS    │  QUESTION   │
             │  (Invest)   │   MARKS     │
             │             │  (Decide)   │
             ├─────────────┼─────────────┤
LOW GROWTH   │  CASH COWS  │    DOGS     │
             │  (Harvest)  │  (Divest)   │
             └─────────────┴─────────────┘
```

## Quadrant Definitions

### Stars — High Growth, High Share
- Market leaders in growing markets
- Require heavy investment to maintain position
- Goal: protect share; they become Cash Cows as growth slows
- Action: **Invest**

### Cash Cows — Low Growth, High Share
- Dominant in mature/stable markets
- Generate more cash than needed to maintain position
- Fund Stars and Question Marks
- Action: **Harvest / Milk**

### Question Marks — High Growth, Low Share
- In growing markets but trailing competitors
- Require cash to grow; uncertain payoff
- Must choose: invest to become Stars, or exit
- Action: **Decide (build or harvest)**

### Dogs — Low Growth, Low Share
- Weak position in stagnant/declining market
- Consume resources with little return
- Candidates for divestiture unless strategic reason to keep
- Action: **Divest or wind down**

## How to Apply

### Step 1 — Define the portfolio
Identify the set of items to analyze (products, services, business units, projects, features).

### Step 2 — Score each item

**Market Growth Rate:**
- What is the annual growth rate of the market/segment?
- High = above your threshold (typically >10% for fast-moving sectors)
- Use industry data, trends, or estimates

**Relative Market Share:**
- Your market share ÷ largest competitor's market share
- >1.0 = you lead. <1.0 = competitor leads
- Simplify to High/Low if exact data unavailable

### Step 3 — Plot and classify
Place each item in the correct quadrant.

### Step 4 — Allocate resources
- Fund Stars to sustain growth
- Extract Cash Cows efficiently
- Make explicit decisions on Question Marks (don't drift)
- Exit Dogs unless strategic rationale exists

## Output Format

```
BCG MATRIX ANALYSIS: [portfolio context]

STARS (Invest)
- [item]: growth=[X%], share=[Y] — [rationale]

CASH COWS (Harvest)
- [item]: growth=[X%], share=[Y] — [rationale]

QUESTION MARKS (Decide)
- [item]: growth=[X%], share=[Y] — RECOMMENDATION: [build/harvest/exit + why]

DOGS (Divest)
- [item]: growth=[X%], share=[Y] — [exit plan or rationale for keeping]

PORTFOLIO HEALTH: [overall assessment and resource allocation recommendation]
```

## Limitations

- Oversimplifies complex competitive dynamics
- Market share data often unavailable or lagged
- Growth rate alone doesn't capture profitability
- Use as starting point for discussion, not final verdict
