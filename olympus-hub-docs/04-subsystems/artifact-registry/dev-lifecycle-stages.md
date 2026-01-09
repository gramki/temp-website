# Dev-Lifecycle-Stages

## Overview

Every Workbench in Hub is assigned a **Dev-Lifecycle-Stage** tag that indicates its position in the software development lifecycle. This tag determines which artifact registries the workbench can access and how it participates in promotion flows.

> **Terminology Note:** We use "Dev-Lifecycle-Stage" rather than "Environment" to avoid confusion with **Hub Environment** — a business/operations domain entity used for runtime configuration.

---

## Recommended Baseline: Two-Subscription Model

For regulated enterprises (Hub's target audience), the **recommended baseline** uses separate subscriptions to achieve near-physical separation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TWO-SUBSCRIPTION MODEL (RECOMMENDED)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                       PROD SUBSCRIPTION                   │
│   ┌─────────────────────────┐           ┌─────────────────────────┐         │
│   │                         │           │                         │         │
│   │  dispute-ops-dev (DEV)  │           │  dispute-ops-prod (PROD)│         │
│   │           │             │           │                         │         │
│   │           ▼             │  ──────▶  │                         │         │
│   │  dispute-ops-stg (STAG) │  Promote  │                         │         │
│   │                         │           │                         │         │
│   │  Snapshot Registry      │           │  Production Registry    │         │
│   │                         │           │                         │         │
│   └─────────────────────────┘           └─────────────────────────┘         │
│                                                                              │
│   BENEFITS:                                                                  │
│   • Separate registries, repos, credentials                                 │
│   • Clear security boundary                                                 │
│   • Different access control (dev team vs ops)                              │
│   • Compliance requirement for regulated industries                         │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

| Subscription | Contains | Registry Access |
|--------------|----------|-----------------|
| **DEV Subscription** | DEV and STAGING workbenches | Snapshot + Production |
| **PROD Subscription** | PROD workbenches only | Production only |

> **Note:** STAGING can be in DEV subscription (for internal validation) or PROD subscription (for pre-prod), depending on organizational requirements.

---

## Default Stages

| Stage | Registry Access | Purpose |
|-------|-----------------|---------|
| **DEV** | Snapshot | Active development, feature work |
| **STAGING** | Production | Pre-production testing, validation |
| **PROD** | Production | Production operations |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEV-LIFECYCLE-STAGE FLOW                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│     DEV                    STAGING                   PROD                    │
│   ┌───────┐              ┌───────┐               ┌───────┐                  │
│   │       │   Promote    │       │   Promote     │       │                  │
│   │  DEV  │─────────────▶│STAGING│──────────────▶│ PROD  │                  │
│   │       │   Scenario   │       │   Scenario    │       │                  │
│   └───────┘              └───────┘               └───────┘                  │
│       │                      │                       │                       │
│       │                      │                       │                       │
│       ▼                      ▼                       ▼                       │
│   Snapshot               Production              Production                  │
│   Registry               Registry                Registry                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Stage Characteristics

### DEV Stage

| Aspect | Behavior |
|--------|----------|
| **Registry** | Snapshot registry only |
| **External Sources** | Can reference external Git repositories |
| **Artifact State** | Work-in-progress, unstable |
| **Promotion** | Source for all promotions |
| **Typical Use** | Feature development, experimentation |

### STAGING Stage

| Aspect | Behavior |
|--------|----------|
| **Registry** | Production registry only |
| **External Sources** | Not allowed (must use promoted artifacts) |
| **Artifact State** | Release candidates, validated |
| **Promotion** | Can promote to PROD |
| **Typical Use** | Integration testing, UAT |

### PROD Stage

| Aspect | Behavior |
|--------|----------|
| **Registry** | Production registry only |
| **External Sources** | Not allowed |
| **Artifact State** | Released, stable |
| **Promotion** | Final destination (or source for cross-tenant) |
| **Typical Use** | Production operations |

---

## Custom Stages

Tenant Admins can define additional Dev-Lifecycle-Stages beyond the defaults:

```yaml
apiVersion: hub.olympus.io/v1
kind: DevLifecycleStage
metadata:
  name: uat
  namespace: acme-bank
spec:
  display_name: "User Acceptance Testing"
  
  # Registry access
  accepts_snapshot_artifacts: false  # Must use production registry
  
  # Position in lifecycle (for UI ordering)
  ordinal: 15  # Between STAGING (10) and PROD (20)
  
  # Optional: promotion constraints
  promotion:
    allowed_sources:
      - DEV
      - STAGING
    allowed_targets:
      - PROD
```

### Common Custom Stages

| Stage | `accepts_snapshot_artifacts` | Typical Use |
|-------|------------------------------|-------------|
| **UAT** | `false` | User acceptance testing |
| **PERF** | `false` | Performance testing |
| **SANDBOX** | `true` | Isolated experimentation |
| **HOTFIX** | `true` | Emergency fixes (dev-like) |

---

## Stage Assignment

### At Workbench Creation

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-staging
  namespace: acme-bank
spec:
  display_name: "Dispute Operations - Staging"
  
  # Lifecycle stage assignment
  dev_lifecycle_stage: STAGING
  
  # ... other configuration
```

### Stage Immutability

| Rule | Rationale |
|------|-----------|
| **One stage per workbench** | Clear operational boundaries |
| **Stage is not fluid** | Prevents accidental production exposure |
| **Admin can change** | Exceptional cases with full awareness |
| **No in-place promotion** | Always promote to different workbench |

> **Warning:** Changing a workbench's stage can lead to inconsistencies (e.g., DEV workbench with PROD artifacts). Admins must understand consequences before changing.

---

## Registry Access Rules

| Workbench Stage | Snapshot Registry | Production Registry |
|-----------------|-------------------|---------------------|
| DEV | ✅ Pull | ❌ No access |
| STAGING | ❌ No access | ✅ Pull |
| PROD | ❌ No access | ✅ Pull |
| Custom (`accepts_snapshot: true`) | ✅ Pull | ❌ No access |
| Custom (`accepts_snapshot: false`) | ❌ No access | ✅ Pull |

---

## Multiple Workbenches per Stage

A subscription can have multiple workbenches at the same stage:

```
SUBSCRIPTION: acme-bank-sub-001
├── dispute-ops-dev-1         (DEV)    ← Developer A's workspace
├── dispute-ops-dev-2         (DEV)    ← Developer B's workspace
├── dispute-ops-staging       (STAGING)
├── dispute-ops-uat           (UAT)
└── dispute-ops-prod          (PROD)
```

### Use Cases

| Pattern | Purpose |
|---------|---------|
| **Developer workspaces** | Each developer has own DEV workbench |
| **Feature isolation** | Separate DEV workbenches per feature |
| **Regional PROD** | Multiple PROD workbenches for regions |

---

## Promotion and Stage Compatibility

Promotion requires the target workbench to be based on a **compatible Workbench Specification**:

### Compatibility Rules (Semantic Versioning)

| Source Version | Target Version | Compatible? |
|----------------|----------------|-------------|
| 1.2.3 | 1.2.3 | ✅ Same version |
| 1.2.3 | 1.2.0 | ✅ Same MAJOR.MINOR |
| 1.2.3 | 1.0.0 | ⚠️ Same MAJOR (may work) |
| 1.2.3 | 2.0.0 | ❌ Breaking change |

### Breaking Changes

Promotion is blocked if the target has:
- Different MAJOR version (breaking changes)
- Removed required roles or task types
- Incompatible Scenario definitions

---

## Related Documentation

- [Container Registry](./container-registry.md) — Snapshot and Production registries
- [Promotion Model](./promotion-model.md) — Promotion workflow and approval
- [Git Repository](./git-repository.md) — CRD storage


