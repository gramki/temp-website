# Hub Workbench Studio

> **Status:** 🔴 Stub — Placeholder for expansion

**Hub Workbench Studio** is the design and development environment for Process Architects and Developers to build operational scenarios and Hub Applications.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Personas** | Process Architect, Developer |
| **Scope** | Workbench |
| **Access** | Web, MCP (Creator Gateway) |

---

## Capabilities

### Design Capabilities (Process Architect)

| Capability | Description |
|------------|-------------|
| **Scenario Builder** | Define Signal → Trigger → Scenario → Operation flows |
| **SOP Editor** | Create and manage Standard Operating Procedures |
| **Knowledge Base Manager** | Organize SOPs, reference manuals, policies |
| **Memory Configuration** | Configure Enterprise Memory structure |
| **Role Definitions** | Map organizational roles to workbench roles |
| **Checklist Designer** | Create operational checklists |

### Development Capabilities (Developer)

| Capability | Description |
|------------|-------------|
| **Automation Builder [Agentic]** | Develop Hub Applications with AI-assisted development |
| **Automation Publisher [Agentic]** | Deploy applications with AI-assisted validation |
| **Trigger Designer** | Define signal matching, transformations |
| **Tool Registry** | Manage workbench-scoped tool configurations |
| **Testing & Debugging** | Test triggers, simulate requests |

> **[Agentic]** indicates AI-assisted development capabilities — AI helps with code generation, configuration validation, and best practice suggestions.

### UI Building Capabilities

| Capability | Description |
|------------|-------------|
| **Angelos Page Builder** | Visual tool for building custom consoles using Angelos web components |
| **Angelos Components & Binders** | Wire events between UI components |
| **Angelos Action Repository** | Catalog of pre-built actions available via Hercules (see below) |
| **Task Solver Templates** | Create custom task interfaces |

> **Angelos** is an internal framework for building web components. **Hercules** is a framework for web application development and hosting. The **Angelos Action Repository** is cataloged and made available through Hercules — all tenant developers can contribute actions, and the repository includes pre-built actions for common tasks against business entities and Hub platform entities.

---

## Screen Structure

```
Workbench Studio
├── Dashboard
│   ├── Workbench Overview
│   ├── Recent Changes
│   └── Deployment Status
│
├── Scenarios
│   ├── Scenario List
│   ├── Scenario Designer
│   │   ├── Signals
│   │   ├── Triggers
│   │   ├── Goals & SLAs
│   │   └── Roles
│   └── Scenario Manifest
│
├── Applications
│   ├── Application List
│   ├── Application Editor
│   ├── Trigger Configuration
│   └── Deployment Manager
│
├── Knowledge
│   ├── SOPs
│   ├── Reference Manuals
│   ├── Policies
│   └── Retrieval Configuration
│
├── Memory
│   ├── Memory Stores
│   ├── Schema Definitions
│   └── Access Policies
│
├── UI Builder
│   ├── Pages
│   ├── Components
│   ├── Actions
│   └── Task Solvers
│
├── Tools
│   ├── Tool Registry
│   ├── Machine Bindings
│   └── Access Configuration
│
└── Settings
    ├── Roles & Permissions
    ├── Environment Bindings
    └── Version History
```

---

## Scenario Builder

The Scenario Builder supports two perspectives:

### Process Architect Perspective

Visual, drag-drop tool or free-flow document for designing scenario components:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SCENARIO BUILDER (Process Architect)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Visual Canvas / Free-Flow Document                                  │    │
│  │                                                                      │    │
│  │  [Signal Sources] ──→ [Trigger Conditions] ──→ [Scenario Goals]     │    │
│  │                                                                      │    │
│  │  Drag components, connect flows, define SLAs                        │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Developer Perspective

CRDs/YAMLs that describe scenario components and their relationships:

```yaml
# Example Scenario CRD
apiVersion: hub.olympus.tech/v1
kind: Scenario
metadata:
  name: payment-dispute-filed
  workbench: dispute-operations
spec:
  signals:
    - source: atropos
      topic: card-network.disputes
  triggers:
    - ref: card-network-dispute-trigger
  application:
    ref: dispute-resolution-app
  goals:
    - id: resolve-dispute
      sla: P10D
```

---

## Related Documentation

- [Process Architect Persona](../08-personas-and-journeys/personas/process-architect.md)
- [Developer Persona](../08-personas-and-journeys/personas/developer.md)
- [Scenario Development Journey](../08-personas-and-journeys/journeys/scenario-development.md)
- [Angelos Framework](./angelos-framework.md)

---

*TODO: Detailed tool specifications, builder workflows, publishing process*

