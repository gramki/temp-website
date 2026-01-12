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
- Serves as **Hub ingress endpoints** where Machines send signals
- Accepts signals in protocol-native format (push model) or processes signals from Hub-hosted topics (pull model)
- Validates signal schemas according to protocol requirements during normalization
- Normalizes signals to standard DTO
- Forwards normalized signals to Signal Exchange
- Receives updates from Signal Exchange
- Delivers updates in protocol-native format

### Machine Signal Emission

**I/O Gateways serve as Hub ingress endpoints for Machine signals.** Machines emit signals through Signal Providers using two models:

**Push Model:** Machines actively send signals to Gateway endpoints
- **Webhook**: Machine sends HTTP POST to Heracles gateway endpoint
- **Atropos Inbox**: Machine publishes events to Event Bus topic
- **SFTP**: Machine uploads files to Dia SFTP endpoint

**Pull Model:** Signal-pulling applications retrieve signals from Machines, queue to Hub-hosted topics, then Gateway processes from Hub-hosted resources
- **Atropos Subscription**: Signal-pulling app subscribes to Machine topic, queues to Hub-hosted topic
- **Kafka Connect**: Signal-pulling app connects to Machine Kafka, queues to Hub-hosted topic
- **SFTP**: Signal-pulling app polls Machine SFTP, uploads to Hub Dia SFTP

**Hub Ingress Endpoints:**
- **Scoped**: Subscription-scoped and per-workbench
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Provisioning**: Provisioned by tenant admin or authorized developers as resources

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
| [ADR-0001](../../decision-logs/0001-signal-normalization.md) | Normalize signal format between SPs and SX |
| [ADR-0103](../../decision-logs/0103-machine-signal-emission.md) | Machine Signal Emission Through Signal Providers |

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

**Push Model:**
```
1. Machine sends signal to Hub ingress endpoint
   └── HTTP POST (Heracles), Event Bus publish (Atropos), SFTP upload (Dia)

2. Gateway receives at Hub ingress endpoint:
   ├── Transport-level authentication (per-provider mechanisms)
   ├── Access control (tenant, subscription, workbench)
   └── Schema validation (OpenAPI, CloudEvents, File Format Spec)

3. Gateway normalizes to DTO:
   ├── Extract tenant/subscription/workbench context
   ├── Map protocol fields to standard structure
   └── Generate signal_id, timestamp

4. Gateway forwards to Signal Exchange:
   └── Normalized DTO via internal protocol

5. Gateway returns acknowledgment:
   └── Sync: wait for SX response
   └── Async: immediate ACK, SX processes later
```

**Pull Model:**
```
1. Signal-pulling application retrieves signal from Machine
   └── Subscribe to topic, poll SFTP, connect via Kafka Connect

2. Signal-pulling application queues to Hub-hosted topic/endpoint
   └── Pattern: /hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}

3. Gateway processes from Hub-hosted resource (push semantics):
   ├── Receive from Hub-hosted topic/endpoint
   ├── Schema validation (same as push model)
   └── Normalize to DTO

4. Gateway forwards to Signal Exchange:
   └── Normalized DTO via internal protocol
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

## Hub Ingress Endpoint Configuration

**Hub ingress endpoints** are the entry points into the Hub platform where Machines send signals. These endpoints are exposed by I/O Gateways and serve as the Hub's boundary for signal reception.

### Endpoint Characteristics

| Characteristic | Description |
|---------------|-------------|
| **Scoping** | Subscription-scoped and per-workbench |
| **Naming Pattern** | `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}` |
| **Provisioning** | Provisioned by tenant admin or authorized developers as resources when required |
| **Authentication** | Per-provider authentication mechanisms |

### Endpoint Provisioning

Hub ingress endpoints are provisioned as resources within a subscription and workbench context:

1. **Tenant Admin** can provision endpoints for any workbench in their tenant
2. **Authorized Developers** can provision endpoints for workbenches they have access to
3. Endpoints are tied to the workbench lifecycle
4. Endpoint configuration includes authentication credentials and access policies

### Example Endpoint Patterns

- **Heracles Webhook**: `https://heracles.olympus.tech/api/workbenches/{workbench-id}/signals`
- **Atropos Topic**: `/hub/{tenant}/{subscription}/{workbench-id}/atropos/{topic-name}`
- **Dia SFTP**: `sftp://dia.olympus.tech:22/inbound/{workbench-id}/{folder-path}`

## Signal Schema Validation

**Signal schema validation occurs at the I/O Gateway during normalization.** Each Gateway validates according to its protocol requirements:

| Gateway | Validation Method |
|---------|-------------------|
| **Heracles (Webhook)** | Validates against OpenAPI specification for POST request body |
| **Atropos Inbox** | Validates CloudEvents v1.0 compliance |
| **Dia (SFTP)** | Validates file format specification (CSV/TSV/Fixed-Width) |

Validation failures are handled according to provider-specific error handling policies.

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Tenant scoping** | All signals must include tenant context |
| **Subscription scoping** | All signals must include subscription context |
| **Workbench scoping** | Hub ingress endpoints are per-workbench |
| **Normalization** | All signals must be normalized before SX |
| **Schema validation** | All signals must be validated at Gateway during normalization |
| **Authentication** | All requests must be authenticated (per-provider mechanisms) |
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

- [Signal Providers Subsystem](../../04-subsystems/signal-providers/README.md)
- [Heracles Gateway](../../04-subsystems/signal-providers/heracles-api-gateway.md)
- [Atropos Event Bus](../../04-subsystems/signal-providers/atropos-event-bus.md)
- [ADR-0001: Signal Normalization](../../decision-logs/0001-signal-normalization.md)

