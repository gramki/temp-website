# Change Request

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** DevOps, SRE, Release Engineering, Change Advisory Board (CAB)

## Definition

A formal change management envelope governing deployment-related changes to production environments, scoped to a Deployment Train (Dim 7) or a specific Station within a train. A Change Request captures the justification, approval workflow, and completion criteria for a set of deployment-related work — it is the **auditable container** within which Deployment Plans, Deployment Tasks, and Verification Tasks execute.

A Change Request is **successfully completed** when all Deployment Tasks AND all Verification Tasks associated with it have passed. This completion model ensures that deployments are not considered "done" until they are both executed and verified.

Change Requests govern **deployment-related changes only**. Maintenance Tasks (routine preventative work) may go through their own change processes but are not governed by Change Requests. The scoping of Change Requests to deployment-related changes ensures they serve their primary purpose: providing the auditable, approval-gated envelope for code and configuration changes to production environments.

> **Three Change Request types.** Standard changes follow the normal promotion path through a Deployment Train. Emergency-Technical changes arise from Incidents (SEV-0/SEV-1 → emergency fix → immediate deployment), bypassing normal cadences with documented waivers. Emergency-Business changes arise from business exigencies (e.g., campaign deadlines, festival-day feature rollouts), fast-tracking through a compressed train or abbreviated soak times with explicit ODR justification. See DR-029 D11.
>
> **Scoping to Train or Station.** A Change Request scoped to a Train means the change will progress through the full promotion path. A Change Request scoped to a specific Station means the change targets only that station's environment — useful for environment-specific fixes, targeted rollbacks, or station-level hotfixes. Transitively, scoping to a station implies scoping to a package or deployment descriptor at that station.

## Purpose

Captures planned deployment changes that carry risk and need controlled execution. Change Requests ensure production stability through formal change management. In regulated fintech:
- Audit trails for deployment changes are a compliance requirement (PCI-DSS, SOC 2)
- Change Advisory Board (CAB) approval is required for production changes
- Deployment governance must be documented and traceable
- Commercial contracts may require demonstrable change management processes

Without Change Requests:
- Deployments have no formal approval envelope
- The relationship between "what was approved" and "what was deployed" is informal
- Audit trails for "who approved this change?" have no anchor entity
- Emergency changes cannot be distinguished from standard changes in the model

## Fields

| Field | Type | Description |
|---|---|---|
| Type | Enum | `Standard` / `Emergency-Technical` / `Emergency-Business` |
| Scope | Reference (Dim 7) | Deployment Train or specific Station this change request targets |
| Requestor | String | Person or team requesting the change |
| Justification | Text | Why this change is needed (may reference Customer Release, Incident, business exigency) |
| Impact Assessment | Text | Blast radius, affected tenants, affected services, risk level |
| CAB Decision | Text | Change Advisory Board decision and rationale (if applicable) |
| Completion Criteria | Text | What must be true for this CR to be considered complete (all Deployment Tasks + Verification Tasks succeed) |
| Customer Release | Reference (Dim 1) | Customer Release this change supports (if applicable) |
| Emergency Justification | Text | For Emergency types: why normal process is being bypassed; documented waiver; ODR reference |

## Statuses

| Status | Description |
|---|---|
| Submitted | Change Request has been submitted for review |
| Approved | Change Request has been approved (CAB or automated approval based on governance level) |
| In Progress | Deployment Plan is executing — Deployment Tasks and Verification Tasks are in progress |
| Complete | All Deployment Tasks succeeded AND all Verification Tasks passed |
| Rejected | Change Request was rejected by CAB or approving authority |
| Cancelled | Change Request was withdrawn before completion |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scoped to | Deployment Train (Dim 7) | Change Request follows a Deployment Train's promotion path |
| Scoped to | Station (Dim 7) | Change Request may be scoped to a specific Station within a Train |
| Contains | Deployment Plan(s) (Track 3) | Change Request contains the Deployment Plan(s) that scope the rollout |
| Contains | Verification Task(s) (Track 3) | Change Request contains Verification Tasks (created by planning or added independently) |
| May reference | Customer Release (Dim 1) | Change Request may support a Customer Release's deployment needs |
| May originate from | Incident (Track 3, artifact) | Emergency-Technical changes may originate from an Incident; triggered via Incident Response Task |
| May originate from | Release Planning Task (Track 2) | Emergency-Business changes may originate from accelerated Release Plans |
| Respects | Deployment Environment Change Cycle (Dim 7) | Change Request timing respects the target environment's change windows and freeze periods |

## Examples

### Standard Change Request

```
Change Request: CR-2026-0142
├── Type: Standard
├── Scope: PCI Regulated Train (full promotion path)
├── Requestor: Release Engineering
├── Justification: "Deploy Payments Module Package Version v2.3.0 — includes FX rate-lock feature for LATAM Expansion Customer Release"
├── Customer Release: "LATAM Expansion"
├── Impact Assessment: "Medium risk — DB migration in pre-rollout; 3 production environments; affects all Payments tenants"
├── CAB Decision: "Approved — drill required before production deployment"
├── Completion Criteria: "All Deployment Tasks (staging, prod-us, prod-latam) + all Verification Tasks (SLA, compliance) pass"
├── Contains:
│   ├── Deployment Plan: "Deploy Payments Module Package Version v2.3.0 to Production"
│   ├── Verification Task: "Post-deployment SLA verification — production-us"
│   └── Verification Task: "LATAM compliance audit — production-latam"
└── Status: In Progress
```

### Emergency-Business Change Request

```
Change Request: CR-2026-0158
├── Type: Emergency-Business
├── Scope: Fast-Track Train (abbreviated promotion)
├── Requestor: Product Management
├── Justification: "LATAM Independence Day campaign requires FX rate display feature by Sept 7 — Release Plan acceleration"
├── Emergency Justification: "Business exigency — campaign budget committed; 72h soak waived to 4h with VP approval; ODR-015 documents waiver"
├── Customer Release: "LATAM Campaign Q3"
├── Impact Assessment: "Low risk — feature flag controlled; no schema changes; single module"
├── Status: Approved
```

---
