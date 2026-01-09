# ADR-0067: Agent Memory Session Scope

> **Status**: Accepted  
> **Date**: 2026-01-08  
> **Category**: memory-services

---

## Context

Hub provides two types of memory services: Enterprise Memory (organizational, durable) and Agent Memory (operational, ephemeral). A key design decision is defining the lifecycle and scope boundaries for Agent Memory.

### Considerations

1. **Enterprise Constraints**: Hub runtimes don't guarantee VM affinity; agents may be restarted on different nodes
2. **Isolation Requirements**: Multi-tenant environment requires strict data isolation
3. **Enterprise/Agent Boundary**: Clear separation needed between governed Enterprise Memory and operational Agent Memory
4. **Framework Compatibility**: Agent Memory must work with various agentic frameworks (LangChain, LangGraph, Strands, etc.)

### Options Considered

1. **Cross-session Agent Memory**: Allow agent memory to persist across sessions (like Strands + AgentCore)
2. **Session-scoped Agent Memory**: Bound all agent memory to Request/Session lifecycle
3. **Hybrid**: Short-term session-scoped, long-term promoted to Enterprise Memory

---

## Decision

**Agent Memory is strictly session-scoped.** All agent memory is bounded by the Request/Session lifecycle with the following constraints:

1. **Maximum lifetime = Session lifetime**: Memory cannot persist beyond the session
2. **No in-memory stores**: All storage is durable (survives restarts within session)
3. **Strict isolation**: Per (tenant, workbench, scenario, request, agent)
4. **Retention period**: Admin-configurable retention after session completion (for debugging)
5. **Automatic cleanup**: Memory deleted after retention period expires

### Cross-Session Memory Path

For data that must persist across sessions:
- Use **Enterprise Memory** (via Signal Exchange and Cognitive Application)
- Use **operational data stores** with business entity semantics

---

## Consequences

### Positive

1. **Clear Enterprise/Agent boundary**: No accidental cross-session data leakage
2. **Simplified governance**: Session-scoped data doesn't require long-term compliance
3. **Security by design**: Encryption keys are session-unique; data cannot escape scope
4. **Cleanup guarantee**: No orphaned agent data accumulating over time
5. **Framework compatibility**: Works with any framework that supports external storage

### Negative

1. **Cross-session learning requires explicit action**: Developers must use Enterprise Memory
2. **No automatic preference persistence**: User preferences must be re-learned or stored in Enterprise Memory
3. **Session continuity requires Enterprise Memory**: Long-running cases need explicit context persistence

### Neutral

1. Retention period allows debugging without compromising session scope
2. Developers have clear guidance on when to use each memory type

---

## Alternatives Rejected

### Cross-Session Agent Memory (like Strands + AgentCore)

- **Why rejected**: Would blur the Enterprise/Agent boundary; cross-session data requires governance that Agent Memory doesn't provide
- **Trade-off**: Strands operates in a different context (single-tenant, developer-controlled) where this is acceptable

### Hybrid Approach

- **Why rejected**: Complexity without clear benefit; better to have explicit promotion to Enterprise Memory when needed

---

## Related Decisions

- [ADR-0061: No PII in Episodic Memory](./0061-no-pii-in-episodic-memory.md) — Enterprise Memory PII constraints
- [ADR-0062: Memory Writes via Signal Exchange](./0062-memory-writes-via-signal-exchange.md) — Enterprise Memory write path
- [ADR-0064: Memory Services Subfolder Organization](./0064-memory-services-subfolder-organization.md) — Memory services structure

---

## References

- [Agent Memory Services](../04-subsystems/memory-services/agent-memory/README.md)
- [Agent Memory Design Rationale](../04-subsystems/memory-services/agent-memory/design-rationale.md)
- [Agent Memory Retention & Lifecycle](../04-subsystems/memory-services/agent-memory/retention-and-lifecycle.md)

