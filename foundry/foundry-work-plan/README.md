# Foundry Work Plan

This folder contains the **project plan** for building the Foundry Platform: people, milestones, governance cadences, and value-realized verification checkpoints. It complements the engineering documentation in [../foundry-platform/](../foundry-platform/README.md).

**Phase 1 build contracts** (scope, golden path, module boundaries) live in [phase-1/](phase-1/README.md). This folder is the **when, who, and how**; `phase-1/` is the **what to build**.

## Documentation index

| Document | Purpose |
|----------|---------|
| [people-plan.md](people-plan.md) | Program roles, five delivery streams, roster templates |
| [milestones.md](milestones.md) | M0–M5 vertical slices and definition of done |
| [governance-cadences.md](governance-cadences.md) | Project steering cadences (not ACE Governance Workspace) |
| [value-checkpoints.md](value-checkpoints.md) | Phase 1 value verification against the build question |
| [squad-charters/](squad-charters/) | Per-stream scope, deliverables, dependencies |
| [integration/](integration/) | Dependency graph, contract gates, demo runbook |
| [phase-1/](phase-1/README.md) | Technical build contracts for Phase 1 |

### Squad charters

| Stream | Charter |
|--------|---------|
| Control Plane | [squad-charters/control-plane.md](squad-charters/control-plane.md) |
| Execution Plane | [squad-charters/execution-plane.md](squad-charters/execution-plane.md) |
| Builder Experience | [squad-charters/builder-experience.md](squad-charters/builder-experience.md) |
| Release Engineering | [squad-charters/release-engineering.md](squad-charters/release-engineering.md) |
| Work Catalog Authoring | [squad-charters/work-catalog-authoring.md](squad-charters/work-catalog-authoring.md) |

### Integration

| Document | Purpose |
|----------|---------|
| [integration/dependency-graph.md](integration/dependency-graph.md) | Squad blocking relationships and critical path |
| [integration/contract-gates.md](integration/contract-gates.md) | API/event gates between streams |
| [integration/demo-runbook.md](integration/demo-runbook.md) | Golden-path demo operations |

## Planning principle

> Platform squads build the engine; track experts write the catalog; Release Engineering builds and owns CI pipelines.

Organize **delivery** around golden-path milestones ([milestones.md](milestones.md)). Organize **ownership** around the five streams ([people-plan.md](people-plan.md)).

## Audience

Primary readers: Foundry engineering leadership (EMs, tech leads, program management) and executive stakeholders who fund and oversee the work.

## How this folder relates to the rest of the tree

- The **what** of the platform lives in [../foundry-platform/](../foundry-platform/README.md).
- Governance cadences here are **project-level** steering — not the [Governance Workspace](../ace/governance.md) inside a Workbench.
- Value checkpoints reference UPIM entities where appropriate. See [../product-information-model/](../product-information-model/README.md).

## Not in this folder

| Topic | Location |
|-------|----------|
| Module specs and design decisions | [../foundry-platform/](../foundry-platform/README.md) |
| ACE conceptual content | [../ace/](../ace/README.md) |
| Customer-facing positioning | [../stakeholder-briefs/](../stakeholder-briefs/README.md) |
| **Budget plan** | TBD |

## Read next

- [people-plan.md](people-plan.md) — start here for team structure
- [milestones.md](milestones.md) — delivery sequence
- [phase-1/golden-path.md](phase-1/golden-path.md) — end-to-end demo path
