---
name: star-method
description: "Structure responses or case studies as Situation → Task → Action → Result for clear, evidence-based communication."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [star, communication, storytelling, behavioral, interview, evidence]
    related_skills: [scqa, pyramid-principle, smeac]
---

# star Method

## Overview

star is a four-part narrative structure for communicating past experiences or case studies with precision and impact. Each element builds on the last: context sets the scene, task pins accountability, action shows what *you* did, result proves it worked.

```
┌─────────────────────────────────────────────────────────┐
│  S ──► T ──► A ──► R                                    │
│                                                         │
│  Situation   Task       Action      Result              │
│  (context)  (your      (steps      (measurable         │
│              role)      taken)      outcome)            │
└─────────────────────────────────────────────────────────┘
```

Use star in behavioral interviews, performance reviews, retrospectives, case study presentations, and any situation where "trust me, I handled it" is not enough.

## Element Breakdowns

### S — Situation

Set the scene with just enough context for the listener to understand what was at stake.

Include:
- What was happening and why it mattered
- The scale or scope (team size, revenue at risk, timeline pressure)
- Any constraints the audience needs to evaluate your response

Keep it to 1–3 sentences. Do not editorialize — state facts.

Bad: "Things were pretty chaotic and nobody knew what to do."
Good: "Our production database went down during peak traffic, affecting 40,000 active users and threatening $200K in same-day revenue."

### T — Task

State your specific responsibility. This separates what the *situation* demanded from what *you* were accountable for.

Include:
- Your role or title at the time
- What was explicitly expected of you
- Any competing priorities or constraints you personally faced

Bad: "I needed to fix things."
Good: "As on-call engineer, I was responsible for restoring service within our 30-minute SLA while keeping the support team informed."

### A — Action

The most important section. Detail the steps *you personally* took — not "we did."

Structure:
1. First action and rationale
2. Pivots or decisions made under uncertainty
3. How you handled obstacles or involved others

Rules:
- Use "I" not "we" — the listener needs to know your contribution
- Sequence actions chronologically so the logic is followable
- Name the skills or judgment calls that made the difference

Bad: "We worked really hard and figured it out together."
Good: "I ran a query to isolate the failing index, rolled back the last migration, then scripted a health-check that confirmed replication lag before restoring write traffic."

### R — Result

Quantify the outcome. Then add the secondary impact if there was one.

Include:
- The primary metric (time saved, revenue protected, error rate reduced)
- Secondary effects (team morale, process changes, lessons institutionalized)
- What you would do differently (optional — shows self-awareness)

Bad: "Everything turned out fine."
Good: "Service restored in 22 minutes, within SLA. The post-mortem I led produced a runbook that cut average incident resolution time by 40% over the next quarter."

## How to Apply

### Step 1 — Identify the claim you need to prove

Before writing, state the competency or value you are demonstrating. Example: "I want to show I can lead under pressure." Every element should serve that claim.

### Step 2 — Draft Situation and Task in one pass

Write 2–4 bullet points of raw context, then distill to the facts that make the Action and Result legible.

### Step 3 — Write Action in detail first, then edit down

Dump every step you took, then cut anything that did not directly contribute to the result. Aim for 3–5 distinct actions.

### Step 4 — Anchor Result to a number

If no hard metric exists, use a ratio, a before/after comparison, or stakeholder feedback with a source. "My manager called it the fastest recovery in the team's history" is better than nothing.

### Step 5 — Time-check the full story

Spoken star answers should run 90 seconds to 3 minutes. Written star responses should fit on one page. If you are over, cut Situation first, then detail from Action.

## Output Format

```
star RESPONSE: [competency or question being answered]

S — SITUATION
[1–3 sentences: what was happening, what was at stake, relevant scale/constraints]

T — TASK
[1–2 sentences: your specific role and what you were accountable for]

A — ACTION
1. [First action + why you took it]
2. [Second action + decision or pivot]
3. [Third action + how you handled an obstacle or involved others]
(add steps as needed; 3–5 is typical)

R — RESULT
Primary outcome: [metric — number, percentage, time, revenue, error rate, etc.]
Secondary impact: [process change, team effect, or follow-on outcome]
Reflection (optional): [what you would do differently]
```

## Common Mistakes

- **Conflating Situation and Task.** Situation is what the world looked like; Task is what you personally owned. Mixing them hides your accountability.
- **Using "we" throughout Action.** Interviewers and readers want to evaluate *you*. Credit the team in Result, not in Action.
- **Vague results.** "It went well" is not a result. If you cannot find a number, find a proxy — user complaints dropped, a senior leader cited your work, the project shipped on time against a 6-month history of delays.
- **Over-investing in Situation.** Context should be the shortest section. If you are spending more than 20% of the story on setup, you are hiding from the hard part.
- **Picking examples that show effort, not judgment.** star is most compelling when the Action section contains a non-obvious decision, not just hard work. Choose examples where you chose between options, not just where you worked long hours.
