# Rituals Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/rituals`

**Group:** Governance

**Purpose:** Manage Governance Rituals as repeatable operating practices with inputs, participants, decisions, outputs, action items, findings, registers, and recognition.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **Governance Ritual** | Cadence-based or event-triggered governance orchestration item. |
| **Ritual Definition** | Operating Model definition that describes purpose, cadence, participants, inputs, checklist, authority, and outputs. |
| **Ritual Instance** | One occurrence of a ritual for this Workbench. |
| **Ritual Output** | Decision, action item, finding, approval, exception, register entry, recognition, or Evolve Case. |

---

## Page Sections

### 1. Ritual Calendar

| Element | Description |
|---------|-------------|
| **Upcoming rituals** | Scheduled rituals for the Workbench |
| **Event-triggered rituals** | Rituals created by transitions, exceptions, or readiness checks |
| **Overdue rituals** | Rituals not completed within cadence |
| **Recently completed** | Rituals closed in recent window |

### 2. Ritual Definitions

| Field | Description |
|-------|-------------|
| **Purpose** | Why the ritual exists |
| **Cadence / trigger** | Weekly, sprintly, release-bound, transition-triggered, on-demand |
| **Participants** | Roles expected to attend or review |
| **Inputs** | Reports, dashboards, evidence, orchestration items, Work Orders, register entries |
| **Checklist** | What must be reviewed |
| **Decision authority** | Approvers who can approve, reject, defer, accept debt, or grant exception/waiver |
| **Expected outputs** | Decisions, action items, findings, recognitions, register entries |

### 3. Ritual Instance Detail

| Section | Description |
|---------|-------------|
| **Header** | Ritual ID, definition, status, cadence/trigger |
| **Participants** | Required and actual participants |
| **Input package** | Dashboards, reports, evidence bundles, cases, Product Intents, Work Orders |
| **Agenda / checklist** | Ritual checklist and completion state |
| **Decisions** | Approvals, rejections, deferrals, risk/debt/exception decisions |
| **Action items** | Follow-up Work Orders or tasks |
| **Findings** | Governance Findings produced |
| **Registers** | Risk, debt, exception, compliance, and finding entries |
| **Recognitions** | WFR Recognition entries produced by the ritual |
| **Evolve candidates** | Suggestions to improve policy, ritual, dashboard, or playbook |

### 4. Ritual Types

Examples:
- Product Intent Review
- Discovery Case Review
- Release Readiness Review
- Customer Release Intent Readiness Review
- Architecture Review Board
- Compliance Evidence Review
- Governance Trend Review
- Monthly Workbench Summary
- Workbench SLA Adherence Review
- Product Intent Retrospective
- Team Productivity / Contribution Review

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Schedule ritual | Governance Admin / Governance | Create ritual instance |
| Start ritual | Ritual participant | Begin ritual execution |
| Attach input | Participant | Attach dashboard, report, evidence, or register entry |
| Record decision | Approver / Ritual lead | Capture approval, rejection, deferral, or exception |
| Create finding | Participant | Record governance observation or issue |
| Create register entry | Participant / Governance | Add risk, debt, exception, compliance, deferred obligation, or kudos |
| Create Evolve Case | Governance / Evolve | Improve governance practice based on ritual output |
| Close ritual | Ritual lead | Close ritual instance with outputs recorded |

---

## Phase Position

| Maturity | Scope |
|----------|-------|
| Phase 1 | Basic event-triggered rituals and simple ritual output capture |
| Phase 2 | Ritual calendar, recurring cadence support, input packages |
| Phase 3 | Full ritual definitions, trend analytics, recognition patterns, Evolve integration |

---

## Related Consoles

- **Governance Overview** — ritual health and attention queue
- **Controls & Enforcement** — enforcement items created during rituals
- **Registers** — ritual outputs stored as register entries
- **Reports & Dashboards** — ritual inputs
