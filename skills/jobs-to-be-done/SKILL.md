---
name: jobs-to-be-done
description: "Identify what customers hire a product to accomplish — functional, social, and emotional jobs."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [jtbd, jobs-to-be-done, customer, product, motivation, innovation]
    related_skills: [value-proposition-canvas, kano-model, customer-journey-map]
---

# Jobs to Be Done (JTBD)

## Overview

JTBD reframes product thinking around the customer's underlying goal, not the feature they use. The core idea: customers don't buy products — they "hire" them to make progress in a specific situation. A milkshake isn't bought for taste; commuters hire it to make a boring drive tolerable and keep one hand free.

Three job types exist for every customer action:

```
┌─────────────────────────────────────────────────────────┐
│                      THE JOB                            │
│                                                         │
│  FUNCTIONAL          SOCIAL           EMOTIONAL         │
│  ───────────         ──────           ─────────         │
│  What they           How they         How they          │
│  need to DO          want to APPEAR   want to FEEL      │
│                                                         │
│  "File my taxes      "Look competent  "Stop worrying    │
│   before April 15"   to my CFO"       about audits"     │
└─────────────────────────────────────────────────────────┘
```

Social and emotional jobs are often stronger purchase drivers than functional ones. Ignoring them produces features nobody cares about.

## Job Types

### Functional Job
The concrete task the customer is trying to complete. Expressed as: **verb + object + context**.
- "Commute from home to office in under 30 minutes"
- "Send money to a family member abroad instantly"
- Avoid: "use our app" — that is a solution, not a job

### Social Job
How the customer wants to be perceived by others while getting the job done.
- "Be seen as a financially responsible parent"
- "Signal technical credibility to my team"
- Surfaces in: testimonials, LinkedIn shares, status features

### Emotional Job
How the customer wants to feel internally during or after the job.
- "Feel in control of my finances"
- "Not feel stupid when configuring this"
- Surfaces in: support tickets, churn interviews, NPS comments

### Related Jobs
Adjacent jobs triggered before, during, or after the core job. Expansion opportunities live here.
- Core job: "book a flight" → Related: "find accommodation," "arrange airport transfer"

## How to Apply

### Step 1 — Define the situation, not the segment
Avoid demographic personas. Instead: "When [situation], I want to [progress], so I can [outcome]."
- Bad: "small business owners aged 35–50"
- Good: "When I've just landed a new client and need to look professional fast"

### Step 2 — Interview customers about past behavior
Ask about a specific recent purchase or switch — never hypotheticals. Key questions:
- "Walk me through the last time you [did X]."
- "What were you doing just before you decided to look for a solution?"
- "What almost stopped you from switching?"
- "What job were you firing the old solution from?"

### Step 3 — Extract the three job types
From each interview, pull one statement per job type. Use the format: **[situation] + [motivation] + [expected outcome]**.

### Step 4 — Identify struggling moments
The moment customers feel friction with an existing solution is where new products win. Ask: "What was the most frustrating part of your current approach?"

### Step 5 — Map to product implications
For each job, answer: does your product address this, partially address it, or ignore it? Gaps are roadmap candidates.

## Output Format

```
JTBD ANALYSIS: [product / feature / market]

SITUATION
When: [specific trigger or context]
Customer: [role or behavior, not demographic]

FUNCTIONAL JOB
"[verb] + [object] + [context/constraint]"
Current solution hired: [what they use today]
Struggling moment: [where it fails them]

SOCIAL JOB
"Be perceived as [X] by [audience]"
Signal needed: [what validates this perception]

EMOTIONAL JOB
"Feel [X] when [situation]"
Current anxiety/frustration: [pain point]

RELATED JOBS
Before: [job that precedes this one]
After: [job triggered by completion]

PRODUCT IMPLICATIONS
- [functional gap / feature opportunity]
- [social signal to add or strengthen]
- [emotional friction to reduce]

HIRING CRITERIA (why they'd choose your product)
1. [criterion] — [how your product meets it]
2. ...
```

## Common Mistakes

- Describing the solution as the job — "use a spreadsheet" is not a job; "track spending without losing receipts" is
- Stopping at functional jobs — most differentiation lives in emotional and social jobs that competitors overlook
- Using hypothetical questions in interviews — "would you want X?" tells you nothing; past behavior is the only reliable signal
- Writing jobs at the wrong altitude — too broad ("be healthy") has no actionable boundary; too narrow ("click the export button") misses motivation entirely
- Mapping one job per segment and calling it done — one customer hires the same product for multiple competing jobs in different situations; treat each situation separately
