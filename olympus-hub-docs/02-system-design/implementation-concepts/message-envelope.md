# Message Envelope

> **Category:** Signal Architecture

---

## Overview

The **Message Envelope** is the standard wrapper used for communication between Signal Exchange and Hub Applications. It provides consistent structure for request delivery, updates, reminders, and response handling. All messages flowing through Signal Exchange are wrapped in this envelope format.

---

## Ontology Context

### Relationship to Ontology

The ontology describes signals and operations but doesn't specify internal communication formats. Message Envelope is the implementation of the request-update communication protocol.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Operation updates | Message Envelope | Envelope wraps all operation messages |
| (not covered) | Message types | Different message types for different purposes |

### Gap This Fills

The ontology focuses on conceptual operations. Message Envelope specifies:
1. **Message structure**: How are messages formatted?
2. **Message types**: What kinds of messages exist?
3. **Delivery semantics**: How are messages handled?
4. **Update sequencing**: How are updates ordered?

---

## Definition

**Message Envelope** is a standard wrapper containing:
- **Update header**: Message type, sequence, timestamp
- **Request context**: Request ID, status, correlation
- **Payload**: Message-specific content
- **Delivery metadata**: Routing and handling information

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | All SX-to-Application and Application-to-SX communication |
| **Lifecycle** | Created for each message; immutable once sent |
| **Ownership** | Platform-defined format |
| **Multiplicity** | Many messages per Request |

---

## Rationale

### Why This Design?

Consistent envelope format enables:
1. **Uniform handling**: All messages processed similarly
2. **Sequence tracking**: Updates ordered correctly
3. **Type safety**: Message type determines payload schema
4. **Delivery flexibility**: Same format across delivery interfaces

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Per-message-type formats** | Inconsistent; harder to process |
| **Flat structure** | No clear separation of concerns |
| **No sequencing** | Out-of-order updates undetectable |

---

## Structure

### Envelope Schema

```json
{
  "envelope_id": "env-12345",
  "timestamp": "2026-01-06T10:00:00Z",
  
  "update": {
    "update_type": "REQUEST_CREATED",  // Message type
    "sequence": 1                       // Sequence within request
  },
  
  "request_context": {
    "request_id": "req-abc-123",
    "request_type": "standard-dispute",
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "workbench_id": "dispute-ops-prod",
    "scenario_id": "standard-dispute"
  },
  
  "payload": {
    "content_type": "application/json",
    "semantic_type": "com.hub.RequestCreated",
    "data": {
      // Message-type-specific content
    }
  },
  
  "delivery": {
    "interface": "http",           // http | atropos | oms
    "reply_to": "https://...",     // Where to send response
    "correlation_id": "corr-xyz"   // For response matching
  }
}
```

### Message Types

| Type | Direction | Purpose |
|------|-----------|---------|
| **REQUEST_CREATED** | SX → App | New request for application |
| **REQUEST_UPDATE** | SX → App | External update to request |
| **APPLICATION_UPDATE** | App → SX | Application's update to request |
| **TASK_UPDATE** | SX → App | Task status change |
| **REMIND** | App → SX | Schedule reminder |
| **CANCEL_REMINDER** | App → SX | Cancel scheduled reminder |
| **REMINDER_NOTIFICATION** | SX → App | Scheduled reminder triggered |
| **REMINDER_CANCELLED** | SX → App | Reminder was cancelled |
| **COMPLETE** | App → SX | Request completed |
| **CANCEL** | App → SX | Request cancelled |

---

## Behavior

### How It Works

**Request Delivery:**
```
1. Signal triggers new Request
2. SX creates Message Envelope:
   ├── update_type: REQUEST_CREATED
   ├── sequence: 1
   └── payload: initial signal data
3. SX delivers to Application via configured interface
4. Application acknowledges receipt
```

**Application Update:**
```
1. Application processes Request
2. Application creates Message Envelope:
   ├── update_type: APPLICATION_UPDATE
   ├── sequence: (next in sequence)
   └── payload: update data
3. Application sends to SX
4. SX appends to Request, notifies observers
```

**Reminder Flow:**
```
1. App sends REMIND envelope with schedule
2. SX stores reminder
3. At scheduled time, SX sends REMINDER_NOTIFICATION
4. App receives and acts on reminder
```

### Sequence Handling

```
Sequence rules:
├── Starts at 1 for each Request
├── Increments for each update
├── SX assigns sequence for incoming
├── Applications should include expected sequence
└── Out-of-order delivery possible; recipient reorders
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Signal Exchange | ↔ creates/receives | SX uses envelopes for all communication |
| Hub Application | ↔ receives/creates | Applications receive and send envelopes |
| Automation Runtime | → routes | Runtime routes envelopes to Application instances |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Unique envelope_id** | Each envelope has unique ID |
| **Sequential ordering** | Sequence numbers are monotonic per request |
| **Valid message type** | Must be known message type |
| **Request context** | All envelopes include request context |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Consistent format** | All messages structured identically |
| ✅ **Sequence tracking** | Order is explicit |
| ✅ **Type safety** | Payload schema by type |
| ✅ **Delivery agnostic** | Works across HTTP, event bus, OMS |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Envelope overhead** | Minimal; efficient serialization |
| ⚠️ **Schema versioning** | Backward compatible evolution |

---

## Examples

### Example 1: Request Created Envelope

```json
{
  "envelope_id": "env-001",
  "timestamp": "2026-01-06T10:00:00Z",
  "update": {
    "update_type": "REQUEST_CREATED",
    "sequence": 1
  },
  "request_context": {
    "request_id": "req-dispute-001",
    "request_type": "standard-dispute",
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "workbench_id": "dispute-ops-prod",
    "scenario_id": "standard-dispute"
  },
  "payload": {
    "content_type": "application/json",
    "data": {
      "customer_id": "CUST-001",
      "amount": 500.00,
      "reason": "unauthorized_charge"
    }
  }
}
```

### Example 2: Reminder Envelope

```json
{
  "envelope_id": "env-010",
  "timestamp": "2026-01-06T10:30:00Z",
  "update": {
    "update_type": "REMIND",
    "sequence": 10
  },
  "request_context": {
    "request_id": "req-dispute-001"
  },
  "payload": {
    "reminder": {
      "reminder_schedule_id": "rem-doc-48h",
      "kind": "document_upload_timeout",
      "schedule": {
        "type": "once",
        "when": "2026-01-08T10:30:00Z"
      },
      "reminder_payload": {
        "data": {
          "message": "Customer has not uploaded documents"
        }
      }
    }
  }
}
```

---

## Implementation Notes

### For Developers

- Always include request_context in outbound envelopes
- Track sequence numbers to detect gaps
- Use appropriate update_type for each message purpose
- Handle REMINDER_NOTIFICATION to continue paused workflows

### For Operators

- Monitor envelope delivery latency
- Check for sequence gaps indicating lost messages
- Review message type distribution for anomalies

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Normalized Signal Format](./normalized-signal-format.md) | Inbound signals normalized before envelope |
| [Signal Exchange](./signal-exchange.md) | Creates and routes envelopes |
| [Request Lifecycle](./request-lifecycle.md) | Envelopes drive Request state |
| [Reminder Capability](./reminder-capability.md) | REMIND/REMINDER_NOTIFICATION envelopes |

---

## References

- [Message Envelope Subsystem](../../04-subsystems/signal-exchange/message-envelope.md)
- [Application Router](../../04-subsystems/signal-exchange/application-router.md)

