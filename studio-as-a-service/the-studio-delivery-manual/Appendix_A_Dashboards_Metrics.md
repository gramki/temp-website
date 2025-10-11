# Appendix A — Dashboards & Metrics

This appendix defines the dashboard specifications and core metrics used across Requirements, Quality, Commercial, and Debt, plus a sample alert matrix and a metrics maturity ladder. Use these as implementation guides in Grafana and Jira.

---

## A.1 Requirements Dashboard (Section 5)

Purpose
- Make requirement readiness and stability visible so planning is realistic.

Audience
- Delivery Manager (primary), Delivery Product Owner, Delivery Product Managers; Customer PM/PO (consumption).

Primary signals
- % RfP with signed features (by increment); RfP shelf‑life; volatility; decomposition label trends; integration readiness flags; dependency readiness summary.

Widgets (spec)
- RfP readiness: %RfP by increment with target line.
- RfP shelf‑life histogram with aging buckets and drill‑down to items.
- Volatility trend (adds/removals/major changes) 4–8 week window.
- Integration readiness index (contracts/creds/env) summary list.
- DependencyFunding% summary (from register; see Section 8 and 5.10).

Thresholds (tunable; see Appendix T)
- %RfP ≥ 70% for next increment; shelf‑life median ≤ 2 sprints; volatility spike > 20% triggers review.

Implementation notes
- Jira filters/labels: `RfP`, `decomposition/*`, `integration-risk`, `dependency/*`.
- Ownership: Delivery Product Owner (content), Delivery Manager (operational), SCM (lifecycle tracking).

---

## A.2 Quality & SLO Dashboard (Section 7)

Purpose
- Show readiness and stability of critical customer journeys and the health of the error budget.

Audience
- QA/Test Lead (primary), Engineering Manager, Delivery Manager; Customer QA (consumption).

Primary signals
- Critical‑path pass rate; error budget remaining; leakage trend; flake rate; MTTR/MTTD; pipeline stability.

Widgets (spec)
- Critical‑path pass rate with per‑journey breakdown (≥95% target).
- Error budget burn‑down (window per SLO) with policy line.
- Leakage trend by severity (P0–P5) and root‑cause bands.
- Flake rate (7‑day) and top flaky tests list.
- MTTR/MTTD trend; pipeline stability (green‑to‑green time).

Thresholds (tunable; see Appendix T)
- Error budget < 20% triggers stabilization; flake > 5% (7‑day) triggers hardening window; pass rate < 95% requires gate.

Implementation notes
- Allure TestOps integration for test suites; CI events for pipeline; Jira for defect stats.
- Ownership: QA/Test Lead; Delivery Manager enforces gate policy per Section 7.

---

## A.3 Commercial Health Dashboard (Section 8)

Purpose
- Surface funding readiness and exposure; separate delivery vs dependency variance; support Steering decisions.

Audience
- Delivery Manager, Commercial Manager, Engagement Owner, Account Manager; Steering.

Primary signals
- Funding Visibility Score (SFM); Capacity Health Score (TCM); unfunded exposure; delivery variance; dependency variance; DependencyFunding%; dependency financial risk.

Widgets (spec)
- FVS/Capacity Health trend with bands.
- Unfunded exposure ($/%), forecast vs actual (last two cycles).
- Dependency variance (current + 2 cycles) and DependencyFunding%.
- Dependency Financial Risk ($) widget from financial ledger.

Thresholds (tunable; see Appendix T)
- FVS < 60 (SFM) / Capacity Health < 60 (TCM) → Steering; unfunded exposure > 10% → freeze new scope.

Implementation notes
- Sources: Jira (RfP/CRs), planning tool (forecast), dependency register (funding/lead‑time/financial risk).
- Ownership: Commercial Manager (content), Delivery Manager (ops), EO/Steering (decisions).

---

## A.4 Debt Portfolio Dashboard (Section 6)

Purpose
- Keep debt accumulation vs amortization visible and prioritize risk‑reducing paydowns.

Audience
- Engineering Manager, Tech/QA Leads, Delivery Manager; Steering/Architecture (consumption).

Primary signals
- Accumulation vs amortization trend; top risks by impact domain; origin reason distribution; paydowns scheduled vs completed.

Widgets (spec)
- Accumulation vs amortization line chart (target ≥ 1.0 amortization ratio).
- Heatmap by impact domain (stability/security/performance/operability/compliance/maintainability/financial).
- Reason buckets (Time Pressure / Information & Volatility / Constraints / Capability & Process).
- Upcoming paydowns with owners/dates and risk links.

Thresholds (tunable; see Appendix T)
- Amortization ratio < 1.0 for 2 sprints triggers Steering/Architecture review; high‑risk shortcuts unresolved > 1 sprint → escalation.

Implementation notes
- Jira board/labels for debt items; link to incidents, SLO breaches, or gating risks.
- Ownership: Engineering Manager (content), Delivery Manager (ops), SCM (tracking).

---

## A.5 Sample Alert Matrix (see also Appendix B)

Purpose
- Provide a starter alert matrix with audiences and default thresholds; Appendix B contains the full matrix and audience register.

Structure
- Requirement alerts: %RfP low, volatility spike, shelf‑life breach.
- Quality alerts: error budget, leakage severity, flake rate, critical‑path pass rate.
- Commercial alerts: FVS/Capacity Health low, unfunded exposure, dependency financial risk.
- Operational alerts: dependency variance sustained, integration readiness incomplete, idle time (TCM).

Implementation notes
- Route alerts to forums with owners; tie to escalation ladders (Section 9).
- Tune per engagement in Appendix T.

---

## A.6 Metrics Maturity Ladder (Section 9.7)

Purpose
- Guide progression from manual to automated to predictive metrics safely.

Levels
- Manual: spreadsheets and ledgers; reviews run; signals trusted.
- Automated: dashboards wired to Jira/CI/observability; alert thresholds in place.
- Predictive: trend‑based forecasts (velocity bands, runway, leakage predictors); what‑if scenarios.

Guardrails
- Do not skip levels; automate after manual discipline exists; retire stale widgets quarterly.

Implementation notes
- SCM tracks adoption and proposes level shifts in Operational Review.
