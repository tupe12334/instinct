---
name: raci
description: "Clarify roles on any task or decision: Responsible, Accountable, Consulted, Informed."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [raci, roles, accountability, responsibility, decision, team]
    related_skills: [daci, rapid-decision, smeac]
---

# RACI Matrix

## Overview

RACI assigns one of four roles to every person on every task or decision, eliminating the ambiguity that causes dropped work and duplicated effort. Each row is a task; each column is a person or team.

```
         Person A   Person B   Person C   Person D
Task 1      R          A          C          I
Task 2      A          R          I          C
Task 3      C          I          R          A
```

- **R — Responsible**: Does the work. Can be multiple people.
- **A — Accountable**: Owns the outcome; makes the final call. Exactly one per task.
- **C — Consulted**: Provides input before the decision or action. Two-way communication.
- **I — Informed**: Notified after the decision or action. One-way communication.

## Role Definitions

### R — Responsible
The person or people executing the task. They do the actual work. Multiple Rs are allowed, but each R must have a clearly scoped slice — two Rs with identical scope creates confusion, not coverage.

### A — Accountable
The single owner. If the task fails, A answers for it. A has final authority to approve, reject, or change direction. There must be exactly one A per task — two As means no one is actually accountable.

### C — Consulted
Their expertise or stake affects the outcome. They must be asked before decisions are finalized. Ignoring a C is a process failure. Keep this list short: Consulted is a cost — it adds latency and coordination overhead.

### I — Informed
They need visibility, not a vote. Inform them after the fact. Over-informing is as harmful as under-informing — too many Is means noise, and people stop reading updates.

## How to Apply

### Step 1 — List all tasks and decisions
Write out every discrete deliverable, decision, or milestone. Be specific. "Design" is not a task. "Approve final UI mockup" is.

### Step 2 — List all roles or people
Use roles (Engineering Lead, Product Manager, Legal) rather than names where possible — the matrix survives org changes longer.

### Step 3 — Assign R, A, C, I for each task
Fill in the matrix cell by cell. For each task, ask: who does it (R), who owns the outcome (A), who must be asked (C), who must be told (I).

### Step 4 — Validate against the rules
Check every row: exactly one A, at least one R, and no cell left blank. Review columns: anyone with all Is and no Rs or Cs is probably not needed in the matrix.

### Step 5 — Review with stakeholders
Share the draft. The most productive disagreements surface here. If two people both write A for the same task, that conflict existed before the matrix — now you can resolve it.

## Output Format

```
RACI MATRIX: [project / initiative name]
Date: [YYYY-MM-DD]

              [Role 1]   [Role 2]   [Role 3]   [Role 4]
─────────────────────────────────────────────────────────
[Task 1]        R          A          C          I
[Task 2]        A          R          I          C
[Task 3]        C          R          A          -
[Task 4]        I          C          R          A

Legend:
  R = Responsible (does the work)
  A = Accountable (owns outcome, single per task)
  C = Consulted (input required before action)
  I = Informed (notified after action)
  - = No involvement

NOTES:
- [Any clarifications on split responsibilities or escalation paths]
```

## Common Mistakes

- **Multiple As on one task**: "Co-accountable" is not accountable. Pick one. If two people insist they both own it, escalate to their shared manager before proceeding.
- **Conflating R and A**: The person doing the work (R) is not always the owner (A). A senior contributor can be R while their manager holds A.
- **Too many Cs**: Every C is a blocker. If you have more than 3 Cs on a single task, you are designing a committee, not a workflow. Cut ruthlessly.
- **Skipping tasks that feel obvious**: "Everyone knows who owns onboarding." They don't. Write it down.
- **Building RACI and never revisiting it**: Roles shift. Revalidate at each project phase or when team composition changes.
