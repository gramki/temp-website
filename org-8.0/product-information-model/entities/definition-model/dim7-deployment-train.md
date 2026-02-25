# Deployment Train

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** Platform Engineering, Release Engineering, DevOps Leadership

## Definition

A reusable promotion path defining the ordered sequence of environments through which deployments progress, carrying contractual and governance significance. A Deployment Train represents both a **technical promotion workflow** (code progresses from development through staging to production) and a **contractual commitment** (tenants and commercial partners can rely on the promotion path for planning changes to their dependent applications and processes).

Deployment Trains enable certain operating models while rejecting non-compliant ones. A regulated fintech train may require multi-environment soak periods, CAB approvals at each station, and documented verification — enforcing safety and compliance assurances. A fast-track train for non-critical services may allow abbreviated soak times and automated approvals. The train is not overly prescriptive but provides a reasonably flexible construct that the Operating Model can configure.

> **Contractual significance.** Tenants may rely on the Deployment Train to plan changes to their own dependent applications and processes. When code reaches a staging station, tenant integration teams can begin testing their dependent workflows against the upcoming changes. The promotion path is not just an internal process — it is externally visible to commercial partners who need assurance that what they test is what reaches their production tenant. Commercial contracts may reference Deployment Trains for safety and compliance guarantees. See DR-029 D3.
>
> **Tenant relationship is derived.** Tenants do not directly subscribe to Deployment Trains. Instead, a Tenant is provisioned in a Deployment Environment (Track 3), and that environment is targeted by a Station within a Train. The Tenant's visibility into the Train is derived from this environment relationship. Whether tenants are notified of change requests and their updates is an Operating Model decision. See DR-029 D13.

## Purpose

Captures the strategic deployment promotion decisions that govern how changes move through environments. Without Deployment Trains:
- Promotion paths are implicit — "we deploy to staging before production" is tribal knowledge, not a structured entity
- Contractual commitments about deployment safety cannot be formally represented
- Change Requests have no promotion path to scope against — "deploy to production" has no structured sequence of verifications
- Emergency changes cannot be modeled as fast-tracking through a compressed train — there's no train to fast-track through
- Compliance and audit requirements for deployment governance have no anchor entity

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Train name (e.g., "PCI Regulated Train," "Fast-Track Train," "LATAM Production Train") |
| Stations | Ordered List of References (Dim 7) | The ordered sequence of Stations that compose this train |
| Governance Level | Enum | `Standard` / `Regulated` / `Critical` — determines approval requirements, soak times, and documentation thresholds |
| Contractual Commitments | Text | Commitments made to tenants and partners about this promotion path (e.g., "all production deployments traverse staging with minimum 72-hour soak") |
| Allowed Change Types | List | Which Change Request types (Standard, Emergency-Technical, Emergency-Business) are permitted on this train |
| Description | Text | Purpose and scope of this train — which modules, services, or change categories use it |

## Statuses

| Status | Description |
|---|---|
| Draft | Train is being designed; stations and governance are not yet finalized |
| Active | Train is the current promotion path for its scoped changes |
| Suspended | Train is temporarily not accepting changes (e.g., regulatory freeze, major restructuring) |
| Retired | Train has been decommissioned and replaced |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Contains | Station(s) (Dim 7) | The ordered sequence of checkpoints in this train |
| Scoped by | Change Request(s) (Track 3) | Change Requests are scoped to this train (or to a specific Station within it) |
| Referenced by | Customer Release (Dim 1) | A Customer Release may span multiple Deployment Trains |
| Derived visibility | Tenant(s) (Track 3) | Tenants derive visibility into this train via their Deployment Environment |
| Justified by | ODR (Dim 7) | Operational decisions justify train design choices |
| Constrained by | Operational Constraint (Dim 7) | Constraints may mandate certain governance levels or station requirements |

## Examples

### PCI Regulated Train

```
Deployment Train: PCI Regulated Train
├── Governance Level: Regulated
├── Contractual Commitments:
│   ├── "All production deployments traverse staging with minimum 72-hour soak"
│   ├── "CAB approval required at production stations"
│   └── "PCI audit trail maintained for all station transitions"
├── Allowed Change Types: Standard, Emergency-Technical
├── Stations (ordered):
│   1. Development → (auto-promote on CI pass)
│   2. Staging EU-West → (72h soak, integration tests, security scan)
│   3. Production US-East → (CAB approval, canary 5%→25%→100% over 48h)
│   4. Production LATAM → (CAB approval, LATAM regulatory window, canary 5%→25%→100% over 72h)
└── Scope: All payment-processing modules (Payments, FX, Compliance)
```

### Fast-Track Train

```
Deployment Train: Fast-Track Train
├── Governance Level: Standard
├── Contractual Commitments: "Best-effort staging soak; no minimum soak time"
├── Allowed Change Types: Standard, Emergency-Technical, Emergency-Business
├── Stations (ordered):
│   1. Development → (auto-promote on CI pass)
│   2. Staging EU-West → (automated tests, no minimum soak)
│   3. Production US-East → (automated approval, rolling deployment)
└── Scope: Non-PCI modules (Marketing Portal, Developer Portal, internal tooling)
```

---
