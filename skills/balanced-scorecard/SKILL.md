---
name: balanced-scorecard
description: "Translate strategy into metrics across Financial, Customer, Internal Process, and Learning & Growth perspectives."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [balanced-scorecard, strategy, metrics, kpi, performance, financial]
    related_skills: [okr, north-star-metric, mckinsey-7s]
---

# Balanced Scorecard

## Overview

The Balanced Scorecard (BSC) translates an organization's vision and strategy into a coherent set of performance measures across four perspectives. It prevents over-optimization on financials alone by forcing explicit measurement of the drivers that produce financial results — customers, processes, and the people and systems behind them.

```
                        VISION & STRATEGY
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
  FINANCIAL              CUSTOMER             INTERNAL PROCESS
  "To succeed            "To achieve          "To satisfy
  financially,           our vision,          customers and
  how should             how should we        shareholders,
  we appear to           appear to our        which processes
  shareholders?"         customers?"          must we excel at?"
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               │
                    LEARNING & GROWTH
                    "To achieve our vision,
                    how will we sustain our
                    ability to change and improve?"
```

## Perspectives

### Financial
Measures whether strategy execution is creating shareholder value. Lagging indicators — they tell you what already happened.
- Revenue growth, profit margin, ROI, EBITDA, cost reduction, cash flow

### Customer
Measures how the organization is perceived by the customers it targets. Links customer outcomes to financial results.
- Net Promoter Score, customer retention rate, market share, customer acquisition cost, satisfaction scores

### Internal Process
Identifies the critical processes where the organization must excel to deliver on customer and financial goals. These are leading indicators.
- Cycle time, defect rate, on-time delivery, throughput, process cost, innovation pipeline size

### Learning & Growth
Measures the organizational infrastructure — people, systems, and culture — that enables the other three perspectives. The root cause layer.
- Employee engagement, skill coverage gaps, training hours, system uptime, knowledge-sharing activity

## How to Apply

### Step 1 — Anchor to strategy
State your 1–3 sentence strategic intent. Every objective and metric you add must link back to this statement. If a metric doesn't connect, cut it.

### Step 2 — Define objectives per perspective
For each of the four perspectives, write 2–4 short strategic objectives (what must be true). Use action phrases: "Grow recurring revenue," "Reduce onboarding friction," "Shorten release cycle." Aim for 8–12 objectives total across all four.

### Step 3 — Select metrics (KPIs) per objective
Assign 1–2 measurable KPIs to each objective. Each KPI needs:
- A **baseline** (current state)
- A **target** (desired state by a specific date)
- A **data source** (who owns it and where it lives)

Avoid proxy metrics that can be gamed (e.g., "number of meetings held" instead of "decision turnaround time").

### Step 4 — Build a strategy map
Draw cause-and-effect arrows between objectives across perspectives. Learning & Growth objectives should feed Internal Process objectives, which feed Customer objectives, which feed Financial objectives. If an objective has no arrows, question whether it belongs.

### Step 5 — Assign owners and review cadence
Each KPI needs one accountable owner. Review the full scorecard monthly; adjust targets quarterly. Do not add new metrics without removing old ones.

## Output Format

```
BALANCED SCORECARD — [Organization / Team] — [Period]
Strategic Intent: [1-2 sentences]

FINANCIAL PERSPECTIVE
┌─────────────────────────┬──────────────────┬──────────┬──────────┬────────────┐
│ Objective               │ KPI              │ Baseline │ Target   │ Owner      │
├─────────────────────────┼──────────────────┼──────────┼──────────┼────────────┤
│ [Grow recurring revenue]│ [ARR growth %]   │ [12%]    │ [25%]    │ [CFO]      │
│ [Reduce cost to serve]  │ [Support cost/user]│[$4.20] │ [$2.80]  │ [COO]      │
└─────────────────────────┴──────────────────┴──────────┴──────────┴────────────┘

CUSTOMER PERSPECTIVE
┌─────────────────────────┬──────────────────┬──────────┬──────────┬────────────┐
│ Objective               │ KPI              │ Baseline │ Target   │ Owner      │
├─────────────────────────┼──────────────────┼──────────┼──────────┼────────────┤
│ [...]                   │ [...]            │ [...]    │ [...]    │ [...]      │
└─────────────────────────┴──────────────────┴──────────┴──────────┴────────────┘

INTERNAL PROCESS PERSPECTIVE
┌─────────────────────────┬──────────────────┬──────────┬──────────┬────────────┐
│ Objective               │ KPI              │ Baseline │ Target   │ Owner      │
├─────────────────────────┼──────────────────┼──────────┼──────────┼────────────┤
│ [...]                   │ [...]            │ [...]    │ [...]    │ [...]      │
└─────────────────────────┴──────────────────┴──────────┴──────────┴────────────┘

LEARNING & GROWTH PERSPECTIVE
┌─────────────────────────┬──────────────────┬──────────┬──────────┬────────────┐
│ Objective               │ KPI              │ Baseline │ Target   │ Owner      │
├─────────────────────────┼──────────────────┼──────────┼──────────┼────────────┤
│ [...]                   │ [...]            │ [...]    │ [...]    │ [...]      │
└─────────────────────────┴──────────────────┴──────────┴──────────┴────────────┘

STRATEGY MAP (cause-and-effect links)
Learning & Growth → Internal Process → Customer → Financial
[Objective A] ──► [Objective C] ──► [Objective E] ──► [Objective G]
[Objective B] ──► [Objective D] ──► [Objective F]
```

## Common Mistakes

- **Too many KPIs.** A scorecard with 40 metrics is a data dump, not a strategy tool. Ruthlessly limit to 1–2 KPIs per objective and 8–12 objectives total. When everything is measured, nothing is managed.
- **No baselines.** Setting a target without recording the current state makes progress unmeasurable and lets teams claim success by moving the goalposts.
- **Treating all four perspectives as equally urgent.** They are not equal in timing — Learning & Growth problems take the longest to fix. If your people and systems are weak, financial targets 90 days out are fiction.
- **Skipping the strategy map.** Without explicit cause-and-effect links, the four perspectives are just four separate dashboards. The power of the BSC is showing how investing in capability today creates customer value tomorrow and financial results next year.
- **Reviewing annually.** Markets shift faster than that. A BSC reviewed only at year-end is decorative. Monthly reviews with quarterly target recalibration keep it actionable.
