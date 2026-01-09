# ADR-0066: Request Hierarchy and Context Inheritance

> **Status:** Accepted  
> **Date:** 2026-01-07  
> **Category:** request-management

---

## Context

Hub Applications can invoke other Scenarios within their workbench (as tools or agents). This creates questions about:

1. How are the resulting requests related?
2. Can the invoked scenario access the invoker's context?
3. What happens when the parent request completes or is cancelled?
4. How do cross-workbench invocations differ?

---

## Decision

### 1. Parent-Child Request Relationship (Same-Workbench Only)

When a Hub Application invokes another Scenario **within the same workbench**, a **parent-child request relationship** is established:

```
Parent Request (Fraud Investigation)
├── Child Request (Document Verification) ─── same workbench
│   └── Grandchild Request (OCR Extraction) ─── same workbench
└── Child Request (Customer Verification) ─── same workbench
```

**Cross-workbench invocations do NOT create parent-child relationships** — they are treated as external machine/tool invocations.

### 2. Context Inheritance (by Reference)

Child requests can access parent (and ancestor) context through **reference**:

| Aspect | Decision |
|--------|----------|
| **Inheritance model** | Reference, not copy |
| **Context immutability** | Context records are immutable; updates create new versions |
| **API response** | Compiled-context API includes ancestor chain + current context |
| **What's inherited** | Context records only — NOT environment variables or secrets |

### 3. Lifecycle Cascade

When a parent request reaches a terminal state, all descendants **cascade**:

| Parent State | Descendant Behavior |
|--------------|---------------------|
| `COMPLETED` | Marked `COMPLETED` with reason `PARENT_COMPLETED` |
| `CANCELLED` | Marked `CANCELLED` with reason `PARENT_CANCELLED` |

Non-terminal state changes (`ACTIVE` ↔ `PENDING`) do **not** cascade.

### 4. Child Context Isolation

When a child request completes:

- Child's **result payload** returns to parent application
- Child's **context is isolated** — does NOT merge into parent context
- Parent decides how to use child's result

### 5. Observer Isolation

Observers receive notifications **only** for the specific request they're watching:

- Parent observers do NOT receive child request updates
- Child observers do NOT receive parent request updates
- To watch entire hierarchy, register on each request

### 6. Depth Limits

Maximum request hierarchy depth is **configurable per workbench**:

| Aspect | Value |
|--------|-------|
| **Default** | 5 levels |
| **Maximum** | 10 levels (platform limit) |
| **Violation** | Scenario invocation fails with `REQUEST_DEPTH_EXCEEDED` |

### 7. Cross-Workbench Invocations

Cross-workbench scenario invocations:

| Aspect | Behavior |
|--------|----------|
| **Relationship** | None — treated as external machine/tool invocation |
| **Context** | No implicit sharing — invoker must explicitly forward |
| **Lifecycle** | Independent — no cascade |
| **Terminology** | "External invocation" not "child request" |

---

## Consequences

### Positive

| Consequence | Description |
|-------------|-------------|
| ✅ **Context sharing without copying** | Children access parent context efficiently via reference |
| ✅ **Clean lifecycle management** | Cascade ensures no orphaned child requests |
| ✅ **Clear isolation boundaries** | Each request's context and observers are isolated |
| ✅ **Cross-workbench security** | No implicit data leakage between workbenches |
| ✅ **Depth protection** | Configurable limits prevent runaway nesting |

### Neutral

| Consequence | Description |
|-------------|-------------|
| ≈ **Reference tracking** | System must maintain and resolve context references |
| ≈ **Cascade processing** | Terminal state changes require descendant updates |

### Negative

| Consequence | Mitigation |
|-------------|------------|
| ⚠️ **Hierarchy query overhead** | Cache hierarchy for active requests |
| ⚠️ **Cross-workbench explicit forwarding** | Provide SDK helpers for context serialization |

---

## Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Copy-on-create context** | Inefficient for large context; loses updates |
| **No parent-child relationship** | Would require explicit context passing everywhere |
| **Independent lifecycle** | Risk of orphaned child requests |
| **Cross-workbench parent-child** | Security concerns; implicit data sharing across boundaries |
| **Merge child context on completion** | Context pollution; unclear ownership |

---

## Related Decisions

- [ADR-0003](./0003-signal-exchange-responsibility-boundaries.md) — Signal Exchange operates at Request level
- [ADR-0042](./0042-scenario-as-tool-granularity.md) — Scenario as Tool granularity
- [ADR-0065](./0065-cognitive-application-capability-profile.md) — Cognitive Application context compilation

---

## References

- [Request Hierarchy](../04-subsystems/request-management/request-hierarchy.md)
- [Request Lifecycle](../04-subsystems/request-management/request-lifecycle.md)
- [Scenario as a Tool](../09-composite-systems-and-patterns/scenario-as-a-tool.md)
- [Scenario as an Agent](../09-composite-systems-and-patterns/scenario-as-an-agent.md)

