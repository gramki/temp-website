# Enterprise Memory Services

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Parent**: [Memory Services](../README.md)

---

## Overview

**Enterprise Memory Services** provides Hub's implementation of CAF-compliant memory stores for organizational-level cognition. These stores capture decisions, outcomes, patterns, and learnings that persist across agents and inform institutional behavior.

### Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Organizational — cross-agent, cross-session |
| **Persistence** | Durable — 7+ years for episodic records |
| **Purpose** | Audit, precedent, institutional learning, compliance |
| **Write Path** | Via Signal Exchange (no direct writes) |
| **Read Path** | Via Memory Access Tools |
| **PII Policy** | **Prohibited** — entity references only |

---

## Architecture

### Storage Backend: Europa (OpenSearch)

Enterprise Memory stores use **Olympus Europa** — the platform's managed OpenSearch service:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ENTERPRISE MEMORY STORAGE                                  │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐    │
│   │                      OLYMPUS EUROPA                                  │    │
│   │                  (Managed OpenSearch Service)                        │    │
│   │                                                                      │    │
│   │   • Multi-tenant isolation                                           │    │
│   │   • k-NN plugin for semantic search                                  │    │
│   │   • Index lifecycle management                                       │    │
│   │   • Backup and disaster recovery                                     │    │
│   │   • Workbench-scoped indices                                         │    │
│   └─────────────────────────────────────────────────────────────────────┘    │
│                                                                               │
│   Index Pattern: {tenant}_{workbench}_{memory_class}_{record_type}           │
│                                                                               │
│   Examples:                                                                   │
│   • acme_fraud_ops_episodic_decision_records                                 │
│   • acme_fraud_ops_semantic_patterns                                         │
│   • acme_fraud_ops_procedural_skills                                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Why Europa?

| Benefit | Description |
|---------|-------------|
| **Managed Service** | Olympus handles provisioning, scaling, backup |
| **Platform Integration** | Consistent with other Olympus data services |
| **Multi-Tenancy** | Built-in tenant isolation and resource management |
| **Semantic Search** | k-NN plugin pre-configured for vector search |
| **Compliance** | Platform-level encryption, audit logging |

---

## Write Path

**Critical Design Decision:** No Hub agent or application directly writes to Enterprise Memory. All writes flow through Signal Exchange.

```
Hub Application/Agent
        │
        │ Adds memory_records to REQUEST_UPDATE
        ▼
Signal Exchange
        │
        │ Validates, enriches with hub_metadata, routes
        ▼
Atropos Topic (per memory store)
        │
        │ Async consumption
        ▼
Memory Store Writer Service
        │
        │ Schema validation, embedding generation
        ▼
Europa (OpenSearch)
```

See [Memory Record Routing](../../signal-exchange/memory-record-routing.md) for details.

---

## Read Path

Applications and agents read via **Memory Access Tools**:

| Tool | Purpose |
|------|---------|
| `memory.search_precedent` | Semantic similarity search for cases |
| `memory.get_case_history` | Full case timeline retrieval |
| `memory.query_decisions` | Structured decision queries |
| `memory.get_handoff_context` | Handoff context for case |
| `memory.search_patterns` | Semantic pattern search |
| `memory.get_entity_beliefs` | Entity belief retrieval |

See [Memory Access Tools](./access-tools.md) for specifications.

---

## Memory Classes (ESPP)

Enterprise Memory implements the full ESPP taxonomy:

| Class | Record Types | Purpose |
|-------|-------------|---------|
| **Episodic** | CaseRecord, DecisionRecord, EvidenceBundle, ContextSnapshot, OutcomeRecord, OverrideRecord, HandoffContext, HypothesisRecord, IncidentTimeline | What happened — decisions, outcomes, handoffs |
| **Semantic** | HypothesisRecord, PatternSummary, LearnedConstraint, EntityBelief, RelationshipBelief, EvaluationFinding | What we know — patterns, beliefs |
| **Procedural** | LearnedSkill, Procedure, ActionSequence, ToolUsagePattern | How to act — learned procedures |
| **Preference** | UserPreference, AgentBehavior, InteractionPattern, ContextualPreference | How to personalize — preferences |

See [ESPP Taxonomy](../shared/espp-taxonomy.md) for unified taxonomy reference.

---

## Provisioning

Enterprise Memory stores are provisioned via Workbench CRDs:

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: fraud-ops-prod
  namespace: acme-bank
spec:
  memory_services:
    enterprise_memory:
      enabled: true
      stores:
        - name: "fraud-ops.episodic.primary"
          memory_class: episodic
          storage:
            backend: europa           # Olympus managed OpenSearch
            cluster_ref: europa-prod
            index_prefix: "fraud_ops_episodic"
          atropos_topic: "fraud-ops-episodic-records"
          retention:
            default_days: 2555        # 7 years
            legal_hold_enabled: true
```

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Query API](./query-api.md) | Query API specification for memory retrieval | 🟡 Draft |
| [Access Tools](./access-tools.md) | Tool specifications for memory access | 🟡 Draft |
| [Retention Policy](./retention-policy.md) | Retention, legal hold, deletion semantics | 🟡 Draft |

---

## Related Documents

- [Memory Services Overview](../README.md) — Parent subsystem
- [Agent Memory Services](../agent-memory/README.md) — Agent-level memory
- [Shared Concepts](../shared/README.md) — ESPP taxonomy, PII policy
- [Signal Exchange - Memory Record Routing](../../signal-exchange/memory-record-routing.md) — Write path
- [Cognitive Audit Fabric](../../cognitive-audit-fabric/README.md) — CAF integration

---

*TODO: Europa cluster sizing, index lifecycle policies, cross-workbench federation*

