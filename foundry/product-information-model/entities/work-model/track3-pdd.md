# Product Deployment Descriptor (PDD)

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** SRE, Release Engineering, DevOps

## Definition

An **environment-specific deployment specification** for a Product Package Version. The PDD composes MDDs by reference, adds product-level cross-module environment configuration, and includes **product-level deployment scripts** for cross-module orchestration, product-wide health verification, and coordinated rollback. The PDD is the highest-order deployment specification — it describes how an entire Product Package Version is deployed as a coordinated unit to a specific environment.

PDD = Product Package Version (by reference) + MDDs (by reference) + Cross-Module Environment Config + Product-level Deployment Scripts.

PDD is the **complete deployment specification** — it orchestrates the deployment of all Module Package Versions (via their MDDs) with product-wide coordination. Where the Product Package Version defines *what* is deployed (environment-independent composition of Module Package Versions), the PDD defines *how* and *where* the full product is deployed (environment-specific orchestration).

PDD has its own version, reflecting **deployment progression** at the product level — changes to cross-module orchestration, deployment ordering, product-wide configuration, or MDD composition — independent of Product Version (functional) and Product Package Version (operator-facing systems).

> **PDD is not Product Package Version.** Product Package Version is an environment-independent artifact that enriches Product Version with Module Package Versions and cross-module operational wiring. PDD is an environment-specific specification that describes how to deploy that Product Package Version to a specific environment with cross-module coordination. See DR-028, DR-029.

## Fields

| Field | Type | Description |
|---|---|---|
| Product Package Version | Reference (Track 3) | The Product Package Version this descriptor deploys |
| Target Environment | Reference (Dim 7) | The Deployment Environment this descriptor targets |
| PDD Version | String | Deployment progression version (e.g., `pdd-1.0`, `pdd-2.0`) — independent of Product Version and Product Package Version |
| MDDs | List of References (Track 3) | MDD versions composed by reference — one per Module Package Version in the Product Package Version |
| Cross-Module Environment Config | Structured Config | Product-wide environment-specific configuration: cross-module monitoring dashboards, product-level alerting rules, cross-module scaling coordination, product-level health aggregation thresholds |
| Deployment Ordering | Ordered List | Module deployment sequence with dependencies (e.g., deploy Compliance MDD before Payments MDD) |
| Product-level Deployment Scripts | List | Scripts/applications for cross-module coordination: product-wide health verification, cross-module integration smoke tests, coordinated rollback |
| Last Updated | DateTime | When this PDD version was created or modified |

## Statuses

| Status | Description |
|---|---|
| Draft | PDD is being authored; MDDs being composed; scripts under development |
| Ready | All MDDs referenced; cross-module configuration complete; scripts validated |
| Approved | PDD has passed change management review and is cleared for deployment |
| Active | PDD is the current deployment specification for this Product Package Version in this environment |
| Superseded | A newer PDD version has replaced this one |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Specifies deployment of | Product Package Version (Track 3) | PDD specifies how a Product Package Version is deployed to a specific environment |
| Composes | MDD(s) (Track 3) | PDD composes MDDs by reference for all Module Package Versions within the Product Package Version |
| Targets | Deployment Environment (Dim 7) | PDD targets a specific environment |
| Applied by | Deployment Task (Track 3) | PDD version is applied to an environment by a Deployment Task (complete level) |
| Produced by | Deployment Planning Task (Track 3) | Deployment Planning Task creates/updates PDD versions |
| Enables | Customer Release (Dim 1) | Successful PDD deployment enables Customer Release activation |

## Examples

### PDD for Product v3.2.0 in production-latam

```
PDD: Product Package Version v3.2.0 → production-latam (pdd-1.0)
├── Product Package Version: Product Package Version v3.2.0
├── Target Environment: production-latam
├── MDDs (by reference):
│   ├── Payments Module Package Version v2.3.0 → production-latam (mdd-3.1)
│   ├── FX Module Package Version v1.8.0 → production-latam (mdd-2.0)
│   └── Compliance Module Package Version v3.1.0 → production-latam (mdd-1.2)
├── Deployment Ordering:
│   ├── 1. Compliance MDD (regulatory dependency — must be ready first)
│   ├── 2. FX MDD (rate provider — Payments depends on FX rates)
│   └── 3. Payments MDD (depends on Compliance and FX)
├── Cross-Module Environment Config:
│   ├── Product-wide health dashboard: aggregates all Module health signals
│   ├── Cross-module alerting: end-to-end payout latency threshold = 500ms
│   └── Product-level scaling coordination: FX scaling triggers Payments scaling review
└── Product-level Deployment Scripts:
    ├── 001-pre-deploy-cross-module-check.sh (verify all Module MDDs are Approved)
    ├── 002-post-deploy-e2e-smoke-test.py (end-to-end payout: payment → FX → compliance → settlement)
    └── 003-coordinated-rollback.sh (rollback all Modules in reverse order if e2e fails)
```

---
