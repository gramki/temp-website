# Evidence Bundles

> **Status:** 🔴 Stub — Placeholder for expansion

Evidence Bundles capture the **complete context at decision time**—enabling reproduction, audit, and verification of decisions. CAF provides the **catalog and schema** for evidence bundles; the bundles themselves are stored in **Enterprise Memory**.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Preserve state of information when decision was made |
| **Contents** | Documents, data, model I/O, retrieval results |
| **Immutability** | Frozen at decision time |
| **Use Cases** | Audit, replay, dispute resolution |
| **Storage** | Enterprise Memory (via Memory Services) |
| **CAF Role** | Catalog, schema, policies, integrity verification |

---

## Why Evidence Bundles Matter

Without evidence bundles:
- Cannot prove what information was available at decision time
- Cannot reproduce the decision with original context
- Cannot defend against claims of unfair treatment
- Cannot distinguish between bad decision vs. bad data

---

## Evidence Bundle Contents

```yaml
evidence_bundle:
  # Identity
  id: uuid                         # Unique identifier (UUID v4)
  timestamp: datetime
  decision_record_id: uuid         # → DecisionRecord this evidence supports (1:1)
  context_snapshot_id: uuid        # → ContextSnapshot at decision time
  case_id: uuid                    # Universal binding ID (UUID v4, = hub request_id when Hub-originated)
  
  # Hub Metadata (optional - populated when captured within Hub context)
  hub_metadata:
    tenant_id: string              # Tenant identifier
    subscription_id: string        # Subscription within tenant
    workbench_id: string           # Workbench where decision occurred
    scenario_id: string            # Scenario governing this decision
    request_id: string             # Hub Request this decision belongs to
    parent_request_id: string      # Parent request if nested (optional)
  
  # Context Snapshot
  context:
    session_state: object       # Agent session state
    session_state_content_type:
      mime: string              # e.g., "application/vnd.olympus.seer.session-state.v1+json"
      schema: string
      schema_version: string
    agent_memory: object        # Agent memory snapshot
    agent_memory_content_type:
      mime: string              # e.g., "application/vnd.olympus.seer.agent-memory.v1+json"
      schema: string
      schema_version: string
    enterprise_memory: array    # Retrieved enterprise memory
    enterprise_memory_content_type:
      mime: string              # Items conform to this type
      schema: string
      schema_version: string
    enterprise_knowledge: array # Retrieved knowledge
    enterprise_knowledge_content_type:
      mime: string
      schema: string
      schema_version: string
  
  # Data References
  data:
    entity_snapshots: array     # Business entity states
    entity_snapshots_content_type:
      mime: string              # e.g., "application/vnd.olympus.caf.entity-snapshot.v1+json"
      schema: string
      schema_version: string
    documents: array            # Document references
    documents_content_type:
      mime: string
      schema: string
      schema_version: string
    external_data: array        # API responses, lookups
    external_data_content_type:
      mime: string              # May vary per item; this is default
      schema: string
      schema_version: string
  
  # Model I/O
  model:
    prompts: array              # LLM prompts sent
    prompts_content_type:
      mime: string              # e.g., "application/vnd.olympus.seer.llm-prompt.v1+json"
      schema: string
      schema_version: string
    completions: array          # LLM responses received
    completions_content_type:
      mime: string              # e.g., "application/vnd.olympus.seer.llm-completion.v1+json"
      schema: string
      schema_version: string
    embeddings: object          # Embedding inputs/outputs
    embeddings_content_type:
      mime: string
      schema: string
      schema_version: string
    predictions: array          # ML model predictions
    predictions_content_type:
      mime: string              # e.g., "application/vnd.olympus.seer.ml-prediction.v1+json"
      schema: string
      schema_version: string
  
  # Retrieval
  retrieval:
    queries: array              # RAG queries executed
    queries_content_type:
      mime: string
      schema: string
      schema_version: string
    results: array              # Retrieved chunks
    results_content_type:
      mime: string
      schema: string
      schema_version: string
    rankings: object            # Relevance rankings
    rankings_content_type:
      mime: string
      schema: string
      schema_version: string
  
  # Metadata
  metadata:
    bundle_version: string
    created_by: string
    storage_location: string
    checksum: string
```

---

## Capture Triggers

Evidence bundles are captured:

| Trigger | Description |
|---------|-------------|
| **Decision Point** | Every decision record gets an evidence bundle |
| **Exception** | Policy violations or overrides |
| **High-Stakes** | Decisions above certain thresholds |
| **Audit Flag** | Marked for potential audit |
| **Sampling** | Random sampling for quality assurance |

---

## CAF's Role

CAF provides the **control plane** for evidence bundles, not the storage:

| CAF Provides | Memory Services Provides |
|--------------|-------------------------|
| Schema definitions | Actual bundle storage |
| Capture policies (triggers) | Write operations |
| Catalog (metadata, indexes) | Read/query operations |
| Integrity verification | Storage tiering |
| Replay orchestration | Retention execution |

---

## Storage Tiers (Managed by Memory Services)

| Tier | Retention | Access | Use Case |
|------|-----------|--------|----------|
| **Hot** | 30 days | Fast | Active cases, recent decisions |
| **Warm** | 1 year | Moderate | Recent audit, disputes |
| **Cold** | 7+ years | Slow | Compliance archive |

---

## Reproducibility

Evidence bundles enable decision replay:

```
┌─────────────────────────────────────────────────────────────────┐
│                    REPLAY CAPABILITY                             │
│                                                                  │
│  1. Load evidence bundle from decision time                      │
│  2. Reconstruct context (memory, knowledge, data)               │
│  3. Re-execute decision logic                                    │
│  4. Compare: original decision vs. replayed decision             │
│  5. Explain any differences                                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Integrity Guarantees

| Guarantee | Implementation |
|-----------|----------------|
| **Immutability** | Write-once storage, no modifications |
| **Completeness** | All relevant context captured |
| **Authenticity** | Cryptographic checksums |
| **Provenance** | Chain of custody tracked |

---

## Privacy Considerations

| Consideration | Approach |
|---------------|----------|
| **PII** | Tokenized references, not raw PII |
| **Data Minimization** | Only decision-relevant data |
| **Retention** | Aligned with regulatory requirements |
| **Access Control** | Role-based access to bundles |

---

## API Operations

| Operation | Description |
|-----------|-------------|
| `capture` | Create evidence bundle for a decision |
| `retrieve` | Load evidence bundle by ID |
| `replay` | Reconstruct decision context |
| `verify` | Check integrity of bundle |
| `export` | Export for audit/compliance |

---

## Related Documentation

- [CAF Overview](./README.md)
- [Decision Records](./decision-records.md)
- [Explanation Service](./explanation-service.md)

---

*TODO: Detailed design — storage format, capture hooks, retention automation, integrity verification*

