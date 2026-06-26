---
name: rapid-decision
description: "Clarify decision authority with five roles: Recommend, Agree, Perform, Input, Decide."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [rapid, decision, authority, roles, alignment, bain]
    related_skills: [daci, raci, smeac]
---

# RAPID Decision Framework

## Overview

RAPID is a Bain & Company framework that assigns five distinct roles to every significant decision, making explicit who has a voice, who has a veto, and who pulls the trigger. It prevents the two most common failure modes: decisions made by committee with no clear owner, and decisions made unilaterally that generate downstream resistance.

```
           R             A            P             I            D
     ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
     │Recommend │→ │  Agree   │→ │ Perform  │  │  Input   │→ │  Decide  │
     │          │  │ (veto)   │  │          │  │(consult) │  │          │
     └──────────┘  └──────────┘  └──────────┘  └──────────┘  └──────────┘
          ↑                                           │              │
          └───────────────────────────────────────────┘              │
                        feeds into                                   ↓
                                                            Final call here
```

## Role Definitions

### R — Recommend
Proposes a course of action with supporting analysis. This is not a ceremonial role: Recommend gathers Input, synthesizes it, and presents a concrete proposal — not options for others to choose from. If Recommend presents three options without a recommendation, they have not done the job.

### A — Agree
Holds formal veto power. A decision cannot proceed if Agree withholds sign-off. Use this role sparingly — typically for legal, finance, or compliance stakeholders whose domain creates binding constraints. If Agree is overused, it becomes a bottleneck disguised as governance.

### P — Perform
Executes the decision once it is made. Perform must be consulted during the Recommend phase — if the people doing the work consider the plan unworkable, that signal belongs in the recommendation, not surfaced after the decision is final.

### I — Input
Consulted for expertise or perspective before the recommendation is finalized. Input has no veto and does not vote; they inform. The key discipline: Input must be asked, not just offered the chance to speak. Recommend is responsible for actively pulling Input from the right people.

### D — Decide
Makes the final call. Exactly one person per decision. D is accountable for the outcome and has authority to override Recommend if the rationale is clear. D does not do the analysis — that is Recommend's job. If D is consistently overriding Recommend without explanation, Recommend is the wrong person in the role.

## How to Apply

### Step 1 — Define the decision precisely
Write the decision as a single, unambiguous question: "Which vendor do we contract for data infrastructure?" or "Do we launch in the EU in Q3 or delay to Q4?" Vague decisions produce vague role assignments.

### Step 2 — Assign exactly one D
Name a specific person, not a committee, not a team. If two people each believe they are D on the same decision, that conflict must be resolved before proceeding — not after.

### Step 3 — Assign R, A, and P
R should be the person with the most relevant analytical capability and context. A should be limited to stakeholders with genuine veto authority (legal, finance, a partner whose commitment is required). P should include everyone who will execute — their buy-in is not optional, it is a precondition for workable recommendations.

### Step 4 — Identify I stakeholders
List everyone whose expertise should shape the recommendation. Keep this list finite. For each person on the I list, define what specific question they are being asked — not "what do you think?" but "does this approach create regulatory exposure in Germany?"

### Step 5 — Run the process and make the decision
Recommend gathers Input, incorporates Agree constraints, checks P feasibility, and presents a proposal to D. D decides. Document the decision and communicate it — silence after a decision is a process failure.

## Output Format

```
RAPID DECISION: [decision statement as a clear question]
Date: [YYYY-MM-DD]
Target decision date: [YYYY-MM-DD]

─────────────────────────────────────────────
ROLES

  D — Decide:     [Name, Title]
  R — Recommend:  [Name, Title]
  A — Agree:      [Name, Title] — scope of veto: [domain]
  P — Perform:    [Name or team] — consulted on feasibility by [date]
  I — Input:      [Name] — question: [specific question]
                  [Name] — question: [specific question]

─────────────────────────────────────────────
RECOMMENDATION SUMMARY (filled in by R)

Proposed action: [one sentence]
Supporting rationale: [2-4 bullets]
Alternatives considered: [brief]
Key risks: [brief]
P feasibility confirmed: [yes / no / conditions]
A sign-off received: [yes / pending / not required]

─────────────────────────────────────────────
DECISION (filled in by D)

Outcome: [approved / modified / rejected]
If modified: [what changed and why]
Decision date: [YYYY-MM-DD]
Next owner: [P — Name/team]
```

## Common Mistakes

- **Multiple Ds**: "The leadership team decides" is not a decision owner. One name, one accountability. Leadership teams can be consulted (I) or can contain the D, but the D is a person.
- **Agree as a rubber stamp**: If Agree always approves, they are I, not A. Assign A only when withholding sign-off is a realistic and legitimate outcome.
- **Recommend presenting options instead of a recommendation**: Presenting three equally-weighted options and asking D to pick is offloading analytical work upward. Recommend must have a view.
- **Skipping P in the recommendation phase**: Discovering that the decision is operationally unworkable after D signs off wastes the entire process. Perform must validate feasibility before the recommendation reaches D.
- **Treating RAPID as a one-time assignment**: Roles are scoped to a specific decision. A person who is D on pricing strategy may be I on a hiring decision. Rebuild the matrix for each significant decision rather than carrying over assignments from prior ones.
