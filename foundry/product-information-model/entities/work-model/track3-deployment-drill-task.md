# Deployment Drill Task

**Model:** Work Model
**Track:** Run
**Owner:** SRE, DevOps, Release Engineering

## Definition

An optional rehearsal of a Deployment Plan in a non-production environment — validating the deployment procedure, scripts, orchestration, and rollback mechanisms before executing the actual deployment. When present, the Deployment Drill Task is a **predecessor** to the Deployment Tasks under the same Deployment Plan: the drill must pass before actual deployment tasks can proceed.

The Deployment Drill Task is scoped per **Deployment Plan**, not per individual Deployment Task. The value of a drill is rehearsing the **orchestrated sequence** — running pre-rollout scripts, applying Deployment Specifications in the correct order, executing validation scripts, and testing rollback procedures — as a complete end-to-end exercise.

> **Drill is optional.** Not every Deployment Plan requires a drill. The Operating Model determines when drills are required (e.g., "all Regulated-governance deployments with DB migrations must include a drill," "drills are recommended for first-time deployments to new environments"). The Deployment Plan decides whether to include one. See DR-029 D10.
>
> **Drill is a predecessor, not a parent.** A Deployment Task is not a child of the Drill Task. The Drill Task validates the procedure; the Deployment Task executes it for real. The precedence relationship ensures the drill completes before execution begins.

## Purpose

Makes deployment rehearsal explicit in the Run Track. Without Deployment Drill Tasks:
- Pre-deployment rehearsals are informal — there's no structured entity to track whether a drill was performed, what was rehearsed, and whether it passed
- Audit trails for "was this deployment procedure validated before production execution?" have no anchor
- The relationship between rehearsal and execution is implicit — the model doesn't distinguish "we tested the deployment" from "we deployed"

## Fields

| Field | Type | Description |
|---|---|---|
| Deployment Plan | Reference (Run) | The Deployment Plan being rehearsed |
| Drill Environment | Reference (Operational) | The non-production Deployment Environment used for the drill (e.g., staging, drill-specific environment) |
| Drill Scope | Text | What is being rehearsed: full plan, specific station sequence, specific specification application with rollback |
| Drill Results | Text | Outcome of the drill: what succeeded, what failed, what was learned, adjustments made to the plan |
| Drilled At | DateTime | When the drill was executed |

## Statuses

| Status | Description |
|---|---|
| Scheduled | Drill is planned and the drill environment is identified |
| Executing | Drill is in progress — deployment procedure is being rehearsed |
| Passed | Drill completed successfully; deployment procedure is validated; Deployment Tasks may proceed |
| Failed | Drill identified issues; Deployment Plan may need adjustment before re-drill or execution |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Rehearses | Deployment Plan (Run) | Drill Task rehearses a Deployment Plan's procedure |
| Predecessor to | Deployment Task(s) (Run) | When present, drill must pass before actual Deployment Tasks proceed |
| Targets | Deployment Environment (Operational) | Drill is executed against a non-production environment |
| Governed by | Deployment Plan (Run) | Drill Task is produced by and scoped within a Deployment Plan |

## Examples

### Full Rehearsal Drill

```
Deployment Drill Task: "Rehearse Product Deployment Specification pds-1.0 procedure"
├── Deployment Plan: "Deploy Product v4.0.0 to Production"
├── Drill Environment: Staging-Drill (eu-west-1, isolated staging clone)
├── Drill Scope:
│   ├── Run pre-rollout scripts (DB migration to v47)
│   ├── Apply pds-1.0 (all constituent System Deployment Specifications)
│   ├── Run validation scripts (health checks, smoke tests)
│   ├── Verify canary progression (5% → 25% → 100%)
│   └── Execute rollback procedure (migration reversal, prior specification restoration)
├── Drill Results:
│   ├── Pre-rollout: DB migration completed in 4 min (within 10-min threshold)
│   ├── Specification application: all System specs applied successfully
│   ├── Validation: all smoke tests passed; health checks green
│   ├── Canary: progression completed successfully
│   ├── Rollback: migration reversal completed in 6 min (within 15-min threshold)
│   └── Adjustment: increased DB migration timeout from 5 min to 10 min in specification
├── Status: Passed
└── Drilled At: 2026-02-10T14:00:00Z
```

---
