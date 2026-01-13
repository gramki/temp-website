# Subscription Management

> **Status:** 🔴 Stub — Placeholder for expansion

Subscription Management is the **tenant administration subsystem** responsible for managing tenant subscriptions, resources, configurations, and administrative access within Olympus Hub.

---

## Overview

| Function | Description |
|----------|-------------|
| **Tenant Subscription Lifecycle** | Provisioning, activation, suspension, and termination of tenant subscriptions |
| **Resource Management** | Allocation and management of platform resources |
| **Resource Configuration** | Configuration of resources for tenant use |
| **Budget Management** | Quotas, limits, and usage tracking |
| **Branding and Themes** | Tenant-specific customization and white-labeling |
| **Administrators Management** | Tenant administrator access and permissions |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   SUBSCRIPTION MANAGEMENT                        │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │            TENANT SUBSCRIPTION LIFECYCLE                 │    │
│  │                                                          │    │
│  │   [Provisioned] → [Active] → [Suspended] → [Terminated] │    │
│  │                       ↓                                  │    │
│  │                  [Upgraded/Downgraded]                   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 RESOURCE MANAGEMENT                      │    │
│  │                                                          │    │
│  │   ┌────────────┐ ┌────────────┐ ┌────────────────────┐  │    │
│  │   │   Data     │ │  Memory    │ │    Knowledge       │  │    │
│  │   │   Stores   │ │  Stores    │ │      Stores        │  │    │
│  │   └────────────┘ └────────────┘ └────────────────────┘  │    │
│  │                                                          │    │
│  │   ┌────────────┐ ┌────────────┐ ┌────────────────────┐  │    │
│  │   │  Machines  │ │    I/O     │ │   Notification     │  │    │
│  │   │            │ │  Gateways  │ │     Services       │  │    │
│  │   └────────────┘ └────────────┘ └────────────────────┘  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │               CONFIGURATION & QUOTAS                     │    │
│  │                                                          │    │
│  │   • Resource configuration per tenant                    │    │
│  │   • Budget and quota management                          │    │
│  │   • Usage tracking and alerts                            │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              TENANT CUSTOMIZATION                        │    │
│  │                                                          │    │
│  │   • Branding (logos, colors, fonts)                      │    │
│  │   • Themes (light/dark, custom)                          │    │
│  │   • White-labeling                                       │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │             ADMINISTRATORS MANAGEMENT                    │    │
│  │                                                          │    │
│  │   • Tenant admin provisioning                            │    │
│  │   • Admin roles and permissions                          │    │
│  │   • Admin access audit                                   │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Tenant Subscription Lifecycle](./tenant-subscription-lifecycle.md) | Subscription states and transitions | 🔴 Stub |
| [Resource Management](./resource-management.md) | Resource allocation and management | 🔴 Stub |
| [Resource Configuration](./resource-configuration.md) | Resource configuration per tenant | 🔴 Stub |
| [Budget Management](./budget-management.md) | Quotas, limits, and usage tracking | 🔴 Stub |
| [Branding and Themes](./branding-themes.md) | Tenant customization and white-labeling | 🔴 Stub |
| [Administrators Management](./administrators-management.md) | Tenant admin access and permissions | 🔴 Stub |

---

## Key Concepts

### Tenant

A **Tenant** represents an organization using Olympus Hub:

| Aspect | Description |
|--------|-------------|
| **Identity** | Unique tenant ID, domain |
| **Subscription** | Plan, tier, billing cycle |
| **Resources** | Allocated platform resources |
| **Users** | Tenant users and administrators |
| **Workbenches** | Tenant's operational workbenches |

### Subscription Tiers

| Tier | Description | COGW |
|------|-------------|------|
| **Starter** | Basic resources, limited quotas | ❌ Not included |
| **Professional** | Standard resources, moderate quotas | ✅ Default COGW |
| **Enterprise** | Full resources, high quotas, dedicated support | ✅ Default COGW + Custom COGWs |
| **Custom** | Tailored configuration | Configurable |

### Default COGW Creation

Eligible subscriptions automatically receive a default Cognitive Operations Governance Workbench (COGW) at creation:

| Aspect | Behavior |
|--------|----------|
| **Trigger** | Subscription creation |
| **Name** | `<subscription-id>-default-cogw` |
| **Content** | Standard governance scenarios |
| **Deletable** | Yes |

> See [COGW Specification](../../../olympus-seer-docs/seer-design/subsystems/cognitive-operations-governance-workbench/cogw-specification.md) for details.

### Managed Resources

| Resource Type | Examples |
|---------------|----------|
| **Data Stores** | PostgreSQL, MongoDB instances for operations data |
| **Memory Stores** | Agent memory, enterprise memory storage |
| **Knowledge Stores** | RAG vector stores, knowledge bank storage |
| **Machines** | Registered external systems and integrations |
| **I/O Gateways** | Configured signal providers (Atropos, Heracles, etc.) |
| **Notification Services** | Email, SMS, push notification channels |
| **Compute** | Automation system allocations |

---

## Marketplace Publisher Registration

Subscription Management handles the **publisher registration workflow** for tenants who want to publish packages to the Marketplace.

### Registration Flow

```
Tenant Admin initiates registration
         │
         │ Submits: Publisher name, contact, signing certificate
         ▼
Hub Win Team reviews
         │
         │ Validates: Business legitimacy, certificate
         ▼
Approval/Rejection
         │
         │ If approved: Publisher status activated
         ▼
Tenant can now publish packages
```

### Registration Requirements

| Requirement | Description |
|-------------|-------------|
| **Initiator** | Tenant Admin |
| **Approver** | Hub Win (Customer Success) team |
| **Certificate** | Valid signing certificate required |
| **Status** | Active subscription required |

→ See [Marketplace Publishing Services](../marketplace/publishing-services.md) for details.

---

## Integration Points

| Component | Integration |
|-----------|-------------|
| **Cipher IAM** | Administrator authentication and authorization |
| **Registry Services** | Machine, Tool, Environment registrations |
| **Workbench Management** | Workbench provisioning within subscription |
| **Memory Services** | Memory store allocation |
| **Knowledge Services** | Knowledge store allocation |
| **Signal Providers** | I/O Gateway configuration |
| **Marketplace** | Publisher registration and management |
| **Billing System** | Usage metering and billing (external) |

---

## Related Documentation

- [Cipher IAM](../supporting-systems/cipher-iam.md) — Identity and access management
- [Registry Services](../registry-services/README.md) — Resource registrations
- [Workbench Management](../workbench-management/README.md) — Workbench administration

---

*TODO: Detailed design — provisioning workflows, quota enforcement, billing integration*

