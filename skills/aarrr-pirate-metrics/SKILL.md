---
name: aarrr-pirate-metrics
description: "Measure startup/product growth across Acquisition, Activation, Retention, Referral, Revenue."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [aarrr, pirate-metrics, growth, startup, acquisition, retention, revenue]
    related_skills: [north-star-metric, customer-journey-map, okr]
---

# AARRR — Pirate Metrics

## Overview

AARRR is a five-stage funnel framework for diagnosing where a product is losing users and revenue. Each stage maps to a measurable rate. Fix the worst-leaking stage first — patching acquisition while retention is broken is pouring water into a cracked bucket.

```
[Acquisition]
     |  % who visit / sign up
     v
[Activation]
     |  % who reach first value moment
     v
[Retention]
     |  % who come back
     v
[Referral]
     |  % who invite others
     v
[Revenue]
     |  % who pay / expand
     v
  GROWTH
```

## Core Components

### Acquisition
How do users find you? Channels: SEO, paid ads, social, content, outbound, partnerships.
- Key metric: visitors, sign-ups, or installs per channel
- Measure **cost per acquisition (CPA)** and **channel mix** to avoid over-dependence on one source

### Activation
Do users experience the core value before they leave? This is the "aha moment" — the first action that predicts long-term retention.
- Key metric: % of new users who complete the activation event within N days
- Example activation events: sent first message, created first project, ran first report

### Retention
Do users come back? This is the most important stage — without it, every other investment leaks.
- Key metric: Day-7 / Day-30 retention rate; or weekly/monthly active user (WAU/MAU) ratio
- A retention curve that flattens above 0% indicates a sustainable product

### Referral
Do users bring others? Referral is the multiplier on every other stage.
- Key metric: Net Promoter Score (NPS) and viral coefficient (invites sent × invite conversion rate)
- Viral coefficient > 1.0 means the product grows without paid spend

### Revenue
Do users pay, and do they expand? Revenue validates that value is real.
- Key metric: MRR, ARPU, LTV, LTV:CAC ratio
- A healthy ratio is LTV ≥ 3× CAC; payback period under 12 months for SaaS

## How to Apply

### Step 1 — Instrument each stage
Before analyzing anything, confirm you can measure each funnel step. Map one primary metric per stage. If you cannot measure it today, define the event and build the tracking first.

### Step 2 — Populate the funnel with real numbers
Pull the last 30–90 days of data. Fill in the conversion rate between each stage. Use cohort data for retention, not averages.

| Stage       | Volume      | Conversion to next stage |
|-------------|-------------|--------------------------|
| Acquisition | 10,000 / mo | 30% → Activation         |
| Activation  | 3,000 / mo  | 40% → Retention (D30)    |
| Retention   | 1,200 / mo  | 15% → Referral           |
| Referral    | 180 / mo    | —                        |
| Revenue     | 600 / mo    | ARPU $45                 |

### Step 3 — Identify the biggest leak
Find the stage with the worst conversion rate relative to industry benchmarks or your own historical trend. This is where to focus next. Do not work on Referral if Activation is below 20%.

### Step 4 — Form one hypothesis per leaking stage
State the problem, the root cause, and the proposed fix as a testable experiment. Example: "Activation is 18% because users never reach the dashboard — add a guided setup checklist to increase it to 30% in 4 weeks."

### Step 5 — Run, measure, iterate
Ship the fix, measure the specific stage metric (not a vanity metric), and re-check the full funnel. Repeat the leak-finding step quarterly or after any major product change.

## Output Format

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                    AARRR PIRATE METRICS AUDIT                                            ║
║                    [Product / Team]  ●  [Date]  ●  Period: last [N] days                 ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

 FUNNEL FLOW & CONVERSION RATES
 ┌──────────────────────────────────────────────────────────────────────────────────────┐
 │                                                                                      │
 │  ╔══════════════════════════════════════════════════════════════════════════════╗    │
 │  ║  A  ACQUISITION  │  [channel mix: SEO / paid / social / other]              ║    │
 │  ║                  │  [volume/mo]  ·  CPA: [value]  ·  top channel: [name]    ║    │
 │  ╚══════════════════════════════════════════════════════════════════════════════╝    │
 │            │  ▼  conversion  [conv%]  (industry avg ~25–40%)                        │
 │  ╔══════════════════════════════════════════════════╗                               │
 │  ║  A  ACTIVATION  │  aha-moment: [activation event]║                               │
 │  ║                 │  [volume/mo]  ·  rate: [value]  ║                               │
 │  ╚══════════════════════════════════════════════════╝                               │
 │            │  ▼  conversion  [conv%]  (industry avg ~20–35%)                        │
 │  ╔══════════════════════════════╗                                                   │
 │  ║  R  RETENTION  │  D7: [val]  ║                                                   │
 │  ║                │  D30: [val] ║                                                   │
 │  ╚══════════════════════════════╝                                                   │
 │            │  ▼  conversion  [conv%]  (industry avg ~10–20%)                        │
 │  ╔══════════════════════════════╗                                                   │
 │  ║  R  REFERRAL  │  NPS: [val] ║                                                   │
 │  ║               │  K:   [val] ║                                                   │
 │  ╚══════════════════════════════╝                                                   │
 │            │  ▼  conversion  [conv%]                                                │
 │  ╔══════════════════════════════╗                                                   │
 │  ║  R  REVENUE  │  MRR: [val] ║                                                    │
 │  ║              │  LTV: [val] ║                                                    │
 │  ╚══════════════════════════════╝                                                   │
 │            │  ▼  GROWTH                                                             │
 └──────────────────────────────────────────────────────────────────────────────────────┘

 FUNNEL SNAPSHOT  ─────────────────────────────────────────────────────────────────────
 ┌─────────────┬──────────────────────────────────┬───────────┬───────────┬──────────┐
 │ Stage       │ Primary Metric                   │  Current  │  Target   │  Status  │
 ├─────────────┼──────────────────────────────────┼───────────┼───────────┼──────────┤
 │ Acquisition │ [e.g. signups/mo]                │  [value]  │  [value]  │  [R/Y/G] │
 ├─────────────┼──────────────────────────────────┼───────────┼───────────┼──────────┤
 │ Activation  │ [activation event rate]          │  [value]  │  [value]  │  [R/Y/G] │
 ├─────────────┼──────────────────────────────────┼───────────┼───────────┼──────────┤
 │ Retention   │ [D7 / D30 retention]             │  [value]  │  [value]  │  [R/Y/G] │
 ├─────────────┼──────────────────────────────────┼───────────┼───────────┼──────────┤
 │ Referral    │ [viral coeff K / NPS]            │  [value]  │  [value]  │  [R/Y/G] │
 ├─────────────┼──────────────────────────────────┼───────────┼───────────┼──────────┤
 │ Revenue     │ [MRR / LTV:CAC]                  │  [value]  │  [value]  │  [R/Y/G] │
 └─────────────┴──────────────────────────────────┴───────────┴───────────┴──────────┘

 FUNNEL SHAPE  (proportional bars — widest gap = biggest leak)
 ┌──────────────────────────────────────────────────────────────────────────────────────┐
 │                                                                                      │
 │  Acquisition ████████████████████████████████████████████████████  [value]  100%   │
 │              ▼ ─[conv%]──────────────────────────────────────────────────────────   │
 │  Activation  █████████████████████████████████████               [value]   [xx]%   │
 │              ▼ ─[conv%]──────────────────────────────────────────────────────────   │
 │  Retention   ████████████████████████                            [value]   [xx]%   │
 │              ▼ ─[conv%]──────────────────────────────────────────────────────────   │
 │  Referral    █████████                                           [value]   [xx]%   │
 │              ▼ ─[conv%]──────────────────────────────────────────────────────────   │
 │  Revenue     ████████████████████                                [value]   [xx]%   │
 │                                                                                      │
 └──────────────────────────────────────────────────────────────────────────────────────┘

 ┌──────────────────────────────────────────┐  ┌──────────────────────────────────────┐
 │ ● BIGGEST LEAK                           │  │ ● NEXT EXPERIMENT                    │
 │                                          │  │                                      │
 │  Stage      ► [stage name]               │  │  Owner          ► [name]             │
 │  Root cause ► [why this stage leaks —    │  │  Deadline       ► [date]             │
 │               one sentence]             │  │  Success signal ► [metric] ≥ [thresh] │
 │  Hypothesis ► [fix] will move [metric]  │  │  Rollback if    ► [metric] < [floor]  │
 │               from [X%] → [Y%]          │  │                                      │
 │               in [timeframe]            │  │                                      │
 └──────────────────────────────────────────┘  └──────────────────────────────────────┘
```

Status key: R = needs urgent attention  ·  Y = watch closely  ·  G = on track. The funnel shape block makes the biggest drop-off visible at a glance — the stage immediately below the widest gap is your highest-leverage fix. The side-by-side boxes at the bottom keep diagnosis and action together so the audit ends with a clear owner and deadline.

## Common Mistakes

- **Optimizing acquisition before fixing retention.** Pouring budget into ads when Day-30 retention is 5% accelerates cash burn with no compounding. Always fix the floor before filling the funnel.
- **Using average retention instead of cohort retention.** A rising MAU can mask the fact that every cohort churns completely within 60 days, replaced by new users. Look at cohort curves.
- **Defining "activation" as account creation.** Signing up is not activation. Activation is the first action that correlates with long-term retention — identify it from cohort data, not intuition.
- **Treating referral as a campaign, not a product feature.** A referral program bolted on top of a product people barely use generates nothing. Referral only scales when retention is already strong.
- **Measuring revenue too early.** In pre-product-market-fit stages, optimizing for revenue before retention is confirmed leads to pricing and packaging decisions that obscure whether the core product works.
