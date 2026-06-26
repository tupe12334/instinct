---
name: inversion
description: "Solve forward problems by thinking backward: instead of 'how to succeed', ask 'how to fail' then avoid it."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [inversion, mental-model, problem-solving, strategy, failure, charlie-munger]
    related_skills: [first-principles, pre-mortem, second-order-thinking]
---

# Inversion

## Overview

Inversion is a mental model popularized by Charlie Munger and rooted in the mathematics of Jakob Jacobi: instead of asking "how do I achieve X?" ask "what would guarantee I never achieve X?" then systematically avoid those things. Removing obstacles is often faster than adding effort — the answer to a hard forward problem is frequently obvious once you look at it from the other end.

```
FORWARD THINKING          INVERTED THINKING
─────────────────         ──────────────────────────────────
"How do we build          "How would we guarantee users
 a loyal user base?"   ←  never come back?"
                                 │
                          - Ignore support tickets
                          - Ship confusing UX
                          - Break things without notice
                                 │
                          INVERT the list:
                          → Respond fast, fix UX, communicate changes
```

Inversion does not replace forward planning — it stress-tests it and fills in blind spots that optimism and familiarity hide.

## Core Concepts

### The Inversion Flip
Every goal statement has a mirror. "Maximize customer trust" inverts to "destroy customer trust." The mirrored question is psychologically easier to answer because humans are wired to spot threats and failures more readily than they are to generate novel paths to success.

### Obstacle Removal vs. Goal Pursuit
Two routes to any outcome:
- Add things that produce it (the standard approach).
- Remove things that prevent it (inversion's contribution).

Munger's formulation: "All I want to know is where I'm going to die, so I'll never go there."

### Completeness Check
Inversion is a completeness tool. Apply it after forward brainstorming to catch what you missed — the goal is not to replace positive plans but to find the failures your forward plan silently assumes away.

```
┌───────────────────┬───────────────────────────────────────────┐
│ FORWARD QUESTION  │ INVERTED MIRROR                           │
├───────────────────┼───────────────────────────────────────────┤
│ How do we grow    │ How would we reliably kill revenue?        │
│ revenue?          │                                           │
├───────────────────┼───────────────────────────────────────────┤
│ How do we ship    │ How would we guarantee this launch fails?  │
│ this on time?     │                                           │
├───────────────────┼───────────────────────────────────────────┤
│ How do we build   │ What would make top performers leave       │
│ a great team?     │ within six months?                        │
├───────────────────┼───────────────────────────────────────────┤
│ How do we make    │ What would make this decision obviously    │
│ the right call?   │ the wrong one in hindsight?               │
└───────────────────┴───────────────────────────────────────────┘
```

## How to Apply

### Step 1 — State the goal precisely
Write your forward goal in one sentence. Vague goals produce vague inversions. "Increase user retention" is usable. "Do better" is not.

### Step 2 — Invert the goal
Rewrite the goal as its opposite: "What actions, conditions, or decisions would guarantee we fail at this?" Commit to the negative framing — do not hedge with "might."

### Step 3 — Brainstorm failure modes
Generate as many specific answers to the inverted question as possible. Be concrete. "Ignore user feedback" is useful. "Have bad culture" is not. Aim for at least 10 items; the obvious ones come first, the dangerous ones come later.

### Step 4 — Invert the failure list
Flip each failure mode back into a positive action or constraint. Each item now tells you something to do, avoid, or put a guardrail around.

### Step 5 — Merge with your forward plan
Overlay the inverted list on your existing plan. Items already covered are validation. Items not covered are gaps. Gaps are the output — treat each one as a required addition or explicit accepted risk.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  INVERSION ANALYSIS: [Goal or decision being examined]            Date: [date]          ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                          ║
║  ┌──────────────────────────────────────┐  ←flip→  ┌──────────────────────────────────┐ ║
║  │  ► FORWARD GOAL                      │          │  ◄ INVERTED QUESTION             │ ║
║  │                                      │          │                                  │ ║
║  │  [One-sentence statement of what     │          │  "What would guarantee           │ ║
║  │   success looks like]                │          │   [opposite of goal]?"           │ ║
║  └──────────────────────────────────────┘          └──────────────────────────────────┘ ║
║                                                                    │                     ║
║                                                                    ▼                     ║
║  ┌──────────────────────────────────────────────────────────────────────────────────┐   ║
║  │  ▼ FAILURE MODES  (be specific — minimum 10; the dangerous ones live at 8–15)    │   ║
║  ├──────────────────────────────────────────────────────────────────────────────────┤   ║
║  │   1. [Concrete action or condition that guarantees failure]                       │   ║
║  │   2. [Concrete action or condition that guarantees failure]                       │   ║
║  │   3. [Concrete action or condition that guarantees failure]                       │   ║
║  │   4. [...]                                                                        │   ║
║  │   5. [...]                                                                        │   ║
║  │   6–10+  ← keep pushing past the obvious                                         │   ║
║  └──────────────────────────────────────────────────────────────────────────────────┘   ║
║                                           │                                              ║
║                         ┌─────────────────┘  FLIP EACH ITEM                             ║
║                         ▼                                                                ║
║  ┌────────────────────────────────────────┬─────────────────────────────────────────┐   ║
║  │  → INVERTED ACTIONS                    │                                         │   ║
║  ├────────────────────────────────────────┼─────────────────────────────────────────┤   ║
║  │  Failure Mode                          │  Positive Action / Constraint           │   ║
║  ├────────────────────────────────────────┼─────────────────────────────────────────┤   ║
║  │  [failure mode 1]                      │  → [positive action or constraint]      │   ║
║  │  [failure mode 2]                      │  → [positive action or constraint]      │   ║
║  │  [failure mode 3]                      │  → [positive action or constraint]      │   ║
║  └────────────────────────────────────────┴─────────────────────────────────────────┘   ║
║                                           │                                              ║
║                                           ▼                                              ║
║  ┌────────────────────────────────────────┬─────────────────────────────────────────┐   ║
║  │  ● COVERED BY CURRENT PLAN             │  ○ GAPS FOUND  ◄── these are the output │   ║
║  ├────────────────────────────────────────┼─────────────────────────────────────────┤   ║
║  │  ● [item already addressed]            │  ○ [item NOT addressed]                 │   ║
║  │  ● [item already addressed]            │  ○ [item NOT addressed]                 │   ║
║  │  ● [item already addressed]            │  ○ [item NOT addressed]                 │   ║
║  └────────────────────────────────────────┴─────────────────────────────────────────┘   ║
║                                           │                                              ║
║                                           ▼                                              ║
║  ┌──────────────────────────────────────────────────────────────────────────────────┐   ║
║  │  ► DECISIONS / ADDITIONS  (one line per gap — plan change or accepted risk)       │   ║
║  ├──────────────────────────────────────────────────────────────────────────────────┤   ║
║  │  ▸ [Gap 1]  →  [specific plan change or accepted risk]                            │   ║
║  │  ▸ [Gap 2]  →  [specific plan change or accepted risk]                            │   ║
║  └──────────────────────────────────────────────────────────────────────────────────┘   ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
```

Read top-to-bottom: state your forward goal, flip it to an inverted question, brainstorm failure modes until the list feels uncomfortable, invert each mode into a positive action, then use the gap analysis split to distinguish what your current plan already covers (left, ●) from what it silently ignores (right, ○). The right column is the deliverable — every ○ item becomes a decision or an explicitly accepted risk in the final block.

## Common Mistakes

- **Inverting to platitudes.** "Don't ignore customers" is not actionable. Push for specifics: "Don't take more than 48 hours to respond to tier-1 support tickets" — that is something you can actually measure and violate.
- **Stopping at the obvious.** The first five failure modes are always the ones everyone already knows. The dangerous failures live at item 8–15. Keep going past the point of comfort.
- **Treating inversion as standalone.** Inversion alone produces a list of things to avoid but no positive direction. It must be paired with a forward plan — its job is to find gaps in that plan, not replace it.
- **Confusing inversion with pessimism.** The goal is not to conclude the project is doomed; it is to find blind spots and remove them. Stop when you have actionable gaps, not when you have maximum anxiety.
- **One-and-done application.** Inversion is cheap enough to run in 20 minutes. Re-run it at every major scope change, pivot, or decision point — the failure modes at month six are not the same as at kickoff.
