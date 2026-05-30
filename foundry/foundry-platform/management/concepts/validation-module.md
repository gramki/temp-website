# Validation Module

The Validation Module is the pre-publish gate for all Foundry-scope configuration — ensuring that entity configuration, Work Catalog definitions, and knowledge content are well-formed, referentially consistent, and safe to propagate before reaching the Metadata Service.

## What it is

The Validation Module answers one question: *Is this Foundry-scope configuration valid enough to merge and sync?*

It does **not** answer: *Does this product build pass tests?* — that belongs to Release Tools (product-scope CI).

The module validates three categories of artifacts:

| Category | Artifacts | Validation |
|----------|-----------|------------|
| **Entity Configuration** | `foundry.yaml`, `workshop.yaml`, `workbench.yaml`, `workspace.yaml`, `team.yaml`, `integrations.yaml` | Schema conformance, cross-references |
| **Work Catalog** | OI Workflows (`workflow.yaml`), Scenarios (`*.yaml`) | Schema, OI→Scenario linkage, skill references |
| **Knowledge** | `domain/`, `practices/` structure and content | Folder structure, content rules, no circular refs |

All artifacts pass through four validation layers:

```
YAML Parsing → Schema Validation → Reference Validation → Semantic Validation
```

Validation runs at two points:

| Point | When | Purpose |
|-------|------|---------|
| **PR validation** | PR opened/updated on definition repos | Block invalid merges |
| **Sync validation** | Post-merge sync to Metadata Service | Safety net before registry write |

For definition repositories (Foundry, Workshop), validation holds merge permission — invalid config cannot reach main. For user work catalogs, direct push is allowed; validation runs on push but reports rather than blocks, enabling experimentation.

The module operates as a GitHub App, posting a single `foundry-validation` check on PRs with file/line annotations for errors.

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Validation Orchestrator** | Coordinates validators, manages PR/push triggers |
| **ConfigValidator** | Entity YAML schemas, folder structure, permissions |
| **WorkCatalogValidator** | OI Workflow and Scenario validation (delegates to WCM) |
| **KnowledgeValidator** | Domain and practices content validation |
| **GitHub App** | Receives PR events, posts check status, controls merge |

Configuration pipeline:

```
Author opens PR (or pushes to user repo)
        │
        ▼
┌─────────────────────────┐
│   Validation Module     │  ← PR gate
└───────────┬─────────────┘
            │ pass
            ▼
       merge (definition repos only)
            │
            ▼
┌─────────────────────────┐
│   Workshop Sync         │  ← Re-validates as safety net
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│   Metadata Service      │
└─────────────────────────┘
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Governance](../../concepts/governance.md) | Validation enforces configuration governance |
| [Scenario](../../concepts/scenario.md) | Scenario schemas validated before use |
| [Work Catalog](../../concepts/work-catalog.md) | Catalog structure and references validated |

The Validation Module operationalizes ACE's governance principle for configuration. Just as code has CI, Foundry configuration has the Validation Module — ensuring that what gets deployed is safe and consistent.

## Related concepts

- [Work Catalog](../../concepts/work-catalog.md) — Artifacts that validation checks
- [Governance](../../concepts/governance.md) — Validation as a governance mechanism
- [Workshop Sync](workshop-sync.md) — Downstream consumer of validated config
- [Work Catalog Resolution](work-catalog-resolution.md) — Uses validated catalog content

## Further reading

- [../platform-developer-guide/validation/README.md](../platform-developer-guide/validation/README.md) — Validation module specification
- [../platform-developer-guide/validation/requirements.md](../platform-developer-guide/validation/requirements.md) — Implementation requirements
- [../platform-developer-guide/work-catalog-management/validation-rules.md](../platform-developer-guide/work-catalog-management/validation-rules.md) — OI Workflow and Scenario rules
