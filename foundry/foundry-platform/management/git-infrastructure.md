# Git Infrastructure for a Foundry

Operational guide to Git repositories in the Foundry Platform — provisioning, configuration, access, and maintenance.

## Purpose

This document provides a consolidated view of all Git repositories involved in a Foundry, focused on infrastructure operations: provisioning sequences, access control, webhook configuration, validation pipelines, and naming conventions.

For conceptual repository definitions, see [../../ace/repositories.md](../../ace/repositories.md).
For logical Workbench architecture, see [workbench-architecture.md](workbench-architecture.md).

---

## Git Repository Inventory

### Definition Repositories (Platform-Managed)

Configuration repositories managed by the Foundry Platform for declarative infrastructure.

| Repository | Scope | Provisioned By | Provisioned When | Purpose |
|------------|-------|----------------|------------------|---------|
| `foundry-{id}/` | Foundry | Platform Admin | Foundry creation | Foundry metadata, Domain, Practices, Capable Agents |
| `workshop-{id}/` | Workshop | Foundry Admin | Workshop creation | Workshop + Workbench config, Domain, Practices, Ontology, Workspaces |

### Product Repositories (Workbench-Managed)

Product development repositories created and managed through Workbench interfaces.

| Repository | Scope | Provisioned By | Provisioned When | Purpose |
|------------|-------|----------------|------------------|---------|
| Intent | Workbench | Workbench Manager | Workbench setup | Product Intents, PSDs, PDRs |
| Design | Workbench | Workbench Manager | Workbench setup | Architecture, API models, infrastructure specs |
| Code (multiple) | Workbench | Workbench Manager | As needed | Source code per System/Component |
| Quality Automation | Workbench | Workbench Manager | Workbench setup | Test automation scripts |

---

## Repository Hierarchy

```
GitHub Organization (one per Workshop or Foundry)
│
├── foundry-zeta/                        # Foundry Definition Repository
│   ├── foundry.yaml                     #   Foundry metadata
│   ├── domain/                          #   Foundry-level domain knowledge
│   │   ├── universal/
│   │   └── {workspace-type}/
│   ├── practices/                       #   Foundry-level practices
│   │   ├── universal/
│   │   └── {workspace-type}/
│   └── capable-agents.yaml              #   Foundry-level agent config
│
├── workshop-payments/                   # Workshop Definition Repository
│   ├── workshop.yaml                    #   Workshop metadata
│   ├── domain/                          #   Workshop-level domain knowledge
│   ├── practices/                       #   Workshop-level practices
│   ├── workspaces/                      #   Base workspace configurations (all 6)
│   └── workbenches/
│       └── checkout/                    #   Workbench configuration
│           ├── workbench.yaml
│           ├── ontology/                #   Product structure, capabilities
│           ├── domain/                  #   Workbench-level domain knowledge
│           ├── practices/               #   Workbench-level practices
│           └── workspaces/              #   Workspace overrides (sparse)
│
└── (Product repos - per Workbench)
    ├── checkout-intent/                 # Intent Repository
    ├── checkout-design/                 # Design Repository
    ├── checkout-api/                    # Code Repository (1 of N)
    ├── checkout-ui/                     # Code Repository (2 of N)
    └── checkout-tests/                  # Quality Automation Repository
```

---

## Provisioning Sequence

### 1. Foundry Creation

```
Platform Admin initiates Foundry creation
        │
        ▼
┌─────────────────────────────────────────┐
│ Foundry Provisioning Service            │
│                                         │
│ 1. Create logical database              │
│ 2. Provision object storage prefix      │
│ 3. Create foundry-{id}/ Git repo        │
│ 4. Install GitHub App on target org     │
│ 5. Configure webhook → Workshop Sync    │
│ 6. Register in Olympus Cipher           │
│ 7. Send Foundry Admin invitation        │
└─────────────────────────────────────────┘
        │
        ▼
Foundry Definition Repo created with:
  - foundry.yaml (metadata)
  - domain/universal/ (empty)
  - practices/universal/ (empty)
  - capable-agents.yaml (defaults)
  - README.md
```

### 2. Workshop Creation

```
Foundry Admin creates Workshop
        │
        ▼
┌─────────────────────────────────────────┐
│ Workshop Provisioning Service           │
│                                         │
│ 1. Create workshop-{id}/ Git repo       │
│ 2. Configure webhook → Workshop Sync    │
│ 3. Initialize base workspace folders    │
│ 4. Register in Metadata Service         │
└─────────────────────────────────────────┘
        │
        ▼
Workshop Definition Repo created with:
  - workshop.yaml (metadata)
  - domain/universal/ (empty)
  - practices/universal/ (empty)
  - workspaces/ (all 6 base workspaces)
  - workbenches/ (empty)
  - README.md
```

### 3. Workbench Setup

```
Workshop Admin creates Workbench
        │
        ▼
┌─────────────────────────────────────────┐
│ Workbench Provisioning Service          │
│                                         │
│ 1. Add workbenches/{product-code}/ to   │
│    Workshop Definition Repo             │
│ 2. Create product repos in GitHub Org:  │
│    - {product}-intent                   │
│    - {product}-design                   │
│    - {product}-tests                    │
│ 3. Configure webhooks → Metadata Svc    │
│ 4. Provision Ontology Service           │
│ 5. Register in Metadata Service         │
│ 6. Connect to Olympus Weave (get code)  │
└─────────────────────────────────────────┘
        │
        ▼
Product repos created and tagged
Code repos created later as Systems are defined
```

---

## Access Model

### Repository Access by Persona

| Persona | Foundry Repo | Workshop Repo | Product Repos |
|---------|--------------|---------------|---------------|
| **Platform Admin** | Admin | Read | — |
| **Foundry Admin** | Write | Read | — |
| **Workshop Admin** | Read | Write | — |
| **Workbench Manager** | Read | Write (workbench scope) | Admin |
| **Workbench Member** | Read | Read | Write |
| **GitHub App** | Read | Read | Manage |

### Access Enforcement

| Level | Mechanism |
|-------|-----------|
| Foundry Repo | GitHub App permissions + branch protection |
| Workshop Repo | GitHub App permissions + CODEOWNERS + branch protection |
| Product Repos | GitHub teams synced from Workbench team |

### CODEOWNERS for Workshop Repo

```
# Workshop repo CODEOWNERS

# Workshop-level config
/workshop.yaml                    @workshop-admins
/domain/                          @workshop-admins
/practices/                       @workshop-admins
/workspaces/                      @workshop-admins

# Workbench-level config (per Workbench)
/workbenches/checkout/            @checkout-managers
/workbenches/payments-core/       @payments-core-managers
```

---

## Webhook Configuration

### Definition Repositories

| Repo Type | Webhook Target | Events | Purpose |
|-----------|---------------|--------|---------|
| Foundry Definition | Workshop Sync Service | `push`, `pull_request` | Sync Foundry config to Metadata Service |
| Workshop Definition | Workshop Sync Service | `push`, `pull_request` | Sync Workshop/Workbench config to Metadata Service |

### Product Repositories

| Repo Type | Webhook Target | Events | Purpose |
|-----------|---------------|--------|---------|
| Intent | Metadata Service | `push` | Track PI commits, trigger workflows |
| Design | Metadata Service | `push` | Track design commits |
| Code | Metadata Service | `push` | Track code commits, trigger CI |
| Quality Automation | Metadata Service | `push` | Track test automation changes |

### Webhook Payload Processing

```
GitHub Webhook
      │
      ▼
┌─────────────────────────────────────────┐
│ Workshop Sync Service (Definition repos)│
│                                         │
│ 1. Validate payload signature           │
│ 2. Parse changed files                  │
│ 3. Validate configuration (if PR)       │
│ 4. Update Metadata Service (if push)    │
│ 5. Trigger downstream notifications     │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ Metadata Service (Product repos)        │
│                                         │
│ 1. Validate payload signature           │
│ 2. Record commit metadata               │
│ 3. Update commit tracking tables        │
│ 4. Trigger CI/CD pipelines if needed    │
└─────────────────────────────────────────┘
```

---

## Branch Protection

### Definition Repositories (Foundry, Workshop)

| Setting | Value | Rationale |
|---------|-------|-----------|
| Require PR | Yes | All changes reviewed |
| Required reviewers | 1+ | Depends on governance policy |
| Required status checks | Workshop Validation Service | Config must be valid |
| Dismiss stale reviews | Yes | Re-review after changes |
| Require linear history | Yes (squash) | Clean history |
| Allow force push | No | Audit trail |
| Allow deletion | No | Protection |

### Product Repositories

| Setting | Default | Configurable |
|---------|---------|--------------|
| Require PR | Yes | Per Workbench policy |
| Required reviewers | 1 | Per Workbench policy |
| Required status checks | CI must pass | Per Workbench policy |
| Allow force push | No | Not recommended |

---

## Validation Pipeline

### Definition Repository Validation

```
PR Opened to Definition Repo
        │
        ▼
┌─────────────────────────────────────────┐
│ Workshop Validation Service             │
│                                         │
│ Schema Validation                       │
│ ├── foundry.yaml conforms to schema     │
│ ├── workshop.yaml conforms to schema    │
│ ├── workbench.yaml conforms to schema   │
│ └── workspace.yaml conforms to schema   │
│                                         │
│ Folder Structure Validation             │
│ ├── domain/ uses valid workspace types  │
│ ├── practices/ uses valid workspace types│
│ └── No unknown folders at scope level   │
│                                         │
│ Content Validation                      │
│ ├── No hardcoded secrets                │
│ ├── YAML files parse correctly          │
│ ├── Markdown files pass linting         │
│ └── Cross-references resolve            │
│                                         │
│ Semantic Validation                     │
│ ├── Referenced Workbenches exist        │
│ ├── Team members exist in identity      │
│ └── Integration configs are valid       │
└─────────────────────────────────────────┘
        │
        ▼
    Pass/Fail reported to GitHub
        │
        ▼ (on merge)
Workshop Sync Service updates Metadata Service
```

→ [services/workshop-validation.md](services/workshop-validation.md) for validation rules

---

## Tagging and Metadata

All repositories created through Foundry Platform are tagged with metadata for identification and filtering.

### Repository Tags (GitHub Topics)

| Tag | Format | Example | Purpose |
|-----|--------|---------|---------|
| `foundry-id` | `foundry-{id}` | `foundry-zeta` | Tenant identification |
| `workshop-id` | `workshop-{id}` | `workshop-payments` | Division identification |
| `workbench-id` | `wb-{id}` | `wb-checkout` | Product identification |
| `product-code` | `{code}` | `CHKOUT-001` | Olympus Weave linkage |
| `repo-type` | `foundry-def`, `workshop-def`, `intent`, `design`, `code`, `quality` | `intent` | UPIM classification |

### Custom Properties (GitHub Repository Properties)

```yaml
foundry:
  id: foundry-zeta
  name: "Zeta Corporation"
workshop:
  id: workshop-payments
  name: "Payments Platform"
workbench:
  id: wb-checkout
  name: "Checkout Service"
  productCode: CHKOUT-001
repoType: intent
```

---

## Naming Conventions

### Definition Repositories

| Repo Type | Pattern | Example |
|-----------|---------|---------|
| Foundry Definition | `foundry-{foundry-id}` | `foundry-zeta` |
| Workshop Definition | `workshop-{workshop-id}` | `workshop-payments` |

### Product Repositories

| Repo Type | Pattern | Example |
|-----------|---------|---------|
| Intent | `{product}-intent` | `checkout-intent` |
| Design | `{product}-design` | `checkout-design` |
| Code | `{product}-{component}` | `checkout-api`, `checkout-ui` |
| Quality Automation | `{product}-tests` | `checkout-tests` |

### Constraints

- Lowercase alphanumeric with hyphens
- Max 100 characters
- Must be unique within GitHub Org
- Product name derived from `workbench.yaml` metadata

---

## UPIM Repository Mapping

Mapping between Git repositories and UPIM conceptual repositories.

| Git Repository | UPIM Repository | Notes |
|----------------|-----------------|-------|
| `foundry-{id}/domain/` | Domain | Foundry-level |
| `foundry-{id}/practices/` | Practices | Foundry-level |
| `workshop-{id}/domain/` | Domain | Workshop-level |
| `workshop-{id}/practices/` | Practices | Workshop-level |
| `workshop-{id}/workbenches/{x}/domain/` | Domain | Workbench-level |
| `workshop-{id}/workbenches/{x}/practices/` | Practices | Workbench-level |
| `workshop-{id}/workbenches/{x}/ontology/` | Ontology | Workbench-level (also served by Ontology Service) |
| `{product}-intent` | Intent | Product Intents, PSDs |
| `{product}-design` | Design | Architecture, API specs |
| `{product}-{component}` | Code | Source code |
| `{product}-tests` | Quality | Test automation (test cases in TestRail) |

### Non-Git UPIM Repositories

| UPIM Repository | Storage | Notes |
|-----------------|---------|-------|
| Ontology | Native Service | Auto-provisioned per Workbench |
| Operations | Jira (JSM) | Label-filtered |
| Feedback | Jira | Label-filtered |
| Work | Jira | Label-filtered |
| Work Orders | Jira | Dedicated project per Workbench |
| Evolution | TBD | Deferred (not Phase 1) |
| Workforce | Metadata Service | Foundry-scoped |
| Stakeholders | Metadata Service | Workshop-scoped |

---

## Backup and Recovery

### Definition Repositories

| Aspect | Strategy |
|--------|----------|
| Primary | GitHub native redundancy |
| Secondary | Daily Git mirror to backup location |
| Recovery SLA | 1 hour |
| Point-in-time | Git history provides full history |

### Product Repositories

| Aspect | Strategy |
|--------|----------|
| Primary | GitHub native redundancy |
| Secondary | Customer responsibility (can enable GitHub backup) |
| Recovery SLA | Per GitHub SLA |

### Metadata Service Sync

If Metadata Service loses sync with Git:
1. Trigger full re-sync from Git repos
2. Workshop Sync Service rebuilds state
3. Validate against current Git HEAD

---

## Disaster Recovery

### Scenario: GitHub Org Unavailable

1. Failover to Git mirror (read-only mode)
2. Platform operates in degraded mode (no pushes)
3. Once GitHub restored, verify sync

### Scenario: Definition Repo Corrupted

1. Restore from most recent valid commit
2. Re-run Workshop Sync to update Metadata Service
3. Validate all downstream configurations

### Scenario: Product Repo Lost

1. Restore from GitHub backup or customer backup
2. Re-register webhooks
3. Re-sync commit tracking in Metadata Service

---

## Open Questions

- **Git LFS** — Strategy for large assets (design files, binaries)
- **Archival** — Workflow when Workbench is decommissioned
- **Cross-Workshop sharing** — Repos shared across Workshops
- **Mono-repo vs multi-repo** — Guidance for Code repositories
- **Forking** — Support for forked repos in Code repository

---

## Read Next

- [foundry-definition-repository.md](foundry-definition-repository.md) — Foundry repo structure
- [workshop-repository.md](workshop-repository.md) — Workshop repo structure
- [workbench-architecture.md](workbench-architecture.md) — Workbench logical architecture
- [services/workshop-validation.md](services/workshop-validation.md) — PR validation
- [services/workshop-sync.md](services/workshop-sync.md) — Webhook processing
- [../../ace/repositories.md](../../ace/repositories.md) — UPIM repository concepts
