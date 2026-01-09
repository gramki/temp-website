# CAF Store REST API Specification

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [CAF README](../README.md) | [Memory Store Contract](./memory-store-contract.md) | [Case Records](./case-records.md)

---

## Overview

This document defines the **default write API** that all CAF-compliant Episodic Memory Stores must implement. Stores advertise this capability during registration and CAF (or any authorized writer) uses this API to persist records.

### Design Principles

| Principle | Description |
|-----------|-------------|
| **Immutable** | Once written, records cannot be modified or deleted |
| **Order-Tolerant** | Records may arrive in any order (decision before case, outcome before decision) |
| **Idempotent** | Same record written twice produces same result (de-duplication by ID + hash) |
| **Eventually Consistent** | Relationships resolved asynchronously |
| **Schema-Validating** | Stores validate against CAF schemas before accepting |
| **Hash-Verified** | All records include content hash for integrity verification |

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
  "content_hash": "sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  
  "data": {
    // Full record content per CAF schema
  },
  
  "write_options": {
    "validate_references": false      // Check foreign keys exist (default: false)
  }
}
```

#### Response: Success (201 Created)

```json
{
  "status": "accepted",
  "record_type": "decision_record",
  "record_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "case_id": "550e8400-e29b-41d4-a716-446655440000",
  "content_hash": "sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  
  "self": {
    "href": "https://memory.../v1/stores/.../records/decision_record/a1b2c3d4-..."
  },
  
  "write_result": {
    "action": "created",              // created | duplicate (exact match)
    "written_at": "2026-01-07T10:15:01Z"
  }
}
```

#### Response: Duplicate (200 OK)

When the exact same record (matching `record_id` + `content_hash`) is written again:

```json
{
  "status": "accepted",
  "record_id": "a1b2c3d4-...",
  "content_hash": "sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "write_result": {
    "action": "duplicate",
    "written_at": "2026-01-07T10:15:01Z"   // Original write time
  }
}
```

#### Response: Conflict (409 Conflict)

When a record with the same `record_id` but **different** `content_hash` is written:

```json
{
  "status": "rejected",
  "error": {
    "code": "IMMUTABLE_CONFLICT",
    "message": "Record already exists with different content",
    "details": {
      "record_id": "a1b2c3d4-...",
      "existing_hash": "sha256:abc123...",
      "submitted_hash": "sha256:def456...",
      "written_at": "2026-01-07T10:15:01Z"
    }
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
      "content_hash": "sha256:abc123...",
      "data": { /* ... */ }
    },
    {
      "record_type": "decision_record",
      "record_id": "a1b2c3d4-...",
      "case_id": "550e8400-...",
      "timestamp": "2026-01-07T10:15:00Z",
      "content_hash": "sha256:def456...",
      "data": { /* ... */ }
    },
    {
      "record_type": "evidence_bundle",
      "record_id": "b2c3d4e5-...",
      "case_id": "550e8400-...",
      "timestamp": "2026-01-07T10:15:00Z",
      "content_hash": "sha256:789abc...",
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

## Immutability

**All episodic memory records are immutable.** Once written, a record cannot be modified or deleted.

### Immutability Guarantees

| Guarantee | Description |
|-----------|-------------|
| **No Updates** | `PUT` and `PATCH` are not supported |
| **No Deletes** | `DELETE` is not supported |
| **Hash Verification** | Content hash prevents accidental rewrites with different data |
| **Audit Trail** | Every write is logged with timestamp and writer identity |

### Why Immutability?

| Reason | Description |
|--------|-------------|
| **Audit Integrity** | Records cannot be tampered with after the fact |
| **Reproducibility** | Decisions can be exactly reconstructed |
| **Compliance** | Meets regulatory requirements for decision traceability |
| **Trust** | Consumers can trust that what they read is what was written |

### Corrections Pattern

If a record contains errors, the correction is captured as a **new record**:

```json
{
  "record_type": "override_record",
  "record_id": "ovr-987654",
  "case_id": "550e8400-...",
  "timestamp": "2026-01-07T11:00:00Z",
  "content_hash": "sha256:correction123...",
  
  "data": {
    "supersedes_record_id": "a1b2c3d4-...",        // Original record
    "supersedes_record_type": "decision_record",
    "reason": "data_correction",
    "corrected_fields": ["decision.confidence"],
    "authority": { "actor_id": "user-jane", "actor_type": "human" },
    "notes": "Original confidence value was calculated incorrectly"
  }
}
```

---

## De-duplication

Stores must handle duplicate writes idempotently based on `(record_type, record_id, content_hash)`.

### De-duplication Key

```
(record_type, record_id, content_hash)
```

### De-duplication Behavior

| Scenario | Behavior |
|----------|----------|
| Same ID + same hash | Return `duplicate`, accept idempotently |
| Same ID + different hash | Return error `IMMUTABLE_CONFLICT` |

### Content Hash Requirements

| Attribute | Requirement |
|-----------|-------------|
| **Algorithm** | SHA-256 (required) |
| **Format** | `sha256:<hex-encoded-hash>` |
| **Scope** | Hash of `data` field contents (canonical JSON) |
| **Validation** | Store MUST verify submitted hash matches computed hash |

```python
import hashlib
import json

def compute_content_hash(data: dict) -> str:
    """Compute canonical hash of record data."""
    canonical = json.dumps(data, sort_keys=True, separators=(',', ':'))
    hash_bytes = hashlib.sha256(canonical.encode('utf-8')).digest()
    return f"sha256:{hash_bytes.hex()}"
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
| 400 | `HASH_MISMATCH` | Submitted hash doesn't match computed hash of data |
| 400 | `HASH_MISSING` | Required `content_hash` field not provided |
| 401 | `SIGNATURE_INVALID` | JWS signature verification failed |
| 401 | `SIGNATURE_EXPIRED` | JWS token expired |
| 404 | `STORE_NOT_FOUND` | Store canonical name not recognized |
| 405 | `METHOD_NOT_ALLOWED` | PUT, PATCH, DELETE not supported (immutability) |
| 409 | `IMMUTABLE_CONFLICT` | Record exists with different content (hash mismatch) |
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
| 1 | **Enforce immutability** — reject PUT, PATCH, DELETE |
| 2 | **Validate content hash** — verify submitted hash matches computed hash |
| 3 | **Detect conflicts** — reject same ID with different hash |
| 4 | Accept records in any order (case may arrive after decisions) |
| 5 | De-duplicate by `(record_type, record_id, content_hash)` |
| 6 | Validate against CAF schemas |
| 7 | Resolve pending references when anchor records arrive |
| 8 | Return standardized error codes |
| 9 | Support batch writes |
| 10 | Implement rate limiting |

---

## Related Documents

- [Memory Store Contract](./memory-store-contract.md) — Registration and read API
- [Case Records](./case-records.md) — Case record schema
- [Record Relationships](./record-relationships.md) — How records link together

