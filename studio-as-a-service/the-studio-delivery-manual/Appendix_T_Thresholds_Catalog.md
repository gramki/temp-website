# Appendix T — Thresholds Catalog (Tunable Defaults)

Use this catalog to define program‑specific thresholds. Start with the defaults below, then tune per evidence. Record who owns each threshold, which forum adjusts it, when it was last tuned, and where the evidence comes from. The Studio Council Member (SCM) owns lifecycle tracking and quarterly review.

How to use
- For each metric: set the current threshold, allowed range, owner, forum, evidence source, and last tuned date.
- Tune quarterly (or on signal failure). Retire noisy thresholds; add missing ones with a short proposal (see Section 11 template).

Template (copy per row)
- Metric | Default | Allowed range | Evidence source | Owner | Forum (adjusts) | Last tuned (date)

---

## T.1 Requirements (Section 5)

Defaults
- %RfP (next increment) | 70% | 60–85% | Requirements dashboard (Appendix A) | DPO | Weekly Review → Monthly | ____
- RfP shelf‑life (median) | ≤ 2 sprints | 1–3 sprints | Requirements dashboard | DPO | Weekly → Monthly | ____
- Volatility spike (2‑week) | > 20% triggers review | 15–30% | Requirements dashboard | DPO | Weekly | ____
- Integration readiness start gate | Contract or approved contract‑first stub required | N/A | Dependency register; checklist | DPO/Integration Lead | Weekly → RfP | ____

Guidance
- Raise %RfP when scope churn is low and planning cadence is stable; lower when discovery dominates the increment.
- Shelf‑life outside range indicates churn; revisit scope and customer sign‑off cadence.

---

## T.2 Quality & Readiness (Section 7)

Defaults
- Critical‑path pass rate | ≥ 95% | 93–98% | Quality dashboard (Appendix A) | QA/Test Lead | Quality Council | ____
- Error budget remaining | ≥ 20% before release | 15–30% | Quality dashboard | QA/Test Lead | Weekly → Monthly | ____
- Flake rate (7‑day) | ≤ 5% | 3–8% | CI/Allure | QA/Test Lead | Weekly | ____
- MTTR (P1/P2 defects) | ≤ 30m/2h | per domain | Incident reports | QA/Test Lead/EM | Weekly → Monthly | ____

Guidance
- When error budget is depleted, schedule stabilization before new intake; adjust pass‑rate threshold for highly regulated journeys upward.

---

## T.3 Commercial — SFM & TCM (Section 8)

SFM
- Funding Visibility Score (FVS) bands | 80–100 Healthy; 60–79 Watch; <60 At Risk | tune ±5 | Commercial dashboard | Commercial Manager | Monthly → Steering | ____
- Unfunded Exposure | ≤ 10% of forecast | 5–15% | Commercial dashboard | Commercial Manager | CCB → Steering | ____
- Delivery variance (2 cycles) | ≤ 8% | 5–12% | Forecast vs actual | Delivery Manager | Monthly | ____
- Dependency variance (2 cycles) | ≤ 12% | 8–20% | Dependency register | Delivery Manager | Monthly → Steering | ____

TCM
- Capacity Health bands | ≥ 80 Healthy; 60–79 Watch; <60 At Risk | tune ±5 | Capacity dashboard | Delivery Manager | Monthly → Steering | ____
- Ready coverage (backlog runway) | ≥ 2 sprints | 1–3 | Requirements dashboard | DPM | Weekly → Monthly | ____
- Idle time (rolling 4 weeks) | ≤ 10% | 5–15% | Capacity dashboard | Delivery Manager | Monthly → Steering | ____

Guidance
- Tighten FVS bands when runway is thin; relax when dependencies are well‑funded. For TCM, enforce idle‑time protections when dependency starvation persists.

---

## T.4 Operational & Dependencies (Sections 5.10, 9)

Defaults
- Dependency variance sustained | Threshold breach if > X% for 2 cycles | 8–20% | Dependency register | Integration Lead/Ops owner | Weekly → Monthly | ____
- Integration readiness incomplete | Breach if contracts/creds/env not ready within 2 sprints of planned start | N/A | Checklist/register | DPO/Integration Lead | Weekly → RfP | ____
- Decision backlog age (exec) | ≤ 3 business days | 2–5 | Decision log | Delivery Manager | Monthly → Steering | ____

Guidance
- Pick X based on provider SLA and business criticality; require evidence (SLA link, PO/CR) for readiness.

---

## T.5 Governance & Exceptions (Sections 9, 10.9)

Defaults
- Exception time‑box | ≤ 2 sprints | N/A | Exception index | Delivery Manager | Monthly | ____
- Exception reversion | Date set + reversion plan mandatory | N/A | Exception index | Delivery Manager | Monthly | ____
- Steering decision SLA | ≤ 3 business days | 2–5 | Decision log | EO/Engagement Owner | Steering | ____

Guidance
- Repeated exceptions on the same control trigger a policy/threshold proposal at Steering; SCM records lifecycle to closure.

---

## T.6 Tuning Process & Record

Process
1) Identify noisy or failing signals (late/false‑positive/negative). Gather evidence.
2) Propose threshold change (one‑pager) with owner, forum, effective date (Section 11 template).
3) Decide in Weekly/Monthly/Steering per scope; update dashboards and this catalog.
4) Audit impact after one cycle; revert or adopt as standard.

Record (fill per change)
- Metric changed: __________  Old → New: __________  Date: __________
- Owner: __________  Forum: __________  Evidence link(s): __________
- Adoption audit outcome: Keep / Revert / Tune further (notes)

SCM ownership
- The SCM curates Appendix T, ensures entries match dashboards/alerts, and publishes quarterly tuning summaries with manual version notes.
