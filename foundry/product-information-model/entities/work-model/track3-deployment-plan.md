# Deployment Plan

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** SRE, DevOps, Release Engineering

## Definition

A deliberation activity where the Run team scopes a rollout — determining which packages and descriptors advance through which Deployment Trains and Stations, identifying verification and maintenance prerequisites, assessing risks, and producing the Deployment Planning Tasks that create the actual deployment descriptors. The Deployment Plan is the Run Track's equivalent of the Build Track's Release Planning Task: it scopes and organizes the deployment work without directly executing it.

Deployment Planning is a **deliberation activity** — the team learns as it plans. New information discovered during planning (infrastructure gaps, missing operational readiness, required maintenance) feeds back into the plan, producing additional tasks and updating operating artifacts. Every task produced by a Deployment Plan can produce or update work artifacts in the Run Track.

A Deployment Plan is governed by a Change Request, which provides the change management envelope with audit trail, approvals, and scoping to a Deployment Train or Station.

> **Deployment Plan encapsulates Deployment Planning Tasks.** The Deployment Plan is the upstream deliberation that scopes what needs to be deployed, where, and how. Deployment Planning Tasks are the leaf-level work items that produce the actual deployment descriptors (SDD/MDD/PDD), verification tasks, and maintenance tasks. A single Deployment Plan may produce multiple Deployment Planning Tasks — one per descriptor or composition level. See DR-029 D9.

## Purpose

Makes deployment scoping and deliberation explicit in the Run Track. Without Deployment Plans:
- Deployment Planning Tasks exist in isolation — there's no parent entity that scopes the overall rollout
- Risk assessment, promotion path selection, and verification planning have no structured deliberation entity
- The relationship between a Change Request (change management) and the actual deployment work is unstructured
- Deployment Drill Tasks have no parent scope — a drill is most valuable when it rehearses the entire orchestrated rollout, not individual descriptor applications

## Fields

| Field | Type | Description |
|---|---|---|
| Change Request | Reference (Track 3) | The Change Request this plan fulfills |
| Scope | Text | What is being deployed: Train/Station/Package/Descriptor level description |
| Deployment Train | Reference (Dim 7) | The Deployment Train this plan follows (may be derived from Change Request scope) |
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
| Governed by | Change Request (Track 3) | Deployment Plan is governed by a Change Request |
| Follows | Deployment Train (Dim 7) | Deployment Plan follows a Deployment Train's promotion path |
| Produces | Deployment Planning Task(s) (Track 3) | Planning produces leaf-level tasks that create descriptors |
| May produce | Deployment Drill Task (Track 3) | Planning may produce an optional rehearsal task |
| May produce | Verification Task(s) (Track 3) | Planning produces verification tasks for post-deployment validation |
| May produce | Maintenance Task(s) (Track 3) | Planning may discover maintenance prerequisites |
| Contains | Deployment Task(s) (Track 3) | Deployment Tasks execute within the scope of this plan |
| Informed by | Operational Readiness (Dim 7) | Planning considers environment readiness status |

## Examples

### Standard Deployment Plan

```
Deployment Plan: "Deploy Payments Module Package v2.3.0 to Production"
├── Change Request: CR-2026-0142 (Standard, PCI Regulated Train)
├── Scope: Payments Module Package v2.3.0 through PCI Regulated Train
├── Deployment Train: PCI Regulated Train
├── Risk Assessment: Medium — DB migration in pre-rollout script; rollback requires migration reversal
├── Produced Tasks:
│   ├── Deployment Planning Task: "Create MDD v3.1 for staging" → produces MDD v3.1
│   ├── Deployment Planning Task: "Create MDD v3.2 for production-us" → produces MDD v3.2
│   ├── Deployment Planning Task: "Create MDD v3.3 for production-latam" → produces MDD v3.3
│   ├── Verification Task: "Post-deployment SLA verification — staging"
│   ├── Verification Task: "Post-deployment SLA verification — production-us"
│   ├── Verification Task: "Post-deployment compliance audit — production-latam"
│   ├── Maintenance Task: "Rotate payment-gateway API keys before deployment"
│   └── Deployment Drill Task: "Rehearse MDD v3.1 application in staging-drill environment"
└── Timeline: Staging (Day 1) → Prod-US (Day 4) → Prod-LATAM (Day 11)
```

### Emergency Business Deployment Plan

```
Deployment Plan: "Accelerate LATAM Campaign Feature Rollout"
├── Change Request: CR-2026-0158 (Emergency-Business, Fast-Track Train)
├── Scope: FX Module Package v1.9.0 — campaign-critical FX rate display feature
├── Deployment Train: Fast-Track Train (abbreviated soak)
├── Risk Assessment: Low — feature flag controlled; no schema changes
├── Produced Tasks:
│   ├── Deployment Planning Task: "Create MDD v2.1 for production-latam" → produces MDD v2.1
│   ├── Verification Task: "Business metric validation — campaign feature activation"
│   └── Deployment Task: "Apply MDD v2.1 to production-latam"
└── Timeline: Staging (Day 0, 4h soak) → Prod-LATAM (Day 0, evening)
```

---
