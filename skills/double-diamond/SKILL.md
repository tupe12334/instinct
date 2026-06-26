---
name: double-diamond
description: "Design problems with two diamond phases: Discover/Define (right problem), Develop/Deliver (right solution)."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [double-diamond, design-thinking, diverge, converge, problem, solution]
    related_skills: [scamper, pdca, jobs-to-be-done]
---

# Double Diamond

## Overview

The Double Diamond is a design process model developed by the UK Design Council in 2005. It structures creative problem-solving into two back-to-back cycles of divergent and convergent thinking: the first diamond ensures you are solving the *right* problem; the second ensures you solve it *right*. Skip the first diamond and you risk building the wrong thing elegantly.

```
┌──────────────────────────────┬──────────────────────────────┐
│          DIAMOND 1           │          DIAMOND 2           │
│   "Are we solving the        │   "Are we solving the        │
│      right problem?"         │      problem right?"         │
├──────────────┬───────────────┼──────────────┬───────────────┤
│   DISCOVER   │    DEFINE     │   DEVELOP    │   DELIVER     │
│  (diverge)   │  (converge)   │  (diverge)   │  (converge)   │
├──────────────┼───────────────┼──────────────┼───────────────┤
│ Research     │ Synthesize    │ Ideate       │ Prototype     │
│ Observe      │ Reframe       │ Build drafts │ Test & learn  │
│ Empathize    │ Define HMW    │ Experiment   │ Ship or kill  │
└──────────────┴───────────────┴──────────────┴───────────────┘
```

## Phase Definitions

### Discover — Diverge to understand the problem space
Open up. The goal is to gather raw evidence before forming opinions.
- Conduct user interviews, field observations, diary studies, or competitive reviews.
- Do not filter yet. Capture contradictions, edge cases, and surprises.
- Outputs: interview transcripts, observation notes, data, market research.

### Define — Converge to frame the right problem
Close down. Synthesize everything from Discover into a single, testable problem statement.
- Cluster insights by theme (affinity mapping).
- Write a "How Might We" (HMW) question that is neither too broad ("improve healthcare") nor too narrow ("add a button on screen 3").
- Validate the framing: could solving this HMW address the root causes surfaced in Discover?
- Outputs: insight themes, HMW problem statement, design brief.

### Develop — Diverge to explore solutions
Open up again, now with a clear problem. Generate a wide range of possible solutions — including bad ones.
- Run ideation sessions (brainstorming, SCAMPER, worst-possible-idea, analogous inspiration).
- Build rough, cheap artifacts: sketches, paper prototypes, service blueprints.
- Do not commit to one solution yet. Aim for 5–10 distinct concepts.
- Outputs: concept sketches, low-fidelity prototypes, decision criteria.

### Deliver — Converge on the right solution
Close down. Test, learn, and ship.
- Select 1–3 concepts to prototype at higher fidelity.
- Run structured usability tests or pilots with real users against defined criteria.
- Iterate in tight loops until success criteria are met or a concept is killed.
- Ship the surviving solution. Document what was learned regardless of outcome.
- Outputs: tested prototype, launch plan, post-launch measurement plan.

## How to Apply

### Step 1 — State your starting assumption
Write one sentence: what you think the problem is and why it needs solving. This is your assumption — the first diamond will stress-test it.

### Step 2 — Run Discover (time-box to 1–2 weeks for most projects)
Talk to at least 5–8 users or stakeholders. Observe the behavior in context if possible. Resist the urge to pitch solutions during research sessions.

### Step 3 — Synthesize and Define the real problem
Cluster your notes. Identify 3–5 key insight themes. Write one HMW statement that captures the tension at the core of the problem. Check: does solving this HMW address what you actually observed?

### Step 4 — Run Develop with constraints
Set a hard limit on the number of concepts (5–10) and a budget cap on prototyping (no more than you can build in a day). Variety matters more than polish at this stage.

### Step 5 — Test and Deliver
Write a test script with specific tasks and success criteria before touching users. After 5 tests you will have enough signal to decide: iterate, pivot, or ship.

## Output Format

```
DOUBLE DIAMOND: [project / challenge name]
Date: [YYYY-MM-DD]   Owner: [name/role]

─── DIAMOND 1 ───────────────────────────────────────────────

DISCOVER — Key Findings
1. [Finding]: [evidence — source, quote, or data point]
2. [Finding]: [evidence]
3. [Finding]: [evidence]

DEFINE — Problem Framing
Insight themes:
  - [Theme 1]: [what multiple findings have in common]
  - [Theme 2]: [theme]
HMW statement: "How might we [verb] [user] [goal] so that [outcome]?"
Assumptions still to validate: [list remaining unknowns]

─── DIAMOND 2 ───────────────────────────────────────────────

DEVELOP — Concepts Explored
  Concept A: [name] — [one-line description]
  Concept B: [name] — [one-line description]
  Concept C: [name] — [one-line description]
Selected for testing: [concept name] — Reason: [why this over the others]

DELIVER — Test Results
Test setup: [who tested, how many users, what tasks, success criteria]
Results:
  - Task 1: [pass rate / key observation]
  - Task 2: [pass rate / key observation]
Verdict: [Ship / Iterate / Kill] — [one-sentence rationale]
Next action: [specific step with owner and date]
```

## Common Mistakes

- **Jumping straight to Diamond 2**: teams that already "know the problem" skip Discover and spend weeks building the wrong thing. Even a 3-day discovery sprint is better than none.
- **Confusing Discover with a survey**: a 20-question Google Form is not discovery. You need direct contact with users — watching them struggle reveals what they will never write in a form.
- **Writing a vague HMW**: "How might we improve the user experience?" is not a problem statement — it is a category. A good HMW constrains without prescribing a solution.
- **Converging too early in Develop**: teams fall in love with the first concept and stop generating alternatives. Lock the idea too early and you miss the better option sitting two concepts away.
- **Shipping without defined success criteria**: if you did not write down what "good enough" looks like before testing, you will rationalize whatever result you get. Define pass/fail thresholds before you recruit a single test participant.
