# Kafka Connect Puller

> **Category:** Hub Native Utilities - Signal-Pulling Applications  
> **Status:** ✅ Complete

---

## Overview

**Kafka Connect Puller** is a native Hub application that connects to Machine-provided Kafka brokers via Kafka Connect protocol and queues messages to Hub-hosted topics for dispatch to Signal Exchange.

**Purpose:** Enable Machines to emit signals via Kafka when Machines publish to their own Kafka topics.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOMAIN MACHINE                                │
│              (publishes events to Kafka)                         │
│                                                                  │
│  Kafka Topic: transactions                                       │
│  Broker: kafka://legacy-system.acme.com:9092                     │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Kafka Connect
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              KAFKA CONNECT PULLER                                │
│              (Signal-Pulling Application)                        │
│                                                                  │
│  1. Internal Kafka Connect connector                             │
│  2. Provisioned with machine instance                            │
│  3. Tied to machine instance lifecycle                          │
│  4. Messages queued to Hub-hosted topic                         │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Queue to Hub-hosted topic
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              HUB-HOSTED TOPIC                                     │
│         (dedicated to machine instance)                          │
│                                                                  │
│  /hub/acme-bank/prod-subscription/transaction-ops/               │
│  atropos/legacy-kafka-transactions                               │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Push semantics
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              ATROPOS (Signal Provider)                          │
│              (normalizes and forwards)                          │
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
  id: "legacy-kafka-system"
  signal_emission:
    pull:
      kafka_connect:
        # Machine-provided Kafka endpoint and topic
        machine_broker: "kafka://legacy-system.acme.com:9092"
        machine_topic: "transactions"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/legacy-kafka/auth"
        
        # Kafka Connect specific configuration
        connect_config:
          connector_class: "io.confluent.connect.kafka.KafkaSourceConnector"
          # Additional Kafka Connect properties
        
        # Hub-hosted topic (auto-provisioned, dedicated to machine instance)
        hub_topic: "/hub/acme-bank/prod-subscription/transaction-ops/atropos/legacy-kafka-transactions"
```

### Application Configuration

```yaml
kafka_connect_puller:
  machine_instance_id: "legacy-kafka-system"
  
  # Source: Machine-provided Kafka
  source:
    broker_endpoint: "kafka://legacy-system.acme.com:9092"
    topic: "transactions"
    auth:
      type: sasl_scram
      credentials_ref: "vault://secrets/legacy-kafka/auth"
  
  # Kafka Connect configuration
  connect_config:
    connector_class: "io.confluent.connect.kafka.KafkaSourceConnector"
    tasks_max: 1
    # Additional Kafka Connect properties
  
  # Target: Hub-hosted topic
  target:
    hub_topic: "/hub/acme-bank/prod-subscription/transaction-ops/atropos/legacy-kafka-transactions"
```

---

## Behavior

### Kafka Connect Integration

**Key Points:**
- **Hub runs Kafka Connect connectors internally**
- **Connectors are provisioned with machine instance**
- **Connector lifecycle is tied to machine instance lifecycle**
- **Schema transformation**: TBD (transformation should be possible but not specified at this stage)

### Message Processing

1. **Connect**: Application uses Kafka Connect to connect to Machine-provided Kafka
2. **Read**: Application reads messages from Machine topic
3. **Transform**: Application transforms messages (if schema transformation configured)
4. **Queue**: Application queues messages to Hub-hosted topic
5. **Commit**: Application commits offsets to Kafka

### Hub-Hosted Topic

**Characteristics:**
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Dedicated**: Topic is dedicated to machine instance
- **Auto-Provisioned**: Topic is auto-provisioned with machine instance
- **Lifecycle Management**: Tenant admin manages topic lifecycle
- **Tied to Instance**: Topic lifecycle is tied to machine instance lifecycle

**Example:**
```
/hub/acme-bank/prod-subscription/transaction-ops/atropos/legacy-kafka-transactions
```

### Signal Format

Messages should be CloudEvents v1.0 compliant (same as Atropos Inbox push model):

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "source": "legacy-system.acme.com",
  "specversion": "1.0",
  "type": "com.acme.transaction.completed",
  "datacontenttype": "application/json",
  "time": "2026-01-15T10:30:00Z",
  "data": {
    "transaction_id": "txn_12345",
    "amount": 100.50,
    "status": "completed"
  }
}
```

**Note:** Schema transformation between Machine topic and Hub topic is TBD. Transformation should be possible but not specified at this stage.

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

- **Kafka Connect Managed**: Kafka Connect manages offsets
- **Recovery**: Automatic offset recovery on reconnection
- **Manual Reset**: Tenant admin can reset offsets for reprocessing

---

## Observability

| Metric | Description |
|--------|-------------|
| `kafka_connect_puller.messages.received` | Messages received from Machine topic |
| `kafka_connect_puller.messages.queued` | Messages queued to Hub-hosted topic |
| `kafka_connect_puller.messages.failed` | Messages that failed to queue |
| `kafka_connect_puller.connector.status` | Kafka Connect connector status |
| `kafka_connect_puller.lag` | Consumer lag (delay in processing) |

---

## Example Use Cases

1. **Legacy System Integration**: Connect to legacy system's Kafka for transaction events
2. **Partner Integration**: Connect to partner's Kafka for business events
3. **Multi-Region Integration**: Connect to Kafka in different regions

---

## Related Documentation

- [Signal-Pulling Applications](./signal-pulling-applications.md) - Overview
- [Atropos Event Bus](../signal-providers/atropos-event-bus.md) - Signal Provider documentation
- [Machine Registry](../registry-services/machine-registry.md) - Machine configuration
- [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md) - Complete guide

---

*Status: ✅ Complete*
