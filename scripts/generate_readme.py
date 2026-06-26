#!/usr/bin/env python3
"""Generate README.md and demo GIFs from skills directory."""

import os
import re
import subprocess
import sys
import threading

REPO_ROOT = os.path.dirname(os.path.dirname(__file__))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")
README_PATH = os.path.join(REPO_ROOT, "README.md")


def parse_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"')
    return fm


def extract_overview_diagram(skill_name):
    """Extract first code block from ## Overview section of a SKILL.md."""
    path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
    with open(path, encoding="utf-8") as f:
        content = f.read()
    overview = re.search(r"## Overview\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if not overview:
        return None
    block = re.search(r"```[^\n]*\n(.*?)```", overview.group(1), re.DOTALL)
    if not block:
        return None
    return block.group(1).rstrip()


def load_skills():
    skills = []
    for name in sorted(os.listdir(SKILLS_DIR)):
        skill_path = os.path.join(SKILLS_DIR, name, "SKILL.md")
        if not os.path.isfile(skill_path):
            continue
        fm = parse_frontmatter(skill_path)
        if fm.get("name") and fm.get("description"):
            skills.append({"name": fm["name"], "description": fm["description"]})
    return skills


def build_skills_table(skills):
    rows = ["| Skill | What it does |", "|---|---|"]
    for s in skills:
        rows.append(f"| `/{s['name']}` | {s['description']} |")
    return "\n".join(rows)


def build_readme(skills):
    count = len(skills)
    skills_table = build_skills_table(skills)

    swot_diagram = extract_overview_diagram("swot")
    fp_diagram = extract_overview_diagram("first-principles")
    pm_diagram = extract_overview_diagram("pre-mortem")

    swot_diagram_block = f"```\n{swot_diagram}\n```\n\n" if swot_diagram else ""
    fp_diagram_block = f"```\n{fp_diagram}\n```\n\n" if fp_diagram else ""
    pm_diagram_block = f"```\n{pm_diagram}\n```\n\n" if pm_diagram else ""

    return f"""# instinct

**{count} strategy and decision frameworks as Claude Code slash commands.**

Run SWOT, OKR, First Principles, Pre-Mortem, RICE, and {count - 5} more — directly in your terminal. No tab switching. No blank-page paralysis. Type a command, describe your situation, get a structured analysis.

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

![swot demo](assets/demo-swot.gif)

{swot_diagram_block}> *"Should we rewrite our monolith into microservices?"*

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

![first-principles demo](assets/demo-first-principles.gif)

{fp_diagram_block}> *"We can't ship faster than bi-weekly — our release process takes two weeks."*

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

![pre-mortem demo](assets/demo-pre-mortem.gif)

{pm_diagram_block}> *"We're launching our mobile app in 8 weeks."*

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

## All {count} Skills

{skills_table}

---

## How it works

Each skill loads a full framework — definitions, step-by-step process, output template, and common mistakes — into the Claude Code context. You describe your situation; Claude applies the framework and returns structured analysis.

Works with Claude Code CLI, desktop app, and IDE extensions (VS Code, JetBrains).

---

## Contributing

New framework? Open a PR. Each skill is a single `SKILL.md` file in `skills/<name>/`.

See any existing skill for the format.
"""


DEMOS = [
    {"tape": "scripts/demo-swot.tape",            "gif": "assets/demo-swot.gif"},
    {"tape": "scripts/demo-first-principles.tape", "gif": "assets/demo-first-principles.gif"},
    {"tape": "scripts/demo-pre-mortem.tape",       "gif": "assets/demo-pre-mortem.gif"},
]


def generate_gif(demo):
    tape = os.path.join(REPO_ROOT, demo["tape"])
    gif  = os.path.join(REPO_ROOT, demo["gif"])
    if os.path.exists(gif):
        os.remove(gif)
    result = subprocess.run(
        ["vhs", tape],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"vhs failed for {demo['tape']}:\n{result.stderr}", file=sys.stderr)
    else:
        print(f"Generated {demo['gif']}")


def generate_gifs():
    threads = [threading.Thread(target=generate_gif, args=(d,)) for d in DEMOS]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    gifs = "--gifs" in sys.argv

    skills = load_skills()
    readme = build_readme(skills)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"Generated README.md with {len(skills)} skills.")

    if gifs:
        print("Recording demo GIFs (parallel)...")
        generate_gifs()
