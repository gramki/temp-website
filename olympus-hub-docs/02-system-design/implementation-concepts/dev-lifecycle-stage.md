# Dev-Lifecycle-Stage

> **Category:** Platform Foundation

---

## Overview

**Dev-Lifecycle-Stage** is a tag assigned to each Workbench indicating its position in the software development lifecycle (DEV, STAGING, PROD). This tag determines which artifact registries the Workbench can access, what promotion paths are available, and how the Workbench participates in the development-to-production flow.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Workbench** as the operational realization of a Domain, but doesn't address the software development lifecycle or environment management. Dev-Lifecycle-Stage is an implementation concept for development workflow.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Workbench | Workbench + Dev-Lifecycle-Stage | Stage categorizes Workbench purpose |
| (not covered) | Dev-Lifecycle-Stage | Manages development lifecycle |

### Gap This Fills

The ontology doesn't address development lifecycle. Dev-Lifecycle-Stage specifies:
1. **Environment separation**: DEV for development, PROD for production
2. **Registry access**: Which artifacts can be used
3. **Promotion eligibility**: Where artifacts can be promoted
4. **Compliance**: Regulated industry requirements

---

## Definition

**Dev-Lifecycle-Stage** is a tag on a Workbench that:
- Indicates the Workbench's purpose (development, staging, production)
- Determines artifact registry access (snapshot vs production)
- Controls promotion eligibility
- Cannot be changed in-place (workbenches don't migrate between stages)

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-level; one stage per Workbench |
| **Lifecycle** | Set at Workbench creation; immutable in practice |
| **Ownership** | Tenant Admin assigns during Workbench setup |
| **Multiplicity** | Each Workbench has exactly one stage |

---

## Rationale

### Why This Design?

Explicit stage tagging enables:
1. **Clear intent**: Everyone knows the Workbench's purpose
2. **Automatic constraints**: Registry access enforced by stage
3. **Compliance**: Regulated industries require environment separation
4. **Simplified promotion**: Promotion rules based on stages

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Implicit by naming** | Error-prone; not enforced |
| **Mutable stages** | Inconsistent state; compliance issues |
| **No stages** | No clear separation; compliance failure |

---

## Structure

### Default Stages

| Stage | Registry Access | Purpose |
|-------|-----------------|---------|
| **DEV** | Snapshot only | Active development, feature work |
| **STAGING** | Production | Pre-production testing, validation |
| **PROD** | Production only | Production operations |

### Stage and Registry Relationship

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEV-LIFECYCLE-STAGE AND REGISTRIES                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                       PROD SUBSCRIPTION                   │
│   ─────────────────                      ─────────────────                   │
│                                                                              │
│   ┌─────────────────────┐               ┌─────────────────────┐             │
│   │  DEV Workbench      │               │  PROD Workbench     │             │
│   │  ─────────────      │               │  ──────────────     │             │
│   │  Stage: DEV         │               │  Stage: PROD        │             │
│   │                     │               │                     │             │
│   │  Registry Access:   │               │  Registry Access:   │             │
│   │  ✓ Snapshot         │               │  ✓ Production       │             │
│   │  ✗ Production       │               │  ✗ Snapshot         │             │
│   └─────────────────────┘               └─────────────────────┘             │
│                                                                              │
│   ┌─────────────────────┐                                                   │
│   │  STAGING Workbench  │                                                   │
│   │  ────────────────   │                                                   │
│   │  Stage: STAGING     │                                                   │
│   │                     │                                                   │
│   │  Registry Access:   │                                                   │
│   │  ✓ Production       │  ← Same artifacts as PROD                        │
│   │  ✗ Snapshot         │                                                   │
│   └─────────────────────┘                                                   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Stage Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-dev
  namespace: acme-bank
spec:
  display_name: "Dispute Operations (Development)"
  
  # Dev-Lifecycle-Stage
  dev_lifecycle_stage: DEV
  
  # Registry access derived from stage
  # DEV → snapshot registry
  # STAGING/PROD → production registry
```

---

## Behavior

### Stage Constraints

| Stage | Can Pull From | Can Push To | Promotion Target |
|-------|---------------|-------------|------------------|
| **DEV** | Snapshot | Snapshot | STAGING, PROD |
| **STAGING** | Production | (validation only) | PROD |
| **PROD** | Production | N/A | (terminal) |

### Custom Stages

Tenant Admins can define custom stages (e.g., UAT, PERF):

```yaml
custom_stages:
  - name: UAT
    accepts_snapshot: false  # Must use production artifacts
  - name: PERF
    accepts_snapshot: true   # Can use snapshot for load testing
```

### Stage Immutability

```
Why stages don't change:

1. Changing DEV → PROD would:
   - Allow snapshot artifacts in production
   - Bypass approval workflows
   - Create audit trail gaps

2. Instead, promote artifacts:
   - DEV Workbench → artifacts → PROD Workbench
   - Clear approval and audit trail
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Workbench | ← tags | Stage is property of Workbench |
| Artifact Registry | → determines access | Stage controls registry access |
| Promotion | → enables | Stage determines promotion eligibility |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Single stage** | Each Workbench has exactly one stage |
| **Immutable** | Stage cannot be changed after creation |
| **Registry enforcement** | Stage determines registry access automatically |
| **No downgrade** | PROD workbench can't become DEV |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Clear intent** | Workbench purpose is explicit |
| ✅ **Automatic constraints** | Registry access enforced |
| ✅ **Compliance** | Environment separation for auditors |
| ✅ **Simple model** | Easy to understand and explain |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Immutability** | Create new workbench if stage needs change |
| ⚠️ **Multiple workbenches** | Sensible default: few per subscription |

---

## Examples

### Example 1: Two-Subscription Model

```
ACME Bank Setup:

acme-dev (DEV Subscription)
├── dispute-ops-dev     (DEV)      → Snapshot registry
├── dispute-ops-staging (STAGING)  → Production registry
└── recon-dev           (DEV)      → Snapshot registry

acme-prod (PROD Subscription)
├── dispute-ops-prod    (PROD)     → Production registry
└── recon-prod          (PROD)     → Production registry
```

### Example 2: Development Flow

```
Developer Workflow:

1. Work in dispute-ops-dev (DEV)
   - Pull from snapshot registry
   - Push builds to snapshot registry
   - Test with snapshot artifacts

2. Promote to dispute-ops-staging (STAGING)
   - Artifacts copied to production registry
   - STAGING pulls from production registry
   - Validates production-ready artifacts

3. Promote to dispute-ops-prod (PROD)
   - Same production artifacts
   - Running in production workbench
```

---

## Implementation Notes

### For Developers

- Know your Workbench's stage
- DEV workbenches use snapshot artifacts
- Can't reference snapshot artifacts in STAGING/PROD
- Promotion is required to move artifacts

### For Operators

- Assign appropriate stage at Workbench creation
- Don't change stage — create new Workbench if needed
- Configure custom stages if default three aren't sufficient

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Subscription](./subscription.md) | Workbenches exist within Subscriptions |
| [Promotion](./promotion.md) | Moves artifacts across stages |
| [Artifact Registry](./artifact-registry.md) | Stage controls registry access |

---

## References

- [Dev-Lifecycle-Stages](../../04-subsystems/artifact-registry/dev-lifecycle-stages.md)
- [Hub Development Flow Primer](../../10-guides/hub-development-flow/README.md)
- [Two-Subscription Model](../../10-guides/hub-development-flow/02-two-subscription-model.md)

