# Build Track

**Track purpose:** Transform product ideas into released, customer-ready features.

## Overview

The Build track covers the complete journey from product intent to customer release. It's the primary track for feature development in ACE Foundry.

## Orchestration Item: Product Intent

The Build track uses **Product Intent (PI)** as its orchestration item. A Product Intent represents a product idea or feature request that will be implemented and released.

→ [product-intent/](product-intent/) — Product Intent OI Workflow and Workspace scenarios

## Workspaces

The Build track spans these Workspaces:

| Workspace | Purpose |
|-----------|---------|
| Product Specification | Define detailed product requirements from the PI |
| UX Design | Design user experience and interface |
| Development | Implement the specified feature |
| QA | Test the implementation |
| Release | Package and release to customers |
| Governance | Cross-cutting governance checks |

## Workflow Summary

```
PI Created
    ↓
draft-ready ─────────────────────→ ready-for-specification
    (PO approval)                      (awaits Release Intent milestone)
                                           ↓
                                   in-specification
                                       (Product Specification WO)
                                           ↓
                                   specified ───────────────────→ in-qa
                                       (Dev + QA prep WOs parallel)  (QA WO)
                                                                       ↓
                                                               ready-for-release
                                                                   (Release WO)
                                                                       ↓
                                                                   released
                                                                       ↓
                                                                     end
```

## UPIM Alignment

| UPIM Concept | Build Track Realization |
|--------------|------------------------|
| Build Track | This folder |
| Product Intent | product-intent/ OI |
| Work entities | Epics, Stories, Tasks, Bugs processed by scenarios |

## Platform Default Content

This folder contains platform-shipped defaults. Organizations can:
- Use these as-is
- Override at Foundry/Workshop/Workbench levels
- Extend with additional scenarios

See [../../README.md](../../README.md) for the complete platform-defaults structure.
