# Apache Kafka — Event Bus

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Apache Kafka** provides the distributed event streaming platform for Olympus Hub, enabling asynchronous communication, event sourcing, and reliable message delivery between services.

---

## Purpose in Olympus Hub

Kafka provides:

- **Event Streaming** — Asynchronous event delivery between services
- **Signal Transport** — Event-based signals from Atropos gateway
- **Async Updates** — Request update message delivery
- **Observer Notifications** — Fan-out to registered observers
- **Audit Events** — Reliable audit event delivery

---

## Topic Architecture

### Core Topics

| Topic Pattern | Purpose | Retention |
|---------------|---------|-----------|
| `hub.signals.<gateway>` | Inbound signals from I/O gateways | 7 days |
| `hub.requests.<workbench>` | Request lifecycle events | 30 days |
| `hub.updates.<workbench>` | Async update messages | 14 days |
| `hub.notifications` | Observer notification dispatch | 3 days |
| `hub.audit` | Audit events to Cipher | 90 days |

### Tenant-Scoped Topics

```
hub.tenant.<tenant-id>.signals
hub.tenant.<tenant-id>.requests.<workbench-id>
hub.tenant.<tenant-id>.updates.<workbench-id>
```

---

## Integration with Hub Subsystems

### Atropos — Event Bus Gateway

```
┌──────────────────┐     ┌──────────────────┐
│  External Event  │────►│     Atropos      │
│    Sources       │     │  (I/O Gateway)   │
└──────────────────┘     └────────┬─────────┘
                                  │
                                  ▼
                         hub.signals.atropos
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Signal Exchange  │
                         └──────────────────┘
```

### Signal Exchange — Async Updates

```
┌──────────────────┐     ┌──────────────────┐
│  Hub Application │────►│ Signal Exchange  │
│  (Async Update)  │     │                  │
└──────────────────┘     └────────┬─────────┘
                                  │
                                  ▼
                         hub.updates.<workbench>
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              Operations    Memory Store   Notifications
                 Data         Update        Dispatch
```

---

## Message Schema

### Signal Message

```json
{
  "header": {
    "message_id": "msg-123",
    "correlation_id": "corr-456",
    "timestamp": "2026-01-04T12:00:00Z",
    "source": "atropos",
    "tenant_id": "tenant-001",
    "trace_id": "trace-789"
  },
  "signal": {
    "type": "event",
    "name": "payment.completed",
    "payload": { ... }
  }
}
```

### Update Message

```json
{
  "header": {
    "message_id": "msg-789",
    "request_id": "req-123",
    "timestamp": "2026-01-04T12:05:00Z"
  },
  "update": {
    "type": "ASYNC_UPDATE",
    "sub_type": "DECISION",
    "payload": { ... }
  }
}
```

---

## Consumer Groups

| Consumer Group | Topics | Purpose |
|----------------|--------|---------|
| `signal-exchange` | `hub.signals.*` | Signal processing |
| `request-factory` | `hub.signals.*` | Request creation |
| `update-processor` | `hub.updates.*` | Update application |
| `notification-dispatcher` | `hub.notifications` | Observer notifications |
| `audit-writer` | `hub.audit` | Audit persistence |

---

## Partitioning Strategy

| Topic Type | Partition Key | Rationale |
|------------|---------------|-----------|
| Signals | `tenant_id` | Tenant isolation |
| Requests | `request_id` | Ordering per request |
| Updates | `request_id` | Ordering per request |
| Notifications | `observer_id` | Observer parallelism |

---

## Reliability Guarantees

- **At-least-once delivery** — Consumer acknowledgment required
- **Ordering** — Per-partition ordering guaranteed
- **Durability** — Replication factor of 3
- **Retention** — Configurable per topic

---

## Cluster Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Kafka Cluster                      │
│                                                      │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │ Broker 1 │   │ Broker 2 │   │ Broker 3 │        │
│  └──────────┘   └──────────┘   └──────────┘        │
│                                                      │
│  ┌──────────────────────────────────────────┐      │
│  │              ZooKeeper Ensemble           │      │
│  └──────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────┘
```

---

## Schema Registry

- **Confluent Schema Registry** — Avro/JSON schema management
- **Schema Evolution** — Backward/forward compatibility
- **Validation** — Producer-side schema validation

---

## Monitoring

Kafka metrics exported to Olympus Watch:

- `kafka_consumer_lag` — Consumer lag per partition
- `kafka_messages_in_per_sec` — Message throughput
- `kafka_bytes_in_per_sec` — Byte throughput
- `kafka_under_replicated_partitions` — Replication health

---

## Security

- **SASL/SCRAM** — Authentication
- **ACLs** — Topic-level authorization
- **TLS** — In-transit encryption
- **Encryption at Rest** — Disk-level encryption

---

## Related Documentation

- [Atropos Event Bus](../04-subsystems/signal-providers/atropos-event-bus.md) — Event gateway
- [Signal Exchange](../04-subsystems/signal-exchange/README.md) — Signal processing
- [Observer Notifications](../04-subsystems/signal-exchange/observer-notifications.md) — Notification dispatch

---

*Expand this document with topic naming conventions, consumer configuration, and operational procedures.*

