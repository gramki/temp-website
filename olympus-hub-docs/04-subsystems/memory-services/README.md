# Memory Services

> **Status:** 🔴 Stub — Placeholder for expansion

Memory Services provide the **memory storage and access layer** for Olympus Hub. This subsystem is critical for Seer integration—all agents *should* use Hub memory storage services.

---

## Overview

Memory Services implements the cognitive memory layer defined in the [Enterprise Knowledge vs Memory vs Agent Memory](../../../olympus-seer-docs/agentic-ai-concepts/enprise-knowledge-memory-other-data.md) specification.

---

## Memory Types

| Memory Type | Scope | Purpose | Persistence |
|-------------|-------|---------|-------------|
| **Agent Memory** | Agent/Session | Operational continuity, recent interactions | Ephemeral |
| **Enterprise Memory** | Organization | Institutional cognition, cross-agent learning | Durable |

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Hub Agent Memory](./hub-agent-memory.md) | Agent Memory persistence and management | 🔴 Stub |
| [Hub Enterprise Memory](./hub-enterprise-memory.md) | Enterprise Memory persistence and management | 🔴 Stub |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MEMORY SERVICES                               │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 MEMORY ACCESS LAYER                      │    │
│  │        (APIs for read, write, query, search)             │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │               MEMORY TYPE MANAGERS                       │    │
│  │                                                          │    │
│  │  ┌──────────────┐  ┌──────────────┐                     │    │
│  │  │    Agent     │  │  Enterprise  │                     │    │
│  │  │    Memory    │  │    Memory    │                     │    │
│  │  │   Manager    │  │   Manager    │                     │    │
│  │  └──────────────┘  └──────────────┘                     │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 STORAGE BACKENDS                         │    │
│  │   (Vector stores, Key-value, Document, Time-series)     │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Agent Memory Categories

From Seer specifications, Agent Memory includes:

| Category | Description | Examples |
|----------|-------------|----------|
| **Episodic** | Recent interactions and events | Chat history, tool calls |
| **Semantic** | Facts promoted from experience | Learned preferences, patterns |
| **Preference** | User/context preferences | Communication style, timezone |
| **Procedural** | Workflows, skills, procedures | Task execution patterns |

---

## Enterprise Memory Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Decision Records** | What was decided and why | Approval decisions, exceptions |
| **Outcome Records** | What happened after decisions | Success/failure outcomes |
| **Exception History** | Overrides and exceptions granted | Manual overrides with rationale |
| **Handoff Context** | Prior agent/human actions | Case transition context |

---

## Key Principles

1. **Agent Memory is Operational** — Helps agents act in the moment
2. **Enterprise Memory is Institutional** — Captures what the organization learned
3. **Promotion Path** — Agent Memory → Enterprise Memory → Enterprise Knowledge
4. **All Agents Use Hub Storage** — Even with custom frameworks, storage is centralized

---

## Seer Integration

| Integration Point | Description |
|-------------------|-------------|
| **Memory SDKs** | Seer provides SDKs; Hub provides storage |
| **Context Assembly** | Seer Context Assembly retrieves from Hub Memory |
| **CAF Integration** | Enterprise Memory feeds Cognitive Audit Fabric |
| **Cross-Agent Learning** | Enterprise Memory enables learning across agents |

---

## Multi-Tenancy & Scoping

| Scope Level | Description |
|-------------|-------------|
| **Tenant** | Strict tenant isolation |
| **Workbench** | Memory scoped to specific workbenches |
| **Agent** | Agent-specific memory within workbench |
| **Session** | Session-scoped ephemeral memory |
| **Request** | Request-scoped memory |

---

## Related Documentation

- [Cognitive Audit Fabric](../cognitive-audit-fabric/README.md) — CAF integration
- [Knowledge Services](../knowledge-services/README.md) — Knowledge vs Memory
- [Seer Context Assembly](../../../olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md)

---

*TODO: Detailed design — storage backends, retention policies, promotion mechanisms*

