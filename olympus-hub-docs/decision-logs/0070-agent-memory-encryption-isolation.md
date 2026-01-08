# ADR-0070: Agent Memory Encryption and Isolation

> **Status**: Accepted  
> **Date**: 2026-01-08  
> **Category**: memory-services

---

## Context

Agent Memory stores operational data including potentially sensitive session context. In a multi-tenant Hub environment, strict isolation and encryption are required to ensure:

1. Agents cannot access other agents' memory
2. Memory is protected at rest and in transit
3. Session-scoped data cannot leak beyond session boundaries
4. No values are logged or accessible outside session scope

---

## Decision

**Agent Memory uses application-layer encryption with strict hierarchical isolation.**

### Isolation Model

All storage is scoped by a strict hierarchy:

```
tenant → workbench → scenario → request → agent
```

- All read/write APIs operate **only within this scope**
- Agents cannot access higher scopes or other agents' memory
- No cross-talk between agents is supported

### Encryption Model

| Aspect | Implementation |
|--------|----------------|
| **Encryption Level** | Application layer (before persistence) |
| **Key Scope** | Unique per agent, per session |
| **Key Derivation** | From Workbench-scoped root key |
| **Values** | Encrypted; not logged; not retrievable outside session |

### Key Lifecycle

| Phase | Key Status |
|-------|------------|
| Session Active | Keys active, derived from Workbench root |
| Session Completed | Keys retained for retention period |
| Retention Expired | Keys securely deleted |

### Privacy Guarantees

| Constraint | Enforcement |
|------------|-------------|
| Agent memory is agent-private | Scoped APIs enforce isolation |
| Values not logged | Application-layer encryption |
| Not retrievable outside session | Session-scoped keys |
| Store names: no PII | Validation on `(a-zA-Z_-)+` pattern |

---

## Consequences

### Positive

1. **Defense in depth**: Even if storage is compromised, data is encrypted with session-unique keys
2. **Automatic cleanup**: Key deletion ensures data is unrecoverable after retention
3. **No accidental leakage**: Scoping enforced at API level
4. **Audit simplification**: No need to audit agent memory (no long-term retention)

### Negative

1. **No memory sharing**: Agents cannot share memory even if desired
2. **Key management overhead**: Keys must be managed per session
3. **No admin access to values**: Even admins cannot read encrypted values

### Neutral

1. Store names (keys) are validated but not encrypted in metadata
2. Retention period allows debugging without exposing values

---

## Contrast with Enterprise Memory

| Aspect | Enterprise Memory | Agent Memory |
|--------|-------------------|--------------|
| Encryption | Platform-level | Application-layer |
| Key Scope | Workbench | Agent + Session |
| Isolation | Workbench-scoped | Agent-scoped |
| Admin Access | Read-only for audit | No access to values |
| Cross-Agent | Shared (governed) | Isolated (no sharing) |

---

## Related Decisions

- [ADR-0067: Agent Memory Session Scope](./0067-agent-memory-session-scope.md) — Session lifecycle
- [ADR-0061: No PII in Episodic Memory](./0061-no-pii-in-episodic-memory.md) — Enterprise Memory PII handling

---

## References

- [Agent Memory Services](../04-subsystems/memory-services/agent-memory/README.md#security-model)
- [Agent Memory Retention & Lifecycle](../04-subsystems/memory-services/agent-memory/retention-and-lifecycle.md)

