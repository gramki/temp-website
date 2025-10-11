# Appendix N — End‑to‑End Journey of a Requirement (Role‑play, Gates, AC Evolution)

Purpose: Show, with a realistic BFSI example, how a requirement moves MAR → Decomposed → RfP → Planned → In Development → Done. For each stage: inputs, what transpired (role‑play), outputs/artifacts, gates/criteria to progress, and how AC evolved.

Example scenario: Reduce card‑fraud false‑positives by 20% without increasing checkout abandonment or auth SLAs.
Subsystems: Payments Authorization, Fraud/Risk, Notifications.
Constraints: PCI DSS; P95 `/authorize` < 150ms; abandonment delta ≤ +1%.

---

## N.1 MAR — Minimally Acceptable Requirement (inputs → AC seed)

Inputs
- Customer PM shares business intent: “Reduce false‑positives by 20%.”
- Baselines: current false‑positive rate (FPR) = 2.5%; abandonment = 2.0%; P95 auth latency = 120ms.
- Known constraints: PCI DSS; no external PII outside approved providers.

What transpired (role‑play)
- Customer PM: “We’re losing approvals to over‑zealous rules; we need a 20% improvement.”
- DPO: “We can help. We must protect auth latency and abandonment. Let’s define measurable AC and subsystem boundaries.”
- DPM: “We’ll produce AC seed now; details will evolve in decomposition.”

Outputs / Artifacts
- MAR record (fields complete):
  - Intent: Reduce card‑fraud false‑positives by 20% while maintaining P95 `/authorize` < 150ms and checkout abandonment ≤ baseline + 1%.
  - Boundaries:
    - In‑scope subsystems: Payments Authorization (risk signal), Fraud/Risk (exemptions policy), Notifications (step‑up communications).
    - Out‑of‑scope: Core fraud model re‑training, acquirer/bank rule changes, full checkout UX redesign, data‑warehouse analytics/reporting.
  - Dependencies:
    - Card‑network/3DS directory server integration; risk‑scoring/provider API (keys, quotas, mTLS); SMS/email provider (sender IDs, templates); feature‑flag/experimentation platform; metrics/dashboards; change‑window approvals.
  - Constraints: PCI DSS; no PII to non‑approved processors; P95 `/authorize` < 150ms; abandonment delta ≤ +1%; adhere to bank change‑window policy.
- Initial AC (seed):
  1) Reduce FPR by ≥ 20% vs baseline over a 4‑week window
  2) P95 `/authorize` latency remains < 150ms
  3) Checkout abandonment ≤ baseline + 1%
- Labels: `new-requirement`

Gate to progress
- MAR checklist (Section 5.2) passes: testability exists; boundaries/constraints noted.

---

## N.2 Decomposed — Requirement → Features (subsystem‑scoped)

Inputs
- MAR record; fraud rule inventory; card‑network constraints; data availability notes.

What transpired (role‑play)
- DPO: “We’ll scope solution Features at subsystem boundaries.”
- EM / Tech Lead: “We can compute a risk signal during `/authorize` and move exemptions logic into Fraud/Risk.”
- Customer PM: “Notifications can handle step‑up flows.”

Outputs / Artifacts
- Features identified:
  1) Authorization subsystem: real‑time risk signal on `/authorize`
  2) Fraud/Risk subsystem: risk‑based exemptions policy engine (TRA/low value)
  3) Notifications subsystem: step‑up comms (OTP/SMS/email) with localized templates
- Labels: `decomposed`
- AC (evolving):
  - Keep AC‑1 (FPR) but add subsystem testability:
    - “Risk signal computed within 10ms budget inside `/authorize` pipeline.”
    - “Exemptions engine logs policy decision and outcome per txn.”

Gate to progress
- Decomposition complete and testability plausible; ready for RfP workshop.

---

## N.3 RfP — Ready‑for‑Planning (signed Features, design/impact)

Inputs
- Draft Feature definitions; design/impact addenda; dependency map; Risk Surfaces (e.g., network model drift, sandbox gaps).

What transpired (role‑play)
- RfP Workshop (Section 9.8):
  - DPO: “Here are the Features and their AC/NFR; here’s the design/impact for each.”
  - Integration Lead: “Providers require mTLS and quota increases; sandbox doesn’t mirror prod rate‑limits.”
  - QA Lead: “Critical‑path tests will include step‑up/TRA flows; budget error‑budget to protect releases.”
  - Customer PM: “Approved with these AC clarifications.”

Outputs / Artifacts
- Signed Feature definitions + design/impact addenda
- Updated AC (refined and testable):
  1) FPR reduction ≥ 20% over 4 weeks on matched cohorts (A/B or pre/post) with confidence interval ≥ 95%
  2) P95 `/authorize` < 150ms across peak; risk signal compute ≤ 10ms budget
  3) Checkout abandonment ≤ +1% vs baseline during step‑up
  4) Policy audit trail present (decision, inputs, exemption rationale) and exportable
- Labels: `rfp-yes` (remove `features-pending-signoff`)

Gate to progress
- RfP gate (Section 5.3) passes: AC complete; dependencies mapped; design/impact signed; Risk Surfaces recorded.

---

## N.4 Planned — Features → Epics/Stories (DoR met)

Inputs
- Signed Features; design/impact; Definition of Ready; dependency/credential checklists.

What transpired (role‑play)
- Grooming (9.5):
  - DPM: “Break Features into Epics/Stories; capture NFR/test notes; size.”
  - QA Lead: “Add contract tests on `/authorize` risk signal; add customer‑service test flows.”
  - EM: “Reserve 15–25% for quality/debt.”

Outputs / Artifacts
- Epics/Stories with AC/NFR; DoR satisfied; sprint allocation ready
- Labels: `planned`, `design-complete`

Gate to progress
- DoR rules met; unready work blocked; integration readiness items tracked for gating (Section 5.10).

---

## N.5 In Development — Build, test, and accept incrementally

Inputs
- Planned Stories; CI gates; Allure/Jira traceability; integration readiness checklist.

What transpired (role‑play)
- Daily/Weekly:
  - DM: “Triage by breaches (requirements/quality/commercial/ops); propose options with owners/dates.”
  - Tech Lead: “Add contract tests for latency/429/5xx; validate idempotency/ordering.”
  - QA Lead: “Quarantine flaky tests; schedule mini‑hardening if error‑budget red.”
  - Customer PM: “Accept Stories/Epics that meet AC and non‑functional gates.”

Outputs / Artifacts
- Incremental accepts (e.g., Exemptions engine epics accepted; risk signal stories in progress)
- Labels: `in-development`, `partially-delivered`
- AC evolution (clarifications during build):
  - “Exemption policy changes require decision log entry + replay test pack.”
  - “Risk signal tolerates ±5ms variance at P95 under peak.”

Gate to progress
- Release gates (Section 7) hold: no P0/P1; critical‑path pass rate met; error‑budget ≥ threshold; integration readiness green (5.10).

---

## N.6 Done — Accepted and released

Inputs
- All features delivered; dashboards green; Quality Council sign‑off; Steering informed.

What transpired (role‑play)
- DM to Steering: “FPR reduced by 23%; latency/abandonment within limits; risk/exception logs auditable.”
- EO: “Approve close‑out and move residual improvements to roadmap.”

Outputs / Artifacts
- Requirement: `done`, `delivered`; decision paper archived; dashboards snapshot
- Post‑release review items: tune thresholds; backlog improvements

Gate to close
- All acceptance criteria met; error‑budget respected; post‑release monitoring stable.

---

## N.7 At‑a‑glance checklist by stage
- MAR: AC seed (measurable), boundaries, constraints, dependencies
- Decomposed: subsystem‑scoped Features; testability plausible
- RfP: signed AC/NFR; design/impact; dependency map; Risk Surfaces
- Planned: DoR met; Stories sized; readiness tracked
- In Dev: critical‑path green; error‑budget healthy; incremental acceptance; exceptions labeled and time‑boxed
- Done: AC met; release stable; learnings captured; improvements logged

Cross‑references: Section 5.2/5.3/5.7/5.8/5.10; Section 7 gates; Section 9.3/9.4/9.5/9.6/9.8/9.11; Appendix A/B/L/M.
