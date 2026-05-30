# Run Case

**Orchestration Item for the Run track.**

> **Status:** Stub — workflow and scenarios to be defined.

## Overview

A Run Case represents an operational activity — managing production systems, responding to incidents, executing maintenance windows, and ensuring system health. Run Cases coordinate the ongoing work required to keep products operational.

## UPIM Alignment

| UPIM Concept | Run Track Realization |
|--------------|----------------------|
| Run Track | This folder |
| Run Case | OI coordinating operational activities |
| Incidents, Changes, Maintenance | Work entities processed by scenarios |

## Lifecycle (Proposed)

```
start → case-opened → triage-complete → work-in-progress → 
resolution-implemented → verified → case-closed → end
```

### Stage Descriptions (Proposed)

| Stage | Description |
|-------|-------------|
| `case-opened` | Operational case created (incident, change request, etc.) |
| `triage-complete` | Priority and ownership assigned |
| `work-in-progress` | Active resolution/implementation work |
| `resolution-implemented` | Fix or change applied |
| `verified` | Resolution confirmed working |
| `case-closed` | Case complete, documentation updated |

## Stations and scenarios (Proposed)

Run reuses the canonical six [workspace stations](../../../../../../ace/workspaces/README.md) — functional teams, not stages. Operational activities are run-flavored ingress scenarios on those same teams; the items below are scenarios, not new workspaces.

| Station | Run scenarios (activities) |
|---------|----------------------------|
| Development | Implement change/fix, execute maintenance action |
| QA | Verify resolution, post-change validation |
| Release | Deploy change, roll back, maintenance window execution |
| Product Specification | Incident triage and ownership, change scoping |
| Governance | Change approval, incident review (cross-cutting) |

Run typically uses *some* stations (Development, QA, Release) heavily and others lightly. Monitoring/alerting is tooling consumed across stations, not a workspace.

## TODO

- [ ] Define `workflow.yaml` for Run Case lifecycle
- [ ] Add run scenario files under the relevant station folders (no new workspaces)
- [ ] Document SLA tracking and escalation
- [ ] Define integration with incident management systems

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../build/product-intent/](../build/product-intent/) — Build track example (fully defined)
