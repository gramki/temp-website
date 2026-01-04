# Admin Desk

> **Status:** 🔴 Stub — Placeholder for expansion

**Admin Desk** is the workbench-level administration console for configuring workbench-specific settings.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | Workbench Administrator (subset of Administrator role) |
| **Scope** | Workbench |
| **Access** | Web |

---

## Distinction from Hub Control Center

| Aspect | Hub Control Center | Admin Desk |
|--------|-------------------|------------|
| **Scope** | Tenant Subscription | Single Workbench |
| **Users** | Tenant Administrator | Workbench Administrator |
| **Focus** | Resource allocation, machines, tools | Workbench configuration, agents |

---

## Capabilities

| Capability | Description |
|------------|-------------|
| **Agent Enrollment** | Add/remove agents to workbench |
| **Queue Management** | Create queues, assign to scenarios |
| **Resource Allocation** | Configure workbench data stores, memory |
| **Tool Permissions** | Control which tools are available |
| **Notification Configuration** | Set up workbench-specific notifications |
| **Branding** | Workbench-specific theme overrides |

---

## Screen Structure

```
Admin Desk
├── Overview
│   ├── Workbench Status
│   ├── Active Scenarios
│   └── Agent Summary
│
├── Agents
│   ├── Agent List
│   ├── Role Assignment
│   └── Queue Enrollment
│
├── Queues
│   ├── Queue List
│   ├── Scenario Mapping
│   └── Escalation Configuration
│
├── Resources
│   ├── Data Stores
│   ├── Memory Stores
│   └── Knowledge Bases
│
├── Tools
│   ├── Available Tools
│   └── Access Policies
│
└── Settings
    ├── Notifications
    ├── Branding
    └── Integrations
```

---

## Related Documentation

- [Administrator Persona](../08-personas-and-journeys/personas/administrator.md)
- [Workbench Management](../04-subsystems/workbench-management/README.md)
- [Hub Control Center](./hub-control-center.md)

---

*TODO: Detailed configuration workflows, delegation model*

