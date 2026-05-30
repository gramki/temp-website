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

## Workspaces (Proposed)

| Workspace | Purpose |
|-----------|---------|
| Incident Response | Handle production incidents |
| Change Management | Manage planned changes |
| Maintenance | Execute maintenance activities |
| Monitoring | Configure and respond to alerts |

## TODO

- [ ] Define `workflow.yaml` for Run Case lifecycle
- [ ] Create workspace folders with scenario placeholders
- [ ] Document SLA tracking and escalation
- [ ] Define integration with incident management systems

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../build/product-intent/](../build/product-intent/) — Build track example (fully defined)
