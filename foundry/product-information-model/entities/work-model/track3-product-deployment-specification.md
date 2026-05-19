# Product Deployment Specification

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** SRE, Release Engineering, DevOps

## Definition

An **environment-specific deployment specification** for a Product Version. The Product Deployment Specification references a Product Version and composes System Deployment Specifications for all constituent Systems. It adds product-level deployment coordination: deployment ordering across Systems, cross-System environment configuration, end-to-end smoke tests, and coordinated rollback procedures.

Product Deployment Specification = Product Version + System Deployment Specifications (by reference) + Cross-System Environment Config + Product-level Deployment Scripts.

Replaces the former **Product Deployment Descriptor (PDD)**. See DR-036 D6.

> **Product Deployment Specification is not Product Version.** Product Version is environment-independent — a certified BOM of System Versions. Product Deployment Specification is environment-specific — it describes how that Product Version is deployed to a specific environment with cross-System orchestration.

> **Independent versioning.** The Product Deployment Specification has its own version stream reflecting **deployment progression** at the product level — orchestration changes, ordering updates, cross-System script changes — independent of Product Version.

## Purpose

Orchestrates full-product deployment to a specific environment. Without Product Deployment Specifications:

- Each System would be deployed independently with no cross-System ordering or coordinated verification
- Product-wide rollouts (Compliance before Payments, FX before Payments) have no structured specification
- End-to-end smoke tests and coordinated rollback have no versioned home
- Change Requests scoped to "full product release" lack a single deployable specification to reference

## Fields

| Field | Type | Description |
|---|---|---|
| Product Version | Reference (Track 2) | The Product Version this specification deploys |
| Target Environment | Reference (Dim 7) | The Deployment Environment this specification targets |
| Specification Version | String | Deployment progression version (e.g., `pds-1.0`, `pds-2.0`) — independent of Product Version |
| System Deployment Specifications | List of References (Track 3) | System Deployment Specification versions composed by reference — one per System in the Product Version BOM |
| Deployment Ordering | Ordered List | System deployment sequence with dependencies (e.g., deploy compliance-system before payments-system) |
| Cross-System Environment Configuration | Structured Config | Product-wide environment-specific configuration: cross-System monitoring dashboards, product-level alerting rules, cross-System scaling coordination |
| Cross-System Deployment Scripts | List | Scripts/applications for product-level coordination: pre-rollout health check across all Systems, end-to-end smoke test, coordinated cross-System rollback |
| Last Updated | DateTime | When this specification version was created or modified |

## Statuses

| Status | Description |
|---|---|
| Draft | Specification is being authored; System Deployment Specifications being composed; scripts under development |
| Ready | All System Deployment Specifications referenced; cross-System configuration complete; scripts validated |
| Active | Current deployment specification for this Product Version in this environment |
| Superseded | A newer specification version has replaced this one |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Specifies deployment of | Product Version (Track 2) | References a certified Product Version |
| Composes | System Deployment Specification(s) (Track 3) | Composes System Deployment Specifications by reference for all Systems in the Product Version |
| Targets | Deployment Environment (Dim 7) | Targets a specific environment |
| Applied by | Deployment Task (Track 3) | Applied to an environment by a Deployment Task (Product-level) |
| Produced by | Deployment Planning Task (Track 3) | Deployment Planning Task creates/updates specification versions |
| Enables | Customer Release (Dim 1) | Successful Product Deployment Specification deployment enables Customer Release activation |

## Example

### Product v4.0.0 → production-latam

```
Product Deployment Specification: Product v4.0.0 → production-latam (pds-1.0)
├── Product Version: Product v4.0.0
├── Target Environment: production-latam
├── System Deployment Specifications (by reference):
│   ├── compliance-system v3.2.0 → production-latam (sds-1.0)
│   ├── fx-system v2.0.1 → production-latam (sds-1.1)
│   ├── payments-system v3.1.0 → production-latam (sds-1.2)
│   ├── bank-connectivity-system v1.6.0 → production-latam (sds-1.0)
│   ├── customer-portal-system v2.1.0 → production-latam (sds-1.0)
│   └── payments-monitoring-system v1.2.0 → production-latam (sds-1.0)
├── Deployment Ordering:
│   ├── 1. compliance-system (regulatory dependency — must be ready first)
│   ├── 2. fx-system (rate provider — Payments depends on FX rates)
│   ├── 3. bank-connectivity-system
│   ├── 4. payments-system (depends on Compliance, FX, Bank Connectivity)
│   ├── 5. payments-monitoring-system (observability after core Systems)
│   └── 6. customer-portal-system
├── Cross-System Environment Configuration:
│   ├── Product-wide health dashboard: aggregates all System health signals
│   ├── Cross-System alerting: end-to-end payout latency threshold = 500ms
│   └── Product-level scaling coordination: FX scaling triggers Payments scaling review
└── Cross-System Deployment Scripts:
    ├── 001-pre-deploy-all-systems-check.sh (verify all System Deployment Specifications are Ready)
    ├── 002-post-deploy-e2e-smoke-test.py (end-to-end payout: portal → payment → FX → compliance → settlement)
    └── 003-coordinated-rollback.sh (rollback all Systems in reverse order if e2e fails)
```

---
