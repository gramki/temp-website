# Hub Control Center

> **Status:** 🔴 Stub — Placeholder for expansion

The **Hub Control Center** is the administrative console for Tenant Administrators to manage their Hub subscription.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | Administrator |
| **Scope** | Tenant Subscription |
| **Access** | Web, MCP (Tenant Admin Gateway) |

---

## Capabilities

### Subsystems Configuration

| Subsystem | Configuration |
|-----------|---------------|
| **Task Management** | Queues, escalation defaults, SLA templates |
| **API Gateway (Heracles)** | Endpoints, rate limits, vanity domains, certificates |
| **Event Bus (Atropos)** | Topics, subscriptions, retention |
| **File Gateway (Dia)** | File stores, ingestion pipelines |
| **Automation Engines** | Runtime quotas, deployment settings |
| **Notification Services** | Channels, templates, delivery policies |

### Tenant Ecosystem Setup

| Area | Capabilities |
|------|--------------|
| **User & Access Management** | Provision users, assign roles, manage domains |
| **Machine Registry Management** | Register machines, configure endpoints |
| **Tool Registry Management** | Define tools, set access policies |
| **Workbench Management** | Create workbenches, assign resources |
| **Environments Management** | Configure operational environments |

---

## Screen Structure

```
Hub Control Center
├── Dashboard
│   ├── Subscription Overview
│   ├── Usage Summary
│   └── Alerts & Issues
│
├── Subsystems
│   ├── Task Management
│   ├── API Gateway
│   ├── Event Bus
│   ├── File Gateway
│   ├── Automation Engines
│   └── Notifications
│
├── Ecosystem
│   ├── Users & Access
│   ├── Machines
│   ├── Tools
│   ├── Workbenches
│   └── Environments
│
├── Budget & Usage
│   ├── Resource Usage
│   ├── Cost Tracking
│   └── Quotas
│
└── Settings
    ├── Branding & Themes
    ├── Identity Domains
    └── Support & Contact
```

---

## Related Documentation

- [Administrator Persona](../08-personas-and-journeys/personas/administrator.md)
- [Subscription Management](../04-subsystems/subscription-management/README.md)
- [Subscription Configuration Guide](../10-guides/subscription-configuration-guide.md)

---

*TODO: Detailed screen specifications, wireframes, interaction patterns*

