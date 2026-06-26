---
name: pareto-analysis
description: "Apply the 80/20 rule: find the 20% of causes that drive 80% of effects to focus effort where it matters most."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [pareto, 80-20, prioritization, analysis, efficiency, impact]
    related_skills: [the-eisenhower-matrix, rice-scoring, five-whys]
---

# Pareto Analysis

## Overview

The Pareto Principle — named after economist Vilfredo Pareto — observes that roughly 80% of effects come from 20% of causes. Pareto Analysis turns this observation into a structured method: quantify contributions, rank them, identify the vital few, and concentrate effort there rather than spreading it thin across the trivial many.

```
Cumulative %
of effect
  100% |                              ···············
   80% |·············                ·
       |             ·              ·
       |              ·            ·
       |               ·          ·
       |                ··      ··
    0% +──────────────────────────────────────────▶
        20%          50%        80%        100%
                   % of causes

        ◀── vital few ──▶◀────── trivial many ──────▶
```

The inflection point — where the cumulative curve bends — marks the boundary between your vital few and the rest.

## Core Concepts

### Causes vs. Effects
A **cause** is any discrete category: a customer segment, a bug type, a product SKU, a failure mode, a cost center. An **effect** is the measurable outcome attributed to each cause: revenue, defect count, churn rate, cost. You must pick one effect metric before starting — mixing metrics distorts the ranking.

### Cumulative Frequency
Each cause's contribution is expressed as a percentage of the total effect, then accumulated in descending order. The cumulative column reveals the crossover point — the fewest causes that explain the most effect.

### Vital Few vs. Trivial Many
The **vital few** are the top causes that together account for ~80% of the effect. The **trivial many** account for the remaining ~20% but are far more numerous. Effort belongs on the vital few; the trivial many rarely justify proportional investment.

### The 80/20 Ratio Is a Guideline
The real split may be 70/30 or 90/10. Do not force the data to hit 80%. Look for the natural inflection in the cumulative curve — that is your signal, not the number 80.

## How to Apply

### Step 1 — Define the problem and the effect metric
State what you are trying to reduce, improve, or understand. Name the single metric that measures the effect: defect count, lost revenue, support tickets, churn events. Avoid composite metrics at this stage — they obscure the ranking.

### Step 2 — Collect and categorize data
List every distinct cause that contributes to the effect. Assign a measured value of the effect to each cause. Use real data — counts, dollars, times — not estimates. If data does not exist, gather a representative sample before proceeding.

### Step 3 — Rank causes from largest to smallest contribution
Sort the cause list in descending order of their individual effect value. Compute each cause's percentage share of the total effect, then compute the running cumulative percentage.

| Cause       | Effect Value | % of Total | Cumulative % |
|-------------|-------------|------------|--------------|
| Cause A     | [largest]   | [##%]      | [##%]        |
| Cause B     | [...]       | [##%]      | [##%]        |
| Cause C     | [...]       | [##%]      | [##%]        |
| ...         | ...         | ...        | ...          |
| Cause N     | [smallest]  | [##%]      | 100%         |

### Step 4 — Identify the vital few
Find the row where cumulative percentage first crosses your threshold (typically 80%). Every cause above that row is a vital few item. Circle or highlight them — these are your targets.

### Step 5 — Act on the vital few
For each vital few cause, define a specific intervention, assign an owner, and set a measurable target. Do not attempt to solve the trivial many simultaneously — diluted effort rarely moves the needle.

### Step 6 — Rerun after intervention
Once changes are in place, repeat the analysis. The distribution shifts. What was trivial may become vital, or a previously hidden cause may emerge. Pareto Analysis is not a one-time snapshot.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                               PARETO ANALYSIS                                        ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║  Problem:        [what problem you are analyzing]                                    ║
║  Effect Metric:  [the single measurable outcome]                                     ║
║  Data Period:    [date range]                      Source: [data source]             ║
╚══════════════════════════════════════════════════════════════════════════════════════╝

 RANKED CAUSES
┌──────┬───────────────────────┬──────────────┬────────────┬──────────────┬──────────────────────────────────┐
│ Rank │ Cause                 │ Effect Value │ % of Total │ Cumulative % │ Contribution Bar                 │
├──────┼───────────────────────┼──────────────┼────────────┼──────────────┼──────────────────────────────────┤
│  1   │ [cause A]             │   [value]    │   [##%]    │    [##%]     │ ████████████████████░░░░░░░░░░░░ │
│  2   │ [cause B]             │   [value]    │   [##%]    │    [##%]     │ ██████████████░░░░░░░░░░░░░░░░░░ │
│  3   │ [cause C]             │   [value]    │   [##%]    │    [##%]     │ █████████░░░░░░░░░░░░░░░░░░░░░░░ │
├ ─ ─ ─┼─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┼─ ─ ─ ─ ─ ─ ─ ─┼─ ─ ─ ─ ─ ─ ─┼──────────────┼──────────────────────────────────┤
│      │  ▲ vital few above    │              │            │  ~80% ◄──── │ ░ = remaining share              │
├ ─ ─ ─┼─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┼─ ─ ─ ─ ─ ─ ─ ─┼─ ─ ─ ─ ─ ─ ─┼──────────────┼──────────────────────────────────┤
│  4   │ [cause D]             │   [value]    │   [##%]    │    [##%]     │ █████░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│  5   │ [cause E]             │   [value]    │   [##%]    │    [##%]     │ ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│  N   │ [cause N]             │   [value]    │   [##%]    │   100%       │ █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
└──────┴───────────────────────┴──────────────┴────────────┴──────────────┴──────────────────────────────────┘

 CUMULATIVE EFFECT CURVE
                                                                        
 100% ┤                                              ·················
  90% ┤                                         ····
  80% ┤· · · · · · · · · · · · · · · ·─ ─ ─ ─ ·    ← inflection point
  70% ┤                            ··
  60% ┤                         ··
  50% ┤                      ··
  40% ┤                   ··
  20% ┤              ····
   0% ┼──────────────────────────────────────────────────────────► Causes (ranked 1→N)
      │◄────── vital few (≈20% of causes) ──────►◄──── trivial many (≈80% of causes) ────►

┌──────────────────────────────────────────────────┐  ┌────────────────────────────────────────────────┐
║  ● VITAL FEW                                     ║  ║  ○ TRIVIAL MANY                                ║
║    causes 1–[N] → [##%] of total effect          ║  ║    causes [N+1]–[M] → [##%] of total effect   ║
╠══════════════════════════════════════════════════╣  ╠════════════════════════════════════════════════╣
│ ► [Cause A]: [value] — [why it ranks here]       │  │   [Cause D]: [value] — [brief note]            │
│ ► [Cause B]: [value] — [why it ranks here]       │  │   [Cause E]: [value] — [brief note]            │
│ ► [Cause C]: [value] — [why it ranks here]       │  │   … (lower-priority; address after vital few)  │
└──────────────────────────────────────────────────┘  └────────────────────────────────────────────────┘

 ACTIONS  (vital few only — do not dilute effort on trivial many)
┌──────────────────────┬──────────────────────────────────────────┬──────────────────┬──────────────────────────┐
│ Cause                │ Intervention                             │ Owner            │ Target                   │
├──────────────────────┼──────────────────────────────────────────┼──────────────────┼──────────────────────────┤
│ [Cause A]            │ [specific action to take]                │ [name / team]    │ [measurable outcome]     │
│ [Cause B]            │ [specific action to take]                │ [name / team]    │ [measurable outcome]     │
│ [Cause C]            │ [specific action to take]                │ [name / team]    │ [measurable outcome]     │
└──────────────────────┴──────────────────────────────────────────┴──────────────────┴──────────────────────────┘

 NEXT REVIEW: [date to rerun analysis after interventions]
```

The ranked table and bar column let you see at a glance how steeply contributions drop off — a sharp drop after the first 2–3 causes signals a high-leverage 80/20 split. The cumulative curve section confirms where the natural inflection point sits, which is the true vital few / trivial many boundary regardless of whether it lands exactly at 80%.

## Common Mistakes

- **Using subjective estimates instead of data.** Ranking causes by gut feel produces a Pareto chart that reflects bias, not reality. If you do not have data, your first action is to instrument and collect it — not to guess.
- **Mixing effect metrics in one analysis.** Ranking some causes by revenue impact and others by frequency makes cumulative percentages meaningless. Pick one metric per analysis; run separate analyses for separate questions.
- **Treating 80% as a hard rule.** If the natural inflection point is at 70% or 90%, use that. Forcing three more causes in or out to hit exactly 80% wastes focus and creates false precision.
- **Fixing symptoms instead of causes.** If "support tickets from feature X" is a vital few item, the action is to fix feature X — not to hire more support staff. Use Five Whys on each vital few cause to find what actually drives it.
- **Running the analysis once and moving on.** Pareto distributions shift as you fix the vital few. Yesterday's trivial cause becomes tomorrow's top issue. Schedule a rerun after every major intervention or on a fixed cadence.
