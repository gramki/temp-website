# Cross-Workbench Context Sharing

> **Category:** Composite Patterns

---

## Overview

**Cross-Workbench Context Sharing** extends the request hierarchy model to support parent-child relationships across workbench boundaries. This enables scenarios in different workbenches to establish parent-child request relationships with shared context, supporting cross-domain agent collaboration while maintaining security boundaries.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Request** as an operation instance with context. This implementation extends the request hierarchy (previously same-workbench only) to support cross-workbench parent-child relationships.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Operation (Request) | Cross-Workbench Request Hierarchy | Parent-child across workbenches |
| Context | Ancestor Context Access | Context sharing via tokens |
| Domain (Workbench) | WorkbenchContextSharingSpec | Explicit sharing configuration |

### Gap This Fills

The base request hierarchy is same-workbench only. This pattern addresses:
1. **Cross-domain collaboration**: How can agents in different domains share context?
2. **Explicit authorization**: How is cross-workbench context access controlled?
3. **Security boundaries**: How is implicit data leakage prevented?

---

## Definition

**Cross-Workbench Context Sharing** is a pattern where:
- Two workbenches explicitly configure mutual context sharing
- Parent requests in one workbench can create child requests in another
- Child requests access parent context via request-specific access tokens
- Lifecycle events cascade across workbench boundaries (best-effort)

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Cross-workbench; same subscription only |
| **Configuration** | Bidirectional mutual acknowledgment required |
| **Granularity** | Workbench-level and/or Scenario-level |
| **Lifecycle** | Configured by Process Architect; validated at deployment time |
| **Ownership** | Each workbench owns its own sharing configuration |

---

## Rationale

### Why This Design?

Cross-Workbench Context Sharing enables:
1. **Cross-domain collaboration**: Agents in different operational domains can collaborate with full context
2. **Explicit consent**: Both workbenches must explicitly agree to share
3. **Security by default**: No implicit cross-workbench data sharing
4. **Flexible granularity**: Share with entire workbench or specific scenarios

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Implicit cross-workbench hierarchy** | Security risk; data leakage across domains |
| **Context forwarding only** | Cumbersome; must serialize/deserialize context manually |
| **Single mega-workbench** | Violates domain separation; operational complexity |
| **No cross-workbench support** | Limits multi-domain agent collaboration |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0066](../../decision-logs/0066-request-hierarchy-context-inheritance.md) | Request hierarchy and context inheritance (same-workbench) |
| [ADR-0115](../../decision-logs/0115-cross-workbench-context-sharing.md) | Cross-workbench context sharing extension |

---

## Structure

### WorkbenchContextSharingSpec CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchContextSharingSpec
metadata:
  name: retail-loans-context-sharing
  namespace: acme-bank
  labels:
    hub.olympus.io/workbench: retail-loans-workbench
spec:
  # Reference to the workbench this spec configures
  workbench_ref:
    name: retail-loans-workbench
    subscription_id: sub-acme-prod
  
  # Workbenches/Scenarios that can be parents of requests in THIS workbench
  parent_contexts:
    # Workbench-level: Any scenario in treasury-ops can be a parent
    - type: workbench
      workbench_ref:
        name: treasury-ops-workbench
        subscription_id: sub-acme-prod
      enabled: true
    
    # Scenario-level: Only specific scenario from customer-ops
    - type: scenario
      workbench_ref:
        name: customer-lifecycle-ops
        subscription_id: sub-acme-prod
      scenario_ref:
        name: customer-verification
      enabled: true
  
  # Workbenches/Scenarios where THIS workbench can create child requests
  child_contexts:
    # Workbench-level: Can create children in customer-lifecycle-ops
    - type: workbench
      workbench_ref:
        name: customer-lifecycle-ops
        subscription_id: sub-acme-prod
      enabled: true
    
    # Scenario-level: Can create children in specific AML scenario
    - type: scenario
      workbench_ref:
        name: customer-lifecycle-ops
        subscription_id: sub-acme-prod
      scenario_ref:
        name: aml-clearance-check
      enabled: true
```

### ScenarioAutomationSpec Extension

Scenarios can specify additional context sharing on top of workbench defaults:

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAutomationSpec
metadata:
  name: credit-assessment-automation
  namespace: retail-loans-workbench
spec:
  normative_ref:
    name: credit-assessment-normative
    version: "1.0.0"
  
  application:
    ref:
      name: credit-assessment-agent
    runtime: seer
  
  triggers:
    - id: loan-application-received
      signal_source: loan-origination-system
  
  # Cross-workbench context sharing (extends WorkbenchContextSharingSpec)
  contextSharing:
    # Additional parent contexts for this scenario (union with workbench config)
    parent_contexts: []
    
    # Additional child contexts for this scenario (union with workbench config)
    child_contexts:
      - type: scenario
        workbench_ref:
          name: customer-lifecycle-ops
          subscription_id: sub-acme-prod
        scenario_ref:
          name: aml-clearance-check
```

### Union Logic

The effective context sharing configuration for a scenario is the **union** of:
1. `WorkbenchContextSharingSpec` for the workbench
2. `ScenarioAutomationSpec.contextSharing` for the specific scenario

```
Effective parent_contexts = WorkbenchSpec.parent_contexts ∪ ScenarioSpec.parent_contexts
Effective child_contexts = WorkbenchSpec.child_contexts ∪ ScenarioSpec.child_contexts
```

---

## Behavior

### Mutual Acknowledgment Requirement

Cross-workbench context sharing requires **mutual acknowledgment** — both sides must explicitly configure:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MUTUAL ACKNOWLEDGMENT REQUIREMENT                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   For W1 Scenario A to create child request in W2 Scenario B:               │
│                                                                              │
│   W1 WorkbenchContextSharingSpec         W2 WorkbenchContextSharingSpec     │
│   ┌─────────────────────────────┐        ┌─────────────────────────────┐    │
│   │ child_contexts:             │        │ parent_contexts:            │    │
│   │   - workbench_ref: W2       │   ✓    │   - workbench_ref: W1       │    │
│   │     enabled: true           │  ───▶  │     enabled: true           │    │
│   └─────────────────────────────┘        └─────────────────────────────┘    │
│                                                                              │
│   OR (more granular):                                                        │
│                                                                              │
│   W1 ScenarioAutomationSpec              W2 ScenarioAutomationSpec          │
│   ┌─────────────────────────────┐        ┌─────────────────────────────┐    │
│   │ contextSharing:             │        │ contextSharing:             │    │
│   │   child_contexts:           │        │   parent_contexts:          │    │
│   │     - scenario_ref: B       │   ✓    │     - scenario_ref: A       │    │
│   │       workbench_ref: W2     │  ───▶  │       workbench_ref: W1     │    │
│   └─────────────────────────────┘        └─────────────────────────────┘    │
│                                                                              │
│   BOTH sides must configure — one-sided configuration is NOT sufficient     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Subscription Validation

Context sharing is validated at **configuration time**:

| Validation | When | Behavior |
|------------|------|----------|
| **Subscription membership** | CRD deployment | Both workbenches must be in the same subscription |
| **Workbench existence** | CRD deployment | Referenced workbenches must exist |
| **Scenario existence** | CRD deployment | Referenced scenarios must exist |
| **Mutual acknowledgment** | CRD deployment | Logs warning if one-sided (not an error) |
| **Effective config** | Request creation | Runtime check of complete mutual acknowledgment |

### Request Entity Extension

Cross-workbench child requests include additional fields:

```yaml
# Request entity with cross-workbench hierarchy fields
request:
  id: "req-child-001"
  workbench_id: "customer-lifecycle-ops"
  scenario_id: "aml-clearance-check"
  
  # Standard hierarchy fields
  hierarchy:
    parent_request_id: "req-parent-001"
    root_request_id: "req-parent-001"
    depth: 0                               # Depth within THIS workbench (resets)
    
  # Cross-workbench hierarchy fields
  cross_workbench:
    parent_workbench_id: "retail-loans-workbench"
    root_workbench_id: "retail-loans-workbench"
    global_depth: 1                        # Total depth across all workbenches
    ancestor_context_tokens:
      - workbench_id: "retail-loans-workbench"
        token: "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
        scope: ["req-parent-001"]          # Request IDs accessible via this token
        expires_at: "2026-01-15T10:30:00Z"
  
  status: "ACTIVE"
  created_at: "2026-01-14T10:15:00Z"
```

### Access Token Management

Each workbench in the ancestor chain provides a unique access token:

| Aspect | Description |
|--------|-------------|
| **Token scope** | Allows access to all requests in the ancestor chain from that workbench |
| **Token type** | JWT with request-specific claims |
| **Token lifetime** | Valid until parent request completes or is cancelled |
| **Token revocation** | Automatic on parent lifecycle completion |

### Context Compilation

When compiling context across workbenches:

```yaml
# GET /requests/req-child-001/compiled-context

response:
  request_id: "req-child-001"
  workbench_id: "customer-lifecycle-ops"
  
  # Ancestor context (includes cross-workbench parent)
  ancestor_context:
    - request_id: "req-parent-001"
      workbench_id: "retail-loans-workbench"  # Different workbench
      depth: 0
      context:
        version: "v2"
        verified_facts:
          - type: customer_identity
            customer_id: "cust-12345"
            verified: true
          - type: loan_application
            loan_amount: 500000
            loan_purpose: "home_purchase"
        constraints:
          - "Loan requires AML clearance"
  
  # Current request context
  current_context:
    request_id: "req-child-001"
    workbench_id: "customer-lifecycle-ops"
    depth: 0  # First request in THIS workbench
    context:
      version: "v1"
      verified_facts: []
```

Context is fetched from each workbench using the corresponding access token:

```
Request Lifecycle Manager (child workbench)
    │
    ├── Local context (same workbench ancestors)
    │       └── Direct database query
    │
    └── Cross-workbench context (each ancestor workbench)
            └── HTTP call to ancestor workbench's RLM using access token
```

### Lifecycle Cascade

Parent completion/cancellation cascades to child requests in other workbenches:

| Event | Behavior |
|-------|----------|
| **Parent COMPLETED** | Child marked COMPLETED with reason PARENT_COMPLETED (best-effort) |
| **Parent CANCELLED** | Child marked CANCELLED with reason PARENT_CANCELLED (best-effort) |
| **Network failure** | Retry with exponential backoff; eventually mark as orphaned |

**Best-effort semantics**: Cross-workbench cascade is asynchronous with retry. If cascade fails after retries, the child request is marked as potentially orphaned for cleanup.

### Depth Limits

Depth limits apply **per-workbench**, not globally:

```yaml
# Workbench A config
request_hierarchy:
  max_depth: 5    # Applies to requests within Workbench A

# Workbench B config  
request_hierarchy:
  max_depth: 3    # Applies to requests within Workbench B
```

A request in Workbench B that is a child of a request in Workbench A:
- Has `depth: 0` in Workbench B (first request in that workbench)
- Has `global_depth: 1` (one level from root across all workbenches)

---

## Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Signal Exchange | ← routes through | Creates cross-workbench child requests |
| Request Lifecycle Manager | ↔ coordinates | Compiles context across workbenches |
| Process Architect Operator | ← validated by | Validates CRD at deployment |
| Notification Services | ← notifies via | Cascade completion notifications |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Same subscription** | Cross-workbench sharing only within same subscription |
| **Mutual acknowledgment** | Both workbenches must configure sharing |
| **Token-based access** | Context accessed only via valid access tokens |
| **Depth per workbench** | Depth limits apply within each workbench |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Cross-domain collaboration** | Agents in different domains can share context |
| ✅ **Explicit authorization** | No implicit data sharing; both sides must agree |
| ✅ **Security maintained** | Token-based access with automatic revocation |
| ✅ **Flexible granularity** | Workbench or scenario level configuration |
| ✅ **Context inheritance** | Full ancestor chain accessible |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Network latency** | Context compilation requires cross-workbench calls |
| ⚠️ **Configuration complexity** | Both sides must configure correctly |
| ⚠️ **Best-effort cascade** | Lifecycle cascade may be delayed |
| ⚠️ **Token management** | Additional token lifecycle to manage |

---

## Examples

### Example 1: Retail Loans → AML Clearance

Credit assessment in Retail Loans needs AML clearance from Customer Lifecycle Operations:

```yaml
# Retail Loans Workbench configuration
apiVersion: hub.olympus.io/v1
kind: WorkbenchContextSharingSpec
metadata:
  name: retail-loans-context-sharing
  namespace: acme-bank
spec:
  workbench_ref:
    name: retail-loans-workbench
    subscription_id: sub-acme-prod
  
  parent_contexts: []  # No workbench is parent to this
  
  child_contexts:
    - type: scenario
      workbench_ref:
        name: customer-lifecycle-ops
      scenario_ref:
        name: aml-clearance-check
      enabled: true
---
# Customer Lifecycle Ops Workbench configuration
apiVersion: hub.olympus.io/v1
kind: WorkbenchContextSharingSpec
metadata:
  name: customer-ops-context-sharing
  namespace: acme-bank
spec:
  workbench_ref:
    name: customer-lifecycle-ops
    subscription_id: sub-acme-prod
  
  parent_contexts:
    - type: scenario
      workbench_ref:
        name: retail-loans-workbench
      scenario_ref:
        name: credit-assessment
      enabled: true
  
  child_contexts: []
```

---

## Implementation Notes

### For Process Architects

- Configure `WorkbenchContextSharingSpec` for workbench-wide sharing
- Use `ScenarioAutomationSpec.contextSharing` for scenario-specific sharing
- Ensure mutual acknowledgment with partner workbench
- Verify both workbenches are in the same subscription

### For Developers

- Access parent context via compiled-context API
- Handle potential latency for cross-workbench context
- Design for context being unavailable (parent completed)
- Use access tokens appropriately

### For Operators

- Monitor cross-workbench context access patterns
- Review cascade completion success rates
- Manage orphaned child requests (failed cascade)

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Request Hierarchy](../../04-subsystems/request-management/request-hierarchy.md) | Extended for cross-workbench |
| [Workbench as Machine](./workbench-as-machine.md) | Alternative pattern (no context inheritance) |
| [Signal Exchange](./signal-exchange.md) | Routes cross-workbench requests |

---

## References

- [Request Hierarchy Subsystem](../../04-subsystems/request-management/request-hierarchy.md)
- [Workbench Context Sharing Subsystem](../../04-subsystems/workbench-management/workbench-context-sharing.md)
- [ADR-0115: Cross-Workbench Context Sharing](../../decision-logs/0115-cross-workbench-context-sharing.md)
- [Cross-Workbench Context Sharing Guide](../../10-guides/cross-workbench-context-sharing-guide.md)
