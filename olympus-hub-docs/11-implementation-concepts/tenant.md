# Tenant

> **Category:** Platform Foundation

---

## Overview

A **Tenant** is the top-level isolation boundary in Hub, representing a distinct organization or organizational unit. Each Tenant has complete separation of data, configurations, users, and operations from other Tenants. A Tenant contains one or more Subscriptions, which further subdivide resources for different environments or use cases.

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Domain** as a conceptual scope of business operations but doesn't address multi-tenancy or organizational isolation. Tenant is an implementation concept for platform-level isolation.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| (not covered) | Tenant | Top-level organizational isolation |
| Domain | Workbench (within Subscription within Tenant) | Domains realized within Tenant boundaries |

### Gap This Fills

The ontology focuses on operational concepts. Tenant addresses:
1. **Multi-tenancy**: How different organizations coexist on shared infrastructure
2. **Data isolation**: How tenant data is separated
3. **Identity boundaries**: How users belong to specific organizations
4. **Billing scope**: How resource usage is attributed

---

## Definition

**Tenant** is the highest-level isolation boundary that:
- Represents a distinct organization (e.g., a bank, enterprise)
- Contains one or more Subscriptions
- Has dedicated identity namespace in Cipher IAM
- Has separate billing and quota tracking
- Cannot access or see other Tenants' data

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Platform-wide; highest isolation unit |
| **Lifecycle** | Provisioned by SRE; managed by Hub operations |
| **Ownership** | Organization owns; Tenant Admin manages |
| **Multiplicity** | Hub hosts many Tenants |

---

## Rationale

### Why This Design?

Hub is designed for **regulated enterprises** requiring strict data isolation:
1. **Regulatory compliance**: Banks cannot share data with other banks
2. **Security boundaries**: Compromised tenant cannot affect others
3. **Independent operations**: Each tenant operates autonomously
4. **Clear billing**: Resource costs attributed to specific organization

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **No multi-tenancy** | Not scalable; separate deployments costly |
| **Soft isolation (tags only)** | Insufficient for regulated industries |
| **Tenant = Subscription** | Over-simplified; no environment separation |

---

## Structure

### Key Attributes

```yaml
tenant:
  id: "acme-bank"
  display_name: "ACME Bank"
  
  # Organizational info
  organization:
    legal_name: "ACME Banking Corporation"
    industry: "financial_services"
    region: "north_america"
  
  # Subscriptions within this tenant
  subscriptions:
    - id: "acme-dev"
      purpose: development
    - id: "acme-prod"
      purpose: production
  
  # Identity namespace
  identity:
    iam_realm: "acme-bank"
    user_directory_ref: "acme-ad-integration"
  
  # Billing
  billing:
    account_id: "bill-acme-001"
    plan: "enterprise"
  
  # Quotas (aggregate across subscriptions)
  quotas:
    max_subscriptions: 5
    max_users: 500
    max_workbenches_total: 50
```

### States

| State | Description | Transitions |
|-------|-------------|-------------|
| **Provisioning** | Tenant being created | → Active, Failed |
| **Active** | Normal operation | → Suspended, Deprovisioning |
| **Suspended** | Temporarily disabled | → Active, Deprovisioning |
| **Deprovisioning** | Being removed | → Terminated |
| **Terminated** | Fully removed | (terminal) |

---

## Behavior

### How It Works

```
1. Hub operations provisions Tenant
   └── Creates identity realm, billing account

2. SRE creates Subscriptions within Tenant
   └── Typically DEV and PROD subscriptions

3. Tenant Admin receives credentials
   └── Can manage users, subscriptions (within limits)

4. Tenant operates independently
   ├── Users in tenant identity namespace
   ├── Resources in tenant subscriptions
   └── Data isolated from other tenants
```

### Tenant Hierarchy

```
Platform (Hub)
└── Tenant (ACME Bank)
    ├── Subscription (acme-dev)
    │   ├── Workbench (dispute-ops-dev)
    │   └── Workbench (recon-dev)
    └── Subscription (acme-prod)
        ├── Workbench (dispute-ops-prod)
        └── Workbench (recon-prod)
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Subscription | ↓ contains | Tenant contains subscriptions |
| Cipher IAM | → configures | Tenant has identity realm |
| Billing | → attributed to | Resources billed to tenant |
| Hub Operations | ← managed by | SRE manages tenant lifecycle |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Complete isolation** | Tenant data never visible to other tenants |
| **Unique ID** | Tenant ID globally unique |
| **Identity namespace** | Users belong to exactly one tenant |
| **Resource attribution** | All resources attributed to tenant |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Complete isolation** | Regulatory compliance for sensitive industries |
| ✅ **Independent operations** | Tenants don't affect each other |
| ✅ **Clear billing** | Costs attributed to organization |
| ✅ **Scalable platform** | Single platform, many organizations |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **No cross-tenant sharing** | By design; use external integration for sharing |
| ⚠️ **Tenant provisioning overhead** | Automated provisioning; self-service where possible |

---

## Examples

### Example 1: Tenant Provisioning

```yaml
apiVersion: hub.olympus.io/v1
kind: Tenant
metadata:
  name: acme-bank
spec:
  display_name: "ACME Bank"
  
  organization:
    legal_name: "ACME Banking Corporation"
    industry: financial_services
    
  plan: enterprise
  
  quotas:
    max_subscriptions: 5
    max_users: 500
```

### Example 2: Tenant with Subscriptions

```
acme-bank (Tenant)
│
├── Identity: acme-bank realm in Cipher IAM
│   ├── admin@acme.com (Tenant Admin)
│   ├── developer@acme.com (Developer)
│   └── agent@acme.com (Agent)
│
├── acme-dev (Development Subscription)
│   ├── dispute-ops-dev (DEV Workbench)
│   └── recon-dev (DEV Workbench)
│
└── acme-prod (Production Subscription)
    ├── dispute-ops-prod (PROD Workbench)
    └── recon-prod (PROD Workbench)
```

---

## Implementation Notes

### For Developers

- You work within a single Tenant
- Your credentials are scoped to your Tenant
- You cannot access other Tenants' resources or data

### For Operators

- Provision Tenants during customer onboarding
- Monitor Tenant quota usage
- Handle Tenant suspension/deprovisioning
- Manage cross-subscription promotion within Tenant

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Subscription](./subscription.md) | Tenant contains Subscriptions |
| [Persona](./persona.md) | Users in Tenant have Personas |
| [Promotion](./promotion.md) | Promotion within and across Subscriptions (same Tenant) |

---

## References

- [Tenant Management Subsystem](../04-subsystems/tenant-management/README.md)
- [Cipher IAM Integration](../04-subsystems/iam-integration/README.md)

