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

## Related Documentation

- [Supervisor Persona](../../08-personas-and-journeys/personas/supervisor.md)
- [Task Management](../../04-subsystems/task-management/README.md)
- [Checklist Service](../../04-subsystems/hub-native-utilities/checklist-service.md)
- [Routine Service](../../04-subsystems/hub-native-utilities/routine-service.md)
- [Hub Analytics](../../04-subsystems/hub-analytics/README.md) — Powers Reports Console

---

*TODO: Detailed analytics specifications, queue management workflows, agent performance tracking*

