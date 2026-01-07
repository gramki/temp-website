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

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           HUB MEMORY SERVICES                                 │
│                                                                               │
│   ┌───────────────────────────────────┐   ┌───────────────────────────────┐  │
│   │      ENTERPRISE MEMORY            │   │       AGENT MEMORY            │  │
│   │                                   │   │                               │  │
│   │   Scope: Organizational           │   │   Scope: Agent/Session        │  │
│   │   Retention: 7+ years             │   │   Retention: Days to months   │  │
│   │   Write: Signal Exchange          │   │   Write: Direct SDK           │  │
│   │   PII: Prohibited                 │   │   PII: Permitted              │  │
│   │   Storage: Europa (OpenSearch)    │   │   Storage: TBD                │  │
│   │                                   │   │                               │  │
│   │   • Audit & compliance            │   │   • Operational continuity    │  │
│   │   • Precedent search              │   │   • Personalization           │  │
│   │   • Institutional learning        │   │   • Session context           │  │
│   │   • Cross-agent knowledge         │   │   • Preference learning       │  │
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

Agent/session-level memory for operational continuity and personalization.

| Document | Description | Status |
|----------|-------------|--------|
| [Agent Memory README](./agent-memory/README.md) | Overview and architecture | 🟡 Draft |
| [Agent Memory SDK](./agent-memory/sdk.md) | SDK specification | 🔴 Stub |
| [Retention & Decay](./agent-memory/retention-and-decay.md) | Retention and decay models | 🔴 Stub |

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
| **Scope** | Organizational — cross-agent, cross-session | Agent/Session — individual context |
| **Persistence** | Durable — 7+ years for episodic | Ephemeral — days to months |
| **Purpose** | Audit, precedent, institutional learning | Operational continuity, personalization |
| **Write Path** | Via Signal Exchange (no direct writes) | Direct SDK access |
| **Read Path** | Via Memory Access Tools | SDK methods, Seer context assembly |
| **PII Policy** | **Prohibited** — entity references only | **Permitted** — with consent |
| **Immutability** | Immutable records (CAF compliance) | Mutable (update/delete allowed) |
| **Storage Backend** | Olympus Europa (managed OpenSearch) | TBD (to be determined) |

---

## ESPP Memory Taxonomy

Both Enterprise and Agent Memory implement the **ESPP (Episodic-Semantic-Procedural-Preference)** taxonomy:

| Memory Class | Anchoring | Purpose |
|--------------|-----------|---------|
| **Episodic** | Event/Time/Case | What happened — decisions, outcomes, handoffs |
| **Semantic** | Entity/Domain | What we know — patterns, beliefs, constraints |
| **Procedural** | Skill/Task | How to act — learned procedures, skills |
| **Preference** | Subject | How to personalize — user/agent preferences |

See [ESPP Taxonomy](./shared/espp-taxonomy.md) for detailed record types and semantics.

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
      defaults:
        retention:
          episodic_hours: 24
          semantic_days: 30
          procedural_days: -1  # Indefinite
          preference_days: 90
```

### Admin Delegation

| Role | Capability |
|------|-----------|
| **Tenant Admin** | Provision memory stores for any workbench |
| **Workbench Admin** | Configure memory stores if delegated rights |
| **Developer** | Request memory store provisioning, use memory access tools |

---

## Promotion Paths

Memory can be **promoted** across types and scopes:

```
Agent Memory (observed pattern)
        │
        │ Pattern validated across sessions
        ▼
Enterprise Memory (institutional knowledge)
        │
        │ High confidence + governance approval
        ▼
ETSL (Enterprise Temporal Semantic Layer)
```

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

| ADR | Title |
|-----|-------|
| [0061](../../decision-logs/0061-no-pii-in-episodic-memory.md) | No PII in Episodic Memory |
| [0062](../../decision-logs/0062-memory-writes-via-signal-exchange.md) | Memory Writes via Signal Exchange |
| [0063](../../decision-logs/0063-memory-reads-via-access-tools.md) | Memory Reads via Access Tools |
| [0064](../../decision-logs/0064-memory-services-subfolder-organization.md) | Memory Services Subfolder Organization |

---

## Legacy Files

> **Note**: The following files at the root of memory-services/ are being retained for reference but are superseded by the new subfolder structure:
> - `hub-enterprise-memory.md` → See `enterprise-memory/README.md`
> - `hub-agent-memory.md` → See `agent-memory/README.md`
> - `memory-query-api.md` → See `enterprise-memory/query-api.md`
> - `memory-access-tools.md` → See `enterprise-memory/access-tools.md`
> - `retention-and-pii-policy.md` → See `enterprise-memory/retention-policy.md` and `shared/pii-policy.md`

---

*TODO: Agent memory storage decision, cross-memory queries, federation*
