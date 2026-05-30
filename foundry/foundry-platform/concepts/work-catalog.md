# Work Catalog

A Work Catalog is the hierarchical collection of OI Workflows and Scenarios that defines what work a Foundry can execute and how it flows through the system — the executable realization of the UPIM Work Model.

## What it is

Work Catalogs answer two questions: (1) how do orchestration items move through their lifecycle? and (2) what work does each Workspace accept?

The catalog consists of two components:

- **OI Workflows** — State machines that orchestrate an Orchestration Item (Product Intent, Discovery Case, etc.) through its lifecycle, defining stages, transitions, and which Work Orders to create.
- **Scenarios** — Ingress contracts that define what work a Workspace accepts and how it should be executed.

Work Catalogs exist at five levels, with more specific levels overriding more general ones:

```
Platform                    ← Shipped with Foundry product
    └── Foundry             ← Organization-wide customizations
        └── Workshop        ← Division/unit defaults
            └── Workbench   ← Product-specific overrides
                └── User    ← Personal experiments (requires activation)
```

**Resolution rule:** Closest wins. If you define a scenario in your User catalog, it shadows the same-named scenario at all higher levels. This enables org-wide defaults with product-specific exceptions.

**User catalog activation:** User-level customizations require explicit opt-in via session flag or user profile setting. This prevents accidental production impact from experimental scenarios.

The folder structure reflects Track and Workspace organization:

```
work-catalog/
├── {track}/                      # build, discovery, run, win, evolve, governance
│   └── {orchestration-item}/     # product-intent, discovery-case, etc.
│       ├── workflow.yaml         # OI Workflow definition
│       └── {workspace}/          # development, qa, release, etc.
│           └── scenarios/
│               └── scenario.yaml
```

## Where it lives in Foundry

| Level | Repository Location | Provisioned By |
|-------|---------------------|----------------|
| **Platform** | `work-catalogues/platform-defaults/work-catalog/` | Platform release |
| **Foundry** | `foundry-{id}/work-catalog/` | Foundry provisioning |
| **Workshop** | `workshop-{id}/work-catalog/` | Workshop provisioning |
| **Workbench** | `workshop-{id}/workbenches/{wb}/work-catalog/` | Workbench provisioning |
| **User** | `user-work-catalog-{userId}/work-catalog/` | On first publish |

| Module | Responsibility |
|--------|----------------|
| **Work Catalog Management** (Management subsystem) | Schema, validation, resolution algorithm |
| **Validation Module** | PR validation for catalog changes |
| **Workshop Sync** | Sync catalog changes to Metadata Service |
| **Orchestrator** | Consumes OI Workflows |
| **WO Runtime** | Consumes Scenarios |

## ACE/UPIM alignment

| UPIM Concept | Work Catalog Realization |
|--------------|--------------------------|
| 6 Tracks | Track folders in catalog structure |
| Orchestration Items | OI folders containing `workflow.yaml` |
| Work Model entities | Input/output types in Scenarios |
| State transitions | OI Workflow stages and handlers |

The Work Catalog makes UPIM executable. UPIM says "Product Intents move through specification, development, QA, and release"; the Work Catalog's `product-intent/workflow.yaml` defines exactly how — what triggers each transition, what Work Orders get created, what governance checks apply.

## Related concepts

- [Scenario](scenario.md) — The ingress contracts within the catalog
- [Orchestration Item](orchestration-item.md) — What OI Workflows orchestrate
- [Work Order](work-order.md) — What gets created when Scenarios trigger
- [Knowledge Hierarchy](knowledge-hierarchy.md) — Similar hierarchy pattern for knowledge

## Further reading

- [../work-catalogues/README.md](../work-catalogues/README.md) — Conceptual overview and user guide index
- [../management/platform-developer-guide/work-catalog-management/README.md](../management/platform-developer-guide/work-catalog-management/README.md) — Schemas, validation, resolution algorithm
- [../work-catalogues/user-guide/authoring-scenarios.md](../work-catalogues/user-guide/authoring-scenarios.md) — How to create Scenarios
- [../management/platform-developer-guide/work-catalog-management/resolution-algorithm.md](../management/platform-developer-guide/work-catalog-management/resolution-algorithm.md) — Full resolution details
