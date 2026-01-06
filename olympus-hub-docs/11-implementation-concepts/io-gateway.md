# I/O Gateway

> **Category:** Signal Architecture

---

## Overview

An **I/O Gateway** is Hub's protocol-specific entry and exit point for signals. Gateways handle transport layer concerns (HTTP, event streams, files, schedules), normalize incoming signals to the standard DTO format, and deliver outbound updates to Signal Providers. Each Gateway is specialized for a particular protocol while conforming to Hub's normalized signal contract.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Sensors** as components that detect signals from the environment, and **Signal** as the raw data captured. I/O Gateways are the implementation of sensor ingress and actuator egress at the platform level.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Sensor | I/O Gateway (inbound) | Gateway receives signals from sensors |
| Signal | Normalized Signal DTO | Gateway normalizes to standard format |
| Command/Actuator | I/O Gateway (outbound) | Gateway delivers updates to actuators |

### Gap This Fills

The ontology describes signals abstractly. I/O Gateways specify:
1. **Protocol handling**: How different transports are managed
2. **Normalization**: How protocol-specific data becomes standard DTO
3. **Security**: How authentication and authorization are enforced
4. **Routing**: How signals reach Signal Exchange

---

## Definition

**I/O Gateway** is a protocol-specific component that:
- Accepts signals in protocol-native format
- Normalizes signals to standard DTO
- Forwards normalized signals to Signal Exchange
- Receives updates from Signal Exchange
- Delivers updates in protocol-native format

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Platform-wide; shared across subscriptions |
| **Lifecycle** | Deployed and managed by SRE |
| **Ownership** | Platform-owned; tenant-configured per Signal Provider |
| **Multiplicity** | One per protocol type |

---

## Rationale

### Why This Design?

Protocol abstraction enables:
1. **Signal Exchange simplicity**: SX only handles normalized DTOs
2. **Protocol diversity**: Different sources, same processing
3. **Security boundary**: Gateways enforce access control
4. **Extensibility**: New protocols without SX changes

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Direct SX protocol handling** | SX becomes complex; protocol coupling |
| **Single gateway type** | Can't optimize per protocol |
| **Application-level normalization** | Inconsistent; security gaps |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0001](../decision-logs/0001-signal-normalization.md) | Normalize signal format between SPs and SX |

---

## Structure

### Hub I/O Gateways

| Gateway | Protocol | Use Cases |
|---------|----------|-----------|
| **Heracles** | HTTP/REST/MCP | API calls, web hooks, AI agents |
| **Atropos** | Event Bus (Kafka, RabbitMQ) | Event-driven signals, CDC |
| **Cronus** | Business Exceptions | Exception queues, observations |
| **Dia** | File/Batch | File uploads, bulk processing |
| **Kale** | Scheduler | Time-based signals (cron) |
| **MS Teams** | Teams Bot Framework | Chat messages, commands |

### Gateway Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    I/O GATEWAY ARCHITECTURE                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   EXTERNAL SYSTEM                       HUB INTERNAL                         │
│   ───────────────                       ────────────                         │
│                                                                              │
│   ┌───────────────┐                    ┌───────────────┐                    │
│   │ HTTP Client   │                    │               │                    │
│   │ (REST API)    │───────────────────▶│   HERACLES    │                    │
│   └───────────────┘                    │   Gateway     │                    │
│                                        │               │                    │
│   ┌───────────────┐                    │  ┌─────────┐  │   ┌─────────────┐  │
│   │ Kafka Topic   │                    │  │Transport│  │   │             │  │
│   │ (Events)      │───────────────────▶│  │ Handler │  │──▶│   Signal    │  │
│   └───────────────┘   ATROPOS          │  └────┬────┘  │   │  Exchange   │  │
│                       Gateway          │       │       │   │             │  │
│   ┌───────────────┐                    │  ┌────▼────┐  │   │             │  │
│   │ S3/SFTP       │                    │  │Normalize│  │   │             │  │
│   │ (Files)       │───────────────────▶│  │  DTO    │  │──▶│             │  │
│   └───────────────┘   DIA              │  └─────────┘  │   │             │  │
│                       Gateway          │               │   │             │  │
│   ┌───────────────┐                    │  ┌─────────┐  │   │             │  │
│   │ Cron Schedule │                    │  │ Auth &  │  │   │             │  │
│   │ (Time)        │───────────────────▶│  │ Access  │  │   │             │  │
│   └───────────────┘   KALE             │  └─────────┘  │   └─────────────┘  │
│                       Gateway          │               │                    │
│                                        └───────────────┘                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Normalized Signal DTO

```json
{
  "signal_header": {
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "signal_id": "sig-12345",
    "signal_type": "dispute.filed",
    "timestamp": "2026-01-06T10:00:00Z",
    "correlation_id": "txn-99999",
    "idempotency_key": "idem-22222"
  },
  "payload": {
    "content_type": "application/json",
    "data": {
      /* Protocol-specific payload normalized */
    }
  },
  "metadata": {
    "source_system": "core-banking",
    "source_event_id": "evt-99999",
    "trace_id": "trace-abc123"
  }
}
```

---

## Behavior

### Inbound Flow

```
1. External system sends protocol-native request
   └── HTTP POST, Kafka message, file drop, etc.

2. Gateway receives and validates:
   ├── Transport-level authentication
   ├── Access control (tenant, subscription)
   └── Payload validation

3. Gateway normalizes to DTO:
   ├── Extract tenant/subscription context
   ├── Map protocol fields to standard structure
   └── Generate signal_id, timestamp

4. Gateway forwards to Signal Exchange:
   └── Normalized DTO via internal protocol

5. Gateway returns acknowledgment:
   └── Sync: wait for SX response
   └── Async: immediate ACK, SX processes later
```

### Outbound Flow

```
1. Signal Exchange has update for Signal Provider
2. SX routes to appropriate Gateway
3. Gateway transforms to protocol-native format
4. Gateway delivers to registered endpoint
5. Gateway reports delivery status back to SX
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| External Systems | ↔ bidirectional | Receive signals, send updates |
| Signal Exchange | ↔ bidirectional | Forward signals, receive updates |
| Signal Provider Registry | ← reads | Provider configurations |
| Cipher IAM | ← authenticates | Validate credentials |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Tenant scoping** | All signals must include tenant context |
| **Subscription scoping** | All signals must include subscription context |
| **Normalization** | All signals must be normalized before SX |
| **Authentication** | All requests must be authenticated |
| **Idempotency** | Gateways should support idempotency keys |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Protocol abstraction** | SX doesn't deal with protocol details |
| ✅ **Security boundary** | Auth/access enforced at edge |
| ✅ **Specialized optimization** | Each gateway optimized for its protocol |
| ✅ **Extensibility** | Add new gateways without SX changes |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Multiple components** | Managed by platform; transparent to tenants |
| ⚠️ **Normalization overhead** | Efficient transformation; minimal latency |

---

## Examples

### Example 1: Heracles HTTP Gateway

```yaml
# Signal Provider registration for HTTP
provider:
  name: core-banking-webhooks
  gateway: heracles
  
  inbound:
    path: "/signals/core-banking"
    methods: ["POST"]
    auth:
      type: bearer
      validate_with: cipher-iam
      
  outbound:
    endpoint: "https://core.acme.com/hub-updates"
    method: "POST"
    auth:
      type: oauth2
      token_url: "https://auth.acme.com/token"
```

### Example 2: Kale Scheduler Gateway

```yaml
# Time-based signal generation
schedule:
  name: daily-reconciliation
  gateway: kale
  
  cron: "0 6 * * *"  # 6 AM daily
  
  generates:
    signal_type: "reconciliation.scheduled"
    payload:
      job_type: "daily"
```

---

## Implementation Notes

### For Developers

- Register Signal Providers with appropriate Gateway
- Include required headers (tenant, subscription)
- Use idempotency keys for reliability
- Handle async acknowledgments appropriately

### For Operators

- Monitor Gateway health and throughput
- Configure rate limiting per tenant
- Review authentication failures
- Manage certificate rotations

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Signal Exchange](./signal-exchange.md) | Gateways forward to SX |
| [Normalized Signal Format](./normalized-signal-format.md) | Output format of Gateways |
| [Subscription](./subscription.md) | Signals scoped to subscription |

---

## References

- [Signal Providers Subsystem](../04-subsystems/signal-providers/README.md)
- [Heracles Gateway](../04-subsystems/signal-providers/heracles-api-gateway.md)
- [Atropos Event Bus](../04-subsystems/signal-providers/atropos-event-bus.md)
- [ADR-0001: Signal Normalization](../decision-logs/0001-signal-normalization.md)

