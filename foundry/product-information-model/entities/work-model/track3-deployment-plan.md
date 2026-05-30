# Deployment Plan

**Model:** Work Model
**Track:** Run
**Owner:** SRE, DevOps, Release Engineering

## Definition

A deliberation activity where the Run team scopes a rollout — determining which System or Product deployments advance through which Deployment Trains and Stations, identifying verification and maintenance prerequisites, assessing risks, and producing Deployment Planning Tasks that create **System Deployment Specifications** or **Product Deployment Specifications**. The Deployment Plan is the Run Track's equivalent of the Build Track's Release Planning Task: it scopes and organizes deployment work without directly executing it.

Deployment Planning is a **deliberation activity** — the team learns as it plans. New information discovered during planning (infrastructure gaps, missing operational readiness, required maintenance) feeds back into the plan, producing additional tasks and updating operating artifacts. Every task produced by a Deployment Plan can produce or update work artifacts in the Run Track.

A Deployment Plan is governed by a Change Request, which provides the change management envelope with audit trail, approvals, and scoping to a Deployment Train or Station.

> **Deployment Plan encapsulates Deployment Planning Tasks.** The Deployment Plan scopes what needs to be deployed (System Version or Product Version), where, and how. Deployment Planning Tasks produce Deployment Specifications, verification tasks, and maintenance tasks. See DR-029 D9; DR-036.

## Purpose

Makes deployment scoping and deliberation explicit in the Run Track. Without Deployment Plans:
- Deployment Planning Tasks exist in isolation — there's no parent entity that scopes the overall rollout
- Risk assessment, promotion path selection, and verification planning have no structured deliberation entity
- The relationship between a Change Request (change management) and the actual deployment work is unstructured
- Deployment Drill Tasks have no parent scope — a drill is most valuable when it rehearses the entire orchestrated rollout, not individual descriptor applications

## Fields

| Field | Type | Description |
|---|---|---|
| Change Request | Reference (Run) | The Change Request this plan fulfills |
| Scope | Text | What is being deployed: System or Product deployment scope, Train/Station targets |
| Deployment Scope | Enum | `System` / `Product` — primary granularity of this plan |
| Deployment Train | Reference (Operational) | The Deployment Train this plan follows (may be derived from Change Request scope) |
| Planning Participants | List | Roles and individuals involved in the planning deliberation |
| Risk Assessment Summary | Text | Overall risk analysis for this rollout: blast radius, rollback complexity, coordination requirements |
| Target Timeline | Text | Planned deployment timeline across stations |

## Statuses

| Status | Description |
|---|---|
| Planning | Deliberation in progress; scope being determined; risks being assessed; tasks being identified |
| Planned | All Deployment Planning Tasks, Verification Tasks, and optional Drill Task have been produced; plan is ready for execution |
| Executing | Deployment Tasks are being executed according to the plan |
| Complete | All Deployment Tasks and Verification Tasks have succeeded; Change Request can be closed |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Governed by | Change Request (Run) | Deployment Plan is governed by a Change Request |
| Follows | Deployment Train (Operational) | Deployment Plan follows a Deployment Train's promotion path |
| Produces | Deployment Planning Task(s) (Run) | Planning produces leaf-level tasks that create Deployment Specifications |
| May produce | Deployment Drill Task (Run) | Planning may produce an optional rehearsal task |
| May produce | Verification Task(s) (Run) | Planning produces verification tasks for post-deployment validation |
| May produce | Maintenance Task(s) (Run) | Planning may discover maintenance prerequisites |
| Contains | Deployment Task(s) (Run) | Deployment Tasks execute within the scope of this plan |
| Informed by | Operational Readiness (Operational) | Planning considers environment readiness status |

## Examples

### Standard Deployment Plan (Product scope)

```
Deployment Plan: "Deploy Product v4.0.0 to Production"
├── Change Request: CR-2026-0142 (Standard, PCI Regulated Train)
├── Deployment Scope: Product
├── Scope: Product v4.0.0 through PCI Regulated Train
├── Deployment Train: PCI Regulated Train
├── Risk Assessment: Medium — DB migration in payments-system pre-rollout; rollback requires migration reversal
├── Produced Tasks:
│   ├── Deployment Planning Task: "Create Product Deployment Specification pds-1.0 for staging"
│   ├── Deployment Planning Task: "Create pds-1.1 for production-us"
│   ├── Deployment Planning Task: "Create pds-1.2 for production-latam"
│   ├── Verification Task: "Post-deployment SLA verification — staging"
│   ├── Verification Task: "Post-deployment SLA verification — production-us"
│   ├── Verification Task: "LATAM compliance audit — production-latam"
│   ├── Maintenance Task: "Rotate payment-gateway API keys before deployment"
│   └── Deployment Drill Task: "Rehearse pds-1.0 application in staging-drill environment"
└── Timeline: Staging (Day 1) → Prod-US (Day 4) → Prod-LATAM (Day 11)
```

### Emergency Business Deployment Plan (System scope)

```
Deployment Plan: "Accelerate fx-system v2.0.1 to production-latam"
├── Change Request: CR-2026-0158 (Emergency-Business, Fast-Track Train)
├── Deployment Scope: System
├── Scope: fx-system v2.0.1 — campaign-critical FX rate display
├── Deployment Train: Fast-Track Train (abbreviated soak)
├── Risk Assessment: Low — feature flag controlled; no schema changes
├── Produced Tasks:
│   ├── Deployment Planning Task: "Create System Deployment Specification sds-2.1 for production-latam"
│   ├── Verification Task: "Business metric validation — campaign feature activation"
│   └── Deployment Task: "Apply sds-2.1 to production-latam"
└── Timeline: Staging (Day 0, 4h soak) → Prod-LATAM (Day 0, evening)
```

---
