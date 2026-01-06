# Artifact Registry

> **Category:** DevOps and Lifecycle

---

## Overview

**Artifact Registry** is the Hub subsystem for storing and managing OCI containers and CRDs. Each Subscription has two registries — snapshot (for development) and production (for promoted artifacts). The registry integrates with the promotion system to control artifact movement across lifecycle stages.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't address artifact storage or deployment. Artifact Registry is an implementation concept for managing deployable assets.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Automation | Container image | Packaged automation code |
| (not covered) | Artifact Registry | Storage and versioning |

### Gap This Fills

The ontology focuses on runtime concepts. Artifact Registry addresses:
1. **Storage**: Where are deployable artifacts kept?
2. **Versioning**: How are versions managed?
3. **Isolation**: How are DEV and PROD separated?
4. **Promotion**: How do artifacts move to production?

---

## Definition

**Artifact Registry** is a storage subsystem that:
- Stores OCI container images for Hub Applications
- Maintains snapshot and production repositories
- Integrates with semantic versioning
- Supports promotion-based artifact movement

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Subscription-level; two registries per subscription |
| **Lifecycle** | Provisioned with subscription; managed by platform |
| **Ownership** | Platform owns; developers publish; admins promote |
| **Multiplicity** | Two per subscription (snapshot + production) |

---

## Rationale

### Why This Design?

Dual registry model enables:
1. **Isolation**: PROD never pulls from DEV registry
2. **Promotion control**: Explicit approval to move artifacts
3. **Audit**: Clear record of what's in production
4. **Security**: Separate credentials per registry

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Single registry with tags** | Weaker isolation |
| **External registries only** | No Hub integration |
| **No registry (direct deploy)** | No versioning; no rollback |

---

## Structure

### Registry Architecture

```
Subscription: acme-dev
├── Snapshot Registry
│   └── registry.hub.olympus.io/acme-bank/acme-dev/snapshot/
│       ├── dispute-handler:1.0.0-dev.1
│       ├── dispute-handler:1.0.0-dev.2
│       └── notification-sender:0.5.0-dev.1
│
└── Production Registry
    └── registry.hub.olympus.io/acme-bank/acme-dev/production/
        ├── dispute-handler:1.0.0
        └── notification-sender:0.5.0

Subscription: acme-prod
└── Production Registry
    └── registry.hub.olympus.io/acme-bank/acme-prod/production/
        ├── dispute-handler:1.0.0
        └── notification-sender:0.5.0
```

### Registry Types

| Type | Purpose | Access From |
|------|---------|-------------|
| **Snapshot** | Development builds | DEV workbenches |
| **Production** | Promoted artifacts | STAGING, PROD workbenches |

### Artifact Versioning

```
Version format: MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]

Examples:
├── 1.0.0-dev.1      # Development build
├── 1.0.0-rc.1       # Release candidate
├── 1.0.0            # Production release
└── 1.0.0+sha.abc123 # With build metadata
```

---

## Behavior

### How It Works

**Publishing to Snapshot:**
```
1. Developer builds container
2. Runtime CI validates and tests
3. Container pushed to snapshot registry
4. Dev workbench can pull and deploy
```

**Promotion to Production:**
```
1. Developer requests promotion
2. Admin reviews and approves
3. Promotion system:
   ├── Copies container from snapshot to production
   ├── Strips prerelease suffix (if present)
   └── Records promotion in audit log
4. STAGING/PROD workbenches can pull
```

**Cross-Subscription Promotion:**
```
1. Promotion approved
2. Container physically copied to target subscription
   └── From: acme-dev/production
   └── To: acme-prod/production
3. Complete audit trail maintained
```

### Stage and Registry Access

| Dev-Lifecycle-Stage | Can Pull From |
|--------------------|---------------|
| DEV | Snapshot only |
| STAGING | Production only |
| PROD | Production only |

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Runtime CI | ← receives | CI pushes built containers |
| Promotion | → reads/writes | Promotion copies artifacts |
| Automation Runtime | ← pulls | Runtime pulls containers |
| Olympus Weave | ↔ backed by | Underlying infrastructure |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Subscription scoped** | Registry belongs to subscription |
| **Stage determines access** | DEV can't pull from production |
| **Immutable versions** | Published version cannot change |
| **Physical copy on promotion** | Not references |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Isolation** | DEV and PROD separated |
| ✅ **Audit** | Clear promotion history |
| ✅ **Rollback** | Previous versions available |
| ✅ **Security** | Separate credentials |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Storage duplication** | Cleanup policies; efficient layers |
| ⚠️ **Copy time** | Lean containers |

---

## Examples

### Example 1: Publishing Container

```bash
# Build and push to snapshot
docker build -t registry.hub.olympus.io/acme-bank/acme-dev/snapshot/dispute-handler:1.1.0-dev.1 .
docker push registry.hub.olympus.io/acme-bank/acme-dev/snapshot/dispute-handler:1.1.0-dev.1
```

### Example 2: Container After Promotion

```
Before promotion:
└── acme-dev/snapshot/dispute-handler:1.1.0-dev.5

After promotion to acme-dev production:
└── acme-dev/production/dispute-handler:1.1.0

After promotion to acme-prod:
└── acme-prod/production/dispute-handler:1.1.0
```

---

## Implementation Notes

### For Developers

- Use semantic versioning consistently
- Keep containers lean for faster promotion
- Test in DEV before requesting promotion
- Include meaningful tags

### For Operators

- Monitor registry storage usage
- Configure retention policies
- Review promotion audit logs
- Manage credential rotation

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Promotion](./promotion.md) | Promotion moves artifacts |
| [Dev-Lifecycle-Stage](./dev-lifecycle-stage.md) | Stage determines registry access |
| [CI Subsystem](./ci-subsystem.md) | CI publishes to registry |

---

## References

- [Artifact Registry Subsystem](../04-subsystems/artifact-registry/README.md)
- [Container Registry](../04-subsystems/artifact-registry/container-registry.md)

