---
name: scamper
description: "Generate creative ideas by applying seven lenses: Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [scamper, creativity, innovation, ideation, brainstorming]
    related_skills: [double-diamond, first-principles, jobs-to-be-done]
---

# SCAMPER

## Overview

SCAMPER is a structured ideation checklist that forces creative thinking by interrogating an existing product, process, or idea through seven lenses. Each lens prompts a different type of transformation. Use it when brainstorming stalls, when iterating on an existing solution, or when you need a fast way to generate a wide range of options.

```
┌───────────────────┬──────────────────────────────────────────────────┐
│  LENS             │  CORE QUESTION                                   │
├───────────────────┼──────────────────────────────────────────────────┤
│  S — Substitute   │  What can be swapped out?                        │
│  C — Combine      │  What can be merged or bundled?                  │
│  A — Adapt        │  What can be borrowed from elsewhere?            │
│  M — Modify       │  What can be magnified, shrunk, or altered?      │
│  P — Put to use   │  What other contexts could this serve?           │
│  E — Eliminate    │  What can be removed without loss of core value? │
│  R — Reverse      │  What if the order or assumption were flipped?   │
└───────────────────┴──────────────────────────────────────────────────┘
```

## Lens Definitions

### S — Substitute
Replace a component, material, person, rule, or process with something else.
- "What if we used X instead of Y?"
- Examples: replace human review with automated scoring; swap synchronous meetings with async video updates.

### C — Combine
Merge two or more elements, functions, or products.
- "What two things could be joined to create something new?"
- Examples: bundle onboarding and the first purchase into one flow; combine customer support with product telemetry.

### A — Adapt
Borrow and apply ideas from another domain, product, or era.
- "What already exists elsewhere that solves a similar problem?"
- Examples: apply airline boarding-zone logic to hospital triage; adapt subscription pricing from SaaS to hardware.

### M — Modify / Magnify / Minify
Change a property — size, speed, frequency, color, shape, intensity.
- "What happens if we 10x this? Halve it? Make it daily instead of monthly?"
- Examples: compress a 2-hour onboarding to 10 minutes; magnify personalization from segment-level to individual.

### P — Put to Other Uses
Find new applications for the current product, feature, or resource.
- "Who else could use this, or in what other context?"
- Examples: an internal analytics tool repackaged as a customer-facing dashboard; spare warehouse capacity rented as fulfillment for third parties.

### E — Eliminate
Remove steps, features, roles, or constraints.
- "What could be cut without losing core value?"
- Examples: remove the email verification step from signup; eliminate the middle-manager approval loop in procurement.

### R — Reverse / Rearrange
Flip the order, invert the assumption, or transpose roles.
- "What if the customer did this step instead of us? What if this happened first instead of last?"
- Examples: let customers configure the product before they sign up; move quality control to the start of the assembly line.

## How to Apply

### Step 1 — Define the subject
State exactly what you are improving: a specific product, feature, process, or experience. Vague subjects produce vague ideas. ("Improve the user onboarding flow for B2B SaaS" beats "improve the product.")

### Step 2 — Timebox each lens
Spend 5–10 minutes per letter. Do not evaluate yet — generate only. Aim for at least 3 raw ideas per lens before moving on.

### Step 3 — Document all raw ideas
Write every idea down, no matter how impractical. Filtering too early kills the useful ones before they surface.

### Step 4 — Filter and score
After all seven lenses, score each idea on two axes: **feasibility** (1–5) and **impact** (1–5). Multiply for a priority score.

### Step 5 — Develop top candidates
For the top 3–5 ideas, write a one-paragraph "what this would actually look like" description. This converts the idea into something testable.

## Output Format

```
SCAMPER: [subject]

S — SUBSTITUTE
- [idea]: [brief rationale]
- [idea]: [brief rationale]

C — COMBINE
- [idea]: [brief rationale]
- [idea]: [brief rationale]

A — ADAPT
- [idea]: [brief rationale]
- [idea]: [brief rationale]

M — MODIFY
- [idea]: [brief rationale]
- [idea]: [brief rationale]

P — PUT TO OTHER USES
- [idea]: [brief rationale]
- [idea]: [brief rationale]

E — ELIMINATE
- [idea]: [brief rationale]
- [idea]: [brief rationale]

R — REVERSE
- [idea]: [brief rationale]
- [idea]: [brief rationale]

TOP CANDIDATES (Feasibility x Impact)
1. [idea] — F:[1-5] x I:[1-5] = [score] — [one sentence on next step]
2. [idea] — F:[1-5] x I:[1-5] = [score] — [one sentence on next step]
3. [idea] — F:[1-5] x I:[1-5] = [score] — [one sentence on next step]
```

## Common Mistakes

- Treating SCAMPER as a checklist to complete rather than a thinking tool — if a lens yields nothing useful after 5 minutes, move on; not every lens applies to every subject.
- Evaluating ideas during generation — defer judgment until Step 4 or you will prematurely discard the best idea.
- Applying the lenses to the wrong level — "Substitute the whole product" is too broad; "Substitute the payment method on the checkout screen" generates actionable ideas.
- Stopping at one idea per lens — the first idea is always the most obvious; the third or fourth is where novelty lives.
- Skipping the "put to other uses" lens — it is the most underused and often surfaces the highest-leverage pivot ideas.
