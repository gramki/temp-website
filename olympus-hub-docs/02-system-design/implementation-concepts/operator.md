# Operator

> **Category:** Configuration Model

---

## Overview

An **Operator** is a GitOps-based controller that reconciles CRD specifications with the actual state of Hub resources. Operators watch for CRD changes in the Git repository and apply necessary changes to bring the system to the desired state. Hub groups operators by persona to align with responsibility boundaries.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't address configuration management or GitOps. Operators are an implementation mechanism for declarative resource management.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| (not covered) | Operator | Configuration reconciliation |
| (not covered) | GitOps | Git as source of truth |

### Gap This Fills

The ontology focuses on runtime concepts. Operators address:
1. **Configuration management**: How are resources configured?
2. **Reconciliation**: How does desired become actual?
3. **Persona alignment**: Who manages which resources?

---

## Definition

**Operator** is a controller that:
- Watches for CRD changes in subscription Git repository
- Compares desired state (CRD) with actual state (system)
- Applies changes to reconcile differences
- Reports status back to CRD

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Subscription or system level |
| **Lifecycle** | Platform-managed; always running |
| **Ownership** | Platform owns operators; personas own CRDs |
| **Multiplicity** | Multiple operators per persona |

---

## Rationale

### Why This Design?

GitOps-based operators enable:
1. **Declarative configuration**: Specify what, not how
2. **Audit trail**: Git history is audit log
3. **Review process**: Pull requests for changes
4. **Rollback**: Revert via Git

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Imperative APIs only** | No audit trail; no review |
| **GUI-only configuration** | Not GitOps; limited automation |
| **Manual kubectl-style apply** | Error-prone; no continuous reconciliation |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0014](../../decision-logs/0014-gitops-operator-model.md) | GitOps-based operator model |
| [ADR-0015](../../decision-logs/0015-persona-based-operator-grouping.md) | Operators grouped by persona |

---

## Structure

### Operators by Persona

| Persona | Operators | CRDs Managed |
|---------|-----------|--------------|
| **SRE** | sre-operator | HubClusterDeployment, SystemResource, BlueprintSpec |
| **Win** | win-operator | TenantSubscription |
| **Admin** | resource-operators, workbench-admin-operator | Data stores, Machines, Tools, Environments |
| **Process Architect** | workbench-architect-operator | Normative specs, SOPs, Notification templates |
| **Developer** | workbench-developer-operator, scenario-developer-operator | Automation specs, Hub Applications, Triggers |
| **Supervisor** | workbench-supervisor-operator | Task queues, Supervision specs |

### Operator Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OPERATOR ARCHITECTURE                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   GIT REPOSITORY                      OPERATORS                              │
│   ──────────────                      ─────────                              │
│                                                                              │
│   ┌─────────────────┐                ┌─────────────────┐                    │
│   │ subscription/   │                │                 │                    │
│   │   workbenches/  │──── watch ────▶│   workbench-    │                    │
│   │     wb-1/       │                │   developer-    │                    │
│   │       scenarios/│                │   operator      │                    │
│   │         ...yaml │                │                 │                    │
│   └─────────────────┘                └────────┬────────┘                    │
│                                               │                              │
│                                               │ reconcile                    │
│                                               ▼                              │
│                                      ┌─────────────────┐                    │
│                                      │   HUB SYSTEM    │                    │
│                                      │                 │                    │
│                                      │ • Workbench     │                    │
│                                      │ • Scenarios     │                    │
│                                      │ • Applications  │                    │
│                                      │ • Triggers      │                    │
│                                      │                 │                    │
│                                      └─────────────────┘                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Behavior

### Reconciliation Loop

```
1. Operator detects CRD change
   ├── Git sync triggered
   └── CRD file modified

2. Operator reads desired state
   └── Parse CRD from Git

3. Operator reads current state
   └── Query Hub system

4. Operator calculates diff
   └── What needs to change?

5. Operator applies changes
   ├── Create new resources
   ├── Update existing resources
   └── (Deletion typically manual)

6. Operator updates status
   └── Write status back to CRD
```

### Sync Trigger

```
Sync triggered by:
├── Manual: Admin invokes sync
├── Promotion: Artifacts promoted to workbench
└── Scheduled: Periodic reconciliation (optional)

Note: Git is storage, not auto-sync trigger by default
```

### Status Reporting

```yaml
# CRD with status after reconciliation
apiVersion: hub.olympus.io/v1
kind: ScenarioAutomationSpec
metadata:
  name: standard-dispute
spec:
  # ... specification ...
status:
  phase: Active           # Active | Pending | Failed
  lastReconciled: "2026-01-06T10:00:00Z"
  conditions:
    - type: Ready
      status: "True"
      lastTransitionTime: "2026-01-06T10:00:00Z"
    - type: ApplicationDeployed
      status: "True"
      lastTransitionTime: "2026-01-06T10:00:00Z"
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Git Repository | ← watches | Detects CRD changes |
| Hub System | → manages | Creates/updates resources |
| CRD Status | → writes | Reports reconciliation status |
| Olympus Watch | → logs | Observability integration |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Idempotent** | Multiple reconciliations produce same result |
| **Persona-scoped** | Operators only manage their persona's CRDs |
| **Status reflects reality** | Status accurately shows current state |
| **Reference validity** | Referenced resources must exist |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **GitOps** | Git as source of truth |
| ✅ **Audit trail** | Git history |
| ✅ **Declarative** | Specify desired state |
| ✅ **Automatic reconciliation** | Drift corrected |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Sync delay** | Clear sync triggers |
| ⚠️ **Error handling** | Status conditions show errors |

---

## Examples

### Example 1: Scenario Reconciliation

```
1. Developer commits ScenarioAutomationSpec change
2. Developer requests sync
3. scenario-developer-operator:
   ├── Reads updated spec
   ├── Detects trigger reference change
   ├── Validates trigger exists
   ├── Updates scenario in Hub
   └── Updates status: Ready
```

### Example 2: Failed Reconciliation

```yaml
status:
  phase: Failed
  lastReconciled: "2026-01-06T10:00:00Z"
  conditions:
    - type: Ready
      status: "False"
      reason: InvalidReference
      message: "Referenced trigger 'missing-trigger' not found"
```

---

## Implementation Notes

### For Developers

- Ensure CRD references are valid before commit
- Check operator status after sync
- Fix failed reconciliations promptly

### For Operators

- Monitor operator health
- Review failed reconciliations
- Manage sync trigger permissions

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [CRD](./crd.md) | Operators reconcile CRDs |
| [Subscription](./subscription.md) | Operators work within subscription scope |
| [Scenario Specification Types](./scenario-specification-types.md) | Key CRDs managed by operators |

---

## References

- [Hub Operators Subsystem](../../04-subsystems/operators/README.md)
- [CRD Reference](../../04-subsystems/operators/crd-reference.md)
- [ADR-0014: GitOps Operator Model](../../decision-logs/0014-gitops-operator-model.md)

