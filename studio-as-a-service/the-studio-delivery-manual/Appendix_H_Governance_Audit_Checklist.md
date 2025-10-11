# Appendix H — Governance Audit Checklist (with Maturity Guidance)

Use this checklist to assess whether delivery discipline is operating as designed. Score maturity, collect evidence, and record targeted remediations. Run this audit monthly during stabilization and quarterly thereafter. The Studio Council Member (SCM) owns scheduling and lifecycle tracking.

Maturity levels
- Level 1 (Manual): Practices exist and are performed consistently, even if artifacts are manual.
- Level 2 (Automated): Dashboards/alerts are wired; decisions and exceptions are indexed and visible.
- Level 3 (Predictive): Trends drive proactive decisions; thresholds and policies are tuned from evidence.

Scoring rubric (per area)
- 0 = Not in place; 1 = In place but inconsistent; 2 = Consistent & automated; 3 = Predictive/optimized.
- Area score = average of items (round down). Overall maturity = average of area scores.

Evidence required
- Stable links to dashboards (Appendix A), alert matrix (Appendix B), ledgers (Appendix C), RACI/readiness (Appendix D), ritual templates (Appendix E), governance flow (Appendix F), SOPs (Appendix G), thresholds (Appendix T).

---

## H.1 Requirements (Section 5)

Checklist
- MAR completeness and testability are verified before decomposition (0–3)
- RfP criteria met; Features signed by Customer; shelf‑life within target (0–3)
- Integration readiness (contracts/creds/env) tracked and visible (0–3)
- Decomposition labels/statuses used consistently; traceability intact (0–3)

Maturity cues
- L1: Checklists used manually; sign‑offs recorded on issues
- L2: RfP %, shelf‑life, volatility on dashboard; stale items auto‑surfaced
- L3: Volatility predicts planning risk; integration readiness gates prevent churn

Evidence
- Requirements dashboard; RfP workshop notes; dependency register snapshots

---

## H.2 Quality & Readiness (Section 7)

Checklist
- Critical‑path pass rate meets target; error budget policy enforced (0–3)
- Leakage and flake trends monitored; stabilization actions scheduled (0–3)
- Quality Council decisions recorded; gates respected (0–3)

Maturity cues
- L1: Gate decisions documented; manual enforcement
- L2: Dashboards alert on pass rate/error budget/flake; mini‑hardening scheduled
- L3: Predictors point to risky journeys; repair work preemptively planned

Evidence
- Quality dashboard; Allure reports; gate decision forms; stabilization plans

---

## H.3 Debt Management (Section 6; Appendix C)

Checklist
- Debt register fields complete (impact domain, reason, residual risk) (0–3)
- Amortization reserve (10–20%) protected and visible (0–3)
- Catch‑up plans linked to incidents/risks; outcomes verified (0–3)

Maturity cues
- L1: Ledger maintained; ad‑hoc scheduling
- L2: Dashboard shows accumulation vs amortization; reserves honored
- L3: Debt trends predict stability risk; paydowns prioritized by impact

Evidence
- Debt dashboard; catch‑up plans; funding ledger entries

---

## H.4 Commercial Governance (Section 8)

Checklist
- SFM: FVS computed; unfunded exposure visible; CR lifecycle timely (0–3)
- TCM: Capacity Health computed; idle‑time protections enforced (0–3)
- Delivery vs dependency variance separated; actions recorded (0–3)

Maturity cues
- L1: CRs and capacity changes tracked; basic reports
- L2: Dashboards for FVS/Capacity Health; thresholds and escalations wired
- L3: Trends predict exposure; Steering options pre‑baked with costs

Evidence
- Commercial dashboard; CR register; capacity ledger; decision papers

---

## H.5 Operational Governance & Rituals (Section 9; Appendix E, F)

Checklist
- Ritual calendar active; forums run to template; outputs recorded (0–3)
- Weekly → Monthly → Steering decisions flow with options & impacts (0–3)
- Dashboards/alerts mapped to forums; owners and SLAs clear (0–3)

Maturity cues
- L1: Meetings held; minutes recorded
- L2: Breach‑first agendas; decision log current; alert routes defined
- L3: Quiet, short meetings; few escalations; policy tuning driven by trends

Evidence
- Meeting packs; decision log; governance flow map; alert matrix

---

## H.6 Human Contract & Exceptions (Section 10)

Checklist
- Value framing used; scripts and lighter controls offered (0–3)
- Exceptions/concessions: time‑boxed, labeled, reversion dates set (0–3)
- Contract‑ready clauses mirrored in practice; approvals per decision rights (0–3)

Maturity cues
- L1: Scripts and policy notes referenced occasionally
- L2: Exceptions indexed with labels; tracked to reversion; contract clauses applied
- L3: Patterns drive policy/threshold updates; fewer exceptions over time

Evidence
- Exception index; decision papers; contract appendix updates

---

## H.7 Continuous Improvement & SCM (Section 11)

Checklist
- Program retros run on cadence (milestones or quarterly) (0–3)
- Manual Change Register maintained; lifecycle tracked (discovery→decision→implementation→adoption audit) (0–3)
- Manual versioning with release notes; adoption metrics reported (0–3)

Maturity cues
- L1: Retro notes exist; ad‑hoc follow‑through
- L2: Register and metrics wired to dashboards; SCM reports at Monthly
- L3: Improvement items close predictably; fewer repeated exceptions

Evidence
- Retro notes; Manual Change Register; version tags and release notes; adoption metrics

---

## H.8 Thresholds & Tuning (Appendix T)

Checklist
- Tunable defaults documented; program‑specific thresholds recorded with date/owner (0–3)
- Quarterly tuning performed; decommissioned signals retired (0–3)

Maturity cues
- L1: Thresholds in a doc; seldom updated
- L2: Appendix T updated per quarter; dashboards reflect current values
- L3: Tuning driven by false‑positive/negative analysis and outcome impact

Evidence
- Appendix T entries; dashboard change logs

---

## H.9 Scoring & Interpretation

How to score
- For each item, assign 0–3 based on the rubric. Average to get area score; average areas for overall maturity.

Interpretation guidance
- Overall ≤ 1.5: Foundational
  - Focus on wiring dashboards/alerts, decision logs, and exception indexing; adopt Appendix E templates.
- 1.6–2.2: Operationalizing
  - Ensure Monthly → Steering pipeline produces decisions; protect reserves; enforce gates.
- ≥ 2.3: Stabilizing/Predictive
  - Shift to trend‑based thresholds; retire noisy widgets; pilot predictive indicators.

---

## H.10 Remediation Playbook

- Missing dashboards/alerts → Implement Appendix A/B; map signals to forums; assign owners.
- Repeated exceptions → Enforce exception policy (Sec 10.9); propose policy/threshold updates.
- Weak adoption → SCM to publish version update; run three‑month post‑change adoption audits.
- Quality instability → Enforce error budget; schedule mini‑hardening; protect reserves (Appendix T).
- Debt growth → Establish/defend amortization reserve; prioritize high‑impact paydowns (Appendix C).

Owner & cadence
- SCM coordinates the audit, records actions/owners/dates, and reports status at Monthly Operational Review; escalate blockers to Steering.
