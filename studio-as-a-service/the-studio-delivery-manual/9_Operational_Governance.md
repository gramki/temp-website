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

Rituals index (see sections 9.2–9.13 for run‑books):
- [9.2 Flight Check](#sec-9-2-flight) (Setup; Chair: Delivery Manager) — install ledgers, gates, dashboards
- [9.3 Daily Flow Stand‑up](#sec-9-3) (Team; Chair: Delivery Team Lead) — keep flow, surface blockers early
- [9.4 Weekly Health & Risk Review](#sec-9-4) (Program; Chair: Delivery Manager) — decide sequencing and risks (+ optional Dependency Huddle during spikes)
- [9.5 Backlog Grooming / Refinement](#sec-9-5-groom) (Chair: DPM) — make next 2–3 sprints Ready
- [9.6 Sprint Planning](#sec-9-6-planning) (Chair: Delivery Team Lead) — set sprint goal, commit to Ready items
- [9.7 Debt Clearance Review](#sec-9-7-debt) (Chair: Delivery Manager) — keep amortization ≥ accumulation
- [9.8 RfP Readiness Workshop](#sec-9-8-rfp) (Requirement→Feature Gate; Chair: DPO) — move MAR → RfP with signed Features
- [9.9 Monthly Operational Review](#sec-9-9-monthly) (Tactical Steering; Chair: Delivery Manager) — synthesize trends; propose decisions
- [9.10 Executive Steering Committee](#sec-9-10-steering) (Governance; Chair: Engagement Owner) — approve material trade‑offs; enforce thresholds

---

<a id="sec-9-2-flight"></a>
## 9.2 Flight Check (Foundational Setup)

Do this once, then audit monthly. A missing piece here becomes a month‑end surprise later.
- Jira structure: requirements/features traceability, labels (RfP, integration risk, decomposition, dependency), workflows
- RfP gate setup: MAR fields/templates, RfP criteria and labels, decomposition board, sign‑off workflow between Delivery Product Owner and Customer Product Manager
- Dashboards: requirements (Sec 5), quality (Sec 7), commercial SFM/TCM (Sec 8), operational (this section)
- Ledgers/registers: dependency register (owners, funding, lead‑time), debt portfolio (Sec 6), risk register
- Environments & access: cluster certification environment, secrets management, CI/CD pipelines, observability baseline
- Forum calendar: daily/weekly/monthly/Steering with owners, agendas, and packs

> Why This Matters: Most “governance problems” are missing ledgers, dashboards, or owners — not meetings.

---

<a id="sec-9-3"></a>
## 9.3 Daily Flow Rituals (Studio‑owned)

Purpose: maintain flow; surface blockers early; prevent same‑day surprises.
- Cadence: daily, 15 min, stand‑up format; +10–15 min board hygiene
- Inputs: sprint board, CI/test dashboard, dependency register deltas
- Agenda (round‑robin, time‑boxed):
  1) Yesterday’s outcome vs plan
  2) Today’s plan (one sentence)
  3) Blockers/risks (name owner, due date)
- Outputs/Artifacts: updated board; blocker list with owners/dates; escalations queued for Weekly Review
- Participants: Delivery Team Lead (chair), Delivery Product Manager (module), QA, Tech Lead/Principal Engineer; DevOps/Platform as needed
- Anti‑patterns: deep dives, problem‑solving live, status monologues

---

<a id="sec-9-4"></a>
## 9.4 Weekly Health & Risk Reviews (Studio‑owned)

Purpose: decide sequencing and risk treatments across squads; align to gates and budgets.
- Cadence: weekly 60–90 min
- Inputs: plan vs actual; quality (error budgets, leakage/flake); commercial (FVS/Capacity); dependency variance; debt trends
- Agenda:
  1) Threshold breaches first (requirements, quality, commercial, operational)
  2) Options/trade‑offs and owner actions
  3) CCB candidates and re‑estimates
- Outputs/Artifacts: decision log; owner/action/date; CCB items; Steering prep items
- Participants: Delivery Manager (chair), Delivery Product Owner, Delivery Product Managers, QA/Test Lead, Tech/Integration Leads, Squad Leads; optional: Studio Owner, Commercial, Customer PM
- Anti‑patterns: slide‑only reviews; no owner/dates; mixing Steering decisions

Optional: Dependency Huddle (spike‑only)
- Purpose: rapidly unblock high‑risk dependencies without adding a permanent meeting.
- Cadence: 15 minutes, up to twice weekly, limited to ≤ 3 weeks; then fold back into the standard Weekly Review.
- Inputs: dependency register with evidence and lead‑times; DependencyFunding% and variance; open owners/actions.
- Outputs: owner/date per dependency, escalation/funding decisions recorded, updated register.
- Anti‑patterns: open‑ended status sharing, no evidence, no owner/dates.

---

<a id="sec-9-5-groom"></a>
## 9.5 Backlog Grooming / Refinement (Studio‑owned)

Purpose: ensure the next 2–3 sprints have “Ready” work. Break Features (already in RfP) into well‑formed Stories with AC/NFR, estimates, test notes, and known dependencies.
- Cadence: weekly 60–90 minutes per subsystem/module
- Inputs: signed‑off Features (RfP), design note/impact assessment, dependency map, Definition of Ready, quality signals (flake/leakage), open spikes
- Agenda:
  1) Select top Features in priority order
  2) Decompose into Stories; write AC aligned to Feature AC; capture NFR and test notes
  3) Identify dependencies/spikes; assign owners and due dates
  4) Size Stories; confirm DoR; mark Ready or list gaps
- Outputs/Artifacts: Ready Stories with AC/NFR/estimates; spike tasks with owners/dates; updated dependency register; Ready coverage metric
- Participants: Delivery Product Manager (chair), Tech Lead/Principal Engineer, QA/Test Lead; optional: Engineering Manager, Delivery Product Owner for clarifications
- Non‑participants: Steering/executive roles; observers without agenda contributions — avoid crowding
- Anti‑patterns: solutioning beyond Story scope; “discovery” without capturing spikes; skipping AC/NFR; unestimated Stories marked Ready

> Pro Tip: Keep grooming tactical; design happens pre‑RfP. Grooming assures DoR and schedule realism.

---

<a id="sec-9-6-planning"></a>
## 9.6 Sprint Planning (Studio‑owned)

Purpose: agree on a sprint goal and commit to a feasible sprint backlog.
- Cadence: each sprint start; 60–120 minutes depending on team size
- Inputs: Ready Stories (9.5), team capacity, historical velocity, quality gates (error budget, flake/leakage — see Section 7), known dependencies and spikes
- Agenda:
  1) Propose sprint goal aligned to roadmap
  2) Select Ready Stories to meet goal; include repair/hardening as needed
  3) Check capacity: reserve for quality/debt; account for holidays/leave
  4) Identify risks and dependency calls this sprint; assign owners/dates
- Outputs/Artifacts: sprint goal; committed sprint backlog; capacity breakdown (feature, quality, debt); owner/date list for risks/dependencies
- Participants: Delivery Team Lead (chair), Engineering Manager, Delivery Product Manager, Tech Lead/Principal Engineer, QA/Test Lead
- Non‑participants: Steering/executive roles; extended stakeholders without immediate decision rights
- Guardrails: reserve 15–25% capacity for quality/debt; no unready work enters the sprint; if error budget is depleted (Section 7), prioritize stabilization over new intake
- Anti‑patterns: over‑commitment; planning with unready work; ignoring repair work; hours‑driven micro‑planning

---

<a id="sec-9-7-debt"></a>
## 9.7 Debt Clearance Review (Studio‑owned)

Purpose: keep debt amortization at least equal to accumulation and remove high‑risk shortcuts promptly.
- Cadence: weekly 30–45 minutes, or mid‑sprint as needed
- Inputs: debt portfolio (Section 6), error budgets (Section 7), stability signals, upcoming release risks, reserved capacity for paydowns
- Agenda:
  1) Review accumulation vs amortization trend; breach first
  2) Select highest risk/return paydowns; link each to a risk/quality signal
  3) Schedule paydowns within sprint or next; confirm owners/dates
- Outputs/Artifacts: scheduled clearance tasks; updated portfolio with reasons/impacts; capacity allocation visible on board
- Participants: Delivery Manager (chair), Tech Lead/Principal Engineer, QA/Test Lead, Delivery Product Manager; optional: DPO for customer‑visible trade‑offs
- Guardrails: cap to top 3 paydowns per cycle; maintain 10–20% amortization reserve by default; do not consume reserve for feature work
- Anti‑patterns: “nice‑to‑clean” tasks displacing risk‑reducing paydowns; no capacity reserved; no linkage to risk/quality signals

---

<a id="sec-9-8-rfp"></a>
## 9.8 RfP Readiness Workshop (Requirement→Feature Gate)
- Purpose: move Requirements from MAR → RfP with signed‑off Features
- Cadence: weekly 60–90 min; ad‑hoc for hot items; pre‑increment checkpoint
- Inputs: MAR fields, draft Features, initial AC/NFR, design note/doc, dependency map, Risk Surfaces
- Agenda:
  1) Top candidates (by priority/risk)
  2) Decompose to subsystem‑scoped Features; seed AC/NFR; identify spikes
  3) Confirm design/impact assessment readiness; list Risk Surfaces
  4) Customer sign‑off decision or actions to sign‑off
- Outputs/Artifacts: RfP labels set; signed Features; CRs for decomposition (if billable); blockers/owners; dependency/register updates
- Commercial note: requirement→feature decomposition is billable by default; tag Jira items with a decomposition label/field and link to the CR reference
- Anti‑patterns: solutioning without AC/NFR; skipping design/impact; unsigned Features entering planning

---

<a id="sec-9-9-monthly"></a>
## 9.9 Monthly Operational Review (Studio‑owned; feeds Steering)

Purpose: synthesize trends; recommend Steering decisions; update policies/thresholds as needed.
- Cadence: monthly 60–90 min
- Inputs: weekly packs; breaches; capacity/funding gaps; dependency register; incident post‑mortems
- Agenda:
  1) Top 5 risks with trend and impact
  2) Options with scope/date/capacity impacts
  3) Recommended decisions and threshold updates
- Outputs/Artifacts: decision papers for Steering; updated policies/threshold proposals and owners
- Decision paper (lightweight): context (1 para), options (2–3) with impacts, recommendation, cost/funding note, owner/date
- SLA: decisions turned around within 3 business days or escalated to Steering
- Participants: Delivery Manager (chair), Studio Owner, Delivery Product Owner, QA/Test Lead, Tech/Integration Leads, Risk/Dependency Owners; optional: EO Commercial, Customer PMO
- Anti‑patterns: Steering‑level debates here; lack of options or impact quantification

---

<a id="sec-9-10-steering"></a>
## 9.10 Executive Steering Committee (Governance/Steering)
- Purpose: approve material trade‑offs; enforce policy thresholds; unblock
- Cadence: monthly/quarterly or on breach; 60–90 min
- Inputs: decision papers with options/costs/risks; FVS/Capacity bands; escalations
- Agenda:
  1) Decisions required (time‑boxed)
  2) Policy/threshold changes
  3) Escalation outcomes and owners
- Outputs/Artifacts: approved changes (scope/capacity/dates/policy), recorded decisions and owners
- Decision paper template: same as 9.9; pre‑wire 48 hours ahead
- SLA: decision issuance within 3 business days; unresolved items return to 9.9 with next steps
- Participants: Engagement Owner (chair), Studio Owner, Delivery Manager, DPO, Customer execs/Product leadership; optional: Account/Commercial, Finance/Legal
- Anti‑patterns: unprepared topics; no options; decisions not recorded

---

<a id="sec-9-11-sprintend"></a>
## 9.11 Sprint‑End Learning & Stabilization Rituals (Studio‑owned)

Purpose: demonstrate value, stabilize risks, and improve the system.
- Cadence: each sprint end
- Components & signals:
  - **Feature Demo**: demonstrate against AC and listed Risk Surfaces; call out gaps explicitly
    - Participants (required): squad, Delivery Product Manager, QA/Test Lead; (optional) Delivery Product Owner, Customer stakeholders
  - **Mini Hardening Window** (0.5–1 day, time‑boxed): fix flaky tests/high‑risk areas; if error budget is depleted (Section 7), expand repair scope before new intake
    - Participants (required): engineers, QA/Test Lead; (optional) Technical/Integration Lead
  - **Retrospective**: 3 columns — what worked; what hurt; what we’ll change next sprint (max 3 actions)
    - Participants (required): full squad incl. DPM and QA; (optional) Delivery Manager for coaching
  - **Debt Roll‑call** (15 min): shortcuts taken, origin/reason, catch‑up plan link (Section 6)
    - Participants (required): squad, DPM, QA/Test Lead; (optional) Delivery Manager, Solution/Architecture lead
- Outputs: accepted items, repair tasks scheduled, retro actions (max 3, owned), updated debt portfolio and trends

> Pro Tip: Keep retro actions small and owned; large refactors belong in the plan with funding.

---

<a id="sec-9-12-metrics"></a>
## 9.12 Metrics Maturity Ladder (Evolve, don’t stall)

- Level 1 (Manual): spreadsheets, ad‑hoc reports; ledgers maintained; reviews run
- Level 2 (Automated): dashboards connected to Jira/CI/observability; alerts on thresholds
- Level 3 (Predictive): trend‑based forecasts (velocity bands, budget runway, leakage predictors); what‑if scenarios

Guardrails: do not skip levels; automate only after manual discipline exists; decommission stale widgets.

---

<a id="sec-9-13-dash"></a>
## 9.13 Dashboards, Alerts & Audience Assignment

### Dashboards (by audience)
- Team: today’s blockers, CI/test state, flaky tests, dependency calls, board aging, critical path pass rate, Ready coverage (next sprint), retro actions due
- Program (Studio): %RfP and volatility, RfP throughput and shelf‑life, quality gates and error budgets, FVS/Capacity Health, dependency variance, DependencyFunding% and Dependency Financial Risk ($), integration readiness index (Section 5.10), debt accumulation vs amortization trend, decision/action closure rate
- Steering (EO): release readiness and gating checks, top 5 risks with options, FVS/Capacity Health bands, unfunded/runway, dependency funding and financial risk, incident trend and MTTR impacting release

### Alerts (defaults; tune per program)
- Requirements: %RfP < 70% for next increment; volatility spike > 20%; RfP throughput below target 2 cycles; RfP shelf‑life > 2 sprints
- Backlog Readiness (TCM): Ready coverage < 1 sprint of planned capacity; spike outcomes overdue > 1 sprint
- Quality: error budget < 20%; leakage > threshold; flake > 5% (7‑day); critical path pass rate < 95%
- Commercial: FVS < 60 (SFM); Capacity Health < 60 (TCM); unfunded exposure > 10%
- Operational: dependency variance > threshold for 2 cycles; DependencyFunding% < target; integration readiness checklist incomplete within 2 sprints of planned start; idle time > 10% rolling (TCM)
- Governance Hygiene: decision log stale items > 14 days; retro action closure < 80% for 2 cycles; debt amortization < accumulation for 2 sprints

### Ritual → Primary signals
Use this map to focus each ritual on the few signals that matter most for decisions in that forum. It is not a full dashboard; it lists the minimum evidence to run the meeting well. If a primary signal is red or missing, resolve that gap first, then proceed with the agenda.
- 9.2 Flight Check: ledgers present, dashboards wired, RfP gate configured — If any of these are missing or stale, governance is blind. Set them up before the cadence starts; audit monthly so signals remain trustworthy.
- 9.3 Daily Flow: WIP/aging, CI/test state, today’s dependency calls — Aging work or red pipelines indicate today’s unblocks; confirm owners and outcomes of dependency calls to prevent idle time.
- 9.4 Weekly Review: gate breaches, FVS/Capacity bands, dependency variance — Triage by breach type first (requirement, quality, commercial), then check if funding/capacity are within bands; compare promised vs actual dependency lead‑times to decide escalations.
- 9.5 Grooming: Ready coverage, spike outcomes on time — Ensure 1–2 sprints of Ready work relative to capacity; overdue spikes signal unknowns that must be resolved before planning.
- 9.6 Sprint Planning: capacity reserve %, error budget state, committed vs velocity bands — Reserve 15–25% for quality/debt, pause new intake if error budget is depleted, and keep commitment within historic velocity bands to avoid thrash.
- 9.7 Debt Clearance: amortization vs accumulation, high‑risk shortcuts outstanding — If accumulation outpaces amortization, schedule top paydowns now; prioritize shortcuts tied to incidents or stability risks.
- 9.8 RfP Workshop: %RfP for next increment, shelf‑life, dependency readiness — Maintain sufficient signed‑off Features ahead of planning; stale items indicate churn; verify integration readiness (contracts, test creds, environments) before green‑lighting.
- 9.9 Monthly: top risks with trend, funding/runway, incident trends — Use trends, not snapshots, to propose trade‑offs; ensure runway/funding are sufficient through the next increment; show incident MTTR/recurrence that threaten releases.
- 9.10 Steering: decision backlog age, policy threshold changes queued — Escalate only the decisions that unblock scope/date/capacity; propose policy/threshold changes when repeated breaches show current limits are unrealistic.

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

6) Make dependencies real
- Keep a living dependency register with evidence, lead‑times, and funding status; track Delivery vs Dependency variance separately; escalate early when lead‑times slip.

7) Decision hygiene
- Maintain a decision log; time‑box decisions; favor reversible decisions to unblock; always record owner and effective date.

8) Pre‑wire Steering
- Circulate decision papers 48 hours ahead; present 2–3 options with scope/date/capacity impacts; ask for a choice, not a debate.

9) RfP discipline is non‑negotiable
- Do not decompose Features without design note/impact assessment; get Customer sign‑off; log billable decomposition via CR where applicable.

10) Stabilize before speed
- Respect hardening windows; cap WIP when error budgets deplete; pause new intake until critical path is green.

11) Change the system, not the people
- If the same breach recurs for two cycles, treat it as a system constraint. Adjust cadence, thresholds, or policy rather than coaching the same behavior again. The goal is to change the conditions that produce the breach.

When to act
- Act when any of these persist for two cycles: threshold breach, error‑budget depletion, Ready coverage below target, or missed dependency lead‑times. Two cycles establishes a pattern, not noise.

How to act (use existing forums)
- Pick one or two levers and time‑box them for the next two sprints. Examples: cap WIP; tighten or relax RfP criteria; lengthen a mini hardening window; temporarily shift an existing weekly risk review to twice‑weekly during the spike; move decision rights closer to the work; add an integration readiness check inside the RfP Readiness Workshop. Do not create new meetings—extend the scope or cadence of forums you already run, then revert when the constraint clears.

Illustration (Payments dispute flow)
- Leakage stayed above threshold for two sprints, driven by flaky component tests and late dependency payload changes. We capped parallel feature work to two items, added a pre‑merge component‑test gate, and extended the existing Weekly Health & Risk Review to include a 10‑minute dependency evidence check. In two sprints, flake fell by 60%, leakage returned below threshold, and demos were predictable again.

> VP Reflection: "Good governance is quiet. If the meetings are calm and short, the system is working."
