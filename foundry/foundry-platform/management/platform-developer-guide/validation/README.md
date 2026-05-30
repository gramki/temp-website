# Validation Module

**Module scope:** Subsystem of Management — pre-publish gate for all Foundry-scope configuration.

## Purpose

The Validation module ensures that Foundry, Workshop, Workbench, Work Catalog, and knowledge configuration is well-formed, referentially consistent, and safe to propagate before it reaches the Metadata Service.

It answers: *Is this Foundry-scope configuration valid enough to merge and sync?*

It does **not** answer: *Does this product build pass tests?* — that belongs to **Release Tools** (product-scope CI).

## Scope

### In scope

| Category | Artifacts | Repositories |
|----------|-----------|--------------|
| Entity configuration | `foundry.yaml`, `workshop.yaml`, `workbench.yaml`, `workspace.yaml`, `team.yaml`, `integrations.yaml` | Foundry and Workshop definition repos |
| Work Catalog | OI Workflows (`workflow.yaml`), Scenarios (`*.yaml`) | All catalog repos (see path model below) |
| Knowledge | `domain/`, `practices/` structure and content | Foundry and Workshop definition repos |
| Platform defaults | OI Workflows and Scenarios at ship time | `work-catalogues/platform-defaults/` in Foundry codebase |

### Out of scope

| Boundary | Owned by |
|----------|----------|
| Product repos (intent, design, code, tests) | Release Tools CI |
| Build / test / release pipelines | Release Tools |
| Post-sync resolution | Work Catalog Management (Resolution Engine) |
| Agent recommendations | Work Catalog Management (Agent Recommender) |
| Config propagation after merge | Workshop Sync / Work Catalog Sync |
| Runtime work execution | Orchestrator, WO Runtime |

**Release Tools has no relationship with the Validation module.** Product CI runs independently; runtime modules consume resolved config from Metadata Service.

## Canonical Work Catalog path model

All catalog levels use the same structure under a `work-catalog/` root:

```
work-catalog/{track}/{oi-type}/workflow.yaml
work-catalog/{track}/{oi-type}/{workspace}/scenarios/*.yaml
```

| Level | Repository | Catalog path |
|-------|------------|--------------|
| Platform | Foundry codebase | `work-catalogues/platform-defaults/work-catalog/{track}/{oi-type}/...` |
| Foundry | `foundry-{id}/` (embedded) | `work-catalog/{track}/{oi-type}/...` |
| Workshop | `workshop-{id}/` | `work-catalog/{track}/{oi-type}/...` |
| Workbench | `workshop-{id}/` | `workbenches/{wb}/work-catalog/{track}/{oi-type}/...` |
| User | `user-work-catalog-{userId}/` | `work-catalog/{track}/{oi-type}/...` |

Legacy paths (`workbenches/{wb}/workspaces/{ws}/scenarios/`) are not supported.

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Validation Module                                  │
│                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐         │
│  │ ConfigValidator  │  │WorkCatalogValidator│ │KnowledgeValidator│         │
│  │                  │  │                  │  │                  │         │
│  │ foundry.yaml     │  │ OI Workflows     │  │ domain/          │         │
│  │ workshop.yaml    │  │ Scenarios        │  │ practices/       │         │
│  │ workbench.yaml   │  │ (delegates to    │  │ folder structure │         │
│  │ workspace.yaml   │  │  WCM rules API)  │  │ content rules    │         │
│  │ team, integrations│ │                  │  │                  │         │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘         │
│           └─────────────────────┴─────────────────────┘                     │
│                                 │                                           │
│                    Validation Orchestrator                                   │
│                    (PR / push / release triggers)                             │
└─────────────────────────────────┬───────────────────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │   Execution adapters       │
                    │   GitHub Checks / App      │
                    │   (Jenkins optional)       │
                    └───────────────────────────┘
```

### Domain validators

| Validator | Responsibility |
|-----------|----------------|
| **ConfigValidator** | Entity YAML schemas, folder structure, permissions, cross-references between workbenches/workspaces |
| **WorkCatalogValidator** | OI Workflow and Scenario validation via Work Catalog Management (`POST /api/v1/work-catalog/validate`) |
| **KnowledgeValidator** | Valid workspace types under `domain/` and `practices/`, content hygiene, no circular references |

→ [../work-catalog-management/validation-rules.md](../work-catalog-management/validation-rules.md) for OI Workflow and Scenario rule IDs

## Validation layers

All artifact types pass through four layers:

```
YAML Parsing → Schema Validation → Reference Validation → Semantic Validation
```

| Layer | Purpose | Fails fast |
|-------|---------|------------|
| YAML parsing | Syntax correctness | Yes |
| Schema | Structure conformance | Yes |
| Reference | Cross-references exist | No (collects all errors) |
| Semantic | Business logic, scope rules, permissions | No (collects all errors) |

Work Catalog validation is hierarchy-aware: the orchestrator loads the **parent effective catalog** so OI Workflows can reference Scenarios defined at higher levels.

## Execution points

Validation runs at two points with the same rules:

| Point | When | Purpose |
|-------|------|---------|
| **PR validation** | PR opened/updated on definition repos | Block invalid merges |
| **Sync validation** | Post-merge sync to Metadata Service | Safety net before registry write |

### Triggers by repository type

| Repository | Trigger | Merge gate |
|------------|---------|------------|
| Foundry definition (`foundry-{id}/`) | PR to main | Yes — Validation holds merge permission |
| Workshop definition (`workshop-{id}/`) | PR to main | Yes |
| User work catalog (`user-work-catalog-{userId}/`) | Push to main | No — direct push allowed; validate and report |
| Platform defaults | Foundry deployment/upgrade | Release gate |

## Configuration pipeline

```
Author opens PR (definition repo) or pushes (user repo)
        │
        ▼
┌─────────────────────────┐
│   Validation Module     │
└───────────┬─────────────┘
            │ pass
            ▼
       merge (definition repos only)
            │
            ▼
┌─────────────────────────┐
│   Sync Services         │  ← not Validation; propagates validated config
└───────────┬─────────────┘
            │ re-validate (safety net)
            ▼
┌─────────────────────────┐
│   Metadata Service      │
└───────────┬─────────────┘
            │ resolve (not validate)
            ▼
   Orchestrator / WO Runtime / Web App
```

## GitHub integration

Foundry operates as a **GitHub App**. The Validation module:

| Capability | Detail |
|------------|--------|
| Check name | `foundry-validation` |
| PR trigger paths | `work-catalog/**`, `workbenches/**`, `workspaces/**`, `domain/**`, `practices/**`, `*.yaml` |
| Merge control | Only Validation module can merge to main on definition repos |
| Status reporting | GitHub check annotations with file/line errors |

→ [../services/workshop-validation.md](../services/workshop-validation.md) for GitHub integration appendix

## Execution adapters

The Validation module owns **policy and orchestration**. Execution infrastructure is pluggable:

| Adapter | Role |
|---------|------|
| GitHub Checks / App | Primary — receive PR events, post `foundry-validation` status, perform merge |
| Jenkins (or similar) | Optional — run heavy or async validation jobs; results reported back to Validation orchestrator |

These are implementation details, not separate product modules. Do not describe Validation as "CI."

## Relationship to sibling modules

| Module | Relationship |
|--------|--------------|
| **Work Catalog Management** | Supplies schemas, validation rules, and validation API; Validation module orchestrates |
| **Workshop Sync / Work Catalog Sync** | Downstream — propagates validated config to Metadata Service |
| **Metadata Service** | Stores synced artifacts; queried at runtime |
| **Orchestrator / WO Runtime** | Consume resolved config — no Validation calls |
| **Release Tools** | Independent — product-repo CI only |

## Key design decisions

- **Validation is synchronous for PR gates.** PR validation must block on results — async would create race conditions with merge.
- **Single check name.** All Foundry-scope validation reports as `foundry-validation`.
- **User catalogs are experimentation-first.** Direct push to main; validation runs on push but does not require PR approval.
- **Sync re-validates.** Same rules applied during sync as a safety net, even after PR validation passed.

## Module documents

| Document | Content |
|----------|---------|
| [requirements.md](requirements.md) | Implementation requirements, APIs, triggers, permissions |
| [../services/workshop-validation.md](../services/workshop-validation.md) | GitHub integration appendix |
| [../work-catalog-management/validation-rules.md](../work-catalog-management/validation-rules.md) | OI Workflow and Scenario rule specification |

## Read Next

- [requirements.md](requirements.md) — Implementation requirements
- [../work-catalog-management/README.md](../work-catalog-management/README.md) — Schemas, resolution, sync
- [../git-infrastructure.md](../git-infrastructure.md) — Repository provisioning and branch protection
- [../../release-tools/README.md](../../release-tools/README.md) — Product-scope CI (separate boundary)
