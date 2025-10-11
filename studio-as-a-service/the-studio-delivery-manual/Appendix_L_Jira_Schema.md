# Appendix L — Jira Schema (Requirements, RfP, Labels, Statuses)

This appendix defines a pragmatic Jira configuration to support the manual. It covers issue types, workflows, fields, labels, automations, boards/filters, and a compact data dictionary. Cross‑references: Section 5 (Requirements), Section 7 (Quality), Section 8 (Commercial), Section 9 (Operations), Appendix A/B (dashboards/alerts), Appendix C (ledgers), Appendix G (SOPs), Appendix T (thresholds).

---

## L.1 Issue Types & Usage

Core types
- Requirement — Business problem statement tracked from MAR → RfP → Delivered (Section 5)
- Feature — Subsystem‑scoped, testable unit derived from a Requirement; owned by Customer team (acceptance) with Studio support
- Epic — Delivery planning container for Feature implementation work
- Story/Task — Implementation items; Story for user‑visible slices, Task for engineering work
- Defect — Quality issues with P0–P5 severity (Section 7)
- Debt — Portfolio items for shortcuts/technical/process debt (Appendix C)
- Dependency — Track critical external/internal dependencies (owner, funding, lead‑time)
- CR (Change Request) — SFM changes (Section 8A)

Optional/supporting types
- Spike — Time‑boxed investigation with exit criteria
- Decision — Key decisions when a dedicated record is helpful (mirrors decision log)

---

## L.2 Workflows (by type)

Requirement workflow
- New → In Progress → Decomposed → RfP (Ready‑for‑Planning) → Planned → In Development → Done
- Transitions
  - New→In Progress: MAR fields complete
  - In Progress→Decomposed: Features drafted; AC/NFR seeded; design/impact addendum drafted
  - Decomposed→RfP: Customer sign‑off on features/AC; labels set (RfP)
  - RfP→Planned: Entered into a planning increment; capacity available
  - Planned→In Development: Work has started on related epics/stories
  - In Development→Done: Requirement acceptance achieved (effort‑weighted completion accepted)

Feature/Epic/Story workflow (lightweight)
- To Do → In Progress → In Review → Done; Blocked (pseudo‑status via label)

Defect workflow
- New → Triage → In Progress → In Review → Done; Severity P0–P5 required

Debt workflow
- New → Prioritized → Scheduled → In Progress → Done; Link to catch‑up plan and risk

Dependency workflow
- Identified → Evidence Gathered → Committed → Delivered; Evidence includes funding and lead‑time commitment

CR workflow (SFM)
- Intake → Impacted (time/cost/risk/owner) → Approved/Rejected → Executed → Closed

---

## L.3 Custom Fields (key)

Requirement (all required unless noted)
- MAR Testability (Yes/No)
- Problem Statement (Text)
- Value Hypothesis (Text) (optional)
- Affected Subsystems (Multi‑select)
- Feature List (Links) (auto‑populated)
- Design/Impact Addendum (URL)
- Risk Surfaces (Multi‑select)
- Dependency Map (Links)
- RfP Signed (Yes/No + Date)

Feature
- Subsystem (Select)
- AC/NFR (Rich text or Links)
- Integration Readiness Flags (Contracts/Creds/Env) (3× Yes/No)

Defect
- Severity (P0–P5)
- Root Cause (Select: Requirements/Design/Code/Test/Ops/External)

Dependency
- Owner Team/Org (Text)
- Funding Status (Approved/Pending/None + CR/PO ID)
- Lead‑time Commitment (Date or SLA Link)
- Contract/Access Readiness (Yes/No)

Debt
- Impact Domain (Select)
- Reason Bucket (Select)
- Residual Risk (Text)
- Catch‑up Plan Link(s)

---

## L.4 Labels & Conventions

- decomposition/* — `decomposition/requirements→features`, `decomposition/features→stories`
- RfP — Apply to Requirements at RfP and to signed Features
- integration-risk — Apply to Requirements/Features with external integrations
- dependency/* — `dependency/external`, `dependency/internal`, `dependency/critical`
- process-exception — Index time‑boxed concessions (Section 10.9)
- quality/* — `quality/critical-path`, `quality/flake`
- debt/* — `debt/high-risk`, `debt/catchup-scheduled`

Naming
- Features: Subsystem: Short verb‑noun (e.g., Authorization: Idempotency Keys)
- Stories: <Subsystem> <Feature> — #<sequence>

---

## L.5 Boards & Filters

Boards
- Requirements board: Columns reflect Requirement workflow; swimlanes by increment
- Delivery board: Epics/Stories across squads; swimlanes by subsystem
- Quality board: Defects by severity; flake quarantine lane
- Debt board: Debt items by status; catch‑up swimlane

Filters (examples)
- RfP readiness: `type=Requirement AND status in ("RfP")`
- Shelf‑life watch: `type=Requirement AND "RfP Signed Date" <= -14d`
- Integration readiness gaps: `type=Feature AND ("Contract Ready"=No OR "Credentials Ready"=No OR "Environments Ready"=No)`
- Exceptions open: `labels=process-exception AND statusCategory != Done`

---

## L.6 Automations (examples)

Requirements
- When Requirement transitions to RfP, set `labels += RfP`, set `RfP Signed Date = now`, and create Dashboard event.
- If Requirement at RfP has no planned increment within 14 days, notify DPO/DPM and flag shelf‑life.

Features
- When any Integration Readiness Flag is No and status changes to In Progress, auto‑comment with checklist link and notify Integration Lead.

Defects
- If Severity=P0 and environment=Production, auto‑page on‑call and create Steering agenda item.

Debt
- When Debt labeled `debt/high-risk` moves to Scheduled, create catch‑up sub‑tasks and set due date within 2 sprints.

Dependencies
- If Funding Status != Approved and Lead‑time not committed by target date, escalate to Monthly with owner/date.

Exceptions
- When `process-exception` created, require reversion date field; auto‑create Monthly review task 10 days before reversion.

---

## L.7 Dashboards & Gadgets (mapping)

- Requirements: %RfP, shelf‑life, volatility (Appendix A)
- Quality: pass rate, error budget, leakage/flake (Appendix A)
- Commercial: FVS/Capacity Health, unfunded exposure, variance (Appendix A)
- Debt: accumulation vs amortization, reason/impact heatmaps (Appendix A)
- Operational: dependency variance, readiness checklist completion, decision backlog age (Appendix A/B)

---

## L.8 Data Dictionary (selected)

| Field | Type | Applies to | Description |
|---|---|---|---|
| MAR Testability | Boolean | Requirement | Whether the requirement can be validated via tests |
| RfP Signed | Boolean/Date | Requirement | Indicates RfP sign‑off and date |
| Affected Subsystems | Multi‑select | Requirement | Subsystems touched by the requirement |
| Integration Readiness Flags | 3× Boolean | Feature | Contracts, Credentials, Environments readiness |
| Severity | Enum (P0–P5) | Defect | Defect severity per Section 7 |
| Root Cause | Enum | Defect | Primary cause category |
| Impact Domain | Enum | Debt | Affected domain for risk |
| Reason Bucket | Enum | Debt | Origin reason of the debt |
| Funding Status | Enum + Text | Dependency | Funding state with CR/PO id |
| Lead‑time Commitment | Date/SLA | Dependency | Committed availability date or SLA link |

Governance
- Owner field should map to a named role; forum fields (Weekly/Monthly/Steering) indicate where decisions are made. SCM audits field usage and consistency quarterly (Section 11).
