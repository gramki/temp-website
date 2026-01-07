# ADR-0065: Cognitive Application as Capability Profile

> **Status:** Accepted  
> **Date:** 2026-01-07  
> **Category:** architecture

---

## Context

Hub Applications can vary significantly in their complexity and integration with platform infrastructure:

1. **Simple applications** — Request-response automations (validation, prediction, HTTP integration)
2. **Complex applications** — Case orchestration with task delegation, context management, and memory emission

The platform needs to distinguish between these to:
- Set clear expectations for developers building task-emitting applications
- Ensure proper context compilation and memory record emission
- Enable schema validation and audit capabilities

---

## Decision

**Cognitive Application** is defined as a **capability profile** of Hub Application (not a separate type). A Hub Application is "cognitive" when it:

1. **Emits Tasks** — Creates tasks for human and AI agents via Task Management
2. **Compiles Context** — Builds and maintains request-level context for agents with each relevant update
3. **Emits Memory Records** — Produces structured episodic memory records adhering to CAF schemas
4. **Registers Schemas** — Declares the memory record schemas it will emit in its specification

### Key Design Points

| Aspect | Decision |
|--------|----------|
| **Not a separate type** | Cognitive Application is a capability profile, not a distinct kind of Hub Application |
| **Runtime-agnostic** | Can run on any Automation Runtime (Seer, Rhea, ChronoShift, Atlantis) |
| **Context scope** | Request-level context is the default; task-level specialization is left to agents |
| **Schema registration** | Applications must register schemas at application or workbench scope |
| **Recommendation** | Any application that emits tasks is advised to be modeled as Cognitive Application |

### Context Compilation Model

```
Cognitive Application                        Agent
────────────────────                        ─────

Request-Level Context                       Task-Specific Context
• Compiled with each relevant update        • Compiled by agent as needed
• Available to all agents on request        • Specialized for agent's role
• Stored as Context records in request      • May use application context
```

Context compilation by application and agent are **mutually independent** — agents may rely on application context but cannot be forced to.

### Schema Resolution Order

1. Application-registered schema (most specific)
2. Workbench-registered schema
3. Platform schema (CAF defaults)

If same type and version exist at both Application and Workbench scope, **Workbench wins** (operator alerts on conflict).

### Validation Behavior

| Condition | Action |
|-----------|--------|
| **Valid** | Route to memory store |
| **Invalid** | Retain in request history (marked invalid), do NOT route to memory store |
| **Schema not found** | Retain (unvalidated), alert operator |

Invalid records are **never discarded** — they are preserved for debugging and audit.

---

## Consequences

### Positive

| Consequence | Description |
|-------------|-------------|
| ✅ **Clear developer expectations** | Developers know what's expected for task-emitting applications |
| ✅ **Runtime flexibility** | Cognitive Applications not tied to AI/Seer; can be workflows, containers, etc. |
| ✅ **Schema governance** | Explicit schema registration enables validation and audit |
| ✅ **Context consistency** | Standard pattern for context compilation across applications |
| ✅ **Memory quality** | Invalid records don't pollute memory stores |

### Neutral

| Consequence | Description |
|-------------|-------------|
| ≈ **Additional specification** | Cognitive applications need `cognitive:` section in spec |
| ≈ **Migration path** | Non-cognitive applications can become cognitive by adding capabilities |

### Negative

| Consequence | Mitigation |
|-------------|------------|
| ⚠️ **Learning curve** | Provide templates and examples for cognitive application specs |
| ⚠️ **Schema management overhead** | Workbench-level schemas reduce duplication |

---

## Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Separate CognitiveApplicationSpec** | Unnecessary; it's a capability profile, not a distinct type |
| **Seer-only cognitive capability** | Would limit workflow and container applications from context/memory participation |
| **Optional schema registration** | Would prevent validation and reduce memory quality |
| **Discard invalid records** | Would lose debugging information and audit trail |

---

## Related Decisions

- [ADR-0007](./0007-composite-pattern-technology-agnostic.md) — Hub Applications can be any technology
- [ADR-0062](./0062-memory-writes-via-signal-exchange.md) — All memory writes via Signal Exchange
- [ADR-0063](./0063-memory-reads-via-access-tools.md) — Memory reads via access tools

---

## References

- [Cognitive Application](../02-system-design/implementation-concepts/cognitive-application.md)
- [Hub Application](../02-system-design/implementation-concepts/hub-application.md)
- [Memory Record Routing](../04-subsystems/signal-exchange/memory-record-routing.md)

