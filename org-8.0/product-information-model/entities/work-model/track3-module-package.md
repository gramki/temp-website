# Module Package

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** SRE, DevOps, Platform Engineering

## Definition

A **deployable composition** enriched by the Run Track — combining a Module Version (Build Track artifact) with operational System Versions and operational configuration to produce what is actually deployed to environments. Module Package is the Run Track's counterpart to the Build Track's Module Version. Where Module Version certifies that product Systems integrate correctly (build-time concern), Module Package ensures the composition is **operationally complete** (run-time concern): probes are attached, automation is wired, environment-specific configuration is applied.

Module Package = Module Version + Operational System Versions + Operational Configuration.

Module Package is the **integrated deployment unit** — it can be deployed to multiple environments (staging, production-us, production-latam) with environment-specific configuration. A single Module Version may produce multiple Module Packages (one per target environment set, or a single package with environment-specific overlays).

> **Module Package is NOT Module Version.** Module Version is a Build Track artifact — it certifies integration between product System Versions with binding configuration. Module Package is a Run Track artifact — it enriches Module Version with operational systems and configuration for deployment. The Build Track produces what is *verified*; the Run Track produces what is *deployed*. See DR-027.
>
> **Environment-specific work is not just configuration.** The Run Track may introduce code (operational subsystems) per environment — custom probes, scheduled reconciliation jobs, cert rotation automation, environment-specific adapters. These are legitimate Systems (Dim 5) with code, repos, CI/CD pipelines, and System Versions. They serve Operational Personas (Dim 7) and are built through Run Track engineering (Run Epics and Run Stories). Module Package includes their System Versions alongside the product System Versions from Module Version.

## Purpose

Bridges the gap between what the Build Track produces (verified Module Version) and what the Run Track deploys (operationally complete composition). Without Module Package:
- Operational systems (probes, automation, reconcilers) have no composition entity — they exist as loose deployments alongside product systems
- The relationship between product systems and their operational support systems is invisible in the model
- Environment-specific enrichment (which probes for LATAM, which automation for US) has no structured representation
- The Run Track's engineering contribution (building operational systems) is not modeled as producing deployable artifacts
- Deployment Planning has to reason about product System Versions AND operational System Versions separately, with no composition entity to anchor the conversation

## Fields

| Field | Type | Description |
|---|---|---|
| Module Version | Reference (Track 2) | The Build Track's verified Module Version this Package enriches |
| Operational System Versions | Map | Operational System Versions included (e.g., `{payments-healthcheck: v1.2.0, payment-reconciler: v2.1.0}`) |
| Operational Configuration | Structured Config | Environment-specific operational configuration: monitoring thresholds, alerting rules, scaling policies, probe schedules, automation triggers |
| Target Environment(s) | List of References (Dim 7) | Which Deployment Environment(s) this Package targets (or environment overlay definitions) |
| Binding Configuration (Operational) | Structured Config | Operational wiring: probe-to-system mappings, automation triggers, scheduled job configurations, operational service mesh routes |
| Assembly Date | DateTime | When the Module Package was assembled |
| Run Epic | Reference (Track 3) | Run Epic that produced the operational enrichment (if applicable) |

## Statuses

| Status | Description |
|---|---|
| Assembling | Module Version is being enriched with operational systems and configuration |
| Ready | All operational System Versions included; operational configuration validated; ready for deployment |
| Deployed | Module Package has been deployed to at least one target environment |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Enriches | Module Version (Track 2) | Module Package enriches a verified Module Version with operational systems and configuration |
| Includes | Operational System Version(s) (Track 2/3) | Module Package includes operational System Versions built by Run Track engineering |
| Deployed by | Deployment (Track 3) | Module Package is deployed to environments by the Run Track |
| Targets | Deployment Environment(s) (Dim 7) | Module Package targets specific environments |
| Composed into | Product Package (Track 3) | Module Packages compose a Product Package |
| Produced by | Run Epic (Track 3) | Run Epic work produces operational System Versions and configuration for the Package |
| Produced by | Run Story(ies) (Track 3) | Run Stories contribute specific operational systems and configuration |

## Examples

### Payments Module Package for Production LATAM

```
Module Package: Payments Module v2.3.0 → Production LATAM
├── [From Module Version v2.3.0 — Build Track]
│   ├── payments-service v2.3.3
│   └── payment-gateway v1.2.1
├── [Operational Systems — Run Track]
│   ├── payments-healthcheck v1.2.0 (synthetic payment probes for LATAM corridors)
│   └── payment-reconciler v2.1.0 (daily settlement reconciliation for LATAM banks)
└── [Operational Configuration]
    ├── Monitoring: P95 latency alert threshold = 250ms (LATAM baseline is higher)
    ├── Scaling: min 3 replicas (LATAM regulatory requirement: 3-AZ)
    ├── Probe schedule: payments-healthcheck runs every 60s against BRL/MXN corridors
    └── Automation: payment-reconciler runs daily at 02:00 BRT

Target Environment: production-latam
Assembly Date: 2026-02-12T10:00:00Z
```

### FX Module Package for Staging (All Regions)

```
Module Package: FX Module v1.8.0 → Staging
├── [From Module Version v1.8.0 — Build Track]
│   ├── fx-service v1.8.1
│   └── fx-calculator v1.8.0
├── [Operational Systems — Run Track]
│   └── fx-rate-monitor v1.0.0 (rate-provider health monitoring)
└── [Operational Configuration]
    ├── Monitoring: Rate staleness alert = 5min (staging tolerance is higher)
    ├── Scaling: min 1 replica (staging)
    └── Probe schedule: fx-rate-monitor runs every 120s

Target Environment: staging
Assembly Date: 2026-02-11T14:00:00Z
```

---
