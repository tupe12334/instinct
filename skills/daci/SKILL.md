---
name: daci
description: "Assign decision roles: Driver (moves it forward), Approver (decides), Contributors (advise), Informed (notified)."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [daci, decision, roles, driver, approver, contributor, informed]
    related_skills: [raci, rapid-decision, smeac]
---

# DACI Decision Framework

## Overview

DACI assigns exactly one role to every person on every decision, making clear who drives it, who owns the final call, who advises, and who just needs to know the outcome. It is purpose-built for decisions — not tasks — which is the key distinction from RACI.

```
Decision: Choose the new data warehouse vendor
─────────────────────────────────────────────────────────
Role          Person / Team       Obligation
─────────────────────────────────────────────────────────
Driver        Engineering Lead    Runs the process, collects input, writes the recommendation
Approver      VP Engineering      Makes the final call
Contributors  Data Team, Finance  Provide requirements, cost constraints, technical input
Informed      Product, Legal      Notified once the decision is made
─────────────────────────────────────────────────────────
```

## Role Definitions

### D — Driver
Moves the decision forward from start to finish. Owns the process, not the outcome. Gathers input from Contributors, synthesizes options, writes the recommendation, sets the timeline, and ensures the Approver has everything they need to decide. Exactly one Driver per decision — co-drivers create diffusion of responsibility.

### A — Approver
Makes the final call. Has the authority and accountability for the outcome. Can be one person or a small group (e.g., two co-founders who must both agree), but keep this number as small as possible. The Approver is not required to do the research — that is the Driver's job. If the Approver is also doing the research, the Driver role is redundant and someone is wearing two hats.

### C — Contributors
Anyone whose expertise or stake materially affects the quality of the decision. They are asked for input before the decision is made, not after. Contributors advise — they do not decide. If a Contributor's input is consistently ignored, remove them from the list. If their input is consistently required to decide, they may be an Approver.

### I — Informed
Notified of the outcome after the decision is made. No input, no vote. Keep this list accurate: people who should be Informed but aren't become blockers later; people who shouldn't be Informed but are will treat every decision as an invitation to weigh in.

## How to Apply

### Step 1 — Name the decision precisely
Write it as a question or a sentence with a clear yes/no or option-selection answer. "Platform strategy" is not a decision. "Should we migrate the API from REST to GraphQL by Q3?" is.

### Step 2 — Identify the Approver first
Who has the authority and accountability to make this call? If you can't name one person (or a small named group), the decision is either too big, too vague, or owned by the wrong team. Resolve that before continuing.

### Step 3 — Name the Driver
Who will run the process? This is often a project lead, product manager, or subject-matter expert closest to the problem. The Driver does not have to be senior — they need to be organized and credible.

### Step 4 — List Contributors
Ask: whose input is necessary to make a good decision? Be strict. Every Contributor adds latency. Aim for three to five. If a team is listed, name the specific person who will engage — not the whole team.

### Step 5 — List who needs to be Informed
Think downstream: who will be affected by this decision and needs to adjust their plans? Err on the side of over-informing here (unlike Contributors, Informed is cheap), but do not add people who can unilaterally reverse or relitigate the decision — they are Approvers, not recipients.

### Step 6 — Set the decision deadline
DACI without a date is not a process — it is a conversation. The Driver owns this date. Put it in writing alongside the matrix.

## Output Format

```
DACI: [Decision name — framed as a question or clear choice]
Date needed by: [YYYY-MM-DD]
Context: [1-2 sentences on why this decision needs to be made now]

─────────────────────────────────────────────────────────
Role          Person / Team        Notes
─────────────────────────────────────────────────────────
Driver        [Name / Role]        [Scope of their process ownership]
Approver      [Name / Role]        [What authority they hold]
Contributors  [Name / Role]        [What input they provide]
              [Name / Role]        [What input they provide]
Informed      [Name / Team]        [When and how they will be notified]
─────────────────────────────────────────────────────────

Options under consideration:
  1. [Option A] — [one-line summary]
  2. [Option B] — [one-line summary]

Recommendation (Driver): [Option X], because [brief rationale]

Decision (Approver): [Approved / Modified / Rejected] on [date]
Rationale: [why]

Notification sent to Informed: [date]
```

## Common Mistakes

- **Driver and Approver are the same person**: This collapses DACI into one person making a solo call with extra paperwork. DACI is useful when the person doing the work is not the person with final authority.
- **Multiple Approvers without a tiebreaker rule**: If two Approvers disagree and there is no escalation path, the decision stalls. Either reduce to one Approver or define who breaks ties.
- **Contributors treated as Approvers**: If Contributors feel entitled to veto the decision, they are behaving as Approvers. Clarify their role explicitly — they advise, the Approver decides.
- **No deadline**: Without a date, every decision competes with urgent work and loses. The Driver must set and enforce a deadline from the start.
- **Applying DACI to tasks, not decisions**: Use RACI for work ownership across tasks. DACI is specifically for a single decision with a discrete outcome. Mixing the two produces an awkward hybrid that serves neither purpose.
