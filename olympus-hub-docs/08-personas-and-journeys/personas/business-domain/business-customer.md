# Business Domain Actor: Business Customer

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **Business Customer** is an external customer of the tenant's business whose interactions and service needs trigger **Service Requests** in Hub.

| Attribute | Value |
|-----------|-------|
| **Category** | Business Domain Actor |
| **Request Type** | Service Request |
| **Interaction** | Via Neutrino Channels, portals, apps, or assisted by Agents |

---

## Who Are Business Customers?

Business Customers are the end-users of the tenant's products and services:

| Industry | Examples |
|----------|----------|
| **Banking** | Account holders, loan applicants, credit card users |
| **Insurance** | Policyholders, claimants, beneficiaries |
| **Retail** | Buyers, loyalty members |
| **Telecom** | Subscribers, service users |
| **Healthcare** | Patients, members |

---

## How They Generate Requests

Business Customers trigger Service Requests through various channels:

| Channel | Example | Signal Provider |
|---------|---------|-----------------|
| **Self-Service Portal** | File a dispute online | Heracles |
| **Mobile App** | Report a lost card | Heracles |
| **Chat/Messaging** | Ask about account status | Neutrino |
| **Phone (Agent-Assisted)** | Request service change | Agent-initiated |
| **Email** | Submit documentation | Dia |

---

## Request Flow

```
Customer Action ──→ Signal ──→ Trigger ──→ Service Request ──→ Processing
       │                                          │
       │                                          ▼
       │                                   [Tasks Created]
       │                                          │
       └──────────── May complete ────────────────┘
                   Subject Tasks
```

---

## Hub Capabilities Consumed

Business Customers interact with Hub through **Neutrino Channels**, not Hub consoles directly.

### Self-Serve Capabilities (via Neutrino)

| Capability | What It Provides |
|------------|------------------|
| **Request Initiation** | Start Service Requests directly |
| **Status Tracking** | View request progress, timeline |
| **Subject Tasks** | Complete tasks assigned to them as Subject |
| **Document Upload** | Submit supporting documents |
| **Notifications** | Receive updates via preferred channel |

### Hub Services Accessed (Indirectly)

| Service | How Accessed |
|---------|--------------|
| **Heracles** | API gateway for self-serve portals |
| **Request Management** | View request status (read-only) |
| **Task Management** | Complete Subject tasks |
| **Notification Services** | Receive updates |

### Self-Serve Policy

```yaml
self_serve_policy:
  enabled: true
  allowed_user_groups:
    - "verified-customers"
    - "premium-members"
  
  can_initiate: true
  can_receive_tasks: true
  
  channels:
    - "customer-portal"
    - "mobile-app"
```

### What They Produce

| Output | Stored In |
|--------|-----------|
| Service Requests | Operations Data |
| Task Completions (Subject) | Operations Data |
| Documents | Application Data / Knowledge Bank |
| User Preferences | User Memory |

---

## Relationship to Hub Personas

| Relationship | Description |
|--------------|-------------|
| **Agent** | Agents process tasks within their Service Requests |
| **Supervisor** | Supervisors oversee SLAs for customer requests |
| **Subject of Request** | Customer is typically the Subject in Service Requests |

---

## Key Journeys

- [Request Lifecycle](../../journeys/request-lifecycle.md) — Primary journey (as request originator)

---

## Related Documentation

- [Request Types](../../../01-concepts/ontology-1-perception-layer.md)
- [Neutrino Channels](../../../06-ux-architecture/user-interaction-channels.md)
- [Self-Serve Policies](../../../04-subsystems/workbench-management/scenario-definitions.md)

---

*TODO: Channel experiences, notification patterns, self-serve workflows*

