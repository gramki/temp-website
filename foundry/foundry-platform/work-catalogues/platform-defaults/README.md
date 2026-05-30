# Platform Default Work Catalog

Platform-shipped Work Catalog content that bootstraps every new Foundry tenant.

> **Scenario specs are indicative.** The scenario `*.yaml` files shipped here illustrate the *shape* of each track's work — station ownership, scope, and the flow the OI workflow orchestrates. Their `inputs`, `outputs`, `required-skills`, and `tasks` are placeholders, not the true detail or structure. Treat them as worked examples to be replaced with real definitions during specification, not as authoritative contracts. The `workflow.yaml` files are the more reliable artifact; the per-scenario internals are not.

## Structure

```
platform-defaults/
└── work-catalog/
    ├── build/
    │   └── product-intent/
    │       ├── workflow.yaml
    │       └── {workspace}/scenarios/
    ├── discovery/
    │   └── discovery-case/
    ├── run/
    │   └── run-case/
    ├── win/
    │   └── customer-release-intent/
    ├── evolve/
    │   └── evolve-case/
    └── governance/
        └── governance-ritual/
```

The `work-catalog/` segment mirrors tenant repository layout. Path pattern:

```
work-catalog/{track}/{oi-type}/workflow.yaml
work-catalog/{track}/{oi-type}/{workspace}/scenarios/*.yaml
```

## Tracks

| Track | OI type | Status |
|-------|---------|--------|
| build | product-intent | Workflow complete + indicative scenarios |
| discovery | discovery-case | Workflow complete + indicative scenarios |
| run | run-case | Stub |
| win | customer-release-intent | Stub |
| evolve | evolve-case | Stub |
| governance | governance-ritual | Stub |

## Sync and validation

| Aspect | Detail |
|--------|--------|
| Location | Part of Foundry codebase (`work-catalogues/platform-defaults/`) |
| Validation | Validation module at Foundry deployment/upgrade |
| Sync trigger | Foundry deployment/upgrade |
| Resolution level | Platform (lowest in hierarchy; overridden by Foundry → Workshop → Workbench → User) |

## Read Next

- [../README.md](../README.md) — Work Catalogues module overview
- [build/product-intent/README.md](work-catalog/build/product-intent/README.md) — Complete Product Intent example
- [../../management/platform-developer-guide/validation/README.md](../../management/platform-developer-guide/validation/README.md) — Validation module
