# How Product Evolves in ACE

This is the practitioner guide for operating inside ACE. The theory is in [../product-evolution-cycle.md](../product-evolution-cycle.md) and [../concepts.md](../concepts.md); this folder explains how product evolution is organized in practice through Tracks, orchestration items, Workspaces, Work Orders, and governance.

## The operating pattern

```text
Track
  -> primary orchestration item
    -> Workspace Work Orders
      -> outputs / decisions / evidence
        -> downstream track or next orchestration state
```

- A **Track** is a value stream: Discovery, Build, Run, Win, Evolve, and ACE Governance.
- An **orchestration item** is the Track-level coordination item the Orchestrator routes.
- A **Workspace Work Order** is a Scenario execution instance in one Workspace, attached to an orchestration item.
- A **transition** of an orchestration item invokes governance.

## What this guide covers

| File | Purpose |
|------|---------|
| [discovery.md](discovery.md) | How cross-functional discovery forms product decisions and Product Intent. |
| [build.md](build.md) | How Build executes Product Intent, including delivery and discovery-supporting work. |
| [orchestration-items.md](orchestration-items.md) | Track-level orchestration items and how they differ from Work Orders. |

## Boundaries

| Need | Go to |
|------|-------|
| Formal ACE concepts | [../concepts.md](../concepts.md) |
| Structural Product Evolution Cycle | [../product-evolution-cycle.md](../product-evolution-cycle.md) |
| Per-workspace station stubs | [../workspaces/](../workspaces/README.md) |
| UPIM entity definitions | [../../product-information-model/](../../product-information-model/README.md) |
| Platform implementation modules | [../../foundry-platform/](../../foundry-platform/README.md) |
| Work Catalogs (OI Workflows + Scenarios) | [../../foundry-platform/work-catalogues/](../../foundry-platform/work-catalogues/README.md) |
| Work Catalog Management | [../../foundry-platform/management/platform-developer-guide/work-catalog-management/](../../foundry-platform/management/platform-developer-guide/work-catalog-management/README.md) |

## Phase 1 emphasis

This first guide details Discovery and Build because those are the tracks now modeled most concretely for ACE. Run, Win, Evolve, and Governance are named in [orchestration-items.md](orchestration-items.md) and will receive deeper practitioner guides as their orchestration rules mature.
