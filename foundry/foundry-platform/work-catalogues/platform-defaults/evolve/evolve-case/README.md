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

## Workspaces (Proposed)

| Workspace | Purpose |
|-----------|---------|
| Analysis | Assess current state and improvement options |
| Architecture | Design improved architecture |
| Refactoring | Execute code/system improvements |
| Validation | Verify improvements meet goals |

## TODO

- [ ] Define `workflow.yaml` for Evolve Case lifecycle
- [ ] Create workspace folders with scenario placeholders
- [ ] Document prioritization criteria for tech debt
- [ ] Define metrics for measuring improvement success

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../build/product-intent/](../build/product-intent/) — Build track example (fully defined)
