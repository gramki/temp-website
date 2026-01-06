# Git Repository

## Overview

Every Hub subscription is backed by a **platform-managed Git repository** that stores all CRDs and configuration resources. This repository serves as the single source of truth for the subscription's declarative state.

---

## Repository Scope

| Scope | Repository |
|-------|------------|
| **Per Subscription** | One Git repository per subscription |
| **Per Workbench** | 🔴 Future (may be added if needed) |

---

## Design Rationale: Main Branch Only

Hub uses a **main-branch-only** model. This is a deliberate simplification for small teams in regulated environments:

| Benefit | Description |
|---------|-------------|
| **Audit Simplicity** | Single linear history, easy to trace changes |
| **Compliance Clarity** | No merge conflicts, clear change attribution |
| **Reduced Complexity** | No branch management overhead for small teams |
| **Promotion Consistency** | What's in main is what gets promoted |

### Concurrent Development Pattern

For scenarios requiring concurrent development, use **separate DEV workbenches**:

```
DEV SUBSCRIPTION
├── dispute-ops-dev          ← Primary development
├── dispute-ops-dev-feature  ← Feature isolation (when needed)
└── dispute-ops-staging      ← Pre-prod validation
```

> **Note:** For small teams (Hub's target audience), a single DEV workbench is typically sufficient. Feature workbenches are created only when isolation is genuinely needed.

---

## Repository Layout

Hub enforces a standard folder structure:

```
subscription-repo/
├── README.md                           # Auto-generated subscription overview
├── subscription.yaml                   # Subscription-level configuration
│
├── _shared/                            # Subscription-scoped resources
│   ├── machine-definitions/
│   │   ├── external-banking-core.yaml
│   │   └── payment-gateway.yaml
│   ├── tool-definitions/
│   │   ├── email-sender.yaml
│   │   └── sms-sender.yaml
│   ├── data-stores/
│   │   ├── ganymede-dispute-db.yaml
│   │   └── callisto-cache.yaml
│   └── knowledge-banks/
│       └── dispute-regulations.yaml
│
├── workbenches/
│   ├── dispute-ops-dev/
│   │   ├── workbench.yaml              # Workbench specification
│   │   ├── environments/
│   │   │   └── default.yaml
│   │   ├── scenarios/
│   │   │   ├── standard-dispute/
│   │   │   │   ├── normative.yaml
│   │   │   │   ├── automation.yaml
│   │   │   │   ├── deployment.yaml
│   │   │   │   ├── triggers/
│   │   │   │   │   └── dispute-submitted.yaml
│   │   │   │   ├── notifications/
│   │   │   │   │   └── templates.yaml
│   │   │   │   └── migrations/
│   │   │   │       ├── v1.0.0-initial.yaml
│   │   │   │       └── v1.1.0-add-category.yaml
│   │   │   └── fraud-detection/
│   │   │       └── ...
│   │   ├── applications/
│   │   │   └── dispute-handler/
│   │   │       └── application.yaml
│   │   ├── task-queues/
│   │   │   └── tier-1-queue.yaml
│   │   ├── machines/                   # Machine instances for this workbench
│   │   │   └── banking-core.yaml
│   │   └── tools/                      # Tool instances for this workbench
│   │       └── email-tool.yaml
│   │
│   ├── dispute-ops-staging/
│   │   └── ... (same structure)
│   │
│   └── dispute-ops-prod/
│       └── ... (same structure)
│
└── promotion-paths/
    ├── dev-to-staging.yaml
    └── staging-to-prod.yaml
```

---

## Key Directories

### `_shared/`

Subscription-scoped resources shared across workbenches:

| Directory | Contents |
|-----------|----------|
| `machine-definitions/` | Abstract machine definitions |
| `tool-definitions/` | Abstract tool definitions |
| `data-stores/` | Data store specifications |
| `knowledge-banks/` | Knowledge bank configurations |

> **Note:** These are definitions/specifications. Concrete instances are in each workbench's folder.

### `workbenches/<name>/`

Per-workbench resources:

| Directory | Contents |
|-----------|----------|
| `workbench.yaml` | Workbench specification and metadata |
| `environments/` | Hub Environment configurations |
| `scenarios/` | All scenarios in this workbench |
| `applications/` | Hub Application specifications |
| `task-queues/` | Task queue configurations |
| `machines/` | Machine instance bindings |
| `tools/` | Tool instance bindings |

### `workbenches/<name>/scenarios/<scenario>/`

Per-scenario resources:

| File/Directory | Contents |
|----------------|----------|
| `normative.yaml` | Scenario Normative Specification |
| `automation.yaml` | Scenario Automation Specification |
| `deployment.yaml` | Scenario Deployment Specification |
| `triggers/` | Signal triggers for this scenario |
| `notifications/` | Notification templates |
| `migrations/` | Data store migration CRDs |

---

## Git Provider

| Aspect | Details |
|--------|---------|
| **Provider** | Platform-managed Git (internal) |
| **Protocol** | HTTPS with service account authentication |
| **Access** | Via Hub APIs and Developer interfaces |

### Additional Origins (Optional)

Tenants can configure push to additional Git remotes:

```yaml
apiVersion: hub.olympus.io/v1
kind: SubscriptionGitConfig
metadata:
  name: git-config
  namespace: acme-bank
spec:
  # Primary (platform-managed)
  primary:
    enabled: true  # Always true
  
  # Additional remotes for tenant visibility
  additional_origins:
    - name: github-mirror
      url: https://github.com/acme-bank/hub-config.git
      credentials:
        secret_ref: github-push-creds
      push_on:
        - promotion_complete
        - manual_sync
```

---

## Branching Model

Hub uses a **simplified single-branch model** optimized for small teams with compliance requirements:

| Aspect | State | Rationale |
|--------|-------|-----------|
| **Branches** | Main only | Simplifies audit trail |
| **Environment Branches** | Not needed | Workbenches represent environments |
| **Feature Branches** | Via workbenches | Isolation when genuinely required |

### Why Not Git Branches?

| Traditional Approach | Hub Approach |
|---------------------|--------------|
| Feature branches in Git | Separate DEV workbenches |
| Merge conflicts to resolve | No conflicts (isolated workbenches) |
| Branch policies to configure | Promotion policies instead |
| Complex history | Linear, auditable history |

For small teams in regulated environments, this model provides **compliance-friendly simplicity** without sacrificing capability.

---

## Sync Mechanism

### Current: Manual Sync

Git is **storage only**. Sync to target workbenches is triggered manually:

```
Developer/Admin                Git Repository              Workbench
       │                            │                          │
       │  Commit CRD changes        │                          │
       ├───────────────────────────▶│                          │
       │                            │                          │
       │  Trigger Sync              │                          │
       ├────────────────────────────┼─────────────────────────▶│
       │                            │       Apply CRDs         │
       │                            │                          │
       │                            │    Reconcile Resources   │
       │                            │                          │
```

### Sync Triggers

| Trigger | Initiator | Use Case |
|---------|-----------|----------|
| Manual via UI | Developer/Admin | On-demand deployment |
| Manual via API | Developer/Admin | Scripted deployment |
| Promotion Complete | System | After successful promotion |

### Sync Delegation

Admins can delegate sync trigger permissions to Developers.

#### Default Permissions (Out-of-the-Box)

| Workbench Stage | Developer Sync Permission |
|-----------------|--------------------------|
| **DEV** | ✅ Developers can sync their assigned DEV workbenches |
| **STAGING** | ❌ Admin approval required |
| **PROD** | ❌ Admin approval required |

> **Rationale:** Developers need agility in DEV; non-DEV requires oversight.

#### Custom Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchSyncPermission
metadata:
  name: dev-sync-permission
  namespace: acme-bank
spec:
  workbench: dispute-ops-dev
  
  # Who can trigger sync
  allowed_users:
    - developer@acme.com
  allowed_roles:
    - senior-developer
  
  # Constraints
  constraints:
    require_approval: false
    allowed_hours: "09:00-18:00"  # Optional: business hours only
```

---

## Version Control

### Commit Practices

| Practice | Enforcement |
|----------|-------------|
| Meaningful messages | Encouraged (template provided) |
| Author attribution | Automatic (from Hub user) |
| Atomic commits | Per-resource or per-promotion |

### Commit Message Template

```
[<workbench>/<scenario>] <action>: <description>

Examples:
[dispute-ops-dev/standard-dispute] feat: add fraud detection trigger
[dispute-ops-staging] promote: v1.2.3 from dev
[_shared/machine-definitions] add: payment-gateway definition
```

### Version History

- Full Git history preserved
- Rollback uses Git history (revert to previous commit)
- Audit trail via Git log

---

## Access Control

| Actor | Permissions |
|-------|-------------|
| **Developer** | Read all; Write to assigned workbenches |
| **Admin** | Full access |
| **CI System** | Write (for build artifacts) |
| **Promotion System** | Write (for promotion operations) |

### Repository-Level Permissions

```yaml
apiVersion: hub.olympus.io/v1
kind: GitRepositoryAccess
metadata:
  name: repo-access
  namespace: acme-bank
spec:
  rules:
    - path: "workbenches/dispute-ops-dev/**"
      users:
        - developer@acme.com
      roles:
        - dispute-developer
      permissions: [read, write]
    
    - path: "_shared/**"
      roles:
        - tenant-admin
      permissions: [read, write]
    
    - path: "**"
      roles:
        - tenant-admin
      permissions: [read, write]
```

---

## No External Resources

> **Critical Constraint:** All subscription resources must be defined in the Git repository and/or Container registry. No external resource definitions are permitted.

| Allowed | Not Allowed |
|---------|-------------|
| CRDs in Git repo | Direct Kubernetes manifests |
| Containers in Hub registry | External container references (prod) |
| Hub-defined resources | Helm charts, Kustomize overlays |

### Exception: DEV Workbenches

DEV workbenches can reference external source repositories for Hub Application development. Built artifacts must still be stored in the subscription's registry.

---

## Related Documentation

- [Container Registry](./container-registry.md) — OCI artifact storage
- [Promotion Model](./promotion-model.md) — Artifact promotion
- [Developer Operators](../operators/developer-operators.md) — CRD management


