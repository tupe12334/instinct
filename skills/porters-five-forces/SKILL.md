---
name: porters-five-forces
description: "Assess industry competitiveness via Threat of Entry, Supplier Power, Buyer Power, Substitutes, and Rivalry."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [porter, five-forces, competition, industry, strategy, analysis]
    related_skills: [swot, pestle, bcg-matrix]
---

# Porter's Five Forces

## Overview

Industry-level competitive analysis developed by Michael Porter. Measures the structural forces that determine how much profit potential an industry holds. Use it before entering a market, launching a product, or stress-testing a competitive position.

```
                        THREAT OF NEW ENTRANTS
                                 ▲
                                 │
  SUPPLIER POWER ───── INDUSTRY RIVALRY ───── BUYER POWER
                                 │
                                 ▼
                        THREAT OF SUBSTITUTES
```

High force intensity = low industry attractiveness (profits get competed away). Low force intensity = pricing power and sustained margins.

## The Five Forces

### 1 — Threat of New Entrants
How easy is it for new competitors to enter?
- **Raises threat**: low capital requirements, no IP protection, commodity product, low switching costs
- **Lowers threat**: patents, regulatory licenses, economies of scale, strong brand loyalty, network effects, high upfront investment
- Rate: Low / Medium / High

### 2 — Supplier Power
How much leverage do suppliers have over your costs?
- **Raises power**: few suppliers, no substitutes for inputs, suppliers can forward-integrate, your industry is a small customer for them
- **Lowers power**: many competing suppliers, you can backward-integrate, inputs are commodities, switching costs are low
- Rate: Low / Medium / High

### 3 — Buyer Power
How much leverage do customers have over your prices?
- **Raises power**: few large customers, product is undifferentiated, buyers can backward-integrate, buyers are price-sensitive, low switching costs
- **Lowers power**: fragmented customer base, high switching costs, product is essential or highly differentiated
- Rate: Low / Medium / High

### 4 — Threat of Substitutes
How likely are customers to switch to a different solution?
- **Raises threat**: substitute meets same need at lower price or higher convenience, low switching costs, buyers are willing to experiment
- **Lowers threat**: no close substitute exists, substitute requires behavior change, strong brand allegiance to your product
- Rate: Low / Medium / High

### 5 — Competitive Rivalry
How intense is the competition among existing players?
- **Raises rivalry**: many similarly sized competitors, slow market growth, low differentiation, high exit barriers, commodity pricing
- **Lowers rivalry**: few dominant players, fast-growing market, high differentiation, niche segments reduce direct overlap
- Rate: Low / Medium / High

## How to Apply

### Step 1 — Define the industry scope
Specify the exact industry or segment being analyzed. Too broad ("tech") loses signal; too narrow ("enterprise SaaS HR tools for 500-seat companies in Europe") may miss relevant threats. One sentence describing the competitive arena is enough.

### Step 2 — Rate each force (Low / Medium / High)
For each force, list 2–4 concrete evidence points, then assign a rating. Pull from actual data where possible: number of suppliers, customer concentration ratios, regulatory filings, patent counts.

### Step 3 — Identify the dominant forces
The 1–2 highest-rated forces are the structural constraints on profitability. These deserve the most strategic attention.

### Step 4 — Map strategic implications
For each dominant force, ask: What can we do to reduce its intensity or position ourselves to benefit from it? This is where analysis becomes strategy.

### Step 5 — Reassess over time
Forces shift. New regulation can raise entry barriers; a technology shift can make substitutes viable overnight. Schedule a re-analysis when market conditions change materially.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════╗
║               PORTER'S FIVE FORCES  ·  [industry / segment]                                     ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════╝

                     ┌──────────────────────────────────────────────┐
                     │           THREAT OF NEW ENTRANTS             │
                     │        Rating: [Low / Medium / High]         │
                     │  ● [barrier or enabler factor 1]             │
                     │  ● [barrier or enabler factor 2]             │
                     └─────────────────────┬────────────────────────┘
                                           │
                                           ▼
┌──────────────────────────────┐  ┌────────┴────────────────────────┐  ┌──────────────────────────────┐
│       SUPPLIER POWER         │  │      COMPETITIVE RIVALRY        │  │        BUYER POWER           │
│  Rating: [Low / Med / High]  │─►│    Rating: [Low / Med / High]   │◄─│  Rating: [Low / Med / High]  │
│                              │  │                                 │  │                              │
│  ● [factor 1]                │  │  ● [factor 1]                   │  │  ● [factor 1]                │
│  ● [factor 2]                │  │  ● [factor 2]                   │  │  ● [factor 2]                │
└──────────────────────────────┘  └────────┬────────────────────────┘  └──────────────────────────────┘
                                           │
                                           ▼
                     ┌─────────────────────┴────────────────────────┐
                     │            THREAT OF SUBSTITUTES             │
                     │        Rating: [Low / Medium / High]         │
                     │  ● [substitute factor 1]                     │
                     │  ● [substitute factor 2]                     │
                     └──────────────────────────────────────────────┘

╔══════════════════════════════════════════════════════════════════════════════════════════════════╗
║  FORCE SUMMARY                                                                                   ║
╠═══════════════════════════════════╦══════════════════╦════════════════════════════════════════════╣
║  Force                            ║  Rating          ║  Key Driver                              ║
╠═══════════════════════════════════╬══════════════════╬════════════════════════════════════════════╣
║  Threat of New Entrants           ║  [L / M / H]     ║  [single biggest factor]                 ║
╠═══════════════════════════════════╬══════════════════╬════════════════════════════════════════════╣
║  Supplier Power                   ║  [L / M / H]     ║  [single biggest factor]                 ║
╠═══════════════════════════════════╬══════════════════╬════════════════════════════════════════════╣
║  Buyer Power                      ║  [L / M / H]     ║  [single biggest factor]                 ║
╠═══════════════════════════════════╬══════════════════╬════════════════════════════════════════════╣
║  Threat of Substitutes            ║  [L / M / H]     ║  [single biggest factor]                 ║
╠═══════════════════════════════════╬══════════════════╬════════════════════════════════════════════╣
║  Competitive Rivalry              ║  [L / M / H]     ║  [single biggest factor]                 ║
╠═══════════════════════════════════╬══════════════════╬════════════════════════════════════════════╣
║  OVERALL ATTRACTIVENESS           ║  [Low/Med/High]  ║  Dominant: [force 1], [force 2]          ║
╚═══════════════════════════════════╩══════════════════╩════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│  STRATEGIC IMPLICATIONS                                                                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  1. [action addressing dominant force 1]                                                         │
│  2. [action addressing dominant force 2]                                                         │
│  3. [action to sustain or build competitive position]                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

The hub-and-spoke diagram shows directional pressure on the central rivalry box — forces rated High compress margins most. The summary table lets you scan all five ratings at a glance and quickly spot which one or two forces dominate the industry's profit structure.

## Common Mistakes

- Analyzing the wrong scope — rating "automotive" instead of "electric vehicles under $40K in North America" dilutes every finding
- Listing generic observations without evidence — "buyer power is high because customers want low prices" applies to every industry and says nothing
- Treating all five forces as equally important — identify the 1–2 forces that actually constrain your margins and focus there
- Ignoring force interactions — high supplier power combined with high buyer power is a margin squeeze; the combination matters, not just each force in isolation
- Using the analysis as a one-time snapshot — industries restructure; a force rated Low today can shift to High within 18 months after a regulatory change or new entrant
