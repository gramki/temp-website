# Request Management

> **Status:** 🟡 Draft — Core concepts defined

Request Management handles the **lifecycle, storage, and entity binding for Requests**—the standardized inputs to Operations.

---

## Overview

From Hub Architecture:
> *"Signal → Trigger → Request → Scenario → Operation"*

Requests are the **standardized representation** of work to be done, created from Signals by Triggers, and consumed by Automation Runtimes.

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Request Lifecycle](./request-lifecycle.md) | Request states, updates, session boundary | 🔴 Stub |
| [Request Hierarchy](./request-hierarchy.md) | Parent-child requests, context inheritance, lifecycle cascade | ✅ Complete |
| [Request Storage](./request-storage.md) | Request scope storage | 🔴 Stub |
| [Request Entity Binding](./request-entity-binding.md) | Request to Business Entity mapping | 🔴 Stub |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   REQUEST MANAGEMENT                             │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 REQUEST LIFECYCLE                        │    │
│  │       (States, Updates, Session Management)              │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │              REQUEST SERVICES                            │    │
│  │                                                          │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │    │
│  │  │   Storage    │  │   Entity     │  │   Memory     │   │    │
│  │  │   Service    │  │   Binding    │  │  Integration │   │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │            AUTOMATION SYSTEMS                            │    │
│  │    (Consume Requests, Update Status)                     │    │
│  └──────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Request Types

From Hub Architecture:

| Type | Initiated By | Subject Association |
|------|--------------|---------------------|
| **Service Requests** | Customers (self-service or assisted) | Required — always identifies a customer |
| **Business Requests** | Operations teams, Internal users | Optional |
| **System Requests** | Applications/Machines | Optional |

---

## Request as Session Boundary

From Todo notes:
> *"Request as a Session Boundary"*

Requests define the boundary for:
- Scope storage (request-scoped data)
- Memory context
- Audit trail
- Participant involvement

---

## Request-like Entities

From Todo notes:
> *"Requests are like Jira Items, they can have various comments and statuses"*

Requests support:
- Status updates
- Comments and notes
- Attachments
- Participant tracking
- Timeline of events

---

## Enterprise Memory Integration

Requests integrate with Enterprise Memory:
- Decision Records linked to request
- Evidence Bundles scoped to request
- Outcome Records linked to request

---

## Related Documentation

- [Hub Architecture - Signals](../../02-system-design/hub-architecture.md#13-signals)
- [Hub Architecture - Triggers](../../02-system-design/hub-architecture.md#14-triggers)
- [I/O Gateways](../signal-providers/README.md)
- [Automation Runtimes](../automation-runtimes/README.md)

---

*TODO: Detailed design — request schema, lifecycle state machine, storage model*

