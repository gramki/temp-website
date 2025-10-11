# Appendix E — Operational Ritual Templates

Use these templates to run forums consistently. Each template ends with “Why This Exists” so new participants understand the purpose beyond the mechanics.

---

## E.1 Daily Flow Stand‑up (Section 9.3)

Purpose
- Keep work flowing by surfacing today’s blockers and making owner/date assignments.

Cadence/Timebox
- Daily; 15 minutes; +10–15 minutes board hygiene after the stand‑up.

Inputs
- Sprint board; CI/test state; dependency call sheet for the day.

Agenda
1) Yesterday’s outcome vs plan (brief)
2) Today’s plan (one sentence per person)
3) Blockers/risks (name owner/date)

Outputs/Artifacts
- Updated board; blocker list with owners/dates; queued escalations for Weekly Review.

Participants
- Delivery Team Lead (chair), DPM, QA, Tech/Principal Engineer; DevOps/Platform as needed.

Anti‑patterns
- Deep dives; status monologues; problem‑solving in‑meeting.

Why This Exists
- To prevent same‑day surprises by making ownership explicit and keeping WIP flowing.

---

## E.2 Weekly Health & Risk Review (Section 9.4)

Purpose
- Decide sequencing and risk treatments; prepare items for CCB/Steering.

Cadence/Timebox
- Weekly; 60–90 minutes.

Inputs
- Gate breaches (requirements/quality/commercial/operational), variance snapshots, dependency register deltas, debt trends.

Agenda
1) Breaches first (by domain)
2) Options/trade‑offs; assign owners/dates
3) CCB candidates and re‑estimates

Outputs/Artifacts
- Decision log entries; owner/action/date list; Steering prep items.

Participants
- Delivery Manager (chair), DPO, DPMs, QA/Test Lead, Tech/Integration Leads, Squad Leads; optional: Studio Owner, Commercial, Customer PM.

Anti‑patterns
- Slides without decisions; no owner/dates; mixing Steering debates.

Why This Exists
- To convert weak signals into concrete actions before they become escalations.

---

## E.3 Sprint‑End Learning & Stabilization (Section 9.11)

Purpose
- Demonstrate value, stabilize risks, and improve the system each sprint.

Cadence/Timebox
- Each sprint end; Demo (≤45m), Mini‑hardening (0.5–1 day), Retrospective (45–60m), Debt Roll‑call (15m).

Inputs
- Accepted items vs AC; flake/leakage; error budget; expediency log; debt register deltas.

Agenda
1) Feature Demo vs AC (call out gaps)
2) Mini‑hardening window for flaky/high‑risk areas
3) Retrospective (what worked/hurt/3 actions)
4) Debt Roll‑call (shortcuts, reasons, catch‑ups)

Outputs/Artifacts
- Accepted items; repair tasks; max 3 retro actions with owners/dates; updated debt portfolio.

Participants
- Full squad, DPM, QA/Test Lead; optional: Delivery Manager, DPO.

Anti‑patterns
- Endless demo; too many retro actions; ignoring repair signals when error budget is red.

Why This Exists
- To keep quality debt from compounding and to learn deliberately every sprint.

---

## E.4 Monthly Operational Review (Section 9.9)

Purpose
- Synthesize trends, recommend Steering decisions, and tune policies/thresholds.

Cadence/Timebox
- Monthly; 60–90 minutes.

Inputs
- Weekly packs; breaches; capacity/funding gaps; dependency and incident trends.

Agenda
1) Top 5 risks with trend/impact
2) Options with scope/date/capacity impacts
3) Recommended policy/threshold updates

Outputs/Artifacts
- Decision papers for Steering; updated threshold proposals and owners.

Participants
- Delivery Manager (chair), Studio Owner, DPO, QA/Test Lead, Tech/Integration Leads, Risk/Dependency Owners; optional: EO Commercial, Customer PMO.

Anti‑patterns
- Steering‑level debates here; no options; unquantified impacts.

Why This Exists
- To keep the operating model tuned to reality and to pre‑wire Steering decisions.

---

## E.5 RfP Readiness Workshop (Section 9.6)

Purpose
- Move Requirements from MAR → RfP with signed Features and design/impact readiness.

Cadence/Timebox
- Weekly; 60–90 minutes; ad‑hoc for hot items; pre‑increment checkpoint.

Inputs
- MAR fields; draft Features; initial AC/NFR; design note/doc; dependency map; Risk Surfaces.

Agenda
1) Top candidates by priority/risk
2) Decompose to subsystem‑scoped Features; seed AC/NFR; identify spikes
3) Confirm design/impact readiness; list Risk Surfaces
4) Customer sign‑off or actions

Outputs/Artifacts
- RfP labels set; signed Features; CRs for decomposition (if billable); blockers/owners; dependency updates.

Participants
- DPO (chair), Customer PM, DPMs, Tech/Integration Leads, QA/Test Strategy; optional: Delivery Manager, Security, Data, Ops.

Anti‑patterns
- Solutioning without AC/NFR; skipping design/impact; unsigned Features entering planning.

Why This Exists
- To protect planning reality by locking definitions and readiness before commitment.

---

## E.6 Backlog Grooming / Refinement (Section 9.6)

Purpose
- Ensure the next 2–3 sprints have Ready work (stories with AC/NFR/estimates/test notes).

Cadence/Timebox
- Weekly; 60–90 minutes per subsystem.

Inputs
- Signed‑off Features (RfP); design note/impact assessment; Definition of Ready; spikes and dependency map.

Agenda
1) Select top Features
2) Decompose into Stories; write AC aligned to Feature AC; capture NFR/test notes
3) Identify dependencies/spikes; assign owners/dates
4) Size; confirm DoR; mark Ready or list gaps

Outputs/Artifacts
- Ready stories; spike tasks; updated dependency register; Ready coverage metric.

Participants
- DPM (chair), Tech/Principal Engineer, QA/Test Lead; optional: EM, DPO.

Anti‑patterns
- Design during grooming; unestimated stories marked Ready; ignoring spikes.

Why This Exists
- To make planning feasible and prevent sprint churn from unready work.

---

## E.7 Sprint Planning (Section 9.6)

Purpose
- Agree a sprint goal and commit to a feasible backlog.

Cadence/Timebox
- Each sprint start; 60–120 minutes.

Inputs
- Ready stories; team capacity; velocity bands; error budget state; dependencies/spikes.

Agenda
1) Propose sprint goal
2) Select Ready items (include repair/hardening)
3) Check capacity (reserve 15–25% for quality/debt)
4) Identify risks and dependency calls; assign owners/dates

Outputs/Artifacts
- Sprint goal; committed backlog; capacity breakdown; owner/date list.

Participants
- Delivery Team Lead (chair), EM, DPM, Tech/Principal Engineer, QA/Test Lead.

Anti‑patterns
- Over‑commitment; planning with unready work; ignoring repair work.

Why This Exists
- To protect predictability by matching commitment to proven capacity and quality state.

---

## E.8 Dependency Huddle (spike‑only) (Section 9.4)

Purpose
- Rapidly unblock high‑risk dependencies without creating a permanent meeting.

Cadence/Timebox
- 15 minutes; up to twice weekly; limited to ≤ 3 weeks.

Inputs
- Dependency register with evidence/lead‑times; DependencyFunding%; open owners/actions.

Agenda
1) Top blockers; evidence check
2) Owner/date per dependency; funding/decision asks

Outputs/Artifacts
- Updated register; recorded escalations/funding decisions.

Participants
- Delivery Manager (chair), Integration Lead/Ops owner, DPO/DPM as needed.

Anti‑patterns
- Status sharing without evidence; no owner/dates.

Why This Exists
- To keep external/internal dependencies from starving delivery.

---

## E.9 Quality Council (Section 7)

Purpose
- Govern quality gates and stabilization using SLO/error‑budget framing.

Cadence/Timebox
- Weekly or bi‑weekly; 45–60 minutes.

Inputs
- Critical‑path pass rate; leakage; flake; error budget; MTTR; pipeline stability.

Agenda
1) Gates at risk (pass rate/error budget)
2) Stabilization plan (mini‑hardening/repair tasks)
3) Test strategy adjustments (risk‑based)

Outputs/Artifacts
- Gate decisions; repair plan; test strategy notes.

Participants
- QA/Test Lead (chair), EM/Tech Lead, DPM, Delivery Manager; optional: DPO.

Anti‑patterns
- Vanity coverage debates; ignoring flake; shipping with unknown leakage.

Why This Exists
- To keep releases safe by protecting critical journeys and error budgets.

---

## E.10 Architecture Roundtable (Section 9)

Purpose
- Approve integration patterns and exceptions; enforce contract‑first discipline.

Cadence/Timebox
- Weekly or as needed; 45–60 minutes.

Inputs
- Interface contracts; impact addenda; Risk Surfaces; NFRs.

Agenda
1) Interface proposals/changes
2) Impact and blast radius
3) Decision and next steps

Outputs/Artifacts
- Approved contracts/stubs; impact notes; decision log entries.

Participants
- DPO/Technical Architect (chair), Customer Enterprise Architect, Integration Lead, Tech Lead.

Anti‑patterns
- Ad‑hoc stubs without contracts; skipping impact assessment.

Why This Exists
- To reduce integration surprises by aligning early and documenting impact.

---

## E.11 Executive Steering Committee (Section 9.10)

Purpose
- Approve material trade‑offs; enforce policy thresholds; unblock decisions.

Cadence/Timebox
- Monthly/quarterly or on breach; 60–90 minutes.

Inputs
- Decision papers (options/costs/risks); FVS/Capacity Health bands; escalations.

Agenda
1) Decisions required (time‑boxed)
2) Policy/threshold changes
3) Escalation outcomes and owners

Outputs/Artifacts
- Approved changes (scope/capacity/dates/policy); recorded decisions and owners.

Participants
- Engagement Owner (chair), Studio Owner, Delivery Manager, DPO, Customer execs/Product leadership; optional: Account/Commercial, Finance/Legal.

Anti‑patterns
- Unprepared topics; no options; decisions not recorded.

Why This Exists
- To make binding trade‑offs transparently with the right decision‑makers.
