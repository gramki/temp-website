# Request Hierarchy

> **Status:** ✅ Complete  
> **Last Updated:** 2026-01-14  
> **Parent:** [Request Management](./README.md)

---

## Overview

When a Hub Application invokes another Scenario **within the same workbench** (as a tool or as an agent), a **child request** is created. This establishes a parent-child relationship between requests, enabling context inheritance and lifecycle coordination.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Same-Workbench Default** | Parent-child relationships exist within the same workbench by default |
| **Cross-Workbench Extension** | Parent-child can span workbenches with explicit configuration |
| **Context Inheritance** | Child requests can access parent context via reference (or token for cross-workbench) |
| **Lifecycle Cascade** | Child requests are completed/cancelled when parent completes/cancels |
| **Observer Isolation** | Observers see updates for their specific request only |
| **Depth Limits** | Configurable maximum nesting depth per workbench (not global) |

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

### Cross-Workbench Invocations (Default Behavior)

By default, cross-workbench scenario invocations do **NOT** create parent-child relationships:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              CROSS-WORKBENCH INVOCATION (Default — No Context Sharing)       │
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

### Cross-Workbench Parent-Child (With Context Sharing)

When both workbenches configure explicit context sharing via `WorkbenchContextSharingSpec`, cross-workbench parent-child relationships **are** supported:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│           CROSS-WORKBENCH INVOCATION (With Context Sharing Configured)       │
│                                                                              │
│   Workbench A (Parent)                  Workbench B (Child)                  │
│   ────────────────────                  ───────────────────                  │
│                                                                              │
│   Hub Application ────▶ Invoke Scenario ────▶ Child Request                  │
│   (Request A)                                 (Request B — IS a child)       │
│                                                                              │
│   Request B includes:                                                        │
│   • parent_request_id: Request A                                             │
│   • cross_workbench.parent_workbench_id: Workbench A                        │
│   • cross_workbench.ancestor_context_tokens: [token for WB-A]               │
│   • Context inheritance via token-based access                               │
│   • Lifecycle cascade (best-effort)                                          │
│                                                                              │
│   Requirements:                                                              │
│   • Both workbenches must be in same subscription                            │
│   • WB-A must have child_contexts including WB-B                             │
│   • WB-B must have parent_contexts including WB-A                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

→ See [Cross-Workbench Context Sharing](../../02-system-design/implementation-concepts/workbench-context-sharing.md) for full configuration details.

---

## Request Hierarchy Structure

### Request Entity Extension

```yaml
# Request entity with hierarchy fields
request:
  id: "req-child-001"
  workbench_id: "wb-fraud-ops"
  scenario_id: "document-verification"
  
  # Hierarchy fields (same-workbench)
  hierarchy:
    parent_request_id: "req-parent-001"    # Immediate parent (null if root)
    root_request_id: "req-parent-001"      # Top-level ancestor
    depth: 1                                # 0 = root, 1 = child, 2 = grandchild, etc.
  
  # Cross-workbench hierarchy fields (only present for cross-workbench children)
  cross_workbench:
    parent_workbench_id: "wb-retail-loans" # Parent's workbench (null if same workbench)
    root_workbench_id: "wb-retail-loans"   # Root request's workbench
    global_depth: 2                         # Total depth across all workbenches
    ancestor_context_tokens:                # Tokens for accessing ancestor contexts
      - workbench_id: "wb-retail-loans"
        token: "eyJhbGciOiJSUzI1NiIs..."
        scope: ["req-root-001", "req-parent-001"]
        expires_at: "2026-01-15T10:30:00Z"
    
  # Standard fields
  status: "ACTIVE"
  created_at: "2026-01-07T10:15:00Z"
```

**Cross-Workbench Fields Explained:**

| Field | Description |
|-------|-------------|
| `parent_workbench_id` | Workbench ID of the immediate parent (null if same workbench) |
| `root_workbench_id` | Workbench ID of the root request in the hierarchy |
| `global_depth` | Total depth counting across all workbenches (0 = root) |
| `ancestor_context_tokens` | JWT tokens for accessing ancestor context in each workbench |

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

Maximum request hierarchy depth is configurable **per workbench**:

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

### Per-Workbench vs Global Depth

Depth limits apply **within each workbench**, not globally across workbenches:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEPTH LIMITS: PER-WORKBENCH                               │
│                                                                              │
│   Workbench A (max_depth: 5)          Workbench B (max_depth: 3)            │
│   ──────────────────────────          ──────────────────────────            │
│                                                                              │
│   Request A-1 (depth: 0)                                                     │
│   └── Request A-2 (depth: 1)                                                 │
│       └── Request A-3 (depth: 2) ─── creates cross-WB child ───▶            │
│                                       Request B-1 (depth: 0, global: 3)     │
│                                       └── Request B-2 (depth: 1, global: 4)  │
│                                           └── Request B-3 (depth: 2, global: 5)
│                                                                              │
│   • depth resets to 0 when entering new workbench                            │
│   • global_depth counts total across all workbenches                         │
│   • Each workbench enforces its own max_depth limit                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Default and Recommendations

| Aspect | Value |
|--------|-------|
| **Default max_depth** | 5 (per workbench) |
| **Practical recommendation** | ≤5 levels for maintainability |
| **Minimum** | 1 (at least one level of child requests) |
| **Maximum** | 10 (platform limit per workbench) |

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
    workbench_id: "fraud-ops"
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

Request Lifecycle Manager provides an API to retrieve compiled context including ancestor context:

```yaml
# GET /requests/{request_id}/compiled-context
# Returns context from current request + all ancestors

response:
  request_id: "req-grandchild-001"
  workbench_id: "fraud-ops"
  
  # Ancestor chain (root first) — may include cross-workbench ancestors
  ancestor_context:
    - request_id: "req-root-001"
      workbench_id: "fraud-ops"           # Same workbench
      depth: 0
      context:
        version: "v3"
        constraints: [...]
        verified_facts: [...]
        applicable_sops: [...]
    
    - request_id: "req-child-001"
      workbench_id: "fraud-ops"           # Same workbench
      depth: 1
      context:
        version: "v2"
        constraints: [...]
        verified_facts: [...]
  
  # Current request context
  current_context:
    request_id: "req-grandchild-001"
    workbench_id: "fraud-ops"
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

### Cross-Workbench Context Compilation

For requests with cross-workbench ancestors, context is compiled by fetching from each workbench:

```yaml
# GET /requests/{request_id}/compiled-context
# Request B-1 in Workbench B with parent A-1 in Workbench A

response:
  request_id: "req-B-1"
  workbench_id: "customer-lifecycle-ops"
  
  # Ancestor context includes cross-workbench parent
  ancestor_context:
    - request_id: "req-A-1"
      workbench_id: "retail-loans-workbench"  # Different workbench!
      depth: 0
      context:
        version: "v2"
        verified_facts:
          - type: customer_identity
            customer_id: "cust-12345"
          - type: loan_application
            loan_amount: 500000
            loan_purpose: "home_purchase"
        constraints:
          - "Loan requires AML clearance"
  
  current_context:
    request_id: "req-B-1"
    workbench_id: "customer-lifecycle-ops"
    depth: 0                               # Depth resets in new workbench
    context:
      version: "v1"
      verified_facts: []                   # Initially empty
```

**How Cross-Workbench Context is Fetched:**

```
Request Lifecycle Manager (child workbench)
    │
    ├── Local context (same-workbench ancestors)
    │       └── Direct database query
    │
    └── Cross-workbench context (per ancestor workbench)
            └── HTTP call using ancestor_context_token
                    │
                    ▼
            Request Lifecycle Manager (ancestor workbench)
                    │
                    └── Validates token, returns context
```

→ One API call per unique workbench in the ancestor chain.

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

### Cross-Workbench Cascade (Best-Effort)

For cross-workbench parent-child relationships, cascade is **best-effort**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CROSS-WORKBENCH LIFECYCLE CASCADE                         │
│                                                                              │
│   Workbench A                           Workbench B                          │
│   ──────────                           ──────────                            │
│                                                                              │
│   Parent Request                        Child Request                        │
│   ┌─────────────────┐                   ┌─────────────────┐                  │
│   │ COMPLETED       │                   │ ACTIVE          │                  │
│   └────────┬────────┘                   └────────┬────────┘                  │
│            │                                     │                           │
│            │  ─── Cascade notification ────────▶ │                           │
│            │      (async, with retry)            ▼                           │
│            │                            ┌─────────────────┐                  │
│            │                            │ COMPLETED       │                  │
│            │                            │ reason:         │                  │
│            │                            │ PARENT_COMPLETED│                  │
│            │                            └─────────────────┘                  │
│                                                                              │
│   If cascade fails after retries:                                            │
│   • Child marked as potentially orphaned                                     │
│   • Cleanup job will reconcile                                               │
│   • Access tokens revoked                                                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

| Aspect | Same-Workbench | Cross-Workbench |
|--------|----------------|-----------------|
| **Semantics** | Synchronous | Asynchronous (best-effort) |
| **Retry** | Not needed | 3 attempts with exponential backoff |
| **Failure handling** | Guaranteed | Mark as orphaned for cleanup |
| **Token revocation** | N/A | Automatic on parent completion |

### Child Completion Does Not Affect Parent

When a child request completes:

- Child's result is returned to the invoking application
- Parent request continues processing
- Parent decides next steps based on child result
- Child context is **isolated** — does not merge into parent

---

## Request Sentinel Child Requests

Request Sentinels are AI agents that observe and/or participate in requests. When a sentinel enrolls in a request, a child request is created using the sentinel's own scenario.

### Sentinel Child Request Characteristics

| Aspect | Behavior |
|--------|----------|
| **Scenario** | Child uses sentinel's scenario (NOT parent's scenario) |
| **Context Inheritance** | By reference (same as regular child requests) |
| **Lifecycle Cascade** | Standard cascade applies (parent completion → child completion) |
| **Observer** | Sentinel is automatically the primary observer of its child request |

### Sentinel Child Request Structure

```yaml
child_request:
  id: "req-sentinel-child-001"
  parent_request_id: "req-parent-001"
  workbench_id: "acme-disputes"
  scenario_id: "token-usage-governance"  # Sentinel's scenario, NOT parent's
  
  hierarchy:
    parent_request_id: "req-parent-001"
    root_request_id: "req-parent-001"
    depth: 1
    child_type: "sentinel"  # Distinguishes from tool/agent invocation
  
  # Sentinel-specific metadata
  sentinel_metadata:
    sentinel_id: "token-usage-governance"
    participation_mode: "observe_and_participate"
    enrolled_at: "2026-01-14T10:30:00Z"
    enrollment_trigger: "on_request_creation"
  
  status: "ACTIVE"
```

### Stale Update Handling

When a parent request completes or is cancelled:

1. All sentinel child requests are marked `COMPLETED` or `CANCELLED` (standard cascade)
2. Any REQUEST_UPDATE received after completion is **not delivered** to sentinels
3. Sentinel's child request status reflects parent's terminal status

If a sentinel receives an update for an already-completed child request:
- The sentinel can detect this via the child request status
- No action is expected — the monitoring context is closed
- Any pending actions in the sentinel should be gracefully abandoned

### Multiple Sentinels on Same Request

Multiple Request Sentinels can enroll in the same parent request:

```
Parent Request (depth=0)
├── Sentinel Child A (depth=1) — Token Usage Governance
├── Sentinel Child B (depth=1) — Compliance Monitor
└── Sentinel Child C (depth=1) — Quality Assurance Sampler
```

Each sentinel:
- Has its own independent child request
- Receives the same REQUEST_UPDATE notifications
- Operates in isolation from other sentinels
- Uses its own scenario for processing

### COG Sentinel Child Requests (Cross-Workbench)

COG Sentinels (sentinels defined in COGW workbenches) create child requests across workbench boundaries:

```
TARGET WORKBENCH (production-loans)        COGW WORKBENCH (acme-cogw)
─────────────────────────────────          ───────────────────────────

Parent Request (req-12345)                  COG Child Request (cog-req-67890)
├── scenario: loan-application              ├── scenario: token-governance
├── depth: 0                                ├── parent:
│                                           │     request_id: req-12345
│                                           │     workbench_id: production-loans
│                                           │     cross_workbench: true
│                                           │     context_token: "jwt-token"
│                                           └── depth: 0 (resets in new workbench)
```

| Aspect | Behavior |
|--------|----------|
| **Parent Workbench** | Target workbench where parent request lives |
| **Child Workbench** | COGW workbench where COG Sentinel is defined |
| **Context Access** | Via cross-workbench context token (same as Cross-Workbench Context Sharing) |
| **Lifecycle Cascade** | Best-effort cascade (parent completion → child notification) |
| **Depth** | Resets in new workbench (per Cross-Workbench Context Sharing) |

→ See [COGW Signal Forwarding](../../../olympus-seer-docs/seer-design/subsystems/cognitive-operations-governance-workbench/signal-forwarding.md) for details.

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

There are two patterns for cross-workbench invocations:

### Pattern 1: No Context Sharing (Default)

When invoking a scenario in a **different workbench** without context sharing configured:

| Aspect | Behavior |
|--------|----------|
| **Relationship** | No parent-child relationship |
| **Context** | No implicit sharing — invoker must explicitly forward |
| **Lifecycle** | Independent — no cascade |
| **Terminology** | "External invocation" not "child request" |

**Explicit Context Forwarding:**

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

| Actor | Responsibility |
|-------|----------------|
| **Publisher** (target workbench) | Defines what context the tool/machine expects in its contract |
| **Consumer** (invoking workbench) | Explicitly provides required context per contract |

### Pattern 2: With Context Sharing (Configured)

When both workbenches configure `WorkbenchContextSharingSpec`:

| Aspect | Behavior |
|--------|----------|
| **Relationship** | Parent-child relationship created |
| **Context** | Automatic inheritance via access tokens |
| **Lifecycle** | Cascade (best-effort) |
| **Terminology** | Cross-workbench "child request" |

**Automatic Context Inheritance:**

```python
# Cross-workbench invocation with context sharing configured
# Child automatically inherits parent context via tokens
result = await scenario_client.invoke(
    workbench="customer-lifecycle-ops",
    scenario="aml-clearance-check",
    input={
        "customer_id": "cust-12345"
        # No need to manually forward context!
        # Child will access parent context via compiled-context API
    }
)
```

→ See [Cross-Workbench Context Sharing](../../02-system-design/implementation-concepts/workbench-context-sharing.md) for configuration.

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
- [Workbench as a Machine](../../09-composite-systems-and-patterns/workbench-as-a-machine.md) — Cross-workbench invocations (no parent-child by default)
- [Cross-Workbench Context Sharing](../../02-system-design/implementation-concepts/workbench-context-sharing.md) — Cross-workbench parent-child relationships
- [Cross-Workbench Context Sharing Guide](../../10-guides/cross-workbench-context-sharing-guide.md) — Step-by-step configuration guide

---

## References

- [ADR-0066: Request Hierarchy and Context Inheritance](../../decision-logs/0066-request-hierarchy-context-inheritance.md)
- [ADR-0115: Cross-Workbench Context Sharing](../../decision-logs/0115-cross-workbench-context-sharing.md)

