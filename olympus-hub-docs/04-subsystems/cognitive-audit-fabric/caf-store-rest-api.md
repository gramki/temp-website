# CAF Store REST API Specification

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [Memory Store Contract](./memory-store-contract.md) | [Case Records](./case-records.md)

---

## Overview

This document defines the **default write API** that all CAF-compliant Episodic Memory Stores must implement. Stores advertise this capability during registration and CAF (or any authorized writer) uses this API to persist records.

### Design Principles

| Principle | Description |
|-----------|-------------|
| **Order-Tolerant** | Records may arrive in any order (decision before case, outcome before decision) |
| **Idempotent** | Same record written twice produces same result (de-duplication by ID) |
| **Eventually Consistent** | Relationships resolved asynchronously |
| **Schema-Validating** | Stores validate against CAF schemas before accepting |

---

## Protocol Registration

Memory Stores declare supported writer protocols in their CRD:

```yaml
apiVersion: olympus.hub/v1
kind: MemoryStore
metadata:
  name: fraud-ops-enterprise-memory
spec:
  canonical_name: "fraud-ops.episodic-memory.primary"
  store_type: episodic_memory           # Qualified as episodic
  
  # ─────────────────────────────────────────────────────────────────
  # Writer Protocols
  # ─────────────────────────────────────────────────────────────────
  writer_protocols:
    - protocol: rest
      version: "1.0"
      spec: "caf-store-rest-api/v1"     # Reference to this spec
      endpoint: https://memory.fraud-ops.olympus.internal/v1/stores/{store_name}/records
      status: active
      
    - protocol: grpc
      version: "1.0"
      spec: "caf-store-grpc-api/v1"     # Optional gRPC spec
      endpoint: grpc://memory.fraud-ops.olympus.internal:443
      status: active
      
    - protocol: kafka
      version: "1.0"
      spec: "vendor-specific"            # Custom streaming protocol
      endpoint: kafka://kafka.internal:9092/caf-records
      status: active
      
  # Reader protocols (from memory-store-contract.md)
  reader_protocols:
    - protocol: rest
      version: "1.0"
      spec: "caf-store-read-api/v1"
      endpoint: https://memory.fraud-ops.olympus.internal/v1/stores/{store_name}
      status: active
```

### Protocol Priority

When multiple protocols are available, writers should prefer:
1. **REST** — Default, always supported, synchronous acknowledgment
2. **gRPC** — High-performance alternative when available
3. **Kafka/Streaming** — For high-volume batch writes

---

## REST API Endpoints

### Base URL

```
https://{store_host}/v1/stores/{store_name}/records
```

### Authentication

All write requests must include CAF JWS signature (see [Memory Store Contract](./memory-store-contract.md)):

```
X-CAF-Signature: <jws>
```

---

## Write Operations

### POST Record

Write a single record to the store.

```
POST /v1/stores/{store_name}/records
Content-Type: application/json
X-CAF-Signature: <jws>
```

#### Request Body

```json
{
  "record_type": "decision_record",
  "record_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "case_id": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2026-01-07T10:15:00Z",
  
  "data": {
    // Full record content per CAF schema
  },
  
  "write_options": {
    "if_not_exists": false,           // Fail if record exists (default: upsert)
    "validate_references": false      // Check foreign keys exist (default: false)
  }
}
```

#### Response: Success (201 Created / 200 OK)

```json
{
  "status": "accepted",
  "record_type": "decision_record",
  "record_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "case_id": "550e8400-e29b-41d4-a716-446655440000",
  
  "self": {
    "href": "https://memory.../v1/stores/.../records/decision_record/a1b2c3d4-..."
  },
  
  "write_result": {
    "action": "created",              // created | updated | duplicate_ignored
    "version": 1,                     // Record version (increments on update)
    "written_at": "2026-01-07T10:15:01Z"
  }
}
```

#### Response: Duplicate (200 OK with duplicate_ignored)

When the exact same record is written again:

```json
{
  "status": "accepted",
  "record_id": "a1b2c3d4-...",
  "write_result": {
    "action": "duplicate_ignored",
    "existing_version": 1,
    "written_at": "2026-01-07T10:15:01Z"   // Original write time
  }
}
```

---

### POST Batch Records

Write multiple records in a single request.

```
POST /v1/stores/{store_name}/records/batch
Content-Type: application/json
X-CAF-Signature: <jws>
```

#### Request Body

```json
{
  "records": [
    {
      "record_type": "case_record",
      "record_id": "550e8400-...",
      "case_id": "550e8400-...",
      "timestamp": "2026-01-07T10:00:00Z",
      "data": { /* ... */ }
    },
    {
      "record_type": "decision_record",
      "record_id": "a1b2c3d4-...",
      "case_id": "550e8400-...",
      "timestamp": "2026-01-07T10:15:00Z",
      "data": { /* ... */ }
    },
    {
      "record_type": "evidence_bundle",
      "record_id": "b2c3d4e5-...",
      "case_id": "550e8400-...",
      "timestamp": "2026-01-07T10:15:00Z",
      "data": { /* ... */ }
    }
  ],
  
  "batch_options": {
    "atomic": false,                  // All-or-nothing (default: false = best effort)
    "continue_on_error": true         // Process remaining after error
  }
}
```

#### Response: Batch Result

```json
{
  "status": "completed",
  "total": 3,
  "succeeded": 3,
  "failed": 0,
  
  "results": [
    {
      "record_type": "case_record",
      "record_id": "550e8400-...",
      "status": "accepted",
      "action": "created"
    },
    {
      "record_type": "decision_record",
      "record_id": "a1b2c3d4-...",
      "status": "accepted",
      "action": "created"
    },
    {
      "record_type": "evidence_bundle",
      "record_id": "b2c3d4e5-...",
      "status": "accepted",
      "action": "created"
    }
  ]
}
```

---

## Order Tolerance

The API is designed to handle out-of-order record arrival.

### Scenario: Decision Before Case

```
# Decision record arrives first
POST /records
{
  "record_type": "decision_record",
  "case_id": "case-123",        # Case doesn't exist yet
  "data": { ... }
}

# Response: Accepted (case_id stored as dangling reference)
{
  "status": "accepted",
  "write_result": {
    "action": "created",
    "pending_references": ["case_id:case-123"]  # Case not yet present
  }
}

# Case record arrives later
POST /records
{
  "record_type": "case_record",
  "case_id": "case-123",
  "data": { ... }
}

# Response: Reference resolved
{
  "status": "accepted",
  "write_result": {
    "action": "created",
    "resolved_references": 1     # Decision now linked
  }
}
```

### Store Behavior

| Situation | Store Behavior |
|-----------|----------------|
| Record references non-existent case | Accept, mark as pending |
| Case arrives after referencing records | Link all pending records |
| Outcome references non-existent decision | Accept, mark as pending |
| Evidence bundle references non-existent context | Accept, mark as pending |

### Consistency Guarantees

| Guarantee | Description |
|-----------|-------------|
| **Immediate** | Record persisted and queryable by ID |
| **Eventually** | Relationships resolved when referenced records arrive |
| **Never Blocking** | Missing references don't block writes |

---

## De-duplication

Stores must handle duplicate writes idempotently.

### De-duplication Key

```
(record_type, record_id)
```

### De-duplication Behavior

| Scenario | Behavior |
|----------|----------|
| Exact duplicate (same content) | Return `duplicate_ignored`, no update |
| Same ID, different content | Return `updated`, increment version |
| Same ID, `if_not_exists: true` | Return error `RECORD_EXISTS` |

### Version Tracking

```json
{
  "record_id": "a1b2c3d4-...",
  "version": 2,
  "version_history": [
    { "version": 1, "written_at": "2026-01-07T10:15:00Z", "writer": "agent-1" },
    { "version": 2, "written_at": "2026-01-07T10:20:00Z", "writer": "human-jane" }
  ]
}
```

---

## Schema Validation

Stores validate incoming records against CAF schemas.

### Validation Levels

| Level | Description | Configurable |
|-------|-------------|--------------|
| **Structure** | Required fields present, types correct | No (always enforced) |
| **Content Types** | MIME types valid, versions recognized | Yes |
| **References** | Foreign keys exist | Yes (`validate_references`) |
| **Business Rules** | Domain-specific constraints | Store-specific |

### Validation Error Response

```json
{
  "status": "rejected",
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "Record validation failed",
    "details": {
      "record_type": "decision_record",
      "record_id": "a1b2c3d4-...",
      "violations": [
        {
          "field": "confidence",
          "constraint": "range",
          "message": "confidence must be between 0 and 1",
          "value": 1.5
        },
        {
          "field": "actor.type",
          "constraint": "enum",
          "message": "actor.type must be one of: agent, human, system",
          "value": "bot"
        }
      ]
    }
  }
}
```

---

## Supported Record Types

This REST API supports all **Episodic Memory** record types:

| Record Type | Description |
|-------------|-------------|
| `case_record` | Case anchor and lifecycle |
| `decision_record` | Decision with rationale |
| `evidence_bundle` | Context snapshot at decision time |
| `context_snapshot` | Compiled context per agent turn |
| `outcome_record` | Post-decision outcome tracking |
| `override_record` | Manual override documentation |
| `handoff_context` | Agent-to-agent state transfer |
| `incident_timeline` | Chronological event sequence |
| `hypothesis_record` | Learned pattern (may promote to Semantic) |

---

## Error Codes

| HTTP Status | Code | Description |
|-------------|------|-------------|
| 400 | `INVALID_REQUEST` | Malformed JSON or missing required fields |
| 400 | `VALIDATION_FAILED` | Schema validation failed |
| 401 | `SIGNATURE_INVALID` | JWS signature verification failed |
| 401 | `SIGNATURE_EXPIRED` | JWS token expired |
| 404 | `STORE_NOT_FOUND` | Store canonical name not recognized |
| 409 | `RECORD_EXISTS` | Record exists and `if_not_exists: true` |
| 413 | `BATCH_TOO_LARGE` | Batch exceeds max records per request |
| 422 | `UNSUPPORTED_RECORD_TYPE` | Record type not in store capabilities |
| 429 | `RATE_LIMITED` | Too many requests |
| 503 | `STORE_UNAVAILABLE` | Store temporarily unavailable |

---

## Rate Limits & Quotas

| Limit | Default | Configurable |
|-------|---------|--------------|
| Single record writes | 1000/min | Yes |
| Batch writes | 100/min | Yes |
| Records per batch | 100 | Yes |
| Max record size | 1 MB | Yes |
| Max batch size | 10 MB | Yes |

---

## Implementation Checklist

Stores implementing this spec must:

| # | Requirement |
|---|-------------|
| 1 | Accept records in any order (case may arrive after decisions) |
| 2 | De-duplicate by `(record_type, record_id)` |
| 3 | Validate against CAF schemas |
| 4 | Track record versions |
| 5 | Resolve pending references when anchor records arrive |
| 6 | Return standardized error codes |
| 7 | Support batch writes |
| 8 | Implement rate limiting |

---

## Related Documents

- [Memory Store Contract](./memory-store-contract.md) — Registration and read API
- [Case Records](./case-records.md) — Case record schema
- [Record Relationships](./record-relationships.md) — How records link together

