# COGW Operator

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14  
> **Design Level**: C2 (Container) with C3 (Component) details for reconciliation logic

---

## Overview

The COGW Operator is a subscription-level operator that manages COG Sentinel deployment across target workbenches. It watches COG Sentinels in all COGW workbenches, evaluates cogSpec patterns, and syncs read-only specs to target workbenches.

---

## Operator Scope

### One Operator Per Subscription

| Aspect | Description |
|--------|-------------|
| **Scope** | Subscription-level (not per-COGW workbench) |
| **Instance** | One operator per subscription |
| **Watch** | All COG Sentinels in all COGW workbenches |
| **Enumerate** | All workbenches in subscription |
| **Access** | Subscription-level access to all workbenches |

### Why Subscription Scope

| Reason | Description |
|--------|-------------|
| **Centralized management** | Single point for all COG Sentinel reconciliation |
| **Consistent pattern evaluation** | All patterns evaluated against same workbench list |
| **Efficient workbench enumeration** | One subscription query, not multiple |
| **Simpler operations** | Fewer operator instances to manage |

---

## Operator Responsibilities

### Primary Functions

| Function | Description |
|----------|-------------|
| **Watch COG Sentinels** | Monitor all COG Sentinels in all COGW workbenches |
| **Evaluate Patterns** | Apply cogSpec patterns against subscription workbenches |
| **Sync Specs** | Create/update read-only specs in target workbenches |
| **Register Enrollment** | Register COG Sentinels for auto-enrollment in Signal Exchange |
| **Handle Updates** | Sync changes to all target workbenches |
| **Handle Deletions** | Remove specs from target workbenches |
| **Handle Workbench Changes** | Re-evaluate when workbenches are added/removed |

### Watch Resources

| Resource | Purpose |
|----------|---------|
| `SentinelSpec` with COG label | Detect COG Sentinel creation/update/deletion |
| `SentinelScenarioNormativeSpec` | Sync normative specs |
| `SentinelScenarioAutomationSpec` | Sync automation specs |
| `SentinelScenarioDeploymentSpec` | Detect cogSpec, sync deployment specs |
| `Workbench` | Detect workbench creation/deletion |

---

## Reconciliation Loop (C3 Detail)

### Trigger Events

| Event | Action |
|-------|--------|
| COG Sentinel created | Evaluate patterns, sync to matching workbenches |
| COG Sentinel updated | Re-sync to all target workbenches |
| COG Sentinel deleted | Remove from all target workbenches |
| Workbench created | Evaluate all COG Sentinels, sync if matched |
| Workbench deleted | Clean up any synced specs |
| cogSpec patterns changed | Re-evaluate, add/remove workbenches |

### Reconciliation Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COGW OPERATOR RECONCILIATION LOOP                         │
│                                                                              │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │ 1. WATCH: Detect change event                                       │    │
│   │    - COG Sentinel created/updated/deleted                           │    │
│   │    - Workbench created/deleted                                      │    │
│   └─────────────────────────────────┬──────────────────────────────────┘    │
│                                     │                                        │
│                                     ▼                                        │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │ 2. ENUMERATE: Get current state                                     │    │
│   │    - List all COGW workbenches in subscription                      │    │
│   │    - List all COG Sentinels in each COGW                            │    │
│   │    - List all non-COGW workbenches in subscription                  │    │
│   └─────────────────────────────────┬──────────────────────────────────┘    │
│                                     │                                        │
│                                     ▼                                        │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │ 3. EVALUATE: For each COG Sentinel, evaluate cogSpec patterns      │    │
│   │    - Apply pattern matching algorithm                               │    │
│   │    - Determine target workbenches (matching)                        │    │
│   │    - Determine removed workbenches (no longer matching)             │    │
│   └─────────────────────────────────┬──────────────────────────────────┘    │
│                                     │                                        │
│                                     ▼                                        │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │ 4. SYNC: For each target workbench                                  │    │
│   │    - Create/update read-only SentinelScenarioSpec copies            │    │
│   │    - Add read-only annotations                                      │    │
│   │    - Add source annotations                                         │    │
│   └─────────────────────────────────┬──────────────────────────────────┘    │
│                                     │                                        │
│                                     ▼                                        │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │ 5. REGISTER: Register COG Sentinels in Signal Exchange             │    │
│   │    - For each target workbench, register for auto-enrollment        │    │
│   │    - Include participation filters                                  │    │
│   │    - Configure webhook forwarding to COGW                           │    │
│   └─────────────────────────────────┬──────────────────────────────────┘    │
│                                     │                                        │
│                                     ▼                                        │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │ 6. CLEANUP: For removed workbenches                                 │    │
│   │    - Delete read-only specs                                         │    │
│   │    - Deregister from Signal Exchange                                │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Reconciliation Pseudocode

```python
def reconcile_cog_sentinel(cog_sentinel):
    # 1. Get cogSpec from deployment spec
    deployment_spec = get_deployment_spec(cog_sentinel)
    cog_spec = deployment_spec.spec.cogSpec
    
    # 2. Enumerate all non-COGW workbenches in subscription
    all_workbenches = list_workbenches(subscription_id)
    target_workbenches = [
        wb for wb in all_workbenches 
        if wb.spec.workbench_type != "cogw"
    ]
    
    # 3. Evaluate patterns for each workbench
    matching_workbenches = []
    for workbench in target_workbenches:
        if evaluate_patterns(workbench.name, cog_spec.workbench_patterns):
            matching_workbenches.append(workbench)
    
    # 4. Get previously synced workbenches
    previously_synced = get_synced_workbenches(cog_sentinel)
    
    # 5. Calculate additions and removals
    to_add = set(matching_workbenches) - set(previously_synced)
    to_remove = set(previously_synced) - set(matching_workbenches)
    to_update = set(matching_workbenches) & set(previously_synced)
    
    # 6. Sync to new workbenches
    for workbench in to_add:
        create_readonly_specs(workbench, cog_sentinel)
        register_signal_exchange(workbench, cog_sentinel)
    
    # 7. Update existing workbenches
    for workbench in to_update:
        update_readonly_specs(workbench, cog_sentinel)
    
    # 8. Remove from old workbenches
    for workbench in to_remove:
        delete_readonly_specs(workbench, cog_sentinel)
        deregister_signal_exchange(workbench, cog_sentinel)

def evaluate_patterns(workbench_name, patterns):
    """Apache-style sequential pattern evaluation."""
    for rule in patterns:
        if wildcard_match(workbench_name, rule.pattern):
            return rule.action == "allow"
    return False  # Default deny
```

---

## Read-only Spec Sync

### Spec Creation

When syncing to a target workbench, the operator creates:

1. `SentinelScenarioNormativeSpec` (read-only copy)
2. `SentinelScenarioAutomationSpec` (read-only copy)
3. `SentinelScenarioDeploymentSpec` (read-only copy)
4. `SentinelSpec` (read-only reference)

### Read-only Annotations

```yaml
metadata:
  name: token-governance-sentinel  # Same name as source
  namespace: target-workbench      # Target workbench namespace
  annotations:
    sentinel.olympus.io/read-only: "true"
    sentinel.olympus.io/cog-sentinel-source: "acme-cogw/token-governance-sentinel"
    sentinel.olympus.io/sync-timestamp: "2026-01-14T10:30:00Z"
  labels:
    sentinel.olympus.io/cog-sentinel: "true"
    sentinel.olympus.io/source-workbench: acme-cogw
```

### Validation Enforcement

| Operation | Behavior |
|-----------|----------|
| **Create** | Only by COGW Operator (validated by annotation) |
| **Update** | Rejected if `read-only: "true"` annotation present |
| **Delete** | Only by COGW Operator |
| **Enable/Disable** | Allowed via Sentinel Levers (local control) |

---

## Signal Exchange Registration

### Registration Data

When registering a COG Sentinel for a target workbench:

```yaml
registration:
  sentinel_id: token-governance-sentinel
  source_workbench: acme-cogw
  target_workbench: production-loans
  participation:
    mode: observe_and_participate
    filters:
      scenario_whitelist: ["*"]
      on_request_update:
        enabled: true
        update_filter_policy: |
          allow { input.payload.metrics.token_usage != null }
  webhook:
    target_url: "https://seer.internal/cogw/acme-cogw/sentinel/token-governance/webhook"
    retry_policy:
      max_retries: 3
```

### Signal Exchange Behavior

1. **Request Created** in target workbench
2. **Filter Evaluation** — Apply COG Sentinel's participation filters
3. **Match** — Forward signal to COGW, create child request
4. **No Match** — No action

---

## Workbench Change Handling

### New Workbench Created

When a new workbench is created in the subscription:

1. **Enumerate** all COG Sentinels in all COGWs
2. **Evaluate** each COG Sentinel's cogSpec patterns
3. **Sync** if new workbench matches any pattern

### Workbench Deleted

When a workbench is deleted:

1. **Identify** synced COG Sentinel specs in deleted workbench
2. **Clean up** registrations (already handled by deletion)
3. **Update** operator state

---

## Operator CRD

### COGW Operator Configuration

```yaml
apiVersion: seer.olympus.io/v1
kind: COGWOperatorConfig
metadata:
  name: cogw-operator
  namespace: subscription-operators
spec:
  subscription_id: acme-subscription
  
  watch:
    # Resources to watch
    resources:
      - apiGroup: seer.olympus.io
        kind: SentinelSpec
        labelSelector:
          sentinel.olympus.io/cog-sentinel: "true"
      - apiGroup: seer.olympus.io
        kind: SentinelScenarioDeploymentSpec
      - apiGroup: hub.olympus.io
        kind: Workbench
  
  reconciliation:
    interval_seconds: 60
    retry_policy:
      max_retries: 3
      backoff_multiplier: 2.0
  
  logging:
    level: info
```

---

## Error Handling

### Common Errors

| Error | Handling |
|-------|----------|
| **Target workbench not found** | Skip, log warning, retry on next reconciliation |
| **Spec creation failed** | Retry with backoff |
| **Signal Exchange registration failed** | Retry, alert if persistent |
| **Read-only violation** | Block operation, log error |
| **Pattern syntax error** | Reject COG Sentinel creation |

### Reconciliation Retry

```yaml
reconciliation:
  retry_policy:
    max_retries: 3
    initial_delay_seconds: 5
    max_delay_seconds: 60
    backoff_multiplier: 2.0
```

---

## Related Documentation

- [COGW Specification](./cogw-specification.md) — COGW workbench type
- [COG Sentinel Specification](./cog-sentinel-specification.md) — COG Sentinel definition
- [Signal Forwarding](./signal-forwarding.md) — Signal forwarding mechanism
- [Administrative Controls](./administrative-controls.md) — Enable/disable controls
- [Seer Operator](../../hub-integration/training-spec-crd.md) — CRD reconciliation patterns

---

*COGW Operator manages subscription-wide COG Sentinel deployment through pattern-based workbench targeting and read-only spec synchronization.*
