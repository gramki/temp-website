# Tenant Subscription Users

> **Status:** 🔴 Stub — Placeholder for expansion

Tenant Subscription Users operate at the subscription level and are responsible for configuring, developing, and auditing the tenant's use of Olympus Hub.

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Scope** | Tenant Subscription |
| **Domain** | Tenant Domain(s) — configurable by tenant |
| **Personas** | Administrator, Process Architect, Developer, Auditor |
| **Access** | Subscription-wide, may be scoped to specific workbenches |

---

## Personas

### Administrator

| Attribute | Description |
|-----------|-------------|
| **Primary Focus** | Subscription and user management |
| **Scope** | Entire tenant subscription |

#### Responsibilities

| Area | Responsibilities |
|------|------------------|
| **Subscription** | Manage subscription settings and tier |
| **Machines** | Register and configure external machines |
| **Users** | Manage all tenant users across personas |
| **Resources** | Configure data stores, memory stores, knowledge stores |
| **Services** | Configure I/O gateways, notification services |
| **Support** | Interact with system providers (Zeta) for technical and administrative support |

#### Permissions

| Permission | Scope |
|------------|-------|
| Manage subscription | Full |
| Manage users | All tenant users |
| Configure resources | All resources |
| Register machines | All |
| View billing | Full |
| Access audit logs | Full |

---

### Process Architect

| Attribute | Description |
|-----------|-------------|
| **Primary Focus** | Operational design and knowledge modeling |
| **Scope** | Workbenches and scenarios |

#### Responsibilities

| Area | Responsibilities |
|------|------------------|
| **Workbenches** | Define and configure workbenches |
| **Scenarios** | Define scenarios and triggers |
| **Knowledge** | Specify org knowledge required for workbenches |
| **Memory** | Define org memory requirements |
| **Roles & Groups** | Define roles and groups in Cipher IAM for workbench agents |
| **SOPs** | Document and configure Standard Operating Procedures |

#### Permissions

| Permission | Scope |
|------------|-------|
| Create workbenches | Full |
| Configure scenarios | Assigned workbenches |
| Manage knowledge bases | Assigned workbenches |
| Define roles/groups | Workbench scope |
| View operational data | Assigned workbenches |
| Deploy applications | No (Developer role) |

---

### Developer

| Attribute | Description |
|-----------|-------------|
| **Primary Focus** | Application development and deployment |
| **Scope** | Applications and integrations |

#### Responsibilities

| Area | Responsibilities |
|------|------------------|
| **Applications** | Create and manage Hub Applications for scenarios |
| **Deployment** | Deploy applications to automation runtimes |
| **Support** | Support application use and troubleshooting |
| **Machines** | Enrol machines required for applications |
| **Tools** | Register and configure tools |
| **Testing** | Test applications in sandbox environments |

#### Permissions

| Permission | Scope |
|------------|-------|
| Create applications | Assigned scenarios |
| Deploy applications | Assigned environments |
| Register machines | Limited |
| Register tools | Limited |
| Access logs | Application scope |
| View operational data | Application scope |

---

### Auditor

| Attribute | Description |
|-----------|-------------|
| **Primary Focus** | Compliance and governance |
| **Scope** | Entire tenant subscription (read-only) |

#### Responsibilities

| Area | Responsibilities |
|------|------------------|
| **Compliance** | Review compliance of operations |
| **Audit Trail** | Review decision records and evidence bundles |
| **Policy** | Verify policy adherence |
| **Reporting** | Generate compliance reports |
| **Investigation** | Investigate specific requests or decisions |

#### Permissions

| Permission | Scope |
|------------|-------|
| View operational data | Full (read-only) |
| View decision records | Full |
| View evidence bundles | Full |
| View audit logs | Full |
| Generate reports | Full |
| Modify anything | No |

---

## Domain Organization

Tenants can organize these personas across domains as they prefer:

| Pattern | Description |
|---------|-------------|
| **Single Domain** | All personas in one tenant domain |
| **Separated** | Admins in one domain, operational users in another |
| **Federated** | Integrated with tenant's existing identity providers |

---

## Related Documentation

- [User Management Overview](./README.md)
- [Hub System Users](./hub-system-users.md)
- [Workbench Users](./workbench-users.md)
- [Workbench Management](../workbench-management/README.md)

---

*TODO: Detailed design — permission matrices, delegation patterns, approval workflows*

