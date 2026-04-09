# Operational Constraint

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** Engineering Leadership, Compliance, Legal

## Definition

A non-negotiable infrastructure requirement imposed by regulation, compliance, customer contract, or architectural decision. Operational Constraints are structural impediments to operational choices — they limit what the product's infrastructure can do and how it can be configured. Parallel to Win Barrier (Dim 2), which captures structural impediments to commercial success.

When an Operational Constraint is unmet, it may surface as an Adoption Barrier (Dim 3) — preventing customers from adopting — or a Win Barrier (Dim 2) — preventing the vendor from winning commercially.

## Purpose

Captures the non-negotiable requirements that constrain Deployment Environments, module placement, and operational choices. Without Operational Constraints:
- Compliance requirements are implicit — which environments must be PCI-scoped is undocumented
- Data residency requirements are invisible — "LATAM data must stay in-country" has no entity to trace to
- The impact of constraints on product strategy is unclear — a data residency constraint may block market entry if no in-country environment exists

**Constraint vs. Target:** An Operational Target is aspirational ("99.99% availability" — we strive for it, measure it, invest in it). An Operational Constraint is non-negotiable ("payment data must be encrypted at rest" — there is no trade-off; failure is a compliance violation or contract breach).

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Constraint name (e.g., "LATAM data residency — LGPD") |
| Type | Enum | `Data Residency` / `Compliance Boundary` / `Network Segmentation` / `Security Standard` / `Change Window` / `Audit Requirement` / `Regulatory` |
| Source | Text | Where this constraint comes from (regulation, customer contract, architectural decision) |
| Description | Text | What the constraint requires |
| Affected Environment(s) | List of References (Dim 7) | Which Deployment Environments are constrained |
| Enforcement Mechanism | Text | How compliance with this constraint is verified |
| Structural Root (Dim 8) | List of References (Dim 8) | When the constraint affects specific modules or capabilities |

## Statuses

| Status | Description |
|---|---|
| Identified | Constraint has been documented |
| Enforced | Constraint is actively enforced in affected environments |
| At Risk | Constraint enforcement is degraded or under threat |
| Waived | Constraint has been temporarily waived with documented rationale and timeline |
| Retired | Constraint is no longer applicable (regulation changed, contract amended) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Imposed by | Compliance Posture (Dim 3) | Compliance Posture's customer-facing commitments impose operational constraints |
| Constrains | Deployment Environment (Dim 7) | Constraints limit what environments can do |
| May surface as | Adoption Barrier (Dim 3) | When unmet, constraint blocks customer adoption |
| May surface as | Win Barrier (Dim 2) | When unmet, constraint blocks vendor commercial success |
| May root in | Module / Capability (Dim 8) | Constraint may affect specific product structure |
| Frames | Infrastructure Model (Dim 7) | Constraints shape the overall infrastructure strategy |
| Decisions | ODR(s) (Dim 7) | Operational decisions that introduce or modify constraints are recorded as ODRs |
| Work Model | Modeling Task (Track 1) | Constraints are documented through Modeling Tasks |
| Signals | Signal (Dim 1) | Constraint gaps surface as Problem Signals |

## Examples

| Constraint | Type | Source | Affected Environments | Enforcement | Surface as |
|---|---|---|---|---|---|
| "LATAM data residency — LGPD" | Data Residency | LGPD regulation + LATAM Enterprise contracts | Production LATAM | Quarterly audit of data flow; automated data classification scanning | Adoption Barrier if no LATAM environment exists |
| "PCI-DSS scope — payment processing" | Compliance Boundary | PCI-DSS Level 1 certification | All Production environments processing payment data | Annual PCI audit; continuous compliance monitoring | — (already enforced) |
| "Change freeze — financial quarter end" | Change Window | Internal policy + Enterprise customer contracts | All Production environments | Deployment automation blocks non-emergency changes during freeze windows | — |
| "mTLS for all inter-service communication" | Security Standard | SOC 2 + architectural decision | All Production and Staging environments | Certificate validation in service mesh; automated mTLS enforcement | — |
| "Data sovereignty — EU customer data" | Data Residency | GDPR | Production EU-West | Automated data routing rules; quarterly data residency audit | Adoption Barrier for EU customers if not enforced |

---
