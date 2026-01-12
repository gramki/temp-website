# Atropos - Event Bus Gateway

Atropos is the I/O Gateway for **Event signals**—state changes published by Machines in the Domain. As Olympus's Event Bus as a Service, Atropos powers event-driven workflows by enabling real-time, scalable, and fault-tolerant communication between services.

> **Olympus Academy:** [Atropos Documentation](https://atropos.olympus.tech/)

## Overview

| Attribute | Value |
|-----------|-------|
| **Signal Type** | Events |
| **Protocol** | Pub-Sub Event Bus |
| **Direction** | Inbound (events) and Outbound (event publishing) |
| **Role** | Senses domain events, executes Triggers, creates Requests |

## Key Concepts (from Olympus Academy)

| Concept | Description |
|---------|-------------|
| **Event** | A data point or state change shared between services—user actions, system notifications, or status updates |
| **Topic** | Logical grouping of events that categorizes them; channels for delivering information to subscribers |
| **Subscription** | Defines how a service consumes events from a Topic; includes filters and transformers |
| **Partition** | Divides events within a Topic for scalability and parallel processing |
| **Broker** | Routes events between producers and consumers; ensures reliable delivery and load balancing |
| **Consumer** | Service that subscribes to a Topic to receive and process events |
| **Producer** | Service or application that publishes events to a Topic |
| **Offset** | Position of a consumer within a Topic's event log; enables replay and recovery |

## Event Signal Characteristics

Events represent **state changes** in Business Entities managed by Machines:

| Characteristic | Description |
|----------------|-------------|
| **Immutable** | Events are facts that happened; cannot be changed |
| **Ordered** | Events from same source maintain ordering via partitions |
| **Timestamped** | Precise occurrence time |
| **Typed** | Schema-defined event types per Topic |
| **7-day Retention** | Events are stored for seven days (configurable) |

**Examples:**
- `OrderPlaced` - Customer placed an order
- `PaymentCompleted` - Payment transaction succeeded
- `EmployeeOnboarded` - New employee record created
- `InventoryLow` - Stock below threshold

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    DOMAIN MACHINES                       │
│   (ERP, CRM, Payment Systems, Custom Applications)      │
└────────────────────────┬────────────────────────────────┘
                         │ Events
                         ▼
┌─────────────────────────────────────────────────────────┐
│                    EVENT BUS                             │
│           (Kafka, RabbitMQ, AWS EventBridge)            │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                      ATROPOS                             │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ Event       │  │ Trigger     │  │ Request     │      │
│  │ Consumer    │→ │ Executor    │→ │ Publisher   │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                          │
└────────────────────────┬────────────────────────────────┘
                         │ Request
                         ▼
                   OPERATIONS CENTER
```

## Trigger Configuration

Atropos executes Triggers defined in Workbench configurations:

```yaml
# Example: Workbench Trigger for Atropos
trigger:
  name: "fraud-detection-trigger"
  gateway: atropos
  
  # Signal matching
  filter:
    event_type: "PaymentCompleted"
    conditions:
      - field: "amount"
        operator: ">"
        value: 10000
  
  # Transformation
  transform:
    request_type: "HighValuePaymentReview"
    mapping:
      payment_id: "$.event.payment_id"
      amount: "$.event.amount"
      customer_id: "$.event.customer_id"
  
  # Access control
  access:
    require_auth: false  # Events are system-internal
  
  # Target
  target:
    workbench: "fraud-operations"
    scenario: "high-value-payment-review"
```

## Capabilities

### For Publishers (Producers)
- **Self-Service Topic Creation**: Define and manage event Topics for your services
- **Scheduled Event Publishing**: Trigger time-based events using built-in scheduling workflows
- **End-to-End Visibility**: Validate publishing outcomes, view delivery stats, and simulate events

### For Consumers
- **Subscription with Filters**: Fine-grained control over which events are received
- **Transformers**: Modify or enrich events before delivery to consumer
- **Webhook Delivery**: Send events to non-OMS applications via HTTP with HMAC validation
- **Idempotent Processing**: Consumer applications must be idempotent (at-least-once delivery)

### For SREs
- **Real-Time Monitoring**: Track consumer lag, event flow, and delivery health
- **Failure Handling**: Configure circuit breakers, alerts, and DLQ routing
- **Incident Diagnosis**: Use traces and simulations to debug production issues
- **Offset Management**: Reset offsets for reprocessing or recovery

### Event Reprocessing
- Replay past events by resetting consumer offsets to a specific timestamp
- Useful for error recovery, debugging, or reprocessing missed events

## Integration with Kubernetes

Atropos uses Kubernetes Custom Resources (CRs) for declarative management:

| Resource | Purpose |
|----------|---------|
| **Topic CR** | Define and manage event Topics |
| **Subscription CR** | Configure event consumption with filters and transformers |

## Configuration

### Workbench-level Configuration
- Event subscriptions per Workbench
- Trigger definitions
- Request mappings

### System-level Configuration
- Event bus connection settings
- Consumer group settings
- Retry and dead-letter policies

## Observability

| Metric | Description |
|--------|-------------|
| **Lag** | Delay/backlog of unprocessed events by a consumer in a partition |
| **Flow Control** | Rate regulation to prevent consumer overload |
| `atropos.events.received` | Total events received |
| `atropos.events.filtered` | Events filtered out by Triggers |
| `atropos.requests.created` | Requests created from events |
| `atropos.processing.latency` | Event-to-Request latency |

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Event-Driven Service Communication** | Loosely coupled services via structured events |
| **Scheduled Events & Cron Workflows** | Trigger downstream actions at defined times |
| **Graceful Failure Handling** | DLQs, circuit breakers, replay mechanisms |
| **Event Flow Observability** | Logs, traces, and alerts for event workflows |

## Machine Signal Emission

Machines can emit signals through Atropos using two models: **push** (Atropos Inbox) and **pull** (Atropos Subscription).

### Push Model: Atropos Inbox

**Flow:** Machine publishes events to Atropos topic → Atropos normalizes and forwards to Signal Exchange

**Configuration:**
- Machine publishes events to Event Bus topic (Kafka, RabbitMQ, AWS EventBridge)
- Events must be CloudEvents v1.0 compliant
- Atropos consumes from the topic and normalizes to Signal Exchange format

**Example Machine Configuration:**
```yaml
machine:
  id: "payment-switch"
  signal_emission:
    push:
      atropos_inbox:
        broker_endpoint: "kafka://kafka.olympus.tech:9092"
        topic: "payment.events"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/payment-switch/kafka-auth"
```

**Event Format (CloudEvents v1.0):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "source": "payment-switch.acme.com",
  "specversion": "1.0",
  "type": "com.acme.payment.authorized",
  "datacontenttype": "application/json",
  "time": "2026-01-15T10:30:00Z",
  "data": {
    "payment_id": "pay_12345",
    "amount": 100.50,
    "customer_id": "cust_67890",
    "currency": "USD"
  }
}
```

### Pull Model: Atropos Subscription

**Flow:** Hub subscribes to Machine-provided topic → Messages queued to Hub-hosted topic → Signal Provider → Signal Exchange

**Configuration:**
- Machine provides broker endpoint and topic name
- Hub uses signal-pulling application (Atropos Subscriber) to subscribe
- Messages are queued to Hub-hosted topic for dispatch
- Hub-hosted topic follows naming pattern: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`

**Example Machine Configuration:**
```yaml
machine:
  id: "external-payment-system"
  signal_emission:
    pull:
      atropos_subscription:
        # Machine-provided endpoint and topic
        machine_broker: "kafka://external-payment.acme.com:9092"
        machine_topic: "payment.events"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/external-payment/kafka-auth"
        
        # Hub-hosted topic (auto-provisioned, dedicated to machine instance)
        hub_topic: "/hub/acme-bank/prod-subscription/payment-ops/atropos/external-payment-events"
```

**Flow:**
1. Signal-pulling application (Atropos Subscriber) registers as subscriber with Atropos
2. Atropos manages subscription aspects (consumer groups, offsets, etc.)
3. Subscriber reads messages from Machine topic
4. Subscriber queues messages to Hub-hosted topic
5. Hub-hosted topic dispatches to Signal Exchange (push semantics)
6. Signal Exchange processes as normal push signals

### Subscription Management

**Key Points:**
- Signal-pulling application registers as subscriber with configured credentials
- **Atropos manages all subscription aspects** (consumer groups, offsets, reconnection, etc.)
- Subscriber only needs to acknowledge processed messages
- Subscription lifecycle is tied to machine instance lifecycle

**Subscription Characteristics:**
- Consumer group naming: Managed by Atropos
- Offset management: Managed by Atropos (start from beginning, latest, or specific offset)
- Reconnection: Automatic with offset recovery
- Error handling: Sound defaults with retry and dead-letter handling

### Hub-Hosted Topics

**Characteristics:**
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Dedicated**: Each topic is dedicated to a machine instance
- **Auto-Provisioning**: Topics are auto-provisioned with machine instance
- **Lifecycle Management**: Tenant admin manages topic lifecycle (creation, deletion, cleanup)
- **Tied to Instance**: Topic lifecycle is tied to machine instance lifecycle

**Example Hub-Hosted Topic:**
```
/hub/acme-bank/prod-subscription/payment-ops/atropos/external-payment-events
```

This topic is:
- Subscription-scoped: `prod-subscription`
- Workbench-scoped: `payment-ops`
- Signal Provider: `atropos`
- Machine-specific: `external-payment-events`

For detailed configuration, see [Machine Registry](../registry-services/machine-registry.md) and [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md).

## Related Documentation

- [Olympus Academy - Atropos](https://atropos.olympus.tech/)
- [Hub Architecture - Signals](../../02-system-design/hub-architecture.md#13-signals)
- [Hub Architecture - Triggers](../../02-system-design/hub-architecture.md#14-triggers)
- [Ontology - Signal](../../01-concepts/ontology-reference.md#signal)
- [Ontology - Trigger](../../01-concepts/ontology-reference.md#trigger)
- [Machine Registry](../registry-services/machine-registry.md)
- [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md)
- [Machine Signal Emission Concept](../../02-system-design/implementation-concepts/machine-signal-emission.md) - Implementation concept

---

*Status: 🟡 WIP - Definition phase*

