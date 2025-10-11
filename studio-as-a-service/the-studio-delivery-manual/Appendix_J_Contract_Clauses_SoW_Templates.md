# Appendix J — Contract Clauses & SoW Templates (SFM and TCM)

This appendix provides model clauses and SoW templates aligned to Section 8 (Commercial Models & Governance Alignment). Split content by model and keep language consistent with governance (Section 9), quality (Section 7), requirements (Section 5), and exception policy (Section 10.9). Tunable thresholds live in Appendix T.

---

## J.1 Scope‑Funded Model (SFM) — Model Clauses

Change Management & Decision Rights
- The Parties shall route all changes to scope, dates, or cost through the Change Request (CR) lifecycle: Intake → Impact (time/cost/risk/owner) → Approval → Execution → Closure (Section 8A).
- Decision rights: Studio (Delivery Manager) approves zero‑cost/low‑risk changes within buffer; CCB approves mid‑range changes within budget guardrails; Steering (EO‑owned) approves material scope/cost/date or policy exceptions.
- Steering decision SLA: Executive approvals shall be issued within three (3) business days of submission, unless otherwise agreed in writing.

Funding Visibility & Unfunded Exposure
- The Parties shall maintain the Commercial Health Dashboard including the Funding Visibility Score (FVS) (Section 8A). If FVS < 60 or Unfunded Exposure > 10% of forecast, the Parties shall not harden new milestone dates until remediation is approved by Steering.

Integration Readiness (Requirements‑Linked)
- For any external integration or customer‑visible interface, the Parties shall maintain an Integration Readiness checklist (contracts, credentials, environments) and shall not schedule development to start until at least one of the following is true: (a) a signed interface contract exists; or (b) an approved contract‑first stub is in place (Sections 5.10, 10.9).

Process Exceptions / Concessions
- Any process exception or concession (as defined in Section 10.9) must be time‑boxed (≤ two sprints), labeled in the project tracker as a process exception, assigned an owner, and include a reversion plan and date. Repeated exceptions shall be brought to Steering with a proposal to update policy/thresholds.

Quality Commitments (Acceptance & Defect Severity)
- Acceptance shall be measured against approved Acceptance Criteria (AC) and documented Risk Surfaces. Defect severity P0–P5 shall be defined per Section 7; P0 defects are production defects that cause SEV‑0 or SEV‑1 outages and are unrecoverable without a fix.
- Release gating shall respect SLO/error‑budget policy (Section 7). When the agreed error budget is exhausted, the Parties shall prioritize stabilization before net‑new intake.

Dependency Variance & Financial Risk
- The Parties shall maintain a dependency register with funding and lead‑time evidence (Section 8). Delivery variance and dependency variance shall be tracked separately; material dependency variance shall be escalated to Steering with options (fund, re‑sequence, de‑scope) and an estimate of financial risk.

Commercial Exclusions
- The Delivery Team shall not be responsible for costs or delays caused by unapproved scope, customer‑owned dependencies or environments, or third‑party constraints outside Delivery Team control, unless specifically assumed in an approved CR or capacity change (Section 8C).

---

## J.2 Team‑Capacity Model (TCM) — Model Clauses

Capacity, Mix, and Idle‑Time Protections
- The Parties agree on the minimum monthly capacity (team‑weeks), permitted mix swaps within envelope, price/indexation rules, and notice periods for ramp up/down.
- If dependency/demand starvation exceeds the agreed grace period, standby/idle‑time protections apply (billable standby or redeploy by mutual agreement) (Section 8B).

Planning Cadence & Readiness
- The Parties shall run a rolling quarterly plan, monthly reforecast, and sprint‑level execution. Backlog Readiness Coverage (percentage of next 2–3 sprints groomed to Ready) and Funded Capacity Coverage (weeks) shall be reported monthly (Section 8B).

Capacity Health & Escalations
- The Capacity Health Score shall be computed as per Section 8B. If Capacity Health < 60, the Parties shall bring options to Steering to adjust mix, funding, or demand to restore health.

Quality & Stabilization Under TCM
- The error‑budget and gating policy (Section 7) applies under TCM. When error budget is exhausted or critical‑path pass rate falls below threshold, stabilization work shall be scheduled from within team capacity before new intake.

Process Exceptions / Concessions
- Exceptions shall follow Section 10.9 (time‑box, label, owner, reversion date) and shall be recorded for review at Operational Review; repeated exceptions require a Steering policy decision.

Commercial Exclusions
- Idle time caused by customer‑owned dependencies or demand starvation beyond the grace period shall be protected under the agreed standby terms (Section 8B). Other exclusions follow Section 8C.

---

## J.3 Common Provisions (SFM & TCM)

Forum Ownership & Records
- Steering is chaired by the Engagement Owner (EO org). CCB and Operational Reviews are chaired by the Delivery Manager (Studio org). Decisions taken in these forums supersede informal communications and shall be recorded in the decision log (Sections 8, 9).

Auditability & Artifacts
- The Parties shall maintain stable links to dashboards (Appendix A), alert matrix (Appendix B), ledgers (Appendix C), RACI/readiness (Appendix D), ritual templates (Appendix E), governance flow (Appendix F), SOPs (Appendix G), audit checklist (Appendix H), thresholds (Appendix T). These artifacts must be available for audit within three (3) business days of request.

Security/Compliance/Operations Involvement
- When a concession or change touches Security, Compliance, or Operations Risk Surfaces, the relevant owner shall be included in the approval path and evidence pack (Sections 7, 10.9, 11).

Manual Versioning & Improvements
- The Studio Council Member (SCM) owns institutional learning and versioning of this manual. Improvements shall be tracked lifecycle end‑to‑end (discovery → decision → implementation → adoption audit), with release notes published after approvals (Section 11).

---

## J.4 SoW Templates (Outlines)

Template A — SFM Statement of Work (Scope‑Funded)
1. Scope Definition
   - In‑scope requirements/features and explicit out‑of‑scope list; mapping to business outcomes; interfaces affected.
2. Deliverables & Acceptance
   - Feature‑level deliverables; AC/NFR definition approach; traceability; Risk Surfaces.
3. Change Management
   - CR lifecycle; decision rights; Steering SLA; estimation bands by maturity (±20–30% at RfP; Section 8A).
4. Governance & Reporting
   - Forums, cadences, owners (EO vs Studio); decision log; dashboards and alerts.
5. Quality & Stabilization
   - Gating policy (SLO/error budget); defect severity P0–P5; stabilization protocol.
6. Integrations & Dependencies
   - Integration Readiness checklist requirement (contracts/creds/env or contract‑first stubs); dependency register.
7. Commercials
   - Funding, billing rules, and exclusions; unfunded exposure handling; invoicing cadence.
8. Risks & Assumptions
   - Key risks; assumptions; escalation paths; standby arrangements if applicable.

Template B — TCM Statement of Work (Team‑Capacity)
1. Capacity & Mix
   - Baseline team‑weeks per month; permitted mix swaps; indexation; notice periods.
2. Planning & Readiness
   - Rolling plan; monthly reforecast; Backlog Readiness Coverage; Capacity Health reporting.
3. Governance & Reporting
   - Forums and cadences; decision rights; dashboards and alert routing.
4. Quality & Stabilization
   - SLO/error‑budget policy; stabilization before new intake when depleted.
5. Integrations & Dependencies
   - Integration Readiness checklist; dependency register; standby protections.
6. Commercials & Protections
   - Idle‑time/standby protections; exclusions per Section 8C; invoicing cadence.
7. Risks & Assumptions
   - Risks; assumptions; escalation paths; model change triggers.

---

## J.5 Definitions & References
- “SFM” and “TCM” are defined in Section 8.
- “Risk Surfaces”, “Defect Severity P0–P5”, and “Error Budget” are defined in Section 7.
- “Process Exception / Concession”, “Lighter Control”, and exception policy are defined in Section 10.9.
- “SCM” responsibilities and manual versioning are defined in Section 11 and `roles_reference.md`.
- Tunable thresholds (e.g., %RfP, pass rate, FVS bands) are documented in Appendix T.

---

## J.6 Governance Change & Continuity (SFM and TCM)

Governance Change Notification & Re‑affirmation Window
- The Customer shall notify the Delivery Manager within three (3) business days of any material change in governance, decision rights, sponsoring executive, or operating model that affects program scope, approvals, or forums. Until re‑affirmation, the Parties shall not harden new milestone dates or expand committed scope beyond existing baselines, except for jointly agreed urgent risk mitigations. Within ten (10) business days of notice, Steering (EO‑owned) shall re‑affirm or replace prior decisions in writing. Absent written change, previously recorded decisions remain binding.

Decision Records Are Authoritative
- The Parties agree that the program decision log and SoW Annexes (including signed RfP feature definitions and interface contracts) are the authoritative records of scope, readiness, and decision history. Email/chat communications do not supersede these records unless captured into the decision log or a signed CR/capacity change.

Continuity Pack & Review SLA
- Within five (5) business days of governance‑change notice, the Delivery Manager will provide a continuity pack summarizing: (i) current plan and baseline, (ii) funded vs unfunded exposure, (iii) critical dependencies with funding/lead‑time evidence, and (iv) open decisions with options/impacts and owners. Steering shall review and provide re‑affirmations or changes within five (5) business days of receipt.

Requirements Revalidation & Shelf‑life
- RfP‑signed Feature definitions remain valid through the governance‑change window. Shelf‑life is extended by the duration of any Customer‑requested pause. If the Customer requests revalidation, or if the governance change materially impacts scope, the Parties shall run a time‑boxed RfP confirmation workshop; resulting changes are handled via CR (SFM) or capacity re‑allocation (TCM).

Commercial Protections — SFM
- Customer‑requested pauses exceeding five (5) business days and governance/policy resets that invalidate previously signed designs or RfP definitions shall be handled via Change Request, including timeline/budget re‑baselining and funding for incremental analysis/rework. Unfunded exposure identified in the continuity pack shall be resolved (fund/de‑scope/re‑sequence) before milestone dates are hardened.

Commercial Protections — TCM
- Under TCM, dependency/demand starvation caused by governance‑change pauses beyond the agreed grace period triggers standby/idle‑time protections per the SoW (billable standby or mutually agreed redeployment). Capacity/mix changes shall be routed via Operational Review/Steering and reflected in the capacity ledger; stabilization reserves (quality/debt) remain protected.

Architecture/Policy Resets & Integration Contracts
- Customer‑mandated architecture/policy resets or integration‑contract changes that invalidate previously approved designs/interfaces shall be recorded via CR (SFM) or capacity change (TCM). The Customer shall fund incremental rework, testing, and certification necessitated by such resets.

Dependencies & Third‑Party Commitments
- Previously approved dependency commitments (funding and lead‑time) remain obligations of the Customer. If altered due to leadership change, the Customer shall provide revised commitments or fund agreed mitigations (workarounds, additional environments, quota upgrades) before resuming affected scope.

Timelines & SLAs
- Re‑affirmation SLA: ten (10) business days from notice. Decision turnaround SLA: three (3) business days for Steering items once the continuity pack is tabled. Pauses exceeding these SLAs require a CR (SFM) or documented capacity change (TCM) with adjusted dates/funding.
