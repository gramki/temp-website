# Hub Enterprise Memory

> **Status:** 🟡 Draft — Under active development

Hub Enterprise Memory captures the organization's **lived cognition over time**—what happened, what was decided, why, and how it influenced future behavior. This document describes Hub's concrete implementation of CAF-compliant enterprise memory stores.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Memory Types** | Decision Records, Outcome Records, Exception History, Handoff Context |
| **Scope** | Organization-wide |
| **Persistence** | Durable |
| **Purpose** | Institutional learning, auditability, cross-agent coordination |

---

## The Question Enterprise Memory Answers

> *"What did we experience and learn, and how did it shape our actions?"*

---

## Why Enterprise Memory Matters

In an agentic world, Enterprise Memory becomes the **institutional learning layer** that enables:

| Capability | Without Enterprise Memory |
|------------|---------------------------|
| **Auditability** | Cannot explain past decisions |
| **Cross-Agent Learning** | Agents don't learn from each other |
| **Human-Agent Collaboration** | No shared context for handoffs |
| **Institutional Continuity** | Organization forgets when agents change |

---

## Memory Categories

### Decision Records
What was decided and why:
- Decision made
- Decision rationale
- Evidence considered
- Alternatives evaluated
- Confidence level
- Accountable party

### Outcome Records
What happened after decisions:
- Decision outcome (success/failure)
- Actual vs. expected results
- Downstream effects
- Time to outcome

### Exception History
Overrides and exceptions granted:
- Original decision
- Override decision
- Override rationale
- Override authority
- Outcome of override

### Handoff Context
Prior agent/human actions on a case:
- Actions taken by previous participants
- Current state summary
- Open items and pending actions
- Relevant learnings

---

## Use Cases

| Use Case | How Enterprise Memory Helps |
|----------|----------------------------|
| **Audit & Compliance** | Full decision trail with rationale |
| **Cross-Agent Learning** | Patterns discovered by one agent available to all |
| **Human-Agent Handoffs** | Shared context for seamless transitions |
| **Postmortem Analysis** | Forensic trail for root cause analysis |
| **Precedent Recognition** | Similar situations trigger relevant history |
| **Model Improvement** | Real decisions as training data |

---

## Storage Model

```
┌─────────────────────────────────────────────────────────────────┐
│                 ENTERPRISE MEMORY STORE                          │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  MEMORY RECORD                           │    │
│  │                                                          │    │
│  │  tenant_id: string                                       │    │
│  │  record_id: string                                       │    │
│  │  record_type: enum (decision|outcome|exception|handoff)  │    │
│  │  entity_type: string (what entity this relates to)       │    │
│  │  entity_id: string                                       │    │
│  │  content: structured                                     │    │
│  │  embedding: vector (for semantic search)                 │    │
│  │  timestamp: datetime                                     │    │
│  │  actor: string (who created this record)                 │    │
│  │  actor_type: enum (human|agent)                          │    │
│  │  linked_records: array (related records)                 │    │
│  │  metadata: key-value                                     │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Retention & Archival

| Record Type | Default Retention | Archival |
|-------------|-------------------|----------|
| **Decision Records** | 7 years | Cold storage |
| **Outcome Records** | 7 years | Cold storage |
| **Exception History** | 10 years | Cold storage |
| **Handoff Context** | 1 year | Archive on case close |

---

## API Operations

| Operation | Description |
|-----------|-------------|
| `record` | Create an enterprise memory record |
| `query` | Query by entity, type, time range |
| `search` | Semantic search across records |
| `link` | Link related records |
| `promote` | Promote to Enterprise Knowledge |
| `explain` | Generate explanation from records |

---

## CAF Integration

Enterprise Memory integrates tightly with Cognitive Audit Fabric. **CAF is the control plane; Enterprise Memory is the storage.**

| Aspect | CAF Provides | Enterprise Memory Provides |
|--------|--------------|---------------------------|
| **Decision Records** | Catalog, schema, policies | Actual storage |
| **Evidence Bundles** | Catalog, linking rules | Actual storage |
| **Explanation Service** | Narrative generation | Source data for explanations |
| **Audit Trail** | Access control, indexing | Memory records that form the trail |

> **Key distinction:** CAF defines *how* memory is structured and accessed; Enterprise Memory stores the actual records.

---

## Promotion to Enterprise Knowledge

When patterns in Enterprise Memory become asserted truth:

```
Enterprise Memory (observed patterns)
        │
        ▼
Review & Validation (human oversight)
        │
        ▼
Enterprise Knowledge (asserted facts, policies)
```

---

## Implementation Architecture

### OpenSearch-Based Storage

Hub Enterprise Memory uses **OpenSearch** as the storage engine, providing:

| Capability | OpenSearch Feature |
|------------|-------------------|
| **Document storage** | JSON document store |
| **Semantic search** | k-NN plugin with dense vectors |
| **Structured queries** | Query DSL with filters |
| **Aggregations** | Analytics and histograms |
| **Time-series** | Date histograms, range queries |

### Index Structure

```yaml
# Index naming convention
indices:
  # Episodic memory (per record type)
  - "{tenant}_{workbench}_episodic_case_records"
  - "{tenant}_{workbench}_episodic_decision_records"
  - "{tenant}_{workbench}_episodic_evidence_bundles"
  - "{tenant}_{workbench}_episodic_context_snapshots"
  - "{tenant}_{workbench}_episodic_outcome_records"
  - "{tenant}_{workbench}_episodic_override_records"
  - "{tenant}_{workbench}_episodic_handoff_context"
  - "{tenant}_{workbench}_episodic_hypothesis_records"
  - "{tenant}_{workbench}_episodic_incident_timelines"
  
  # Semantic memory
  - "{tenant}_{workbench}_semantic_patterns"
  - "{tenant}_{workbench}_semantic_constraints"
  - "{tenant}_{workbench}_semantic_entity_beliefs"
  - "{tenant}_{workbench}_semantic_relationship_beliefs"
  
  # Procedural memory
  - "{tenant}_{workbench}_procedural_skills"
  - "{tenant}_{workbench}_procedural_procedures"
  
  # Preference memory
  - "{tenant}_{workbench}_preference_user"
  - "{tenant}_{workbench}_preference_agent"
```

### Embedding Configuration

```yaml
embedding_config:
  model: "olympus-embed-v2"
  dimension: 1024
  
  # Per-record-type embedding sources
  embedding_sources:
    decision_record:
      fields: ["action", "rationale.summary", "rationale.factors_considered"]
      weight_strategy: "field_importance"
    
    case_record:
      fields: ["summary", "entity_type", "resolution.outcome"]
    
    handoff_context:
      fields: ["current_state.summary", "current_state.key_facts", "recommendations.suggested_next_steps"]
    
    pattern_summary:
      fields: ["description", "conditions", "implications"]
```

---

## Write Path (via Signal Exchange)

**Critical Design Decision:** No Hub agent or application directly writes to Enterprise Memory stores. All writes flow through Signal Exchange.

### Write Flow

```
Hub Application/Agent
        │
        │ Adds memory_records to REQUEST_UPDATE
        ▼
Signal Exchange
        │
        │ Validates, enriches, routes
        ▼
Atropos Topic (per memory store)
        │
        │ Async consumption
        ▼
Memory Store Writer Service
        │
        │ Schema validation, embedding generation, indexing
        ▼
OpenSearch
```

See [Signal Exchange - Memory Record Routing](../signal-exchange/memory-record-routing.md) for full specification.

### Why No Direct Writes?

| Reason | Benefit |
|--------|---------|
| **Centralized auditing** | All writes logged through Signal Exchange |
| **Request context binding** | Records automatically linked to Request |
| **Async processing** | Application latency decoupled from storage |
| **Deduplication** | Signal Exchange handles idempotency |
| **Schema enforcement** | Consistent validation before storage |

---

## Read Path (via Memory Access Tools)

Applications and agents read from Enterprise Memory using **Memory Access Tools**:

| Tool | Purpose |
|------|---------|
| `memory.search_precedent` | Semantic search for similar cases |
| `memory.get_case_history` | Full case timeline retrieval |
| `memory.query_decisions` | Structured decision queries |
| `memory.get_handoff_context` | Handoff context for case |
| `memory.search_patterns` | Semantic pattern search |
| `memory.get_entity_beliefs` | Entity belief retrieval |

See [Memory Access Tools](./memory-access-tools.md) for tool specifications.

### Read Flow

```
Hub Application/Agent
        │
        │ Invokes memory access tool
        ▼
Memory Tool Executor
        │
        │ Authorization, query building
        ▼
Memory Query Service
        │
        │ Embedding generation (if semantic), query execution
        ▼
OpenSearch
        │
        │ Results
        ▼
Response Formatting
        │
        │ Formatted for agent consumption
        ▼
Hub Application/Agent
```

---

## Retention and Deletion

### Retention Policies

| Memory Class | Default Retention | Legal Hold |
|--------------|-------------------|------------|
| **Episodic** | 7 years | ✅ Supported |
| **Semantic** | 5 years | ✅ Supported |
| **Procedural** | 3 years | ⚠️ Limited |
| **Preference** | 2 years | ❌ Not applicable |

### PII Prohibition

> **Critical Constraint:** No Episodic memory record may contain PII.

- Records use entity references (e.g., `entity_id: cust-abc123`) instead of PII
- PII is resolved at query time via separate PII-enabled tools
- Write-time validation rejects records with detected PII

See [Retention and PII Policy](./retention-and-pii-policy.md) for full details.

---

## Related Documentation

- [Memory Services Overview](./README.md)
- [Memory Query API](./memory-query-api.md)
- [Memory Access Tools](./memory-access-tools.md)
- [Retention and PII Policy](./retention-and-pii-policy.md)
- [Hub Agent Memory](./hub-agent-memory.md)
- [Cognitive Audit Fabric](../cognitive-audit-fabric/README.md)
- [Signal Exchange - Memory Record Routing](../signal-exchange/memory-record-routing.md)
- [Knowledge Services](../knowledge-services/README.md)

---

*TODO: Detailed design — index lifecycle management, embedding model training, performance tuning, cross-workbench federation*

