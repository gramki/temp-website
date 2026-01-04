# Hub Enterprise Memory

> **Status:** 🔴 Stub — Placeholder for expansion

Hub Enterprise Memory captures the organization's **lived cognition over time**—what happened, what was decided, why, and how it influenced future behavior.

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

## Related Documentation

- [Memory Services Overview](./README.md)
- [Hub Agent Memory](./hub-agent-memory.md)
- [Cognitive Audit Fabric](../cognitive-audit-fabric/README.md)
- [Knowledge Services](../knowledge-services/README.md)

---

*TODO: Detailed design — storage backends, linking mechanisms, promotion workflows, search optimization*

