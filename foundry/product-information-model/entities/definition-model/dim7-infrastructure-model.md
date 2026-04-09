# Infrastructure Model

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** Engineering Leadership, Platform Engineering, DevOps Leadership

## Definition

The fundamental hosting and operations strategy — how the vendor operates the product in production. The Infrastructure Model is the structural root of Dimension 7 — all other Dim 7 entities derive from or operate within it. Parallel to Business Model (Dim 2): "how we make money" vs. "how we run it."

The Infrastructure Model also defines the product's **Tenancy Architecture** — the pattern for how customer tenants are organized within Deployment Environments. Actual Tenants are Run Track (Track 3) operational artifacts; Dim 7 defines the architecture pattern.

## Purpose

Anchors the Operational dimension by establishing the macro-level infrastructure strategy. Like Business Model (Dim 2), the Infrastructure Model is a lightweight, rarely-changing entity — it provides context for the more dynamic entities (Operational Targets, Constraints, Pains). It changes at the scale of years (e.g., migrating from single-cloud to multi-cloud, shifting from shared tenancy to hybrid), not quarters. Without Infrastructure Model:
- Deployment Environments lack a strategic frame — they exist without explaining *why* this topology
- Cost strategy is implicit — no explicit model for cost allocation or scaling economics
- Tenancy decisions are undocumented — shared vs. dedicated is a critical architectural decision

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Multi-region AWS SaaS") |
| Cloud Strategy | Enum | `Single-cloud` / `Multi-cloud` / `Hybrid` / `On-premise` |
| Region Strategy | Enum | `Single-region` / `Multi-region` / `Global` |
| Tenancy Architecture | Enum | `Shared` / `Dedicated` / `Hybrid` |
| DR Strategy | Enum | `Active-active` / `Active-passive` / `Cold standby` / `None` |
| Scale Model | Enum | `Horizontal auto-scale` / `Vertical` / `Manual` / `Serverless` |
| Cost Model | Text | Cost allocation approach — reserved instances, spot, committed spend, pay-as-you-go. Key cost categories and scaling economics. |
| Compliance Architecture | Text | PCI scope, SOC 2 boundary, data sovereignty zones — the compliance-driven infrastructure constraints. |

## Statuses

_Not applicable — the Infrastructure Model is a structural descriptor that changes extremely rarely. When it does change, it is a company-level infrastructure event warranting its own PDR and ODR(s)._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Downstream | Deployment Environment (Dim 7) | Infrastructure Model defines the frame for Deployment Environments |
| Context for | Operational Target (Dim 7) | Infrastructure Model provides the operational context for targets |
| Context for | Operational Constraint (Dim 7) | Infrastructure Model frames which constraints apply |
| Context for | Operational Readiness (Dim 7) | Infrastructure Model determines readiness criteria scope |
| Work Model | Modeling Task (Track 1) | Infrastructure Model is evolved through Modeling Tasks |
| Justified by | PDR (Dim 1) | Infrastructure strategy changes are justified by PDRs |
| Justified by | ODR(s) (Dim 7) | Operational decisions that shape the Infrastructure Model are recorded as ODRs |

## Example

**"Multi-region AWS SaaS"**
- Cloud Strategy: Single-cloud (AWS)
- Region Strategy: Multi-region (us-east-1, eu-west-1, sa-east-1)
- Tenancy Architecture: Hybrid (shared for Mid-Market, dedicated for Enterprise)
- DR Strategy: Active-passive (us-east-1 primary, us-west-2 DR)
- Scale Model: Horizontal auto-scale with reserved base capacity
- Cost Model: Reserved instances for baseline (70% of capacity), auto-scale on-demand for peaks, committed spend discount for 1-year term. Key cost categories: compute (40%), data transfer (25%), compliance/audit (15%), storage (10%), support (10%).
- Compliance Architecture: PCI-DSS Level 1 scope across all payment-processing modules; SOC 2 Type II boundary includes all production environments; LGPD data sovereignty requires sa-east-1 for LATAM customer data.

---
