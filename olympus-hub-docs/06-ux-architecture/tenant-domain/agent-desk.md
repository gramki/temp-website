# Agent Desk

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-08

**Agent Desk** is the operational console for Agents to view, investigate, and complete tasks assigned through Task Queues.

Agent Desk includes **Intervention Interfaces** for handling escalation tasks created when AI agent outputs are rejected. See [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md) for the full directability model.

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

## Intervention Solver Interface

When an AI agent's output is **rejected** (by guardrails, policies, or applications), an **Escalation Task** is created for human intervention. The Intervention Solver is a specialized Task Solver for resolving these escalations.

### Intervention Solver Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          INTERVENTION SOLVER                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  ESCALATION HEADER                                                       ││
│  │  ⚠ Intervention Required | Request: REQ-1234 | Agent: fraud-case-ai     ││
│  │  Rejection Source: Guardrail | Reason: Confidence below threshold       ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ┌───────────────────────────────┐  ┌─────────────────────────────────────┐ │
│  │  REJECTED ARTIFACT            │  │  ORIGINAL CONTEXT                   │ │
│  │                               │  │                                     │ │
│  │  Type: Decision Result        │  │  Customer: John Smith               │ │
│  │  Agent: fraud-case-ai         │  │  Transaction: TXN-99999             │ │
│  │  Confidence: 0.45             │  │  Amount: $1,250.00                  │ │
│  │  Threshold: 0.70              │  │                                     │ │
│  │                               │  │  Context Provided:                  │ │
│  │  Proposed Decision:           │  │  • Transaction history              │ │
│  │  "Deny refund - suspected     │  │  • Customer profile                 │ │
│  │   first-party fraud"          │  │  • Merchant data                    │ │
│  │                               │  │                                     │ │
│  │  Evidence Considered:         │  │  Missing Context:                   │ │
│  │  • Transaction pattern        │  │  ⚠ Customer tier not provided      │ │
│  │  • Device fingerprint         │  │  ⚠ Previous dispute history empty  │ │
│  └───────────────────────────────┘  └─────────────────────────────────────┘ │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  RESOLUTION OPTIONS                                                      ││
│  │                                                                          ││
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐            ││
│  │  │  ✓ Override     │ │  ↺ Change       │ │  → Reassign     │            ││
│  │  │    Decision     │ │    Context      │ │    Task         │            ││
│  │  └─────────────────┘ └─────────────────┘ └─────────────────┘            ││
│  │                                                                          ││
│  │  ┌─────────────────┐ ┌─────────────────┐                                ││
│  │  │  ✗ Fail         │ │  ⊕ Corrective   │                                ││
│  │  │    Scenario     │ │    Action       │                                ││
│  │  └─────────────────┘ └─────────────────┘                                ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  SELECTED: Override Decision                                             ││
│  │                                                                          ││
│  │  New Decision: [Approve Refund ▼]                                        ││
│  │                                                                          ││
│  │  Rationale: _________________________________________________            ││
│  │             _________________________________________________            ││
│  │                                                                          ││
│  │  Category: [New Information ▼]                                           ││
│  │                                                                          ││
│  │  [Submit Override]                                                       ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Resolution Option Details

| Option | Interface | Effect |
|--------|-----------|--------|
| **Override Decision** | Select new decision, provide rationale | Creates Override Record, completes escalation |
| **Change Context** | Add/modify context fields, instructions | Creates ContextIntervention Record, triggers re-run |
| **Reassign Task** | Select new agent from eligible pool | Reassigns original task, completes escalation |
| **Fail Scenario** | Confirm failure, select reason code | Fails request, cancels tasks, completes escalation |
| **Corrective Action** | Select scenario, provide payload | Creates child request, completes escalation |

### Intervention Solver Access

| Channel | Access Method |
|---------|---------------|
| **Agent Desk (Web)** | Full Intervention Solver UI |
| **MS Teams** | Adaptive card with resolution buttons |
| **MCP (Agent Gateway)** | Programmatic resolution via MCP methods |
| **REST API** | Resolution via Agent REST endpoints |

### Escalation Task Types

| Task Type | Description | Typical Resolver |
|-----------|-------------|------------------|
| `intervention_required` | Standard rejection escalation | Senior Agent / Supervisor |
| `high_impact_intervention` | High-value or high-risk rejection | Supervisor / Manager |
| `compliance_intervention` | Regulatory/compliance rejection | Compliance Officer |

---

---

## Feedback Promotion (Non-Development Workbenches)

In **non-development workbenches** (STAGING, PROD), agents can promote feedback to the linked development workbench. See [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md).

### Feedback Promotion Interface

Agents can promote feedback from any context in the Agent Desk:

| Promotion Point | Typical Feedback |
|-----------------|------------------|
| **Task Solver** | Bug encountered while completing task |
| **Signals Console** | Observation about signal patterns |
| **Knowledge Base Console** | Suggestion for SOP improvement |

### Feedback Promotion Dialog

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     PROMOTE FEEDBACK TO DEVELOPMENT                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Type: [Problem ▼]     Subtype: [Bug ▼]     Severity: [High ▼]              │
│                                                                              │
│  Title: _______________________________________________________________     │
│                                                                              │
│  Description:                                                                │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │                                                                     │    │
│  │                                                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  Related Entities (auto-populated from context):                            │
│  ☑ Request: REQ-1234                                                        │
│  ☑ Task: TASK-5678                                                          │
│  ☑ Scenario: standard-dispute                                               │
│                                                                              │
│  Attachments: [+ Add Screenshot] [+ Add File]                               │
│                                                                              │
│  Target: dispute-ops-dev (Development Workbench)                            │
│                                                                              │
│  [Cancel]                                              [Promote Feedback]   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### My Promoted Feedback

Agents can track feedback they've promoted:

| Column | Description |
|--------|-------------|
| **Title** | Feedback title |
| **Type** | Problem/Feedback subtype |
| **Promoted** | Timestamp |
| **Status** | Pending, In Review, Accepted, Rejected, Resolved |
| **Resolution** | Link to fix (if resolved) |

---

## Related Documentation

- [Agent Persona](../../08-personas-and-journeys/personas/agent.md)
- [Task Management](../../04-subsystems/task-management/README.md)
- [Agent Task Operations](../../04-subsystems/task-management/agent-task-operations.md) — Directability operations
- [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md)
- [Request Lifecycle Journey](../../08-personas-and-journeys/journeys/request-lifecycle.md)
- [Angelos Framework](../frameworks-and-integrations/angelos-framework.md)
- [Hub Analytics](../../04-subsystems/hub-analytics/README.md) — Powers Reports Console
- [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md) — Production feedback architecture

---

