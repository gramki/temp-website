# Supervisor Desk

> **Status:** 🔴 Stub — Placeholder for expansion

**Supervisor Desk** is the management console for Supervisors to monitor operations, manage queues, and oversee agents within a Workbench.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | Supervisor |
| **Scope** | Workbench |
| **Access** | Web, MCP (Supervisor Gateway) |

---

## Console Types

### Utility Consoles (Shared with Agent)

| Console | Purpose |
|---------|---------|
| **Tasks Console** | View all tasks, not just assigned |
| **Files Console** | Access files across requests |
| **Reports Console** | Run operational + business domain reports (via [Hub Analytics](../../04-subsystems/hub-analytics/README.md)) |
| **Knowledge Base Console** | Manage SOPs, policies |
| **Signals Console** | Monitor exceptions, observations |
| **Routines & Checklists Console** | Define and monitor checklists |

### Supervisor-Only Consoles

| Console | Purpose |
|---------|---------|
| **Analytics Console** | Queue metrics, SLA tracking, throughput analysis |
| **Task Allocation Management** | Queue configuration, escalation policies |
| **Agents & Access Management** | Agent enrollment, capabilities, availability |

---

## Analytics Console

Real-time and historical views of operational performance.

### Dashboards

| Dashboard | Metrics |
|-----------|---------|
| **Queue Health** | Queue depths, wait times, throughput |
| **SLA Performance** | Compliance rates, at-risk items, breaches |
| **Agent Performance** | Task completion, efficiency, quality |
| **Scenario Performance** | Request volumes, resolution times |

### Sample Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ANALYTICS CONSOLE                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────┐  │
│  │  QUEUE HEALTH        │  │  SLA COMPLIANCE      │  │  ACTIVE AGENTS   │  │
│  │  ██████████░░ 85%    │  │  ████████████ 97%    │  │      12 / 15     │  │
│  │  2 queues at risk    │  │  3 at-risk items     │  │  3 unavailable   │  │
│  └──────────────────────┘  └──────────────────────┘  └──────────────────┘  │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  QUEUE DETAILS                                                      │    │
│  │                                                                     │    │
│  │  Queue              │ Depth │ Wait Time │ Throughput │ SLA Risk    │    │
│  │  ─────────────────────────────────────────────────────────────────  │    │
│  │  Doc Verification   │   8   │   15m     │   4/hr     │  🟢         │    │
│  │  Merchant Contact   │  12   │   45m     │   2/hr     │  🟡         │    │
│  │  Final Decision     │   3   │   20m     │   3/hr     │  🟢         │    │
│  │  Escalations        │   5   │   1h 20m  │   1/hr     │  🔴         │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Task Allocation Management

Configure queues and manage work distribution.

### Capabilities

| Capability | Description |
|------------|-------------|
| **Queue Configuration** | Create queues, set capacity limits |
| **Escalation Policies** | Define timeout thresholds, escalation paths |
| **SLA Rules** | Set SLA targets, warning thresholds |
| **Assignment Rules** | Round-robin, skill-based, load-balanced |
| **Priority Configuration** | Priority levels, override rules |

---

## Agents & Access Management

Manage the agent workforce within the workbench.

### Capabilities

| Capability | Description |
|------------|-------------|
| **Agent Enrollment** | Add/remove agents from queues |
| **Capability Assignment** | Set agent skills and certifications |
| **Availability Management** | Track online/offline, schedule management |
| **Performance Review** | View agent metrics, quality scores |
| **Routine Assignment** | Assign routines to agents |

### Agent View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      AGENTS & ACCESS MANAGEMENT                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Agent          │ Status │ Queues              │ Tasks │ Avg Time │ Quality │
│  ───────────────────────────────────────────────────────────────────────────│
│  Alice Chen     │ 🟢     │ Doc, Decision       │  5    │  12m     │  98%    │
│  Bob Kumar      │ 🟢     │ Doc, Merchant       │  8    │  18m     │  94%    │
│  Carol Smith    │ 🟡     │ Merchant            │  3    │  25m     │  91%    │
│  David Lee      │ ⚫     │ All                 │  -    │  -       │  96%    │
│                                                                              │
│  🟢 Online  🟡 Busy  ⚫ Offline                                              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Screen Structure

```
Supervisor Desk
├── Home (Workbench overview)
│
├── Utility Consoles
│   ├── Tasks (all workbench tasks)
│   ├── Files
│   ├── Reports
│   ├── Knowledge Base
│   ├── Signals
│   └── Routines & Checklists
│
├── Supervisor Consoles
│   ├── Analytics
│   │   ├── Queue Dashboard
│   │   ├── SLA Dashboard
│   │   ├── Agent Dashboard
│   │   └── Trend Analysis
│   ├── Task Allocation
│   │   ├── Queues
│   │   ├── Escalation Policies
│   │   └── Assignment Rules
│   └── Agents & Access
│       ├── Agent List
│       ├── Capabilities
│       ├── Availability
│       └── Routines
│
└── Escalation Queue
    └── (High-priority view of escalated items)
```

---

---

## Feedback Promotion (Non-Development Workbenches)

In **non-development workbenches** (STAGING, PROD), supervisors can promote feedback to the linked development workbench. Supervisors typically promote operational issues and critical limitations. See [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md).

### Feedback Promotion Points

| Console | Typical Promotions |
|---------|-------------------|
| **Analytics Console** | Issues with metrics, thresholds, or SLA configurations |
| **Task Allocation** | Escalation policy issues, queue configuration problems |
| **Signals Console** | Pattern observations, signal handling bugs |
| **Escalation Queue** | Systemic escalation issues, process gaps |

### Feedback Console (Supervisor-Specific)

Supervisors have a dedicated console for managing and promoting operational feedback:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        FEEDBACK CONSOLE                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  [+ New Feedback]                              [Filter: Open ▼]             │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  LOCAL ISSUES (This Workbench)                                        │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │ 🔴 Queue config causing missed SLAs     | Open    | [Promote]         │  │
│  │ 🟡 Escalation matrix needs adjustment   | Open    | [Promote]         │  │
│  │ 🟢 Agent skill mapping verified         | Closed  |                   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  PROMOTED TO DEVELOPMENT                                              │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │ Escalation not triggering for priority | Pending  | Promoted 2h ago  │  │
│  │ SLA thresholds too aggressive          | In Review| Promoted 1d ago  │  │
│  │ Missing notification template          | Resolved | Fixed in v1.3.0  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Supervisor Feedback Types

| Type | Subtype | Description |
|------|---------|-------------|
| **Problem** | Bug | Implementation defect affecting operations |
| **Problem** | Issue | Operational constraint requiring attention |
| **Problem** | Critical Limitation | Capability gap blocking operations |
| **Feedback** | Observation | Behavioral pattern worth noting |
| **Feedback** | Suggestion | Improvement idea |

---

## Persona Twins Console

Supervisors can create and manage **Persona Twins** — personal AI agents that handle delegated tasks, notifications, and scheduled activities.

### Persona Twins Section

Within the Supervisor Desk, the Persona Twins console is accessible via Scenarios:

```
Supervisor Desk
├── ...
├── Scenarios
│   ├── Business Scenarios (operational scenarios)
│   └── Persona Twins
│       ├── My Twins (supervisor's personal twins)
│       │   ├── Task Triage Assistant
│       │   └── Daily Summary Bot
│       └── All Twins (admin view)
└── ...
```

### Persona Twin Management

| Capability | Description |
|------------|-------------|
| **Create Twin** | Create a new Persona Twin from blueprint |
| **View Activity** | Monitor twin's requests and actions |
| **Configure Triggers** | Set up task assignment, notification, and schedule triggers |
| **Manage Authority** | Configure delegation and OPA policies |
| **Suspend/Resume** | Temporarily disable or re-enable twin |

### Sample Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PERSONA TWINS CONSOLE                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  [+ Create Persona Twin]                                                    │
│                                                                              │
│  MY TWINS                                                                   │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ Twin                    │ Status │ Today │ Last Active │ Actions     │  │
│  │ ─────────────────────────────────────────────────────────────────────│  │
│  │ Task Triage Assistant   │ 🟢     │   12  │ 5m ago      │ [Configure] │  │
│  │ Daily Summary Bot       │ 🟢     │    1  │ 2h ago      │ [Configure] │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  RECENT ACTIVITY                                                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ 10:32 AM │ Task Triage Assistant │ Triaged high-priority dispute    │  │
│  │ 10:28 AM │ Task Triage Assistant │ Gathered context for case #4521  │  │
│  │ 10:15 AM │ Task Triage Assistant │ Prepared recommendation          │  │
│  │  5:00 PM │ Daily Summary Bot     │ Generated end-of-day summary     │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Supervisor Use Cases for Persona Twins

| Use Case | Blueprint | Triggers |
|----------|-----------|----------|
| Task Triage | Task Triage Assistant | Task assignments (high priority) |
| End-of-Day Review | Collaborator Assistant | Daily schedule (5 PM) |
| Escalation Monitor | Compliance Monitor | Platform notifications |
| Weekly Planning | Collaborator Assistant | Weekly schedule (Monday 9 AM) |

---

## Related Documentation

- [Supervisor Persona](../../08-personas-and-journeys/personas/supervisor.md)
- [Task Management](../../04-subsystems/task-management/README.md)
- [Checklist Service](../../04-subsystems/hub-native-utilities/checklist-service.md)
- [Routine Service](../../04-subsystems/hub-native-utilities/routine-service.md)
- [Hub Analytics](../../04-subsystems/hub-analytics/README.md) — Powers Reports Console
- [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md) — Production feedback architecture
- [Persona Twin Creation Guide](../../10-guides/persona-twin-creation-guide.md) — How to create twins
- [Persona Twin Management Guide](../../10-guides/persona-twin-management-guide.md) — How to manage twins
- [Persona Twins Concept](../../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md) — Technical concept

---

*TODO: Detailed analytics specifications, queue management workflows, agent performance tracking*

