---
name: marketing-mix-4ps
description: "Design or audit a go-to-market strategy across Product, Price, Place, and Promotion."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [4ps, marketing, product, price, place, promotion, go-to-market]
    related_skills: [stp-framework, value-proposition-canvas, ansoff-matrix]
---

# Marketing Mix — 4Ps

## Overview

The 4Ps framework structures a go-to-market strategy around four interdependent decisions: what you sell, what you charge, where you sell it, and how you tell people about it. Each P influences the others — a premium price demands a premium product and selective distribution. Use this to design a new GTM strategy or audit an existing one for internal inconsistencies.

```
┌──────────────┬──────────────────────────────────────┐
│ P            │ Core question                        │
├──────────────┼──────────────────────────────────────┤
│ PRODUCT      │ What are we selling and why it wins? │
│ PRICE        │ What do we charge and how?           │
│ PLACE        │ Where and how do buyers get it?      │
│ PROMOTION    │ How do buyers learn and decide?      │
└──────────────┴──────────────────────────────────────┘
```

## The Four Elements

### Product
Everything about the offering itself: features, quality, packaging, variants, support, and lifecycle stage. Product decisions must directly map to a target segment's job-to-be-done. Key sub-decisions: core vs. augmented product, differentiation from substitutes, and planned obsolescence or roadmap.

### Price
The revenue mechanism and positioning signal. Price communicates value before the customer experiences the product. Sub-decisions: pricing model (subscription, usage, one-time, freemium), anchor points, discounting policy, and price-to-value perception vs. competitors. A mismatched price undermines every other P.

### Place (Distribution)
The channels and logistics through which buyers access the product. Includes direct (own website, sales team, stores) and indirect (resellers, marketplaces, distributors). Sub-decisions: channel exclusivity, margin given to intermediaries, geographic coverage, and last-mile experience.

### Promotion
All communications that create awareness, interest, desire, and action. Includes advertising, content, PR, events, SEO/SEM, influencer, sales enablement, and in-product prompts. Sub-decisions: channel mix, message hierarchy, timing relative to purchase cycle, and measurement approach.

## How to Apply

### Step 1 — Anchor on the target segment
Before touching any P, state who you are selling to (segment + ICP), what problem you are solving, and what success looks like for them. Every 4P decision is only valid relative to a specific buyer. If the segment is unclear, stop and use STP or Value Proposition Canvas first.

### Step 2 — Define Product
Describe the offering in concrete terms: what it does, what it does not do, how it differs from the closest alternative, and what proof exists that it works. Name the lifecycle stage (launch, growth, maturity, decline) — this constrains your price and promotion choices.

### Step 3 — Set Price
Choose a primary pricing model and a specific price point. State the rationale: cost-plus, competitor-anchored, or value-based. Identify the price floor (unit economics) and ceiling (willingness to pay from research or proxy data). Specify discounting rules and whether you will use tiering.

### Step 4 — Map Place
List every channel where buyers can acquire the product, ranked by expected volume. For each channel: who owns it (direct vs. partner), what margin or cost it carries, and what the buyer experience looks like end-to-end. Flag channel conflicts if selling through multiple routes.

### Step 5 — Design Promotion
For each stage of the buyer journey (awareness, consideration, decision, retention), name the tactic, the message, the channel, the owner, and the KPI. Check that the message hierarchy is consistent across all channels and that it matches the price and product positioning.

### Step 6 — Audit for consistency
Do the four Ps tell the same story? A low price with premium promotion creates dissonance. A complex product sold exclusively through self-serve creates support debt. List any contradictions and resolve them before going to market.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  4PS ANALYSIS  ►  [product / company / campaign name]                               ║
║  TARGET SEGMENT:  [who — be specific]                                               ║
║  JOB-TO-BE-DONE:  [one sentence]                                                    ║
╚══════════════════════════════════════════════════════════════════════════════════════╝

┌───────────────────────────────────┬───────────────────────────────────┐
│  ● PRODUCT                        │  ● PRICE                          │
│                                   │                                   │
│  Offering:       [what it is and  │  Model:       [subscription /     │
│                  what it does]    │               one-time / usage /  │
│                                   │               freemium / hybrid]  │
│  Differentiator: [vs. closest     │                                   │
│                  alternative]     │  Price point: [specific number    │
│                                   │               or range]           │
│  Lifecycle:      [launch /        │                                   │
│                  growth /         │  Rationale:   [value-based /      │
│                  maturity /       │               competitor-anchored │
│                  decline]         │               / cost-plus]        │
│                                   │                                   │
│  Gaps:           [missing         │  Floor:       [unit cost]         │
│                  features or      │  Ceiling:     [max WTP]           │
│                  known weaknesses]│                                   │
│                                   │  Discounting: [policy]            │
├───────────────────────────────────┼───────────────────────────────────┤
│  ● PLACE                          │  ● PROMOTION                      │
│                                   │                                   │
│  Primary:   [channel] — [owner]   │  Awareness    → [tactic] via      │
│             — [margin/cost]       │    [channel]  KPI: [metric]       │
│                                   │       │                           │
│  Secondary: [channel] — [owner]   │       ▼                           │
│             — [margin/cost]       │  Consideration → [tactic] via     │
│                                   │    [channel]  KPI: [metric]       │
│  Conflict:  [yes / no —           │       │                           │
│             describe if yes]      │       ▼                           │
│                                   │  Decision     → [tactic] via      │
│  Last-mile: [fulfillment or       │    [channel]  KPI: [metric]       │
│             experience issue]     │       │                           │
│                                   │       ▼                           │
│                                   │  Retention    → [tactic] via      │
│                                   │    [channel]  KPI: [metric]       │
│                                   │                                   │
│                                   │  Theme: [brand/product promise]   │
└───────────────────────────────────┴───────────────────────────────────┘

╔══════════════════════════════════════════════════════════════════════════════════════╗
║  CONSISTENCY CHECK                                                                  ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║  Conflicts:       [list any P-vs-P mismatches]                                      ║
║  Recommended fix: [one action per conflict]                                         ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║  PRIORITY ACTIONS                                                                   ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║  1 ► [highest-impact change or decision]                                            ║
║  2 ► [second]                                                                       ║
║  3 ► [third]                                                                        ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

The four-quadrant grid keeps each P side-by-side so misalignments between them are immediately visible. The Promotion quadrant shows the buyer journey as a vertical arrow flow (Awareness → Consideration → Decision → Retention). The Consistency Check and Priority Actions panels at the bottom force an explicit cross-P audit before the output is considered complete.

## Common Mistakes

- Treating the 4Ps as independent — price set by finance, product by engineering, promotion by marketing, distribution by sales, with no one checking alignment. The result is incoherent positioning.
- Using aspirational product descriptions instead of what is shipping today. If the differentiator is on the roadmap, it cannot anchor the current promotion strategy.
- Skipping the segment definition and filling in Ps for "everyone" — every decision becomes a compromise that serves no one well.
- Confusing promotion budget with promotion strategy. Listing channel spend without naming the message, the KPI, or the buyer stage it targets produces activity, not results.
- Ignoring channel economics. A direct-sales channel and a marketplace channel at the same price point will create conflict or destroy margins; model both before committing.
