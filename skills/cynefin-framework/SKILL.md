---
name: cynefin-framework
description: "Match decision-making approach to context complexity: Clear, Complicated, Complex, Chaotic, Confused."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [cynefin, complexity, decision-making, context, sense-making, domains]
    related_skills: [first-principles, second-order-thinking, rapid-decision]
---

# Cynefin Framework

## Overview

Cynefin (pronounced "ku-NEV-in") is a sense-making framework developed by Dave Snowden that helps you identify which type of context you are operating in before choosing how to respond. The core insight is that different domains require fundamentally different decision-making approaches — a method that works brilliantly in one domain can be catastrophically wrong in another.

```
            COMPLICATED          │          COMPLEX
  Cause & effect need analysis   │  Cause & effect only visible
  Expert judgment required       │  in retrospect; experiment first
  Sense → Analyze → Respond      │  Probe → Sense → Respond
                                 │
─────────────────────────────────┼─────────────────────────────────
                                 │
            CLEAR                │          CHAOTIC
  Cause & effect are obvious     │  No discernible cause & effect
  Best practice applies          │  Act first to establish order
  Sense → Categorize → Respond   │  Act → Sense → Respond
                                 │
                        ┌────────┴────────┐
                        │    CONFUSED     │
                        │  (you don't     │
                        │  know which     │
                        │  domain you're  │
                        │  in yet)        │
                        └─────────────────┘
```

The most dangerous move is applying the wrong domain's logic — treating a complex problem with best-practice checklists, or stalling on analysis during a crisis that demands immediate action.

## Domain Definitions

### Clear (formerly "Obvious")
Cause and effect are self-evident to any reasonable person. The right answer is known; it is a matter of following established process. Examples: processing a standard expense report, resetting a password, filing a tax return.
- Action: Sense → Categorize → Respond
- Use: best practice, standard operating procedures, automation

### Complicated
Cause and effect exist but require expertise to see. Multiple valid approaches exist; an expert can determine which is best through analysis. Examples: designing a software architecture, performing surgery, diagnosing a mechanical failure.
- Action: Sense → Analyze → Respond
- Use: expert judgment, structured analysis, good practice (not one single best practice)

### Complex
Cause and effect can only be identified after the fact. The system is adaptive — it changes as you interact with it. No expert can predict outcomes reliably in advance. Examples: entering a new market, launching a culture change program, raising a child.
- Action: Probe → Sense → Respond
- Use: safe-to-fail experiments, emergent practice, parallel bets, retrospective analysis

### Chaotic
No discernible cause-and-effect relationship. The situation is in crisis — stability must be established before analysis is possible. Examples: a production system down with no rollback, a PR crisis going viral, an active security breach.
- Action: Act → Sense → Respond
- Use: novel and immediate action to contain damage, then shift to Complex or Complicated once order is restored

### Confused (Disorder)
You do not know which domain applies. This is the most dangerous state because people default to their preferred decision style regardless of fit. The only move is to break the situation into parts and assign each part to a domain.

## How to Apply

### Step 1 — Describe the situation in concrete terms
Write out what you know and do not know about the cause-and-effect relationships at play. Avoid labeling it too early. Focus on: Can experts reliably predict outcomes? Have you seen this before? Is the system stable or shifting?

### Step 2 — Assign a domain to each part
If the situation is large, decompose it. Different components may sit in different domains. Assign each component to Clear, Complicated, Complex, or Chaotic based on the cause-and-effect test — not based on how stressful or unfamiliar the situation feels.

### Step 3 — Choose the matching decision approach
Apply the domain's prescribed action pattern:
- Clear → implement best practice without debate
- Complicated → bring in the right expert and analyze before acting
- Complex → run the smallest safe-to-fail experiment that will generate signal; do not plan exhaustively
- Chaotic → act immediately to stabilize, then reassess domain

### Step 4 — Watch for domain shifts
Complacency can drag a Clear situation into Chaos (over-reliance on best practice creates brittleness). A Chaotic crisis, once contained, shifts into Complex or Complicated. Reassess the domain after any significant intervention.

### Step 5 — Document what domain you assumed and why
Record your domain assignment explicitly. When outcomes diverge from expectations, check whether you diagnosed the domain correctly — this is the most common root cause of failed decisions.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  CYNEFIN ANALYSIS: [situation or decision being assessed]                 Date: [YYYY-MM-DD] ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│  SITUATION DESCRIPTION                                                                       │
│  [2-4 sentences: what is known, what is unknown, and the stability of cause-and-effect       │
│   relationships — avoid labeling a domain until the breakdown below]                         │
└──────────────────────────────────────────────────────────────────────────────────────────────┘

   ╔══════════════════════════════════════╦══════════════════════════════════════╗
   ║           COMPLICATED                ║              COMPLEX                 ║
   ║  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ║  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ║
   ║  Sense ──► Analyze ──► Respond       ║  Probe ──► Sense ──► Respond         ║
   ║  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ║  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ║
   ║  ● Expert judgment required          ║  ● Cause & effect only in retrospect ║
   ║  ● Multiple valid approaches         ║  ● System adapts to interventions    ║
   ║  ● Good practice (not one best)      ║  ● Safe-to-fail experiments          ║
   ╠══════════════════════════════════════╬══════════════════════════════════════╣
   ║             CLEAR                    ║             CHAOTIC                  ║
   ║  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ║  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ║
   ║  Sense ──► Categorize ──► Respond    ║  Act ──► Sense ──► Respond           ║
   ║  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ║  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ║
   ║  ● Cause & effect are obvious        ║  ● No discernible cause-and-effect   ║
   ║  ● Best practice applies             ║  ● Act first to establish order      ║
   ║  ● Automate & delegate               ║  ● Reassess domain once stable       ║
   ╚══════════════════════════════════════╩══════════════════════════════════════╝
                         ┌───────────────────────────┐
                         │         CONFUSED          │
                         │  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  │
                         │  Decompose ──► assign     │
                         │  each part to a domain    │
                         │  above; do not stay here  │
                         └───────────────────────────┘

   DOMAIN BREAKDOWN
   ┌────────────────────────────────┬─────────────────┬──────────────────────────────────────────┐
   │ Component / Aspect             │ Domain          │ Reasoning                                │
   ├────────────────────────────────┼─────────────────┼──────────────────────────────────────────┤
   │ [aspect 1]                     │ [domain]        │ [one-sentence rationale]                 │
   │ [aspect 2]                     │ [domain]        │ [one-sentence rationale]                 │
   │ [aspect 3]                     │ [domain]        │ [one-sentence rationale]                 │
   └────────────────────────────────┴─────────────────┴──────────────────────────────────────────┘

   PRIMARY DOMAIN ──► ● [ Clear / Complicated / Complex / Chaotic / Confused ]

   PRESCRIBED ACTION PATTERN
   ┌──────────────────────────────────────────────────────────────────────────────────────────┐
   │  Clear       →  Sense ──────────► Categorize ──────────► Respond                        │
   │  Complicated →  Sense ──────────► Analyze    ──────────► Respond                        │
   │  Complex     →  Probe ──────────► Sense      ──────────► Respond                        │
   │  Chaotic     →  Act   ──────────► Sense      ──────────► Respond                        │
   │                                                                                          │
   │  ► ACTIVE: [full active pattern for the primary domain]                                  │
   └──────────────────────────────────────────────────────────────────────────────────────────┘

   IMMEDIATE NEXT STEPS
   ┌──────────────────────────────────────────────────────────────────────────────────────────┐
   │  1. ► [Concrete action matching the domain]                                              │
   │  2. ► [Concrete action matching the domain]                                              │
   │  3. ▲ [Trigger or threshold that would prompt a domain reassessment]                     │
   └──────────────────────────────────────────────────────────────────────────────────────────┘

   DOMAIN REASSESSMENT TRIGGER
   ┌──────────────────────────────────────────────────────────────────────────────────────────┐
   │  ● Signal:    [specific observable event indicating the domain has shifted]              │
   │  ● Watch for: [cliff / containment point / emerging pattern / anomaly]                   │
   │  ● New domain if triggered: [domain] ──► re-run from Step 2                             │
   └──────────────────────────────────────────────────────────────────────────────────────────┘
```

The 2×2 grid maps each domain's action pattern so you can visually confirm the prescribed response logic before acting. The Domain Breakdown table forces explicit per-component reasoning, and the Reassessment Trigger section closes the loop — naming in advance the signal that would invalidate the current diagnosis.

## Common Mistakes

- **Treating complexity as merely "complicated."** Complicated problems have knowable solutions that experts can find through analysis. Complex problems do not — running more analysis before acting is procrastination, not rigor. The test: could the best expert in the world reliably predict the outcome in advance? If no, it is Complex, not Complicated.
- **Skipping Chaotic straight to Complicated.** In a genuine crisis, pausing to assemble expert panels and write analysis documents while the building is burning is a domain mismatch. Act first to contain, analyze after the bleeding stops.
- **Applying best practice to a Complex domain.** In Complex contexts the system adapts to your intervention. A practice that worked before may not work now because the environment has changed in response to prior actions. Run experiments; do not implement solutions.
- **Staying in Confused and calling it "nuanced."** Confused is not a comfortable home — it is a temporary state requiring decomposition. If your answer to "what domain is this?" is "it depends" with no further breakdown, you have not done the work.
- **Ignoring the cliff between Clear and Chaotic.** Overconfidence in best practice can push a Clear situation over a cliff into Chaos when the underlying conditions change unnoticed. Build sensing mechanisms that surface anomalies in ostensibly Clear domains before they cascade.
