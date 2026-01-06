# CRD Specification Reference

> **Status:** 🟡 Draft — Under active development

This document provides a quick reference for all Custom Resource Definitions (CRDs) used by Hub Operators.

---

## CRD Summary

### Publisher Domain

| CRD | Operator | Persona | Description |
|-----|----------|---------|-------------|
| `HubClusterDeployment` | SRE Operator | SRE Team | Hub cluster infrastructure |
| `SystemResource` | SRE Operator | SRE Team | System-scoped shared resources |
| `BlueprintSpec` | SRE Operator | SRE Team | Workbench blueprints for tenants |
| `SystemToolSpec` | SRE Operator | SRE Team | Platform-provided tools |
| `IndustryKnowledgeSpec` | SRE Operator | SRE Team | Industry knowledge bases |
| `TenantSubscription` | Win Operator | Win Team | Tenant subscription provisioning |

### Tenant Domain — Admin

| CRD | Operator | Persona | Description |
|-----|----------|---------|-------------|
| `GanymedeStore` | Application Data Store Operators | Tenant Admin | Relational DBaaS (PostgreSQL-compatible) |
| `CallistoStore` | Application Data Store Operators | Tenant Admin | Key-Value Store |
| `EuropaStore` | Application Data Store Operators | Tenant Admin | Search/Analytics (OpenSearch) |
| `KnowledgeBankConfig` | Cognitive Services Operators | Tenant Admin | Knowledge Bank access & ingestion |
| `MemoryServicesConfig` | Cognitive Services Operators | Tenant Admin | Memory Services (Enterprise, Agent, User) |
| `EnvironmentSpec` | workbench-admin-operator | Tenant Admin | Environment configuration |
| `MachineDefinition` | workbench-admin-operator | Tenant Admin | Abstract machine template |
| `MachineInstance` | workbench-admin-operator | Tenant Admin | Concrete machine endpoint |
| `ToolDefinition` | workbench-admin-operator | Tenant Admin | Abstract tool template |
| `ToolInstance` | workbench-admin-operator | Tenant Admin | Concrete tool endpoint |

### Tenant Domain — Process Architect

| CRD | Operator | Persona | Description |
|-----|----------|---------|-------------|
| `WorkbenchNormativeSpec` | workbench-architect-operator | Process Architect | Workbench governance |
| `ScenarioNormativeSpec` | workbench-architect-operator | Process Architect | Scenario SOPs and rules |
| `SOPDocumentSpec` | workbench-architect-operator | Process Architect | Standard Operating Procedures |
| `NotificationTemplateSpec` | workbench-architect-operator | Process Architect | Notification templates |

### Tenant Domain — Developer

| CRD | Operator | Persona | Description |
|-----|----------|---------|-------------|
| `WorkbenchDeploymentSpec` | workbench-developer-operator | Developer | Workbench deployment config |
| `TriggerSpec` | scenario-developer-operator | Developer | Signal-to-scenario bindings |
| `ScenarioAutomationSpec` | scenario-developer-operator | Developer | Application, tools, runtime |
| `ScenarioDeploymentSpec` | scenario-developer-operator | Developer | SLAs, queues, activation |
| `HubApplicationSpec` | hub-application-operator | Developer | Application code and config |
| `LogAlertSpec` | workbench-apm-operator | Developer | Log-based alerts |
| `MetricAlertSpec` | workbench-apm-operator | Developer | Metric-based alerts |
| `ProbeSpec` | workbench-apm-operator | Developer | Health and availability probes |
| `SLOAlertSpec` | workbench-apm-operator | Developer | SLO targets and error budgets |
| `NotificationChannelConfig` | workbench-apm-operator | Developer | Alert notification channels |
| `WorkbenchAsMachine` | workbench-as-a-machine-operator | Developer | Expose workbench as machine |
| `ScenarioAsTool` | scenario-as-a-tool-operator | Developer | Expose scenario as tool |
| `ScenarioAsAgent` | scenario-as-an-agent-operator | Developer | Expose scenario as agent (task queue or A2A) |
| `WorkbenchMSTeams` | workbench-ms-teams-operator | Developer | MS Teams integration |

### Tenant Domain — Supervisor

| CRD | Operator | Persona | Description |
|-----|----------|---------|-------------|
| `TaskQueueSpec` | workbench-supervisor-operator | Supervisor | Task queue configuration |
| `WorkbenchSupervisionSpec` | workbench-supervisor-operator | Supervisor | Supervision settings |

---

## CRD API Groups

All CRDs belong to the `hub.olympus.io` API group:

```yaml
apiVersion: hub.olympus.io/v1
kind: <CRDKind>
metadata:
  name: <resource-name>
  namespace: <tenant-namespace>  # For tenant-scoped resources
  labels:
    <standard-labels>
spec:
  <specification>
```

---

## Common Metadata Labels

| Label | Description | Example |
|-------|-------------|---------|
| `hub.olympus.io/tenant` | Tenant identifier | `acme-bank` |
| `hub.olympus.io/subscription` | Subscription identifier | `sub-prod-001` |
| `hub.olympus.io/workbench` | Workbench identifier | `dispute-operations` |
| `hub.olympus.io/scenario` | Scenario identifier | `standard-dispute` |
| `hub.olympus.io/environment` | Environment type | `production` |

---

## CRD Dependency Graph

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PUBLISHER DOMAIN                                   │
│                                                                              │
│   HubClusterDeployment ──► SystemResource                                   │
│          │                      │                                            │
│          └──────────────────────┼────────────────────────────────────────┐  │
│                                 │                                         │  │
└─────────────────────────────────┼─────────────────────────────────────────┘  │
                                  │                                            │
                                  ▼                                            │
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TENANT SUBSCRIPTION                                │
│                                                                              │
│   TenantSubscription                                                         │
│          │                                                                   │
│          ├──► GanymedeStore (Relational)                                     │
│          ├──► CallistoStore (Key-Value)                                      │
│          ├──► EuropaStore (Search/Analytics)                                 │
│          ├──► KnowledgeBankConfig                                            │
│          └──► MemoryServicesConfig                                           │
│                    │                                                         │
└────────────────────┼─────────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ENVIRONMENT & REGISTRIES                           │
│                                                                              │
│   MachineDefinition ◄───────────── MachineInstance                          │
│          │                               │                                   │
│          ▼                               │                                   │
│   ToolDefinition ◄──────────────── ToolInstance                             │
│                                          │                                   │
│   GanymedeStore ─────────────────────────┤                                   │
│   CallistoStore ─────────────────────────┼───────► EnvironmentSpec           │
│   EuropaStore ───────────────────────────┤               │                   │
│   KnowledgeBankConfig ───────────────────┘               │                   │
│   MemoryServicesConfig ──────────────────────────────────┘                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           WORKBENCH LAYER                                    │
│                                                                              │
│   WorkbenchNormativeSpec ◄──────── WorkbenchDeploymentSpec                  │
│          │                                │                                  │
│          │                                ├──► WorkbenchMSTeams              │
│          │                                └──► WorkbenchAsMachine            │
│          │                                                                   │
│          ▼                                                                   │
└──────────┼───────────────────────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SCENARIO LAYER                                     │
│                                                                              │
│   ScenarioNormativeSpec                                                      │
│          │                                                                   │
│          ├──► ScenarioAutomationSpec ──► HubApplicationSpec                 │
│          │           │                                                       │
│          │           ├──► ScenarioAsTool                                    │
│          │           └──► ScenarioAsAgent                                   │
│          │                                                                   │
│          └──► ScenarioDeploymentSpec                                        │
│                      │                                                       │
│                      ▼                                                       │
│               TaskQueueSpec ◄──── WorkbenchSupervisionSpec                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## CRD Status Fields

All CRDs include a `status` section updated by operators:

```yaml
status:
  # Reconciliation state
  phase: Reconciled  # Pending | Reconciling | Reconciled | Failed
  
  # Last reconciliation
  lastReconciled: "2026-01-05T10:00:00Z"
  
  # Conditions
  conditions:
    - type: Ready
      status: "True"
      lastTransitionTime: "2026-01-05T10:00:00Z"
      reason: ReconcileSucceeded
      message: "Resource reconciled successfully"
    
    - type: DependenciesResolved
      status: "True"
      lastTransitionTime: "2026-01-05T09:55:00Z"
      reason: AllDependenciesFound
      message: "All referenced resources exist"
  
  # Observed generation (for change detection)
  observedGeneration: 5
  
  # Resource-specific status fields
  # (varies by CRD)
```

### Common Phases

| Phase | Description |
|-------|-------------|
| `Pending` | Resource created, awaiting reconciliation |
| `Reconciling` | Operator is processing the resource |
| `Reconciled` | Successfully reconciled with target state |
| `Failed` | Reconciliation failed (see conditions) |
| `Deleting` | Resource being deleted, finalizers running |

### Common Conditions

| Condition | Description |
|-----------|-------------|
| `Ready` | Resource is fully operational |
| `DependenciesResolved` | All referenced resources exist |
| `Validated` | Specification passed validation |
| `Deployed` | Resource deployed to target |
| `Degraded` | Resource operational but with issues |

---

## Version Compatibility

### Specification Versioning

```yaml
spec:
  # Reference with version
  normative_ref:
    name: standard-dispute-normative
    version: "1.2.0"           # Exact version
    # OR
    version: "1.x"             # Any 1.x version
    # OR
    version: ">=1.2.0 <2.0.0"  # SemVer range
```

### API Version Migration

| API Version | Status | Notes |
|-------------|--------|-------|
| `hub.olympus.io/v1alpha1` | Deprecated | Migrate to v1 |
| `hub.olympus.io/v1beta1` | Deprecated | Migrate to v1 |
| `hub.olympus.io/v1` | Stable | Current version |

---

## Validation Rules

### Common Validations

| Rule | Applies To | Description |
|------|------------|-------------|
| `name-format` | All | Names must be DNS-compatible |
| `version-format` | All versioned | Semantic versioning required |
| `reference-exists` | All refs | Referenced resources must exist |
| `namespace-match` | Tenant resources | Must be in tenant namespace |

### Cross-CRD Validations

| Source CRD | Target CRD | Validation |
|------------|------------|------------|
| `MachineInstance` | `MachineDefinition` | Version compatibility |
| `ToolInstance` | `ToolDefinition` | Version compatibility |
| `ScenarioAutomationSpec` | `ScenarioNormativeSpec` | Task types match |
| `ScenarioDeploymentSpec` | `ScenarioAutomationSpec` | Queue mappings valid |
| `TaskQueueSpec` | `ScenarioDeploymentSpec` | Task types served |

---

## Quick Reference: Key Fields by CRD

### WorkbenchNormativeSpec
```yaml
spec:
  workbench: { name, display_name, version }
  purpose: { description, in_scope, out_of_scope }
  compliance: { frameworks, audit_controls }
  roles: [ { id, name, responsibilities, required_skills } ]
  policies: [ { id, name, applies_to } ]
  supervision: { escalation_contacts, review_requirements }
```

### ScenarioNormativeSpec
```yaml
spec:
  scenario: { name, display_name, version, workbench_ref }
  goals: { primary, secondary }
  agent_roles: [ { id, tasks, decision_authority } ]
  sops: [ { id, steps } ]
  decision_criteria: [ { id, rules } ]
  evidence_requirements: { intake, resolution }
  escalation: { sla_based, value_based, exception_based }
  task_types: [ { id, expected_duration, sla } ]
```

### ScenarioAutomationSpec
```yaml
spec:
  normative_ref: { name, version }
  application: { ref, version, runtime }
  triggers: [ { id, signal_source, signal_match, context_transform } ]
  tools: [ { id, tool_ref, permissions } ]
  state_machine: { initial_state, states }
  ai_agent: { model, system_prompt_ref, guardrails }
```

### ScenarioDeploymentSpec
```yaml
spec:
  automation_ref: { name, version }
  activation: { status, effective_from, effective_to }
  task_queues: [ { task_type, queue_ref } ]
  sla: { overall, per_task }
  agent_enrollment: { auto_enroll, enrollment_mode }
```

### TaskQueueSpec
```yaml
spec:
  queue: { name, display_name, workbench_ref }
  task_types: [ ]
  allocation: { algorithm, parameters }
  candidates: { roles, groups, workbench_roles, explicit_users }
  escalation: { levels }
  behavior: { assignment_mode, rebalancing, max_tasks_per_agent }
  working_hours: { timezone, schedule, after_hours }
```

---

## Related Documentation

- [Operators Overview](./README.md)
- [Publisher Domain Operators](./publisher-domain-operators.md)
- [Admin Operators](./admin-operators.md)
- [Process Architect Operator](./process-architect-operator.md)
- [Developer Operators](./developer-operators.md)
- [Supervisor Operators](./supervisor-operators.md)

---

*This reference provides a consolidated view of all Hub CRDs for quick lookup during development and operations.*

