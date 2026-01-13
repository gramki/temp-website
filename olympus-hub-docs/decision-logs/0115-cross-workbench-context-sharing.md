# ADR-0115: Cross-Workbench Context Sharing

> **Status:** Accepted  
> **Date:** 2026-01-14  
> **Category:** request-management

---

## Context

Hub's request hierarchy (defined in ADR-0066) currently only supports parent-child relationships **within the same workbench**. Cross-workbench scenario invocations are treated as external machine/tool invocations with no context inheritance.

However, enterprise operations often span multiple domains (workbenches), and agents in different domains need to collaborate with shared context. For example:
- Credit assessment in Retail Loans needs AML clearance from Customer Lifecycle Operations
- The AML agent needs access to the loan application context (customer details, loan amount, purpose)

Without cross-workbench context sharing:
1. Developers must manually serialize and forward context
2. No automatic lifecycle cascade (parent completion doesn't notify child)
3. No standard pattern for cross-domain collaboration

---

## Decision

### 1. Extend Request Hierarchy for Cross-Workbench Support

Parent-child request relationships can now span workbench boundaries when **explicitly configured**:

```
Retail Loans Workbench              Customer Lifecycle Ops Workbench
─────────────────────              ─────────────────────────────────
                                   
Credit Assessment Request (R-A)    AML Check Request (R-B)
├── parent_request_id: null         ├── parent_request_id: R-A
├── depth: 0                        ├── depth: 0 (resets per-workbench)
│                                   ├── cross_workbench:
│   Creates child ────────────────▶ │     ├── parent_workbench_id: retail-loans
│                                   │     ├── global_depth: 1
│                                   │     └── ancestor_context_tokens: [...]
```

### 2. WorkbenchContextSharingSpec CRD

A new CRD defines acceptable parent and child contexts for a workbench:

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchContextSharingSpec
metadata:
  name: retail-loans-context-sharing
spec:
  workbench_ref:
    name: retail-loans-workbench
    subscription_id: sub-acme-prod
  
  parent_contexts: []  # Who can be parent
  
  child_contexts:      # Where we can create children
    - type: workbench
      workbench_ref:
        name: customer-lifecycle-ops
      enabled: true
```

### 3. Mutual Acknowledgment Required

Cross-workbench context sharing requires **both sides** to configure:

| Requirement | Description |
|-------------|-------------|
| **Parent configures** | `child_contexts` must include target workbench/scenario |
| **Child configures** | `parent_contexts` must include source workbench/scenario |
| **Validation** | Checked at configuration time; logged warning if one-sided |
| **Runtime enforcement** | Request creation fails if mutual acknowledgment missing |

### 4. Scenario-Level Extension

`ScenarioAutomationSpec` can extend workbench-level sharing:

```yaml
spec:
  contextSharing:
    parent_contexts: [...]  # Union with workbench config
    child_contexts: [...]   # Union with workbench config
```

Effective config = WorkbenchSpec ∪ ScenarioSpec

### 5. Token-Based Context Access

Child requests receive access tokens for each ancestor workbench:

| Aspect | Decision |
|--------|----------|
| **Token type** | JWT with request-specific claims |
| **Token scope** | Entire ancestor chain in target workbench |
| **Token lifetime** | Valid until parent completes/cancels |
| **Token revocation** | Automatic on parent lifecycle completion |

### 6. Per-Workbench Depth Limits

Depth limits apply within each workbench, not globally:

| Aspect | Behavior |
|--------|----------|
| **`depth` field** | Resets to 0 when entering new workbench |
| **`global_depth` field** | Counts total depth across all workbenches |
| **Limit enforcement** | Per-workbench max_depth applies to `depth` |

### 7. Best-Effort Lifecycle Cascade

Parent completion/cancellation cascades to children in other workbenches:

| Aspect | Decision |
|--------|----------|
| **Cascade semantics** | Best-effort with retry (eventual consistency, not guaranteed delivery) |
| **Retry policy** | Exponential backoff, 3 attempts |
| **Failure handling** | Mark child as potentially orphaned |
| **Notification** | Child receives PARENT_COMPLETED/PARENT_CANCELLED |

### 8. Subscription Constraint

Cross-workbench context sharing is limited to **same subscription**:

| Constraint | Rationale |
|------------|-----------|
| **Same subscription** | Trust boundary; billing; compliance |
| **Validated at config time** | Fail fast on invalid configuration |
| **No cross-tenant** | Different tenants = different organizations |

---

## Consequences

### Positive

| Consequence | Description |
|-------------|-------------|
| ✅ **Cross-domain collaboration** | Agents can share context across workbench boundaries |
| ✅ **Explicit authorization** | Both sides must agree; no implicit sharing |
| ✅ **Security maintained** | Token-based access; automatic revocation |
| ✅ **Flexible granularity** | Workbench-level or scenario-level |
| ✅ **Lifecycle coordination** | Parent completion cascades to children |
| ✅ **Context inheritance** | Child can access full ancestor chain |

### Neutral

| Consequence | Description |
|-------------|-------------|
| ≈ **Token management** | Additional token lifecycle to manage |
| ≈ **Configuration complexity** | Both sides must configure correctly |

### Negative

| Consequence | Mitigation |
|-------------|------------|
| ⚠️ **Network latency** | Cache compiled context where possible |
| ⚠️ **Best-effort cascade** | Monitor orphaned children; cleanup job |
| ⚠️ **Configuration drift** | Validate mutual acknowledgment at runtime |

---

## Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Implicit cross-workbench hierarchy** | Security risk; data leakage |
| **Always copy context** | Inefficient; stale data |
| **No cross-workbench support** | Limits enterprise collaboration |
| **Cross-subscription sharing** | Trust boundary concerns |
| **Global depth limit** | Inflexible; limits valid use cases |

---

## Related Decisions

- [ADR-0066](./0066-request-hierarchy-context-inheritance.md) — Request hierarchy and context inheritance (same-workbench) — **This ADR extends ADR-0066**
- [ADR-0043](./0043-workbench-as-machine-transitive-exposure.md) — Workbench as Machine pattern

---

## References

- [Cross-Workbench Context Sharing Concept](../02-system-design/implementation-concepts/workbench-context-sharing.md)
- [Request Hierarchy](../04-subsystems/request-management/request-hierarchy.md)
- [Cross-Workbench Context Sharing Guide](../10-guides/cross-workbench-context-sharing-guide.md)
