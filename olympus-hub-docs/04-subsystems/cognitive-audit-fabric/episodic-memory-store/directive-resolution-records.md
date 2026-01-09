# Directive Resolution Records

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-08  
> **Parent:** [Episodic Memory Store](./README.md)

---

## Overview

Directive Resolution Records track the **lifecycle of human interventions** in agent operations—from acknowledgment through execution to outcome. They complement Override and ContextIntervention records by providing a complete audit trail of what happened after an intervention was initiated.

| Attribute | Value |
|-----------|-------|
| **Purpose** | Track intervention acknowledgment, execution, and outcome |
| **Timing** | Written after Override or ContextIntervention is created |
| **Linkage** | Always linked to an intervention record (Override or ContextIntervention) |
| **Storage** | Enterprise Memory (via Memory Services) |
| **CAF Role** | Catalog, schema, lifecycle tracking, pattern detection |

---

## Why Directive Resolution Records Matter

Override and ContextIntervention records capture **what intervention was requested**. Directive Resolution records capture **what happened next**:

| Without Resolution Records | With Resolution Records |
|---------------------------|------------------------|
| Cannot confirm intervention was acknowledged | Full acknowledgment trail |
| Cannot track execution status | Execution timeline captured |
| Cannot link intervention to actual outcome | Outcome explicitly linked |
| Cannot detect stalled interventions | Resolution status visible |
| Cannot analyze intervention effectiveness | Outcome data for learning |

---

## Directive Resolution Record Schema

```yaml
directive_resolution_record:
  # Identity & Integrity
  id: uuid                           # Unique identifier (UUID v4)
  content_hash: string               # sha256:<hex> — hash of record content
  timestamp: datetime
  case_id: uuid                      # Universal binding ID
  
  # Hub Metadata
  hub_metadata:
    tenant_id: string                # Tenant identifier
    subscription_id: string          # Subscription within tenant
    workbench_id: string             # Workbench where resolution occurred
    scenario_id: string              # Scenario context
    request_id: string               # Hub Request this resolution belongs to
    parent_request_id: string        # Parent request if nested (optional)
  
  # Record Subtype
  subtype: enum                      # ack | outcome
  
  # Intervention Reference
  intervention_ref:
    record_type: enum                # Override | ContextIntervention
    record_id: uuid                  # ID of the intervention record
  
  # Resolution Details
  resolution:
    status: enum                     # acknowledged | executed | failed | superseded
    resolved_by: string              # User ID or Agent ID who resolved
    resolved_by_type: enum           # human | agent
    resolved_at: datetime            # When resolution occurred
    resolution_notes: text           # Free-form notes about resolution
    resolution_method: enum          # manual | assisted | automatic
  
  # Outcome (only for subtype: outcome)
  outcome:
    result_type: enum                # See Outcome Result Types below
    result_description: text         # Human-readable description
    result_ref:                      # Reference to new artifact created
      ref_type: enum                 # decision | task | scenario | none
      ref_id: uuid                   # ID of the new decision/task/scenario
      ref_workbench_id: string       # Workbench if cross-workbench
    variance_from_expected:          # Did outcome match expectations?
      matched: boolean
      variance_description: text     # If not matched, what differed
  
  # Timing Metrics
  timing:
    intervention_created_at: datetime  # When Override/ContextIntervention was created
    acknowledged_at: datetime          # When intervention was acknowledged
    executed_at: datetime              # When intervention was executed
    outcome_recorded_at: datetime      # When outcome was finalized
    time_to_ack_seconds: integer       # Duration: created → acknowledged
    time_to_resolution_seconds: integer  # Duration: created → outcome
  
  # Escalation Context
  escalation_context:
    escalation_level: integer        # Level at which intervention was handled
    task_id: uuid                    # Escalation task ID
    task_queue_id: string            # Queue that handled escalation
    original_rejection:
      rejection_source: enum         # agent | guardrail | policy | application
      rejection_reason: text         # Why the original artifact was rejected
  
  # Metadata
  tags: array
  linked_records: array
```

---

## Record Subtypes

Directive Resolution records have two subtypes, written at different points in the intervention lifecycle:

### Subtype: `ack` (Acknowledgment)

Written when a human acknowledges the intervention requirement.

```json
{
  "subtype": "ack",
  "resolution": {
    "status": "acknowledged",
    "resolved_by": "user-alice-supervisor",
    "resolved_by_type": "human",
    "resolved_at": "2026-01-08T10:15:00Z",
    "resolution_notes": "Reviewing escalated decision",
    "resolution_method": "manual"
  },
  "outcome": null
}
```

### Subtype: `outcome` (Resolution Outcome)

Written when the intervention is fully resolved with an outcome.

```json
{
  "subtype": "outcome",
  "resolution": {
    "status": "executed",
    "resolved_by": "user-alice-supervisor",
    "resolved_by_type": "human",
    "resolved_at": "2026-01-08T10:30:00Z",
    "resolution_notes": "Context updated with additional customer history; re-run successful",
    "resolution_method": "manual"
  },
  "outcome": {
    "result_type": "context_rerun",
    "result_description": "Agent re-ran decision with enriched context, produced acceptable result",
    "result_ref": {
      "ref_type": "decision",
      "ref_id": "dec-new-12345"
    },
    "variance_from_expected": {
      "matched": true
    }
  }
}
```

---

## Resolution Status Values

| Status | Description | Typical Flow |
|--------|-------------|--------------|
| **acknowledged** | Human has seen and acknowledged the intervention | First step after Override/ContextIntervention created |
| **executed** | Intervention action was successfully executed | Context changed, decision overridden, etc. |
| **failed** | Intervention could not be executed | Technical failure, permission issue, etc. |
| **superseded** | Intervention was replaced by another intervention | Higher authority override, scenario cancellation |

---

## Outcome Result Types

| Result Type | Description | Result Ref Type |
|-------------|-------------|-----------------|
| **decision_changed** | Decision was overridden with new value | `decision` |
| **context_rerun** | Context was modified and agent re-ran | `decision` (new decision) |
| **task_reassigned** | Task was reassigned to different agent | `task` |
| **task_abandoned** | Task was abandoned | `task` |
| **scenario_failed** | Scenario was failed/cancelled | `scenario` |
| **corrective_action_spawned** | New scenario created for correction | `scenario` |
| **no_action_taken** | Intervention reviewed but no action needed | `none` |

---

## Lifecycle Example

```
T+0s    Override Record created (agent decision rejected by guardrail)
        ├── override_id: ovr-001
        └── Escalation task created in Supervisor Queue

T+120s  DirectiveResolution (subtype: ack) created
        ├── resolution.status: acknowledged
        ├── resolution.resolved_by: supervisor-alice
        └── timing.time_to_ack_seconds: 120

T+300s  Supervisor reviews, decides to add context and re-run

T+310s  ContextIntervention Record created
        └── context_intervention_id: ctx-001

T+320s  Agent re-runs with new context, produces acceptable decision

T+325s  DirectiveResolution (subtype: outcome) created
        ├── resolution.status: executed
        ├── outcome.result_type: context_rerun
        ├── outcome.result_ref: { ref_type: "decision", ref_id: "dec-new-001" }
        └── timing.time_to_resolution_seconds: 325
```

---

## Timing Metrics for Analysis

| Metric | Purpose | Healthy Range |
|--------|---------|---------------|
| **time_to_ack_seconds** | How quickly was intervention acknowledged? | <300s for high-priority |
| **time_to_resolution_seconds** | Total intervention duration | Depends on complexity |
| **execution_duration** | Time from ack to outcome | Depends on action type |

These metrics feed into Workbench analytics and Supervisor dashboards.

---

## Relationship to Other Records

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INTERVENTION FLOW                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────────┐         ┌──────────────────┐                         │
│   │ Override Record  │    OR   │ ContextInter-    │                         │
│   │                  │         │ vention Record   │                         │
│   └────────┬─────────┘         └────────┬─────────┘                         │
│            │                            │                                    │
│            └─────────────┬──────────────┘                                   │
│                          │                                                   │
│                          ▼                                                   │
│            ┌──────────────────────────────┐                                 │
│            │  DirectiveResolution (ack)   │                                 │
│            │  subtype: ack                │                                 │
│            │  status: acknowledged        │                                 │
│            └──────────────┬───────────────┘                                 │
│                           │                                                  │
│                           ▼                                                  │
│            ┌──────────────────────────────┐                                 │
│            │ DirectiveResolution (outcome)│                                 │
│            │ subtype: outcome             │                                 │
│            │ status: executed/failed/...  │                                 │
│            │ outcome.result_ref → new     │                                 │
│            │   decision/task/scenario     │                                 │
│            └──────────────────────────────┘                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Pattern Detection

CAF monitors resolution patterns to identify:

| Pattern | Indicator | Action |
|---------|-----------|--------|
| **Slow Acknowledgment** | time_to_ack > threshold | Staffing/routing review |
| **High Failure Rate** | Many `failed` outcomes | Process/tooling issue |
| **Frequent Superseding** | Many `superseded` | Escalation policy review |
| **Variance Mismatches** | Outcomes often don't match expected | Training/calibration need |

---

## Retention

| Record Type | Retention Period | Rationale |
|-------------|------------------|-----------|
| **Directive Resolution Records** | Same as Override Records (10 years) | Audit continuity |

---

## Related Documentation

- [CAF Overview](../README.md)
- [Episodic Memory Store](./README.md)
- [Override Records](./override-records.md)
- [Handoff Context](./handoff-context.md)
- [Agent Directability](../../../02-system-design/implementation-concepts/agent-directability.md)
- [Task Management](../../task-management/README.md)

---

