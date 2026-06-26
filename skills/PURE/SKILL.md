---
name: pure
description: "Validate goals are Positively stated, Understood, Relevant, Ethical."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [goals, pure, objectives, ethics, planning, NLP, coaching]
    related_skills: [smart, clear, the-grow-model]
---

# pure Goals

## Overview

pure is a complementary goal-quality filter, often used alongside smart. It originates from NLP (neuro-linguistic programming) coaching and emphasizes the psychological and ethical framing of goals, not just their structure.

| Letter | Criterion | Core question |
|--------|-----------|---------------|
| **P** | Positively stated | Is the goal framed as what you want (not what you want to avoid)? |
| **U** | Understood | Is the goal clear to everyone involved? |
| **R** | Relevant | Is it aligned with broader priorities and the right time? |
| **E** | Ethical | Does achieving this goal align with your values and not harm others? |

## Criterion Breakdowns

### P — Positively Stated
The brain moves toward what you focus on. Negatively framed goals ("stop missing deadlines", "don't lose customers") keep attention on the unwanted state.

Reframe toward the desired outcome:

| Negative framing | Positive reframe |
|-----------------|-----------------|
| "Stop being late to standups" | "Arrive to every standup on time" |
| "Don't lose the enterprise deal" | "Close the enterprise deal by [date]" |
| "Reduce bugs in production" | "Ship zero-defect releases" |

Test: Can you visualize and feel success? Negatively framed goals are hard to visualize.

### U — Understood
The goal must be clear to every person who will act on it or be affected by it. No ambiguity in scope, ownership, or definition of done.

Test questions:
- If you asked every team member to describe this goal, would they give the same answer?
- Are all key terms defined? ("improve performance" — define "improve" and "performance")
- Is ownership explicit?

If interpretation varies: rewrite until consensus is possible.

### R — Relevant
Right goal at the right time. Connects to the bigger picture.

Ask:
- Does this goal serve the current strategic priority?
- Is the timing right? (If a dependency isn't ready, the goal may be premature)
- Does pursuing this crowd out a higher-priority goal?

Unlike smart's R, pure's R also asks about **timing** — a relevant goal poorly timed can still be a mistake.

### E — Ethical
Does achieving this goal align with your values, your organization's principles, and avoid harm to others?

Ask:
- Who else is affected by achieving this goal?
- Are there trade-offs that compromise integrity (cutting safety, deceiving stakeholders, exploiting users)?
- Would you be comfortable if this goal and how you achieved it were public?

Ethical friction caught early is cheaper than reputational or legal damage caught late.

## How to Apply

### Step 1 — State your draft goal
Write what you want to achieve.

### Step 2 — Run each criterion
Test the goal against P, U, R, E and rewrite to resolve any failures.

### Step 3 — Combine with smart (recommended)
pure filters for psychological framing and ethics; smart structures the mechanics. Use both:
- Write goal
- pure filter: does it clear P, U, R, E?
- smart filter: does it clear S, M, A, R, T?
- Final goal passes all 9 criteria

## Output Format

```
╔═════════════════════════════════════════════════════════════════════════════════════╗
║                        P U R E   G O A L   A N A L Y S I S                         ║
╚═════════════════════════════════════════════════════════════════════════════════════╝

  DRAFT GOAL  ►  [original statement]
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  P  ·  POSITIVELY STATED                                      [ PASS / FAIL ]       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  Issue   ►  [if fail, what's negatively framed]                                     │
│  Rewrite ►  [positive version]                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  U  ·  UNDERSTOOD                                             [ PASS / FAIL ]       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  Ambiguities   ►  [terms or scope unclear]                                          │
│  Clarification ►  [rewrite with definitions]                                        │
└─────────────────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  R  ·  RELEVANT                                               [ PASS / FAIL ]       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  Strategic alignment ►  [which priority it serves]                                  │
│  Timing assessment   ►  [is now the right time?]                                    │
└─────────────────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  E  ·  ETHICAL                                                [ PASS / FAIL ]       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  Stakeholders affected ►  [who else is impacted]                                    │
│  Trade-offs            ►  [any ethical tensions]                                    │
│  Verdict               ►  [proceed / modify / reject]                               │
└─────────────────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼
╔═════════════════════════════════════════════════════════════════════════════════════╗
║  FINAL PURE GOAL:                                                                   ║
║  "[Revised goal that passes all 4 criteria]"                                        ║
╠═════════════════════════════════════════════════════════════════════════════════════╣
║  COMBINED SCORE  ║  PURE  ►  P ✓   U ✓   R ✓   E ✓  │  SMART ►  [run separately]  ║
╚═════════════════════════════════════════════════════════════════════════════════════╝
```

Each box is a criterion gate — the draft goal flows in at the top, passes through all four filters in sequence, and exits at the bottom as a refined, validated goal. Mark each gate PASS or FAIL, then carry only the rewritten version forward to the next criterion.

## Common Mistakes

- Skipping E because the goal seems routine — ethical issues are often subtle (privacy, fairness, incentive misalignment)
- Assuming U without testing it — ask a team member to explain the goal back in their own words
- Mixing pure and smart criteria — they complement, not duplicate each other
