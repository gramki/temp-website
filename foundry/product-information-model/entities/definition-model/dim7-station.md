# Station

**Model:** Definition Model
**Dimension:** Operational
**Owner:** Platform Engineering, Release Engineering

## Definition

A checkpoint within a Deployment Train (Operational), targeting a specific Deployment Environment with defined entry criteria, exit/promotion criteria, and approval requirements. Stations make the promotion path auditable and contractually enforceable — each station transition produces evidence that the deployment met the required quality, compliance, and safety bars before advancing.

A Station is not the same as a Deployment Environment. A Deployment Environment is an infrastructure target (where things run). A Station is a **governance checkpoint** in a promotion path (what must be true before code can enter or leave this environment). The same Deployment Environment may be a Station in multiple Deployment Trains with different entry/exit criteria.

## Purpose

Captures the governance and quality gates at each step of a Deployment Train. Without Stations:
- Promotion criteria are implicit — "staging must pass before production" has no formal entry/exit criteria
- Approval requirements at each stage are undocumented
- Soak time and stabilization windows are tribal knowledge
- Audit trails for deployment progression through environments have no structured anchor
- The same environment used in different trains (e.g., staging used by both PCI Regulated Train and Fast-Track Train) cannot have different governance requirements per train

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Station name (e.g., "Staging Gate," "Production US-East Gate," "LATAM Regulatory Gate") |
| Deployment Environment | Reference (Operational) | The target Deployment Environment for this station |
| Sequence Position | Integer | Position in the Deployment Train's ordered list (1-based) |
| Entry Criteria | Text | What must be true before a deployment can enter this station (e.g., "previous station soak complete," "all integration tests pass") |
| Exit / Promotion Criteria | Text | What must be verified before promotion to the next station (e.g., "72-hour soak with zero SEV-1 incidents," "canary metrics within SLO thresholds") |
| Approval Requirements | Text | Who must approve promotion from this station (e.g., "automated," "CAB approval," "LATAM compliance officer sign-off") |
| Soak Time | Duration | Minimum stabilization window before promotion (e.g., "72 hours," "1 week," "none") |
| Verification Requirements | Text | What verification tasks must pass at this station (e.g., "smoke tests," "integration tests," "SLA verification," "compliance audit") |

## Statuses

| Status | Description |
|---|---|
| Active | Station is operational within its Deployment Train |
| Bypassed | Station is temporarily bypassed (documented waiver for emergency changes) |
| Retired | Station has been removed from its Deployment Train |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | Deployment Train (Operational) | Station is a checkpoint within a Deployment Train |
| Targets | Deployment Environment (Operational) | Station targets a specific Deployment Environment |
| Scoped by | Change Request(s) (Run) | Change Requests may be scoped to a specific Station |
| Verified by | Verification Task(s) (Run) | Verification Tasks at this station validate deployment quality |

## Examples

### Staging Gate (PCI Regulated Train, Position 2)

```
Station: Staging Gate
├── Deployment Environment: Staging EU-West
├── Sequence Position: 2
├── Entry Criteria:
│   ├── Previous station (Development) CI pass
│   └── All unit and integration tests green
├── Exit / Promotion Criteria:
│   ├── 72-hour soak with zero SEV-1 incidents
│   ├── Integration test suite pass rate ≥ 99%
│   ├── Security scan: no critical/high vulnerabilities
│   └── Performance regression: P95 latency within 10% of baseline
├── Approval Requirements: Automated (all criteria met)
├── Soak Time: 72 hours
└── Verification Requirements: Smoke tests, integration tests, security scan, performance benchmark
```

### Production LATAM Gate (PCI Regulated Train, Position 4)

```
Station: Production LATAM Gate
├── Deployment Environment: Production LATAM
├── Sequence Position: 4
├── Entry Criteria:
│   ├── Production US-East soak complete (minimum 1 week)
│   ├── LATAM regulatory change window open
│   └── LATAM compliance officer sign-off
├── Exit / Promotion Criteria:
│   ├── Canary metrics within SLO thresholds at 5%, 25%, 100%
│   ├── LATAM-specific compliance checks pass (LGPD data residency, Central Bank reporting)
│   └── Zero SEV-1/SEV-2 incidents during canary progression
├── Approval Requirements: CAB approval + LATAM compliance officer sign-off
├── Soak Time: 1 week at 100% traffic
└── Verification Requirements: Smoke tests, LATAM compliance audit, SLA verification, business metric validation
```

---
