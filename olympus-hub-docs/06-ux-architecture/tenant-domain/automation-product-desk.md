# Automation Product Desk

> **Status:** 🔴 Stub — Placeholder for expansion

**Automation Product Desk** is the strategic workspace for **Automation Product Owners (APO)** to define, track, and evolve automation capabilities within a Workbench.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | Automation Product Owner (APO) |
| **Scope** | Workbench |
| **Access** | Web, MCP (Creator Gateway) |

---

## Purpose

The APO owns the **business intent** behind automation. This desk provides tools to:

1. **Define** — Create automation charters and articulate business value
2. **Track** — Monitor outcomes against success criteria
3. **Prioritize** — Manage the automation backlog and roadmap
4. **Evolve** — Review learnings and iterate on automation strategy

---

## Consoles

### Charter Console

Define and manage automation charters — the business case for each automation capability.

| Capability | Description |
|------------|-------------|
| **Charter Builder** | Create automation charters with business case, scope, success criteria |
| **Value Proposition** | Document problem, opportunity, and expected value |
| **Success Criteria** | Define measurable KPIs and targets |
| **Scope Definition** | Specify in-scope and out-of-scope boundaries |
| **Stakeholder Mapping** | Identify sponsors, approvers, and stakeholders |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          CHARTER CONSOLE                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Automation Charters                                                 │    │
│  │                                                                      │    │
│  │  [+] New Charter    [Filter: Active ▼]    [Search...]               │    │
│  │                                                                      │    │
│  │  ┌───────────────────────────────────────────────────────────────┐  │    │
│  │  │ Dispute Resolution Automation              ACTIVE              │  │    │
│  │  │ Target: Reduce processing time by 80%     Progress: 65%       │  │    │
│  │  ├───────────────────────────────────────────────────────────────┤  │    │
│  │  │ Card Replacement Automation               DESIGN               │  │    │
│  │  │ Target: Same-day card dispatch            Progress: 20%       │  │    │
│  │  └───────────────────────────────────────────────────────────────┘  │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Outcomes Console

Track business outcomes and value realization for active automations.

| Capability | Description |
|------------|-------------|
| **KPI Dashboard** | Live metrics against charter targets |
| **Value Tracking** | Measure realized value (time saved, cost reduced, etc.) |
| **Trend Analysis** | Track progress over time |
| **Outcome Reports** | Generate stakeholder reports |

### Backlog Console

Manage the automation backlog and prioritization.

| Capability | Description |
|------------|-------------|
| **Backlog View** | List of proposed and in-progress automation initiatives |
| **Prioritization** | Rank by value, effort, risk |
| **Roadmap** | Timeline view of planned automation rollouts |
| **Dependencies** | Track cross-automation dependencies |

### Feedback Console

Capture and route feedback from operations within the current workbench.

| Capability | Description |
|------------|-------------|
| **Issue Aggregation** | View issues raised during Run stage |
| **Feedback Triage** | Categorize, prioritize, and route feedback |
| **Improvement Proposals** | Draft proposals for Evolve stage |
| **Stakeholder Updates** | Communicate progress to sponsors |

### Production Feedback Inbox (Development Workbenches Only)

In **development stage workbenches**, the APO receives feedback promoted from linked production workbenches. See [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md).

| Capability | Description |
|------------|-------------|
| **Inbox** | View all incoming Problems and Feedback from linked production workbenches |
| **Source Filter** | Filter by source workbench (APAC, EMEA, Staging, etc.) |
| **Type Filter** | Filter by type (Bug, Issue, Critical Limitation, Observation, Suggestion, Learning) |
| **Severity Filter** | Filter by severity (Critical, High, Medium, Low) |
| **Triage** | Accept, reject, or route feedback to PA/Developer |
| **Link to Backlog** | Associate feedback with backlog items |
| **Resolve** | Mark resolved and link to fix (scenario version, release) |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     PRODUCTION FEEDBACK INBOX                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  [Filter: All Sources ▼] [Type: All ▼] [Severity: All ▼] [Status: Pending ▼]│
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ 🔴 BUG | Escalation not triggering                                    │  │
│  │    From: dispute-ops-prod-apac | Promoted by: supervisor@acme.com    │  │
│  │    Severity: High | Status: Pending                                   │  │
│  │    Related: REQ-1234, standard-dispute scenario                       │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │ 🟡 ISSUE | SLA thresholds too aggressive for EMEA timezone           │  │
│  │    From: dispute-ops-prod-emea | Promoted by: supervisor@acme.eu     │  │
│  │    Severity: Medium | Status: In Review                               │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │ 💡 SUGGESTION | Add document preview in task solver                   │  │
│  │    From: dispute-ops-staging | Promoted by: agent@acme.com           │  │
│  │    Severity: Low | Status: Accepted                                   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  [Accept] [Reject] [Route to PA] [Route to Dev] [Link to Backlog]           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Feedback Item Detail View

When APO selects a feedback item:

| Section | Content |
|---------|---------|
| **Header** | Type, title, severity, status |
| **Lineage** | Source workbench, promoter, promotion timestamp |
| **Content** | Full description, attachments |
| **Related Entities** | Linked requests, tasks, scenarios |
| **Actions** | Accept, Reject (with reason), Route, Resolve |
| **Resolution** | Link to fix (scenario version, release notes) |

#### Action Reflection

When APO takes action, status is reflected back to the source workbench:

| Action | Source Workbench Effect |
|--------|------------------------|
| **Accept** | Status → `accepted`, promoter notified |
| **Reject** | Status → `rejected` (with reason), promoter notified |
| **Route** | Status → `routed` (to PA/Developer), promoter notified |
| **Resolve** | Status → `resolved` (with link to fix), promoter + supervisor notified |

---

## Key Workflows

### 1. Charter Creation

```
APO                    Charter Console              Workbench
 │                           │                          │
 ├─── Create Charter ───────▶│                          │
 │                           ├─── Save to Workbench ───▶│
 │                           │                          │
 │◀── Charter Draft ─────────┤                          │
 │                           │                          │
 ├─── Submit for Approval ──▶│                          │
 │                           ├─── Notify Sponsor ──────▶│
 │                           │                          │
```

### 2. Outcome Review

```
APO                    Outcomes Console            Analytics
 │                           │                          │
 ├─── View Dashboard ───────▶│                          │
 │                           ├─── Fetch Metrics ───────▶│
 │                           │◀── Aggregated Data ──────┤
 │◀── KPI Dashboard ─────────┤                          │
 │                           │                          │
 ├─── Generate Report ──────▶│                          │
 │◀── Stakeholder Report ────┤                          │
```

### 3. Automation Approach Decision

```
APO                    Charter Console          Process Architect
 │                           │                          │
 ├─── Propose Approach ─────▶│                          │
 │    (Conventional/Agentic) │                          │
 │                           ├─── Notify PA ───────────▶│
 │                           │                          │
 │                           │◀── PA Validates ─────────┤
 │◀── Approach Confirmed ────┤                          │
 │                           │                          │
```

### 4. Production Feedback Review (Development Workbench)

```
Production WB              Dev Workbench APO           PA / Developer
    │                           │                          │
    ├─── Promote Feedback ─────▶│                          │
    │    (with lineage)         │                          │
    │                           │                          │
    │                           ├─── Review in Inbox ─────▶│
    │                           │                          │
    │                           ├─── Accept / Route ──────▶│
    │                           │                          │
    │◀── Status Reflected ──────┤                          │
    │                           │                          │
    │                           │◀── Resolved ─────────────┤
    │◀── Resolution Link ───────┤                          │
    │                           │                          │
```

---

## Integration with Other Desks

| Related Desk | Handoff |
|--------------|---------|
| **Scenario Design Desk** | APO → PA: Charter approved, scenario design begins |
| **Automation Development Desk** | Visibility: Track implementation progress |
| **Supervisor Desk** | Run stage: Receive operational feedback |

---

## Automation Approach Decision

The APO proposes whether a scenario should use:

| Approach | Criteria | Next Step |
|----------|----------|-----------|
| **Conventional** | Structured inputs, rule-based logic | PA → Developer (Hub Application) |
| **Agentic** | Unstructured inputs, judgment required | Transition to Seer lifecycle |
| **Hybrid** | Mix of both | PA defines boundaries |

> **Note:** For agentic automation, the scenario transitions to the Seer Agentic Automation Lifecycle after APO/PA decision.

---

## Channel Support

| Channel | Access |
|---------|--------|
| **Web** | Full desk access |
| **MCP** | Charter query, outcome metrics via Creator Gateway |
| **REST** | Programmatic access to charters and outcomes |

---

## Related Documentation

- [Automation Product Owner Persona](../../08-personas-and-journeys/personas/automation-product-owner.md)
- [Automation Lifecycle Journey](../../08-personas-and-journeys/journeys/automation-lifecycle.md)
- [Scenario Design Desk](./scenario-design-desk.md) — Where PA takes over after charter approval
- [Hub Analytics](../../04-subsystems/hub-analytics/README.md) — Powers outcome dashboards
- [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md) — Production feedback architecture

---

*TODO: Detailed charter templates, outcome tracking specifications, backlog management workflows*

