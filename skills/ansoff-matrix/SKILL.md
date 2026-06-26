---
name: ansoff-matrix
description: "Choose growth strategy — Market Penetration, Market Development, Product Development, or Diversification."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ansoff, growth, strategy, market, product, diversification]
    related_skills: [bcg-matrix, swot, porters-five-forces]
---

# Ansoff Matrix

## Overview

Growth strategy tool. Map expansion options on two axes:
- **Products** (horizontal): existing vs new
- **Markets** (vertical): existing vs new

Each quadrant names a distinct growth strategy with a distinct risk profile. Risk increases as you move away from what you already know.

```
              EXISTING PRODUCT    NEW PRODUCT
             ┌──────────────────┬──────────────────┐
EXISTING     │   MARKET         │   PRODUCT        │
MARKET       │   PENETRATION    │   DEVELOPMENT    │
             │   (lowest risk)  │   (medium risk)  │
             ├──────────────────┼──────────────────┤
NEW          │   MARKET         │   DIVERSIFICATION│
MARKET       │   DEVELOPMENT    │   (highest risk) │
             │   (medium risk)  │                  │
             └──────────────────┴──────────────────┘
```

## Quadrant Definitions

### Market Penetration — Existing Product, Existing Market
- Grow by selling more of what you already have to customers you already reach
- Tactics: pricing changes, loyalty programs, increased marketing spend, outcompeting rivals for their share
- Risk: lowest — you understand the product and the customer
- Limit: ceiling exists; market share gains slow as you approach saturation

### Market Development — Existing Product, New Market
- Sell existing products to new segments, geographies, or channels
- Tactics: international expansion, targeting a new demographic, adding a B2B channel to a B2C product
- Risk: medium — you know the product but not the new customer
- Watch for: regulatory differences, cultural fit, distribution gaps

### Product Development — New Product, Existing Market
- Create new products or major extensions for customers you already serve
- Tactics: new features that become standalone offerings, adjacent product lines, version upgrades that open new use cases
- Risk: medium — you know the customer but carry product delivery risk
- Watch for: cannibalizing existing revenue, R&D overruns, feature-not-product confusion

### Diversification — New Product, New Market
- Enter entirely unfamiliar territory on both dimensions simultaneously
- **Related diversification**: new product/market shares capabilities or supply chain with existing business
- **Unrelated diversification**: pure conglomerate move; no operational overlap
- Risk: highest — limited existing knowledge on either axis
- Justified when: core market is declining, opportunity is asymmetric, or acquisition makes entry viable

## How to Apply

### Step 1 — State the growth objective
Write a single sentence: "We need to grow [revenue / users / market share] by [X] within [timeframe]." This anchors the analysis to a real decision.

### Step 2 — Inventory what you already have
List current products/services and current markets/segments. Be specific — "SMB customers in North America" not "businesses."

### Step 3 — Generate options per quadrant
For each quadrant, brainstorm at least two concrete options. Do not evaluate yet — just generate. Vague options like "expand internationally" must be sharpened to a specific market and entry mechanism.

### Step 4 — Score each option on two dimensions
- **Expected impact**: revenue or growth potential if executed well (High / Medium / Low)
- **Execution risk**: resources required, unknowns, dependencies (High / Medium / Low)

Use this to build a shortlist — favor options with High impact and lower risk unless you have a specific reason to accept more risk.

### Step 5 — Choose and commit
Select one primary strategy and at most one secondary. Trying to pursue all four simultaneously fragments resources and produces none. Assign owners, budget, and a 90-day milestone.

## Output Format

```
ANSOFF MATRIX ANALYSIS: [company / product / team context]

GROWTH OBJECTIVE: [one sentence — what you need to achieve and by when]

MARKET PENETRATION (Existing Product / Existing Market)
- Option 1: [specific action] — Impact: [H/M/L], Risk: [H/M/L]
- Option 2: [specific action] — Impact: [H/M/L], Risk: [H/M/L]

MARKET DEVELOPMENT (Existing Product / New Market)
- Option 1: [specific action + target market] — Impact: [H/M/L], Risk: [H/M/L]
- Option 2: [specific action + target market] — Impact: [H/M/L], Risk: [H/M/L]

PRODUCT DEVELOPMENT (New Product / Existing Market)
- Option 1: [specific product/feature + customer segment] — Impact: [H/M/L], Risk: [H/M/L]
- Option 2: [specific product/feature + customer segment] — Impact: [H/M/L], Risk: [H/M/L]

DIVERSIFICATION (New Product / New Market)
- Option 1: [specific move — related or unrelated] — Impact: [H/M/L], Risk: [H/M/L]
- Option 2: [specific move — related or unrelated] — Impact: [H/M/L], Risk: [H/M/L]

RECOMMENDED STRATEGY: [quadrant name]
PRIMARY INITIATIVE: [the specific option chosen]
RATIONALE: [why this quadrant given current resources, risk tolerance, and objective]
OWNER: [person or team]
90-DAY MILESTONE: [concrete, measurable checkpoint]
```

## Common Mistakes

- **Treating the matrix as a menu, not a choice.** Organizations that pick options from every quadrant end up diluted. The point is to concentrate resources on one strategic direction.
- **Confusing "new" with "slightly different."** A new pricing tier for existing customers is penetration, not product development. Mislabeling the quadrant leads to underestimating risk.
- **Skipping market validation before Product Development.** Building a new product for your existing market assumes those customers want it. Validate demand before committing R&D budget.
- **Defaulting to Diversification as ambition.** Diversification reads as bold; it is also the most likely to fail. Only pursue it when the other three quadrants are genuinely exhausted or blocked.
- **No defined owner or milestone.** A matrix with no committed follow-through is decoration. Every chosen option must have a named owner and a specific checkpoint within 90 days.
