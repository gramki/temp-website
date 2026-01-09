# Flow Controller

> **Status:** 🔴 Stub — Placeholder for expansion

The Flow Controller manages signal throughput, back-pressure, and store-and-forward capabilities within the Signal Exchange.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Control signal flow, ensure reliable delivery |
| **Modes** | Direct (pass-through) or Store-and-Forward (buffered) |
| **Scope** | Configured per Scenario in Workbench Management |

---

## Operating Modes

### Direct Mode (Default)

In direct mode, signals flow through the Signal Exchange without buffering:

```
Signal Provider → Signal Exchange → Hub Application
                     (pass-through)
```

| Characteristic | Description |
|----------------|-------------|
| **Latency** | Minimal — no buffering delay |
| **Durability** | None — signal loss possible on failure |
| **Ordering** | Best-effort |
| **Use Case** | Low-latency, tolerant of occasional signal loss |

### Store-and-Forward Mode

In store-and-forward mode, signals are durably buffered before delivery:

```
Signal Provider → Signal Exchange → [Durable Buffer] → Hub Application
                     (store)           (forward)
```

| Characteristic | Description |
|----------------|-------------|
| **Latency** | Higher — buffering adds delay |
| **Durability** | Guaranteed — signals persisted before ack |
| **Ordering** | Configurable (FIFO, priority) |
| **Use Case** | Critical signals, high-volume bursts, unreliable downstream |

---

## Flow Control Capabilities

### Rate Limiting

Protect downstream Applications from signal overload:

| Parameter | Description |
|-----------|-------------|
| `rate_limit` | Maximum signals per unit time (e.g., `1000/s`, `60000/m`) |
| `burst_limit` | Allowed burst above rate limit |
| `rejection_action` | `reject`, `queue`, `throttle` |

### Back-Pressure

Propagate Application capacity signals upstream:

| Mechanism | Description |
|-----------|-------------|
| **Slow-down** | Signal Providers reduce emission rate |
| **Pause** | Signal Providers pause until capacity available |
| **Reject** | Signal Providers receive rejection (429) |

### Priority Queuing

When using store-and-forward mode:

| Priority | Description |
|----------|-------------|
| `critical` | Processed first, never dropped |
| `high` | Processed before normal |
| `normal` | Default priority |
| `low` | Processed when capacity available |

---

## Store-and-Forward Configuration

Configured in Scenario definition:

```yaml
scenario:
  id: "payment-processing"
  
  flow_control:
    mode: store_and_forward      # direct | store_and_forward
    
    # Rate limiting
    rate_limit: 1000/s
    burst_limit: 1500
    
    # Priority
    priority: high               # critical | high | normal | low
    
    # Ordering
    ordering: fifo               # fifo | priority | none
    partition_key: "customer_id" # For ordered delivery per key
    
    # Batching
    batching:
      enabled: true
      max_size: 100              # Max signals per batch
      max_wait: 500ms            # Max time to wait for batch
    
    # Retry policy
    retry_policy:
      max_attempts: 5
      initial_delay: 100ms
      backoff: exponential       # exponential | linear | fixed
      max_delay: 30s
    
    # Dead letter
    dead_letter:
      enabled: true
      queue: "payments-dlq"
      retention: 7d
```

---

## Buffer Storage

In store-and-forward mode, signals are stored in a durable buffer:

| Option | Description |
|--------|-------------|
| **Kafka** | High-throughput, ordered, partitioned |
| **Redis Streams** | Lower latency, moderate throughput |
| **PostgreSQL** | Transactional, lower throughput |

Buffer selection is based on Scenario requirements and tenant configuration.

---

## Observability

| Metric | Description |
|--------|-------------|
| `signal_relay.flow.rate` | Current signal rate per Scenario |
| `signal_relay.flow.backlog` | Buffered signals awaiting delivery |
| `signal_relay.flow.latency` | Time from intake to delivery |
| `signal_relay.flow.rejections` | Signals rejected due to rate limiting |
| `signal_relay.flow.retries` | Retry attempts |
| `signal_relay.flow.dlq_count` | Signals in dead-letter queue |

---

## Use Cases

| Scenario | Mode | Configuration |
|----------|------|---------------|
| **Real-time fraud detection** | Direct | Low latency, tolerant of loss |
| **Payment processing** | Store-and-Forward | Guaranteed delivery, FIFO |
| **Batch file processing** | Store-and-Forward | Batching enabled, priority ordering |
| **Event notifications** | Direct | Best-effort, high throughput |
| **Regulatory reporting** | Store-and-Forward | Guaranteed, audit trail required |

---

## Integration Points

| Component | Integration |
|-----------|-------------|
| **Workbench Management** | Flow control configuration per Scenario |
| **Signal Providers** | Back-pressure signaling |
| **Application Router** | Delivery to Hub Applications |
| **CAF** | Audit trail for store-and-forward operations |
| **Observability** | Metrics, traces, alerts |

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Application Router](./application-router.md)
- [Workbench Management](../workbench-management/README.md)

---

*TODO: Detailed design — buffer implementation, partitioning strategy, exactly-once semantics*

