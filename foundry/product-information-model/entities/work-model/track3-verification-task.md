# Verification Task

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** SRE, QA, DevOps

## Definition

Post-deployment verification work — structured, trackable, auditable work to confirm that a deployment meets its acceptance criteria. Verification Tasks validate that the deployed descriptor produces the expected operational behavior: services are healthy, SLAs are met, compliance checks pass, and business metrics are within thresholds.

Verification Tasks are created in two ways:
1. **During Deployment Planning** — Deployment Planning Tasks produce Verification Tasks as part of the plan, specifying what must be verified after each deployment.
2. **Independently** — Verification Tasks can be added directly to a Change Request at any time, including after deployment has begun, as new verification needs are discovered.

A Change Request is **successfully completed** only when all Deployment Tasks AND all Verification Tasks associated with it have passed.

> **Why standalone, not a subtype?** Verification Tasks are distinct from Maintenance Tasks (recurring/preventative), Run Track Technical Tasks (serve Run Stories), and Deployment Tasks (apply descriptors). They are post-deployment validation work with pass/fail outcomes and evidence production. Making them standalone ensures they are auditable, trackable, and have clear completion criteria — critical for regulated fintech where post-deployment verification is a compliance requirement. See DR-029 D8.

## Purpose

Makes post-deployment verification explicit and auditable in the Run Track. Without Verification Tasks:
- Post-deployment verification is a text field on the Deployment entity — not a trackable, assignable work item
- Change Request completion cannot formally require verification to pass
- Audit trails for "was the deployment verified?" are informal
- Verification criteria are implicit — what "verified" means for this deployment is not structured

## Fields

| Field | Type | Description |
|---|---|---|
| Deployment Task | Reference (Track 3) | The Deployment Task being verified (may be null if verifying a broader scope) |
| Change Request | Reference (Track 3) | The Change Request this verification belongs to |
| Verification Type | Enum | `Smoke Test` / `Integration Test` / `SLA Verification` / `Compliance Audit` / `Business Metric Validation` / `Security Scan` |
| Verification Criteria | Text | Specific pass/fail criteria (e.g., "P95 latency < 300ms for 24h post-deployment") |
| Evidence | Text | Verification results, logs, metrics, screenshots, or references to evidence artifacts |
| Verifier | String | Person or automation that performed the verification |
| Verified At | DateTime | When verification was completed |

## Statuses

| Status | Description |
|---|---|
| Pending | Verification is defined but the deployment has not yet occurred |
| In Progress | Verification is being executed — metrics being collected, tests being run |
| Passed | Verification criteria met; evidence recorded |
| Failed | Verification criteria not met; may trigger rollback or remediation |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Verifies | Deployment Task (Track 3) | Verification Task validates a specific Deployment Task's outcome |
| Governed by | Change Request (Track 3) | Verification Task completion is required for Change Request closure |
| Governed by | Deployment Plan (Track 3) | Verification Task is produced by and executed within a Deployment Plan |
| Created by | Deployment Planning Task (Track 3) | Deployment Planning produces Verification Tasks as part of the plan |
| Validates at | Station (Dim 7) | Verification at a station validates deployment quality before promotion |

## Examples

### Post-Deployment SLA Verification

```
Verification Task: "SLA Verification — payments-system sds-1.2 → production-latam"
├── Deployment Task: "Apply payments-system System Deployment Specification sds-1.2 to production-latam"
├── Verification Type: SLA Verification
├── Verification Criteria:
│   ├── P95 latency < 300ms for 24h post-deployment
│   ├── Availability ≥ 99.99% for 24h post-deployment
│   ├── Error rate < 0.1% for 24h post-deployment
│   └── Zero SEV-1 incidents during verification window
├── Status: Passed
├── Evidence: "Datadog dashboard link; P95 latency avg 187ms; availability 99.997%; error rate 0.03%"
└── Verified At: 2026-02-14T10:00:00Z
```

### LATAM Compliance Audit Verification

```
Verification Task: "LATAM Compliance Audit — Product Deployment Specification pds-1.2 → production-latam"
├── Deployment Task: "Apply Product Deployment Specification pds-1.2 to production-latam"
├── Verification Type: Compliance Audit
├── Verification Criteria:
│   ├── LGPD data residency: all payment data stored in sa-east-1
│   ├── Central Bank reporting: BRL transaction reports generated correctly
│   └── PCI audit trail: all deployment actions logged with timestamps and actor
├── Status: In Progress
└── Verifier: LATAM Compliance Officer
```

---
