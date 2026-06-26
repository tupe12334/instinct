---
name: fishbone-diagram
description: "Map causes of a problem across categories (People, Process, Technology, Environment, etc.) to find root drivers."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [fishbone, ishikawa, cause-effect, root-cause, analysis, problem-solving]
    related_skills: [five-whys, pdca, pre-mortem]
---

# Fishbone Diagram (Ishikawa / Cause-and-Effect)

## Overview

The fishbone diagram visualizes the causes of a problem by grouping them into categories — the "bones" — radiating from the problem statement — the "head." It forces breadth-first thinking before diving deep, so teams stop anchoring on the first cause that comes to mind. Originally developed by Kaoru Ishikawa for manufacturing quality control; now used across software, ops, healthcare, and strategy.

```
       People          Process         Technology
         \               |               /
          \              |              /
           \             |             /
            \            |            /
 ────────────\───────────|───────────/────────► [PROBLEM]
            /            |            \
           /             |             \
          /              |              \
         /               |               \
      Environment     Materials        Management
```

Each branch holds the direct causes in that category; sub-branches hold the causes of those causes (one level of "why" per branch is usually enough — use Five Whys to go deeper on a single branch).

## Category Definitions

The standard 6M categories for manufacturing; swap freely for your context:

| Category | Covers | Service/Software Alternative |
|----------|--------|------------------------------|
| **People** | Skills, training, behavior, communication | Team, Users |
| **Process** | Steps, procedures, workflows, handoffs | Workflow, Method |
| **Technology** | Tools, systems, machines, software | Systems, Tools |
| **Environment** | Physical conditions, culture, org structure | Culture, Context |
| **Materials** | Inputs, data, third-party content | Data, Dependencies |
| **Management** | Policies, priorities, measurements, incentives | Policy, Metrics |

You do not need all six. Use the categories that apply; invent new ones when none fit (e.g., "Regulation", "Customer").

## How to Apply

### Step 1 — Write the problem statement precisely
Put the effect in the "head." Be specific: not "bad performance" but "API p99 latency exceeds 2 s under peak load on weekdays." Vague problems produce vague causes.

### Step 2 — Select categories
Choose 4–6 categories that are plausible contributors. Eliminate any that obviously cannot apply — blank branches waste facilitation time.

### Step 3 — Brainstorm causes per category
For each category, ask: "How could [category] cause or contribute to [problem]?" Generate 3–6 causes per branch. Do not filter yet — capture everything. Use sticky notes or a whiteboard column per category.

### Step 4 — Add sub-causes
For each cause, ask "what causes this?" once. A single level of sub-branches is usually sufficient; if you need more depth, switch to a Five Whys on that specific cause.

### Step 5 — Vote and prioritize
Have the team dot-vote (2–3 votes each) on the causes most likely to be root drivers. Circle the top 3–5. These become candidates for verification.

### Step 6 — Verify, do not assume
The diagram generates hypotheses, not conclusions. Test the top candidates with data, logs, or interviews before acting. Mark each prioritized cause as Confirmed, Likely, or Unverified.

## Output Format

```
FISHBONE DIAGRAM
Problem: [precise problem statement — measurable if possible]
Date: [date] | Team: [participants]

PEOPLE
  - [cause 1]
      → [sub-cause if known]
  - [cause 2]

PROCESS
  - [cause 1]
      → [sub-cause if known]
  - [cause 2]

TECHNOLOGY
  - [cause 1]
  - [cause 2]

ENVIRONMENT
  - [cause 1]
  - [cause 2]

MATERIALS / DATA
  - [cause 1]
  - [cause 2]

MANAGEMENT / POLICY
  - [cause 1]
  - [cause 2]

PRIORITIZED ROOT CAUSE CANDIDATES (dot-vote results)
1. [cause] — Category: [X] — Status: [Confirmed / Likely / Unverified]
2. [cause] — Category: [X] — Status: [Confirmed / Likely / Unverified]
3. [cause] — Category: [X] — Status: [Confirmed / Likely / Unverified]

NEXT ACTIONS
- Verify [candidate 1] by: [data source / experiment / interview]
- Verify [candidate 2] by: [data source / experiment / interview]
```

## Common Mistakes

- **Vague problem statement**: "Users are unhappy" generates useless branches. If you cannot measure the problem, sharpen it before starting.
- **Causes written as solutions**: "No monitoring in place" is actually "Lack of monitoring" — keep causes as conditions, not action items.
- **Skipping verification**: The diagram is a hypothesis map. Teams that act on unverified causes fix the wrong thing and lose trust in the method.
- **Using the wrong categories**: Forcing every problem into the 6M manufacturing labels when the domain is software or strategy produces artificial groupings. Rename categories to match reality.
- **Solo use**: The fishbone's main value is surfacing blind spots across functions. Running it alone defeats the purpose — include people from at least two different roles or perspectives.
