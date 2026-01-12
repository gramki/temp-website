# Atropos Subscriber

> **Category:** Hub Native Utilities - Signal-Pulling Applications  
> **Status:** ✅ Complete

---

## Overview

**Atropos Subscriber** is a native Hub application that subscribes to Machine-provided Atropos (Event Bus) topics and queues messages to Hub-hosted topics for dispatch to Signal Exchange.

**Purpose:** Enable Machines to emit signals via Event Bus when Machines publish to their own Event Bus topics (Kafka, RabbitMQ, AWS EventBridge, etc.).

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOMAIN MACHINE                                │
│              (publishes events to Event Bus)                     │
│                                                                  │
│  Event Bus Topic: payment.events                                  │
│  Broker: kafka://external-payment.acme.com:9092                  │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Subscribe
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              ATROPOS SUBSCRIBER                                  │
│              (Signal-Pulling Application)                        │
│                                                                  │
│  1. Registers as subscriber with Atropos                         │
│  2. Atropos manages subscription aspects                        │
│  3. Subscriber acks processed messages                          │
│  4. Messages queued to Hub-hosted topic                         │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Queue to Hub-hosted topic
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              HUB-HOSTED TOPIC                                    │
│         (dedicated to machine instance)                          │
│                                                                  │
│  /hub/acme-bank/prod-subscription/payment-ops/                   │
│  atropos/external-payment-events                                │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Push semantics
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              ATROPOS (Signal Provider)                          │
│              (normalizes and forwards)                           │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
                   SIGNAL EXCHANGE
```

---

## Configuration

### Machine Instance Configuration

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

### Application Configuration

```yaml
atropos_subscriber:
  machine_instance_id: "external-payment-system"
  
  # Source: Machine-provided topic
  source:
    broker_endpoint: "kafka://external-payment.acme.com:9092"
    topic: "payment.events"
    auth:
      type: sasl_scram
      credentials_ref: "vault://secrets/external-payment/kafka-auth"
  
  # Target: Hub-hosted topic
  target:
    hub_topic: "/hub/acme-bank/prod-subscription/payment-ops/atropos/external-payment-events"
  
  # Subscription configuration
  subscription:
    consumer_group: "hub-external-payment-events"  # Managed by Atropos
    offset_strategy: "latest"  # latest | earliest | timestamp
    # Atropos manages all subscription aspects
```

---

## Behavior

### Subscription Management

**Key Points:**
- **Signal-pulling application registers as subscriber** with Atropos using configured credentials
- **Atropos manages all subscription aspects**:
  - Consumer group naming and management
  - Offset management (start from beginning, latest, or specific offset)
  - Reconnection and offset recovery
  - Error handling and retry logic
- **Subscriber only needs to acknowledge processed messages**
- Subscription lifecycle is tied to machine instance lifecycle

### Message Processing

1. **Subscribe**: Application registers as subscriber with Atropos
2. **Receive**: Atropos delivers messages from Machine topic
3. **Transform**: Application transforms messages to Signal Exchange format (if needed)
4. **Queue**: Application queues messages to Hub-hosted topic
5. **Acknowledge**: Application acknowledges processed messages to Atropos

### Hub-Hosted Topic

**Characteristics:**
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Dedicated**: Topic is dedicated to machine instance
- **Auto-Provisioned**: Topic is auto-provisioned with machine instance
- **Lifecycle Management**: Tenant admin manages topic lifecycle
- **Tied to Instance**: Topic lifecycle is tied to machine instance lifecycle

**Example:**
```
/hub/acme-bank/prod-subscription/payment-ops/atropos/external-payment-events
```

### Signal Format

Messages must be CloudEvents v1.0 compliant (same as Atropos Inbox push model):

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "source": "external-payment.acme.com",
  "specversion": "1.0",
  "type": "com.acme.payment.authorized",
  "datacontenttype": "application/json",
  "time": "2026-01-15T10:30:00Z",
  "data": {
    "payment_id": "pay_12345",
    "amount": 100.50,
    "customer_id": "cust_67890"
  }
}
```

---

## Error Handling

### Connection Failures

- **Automatic Retry**: Exponential backoff with configurable max retries
- **Reconnection**: Automatic reconnection with offset recovery
- **Alerting**: Automatic alerting for persistent failures

### Queue Failures

- **Dead-Letter Handling**: Messages that fail to queue are sent to dead-letter queue
- **Retry Logic**: Configurable retry for transient failures
- **Monitoring**: Metrics and logs for queue failures

### Offset Management

- **Managed by Atropos**: Atropos manages all offset aspects
- **Recovery**: Automatic offset recovery on reconnection
- **Manual Reset**: Tenant admin can reset offsets for reprocessing

---

## Observability

| Metric | Description |
|--------|-------------|
| `atropos_subscriber.messages.received` | Messages received from Machine topic |
| `atropos_subscriber.messages.queued` | Messages queued to Hub-hosted topic |
| `atropos_subscriber.messages.failed` | Messages that failed to queue |
| `atropos_subscriber.lag` | Consumer lag (delay in processing) |
| `atropos_subscriber.connection.status` | Connection status to Machine broker |

---

## Example Use Cases

1. **External Payment System**: Subscribe to external payment system's Kafka topic for payment events
2. **Legacy System Integration**: Subscribe to legacy system's event bus for state changes
3. **Partner Integration**: Subscribe to partner's event bus for business events

---

## Related Documentation

- [Signal-Pulling Applications](./signal-pulling-applications.md) - Overview
- [Atropos Event Bus](../signal-providers/atropos-event-bus.md) - Signal Provider documentation
- [Machine Registry](../registry-services/machine-registry.md) - Machine configuration
- [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md) - Complete guide

---

*Status: ✅ Complete*
