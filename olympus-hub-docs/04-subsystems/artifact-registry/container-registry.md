# Container Registry

## Overview

Each Hub subscription is provisioned with two OCI-compliant container registries for storing Hub Application artifacts.

---

## Registry Types

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SUBSCRIPTION REGISTRIES                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌───────────────────────────────┐   ┌───────────────────────────────┐     │
│   │      SNAPSHOT REGISTRY        │   │     PRODUCTION REGISTRY       │     │
│   ├───────────────────────────────┤   ├───────────────────────────────┤     │
│   │                               │   │                               │     │
│   │  • Development builds         │   │  • Released artifacts         │     │
│   │  • Feature work               │   │  • Approved for deployment    │     │
│   │  • CI/CD intermediates        │   │  • Versioned releases         │     │
│   │                               │   │                               │     │
│   │  Used by:                     │   │  Used by:                     │     │
│   │  • DEV workbenches            │   │  • STAGING workbenches        │     │
│   │                               │   │  • PROD workbenches           │     │
│   │                               │   │  • Custom non-dev stages      │     │
│   │                               │   │                               │     │
│   └───────────────────────────────┘   └───────────────────────────────┘     │
│                    │                               ▲                         │
│                    │         Promotion             │                         │
│                    └───────────────────────────────┘                         │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Snapshot Registry

| Aspect | Details |
|--------|---------|
| **Purpose** | Store development and in-progress builds |
| **Access** | DEV-stage workbenches only |
| **Retention** | Configurable; typically shorter retention |
| **Versioning** | Semantic version + git-sha |

### Production Registry

| Aspect | Details |
|--------|---------|
| **Purpose** | Store released, approved artifacts |
| **Access** | Non-DEV workbenches (STAGING, PROD, custom) |
| **Retention** | Long-term; version history preserved |
| **Versioning** | Semantic version (git-sha optional) |

---

## Artifact Promotion

Artifacts move from Snapshot to Production registry as part of Scenario promotion:

```
Developer                    Snapshot         Production
    │                        Registry          Registry
    │                            │                 │
    │  build & push              │                 │
    ├───────────────────────────▶│                 │
    │                            │                 │
    │  promote scenario          │                 │
    ├────────────────────────────┼────────────────▶│
    │  (triggers artifact copy)  │     copy        │
    │                            │────────────────▶│
    │                            │                 │
```

### Promotion Trigger

- **Manual**: Developer requests Scenario promotion
- **Coupled**: Artifact promotion is always part of Scenario promotion
- **Atomic**: All artifacts for a Scenario promoted together

---

## Image Naming Convention

```
<registry-host>/<subscription-id>/<workbench-id>/<application-id>:<tag>

Examples:
  registry.hub.acme.com/sub-001/dispute-ops/dispute-handler:1.2.3
  registry.hub.acme.com/sub-001/dispute-ops/dispute-handler:1.2.3-beta.1+abc123
```

### Tag Format

| Tag Type | Format | Example | Use |
|----------|--------|---------|-----|
| Release | `MAJOR.MINOR.PATCH` | `1.2.3` | Production releases |
| Pre-release | `MAJOR.MINOR.PATCH-LABEL` | `1.2.3-beta.1` | Staging/testing |
| Build | `MAJOR.MINOR.PATCH+SHA` | `1.2.3+abc123` | CI builds |
| Combined | `MAJOR.MINOR.PATCH-LABEL+SHA` | `1.2.3-rc.1+abc123` | Pre-release CI |

---

## Cross-Subscription Promotion

When promoting to a different subscription, containers are **physically copied**:

```
SOURCE SUBSCRIPTION                    TARGET SUBSCRIPTION
┌─────────────────────┐               ┌─────────────────────┐
│  Production         │    Copy       │  Production         │
│  Registry           │──────────────▶│  Registry           │
│                     │               │                     │
│  image:1.2.3        │               │  image:1.2.3        │
└─────────────────────┘               └─────────────────────┘
```

### Why Physical Copy?

| Reason | Explanation |
|--------|-------------|
| **Isolation** | Target subscription owns its artifacts |
| **Independence** | Source changes don't affect target |
| **Security** | Cross-tenant boundaries respected |
| **Auditability** | Clear provenance tracking |

---

## External Source Repositories

Developers can reference source code from external Git repositories:

```yaml
# In Hub Application Specification (DEV workbench only)
spec:
  source:
    type: external_git
    repository: https://github.com/acme/dispute-handler.git
    branch: main
    path: /src
    
  build:
    dockerfile: Dockerfile
    context: .
```

| Constraint | Details |
|------------|---------|
| **DEV Only** | External source references only in DEV workbenches |
| **Build Required** | External source must be built to container |
| **Promotion** | Built container promoted, not source reference |

---

## Registry Implementation

Hub uses [Olympus Weave](https://weave.olympus.tech/getting-started/overview/) for registry infrastructure:

| Provider | Support |
|----------|---------|
| Amazon ECR | ✅ Supported |
| JFrog Artifactory | ✅ Supported |
| Others | Via Weave abstraction |

> **Note:** Hub abstracts registry providers. Applications reference Hub-level image paths, not provider-specific URLs.

---

## Access Control

| Actor | Snapshot | Production |
|-------|----------|------------|
| Developer | Push, Pull | Pull only |
| CI System | Push, Pull | Push (via promotion) |
| Workbench (DEV) | Pull | — |
| Workbench (non-DEV) | — | Pull |
| Admin | Full | Full |

---

## Retention Policies

| Registry | Default Retention | Configurable |
|----------|-------------------|--------------|
| Snapshot | 30 days (untagged), 90 days (tagged) | Yes |
| Production | Indefinite | Yes |

### Cleanup Rules

- **Snapshot**: Untagged images cleaned after retention period
- **Production**: No automatic cleanup; admin-initiated only
- **Promoted**: Source snapshot image retained until explicit cleanup

---

## Related Documentation

- [Dev-Lifecycle-Stages](./dev-lifecycle-stages.md) — Workbench stage tagging
- [Promotion Model](./promotion-model.md) — Promotion workflow
- [CI Subsystem](../ci-subsystem/README.md) — Build infrastructure


