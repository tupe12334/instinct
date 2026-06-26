---
name: lean-canvas
description: "One-page business model for startups: Problem, Solution, UVP, Unfair Advantage, Channels, Segments, Revenue Streams, Cost Structure, Key Metrics."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [lean-canvas, startup, business-model, mvp, problem-solution]
    related_skills: [business-model-canvas, value-proposition-canvas, jobs-to-be-done]
---

# Lean Canvas

## Overview

A one-page business model designed for early-stage startups by Ash Maurya (adapted from the Business Model Canvas). It replaces operational blocks (Key Partners, Key Resources, Key Activities, Customer Relationships) with startup-critical blocks (Problem, Solution, Key Metrics, Unfair Advantage). The goal is to capture your riskiest assumptions on a single sheet so you can invalidate them fast.

```
┌──────────────┬──────────────┬───────────────┬──────────────┬──────────────┐
│  PROBLEM     │  SOLUTION    │     UNIQUE    │   UNFAIR     │  CUSTOMER    │
│              │              │     VALUE     │  ADVANTAGE   │  SEGMENTS    │
│  [top 3]     │  [top 3]     │  PROPOSITION  │              │              │
├──────────────┼──────────────┤               ├──────────────┼──────────────┤
│  EXISTING    │  KEY         │               │   CHANNELS   │    EARLY     │
│  ALTERNATIVES│  METRICS     │               │              │   ADOPTERS   │
├──────────────┴──────────────┴───────────────┴──────────────┴──────────────┤
│          COST STRUCTURE                     │       REVENUE STREAMS        │
└─────────────────────────────────────────────┴──────────────────────────────┘
```

## The 9 Blocks

### 1. Customer Segments
Who has the problem you are solving? Name a specific group, not a broad market. Identify the **Early Adopters** — the subset who feel the pain most acutely today and will tolerate an imperfect solution to get relief.

### 2. Problem
List the top 3 problems your customer segment faces. Under each problem, note the **Existing Alternatives** — what customers use today (spreadsheets, manual workarounds, a competitor, doing nothing). If there are no existing alternatives, the problem may not be urgent enough to pay to solve.

### 3. Unique Value Proposition (UVP)
A single, clear sentence that explains why your product is different and worth paying attention to. Write it for your early adopters, not the press. A UVP is not a tagline — it names the outcome the customer gets and, if possible, the timeframe or mechanism. Example: "Close your books in one hour, not one week."

### 4. Solution
The top 3 features or capabilities that address the top 3 problems. Keep this brief at the start — this block should be your smallest. Solutions are hypotheses until customers pay for them.

### 5. Channels
How you acquire and deliver to customers: SEO, paid ads, direct sales, partnerships, content, community. Distinguish between **inbound** (customers find you) and **outbound** (you find customers). Note which channels are proven vs. untested.

### 6. Revenue Streams
How you charge and how much. Include pricing model (subscription, per-seat, usage-based, one-time, freemium). Estimate your target **Average Revenue Per User (ARPU)** and note the price sensitivity of your early adopters.

### 7. Cost Structure
The costs to build and run the business: salaries, infrastructure, marketing spend, tools. Separate **fixed** (exist regardless of users) from **variable** (scale with usage or customers). Identify your burn rate and the point at which revenue covers costs.

### 8. Key Metrics
The 1-3 numbers that tell you whether the business is working. Use the AARRR funnel as a reference (Acquisition, Activation, Retention, Revenue, Referral) but pick the metric that matters most for your current stage. Vanity metrics (page views, registered users) are not key metrics.

### 9. Unfair Advantage
What you have that cannot be easily copied or bought: proprietary data, network effects, a domain expert co-founder, exclusive contracts, community trust. If your answer is "passion" or "hard work," leave this blank until you discover a real advantage.

## How to Apply

### Step 1 — Pick one customer segment and one problem space
Do not try to cover multiple segments on one canvas. If you have two distinct customer types, create two canvases and compare them. Start with the segment that feels most urgent and reachable.

### Step 2 — Fill Problem and Existing Alternatives first
Write the top 3 problems from the customer's perspective, using their words if possible. Then list what they do today to cope. If you cannot name existing alternatives, you have not talked to enough customers.

### Step 3 — Draft your UVP and Solution
Write the UVP in one sentence targeting early adopters. Then match each problem to one solution feature. Resist the urge to list more than 3 features — the canvas forces you to prioritize.

### Step 4 — Fill Channels, Revenue, and Costs
Be specific: name the actual channel (e.g., "cold email to VP of Engineering at 50–200 person SaaS companies"), the price point, and your top 3 cost line items. Vague entries here produce a false sense of completeness.

### Step 5 — Identify Key Metrics and your Unfair Advantage
Choose one metric per stage. At pre-product: number of problem interviews completed. At MVP: activation rate. At growth: retention and ARPU. For Unfair Advantage, be honest — it is fine to leave it blank early and fill it as you learn.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════╗
║  LEAN CANVAS  ►  [Product / Venture Name]                  Date: [YYYY-MM-DD]                   ║
║                                                            Stage: [Idea/Pre-revenue/Revenue/Growth]║
╠═══════════════════╦═══════════════════╦═══════════════════════╦═══════════════════╦══════════════╣
║  PROBLEM          ║  SOLUTION         ║   UNIQUE VALUE        ║  UNFAIR           ║  CUSTOMER    ║
║───────────────────║───────────────────║   PROPOSITION         ║  ADVANTAGE        ║  SEGMENTS    ║
║ 1. [Problem 1]    ║ 1. [Feature for   ║───────────────────────║───────────────────║──────────────║
║                   ║    Problem 1]     ║ [One sentence:        ║ [Hard-to-copy     ║ [Specific    ║
║ 2. [Problem 2]    ║ 2. [Feature for   ║  outcome +            ║  asset — data,    ║  group with  ║
║                   ║    Problem 2]     ║  differentiator,      ║  network effect,  ║  the pain]   ║
║ 3. [Problem 3]    ║ 3. [Feature for   ║  written for early    ║  exclusive deal,  ║              ║
║                   ║    Problem 3]     ║  adopters]            ║  or TBD]          ║  EARLY       ║
╠═══════════════════╬═══════════════════║                       ╠═══════════════════║  ADOPTERS    ║
║  EXISTING         ║  KEY METRICS      ║                       ║  CHANNELS         ║──────────────║
║  ALTERNATIVES     ║───────────────────║                       ║───────────────────║ [Subset with ║
║───────────────────║ Stage metric:     ║                       ║ Inbound:          ║  most acute  ║
║ 1. [Alt for P1]   ║  [metric]         ║                       ║  [channel]        ║  pain,       ║
║ 2. [Alt for P2]   ║  now:[v] → [tgt]  ║                       ║  [proven/untested]║  reachable   ║
║ 3. [Alt for P3]   ║ North Star:       ║                       ║ Outbound:         ║  now]        ║
║                   ║  [metric]         ║                       ║  [channel]        ║              ║
╠═══════════════════╩═══════════════════╩═══════════════════════╩═══════════════════╩══════════════╣
║  COST STRUCTURE                                 ║  REVENUE STREAMS                              ║
║─────────────────────────────────────────────────║───────────────────────────────────────────────║
║  Fixed:    [item 1: $X/mo]  [item 2: $X/mo]     ║  Model:      [subscription / usage / one-time]║
║  Variable: [item: $X/unit]                      ║  Price:      [$X per mo / per unit]           ║
║  Burn:     [$X/month]   Runway: [X months]      ║  Target ARPU: [$X]                            ║
╚═════════════════════════════════════════════════╩═══════════════════════════════════════════════╝

  RISKIEST ASSUMPTIONS  ►  top 3 to invalidate next
  ┌─────┬──────────────────────────────────────────────┬─────────────────────────────────────────┐
  │  #  │  Assumption                                  │  Test (validate in < 2 weeks)           │
  ├─────┼──────────────────────────────────────────────┼─────────────────────────────────────────┤
  │  1  │  [Assumption]                                │  [How to validate]                      │
  │  2  │  [Assumption]                                │  [How to validate]                      │
  │  3  │  [Assumption]                                │  [How to validate]                      │
  └─────┴──────────────────────────────────────────────┴─────────────────────────────────────────┘
```

The top canvas grid mirrors the physical Lean Canvas layout: Problem and Solution occupy the left two columns, the Unique Value Proposition spans the full height of the centre column, Unfair Advantage and Channels share the fourth column (top/bottom), and Customer Segments with Early Adopters anchor the right column. Cost Structure and Revenue Streams run across the full bottom strip. Fill the Riskiest Assumptions table with the three beliefs that, if wrong, would kill the business fastest.

## Common Mistakes

- **Writing the Solution before validating the Problem.** The canvas is built to be filled left-to-right starting from Customer Segments and Problem. Founders who start with Solution build a product that answers a question no one is asking.
- **Confusing UVP with a mission statement.** "We make productivity delightful" is not a UVP. A UVP names the specific outcome for a specific person. If it could apply to any product in your category, rewrite it.
- **Listing revenue streams without a price.** "SaaS subscription" is not a revenue model until you write a number next to it. Price is a hypothesis — state it explicitly so you can test whether customers agree.
- **Treating Key Metrics as a vanity dashboard.** Signups, downloads, and page views are outputs, not evidence of a working business. The metric must connect directly to revenue or retention to be meaningful.
- **Skipping Existing Alternatives.** If you cannot name what customers use today to solve this problem, you do not understand the competitive landscape or the urgency of the pain. No existing alternative usually means no existing market awareness — a much harder sell than displacing a known solution.
