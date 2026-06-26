---
name: okr
description: "Align teams with ambitious Objectives and measurable Key Results on a quarterly cycle."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [okr, objectives, key-results, alignment, goals, strategy]
    related_skills: [smart, clear, north-star-metric]
---

# OKR — Objectives and Key Results

## Overview

OKRs link ambition to evidence. An Objective answers "where do we go?" — it is qualitative, inspiring, and time-boxed. Key Results answer "how will we know we got there?" — they are numeric, binary, and unambiguous. Teams typically run OKRs on a quarterly cadence with a weekly check-in.

```
Company OKR
└── Team OKR (supports company O)
    ├── KR 1 — numeric target
    ├── KR 2 — numeric target
    └── KR 3 — numeric target
        └── Individual Initiative (drives KR 3)
```

One Objective, 2–5 Key Results. Any more and focus collapses.

## Core Components

### Objective
A short, memorable statement of the outcome you want. It should be:
- **Qualitative** — no numbers; those belong in KRs
- **Ambitious** — uncomfortable but not absurd (70% confidence of hitting it is a good target)
- **Time-boxed** — scoped to the quarter
- **Motivating** — a team should feel why this matters

Bad: "Improve the product"
Good: "Make onboarding so fast that new users reach their first win within 10 minutes"

### Key Results
2–5 measurable outcomes that collectively prove the Objective was achieved. Each KR must:
- Have a **baseline** (where you are now) and a **target** (where you need to be)
- Be **outcome-based**, not a task ("ship X" is an initiative, not a KR)
- Be independently verifiable — two people with the data should agree whether it was hit

Bad KR: "Run five customer interviews" (output, not outcome)
Good KR: "Increase activation rate from 28% to 45%"

### Initiatives
The work you do to move KRs. Initiatives are not OKRs — they are the bets you make. Track them separately. If an initiative isn't moving a KR, stop it.

| Layer | Example | Type |
|-------|---------|------|
| Objective | Dominate the SMB market in DACH | Qualitative |
| Key Result 1 | Grow DACH SMB ARR from €400k to €700k | Numeric outcome |
| Key Result 2 | Achieve NPS ≥ 45 among DACH SMB accounts | Numeric outcome |
| Key Result 3 | Win rate vs. top competitor from 30% to 50% | Numeric outcome |
| Initiative | Launch German-language onboarding flow | Task (feeds KR 2 & 3) |

## How to Apply

### Step 1 — Identify the most important problem or opportunity
Ask: "If we could only accomplish one thing this quarter, what would move the business the most?" That answer becomes the candidate Objective. Reject anything that sounds like a to-do list item.

### Step 2 — Draft the Objective
Write one sentence, present tense or infinitive, no numbers. Test it: would someone outside the team understand why this quarter matters after reading it?

### Step 3 — Define Key Results by working backward
Ask: "If the Objective is fully achieved in 90 days, what would be measurably different?" List every signal you can think of, then prune to the 2–5 that are most direct and least gameable. For each KR confirm: baseline, target, and data source.

### Step 4 — Calibrate ambition
Score each KR: "What's our confidence of hitting the full target?" Aim for ~70%. If you are 95% confident, the target is too easy. If you are under 40%, either rescope or call it a "moonshot KR" explicitly.

### Step 5 — Run weekly check-ins
Each week, score KRs on a 0.0–1.0 scale (current / target). A score below 0.4 at mid-quarter triggers an explicit decision: accelerate, rescope, or kill.

## Output Format

```
OKR — [Team / Person] — Q[N] [YEAR]

OBJECTIVE
"[One-sentence qualitative statement of the outcome]"

KEY RESULTS
KR 1: [Metric] from [baseline] to [target] by [date]
      Data source: [where this number lives]
      Confidence: [%]

KR 2: [Metric] from [baseline] to [target] by [date]
      Data source: [where this number lives]
      Confidence: [%]

KR 3: [Metric] from [baseline] to [target] by [date]
      Data source: [where this number lives]
      Confidence: [%]

INITIATIVES (bets that drive KRs)
- [Initiative] → KR [N]
- [Initiative] → KR [N], KR [N]

WEEKLY SCORE (fill each Monday)
Week | KR 1 | KR 2 | KR 3 | Blocker
-----|------|------|------|--------
 W1  | 0.0  | 0.0  | 0.0  |
 W6  |      |      |      |
W13  |      |      |      |
```

## Common Mistakes

- **Writing tasks as Key Results.** "Launch the new pricing page" is an initiative. A KR is what changes in the world because you launched it: "Conversion rate on pricing page from 2.1% to 3.5%."
- **Too many OKRs.** More than one Objective per team per quarter almost always means none of them get full attention. Pick one.
- **Setting targets at 100% confidence.** If you always hit your KRs, they were too easy. The point of 70% targets is that the team stretches — and roughly 30% of KRs should be missed.
- **Skipping baselines.** A KR without a baseline is unverifiable. "Increase NPS" is meaningless; "Increase NPS from 32 to 50" is a commitment.
- **Treating OKRs as a performance review tool.** When compensation is tied to OKR scores, teams sandbag targets. OKRs are a focus and alignment tool, not an appraisal system.
