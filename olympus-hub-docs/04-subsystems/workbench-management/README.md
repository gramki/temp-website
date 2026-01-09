# Workbench Management

> **Status:** 🔴 Stub — Placeholder for expansion

Workbench Management is the **control plane** for creating and managing Workbenches, which contain the definitions of Scenarios, Triggers, and Hub Applications.

---

## Overview

Workbench Management is responsible for:

| Function | Description |
|----------|-------------|
| **Workbench Lifecycle** | Create, update, archive Workbenches |
| **Scenario Management** | Define Scenarios within Workbenches |
| **Trigger Management** | Define Triggers that bind Signals to Scenarios |
| **Application Configuration** | Configure Hub Applications for Scenarios |
| **Request Policies** | Define Request lifecycle policies |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   WORKBENCH MANAGEMENT                           │
│                      (Control Plane)                             │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 WORKBENCH REGISTRY                       │    │
│  │                                                          │    │
│  │   Workbench 1: Dispute Operations                        │    │
│  │   Workbench 2: Payment Operations                        │    │
│  │   Workbench 3: Customer Onboarding                       │    │
│  │   ...                                                    │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              PER-WORKBENCH DEFINITIONS                   │    │
│  │                                                          │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │    │
│  │  │   Scenario   │  │   Trigger    │  │ Application  │   │    │
│  │  │ Definitions  │  │ Definitions  │  │   Configs    │   │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘   │    │
│  │                                                          │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │    │
│  │  │   Request    │  │     SOP      │  │  Knowledge   │   │    │
│  │  │   Policies   │  │ Definitions  │  │    Base      │   │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              CROSS-WORKBENCH CONCERNS                    │    │
│  │                                                          │    │
│  │  • Environment assignments                               │    │
│  │  • Agent enrollments (via Cipher)                        │    │
│  │  • Machine access permissions                            │    │
│  │  • Tool access permissions                               │    │
│  │  • DevOps workbench association (signal routing)         │    │
│  │  • Development workbench reference (feedback flow)       │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Workbench Lifecycle](./workbench-lifecycle.md) | Workbench states and transitions | 🔴 Stub |
| [Scenario Definitions](./scenario-definitions.md) | Scenario configuration | 🔴 Stub |
| [Trigger Definitions](./trigger-definitions.md) | Trigger configuration | 🔴 Stub |
| [Application Configuration](./application-configuration.md) | Hub Application setup | 🔴 Stub |

---

## Workbench Anatomy

A Workbench encapsulates a business domain:

```yaml
workbench:
  id: string
  name: string
  tenant_id: string
  
  # Workbench type
  workbench_type: string     # "business" (default) | "devops"
  
  # Domain context
  domain: string             # e.g., "dispute-resolution"
  description: string
  
  # Lifecycle stage
  dev_lifecycle_stage: string  # DEV | STAGING | PROD | custom
  
  # Development workbench reference (for non-DEV stages)
  development_workbench_ref: string  # ID of DEV-stage workbench
  
  # DevOps workbench association (optional)
  devops:
    reference:
      workbench_id: string           # Target DevOps workbench
      namespace: string              # Target namespace
      subscription_id: string        # If cross-subscription
      tenant_id: string              # If cross-tenant
    signal_routing:
      enabled: boolean
      sources:                       # Subsystem event sources
        - subsystem: string
          events: [string]
      filters: array                 # Optional event filters
    credentials:                     # Required if cross-subscription
      secret_ref:
        name: string
        namespace: string
      auth_type: string              # bot_token | service_account | mtls
  
  # Environment
  environments:
    - environment_id: string
      is_default: boolean
  
  # Scenarios
  scenarios:
    - id: string
      name: string
      application_id: string
      sop_ids: array
  
  # Triggers
  triggers:
    - id: string
      signal_source: string
      conditions: array
      transformation: object
      scenario_id: string
  
  # Access
  machine_access: array     # Machines accessible
  tool_access: array        # Tools available
  agent_groups: array       # Cipher groups enrolled
  
  # Request policies
  request_policies:
    lifecycle: object
    storage: object
    retention: object
  
  # Knowledge
  knowledge_bases: array    # Knowledge Bank collections
  sops: array               # Standard Operating Procedures
```

> **See also:** [DevOps Workbench Reference](../../02-system-design/implementation-concepts/devops-workbench-reference.md) for detailed `devops` configuration.

---

## Key Concepts

### Scenario
A Scenario represents a situational context activated by Triggers:
- Determines which Hub Application handles the Request
- Specifies which Roles are involved
- Links to relevant SOPs and Knowledge

### Trigger
A Trigger binds Signals to Scenarios:
- Matches signals based on conditions
- Transforms signal to Request format
- Routes to appropriate Scenario

### Hub Application
The automation artifact that executes a Scenario:
- Each Automation Runtime provides specialized types
- Configured per Scenario within Workbench

### Request Policy
Policies governing Request behavior within the Workbench:
- Lifecycle states and transitions
- Storage and retention
- Entity binding rules

---

## Workbench Lifecycle

```
[Draft] → [Validated] → [Published] → [Active] → [Archived]
              │
              └─→ [Rejected] → [Draft]
```

| State | Description |
|-------|-------------|
| **Draft** | Under development |
| **Validated** | Tested in sandbox |
| **Published** | Approved for deployment |
| **Active** | Processing signals |
| **Archived** | No longer active |

---

## Integration Points

| Component | Integration |
|-----------|-------------|
| **Signal Exchange** | Consumes trigger definitions |
| **Automation Runtimes** | Consumes application configurations |
| **Registry Services** | Machine, Tool, Environment access |
| **Cipher IAM** | Agent enrollment, role assignment |
| **Knowledge Services** | Knowledge Base associations |
| **Atropos** | DevOps signal routing to external workbenches |
| **DevOps Workbench** | Receives development lifecycle signals |
| **Scenario Design Desk** | UI for Scenario design (see UX Architecture) |
| **Automation Development Desk** | UI for Application development (see UX Architecture) |

---

## Related Documentation

- [Signal Exchange](../signal-exchange/README.md) — Data plane consuming definitions
- [Automation Runtimes](../automation-runtimes/README.md) — Hub Application hosts
- [Hub Architecture](../../02-system-design/hub-architecture.md) — Workbench concept
- [DevOps Workbench](../../09-composite-systems-and-patterns/devops-workbench/README.md) — Automated development operations
- [DevOps Workbench Reference](../../02-system-design/implementation-concepts/devops-workbench-reference.md) — Cross-workbench association
- [Scenario Design Desk](../../06-ux-architecture/tenant-domain/scenario-design-desk.md) — Scenario design UI
- [Automation Development Desk](../../06-ux-architecture/tenant-domain/automation-development-desk.md) — Application development UI

---

*TODO: Detailed design — schema validation, versioning, deployment pipeline*

