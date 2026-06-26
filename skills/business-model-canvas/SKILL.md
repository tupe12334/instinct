---
name: business-model-canvas
description: "Design or audit a business model across 9 blocks: segments, value props, channels, relationships, revenue, resources, activities, partners, costs."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [business-model, canvas, strategy, revenue, channels, segments]
    related_skills: [lean-canvas, value-proposition-canvas, swot]
---

# Business Model Canvas

## Overview

A single-page strategic tool for designing or stress-testing how a business creates, delivers, and captures value. Nine blocks map the full operating logic — from who you serve to how you make money and what it costs.

```
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│  KEY         │  KEY         │    VALUE      │  CUSTOMER    │  CUSTOMER    │
│  PARTNERS    │  ACTIVITIES  │ PROPOSITIONS  │  RELATIONS   │  SEGMENTS    │
│              │              │               │              │              │
│              ├──────────────┤               │              │              │
│              │  KEY         │               ├──────────────┤              │
│              │  RESOURCES   │               │  CHANNELS    │              │
├──────────────┴──────────────┴───────────────┴──────────────┴──────────────┤
│             COST STRUCTURE              │         REVENUE STREAMS          │
└─────────────────────────────────────────┴──────────────────────────────────┘
```

## The 9 Blocks

### 1. Customer Segments
Who are you creating value for? Name distinct groups — not "everyone." Each segment may warrant a separate canvas if their needs, channels, or willingness-to-pay differ significantly.

### 2. Value Propositions
What problem do you solve or need do you satisfy, and why choose you? Be specific: faster, cheaper, more accurate, exclusive access, reduced risk. Vague claims ("best quality") are not value propositions.

### 3. Channels
How do you reach and deliver to each segment? Include awareness, evaluation, purchase, delivery, and post-sale stages. Distinguish owned (website, salesforce) from partner channels (resellers, marketplaces).

### 4. Customer Relationships
What type of relationship does each segment expect? Options include self-service, automated, personal account manager, community, co-creation. This drives support costs and retention.

### 5. Revenue Streams
How does each segment pay, and for what? Separate revenue types: transaction fees, subscriptions, licensing, advertising, freemium upsell. Note pricing mechanism (fixed, dynamic, auction, usage-based).

### 6. Key Resources
What assets are non-negotiable to deliver the value proposition? Physical (factories, hardware), intellectual (patents, data, brand), human (specialized talent), financial (credit lines).

### 7. Key Activities
What must the business do well to function? Product development, platform management, supply chain, content production. Focus on activities that directly support the value proposition.

### 8. Key Partners
Who do you rely on that you do not own? Suppliers, co-creators, alliances, joint ventures. Ask: what do partners provide that we cannot or should not build ourselves?

### 9. Cost Structure
What are the largest costs to operate this model? Separate fixed costs (salaries, rent) from variable costs (COGS, transaction fees). Label the model: cost-driven (minimize costs) or value-driven (premium experience justifies higher costs).

## How to Apply

### Step 1 — Pick a unit of analysis
Define the scope: a whole company, a product line, or a single market entry. The canvas should describe one coherent business model, not an entire conglomerate.

### Step 2 — Start with Customer Segments and Value Propositions
These two blocks anchor everything else. If you cannot name specific segments and concrete value props, the rest of the canvas will be vague. Validate against real customer evidence before proceeding.

### Step 3 — Fill the delivery side (Channels, Relationships, Revenue)
Trace the path from value prop to cash: how do customers find out, buy, receive, and pay? Check that each segment has a matching channel and relationship type.

### Step 4 — Fill the infrastructure side (Resources, Activities, Partners)
Work backwards from the value proposition: what must exist internally (resources, activities) and what can be sourced externally (partners)?

### Step 5 — Map costs and check viability
List all significant costs. Then ask: do the revenue streams plausibly exceed the cost structure at scale? Identify the most cost-intensive and revenue-critical blocks — those are your risk concentration points.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  BUSINESS MODEL CANVAS  ►  [Company / Product / Venture name]                                       ║
╠══════════════════════╦═══════════════════════╦══════════════════════╦══════════════════════╦══════════════════════╣
║  KEY PARTNERS        ║  KEY ACTIVITIES       ║  VALUE               ║  CUSTOMER            ║  CUSTOMER            ║
║                      ║                       ║  PROPOSITIONS        ║  RELATIONSHIPS       ║  SEGMENTS            ║
║  Who we rely on:     ║  What we must do:     ║                      ║                      ║                      ║
║  ● [Partner A]:      ║  ► [Activity 1]:      ║  For [Segment A]:    ║  [Seg A]:            ║  ● [Segment A]:      ║
║    [what provided]   ║    [why critical]     ║  → [problem solved / ║  [relationship type] ║    [size/descriptor] ║
║  ● [Partner B]:      ║  ► [Activity 2]:      ║    gain created]     ║  [rationale]         ║  ● [Segment B]:      ║
║    [what provided]   ║    [why critical]     ║                      ║                      ║    [size/descriptor] ║
║  ● [Partner C]:      ╠═══════════════════════╣  For [Segment B]:    ╠══════════════════════╣                      ║
║    [what provided]   ║  KEY RESOURCES        ║  → [problem solved / ║  CHANNELS            ║                      ║
║                      ║                       ║    gain created]     ║                      ║                      ║
║                      ║  What we must have:   ║                      ║  Awareness:          ║                      ║
║                      ║  ○ [Resource]:        ║                      ║  → [how discovered]  ║                      ║
║                      ║    [why critical]     ║                      ║  Purchase:           ║                      ║
║                      ║  ○ [Resource]:        ║                      ║  → [how they buy]    ║                      ║
║                      ║    [why critical]     ║                      ║  Delivery:           ║                      ║
║                      ║  ○ [Resource]:        ║                      ║  → [how value rcvd]  ║                      ║
║                      ║    [why critical]     ║                      ║                      ║                      ║
╠══════════════════════╩═══════════════════════╩══════╦═══════════════╩══════════════════════╩══════════════════════╣
║  COST STRUCTURE                                     ║  REVENUE STREAMS                                           ║
║                                                     ║                                                            ║
║  Fixed:    [major items — salaries, rent, infra]    ║  ● [Stream 1]: [type] — [pricing model] — [~% of rev]     ║
║  Variable: [major items — COGS, transaction fees]   ║  ● [Stream 2]: [type] — [pricing model] — [~% of rev]     ║
║  Model:    [cost-driven / value-driven]             ║  ● [Stream 3]: [type] — [pricing model] — [~% of rev]     ║
╠═════════════════════════════════════════════════════╩════════════════════════════════════════════════════════════╣
║  VIABILITY CHECK                                                                                                 ║
║  ▲ Biggest cost driver: [block]    ● Biggest revenue dependency: [stream]    ○ Key assumption: [assumption]     ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

Read the canvas left-to-right: the left half (Partners → Activities/Resources → Value Props) describes how value is **built**; the right half (Value Props → Relationships/Channels → Segments) describes how value is **delivered**. The bottom row closes the loop — costs flow left, revenue flows right. The Viability Check forces an explicit confrontation between the two.

## Common Mistakes

- Filling in all 9 blocks with generic placeholders and calling it strategy — every entry must be specific enough to be falsifiable or testable.
- Treating Customer Segments as demographics instead of jobs-to-be-done groups — "35-45 year old professionals" is not a segment, "teams that need to onboard contractors in under 24 hours" is.
- Misclassifying Key Activities as Key Resources — activities are things you do (run a marketplace, manufacture, curate content); resources are things you have (data, patents, facilities).
- Ignoring channel economics — listing "social media" as a channel without specifying CAC or conversion rates leaves cost structure incomplete.
- Skipping the viability check — a completed canvas that doesn't ask whether revenue exceeds costs at realistic volume is decoration, not strategy.
