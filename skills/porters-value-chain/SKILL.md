---
name: porters-value-chain
description: "Identify competitive advantage by auditing primary activities (inbound, ops, outbound, marketing, service) and support activities."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [value-chain, porter, competitive-advantage, operations, strategy, activities]
    related_skills: [porters-five-forces, mckinsey-7s, swot]
---

# Porter's Value Chain

## Overview

Developed by Michael Porter, the Value Chain disaggregates a firm into the discrete activities it performs to design, produce, market, deliver, and support its product. Every activity either adds cost or creates value — competitive advantage emerges when a firm performs activities more cheaply or distinctively than rivals.

```
SUPPORT ACTIVITIES
┌─────────────────────────────────────────────────────────────────┐
│  Firm Infrastructure  (finance, legal, planning, QA)            │
├─────────────────────────────────────────────────────────────────┤
│  Human Resource Management  (recruit, train, incentivize)       │
├─────────────────────────────────────────────────────────────────┤
│  Technology Development  (R&D, process automation, IP)          │
├─────────────────────────────────────────────────────────────────┤
│  Procurement  (supplier contracts, purchasing policies)         │
└──────┬──────────┬──────────┬──────────┬──────────┬─────────────┘
       │          │          │          │          │
  INBOUND    OPERATIONS  OUTBOUND  MARKETING   SERVICE
 LOGISTICS              LOGISTICS   & SALES
       │          │          │          │          │
       └──────────┴──────────┴──────────┴──────────┘
                       PRIMARY ACTIVITIES                ──► MARGIN
```

## Activity Definitions

### Primary Activities

#### 1 — Inbound Logistics
Receiving, storing, and distributing inputs to the production process.
- Examples: supplier relationships, warehousing, inventory management, raw-material handling, just-in-time delivery

#### 2 — Operations
Transforming inputs into the final product or service.
- Examples: manufacturing, assembly, packaging, equipment maintenance, quality control, facility operations

#### 3 — Outbound Logistics
Collecting, storing, and distributing the product to buyers.
- Examples: finished-goods warehousing, order fulfillment, distribution network, delivery scheduling, returns handling

#### 4 — Marketing and Sales
Providing the means for buyers to purchase the product and inducing them to do so.
- Examples: channel selection, advertising, pricing, sales force, promotions, market research

#### 5 — Service
Maintaining or enhancing the product's value after purchase.
- Examples: installation, warranty, repair, customer training, spare parts, helpdesk

### Support Activities

#### Firm Infrastructure
General management, finance, accounting, legal, government affairs, quality management — spans the entire chain.

#### Human Resource Management
Recruiting, training, developing, and compensating all categories of personnel.

#### Technology Development
Know-how, procedures, and technology embedded in every value activity (not just the R&D department).

#### Procurement
Purchasing inputs used across the value chain — raw materials, machinery, office supplies, external services.

## How to Apply

### Step 1 — Define the unit of analysis
Choose a single business unit, product line, or geographic division. Applying the framework to an entire conglomerate produces noise, not insight.

### Step 2 — Map all activities with cost and driver
For each of the nine activities, list the 2–4 sub-activities that matter most. Estimate relative cost share (% of total cost) and the primary cost driver (labor, volume, capital, time).

### Step 3 — Score differentiation potential
Rate each activity: does it currently create a differentiation advantage (D+), parity (D=), or disadvantage (D-) versus the key competitor? Be specific about which competitor.

### Step 4 — Find linkages
Competitive advantage often lives in linkages between activities, not activities in isolation. A superior procurement activity (faster supplier qualification) can directly lower operational cycle time. List every material linkage and its effect on cost or differentiation.

### Step 5 — Identify strategic options
For each activity rated D- or with a high cost share but no offsetting advantage, ask: (a) eliminate or outsource it, (b) invest to reach parity, or (c) redesign the linkage. For D+ activities, ask how to deepen and protect the advantage.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  VALUE CHAIN ANALYSIS  ►  [Company / Business Unit]  vs.  [Primary Competitor]              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝

SUPPORT ACTIVITIES (span all primary activities)
╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  FIRM INFRASTRUCTURE   │ [key finding — finance, legal, planning, QA]                       ║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║  HUMAN RESOURCE MGMT   │ [key finding — recruiting, training, compensation]                 ║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║  TECHNOLOGY DEVELOP.   │ [key finding — R&D, process automation, IP]                        ║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║  PROCUREMENT           │ [key finding — supplier contracts, purchasing policies]            ║
╚══════════════╤═══════════════╤═══════════════╤═══════════════╤═══════════════╤══════════════╝
               │               │               │               │               │
PRIMARY        ▼               ▼               ▼               ▼               ▼
ACTIVITIES
┌──────────────┴──┐  ┌─────────┴───────┐  ┌───┴───────────┐  ┌───┴───────────┐  ┌────┴──────────┐
│ INBOUND         │  │   OPERATIONS    │  │   OUTBOUND    │  │  MARKETING    │  │   SERVICE     │
│ LOGISTICS       │  │                 │  │   LOGISTICS   │  │  & SALES      │  │               │
├─────────────────┤  ├─────────────────┤  ├───────────────┤  ├───────────────┤  ├───────────────┤
│ Cost: [~X%]     │  │ Cost: [~X%]     │  │ Cost: [~X%]   │  │ Cost: [~X%]   │  │ Cost: [~X%]   │
│ Driver:[driver] │  │ Driver:[driver] │  │ Driver:[drv]  │  │ Driver:[drv]  │  │ Driver:[drv]  │
│ Diff:  [D+/=/−] │  │ Diff:  [D+/=/−] │  │ Diff: [D+/=/−]│  │ Diff: [D+/=/−]│  │ Diff: [D+/=/−]│
├─────────────────┤  ├─────────────────┤  ├───────────────┤  ├───────────────┤  ├───────────────┤
│ ● [activity 1]  │  │ ● [activity 1]  │  │ ● [activity 1]│  │ ● [activity 1]│  │ ● [activity 1]│
│ ● [activity 2]  │  │ ● [activity 2]  │  │ ● [activity 2]│  │ ● [activity 2]│  │ ● [activity 2]│
├─────────────────┤  ├─────────────────┤  ├───────────────┤  ├───────────────┤  ├───────────────┤
│ ▸ [finding]     │  │ ▸ [finding]     │  │ ▸ [finding]   │  │ ▸ [finding]   │  │ ▸ [finding]   │
└─────────────────┘  └─────────────────┘  └───────────────┘  └───────────────┘  └───────────────┘
         │                   │                    │                   │                  │
         └───────────────────┴────────────────────┴───────────────────┴──────────────────┘
                                                                                          ══► MARGIN

┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│  KEY LINKAGES                                                                                │
│  ┌──────────────────┐        ┌──────────────────┐       effect on cost / differentiation    │
│  │  [Activity A]    │ ──────► │  [Activity B]    │  →  [effect]                             │
│  └──────────────────┘        └──────────────────┘                                           │
│  ┌──────────────────┐        ┌──────────────────┐                                           │
│  │  [Activity C]    │ ──────► │  [Activity D]    │  →  [effect]                             │
│  └──────────────────┘        └──────────────────┘                                           │
└──────────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│  STRATEGIC OPTIONS                                                                           │
│  1. ► [action]  —  [activity]  —  [expected impact]                                         │
│  2. ► [action]  —  [activity]  —  [expected impact]                                         │
│  3. ► [action]  —  [activity]  —  [expected impact]                                         │
└──────────────────────────────────────────────────────────────────────────────────────────────┘

● COMPETITIVE ADVANTAGE SOURCE:  [cost leadership / differentiation / focus — 1 sentence]
```

Each column in the primary activities row represents one link in the value chain flowing left to right toward the margin. The D+/D=/D− rating in each column shows your differentiation position versus the named competitor; cost share and driver tell you where to focus investment or cost-reduction effort first.

## Common Mistakes

- Treating support activities as overhead to cut — HRM and Technology Development are often the source of durable advantage; gutting them destroys value slowly and silently
- Listing departments instead of activities — "Marketing Department" is not an activity; "channel partner negotiation" is; stay at the activity level
- Skipping cost share estimates — without rough cost weights you cannot tell which D- rating actually hurts margins; a D- activity at 2% cost share rarely matters
- Ignoring the value system — your value chain connects to supplier and channel value chains; a bottleneck upstream (supplier lead times) can neutralize an internal advantage in operations
- Comparing against an average competitor — always name a specific rival; a generic "industry average" benchmark obscures actionable gaps and prevents honest rating
