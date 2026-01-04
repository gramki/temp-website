# Observer Notifications

> **Status:** 🔴 Stub — Placeholder for expansion

Signal Exchange captures intermediate updates from long-running Hub Applications and dispatches notifications to **registered observer modules**.

---

## Critical Principle

**Signal Exchange dispatches Request Updates to observer MODULES only — never to agents, tasks, or users directly.**

| Component | Role |
|-----------|------|
| **Signal Exchange** | Dispatches Request Updates to registered observer modules |
| **Observer Modules** | Receive updates, parse content, determine which agents/users to notify |
| **Agents/Users** | Receive notifications from observer modules (not from Signal Exchange) |

Signal Exchange operates at the **Request level**. It cannot:
- Attribute an update to a specific task
- Attribute an update to a specific agent
- Determine which agent should receive a notification

These responsibilities belong to the observer modules (e.g., MS Teams module, Ops Center, Neutrino).

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Dispatch Request Updates to registered observer modules |
| **Trigger** | Async updates from Applications, state transitions |
| **Consumers** | Observer modules (Ops Center, Neutrino, MS Teams module, etc.) |

Long-running Applications (workflows, durable workflows, case management) can take any duration for completion. Signal Exchange dispatches updates to observer modules, which then determine how to notify end users.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    OBSERVER NOTIFICATIONS                        │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              ASYNC UPDATE RECEIVER                       │    │
│  │                                                          │    │
│  │   ← Workflow Apps (Rhea)                                 │    │
│  │   ← Durable Workflow Apps (ChronoShift)                  │    │
│  │   ← Seer Case Orchestration Agents                       │    │
│  │   ← Any long-running Hub Application                     │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │              UPDATE PROCESSOR                            │    │
│  │                                                          │    │
│  │   • Validate update envelope                             │    │
│  │   • Update Request state (if state change)              │    │
│  │   • Record update in Request history                    │    │
│  │   • Identify notification triggers                      │    │
│  └─────────────────────────┼───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │              SUBSCRIPTION REGISTRY                       │    │
│  │                                                          │    │
│  │   • Request-level subscriptions                          │    │
│  │   • User-level subscriptions                             │    │
│  │   • System-level subscriptions                           │    │
│  │   • Filter by event types, state transitions             │    │
│  └─────────────────────────┼───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │              NOTIFICATION DISPATCHER                     │    │
│  │                                                          │    │
│  │   • Format per observer subscription                     │    │
│  │   • Deliver via appropriate channel                      │    │
│  │   • Handle delivery failures / retries                   │    │
│  └─────────────────────────┼───────────────────────────────┘    │
│                            │                                     │
│                            ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    DELIVERY CHANNELS                     │    │
│  │                                                          │    │
│  │   • WebSocket (real-time dashboards, Ops Center)         │    │
│  │   • Webhook (external system callbacks)                  │    │
│  │   • Event Bus (Atropos, for downstream systems)          │    │
│  │   • Push Notification (mobile/desktop via Neutrino)      │    │
│  │   • Email (for non-urgent notifications)                 │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Async Update Message (Application → Signal Exchange)

Hub Applications send async updates using a standard envelope:

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "ASYNC_UPDATE",
    "message_id": "uuid",
    "timestamp": "2026-01-04T12:45:00Z"
  },
  "request": {
    "id": "req-12345",
    "correlation_id": "corr-67890"
  },
  "update": {
    "update_type": "STATUS_CHANGE",     // STATUS_CHANGE | PROGRESS | INFO | MILESTONE | ERROR
    "sequence": 5                        // Ordering for concurrent updates
  },
  "request_status": {
    "status": "ACTIVE",
    "status_reason": "Document verification complete, awaiting review"
  },
  "progress": {
    "percent_complete": 60,
    "current_step": "manager_review",
    "total_steps": 5,
    "completed_steps": 3
  },
  "user_notification": {
    "enabled": true,
    "title": "Document Verified",
    "message": "Your documents have been verified. A manager will review your dispute shortly.",
    "priority": "normal"
  },
  "payload": {
    // Application-specific update details
  }
}
```

---

## Update Types

| Type | Description | Typical Trigger |
|------|-------------|-----------------|
| **STATUS_CHANGE** | Request state transition | State machine advancement |
| **PROGRESS** | Progress indicator update | Step completion, percentage |
| **INFO** | Informational update | FYI for observers |
| **MILESTONE** | Significant milestone reached | Key checkpoint |
| **ERROR** | Error or issue notification | Recoverable error, warning |

---

## Observer Module Registration

### What is an Observer Module?

An **observer module** is a Hub subsystem or integration that:
1. Registers to receive Request Updates from Signal Exchange
2. Parses update content to determine affected entities (tasks, agents, users)
3. Takes appropriate action (notify users, update dashboards, trigger workflows)

| Observer Module | Responsibility |
|-----------------|----------------|
| **Ops Center** | Update dashboards, notify operators |
| **Neutrino** | Notify customers via configured channels |
| **MS Teams Module** | Post to chat groups, add members, notify agents |
| **Atropos** | Publish events to downstream systems |

### Subscription Registration

Observer modules register interest in request lifecycle events:

```json
{
  "subscription": {
    "id": "sub-99999",
    "observer_type": "module",          // module | system | dashboard
    "observer_id": "ms-teams-module",   // Identifies the observer MODULE (not a user)
    
    "scope": {
      "type": "workbench",              // request | workbench | scenario | tenant
      "workbench_id": "dispute-ops"
    },
    
    "filters": {
      "update_types": ["STATUS_CHANGE", "TASK_LIFECYCLE", "MILESTONE", "ERROR"],
      "state_transitions": ["ACTIVE→COMPLETED"],
      "min_priority": "normal"
    },
    
    "delivery": {
      "channel": "webhook",             // websocket | webhook | event
      "endpoint": "https://hub/ms-teams-module/updates",
      "format": "full"                  // full | summary | minimal
    },
    
    "preferences": {
      "batch_window": null,             // null = immediate, or duration
      "max_frequency": "100/s"          // Module-level, not user-level
    }
  }
}
```

### Subscription Scopes

| Scope | Description |
|-------|-------------|
| **Request** | Specific request ID (rarely used by modules) |
| **Workbench** | All requests in a workbench (common for modules) |
| **Scenario** | All requests for a scenario |
| **Tenant** | All requests for tenant (admin dashboards) |

> **Note:** Observer modules typically subscribe at Workbench or Tenant level, then filter updates internally based on their logic. User-level subscriptions (e.g., "notify user X about request Y") are managed by the observer module, not Signal Exchange.

---

## Notification Message

Dispatched to observers:

```json
{
  "notification": {
    "id": "notif-88888",
    "timestamp": "2026-01-04T12:45:01Z",
    "subscription_id": "sub-99999"
  },
  "request": {
    "id": "req-12345",
    "workbench": "Dispute Operations",
    "scenario": "Dispute Filing"
  },
  "event": {
    "type": "STATUS_CHANGE",
    "previous_status": "ACTIVE",
    "current_status": "ACTIVE",
    "status_reason": "Document verification complete, awaiting review"
  },
  "progress": {
    "percent_complete": 60,
    "current_step": "Manager Review"
  },
  "user_content": {
    "title": "Document Verified",
    "message": "Your documents have been verified. A manager will review your dispute shortly."
  },
  "actions": [
    {
      "label": "View Details",
      "url": "https://ops.acme.com/requests/req-12345"
    }
  ]
}
```

---

## Delivery Channels (to Observer Modules)

Signal Exchange delivers to observer modules via these channels:

| Channel | Use Case | Latency |
|---------|----------|---------|
| **WebSocket** | Real-time dashboards, Ops Center module | Immediate |
| **Webhook** | Observer module callbacks | Near-immediate |
| **Event Bus** | Atropos-based observer modules | Near-immediate |

> **Note:** Push notifications and Email are **not** Signal Exchange responsibilities. Observer modules (like Neutrino) handle user-level notification delivery.

---

## Notification Patterns

| Pattern | Configuration | Use Case |
|---------|---------------|----------|
| **Immediate** | `batch_window: null` | Critical updates, real-time dashboards |
| **Batched** | `batch_window: 5m` | Reduce noise, aggregate updates |
| **Digest** | `batch_window: 1h` | Daily/hourly summaries |
| **Quiet Hours** | `quiet_hours: 22:00-08:00` | Respect user preferences |

---

## Built-in Observer Modules

Signal Exchange integrates with these Hub observer modules:

| Observer Module | Responsibility |
|-----------------|----------------|
| **Ops Center** | Update dashboards; operators monitor via UI |
| **Neutrino** | Customer-facing notifications (push, email, SMS) |
| **MS Teams Module** | Post to chat groups, add/notify agents |
| **CAF** | Audit trail of request lifecycle |
| **Atropos** | Event publication for downstream systems |

### Observer Module Responsibility Chain

```
Signal Exchange                    Observer Module                    End User
       │                                 │                                │
       │ ── Request Update ────────────> │                                │
       │    (Request-level only)         │                                │
       │                                 │ ── Parse update ─────────────> │
       │                                 │    Determine affected agents   │
       │                                 │    Format for channel          │
       │                                 │                                │
       │                                 │ ── Deliver notification ─────> │
       │                                 │    (channel-specific)          │
       │                                 │                                │
```

---

## Integration Points

| Component | Integration |
|-----------|-------------|
| **Hub Applications** | Send async updates |
| **Request Factory** | Update request state |
| **Ops Center** | Real-time dashboard updates |
| **Neutrino** | Customer notifications |
| **CAF** | Audit trail |
| **Atropos** | Event publication |

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Message Envelope](./message-envelope.md)
- [Ops Center](../../06-ux-architecture/ops-center.md)
- [User Interaction Channels](../../06-ux-architecture/user-interaction-channels.md)

---

*TODO: Detailed design — subscription management, delivery guarantees, rate limiting, quiet hours*

