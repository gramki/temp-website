# Hub Operators Subsystem

> **Status:** 🟡 Draft — Under active development

The Hub Operators Subsystem provides **GitOps-native provisioning and management** for all Hub resources, configurations, and metadata. Operators translate declarative specifications (CRDs) into desired state across Hub Deployments and Tenant Subscriptions.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Enable GitOps practices for Hub resource management |
| **Approach** | Kubernetes-style Custom Resource Definitions (CRDs) |
| **Scope** | Publisher Domain + Tenant Domain operations |
| **Personas** | SRE, Win Team, Admin, Process Architect, Developer, Supervisor |

---

## GitOps Philosophy

Hub advocates and supports GitOps practices where:

1. **Declarative Specifications** — All configurations are expressed as versioned CRD documents
2. **Git as Source of Truth** — CRDs are stored in Git repositories with full version history
3. **Automated Reconciliation** — Operators continuously reconcile declared state with actual state
4. **Auditability** — All changes are traceable through Git commits and operator logs

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         GitOps Flow                                      │
│                                                                          │
│   ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐   │
│   │   Git    │ ───► │ Operator │ ───► │   Hub    │ ───► │ Desired  │   │
│   │  (CRDs)  │      │  Watch   │      │   API    │      │  State   │   │
│   └──────────┘      └──────────┘      └──────────┘      └──────────┘   │
│        │                                                      │         │
│        │              Reconciliation Loop                     │         │
│        └──────────────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Operator Classification

Operators are grouped by the **domain** and **persona** whose operations they serve:

### Publisher Domain

Operators managing Hub infrastructure and tenant onboarding:

| Operator | Persona | Purpose |
|----------|---------|---------|
| **SRE Operator** | SRE Team | Hub cluster deployment and system resources |
| **Win Operator** | Win Team | Tenant subscription provisioning |

### Tenant Domain

Operators managing tenant-specific resources and configurations:

| Operator Category | Persona | Purpose |
|-------------------|---------|---------|
| **Admin Operators** | Tenant Admin | Infrastructure resources, machine/tool definitions, DevOps bindings |
| **Process Architect Operator** | Process Architect | Workbench and Scenario normative specifications |
| **Developer Operators** | Developer | Automation, deployment, application, and composite pattern specifications |
| **Supervisor Operators** | Supervisor | Task queues and supervision configuration |

### Marketplace Domain

Operators managing Marketplace-related resources:

| Operator | Persona | Purpose |
|----------|---------|---------|
| **marketplace-package-operator** | Developer | Package Manifest CRD management |
| **marketplace-subscription-operator** | Admin | Package Subscription lifecycle |
| **blueprintspec-operator** | System | BlueprintSpec delivery and management |

→ See [Marketplace Operators](./marketplace-operators.md) for details.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PUBLISHER DOMAIN                                   │
│  ┌─────────────────────────────────┐  ┌─────────────────────────────────┐   │
│  │         SRE Operator            │  │         Win Operator            │   │
│  │  ┌───────────────────────────┐  │  │  ┌───────────────────────────┐  │   │
│  │  │ Hub Cluster Deployment    │  │  │  │ Tenant Subscription Spec  │  │   │
│  │  │ System Resource Specs     │  │  │  └───────────────────────────┘  │   │
│  │  └───────────────────────────┘  │  │                                 │   │
│  └─────────────────────────────────┘  └─────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            TENANT DOMAIN                                     │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        Admin Operators                               │    │
│  │  ┌─────────────────────┐  ┌─────────────────────────────────────┐   │    │
│  │  │  Resource Operators │  │  workbench-admin-operator           │   │    │
│  │  │  • Data Stores      │  │  • Environment Specification        │   │    │
│  │  │  • Knowledge Stores │  │  • Machine Definition Specification │   │    │
│  │  │  • Memory Stores    │  │  • Machine Instance Specification   │   │    │
│  │  └─────────────────────┘  │  • Tool Definition Specification    │   │    │
│  │                           │  • Tool Instance Specification      │   │    │
│  │  ┌─────────────────────┐  └─────────────────────────────────────┘   │    │
│  │  │  DevOps Operators   │                                            │    │
│  │  │  • devops-binding-  │  (Manages DevOpsWorkbenchBinding CRD)     │    │
│  │  │    operator         │  (Pushes BusinessWorkbenchManifest to D)  │    │
│  │  │  • manifest-operator│  (Registers gateway Machine and Tools)    │    │
│  │  └─────────────────────┘                                            │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                   Process Architect Operator                         │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │  workbench-architect-operator                                │    │    │
│  │  │  • Workbench Normative Specification                         │    │    │
│  │  │  • Scenario Normative Specification                          │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      Developer Operators                             │    │
│  │  ┌────────────────────────────┐  ┌────────────────────────────┐     │    │
│  │  │ workbench-developer-op     │  │ scenario-developer-op      │     │    │
│  │  │ • Workbench Deployment     │  │ • Scenario Automation Spec │     │    │
│  │  │   Specification            │  │ • Scenario Deployment Spec │     │    │
│  │  └────────────────────────────┘  └────────────────────────────┘     │    │
│  │                                                                      │    │
│  │  ┌────────────────────────────────────────────────────────────┐     │    │
│  │  │  Composite Pattern Operators                                │     │    │
│  │  │  • Hub Application Specification                            │     │    │
│  │  │  • workbench-as-a-machine-operator                          │     │    │
│  │  │  • scenario-as-a-tool-operator                              │     │    │
│  │  │  • scenario-as-an-agent-operator                            │     │    │
│  │  │  • workbench-ms-teams-operator                              │     │    │
│  │  └────────────────────────────────────────────────────────────┘     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     Supervisor Operators                             │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │  workbench-supervisor-operator                               │    │    │
│  │  │  • Task Queue Specification                                  │    │    │
│  │  │  • Workbench Supervision Specification                       │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Specification Lifecycle

Each specification type follows a consistent lifecycle:

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  Draft   │ ──► │ Pending  │ ──► │  Active  │ ──► │ Archived │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
     │                │                 │
     │                │                 │
     ▼                ▼                 ▼
 Git Commit      Operator          Reconciled
               Validation         with Hub State
```

| State | Description |
|-------|-------------|
| **Draft** | Specification under development (not yet committed) |
| **Pending** | Committed to Git, awaiting operator reconciliation |
| **Active** | Successfully reconciled with Hub state |
| **Archived** | Specification superseded or retired |

---

## Cross-Operator Dependencies

Some specifications have dependencies on others:

```
Machine Definition ◄──────────── Machine Instance
        │                               │
        ▼                               ▼
Tool Definition ◄────────────── Tool Instance
                                        │
                                        ▼
                               Environment Specification
                                        │
                                        ▼
                               Workbench Normative Spec
                                        │
                               ┌────────┴────────┐
                               ▼                 ▼
                    Scenario Normative    Workbench Deployment
                    Specification               Specification
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
           Scenario Automation    Scenario Deployment
           Specification          Specification
                    │
                    ▼
           Hub Application Specification
```

Operators validate dependencies and fail fast if prerequisites are not met.

---

## Operator Execution Model

### Reconciliation Triggers

| Trigger | Description |
|---------|-------------|
| **Git Push** | Webhook triggers reconciliation for changed specifications |
| **Periodic Sync** | Regular interval reconciliation (drift detection) |
| **Manual Trigger** | On-demand reconciliation via CLI or Console |
| **Dependency Update** | Cascading reconciliation when dependencies change |

### Reconciliation Guarantees

- **Idempotent** — Running the same specification multiple times produces the same result
- **Atomic** — Specifications either fully apply or fully roll back
- **Ordered** — Dependencies are resolved before dependents are processed
- **Observable** — Reconciliation status is visible via API and Console

---

## Documentation Structure

| Document | Description |
|----------|-------------|
| [Publisher Domain Operators](./publisher-domain-operators.md) | SRE and Win operators |
| [Admin Operators](./admin-operators.md) | Resource and workbench-admin operators |
| [Process Architect Operator](./process-architect-operator.md) | Normative specification operators |
| [Developer Operators](./developer-operators.md) | Automation and deployment operators |
| [Supervisor Operators](./supervisor-operators.md) | Task queue and supervision operators |
| [Marketplace Operators](./marketplace-operators.md) | Package manifest and subscription operators |
| [CRD Reference](./crd-reference.md) | Complete CRD schema reference |

---

## Related Documentation

- [Workbench Management](../workbench-management/README.md) — Workbench lifecycle
- [Registry Services](../registry-services/README.md) — Machine and Tool registries
- [Task Management](../task-management/README.md) — Task queue operations
- [Scenario Development Journey](../../08-personas-and-journeys/journeys/scenario-development.md) — End-to-end scenario development
- [Subscription Configuration Guide](../../10-guides/subscription-configuration-guide.md) — Manual configuration alternative

---

*This subsystem enables Infrastructure-as-Code practices for Hub, ensuring reproducible, auditable, and version-controlled configuration management.*

