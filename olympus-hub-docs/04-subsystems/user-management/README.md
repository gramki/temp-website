# User Management

> **Status:** 🔴 Stub — Placeholder for expansion

User Management is responsible for managing all user personas across different scopes within Olympus Hub, from system-level operators to tenant customers.

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Purpose** | Manage users across all scopes and personas |
| **IAM** | Cipher provides authentication and authorization for all users |
| **Scopes** | Hub System, Tenant Subscription, Workbench, Tenant Customers |
| **Domains** | Publisher Domain (Zeta) + Tenant Domains |

---

## User Scope Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                    HUB SYSTEM SCOPE                              │
│                   (Publisher Domain - Zeta)                      │
│                                                                  │
│   ┌─────────────────┐  ┌─────────────────────────────────────┐  │
│   │      SRE        │  │    Customer Success Executive       │  │
│   └─────────────────┘  └─────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│               TENANT SUBSCRIPTION SCOPE                          │
│                  (Tenant Domain(s))                              │
│                                                                  │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌────────┐  │
│  │Administrator │ │   Process    │ │  Developer   │ │Auditor │  │
│  │              │ │  Architect   │ │              │ │        │  │
│  └──────────────┘ └──────────────┘ └──────────────┘ └────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    WORKBENCH SCOPE                               │
│                                                                  │
│           ┌──────────────┐    ┌──────────────┐                  │
│           │    Agent     │    │  Supervisor  │                  │
│           └──────────────┘    └──────────────┘                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   TENANT CUSTOMERS                               │
│                                                                  │
│              ┌────────────────────────────────┐                 │
│              │     Self-Serve Users           │                 │
│              │  (per Scenario self-serve      │                 │
│              │        policy)                 │                 │
│              └────────────────────────────────┘                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Hub System Users](./hub-system-users.md) | SRE and Customer Success personas | 🔴 Stub |
| [Tenant Subscription Users](./tenant-subscription-users.md) | Administrators, Architects, Developers, Auditors | 🔴 Stub |
| [Workbench Users](./workbench-users.md) | Agents and Supervisors | 🔴 Stub |
| [Tenant Customers](./tenant-customers.md) | Self-serve users and policies | 🔴 Stub |
| [Domain Management](./domain-management.md) | Publisher and Tenant domains | 🔴 Stub |

---

## User Personas Summary

### Hub System Scope (Publisher Domain)

| Persona | Responsibilities |
|---------|------------------|
| **SRE** | Deploy and maintain Hub System. Ensure availability, capacity, and security. Monitor usage and cost. Provide technical assistance (network, security) for tenant resource configuration. |
| **Customer Success Executive** | Create tenant subscriptions. Review usage. Provide usage assistance. |

### Tenant Subscription Scope

| Persona | Responsibilities |
|---------|------------------|
| **Administrator** | Manage subscription, machines, and users. Configure resources and services. Interact with system providers for support. |
| **Process Architect** | Define Workbenches and Scenarios. Specify org knowledge and org memory. Define roles and groups in Cipher IAM. |
| **Developer** | Create and manage Requests and Applications. Deploy applications. Enrol machines and tools. |
| **Auditor** | Review compliance of operations across the organisation. |

### Workbench Scope

| Persona | Responsibilities |
|---------|------------------|
| **Agent** | Complete assigned tasks or reassign. Investigate business domain entities and signals. Trigger scenarios explicitly when required. |
| **Supervisor** | Review SLAs, agent efficiency, and operations effectiveness. Define and manage task queues. Enrol/remove agents from queues. Manage escalation matrix. Control agent availability for assignment. |

### Tenant Customers

| Persona | Responsibilities |
|---------|------------------|
| **Self-Serve User** | Initiate requests when enabled by scenario self-serve policy. May be assigned tasks if scenario policy allows subject assignment. |

---

## Domain Model

### Publisher Domain

The **Publisher Domain** is managed by the creator of Olympus Hub (Zeta):
- Contains Hub System scoped users (SRE, Customer Success)
- Managed entirely by Zeta
- Isolated from tenant domains

### Tenant Domains

Tenants can organize their users across domains as they prefer:
- **Single Domain**: All tenant personas in one domain
- **Multiple Domains**: Separate domains for different user groups
- **Federated**: Integration with tenant's existing identity providers

```
Publisher Domain (Zeta)
├── SREs
└── Customer Success Executives

Tenant Domain(s)
├── Administrators
├── Process Architects
├── Developers
├── Auditors
├── Agents
├── Supervisors
└── Customer Users (Self-Serve)
```

---

## Integration with Cipher IAM

All users are managed through Cipher IAM:

| Function | Cipher Capability |
|----------|-------------------|
| **Authentication** | SSO, MFA, password policies |
| **Authorization** | Role-based access control (RBAC) |
| **Federation** | SAML, OIDC for tenant identity providers |
| **Agent Identity** | SPIFFE-based identities for AI agents |
| **Domain Management** | Multi-domain support |

---

## Access Control Model

| Scope | Access Pattern |
|-------|----------------|
| **Hub System** | Publisher domain credentials, system-level permissions |
| **Tenant Subscription** | Tenant domain credentials, subscription-level permissions |
| **Workbench** | Tenant domain credentials, workbench-scoped permissions |
| **Tenant Customers** | Customer domain credentials, scenario-scoped permissions |

---

## Related Documentation

- [Cipher IAM](../supporting-systems/cipher-iam.md) — Identity and access management
- [Subscription Management](../subscription-management/README.md) — Tenant subscription administration
- [Administrators Management](../subscription-management/administrators-management.md) — Admin roles and permissions
- [Workbench Management](../workbench-management/README.md) — Workbench configuration
- [Task Management](../task-management/README.md) — Task assignment and queues

---

*TODO: Detailed design — persona lifecycle, permission matrices, domain federation*

