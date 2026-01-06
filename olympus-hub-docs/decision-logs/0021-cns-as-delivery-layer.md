# ADR-0021: Cipher Notification Service as Delivery Layer

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub's Notification Services subsystem translates Request Updates into notifications for various personas. These notifications must be delivered via multiple mechanisms:
- Email
- SMS
- Push Notifications
- Webhooks

Each mechanism requires:
- Integration with service providers (SendGrid, Twilio, Firebase, etc.)
- Retry logic for transient failures
- Delivery tracking and status callbacks
- Read receipt handling (where supported)
- CTA (Call-to-Action) response handling

The question is where this delivery logic should reside:
- Within Hub's Notification Services
- In an external delivery service (Cipher Notification Service - CNS)

## Decision

**Cipher Notification Service (CNS)** is the delivery layer for all Hub notifications.

### Responsibility Split

| Component | Responsibility |
|-----------|----------------|
| **Notification Services (Hub)** | Translate Request Updates to notifications, resolve recipients, render templates, apply preferences, send to CNS |
| **CNS (External)** | Route to service providers, handle delivery/retries/failures, track delivery status, send callbacks |

### Integration Flow

```
Notification Services                 CNS                    Service Provider
       │                               │                            │
       │ ── Notification Request ────> │                            │
       │    (rendered content,         │                            │
       │     recipient, mechanism,     │                            │
       │     callback URL, CTA)        │                            │
       │                               │ ── Deliver ───────────────> │
       │                               │    (Email/SMS/Push/Webhook) │
       │                               │                            │
       │                               │ <── Delivery Status ────── │
       │                               │                            │
       │ <── Callback ─────────────────│                            │
       │    (status, read receipt,     │                            │
       │     CTA response)             │                            │
```

### Callback Types from CNS

1. **Delivery Status**: Success, failure, bounce
2. **Read Receipts**: When recipient reads notification (mechanism-dependent)
3. **CTA Responses**: When recipient clicks action button

### CTA Handling

1. CNS generates correlation tracker in CTA URLs
2. When user clicks CTA, CNS receives request
3. CNS sends callback to Notification Services with correlation info
4. Notification Services creates signal and sends to Signal Exchange
5. Signal correlates to original Request

## Alternatives Considered

### Alternative 1: Hub Manages Delivery Directly
Notification Services integrates directly with Email/SMS/Push providers.

- **Pros**: Fewer external dependencies, simpler architecture
- **Cons**: Duplicates Cipher's existing capability, more code to maintain, less robust retry logic

### Alternative 2: CNS Pulls Notifications
CNS polls Hub for pending notifications.

- **Pros**: CNS controls rate
- **Cons**: Increased latency, inefficient, complex state management

### Alternative 3: Event-Based Integration (Atropos)
Notifications published to event bus; CNS subscribes.

- **Pros**: Decoupled, async
- **Cons**: No direct acknowledgment, harder to track delivery, complex correlation

## Consequences

### Positive
- **Reuse**: Leverages CNS's existing delivery infrastructure
- **Reliability**: CNS handles retries, failover across providers
- **Separation**: Hub focuses on notification logic; CNS focuses on delivery
- **Consistency**: Same delivery infrastructure used across Olympus platform

### Negative
- **External Dependency**: Hub depends on CNS availability
- **Callback Complexity**: Must handle async callbacks for status updates
- **Correlation Management**: Must maintain correlation between notification and original request

### Neutral
- Callback URLs registered per workbench with CNS
- CNS manages correlation tracker generation
- Read receipt support varies by mechanism

## Callback URL Pattern

Notification Services registers callback URLs with CNS:
- **Format**: `https://hub/notification-services/{workbench_id}/callbacks`
- **Scope**: Per workbench
- **Resolution**: `{workbench_id}` resolved from request context when sending to CNS

## Delivery Failure Handling

1. CNS exhausts all retry attempts
2. CNS sends failure callback to Notification Services
3. Notification Services creates signal (acts as Signal Provider)
4. Signal Exchange has preconfigured trigger that translates to MEMO
5. MEMO recorded against request scope

## Related Decisions

- [ADR-0005: Notification Services Architecture](./0005-notification-services-architecture.md)
- [ADR-0019: Signal Exchange Observer Pattern](./0019-signal-exchange-observer-pattern.md)

