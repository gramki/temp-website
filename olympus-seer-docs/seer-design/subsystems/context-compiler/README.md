# Context Compiler

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Overview

Context Compiler provides the service implementation for context assembly, compiling context from four sources: Enterprise Knowledge, Enterprise Memory, Agent Memory, and Hub Request Context (including request hierarchy/ancestry topology). The service automatically selects retrievers based on request update metadata matching Training Spec selector criteria, incorporates available tools into context constraints, and manages token budgets, ranking, and provenance tracking.

**Key Design Point**: The service is explicitly invoked by agents — it does not pre-compile context. Agents choose when to invoke compilation, and the service automatically applies Training Spec retriever configurations based on the incoming request update.

---

## Design Documents

| Document | Status | Description |
|----------|--------|-------------|
| [Compilation Service](compilation-service.md) | 🟢 Complete | Main context compilation service with four-source compilation, request hierarchy integration, tool-aware compilation, ranking, token budgeting, and provenance tracking |
| [SCOPE](SCOPE.md) | 🟢 Complete | Coverage summary, design status, intended depth, implementation details deferred |

---

## Key Design Decisions

### Request-Update-Based Retriever Configuration

**Principle**: Agent code (Raw Agent) is framework-agnostic and precedes Training Spec. Agents cannot be Training-aware.

**Approach**: Training Spec defines retriever configurations with selectors that match against request update metadata. Context Compiler automatically selects the matching configuration based on the incoming request update.

**Benefits**:
- Agent code remains framework-agnostic
- Context compilation behavior configured declaratively in Training Spec
- Automatic adaptation to different request update types
- No code changes needed when retriever strategies evolve

### Multiple Selector Matching and Merging

**Decision**: When multiple selectors match a request update, all matching retriever configurations are merged.

**Merging Behavior**:
- **Retrievers**: Combined (union of all retrievers from matching configs)
- **Token Budgets**: Aggregated (sum of allocations, with reserve preserved)
- **Ranking Strategies**: Merged with precedence rules (most specific strategy wins conflicts)

**Rationale**: Allows fine-grained control while supporting overlapping scenarios (e.g., both "task_created" and "fraud_investigation" match).

### Goal and Role-Based Ancestor Context Filtering

**Decision**: Ancestor contexts are filtered based on agent goal and role to determine relevance.

**Filtering Logic**:
- Agent goal (from Training Spec) determines which ancestor contexts align with agent's purpose
- Agent role (from Training Spec) determines which ancestor contexts are within agent's responsibility scope
- Only relevant ancestor contexts are included in compilation

**Rationale**: Prevents information overload and ensures context relevance. A fraud analyst agent doesn't need context from a customer service ancestor request unless it's relevant to fraud detection.

### Tool-Aware Compilation

**Decision**: Available tools are incorporated into context constraints, and tool capabilities influence context retrieval and ranking.

**Rationale**:
- Agents need to know what tools are available
- Tool capabilities can reduce redundant context (if tool can query DB, less need for pre-fetched data)
- Context should help with tool selection decisions

---

## Related Documentation

### Seer Design
- [Context Assembly Concepts](../implementation-concepts/context-assembly.md) — Context assembly principles
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) — Training/Employment Spec management
- [Seer Agent SDK](../seer-agent-sdk/README.md) — SDK APIs for context compilation

### Hub Documentation
- [Hub Request Hierarchy](../../../olympus-hub-docs/04-subsystems/request-management/request-hierarchy.md) — Request hierarchy and context inheritance
- [Hub Memory Services](../../../olympus-hub-docs/04-subsystems/memory-services/README.md) — Enterprise Memory and Agent Memory
- [Hub Knowledge Services](../../../olympus-hub-docs/04-subsystems/knowledge-services/README.md) — Enterprise Knowledge
- [ADR-0066: Request Hierarchy and Context Inheritance](../../../olympus-hub-docs/decision-logs/0066-request-hierarchy-context-inheritance.md)

---

*Context Compiler provides automatic, tool-aware context assembly from four sources with request hierarchy integration and Training Spec-based retriever configuration.*
