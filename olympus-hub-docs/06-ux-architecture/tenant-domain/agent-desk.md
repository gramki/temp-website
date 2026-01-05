# Agent Desk

> **Status:** 🔴 Stub — Placeholder for expansion

**Agent Desk** is the operational console for Agents to view, investigate, and complete tasks assigned through Task Queues.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | Agent |
| **Scope** | Workbench |
| **Access** | Web, Mobile, MS Teams, MCP (Agent Gateway) |

---

## Console Types

### Utility Consoles (Common)

Utility consoles are shared between Agent Desk and Supervisor Desk:

| Console | Purpose |
|---------|---------|
| **Tasks Console** | View and manage assigned tasks |
| **Files Console** | Access files related to requests and entities |
| **Reports Console** | Run and view operational + business domain reports (via [Hub Analytics](../../04-subsystems/hub-analytics/README.md)) |
| **Knowledge Base Console** | Search SOPs, policies, reference materials |
| **Signals Console** | View exceptions, observations, and other signals |
| **Routines & Checklists Console** | View and complete assigned routines |
| **Agents & Roles Console** | See who is working on what, own roles and responsibilities |

### Optional Consoles (If Enabled by Supervisor/Process Architect)

| Console | Purpose |
|---------|---------|
| **Signals, Triggers, Scenarios Console** | Read-only view of scenario definitions |
| **Operations Console** | View operation flows and status |

> These consoles provide transparency into the operational structure when enabled by Supervisor or Process Architect.

### Custom Consoles

Custom consoles are workbench-specific, built using Angelos Page Builder:

- Entity-specific views (e.g., Customer 360, Transaction Details)
- Domain dashboards (e.g., Dispute Analytics, Fraud Patterns)
- Specialized tools (e.g., Document Comparison, Timeline Viewer)

---

## Task Solver Interface

The Task Solver Interface is the primary work area for processing tasks.

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Custom per Task Type** | Each task type can have its own solver interface |
| **Developer-Defined** | Workbench developers create solver templates |
| **Context-Rich** | Presents all relevant information for decision-making |
| **Action-Oriented** | Clear paths to completion |

### View Modes

| Mode | Purpose |
|------|---------|
| **Read-Only View** | Investigation, context gathering |
| **Solver View** | Decision-making, action execution |

### Standard Sections

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          TASK SOLVER                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  TASK HEADER                                                        │    │
│  │  Task: Verify KYC Documents | Request: REQ-1234 | SLA: 2h remaining │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌───────────────────────────────┐  ┌─────────────────────────────────┐    │
│  │  CONTEXT PANEL                │  │  ACTION PANEL                   │    │
│  │                               │  │                                 │    │
│  │  Subject: John Smith          │  │  [✓ Approve Documents]          │    │
│  │  Entity: Account #12345       │  │  [✗ Reject - Reason Required]   │    │
│  │                               │  │  [↺ Request More Info]          │    │
│  │  Request Timeline:            │  │  [⇧ Escalate to Supervisor]     │    │
│  │  • Dispute filed (2h ago)     │  │                                 │    │
│  │  • Auto-check passed          │  │  ─────────────────────────────  │    │
│  │  • Assigned to you            │  │                                 │    │
│  │                               │  │  Decision Rationale:            │    │
│  │  Related Decisions:           │  │  [________________________]     │    │
│  │  • Previous dispute: Denied   │  │  [________________________]     │    │
│  │                               │  │                                 │    │
│  └───────────────────────────────┘  └─────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  EVIDENCE & DOCUMENTS                                               │    │
│  │  📄 ID Proof.pdf  |  📄 Address Proof.pdf  |  📄 Bank Statement     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  TOOLS                                                              │    │
│  │  [🔍 Query Core Banking] [📞 Contact Customer] [📝 Add Memo]        │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Screen Structure

```
Agent Desk
├── Home (Workbench-specific landing)
│
├── Utility Consoles
│   ├── Tasks
│   │   ├── My Tasks (assigned to me)
│   │   ├── Queue Tasks (pick from queue)
│   │   └── Task History
│   ├── Files
│   ├── Reports
│   ├── Knowledge Base
│   ├── Signals
│   ├── Routines & Checklists
│   └── Agents & Roles
│
├── Optional Consoles (if enabled)
│   ├── Signals, Triggers, Scenarios (read-only)
│   └── Operations
│
├── Custom Consoles
│   └── (Workbench-specific)
│
└── Task Solver
    └── (Opens per selected task)
```

---

## Related Documentation

- [Agent Persona](../../08-personas-and-journeys/personas/agent.md)
- [Task Management](../../04-subsystems/task-management/README.md)
- [Request Lifecycle Journey](../../08-personas-and-journeys/journeys/request-lifecycle.md)
- [Angelos Framework](../frameworks-and-integrations/angelos-framework.md)
- [Hub Analytics](../../04-subsystems/hub-analytics/README.md) — Powers Reports Console

---

*TODO: Detailed console specifications, task solver templates, mobile experience*

