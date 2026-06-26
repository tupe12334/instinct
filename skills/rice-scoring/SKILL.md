---
name: rice-scoring
description: "Prioritize features/projects by Reach, Impact, Confidence, and Effort into a single score."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [rice, prioritization, product, scoring, reach, impact, confidence, effort]
    related_skills: [moscow, kano-model, the-eisenhower-matrix]
---

# RICE Scoring

## Overview

RICE is a quantitative prioritization framework that computes a single comparable score for each feature or initiative. It prevents gut-feel ranking by forcing explicit estimates across four dimensions: how many people are affected, how much it helps them, how sure you are, and how much work it takes.

```
RICE Score = (Reach × Impact × Confidence) / Effort
```

Higher score = higher priority. Items are ranked by score descending.

## The Four Dimensions

### Reach — "How many people, in what time window?"
Count the number of users or customers affected per time period (typically per quarter). Use real data: DAU, MAU, conversion funnel counts, support ticket volume. Do NOT estimate in percentages here — use absolute numbers.

- Example: 2,400 users/quarter who go through the checkout flow

### Impact — "How much does this move the needle per person?"
Rate the impact on the individual user when they encounter the feature. Use a fixed scale:

| Score | Meaning |
|-------|---------|
| 3     | Massive (transforms the experience) |
| 2     | High (clear improvement) |
| 1     | Medium (noticeable) |
| 0.5   | Low (minor) |
| 0.25  | Minimal (barely perceptible) |

### Confidence — "How sure are we about Reach and Impact?"
Express as a percentage reflecting evidence quality:

| % | Evidence |
|---|---------|
| 100% | Hard data (A/B test, analytics, user research) |
| 80%  | Some data (anecdotal, partial research) |
| 50%  | Weak data (gut feel, one conversation) |

Never exceed 100%. Round to 100/80/50 — false precision is noise.

### Effort — "How many person-months does this take?"
Estimate total engineering + design + PM time in person-months. Minimum value: 0.5 (half a person-month). Do NOT use story points — convert to time.

- 1 engineer for 2 weeks = 0.5 person-months
- 2 engineers + 1 designer for 1 month = 3 person-months

## How to Apply

### Step 1 — List all candidates
Write out every feature, project, or initiative under consideration. Aim to score at least 5–10 items so the ranking is meaningful.

### Step 2 — Estimate each dimension independently
For each item, assign Reach, Impact, Confidence, and Effort without looking at the final score yet. Involve the team — engineering owns Effort, product/data owns Reach, design/research informs Impact and Confidence.

### Step 3 — Calculate the score
```
Score = (Reach × Impact × Confidence%) / Effort
```
Example: Reach=2400, Impact=2, Confidence=80%, Effort=3
Score = (2400 × 2 × 0.80) / 3 = 1280

### Step 4 — Rank and sanity-check
Sort by score descending. Ask: does this order match intuition? If not, find the mismatch — either the intuition is wrong or an estimate is off. Adjust estimates with justification, not to make the answer "look right."

### Step 5 — Communicate the tradeoffs
Share the scoring table with stakeholders. The score is a conversation starter, not a decree. Flag items where Confidence is low — they may need a spike or experiment before committing.

## Output Format

```
RICE SCORING: [product area or initiative set]
TIME WINDOW: [quarter / month / etc.]

| Item                  | Reach  | Impact | Confidence | Effort | RICE Score |
|-----------------------|--------|--------|------------|--------|------------|
| [Feature A]           | [####] | [#.#]  | [##%]      | [#.#]  | [####]     |
| [Feature B]           | [####] | [#.#]  | [##%]      | [#.#]  | [####]     |
| [Feature C]           | [####] | [#.#]  | [##%]      | [#.#]  | [####]     |

RANKING (highest to lowest):
1. [Feature X] — Score: [####] — [one-line rationale]
2. [Feature Y] — Score: [####] — [one-line rationale]
3. [Feature Z] — Score: [####] — [one-line rationale]

LOW CONFIDENCE FLAGS:
- [Item]: needs [user research / data / spike] before committing

RECOMMENDATION: [top 1-2 items to act on next and why]
```

## Common Mistakes

- **Using percentages for Reach.** "20% of users" is meaningless without an absolute base. Always convert to a real count per time period.
- **Inflating Confidence to avoid hard conversations.** If you haven't done the research, 50% is honest. Marking everything 80% defeats the framework.
- **Rounding Effort to 1 when it's really 0.5.** Small items get artificially deprioritized. Use 0.5 for sub-month work.
- **Ignoring strategic bets.** A high-confidence, low-Reach compliance item may rank low but be non-negotiable. Flag these separately — RICE ranks by user value, not legal necessity.
- **Running RICE in a room without data.** The framework exposes gaps in your data, not just priorities. Missing Reach data is a signal to instrument your funnel, not to guess.
