# Workbench Studio

> **Status:** 🔴 Stub — Placeholder for expansion

**Workbench Studio** is the design and development environment for Process Architects and Developers to build operational scenarios and Hub Applications.

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
| **Automation Builder** | Develop Hub Applications with runtime SDKs |
| **Automation Publisher** | Deploy applications to Automation Runtimes |
| **Trigger Designer** | Define signal matching, transformations |
| **Tool Registry** | Manage workbench-scoped tool configurations |
| **Testing & Debugging** | Test triggers, simulate requests |

### UI Building Capabilities

| Capability | Description |
|------------|-------------|
| **Angelos Page Builder** | Visual tool for building custom consoles |
| **Angelos Components & Binders** | Wire events between UI components |
| **Angelos Action Repository** | Define reusable actions |
| **Task Solver Templates** | Create custom task interfaces |

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

## Scenario Builder Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SCENARIO BUILDER                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐           │
│  │  Signal  │ ──→ │ Trigger  │ ──→ │ Scenario │ ──→ │   Hub    │           │
│  │ Selector │     │ Designer │     │ Config   │     │   App    │           │
│  └──────────┘     └──────────┘     └──────────┘     └──────────┘           │
│                                                                              │
│  1. Select Signal   2. Define        3. Set Goals    4. Link to            │
│     Sources            Conditions       & SLAs          Application         │
│                        & Transform                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [Process Architect Persona](../08-personas-and-journeys/personas/process-architect.md)
- [Developer Persona](../08-personas-and-journeys/personas/developer.md)
- [Scenario Development Journey](../08-personas-and-journeys/journeys/scenario-development.md)
- [Angelos Framework](./angelos-framework.md)

---

*TODO: Detailed tool specifications, builder workflows, publishing process*

