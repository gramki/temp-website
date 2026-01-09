# ADR-0019: Signal Exchange Observer Pattern for Module Integration

## Status

**Accepted**

## Date

2026-01-06

## Context

Signal Exchange (SX) captures intermediate updates from long-running Hub Applications and must distribute these updates to various Hub subsystems and integrations:
- Notification Services (for Email, SMS, Push notifications)
- Task Management (for task assignment and escalation)
- Ops Center (for real-time dashboards)
- MS Teams Module (for chat group notifications)
- CAF (for audit trail)
- Atropos (for downstream event publication)

The question is how SX should integrate with these diverse consumers with different:
- Update type interests (some care about TASK_LIFECYCLE, others about STATUS_CHANGE)
- Delivery requirements (real-time vs. batched)
- Scope requirements (per-request, per-workbench, per-tenant)

## Decision

Signal Exchange implements an **Observer Pattern** where:

1. **Observer Modules Register with SX**: Subsystems register as observer modules with subscription specifications

2. **Subscription-Based Filtering**: Each observer specifies:
   - **Scope**: Request, Workbench, Scenario, or Tenant level
   - **Update Types**: Which event types to receive (STATUS_CHANGE, TASK_LIFECYCLE, MILESTONE, etc.)
   - **Delivery Channel**: WebSocket, Webhook, or Event Bus
   - **Delivery Preferences**: Immediate, batched, or digest

3. **SX Dispatches to Modules Only**: Signal Exchange dispatches Request Updates to registered observer **modules** — never directly to agents, tasks, or users

4. **Modules Handle User-Level Routing**: Observer modules receive Request Updates and determine internally which agents/users to notify

```
Signal Exchange                    Observer Module                    End User
       │                                 │                                │
       │ ── Request Update ────────────> │                                │
       │    (Request-level only)         │                                │
       │                                 │ ── Parse update ─────────────> │
       │                                 │    Determine affected agents   │
       │                                 │    Format for channel          │
       │                                 │ ── Deliver notification ─────> │
```

## Alternatives Considered

### Alternative 1: Direct User Notifications from SX
SX maintains user subscriptions and delivers notifications directly.

- **Pros**: Simpler architecture, fewer hops
- **Cons**: SX becomes bloated, violates single responsibility, must understand all notification channels

### Alternative 2: Pub/Sub Event Bus Only
All updates published to Atropos; consumers subscribe to event bus.

- **Pros**: Decoupled, standard pub/sub pattern
- **Cons**: No guaranteed delivery, higher latency, difficult to manage subscriptions

### Alternative 3: Polling-Based Integration
Consumers poll SX for updates.

- **Pros**: Simple for SX, consumers control rate
- **Cons**: Increased latency, inefficient, doesn't scale

## Consequences

### Positive
- **Separation of Concerns**: SX handles request lifecycle; modules handle user delivery
- **Scalable**: Modules can scale independently
- **Flexible**: Each module defines its own subscription scope and filters
- **Extensible**: New observer modules can be added without changing SX

### Negative
- **Additional Hop**: Updates pass through observer modules before reaching users
- **Subscription Management**: SX must track and validate subscriptions
- **Delivery Guarantees**: SX must ensure reliable delivery to observer modules

### Neutral
- Observer modules are responsible for their internal user-level routing
- SX provides at-least-once delivery to observer modules

## Observer Module Examples

| Observer Module | Scope | Update Types | Responsibility |
|-----------------|-------|--------------|----------------|
| **Notification Services** | Tenant | All | Translate to Email/SMS/Push per user preferences |
| **Task Management** | Tenant | TASK_LIFECYCLE | Assign tasks, manage escalations |
| **Ops Center** | Workbench | All | Update real-time dashboards |
| **MS Teams Module** | Workbench | TASK_LIFECYCLE, MILESTONE | Post to chat groups |
| **CAF** | Tenant | All | Audit trail recording |

## Related Decisions

- [ADR-0003: Signal Exchange Responsibility Boundaries](./0003-signal-exchange-responsibility-boundaries.md)
- [ADR-0020: Request-Level Granularity for Signal Exchange](./0020-request-level-granularity.md)
- [ADR-0005: Notification Services Architecture](./0005-notification-services-architecture.md)

