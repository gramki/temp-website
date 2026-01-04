# Observer Notifications

> **Status:** 🔴 Stub — Placeholder for expansion

Signal Exchange captures intermediate updates from long-running Hub Applications and dispatches notifications to interested observers.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Notify interested parties of request lifecycle changes |
| **Trigger** | Async updates from Applications, state transitions |
| **Consumers** | Users, systems, dashboards, downstream services |

Long-running Applications (workflows, durable workflows, case management) can take any duration for completion. Signal Exchange ensures observers are notified of intermediate status changes.

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

## Observer Subscriptions

### Subscription Registration

Observers register interest in request lifecycle events:

```json
{
  "subscription": {
    "id": "sub-99999",
    "observer_type": "user",           // user | system | dashboard
    "observer_id": "user-12345",
    
    "scope": {
      "type": "request",               // request | workbench | scenario | tenant
      "request_id": "req-12345"        // Specific request
    },
    
    "filters": {
      "update_types": ["STATUS_CHANGE", "MILESTONE", "ERROR"],
      "state_transitions": ["IN-PROGRESS→COMPLETED"],
      "min_priority": "normal"
    },
    
    "delivery": {
      "channel": "websocket",          // websocket | webhook | event | push | email
      "endpoint": "wss://...",         // Channel-specific endpoint
      "format": "summary"              // full | summary | minimal
    },
    
    "preferences": {
      "batch_window": null,            // null = immediate, or duration
      "quiet_hours": null,
      "max_frequency": "1/min"
    }
  }
}
```

### Subscription Scopes

| Scope | Description |
|-------|-------------|
| **Request** | Specific request ID |
| **Workbench** | All requests in a workbench |
| **Scenario** | All requests for a scenario |
| **Tenant** | All requests for tenant (admin) |

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

## Delivery Channels

| Channel | Use Case | Latency |
|---------|----------|---------|
| **WebSocket** | Real-time dashboards, Ops Center | Immediate |
| **Webhook** | External system integration | Near-immediate |
| **Event Bus** | Downstream service triggers | Near-immediate |
| **Push** | Mobile/desktop notifications | Seconds |
| **Email** | Non-urgent, audit trail | Minutes |

---

## Notification Patterns

| Pattern | Configuration | Use Case |
|---------|---------------|----------|
| **Immediate** | `batch_window: null` | Critical updates, real-time dashboards |
| **Batched** | `batch_window: 5m` | Reduce noise, aggregate updates |
| **Digest** | `batch_window: 1h` | Daily/hourly summaries |
| **Quiet Hours** | `quiet_hours: 22:00-08:00` | Respect user preferences |

---

## Built-in Observers

Signal Exchange provides built-in observer integrations:

| Observer | Description |
|----------|-------------|
| **Ops Center** | Real-time request status in operations dashboard |
| **Neutrino** | User notifications via customer channels |
| **CAF** | Audit trail of request lifecycle |
| **Atropos** | Event publication for downstream systems |

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

