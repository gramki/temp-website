# Appendix M — Decision & Exception Templates

Use these templates to standardize how decisions and exceptions are proposed, recorded, and audited. Keep each artifact to one page when possible. Cross‑references: Sections 9, 10.9, 11; Appendix H (audit), Appendix T (thresholds).

---

## M.1 Decision Paper (One‑Pager)

Purpose
- Request a decision from CCB or Steering with clear options and quantified impacts.

Template
- Title: Decision required — <topic>
- Context (≤ 5 lines): current state, signal/threshold breach, why now
- Options (2–3 only):
  1) <Option A> — Scope/Date/Capacity/Cost impacts; risks; owner
  2) <Option B> — …
  3) <Option C> — … (optional)
- Recommendation: <Option X> with rationale
- Evidence links: dashboards (Appendix A), registers (Appendix C), CRs (Sec 8A)
- Requested forum/date: CCB or Steering; target decision by <date>
- Owner: <name/role>  Co‑owners: <roles>

Notes
- Attach numbers not adjectives (variance %, FVS/Capacity, pass rate, error budget).
- Steering SLA is ≤ 3 business days (Section 8/9).

---

## M.2 Process Exception / Concession Record

Purpose
- Capture a time‑boxed relaxation or replacement of a control (Section 10.9).

Template
- Title: Exception — <control being relaxed>
- Description: what is changing and why (near‑term goal)
- Lighter control chosen: <shorter template / time‑boxed review / sample tests / contract‑first stub>
- Risk surfaces touched: <regulatory/customer‑visible?>
- Owner: <name/role>  Reversion date (≤ 2 sprints): <date>
- Labels: `process-exception` + <control area>
- Forum trail: requested at <forum>; review at Monthly on <date>
- Evidence links: dashboards / SOPs / checklists
- Closure: reverted on <date> / converted to policy via Steering on <date>

Notes
- If repeated, bring a policy/threshold proposal to Steering.

---

## M.3 Manual Change Register Entry (SCM)

Purpose
- Track improvement items lifecycle from discovery to adoption audit (Section 11).

Template
- Title: Improvement — <area>
- Discovery: date; source (retro/signal failure)
- Proposal: link to Decision Paper; target forum/date
- Decision: outcome/date; effective (change go‑live) date
- Adoption audit: dates (monthly ×3) and outcomes; metrics before/after
- Status: Open / In progress / Closed; notes

Notes
- Publish release notes for manual version updates after approvals.

---

## M.4 Steering Agenda Item (Short Form)

Purpose
- Add a concise, ready‑to‑decide item to the Steering pack.

Template
- Item: <title>
- Ask: choose between Option A / B (see Decision Paper)
- Impacts: Scope/Date/Capacity/Cost summary (1–2 lines)
- Evidence: link to Decision Paper; dashboard screenshot
- Owner: <role>  Decision due: <date>

---

## M.5 RfP Design/Impact Addendum (Pointer)

Purpose
- Summarize impacts before Feature commitment (Section 5; used in RfP Workshop).

Contents (see Appendix G — Requirements SOPs)
- Interfaces touched; AC/NFR changes; testing implications; operational impacts; dependency/readiness changes.

---

## Usage & Storage
- Store each artifact alongside the related Jira items; link from decision logs and dashboards.
- The Studio Council Member (SCM) audits usage and completeness as part of Appendix H.
