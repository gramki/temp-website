# Appendix C — Debt Portfolio Ledgers

This appendix provides the canonical ledgers for managing delivery debt as a portfolio. Use these templates to record where debt exists, why it exists, how risky it is, and how it will be paid down over time without derailing delivery.

Cross‑references: Section 6 (taxonomy, portfolio, catch‑ups), Appendix A (Debt dashboard), Appendix B (alerts/escalations), Appendix T (tunable thresholds).

---

## C.1 Debt Register (portfolio index)

Purpose
- Maintain a single indexed register of all known debt items with consistent fields for prioritization and reporting.

Fields (minimum)
- Debt ID (unique) and title
- Impact domain (stability/security/performance/operability/compliance/maintainability/financial)
- Reason bucket (Time Pressure / Information & Volatility / Constraints / Capability & Process)
- Principal description (what was deferred/short‑cut)
- Residual risk (what can fail, where, and how observable it is)
- Severity band (High/Med/Low) with rationale
- Origin date and origin context (sprint/feature/incident)
- Ownership (role + person) and affected subsystem(s)
- Links (code/infra/ADR/test) and related incidents or defects
- Status (Open / Scheduled / In progress / Paused / Done) and last updated

Example (abbrev)
- CRED‑D‑017 — Checkout: retry logic bypasses idempotency key validation
  - Impact domain: operability; Reason: Time Pressure; Severity: High
  - Residual risk: duplicate captures on network retries; observable via chargeback spike
  - Owner: Tech Lead (Payments Authorization); Links: PR#1243, ADR‑11

Ownership & process
- Engineering Manager curates content; Delivery Manager reviews weekly; SCM audits lifecycle tracking and portfolio hygiene monthly.

---

## C.2 Catch‑Up Plans (paydown records)

Purpose
- Define and track the explicit work that will amortize debt items, with dates and owners.

Fields (per plan)
- Debt IDs addressed (one or many)
- Paydown strategy (refactor/test/add guardrail/runbook/tooling)
- Work items (tasks/PRs/tests) with estimates and owners
- Scheduling window (sprint(s), target finish date)
- Risk reduction hypothesis and expected signals (e.g., leakage↓, MTTR↓)
- Verification method (tests, dashboards/alerts changes)
- Result & follow‑up (achieved/not, next action)

Example
- Plan: Idempotency & retries stabilization (Sprint 14)
  - Debt: CRED‑D‑017, CRED‑D‑022; Strategy: add idempotency key validation, circuit breaker
  - Tasks: API contract update; component tests; runbook updates; alert tuning
  - Signals: duplicate capture defects → 0; MTTR → < 30m; flake → < 2%

Ownership & cadence
- Tech Lead owns plan; Delivery Manager schedules capacity; QA/Test Lead owns verification; review in Sprint‑End ritual and Weekly Review.

---

## C.3 Funding Ledger (origin & commercial treatment)

Purpose
- Record who funds each paydown and why, consistent with origin and commercial model.

Fields
- Debt ID(s); Origin category (customer‑induced, delivery‑induced, shared, third‑party)
- Commercial model (SFM/TCM) and funding rule applied
- Decision forum/date (CCB/Steering) and references (CR IDs)
- Budget line or capacity allocation reference; amount or team‑weeks allocated
- Notes (justification, constraints)

Guidance
- SFM: customer‑induced or shared items typically funded via CR; delivery‑induced items absorbed by Studio unless agreed otherwise; document exceptions.
- TCM: reserve 10–20% amortization capacity by default (Appendix T); use ledger to protect reserve from erosion.

---

## C.4 Expediency Ledger (shortcuts taken under pressure)

Purpose
- Make “just this once” choices visible immediately so they can be retired quickly.

Fields
- Shortcut ID and description
- Trigger/context (deadline, environment outage, integration slip)
- Risk surface touched (customer‑visible? regulatory?)
- Owner and expiry date (≤ 2 sprints) with reversion plan
- Related labels (`process-exception`, `expediency`) and links to work items
- Close‑out notes (paydown completed, controls restored)

Usage
- Log at the Sprint‑End Debt Roll‑call (Section 9.5) and review at Weekly Review; if expiry passes, escalate in Operational Review.

---

## Implementation notes

- Index in Jira with consistent labels and boards per subsection; use saved filters for the dashboard in Appendix A.
- SCM ensures discovery → decision → implementation → adoption audit is recorded per item and that portfolio snapshots feed Operational Review and Steering.
- Export ledgers as CSV for quarterly archive; preserve stable links for audits.
