# Enterprise Memory Query API

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Parent**: [Enterprise Memory](./README.md)  
> **Related**: [Memory Services](../README.md) | [CAF Store REST API](../../cognitive-audit-fabric/episodic-memory-store/caf-store-rest-api.md) | [Access Tools](./access-tools.md)

---

## Overview

The **Memory Query API** provides the read interface for Hub Memory Stores. This API enables applications and agents to query enterprise memory for precedents, case histories, decisions, and semantic patterns.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Read-Only** | This API is exclusively for reads; writes flow through Signal Exchange |
| **Semantic + Filter** | Supports both semantic (vector) search and structured filtering |
| **CAF-Compliant** | Implements CAF read protocols and schema expectations |
| **Workbench-Scoped** | All queries are scoped to workbench with RBAC enforcement |
| **Pagination** | All list/search endpoints support pagination |
| **Tool-Oriented** | Designed for consumption by Memory Access Tools |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          MEMORY QUERY SERVICE                                 │
│                                                                               │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                         QUERY PROCESSING                                 │ │
│  │                                                                          │ │
│  │   Query Request                                                          │ │
│  │        │                                                                 │ │
│  │        ▼                                                                 │ │
│  │   ┌────────────────┐                                                     │ │
│  │   │  Authorization │ ─► Validate workbench access, RBAC permissions      │ │
│  │   └───────┬────────┘                                                     │ │
│  │           │                                                              │ │
│  │           ▼                                                              │ │
│  │   ┌────────────────┐                                                     │ │
│  │   │  Query Parser  │ ─► Parse filters, semantic query, pagination        │ │
│  │   └───────┬────────┘                                                     │ │
│  │           │                                                              │ │
│  │           ▼                                                              │ │
│  │   ┌────────────────┐     ┌─────────────────────┐                         │ │
│  │   │ Query Planner  │ ──► │  Embedding Service  │ (for semantic queries)  │ │
│  │   └───────┬────────┘     └─────────────────────┘                         │ │
│  │           │                                                              │ │
│  │           ▼                                                              │ │
│  │   ┌────────────────┐                                                     │ │
│  │   │ OpenSearch     │ ─► Execute hybrid query (k-NN + filters)            │ │
│  │   │ Query Engine   │                                                     │ │
│  │   └───────┬────────┘                                                     │ │
│  │           │                                                              │ │
│  │           ▼                                                              │ │
│  │   ┌────────────────┐                                                     │ │
│  │   │ Response       │ ─► Format, paginate, add hypermedia links           │ │
│  │   │ Formatter      │                                                     │ │
│  │   └────────────────┘                                                     │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Base URL

```
https://{memory-host}/v1/memory/{workbench_id}
```

---

## Authentication & Authorization

### Authentication

All requests require a valid Hub JWT token:

```
Authorization: Bearer <hub-jwt-token>
```

### Authorization

| Permission | Description |
|------------|-------------|
| `memory:read` | Read access to memory stores in workbench |
| `memory:search` | Execute semantic search queries |
| `memory:explain` | Access explanation generation |
| `memory:admin` | Full access including retention management |

### Workbench Scoping

All queries are automatically scoped to the authenticated workbench. Cross-workbench queries are not permitted (each workbench has isolated memory stores).

---

## Query Endpoints

### Search Precedent

Find similar past cases based on semantic similarity. This is the primary tool for precedent retrieval.

```yaml
POST /v1/memory/{workbench_id}/search/precedent

Request:
{
  "query": {
    # Natural language query describing the situation
    "text": "Customer claims unauthorized international wire transfer of $50,000",
    
    # OR structured query components
    "structured": {
      "entity_type": "dispute",
      "amount_range": { "min": 40000, "max": 60000 },
      "transaction_types": ["wire_transfer", "international"]
    }
  },
  
  "filters": {
    # Restrict to specific memory classes
    "memory_classes": ["episodic"],
    
    # Restrict to specific record types
    "record_types": ["case_record", "decision_record"],
    
    # Time range
    "time_range": {
      "from": "2025-01-01T00:00:00Z",
      "to": "2026-01-07T23:59:59Z"
    },
    
    # Only cases with specific outcomes
    "outcome_types": ["approved", "denied"],
    
    # Scenario filter
    "scenario_ids": ["fraud-dispute-resolution"]
  },
  
  "options": {
    # Number of results
    "limit": 10,
    
    # Minimum similarity threshold (0-1)
    "min_similarity": 0.7,
    
    # Include related records
    "expand": ["decisions", "outcomes", "evidence"],
    
    # Response format
    "format": "detailed"  # summary | detailed | full
  }
}

Response: 200 OK
{
  "results": [
    {
      "case_id": "550e8400-e29b-41d4-a716-446655440000",
      "similarity_score": 0.89,
      
      "case_summary": {
        "title": "Unauthorized International Wire - Premium Customer",
        "status": "resolved",
        "resolution": "approved",
        "resolved_at": "2025-11-15T14:30:00Z",
        "entity_type": "dispute",
        "entity_id": "disp-78901"
      },
      
      "relevance_factors": [
        "Similar transaction amount ($48,500)",
        "Same transaction type (international wire)",
        "Similar customer segment (premium)"
      ],
      
      "key_decisions": [
        {
          "decision_id": "dec-12345",
          "action": "approve_full_refund",
          "confidence": 0.92,
          "rationale_summary": "Pattern matched known fraud ring, customer history clean"
        }
      ],
      
      "outcome": {
        "outcome_id": "out-67890",
        "actual_outcome": "customer_satisfied",
        "variance": "none",
        "learnings": ["Fast resolution improves NPS for premium segment"]
      },
      
      "_links": {
        "self": "/v1/memory/.../cases/550e8400-...",
        "full_case": "/v1/memory/.../cases/550e8400-.../full",
        "decisions": "/v1/memory/.../cases/550e8400-.../decisions",
        "timeline": "/v1/memory/.../cases/550e8400-.../timeline"
      }
    },
    // ... more results
  ],
  
  "pagination": {
    "total_matches": 47,
    "returned": 10,
    "offset": 0,
    "has_more": true,
    "next_cursor": "eyJvZmZzZXQiOjEwfQ=="
  },
  
  "query_metadata": {
    "query_id": "qry-abc123",
    "executed_at": "2026-01-07T15:30:00Z",
    "latency_ms": 145,
    "embedding_model": "olympus-embed-v2"
  }
}
```

### Get Case History

Retrieve complete case timeline with all related records.

```yaml
GET /v1/memory/{workbench_id}/cases/{case_id}
  ?expand=decisions,evidence,outcomes,overrides,handoffs
  &format=timeline

Response: 200 OK
{
  "case": {
    "case_id": "550e8400-e29b-41d4-a716-446655440000",
    "content_hash": "sha256:abc123...",
    "status": "resolved",
    "created_at": "2025-11-10T09:00:00Z",
    "resolved_at": "2025-11-15T14:30:00Z",
    
    "hub_metadata": {
      "tenant_id": "tenant-acme-bank",
      "subscription_id": "sub-fraud-premium",
      "workbench_id": "wb-fraud-ops",
      "scenario_id": "fraud-dispute-resolution",
      "request_id": "req-12345"
    },
    
    "entity_binding": {
      "entity_type": "dispute",
      "entity_id": "disp-78901"
    },
    
    "actors": [
      { "actor_id": "agent-triage-001", "actor_type": "agent", "role": "initial_triage" },
      { "actor_id": "user-jane", "actor_type": "human", "role": "case_analyst" }
    ],
    
    "resolution": {
      "outcome": "approved",
      "resolution_type": "full_refund",
      "resolved_by": { "actor_id": "user-jane", "actor_type": "human" }
    }
  },
  
  "timeline": [
    {
      "timestamp": "2025-11-10T09:00:00Z",
      "event_type": "case_created",
      "record_type": "case_record",
      "record_id": "550e8400-...",
      "summary": "Case opened for dispute DISP-78901"
    },
    {
      "timestamp": "2025-11-10T09:05:00Z",
      "event_type": "decision_made",
      "record_type": "decision_record",
      "record_id": "dec-11111",
      "summary": "Initial classification: High-value international wire fraud",
      "actor": { "actor_id": "agent-triage-001", "actor_type": "agent" }
    },
    {
      "timestamp": "2025-11-10T09:10:00Z",
      "event_type": "handoff",
      "record_type": "handoff_context",
      "record_id": "hoff-22222",
      "summary": "Escalated to human analyst",
      "from_actor": "agent-triage-001",
      "to_actor": "user-jane"
    },
    // ... more timeline events
  ],
  
  "expanded": {
    "decisions": [ /* full decision records */ ],
    "evidence": [ /* full evidence bundles */ ],
    "outcomes": [ /* outcome records */ ],
    "handoffs": [ /* handoff context records */ ]
  },
  
  "_links": {
    "self": "/v1/memory/.../cases/550e8400-...",
    "decisions": "/v1/memory/.../cases/550e8400-.../decisions",
    "evidence": "/v1/memory/.../cases/550e8400-.../evidence",
    "timeline": "/v1/memory/.../cases/550e8400-.../timeline"
  }
}
```

### Query Decisions

Query decision records with structured filters.

```yaml
POST /v1/memory/{workbench_id}/query/decisions

Request:
{
  "filters": {
    "time_range": {
      "from": "2025-06-01T00:00:00Z",
      "to": "2026-01-07T23:59:59Z"
    },
    
    "decision_types": ["classification", "approval", "escalation"],
    
    "confidence_range": {
      "min": 0.8,
      "max": 1.0
    },
    
    "actor_types": ["agent"],
    
    "scenario_ids": ["fraud-dispute-resolution"],
    
    "has_override": false,
    
    # Semantic filter (optional)
    "rationale_contains": "fraud pattern matching"
  },
  
  "aggregations": {
    "by_decision_type": true,
    "by_actor": true,
    "by_outcome": true,
    "confidence_histogram": true
  },
  
  "options": {
    "limit": 50,
    "offset": 0,
    "sort": [
      { "field": "timestamp", "order": "desc" }
    ],
    "format": "summary"
  }
}

Response: 200 OK
{
  "results": [
    {
      "decision_id": "dec-99999",
      "case_id": "550e8400-...",
      "timestamp": "2026-01-05T11:30:00Z",
      "decision_type": "approval",
      "action": "approve_partial_refund",
      "confidence": 0.87,
      "actor": { "actor_id": "agent-resolver-003", "actor_type": "agent" },
      "rationale_summary": "Partial liability based on customer history",
      "_links": {
        "self": "/v1/memory/.../decisions/dec-99999",
        "case": "/v1/memory/.../cases/550e8400-...",
        "evidence": "/v1/memory/.../decisions/dec-99999/evidence"
      }
    },
    // ... more results
  ],
  
  "aggregations": {
    "by_decision_type": {
      "classification": 120,
      "approval": 85,
      "escalation": 45
    },
    "by_actor": {
      "agent-triage-001": 150,
      "agent-resolver-003": 75,
      "user-jane": 25
    },
    "confidence_histogram": {
      "0.8-0.85": 40,
      "0.85-0.9": 80,
      "0.9-0.95": 90,
      "0.95-1.0": 40
    }
  },
  
  "pagination": {
    "total_matches": 250,
    "returned": 50,
    "offset": 0,
    "has_more": true
  }
}
```

### Get Handoff Context

Retrieve handoff context for a case or specific handoff.

```yaml
GET /v1/memory/{workbench_id}/cases/{case_id}/handoffs
  ?latest=true

Response: 200 OK
{
  "handoffs": [
    {
      "handoff_id": "hoff-55555",
      "case_id": "550e8400-...",
      "timestamp": "2026-01-07T10:00:00Z",
      
      "from_agent": {
        "actor_id": "agent-triage-001",
        "actor_type": "agent",
        "role": "triage_agent"
      },
      "to_agent": {
        "actor_id": "user-jane",
        "actor_type": "human",
        "role": "case_analyst"
      },
      "handoff_reason": "escalation",
      
      "current_state": {
        "status": "pending_review",
        "summary": "High-value wire transfer flagged as suspicious. Initial pattern matching suggests known fraud ring. Customer history is clean.",
        "key_facts": [
          "Transaction amount: $48,500",
          "Destination: overseas account (first-time recipient)",
          "Customer tenure: 8 years, no prior disputes",
          "Pattern match: 87% confidence with fraud ring #FR-2025-0034"
        ],
        "working_hypothesis": "Likely unauthorized transaction based on pattern match"
      },
      
      "actions_taken": [
        "Retrieved transaction details from core banking",
        "Ran pattern matching against known fraud rings",
        "Verified customer identity and history",
        "Placed temporary hold on outbound wires"
      ],
      
      "open_items": {
        "pending_actions": [
          "Contact customer to verify transaction intent",
          "Request supporting documentation"
        ],
        "unanswered_questions": [
          "Did customer authorize the beneficiary?",
          "Has customer traveled internationally recently?"
        ]
      },
      
      "recommendations": {
        "suggested_next_steps": [
          "Phone verification with customer (high priority)",
          "If customer denies authorization, initiate full refund",
          "File SAR if fraud confirmed"
        ],
        "areas_of_concern": [
          "Customer may be under duress - watch for coached responses",
          "Potential for account takeover - verify through secondary channel"
        ],
        "relevant_precedent": [
          {
            "case_id": "case-44444",
            "similarity": 0.91,
            "summary": "Similar pattern, confirmed fraud, full refund issued"
          }
        ]
      },
      
      "sla_status": {
        "deadline": "2026-01-08T09:00:00Z",
        "time_remaining": "PT23H",
        "sla_risk": "on_track"
      }
    }
  ],
  
  "_links": {
    "self": "/v1/memory/.../cases/550e8400-.../handoffs",
    "case": "/v1/memory/.../cases/550e8400-..."
  }
}
```

### Search Semantic Patterns

Query semantic memory for patterns and hypotheses.

```yaml
POST /v1/memory/{workbench_id}/search/patterns

Request:
{
  "query": {
    "text": "What patterns have we observed for weekend wire transfer disputes?"
  },
  
  "filters": {
    "memory_class": "semantic",
    "record_types": ["hypothesis", "pattern_summary", "learned_constraint"],
    "min_confidence": 0.75,
    "min_evidence_count": 5,
    "scope": {
      "scenario_ids": ["fraud-dispute-resolution"]
    }
  },
  
  "options": {
    "limit": 20,
    "include_evidence_summary": true
  }
}

Response: 200 OK
{
  "patterns": [
    {
      "pattern_id": "pat-77777",
      "record_type": "pattern_summary",
      "confidence": 0.82,
      "evidence_count": 34,
      
      "pattern": {
        "description": "Weekend wire transfers to new overseas recipients have 3.2x higher fraud rate",
        "conditions": [
          "Transaction type: international wire",
          "Time: Saturday or Sunday",
          "Recipient: first-time (no prior transactions)"
        ],
        "correlation": {
          "fraud_rate_normal": 0.023,
          "fraud_rate_pattern": 0.074,
          "multiplier": 3.2
        }
      },
      
      "applicability": {
        "scope": "fraud-dispute-resolution",
        "entity_types": ["wire_transfer", "dispute"],
        "effective_from": "2025-09-01",
        "last_validated": "2026-01-05"
      },
      
      "evidence_summary": {
        "supporting_cases": 28,
        "contradicting_cases": 6,
        "timespan": "2025-09-01 to 2026-01-05"
      },
      
      "_links": {
        "self": "/v1/memory/.../patterns/pat-77777",
        "evidence": "/v1/memory/.../patterns/pat-77777/evidence"
      }
    }
  ],
  
  "pagination": {
    "total_matches": 12,
    "returned": 12,
    "has_more": false
  }
}
```

---

## Indexing & Search Implementation

### Index Structure (OpenSearch)

Hub Memory Stores use OpenSearch with the following index configuration:

```yaml
# Episodic Memory Index Template
episodic_memory_template:
  index_patterns:
    - "{tenant}_{workbench}_episodic_*"
  
  settings:
    number_of_shards: 3
    number_of_replicas: 1
    
    analysis:
      analyzer:
        caf_text_analyzer:
          type: custom
          tokenizer: standard
          filter:
            - lowercase
            - stop
            - snowball
  
  mappings:
    properties:
      # Core fields
      record_id:
        type: keyword
      record_type:
        type: keyword
      case_id:
        type: keyword
      content_hash:
        type: keyword
      timestamp:
        type: date
      
      # Hub metadata
      hub_metadata:
        properties:
          tenant_id: { type: keyword }
          subscription_id: { type: keyword }
          workbench_id: { type: keyword }
          scenario_id: { type: keyword }
          request_id: { type: keyword }
      
      # Entity binding
      entity_type:
        type: keyword
      entity_id:
        type: keyword
      
      # Semantic search vector
      embedding:
        type: knn_vector
        dimension: 1024
        method:
          name: hnsw
          space_type: cosinesimil
          engine: nmslib
          parameters:
            ef_construction: 256
            m: 16
      
      # Text fields for full-text search
      summary:
        type: text
        analyzer: caf_text_analyzer
      rationale:
        type: text
        analyzer: caf_text_analyzer
      
      # Structured content (stored, not indexed for full-text)
      data:
        type: object
        enabled: false
```

### Embedding Generation

Semantic search uses embeddings generated at write time:

```yaml
embedding_config:
  model: "olympus-embed-v2"
  dimension: 1024
  
  # Fields used to generate embedding
  embedding_sources:
    case_record:
      - summary
      - entity_type
    decision_record:
      - action
      - rationale
      - factors_considered
    evidence_bundle:
      - summary
      - key_evidence
    handoff_context:
      - current_state.summary
      - current_state.key_facts
      - recommendations.suggested_next_steps
```

### Hybrid Query Execution

The Memory Query Service executes hybrid queries combining semantic and filter-based search:

```python
def execute_precedent_search(query: PrecedentQuery) -> SearchResults:
    # 1. Generate embedding for semantic query
    if query.text:
        query_embedding = embedding_service.embed(query.text)
    
    # 2. Build OpenSearch query
    os_query = {
        "size": query.limit,
        "query": {
            "bool": {
                "must": [],
                "filter": []
            }
        }
    }
    
    # 3. Add semantic similarity (k-NN)
    if query_embedding:
        os_query["query"]["bool"]["must"].append({
            "knn": {
                "embedding": {
                    "vector": query_embedding,
                    "k": query.limit * 2  # Over-fetch for filtering
                }
            }
        })
    
    # 4. Add structured filters
    if query.filters.record_types:
        os_query["query"]["bool"]["filter"].append({
            "terms": {"record_type": query.filters.record_types}
        })
    
    if query.filters.time_range:
        os_query["query"]["bool"]["filter"].append({
            "range": {
                "timestamp": {
                    "gte": query.filters.time_range.from_,
                    "lte": query.filters.time_range.to
                }
            }
        })
    
    if query.filters.scenario_ids:
        os_query["query"]["bool"]["filter"].append({
            "terms": {"hub_metadata.scenario_id": query.filters.scenario_ids}
        })
    
    # 5. Execute and format results
    results = opensearch_client.search(index=workbench_index, body=os_query)
    return format_precedent_results(results, query.min_similarity)
```

### Similarity Scoring

Semantic similarity is calculated using cosine similarity on embeddings:

| Similarity Score | Interpretation |
|------------------|----------------|
| 0.90 - 1.00 | Very high similarity (near identical context) |
| 0.80 - 0.89 | High similarity (strong precedent) |
| 0.70 - 0.79 | Moderate similarity (relevant precedent) |
| 0.60 - 0.69 | Low similarity (tangentially related) |
| < 0.60 | Minimal similarity (likely not useful) |

---

## Response Formats

### Summary Format

Lightweight response for list views:

```json
{
  "case_id": "550e8400-...",
  "summary": "High-value wire fraud, resolved with full refund",
  "status": "resolved",
  "timestamp": "2025-11-10T09:00:00Z",
  "_links": { "self": "..." }
}
```

### Detailed Format

Standard response with key fields expanded:

```json
{
  "case_id": "550e8400-...",
  "summary": "...",
  "status": "resolved",
  "key_decisions": [...],
  "outcome": {...},
  "timeline_summary": [...],
  "_links": {...}
}
```

### Full Format

Complete record with all fields:

```json
{
  // All fields from CAF record schema
  // Plus related records if expanded
}
```

---

## Error Codes

| HTTP Status | Code | Description |
|-------------|------|-------------|
| 400 | `INVALID_QUERY` | Query syntax error or missing required fields |
| 400 | `INVALID_FILTERS` | Filter values out of range or incompatible |
| 401 | `UNAUTHORIZED` | Missing or invalid authentication |
| 403 | `FORBIDDEN` | Insufficient permissions for workbench |
| 404 | `CASE_NOT_FOUND` | Case ID not found in memory store |
| 404 | `RECORD_NOT_FOUND` | Specific record not found |
| 422 | `EMBEDDING_FAILED` | Failed to generate query embedding |
| 429 | `RATE_LIMITED` | Query rate limit exceeded |
| 503 | `STORE_UNAVAILABLE` | Memory store temporarily unavailable |

---

## Rate Limits & Quotas

| Operation | Default Limit | Scope |
|-----------|---------------|-------|
| Precedent search | 100/min | Per workbench |
| Case retrieval | 500/min | Per workbench |
| Decision queries | 200/min | Per workbench |
| Pattern search | 100/min | Per workbench |
| Batch queries | 20/min | Per workbench |

---

## Caching

The Memory Query Service implements caching at multiple levels:

| Cache Level | TTL | Invalidation |
|-------------|-----|--------------|
| **Query embeddings** | 1 hour | Query hash |
| **Case summaries** | 5 minutes | Case update |
| **Aggregation results** | 15 minutes | Workbench update |
| **Pattern index** | 30 minutes | Semantic memory update |

---

## Related Documents

- [Memory Services README](./README.md) — Architecture overview
- [Access Tools](./access-tools.md) — Tool specifications
- [CAF Store REST API](../../cognitive-audit-fabric/episodic-memory-store/caf-store-rest-api.md) — Write API
- [Enterprise Memory Overview](./README.md) — Storage implementation

---

*TODO: Query optimization guidelines, performance tuning, cross-memory-class queries*

