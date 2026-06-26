---
name: the-project-portfolio-matrix
description: "Prioritize projects by strategic value vs effort/risk to allocate resources across a portfolio."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [portfolio, projects, prioritization, strategy, resources, planning, roadmap]
    related_skills: [bcg-matrix, the-eisenhower-matrix, swot]
---

# The Project Portfolio Matrix

## Overview

Plot projects on two axes to guide investment and prioritization decisions:
- **Strategic Value** (vertical): impact on goals, revenue, competitive position
- **Effort / Risk** (horizontal): cost, time, complexity, uncertainty

```
              LOW EFFORT        HIGH EFFORT
             ┌─────────────┬─────────────────┐
HIGH VALUE   │  QUICK WINS │  MAJOR PROJECTS │
             │  (Do first) │  (Plan & staff) │
             ├─────────────┼─────────────────┤
LOW VALUE    │  FILL-INS   │   THANKLESS     │
             │  (If spare  │   TASKS         │
             │   capacity) │  (Eliminate)    │
             └─────────────┴─────────────────┘
```

## Quadrant Definitions

### Quick Wins — High Value, Low Effort
- Maximum ROI
- Do these first; they build momentum and free capacity
- Watch for scope creep turning them into Major Projects

### Major Projects — High Value, High Effort
- Strategic bets; essential for long-term positioning
- Require dedicated teams, milestones, and risk management
- Schedule carefully; don't understaff

### Fill-ins — Low Value, Low Effort
- Nice to have; do only when high-value work is blocked
- Easy to overinvest; timebox these

### Thankless Tasks — Low Value, High Effort
- Kill these. If they exist for compliance/legacy reasons, automate or outsource
- Never staff strategically important people here

## How to Apply

### Step 1 — Inventory
List all candidate projects or initiatives.

### Step 2 — Score Strategic Value (1–10)
Consider:
- Revenue or cost impact
- Alignment with top-level goals/OKRs
- Competitive differentiation
- Customer impact
- Strategic optionality (does it unlock future projects?)

### Step 3 — Score Effort / Risk (1–10)
Consider:
- Person-weeks or cost to deliver
- Technical complexity
- Dependencies on other teams or systems
- Uncertainty in scope or outcome
- Opportunity cost

### Step 4 — Plot and classify
High value = score ≥6. High effort = score ≥6. Adjust thresholds to your context.

### Step 5 — Allocate resources
- Protect Quick Wins from being deprioritized by bigger projects
- Staff Major Projects with your best people; set clear milestones
- Timebox Fill-ins; don't let them expand
- Actively kill or outsource Thankless Tasks

### Step 6 — Review quarterly
Projects shift quadrants as scope changes and priorities evolve.

## Output Format

```
PROJECT PORTFOLIO ANALYSIS: [context / team / quarter]

QUICK WINS (High Value, Low Effort) — Do first
- [project]: value=[X/10], effort=[Y/10] — [rationale, suggested owner]

MAJOR PROJECTS (High Value, High Effort) — Plan & staff
- [project]: value=[X/10], effort=[Y/10] — [rationale, key risks, milestone]

FILL-INS (Low Value, Low Effort) — Only if spare capacity
- [project]: value=[X/10], effort=[Y/10] — [why defer]

THANKLESS TASKS (Low Value, High Effort) — Eliminate
- [project]: value=[X/10], effort=[Y/10] — [kill/automate/outsource recommendation]

RESOURCE ALLOCATION RECOMMENDATION:
[Staffing priorities and sequencing for next cycle]
```

## Scoring Tips

- Score **relative to other items in the portfolio**, not absolutely
- Use dot voting or team consensus to reduce individual bias
- Re-score when any major assumption changes (market shift, new competitor, org restructure)
