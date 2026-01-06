# Subscription

> **Category:** Platform Foundation

---

## Overview

A **Subscription** is Hub's fundamental isolation and resource boundary within a Tenant. It represents a billing unit, security perimeter, and deployment context. Every Workbench, artifact, and runtime resource exists within exactly one Subscription, enabling multi-environment isolation (DEV vs PROD) and cross-tenant service delivery.

---

## Ontology Context

### Relationship to Ontology

The ontology defines a **Domain** as a conceptual scope of business operations, realized through a **Workbench**. However, the ontology doesn't address:
- How multiple environments (development, production) are isolated
- How billing and resource quotas are managed
- How artifacts move between environments safely

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Domain | Workbench | Workbenches exist within Subscriptions |
| (not covered) | Subscription | Provides isolation and resource boundary |

### Gap This Fills

The ontology assumes workbenches exist but doesn't address:
1. **Multi-environment isolation** — How do we separate DEV from PROD?
2. **Security boundaries** — How do we ensure DEV credentials can't access PROD?
3. **Resource management** — How are quotas, limits, and billing applied?
4. **Artifact provenance** — How do we track where artifacts come from?

Subscription addresses these requirements by providing a hard isolation boundary.

---

## Definition

**Subscription** is a resource and isolation boundary within a Tenant that provides:
- Dedicated container registry (snapshot and production)
- Dedicated Git repository for CRDs
- Independent credentials and access policies
- Separate workbenches at different lifecycle stages
- Distinct billing and quota tracking

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Within a Tenant; one Tenant can have multiple Subscriptions |
| **Lifecycle** | Created by SRE/Win Operator; managed by Tenant Admin |
| **Ownership** | Tenant Admin manages day-to-day; SRE for provisioning |
| **Multiplicity** | Typical: 2 per Tenant (DEV, PROD); can have more for complex setups |

---

## Rationale

### Why This Design?

Hub targets **small teams in regulated enterprises** (banks, financial services). These environments require:

1. **Separation of Duties**: Developers shouldn't have production access
2. **Audit Trails**: Clear record of what moved to production and when
3. **Security Isolation**: Compromised DEV credentials can't affect PROD
4. **Compliance**: Regulatory requirements often mandate environment separation

A Subscription provides distinct credentials, registries, and Git repositories — achieving environment isolation while remaining within the same Tenant's logical boundary.

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Single Subscription with tags** | Weaker isolation; shared credentials; compliance concerns |
| **Separate Tenants per environment** | Over-isolation; complicates cross-environment promotion |
| **Kubernetes namespaces only** | Insufficient isolation; shared secrets possible |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0045](../../decision-logs/0045-subscription-scoped-git-repository.md) | One Git repo per subscription, main branch only |
| [ADR-0048](../../decision-logs/0048-physical-copy-cross-subscription.md) | Physical copy for cross-subscription promotion |

---

## Structure

### Key Attributes

```yaml
subscription:
  id: "sub-acme-prod"
  tenant_id: "acme-bank"
  
  purpose: "production"  # development | production
  
  # Automatically provisioned
  registries:
    snapshot: "registry.hub.olympus.io/acme-bank/sub-acme-prod/snapshot"
    production: "registry.hub.olympus.io/acme-bank/sub-acme-prod/production"
  
  git_repository:
    url: "git.hub.olympus.io/acme-bank/sub-acme-prod"
    branch: "main"  # Always main
  
  # Workbenches within this subscription
  workbenches:
    - id: "dispute-ops-prod"
      dev_lifecycle_stage: "PROD"
    - id: "reconciliation-prod"
      dev_lifecycle_stage: "PROD"
  
  # Promotion destinations FROM this subscription
  promotion_destinations:
    - id: "to-prod"
      target_subscription: "sub-acme-prod"
      approval_required: true
  
  # Resource quotas
  quotas:
    max_workbenches: 10
    max_storage_gb: 500
    max_concurrent_requests: 1000
```

### States

| State | Description | Transitions |
|-------|-------------|-------------|
| **Provisioning** | Resources being created | → Active, Failed |
| **Active** | Normal operation | → Suspended, Deprovisioning |
| **Suspended** | Temporarily disabled (billing, policy) | → Active, Deprovisioning |
| **Deprovisioning** | Resources being removed | → Terminated |
| **Terminated** | Fully removed | (terminal) |

---

## Behavior

### How It Works

```
1. SRE/Win Operator creates Subscription CRD
   └── Specifies: tenant_id, purpose, quotas

2. Hub provisions resources:
   ├── Create snapshot registry
   ├── Create production registry
   ├── Create Git repository
   └── Configure access policies

3. Tenant Admin receives credentials
   └── Can now create Workbenches within Subscription

4. Workbenches operate within Subscription scope
   ├── All artifacts stored in subscription registries
   ├── All CRDs stored in subscription Git repo
   └── All runtime within subscription quotas

5. Promotion moves artifacts across subscriptions
   └── Physical copy with approval workflow
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Tenant | ↑ | Subscription belongs to exactly one Tenant |
| Workbench | ↓ | Subscription contains one or more Workbenches |
| Promotion Destination | → | Defines where artifacts can be promoted |
| Artifact Registry | ↓ | Subscription has dedicated registries |
| Git Repository | ↓ | Subscription has dedicated Git repo |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **One Tenant** | A Subscription belongs to exactly one Tenant |
| **Unique ID** | Subscription ID must be globally unique |
| **Registry isolation** | Registry credentials are subscription-specific |
| **Git isolation** | Git repo is subscription-specific, main branch only |
| **Workbench containment** | Every Workbench exists in exactly one Subscription |
| **Quota enforcement** | Resource usage must not exceed quotas |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Strong isolation** | Different credentials, registries, repos per subscription |
| ✅ **Compliance-friendly** | Meets regulated industry separation requirements |
| ✅ **Clear audit trail** | Promotion across subscriptions is explicitly logged |
| ✅ **Simple mental model** | DEV subscription vs PROD subscription is clear |
| ✅ **Independent scaling** | Each subscription can have independent quotas |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **More setup** | Sensible defaults; automated provisioning |
| ⚠️ **Promotion overhead** | Physical copy time; mitigated by lean containers |
| ⚠️ **Credential management** | Secure vault; automated rotation |

---

## Examples

### Example 1: Typical Two-Subscription Setup

```yaml
# DEV Subscription
apiVersion: hub.olympus.io/v1
kind: TenantSubscription
metadata:
  name: acme-dev
spec:
  tenant: acme-bank
  purpose: development
  quotas:
    max_workbenches: 5
    max_storage_gb: 100
---
# PROD Subscription
apiVersion: hub.olympus.io/v1
kind: TenantSubscription
metadata:
  name: acme-prod
spec:
  tenant: acme-bank
  purpose: production
  quotas:
    max_workbenches: 3
    max_storage_gb: 500
```

### Example 2: Workbenches Within Subscriptions

```
acme-dev (DEV Subscription)
├── dispute-ops-dev (DEV stage)
├── dispute-ops-staging (STAGING stage)
└── reconciliation-dev (DEV stage)

acme-prod (PROD Subscription)
├── dispute-ops-prod (PROD stage)
└── reconciliation-prod (PROD stage)
```

---

## Implementation Notes

### For Developers

- You typically work within a DEV subscription
- You cannot directly push to PROD subscription registries
- Promotion is your path to production
- Each subscription has its own credentials — don't mix them

### For Operators

- Provision subscriptions during tenant onboarding
- Monitor quota usage per subscription
- Manage promotion destinations and approval workflows
- Handle credential rotation per subscription

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Tenant](./tenant.md) | Subscription belongs to a Tenant |
| [Workbench](../../01-concepts/ontology-1-perception-layer.md#workbench) | Workbenches exist within Subscriptions |
| [Dev-Lifecycle-Stage](./dev-lifecycle-stage.md) | Tags workbenches within a Subscription |
| [Promotion](./promotion.md) | Moves artifacts across Subscriptions |
| [Artifact Registry](./artifact-registry.md) | Subscription-scoped container storage |

---

## References

- [Subscription Management Subsystem](../../04-subsystems/subscription-management/README.md)
- [Artifact Registry Subsystem](../../04-subsystems/artifact-registry/README.md)
- [ADR-0045: Subscription-Scoped Git Repository](../../decision-logs/0045-subscription-scoped-git-repository.md)
- [ADR-0048: Physical Copy Cross-Subscription](../../decision-logs/0048-physical-copy-cross-subscription.md)
- [Hub Development Flow Primer](../../10-guides/hub-development-flow/README.md)

