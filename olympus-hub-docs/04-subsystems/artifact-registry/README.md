# Artifact Registry

> **Status:** 🟡 WIP — Core concepts defined

## Overview

The Artifact Registry subsystem manages the storage, versioning, and promotion of all Hub artifacts across subscriptions and workbenches. It provides a GitOps-based approach to managing Hub resources with OCI container registries for runtime artifacts.

### Target Audience

Hub is designed for **small teams in enterprise environments** (e.g., banks, financial services). This shapes the Artifact Registry design:

| Characteristic | Design Implication |
|----------------|-------------------|
| **Small teams** | Simple defaults, minimal configuration overhead |
| **Enterprise/Regulated** | All controls mandatory, audit trails non-negotiable |
| **Compliance requirements** | Approval workflows essential, not optional |
| **Multi-subscription** | DEV and PROD in separate subscriptions (near-physical separation) |

### Key Principles

| Principle | Description |
|-----------|-------------|
| **OCI-First** | All runtime artifacts are packaged as OCI containers |
| **GitOps Storage** | All CRDs and configurations stored in platform-managed Git |
| **Promotion-Based Flow** | Artifacts move through lifecycle stages via explicit promotion |
| **Subscription Isolation** | Each subscription has dedicated registries and Git repository |
| **Sensible Defaults** | Enterprise controls with minimal configuration for small teams |

---

## Recommended Baseline: Two-Subscription Model

For regulated enterprises, the **recommended baseline** is to use separate subscriptions for development and production contexts:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RECOMMENDED: TWO-SUBSCRIPTION MODEL                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                       PROD SUBSCRIPTION                   │
│   (Development Context)                  (Production Context)                │
│   ┌─────────────────────────┐           ┌─────────────────────────┐         │
│   │                         │           │                         │         │
│   │  ┌─────────┐           │  Promote  │           ┌─────────┐  │         │
│   │  │   DEV   │───────────┼──────────▶│───────────│  PROD   │  │         │
│   │  │Workbench│           │  Scenario │           │Workbench│  │         │
│   │  └─────────┘           │           │           └─────────┘  │         │
│   │                         │           │                         │         │
│   │  ┌─────────┐           │           │  ┌─────────┐           │         │
│   │  │ STAGING │           │           │  │  (UAT)  │ Optional  │         │
│   │  │Workbench│           │           │  │Workbench│           │         │
│   │  └─────────┘           │           │  └─────────┘           │         │
│   │                         │           │                         │         │
│   │  Snapshot Registry      │           │  Production Registry    │         │
│   │  Git Repository         │           │  Git Repository         │         │
│   │                         │           │                         │         │
│   └─────────────────────────┘           └─────────────────────────┘         │
│                                                                              │
│   WHY SEPARATE SUBSCRIPTIONS:                                                │
│   • Near-physical isolation (different registries, repos, credentials)       │
│   • Clear security boundary between dev and prod                            │
│   • Separate access control (dev team vs ops team)                          │
│   • Compliance requirement for many regulated industries                     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Default Promotion Path

A **pre-configured promotion path** is created between DEV and PROD subscriptions:

| Setting | Default Value |
|---------|---------------|
| Approval Required | Yes |
| Approver | Tenant Admin |
| Notifications | Admin + Requester |
| Artifacts Copied | Physical copy to PROD subscription registry |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ARTIFACT REGISTRY ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SUBSCRIPTION                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   ┌─────────────────────┐    ┌─────────────────────┐                │   │
│   │   │  SNAPSHOT REGISTRY  │    │ PRODUCTION REGISTRY │                │   │
│   │   │  ┌───────────────┐  │    │  ┌───────────────┐  │                │   │
│   │   │  │ Dev Builds    │  │───▶│  │ Released      │  │                │   │
│   │   │  │ Feature Work  │  │    │  │ Approved      │  │                │   │
│   │   │  └───────────────┘  │    │  └───────────────┘  │                │   │
│   │   └─────────────────────┘    └─────────────────────┘                │   │
│   │                                        │                             │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    GIT REPOSITORY                            │   │   │
│   │   │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │   │   │
│   │   │  │ Workbench│  │ Workbench│  │ Scenarios│  │ Shared   │     │   │   │
│   │   │  │ Specs    │  │ Configs  │  │          │  │ Resources│     │   │   │
│   │   │  └──────────┘  └──────────┘  └──────────┘  └──────────┘     │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                                                                      │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    WORKBENCHES                               │   │   │
│   │   │  ┌──────────┐  ┌──────────┐  ┌──────────┐                   │   │   │
│   │   │  │   DEV    │  │ STAGING  │  │   PROD   │                   │   │   │
│   │   │  │ (snapsh.)│  │ (prod)   │  │ (prod)   │                   │   │   │
│   │   │  └──────────┘  └──────────┘  └──────────┘                   │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   PROMOTION DESTINATIONS                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │   │
│   │  │ Same Tenant  │  │ Other Tenant │  │ Partner      │               │   │
│   │  │ Subscription │  │ Subscription │  │ Subscription │               │   │
│   │  └──────────────┘  └──────────────┘  └──────────────┘               │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Snapshot Registry** | Container registry for development builds; used by DEV workbenches |
| **Production Registry** | Container registry for released artifacts; used by non-DEV workbenches |
| **Dev-Lifecycle-Stage** | Tag indicating workbench lifecycle stage (DEV, STAGING, PROD, custom) |
| **Promotion Destination** | Configured target for artifact promotion (subscription or workbench) |
| **Promotion Path** | Developer-configured, admin-approved route for frequent promotions |
| **Git Repository** | Platform-managed repo holding all CRDs for a subscription |

---

## Core Responsibilities

- **Artifact Storage**: Manage OCI container registries per subscription
- **Version Management**: Track semantic versions and git-sha tags for all artifacts
- **Promotion Orchestration**: Coordinate artifact movement between workbenches/subscriptions
- **Git Repository Management**: Maintain subscription-scoped CRD storage
- **Sync Coordination**: Trigger reconciliation of CRDs to target workbenches
- **Migration Execution**: Run data store migrations during deployment

---

## Integration with Olympus Weave

The Artifact Registry relies on [Olympus Weave](https://weave.olympus.tech/getting-started/overview/) for underlying infrastructure:

| Hub Concept | Weave Mapping |
|-------------|---------------|
| Workbench | Weave Cluster |
| Container Registry | ECR / JFrog Artifactory (via Weave) |
| Deployment | Weave deployment primitives |

> **Note:** Hub abstracts Weave implementation details. Documentation references Weave capabilities without exposing specific providers.

---

## Artifact Types

All artifacts in Hub are either:

| Type | Storage | Description |
|------|---------|-------------|
| **OCI Containers** | Container Registry | Hub Application runtime artifacts |
| **Hub CRDs** | Git Repository | All configuration and specification resources |

> **Important:** Only Hub-defined CRDs are managed. No underlying infrastructure-specific CRDs (Kubernetes, Helm, etc.) are exposed.

---

## Components

| Component | Description | Documentation |
|-----------|-------------|---------------|
| Container Registry | Snapshot and Production registries | [container-registry.md](./container-registry.md) |
| Dev-Lifecycle-Stages | Workbench lifecycle tagging | [dev-lifecycle-stages.md](./dev-lifecycle-stages.md) |
| Promotion Model | Destinations, paths, approval | [promotion-model.md](./promotion-model.md) |
| Git Repository | Layout, sync, versioning | [git-repository.md](./git-repository.md) |
| Data Store Migrations | Migration CRDs, execution | [data-store-migrations.md](./data-store-migrations.md) |

---

## Versioning

All promotable artifacts use semantic versioning:

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]

Examples:
  1.0.0                    # Release version
  1.2.3-beta.1             # Pre-release
  1.2.3+abc123             # With git-sha build metadata
  1.2.3-rc.1+def456        # Pre-release with build metadata
```

### Version Sources

| Artifact | Version Source |
|----------|----------------|
| Workbench Specification | Explicit in spec |
| Scenario Specification | Explicit in spec |
| Hub Application Container | Tag on OCI image |
| Migration CRD | Explicit in spec (determines execution order) |

---

## Promotion Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PROMOTION FLOW                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SOURCE                           TARGET                                    │
│   ┌──────────────────┐            ┌──────────────────┐                      │
│   │                  │            │                  │                      │
│   │  DEV Workbench   │───────────▶│ STAGING Workbench│                      │
│   │  (Subscription A)│  Promote   │ (Subscription A) │                      │
│   │                  │  Scenario  │                  │                      │
│   └──────────────────┘            └──────────────────┘                      │
│           │                                │                                 │
│           │ Promote                        │ Promote                         │
│           │ Workbench                      │ Scenario                        │
│           ▼                                ▼                                 │
│   ┌──────────────────┐            ┌──────────────────┐                      │
│   │                  │            │                  │                      │
│   │ PROD Workbench   │            │ PROD Workbench   │                      │
│   │ (Subscription B) │            │ (Subscription C) │                      │
│   │                  │            │                  │                      │
│   └──────────────────┘            └──────────────────┘                      │
│                                                                              │
│   WHAT GETS PROMOTED:                                                        │
│   • Scenario: All associated artifacts (atomic unit)                         │
│   • Workbench: All scenarios + workbench-level resources                    │
│   • Subscription: All workbenches + subscription-level resources            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ See [promotion-model.md](./promotion-model.md) for complete details.

---

## Rollback

Rollback is supported to the **last deployed version only**.

| Rollback Scope | Behavior |
|----------------|----------|
| Scenario | Revert to previous scenario version |
| Workbench | Revert all scenarios to previous workbench version |
| Data Stores | Requires manual intervention (no automatic rollback) |

---

## Audit Trail

All promotion activities are logged:

| Event | Captured Data |
|-------|---------------|
| Promotion Request | Requester, source, target, artifacts, timestamp |
| Approval | Approver, decision, comments, timestamp |
| Deployment | Status, duration, errors, timestamp |
| Rollback | Initiator, reason, target version, timestamp |

Accessible via:
- **CD Console**: Admin and Developer views
- **Notification Services**: Configured recipients notified

---

## Related Documentation

- [CI Subsystem](../ci-subsystem/README.md) — Build and test infrastructure
- [Developer Operators](../operators/developer-operators.md) — CRD management
- [Notification Services](../notification-services/README.md) — Promotion notifications
- [Data Architecture](../../03-architecture/data-architecture.md) — Data store concepts

---

## Marketplace Integration

The Artifact Registry integrates with the [Marketplace Subsystem](../marketplace/README.md) for artifact sharing across tenants.

### Key Integration Points

| Integration | Description |
|-------------|-------------|
| **Lazy Container Cloning** | Marketplace containers cloned to tenant registry on first deployment |
| **Signature Verification** | Marketplace signature verified during container clone |
| **Blueprint-Derived Resources** | Containers referenced by derived resources cloned on deployment |

### Container Cloning Flow

```
Marketplace Artifact Repository
            │
            │ First deployment triggers clone
            ▼
Tenant Production Registry
            │
            │ Available for workbench use
            ▼
Workbench Deployment
```

→ See [Marketplace Artifact Repository](../marketplace/marketplace-artifact-repository.md) for details.

---

## Open Points

See [open-points.md](./open-points.md) for unresolved questions.


