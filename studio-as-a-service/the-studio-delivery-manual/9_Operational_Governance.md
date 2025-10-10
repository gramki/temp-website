# 9. Operational Governance & Delivery Discipline

## Purpose

Make delivery predictable with lightweight but reliable rituals, clear ownership of forums (EO vs Studio), early‑warning dashboards, and an explicit maturity path. Rituals replace heroics.

> VP Reflection: "When the system of rituals is healthy, escalation becomes rare and boring. That’s the goal."

---

## 9.1 Tiered Rituals (Why, When, Who)

- Principles
  - Few rituals, done well, beat many rituals, done poorly.
  - Every ritual has inputs, outputs, and a single accountable chair.
  - Label owning org and chair on every invite to avoid shadow governance.

### Daily (Team‑level; Chair: Delivery Team Lead)
- Purpose: flow, blockers, handoffs, today’s risks
- Inputs: board, test/CI status, dependency register updates
- Outputs: updated plan of day, escalations to Weekly Review where needed

### Weekly (Program‑level; Chair: Delivery Manager, Studio)
- Purpose: health and risk review across squads/subsystems
- Inputs: plan vs actual, quality error budgets, commercial signals (per Section 8), dependency register deltas
- Outputs: decisions on sequencing, owner actions, CCB items

### Monthly (Tactical Steering; Chair: Delivery Manager, Studio)
- Purpose: operational deep dive; prepare Steering (EO)
- Inputs: weekly trends, threshold breaches, capacity/funding gaps
- Outputs: recommendations and decision papers for Steering

### Steering (Governance/Steering; Chair: Engagement Owner, EO)
- Purpose: decide material trade‑offs; enforce policy thresholds; unblock
- Inputs: escalations from Monthly Review, options with impacts
- Outputs: approved changes (scope/capacity/dates/policy), recorded decisions

---

## 9.2 Flight Check (Foundational Setup)

Do this once, then audit monthly. A missing piece here becomes a month‑end surprise later.
- Jira structure: requirements/features traceability, labels (RfP, integration risk, decomposition, dependency), workflows
- Dashboards: requirements (Sec 5), quality (Sec 7), commercial SFM/TCM (Sec 8), operational (this section)
- Ledgers/registers: dependency register (owners, funding, lead‑time), debt portfolio (Sec 6), risk register
- Environments & access: cluster certification environment, secrets management, CI/CD pipelines, observability baseline
- Forum calendar: daily/weekly/monthly/Steering with owners, agendas, and packs

> Why This Matters: Most “governance problems” are missing ledgers, dashboards, or owners — not meetings.

---

## 9.3 Daily Flow Rituals (Studio‑owned)

- Stand‑up (15 min): plan of day, unblock, today’s test/CI state, dependency calls
- Board hygiene (10–15 min after stand‑up): WIP limits, aging items, blocked reasons
- Quality snapshot: error budget remaining, flaky tests quarantined, critical path failures
- Operational notes: today’s change windows, access keys/certs expiring

Outputs: updated board, explicit escalations, owner assignments with dates.

---

## 9.4 Weekly Health & Risk Reviews (Studio‑owned)

Scope: program cross‑squad review (60–90 min)
- Health signals
  - Requirements: %RfP, volatility, missing AC (Sec 5)
  - Quality: critical path pass rate, leakage/flake, error budgets (Sec 7)
  - Commercial (SFM/TCM): FVS or Capacity Health Score, unfunded exposure/runway (Sec 8)
  - Operational: dependency variance, idle time (TCM), incident review
- Agenda
  - Threshold breaches first; owner action plans
  - Sequencing decisions, re‑estimates, CCB candidates
  - Debt/refinement paydowns linked to upcoming features (Sec 6)

Outputs: summarized pack to Monthly Operational Review; updated risks with owners/dates.

---

## 9.5 Sprint‑End Learning & Stabilization Rituals (Studio‑owned)

- Demo against AC and risk surfaces; call out gaps explicitly
- Mini hardening window (time‑boxed) for flaky tests/high‑risk areas
- Retrospective with 3 columns: what worked; what hurt; what we’ll change next sprint (max 3 actions)
- Debt roll‑call (15 min): shortcuts taken, origin/reason, catch‑up plan link (Sec 6)

> Pro Tip: Keep retro actions small and owned; large refactors belong in the plan with funding.

---

## 9.6 Monthly Operational Review (Studio‑owned; feeds Steering)

- Inputs: weekly trend packs; threshold breaches; dependency register; FVS/Capacity Health; error budgets; incident post‑mortems
- Agenda: top risks, options with impacts (scope/date/capacity), recommends decisions to Steering
- Outputs: decision papers and proposed forum agendas; policy threshold updates if needed

---

## 9.7 Metrics Maturity Ladder (Evolve, don’t stall)

- Level 1 (Manual): spreadsheets, ad‑hoc reports; ledgers maintained; reviews run
- Level 2 (Automated): dashboards connected to Jira/CI/observability; alerts on thresholds
- Level 3 (Predictive): trend‑based forecasts (velocity bands, budget runway, leakage predictors); what‑if scenarios

Guardrails: do not skip levels; automate only after manual discipline exists; decommission stale widgets.

---

## 9.8 Dashboards, Alerts & Audience Assignment

### Dashboards (by audience)
- Team: today’s blockers, CI/test state, flaky tests, dependency calls, board aging
- Program (Studio): %RfP/volatility, quality gates, FVS/Capacity Health, dependency variance, debt hot‑spots
- Steering (EO): release readiness, top 5 risks with options, FVS/Capacity Health bands, unfunded/runway, gating alerts

### Alerts (defaults; tune per program)
- Requirements: %RfP < 70% for next increment; volatility spike > 20%
- Quality: error budget < 20%; leakage > threshold; flake > 5% (7‑day)
- Commercial: FVS < 60 (SFM); Capacity Health < 60 (TCM); unfunded exposure > 10%
- Operational: dependency variance > threshold for 2 cycles; idle time > 10% rolling (TCM)

> Caution: Fewer, better metrics. Choose 8–12 signals per audience.

---

## Practitioner Guidance (Operational Play)

1) Label owners and forums
- Every ritual has a chair and outputs; record decisions; avoid parallel “side‑governance.”

2) Start with manual, graduate to automated
- Get the ledgers/dashboards right manually; then automate and prune.

3) Escalate with options, not alarms
- Bring 2–3 options with impacts; ask Steering to choose trade‑offs.

4) Protect the runway
- Keep Ready backlog (TCM) and funded scope (SFM) visible; act before cliffs.

5) Debt is part of the plan
- Reserve capacity for paydowns; never let accumulation outpace amortization.

> VP Reflection: "Good governance is quiet. If the meetings are calm and short, the system is working."
