# CAF Memory Store Catalog

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [CAF README](./README.md) | [Episodic Memory Store Contract](./episodic-memory-store/memory-store-contract.md)

---

## Overview

The **Memory Store Catalog** is the CAF service that provides **discovery and introspection of registered memory stores**. It serves as the authoritative registry of all memory stores available within a tenant/workbench scope.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Registration via CRD** | Stores are registered through Kubernetes CRDs, not API calls |
| **Discovery via API** | CAF exposes read-only APIs to discover and introspect stores |
| **Hierarchical scope** | Stores are scoped to tenant, subscription, or workbench |
| **Capability-aware** | Catalog exposes store capabilities for routing decisions |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        KUBERNETES CONTROL PLANE                          │
│                                                                          │
│   ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐   │
│   │  MemoryStore    │     │  MemoryStore    │     │  MemoryStore    │   │
│   │  CRD Instance   │     │  CRD Instance   │     │  CRD Instance   │   │
│   │  (episodic)     │     │  (semantic)     │     │  (procedural)   │   │
│   └────────┬────────┘     └────────┬────────┘     └────────┬────────┘   │
│            │                       │                       │            │
│            └───────────────────────┼───────────────────────┘            │
│                                    │                                     │
│                                    ▼                                     │
│                     ┌──────────────────────────────┐                     │
│                     │   CAF Memory Store Catalog   │                     │
│                     │        Controller            │                     │
│                     │   (watches CRD changes)      │                     │
│                     └──────────────┬───────────────┘                     │
│                                    │                                     │
└────────────────────────────────────┼─────────────────────────────────────┘
                                     │
                                     ▼
                      ┌──────────────────────────────┐
                      │   Memory Store Catalog API   │
                      │      (Discovery Service)     │
                      │                              │
                      │  GET /catalog/stores         │
                      │  GET /catalog/stores/{name}  │
                      │  GET /catalog/capabilities   │
                      └──────────────────────────────┘
```

---

## Discovery API

### List Memory Stores

```yaml
GET /v1/catalog/stores
  ?tenant_id={tenant_id}           # Required
  &subscription_id={subscription_id}  # Optional filter
  &workbench_id={workbench_id}     # Optional filter
  &memory_class={class}            # Optional: episodic | semantic | procedural | preference
  &status={status}                 # Optional: registered | healthy | degraded | offline
  &capability={capability}         # Optional: filter by capability

Response: 200 OK
{
  "stores": [
    {
      "canonical_name": "fraud-ops.enterprise-memory.primary",
      "display_name": "Fraud Operations - Primary Enterprise Memory",
      "memory_class": "episodic",
      "scope": {
        "tenant_id": "tenant-acme-bank",
        "subscription_id": "sub-fraud-premium",
        "workbench_id": "wb-fraud-ops-001"
      },
      "status": {
        "state": "healthy",
        "last_health_check": "2026-01-07T14:30:00Z"
      },
      "endpoints": {
        "base_url": "https://memory.fraud-ops.olympus.internal",
        "case_api": "/v1/stores/{store_name}/cases/{case_id}",
        "health": "/health"
      },
      "capabilities_summary": {
        "record_types": ["case_record", "decision_record", "evidence_bundle", ...],
        "views": ["expanded", "timeline", "summary"],
        "max_records_per_response": 500
      },
      "_links": {
        "self": "/v1/catalog/stores/fraud-ops.enterprise-memory.primary",
        "capabilities": "/v1/catalog/stores/fraud-ops.enterprise-memory.primary/capabilities",
        "health": "/v1/catalog/stores/fraud-ops.enterprise-memory.primary/health"
      }
    },
    ...
  ],
  "pagination": {
    "total": 12,
    "offset": 0,
    "limit": 50
  }
}
```

### Get Store Details

```yaml
GET /v1/catalog/stores/{canonical_name}

Response: 200 OK
{
  "canonical_name": "fraud-ops.enterprise-memory.primary",
  "display_name": "Fraud Operations - Primary Enterprise Memory",
  "host_service": "enterprise-memory-service",
  "store_type": "enterprise_memory",
  "memory_class": "episodic",
  
  "scope": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-fraud-premium",
    "workbench_id": "wb-fraud-ops-001"
  },
  
  "metadata": {
    "purpose": "Primary store for fraud case decisions, evidence, and outcomes",
    "data_classification": "cognitive",
    "retention_policy": "7-years",
    "created_at": "2025-09-01T00:00:00Z",
    "updated_at": "2026-01-07T10:00:00Z"
  },
  
  "endpoints": {
    "base_url": "https://memory.fraud-ops.olympus.internal",
    "case_api": "/v1/stores/{store_name}/cases/{case_id}",
    "record_api": "/v1/stores/{store_name}/records/{record_type}/{record_id}",
    "health": "/health",
    "capabilities": "/v1/stores/{store_name}/capabilities"
  },
  
  "status": {
    "state": "healthy",
    "last_health_check": "2026-01-07T14:30:00Z",
    "uptime_percentage": 99.95,
    "last_error": null
  },
  
  "writer_protocols": [
    {
      "protocol": "rest",
      "endpoint": "/v1/stores/{store_name}/records",
      "spec": "caf-store-rest-api-v1"
    }
  ],
  
  "_links": {
    "self": "/v1/catalog/stores/fraud-ops.enterprise-memory.primary",
    "capabilities": "/v1/catalog/stores/fraud-ops.enterprise-memory.primary/capabilities",
    "health": "/v1/catalog/stores/fraud-ops.enterprise-memory.primary/health",
    "records": "https://memory.fraud-ops.olympus.internal/v1/stores/fraud-ops.enterprise-memory.primary/records"
  }
}
```

### Get Store Capabilities

```yaml
GET /v1/catalog/stores/{canonical_name}/capabilities

Response: 200 OK
{
  "canonical_name": "fraud-ops.enterprise-memory.primary",
  "memory_class": "episodic",
  
  "capabilities": {
    "views": ["expanded", "timeline", "summary", "identifiers_only"],
    
    "record_types": [
      {
        "type": "case_record",
        "schema_ref": "olympus://schemas/caf/episodic/case-record/v1",
        "supports_create": true,
        "supports_update": true,
        "supports_delete": false
      },
      {
        "type": "decision_record",
        "schema_ref": "olympus://schemas/caf/episodic/decision-record/v1",
        "supports_create": true,
        "supports_update": false,
        "supports_delete": false
      },
      ...
    ],
    
    "features": {
      "pagination": true,
      "max_records_per_response": 500,
      "supports_time_range_filter": true,
      "supports_record_type_filter": true,
      "supports_full_text_search": false,
      "supports_semantic_search": true,
      "supports_case_spanning": false
    },
    
    "retention": {
      "default_retention_days": 2555,  # 7 years
      "supports_legal_hold": true,
      "supports_early_deletion": false
    },
    
    "authentication": {
      "method": "jws",
      "issuer": "caf.olympus.internal"
    }
  }
}
```

### Check Store Health

```yaml
GET /v1/catalog/stores/{canonical_name}/health

Response: 200 OK
{
  "canonical_name": "fraud-ops.enterprise-memory.primary",
  "status": "healthy",
  "checked_at": "2026-01-07T14:30:00Z",
  
  "checks": [
    {
      "check": "connectivity",
      "status": "pass",
      "latency_ms": 12
    },
    {
      "check": "authentication",
      "status": "pass"
    },
    {
      "check": "storage_capacity",
      "status": "pass",
      "details": {
        "used_percentage": 34.5,
        "threshold_percentage": 90
      }
    }
  ],
  
  "metrics": {
    "requests_per_minute": 245,
    "error_rate": 0.001,
    "avg_latency_ms": 45
  }
}
```

### List Capabilities (Across Stores)

```yaml
GET /v1/catalog/capabilities
  ?tenant_id={tenant_id}
  &memory_class={class}

Response: 200 OK
{
  "memory_classes": [
    {
      "class": "episodic",
      "stores_count": 3,
      "record_types": ["case_record", "decision_record", "evidence_bundle", ...],
      "stores": [
        {
          "canonical_name": "fraud-ops.enterprise-memory.primary",
          "status": "healthy"
        },
        ...
      ]
    },
    {
      "class": "semantic",
      "stores_count": 2,
      "record_types": ["hypothesis", "pattern_summary", "entity_belief", ...],
      "stores": [...]
    },
    ...
  ]
}
```

### Find Store for Record Type

```yaml
GET /v1/catalog/stores/for-record-type/{record_type}
  ?tenant_id={tenant_id}
  &workbench_id={workbench_id}

Response: 200 OK
{
  "record_type": "decision_record",
  "memory_class": "episodic",
  "matching_stores": [
    {
      "canonical_name": "fraud-ops.enterprise-memory.primary",
      "priority": 1,
      "status": "healthy",
      "write_endpoint": "https://memory.fraud-ops.olympus.internal/v1/stores/.../records"
    }
  ]
}
```

---

## Store Routing

CAF uses the catalog for **routing decisions** when writing or reading records:

```python
def route_record(record_type, workbench_id):
    # 1. Determine memory class from record type
    memory_class = get_memory_class(record_type)
    
    # 2. Find stores for workbench with that memory class
    stores = catalog.find_stores(
        workbench_id=workbench_id,
        memory_class=memory_class,
        status="healthy"
    )
    
    # 3. Select primary store (or apply routing rules)
    primary = select_primary(stores)
    
    return primary.write_endpoint
```

---

## CRD-Based Registration

Stores are registered via Kubernetes CRDs (see [Memory Store Contract](./episodic-memory-store/memory-store-contract.md)):

```yaml
apiVersion: olympus.hub/v1
kind: MemoryStore
metadata:
  name: fraud-ops-enterprise-memory
  namespace: workbench-fraud-ops
spec:
  canonical_name: "fraud-ops.enterprise-memory.primary"
  display_name: "Fraud Operations - Primary Enterprise Memory"
  memory_class: episodic
  # ... (full spec in memory-store-contract.md)
```

The CAF Memory Store Catalog controller watches these CRDs and:
1. Validates the registration
2. Performs initial health check
3. Updates the catalog index
4. Schedules periodic health checks

---

## Catalog Events

The catalog publishes events for store lifecycle:

| Event | Description |
|-------|-------------|
| `store.registered` | New store registered and available |
| `store.updated` | Store configuration changed |
| `store.deregistered` | Store removed from catalog |
| `store.healthy` | Store transitioned to healthy |
| `store.degraded` | Store performance degraded |
| `store.offline` | Store unreachable |

---

## Access Control

| Operation | Required Permission |
|-----------|---------------------|
| List stores | `caf:catalog:read` |
| Get store details | `caf:catalog:read` |
| Get capabilities | `caf:catalog:read` |
| Check health | `caf:catalog:read` |

Note: Registration (CRD creation) requires Kubernetes RBAC permissions.

---

## TODO

| Item | Description | Priority |
|------|-------------|----------|
| Define routing rules configuration | How to specify primary/secondary stores, routing policies | P1 |
| Define failover behavior | What happens when primary store is unavailable | P1 |
| Define multi-store writes | Should writes go to multiple stores? | P2 |
| Define catalog caching strategy | How long to cache catalog data | P2 |

---

## Related Documents

- [CAF README](./README.md) — Cognitive Audit Fabric overview
- [Memory Store Contract](./episodic-memory-store/memory-store-contract.md) — CRD specification
- [CAF Store REST API](./episodic-memory-store/caf-store-rest-api.md) — Write API specification

