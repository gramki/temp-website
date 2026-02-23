# Product Package

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** SRE, DevOps, Release Engineering

## Definition

The **highest-order deployable** — combining a Product Version (Build Track artifact) with Module Packages (Run Track artifacts) and cross-module operational wiring. Product Package is the Run Track's counterpart to the Build Track's Product Version. Where Product Version certifies that Module Versions compose correctly (build-time concern), Product Package ensures the full product composition is **operationally complete** across all Modules (run-time concern): cross-module monitoring, product-wide scaling policies, cross-module operational automation.

Product Package = Product Version + Module Packages + Cross-Module Operational Wiring.

Product Package is the **complete deployment unit** — it represents the entirety of what is deployed for a full product release to a target environment. It operates at the Complete composition level.

> **Product Package is NOT Product Version.** Product Version is a Build Track artifact — it certifies composition integrity across Module Versions. Product Package is a Run Track artifact — it enriches Product Version with operationally complete Module Packages and cross-module operational wiring. See DR-027.

## Purpose

Bridges the gap between the Build Track's certified Product Version and the Run Track's operationally complete deployment. Without Product Package:
- Cross-module operational concerns (product-wide scaling, cross-module monitoring dashboards, cross-module automation) have no composition entity
- The relationship between Module Packages at the product level is invisible — each Module Package is deployed independently with no product-wide coordination artifact
- "What is deployed for Product v3.2 in production-latam?" requires reconstructing from individual Module Package deployments

## Fields

| Field | Type | Description |
|---|---|---|
| Product Version | Reference (Track 2) | The Build Track's certified Product Version this Package enriches |
| Module Packages | Map | Module Packages included, each enriching a Module Version from the Product Version's BOM (e.g., `{Payments: Module Package v2.3.0-latam, FX: Module Package v1.8.0-latam}`) |
| Cross-Module Operational Wiring | Structured Config | Product-wide operational configuration: cross-module monitoring dashboards, product-wide alerting rules, cross-module scaling coordination, product-level health aggregation |
| Target Environment(s) | List of References (Dim 7) | Which Deployment Environment(s) this Package targets |
| Assembly Date | DateTime | When the Product Package was assembled |

## Statuses

| Status | Description |
|---|---|
| Assembling | Module Packages being composed and cross-module operational wiring being configured |
| Ready | All Module Packages ready; cross-module operational wiring validated; ready for deployment |
| Deployed | Product Package has been deployed to at least one target environment |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Enriches | Product Version (Track 2) | Product Package enriches a certified Product Version with operational completeness |
| Composes | Module Package(s) (Track 3) | Product Package composes Module Packages |
| Deployed by | Deployment (Track 3) | Product Package is deployed to environments by the Run Track |
| Targets | Deployment Environment(s) (Dim 7) | Product Package targets specific environments |
| Referenced by | Customer Release (Dim 1) | Customer Releases may reference Product Packages for deployment tracking |

## Examples

### Product Package for Product v3.2.0 — Production LATAM

```
Product Package: Product v3.2.0 → Production LATAM
├── [From Product Version v3.2.0 — Build Track]
│   ├── Declared BOM: {Payments ^2.3.0, FX ~1.8.0, Compliance >=3.1.0 <4.0.0}
│   └── Resolved BOM: {Payments v2.3.0, FX v1.8.0, Compliance v3.1.0}
├── [Module Packages — Run Track]
│   ├── Payments Module Package v2.3.0-latam
│   │   ├── payments-service v2.3.3 + payment-gateway v1.2.1
│   │   ├── payments-healthcheck v1.2.0
│   │   └── payment-reconciler v2.1.0
│   ├── FX Module Package v1.8.0-latam
│   │   ├── fx-service v1.8.1 + fx-calculator v1.8.0
│   │   └── fx-rate-monitor v1.0.0
│   └── Compliance Module Package v3.1.0-latam
│       ├── compliance-service v3.1.1
│       └── compliance-audit-reporter v1.0.0
└── [Cross-Module Operational Wiring]
    ├── Product-wide health dashboard: aggregates all Module Package health signals
    ├── Cross-module alerting: end-to-end payout latency (payments → fx → compliance → settlement)
    └── Product-level scaling coordination: FX scaling triggers Payments scaling

Target Environment: production-latam
Assembly Date: 2026-02-13T08:00:00Z
```

---
