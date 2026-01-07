# CAF Memory Store Contract

> **Status**: Draft  
> **Last Updated**: 2026-01-07  
> **Memory Scope**: Episodic Memory Stores  
> **Related**: [CAF README](./README.md) | [Record Relationships](./record-relationships.md) | [CAF Store REST API](./caf-store-rest-api.md)

---

## Overview

This document defines the contract between the **Cognitive Audit Fabric (CAF)** control plane and **Episodic Memory Stores** that hold CAF records. Memory Stores register with CAF, advertise both reader and writer protocols, and expose standardized APIs for case and record access.

### Scope: Episodic Memory

This contract applies to **Episodic Memory Stores** — stores that hold event-based, time-ordered, case-bound records:

| Record Type | Description |
|-------------|-------------|
| Case Record | Case anchor and lifecycle |
| Decision Record | Decision with rationale |
| Evidence Bundle | Context at decision time |
| Context Snapshot | Compiled context per turn |
| Outcome Record | Post-decision outcomes |
| Override Record | Manual override documentation |
| Handoff Context | State transfer between agents |
| Incident Timeline | Chronological event sequence |
| Hypothesis Record | Learned patterns (may promote to Semantic) |

**Other memory types** (Semantic, Procedural, Preference) will have separate contracts. See [Future: Other Memory Store Types](#future-other-memory-store-types).

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Dual Protocol** | Stores advertise both reader and writer protocols |
| **Default REST** | All stores must implement CAF Store REST API for both read and write |
| **Storage Agnostic** | CAF doesn't know store internals; it follows hypermedia links |
| **Single Store per Case** | A case's records are fully contained in one store |
| **CAF-Controlled Access** | CAF access layer authorizes principals; stores verify CAF signatures |
| **Canonical Naming** | Each store has a unique canonical name within its host service |

---

## Registration Model

Memory Stores register with CAF via a Kubernetes Custom Resource Definition (CRD).

### MemoryStore CRD

```yaml
apiVersion: olympus.hub/v1
kind: MemoryStore
metadata:
  name: fraud-ops-episodic-memory
  namespace: workbench-fraud-ops
spec:
  # ─────────────────────────────────────────────────────────────────
  # Identity
  # ─────────────────────────────────────────────────────────────────
  canonical_name: "fraud-ops.episodic-memory.primary"
  display_name: "Fraud Operations - Primary Episodic Memory"
  
  # A single memory store service can host multiple stores
  # Each store is distinguished by its canonical_name
  host_service: "episodic-memory-service"
  
  # ─────────────────────────────────────────────────────────────────
  # Classification
  # ─────────────────────────────────────────────────────────────────
  memory_class: episodic              # episodic | semantic | procedural | preference
  store_type: enterprise_memory       # enterprise_memory | agent_memory | user_memory
  
  # Metadata describing purpose and scope
  metadata:
    purpose: "Primary store for fraud case decisions, evidence, and outcomes"
    scope: "workbench"                # tenant | subscription | workbench
    data_classification: "cognitive"  # Per ADR-0028
    retention_policy: "7-years"
    
  # ─────────────────────────────────────────────────────────────────
  # Writer Protocols
  # ─────────────────────────────────────────────────────────────────
  writer_protocols:
    - protocol: rest
      version: "1.0"
      spec: "caf-store-rest-api/v1"   # CAF-defined spec (required)
      endpoint: https://memory.fraud-ops.olympus.internal/v1/stores/{store_name}/records
      status: active
      
    - protocol: grpc                   # Optional alternative
      version: "1.0"
      spec: "caf-store-grpc-api/v1"
      endpoint: grpc://memory.fraud-ops.olympus.internal:443
      status: active
      
    - protocol: kafka                  # Optional streaming
      version: "1.0"
      spec: "vendor-specific"
      endpoint: kafka://kafka.internal:9092/caf-records
      status: active
    
  # ─────────────────────────────────────────────────────────────────
  # Reader Protocols
  # ─────────────────────────────────────────────────────────────────
  reader_protocols:
    - protocol: rest
      version: "1.0"
      spec: "caf-store-read-api/v1"   # CAF-defined spec (required)
      endpoint: https://memory.fraud-ops.olympus.internal/v1/stores/{store_name}
      status: active
    
  # ─────────────────────────────────────────────────────────────────
  # Capabilities
  # ─────────────────────────────────────────────────────────────────
  capabilities:
    views:
      - expanded        # All records with full data inline
      - timeline        # Chronological list with record refs and summaries
      - summary         # Counts and metadata only
      
    record_types:
      - case_record           # Case anchor (required for episodic stores)
      - decision_record
      - evidence_bundle
      - context_snapshot
      - outcome_record
      - override_record
      - handoff_context
      - hypothesis_record
      - incident_timeline
      
    features:
      pagination: true
      max_records_per_response: 500
      supports_time_range_filter: true
      supports_record_type_filter: true
      order_tolerant_writes: true     # Handles out-of-order records
      deduplication: true             # Idempotent by record_id

status:
  registered: true
  last_health_check: "2026-01-07T14:30:00Z"
  health_status: healthy
```

### Canonical Naming Convention

```
{scope}.{store_type}.{qualifier}
```

| Component | Description | Examples |
|-----------|-------------|----------|
| `scope` | Workbench, subscription, or tenant identifier | `fraud-ops`, `tenant-acme` |
| `store_type` | Type of memory store | `enterprise-memory`, `agent-memory` |
| `qualifier` | Distinguishes multiple stores of same type | `primary`, `archive`, `hot` |

**Examples:**
- `fraud-ops.enterprise-memory.primary`
- `fraud-ops.agent-memory.session-cache`
- `tenant-acme.enterprise-memory.compliance-archive`

---

## Authentication Model

### CAF Request Signing

CAF signs all requests to memory stores using **JSON Web Signature (JWS)**.

```
┌─────────────────────────────────────────────────────────────────┐
│                         CAF Control Plane                        │
│                                                                  │
│  1. Principal authenticated by CAF Access Layer                  │
│  2. CAF signs request with private key                           │
│  3. JWS includes principal identity (for audit, not authz)       │
│                                                                  │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              │  HTTPS + JWS Header
                              │  X-CAF-Signature: <jws>
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Memory Store                              │
│                                                                  │
│  1. Verify JWS signature using CAF public key                    │
│  2. Extract principal (for logging, not authorization)           │
│  3. Process request (store does NOT authorize principal)         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### JWS Payload Structure

```json
{
  "iss": "olympus.caf",
  "iat": 1736261400,
  "exp": 1736261700,
  "jti": "unique-request-id",
  
  "principal": {
    "type": "user",
    "id": "user-123",
    "tenant_id": "tenant-acme",
    "roles": ["fraud_analyst"]
  },
  
  "request": {
    "method": "GET",
    "path": "/v1/stores/fraud-ops.enterprise-memory.primary/cases/550e8400-...",
    "query": "view=timeline"
  }
}
```

### CAF Public Key Distribution

CAF publishes its public keys at a well-known endpoint:

```
GET https://caf.olympus.internal/.well-known/jwks.json
```

```json
{
  "keys": [
    {
      "kty": "EC",
      "kid": "caf-signing-key-2026-01",
      "use": "sig",
      "alg": "ES256",
      "crv": "P-256",
      "x": "...",
      "y": "..."
    }
  ]
}
```

Memory stores:
- Fetch and cache CAF public keys
- Verify JWS signature on every request
- Reject requests with invalid or expired signatures
- **Do NOT authorize the principal** — CAF access layer handles authorization

### Store-Specific Access (Non-CAF)

Memory stores may expose additional interfaces to their own clients with their own authentication and authorization semantics. This contract only governs the **CAF ↔ Memory Store** interface.

---

## Case Retrieval API

Memory stores implement the following endpoints for CAF to retrieve case data.

### GET Case

```
GET /v1/stores/{store_name}/cases/{case_id}
```

#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `view` | enum | No | `expanded` (default), `timeline`, `summary` |
| `record_types` | string[] | No | Filter to specific record types (comma-separated) |
| `from` | ISO8601 | No | Start of time range |
| `to` | ISO8601 | No | End of time range |
| `cursor` | string | No | Pagination cursor |
| `limit` | integer | No | Max records per page (default: 100, max: 500) |

#### Response: Expanded View

Returns all records with full data inline.

```json
{
  "case_id": "550e8400-e29b-41d4-a716-446655440000",
  "store": {
    "canonical_name": "fraud-ops.enterprise-memory.primary",
    "display_name": "Fraud Operations - Primary Enterprise Memory"
  },
  "retrieved_at": "2026-01-07T14:30:00Z",
  "view": "expanded",
  
  "summary": {
    "total_records": 23,
    "record_counts": {
      "decision_record": 3,
      "evidence_bundle": 3,
      "context_snapshot": 12,
      "outcome_record": 2,
      "override_record": 1,
      "handoff_context": 2
    },
    "time_range": {
      "earliest": "2026-01-07T10:15:00Z",
      "latest": "2026-01-07T14:22:00Z"
    }
  },
  
  "records": [
    {
      "record_type": "decision_record",
      "record_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "timestamp": "2026-01-07T10:15:00Z",
      "self": "https://memory.fraud-ops.olympus.internal/v1/stores/fraud-ops.enterprise-memory.primary/records/decision_record/a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      
      "data": {
        "decision_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "case_id": "550e8400-e29b-41d4-a716-446655440000",
        "timestamp": "2026-01-07T10:15:00Z",
        "actor": {
          "type": "agent",
          "id": "fraud-case-resolution-agent"
        },
        "decision": {
          "action": "step_up",
          "outcome": "Request additional verification from customer"
        },
        "confidence": 0.78,
        "evidence_bundle_id": "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        "hub_metadata": {
          "tenant_id": "tenant-acme",
          "workbench_id": "fraud-ops",
          "request_id": "550e8400-e29b-41d4-a716-446655440000"
        }
      }
    }
    // ... more records
  ],
  
  "_links": {
    "self": {
      "href": "https://memory.fraud-ops.olympus.internal/v1/stores/fraud-ops.enterprise-memory.primary/cases/550e8400-...?view=expanded"
    },
    "timeline": {
      "href": "https://memory.fraud-ops.olympus.internal/v1/stores/fraud-ops.enterprise-memory.primary/cases/550e8400-...?view=timeline"
    },
    "summary": {
      "href": "https://memory.fraud-ops.olympus.internal/v1/stores/fraud-ops.enterprise-memory.primary/cases/550e8400-...?view=summary"
    }
  },
  
  "_pagination": {
    "has_more": true,
    "cursor": "eyJsYXN0X3RpbWVzdGFtcCI6IjIwMjYtMDEtMDdUMTI6MDA6MDBaIn0=",
    "next": {
      "href": "https://memory.fraud-ops.olympus.internal/v1/stores/fraud-ops.enterprise-memory.primary/cases/550e8400-...?view=expanded&cursor=eyJ..."
    }
  }
}
```

#### Response: Timeline View

Chronological list with record references and human-readable summaries.

```json
{
  "case_id": "550e8400-e29b-41d4-a716-446655440000",
  "store": {
    "canonical_name": "fraud-ops.enterprise-memory.primary"
  },
  "view": "timeline",
  
  "timeline": [
    {
      "timestamp": "2026-01-07T10:15:00Z",
      "record_type": "context_snapshot",
      "record_id": "c3d4e5f6-a7b8-9012-cdef-345678901234",
      "self": {
        "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records/context_snapshot/c3d4e5f6-..."
      },
      "summary": "Context compiled for turn 1: 12 facts, 3 policies, 2 prior decisions"
    },
    {
      "timestamp": "2026-01-07T10:15:05Z",
      "record_type": "decision_record",
      "record_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "self": {
        "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records/decision_record/a1b2c3d4-..."
      },
      "summary": "Decision: step_up — Request additional verification (confidence: 0.78)"
    },
    {
      "timestamp": "2026-01-07T10:15:05Z",
      "record_type": "evidence_bundle",
      "record_id": "b2c3d4e5-f6a7-8901-bcde-f23456789012",
      "self": {
        "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records/evidence_bundle/b2c3d4e5-..."
      },
      "summary": "Evidence bundle: 5 items (2 policies, 1 prior decision, 2 facts)"
    },
    {
      "timestamp": "2026-01-07T11:30:00Z",
      "record_type": "handoff_context",
      "record_id": "d4e5f6a7-b8c9-0123-def4-567890123456",
      "self": {
        "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records/handoff_context/d4e5f6a7-..."
      },
      "summary": "Handoff: fraud-case-agent → human-analyst (3 open items)"
    },
    {
      "timestamp": "2026-01-07T14:22:00Z",
      "record_type": "outcome_record",
      "record_id": "e5f6a7b8-c9d0-1234-ef56-789012345678",
      "self": {
        "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records/outcome_record/e5f6a7b8-..."
      },
      "summary": "Outcome: step_up successful — customer verified, case approved"
    }
  ],
  
  "_links": {
    "self": { "href": "...?view=timeline" },
    "expanded": { "href": "...?view=expanded" }
  }
}
```

#### Response: Summary View

Metadata and counts only — no individual records.

```json
{
  "case_id": "550e8400-e29b-41d4-a716-446655440000",
  "store": {
    "canonical_name": "fraud-ops.enterprise-memory.primary"
  },
  "view": "summary",
  
  "summary": {
    "total_records": 23,
    "record_counts": {
      "decision_record": 3,
      "evidence_bundle": 3,
      "context_snapshot": 12,
      "outcome_record": 2,
      "override_record": 1,
      "handoff_context": 2,
      "hypothesis_record": 0,
      "incident_timeline": 0
    },
    "time_range": {
      "earliest": "2026-01-07T10:15:00Z",
      "latest": "2026-01-07T14:22:00Z"
    },
    "actors": [
      { "type": "agent", "id": "fraud-case-resolution-agent", "decision_count": 2 },
      { "type": "human", "id": "analyst-jane", "decision_count": 1 }
    ],
    "final_outcome": {
      "action": "approve",
      "timestamp": "2026-01-07T14:22:00Z"
    }
  },
  
  "_links": {
    "self": { "href": "...?view=summary" },
    "expanded": { "href": "...?view=expanded" },
    "timeline": { "href": "...?view=timeline" }
  }
}
```

---

## Record Retrieval API

### GET Record

```
GET /v1/stores/{store_name}/records/{record_type}/{record_id}
```

#### Response

```json
{
  "record_type": "decision_record",
  "record_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "case_id": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2026-01-07T10:15:00Z",
  
  "self": {
    "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records/decision_record/a1b2c3d4-..."
  },
  
  "data": {
    // Full record content per CAF schema (decision-records.md)
  },
  
  "_links": {
    "case": {
      "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../cases/550e8400-..."
    },
    "evidence_bundle": {
      "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records/evidence_bundle/b2c3d4e5-...",
      "rel": "evidence"
    },
    "context_snapshot": {
      "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records/context_snapshot/c3d4e5f6-...",
      "rel": "context"
    },
    "outcome_record": {
      "href": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records/outcome_record/e5f6a7b8-...",
      "rel": "outcome"
    }
  }
}
```

---

## Capabilities Endpoint

Stores expose their capabilities for CAF to query.

### GET Capabilities

```
GET /v1/stores/{store_name}/capabilities
```

```json
{
  "store": {
    "canonical_name": "fraud-ops.enterprise-memory.primary",
    "display_name": "Fraud Operations - Primary Enterprise Memory",
    "store_type": "enterprise_memory"
  },
  
  "metadata": {
    "purpose": "Primary store for fraud case decisions, evidence, and outcomes",
    "scope": "workbench",
    "data_classification": "cognitive",
    "retention_policy": "7-years"
  },
  
  "capabilities": {
    "views": ["expanded", "timeline", "summary"],
    "record_types": [
      "decision_record",
      "evidence_bundle",
      "context_snapshot",
      "outcome_record",
      "override_record",
      "handoff_context",
      "hypothesis_record",
      "incident_timeline"
    ],
    "features": {
      "pagination": true,
      "max_records_per_response": 500,
      "supports_time_range_filter": true,
      "supports_record_type_filter": true
    }
  },
  
  "_links": {
    "self": { "href": "/v1/stores/fraud-ops.enterprise-memory.primary/capabilities" },
    "jwks": { "href": "https://caf.olympus.internal/.well-known/jwks.json", "rel": "caf-keys" }
  }
}
```

---

## Error Responses

### Standard Error Format

```json
{
  "error": {
    "code": "CASE_NOT_FOUND",
    "message": "Case 550e8400-... not found in store fraud-ops.enterprise-memory.primary",
    "details": {
      "case_id": "550e8400-e29b-41d4-a716-446655440000",
      "store": "fraud-ops.enterprise-memory.primary"
    }
  },
  "request_id": "req-abc123"
}
```

### Error Codes

| HTTP Status | Code | Description |
|-------------|------|-------------|
| 400 | `INVALID_REQUEST` | Malformed request or invalid parameters |
| 401 | `SIGNATURE_INVALID` | JWS signature verification failed |
| 401 | `SIGNATURE_EXPIRED` | JWS token expired |
| 403 | `STORE_ACCESS_DENIED` | Store rejected request (rare — CAF controls access) |
| 404 | `CASE_NOT_FOUND` | Case ID not found in this store |
| 404 | `RECORD_NOT_FOUND` | Record ID not found |
| 404 | `STORE_NOT_FOUND` | Store canonical name not recognized |
| 422 | `VIEW_NOT_SUPPORTED` | Requested view not in store capabilities |
| 429 | `RATE_LIMITED` | Too many requests |
| 503 | `STORE_UNAVAILABLE` | Store temporarily unavailable |

---

## Health Endpoint

### GET Health

```
GET /health
```

```json
{
  "status": "healthy",
  "stores": [
    {
      "canonical_name": "fraud-ops.enterprise-memory.primary",
      "status": "healthy",
      "last_write": "2026-01-07T14:25:00Z",
      "record_count": 15234
    },
    {
      "canonical_name": "fraud-ops.agent-memory.session-cache",
      "status": "healthy",
      "last_write": "2026-01-07T14:29:55Z",
      "record_count": 892
    }
  ]
}
```

---

## Implementation Checklist

Episodic Memory Store implementations must:

| # | Requirement | Notes |
|---|-------------|-------|
| 1 | Register via MemoryStore CRD | Include canonical name, protocols, capabilities |
| 2 | Implement CAF Store REST API (write) | Order-tolerant, idempotent, validating |
| 3 | Implement CAF Store REST API (read) | All three views (expanded, timeline, summary) |
| 4 | Verify JWS signatures | Fetch CAF public keys from JWKS endpoint |
| 5 | Handle out-of-order records | Accept decisions before cases, resolve later |
| 6 | De-duplicate by record_id | Same record twice = idempotent |
| 7 | Implement capabilities endpoint | For CAF discovery |
| 8 | Implement health endpoint | For CAF monitoring |
| 9 | Return standard error format | Use defined error codes |
| 10 | Support pagination | For large cases |
| 11 | Generate record summaries | Human-readable for timeline view |

---

## Future: Other Memory Store Types

This contract covers **Episodic Memory Stores**. Future contracts will define stores for other memory classes:

### Memory Class Taxonomy

| Memory Class | Purpose | Record Types | Contract Status |
|--------------|---------|--------------|-----------------|
| **Episodic** | Event-based, time-ordered, case-bound | Case, Decision, Evidence, Outcome, etc. | ✅ This document |
| **Semantic** | Facts, entities, relationships | Entity, Relationship, Fact, Concept | 🔴 TODO |
| **Procedural** | Learned skills, patterns, procedures | Skill, Procedure, Pattern | 🔴 TODO |
| **Preference** | User/agent preferences, behaviors | Preference, Behavior, Setting | 🔴 TODO |

### Hypothesis Records: The Bridge

`HypothesisRecord` is unique—it starts in Episodic Memory (learned from cases) but may be **promoted** to:
- **Semantic Memory** → becomes a `Fact` or `Entity`
- **Procedural Memory** → becomes a `Skill` or `Pattern`

This promotion workflow will be defined in the Semantic/Procedural contracts.

### Planned Contract Documents

| Document | Description | Priority |
|----------|-------------|----------|
| `semantic-memory-store-contract.md` | Entity, fact, relationship stores | P2 |
| `procedural-memory-store-contract.md` | Skill and pattern stores | P2 |
| `preference-memory-store-contract.md` | User/agent preference stores | P3 |
| `hypothesis-promotion-workflow.md` | Episodic → Semantic/Procedural promotion | P2 |

---

## Related Documents

- [CAF README](./README.md) — Overview and conventions
- [CAF Store REST API](./caf-store-rest-api.md) — Write API specification
- [Case Records](./case-records.md) — Case record schema
- [Record Relationships](./record-relationships.md) — How records link together
- [Decision Records](./decision-records.md) — Decision record schema
- [Evidence Bundles](./evidence-bundles.md) — Evidence bundle schema

