# instinct

**54 strategy and decision frameworks as Claude Code slash commands.**

Run SWOT, OKR, First Principles, Pre-Mortem, RICE, and 49 more — directly in your terminal. No tab switching. No blank-page paralysis. Type a command, describe your situation, get a structured analysis.

[![GitHub stars](https://img.shields.io/github/stars/tupe12334/instinct?style=flat-square)](https://github.com/tupe12334/instinct/stargazers)
[![Version](https://img.shields.io/badge/version-1.0.3-blue?style=flat-square)](https://github.com/tupe12334/instinct)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-blueviolet?style=flat-square)](https://claude.ai/code)

---

## Install

```
/plugin marketplace add tupe12334/instinct
```

---

## Demo

### `/swot` — Analyze a strategic decision

> *"Should we rewrite our monolith into microservices?"*

```
SWOT ANALYSIS: Monolith → Microservices migration

STRENGTHS
1. Engineering team has prior microservices experience — reduces ramp-up risk
2. Current monolith has clear domain boundaries — clean split points identified
3. Two services (auth, billing) already isolated — migration is incremental

WEAKNESSES
1. No internal platform team — each squad would own its own infra overhead
2. Integration test suite covers monolith end-to-end — will break on extraction
3. 3 senior engineers own 80% of the codebase knowledge — bus factor critical

OPPORTUNITIES
1. Competitor outages last quarter traced to shared DB — decoupling = reliability win
2. Two enterprise deals blocked on SOC2 data isolation — microservices unblocks them
3. Cloud provider offering migration credits until Q3

THREATS
1. Distributed systems complexity will slow feature velocity for 6–12 months
2. Network latency between services not yet benchmarked — SLA risk
3. Current on-call rotation too thin to handle N+1 services

STRATEGIC OPTIONS (TOWS)
SO: Use engineering experience + incremental approach to unblock enterprise deals by Q3
ST: Extract auth service first (low risk, high isolation value) before scaling migration
WO: Hire platform engineer before migrating beyond 3 services — remove bus factor risk
WT: Define 90-day pause criteria — if velocity drops >40%, stop and reassess

PRIORITY ACTIONS:
1. Extract auth service as proof-of-concept — validates approach, unblocks SOC2 conversation
2. Hire or designate platform engineer — prerequisite for any further extraction
3. Benchmark inter-service latency against SLA requirements before committing
```

---

### `/first-principles` — Challenge an assumption

> *"We can't ship faster than bi-weekly — our release process takes two weeks."*

```
FIRST-PRINCIPLES ANALYSIS

Problem: Release cycle is 2 weeks minimum, blocking faster iteration.

Current approach: Code freeze → manual QA → staging deploy → sign-off from 3 teams → prod deploy

Decomposition:
  Code freeze period (3 days)      → ASSUMPTION (protects QA, but QA could run on PRs)
  Manual QA (5 days)               → ASSUMPTION (manual because test coverage is low, not by necessity)
  Staging environment validation   → FACT (need to verify behavior before prod)
  3-team sign-off (4 days)         → ASSUMPTION (legal/security/product — policy, not physics)
  Deployment itself                → FACT (takes ~40 minutes, irreducible)

Verified facts (irreducibly true):
- Deployment takes ~40 minutes
- Staging validation catches real bugs (data from last 6 releases)
- Legal sign-off is required for changes touching PII fields (actual regulation)

Challenged assumptions:
- Manual QA → because test coverage is 34%; fix is coverage, not manual process
- 3-team sign-off → only legal sign-off is legally required; product/security is policy
- Code freeze → protects nothing that CI on PRs wouldn't catch earlier

Rebuilt solutions:
  Option A: CI on every PR + automated QA → removes code freeze + manual QA → potential: daily deploys
  Option B: Risk-tiered releases — PII changes require legal sign-off, all others ship immediately
  Option C: Feature flags — decouple deploy from release; ship continuously, enable per segment

Selected: Option A + B combined — automated CI removes QA bottleneck; tiering removes unnecessary sign-offs

Stress-test: Coverage must reach >80% before removing manual QA or we trade speed for regressions.
             Start with non-PII services (3 of 7) while coverage climbs on the rest.
```

---

### `/pre-mortem` — Kill failure before it kills your project

> *"We're launching our mobile app in 8 weeks."*

```
PRE-MORTEM: Mobile app launch
Session date: 2026-06-26  |  Imagined failure date: 2026-08-21

FAILURE NARRATIVES

[Execution]
- We missed the launch date by 3 weeks because push notifications required an OS-level
  entitlement change that Apple took 2 weeks to approve and we discovered this in week 6.
- The app passed QA on iOS 17 but crashes on iOS 16 — still 31% of our user base.
  We found this at launch when 1-star reviews hit.

[Assumptions]
- We assumed 40% of beta users would convert to paid. Actual conversion was 6%.
  Paywall placement killed the activation moment before users saw core value.
- Backend was sized for 10k DAU. Launch PR drove 80k installs in 72 hours.
  API rate limits hit at hour 4. Service degraded for 18 hours.

[External]
- A competitor launched a free tier the week before our launch, repositioning us
  as the "expensive option" before we shipped a single review.
- App Store review took 9 days, not the expected 2. Launch week became launch week+1.

[Team/Process]
- The lead iOS engineer went on parental leave week 5. No knowledge transfer plan existed.
  Critical push notification implementation blocked for 10 days.

RANKED RISKS
#  | Failure Mode                                | Votes | Severity
1  | Backend capacity insufficient for viral spike|  8   | High
2  | App Store review delay                        |  7   | High
3  | iOS 16 compatibility not tested               |  6   | High
4  | Paywall kills activation before value moment  |  5   | Med
5  | Key engineer unavailable                      |  4   | Med

MITIGATION ACTIONS
1. Risk: Backend capacity
   Mitigation: Load test to 10× expected DAU; configure auto-scaling with tested runbook
   Owner: Platform lead
   Done when: Load test passes at 100k concurrent without degradation

2. Risk: App Store review delay
   Mitigation: Submit binary by week 6 (not week 8); build 2-week buffer into timeline
   Owner: Mobile lead
   Done when: Binary submitted by 2026-08-05

3. Risk: iOS 16 compatibility
   Mitigation: Add iOS 16.x device to QA matrix; run full regression suite on it
   Owner: QA lead
   Done when: iOS 16.4 test pass in CI pipeline
```

---

## All 54 Skills

| Skill | What it does |
|---|---|
| `/5w2h` | Define any task or problem completely: What, Why, Where, When, Who, How, How Much. |
| `/aarrr-pirate-metrics` | Measure startup/product growth across Acquisition, Activation, Retention, Referral, Revenue. |
| `/ansoff-matrix` | Choose growth strategy — Market Penetration, Market Development, Product Development, or Diversification. |
| `/balanced-scorecard` | Translate strategy into metrics across Financial, Customer, Internal Process, and Learning & Growth perspectives. |
| `/bcg-matrix` | Classify portfolio items as Stars, Cash Cows, Question Marks, or Dogs by market share and growth. |
| `/business-model-canvas` | Design or audit a business model across 9 blocks: segments, value props, channels, relationships, revenue, resources, activities, partners, costs. |
| `/clear-framework` | Set goals that are Collaborative, Limited, Emotional, Appreciable, Refinable — built for dynamic environments. |
| `/customer-journey-map` | Visualize every touchpoint a customer has with a product or service — stages, actions, emotions, pain points, opportunities. |
| `/cynefin-framework` | Match decision-making approach to context complexity: Clear, Complicated, Complex, Chaotic, Confused. |
| `/daci` | Assign decision roles: Driver (moves it forward), Approver (decides), Contributors (advise), Informed (notified). |
| `/double-diamond` | Design problems with two diamond phases: Discover/Define (right problem), Develop/Deliver (right solution). |
| `/errc-grid` | Create blue ocean strategy by deciding what to Eliminate, Reduce, Raise, and Create vs the industry standard. |
| `/feedback-analysis` | Track predictions vs actual outcomes over time to identify true strengths and blind spots. |
| `/first-principles` | Break problems down to fundamental truths and rebuild solutions from scratch — stripping away assumptions. |
| `/fishbone-diagram` | Map causes of a problem across categories (People, Process, Technology, Environment, etc.) to find root drivers. |
| `/five-whys` | Find root cause of a problem by asking "Why?" five times — moving from symptom to systemic cause. |
| `/force-field-analysis` | Map driving forces (pushing toward change) vs restraining forces (resisting change) to plan change management. |
| `/inversion` | Solve forward problems by thinking backward: instead of 'how to succeed', ask 'how to fail' then avoid it. |
| `/jobs-to-be-done` | Identify what customers hire a product to accomplish — functional, social, and emotional jobs. |
| `/kano-model` | Classify features as Basic, Performance, or Delight to optimize satisfaction and product investment. |
| `/lean-canvas` | One-page business model for startups: Problem, Solution, UVP, Unfair Advantage, Channels, Segments, Revenue Streams, Cost Structure, Key Metrics. |
| `/marketing-mix-4ps` | Design or audit a go-to-market strategy across Product, Price, Place, and Promotion. |
| `/mckinsey-7s` | Align organizations across Strategy, Structure, Systems, Shared Values, Skills, Style, and Staff. |
| `/mece` | Structure any analysis or communication so items are Mutually Exclusive and Collectively Exhaustive — no gaps, no overlaps. |
| `/moscow` | Prioritize scope into Must Have, Should Have, Could Have, and Won't Have for delivery planning. |
| `/north-star-metric` | Identify the single metric that best captures the value delivered to customers and aligns the whole team. |
| `/okr` | Align teams with ambitious Objectives and measurable Key Results on a quarterly cycle. |
| `/pareto-analysis` | Apply the 80/20 rule: find the 20% of causes that drive 80% of effects to focus effort where it matters most. |
| `/pdca` | Drive continuous improvement through iterative Plan → Do → Check → Act cycles. |
| `/pestle` | Audit external macro-environment across Political, Economic, Social, Technological, Legal, Environmental dimensions. |
| `/porters-five-forces` | Assess industry competitiveness via Threat of Entry, Supplier Power, Buyer Power, Substitutes, and Rivalry. |
| `/porters-value-chain` | Identify competitive advantage by auditing primary activities (inbound, ops, outbound, marketing, service) and support activities. |
| `/pre-mortem` | Prevent failure by imagining the project has failed, then working backward to identify what went wrong. |
| `/pure` | Validate goals are Positively stated, Understood, Relevant, Ethical. |
| `/pyramid-principle` | Structure communication top-down: lead with the answer, then group supporting arguments, then evidence below each. |
| `/raci` | Clarify roles on any task or decision: Responsible, Accountable, Consulted, Informed. |
| `/rapid-decision` | Clarify decision authority with five roles: Recommend, Agree, Perform, Input, Decide. |
| `/rice-scoring` | Prioritize features/projects by Reach, Impact, Confidence, and Effort into a single score. |
| `/scamper` | Generate creative ideas by applying seven lenses: Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse. |
| `/scqa` | Frame any communication as Situation → Complication → Question → Answer to create narrative tension and clarity. |
| `/second-order-thinking` | Anticipate downstream consequences of decisions by asking "and then what?" beyond the immediate effect. |
| `/smart` | Define goals as Specific, Measurable, Achievable, Relevant, Time-bound. |
| `/smeac` | Structure briefings as Situation, Mission, Execution, Administration/Logistics, Command/Communications. |
| `/soar-analysis` | Appreciative alternative to SWOT: Strengths, Opportunities, Aspirations, Results — focuses on possibility over deficit. |
| `/spin-selling` | Guide sales conversations through Situation, Problem, Implication, and Need-Payoff questions to surface and grow buyer need. |
| `/star-method` | Structure responses or case studies as Situation → Task → Action → Result for clear, evidence-based communication. |
| `/stp-framework` | Build a targeting strategy through Segmentation → Targeting → Positioning. |
| `/swot` | Analyze Strengths, Weaknesses, Opportunities, Threats for a subject to guide strategy. |
| `/the-eisenhower-matrix` | Prioritize tasks by urgency and importance into Do, Schedule, Delegate, Eliminate. |
| `/the-grow-model` | Coaching framework: Goal → Reality → Options → Will. Structure any problem-solving or coaching conversation. |
| `/the-project-portfolio-matrix` | Prioritize projects by strategic value vs effort/risk to allocate resources across a portfolio. |
| `/tows-matrix` | Generate strategic options by crossing SWOT quadrants: SO, ST, WO, WT strategies. |
| `/value-proposition-canvas` | Match customer jobs/pains/gains to product features/pain-relievers/gain-creators to validate product-market fit. |
| `/woop` | Turn wishes into action plans using mental contrasting: Wish → Outcome → Obstacle → Plan. |

---

## How it works

Each skill loads a full framework — definitions, step-by-step process, output template, and common mistakes — into the Claude Code context. You describe your situation; Claude applies the framework and returns structured analysis.

Works with Claude Code CLI, desktop app, and IDE extensions (VS Code, JetBrains).

---

## Contributing

New framework? Open a PR. Each skill is a single `SKILL.md` file in `skills/<name>/`.

See any existing skill for the format.
