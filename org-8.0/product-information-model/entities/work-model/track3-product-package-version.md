# Product Package Version

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** SRE, DevOps, Release Engineering

## Definition

The **highest-order environment-independent deployable** — a versioned instance that instantiates a Product Package specification (Dim 7), combining a specific Product Version (Build Track artifact) with specific Module Package Versions (Run Track artifacts) and cross-module operational wiring. Product Package Version is the Run Track's counterpart to the Build Track's Product Version. Where Product Version certifies that Module Versions compose correctly (build-time concern), Product Package Version adds the **cross-module operator-facing layer** (run-time concern): cross-module monitoring, product-wide operational automation dashboards, cross-module alerting topology.

Product Package Version = Product Version + Module Package Versions + Cross-Module Operational Wiring.

Product Package Version is **environment-independent** — it defines *what* is deployed at the product level, not *where* or *how*. Environment-specific configuration (cross-module monitoring thresholds, product-wide scaling coordination, deployment ordering, deployment scripts) is specified by the Product Deployment Descriptor (PDD), which references the Product Package Version and targets a specific Deployment Environment.

> **Specification vs. Version.** The Product Package (Dim 7, Definition Model) is the **specification** — the composition template. The Product Package Version (Track 3, Work Model) is the **versioned instance**. See DR-029 D1, D2.
>
> **Product Package Version is NOT Product Version.** Product Version is a Build Track artifact — it certifies composition integrity across Module Versions. Product Package Version is a Run Track artifact — it adds cross-module operator-facing systems (monitoring aggregation, product-wide alerting, cross-module dashboards) and operational wiring to Module Package Versions. See DR-027, DR-029.
>
> **Environment-specific deployment details belong to the PDD.** Product Package Version defines the composition; the PDD specifies how that composition is deployed to a specific environment. See DR-028.

## Purpose

Bridges the gap between the Build Track's certified Product Version and the Run Track's operationally observable and maintainable deployment. Without Product Package Versions:
- Cross-module operational concerns (product-wide monitoring, cross-module automation) have no composition entity
- The relationship between Module Package Versions at the product level is invisible — each Module Package Version is deployed independently with no product-wide coordination artifact
- "What is deployed for Product v3.2?" requires reconstructing from individual Module Package Version deployments

## Fields

| Field | Type | Description |
|---|---|---|
| Product Package | Reference (Dim 7) | The Product Package specification this version instantiates |
| Product Version | Reference (Track 2) | The Build Track's certified Product Version this version enriches |
| Module Package Versions | Map | Module Package Versions included, each enriching a Module Version from the Product Version's BOM (e.g., `{Payments: Module Package Version v2.3.0, FX: Module Package Version v1.8.0}`) |
| Cross-Module Operational Wiring | Structured Config | Product-wide operational wiring: cross-module health aggregation, cross-module alerting topology, cross-module scaling dependencies, product-level automation |
| Assembly Date | DateTime | When the Product Package Version was assembled |

## Statuses

| Status | Description |
|---|---|
| Assembling | Module Package Versions being composed and cross-module operational wiring being configured |
| Ready | All Module Package Versions ready; cross-module operational wiring validated; ready for PDD creation and deployment |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Instantiates | Product Package (Dim 7) | Product Package Version instantiates a Product Package specification |
| Enriches | Product Version (Track 2) | Product Package Version adds cross-module operator-facing systems and wiring to a certified Product Version |
| Composes | Module Package Version(s) (Track 3) | Product Package Version composes Module Package Versions |
| Described by | PDD (Track 3) | Product Package Version is described by one or more PDDs for environment-specific deployment |
| Referenced by | Customer Release (Dim 1) | Customer Releases may reference Product Package Versions for deployment tracking |

## Examples

### Product Package Version for Product v3.2.0 (environment-independent)

```
Product Package Version: Product v3.2.0
├── Instantiates: Core Payment Gateway Product Package specification (Dim 7)
├── [From Product Version v3.2.0 — Build Track]
│   ├── Declared BOM: {Payments ^2.3.0, FX ~1.8.0, Compliance >=3.1.0 <4.0.0}
│   └── Resolved BOM: {Payments v2.3.0, FX v1.8.0, Compliance v3.1.0}
├── [Module Package Versions — Run Track]
│   ├── Payments Module Package Version v2.3.0
│   ├── FX Module Package Version v1.8.0
│   └── Compliance Module Package Version v3.1.0
└── [Cross-Module Operational Wiring]
    ├── Health aggregation: product-level health = f(Payments health, FX health, Compliance health)
    ├── Alerting topology: Payments alerts escalate through FX if FX-dependent
    └── Scaling dependency: FX scaling change triggers Payments scaling review

Assembly Date: 2026-02-13T08:00:00Z

→ Deployed via PDD to production-latam (pdd-1.0), production-us (pdd-2.1), staging (pdd-1.5)
```

---
