# Operational Pain

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** Engineering Leadership, Platform Engineering

## Definition

A specific, concrete suffering experienced by an Operational Persona in operating the product. Operational Pains are discoverable — they surface through Run Track experience and must be investigated, not assumed. Parallel to Delivery Friction (Dim 2) and Pain (Dim 3): same analytical structure (persona endures suffering that undermines an outcome), different beneficiary (operator vs. vendor commercial role vs. customer user). In some cases, the same underlying issue manifests across dimensions: "slow deployments" is an Operational Pain for the Platform Operator (Dim 7) AND a Delivery Friction for the Implementation Consultant (Dim 2) AND may contribute to a customer Pain (Dim 3) if it delays onboarding.

## Purpose

Analogous to Pain (Dim 3) and Delivery Friction (Dim 2). Operational Pain captures operator-level suffering that undermines the product's operational health. Without Operational Pain:
- Operational improvement is reactive — there is no structured entity to trace from operational suffering to product investment
- The Signal pipeline (Dim 1) has no structured Dim 7 entity to point to when operational problems are observed
- Operational Targets are undermined by invisible frictions — "we keep missing our availability SLO" but the root cause (manual failover) is undocumented

**Discovery process:** Operational Pains are observed by Operational Personas during Run Track work, surfaced as Signals (Problem or Opportunity) in Dim 1, investigated through Discovery, and formally documented in Dim 7 through Modeling Tasks triggered by PDRs. Operational Personas are Signal *sources*, not entity authors.

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Concise description of the pain |
| Quality Domain | Enum | From quality taxonomy: `Reliability` / `Performance` / `Security` / `Compliance` / `Cost Efficiency` / `Observability` / `Scalability` / `Platform` / `Data` |
| Endured by | List of References (Dim 7) | Which Operational Persona(s) experience this pain |
| Deployment Environment | List of References (Dim 7) | Which environment(s) this pain is associated with |
| Impact | Text | Quantified impact — engineer-hours, cost, risk, incident frequency |
| Frequency | String | How often this pain is experienced (continuous, daily, weekly, per-deployment, per-incident) |
| Undermines Operational Target | List of References (Dim 7) | Which Operational Target(s) this pain makes harder to achieve |
| Rooted in (Dim 8) | List of References (Dim 8) | When the pain has a product root cause, which Module(s) or Capability(ies) are involved. Optional — some pains are purely procedural. |

## Statuses

| Status | Description |
|---|---|
| Identified | Pain has been documented (via Modeling Task from PDR) |
| Under Investigation | Discovery work is investigating root causes or solutions |
| Mitigated | Product or process changes have reduced the pain (not eliminated) |
| Resolved | Pain has been eliminated through product or operational changes |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Endured by | Operational Persona (Dim 7) | Operational Personas experience this pain in their operational work |
| Scoped to | Deployment Environment (Dim 7) | Pain is associated with specific environments |
| Undermines | Operational Target (Dim 7) | Pain makes targets harder to achieve |
| May surface as | Signal — Problem or Opportunity (Dim 1) | Operational observations of pain become Signals for Discovery |
| Work Model | Modeling Task (Track 1) | Modeling Tasks document Operational Pains in Dim 7 |
| Rooted in | Module / Capability (Dim 8) | When pain has a product root cause, identifies the structural source |

## Examples

| Pain | Quality Domain | Endured by | Environment(s) | Impact | Undermines | Rooted in (Dim 8) |
|---|---|---|---|---|---|---|
| "Manual certificate rotation across 12 environments" | Security | Security Operator | All Production, Staging | 8 engineer-hours/week + risk of expired certificates | "Zero security incidents from operational lapses" | Key Management (Capability — missing automation) |
| "Alert fatigue — 40% of production alerts are false positives" | Observability | Reliability Operator | Production US-East, Production LATAM | SRE burnout; delayed response to real incidents (avg +3 min MTTR) | "MTTR < 30 min for P1" | Monitoring Module — Alert Configuration (Capability) |
| "Cloud spend grew 3x while traffic grew 1.5x" | Cost Efficiency | Platform Operator | Production US-East | $200K/month over budget; no automated right-sizing | "Infrastructure cost per 1K transactions < $0.50" | — (procedural: no FinOps process) |
| "Deployment rollback requires 45 minutes and manual steps" | Platform | Platform Operator | All Production | 45-min rollback window during incidents; increased blast radius | "Zero-downtime deployments; rollback within 5 min" | Deployment Module — Rollback Capability |
| "Database migration has no automated rollback" | Data | Data Operator | All environments | Failed migrations require manual data repair (avg 4 hours) | "RTO < 4 hours" | Database Admin Module — Migration Capability |

---
