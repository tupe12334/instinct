---
name: mece
description: "Structure any analysis or communication so items are Mutually Exclusive and Collectively Exhaustive — no gaps, no overlaps."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [mece, structure, consulting, analysis, logic, communication]
    related_skills: [pyramid-principle, scqa, swot]
---

# MECE (Mutually Exclusive, Collectively Exhaustive)

## Overview

MECE is a structuring principle from McKinsey used to break a problem or topic into categories that do not overlap (mutually exclusive) and together cover every possibility (collectively exhaustive). Apply it to issue trees, slide structures, research questions, and team responsibilities.

```
Topic: "Why are sales falling?"

BAD (overlaps + gaps)          GOOD (MECE)
┌──────────────────┐           ┌──────────────────────┐
│ Marketing issues │           │ Volume (fewer deals) │
│ Bad marketing    │  ← overlap│ Price (lower ASP)    │← no overlap
│ Low pipeline     │           │ Mix (cheaper SKUs)   │
│ Economy          │  ← gap:   └──────────────────────┘
│                  │  product? Revenue = Volume × Price × Mix
└──────────────────┘           covers all levers — no gaps
```

## Core Concepts

### Mutually Exclusive
Each item belongs to exactly one bucket. No item can logically fit in two categories at the same time. If two items can both claim the same fact, they overlap.

### Collectively Exhaustive
The full set of items covers every possible case. No valid instance of the topic is left uncategorized. Ask: "Is there any scenario that falls outside all my buckets?" If yes — you have a gap.

### Issue Tree
The main tool for applying MECE: a hierarchical breakdown where every level is MECE relative to its parent. Each node splits into children that are mutually exclusive and collectively exhaustive of that node.

```
Root question
├── Branch A (MECE siblings at level 1)
│   ├── A1 (MECE siblings at level 2)
│   └── A2
├── Branch B
│   ├── B1
│   └── B2
└── Branch C
```

## How to Apply

### Step 1 — State the root question precisely
Write the single question your structure must answer. Vague roots produce vague trees. "What should we do about revenue?" is weak; "Why did Q3 revenue miss forecast by 15%?" is sharp.

### Step 2 — Choose a splitting logic
Pick one consistent dimension to split on at each level. Common logics:
- **Mathematical identity**: Revenue = Volume × Price × Mix
- **Process/timeline**: Discover → Evaluate → Purchase → Retain
- **Organizational**: By business unit, geography, or customer segment
- **Causal**: Internal vs. External; Supply vs. Demand

Mixing split logics at the same level is the most common source of overlaps.

### Step 3 — Enumerate all buckets, then challenge gaps
List every bucket from your chosen split. Then ask: "What real-world scenario does NOT fit into any of these?" Fill gaps before moving on.

### Step 4 — Challenge overlaps
For each pair of sibling buckets, ask: "Can a single real-world item belong to both?" If yes, redefine boundaries or merge/split buckets.

### Step 5 — Recurse down each branch
For branches that still contain unresolved complexity, repeat Steps 2–4 one level deeper. Stop when a branch is concrete enough to be directly investigated or communicated.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  MECE STRUCTURE: [root question or topic]                                            ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║  SPLIT LOGIC:    [dimension used to divide — e.g., "Revenue = Volume × Price × Mix"]║
╚══════════════════════════════════════════════════════════════════════════════════════╝

  LEVEL 1 ISSUE TREE  (every sibling is ME ↔ all siblings together are CE)

                         ┌─────────────────────────────┐
                         │   [root question / topic]   │
                         └──────────┬──────────────────┘
              ┌───────────────┬─────┴──────┬───────────────┐
              ▼               ▼            ▼               ▼
    ┌─────────────────┐ ┌─────────────┐ ┌─────────────┐  ...
    │   [Bucket A]    │ │  [Bucket B] │ │  [Bucket C] │
    │─────────────────│ │─────────────│ │─────────────│
    │ includes:       │ │ includes:   │ │ includes:   │
    │   [scope def.]  │ │  [scope def]│ │  [scope def]│
    │ excludes:       │ │ excludes:   │ │ excludes:   │
    │   [boundary]    │ │  [boundary] │ │  [boundary] │
    └────────┬────────┘ └─────────────┘ └─────────────┘
             │
             │  LEVEL 2 BREAKDOWN  ─── [Bucket A] only (repeat for other branches)
             │
             ├──► [A1] — [definition of A1 scope]
             └──► [A2] — [definition of A2 scope]

┌──────────────────────────────── OVERLAP CHECK ────────────────────────────────────┐
│  Pair        │  Verdict                                                            │
│──────────────┼─────────────────────────────────────────────────────────────────── │
│  A  vs  B    │  ✓ no overlap — [reason why A and B cannot share an item]          │
│  A  vs  C    │  ✓ no overlap — [reason why A and C cannot share an item]          │
│  B  vs  C    │  ✓ no overlap — [reason why B and C cannot share an item]          │
└──────────────┴─────────────────────────────────────────────────────────────────── ┘

┌──────────────────────────────── GAP CHECK ────────────────────────────────────────┐
│  Scenario tested                  │  Lands in bucket                              │
│───────────────────────────────────┼─────────────────────────────────────────────  │
│  [edge case 1]                    │  → [Bucket X]                                 │
│  [edge case 2]                    │  → [Bucket Y]                                 │
│───────────────────────────────────┴─────────────────────────────────────────────  │
│  Conclusion:  ● no gaps identified          ○ gap found → add [Bucket D]          │
└────────────────────────────────────────────────────────────────────────────────── ┘
```

The **issue tree** shows the hierarchy at a glance — each column of boxes is one MECE level, and every branch must be traceable back to the root question. The **overlap** and **gap** tables are your self-audit: fill every row before treating the structure as final.

## Common Mistakes

- **Mixing split dimensions at the same level** — e.g., splitting customers into "enterprise", "SMB", and "unhappy" mixes size with sentiment; pick one axis per level.
- **Treating MECE as exhaustive brainstorming** — MECE is about structure, not generating ideas; you can have a MECE tree with wrong hypotheses.
- **Residual "other" buckets as a crutch** — an "Other" category signals you haven't found the right split logic; use it temporarily, then resolve it.
- **Conflating levels** — mixing level-1 and level-2 items as siblings makes the tree unreadable and hides gaps.
- **Skipping the gap challenge** — most analysts check for overlaps but forget to enumerate scenarios that might fall outside every bucket; gaps are the silent killers of incomplete analyses.
