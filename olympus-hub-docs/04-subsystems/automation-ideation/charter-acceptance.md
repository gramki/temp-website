# Charter Acceptance

> **Status:** 🟡 Draft

---

## Overview

A **Charter** is created when a Process Architect (PA) accepts an Intent. The Charter represents a **design contract** — the PA commits to designing the automation, and the APO commits to the business case. Charter acceptance triggers the transition from Ideation to Design.

---

## Charter Schema

```yaml
apiVersion: hub.olympus.io/v1
kind: AutomationCharter
metadata:
  id: charter-11111
  name: dispute-auto-triage-charter
  namespace: acme-bank
spec:
  # Source Intent
  intent_id: intent-67890
  
  # Acceptance
  accepted_by: pa@acme.com
  accepted_at: "2026-01-09T16:00:00Z"
  acceptance_notes: |
    Intent is well-defined. Agentic approach is appropriate.
    Will need CSA validation for agent architecture.
    Target Q2 for initial deployment.
  
  # Confirmed Approach
  confirmed_approach: agentic    # Validated by PA
  
  # Design Commitment
  workbench_config:
    create_new_workbench: true
    workbench_name: dispute-auto-triage
    target_subscription: acme-prod
  
  # Or, if adding to existing workbench:
  # workbench_config:
  #   create_new_workbench: false
  #   existing_workbench_id: dispute-ops-dev
  #   new_scenario_name: auto-triage
  
  # Timeline
  design_target: "2026-02-15"
  deployment_target: "2026-04-01"
  
  # Milestones
  milestones:
    - name: "Architecture Complete"
      target_date: "2026-01-30"
    - name: "POC Ready"
      target_date: "2026-02-28"
    - name: "Production Ready"
      target_date: "2026-03-31"

status:
  state: active                  # active | superseded | archived
  
  # Workbench (populated when created)
  workbench_id: null
  workbench_created_at: null
  
  # Supersession
  superseded_by: null
  superseded_at: null
```

---

## Charter Lifecycle

```
                    ┌──────────────┐
                    │   ACTIVE     │
                    └──────┬───────┘
                           │
           ┌───────────────┴───────────────┐
           │                               │
           ▼                               ▼
    ┌──────────────┐               ┌──────────────┐
    │  SUPERSEDED  │               │   ARCHIVED   │
    │              │               │              │
    │ New charter  │               │ No longer    │
    │ replaces     │               │ relevant     │
    └──────────────┘               └──────────────┘
```

| State | Description | Trigger |
|-------|-------------|---------|
| `active` | Design is underway or complete | PA accepts Intent |
| `superseded` | Replaced by new Charter | New Intent accepted for same scope |
| `archived` | No longer relevant | Business case obsolete |

---

## PA Acceptance Flow

### Review Process

```
PA                            Ideation Services              APO
 │                                  │                          │
 │◀── Notification: Intent ─────────┤                          │
 │    submitted for review          │                          │
 │                                  │                          │
 ├─── Open Intent ─────────────────▶│                          │
 │                                  │                          │
 │◀── Intent Details ───────────────┤                          │
 │    + Success Criteria            │                          │
 │    + Proposed Approach           │                          │
 │                                  │                          │
 │    (PA Reviews)                  │                          │
 │    • Design feasibility?         │                          │
 │    • Approach appropriate?       │                          │
 │    • Resources available?        │                          │
 │    • Timeline realistic?         │                          │
 │                                  │                          │
 ├─── Accept Intent ───────────────▶│                          │
 │    + Acceptance notes            │                          │
 │    + Workbench config            │                          │
 │    + Timeline                    │                          │
 │                                  │                          │
 │                                  ├─── Create Charter ───────▶│
 │                                  │                          │
 │                                  ├─── Notify APO ───────────▶│
 │                                  │    "Charter created"      │
 │                                  │                          │
```

### Acceptance Criteria

PA evaluates:

| Criterion | Question | If No |
|-----------|----------|-------|
| **Clarity** | Is the problem well-defined? | Request APO clarification |
| **Feasibility** | Can we design this? | Reject or request scope change |
| **Approach** | Is conventional/agentic right? | Propose alternative |
| **Resources** | Do we have capacity? | Negotiate timeline |
| **Value** | Is success criteria measurable? | Request refinement |

### Rejection or Clarification

If PA cannot accept:

```
PA                            Ideation Services              APO
 │                                  │                          │
 ├─── Request Clarification ───────▶│                          │
 │    + Questions/concerns          │                          │
 │                                  │                          │
 │                                  ├─── Notify APO ───────────▶│
 │                                  │    "PA needs clarification"│
 │                                  │                          │
 │                                  │◀── APO updates Intent ────┤
 │                                  │                          │
 │◀── Intent updated ───────────────┤                          │
 │                                  │                          │
```

---

## Workbench Initiation

When Charter is created, it can trigger Workbench creation:

### New Workbench

```yaml
workbench_config:
  create_new_workbench: true
  workbench_name: dispute-auto-triage
  target_subscription: acme-prod
```

Creates:

```yaml
workbench:
  id: wb-dispute-auto-triage
  name: dispute-auto-triage
  charter_id: charter-11111
  dev_lifecycle_stage: DEV
  # ... other workbench config
```

### Existing Workbench

```yaml
workbench_config:
  create_new_workbench: false
  existing_workbench_id: dispute-ops-dev
  new_scenario_name: auto-triage
```

Adds new Scenario to existing Workbench.

---

## Agentic Path Handoff

If `confirmed_approach: agentic`, Charter triggers CSA engagement:

```
Charter Created              Seer Extension
      │                           │
      ├─── Agentic Charter ──────▶│
      │                           │
      │                           ├─── Notify CSA
      │                           │    "New agentic charter"
      │                           │
      │                           ├─── CSA reviews
      │                           │    architecture feasibility
      │                           │
```

See [Agentic Automation Lifecycle](../../../olympus-seer-docs/seer-design/personas-and-needs/journeys/agentic-automation-lifecycle.md).

---

## Charter Amendments

If scope or approach changes significantly after Charter creation:

1. **Minor changes** — Update Charter, notify stakeholders
2. **Major changes** — Create new Intent, supersede existing Charter

### Supersession

```yaml
# New Charter
charter:
  id: charter-22222
  intent_id: intent-77777  # New Intent

# Old Charter
charter:
  id: charter-11111
  status:
    state: superseded
    superseded_by: charter-22222
    superseded_at: "2026-03-01T10:00:00Z"
```

---

## APIs

### REST (Creator Channel)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/intents/{intent_id}/accept` | PA accepts Intent, creates Charter |
| `GET` | `/charters` | List Charters |
| `GET` | `/charters/{charter_id}` | Get Charter details |
| `PUT` | `/charters/{charter_id}` | Update Charter |
| `POST` | `/charters/{charter_id}/supersede` | Supersede with new Charter |
| `POST` | `/charters/{charter_id}/archive` | Archive Charter |

### MCP (Creator Channel)

| Tool | Description |
|------|-------------|
| `accept_intent` | PA accepts Intent, creates Charter |
| `list_charters` | List with filters |
| `get_charter` | Get details |
| `update_charter` | Update Charter |

---

## Related Documentation

- [Intent Formalization](./intent-formalization.md) — Source of Charters
- [Outcome Tracking](./outcome-tracking.md) — Post-deployment tracking
- [Process Architect](../../08-personas-and-journeys/personas/process-architect.md)
- [Workbench Management](../workbench-management/README.md)

