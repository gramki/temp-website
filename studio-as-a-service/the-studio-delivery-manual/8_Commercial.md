# 8. Commercial Models & Governance Alignment

## Purpose

Align commercial mechanics with delivery reality: estimate with variance, manage change transparently, surface funding health early, and anchor decisions in clear governance (EO vs Studio ownership).

> VP Insight: "Commercial clarity prevents technical heroics from becoming financial accidents."

### Commercial Models and Naming (Use consistently)
- Scope‑Funded Model (SFM): Budget and approvals are tied to defined scope (requirements/features/epics) with CRs to evolve scope, cost, or dates.
- Team‑Capacity Model (TCM): Budget and approvals are tied to a defined team mix/capacity (scrum team model); scope evolves incrementally by iteration.

Use “SFM” and “TCM” prefixes to avoid confusion.

### Quick Comparison (When to use which)
| Aspect | SFM (Scope‑Funded Model) | TCM (Team‑Capacity Model) |
|---|---|---|
| Primary commitment | Scope + CRs | Capacity (team‑weeks) |
| Planning unit | Features/Requirements | Iterations (sprints), rolling plan |
| Health signal | Funding Visibility Score | Capacity Health Score |
| Main risks | Unfunded exposure; dependency gates | Demand starvation; idle time; dependency variance |
| Forums | Steering/CCB/Operational | Same, with mix/idle‑time focus |

### Crib Sheet: SFM vs TCM (At a glance)
- When to choose
  - SFM: scope is largely knowable upfront; compliance/contracted deliverables; fixed outcomes or milestone funding; multi‑vendor coordination needs hard gates.
  - TCM: scope evolves by discovery; product/platform teams; long‑running streams; demand may fluctuate and needs runway/idle‑time protections.
 - When NOT to choose (even if requested)
   - SFM: do not agree when (i) scope is highly volatile or ill‑defined and Customer resists CR discipline; (ii) material dependencies are outside Customer control or unfunded; (iii) regulatory/compliance approvals are uncertain in timing; (iv) integration unknowns dominate and discovery is required; prefer a discovery phase or TCM until uncertainty reduces.
   - TCM: do not agree when (i) there are fixed deliverables with regulatory/milestone dates and penalties; (ii) procurement/legal require fixed outcomes or capped budgets; (iii) Customer refuses idle‑time/standby protections or runway governance; (iv) funding is episodic and cannot assure capacity runway; prefer SFM for those deliverables or a hybrid with SFM‑bounded increments.
- Key risks
  - SFM: unfunded exposure; dependency gates slipping; “approved in principle” CRs without budget; premature date hardening.
  - TCM: demand starvation; idle time; dependency variance stalling squads; unmanaged mix swaps.
- What to watch (widgets)
  - SFM: Unfunded CR Exposure; % RfP Signed; Funding Visibility Score; Dependency Funding & Lead‑time; Dependency Variance; Dependency Financial Risk.
  - TCM: Funded Capacity Coverage (weeks); Backlog Readiness Coverage (sprints); Velocity band vs actual; Idle time %; Dependency Variance; Capacity Health Score.
- Gate rules
  - SFM: If Funding Visibility Score < 60 → do not harden dates; bring options to Steering.
  - TCM: If Capacity Health Score < 60 → pause ramps/commitments; recover runway before scaling.
- Deep dives: see [8A. Scope‑Funded Model (SFM)](#8a-scope-funded-model-sfm) and [8B. Team‑Capacity Model (TCM)](#8b-team-capacity-model-tcm).

### Model Selection Flow (Mermaid)
```mermaid
graph TD
  A[Start: Engagement context] --> B{Is scope largely knowable upfront?}
  B -- Yes --> C{Are regulatory/milestone dates fixed with penalties?}
  B -- No --> D{Is the product a long-running stream with evolving scope?}
  C -- Yes --> E[SFM]
  C -- No --> F{Are dependencies/funding within Customer control?}
  F -- Yes --> E
  F -- No --> G[Discovery (time-box) then decide]
  D -- Yes --> H{Will Customer accept runway/idle-time protections?}
  D -- No --> G
  H -- Yes --> I[TCM]
  H -- No --> J{Can we bound a fixed increment with SFM?}
  J -- Yes --> K[Hybrid: SFM-bounded increments; revisit]
  J -- No --> G

  subgraph Guardrails
    E --> E1[If FVS < 60, do not harden dates]
    I --> I1[If CHS < 60, pause ramps/commitments]
  end
```

---

## 8A. Scope‑Funded Model (SFM)

### A1. Estimation with Variance Bands

- Estimation Policy
  - Feature‑level estimates carry variance bands by maturity:
    - Discovery (pre‑decomposition): ±30–50%
    - RfP (features signed off): ±20–30%
    - Planned (design sign‑off complete): ±10–20%
  - Publish bands with each estimate; update on decomposition/design sign‑off.
- Re‑estimation Rules
  - Trigger a variance review if re‑estimates exceed 20% of prior baseline or if two consecutive sprints show negative drift.
  - Document drivers (scope clarification, constraints, dependency shifts) and update the plan, funding, and dates.

> Pro Tip: Estimates without bands aren’t estimates — they’re wishes.

### A2. Change Management (CR) Lifecycle

- Stages: Intake → Impact (time/cost/risk/owner) → Approval → Execution → Closure
- Impact Template
  - Time: change to schedule milestones
  - Cost: delivery effort, third‑party costs, environments
  - Risk: delivery risk, quality risk, commercial exposure
  - Owner: who funds (Customer / Delivery Team / shared) and decision forum
- Decision Rights
  - Studio (Delivery Manager): approves zero‑cost/low‑risk changes within reserved buffer
  - CCB (Studio‑owned): approves mid‑range changes within budget guardrails
  - Steering (EO‑owned): approves material scope/cost/date changes or policy exceptions

> Why This Matters: CRs are where trust compacts are tested. Make the trade‑offs explicit.

### A3. Commercial Health Dashboard & Funding Visibility Score

- What question this answers
  - “Can we continue at the current delivery pace with the money and approvals we have?” The score converts scattered commercial signals into a single action‑oriented view for Steering and Studio.

- What counts as a dependency (examples)
  - Internal: Security reviews, data‑platform changes, shared schema migrations, infra quotas/capacity, scheduled change windows, SOX/PCI sign‑offs.
  - External: Provider API quota upgrades, new certs/mTLS onboarding, third‑party sandbox/prod access, card‑network/host changes.
  - Nature: Outside the Delivery Team’s control; can block or re‑sequence Studio plans and budgets.

- Dependency register (critical only) — evidence fields
  - Criticality (Y/N), Owner (team/org), Funding status (Approved CR/PO id / Pending / None), Lead‑time commitment (date or SLA link), Contract/Access readiness (Y/N).
  - Dependency Funding & Lead‑time Score (per dependency): 1.0 if Funding=Approved AND Lead‑time=Committed; 0.5 if only one true; 0.0 if neither.
  - DependencyFunding% = (Σ per‑dependency score ÷ count of critical dependencies) × 100.

- Funding Visibility Score (0–100)
  - Inputs (weighted) and how to compute:
    - % RfP with signed features (20): count(requirements with signed features) ÷ count(total in current/next increment) × 100
    - % budget backed by approved CRs/funding (30): (approved funding for in‑scope work ÷ total forecast for in‑scope work) × 100
    - Unfunded exposure (20, inverted): exposure% = (unfunded scope ÷ total in‑scope) × 100; contribution = 100 − exposure%
    - Delivery variance last 2 cycles (15, inverted): var% = avg(|forecast − actual| ÷ forecast) × 100 for Studio‑owned work; contribution = 100 − var%
    - Dependency variance last 2 cycles (10, inverted): depVar% = avg(|promised lead‑time − actual| ÷ promised) × 100 on critical dependencies; contribution = 100 − depVar%
    - Dependency funding & lead‑time (5): DependencyFunding% from the register
  - Bands & actions
    - 80–100 Healthy: proceed; minor watch items only
    - 60–79 Watch: list top 3 gaps; Steering review with options (de‑scope, fund, re‑sequence)
    - <60 At Risk: freeze on net new scope; re‑baseline or add funding before committing dates

- Dashboard Widgets (and why)
  - Unfunded CR Exposure ($ and %): makes invisible commitments visible; primary freeze trigger
  - Forecast vs Actual (current + last two cycles): distinguishes one‑off miss from trend (Studio‑owned)
  - Dependency Variance (current + last two cycles): separates dependency slippage from delivery variance
  - Dependency Funding & Lead‑time (percentage): ensures gates are financed and time‑boxed
  - Dependency Financial Risk ($): cost‑of‑wait (burn rate × idle days), rework, expedite/premium fees, new tooling/license — from the dependency financial ledger
  - Funding Visibility Score trend (8 weeks): shows whether we are stabilizing or deteriorating
  - Top 5 commercial risks and owners: puts names next to problems to accelerate resolution

- Worked example
  - Context: Next 2 months scope forecast = $1.0M; approved funding = $0.78M; unfunded exposure = $0.22M (22%)
  - RfP signed = 70%; Delivery variance (2 cycles avg) = 9%; Dependency variance = 15%; DependencyFunding% = 60%
  - Score calculation (illustrative):
    - RfP: 70 × 0.20 = 14.0
    - Budget backed: 78 × 0.30 = 23.4
    - Unfunded exposure: (100 − 22) × 0.20 = 15.6
    - Delivery variance: (100 − 9) × 0.15 = 13.65
    - Dependency variance: (100 − 15) × 0.10 = 8.5
    - Dependency funding: 60 × 0.05 = 3.0
    - Total ≈ 78.15 (Watch)
  - Actions: bring a Steering paper with three options — (A) fund $220k gap; (B) de‑scope $220k of low value; (C) re‑sequence to reduce near‑term exposure. Recommend A+B split.

- Operating guidance
  - Cadence: refresh weekly; present trend bi‑weekly at CCB; monthly at Steering
  - RACI: Studio compiles; EO Commercial validates; Steering decides on gaps
  - Data sources: Jira (RfP/CRs), planning tool (forecast), dependency register (funding/lead‑time/financial risk)
  - Guardrails: never commit milestone dates if score < 60; if 60–79, require a funded plan to reach ≥80 before date hardening

- Anti‑patterns (avoid)
  - Vanity green: excluding unfunded work from the denominator to inflate the score
  - Zombie CRs: “approved in principle” without budget line — treat as unfunded
  - Forecast optimism: using un‑re‑estimated numbers after scope/constraints changed

> From the Field: Publishing unfunded exposure early prevented three “late surprises” and saved a quarter’s worth of relationship capital.

### A4. Alerts & Escalations (SFM)
- Unfunded CR Exposure > 10% of remaining scope → Steering agenda
- Forecast Variance > 8% for two consecutive cycles (delivery) → re‑baseline review
- Dependency Variance > 12% for two consecutive cycles → re‑sequence plan and owner action
- Funding Visibility Score < 60 for 2 weeks → executive check‑in
- Dependency Financial Risk > [$X or Y% of forecast] → Steering escalation

---

## 8B. Team‑Capacity Model (TCM)

### B1. Capacity Health Score & Dashboard

- Capacity Health Score (0–100)
  - Inputs (weighted):
    - Funded Capacity Coverage (weeks) (35): min(coverageWeeks ÷ targetWeeks, 1.0) × 100
    - Backlog Readiness Coverage (sprints) (25): min(readySprints ÷ targetSprints, 1.0) × 100
    - Delivery variance vs velocity band (20, inverted): band miss% × 100; contribute = 100 − miss%
    - Dependency variance (10, inverted): depVar% × 100; contribute = 100 − depVar%
    - Idle time (10, inverted): idle% × 100; contribute = 100 − idle%
  - Bands: ≥80 Healthy; 60–79 Watch; <60 At Risk
- Dashboard Widgets
  - Ready backlog runway (sprints), Funded capacity runway (weeks)
  - Idle time and causes with owners; Dependency variance; Capacity Health Score trend
  - Velocity band vs actual
- Actions
  - <60: pause ramp; resolve dependency starvation/demand gaps; enforce idle‑time protections
  - 60–79: Steering options — add funding, improve demand, or re‑sequence

### B2. Governance & Decision Mechanics
- Steering (EO‑owned; Chair: Engagement Owner): capacity/rate/term changes; enforce idle‑time protections; resolve demand starvation
- CCB (Studio‑owned): mix swaps within envelope; throughput targets; dependency actions
- Operational Review (Studio‑owned): backlog readiness runway; funded capacity runway; velocity vs band; idle time

### B3. Alerts & Escalations (TCM)
- Funded Capacity Coverage < 6 weeks → Steering agenda
- Backlog Readiness < 2 sprints for 2 consecutive weeks → demand escalation
- Idle time > 10% (rolling 4 weeks) with Dependency variance > threshold → dependency escalation + charge protection

### B4. Contract‑Ready Clauses (TCM)
- Capacity, Mix, and Idle‑Time Protection. The Parties agree on the minimum monthly capacity (team‑weeks), permitted mix swaps within envelope, price/indexation rules, and notice periods for ramp up/down. If dependency/demand starvation exceeds the agreed grace period, standby/idle‑time protections apply (billable standby or redeploy by mutual agreement).
- Planning Cadence. The Parties shall run a rolling quarterly plan, monthly reforecast, and sprint‑level execution. Backlog Readiness Coverage (percentage of next 2–3 sprints groomed to Ready) and Funded Capacity Coverage (team‑weeks funded for next 8–12 weeks) shall be reported monthly.

---

## 8C. Common Provisions & Governance

### C1. Forum Ownership (Applies to SFM and TCM)
- Steering (EO‑owned; Chair: Engagement Owner)
  - Decides: material scope/cost/date (SFM) or capacity/rate/term (TCM); policy thresholds; escalation outcomes
- CCB / Commercial Review (Studio‑owned; Chair: Delivery Manager)
  - Decides: CR approvals within guardrails (SFM); mix/throughput changes within envelope (TCM)
- Operational Review (Studio‑owned; Chair: Delivery Manager)
  - Monitors: plan vs actual, burn vs budget or capacity, early risk indicators; feeds Steering

### C2. Contract Provisions (Common)
- Governance. Steering is chaired by the Engagement Owner (EO org); CCB and Operational Reviews are chaired by the Delivery Manager (Studio org). Decisions taken in these forums supersede informal communications and shall be recorded.
- Exclusions. The Delivery Team shall not be responsible for costs or delays caused by (i) unapproved scope (SFM), (ii) customer‑owned dependencies or environments, or (iii) third‑party constraints outside Delivery Team control, unless specifically assumed in an approved CR or capacity change.

---

## Practitioner Guidance (Commercial Play)

1) Publish the band with the number (SFM)
- Show the estimate and its variance; update when maturity changes.

2) Surface unfunded exposure weekly (SFM)
- Unfunded work is silent risk. Put it on a chart.

3) Tie decisions to forums (Common)
- Move debates into CCB/Steering; record decisions; stop hallway renegotiations.

4) Hold the line on buffers (SFM)
- Buffers are policy; spending them requires the same formality as adding scope.

5) Escalate early with options (Common)
- Bring trade‑offs (scope, date, budget/capacity) with impacts and owners.

6) Keep the runway visible (TCM)
- Maintain ≥ 2–3 sprints of Ready backlog and ≥ 8–12 weeks funded capacity; escalate when either dips.

7) Protect the team from starvation (TCM)
- Track idle time and its causes; enforce standby protections when dependency/demand starvation exceeds grace.

8) Manage mix, not people (TCM)
- Use the CCB to swap skills within the envelope; avoid ad‑hoc reshuffles that erode throughput and morale.

> VP Reflection: "Commercial discipline is delivery discipline written in dollars and dates."
