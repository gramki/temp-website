# CRD (Custom Resource Definition)

> **Category:** Configuration Model

---

## Overview

A **CRD (Custom Resource Definition)** is a declarative specification that defines Hub resources, configurations, and behaviors. Following Kubernetes-style patterns, CRDs allow Hub resources to be defined as YAML documents, stored in Git, and reconciled by Operators. This enables GitOps workflows where the desired state is declared and the platform converges to match.

---

## Ontology Context

### Relationship to Ontology

The ontology describes **what** concepts exist (Scenario, Trigger, Machine, Tool) but not **how** they are configured and managed. CRDs provide the implementation mechanism for declaring these concepts.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Scenario | ScenarioNormativeSpec, ScenarioAutomationSpec, ScenarioDeploymentSpec | CRDs define Scenarios |
| Trigger | TriggerSpec | CRD defines Triggers |
| Machine | MachineDefinition, MachineInstance | CRDs define Machines |
| Tool | ToolDefinition, ToolInstance | CRDs define Tools |

### Gap This Fills

The ontology describes concepts abstractly. CRDs specify:
1. **Configuration format**: How are resources specified?
2. **Validation**: What constraints apply?
3. **Lifecycle**: How are resources created, updated, deleted?
4. **Versioning**: How do specifications evolve?

---

## Definition

**CRD** is a declarative resource specification following a standard structure:
- `apiVersion`: API group and version
- `kind`: Resource type
- `metadata`: Name, namespace, labels, annotations
- `spec`: Desired state specification
- `status`: Current state (managed by system)

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Varies by CRD (subscription, workbench, scenario) |
| **Lifecycle** | Stored in Git; reconciled by Operators |
| **Ownership** | Defined by persona (Admin, Architect, Developer, Supervisor) |
| **Multiplicity** | Multiple instances of each CRD type |

---

## Rationale

### Why This Design?

CRD-based configuration enables:
1. **GitOps**: All configuration in version control
2. **Declarative**: Specify desired state, not imperative commands
3. **Auditable**: Git history provides complete audit trail
4. **Reviewable**: Configuration changes go through review
5. **Rollback**: Revert to previous configuration via Git

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Imperative APIs only** | No audit trail; harder to review |
| **GUI-only configuration** | No GitOps; limited automation |
| **Proprietary format** | Learning curve; limited tooling |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0014](../../decision-logs/0014-gitops-operator-model.md) | GitOps-based operator model |
| [ADR-0015](../../decision-logs/0015-persona-based-operator-grouping.md) | Operators grouped by persona |
| [ADR-0017](../../decision-logs/0017-trigger-as-standalone-specification.md) | TriggerSpec as standalone CRD |

---

## Structure

### CRD Anatomy

```yaml
apiVersion: hub.olympus.io/v1          # API group and version
kind: ScenarioNormativeSpec            # Resource type
metadata:
  name: standard-dispute               # Unique name within namespace
  namespace: acme-bank                 # Scope (tenant/subscription)
  labels:
    workbench: dispute-ops             # Organizational labels
    version: "1.2.0"
  annotations:
    description: "Standard dispute handling"
spec:
  # Desired state specification
  display_name: "Standard Dispute"
  version: "1.2.0"
  roles:
    - name: dispute-analyst
      goals:
        - "Investigate within SLA"
  # ... more specification
status:
  # Current state (managed by system)
  phase: Active
  lastReconciled: "2026-01-06T10:00:00Z"
```

### CRD Categories by Persona

| Persona | CRDs Managed |
|---------|--------------|
| **SRE** | HubClusterDeployment, SystemResource, BlueprintSpec, SystemToolSpec |
| **Win** | TenantSubscription |
| **Administrator** | GanymedeStore, CallistoStore, EuropaStore, KnowledgeBankConfig, MemoryServicesConfig, EnvironmentSpec, MachineDefinition, ToolDefinition |
| **Process Architect** | WorkbenchNormativeSpec, ScenarioNormativeSpec, NotificationTemplateSpec, SOPDocumentSpec |
| **Developer** | WorkbenchDeploymentSpec, ScenarioAutomationSpec, ScenarioDeploymentSpec, HubApplicationSpec, TriggerSpec, WorkbenchAsMachine, ScenarioAsTool, ScenarioAsAgent |
| **Supervisor** | TaskQueueSpecification, WorkbenchSupervisionSpec |

---

## Behavior

### CRD Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CRD LIFECYCLE                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. AUTHOR                                                                  │
│      └── Persona writes CRD YAML in IDE/editor                              │
│                                                                              │
│   2. VALIDATE                                                                │
│      └── Schema validation, reference checking                              │
│                                                                              │
│   3. COMMIT                                                                  │
│      └── Push to subscription Git repository                                │
│                                                                              │
│   4. SYNC                                                                    │
│      └── Admin/Developer triggers sync to workbench                         │
│                                                                              │
│   5. RECONCILE                                                               │
│      └── Operator reads CRD, reconciles desired → actual state              │
│                                                                              │
│   6. OBSERVE                                                                 │
│      └── Status updated, events logged                                      │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Operator Reconciliation

```
1. Operator watches for CRD changes
2. On change detected:
   ├── Read desired state from CRD spec
   ├── Read current state from system
   ├── Calculate diff
   └── Apply changes to converge
3. Update CRD status with result
4. Log events for observability
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Git Repository | ← stored in | CRDs stored in subscription Git |
| Operator | → reconciled by | Operators watch and reconcile CRDs |
| Workbench Management | ↔ affects | CRDs define workbench configuration |
| Signal Exchange | ← reads | SX reads trigger definitions |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Valid schema** | CRD must conform to defined schema |
| **Valid references** | Referenced resources must exist |
| **Unique name** | Name must be unique within namespace |
| **Immutable fields** | Some fields cannot be changed after creation |
| **Version compatibility** | CRD version must be compatible with operator |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **GitOps** | All configuration versioned and auditable |
| ✅ **Declarative** | Specify what, not how |
| ✅ **Familiar pattern** | Kubernetes-style; widely understood |
| ✅ **Tooling** | YAML editors, validators, linters available |
| ✅ **Promotion** | CRDs promote alongside artifacts |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **YAML complexity** | Templates, Studio UI for generation |
| ⚠️ **Learning curve** | Documentation, examples, guides |
| ⚠️ **Sync delay** | Clear sync triggers and status |

---

## Examples

### Example 1: TriggerSpec CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: TriggerSpec
metadata:
  name: dispute-filed-trigger
  namespace: acme-bank
spec:
  display_name: "Dispute Filed"
  
  signal_type: "dispute.filed"
  
  conditions:
    - field: "$.amount"
      operator: "greater_than"
      value: 0
      
  creates:
    scenario_ref: standard-dispute
    
  transformation:
    type: javascript
    script: |
      function(signal) {
        return {
          customer_id: signal.payload.customer_id,
          dispute_amount: signal.payload.amount
        };
      }
```

### Example 2: MachineInstance CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: MachineInstance
metadata:
  name: core-banking-prod
  namespace: acme-bank
spec:
  definition_ref: core-banking-system
  
  connection:
    type: http
    base_url: "https://core.acme.com/api"
    auth:
      type: oauth2
      token_url: "https://auth.acme.com/token"
      client_id_ref: core-banking-client-id
      client_secret_ref: core-banking-client-secret
      
  health_check:
    endpoint: "/health"
    interval_seconds: 60
```

---

## Implementation Notes

### For Developers

- Use schema validation in your editor
- Reference existing CRDs for patterns
- Test CRDs in DEV workbench before promotion
- Include meaningful labels and annotations

### For Operators

- Monitor operator reconciliation logs
- Check CRD status for errors
- Review sync triggers for security
- Manage CRD schema versions

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Operator](./operator.md) | Reconciles CRDs to desired state |
| [Scenario Specification Types](./scenario-specification-types.md) | CRD structure for Scenarios |
| [Subscription](./subscription.md) | CRDs stored in subscription Git |
| [Promotion](./promotion.md) | CRDs promoted across stages |

---

## References

- [Hub Operators Subsystem](../../04-subsystems/operators/README.md)
- [CRD Reference](../../04-subsystems/operators/crd-reference.md)
- [ADR-0014: GitOps Operator Model](../../decision-logs/0014-gitops-operator-model.md)

