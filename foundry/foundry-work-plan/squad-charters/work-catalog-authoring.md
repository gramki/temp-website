# Squad Charter — Work Catalog Authoring

**Stream:** Work Catalog Authoring  
**Catalog steward:** TBD

## Purpose

Produce **authoritative Work Catalog content** — OI workflows and scenarios — that encode SDLC track expertise. This is a **content and domain** stream, not platform engineering. Track owners know Discovery, Build, and Governance transitions; the Catalog steward ensures schema compliance and cross-track consistency.

> Platform squads build the engine; track experts write the catalog; Release Engineering builds and owns CI pipelines.

## Boundaries

### In scope

- Authoritative `workflow.yaml` for Phase 1 OIs: Discovery Case, Product Intent
- Authoritative scenario definitions under [platform-defaults/work-catalog/](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/)
- Governance transition scenarios (seven gates per [governance-mvp.md](../phase-1/governance-mvp.md))
- Cross-track handoff specification (`proceed-to-build` → Product Intent)
- Review of workshop-level catalog overrides (guidance only in Phase 1)

### Out of scope

- WCM engine (schema, resolution, validation) — Control Plane
- Orchestrator implementation of workflow actions — Control Plane
- WO Runtime execution — Execution Plane
- CI / release pipelines — Release Engineering
- Run, Win, Evolve track catalogs (Phase 1)
- Governance Ritual track workflows (cadence rituals deferred)

## Track ownership

| Track | Owner | Catalog path | Milestone when authoritative |
|-------|-------|--------------|------------------------------|
| **Discovery** | Discovery track owner (TBD) | [discovery/discovery-case/](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/) | M1 (first scenario); M3 (full workflow) |
| **Build** | Build track owner (TBD) | [build/product-intent/](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/) | M2 (full workflow + scenarios) |
| **Governance (transitions)** | Governance track owner (TBD) | `governance/scenarios/` under Discovery + Build OI folders | M2 (Build gates); M4 (all seven) |

## Catalog steward responsibilities

- Maintain naming conventions (kebab-case scenarios, station slugs)
- Validate content against WCM schema before publish
- Facilitate cross-track handoff review (Discovery → Build)
- Keep platform-defaults README indicative-spec disclaimer accurate
- Chair catalog review cadence ([governance-cadences.md](../governance-cadences.md))

## Phase 1 deliverables

| Milestone | Deliverable |
|-----------|-------------|
| M0 | Schema contract with Control Plane; steward appointed |
| M1 | `frame-discovery-case` authoritative |
| M2 | Full Product Intent workflow + Build scenarios + Build governance scenarios |
| M3 | Full Discovery Case workflow + Discovery scenarios + handoff spec |
| M4 | All governance scenarios with real inputs/outputs/check criteria |
| M5 | Catalog sign-off for platform defaults |

## Dependencies

| Depends on | For |
|------------|-----|
| Control Plane (WCM) | Schema, validation errors, publish path |
| Control Plane (Orchestrator) | Which workflow actions are implemented — catalog leads implementation |
| [scenario-catalog.md](../phase-1/scenario-catalog.md) | Phase 1 scenario inventory |
| [golden-path.md](../phase-1/golden-path.md) | Sequence to encode in workflows |

**Ordering rule:** Catalog content for a workflow stage must be authoritative **before** Control Plane implements Orchestrator handlers for that stage.

## Skills required

- ACE/UPIM Work Model and six workspace stations (not stages)
- SDLC practice for Discovery and Build tracks
- Scenario design: inputs, outputs, human vs agent tasks, governance hooks
- YAML workflow authoring per [authoring-oi-workflows.md](../../foundry-platform/work-catalogues/user-guide/authoring-oi-workflows.md)

## Non-ownership (explicit)

| Concern | Owner |
|---------|-------|
| WCM resolution algorithm | Control Plane |
| Orchestrator workflow engine | Control Plane |
| Foundry CI | Release Engineering |
| IDE scenario authoring UX (user catalog) | Builder Experience |

## Read next

- [../people-plan.md](../people-plan.md) — track owner roster
- [../phase-1/scenario-catalog.md](../phase-1/scenario-catalog.md)
- [../../foundry-platform/work-catalogues/README.md](../../foundry-platform/work-catalogues/README.md)
