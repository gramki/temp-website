# Governance Overview Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/governance`

**Group:** Governance

**Purpose:** Landing page for Workbench governance health — what needs attention now, what is blocked, what is aging, and what deserves recognition.

---

## Page Sections

### 1. Governance Health Summary

| Metric | Description |
|--------|-------------|
| **Overall governance status** | Aggregated pass / warning / blocked state across active orchestration items |
| **Pending approvals** | Items awaiting Approver decision |
| **Failed controls** | Control Objectives currently failing |
| **Evidence gaps** | Missing or stale evidence bundles |
| **Active debt** | Debt + Catch-Up items still open |
| **Expiring exceptions / waivers** | Exceptions nearing expiry |
| **Open risks** | Active Risk Register entries |
| **Open rituals** | Governance Rituals scheduled, in progress, or overdue |
| **Recent recognitions** | WFR Kudos / Recognition entries from recent rituals |

### 2. Attention Queue

Prioritized list of governance items needing action.

| Item | Type | Priority | Owner / Approver | Due / Expiry | Action |
|------|------|----------|------------------|--------------|--------|
| GE-041 | Enforcement | Blocked | Control Owner | Today | Open |
| DEBT-022 | Debt + Catch-Up | Overdue | Debt Owner | Expired | Escalate |
| RIT-009 | Ritual | Prep needed | Ritual participants | Tomorrow | Prepare |

### 3. Register Summary

| Register | Active | Overdue / Expiring | Trend |
|----------|--------|--------------------|-------|
| Risk | Count | Count | Up / flat / down |
| Debt | Count | Count | Up / flat / down |
| Exceptions / Waivers | Count | Count | Up / flat / down |
| Compliance | Count | Count | Up / flat / down |
| Workforce Recognition | Count | N/A | Up / flat / down |

### 4. Ritual Calendar Snapshot

Upcoming, overdue, and recently completed Governance Rituals.

| Ritual | Cadence / trigger | Status | Inputs ready? | Next action |
|--------|-------------------|--------|---------------|-------------|
| Release Readiness Review | Event-triggered | Scheduled | Partial | Attach evidence |
| Monthly Workbench Summary | Monthly | Due | Yes | Start ritual |

### 5. Evolve Triggers

Governance issues that may require changing the operating model.

Examples:
- repeated findings against the same control;
- recurring debt against one threshold;
- ritual action items that repeatedly age out;
- missing dashboard data required for ritual inputs;
- recognition patterns that should become reusable practice.

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Open item | All | Open enforcement, ritual, or register detail |
| Approve / reject | Approver | Decide pending approval |
| Create remediation Work Order | Control Owner / Governance | Create follow-up work |
| Create Evolve Case | Governance / Evolve | Improve policy, ritual, dashboard, or playbook |
| Add recognition | Ritual participant | Create WFR Recognition entry linked to this ritual |
| Export snapshot | Governance | Export governance health snapshot |

---

## Phase Position

| Maturity | Scope |
|----------|-------|
| Phase 1 | Governance health, pending approvals, failed controls, active debt/exceptions, evidence gaps |
| Phase 2 | Ritual calendar, register trends, dashboard snapshots |
| Phase 3 | Advanced governance analytics, Evolve triggers, recognition trend analysis |

---

## Related Consoles

- **Controls & Enforcement** — control status and enforcement items
- **Registers** — risk, debt, exceptions, compliance, findings
- **Team Console / Agent Console** — Workforce recognition and kudos views
- **Rituals** — ritual calendar and outputs
- **Reports & Dashboards** — governance dashboards and exports
