---
name: pdca
description: "Drive continuous improvement through iterative Plan → Do → Check → Act cycles."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [pdca, continuous-improvement, lean, cycle, plan, do, check, act]
    related_skills: [five-whys, fishbone-diagram, double-diamond]
---

# PDCA Cycle (Plan–Do–Check–Act)

## Overview

PDCA is a four-phase iterative loop for solving problems and improving processes. Each cycle produces a tested change; repeat until the target condition is reached. Also called the Deming Wheel or Shewhart Cycle.

```
          ┌─────────────────────────────┐
          │                             │
     ┌────▼────┐               ┌────────┴────┐
     │  PLAN   │               │     ACT     │
     │ Define  │               │ Standardize │
     │ target  │               │  or re-plan │
     └────┬────┘               └────────▲────┘
          │                             │
     ┌────▼────┐               ┌────────┴────┐
     │   DO    │──────────────►│    CHECK    │
     │ Execute │               │  Measure &  │
     │ on small│               │   compare   │
     │  scale  │               └─────────────┘
     └─────────┘
```

PDCA is most effective on *measurable, repeatable* processes — defect rates, cycle times, conversion rates, error counts.

## Phase Definitions

### Plan — Identify the gap and design a countermeasure
- State the problem in measurable terms: current value vs. target value.
- Root-cause analysis before jumping to solutions (use Five Whys or fishbone if needed).
- Define one hypothesis: "If we change X, we expect Y to improve by Z."
- Specify success criteria, measurement method, and timeline up front.

### Do — Execute the change at small scale
- Run a controlled pilot or time-boxed experiment — not a full rollout.
- Keep scope small enough to be reversible in hours or days.
- Document what was done, who did it, and any deviations from the plan.
- Collect raw data during execution — do not rely on memory after the fact.

### Check — Compare results to the prediction
- Measure the same metric(s) defined in Plan.
- Did results match the hypothesis? If not, why?
- Separate signal from noise: was the sample size or duration enough to draw a conclusion?
- List side effects — unintended changes to adjacent metrics.

### Act — Decide what to do with what you learned
- **If the change worked**: standardize it (update process docs, train team, embed in checklists), then set a new, harder target and start the next cycle.
- **If the change failed**: discard or revise, carry forward the learning, re-enter Plan with better information.
- Never let a "failed" cycle go to waste — document the finding explicitly.

## How to Apply

### Step 1 — Frame the problem
Write one sentence: "[Metric] is currently [X]. We need it to be [Y] by [date]. Root cause hypothesis: [Z]."

### Step 2 — Design the experiment (Plan)
Choose one countermeasure. Define: what changes, who owns it, what data will be collected, and what result would count as success or failure.

### Step 3 — Run a bounded pilot (Do)
Limit scope — one team, one week, one channel. Record everything that happens.

### Step 4 — Analyze results (Check)
Compare actual vs. predicted outcome. Plot the data. State clearly: "Hypothesis confirmed / refuted / inconclusive because..."

### Step 5 — Standardize or pivot (Act)
Write a one-sentence decision. Update standard operating procedures if the change is adopted. Start the next PDCA cycle immediately with a new target or revised hypothesis.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  PDCA CYCLE ▸ [initiative or problem name]          Date: [YYYY-MM-DD]   Cycle #: [N]      ║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                              ║
║  ┌────────────────────────────────────────────────┐  ┌──────────────────────────────────┐   ║
║  │  ① PLAN                                       │  │                       ④ ACT     │   ║
║  ├────────────────────────────────────────────────┤  ├──────────────────────────────────┤   ║
║  │  Problem:    [current state vs. target,        │  │  Decision:  [Standardize /       │   ║
║  │              metric + gap]                     │  │              Revise / Abandon]   │   ║
║  │  Root cause: [hypothesis from analysis]        │  │  If std'd:  [where documented]   │   ║
║  │  Counter:    [specific change to test]         │  │  Next tgt:  [new/refined target] │   ║
║  │  Success:    [metric ≥ X within Y days]        │  │  Key learn: [one sentence]       │   ║
║  │  Owner:      [name / role]                     │  │                                  │   ║
║  └────────────────────────┬───────────────────────┘  └────────────────▲─────────────────┘   ║
║                           │ ▼ PLAN → DO                  CHECK → ACT ▲ │                    ║
║  ┌────────────────────────▼───────────────────────┐  ┌────────────────┴─────────────────┐   ║
║  │  ② DO                                         │  │                     ③ CHECK     │   ║
║  ├────────────────────────────────────────────────┤  ├──────────────────────────────────┤   ║
║  │  Scope:      [team / env / duration]           │  │  Result:    [metric after chg]   │   ║
║  │  Executed:   [actual steps taken]              │──►  Predicted: [expected value]     │   ║
║  │  Deviations: [none / description]              │  │  Verdict:   [Confirmed /         │   ║
║  │  Data:       [raw numbers / source]            │  │              Refuted /           │   ║
║  │                                                │  │              Inconclusive]       │   ║
║  │                                                │  │  Reason:    [brief explanation]  │   ║
║  │                                                │  │  Side FX:   [list or "none"]     │   ║
║  └────────────────────────────────────────────────┘  └──────────────────────────────────┘   ║
║                                                                                              ║
║  ● ACT → PLAN: if standardized, set a harder target and start the next cycle;               ║
║    if failed or inconclusive, carry the learning forward and re-enter Plan.                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝
```

Each quadrant maps to one phase: PLAN defines the hypothesis and success bar, DO runs the bounded pilot, CHECK measures actual vs. predicted outcome, and ACT decides whether to embed the change or revise. The `──►` connector between DO and CHECK shows the data hand-off; the vertical arrows on the left and right flanks show the top-to-bottom and bottom-to-top phase transitions within the cycle.

## Common Mistakes

- **Skipping the prediction in Plan**: without a stated hypothesis, Check becomes meaningless — you can't evaluate results if you never declared what "good" looks like.
- **Piloting at full scale**: running the change everywhere before checking removes the ability to compare and makes rollback expensive.
- **Treating inconclusive as failure**: a weak signal means the sample was too small or the change too subtle — it is information, not a verdict.
- **Declaring victory after one cycle**: a single successful cycle often reflects favorable conditions, not a stable improvement; run 2–3 cycles before standardizing.
- **Abandoning the Act phase**: teams move on to the next problem without updating SOPs or training anyone — the improvement exists only in their heads and erodes within weeks.
