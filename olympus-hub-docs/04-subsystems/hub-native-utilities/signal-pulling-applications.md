# Signal-Pulling Applications

> **Category:** Hub Native Utilities  
> **Status:** ✅ Complete

---

## Overview

**Signal-pulling applications** are native Hub applications that retrieve signals from Machines when Machines don't support push or use a pull model. These applications act as **sensors** that sense Machine state/events and deliver pulled signals to Signal Providers (Hub ingress).

**Flow:**
```
Machine (provides endpoint/topic) → Signal-Pulling Application → Hub-Hosted Topic/Endpoint → Signal Provider → Signal Exchange
```

**Key Distinction:**
- **Signal-Pulling Applications**: Hub applications that *retrieve* signals from Machines (this document)
- **Sensory Tools**: Machine capabilities to *receive* signals (covered in Tools documentation)

---

## Architecture: Pull-to-Push Conversion

All signal-pulling applications follow a **pull-to-push conversion pattern**:

1. **Pull Phase**: Application retrieves signals from Machine-provided endpoints/topics
2. **Queue Phase**: Application queues pulled signals to Hub-hosted topics/endpoints
3. **Push Phase**: Hub-hosted resources dispatch to Signal Providers (push semantics)
4. **Normalization**: Signal Providers normalize and forward to Signal Exchange

**Flow Diagram:**
```
┌─────────────────────────────────────────────────────────────────┐
│                    DOMAIN MACHINE                                │
│              (provides endpoint/topic for querying)              │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Pull (poll/subscribe/query)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│           SIGNAL-PULLING APPLICATION                             │
│              (Native Hub Application)                            │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Pull        │  │ Transform   │  │ Queue to    │             │
│  │ from        │→ │ to Signal   │→ │ Hub-Hosted  │             │
│  │ Machine     │  │ Format      │  │ Topic       │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Queue to Hub-hosted resource
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              HUB-HOSTED TOPIC/ENDPOINT                           │
│         (dedicated to machine instance)                          │
│                                                                  │
│  Pattern: /hub/{tenant}/{subscription}/{workbench-id}/           │
│           {signal-provider}/{name-slug}                          │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Push semantics
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              SIGNAL PROVIDER (Hub Ingress)                       │
│              (normalizes and forwards)                           │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
                   SIGNAL EXCHANGE
```

---

## Essential Signal-Pulling Applications

| Application | Pull Mechanism | Use Case | Status |
|-------------|---------------|----------|--------|
| **Atropos Subscriber** | Event Bus Subscription | Machines on event buses (Kafka, RabbitMQ) | ✅ Documented |
| **Kafka Connect Puller** | Kafka Connect Protocol | Machines with Kafka endpoints | ✅ Documented |
| **SFTP Poller** | SFTP File Polling | Machines that upload via SFTP | ✅ Documented |
| **REST API Poller** | REST API Polling | Machines with REST endpoints | ⬜ To Document |
| **Database Poller** | Database Query Polling | Machines with database access | ⬜ To Document |
| **File Watcher** | File System Polling | Machines that write files | ⬜ To Document |
| **Message Queue Consumer** | Queue Consumption | Machines that publish to queues | ⬜ To Document |
| **Webhook Receiver** | Webhook Registration | Machines that support webhooks | ⬜ To Document |
| **GraphQL Query** | GraphQL Query Polling | Machines with GraphQL APIs | ⬜ To Document |
| **gRPC Client** | gRPC Service Calls | Machines with gRPC services | ⬜ To Document |
| **Change Data Capture (CDC)** | Database CDC | Real-time database change capture | ⬜ To Document |

---

## Common Characteristics

All signal-pulling applications share these characteristics:

### 1. Auto-Provisioning

- **Provisioned with Machine Instance**: Applications are automatically provisioned when a Machine Instance is configured with pull mechanisms
- **Lifecycle Tied to Instance**: Application lifecycle is tied to Machine Instance lifecycle
- **Managed by Tenant Admin**: Tenant admin manages application lifecycle

### 2. Automatic Pull-to-Push Conversion

- **Automatic Conversion**: Pull-to-push conversion is automatic when endpoints are appropriately provisioned and specified
- **Hub-Hosted Resources**: All pulled signals are queued to Hub-hosted topics/endpoints
- **Consistent Processing**: Signals are processed with push semantics regardless of original delivery method

### 3. Configurable Polling/Filtering

- **Polling Schedules**: Configurable polling intervals (cron expressions, intervals)
- **Filtering**: Apply filters during pull (pattern matching, time-based, size-based)
- **Rate Limiting**: Configurable rate limits to avoid overwhelming source Machines

### 4. Error Handling with Sound Defaults

- **Connection Failures**: Automatic retry with exponential backoff
- **Queue Failures**: Dead-letter handling for messages that fail to queue
- **Alerting**: Automatic alerting for persistent failures
- **Recovery**: Automatic recovery and offset management

### 5. Observability

- **Metrics**: Pull rate, queue depth, error rates
- **Logs**: Detailed logs for troubleshooting
- **Traces**: Distributed tracing for end-to-end visibility

---

## Configuration Schema

### Common Configuration Structure

```yaml
signal_pulling_application:
  # Application type
  type: enum  # atropos_subscriber | kafka_connect | sftp_poller | rest_api_poller | ...
  
  # Machine reference
  machine_id: string
  machine_instance_id: string
  
  # Source: Machine-provided endpoint/topic
  source:
    endpoint: string  # Machine endpoint/topic
    auth:
      type: enum
      credentials_ref: string
  
  # Polling/Subscription configuration
  polling:
    schedule: string  # Cron expression or interval
    filters: array     # Filter criteria
  
  # Target: Hub-hosted topic/endpoint
  target:
    hub_topic: string  # Hub-hosted topic (auto-provisioned)
    # OR
    hub_endpoint: string  # Hub-hosted endpoint
  
  # Transformation
  transformation:
    mapping: object  # Machine format → Signal Exchange format
  
  # Error handling
  error_handling:
    retry_policy: object
    dead_letter: object
```

---

## Hub-Hosted Resources

### Topic Naming Pattern

Hub-hosted topics follow this pattern:
```
/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}
```

**Example:**
```
/hub/acme-bank/prod-subscription/payment-ops/atropos/external-payment-events
```

### Endpoint Characteristics

- **Dedicated**: Each topic/endpoint is dedicated to a machine instance
- **Auto-Provisioned**: Topics/endpoints are auto-provisioned with machine instance
- **Lifecycle Management**: Tenant admin manages lifecycle (creation, deletion, cleanup)
- **Tied to Instance**: Lifecycle is tied to machine instance lifecycle

---

## Application-Specific Documentation

For detailed documentation on each application:

- [Atropos Subscriber](./atropos-subscriber.md) - Subscribe to Machine-provided Atropos topics
- [Kafka Connect Puller](./kafka-connect-puller.md) - Connect to Machine-provided Kafka via Kafka Connect
- [SFTP Poller](./sftp-poller.md) - Poll Machine SFTP for files

---

## Related Documentation

- [Machine Registry](../registry-services/machine-registry.md) - Machine signal emission configuration
- [Signal Providers](../signal-providers/README.md) - Hub ingress endpoints
- [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md) - Complete configuration guide

---

*Status: ✅ Complete*
