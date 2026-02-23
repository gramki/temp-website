# Deployment Environment

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** Platform Engineering, DevOps Leadership

## Definition

A named, typed, vendor-operated infrastructure target where modules are deployed and tenants are provisioned. The Deployment Environment carries the vendor's operational purpose — customer-facing purpose lives on the Tenant (Run Track entity). The Tenancy Architecture (inherited from Infrastructure Model or overridden) defines how customer isolation is organized within this environment.

Supersedes the original skeletal "Environment" entity, which lacked vendor purpose, tenancy architecture, compliance zone, scale policy, and a full relationship set.

## Purpose

Captures the strategic infrastructure decisions about where the product runs and how each environment is configured. Without Deployment Environments:
- Module deployment has no target — "deploy to production" has no structured definition of what "production" means
- Tenancy decisions are invisible — shared vs. dedicated isolation within an environment is undocumented
- Operational Targets lack scope — "99.99% availability" has no environment context
- Compliance zones are implicit — which environments are in PCI scope is untracked

**Vendor Purpose vs. Customer Purpose:** The vendor's purpose (Production, Staging, DR) is a property of the environment — how the vendor classifies and operates this infrastructure. The customer's purpose (Production, UAT, Sandbox) lives on the Tenant (Run Track) — what this logical slice means to a specific customer. A single vendor Production environment may host tenants with different customer purposes.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Environment name (e.g., "Production US-East," "Staging EU-West") |
| Vendor Purpose | Enum | `Production` / `Staging` / `Development` / `DR` / `CI/CD` / `Demo` |
| Region | String | Geographic region or zone (e.g., "us-east-1," "eu-west-1," "sa-east-1") |
| Tenancy Architecture | Enum | `Shared` / `Dedicated` / `Hybrid` — inherited from Infrastructure Model or overridden per environment |
| Compliance Zone | Text | Compliance standards enforced in this environment (e.g., "PCI-DSS Level 1," "LGPD data residency") |
| Scale Policy | Text | Scaling behavior for this environment (e.g., "auto-scale 3–12 nodes," "fixed 2 nodes") |
| Hosted Modules | List of References (Dim 8) | Which modules are deployed in this environment |

## Statuses

| Status | Description |
|---|---|
| Planned | Environment has been designed but not yet provisioned |
| Provisioning | Environment is being set up (infrastructure being created) |
| Active | Environment is operational and receiving deployments |
| Maintenance | Environment is temporarily restricted for maintenance work |
| Decommissioning | Environment is being wound down (tenants migrated, modules removed) |
| Retired | Environment has been fully decommissioned |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Defined by | Infrastructure Model (Dim 7) | Infrastructure Model frames this environment's strategy |
| Hosts | Module(s) (Dim 8) | Modules are deployed to this environment (functional view) |
| Hosts | System(s) (Dim 5) | Systems are deployed to this environment (technical view — the deployable units) |
| Hosts | Tenant(s) (Track 3) | Tenants are provisioned within this environment (Run Track) |
| Constrained by | Operational Constraint (Dim 7) | Constraints limit what this environment can do |
| Has | Operational Target(s) (Dim 7) | Environment-level operational targets |
| Operated by | Operational Persona(s) (Dim 7) | Operational Personas manage this environment |
| Scoped by | Operational Readiness (Dim 7) | System readiness is assessed per-environment |
| Justified by | PDR (Dim 1) | New environment provisioning is justified by PDRs |
| Decisions | ODR(s) (Dim 7) | Operational decisions affecting this environment are recorded as ODRs |
| Work Model | Deployment (Track 3) | Deployments target this environment |
| Work Model | Capacity Planning Task (Track 3) | Capacity is planned per-environment |

## Examples

| Environment | Purpose | Region | Tenancy | Compliance | Scale | Status |
|---|---|---|---|---|---|---|
| Production US-East | Production | us-east-1 | Shared | PCI-DSS Level 1 | Auto-scale 3–12 nodes | Active |
| Production LATAM | Production | sa-east-1 | Dedicated (Enterprise) | PCI-DSS Level 1, LGPD | Auto-scale 2–8 nodes | Active |
| Staging EU-West | Staging | eu-west-1 | Shared | SOC 2 (test scope) | Fixed 2 nodes | Active |
| DR US-West | DR | us-west-2 | Shared | PCI-DSS Level 1 | Passive standby, auto-scale on failover | Active |
| Demo | Demo | us-east-1 | Shared | None | Fixed 1 node | Active |

---
