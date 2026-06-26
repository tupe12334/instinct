---
name: tows-matrix
description: "Generate strategic options by crossing SWOT quadrants: SO, ST, WO, WT strategies."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [tows, swot, strategy, options, strengths, opportunities, threats, weaknesses]
    related_skills: [swot, ansoff-matrix, soar-analysis]
---

# TOWS Matrix

## Overview

TOWS converts a SWOT inventory into concrete strategic options by crossing each internal factor (Strengths, Weaknesses) against each external factor (Opportunities, Threats). Where SWOT diagnoses, TOWS prescribes. Run SWOT first, then use TOWS to turn the raw quadrants into actionable strategy.

```
                  OPPORTUNITIES (O)        THREATS (T)
                ┌────────────────────────┬────────────────────────┐
STRENGTHS (S)   │  SO — Aggressive       │  ST — Defensive        │
                │  Use S to exploit O    │  Use S to counter T    │
                │  (Maxi-Maxi)           │  (Maxi-Mini)           │
                ├────────────────────────┼────────────────────────┤
WEAKNESSES (W)  │  WO — Turnaround       │  WT — Survival         │
                │  Fix W to capture O    │  Cut W, avoid T        │
                │  (Mini-Maxi)           │  (Mini-Mini)           │
                └────────────────────────┴────────────────────────┘
```

## Strategy Quadrant Definitions

### SO — Aggressive (Strengths x Opportunities)
Deploy what you are best at against the most attractive market openings. This is your growth engine. Identify which strengths directly enable which opportunities and design initiatives that pair them explicitly.

### ST — Defensive (Strengths x Threats)
Use existing advantages to blunt or neutralize incoming threats. The goal is not to eliminate the threat — you rarely can — but to ensure it lands harder on competitors than on you.

### WO — Turnaround (Weaknesses x Opportunities)
There are opportunities you cannot capture because a weakness blocks you. The strategy here is to close that gap — through hiring, partnering, acquiring, or process change — in time to exploit the window before it closes.

### WT — Survival (Weaknesses x Threats)
Minimize exposure: reduce or exit activities where a weakness overlaps with a threat. This quadrant produces the most defensive and sometimes painful choices — cutting products, exiting markets, restructuring.

## How to Apply

### Step 1 — Populate your SWOT first
List 3–5 specific items per quadrant. Items must be concrete. "Strong brand" is not useful; "top-3 brand recall in the 25–40 urban segment per Q1 survey" is. Run /swot if you have not done this yet.

### Step 2 — Cross-map Strengths against Opportunities (SO)
For each top-ranked Strength, ask: which Opportunities does this directly enable? Write one strategy per meaningful pair. A strategy must name the specific strength, the specific opportunity, and the concrete action.

### Step 3 — Cross-map Strengths against Threats (ST)
For each top-ranked Strength, ask: which Threats does this help absorb or deflect? Write one defensive initiative per meaningful pair.

### Step 4 — Cross-map Weaknesses against Opportunities (WO)
For each Opportunity that matters, identify which Weakness is the primary blocker. Write one turnaround initiative that addresses the weakness as a precondition to capturing the opportunity. Include how and by when the gap will close.

### Step 5 — Cross-map Weaknesses against Threats (WT)
Identify danger zones where a weakness and a threat compound each other. For each, decide: fix it, hedge it, or exit. Avoid paralysis here — the goal is harm reduction, not perfection.

### Step 6 — Prioritize across all four quadrants
Score each initiative by impact and feasibility. Select 1–2 initiatives per quadrant for immediate action. Assign an owner and a 90-day checkpoint to each. Strategies without owners do not execute.

## Output Format

```
TOWS MATRIX: [subject]
DATE: [date]

SWOT INPUTS (top items per quadrant)
S: [S1], [S2], [S3]
W: [W1], [W2], [W3]
O: [O1], [O2], [O3]
T: [T1], [T2], [T3]

SO — AGGRESSIVE STRATEGIES (use strengths to exploit opportunities)
1. [Strength] x [Opportunity] → [specific initiative] | Owner: [name] | Checkpoint: [date]
2. [Strength] x [Opportunity] → [specific initiative] | Owner: [name] | Checkpoint: [date]

ST — DEFENSIVE STRATEGIES (use strengths to counter threats)
1. [Strength] x [Threat] → [specific initiative] | Owner: [name] | Checkpoint: [date]
2. [Strength] x [Threat] → [specific initiative] | Owner: [name] | Checkpoint: [date]

WO — TURNAROUND STRATEGIES (fix weaknesses to capture opportunities)
1. [Weakness] blocks [Opportunity] → [gap-closing action] | Owner: [name] | Checkpoint: [date]
2. [Weakness] blocks [Opportunity] → [gap-closing action] | Owner: [name] | Checkpoint: [date]

WT — SURVIVAL STRATEGIES (minimize weakness + threat overlap)
1. [Weakness] x [Threat] → [reduce/exit/hedge action] | Owner: [name] | Checkpoint: [date]
2. [Weakness] x [Threat] → [reduce/exit/hedge action] | Owner: [name] | Checkpoint: [date]

PRIORITY INITIATIVES (top 3 across all quadrants)
1. [initiative] — [quadrant] — [rationale for priority]
2. [initiative] — [quadrant] — [rationale for priority]
3. [initiative] — [quadrant] — [rationale for priority]
```

## Common Mistakes

- **Running TOWS without a solid SWOT.** Vague SWOT inputs produce vague strategies. If your SWOT items are generic ("good team", "competitive market"), sharpen them before crossing quadrants — garbage in, garbage out.
- **Producing strategies that cross mismatched pairs.** Not every strength pairs with every opportunity. Force-fitting all combinations creates noise. Only write a strategy when the pairing is genuinely causal — when the strength directly enables the opportunity, or the weakness directly blocks it.
- **Treating all four quadrants as equal priority.** SO strategies are your offense; allocate the most resources there. WT strategies are damage control; do not let them consume the roadmap. Tilt the balance toward the quadrant that matches your current position.
- **Skipping the owner and checkpoint.** TOWS outputs are strategy documents, not analysis documents. Every initiative must have a named owner and a specific date. Without this, the matrix becomes wall decoration within a week.
- **Confusing TOWS with SWOT.** SWOT asks "what is true about us and our environment?" TOWS asks "given those truths, what should we do?" They are sequential, not interchangeable. Citing SWOT outputs as strategy is a category error.
