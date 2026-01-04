# Evidence Bundles

> **Status:** 🔴 Stub — Placeholder for expansion

Evidence Bundles capture the **complete context at decision time**—enabling reproduction, audit, and verification of decisions.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Preserve state of information when decision was made |
| **Contents** | Documents, data, model I/O, retrieval results |
| **Immutability** | Frozen at decision time |
| **Use Cases** | Audit, replay, dispute resolution |

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
  id: string
  timestamp: datetime
  decision_record_id: string
  
  # Context Snapshot
  context:
    session_state: object       # Agent session state
    agent_memory: object        # Agent memory snapshot
    enterprise_memory: array    # Retrieved enterprise memory
    enterprise_knowledge: array # Retrieved knowledge
  
  # Data References
  data:
    entity_snapshots: array     # Business entity states
    documents: array            # Document references
    external_data: array        # API responses, lookups
  
  # Model I/O
  model:
    prompts: array              # LLM prompts sent
    completions: array          # LLM responses received
    embeddings: object          # Embedding inputs/outputs
    predictions: array          # ML model predictions
  
  # Retrieval
  retrieval:
    queries: array              # RAG queries executed
    results: array              # Retrieved chunks
    rankings: object            # Relevance rankings
  
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

## Storage Tiers

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

