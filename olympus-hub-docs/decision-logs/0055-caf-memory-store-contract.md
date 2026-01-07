# ADR-0055: CAF Memory Store Contract

## Status

**Accepted**

## Date

2026-01-07

## Context

CAF is a control plane for Enterprise Memory—it governs how memory is captured, linked, explained, and audited, but does **not** store memory itself. Memory Stores are the actual storage implementations.

We needed to define:
1. How Memory Stores register with CAF
2. How CAF retrieves case and record data
3. How authentication works between CAF and stores
4. What capabilities stores can declare

Key design goals:
- **Storage Agnostic**: CAF shouldn't know internal store details
- **Hypermedia-driven**: Follow links rather than construct URLs
- **Single Store per Case**: Simplify case reconstruction
- **CAF-Controlled Access**: CAF authorizes principals; stores verify CAF signatures

## Decision

### 1. CRD-Based Registration

Memory Stores register with CAF via a Kubernetes CRD:

```yaml
apiVersion: olympus.hub/v1
kind: MemoryStore
metadata:
  name: fraud-ops-enterprise-memory
spec:
  canonical_name: "fraud-ops.enterprise-memory.primary"
  store_type: enterprise_memory
  endpoints:
    base_url: https://memory.fraud-ops.olympus.internal
    case_api: /v1/stores/{store_name}/cases/{case_id}
    record_api: /v1/stores/{store_name}/records/{record_type}/{record_id}
  capabilities:
    views: [expanded, timeline, summary]
    record_types: [decision_record, evidence_bundle, ...]
  metadata:
    purpose: "Primary store for fraud case decisions"
    scope: workbench
```

### 2. Canonical Naming Convention

Each store has a unique canonical name:
```
{scope}.{store_type}.{qualifier}
```

Examples:
- `fraud-ops.enterprise-memory.primary`
- `tenant-acme.enterprise-memory.archive`

A single memory store **service** can host multiple stores, each with its own canonical name.

### 3. HTTPS-Based Retrieval (Read-Only)

CAF retrieves data via standardized HTTPS endpoints:

| Endpoint | Purpose |
|----------|---------|
| `GET /v1/stores/{name}/cases/{id}` | Retrieve case at various granularity |
| `GET /v1/stores/{name}/records/{type}/{id}` | Retrieve single record |
| `GET /v1/stores/{name}/capabilities` | Query store capabilities |
| `GET /health` | Health check |

**Write APIs are store-specific** — not part of this contract.

### 4. View-Based Granularity

Case retrieval supports multiple views:

| View | Description | Use Case |
|------|-------------|----------|
| **expanded** | All records with full data inline | Full case reconstruction |
| **timeline** | Chronological list with refs and summaries | Overview, navigation |
| **summary** | Counts and metadata only | Dashboards, quick stats |

Each record in the response includes a `self` URL for individual retrieval.

### 5. JWS-Signed Requests

CAF signs all requests using JSON Web Signature (JWS):

```
┌─────────────────────┐
│  CAF Control Plane  │
│                     │
│  1. Authorize user  │
│  2. Sign request    │
│  3. Include principal in JWS │
└─────────┬───────────┘
          │  X-CAF-Signature: <jws>
          ▼
┌─────────────────────┐
│    Memory Store     │
│                     │
│  1. Verify JWS      │
│  2. Log principal   │
│  3. Process request │
│  (NO authorization) │
└─────────────────────┘
```

- **CAF publishes public keys** at `/.well-known/jwks.json`
- **Stores verify signatures** — reject invalid/expired
- **Stores do NOT authorize principals** — CAF access layer handles that
- **Principal is logged** for audit, not for access control

### 6. Hypermedia Links

All responses include `_links` sections for navigation:

```json
{
  "record_type": "decision_record",
  "record_id": "...",
  "self": { "href": "https://.../.../decision_record/..." },
  "_links": {
    "case": { "href": "https://.../.../cases/..." },
    "evidence_bundle": { "href": "https://.../.../evidence_bundle/..." }
  }
}
```

CAF follows links rather than constructing URLs.

## Alternatives Considered

### Alternative 1: CAF Directly Queries Databases
CAF connects to store databases directly.

- **Pros**: Lower latency, fewer moving parts
- **Cons**: Couples CAF to storage internals, schema dependencies, credential management complexity

### Alternative 2: Message-Based Retrieval
Stores respond to messages on a queue.

- **Pros**: Async, decoupled
- **Cons**: Complex for request-response, harder to implement views and filtering

### Alternative 3: GraphQL Interface
Unified query language across stores.

- **Pros**: Flexible queries, single endpoint
- **Cons**: More complex implementation, harder to version, overkill for defined views

## Consequences

### Positive
- **Storage Independence**: Any storage backend can implement the contract
- **Hypermedia Navigation**: Self-describing APIs, clients don't hardcode URLs
- **Centralized Access Control**: CAF handles authorization once
- **Clear Capabilities**: Stores declare what they support
- **Multi-Store Services**: One service can host multiple stores

### Negative
- **HTTP Overhead**: Each retrieval is an HTTP call
- **View Limitations**: Fixed views may not cover all query patterns

### Neutral
- Stores must implement health endpoint for CAF monitoring
- Stores must implement JWKS verification

## Implementation Notes

### Store Implementation Checklist

1. Register via MemoryStore CRD
2. Implement JWKS verification for CAF signatures
3. Implement case retrieval (all three views)
4. Implement record retrieval with hypermedia links
5. Implement capabilities endpoint
6. Implement health endpoint
7. Support pagination for large cases
8. Generate human-readable summaries for timeline view

### CAF Implementation Checklist

1. Publish JWKS at well-known endpoint
2. Sign all requests to stores
3. Include principal in JWS payload
4. Implement store discovery from CRDs
5. Implement capability checking before requests
6. Follow hypermedia links for navigation

## Related Decisions

- [ADR-0029: CAF as Control Plane](./0029-caf-control-plane.md)
- [ADR-0052: CAF Record Type Taxonomy](./0052-caf-record-type-taxonomy.md)
- [ADR-0053: CAF Record ID and Traversal Conventions](./0053-caf-record-id-traversal.md)

