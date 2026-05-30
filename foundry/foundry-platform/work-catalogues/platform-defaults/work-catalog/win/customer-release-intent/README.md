# Customer Release Intent

**Orchestration Item for the Win track.**

> **Status:** Stub — workflow and scenarios to be defined.

## Overview

A Customer Release Intent (CRI) represents the work to successfully deploy and enable a release for customers. While Build track's Product Intent ends at "released," the Win track's CRI picks up to ensure customers actually adopt and succeed with the release.

## UPIM Alignment

| UPIM Concept | Win Track Realization |
|--------------|----------------------|
| Win Track | This folder |
| Customer Release Intent | OI coordinating customer enablement |
| Enablement, Training, Adoption | Work entities processed by scenarios |

## Lifecycle (Proposed)

```
start → release-received → enablement-planned → enablement-in-progress → 
customers-enabled → adoption-tracked → success-confirmed → end
```

### Stage Descriptions (Proposed)

| Stage | Description |
|-------|-------------|
| `release-received` | New release from Build track received |
| `enablement-planned` | Rollout and enablement plan created |
| `enablement-in-progress` | Documentation, training, communication in progress |
| `customers-enabled` | Customers have access and materials |
| `adoption-tracked` | Monitoring customer adoption metrics |
| `success-confirmed` | Adoption goals met, case closed |

## Stations and scenarios (Proposed)

Win reuses the canonical six [workspace stations](../../../../../../ace/workspaces/README.md) — functional teams, not stages. Customer enablement is win-flavored ingress scenarios on those same teams; the items below are scenarios, not new workspaces.

| Station | Win scenarios (activities) |
|---------|----------------------------|
| Product Specification | Plan rollout/enablement strategy, define adoption goals |
| UX Design | Produce customer-facing docs and training materials |
| Release | Enable customer access, stage rollout |
| QA | Track adoption metrics, confirm success criteria |
| Governance | Release-readiness/customer-commitment review (cross-cutting) |

Win uses *some* stations per release. Documentation, Training, and Customer Success are activities/scenarios, not workspaces.

## TODO

- [ ] Define `workflow.yaml` for Customer Release Intent lifecycle
- [ ] Add win scenario files under the relevant station folders (no new workspaces)
- [ ] Document handoff from Build track
- [ ] Define adoption metrics and success criteria

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../build/product-intent/](../build/product-intent/) — Build track example (fully defined)
