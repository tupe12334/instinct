---
name: pyramid-principle
description: "Structure communication top-down: lead with the answer, then group supporting arguments, then evidence below each."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [pyramid-principle, minto, communication, structure, consulting, writing]
    related_skills: [scqa, mece, star-method]
---

# Pyramid Principle

## Overview

The Pyramid Principle, developed by Barbara Minto at McKinsey, structures written and verbal communication so the main conclusion comes first, followed by grouped supporting arguments, followed by evidence beneath each argument. Readers get the answer before the rationale — saving time and reducing cognitive load.

```
              ┌─────────────────────┐
              │   GOVERNING IDEA    │  ← Lead with the answer
              │  (recommendation    │
              │   or conclusion)    │
              └──────────┬──────────┘
            ┌────────────┼────────────┐
            ▼            ▼            ▼
       ┌─────────┐  ┌─────────┐  ┌─────────┐
       │  Key    │  │  Key    │  │  Key    │  ← 3 grouped arguments
       │  Point  │  │  Point  │  │  Point  │    (MECE at this level)
       │   A     │  │   B     │  │   C     │
       └────┬────┘  └────┬────┘  └────┬────┘
         ┌──┴──┐      ┌──┴──┐      ┌──┴──┐
         │ E1  │      │ E2  │      │ E3  │  ← Data, facts, examples
         │ E2  │      │ E3  │      │ E4  │
         └─────┘      └─────┘      └─────┘
```

Every node in the pyramid must answer the "So what?" of everything beneath it. Every level must be MECE.

## Core Concepts

### Governing Idea
The single sentence that summarizes your entire message. If the reader reads nothing else, this is what they must take away. It is a complete assertion — not a topic. "We should exit the EU market" is a governing idea; "EU market analysis" is a topic heading, not a governing idea.

### Key Lines (Supporting Arguments)
The 2–5 reasons, findings, or proofs that together make the governing idea undeniable. They sit one level below the governing idea and must be:
- **Mutually Exclusive**: no two key points make the same claim
- **Collectively Exhaustive**: together they fully support the governing idea with no logical gaps

### Supporting Evidence
Data, case studies, quotes, calculations, or sub-arguments that prove each key line. Evidence lives at the base of the pyramid and should be concrete and verifiable.

### Vertical Logic (So What? / Why So?)
Reading top-down: each parent must be supportable by its children (Why so? — children answer this). Reading bottom-up: each child must be summarizable into its parent (So what? — parent answers this). If these tests fail, the structure is broken.

### Horizontal Logic (MECE Grouping)
At each level, siblings must form a logical grouping. Three valid grouping types:
- **Deductive**: Premise → Premise → Conclusion (use sparingly; only when the argument is airtight)
- **Inductive**: Multiple parallel findings that, taken together, justify the same conclusion
- **Chronological / Sequential**: Steps in a process that together produce an outcome

## How to Apply

### Step 1 — State the governing idea first
Write your answer or recommendation in one declarative sentence before anything else. If you cannot write it, you do not know your point yet — stop and think before structuring.

### Step 2 — Identify your key supporting arguments
Ask: "What are the 2–5 distinct reasons a skeptical reader would accept this?" Write each as a full sentence assertion, not a label. "Costs are 30% above benchmark" is an argument; "Cost analysis" is not.

### Step 3 — Check key lines are MECE
Verify no two key lines overlap in their claim. Verify that if all key lines are true, the governing idea is necessarily true. If a key line's removal would not weaken the governing idea, cut it.

### Step 4 — Attach evidence to each key line
Under each key line, list the data points, examples, or sub-arguments that prove it. If a key line needs more than 5 pieces of evidence, it likely contains two separate arguments — split it.

### Step 5 — Run the vertical logic test
Read bottom-up: do the evidence items add up to each key line? Read top-down: does each key line answer "why is the governing idea true?" Fix any node where the answer is "not quite."

## Output Format

```
PYRAMID STRUCTURE: [document or presentation title]

GOVERNING IDEA
[One complete sentence — your recommendation or conclusion]

KEY POINT A: [Full sentence assertion]
  Evidence 1: [specific data or fact]
  Evidence 2: [specific data or fact]
  Evidence 3: [specific data or fact]

KEY POINT B: [Full sentence assertion]
  Evidence 1: [specific data or fact]
  Evidence 2: [specific data or fact]
  Evidence 3: [specific data or fact]

KEY POINT C: [Full sentence assertion]
  Evidence 1: [specific data or fact]
  Evidence 2: [specific data or fact]
  Evidence 3: [specific data or fact]

HORIZONTAL LOGIC CHECK
- Grouping type: [deductive / inductive / sequential]
- MECE check: [do key points overlap? are there gaps?]

VERTICAL LOGIC CHECK
- Bottom-up: Key Point A + B + C → [does it prove the governing idea?]
- Top-down: Governing idea → [does each key point answer "why"?]
```

## Common Mistakes

- **Burying the answer.** Starting with context, background, or data before stating the conclusion is the single most common mistake. Readers in business contexts want the answer first — build trust by giving it to them immediately.
- **Writing topic labels instead of assertions.** "Market opportunity" is not a key point. "The addressable market is $4B and growing at 18% CAGR" is. Every node must be a claim that can be true or false.
- **Key lines that are not parallel.** Mixing a financial argument, an operational argument, and a background fact as three siblings violates horizontal logic. All siblings must be the same type of claim at the same logical level.
- **Confusing the pyramid with an executive summary.** An executive summary is a document format. The pyramid is a logical structure that governs every level — slides, memos, emails, and verbal presentations all benefit from it.
- **Too many key lines to hide uncertainty.** Six or seven key lines usually means you have not synthesized your thinking. Force yourself to three to five; the discipline of cutting reveals which arguments actually matter.
