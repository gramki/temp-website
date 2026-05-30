# Evolve Case

**Orchestration Item for the Evolve track.**

> **Status:** Stub — workflow and scenarios to be defined.

## Overview

An Evolve Case represents continuous improvement work — addressing technical debt, improving performance, refactoring architecture, and modernizing systems. Evolve Cases ensure the product remains maintainable and can adapt to changing needs.

## UPIM Alignment

| UPIM Concept | Evolve Track Realization |
|--------------|-------------------------|
| Evolve Track | This folder |
| Evolve Case | OI coordinating improvement work |
| Tech Debt, Refactoring, Migration | Work entities processed by scenarios |

## Lifecycle (Proposed)

```
start → improvement-identified → analysis-complete → plan-approved → 
implementation-in-progress → validation-complete → deployed → end
```

### Stage Descriptions (Proposed)

| Stage | Description |
|-------|-------------|
| `improvement-identified` | Improvement opportunity documented |
| `analysis-complete` | Impact, effort, and approach analyzed |
| `plan-approved` | Stakeholders approve the improvement plan |
| `implementation-in-progress` | Active refactoring/improvement work |
| `validation-complete` | Changes validated (tests, performance) |
| `deployed` | Improvements deployed to production |

## Stations and scenarios (Proposed)

Evolve reuses the canonical six [workspace stations](../../../../../../ace/workspaces/README.md) — functional teams, not stages. Improvement work is evolve-flavored ingress scenarios on those same teams; the items below are scenarios, not new workspaces.

| Station | Evolve scenarios (activities) |
|---------|-------------------------------|
| Product Specification | Assess current state, scope improvement, prioritize tech debt |
| Development | Design improved architecture, execute refactoring/migration |
| QA | Validate improvements (tests, performance, regression) |
| Release | Deploy improvements |
| Governance | Architecture review, improvement-plan approval (cross-cutting) |

Architecture is an activity performed by the Development team, not a separate workspace. Evolve uses *some* stations per case.

## TODO

- [ ] Define `workflow.yaml` for Evolve Case lifecycle
- [ ] Add evolve scenario files under the relevant station folders (no new workspaces)
- [ ] Document prioritization criteria for tech debt
- [ ] Define metrics for measuring improvement success

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../build/product-intent/](../build/product-intent/) — Build track example (fully defined)
