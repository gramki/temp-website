# 5.4 Knowledge Services (RAG)

Knowledge Services provide Enterprise Knowledge retrieval capabilities for context assembly. This is Seer's integration with Hub's Knowledge Bank and ETSL for RAG (Retrieval-Augmented Generation) operations.

## What Knowledge Services Provide

Knowledge Services answer: **"What does the organization say is true, correct, or required?"**

| Capability | Description |
|------------|-------------|
| **Semantic search** | Vector similarity across documents |
| **Hybrid retrieval** | Combine semantic + keyword + filters |
| **Versioning** | Retrieve from specific document versions |
| **Provenance** | Track source, version, and retrieval metadata |
| **Access control** | Workbench-scoped document access |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE SERVICES                        │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │               RETRIEVAL API                        │    │
│   │   • Query parsing    • Result ranking              │    │
│   │   • Filter handling  • Provenance attachment       │    │
│   └────────────────────────┬──────────────────────────┘    │
│                            │                                │
│         ┌──────────────────┴──────────────────┐             │
│         ▼                                     ▼             │
│   ┌───────────────────┐         ┌───────────────────┐      │
│   │   KNOWLEDGE BANK  │         │       ETSL        │      │
│   │                   │         │                   │      │
│   │   • Documents     │         │   • Facts         │      │
│   │   • Policies      │         │   • Rules         │      │
│   │   • Procedures    │         │   • Constraints   │      │
│   │   • Guides        │         │   • Time-aware    │      │
│   │                   │         │                   │      │
│   │   Vector index    │         │   Structured      │      │
│   │   (embeddings)    │         │   queries         │      │
│   └───────────────────┘         └───────────────────┘      │
│                                                              │
│   Storage: Olympus Europa (OpenSearch) + Vector index        │
└─────────────────────────────────────────────────────────────┘
```

## Retrieval Patterns

### Pattern 1: Semantic Search

Find documents by meaning:

```python
results = await knowledge_service.search(
    workbench="dispute-ops-prod",
    query="What is the refund eligibility policy?",
    filters={
        "document_type": ["policy", "procedure"]
    },
    max_chunks=5
)

# Returns ranked chunks with scores
for chunk in results:
    print(f"Score: {chunk.score}, Doc: {chunk.document_id}")
    print(f"Content: {chunk.content[:200]}...")
```

### Pattern 2: Hybrid Search

Combine semantic + keyword + filters:

```python
results = await knowledge_service.hybrid_search(
    workbench="dispute-ops-prod",
    semantic_query="refund eligibility requirements",
    keyword_query="60 days filing deadline",
    filters={
        "document_type": "policy",
        "effective_date": {"lte": "2026-01-10"}
    },
    weights={
        "semantic": 0.7,
        "keyword": 0.3
    }
)
```

### Pattern 3: Specific Document Retrieval

Get exact document or section:

```python
document = await knowledge_service.get_document(
    document_id="dispute-policy-v3.2",
    sections=["eligibility", "timelines"]
)
```

### Pattern 4: Point-in-Time Retrieval

Retrieve knowledge as it was at a specific time:

```python
# What was the policy when this decision was made?
historical_policy = await knowledge_service.search(
    workbench="dispute-ops-prod",
    query="refund eligibility",
    as_of="2025-12-15T10:00:00Z"  # Point in time
)
```

## ETSL Integration

ETSL provides structured, time-aware knowledge:

```python
# Query ETSL for applicable rules
rules = await etsl.query(
    workbench="dispute-ops-prod",
    query={
        "type": "rule",
        "applies_to": "refund_decision",
        "effective_at": "2026-01-10"
    }
)

# Returns structured rules
for rule in rules:
    print(f"Rule: {rule.statement}")
    print(f"Authority: {rule.authority}")
    print(f"Effective: {rule.effective_from} to {rule.effective_to}")
```

### Why ETSL Matters

| Knowledge Bank | ETSL |
|----------------|------|
| Document-based | Structured assertions |
| Semantic search | Exact matching |
| Unstructured text | Typed facts and rules |
| Point-in-time via versioning | Native temporal validity |

Use cases:
- **Knowledge Bank:** Policy documents, procedures, guides
- **ETSL:** Business rules, constraints, temporal facts

## Provenance Tracking

Every retrieval includes provenance:

```yaml
retrieval_result:
  chunk_id: "kb-chunk-123"
  content: "Disputes must be filed within 60 days of the transaction date..."
  
  provenance:
    document_id: "dispute-policy-v3.2"
    document_title: "Customer Dispute Policy"
    version: "3.2"
    effective_date: "2025-01-01"
    section: "Filing Requirements"
    page: 12
    paragraph: 3
    
  retrieval_metadata:
    query: "refund eligibility policy"
    score: 0.92
    method: hybrid
    retrieved_at: "2026-01-10T14:30:00Z"
    workbench: "dispute-ops-prod"
```

## Context Frame Integration

Knowledge results are formatted for context frames:

```yaml
context_frame:
  ground_truth_facts:
    - source: knowledge_bank
      content: "Disputes must be filed within 60 days of the transaction date"
      provenance:
        document: dispute-policy-v3.2
        section: Filing Requirements
        version: 3.2
        retrieved_at: 2026-01-10T14:30:00Z
      confidence: 0.92
      
    - source: etsl
      content: "Max refund without approval: $500"
      provenance:
        rule_id: refund-limit-rule-001
        authority: finance-policy-committee
        effective_from: 2025-01-01
      confidence: 1.0  # Exact match from ETSL
```

## Access Control

Knowledge access is workbench-scoped:

```yaml
access_policy:
  workbench: dispute-ops-prod
  
  document_access:
    - document_type: policy
      access: read
    - document_type: internal_procedure
      access: read
    - document_type: confidential
      access: denied
      
  on_denial:
    log_to: caf
    return_error: "Document access denied"
```

## Caching and Freshness

Knowledge retrieval balances freshness and performance:

```yaml
cache_policy:
  knowledge_bank:
    ttl: 5m  # Cache for 5 minutes
    invalidate_on: document_update
    
  etsl:
    ttl: 1m  # Shorter for time-sensitive rules
    invalidate_on: rule_update
    
  point_in_time:
    ttl: 24h  # Historical queries can be cached longer
```

---

**References:**
*   `olympus-hub-docs/04-subsystems/knowledge-services/README.md`
*   `olympus-hub-docs/pontus/etsl/`
*   `olympus-seer-docs/why-seer/part-2-how-seer-solves/04-memory-knowledge-audit-in-seer/04-2-enterprise-knowledge.md`
