# Phase 2 Writing Backlog (Essential Improvements)

Goal: Address first‑order readability/comprehension gaps in v1 while preserving rigor. Organized by manual sections. Each task includes expectations so execution is unambiguous.

Note: This backlog is intentionally scoped to essentials for Phase 2; non‑essentials are deferred to a future pass.

---

## Section 2 — Context
- Task: Add TL;DR + rule summaries per sub‑section (2.1–2.7)
  - Expectations:
    - TL;DR (3–5 bullets) at section top: “What to do first / What to avoid.”
    - Each sub‑section ends with a 2–3 bullet “Rules we will operate by.”
    - Keep current examples; reduce paragraph length for scanability.
  - Cross‑links: 9.13 (signals), Appendix B (alerts).

---

## Section 5 — Requirements & Evolution
- Task: Add decomposition flow diagram (Mermaid)
  - Expectations:
    - Show Requirement → (MAR) → Decomposed → (RfP) → Planned → In Dev.
    - Show Feature → Epic → Story with gates: Design/Impact sign‑off; AC/NFR sign‑off.
    - Place near 5.3/5.7; link to 5.8 gates.
- Task: Integration Readiness visual checklist (5.10)
  - Expectations:
    - Single visual table/icon list: Contracts; Credentials; Environments; Observability; Runbooks; Change Control; Idempotency/Rate‑limits noted.
    - Include “Green to proceed” rule; add pointer to Appendix A/B widgets.
- Task: End‑to‑end requirement walkthrough
  - Expectations:
    - One realistic requirement tracked across states (MAR → RfP → Planned → In Dev → Done); show labels/fields/dashboards changing.
    - Place as a sub‑section or short appendix referenced from 5.3.

---

## Section 6 — Adaptive Refinements & Debt
- Task: Add sample portfolio row
  - Expectations:
    - One anonymized row illustrating Reason Bucket, Impact Domain(s), Principal, Residual Risk, Touch Frequency, Catch‑up plan, Funding.
    - Brief annotation on how it drives prioritization and dashboards.

---

## Section 7 — Quality, Bugs & Defect Governance
- Task: “Minimum viable quality signals” strip
  - Expectations:
    - Starter set (per new subsystem): Critical‑path pass rate; Leakage (severity‑segmented); Flake rate; Error budget remaining; Change Failure Rate (optional).
    - Provide default targets with link to Appendix T for tuning.

---

## Section 8 — Commercial (SFM/TCM)
- Task: SFM vs TCM crib sheet (one page)
  - Expectations:
    - When to choose; top 3 risks; top 3 widgets; key clauses to check.
    - Prominent link to 8A/8B and Appendix J.
- Task: Model selection flow (simple decision flow)
  - Expectations:
    - Decision nodes for scope certainty, dependency volatility, budget model; outputs SFM/TCM with caveats.

---

## Section 9 — Operational Governance
- Task: Delivery Manager quick start (weekly rhythm + dashboards)
  - Expectations:
    - “Open these dashboards daily” (Reqs/Quality/Commercial/Operational); “Run this weekly pack”; ritual checklist by primary signals.
    - Link to Appendix E (ritual templates), 9.13 (signals), Appendix H (audit).
- Task: Elevate “Ritual → Primary signals” map
  - Expectations:
    - Duplicate or move the primary‑signals block near the top of Section 9; keep detail in 9.13.

---

## Appendix L — Jira Schema
- Task: Example board + automation JSON (illustrative)
  - Expectations:
    - One sample board config (columns, swimlanes) and 2–3 automation rules in JSON/YAML, clearly marked as examples.
    - Link to fields/data dictionary and Appendix A dashboards.

---

## Cross‑section improvements
- Task: Evidence pack one‑pager (template)
  - Expectations:
    - Compact template showing: context, signals (screenshots/links), options with scope/date/capacity/cost impacts, recommendation, forum/date, owners.
    - Place in Appendix M and link from Sections 8, 9, 10.
- Task: Operating defaults callout
  - Expectations:
    - Single “defaults” callout (quality/debt reserve 15–25%; exception time‑box ≤ 2 sprints; %RfP ≥ 70% before planning; Steering SLA 3 business days; dependency variance and unfunded exposure thresholds per current text).
    - Add to Section 9 intro (governance operating defaults) and cross‑link to Appendix T for tuning.

---

## New Appendices & Guides
- Task: Quick Start Guide (role‑based)
  - Expectations:
    - Create a concise “Quick Start Guide” with role cards for Engagement Org (Engagement Owner, Commercial Manager, Account Manager) and Studio Org (Studio Owner, Delivery Manager, DPO, DPM, Engineering Manager, Tech Lead, QA/Test Lead).
    - Each card: first‑week actions, dashboards to open, forums to attend, key SOPs/templates, top 3 signals to watch, common escalations.
    - Location: new file linked from README and Section 9; cross‑link to Appendix E/G/H and 9.13.
- Task: Appendix — Example Artifacts
  - Expectations:
    - Add a new appendix that aggregates redacted examples: decision paper, exception record, continuity pack, dependency register export, RfP feature spec, evidence pack snapshots.
    - Each artifact: 1–2 screenshots (or structure), brief “why this exists,” and links to owning sections.
    - Cross‑link from Sections 5, 8, 9, 10 and Appendix M.
- Task: Appendix — Studio Council Member Roles & Playbook
  - Expectations:
    - Create a dedicated appendix detailing SCM responsibilities across program lifecycle with new sub‑sections: conception, incubation/pre‑flight, infancy (first 90 days), steady‑state, and close‑out.
    - Include cadence, artifacts (Manual Change Register, audits), versioning process, and example KPIs for adoption.
    - Cross‑link from Section 11 and Appendix H/T; align with governance forums in Section 9.

---

## Ownership & sequencing
- Owner: VP Delivery (content lead) with section owners (5/6/7/8/9) and SCM for cross‑section.
- Suggested order: 9 quick start → 5 visuals → 7 signals → 8 crib sheet → 6 sample row → L examples → cross‑section templates → 2 TL;DR.

## Definition of done (per task)
- Text merged; visuals added; cross‑links in place; checklist item created/closed; no new linter issues; glossary updated if new terms.
