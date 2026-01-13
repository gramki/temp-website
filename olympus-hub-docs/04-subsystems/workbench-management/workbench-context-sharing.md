# Workbench Context Sharing

> **Status:** ✅ Complete  
> **Last Updated:** 2026-01-14  
> **Parent:** [Workbench Management](./README.md)

---

## Overview

Workbench Context Sharing enables parent-child request relationships across workbench boundaries. This allows agents in different operational domains to collaborate with shared context while maintaining explicit authorization controls.

---

## WorkbenchContextSharingSpec CRD

### Schema

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
    name: string                          # Workbench name (required)
    subscription_id: string               # Subscription ID (required)
  
  # Workbenches/Scenarios that can be parents of requests in THIS workbench
  parent_contexts:
    - type: workbench | scenario          # Granularity (required)
      workbench_ref:
        name: string                      # Parent workbench name (required)
        subscription_id: string           # Same subscription (required)
      scenario_ref:                       # Only for type: scenario
        name: string                      # Scenario name
      enabled: boolean                    # Enable/disable (default: true)
  
  # Workbenches/Scenarios where THIS workbench can create child requests
  child_contexts:
    - type: workbench | scenario          # Granularity (required)
      workbench_ref:
        name: string                      # Child workbench name (required)
        subscription_id: string           # Same subscription (required)
      scenario_ref:                       # Only for type: scenario
        name: string                      # Scenario name
      enabled: boolean                    # Enable/disable (default: true)
```

### Field Descriptions

| Field | Description |
|-------|-------------|
| `workbench_ref` | Reference to the workbench this spec applies to |
| `parent_contexts` | List of workbenches/scenarios that can be parents |
| `child_contexts` | List of workbenches/scenarios where children can be created |
| `type` | `workbench` for all scenarios, `scenario` for specific scenario |
| `enabled` | Toggle to enable/disable without deleting config |

---

## Validation Rules

### At CRD Deployment Time

| Validation | Rule |
|------------|------|
| **Subscription membership** | All referenced workbenches must be in the same subscription |
| **Workbench existence** | Referenced workbenches must exist |
| **Scenario existence** | Referenced scenarios must exist |
| **Self-reference** | Cannot reference own workbench in parent_contexts or child_contexts |
| **Circular reference** | Circular configurations are allowed (A can be parent and child of B) — useful for bidirectional collaboration scenarios |

### Mutual Acknowledgment Warning

If a workbench configures a parent or child context but the other side has not configured the reciprocal:

```yaml
# Warning logged (not an error)
warning:
  code: "CONTEXT_SHARING_ONE_SIDED"
  message: "retail-loans-workbench lists customer-lifecycle-ops as child, but customer-lifecycle-ops does not list retail-loans-workbench as parent"
  severity: "WARNING"
```

One-sided configuration is **not an error** at deployment time. The runtime will reject cross-workbench child request creation if mutual acknowledgment is missing.

### At Runtime (Request Creation)

| Validation | Rule |
|------------|------|
| **Mutual acknowledgment** | Both sides must have configured reciprocal sharing |
| **Enabled flags** | Both sides must have `enabled: true` |
| **Token generation** | Access token created for child to access parent context |

---

## Integration with ScenarioAutomationSpec

Scenarios can extend workbench-level context sharing via `contextSharing` section:

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAutomationSpec
metadata:
  name: credit-assessment-automation
spec:
  # ... other fields ...
  
  contextSharing:
    parent_contexts:
      - type: scenario
        workbench_ref:
          name: treasury-ops
          subscription_id: sub-acme-prod
        scenario_ref:
          name: collateral-valuation
    
    child_contexts:
      - type: scenario
        workbench_ref:
          name: customer-lifecycle-ops
          subscription_id: sub-acme-prod
        scenario_ref:
          name: aml-clearance-check
```

### Union Logic

Effective context sharing = `WorkbenchContextSharingSpec` ∪ `ScenarioAutomationSpec.contextSharing`

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        UNION LOGIC                                           │
│                                                                              │
│   WorkbenchContextSharingSpec              ScenarioAutomationSpec            │
│   ───────────────────────────              ───────────────────────           │
│                                                                              │
│   child_contexts:                          contextSharing:                   │
│     - workbench: customer-ops               child_contexts:                  │
│       subscription: sub-acme-prod            - scenario: aml-clearance       │
│                                               workbench: customer-ops         │
│                                               subscription: sub-acme-prod     │
│                                                                              │
│                              ↓                                               │
│                                                                              │
│   Effective child_contexts for Scenario:                                     │
│     - workbench: customer-ops (from WorkbenchSpec)                          │
│     - scenario: aml-clearance in customer-ops (from ScenarioSpec)           │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Access Token Management

### Token Structure

```yaml
# JWT claims for cross-workbench context access
token:
  iss: "hub.olympus.io"
  sub: "req-child-001"                      # Child request ID
  aud: "retail-loans-workbench"             # Target workbench
  iat: 1705225800                           # Issued at
  exp: 1705312200                           # Expires at (or on parent completion)
  
  # Custom claims
  parent_request_id: "req-parent-001"
  scope:
    - "req-parent-001"                      # Accessible requests
    - "req-grandparent-001"                 # (entire ancestor chain)
  access_type: "context_read"
```

### Token Lifecycle

| Event | Token Behavior |
|-------|----------------|
| **Child request created** | Token generated and attached to child |
| **Parent completes** | Token revoked (child notified) |
| **Parent cancels** | Token revoked (child notified) |
| **Token expires** | Child can no longer access parent context |

### Token Validation

When child workbench requests parent context:

```
1. Child RLM receives compiled-context request
2. For cross-workbench ancestor, RLM uses stored token
3. HTTP call to parent workbench RLM with token
4. Parent RLM validates:
   - Token signature (valid JWT)
   - Token not expired
   - Token not revoked (parent request still active)
   - Request ID in scope
5. Parent RLM returns context
```

---

## Examples

### Example 1: Retail Loans → Customer Lifecycle Ops

```yaml
# Retail Loans Workbench
apiVersion: hub.olympus.io/v1
kind: WorkbenchContextSharingSpec
metadata:
  name: retail-loans-context-sharing
  namespace: acme-bank
spec:
  workbench_ref:
    name: retail-loans-workbench
    subscription_id: sub-acme-prod
  
  parent_contexts: []
  
  child_contexts:
    - type: scenario
      workbench_ref:
        name: customer-lifecycle-ops
        subscription_id: sub-acme-prod
      scenario_ref:
        name: aml-clearance-check
      enabled: true
---
# Customer Lifecycle Ops Workbench
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
        subscription_id: sub-acme-prod
      scenario_ref:
        name: credit-assessment
      enabled: true
  
  child_contexts: []
```

### Example 2: Workbench-Level Sharing

```yaml
# Treasury Ops — share with entire Retail Loans workbench
apiVersion: hub.olympus.io/v1
kind: WorkbenchContextSharingSpec
metadata:
  name: treasury-context-sharing
spec:
  workbench_ref:
    name: treasury-ops-workbench
    subscription_id: sub-acme-prod
  
  parent_contexts: []
  
  child_contexts:
    - type: workbench                      # All scenarios in target
      workbench_ref:
        name: retail-loans-workbench
        subscription_id: sub-acme-prod
      enabled: true
```

---

## Operator Reconciliation

The Process Architect Operator processes `WorkbenchContextSharingSpec`:

| Action | Behavior |
|--------|----------|
| **Create** | Validate references; store configuration; log one-sided warnings |
| **Update** | Re-validate; update configuration; propagate to affected scenarios |
| **Delete** | Remove configuration; existing cross-workbench requests unaffected |

### Reconciliation Steps

```
1. Validate workbench_ref exists
2. Validate subscription membership for all references
3. For each parent_context/child_context:
   a. Validate workbench exists
   b. Validate scenario exists (if type: scenario)
   c. Check for reciprocal configuration (log warning if missing)
4. Store effective configuration in workbench registry
5. Notify Signal Exchange of updated context sharing rules
```

---

## Related Documentation

- [Cross-Workbench Context Sharing Concept](../../02-system-design/implementation-concepts/workbench-context-sharing.md)
- [Request Hierarchy](../request-management/request-hierarchy.md)
- [Signal Exchange](../signal-exchange/README.md)
- [Process Architect Operator](../operators/process-architect-operator.md)
- [Cross-Workbench Context Sharing Guide](../../10-guides/cross-workbench-context-sharing-guide.md)

---

## References

- [ADR-0115: Cross-Workbench Context Sharing](../../decision-logs/0115-cross-workbench-context-sharing.md)
