# Appendix O — Example Artifacts (Redacted)

Purpose: Provide copy‑pasteable, redacted examples that map to templates in Appendix M and the ledgers/registers across the manual. Replace <…> placeholders with program‑specific details. Do not store secrets; use dummy IDs and scrub PII.

Conventions
- Redaction tags: [REDACTED], <placeholder>, XX‑1234
- Cross‑refs: link to sections/appendices for definitions and gate criteria

---

## O.1 Decision Paper (Example)
- Title: Decision required — Adjust RfP shelf‑life policy for integration items
- Context (≤ 5 lines): RfP shelf‑life breaches rose to 28% for integration‑heavy Features; sandbox fidelity and provider lead‑time variability caused re‑affirmations every 2–3 sprints. Steering guidance needed to set a realistic default and reduce churn.
- Options (2–3 only):
  1) Keep 90‑day default; require exception records per breach; no policy change
  2) Set 120‑day default for integration‑tagged Features; re‑affirm at 90 days if dependencies still pending
  3) Split policy by risk tier (A/B) with 90/150‑day defaults, reviewed quarterly
- Recommendation: Option 2 — balances realism with control; reduces exception overhead by ~40%
- Evidence links: Funding Visibility dashboard [link], Dependency register filter `dependency/critical` [link], RfP shelf‑life widget [link]
- Requested forum/date: Steering — <YYYY‑MM‑DD>
- Owner: Delivery Manager  Co‑owners: DPO, Integration Lead

---

## O.2 Process Exception / Concession (Example)
- Title: Exception — Skip customer‑service tests on non‑critical journey during provider outage
- Description: For 1 sprint, replace full customer‑service suite with contract tests on unaffected paths to ship fraud‑policy hotfix
- Lighter control chosen: contract‑first stub + replay pack at T+5 days
- Risk surfaces touched: Integration instability; customer‑visible latency risk
- Owner: QA Lead  Reversion date: <YYYY‑MM‑DD> (≤ 2 sprints)
- Labels: `process-exception`, `quality/critical-path`
- Forum trail: requested at Weekly Review; review at Monthly on <date>
- Evidence links: pipeline runs [link], incident ref INC‑XX‑123 [link]
- Closure: reverted on <YYYY‑MM‑DD>

---

## O.3 Continuity Pack Snapshot — Governance Change (Example)
- Summary (1 page max)
  - Current plan burn vs funded: $[REDACTED] remaining; unfunded exposure $[REDACTED] (22%)
  - Top dependencies (3):
    1) Provider quotas (Funding=Pending; Lead‑time=Uncommitted)
    2) mTLS onboarding (Funding=Approved; Lead‑time=Committed)
    3) Notification templates (Funding=None; Lead‑time=N/A)
  - Open decisions: RfP re‑affirmations (7 items > 90 days); policy on sandbox fidelity
  - Options for new exec: A) fund gaps; B) de‑scope low value; C) re‑sequence behind committed dependencies
- Attachments: RfP list CSV; dependency register snapshot; Funding Visibility Score trend
- Owners: Delivery Manager, Commercial Manager

---

## O.4 Evidence Pack — Release Readiness (Example)
- Scope window: last 14 days; environments: staging→prod; cohort: peak hours Fri 16:00–20:00
- Signals & thresholds
  - Critical path pass rate — 99.2% vs 99% — Allure run #3456 — Pass
  - Flake rate — 1.3% vs 2% — CI dashboard — Pass
  - Error budget remaining — 28% vs 20% min — SLO panel — Pass
  - P0/P1 open in scope — 0 vs 0 — Jira filter — Pass
  - Integration flags (contracts/creds/env) — Yes/Yes/Yes — Feature checklist — Pass
- Data & method: queries [links]; cohort definition; exclusions noted
- Risk surfaces/exceptions: none active; one expiring <YYYY‑MM‑DD>
- Summary & Ask: Ready — proceed with staged rollout 25%→100% over 48h
- Owner/Reviewers: QA Lead; EM, DM

---

## O.5 RfP Design/Impact Addendum (Example)
- Feature: Authorization — Real‑time risk signal (10ms budget)
- Interfaces touched: `/authorize` (v3), Fraud policy service (v2)
- AC/NFR deltas: latency budgets; audit log fields; idempotency constraints
- Testing implications: add contract tests for 429/5xx; chaos test for downstream latency; customer‑service tests for step‑up journey
- Operational impacts: monitoring KPIs, new alerts, log fields for audit export
- Dependencies/readiness: provider quotas; mTLS onboarding; notification templates
- Sign‑off: DPO (date), Customer PM (date)

---

## O.6 Dependency Register Entry (Example)
- ID: DEP‑045
- Owner team/org: Customer Security
- Funding status: Pending (CR‑221 awaiting approval)
- Lead‑time commitment: Uncommitted (target <YYYY‑MM‑DD>)
- Contract/Access readiness: No (mTLS certs not issued)
- Notes: blocks Features FEA‑210/211; financial risk/day: $12,500 (idle burn)
- Labels: `dependency/critical`

---

## O.7 Debt Ledger Entry (Example)
- ID: DEBT‑017 — UI policy placement (migrate to Fraud service)
- Reason Bucket: Constraints  Impact Domains: Security; Maintainability
- Subsystem: Checkout UI; Fraud/Risk
- Principal: 20 SP  Residual Risk: Medium‑High  Touch Frequency: High
- Catch‑Up Plan: M1 logs+tests; M2 service+25% rollout; M3 delete UI logic+hardening
- Funding: Customer‑induced (Constraints) — via CR
- Labels: `debt/high-risk`, `quality/critical-path`

---

Usage Notes
- Duplicate these examples per program and store alongside Jira items; keep links fresh.
- Redact all customer identifiers and credentials. Replace with placeholders before sharing broadly.
- Align labels/fields to Appendix L; thresholds to Appendix T; templates to Appendix M.
