# Tenant

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Category:** Operational
**Owner:** DevOps, SRE, Platform Engineering

## Definition

A logical isolation unit within a Deployment Environment (Dim 7), belonging to a Customer (instance of Customer Segment, Dim 3), with a customer-facing purpose. Tenants are provisioned, configured, monitored, scaled, and eventually decommissioned as Run Track operational work.

A single Customer may have multiple Tenants in the same environment (e.g., one for production use, one for UAT). The Deployment Environment defines the infrastructure; the Tenant defines the customer's logical slice within it.

> **Tenant vs. Customer.** A Customer is an external stakeholder tracked in the External Stakeholder Registry (ESR). A Tenant is the operational manifestation of that customer's presence in the product's infrastructure. The relationship is Customer (ESR) → Tenant(s) (Run Track). Multiple Tenants may serve the same Customer across different environments or purposes.

## Purpose

Makes the customer's operational presence explicit in the Run Track. Without Tenant:
- There is no structured representation of customer isolation boundaries
- Incident impact cannot be scoped to specific customers ("which tenants were affected?")
- Subscription lifecycle work (provisioning, activation, suspension, decommissioning) has no anchor entity
- SLO compliance cannot be assessed per-customer
- Deployment impact assessment cannot determine which customers are affected by a change

## Fields

| Field | Type | Description |
|---|---|---|
| ID | String | Unique tenant identifier (e.g., `tenant-itau-prod-latam`) |
| Name | String | Human-readable name (e.g., "Banco Itaú — Production LATAM") |
| Customer | Reference (ESR) | Which customer organization this tenant belongs to |
| Deployment Environment | Reference (Dim 7) | Which environment this tenant resides in |
| Purpose | Enum | `Production` / `UAT` / `Sandbox` / `Trial` / `DR` — the customer-facing purpose, distinct from the environment's vendor purpose |
| Isolation Model | Text | How isolation is achieved (e.g., "dedicated schema", "shared schema with row-level isolation", "dedicated namespace") |
| Subscription Tier | Reference (Dim 2) | Which Pricing Tier / Package the customer's subscription corresponds to |
| SLO Tier | Text | Which SLO tier applies to this tenant (derived from subscription or negotiated) |
| Provisioned Modules | List of References (Dim 8) | Which Modules are provisioned for this tenant |
| Configuration | Text / Reference | Tenant-specific configuration — feature flags, capacity limits, integration settings |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Requested | Tenant provisioning has been requested |
| Provisioning | Infrastructure and configuration are being set up |
| Active | Tenant is live and serving the customer |
| Suspended | Tenant is temporarily disabled (billing, compliance, or maintenance) |
| Decommissioning | Tenant is being wound down — data export, notification, resource cleanup |
| Retired | Tenant is fully decommissioned; resources reclaimed; data archived per retention policy |

```
Requested ──► Provisioning ──► Active ──► Suspended ──► Decommissioning ──► Retired
                                  │                          ▲
                                  └──────────────────────────┘
                                    (direct decommission)
```

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | Customer (ESR) | Tenant is a customer's operational slice |
| Resides in | Deployment Environment (Dim 7) | Tenant lives within an environment |
| Governed by | Subscription Tier / Pricing Tier (Dim 2) | Tenant's entitlements are derived from subscription |
| Provisioned with | Module (Dim 8) | Which modules are available to this tenant |
| Affected by | Incident (Track 3, artifact) | Incidents may optionally specify affected tenants |
| Affected by | Deployment (Track 3, artifact) | Deployments to the tenant's environment affect this tenant |
| Monitored by | System Monitoring (Track 3) | Tenant-level metrics are monitored |
| Scoped by | Change Request (Track 3) | Changes may be scoped to specific tenants |
| Referenced by | FIR (Track 4) | FIRs may reference the affected tenant |

## Example

| Tenant ID | Customer | Environment | Purpose | Isolation | SLO Tier | Status |
|---|---|---|---|---|---|---|
| `tenant-itau-prod-latam` | Banco Itaú | Production LATAM | Production | Dedicated schema | Enterprise | Active |
| `tenant-itau-uat-latam` | Banco Itaú | Staging LATAM | UAT | Shared schema, row isolation | Standard | Active |
| `tenant-globalpay-prod-us` | GlobalPay SA | Production US-East | Production | Dedicated namespace | Enterprise | Active |
| `tenant-fintechcorp-trial` | Fintech Corp | Sandbox | Trial | Shared schema, row isolation | Trial | Active |
| `tenant-legacy-bank-prod` | Legacy Bank | Production US-East | Production | Dedicated schema | Enterprise | Decommissioning |
