# Memory Services

> **Status:** 🟡 Draft — Under active development

Memory Services is a Hub subsystem that provides **memory storage and access capabilities** for Hub Applications and agents. It encompasses two major capability areas: **Enterprise Memory** (organizational-level, durable) and **Agent Memory** (agent/session-level, ephemeral).

---

## Overview

Hub provides **built-in memory stores** that adhere to CAF (Cognitive Audit Fabric) expectations. These are concrete implementations provisioned via CRDs as part of workbench specifications.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **CAF Compliance** | All memory stores implement CAF contracts and schemas |
| **Workbench Scoped** | Memory stores are always scoped to a workbench |
| **ESPP Taxonomy** | Unified Episodic-Semantic-Procedural-Preference taxonomy |
| **Olympus Platform** | Uses Olympus platform services (Europa, etc.) |
| **Cognitive Application** | Applications that emit memory records should be modeled as [Cognitive Applications](../../02-system-design/implementation-concepts/cognitive-application.md) |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           HUB MEMORY SERVICES                                 │
│                                                                               │
│   ┌───────────────────────────────────┐   ┌───────────────────────────────┐  │
│   │      ENTERPRISE MEMORY            │   │       AGENT MEMORY            │  │
│   │                                   │   │                               │  │
│   │   Scope: Organizational           │   │   Scope: Request/Session      │  │
│   │   Retention: 7+ years             │   │   Retention: Session + period │  │
│   │   Write: Signal Exchange          │   │   Write: Direct SDK + Tools   │  │
│   │   PII: Prohibited                 │   │   PII: Permitted (session)    │  │
│   │   Storage: Europa (OpenSearch)    │   │   Storage: TBD                │  │
│   │                                   │   │                               │  │
│   │   • Audit & compliance            │   │   • Operational continuity    │  │
│   │   • Precedent search              │   │   • In-session preferences    │  │
│   │   • Institutional learning        │   │   • Conversation context      │  │
│   │   • Cross-agent knowledge         │   │   • Entity extraction         │  │
│   └───────────────────────────────────┘   └───────────────────────────────┘  │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────────┐ │
│   │                        SHARED CONCEPTS                                   │ │
│   │                                                                          │ │
│   │   • ESPP Taxonomy (Episodic, Semantic, Procedural, Preference)          │ │
│   │   • CAF schema compatibility                                            │ │
│   │   • Workbench scoping                                                   │ │
│   │   • Promotion paths (Agent → Enterprise → ETSL)                         │ │
│   └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Subsystem Structure

### Enterprise Memory

Organizational-level memory for audit, compliance, and institutional learning.

| Document | Description | Status |
|----------|-------------|--------|
| [Enterprise Memory README](./enterprise-memory/README.md) | Overview and architecture | 🟡 Draft |
| [Query API](./enterprise-memory/query-api.md) | Query API specification | 🟡 Draft |
| [Access Tools](./enterprise-memory/access-tools.md) | Memory access tool specifications | 🟡 Draft |
| [Retention Policy](./enterprise-memory/retention-policy.md) | Retention, deletion, legal hold | 🟡 Draft |

### Agent Memory

Request/session-scoped memory for operational continuity and personalization.

| Document | Description | Status |
|----------|-------------|--------|
| [Agent Memory README](./agent-memory/README.md) | Overview and architecture | 🟡 Draft |
| [Storage Services](./agent-memory/storage-services.md) | Log, Conversation, KV, Document services | 🟡 Draft |
| [Agent Memory SDK](./agent-memory/sdk.md) | SDK and tool specification | 🟡 Draft |
| [Retention & Lifecycle](./agent-memory/retention-and-lifecycle.md) | Retention policies and lifecycle | 🟡 Draft |
| [Context Assembly](./agent-memory/context-assembly.md) | Seer integration | 🔴 Stub |

### Shared Concepts

Common concepts and specifications across both memory types.

| Document | Description | Status |
|----------|-------------|--------|
| [Shared README](./shared/README.md) | Overview of shared concepts | 🟡 Draft |
| [ESPP Taxonomy](./shared/espp-taxonomy.md) | Unified memory taxonomy | 🟡 Draft |
| [PII Policy](./shared/pii-policy.md) | PII handling across memory types | 🟡 Draft |

---

## Memory Type Comparison

| Aspect | Enterprise Memory | Agent Memory |
|--------|-------------------|--------------|
| **Scope** | Organizational — cross-agent, cross-session | Request/Session — individual agent |
| **Persistence** | Durable — 7+ years for episodic | Session + retention period |
| **Purpose** | Audit, precedent, institutional learning | Operational continuity, session context |
| **Write Path** | Via Signal Exchange (no direct writes) | Direct SDK and Tool access |
| **Read Path** | Via Memory Access Tools | SDK methods, Tools, Seer context assembly |
| **PII Policy** | **Prohibited** — entity references only | **Permitted** — within session scope |
| **Immutability** | Immutable records (CAF compliance) | Mutable (update/delete allowed) |
| **Isolation** | Workbench scoped | Per (tenant, workbench, scenario, request, agent) |
| **Cross-Session** | Yes | No — use Enterprise Memory for cross-session |
| **Encryption** | Platform-level | Application-layer, agent+session unique keys |
| **Storage Backend** | Olympus Europa (managed OpenSearch) | TBD (to be determined) |

---

## ESPP Memory Taxonomy

The **ESPP (Episodic-Semantic-Procedural-Preference)** taxonomy provides a conceptual framework for memory classification:

| Memory Class | Anchoring | Purpose |
|--------------|-----------|---------|
| **Episodic** | Event/Time/Case | What happened — decisions, outcomes, handoffs |
| **Semantic** | Entity/Domain | What we know — patterns, beliefs, constraints |
| **Procedural** | Skill/Task | How to act — learned procedures, skills |
| **Preference** | Subject | How to personalize — user/agent preferences |

### Applicability by Memory Type

| Memory Type | ESPP Enforcement | Rationale |
|-------------|------------------|-----------|
| **Enterprise Memory** | ✅ Enforced | Governance, 7+ year retention, cross-agent knowledge |
| **Agent Memory** | ❌ Optional | Session-scoped, framework-native idioms preferred |

See [ESPP Taxonomy](./shared/espp-taxonomy.md) for detailed record types and applicability.

---

## Storage Architecture

### Enterprise Memory: Olympus Europa

Enterprise Memory uses **Olympus Europa** — the platform's managed OpenSearch service:

| Aspect | Description |
|--------|-------------|
| **Service** | Olympus Europa (managed OpenSearch) |
| **Multi-Tenancy** | Platform-level tenant isolation |
| **Semantic Search** | k-NN plugin for vector similarity |
| **Index Pattern** | `{tenant}_{workbench}_{memory_class}_{record_type}` |

### Agent Memory: To Be Determined

Agent Memory storage backend is **not yet finalized**. Options include:

| Candidate | Consideration |
|-----------|---------------|
| **Olympus Europa** | If semantic search is critical |
| **Olympus Callisto** | If low-latency is critical (Redis-based) |
| **Purpose-built service** | If specialized requirements emerge |

---

## Provisioning

Memory stores are provisioned as part of Workbench specifications via CRDs:

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: fraud-ops-prod
  namespace: acme-bank
spec:
  memory_services:
    # Enterprise Memory
    enterprise_memory:
      enabled: true
      stores:
        - name: "fraud-ops.episodic.primary"
          memory_class: episodic
          storage:
            backend: europa
            cluster_ref: europa-prod
          retention:
            default_days: 2555
            legal_hold_enabled: true
    
    # Agent Memory
    agent_memory:
      enabled: true
      stores:
        log_store:
          retention_after_session_hours: 72
        conversation_store:
          retention_after_session_hours: 48
          compaction:
            default_strategy: summarization
            default_token_budget: 8000
        kv_store:
          retention_after_session_hours: 24
        document_store:
          retention_after_session_hours: 168
          max_document_size_mb: 10
```

### Admin Delegation

| Role | Capability |
|------|-----------|
| **Tenant Admin** | Provision memory stores for any workbench |
| **Workbench Admin** | Configure memory stores if delegated rights |
| **Developer** | Request memory store provisioning, use memory access tools |

---

## Promotion Paths

### Enterprise Memory → ETSL

Enterprise Memory can be **promoted** to ETSL via Enterprise Learning Services:

```
Enterprise Memory (institutional knowledge)
        │
        │ High confidence + governance approval
        ▼
ETSL (Enterprise Temporal Semantic Layer)
```

### Agent Memory → Enterprise Memory

Agent Memory **cannot be automatically promoted** to Enterprise Memory. The path is:

1. Agent developer identifies valuable patterns observed in sessions
2. Developer explicitly writes to Enterprise Memory via Signal Exchange
3. Memory follows normal Enterprise Memory governance

```
Session-Observed Pattern
        │
        │ Developer identifies cross-session value
        ▼
Explicit Write (via Cognitive Application + Signal Exchange)
        │
        ▼
Enterprise Memory
```

> **Note**: Agent Memory is strictly session-scoped. Cross-session persistence requires explicit Enterprise Memory writes.

See [Enterprise Learning Services](../cognitive-audit-fabric/enterprise-learning-services.md) for promotion workflows.

---

## Related Documentation

- [Cognitive Audit Fabric](../cognitive-audit-fabric/README.md) — CAF integration
- [Signal Exchange](../signal-exchange/README.md) — Write path routing (Enterprise Memory)
- [Signal Exchange - Memory Record Routing](../signal-exchange/memory-record-routing.md) — Memory write routing
- [Enterprise Learning Services](../cognitive-audit-fabric/enterprise-learning-services.md) — Promotion workflows
- [Seer Context Assembly](../../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md)

---

## Decision Records

### Enterprise Memory

| ADR | Title |
|-----|-------|
| [0061](../../decision-logs/0061-no-pii-in-episodic-memory.md) | No PII in Episodic Memory |
| [0062](../../decision-logs/0062-memory-writes-via-signal-exchange.md) | Memory Writes via Signal Exchange |
| [0063](../../decision-logs/0063-memory-reads-via-access-tools.md) | Memory Reads via Access Tools |

### Agent Memory

| ADR | Title |
|-----|-------|
| [0067](../../decision-logs/0067-agent-memory-session-scope.md) | Agent Memory Session Scope |
| [0068](../../decision-logs/0068-agent-memory-framework-native-idioms.md) | Framework-Native Idioms (No ESPP Enforcement) |
| [0069](../../decision-logs/0069-agent-memory-storage-services.md) | Four Storage Services |
| [0070](../../decision-logs/0070-agent-memory-encryption-isolation.md) | Encryption and Isolation |

### Subsystem Organization

| ADR | Title |
|-----|-------|
| [0064](../../decision-logs/0064-memory-services-subfolder-organization.md) | Memory Services Subfolder Organization |

---

---

*TODO: Agent memory storage decision, cross-memory queries, federation*
