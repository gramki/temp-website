# Hub System Users

> **Status:** 🔴 Stub — Placeholder for expansion

Hub System Users operate at the platform level within the Publisher Domain (Zeta) and are responsible for the overall operation and support of Olympus Hub.

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Scope** | Hub System (entire platform) |
| **Domain** | Publisher Domain (Zeta) |
| **Personas** | SRE, Customer Success Executive |
| **Access** | Cross-tenant visibility for support and operations |

---

## Personas

### SRE (Site Reliability Engineer)

| Attribute | Description |
|-----------|-------------|
| **Primary Focus** | Platform reliability, availability, and security |
| **Domain** | Publisher Domain |
| **Cross-Tenant** | Yes — can access tenant environments for support |

#### Responsibilities

| Area | Responsibilities |
|------|------------------|
| **Deployment** | Deploy and maintain the Hub System infrastructure |
| **Availability** | Ensure system availability and uptime SLAs |
| **Capacity** | Monitor and manage capacity, scaling |
| **Security** | Maintain platform security posture |
| **Monitoring** | Monitor usage, performance, and cost |
| **Technical Support** | Provide technical assistance for tenant configuration (network, security, etc.) |
| **Resource Configuration** | Assist tenants with resource and machine access configuration |

#### Permissions

| Permission | Scope |
|------------|-------|
| View all tenants | System-wide |
| Access infrastructure | System-wide |
| View tenant configurations | On-demand (support) |
| Modify tenant resources | With approval |
| Access audit logs | System-wide |
| Manage platform settings | System-wide |

---

### Customer Success Executive

| Attribute | Description |
|-----------|-------------|
| **Primary Focus** | Tenant success and adoption |
| **Domain** | Publisher Domain |
| **Cross-Tenant** | Limited — usage visibility, not operational data |

#### Responsibilities

| Area | Responsibilities |
|------|------------------|
| **Subscription Management** | Create and manage tenant subscriptions |
| **Usage Review** | Review tenant usage patterns and trends |
| **Usage Assistance** | Provide guidance on Hub utilization |
| **Onboarding** | Support tenant onboarding process |
| **Relationship** | Maintain tenant relationships |

#### Permissions

| Permission | Scope |
|------------|-------|
| Create subscriptions | System-wide |
| View tenant usage | Aggregated |
| View tenant subscription details | Assigned tenants |
| Access billing information | Assigned tenants |
| View tenant health dashboards | System-wide |
| Modify tenant configurations | No |

---

## Separation from Tenant Operations

Hub System Users:
- **Cannot** access tenant operational data (requests, decisions, business data)
- **Cannot** impersonate tenant users
- **Can** access tenant configuration and usage metrics
- **Can** access tenant systems for technical support (with audit trail)

---

## Audit and Accountability

| Action | Audit |
|--------|-------|
| Tenant access | Logged with reason, duration |
| Configuration changes | Logged with before/after |
| Support interventions | Ticketed and logged |
| Subscription changes | Logged with approvals |

---

## Related Documentation

- [User Management Overview](./README.md)
- [Tenant Subscription Users](./tenant-subscription-users.md)
- [Subscription Management](../subscription-management/README.md)

---

*TODO: Detailed design — support escalation paths, cross-tenant access controls*

