---
name: first-principles
description: "Break problems down to fundamental truths and rebuild solutions from scratch — stripping away assumptions."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [first-principles, reasoning, mental-model, innovation, problem-solving]
    related_skills: [inversion, second-order-thinking, five-whys]
---

# First-Principles Thinking

## Overview

First-principles thinking is a reasoning method that decomposes a problem to its most basic, verified truths and reconstructs a solution from there — rather than reasoning by analogy from what others have done. It was practiced by Aristotle and is closely associated with how physicists approach novel problems.

```
Conventional thinking:        First-principles thinking:
  "Others do X, so we do X"     Problem
         ↓                         ↓
    Analogy / copy            Ask: what is fundamentally true here?
         ↓                         ↓
   Incremental tweak          Strip assumptions → bedrock facts
                                   ↓
                              Rebuild solution from facts up
                                   ↓
                              Novel or superior solution
```

The key discipline is distinguishing what is *actually* true from what is *conventionally* assumed.

## Core Concepts

### Assumptions vs. Fundamental Truths
An assumption is any constraint accepted without verification: cost, time, materials, method. A fundamental truth is a fact that would hold regardless of convention — physics, math, verified data, human need. First-principles thinking hunts for assumptions masquerading as truths.

### Decomposition
Breaking a problem into its component parts until you reach irreducible elements. You cannot decompose "battery is expensive" further by analogy; you *can* decompose it into: cathode material cost, anode material cost, electrolyte cost, manufacturing overhead — each of which can be addressed independently.

### Reconstruction
Once you hold only verified facts, you rebuild a solution unconstrained by how it has been done before. The reconstruction step is creative and deliberate — the facts constrain what is *possible*, not what should be *built*.

### The Socratic Test
For each constraint or belief, ask: "How do I know this is true?" If the answer is "everyone does it this way" or "we've always done it this way," it is an assumption, not a truth. Valid answers cite data, physical laws, or direct measurement.

## How to Apply

### Step 1 — State the problem and your current solution or belief
Write it out explicitly. Include the cost, time, or constraint that feels like a wall. Example: "We cannot ship this feature in under 6 months because our release process takes that long."

### Step 2 — List every assumption embedded in the problem
For each element of the problem, ask "Why is this true?" and "What would have to change for this to be false?" Write down every assumption without judging it. Example assumptions: "QA must be manual," "staging environment requires a separate server," "sign-off requires three departments."

### Step 3 — Verify each assumption against first principles
For each assumption, ask: is this a physical law, a mathematical constraint, or a measured fact — or is it a policy, a habit, or a copy of what others do? Label each: FACT or ASSUMPTION. Facts stay; assumptions become candidates to challenge.

### Step 4 — Rebuild from the verified facts only
Ignoring the assumptions, ask: given only what is actually true, what solutions are possible? Generate at least three options. Constraints that were assumptions are now design variables you can change.

### Step 5 — Select and stress-test
Choose the most promising reconstruction. Then deliberately try to break it: what second-order effects appear, what assumptions crept back in, what physical or resource limits actually apply? Revise until the solution rests only on verified foundations.

## Output Format

```
╔═════════════════════════════════════════════════════════════════════════════════════════╗
║                              FIRST-PRINCIPLES ANALYSIS                                  ║
╠═════════════════════════════════════════════════════════════════════════════════════════╣
║  Problem:          [what you are trying to solve or the belief you are challenging]     ║
║  Current approach: [how it is done now or what is assumed]                              ║
╚══════════════════════════════════════════╤══════════════════════════════════════════════╝
                                           │
                                           ▼  DECOMPOSE — ask "why is this true?" per element
          ┌────────────────────────────────────────────────────────────────────────────┐
          │  Element / Component                              Classification            │
          ├────────────────────────────────────────────────────────────────────────────┤
          │  [component 1]                             ──►  ● FACT                     │
          │  [component 2]                             ──►  ○ ASSUMPTION               │
          │  [component 3]                             ──►  ○ ASSUMPTION               │
          │  [component N]                             ──►  ● FACT                     │
          └───────────────────────┬────────────────────────────────┬───────────────────┘
                                  │                                │
                  ● KEEP AS FACTS ▼                  ○ CHALLENGE THESE ▼
          ┌──────────────────────────────────┐   ┌────────────────────────────────────────┐
          │  VERIFIED TRUTHS                  │   │  CHALLENGED ASSUMPTIONS                │
          ├──────────────────────────────────┤   ├────────────────────────────────────────┤
          │  ● [fact 1]                       │   │  ○ [assumption] — because [reason]     │
          │  ● [fact 2]                       │   │  ○ [assumption] — because [reason]     │
          │  ● [fact 3]                       │   │  ○ [assumption] — because [reason]     │
          └──────────────────┬───────────────┘   └──────────────────────┬─────────────────┘
                             └─────────────────────────┬────────────────┘
                                                       │
                                                       ▼  REBUILD — generate solutions from facts only
          ┌───────────────────────────┐  ┌───────────────────────────┐  ┌───────────────────────────┐
          │  ▸ OPTION A                │  │  ▸ OPTION B                │  │  ▸ OPTION C                │
          ├───────────────────────────┤  ├───────────────────────────┤  ├───────────────────────────┤
          │  [description]             │  │  [description]             │  │  [description]             │
          │                            │  │                            │  │                            │
          │  Removes assumption:       │  │  Removes assumption:       │  │  Removes assumption:       │
          │  [assumption]              │  │  [assumption]              │  │  [assumption]              │
          └─────────────┬─────────────┘  └──────────────┬────────────┘  └─────────────┬─────────────┘
                        └───────────────────────┬────────┘                             │
                                                └──────────────────┬───────────────────┘
                                                                   │
                                                                   ▼  SELECT
                                    ╔══════════════════════════════════════════════════╗
                                    ║  SELECTED APPROACH                               ║
                                    ║  → [chosen option]                               ║
                                    ║  Rationale: [one-sentence rationale]             ║
                                    ╚═════════════════════════╤════════════════════════╝
                                                              │
                                                              ▼  STRESS-TEST
                                    ┌─────────────────────────────────────────────────┐
                                    │  Risk:       [what could still break this]      │
                                    │  Resolution: [how you addressed it]             │
                                    └─────────────────────────────────────────────────┘
```

Read the diagram top-to-bottom as a pipeline: the header anchors the problem, the decomposition table classifies each element as a verified FACT (●) or a challengeable ASSUMPTION (○), the two columns separate what is kept from what is challenged, the three option boxes each rebuild a solution by removing one or more assumptions, and the final selection feeds directly into a stress-test to ensure the chosen solution rests only on verified foundations.

## Common Mistakes

- **Stopping at the first "why."** Asking why once surfaces proximate causes; you need 3–5 levels of decomposition before reaching bedrock. "It's too expensive" is not a first principle — the cost of the raw materials is closer to one.
- **Treating company policy as a fact.** Policies are not physics. "Legal requires 30 days review" is a process rule, not a law of nature. Challenge it separately from the actual legal requirement.
- **Rebuilding inside the old frame.** If your "from scratch" solution looks nearly identical to what you started with, you did not actually strip the assumptions — you rationalized the existing approach. Force yourself to generate at least one solution that would look absurd by conventional standards.
- **Using it for every problem.** First-principles thinking is expensive. It is most valuable when you are stuck against a hard constraint, when the conventional solution is clearly failing, or when you need step-change improvement rather than incremental gain. For routine decisions, analogical reasoning is faster and adequate.
- **Skipping the stress-test.** A solution built from first principles can still be wrong — it may ignore second-order effects, stakeholder constraints, or implementation complexity. The reconstruction step is not a proof of correctness; it is a starting point for rigorous testing.
