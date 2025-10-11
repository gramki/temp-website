# Appendix G — SOPs & Templates

Each SOP starts with “Why this SOP exists” to anchor purpose and ends with metrics and SLAs to sustain discipline. Copy these into your program workspace and tailor thresholds via Appendix T.

---

## G.1 Requirements SOPs (Section 5)

Why this SOP exists
- To prevent scope churn by enforcing clear definitions and readiness before planning.

Scope
- Applies to requirements moving through MAR → Decomposed → RfP and signed Features.

Triggers
- New requirement discovered or clarified; RfP readiness review scheduled; stale shelf‑life detected.

Steps
1) Validate MAR fields (testability first). If missing, return to discovery with DPM support.
2) Decompose requirement → subsystem‑scoped Features; draft AC/NFR and design/impact addendum.
3) Run RfP Readiness Workshop; obtain Customer sign‑off; apply labels (`RfP`, `decomposition/*`).
4) Update dashboards (Appendix A) and dependency register readiness (Sec 5.10).

Roles/RACI
- DPO (A), DPM (R), Customer PM/PO (C/A for sign‑off), Tech/Integration Leads (C), QA/Test Strategy (C).

Artifacts/Templates
- MAR checklist; Feature spec with AC/NFR; design/impact addendum; dependency readiness checklist.

SLAs
- RfP decisions within 3 business days of workshop; stale shelf‑life (> 2 sprints) triggers review.

Metrics
- %RfP, shelf‑life median, volatility, integration readiness index (Appendix A).

---

## G.2 Quality SOPs (Section 7)

Why this SOP exists
- To protect critical journeys and keep releases safe using SLO/error‑budget framing.

Scope
- Applies to gating, stabilization, and defect governance.

Triggers
- Critical‑path pass rate < 95%; error budget < 20%; leakage/flake breaches.

Steps
1) Assess gates against SLOs and error budget; freeze scope when depleted.
2) Schedule mini‑hardening window (0.5–1 day); quarantine flake; add repair tasks.
3) Review at Quality Council; decide gate outcomes; update dashboards/alerts.

Roles/RACI
- QA/Test Lead (R/A), EM/Tech Lead (R), DPM (C), Delivery Manager (C/A for policy), DPO (C).

Artifacts/Templates
- Gate decision form; stabilization plan; flake quarantine list; Allure TestOps report.

SLAs
- Gate decision within 24 hours of breach; stabilization scheduled within next sprint.

Metrics
- Pass rate, error budget, leakage by severity, flake rate, MTTR/MTTD (Appendix A).

---

## G.3 Commercial SOPs (Section 8)

Why this SOP exists
- To make funding readiness and risk explicit and to route changes through the proper forums.

Scope
- Applies to CR lifecycle (SFM) and capacity/mix adjustments (TCM).

Triggers
- FVS < 60 (SFM); Capacity Health < 60 (TCM); unfunded exposure > 10%; dependency financial risk spikes.

Steps
1) Prepare impact (time/cost/risk/owner); route to CCB (SFM) or Operational Review (TCM).
2) Bring Steering options when material; record decisions; update dashboards and registers.
3) Protect idle‑time/standby and quality/debt reserves per model.

Roles/RACI
- Commercial Manager (R), Delivery Manager (A for routing), Account Manager (C), EO/Steering (A for material), Studio Owner (C).

Artifacts/Templates
- CR form; decision paper; funding ledger entry (Appendix C); dashboard widgets (Appendix A).

SLAs
- Steering decision turnaround ≤ 3 business days; CR closure within agreed cycle.

Metrics
- FVS/Capacity Health, unfunded exposure, delivery vs dependency variance, dependency financial risk (Appendix A).

---

## G.4 Operational SOPs (Section 9)

Why this SOP exists
- To keep governance predictable, decisions recorded, and forums effective.

Scope
- Applies to Daily/Weekly/Monthly/Steering forums and exceptions/concessions.

Triggers
- Breach in requirements/quality/commercial/operational signals; exception requested; dependency spike.

Steps
1) Run rituals per Appendix E; lead with breaches; assign owner/action/date.
2) For concessions: apply exception policy (Sec 10.9); label `process-exception`; set reversion date; review in Monthly.
3) Update decision log; publish changes to dashboards and threshold docs (Appendix T).

Roles/RACI
- Delivery Manager (A/R for operations), DPO/DPM/QA/Tech/Integration Leads (R/C), Studio Owner (C), EO/Steering (A for material), SCM (C/R for lifecycle tracking).

Artifacts/Templates
- Ritual templates (Appendix E); decision log template; exception policy checklist; governance flow map (Appendix F).

SLAs
- Weekly decisions recorded same day; Monthly policy proposals prepared 48h before Steering.

Metrics
- Decision backlog age; exception closure rate; ritual action closure rate; dashboard/alert signal health.

---

## G.5 Template Index

- MAR checklist (Sec 5)
- Feature spec with AC/NFR (Sec 5)
- Design/Impact addendum (Sec 5, Sec 10)
- Gate decision form & stabilization plan (Sec 7)
- CR form & decision paper (Sec 8)
- Decision log entry (Sec 9)
- Exception policy checklist (Sec 10.9)

Implementation Notes
- Store SOPs/templates in your program repo; link from ritual invitations and dashboards.
- The SCM reviews SOP usage quarterly and proposes updates to this manual (Sec 11).
