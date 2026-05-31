# Prototype Mock Data

Static fixtures for no-backend prototype flows.

## Principles

- Data should be deterministic and resettable.
- Use realistic entity identifiers and relationships.
- Include both happy-path and failure-path records.

## Suggested fixture groups

- `workshops.*`
- `workbenches.*`
- `discovery-cases.*`
- `product-intents.*`
- `work-orders.*`
- `tasks.*`
- `governance-verdicts.*`
- `traceability-links.*`

## Current fixture files

- `workshops.json` - tenant and workshop definitions
- `workbenches.json` - workbench inventory per workshop
- `discovery-cases.json` - discovery journey entities
- `product-intents.json` - build journey entities
- `work-orders.json` - WO queue and execution records
- `tasks.json` - task-level execution records
- `teams.json` - staffing by workbench, with workshop-level shared UX and release managers
- `governance-verdicts.json` - governance outcomes and block semantics
- `traceability-links.json` - cross-entity lineage graph
- `scenarios/happyPath.json` - deterministic default startup context
- `scenarios/buildTrackTwoWorkOrders.json` - prioritized build-first scenario with two WOs

## Scenario presets

- `happyPath`
- `buildTrackTwoWorkOrders`
- `blockedAtGovernance`
- `parallelWorkOrderGroup`

## Seed context (v0.1)

- Tenant: `Zeta`
- Workshops: `Tachyon`, `Photon`, `Electron`
- `Electron` intentionally has no workbenches yet
- `DDA` display name remains uppercase with slug `dda`
