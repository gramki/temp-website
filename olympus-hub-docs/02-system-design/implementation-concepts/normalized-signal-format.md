# Normalized Signal Format

> **Category:** Signal Architecture

---

## Overview

The **Normalized Signal Format** is the standard DTO (Data Transfer Object) structure that all signals must conform to when delivered to Signal Exchange. I/O Gateways transform protocol-specific signals into this normalized format, enabling Signal Exchange to process signals uniformly regardless of their source.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Signal** as "a message conveying information about an event or request." The Normalized Signal Format is the implementation of this concept as a concrete data structure.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Signal | Normalized Signal DTO | Concrete representation of signal |
| (not covered) | Normalization | Translation from protocol-specific to standard |

### Gap This Fills

The ontology describes signals conceptually. Normalized Signal Format specifies:
1. **Structure**: What fields must every signal have?
2. **Semantics**: What does each field mean?
3. **Extensibility**: How can providers add custom data?
4. **Validation**: What constraints apply?

---

## Definition

**Normalized Signal Format** is a standard DTO structure with:
- **Header**: Routing and identification information
- **Payload**: Signal content with type information
- **Metadata**: Optional tracing and source information
- **Additional Fields**: Provider-specific extensions

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | All signals entering Signal Exchange |
| **Lifecycle** | Created by I/O Gateway; consumed by Signal Exchange |
| **Ownership** | Platform-defined format; providers conform |
| **Multiplicity** | One format for all signal types |

---

## Rationale

### Why This Design?

Normalization enables:
1. **Protocol independence**: SX handles one format
2. **Consistent trigger evaluation**: Same structure for all signals
3. **Reliable routing**: Required fields always present
4. **Extensibility**: Additional fields for custom data

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Per-protocol formats in SX** | SX complexity; trigger inconsistency |
| **Loose schema** | Unpredictable; validation issues |
| **No extensions allowed** | Too rigid; limits adoption |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0001](../../decision-logs/0001-signal-normalization.md) | Normalize signal format between SPs and SX |

---

## Structure

### Signal DTO Schema

```json
{
  "signal_header": {
    "tenant_id": "acme-bank",              // Required: Tenant scope
    "subscription_id": "sub-prod-001",     // Required: Subscription scope
    "signal_id": "sig-12345",              // Required: Unique identifier
    "signal_type": "dispute.filed",        // Required: Type for trigger matching
    "timestamp": "2026-01-06T10:00:00Z",   // Required: When signal occurred
    "correlation_id": "txn-99999",         // Optional: Link to existing request
    "idempotency_key": "idem-22222"        // Optional: Deduplication key
  },
  "payload": {
    "content_type": "application/json",    // Required: application/json | application/base64
    "semantic_type": "com.acme.DisputeFiled", // Optional: Domain-specific type
    "data": {                              // Required: Signal-specific content
      "customer_id": "CUST-001",
      "transaction_id": "TXN-99999",
      "amount": 500.00,
      "reason": "unauthorized_charge"
    }
  },
  "metadata": {                            // Optional: Tracing and source info
    "source_system": "core-banking",
    "source_event_id": "evt-99999",
    "trace_id": "trace-abc123",
    "gateway": "heracles"
  },
  "additional_fields": {                   // Optional: Provider extensions
    "raw_event": { },                      // Preserved but not processed by SX
    "provider_context": { }
  }
}
```

### Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| `signal_header.tenant_id` | ✓ | Tenant owning this signal |
| `signal_header.subscription_id` | ✓ | Subscription scope |
| `signal_header.signal_id` | ✓ | Unique signal identifier (UUID) |
| `signal_header.signal_type` | ✓ | Type used for trigger matching |
| `signal_header.timestamp` | ✓ | ISO 8601 timestamp of signal |
| `signal_header.correlation_id` | | Link to existing request |
| `signal_header.idempotency_key` | | Key for deduplication |
| `payload.content_type` | ✓ | MIME type of data |
| `payload.semantic_type` | | Domain-specific type URI |
| `payload.data` | ✓ | Signal content |
| `metadata.*` | | Tracing and debugging info |
| `additional_fields.*` | | Provider-specific extensions |

---

## Behavior

### How It Works

**Normalization Process:**
```
1. Signal arrives at I/O Gateway
   └── Protocol-specific format (HTTP, Kafka, file, etc.)

2. Gateway extracts required fields:
   ├── tenant_id from auth context or header
   ├── subscription_id from path or header
   ├── signal_type from path, header, or payload
   └── timestamp (gateway adds if missing)

3. Gateway generates signal_id (UUID)

4. Gateway maps payload:
   ├── content_type from Content-Type header or inference
   └── data from request body

5. Gateway preserves metadata and additional fields

6. Normalized DTO forwarded to Signal Exchange
```

### Validation

```
Signal Exchange validates:
├── All required fields present
├── tenant_id matches authenticated context
├── subscription_id exists within tenant
├── signal_type is non-empty string
├── timestamp is valid ISO 8601
├── payload.data is valid JSON (if application/json)
└── idempotency_key unique within window (if provided)
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| I/O Gateway | ← creates | Gateway normalizes to this format |
| Signal Exchange | → consumed by | SX receives normalized signals |
| Trigger Evaluator | → read by | Triggers match against signal_type and payload |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Required fields** | Header fields and payload.data always present |
| **Valid tenant** | tenant_id must match authenticated identity |
| **Unique signal_id** | signal_id is globally unique |
| **Consistent timestamp** | UTC ISO 8601 format |
| **Idempotency window** | Idempotency key valid for configurable window |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Protocol independence** | Any source, same processing |
| ✅ **Consistent triggers** | All signals evaluated uniformly |
| ✅ **Extensible** | Additional fields for custom needs |
| ✅ **Traceable** | Metadata for debugging |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Transformation overhead** | Efficient Gateway implementation |
| ⚠️ **Schema evolution** | Versioned format; backward compatible |

---

## Examples

### Example 1: Dispute Filed Signal

```json
{
  "signal_header": {
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "signal_id": "sig-abc-123",
    "signal_type": "dispute.filed",
    "timestamp": "2026-01-06T10:00:00Z"
  },
  "payload": {
    "content_type": "application/json",
    "semantic_type": "com.acme.disputes.DisputeFiledEvent",
    "data": {
      "customer_id": "CUST-001",
      "transaction_id": "TXN-99999",
      "amount": 500.00,
      "currency": "USD",
      "reason": "unauthorized_charge",
      "filed_at": "2026-01-06T09:58:00Z"
    }
  },
  "metadata": {
    "source_system": "mobile-banking-app",
    "trace_id": "trace-xyz-789"
  }
}
```

### Example 2: Document Uploaded Signal with Correlation

```json
{
  "signal_header": {
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "signal_id": "sig-def-456",
    "signal_type": "document.uploaded",
    "timestamp": "2026-01-06T14:00:00Z",
    "correlation_id": "req-dispute-001"
  },
  "payload": {
    "content_type": "application/json",
    "data": {
      "document_id": "doc-123",
      "document_type": "bank_statement",
      "filename": "statement-jan-2026.pdf"
    }
  }
}
```

---

## Implementation Notes

### For Developers

- Use signal_type for routing; keep it stable
- Include correlation_id when updating existing requests
- Use semantic_type for domain-specific type information
- idempotency_key recommended for reliability

### For Operators

- Monitor signal validation errors
- Review normalization latency at Gateways
- Manage idempotency key window configuration

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [I/O Gateway](./io-gateway.md) | Creates normalized signals |
| [Signal Exchange](./signal-exchange.md) | Consumes normalized signals |
| [Message Envelope](./message-envelope.md) | Wrapper for application communication |

---

## References

- [Signal Exchange Subsystem](../../04-subsystems/signal-exchange/README.md)
- [Signal Provider Interactions](../../04-subsystems/signal-exchange/signal-provider-interactions.md)
- [ADR-0001: Signal Normalization](../../decision-logs/0001-signal-normalization.md)

