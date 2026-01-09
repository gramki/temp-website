# ADR-0015: Persona-Based Operator Grouping

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub's GitOps operator model requires organizing multiple operators that manage different resource types. The organization strategy affects:
- Access control and permissions
- Development team responsibilities
- Deployment and upgrade paths
- Documentation and discoverability

Hub has well-defined personas with distinct responsibilities:
- **Publisher Domain**: SRE (infrastructure), Win Team (sales/onboarding)
- **Tenant Domain**: Admin, Process Architect, Developer, Supervisor

Resources naturally map to persona responsibilities (e.g., Task Queues → Supervisor, Scenarios → Developer).

## Decision

Operators are **grouped by persona**, where each operator manages specifications relevant to that persona's responsibilities:

### Publisher Domain

| Operator | Persona | Resources Managed |
|----------|---------|-------------------|
| **SRE Operator** | SRE Team | Hub cluster deployments, system resources, blueprints, system tools |
| **Win Operator** | Win Team | Tenant subscription provisioning |

### Tenant Domain

| Operator | Persona | Resources Managed |
|----------|---------|-------------------|
| **Admin Operators** | Tenant Admin | Data stores, cognitive services, environments, machines, tools |
| **Process Architect Operator** | Process Architect | Normative specifications (Workbench, Scenario, SOP documents, notification templates) |
| **Developer Operators** | Developer | Automation specs, deployment specs, applications, APM, composite patterns |
| **Supervisor Operators** | Supervisor | Task queues, supervision configurations |

## Alternatives Considered

### Alternative 1: Single Monolithic Operator
- **Pros**: Simpler deployment, single upgrade path
- **Cons**: All-or-nothing permissions, harder to maintain, slower iteration

### Alternative 2: Resource-Type-Based Grouping
- **Pros**: Clear technical boundaries, follows CRD patterns
- **Cons**: Doesn't align with organizational responsibilities, confusing for users

### Alternative 3: Layer-Based Grouping (Normative/Automation/Execution)
- **Pros**: Matches Hub ontology layers
- **Cons**: One persona may work across layers (Developer spans Automation and Execution)

## Consequences

### Positive
- **Clear Ownership**: Each team knows which operators they manage
- **RBAC Alignment**: Operator permissions map to persona permissions
- **Independent Releases**: Teams can update their operators independently
- **Documentation Structure**: Docs organized by persona journey

### Negative
- **Cross-Cutting Concerns**: Some resources touch multiple personas
- **Coordination Required**: Changes spanning personas need multi-operator updates
- **Increased Operators**: More operators to deploy and monitor

### Neutral
- Operators may share common libraries and frameworks
- Dependency validation spans operators (cross-operator validation)

## Implementation

Each operator follows a consistent pattern:
1. Watches specific CRD types
2. Validates against dependencies (may query other operators' resources)
3. Reconciles with Hub APIs
4. Reports status back to CRD

```
┌────────────────────────────────────────────────────────────────────┐
│                      PUBLISHER DOMAIN                               │
│  ┌────────────────────────┐  ┌────────────────────────┐            │
│  │      SRE Operator      │  │      Win Operator      │            │
│  │  • HubClusterDeployment│  │  • TenantSubscription  │            │
│  │  • SystemResource      │  └────────────────────────┘            │
│  │  • Blueprint           │                                        │
│  │  • SystemTool          │                                        │
│  └────────────────────────┘                                        │
└────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌────────────────────────────────────────────────────────────────────┐
│                       TENANT DOMAIN                                 │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    Admin Operators                           │   │
│  │  • GanymedeStore  • CallistoStore  • EuropaStore            │   │
│  │  • KnowledgeBankConfig  • MemoryServicesConfig              │   │
│  │  • EnvironmentSpec  • MachineDefinition  • ToolDefinition   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│  ┌───────────────────────┐  ┌───────────────────────────────────┐  │
│  │ Process Architect Op  │  │       Developer Operators         │  │
│  │ • WorkbenchNormative  │  │ • ScenarioAutomationSpec          │  │
│  │ • ScenarioNormative   │  │ • ScenarioDeploymentSpec          │  │
│  │ • NotificationTemplate│  │ • HubApplicationSpec              │  │
│  │ • SOPDocument         │  │ • TriggerSpec  • APM Specs        │  │
│  └───────────────────────┘  │ • Composite Pattern Specs         │  │
│                             └───────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Supervisor Operators                        │ │
│  │  • TaskQueueSpecification  • WorkbenchSupervisionSpec         │ │
│  └───────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────┘
```

## Related Decisions

- [ADR-0014: GitOps-Based Operator Model](./0014-gitops-operator-model.md)
- [ADR-0002: Scenario Specification Types](./0002-scenario-specification-types.md)

