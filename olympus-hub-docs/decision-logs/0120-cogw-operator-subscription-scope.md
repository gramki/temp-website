# ADR-0120: COGW Operator Subscription Scope

**Status**: Accepted  
**Date**: 2026-01-14  
**Category**: seer, hub-integration, operators

---

## Context

The COGW Operator manages COG Sentinel deployment across target workbenches. We need to determine the appropriate scope for this operator:

1. **What does the operator watch?** — COG Sentinels, workbenches, or both?
2. **Where does it run?** — Per-COGW, per-subscription, or platform-wide?
3. **What access does it need?** — Read/write access to workbenches?

### Requirements

1. Watch all COG Sentinels in all COGW workbenches within scope
2. Enumerate all workbenches in scope for pattern evaluation
3. Create/update/delete read-only specs in target workbenches
4. Register COG Sentinels for auto-enrollment in Signal Exchange
5. Handle workbench creation/deletion events

---

## Decision

### 1. One Operator Per Subscription

We will deploy one COGW Operator per subscription (not per-COGW or platform-wide):

```yaml
# One operator per subscription
apiVersion: seer.olympus.io/v1
kind: COGWOperatorDeployment
metadata:
  name: cogw-operator
  namespace: acme-subscription
spec:
  subscription_id: acme-subscription
```

### 2. Operator Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Watch COGW workbenches** | All `workbench_type: cogw` in subscription |
| **Watch COG Sentinels** | All sentinels with `cog-sentinel: true` label |
| **Watch Workbenches** | All workbenches in subscription (for pattern eval) |
| **Sync Specs** | Create/update read-only specs in target workbenches |
| **Register Auto-enrollment** | Register with Signal Exchange |

### 3. Subscription-Level Access

The operator has subscription-level access:

| Access | Scope | Purpose |
|--------|-------|---------|
| **Read** | All workbenches | Enumerate for pattern matching |
| **Write** | Target workbenches | Create read-only sentinel specs |
| **Read/Write** | COGW workbenches | Watch and manage COG Sentinels |
| **Write** | Signal Exchange | Register auto-enrollment |

---

## Alternatives Considered

### 1. One Operator Per COGW Workbench

Deploy an operator for each COGW workbench.

**Rejected because:**
- **Proliferation** — Many operators if many COGWs
- **Coordination** — Operators would need to coordinate on same targets
- **Inefficiency** — Each operator enumerates same workbench list
- **Complexity** — Multiple operators watching same resources

### 2. Single Platform-Wide Operator

One operator for all subscriptions.

**Rejected because:**
- **Blast radius** — Single failure affects all subscriptions
- **Scaling limits** — One operator watching many subscriptions
- **Security boundary** — Operator has access to all subscriptions
- **Multi-tenancy concerns** — Subscription isolation violated

### 3. Operator Per Workbench (Target Side)

Deploy operator in each target workbench to receive specs.

**Rejected because:**
- **Many operators** — One per workbench is inefficient
- **Pull vs Push** — Reverses the sync model
- **Discovery** — Target workbenches need to know about COGWs
- **Inconsistent** — Different model than other operators

---

## Consequences

### Positive

1. **Right scope** — Subscription is natural boundary for governance
2. **Centralized logic** — One operator per subscription simplifies debugging
3. **Efficient** — Single workbench enumeration, single watch stream
4. **Security** — Operator access limited to subscription
5. **Consistent** — Similar to other subscription-level operators

### Negative

1. **Subscription-level access** — Operator needs broad access within subscription
2. **Operator per subscription** — Increases total operator count vs platform-wide

### Neutral

1. **Standard pattern** — Follows typical Kubernetes operator model
2. **Lifecycle tied to subscription** — Operator created/deleted with subscription

---

## Implementation Notes

### Operator Deployment

The COGW Operator is deployed by the Subscription Provisioning Operator:

```python
def on_subscription_created(subscription):
    # Deploy COGW Operator for this subscription
    deploy_cogw_operator(subscription)
    
    # Create default COGW if eligible tier
    if subscription.tier in ["professional", "enterprise"]:
        create_default_cogw(subscription)

def on_subscription_deleted(subscription):
    # Remove COGW Operator
    remove_cogw_operator(subscription)
```

### Operator Service Account

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: cogw-operator
  namespace: acme-subscription
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: cogw-operator-role
  namespace: acme-subscription
rules:
  - apiGroups: ["hub.olympus.io"]
    resources: ["workbenches"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["seer.olympus.io"]
    resources: ["sentinelspecs", "sentinelscenario*"]
    verbs: ["get", "list", "watch", "create", "update", "delete"]
```

### Reconciliation Loop

```python
class COGWOperator:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
    
    def run(self):
        # Watch COGW workbenches
        watch_cogw_workbenches(self.subscription_id, self.on_cogw_change)
        
        # Watch COG Sentinels
        watch_cog_sentinels(self.subscription_id, self.on_sentinel_change)
        
        # Watch all workbenches for new/deleted
        watch_workbenches(self.subscription_id, self.on_workbench_change)
    
    def on_sentinel_change(self, event):
        sentinel = event.object
        self.reconcile_sentinel(sentinel)
    
    def on_workbench_change(self, event):
        # Re-evaluate all COG Sentinels when workbench list changes
        for sentinel in list_cog_sentinels(self.subscription_id):
            self.reconcile_sentinel(sentinel)
    
    def reconcile_sentinel(self, sentinel):
        # Pattern evaluation and sync logic
        pass
```

---

## Related

- [ADR-0118: Cognitive Operations Governance Workbench Type](./0118-cognitive-operations-governance-workbench-type.md) — COGW workbench type
- [ADR-0119: COG Sentinel Cross-Workbench Enrollment](./0119-cog-sentinel-cross-workbench-enrollment.md) — COG Sentinel targeting
- [COGW Operator](../../olympus-seer-docs/seer-design/subsystems/cognitive-operations-governance-workbench/cogw-operator.md) — Detailed specification
