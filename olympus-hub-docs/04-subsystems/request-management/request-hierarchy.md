# Request Hierarchy

> **Status:** ✅ Complete  
> **Last Updated:** 2026-01-07  
> **Parent:** [Request Management](./README.md)

---

## Overview

When a Hub Application invokes another Scenario **within the same workbench** (as a tool or as an agent), a **child request** is created. This establishes a parent-child relationship between requests, enabling context inheritance and lifecycle coordination.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Same-Workbench Only** | Parent-child relationships only exist within the same workbench |
| **Context Inheritance** | Child requests can access parent context via reference |
| **Lifecycle Cascade** | Child requests are completed/cancelled when parent completes/cancels |
| **Observer Isolation** | Observers see updates for their specific request only |
| **Depth Limits** | Configurable maximum nesting depth per workbench |

---

## Parent-Child Relationship

### When Child Requests Are Created

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SAME-WORKBENCH SCENARIO INVOCATION                        │
│                                                                              │
│   Hub Application (handling Parent Request)                                  │
│         │                                                                    │
│         ├──── Invokes Scenario-as-Tool ────▶ Child Request Created           │
│         │                                                                    │
│         └──── Invokes Scenario-as-Agent ───▶ Child Request Created           │
│                                                                              │
│   Child Request:                                                             │
│   • parent_request_id = Parent's request_id                                  │
│   • depth = Parent's depth + 1                                               │
│   • Can access Parent's context (by reference)                               │
│   • Lifecycle bound to Parent                                                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Not Parent-Child (Cross-Workbench)

Cross-workbench scenario invocations do **NOT** create parent-child relationships:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   CROSS-WORKBENCH INVOCATION                                 │
│                                                                              │
│   Workbench A                           Workbench B                          │
│   ──────────                           ──────────                            │
│                                                                              │
│   Hub Application ────▶ Machine/Tool ────▶ External Request                  │
│   (Request A)            Invocation        (Request B — NOT a child)         │
│                                                                              │
│   • No parent_request_id link                                                │
│   • No context inheritance (must explicitly forward)                         │
│   • No lifecycle cascade                                                     │
│   • Treated as external machine/tool invocation                              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Request Hierarchy Structure

### Request Entity Extension

```yaml
# Request entity with hierarchy fields
request:
  id: "req-child-001"
  workbench_id: "wb-fraud-ops"
  scenario_id: "document-verification"
  
  # Hierarchy fields
  hierarchy:
    parent_request_id: "req-parent-001"    # Immediate parent (null if root)
    root_request_id: "req-parent-001"      # Top-level ancestor
    depth: 1                                # 0 = root, 1 = child, 2 = grandchild, etc.
    
  # Standard fields
  status: "ACTIVE"
  created_at: "2026-01-07T10:15:00Z"
```

### Hierarchy Relationships

```
Root Request (depth=0)
├── Child Request A (depth=1)
│   ├── Grandchild Request A1 (depth=2)
│   └── Grandchild Request A2 (depth=2)
│       └── Great-grandchild A2a (depth=3)
└── Child Request B (depth=1)
    └── Grandchild Request B1 (depth=2)
```

---

## Depth Limits

### Configuration

Maximum request hierarchy depth is configurable per workbench:

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchSpec
metadata:
  name: fraud-ops
spec:
  # ... other workbench configuration ...
  
  request_hierarchy:
    max_depth: 5                    # Maximum nesting depth (0 = unlimited)
    on_violation: reject            # reject | warn_and_reject
```

### Default and Recommendations

| Aspect | Value |
|--------|-------|
| **Default max_depth** | 5 |
| **Practical recommendation** | ≤5 levels for maintainability |
| **Minimum** | 1 (at least one level of child requests) |
| **Maximum** | 10 (platform limit) |

### Violation Handling

When a scenario invocation would exceed max_depth:

```yaml
# Scenario invocation that would exceed depth limit
error:
  code: "REQUEST_DEPTH_EXCEEDED"
  message: "Cannot create child request: max depth (5) exceeded"
  details:
    current_depth: 5
    max_depth: 5
    parent_request_id: "req-12345"
    attempted_scenario: "document-verification"
```

The invocation **fails** — no child request is created.

---

## Context Inheritance

### Inheritance Model

Child requests can access parent (and ancestor) context through **reference**, not copy.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CONTEXT INHERITANCE MODEL                              │
│                                                                              │
│   Root Request Context                                                       │
│   ┌───────────────────────────────────────────────────────────────────────┐ │
│   │  context_id: "ctx-root-001"                                            │ │
│   │  constraints: [...]                                                    │ │
│   │  verified_facts: [...]                                                 │ │
│   └───────────────────────────────────────────────────────────────────────┘ │
│                              ▲                                               │
│                              │ reference                                     │
│   Child Request Context      │                                               │
│   ┌───────────────────────────────────────────────────────────────────────┐ │
│   │  context_id: "ctx-child-001"                                           │ │
│   │  parent_context_ref: "ctx-root-001"                                    │ │
│   │  own_context: [...]   ◀── Child's own additions                        │ │
│   └───────────────────────────────────────────────────────────────────────┘ │
│                              ▲                                               │
│                              │ reference                                     │
│   Grandchild Request Context │                                               │
│   ┌───────────────────────────────────────────────────────────────────────┐ │
│   │  context_id: "ctx-grandchild-001"                                      │ │
│   │  parent_context_ref: "ctx-child-001"                                   │ │
│   │  own_context: [...]                                                    │ │
│   └───────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Context Record Immutability

Context records are **immutable**:

| Aspect | Behavior |
|--------|----------|
| **Creation** | Context record created with specific version |
| **Updates** | New context record created with new version (old record preserved) |
| **Access** | Child accesses parent context by reference to specific version |
| **Versioning** | Each context update creates a new version |

### What Is Inherited vs Not Inherited

| Inherited (via reference) | NOT Inherited |
|--------------------------|---------------|
| Context records | Environment variables |
| Compiled context (constraints, facts, SOPs) | Secrets |
| Ancestor context chain | Parent request status |
| | Parent task state |

---

## Context Access API

### Get Compiled Context (with Ancestors)

Signal Exchange provides an API to retrieve compiled context including ancestor context:

```yaml
# GET /requests/{request_id}/compiled-context
# Returns context from current request + all ancestors

response:
  request_id: "req-grandchild-001"
  
  # Ancestor chain (root first)
  ancestor_context:
    - request_id: "req-root-001"
      depth: 0
      context:
        version: "v3"
        constraints: [...]
        verified_facts: [...]
        applicable_sops: [...]
    
    - request_id: "req-child-001"
      depth: 1
      context:
        version: "v2"
        constraints: [...]
        verified_facts: [...]
  
  # Current request context
  current_context:
    request_id: "req-grandchild-001"
    depth: 2
    context:
      version: "v1"
      constraints: [...]
      verified_facts: [...]
  
  # Merged view (for convenience)
  merged_context:
    constraints: [...]        # Union of all constraints
    verified_facts: [...]     # Union of all facts
    applicable_sops: [...]    # Union of all SOPs
    # Note: On conflict, child values take precedence
```

### Context Update Notifications

When any request's context is updated:

```yaml
# REQUEST_UPDATE notification
message:
  message_type: REQUEST_UPDATE
  request_id: "req-parent-001"
  update_type: CONTEXT_UPDATE
  
  payload:
    context_version: "v4"
    updated_fields:
      - verified_facts
    
  # Observers of req-parent-001 receive this
  # Observers of child requests do NOT receive this
  # Child requests access updated context on next query
```

---

## Lifecycle Cascade

### Completion Cascade

When a parent request completes, all descendant requests are also completed:

```
Parent Request: COMPLETED
├── Child A: COMPLETED (cascaded)
│   ├── Grandchild A1: COMPLETED (cascaded)
│   └── Grandchild A2: COMPLETED (cascaded)
└── Child B: COMPLETED (cascaded)
```

### Cancellation Cascade

When a parent request is cancelled, all descendant requests are also cancelled:

```
Parent Request: CANCELLED
├── Child A: CANCELLED (cascaded)
│   └── Grandchild A1: CANCELLED (cascaded)
└── Child B: CANCELLED (cascaded)
```

### Cascade Behavior

| Parent Status | Descendant Behavior |
|---------------|---------------------|
| `COMPLETED` | All descendants marked `COMPLETED` with reason `PARENT_COMPLETED` |
| `CANCELLED` | All descendants marked `CANCELLED` with reason `PARENT_CANCELLED` |
| `ACTIVE` → `PENDING` | No cascade — descendants continue processing |
| `PENDING` → `ACTIVE` | No cascade — descendants continue processing |

### Child Completion Does Not Affect Parent

When a child request completes:

- Child's result is returned to the invoking application
- Parent request continues processing
- Parent decides next steps based on child result
- Child context is **isolated** — does not merge into parent

---

## Observer Isolation

### Notification Scope

Observers receive notifications **only** for the specific request they're watching:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         OBSERVER ISOLATION                                   │
│                                                                              │
│   Observer A (watching Parent Request)                                       │
│   ├── Receives: Parent status changes, Parent context updates                │
│   └── Does NOT receive: Child request updates                                │
│                                                                              │
│   Observer B (watching Child Request)                                        │
│   ├── Receives: Child status changes, Child context updates                  │
│   └── Does NOT receive: Parent or sibling updates                            │
│                                                                              │
│   To watch entire hierarchy:                                                 │
│   • Register as observer on each request in the hierarchy                    │
│   • Or query hierarchy via API to enumerate all requests                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Hierarchy Query

To observe an entire request hierarchy:

```yaml
# GET /requests/{request_id}/hierarchy

response:
  root:
    request_id: "req-root-001"
    scenario_id: "fraud-investigation"
    status: "ACTIVE"
    depth: 0
  
  descendants:
    - request_id: "req-child-001"
      parent_request_id: "req-root-001"
      scenario_id: "document-verification"
      status: "ACTIVE"
      depth: 1
    
    - request_id: "req-child-002"
      parent_request_id: "req-root-001"
      scenario_id: "customer-verification"
      status: "COMPLETED"
      depth: 1
    
    - request_id: "req-grandchild-001"
      parent_request_id: "req-child-001"
      scenario_id: "ocr-extraction"
      status: "ACTIVE"
      depth: 2
```

---

## Cross-Workbench Invocations

### No Implicit Context Sharing

When invoking a scenario in a **different workbench** (via Machine/Tool interface):

| Aspect | Behavior |
|--------|----------|
| **Relationship** | No parent-child relationship |
| **Context** | No implicit sharing — invoker must explicitly forward |
| **Lifecycle** | Independent — no cascade |
| **Terminology** | "External invocation" not "child request" |

### Explicit Context Forwarding

The invoker must explicitly include relevant context in the invocation:

```python
# Cross-workbench invocation — must explicitly forward context
result = await machine_client.invoke(
    machine="customer-service-workbench",
    tool="eligibility-check",
    operation="check",
    input={
        "customer_id": "cust-12345",
        
        # Explicitly forwarded context (per recipient's contract)
        "context": {
            "requesting_workbench": "fraud-ops",
            "case_id": "case-67890",
            "priority": "high"
        }
    }
)
```

### Contract Responsibility

| Actor | Responsibility |
|-------|----------------|
| **Publisher** (target workbench) | Defines what context the tool/machine expects in its contract |
| **Consumer** (invoking workbench) | Explicitly provides required context per contract |

---

## Implementation Details

### Child Request Creation

When Signal Exchange creates a child request:

```python
def create_child_request(
    parent_request: Request,
    scenario_id: str,
    payload: dict
) -> Request:
    # 1. Check depth limit
    workbench = get_workbench(parent_request.workbench_id)
    max_depth = workbench.request_hierarchy.max_depth
    
    if parent_request.hierarchy.depth >= max_depth:
        raise RequestDepthExceededError(
            current_depth=parent_request.hierarchy.depth,
            max_depth=max_depth
        )
    
    # 2. Create child request with hierarchy
    child_request = Request(
        id=generate_request_id(),
        workbench_id=parent_request.workbench_id,
        scenario_id=scenario_id,
        hierarchy=RequestHierarchy(
            parent_request_id=parent_request.id,
            root_request_id=parent_request.hierarchy.root_request_id or parent_request.id,
            depth=parent_request.hierarchy.depth + 1
        ),
        status="ACTIVE"
    )
    
    # 3. Create context with parent reference
    child_context = Context(
        request_id=child_request.id,
        parent_context_ref=parent_request.current_context_id,
        own_context={}  # Initially empty
    )
    
    return child_request
```

### Cascade Completion

When a request completes:

```python
def complete_request(request_id: str, outcome: RequestOutcome):
    request = get_request(request_id)
    
    # 1. Complete this request
    request.status = "COMPLETED"
    request.outcome = outcome
    save_request(request)
    
    # 2. Cascade to all descendants
    descendants = get_all_descendants(request_id)
    for descendant in descendants:
        descendant.status = "COMPLETED"
        descendant.outcome = RequestOutcome(
            status="COMPLETED",
            reason="PARENT_COMPLETED",
            parent_request_id=request_id
        )
        save_request(descendant)
        
        # 3. Notify observers of each descendant
        notify_observers(descendant.id, "STATUS_CHANGE")
```

---

## Related Documentation

- [Request Management](./README.md) — Parent subsystem
- [Request Lifecycle](./request-lifecycle.md) — Request states and transitions
- [Signal Exchange](../signal-exchange/README.md) — Context access APIs
- [Scenario as a Tool](../../09-composite-systems-and-patterns/scenario-as-a-tool.md) — Tool invocation creating child requests
- [Scenario as an Agent](../../09-composite-systems-and-patterns/scenario-as-an-agent.md) — Agent invocation creating child requests
- [Workbench as a Machine](../../09-composite-systems-and-patterns/workbench-as-a-machine.md) — Cross-workbench invocations (no parent-child)

---

## References

- [ADR-0066: Request Hierarchy and Context Inheritance](../../decision-logs/0066-request-hierarchy-context-inheritance.md)

