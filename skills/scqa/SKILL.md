---
name: scqa
description: "Frame any communication as Situation → Complication → Question → Answer to create narrative tension and clarity."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [scqa, communication, narrative, storytelling, consulting, structure]
    related_skills: [pyramid-principle, mece, star-method]
---

# SCQA (Situation → Complication → Question → Answer)

## Overview

SCQA is a narrative opening structure from Barbara Minto's Pyramid Principle. It hooks the audience by establishing shared ground (Situation), introducing tension (Complication), crystallizing the implied question (Question), and delivering the answer upfront (Answer). The result is communication that earns attention instead of demanding it.

```
┌─────────────────────────────────────────────────────────────┐
│  S ──► C ──► Q ──► A                                        │
│                                                             │
│  Situation     Complication    Question       Answer        │
│  (agreed       (something      (what the      (your         │
│   context)      changed or      audience is    governing    │
│                 went wrong)     now asking)    message)     │
└─────────────────────────────────────────────────────────────┘

Tension builds across S → C → Q, then releases at A.
```

Use SCQA to open executive briefings, emails to senior stakeholders, consulting decks, product proposals, and any communication where you need to be read — not skimmed.

## Element Breakdowns

### S — Situation

State facts the audience already accepts as true. This is not your argument — it is shared ground that anchors everything that follows.

Include:
- The stable background state before anything went wrong
- Scope: the business, team, product, or market being discussed
- Enough context for the audience to recognize the world you are describing

Keep it to 1–3 sentences. If the audience challenges anything in your Situation, you have started too far into disputed territory — move earlier.

Bad: "Our product is struggling and we need to fix it."
Good: "For the past two years, our enterprise tier has been our highest-margin segment, accounting for 60% of ARR."

### C — Complication

Introduce the tension that makes the Situation unstable. This is the reason you are communicating at all.

Types of complications:
- Something changed (market shift, new competitor, regulation)
- Something failed (metric missed, project slipped, assumption proven wrong)
- Something is about to happen (deadline, board review, contract renewal)
- A contradiction emerged (two true things that cannot both stand)

Rules:
- The Complication must logically follow from the Situation — do not invent tension
- One complication per document; multiple complications dilute urgency
- Make it concrete: a number, a deadline, a named event

Bad: "But things have been getting harder lately."
Good: "In Q3, enterprise churn reached 18% annualized — triple the rate from the prior year — driven by three logo losses we did not forecast."

### Q — Question

State the question the audience is now implicitly asking after hearing S + C. Most writers skip this step. Do not — it tells the audience exactly what your document will answer, and it signals that you understand their perspective.

The Question is almost always one of:
- "What is causing this?"
- "What should we do?"
- "How bad is it and can we fix it?"
- "Is this the right approach?"

Rules:
- The Question must arise naturally from the Complication — if it feels forced, rewrite C
- Write it as the audience would ask it, not as you want to answer it
- One question only; if you have two, you have two documents

Bad: "So we need to think about churn."
Good: "What is driving the churn spike, and what must we do in the next 90 days to reverse it?"

### A — Answer

Deliver your governing message — the direct, complete answer to the Question. Everything else in your document supports this sentence.

Rules:
- Answer the Question as stated, not a softer version of it
- If you cannot answer in 1–2 sentences, your Answer is actually a theme, not an answer — sharpen it
- This sentence should still make sense if the audience reads nothing else

Bad: "We need to look into this carefully and consider our options."
Good: "Churn is concentrated in three industries facing budget freezes; we should pause expansion into those verticals and redirect Q4 resources to retention plays in stable segments."

## How to Apply

### Step 1 — Identify your audience and their current belief

Write one sentence describing what your audience already knows and accepts. That sentence is the seed of your Situation. If you cannot write it, you do not know your audience well enough to structure the communication yet.

### Step 2 — State the Complication as a single concrete event

Ask: "What happened, or is about to happen, that makes the Situation no longer stable?" Write it as a fact with a number, a date, or a named event. Remove adjectives and qualifiers — they weaken tension.

### Step 3 — Speak the Question out loud

Read S + C aloud, then say: "So the question is..." and finish the sentence without looking at your notes. If you cannot finish it naturally, your Complication is either too vague or not a real complication.

### Step 4 — Write the Answer before writing the document

Draft your Answer before you fill in supporting detail. This forces you to have a position. If you find yourself writing "it depends" as your Answer, you are still in analysis — finish the analysis first, then write the SCQA.

### Step 5 — Stress-test the chain

Read S → C → Q → A aloud as four consecutive sentences. Each must follow logically from the previous. If any transition feels like a jump, revise that element. Common failure: a Question that does not match the Complication, or an Answer that addresses a different question than the one asked.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════╗
║  SCQA  ►  [document or communication title]                                                     ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════╝

  ◄─────────────────────── TENSION BUILDS ───────────────────────────────────────► RELEASES ────►

┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ S — SITUATION    │ ───► │ C — COMPLICATION │ ───► │ Q — QUESTION     │ ───► │ A — ANSWER       │
├──────────────────┤      ├──────────────────┤      ├──────────────────┤      ├──────────────────┤
│                  │      │                  │      │                  │      │                  │
│ [1–3 sentences   │      │ [1–2 sentences   │      │ [The single      │      │ [1–2 sentences.  │
│  of accepted,    │      │  of the specific │      │  question the    │      │  Direct, complete│
│  stable context. │      │  event, failure, │      │  audience is now │      │  answer to Q.    │
│  No argument.    │      │  or change that  │      │  asking, written │      │  Your governing  │
│  No tension yet] │      │  destabilizes S. │      │  from their own  │      │  message.]       │
│                  │      │  Concrete fact.] │      │  perspective.]   │      │                  │
└──────────────────┘      └──────────────────┘      └──────────────────┘      └──────────────────┘
   shared ground    ───►   tension introduced ───►   implied Q stated  ───►   answer first

  ▼  SUPPORTING STRUCTURE  (optional — attach below A)
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  1.  [First reason or supporting point for A]                            │
  │  2.  [Second reason or supporting point for A]                           │
  │  3.  [Third reason or supporting point for A]                            │
  └──────────────────────────────────────────────────────────────────────────┘
```

Each box feeds the next — your Situation sets the stage, the Complication introduces tension that makes the Question inevitable, and the Answer releases that tension by stating your governing message upfront. Attach the Supporting Structure only when the Answer needs explicit backing; it is not part of the SCQA opening itself.

## Common Mistakes

- **Putting the argument in Situation.** If your S contains a claim the audience might dispute, you have started at C or A. Situation is only what everyone agrees is true — keep it boring.
- **Complication is too vague to create tension.** "The market is changing" is not a complication. A complication has a specific trigger: a number, a date, a named competitor, a failed assumption. Vague complications produce vague Questions and weak Answers.
- **Skipping the Question.** Most practitioners write S → C → A and wonder why readers feel ambushed by the Answer. The Question is what signals to the audience that you know what they are thinking. Never omit it.
- **Answer that hedges.** "We should explore several options" is not an Answer — it is a deferral. If you are not ready to commit to an Answer, do not send the communication. Finish your thinking first.
- **Using SCQA as a full document structure.** SCQA is an opening, not an outline. After the Answer, use MECE or a pyramid structure to organize the supporting argument. SCQA answers "why should I read this?" — the rest of the document answers "how do I know you are right?"
