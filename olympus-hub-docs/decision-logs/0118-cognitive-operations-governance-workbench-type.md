# ADR-0118: Cognitive Operations Governance Workbench Type

**Status**: Accepted  
**Date**: 2026-01-14  
**Category**: seer, hub-integration, workbench

---

## Context

Request Sentinels (ADR-0116) enable AI agents to observe and participate in other agents' requests within a workbench. However, organizations need governance capabilities that span **multiple workbenches** within a subscription:

1. **Subscription-wide token governance** — Enforce token budgets across all workbenches
2. **Cross-domain compliance** — Compliance rules that apply across business domains
3. **Enterprise AI quality** — Quality assurance comparing patterns across workbenches
4. **Unified security monitoring** — Security sentinels observing all workbenches

The current Request Sentinel model only supports single-workbench scope. There is no mechanism for:
- Sentinels that operate across workbench boundaries
- Centralized governance configuration
- Automatic enrollment in multiple target workbenches

### Requirements

1. Define Sentinels that target multiple workbenches
2. Manage cross-workbench Sentinels centrally
3. Provide visibility and control in target workbenches
4. Enable automatic enrollment based on configurable patterns
5. Support subscription-wide governance scenarios

---

## Decision

### 1. Introduce `workbench_type: "cogw"` as Distinct Workbench Type

We will add a third workbench type, `cogw` (Cognitive Operations Governance Workbench), to the existing `business` and `devops` types:

```yaml
workbench_type: "business" | "devops" | "cogw"
```

### 2. COGW Workbench Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Purpose** | Subscription-wide cognitive operations governance |
| **Sentinels** | Can define COG Sentinels that operate across target workbenches |
| **Scope** | Subscription-wide access to all workbenches |
| **Scenarios** | Governance-focused scenarios (token governance, compliance, QA) |

### 3. Default COGW at Subscription Creation

Every eligible subscription automatically receives a default COGW at creation:

- **Auto-created** during subscription provisioning
- **Pre-populated** with standard governance scenarios
- **Deletable** if not needed

### 4. COG Sentinels

COG Sentinels are Request Sentinels defined in COGW workbenches that:

- Target multiple workbenches via `cogSpec.workbench_patterns`
- Appear as read-only specs in target workbenches
- Can be enabled/disabled locally in target workbenches

---

## Alternatives Considered

### 1. Extend Request Sentinel with Multi-Workbench Targeting

Allow any Request Sentinel to target multiple workbenches via configuration.

**Rejected because:**
- **Security concerns** — Any workbench could monitor any other workbench
- **No centralization** — Governance scattered across workbenches
- **Unclear ownership** — Who manages cross-workbench sentinels?
- **Complexity** — Every workbench needs cross-workbench configuration

### 2. Annotation on Business Workbenches

Mark any business workbench as "governance-capable" via annotation.

**Rejected because:**
- **No clear distinction** — Governance workbenches look like regular workbenches
- **Validation complexity** — Hard to enforce governance-specific rules
- **Discovery** — Difficult to find all governance configurations
- **Inconsistent with DevOps pattern** — DevOps uses distinct type, not annotation

### 3. Subscription-Level Sentinel Configuration

Define cross-workbench sentinels at subscription level, not in any workbench.

**Rejected because:**
- **No workbench context** — Sentinels need scenarios, triggers, requests
- **Breaks workbench model** — Would require new subscription-level construct
- **Operational complexity** — Different management model than other sentinels

---

## Consequences

### Positive

1. **Clear distinction** — COGW workbenches explicitly marked for governance
2. **Consistent pattern** — Follows DevOps workbench pattern (`workbench_type`)
3. **Centralized management** — All cross-workbench governance in COGW
4. **Security boundary** — Only COGW workbenches can define COG Sentinels
5. **Standard workbench** — COGW uses standard workbench features (scenarios, triggers)
6. **Visibility** — Target workbenches can see and control COG Sentinels locally

### Negative

1. **New workbench type** — Adds complexity to workbench model
2. **Operator required** — Need COGW Operator to manage sync
3. **Cross-workbench access** — COGW needs subscription-wide access

### Neutral

1. **Similar to DevOps** — Follows established pattern for specialized workbenches
2. **Tier-based availability** — May limit COGW to certain subscription tiers

---

## Implementation Notes

### Workbench Type Extension

Update Hub Workbench Management to accept `cogw` as valid `workbench_type`:

```yaml
# In WorkbenchSpec validation
workbench_type:
  type: string
  enum: ["business", "devops", "cogw"]
  default: "business"
```

### Default COGW Creation

Integrate with Subscription Provisioning Operator:

```python
def on_subscription_created(subscription):
    if subscription.tier in ["professional", "enterprise", "custom"]:
        create_default_cogw(subscription)
```

### COGW Operator Deployment

Deploy COGW Operator per subscription:

```yaml
apiVersion: seer.olympus.io/v1
kind: COGWOperatorDeployment
metadata:
  name: cogw-operator
  namespace: ${subscription_namespace}
spec:
  subscription_id: ${subscription_id}
```

---

## Related

- [ADR-0116: Request Sentinel Type](./0116-request-sentinel-type.md) — Base Request Sentinel
- [ADR-0119: COG Sentinel Cross-Workbench Enrollment](./0119-cog-sentinel-cross-workbench-enrollment.md) — COG Sentinel targeting
- [ADR-0088: DevOps Workbench Composite Pattern](./0088-devops-workbench-composite-pattern.md) — Similar pattern
- [COGW Specification](../../olympus-seer-docs/seer-design/subsystems/cognitive-operations-governance-workbench/cogw-specification.md) — Detailed specification
