---
name: 5w2h
description: "Define any task or problem completely: What, Why, Where, When, Who, How, How Much."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [5w2h, problem-definition, planning, clarity, task, analysis]
    related_skills: [smeac, smart, star-method]
---

# 5W2H

## Overview

5W2H is a problem-definition and task-scoping framework that forces you to answer seven questions before work begins. It eliminates ambiguity by covering every dimension a task or problem can have: identity, purpose, location, timing, ownership, method, and cost.

```
┌──────────┬──────────────────────────────────────────────────────┐
│ Question │ What it pins down                                    │
├──────────┼──────────────────────────────────────────────────────┤
│ WHAT     │ The subject — what exactly is being done/solved      │
│ WHY      │ The justification — why this matters right now       │
│ WHERE    │ The location/scope — where it happens or applies     │
│ WHEN     │ The timeline — start, end, milestones                │
│ WHO      │ The people — owner, doers, approvers, stakeholders   │
│ HOW      │ The method — steps, process, tools                   │
│ HOW MUCH │ The cost — budget, effort, resources consumed        │
└──────────┴──────────────────────────────────────────────────────┘
```

Use it at the start of any project, task delegation, or problem investigation. If you cannot answer all seven, the task is not ready to execute.

## The Seven Questions

### WHAT
The precise subject. Vague "WHAT" answers produce vague work.

Ask: What is the deliverable? What is the problem? What is in scope and explicitly out of scope?

Bad: "Fix the checkout flow"
Good: "Reduce checkout abandonment on the payment step — scoped to the web app only, not mobile"

### WHY
The reason this work exists. The "WHY" justifies priority and guides decisions when the plan hits a fork.

Ask: Why is this a problem worth solving now? What outcome does success produce? What happens if we don't act?

Bad: "Leadership asked for it"
Good: "Payment-step abandonment is 40% vs industry benchmark of 20%; each point costs $15k/month in lost revenue"

### WHERE
The physical or logical location — geography, system, team, product area.

Ask: In which system, market, region, or team does this apply? What is the blast radius if something goes wrong?

Bad: "In the app"
Good: "Payment step in the web app (app.example.com/checkout/payment), affecting all users on the Pro and Enterprise plans"

### WHEN
The time dimension: deadlines, start dates, milestones, and review checkpoints.

Ask: When must this be complete? When does it start? What are the interim checkpoints?

Bad: "ASAP"
Good: "Launch by [date]; design complete by [date minus 2 weeks]; code freeze [date minus 3 days]"

### WHO
Every person with a stake: the owner (single accountable person), doers, reviewers, and impacted parties.

Ask: Who is the single accountable owner? Who does the work? Who approves? Who is notified? Who is affected?

Bad: "The product team"
Good: "Owner: [PM name]; Engineering: [eng lead]; Design: [designer]; Approver: [VP]; Notify: [CS lead]"

### HOW
The method — the process, steps, tools, and approach used to execute.

Ask: What process or steps will be followed? What tools or systems are involved? What approach was chosen over alternatives?

Bad: "We'll figure it out"
Good: "A/B test three checkout UI variants using LaunchDarkly; instrument with Mixpanel; ship winning variant after 2-week test with 95% confidence"

### HOW MUCH
The resource cost: money, time, headcount, and anything else consumed.

Ask: What is the budget? How many hours/days of effort? What other resources (infra, licenses, external vendors) are needed?

Bad: "Whatever it takes"
Good: "Engineering: 3 engineers × 2 weeks = 6 person-weeks; Design: 1 designer × 1 week; A/B testing tool: existing license; total est. cost: $30k"

## How to Apply

### Step 1 — State the raw problem or task
Write the task or problem in one or two sentences — whatever you know right now.

### Step 2 — Answer each question in order
Work through WHAT → WHY → WHERE → WHEN → WHO → HOW → HOW MUCH. For each question, write at least one concrete sentence. If you cannot answer a question, mark it "[OPEN]" and treat it as a blocker before starting.

### Step 3 — Resolve all OPEN items
Every "[OPEN]" is a gap that will cause rework or confusion. Identify who can answer it, set a deadline to resolve it, and do not begin execution until the critical ones are closed. WHAT, WHO, and WHEN are always critical.

### Step 4 — Circulate and align
Share the completed 5W2H with the owner and key doers. Any disagreement on a field surfaces misalignment early — resolve it in writing, not in a meeting two weeks in.

### Step 5 — Use it as a living reference
Revisit the 5W2H at each milestone. If any field has changed (scope crept, timeline shifted, budget increased), update it and re-circulate. Outdated documentation is worse than none.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  5W2H  ·  [task or problem name]                          Date: [YYYY-MM-DD]             ║
║           Author: [name]                                                                 ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║  WHAT ──► WHY ──► WHERE ──► WHEN ──► WHO ──► HOW ──► HOW MUCH                            ║
╠══════════╦═══════════════════════════════════════════════════════════════════════════════╣
║          ║                                                                               ║
║  WHAT  ► ║  [What exactly is being done or solved? What is in scope / out of scope?]     ║
║          ║                                                                               ║
╠══════════╬═══════════════════════════════════════════════════════════════════════════════╣
║          ║                                                                               ║
║  WHY   ► ║  [Why does this matter now? What outcome does solving it produce?]            ║
║          ║                                                                               ║
╠══════════╬═══════════════════════════════════════════════════════════════════════════════╣
║          ║                                                                               ║
║  WHERE ► ║  [Which system, region, team, or product area? What is the scope boundary?]   ║
║          ║                                                                               ║
╠══════════╬═══════════════════════════════════════════════════════════════════════════════╣
║          ║  Start:      [date]                                                           ║
║  WHEN  ► ║  Deadline:   [date]                                                           ║
║          ║  Milestones: ● [date] → [checkpoint]   ● [date] → [checkpoint]                ║
╠══════════╬═══════════════════════════════════════════════════════════════════════════════╣
║          ║  Owner:    [single accountable person]                                        ║
║  WHO   ► ║  Doers:    [name / team — role]                                               ║
║          ║  Approver: [name / role]          Notify:  [name / role]                      ║
║          ║  Affected: [users, customers, teams impacted]                                 ║
╠══════════╬═══════════════════════════════════════════════════════════════════════════════╣
║          ║                                                                               ║
║  HOW   ► ║  [Steps, process, tools, and chosen approach. Include decision rationale.]    ║
║          ║                                                                               ║
╠══════════╬═══════════════════════════════════════════════════════════════════════════════╣
║  HOW   ► ║  Budget: [$ amount or "no separate budget"]                                   ║
║  MUCH    ║  Effort: [X people × Y days = Z person-days]                                  ║
║          ║  Other:  [infra, licenses, vendor costs]                                      ║
╠══════════╩═══════════════════════════════════════════════════════════════════════════════╣
║  ▼ OPEN ITEMS — blockers before execution                                                ║
║    ● [question] ────────────────────────────────► [who resolves it]   by [date]          ║
║    ● [question] ────────────────────────────────► [who resolves it]   by [date]          ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
```

The left column labels the question being answered; the right column holds your response. The OPEN ITEMS footer is a mandatory blockers list — every unanswered question goes here with a named owner and a resolution deadline before execution begins.

## Common Mistakes

- Treating WHAT and HOW as the same field. WHAT is the deliverable; HOW is the method. Conflating them hides whether the approach is the right one for the goal.
- Leaving WHY as "leadership priority." A WHY with no data or reasoning cannot guide decisions when trade-offs appear mid-execution.
- Writing WHO as a team name instead of named individuals. Teams don't own things; people do. "The product team" means nobody is accountable.
- Skipping HOW MUCH because it feels uncertain. An estimate with stated assumptions is always better than none. Unknown cost is a risk, not a reason to omit the field.
- Filling in all seven fields and then never revisiting them. 5W2H is only useful if it stays current — a stale document misleads more than it helps.
