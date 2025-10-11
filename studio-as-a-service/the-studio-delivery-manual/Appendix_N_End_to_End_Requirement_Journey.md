# Appendix N — End‑to‑End Journey of a Requirement (Role‑play, Gates, AC Evolution)

Purpose: Show, with a realistic BFSI example, how a requirement moves MAR → Decomposed → RfP → Planned → In Development → Done. For each stage: inputs, what transpired (role‑play), outputs/artifacts, gates/criteria to progress, and how AC evolved.

Example scenario: Reduce card‑fraud false‑positives by 20% without increasing checkout abandonment or auth SLAs.
Subsystems: Payments Authorization, Fraud/Risk, Notifications.
Constraints: PCI DSS; P95 `/authorize` < 150ms; abandonment delta ≤ +1%.

---

## N.1 MAR — Minimally Acceptable Requirement (inputs → AC seed)

About: Establish a measurable intent, boundaries, constraints, and testable AC seed; the Delivery Manager ensures clarity, names owners, and lines up the path to the RfP workshop.

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
- MAR checklist (Section 5.2):
  - Business intent clearly articulated and measurable — Satisfied
  - Baselines captured (FPR, abandonment, P95 latency) — Satisfied
  - Initial AC seed defined (measurable) — Satisfied
  - Scope boundaries (in/out‑of‑scope) — Satisfied
  - Subsystems identified — Satisfied
  - Constraints documented (PCI, latency, abandonment) — Satisfied
  - High‑level dependencies inventoried — Satisfied
  - Testability plausible at requirement level — Satisfied
  - Named owner(s) and reviewers assigned — Pending (assign Customer PM and DPO formally)
  - Initial Risk Surfaces noted — Pending (draft for model drift, sandbox gaps)
  - Evidence/measurement approach sketched (cohorts, A/B or pre/post) — Pending
  - Commercial model/time‑box for decomposition agreed (SFM/TCM) — Pending
  - Governance path and RfP workshop scheduled — Pending

---

## N.2 Decomposed — Requirement → Features (subsystem‑scoped)

About: Translate the requirement into subsystem‑scoped Features with plausible testability; the Delivery Manager orchestrates owners, risks, dependencies, and materials to secure RfP sign‑off.

Inputs
- MAR record; fraud rule inventory; card‑network constraints; data availability notes.

What transpired (role‑play)
- DPO: “We’ll scope solution Features at subsystem boundaries.”
- EM / Tech Lead: “We can compute a risk signal during `/authorize` and move exemptions logic into Fraud/Risk.”
- Customer PM: “Notifications can handle step‑up flows.”

Work to reach RfP (owning team → output)
- Assign named owner(s) and reviewers in record (Customer PM, DPO) → updated MAR
- Draft initial Risk Surfaces (model drift, sandbox fidelity, quota limits) → risk addendum
- Define evidence/measurement plan (matched cohorts, confidence thresholds, data sources) → AC measurement note
- Draft subsystem‑scoped Feature definitions with AC/NFR → Feature docs (Auth, Fraud/Risk, Notifications)
- Produce design/impact addenda (latency budgets, data flows, audit trail, cost) → signed design notes
- Map and confirm dependencies (mTLS, quotas, templates, feature flags) → dependency register
- Outline test approach (component/contract/customer‑service paths) → QA strategy note
- Schedule and circulate RfP workshop agenda and materials → calendar invite + deck

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

Decomposition checklist (to achieve RfP)
- Subsystem boundaries confirmed — Satisfied
- Features drafted per subsystem — Satisfied
- Each Feature has purpose/scope and AC/NFR seeds — Pending
- Design and impact addenda (latency budgets, data flows, auditability) — Pending
- Dependencies mapped and preliminarily confirmed (keys, quotas, mTLS, templates) — Pending
- Evidence/measurement plan drafted (cohorts, confidence thresholds, data sources) — Pending
- Risk Surfaces drafted (model drift, sandbox fidelity, quota ceilings) — Pending
- Feature owners assigned (Auth, Fraud/Risk, Notifications) — Pending
- RfP workshop scheduled and materials circulated — Pending
- Jira labels reflect state (`decomposed`) — Satisfied

---

## N.3 RfP — Ready‑for‑Planning (signed Features, design/impact)

About: Achieve Customer sign‑off on Feature definitions, AC/NFR, and design/impact; the Delivery Manager secures decisions, records Risk Surfaces, and locks a shelf‑life for planning.

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

Discovered details added to requirement
- Measurement method: matched‑cohort analysis with 95% CI; data sources defined (auth logs + analytics)
- Latency budgets: 10ms budget for risk signal inside `/authorize`; end‑to‑end P95 < 150ms
- Policy auditability: structured decision logs with export to compliance archive (daily)
- Risk Surfaces: model drift tolerance, sandbox fidelity gaps, quota ceilings, notification deliverability
- Governance: RfP decision date, shelf‑life 90 days, re‑affirmation forum set (Monthly Ops Review)
- Dependency lead‑times: provider credentials 5–10 days; quota/allowlist 3–5 days; template approval 2–3 days
- Rollout: feature‑flag kill‑switch and cohort sizing plan documented
- Back‑out: rollback plan and replay test pack defined
- Security: mTLS/jwks endpoints verified; secret rotation plan noted

- Labels: `rfp-yes` (remove `features-pending-signoff`)


Work to reach Planned (owning team → output)
- Provider credentials issuance and mTLS setup (Integration Lead) → credential pack
- Quota/allowlist approvals and rate‑limit letters (Integration Lead) → provider confirmation
- Notification template localization approval (Customer PM) → approved templates
- Feature‑flag rollout plan and kill‑switch (EM/DPM) → rollout spec
- DoR checklist completed for Epics/Stories (DPM) → ready backlog
- CI baseline thresholds and test cases enumerated (QA Lead) → QA readiness memo
- Sprint capacity allocation and sequencing (EM/DPM) → planning board entries
- Dependency lead‑time scheduling (DM) → integrated plan

Gate to progress
- RfP gate (Section 5.3) passes: AC complete; dependencies mapped; design/impact signed; Risk Surfaces recorded.

Gate checklist — RfP
- Feature definitions signed by Customer PM and DPO — Satisfied
- Design/impact addenda attached and signed — Satisfied
- AC complete, testable, and include measurement plan — Satisfied
- Dependencies confirmed with provider commitments (keys, mTLS, quotas, allowlists) — Pending
- Risk Surfaces recorded and linked — Satisfied
- QA strategy defined (component/contract/customer‑service paths) — Satisfied
- Governance recorded (RfP decision date, owners, shelf‑life) — Satisfied
- Jira labels updated to `rfp-yes`; artifacts linked — Satisfied
 - Integration: API spec and version pin agreed — Pending
 - Integration: mTLS/cert chains validated in sandbox — Pending
 - Integration: Quotas/rate‑limits/timeouts confirmed with written commitments — Pending
 - Integration: Error taxonomy mapped; retry/backoff/idempotency rules defined — Pending
 - Integration: Data classification/PII flows reviewed; DPIA/TRA notes recorded — Pending
 - Integration: Sandbox fidelity risks and compensating tests recorded — Satisfied
 - Integration: Provider SLAs/support contacts/escalation paths documented — Pending
 - Integration: Monitoring/alert points and trace/log fields defined — Pending

---

## N.4 Planned — Features → Epics/Stories (DoR met)

About: Convert signed Features into ready backlog (Epics/Stories) that meet DoR; the Delivery Manager ensures capacity alignment, dependency readiness, and QA/CI baselines.

Inputs
- Signed Features; design/impact; Definition of Ready; dependency/credential checklists.

What transpired (role‑play)
- Grooming (9.5):
  - DPM: “Break Features into Epics/Stories; capture NFR/test notes; size.”
  - QA Lead: “Add contract tests on `/authorize` risk signal; add customer‑service test flows.”
  - EM: “Reserve 15–25% for quality/debt.”

Discovered details added to requirement/backlog
- Story‑level AC and NFR linked to each Epic; traceability map updated
- Latency test hooks for risk signal defined; synthetic datasets enumerated
- Notification templates and locales listed; fallback copy rules documented
- Provider sandbox gaps documented with compensating tests
- CI baseline thresholds recorded (pass rates, flake budget, perf budgets)
- Feature‑flag rollout stages (internal, 5%, 25%, 50%, 100%) scheduled
- Capacity plan: 2 sprints for Fraud/Risk, 1 sprint for Notifications, 2 sprints for Auth work

Outputs / Artifacts
- Epics/Stories with AC/NFR; DoR satisfied; sprint allocation ready
- Labels: `planned`, `design-complete`

Planned checklist (DoR)
 

Work to reach In Development (owning team → output)
- Complete provider setup tasks (Integration Lead) → ready environments
- Land CI config changes and smoke tests (QA/EM) → green pipeline
- Lock sprint plan and WIP limits (EM/DM) → sprint start checklist
- Prep data fixtures and contract tests (QA/Tech Lead) → test packs

Gate to progress
- DoR rules met; unready work blocked; integration readiness items tracked for gating (Section 5.10).

Gate checklist — Planned (DoR)
- Epics/Stories linked to Features with AC/NFR and test notes — Satisfied
- Stories sized and prioritized with clear acceptance paths — Satisfied
- Dependencies ready or scheduled (credentials, quotas, templates) — Pending
- CI pipeline updated with new test suites and thresholds — Pending
- QA data and environments ready (synthetic/fixtures, sandbox accounts) — Pending
- Rollout and rollback plans referenced at Epic level — Satisfied
- Non‑functional budgets attached (latency/error budgets) — Satisfied
- Owners and reviewers assigned per Epic/Story — Satisfied

---

## N.5 In Development — Build, test, and accept incrementally

About: Deliver increments against AC/NFR with stable quality signals; the Delivery Manager manages flow, addresses breaches, and protects release integrity.

Inputs
- Planned Stories; CI gates; Allure/Jira traceability; integration readiness checklist.

What transpired (role‑play)
- Daily/Weekly:
  - DM: “Triage by breaches (requirements/quality/commercial/ops); propose options with owners/dates.”
  - Tech Lead: “Add contract tests for latency/429/5xx; validate idempotency/ordering.”
  - QA Lead: “Quarantine flaky tests; schedule mini‑hardening if error‑budget red.”
  - Customer PM: “Accept Stories/Epics that meet AC and non‑functional gates.”

Discovered details during build
- AC clarifications: acceptable latency variance ±5ms at P95; log fields expanded for audit
- Edge cases: retries, idempotency keys, rate‑limit backoff, partial step‑up failures
- Data contracts: schema version pinning; backward compatibility rules
- Operational limits: provider 429 thresholds observed; queue sizing adjusted
- Exception policy: one time‑boxed exception for sandbox fidelity with reversible test control

Outputs / Artifacts
- Incremental accepts (e.g., Exemptions engine epics accepted; risk signal stories in progress)
- Labels: `in-development`, `partially-delivered`
- AC evolution (clarifications during build):
  - “Exemption policy changes require decision log entry + replay test pack.”
  - “Risk signal tolerates ±5ms variance at P95 under peak.”

 

Work to reach Done (owning team → output)
- Burn down remaining defects to P2+ with waivers documented (QA/EM) → clean RC
- Complete staged rollout to 100% (EM/DM) → release note
- Validate post‑release metrics window (QA/DM) → stability report
- Close acceptance on remaining Epics/Stories (Customer PM/DPO) → acceptance log

Gate to progress
- Release gates (Section 7) hold: no P0/P1; critical‑path pass rate met; error‑budget ≥ threshold; integration readiness green (5.10).

Gate checklist — In Development (Release)
- No open P0/P1 defects on release candidate — Satisfied
- Critical‑path test pass rate ≥ threshold — Satisfied
- Error‑budget within limits for affected services — Pending
- Latency budgets respected (risk signal ≤ 10ms; P95 < 150ms) — Pending
- Canary/rollback verified in non‑prod — Satisfied
- Monitoring/alerts configured for new paths — Satisfied
- Customer acceptance recorded for scope included in release — Pending
- Exceptions labeled, time‑boxed, reversion date set — Satisfied

---

## N.6 Done — Accepted and released

About: Confirm AC met in production with stable signals and captured learnings; the Delivery Manager closes the loop and seeds improvements to roadmaps and playbooks.

Inputs
- All features delivered; dashboards green; Quality Council sign‑off; Steering informed.

What transpired (role‑play)
- DM to Steering: “FPR reduced by 23%; latency/abandonment within limits; risk/exception logs auditable.”
- EO: “Approve close‑out and move residual improvements to roadmap.”

Discovered details captured at close
- Measured FPR improvement: 23% over 4‑week matched cohort, CI 96%
- P95 latency observed: 142ms at peak; risk signal compute median 6ms
- Abandonment delta: +0.6% within allowed threshold
- Policy audit exports validated with Compliance
- Residual follow‑ups: improve sandbox fidelity; tune step‑up copy for locale X

Outputs / Artifacts
- Requirement: `done`, `delivered`; decision paper archived; dashboards snapshot
- Post‑release review items: tune thresholds; backlog improvements

 

Gate to close
- All acceptance criteria met; error‑budget respected; post‑release monitoring stable.

Gate checklist — Done (Close‑out)
- All acceptance criteria met in production — Satisfied
- Stability window passed without regression — Satisfied
- Evidence archived (dashboards snapshot, links to logs/export) — Satisfied
- Decision papers, exceptions, waivers closed/archived — Satisfied
- Learnings logged and owners assigned (SCM/DM) — Satisfied
- Residual improvements triaged to roadmap with owners/dates — Satisfied

---

## N.7 At‑a‑glance checklist by stage
- MAR: AC seed (measurable), boundaries, constraints, dependencies
- Decomposed: subsystem‑scoped Features; testability plausible
- RfP: signed AC/NFR; design/impact; dependency map; Risk Surfaces
- Planned: DoR met; Stories sized; readiness tracked
- In Dev: critical‑path green; error‑budget healthy; incremental acceptance; exceptions labeled and time‑boxed
- Done: AC met; release stable; learnings captured; improvements logged

Cross‑references: Section 5.2/5.3/5.7/5.8/5.10; Section 7 gates; Section 9.3/9.4/9.5/9.6/9.8/9.11; Appendix A/B/L/M.
