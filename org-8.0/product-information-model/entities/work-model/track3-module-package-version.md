# Module Package Version

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** SRE, DevOps, Platform Engineering

## Definition

A versioned, **environment-independent composition** that instantiates a Module Package specification (Dim 7) — combining a specific Module Version (Build Track artifact) with specific operator-facing System Versions and operational wiring. Module Package Version is the Run Track's complement to the Build Track's Module Version. Where Module Version is a functionally complete, commercially viable assembly of all tenant-serving Systems, Module Package Version adds the **operator-facing support systems** (run-time concern): observability probes, automated maintenance jobs, health checks, reconcilers, dashboards, and log shippers.

Module Package Version = Module Version + Operational System Versions + Binding Configuration (Operational).

Module Package Version is **environment-independent** — it defines *what* is deployed, not *where* or *how*. Environment-specific configuration (resource limits, replica counts, monitoring thresholds, deployment scripts) is specified by the Module Deployment Descriptor (MDD), which references the Module Package Version and targets a specific Deployment Environment. A single Module Package Version may be described by multiple MDDs — one per target environment.

> **Specification vs. Version.** The Module Package (Dim 7, Definition Model) is the **specification** — the composition template that defines which operational systems and wiring enrich a Module. The Module Package Version (Track 3, Work Model) is the **versioned instance** — a specific assembly with specific System Versions at a specific point in time. The specification says "*what* operational systems a Module needs"; the version says "*which specific versions* are assembled." See DR-029 D1, D2.
>
> **Module Package Version is NOT Module Version.** Module Version is a Build Track artifact — a functionally complete assembly of all tenant-serving Systems (product logic, subscription lifecycle, commercialization) with binding configuration. Module Package Version is a Run Track artifact — it adds operator-facing systems (probes, reconcilers, dashboards, log shippers) and operational wiring. The Build Track produces the functionally complete assembly; the Run Track adds the observability and maintenance tooling. See DR-027, DR-029.
>
> **Environment-specific deployment details belong to the MDD.** Module Package Version defines the composition; the MDD specifies how that composition is deployed to a specific environment — resource sizing, scaling policies, monitoring thresholds, deployment scripts, and target environment. See DR-028.

## Purpose

Bridges the gap between the Build Track's functionally complete Module Version and the operator-facing support systems the Run Track builds to observe and maintain that Module in production. Without Module Package Versions:
- Operator-facing systems (probes, reconcilers, dashboards, log shippers) have no composition entity — they exist as loose deployments alongside tenant-serving systems
- The relationship between tenant-serving systems and their operator-facing support systems is invisible in the model
- The Run Track's engineering contribution (building observability and maintenance tooling) is not modeled as producing structured artifacts
- Deployment Planning has to reason about tenant-serving System Versions AND operator-facing System Versions separately, with no composition entity to anchor the conversation

## Fields

| Field | Type | Description |
|---|---|---|
| Module Package | Reference (Dim 7) | The Module Package specification this version instantiates |
| Module Version | Reference (Track 2) | The Build Track's verified Module Version this version enriches |
| Operational System Versions | Map | Operational System Versions included (e.g., `{payments-healthcheck: v1.2.0, payment-reconciler: v2.1.0}`) |
| Binding Configuration (Operational) | Structured Config | Operational wiring: probe-to-system mappings, automation triggers, scheduled job configurations, operational service mesh routes |
| Assembly Date | DateTime | When the Module Package Version was assembled |
| Run Epic | Reference (Track 3) | Run Epic that produced the operator-facing systems (if applicable) |

## Statuses

| Status | Description |
|---|---|
| Assembling | Module Version is being enriched with operational systems and wiring |
| Ready | All operational System Versions included; operational wiring validated; ready for MDD creation and deployment |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Instantiates | Module Package (Dim 7) | Module Package Version instantiates a Module Package specification |
| Enriches | Module Version (Track 2) | Module Package Version adds operator-facing systems and operational wiring to a verified Module Version |
| Includes | Operational System Version(s) | Module Package Version includes operational System Versions (same System Version entity type) built by Run Track engineering |
| Described by | MDD (Track 3) | Module Package Version is described by one or more MDDs for environment-specific deployment |
| Composed into | Product Package Version (Track 3) | Module Package Versions compose a Product Package Version |
| Produced by | Run Epic (Track 3) | Run Epic work produces operational System Versions and wiring for the version |
| Produced by | Run Story(ies) (Track 3) | Run Stories contribute specific operational systems and wiring |

## Examples

### Payments Module Package Version v2.3.0 (environment-independent)

```
Module Package Version: Payments Module Package v2.3.0
├── Instantiates: Payments Module Package specification (Dim 7)
├── [From Module Version v2.3.0 — Build Track]
│   ├── payments-service v2.3.3
│   └── payment-gateway v1.2.1
├── [Operational Systems — Run Track]
│   ├── payments-healthcheck v1.2.0 (synthetic payment probes)
│   └── payment-reconciler v2.1.0 (daily settlement reconciliation)
└── [Binding Configuration (Operational)]
    ├── Probe mapping: payments-healthcheck → payments-service (health endpoint)
    ├── Automation trigger: payment-reconciler → payment-gateway (settlement files)
    └── Service mesh: payments-healthcheck allowed to call payments-service, payment-gateway

Assembly Date: 2026-02-12T10:00:00Z

→ Deployed via MDD to production-latam (mdd-3.1), production-us (mdd-2.4), staging (mdd-1.8)
```

> **Module vs. Package boundary.** Module Version includes all Systems that **serve tenants** — product logic, tenant subscription lifecycle (provisioning, activation, change, upgrade, downgrade, termination), commercialization logic, and integration adapters. Module Package Version adds Systems that **serve operators** — observability probes, dashboards, automated maintenance jobs, health checks, reconcilers, and log shippers. If a System participates in a tenant-facing workflow, it belongs in the Module Version. If it participates only in an operator-facing workflow (monitoring, alerting, maintenance), it belongs in the Module Package Version.

---
