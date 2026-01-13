# Automation Development Desk

> **Status:** 🔴 Stub — Placeholder for expansion

**Automation Development Desk** is the implementation environment for **Developers** to build, test, and deploy Hub Applications that automate scenarios within a Workbench.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | Developer |
| **Scope** | Workbench |
| **Access** | Web, MCP (Creator Gateway) |

---

## Purpose

The Developer owns the **technical implementation** of automation. This desk provides tools to:

1. **Build** — Implement Hub Applications based on normative specifications
2. **Test** — Validate functionality and integrations
3. **Deploy** — Release applications to production
4. **Maintain** — Monitor, debug, and update running applications

---

## Consoles

### Development Console

Build and implement Hub Applications.

| Capability | Description |
|------------|-------------|
| **Application Builder** | Create and configure Hub Applications |
| **Trigger Designer** | Implement signal matching and transformations |
| **Workflow Editor** | Build automation workflows |
| **Tool Integration** | Configure workbench-scoped tool bindings |
| **Code Editor** | Edit application code and configurations |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      DEVELOPMENT CONSOLE                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Applications                          │  Editor                            │
│  ┌────────────────────────────────┐   │  ┌──────────────────────────────┐  │
│  │ 📦 dispute-resolution-app      │   │  │ dispute-resolution-app.yaml  │  │
│  │    v1.2.0 (production)         │   │  │ ────────────────────────────  │  │
│  │ 📦 card-replacement-app        │   │  │ apiVersion: hub.olympus/v1   │  │
│  │    v0.9.0 (staging)            │   │  │ kind: HubApplication         │  │
│  │ 📦 fraud-detection-app         │   │  │ metadata:                    │  │
│  │    v2.1.0 (production)         │   │  │   name: dispute-resolution   │  │
│  └────────────────────────────────┘   │  │ spec:                        │  │
│                                        │  │   runtime: rhea              │  │
│  [+ New Application]                  │  │   triggers:                   │  │
│                                        │  │     - ref: dispute-filed     │  │
│                                        │  └──────────────────────────────┘  │
│                                        │                                     │
│                                        │  [Save]  [Validate]  [Test]        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Test Console

Test and validate applications.

| Capability | Description |
|------------|-------------|
| **Test Runner** | Execute functional and integration tests |
| **Signal Simulator** | Generate test signals |
| **Request Simulator** | Create test requests |
| **Mock Services** | Configure mock external services |
| **Test Reports** | View test results and coverage |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          TEST CONSOLE                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Test Suites                          │  Test Execution                     │
│  ┌────────────────────────────────┐   │  ┌──────────────────────────────┐  │
│  │ ✅ unit-tests (24/24)          │   │  │ Running: integration-tests   │  │
│  │ ⏳ integration-tests (3/15)    │   │  │ ────────────────────────────  │  │
│  │ ⬚ e2e-tests (0/8)              │   │  │ ✅ test_trigger_matching     │  │
│  └────────────────────────────────┘   │  │ ✅ test_request_creation     │  │
│                                        │  │ ✅ test_task_assignment      │  │
│  Signal Simulator                     │  │ ⏳ test_escalation_flow      │  │
│  ┌────────────────────────────────┐   │  │ ⬚ test_completion_handling   │  │
│  │ Source: card-network           │   │  │ ...                          │  │
│  │ Topic: disputes                │   │  └──────────────────────────────┘  │
│  │ Payload: {...}                 │   │                                     │
│  │ [Generate] [Send]              │   │  Progress: 3/15 (20%)              │
│  └────────────────────────────────┘   │  [Stop]  [Rerun Failed]            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Release Console

Deploy and manage application releases.

| Capability | Description |
|------------|-------------|
| **Deployment Manager** | Manage staged rollouts |
| **Version Control** | Track application versions |
| **Environment Manager** | Configure environment bindings |
| **Rollback** | Revert to previous versions |
| **Release Notes** | Document changes |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          RELEASE CONSOLE                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Application: dispute-resolution-app                                         │
│  ────────────────────────────────────────────────────────────────────────    │
│                                                                              │
│  Versions                                                                    │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ v1.2.0  │ production │ 2026-01-08 │ Current                          │  │
│  │ v1.1.0  │ production │ 2026-01-02 │ Previous                         │  │
│  │ v1.0.0  │ archived   │ 2025-12-15 │                                  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  Pending Deployment                                                          │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ v1.3.0  │ staging    │ Ready for production                          │  │
│  │ Changes: Enhanced escalation logic, bug fixes                        │  │
│  │ Tests: ✅ All passed    Approvals: ⏳ Supervisor pending              │  │
│  │ [Promote to Production]  [View Diff]  [Cancel]                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Tool Console

Manage workbench-scoped tools.

| Capability | Description |
|------------|-------------|
| **Tool Registry** | Browse and configure available tools |
| **Machine Bindings** | Connect tools to machine endpoints |
| **Access Configuration** | Define tool access policies |
| **Tool Testing** | Test tool invocations |

### UI Console

Build custom operational interfaces.

| Capability | Description |
|------------|-------------|
| **Angelos Page Builder** | Visual tool for building custom consoles |
| **Angelos Components** | Browse and configure UI components |
| **Angelos Binders** | Wire events between components |
| **Action Repository** | Catalog of pre-built actions |
| **Task Solver Templates** | Create custom task interfaces |

### Marketplace Console

Access Marketplace for publishing and subscribing to packages.

| Capability | Description |
|------------|-------------|
| **Package Discovery** | Browse and search available packages |
| **Package Creation** | Create Package Manifest CRDs |
| **Publishing** | Publish packages to Marketplace |
| **Subscription** | Subscribe to packages for workbench |
| **BlueprintSpec Usage** | Create derived resources from BlueprintSpecs |
| **Notifications** | View Marketplace notifications |

→ See [Marketplace Console](./marketplace-console.md) for details.

---

## Key Workflows

### 1. Application Development

```
Developer            Development Console      Scenario Design
 │                           │                       │
 ├─── View Spec ─────────────────────────────────────▶
 │◀── Normative Spec ────────────────────────────────│
 │                           │                       │
 ├─── Create App ───────────▶│                       │
 ├─── Configure Triggers ───▶│                       │
 ├─── Build Workflow ───────▶│                       │
 ├─── Integrate Tools ──────▶│                       │
 │                           │                       │
 ├─── Validate ─────────────▶│                       │
 │◀── Validation Result ─────┤                       │
 │                           │                       │
```

### 2. Test and Deploy

```
Developer             Test Console          Release Console
 │                           │                       │
 ├─── Run Tests ────────────▶│                       │
 │◀── Test Results ──────────┤                       │
 │                           │                       │
 │     (if tests pass)       │                       │
 │                           │                       │
 ├─── Create Release ────────────────────────────────▶
 │                           │                       │
 ├─── Deploy to Staging ─────────────────────────────▶
 │◀── Staging Deployed ──────────────────────────────│
 │                           │                       │
 ├─── Request Approval ──────────────────────────────▶
 │                           │           (Supervisor)│
 │◀── Approved ──────────────────────────────────────│
 │                           │                       │
 ├─── Promote to Prod ───────────────────────────────▶
 │◀── Production Live ───────────────────────────────│
 │                           │                       │
```

### 3. Supervisor Handoff

```
Developer            Release Console          Supervisor
 │                           │                       │
 ├─── App Ready ────────────▶│                       │
 │                           ├─── Notify Supervisor ▶│
 │                           │                       │
 │                           │◀── Configure Queues ──┤
 │                           │◀── Assign Agents ─────┤
 │                           │◀── Approve Deploy ────┤
 │                           │                       │
 │◀── Handoff Complete ──────┤                       │
 │                           │                       │
```

---

## Implementation Artifacts

### Hub Application CRD

```yaml
apiVersion: hub.olympus.tech/v1
kind: HubApplication
metadata:
  name: dispute-resolution-app
  workbench: dispute-operations
spec:
  # Automation runtime
  runtime: rhea
  
  # Trigger bindings
  triggers:
    - ref: dispute-filed-trigger
      scenario: dispute-triage
  
  # Workflow definition
  workflow:
    type: state-machine
    definition: |
      # Workflow definition...
  
  # Tool bindings
  tools:
    - name: card-network-api
      binding: machine/card-network
    - name: customer-lookup
      binding: machine/crm-system
  
  # Task definitions
  tasks:
    - type: triage
      solver: dispute-triage-solver
    - type: resolution
      solver: dispute-resolution-solver
```

### Trigger CRD

```yaml
apiVersion: hub.olympus.tech/v1
kind: Trigger
metadata:
  name: dispute-filed-trigger
  workbench: dispute-operations
spec:
  source:
    type: atropos
    topic: card-network.disputes
  
  match:
    event_type: "DISPUTE_FILED"
    
  transform:
    subject_id: "$.customer.id"
    case_id: "$.dispute.id"
```

---

## Integration with Other Desks

| Related Desk | Handoff |
|--------------|---------|
| **Scenario Design Desk** | PA → Developer: Normative spec to implement |
| **Supervisor Desk** | Developer → Supervisor: Application ready for deployment |
| **Steward Desk** | Visibility: Production monitoring and support |

---

## Channel Support

| Channel | Access | Documentation |
|---------|--------|---------------|
| **Web** | Full desk access | This document |
| **CLI** | Full development workflow via `hub` commands | [CLI Channels for Developers](./cli-channels-for-developers.md) |
| **MCP** | Application query, deployment triggers via Creator Gateway | — |
| **REST** | Programmatic CI/CD integration | — |

---

## Agent Lifecycle Console

The Automation Development Desk includes an **Agent Lifecycle Console** for managing Seer agents, including Persona Twins.

### Agent Lifecycle Views

```
Automation Development Desk
├── ...
├── Agent Lifecycle
│   ├── Training Specs
│   │   ├── Business Agents
│   │   └── Persona Twins (filtered view)
│   ├── Employed Agents
│   │   ├── Business Agents
│   │   └── Persona Twins (filtered view)
│   └── Blueprints
│       ├── Agent Blueprints
│       └── Persona Twin Blueprints
└── ...
```

### Persona Twin Filtering

The Agent Lifecycle Console supports filtering to show Persona Twins:

| Filter | Values | Description |
|--------|--------|-------------|
| `personaTwin` | `true` / `false` | Show only Persona Twins or exclude them |
| `delegator` | User reference | Filter by delegator (owner) |
| `blueprintSource` | Blueprint name | Filter by source blueprint |

### Sample Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      AGENT LIFECYCLE CONSOLE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  [Trained Agents]  [Employed Agents]  [Blueprints]                          │
│                                                                              │
│  Filters:  [Category: All ▼]  [Persona Twin: Yes ▼]  [Search...]           │
│                                                                              │
│  TRAINED AGENTS (Persona Twins)                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ Agent                  │ Delegator      │ Blueprint     │ State      │  │
│  │ ─────────────────────────────────────────────────────────────────────│  │
│  │ 🤖 john-task-assistant │ John Smith     │ task-triage   │ Published  │  │
│  │ 🤖 jane-summary-bot    │ Jane Manager   │ collaborator  │ Published  │  │
│  │ 🤖 sarah-monitor       │ Sarah Compliance│ compliance   │ Training   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  🤖 = Persona Twin                                                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Persona Twin Badge

Persona Twins are displayed with a distinct badge/indicator:
- **🤖** icon in list views
- **"Persona Twin"** badge in detail views
- **Delegator** field prominently displayed

### Persona Twin Creation for Developers

While any collaborator can create Persona Twins from blueprints, developers can also:
- Create custom Training Specs with advanced configuration
- Define custom OPA filter policies
- Create custom Persona Twin Blueprints for the team

---

## Related Documentation

- [Developer Persona](../../08-personas-and-journeys/personas/developer.md)
- [Scenario Development Journey](../../08-personas-and-journeys/journeys/scenario-development.md)
- [CLI Channels for Developers](./cli-channels-for-developers.md) — Command-line interface reference
- [Hub CLI Installation Guide](../../10-guides/hub-cli-setup.md) — CLI installation and setup
- [Scenario Design Desk](./scenario-design-desk.md) — Upstream: Normative specifications
- [Supervisor Desk](./supervisor-desk.md) — Downstream: Deployment and operations
- [Marketplace Console](./marketplace-console.md) — Package publishing and subscription
- [Angelos Framework](../frameworks-and-integrations/angelos-framework.md) — UI component framework
- [Rhea Runtime](../../04-subsystems/automation-runtimes/rhea-runtime.md) — Hub Application runtime
- [Persona Twins Concept](../../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md) — Persona Twin technical concept
- [Training Spec Manager](../../../olympus-seer-docs/seer-design/subsystems/trained-agent-lifecycle-manager/training-spec-manager.md) — Training Spec management
- [Employed Agent Directory](../../../olympus-seer-docs/seer-design/subsystems/agent-lifecycle-manager/employed-agent-directory.md) — Employed Agent registry

---

*TODO: Detailed CRD schemas, workflow authoring guide, deployment pipeline specifications*

