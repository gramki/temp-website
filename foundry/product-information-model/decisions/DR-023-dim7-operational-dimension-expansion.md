# DR-023: Operational Expansion

**Status:** Accepted
**Date:** 2026-02-15

## Context

Operational was the least developed dimension in the UPIM — just 3 skeletal entities (Environment, Cluster/Host, Container/Process) with no strategic framing, no personas, no relationships, and no cross-dimensional connections. Meanwhile, the model had already established significant Operational dependencies: Service Commitment (Customer Value) explicitly references "Operational captures the infrastructure that delivers it," API Operation SLOs (Ecosystem) defer to "Technical/Operational/Run Track territory," and Client-Distributed modules (Structural) note a different "Operational footprint."

The expansion drew structural parallels from Vendor Value and Ecosystem, applying proven entity patterns to the operational domain. Discussions addressed several architectural questions: the vendor-vs-customer duality of environment purpose, the distinction between Tenant and Customer, the relationship between Operational and User Experience (independence vs. entity sharing), the role of operational quality attributes (entities vs. taxonomy), and how Operational connects to the Initiative/Lever framework.

## Decisions

### D1: Nine entities for the expanded Operational dimension

Operational is expanded from 3 skeletal entities to 9 fully detailed entities: **Infrastructure Model** (root), **Operational Persona**, **Operational Job**, **Operational Journey**, **Deployment Environment**, **Operational Target (SLO)**, **Operational Constraint**, **Operational Pain**, **Operational Readiness**. The entity set parallels the established patterns: Business Model → Infrastructure Model, Win Stakeholder → Operational Persona, Win Outcome → Operational Target, Delivery Friction → Operational Pain, Win Barrier → Operational Constraint.

### D2: Deprecate Cluster/Host and Container/Process

Cluster/Host and Container/Process are deprecated as below the Definition Model waterline. Specific compute infrastructure (Kubernetes clusters, VM hosts, Docker containers) belongs in PSD/Run Track artifacts. This follows the same deprecation pattern as Touchpoint (User Experience) and Payload Schema (Ecosystem) — the Definition Model captures strategic operational decisions; specific infrastructure choices are work artifacts.

### D3: Operational Quality Taxonomy as classification framework, not entities

Operational quality dimensions (Reliability, Performance, Security, Compliance, Cost Efficiency, Observability, Scalability) are a classification framework used as type/category axes on Operational entities, not standalone entities. This parallels AAARRR in Vendor Value, which classifies Win Outcomes, Win Stakeholders, and Business KPIs without being individual entities itself.

### D4: Tenant is a Run Track work entity

Tenant (a logical isolation unit within a Deployment Environment) is modeled as a Run Track (Run) operational entity, not a Definition Model entity. A Tenant is provisioned, configured, monitored, scaled, and decommissioned — it is the result of operational work. The Definition Model captures the Tenancy Architecture (shared/dedicated/hybrid) on Infrastructure Model and Deployment Environment; the Run Track manages individual Tenants.

### D5: Customer remains implied

Customer (legal/contracting entity) is not a first-class Definition Model entity. It is an instance of Customer Segment (Customer Value), acknowledged in Tenant relationships but not modeled as a standalone entity. The Definition Model captures types and structures, not instances. Customer-level data is operational state (CRM/billing territory).

### D6: Deployment Environment carries vendor purpose only

The vendor's operational purpose (Production, Staging, DR) lives on Deployment Environment. The customer's purpose (Production, UAT, Sandbox) lives on the Tenant (Run Track). A single vendor Production environment may host tenants with different customer purposes. This resolves the purpose duality cleanly: the environment IS "Production" from the vendor's perspective; within it, Customer A has a production tenant and Customer B has a UAT tenant.

### D7: Operational is independent from User Experience — parallel structures, not inheritance

Operational Job and Operational Journey are independent Operational entities, not widened versions of User Experience Job (JTBD) and User Journey. Same analytical pattern (persona → job → journey → module), different domain (operational reality vs. user experience), different relationships (Operational Job connects to SLOs and Run Track; JTBD connects to Business Outcomes and Value Streams). Dimensions are self-contained; structural parallels inform design but do not create shared entities.

### D8: UX Channel (User Experience) scope widened to serve all human personas

UX Channel stays in User Experience (its natural home) but its scope is widened to serve Operational Personas as well. Operational Personas use the same Interaction Modalities (Web, Mobile, Chat, Voice, Email, CLI) and Engagement Modes (Self-serve, Assisted, Managed). This is cross-dimensional referencing, not entity sharing — Operational Journey references UX Channels from User Experience.

### D9: Integration Module (Ecosystem) scope widened to serve Operational Personas

Integration Modules serve Developer Personas, Programmatic User Personas, AND Operational Personas. Third-party ops tooling integrations (Datadog exporters, PagerDuty webhooks, Terraform providers) are Integration Modules deliberately built for the Operations team. Operational Journeys trace through both native operational modules and integration modules to third-party ops tools.

### D10: Operational Target carries Achievement Levers

Operational Targets carry Achievement Levers (Product or Operational), paralleling Win Outcome's Achievement Levers from the Business Model's Lever Portfolio. This connects Operational into the Initiative/Lever framework: an Initiative with Operational lever weight drives work to improve Operational Targets. Operational Pains feed the Signal pipeline (Strategy), driving Initiatives with appropriate lever mixes.

### D11: Operational Readiness at System scope

Operational Readiness is a per-System × per-environment assessment entity in Operational — does this System (Technical) meet operational acceptance criteria (observability, security, performance, operability, DR, compliance) for this environment? This is distinct from Evolve Track which assesses process effectiveness. The criteria definition is a Definition Model concern; the assessment work is Run Track activity. Module-level readiness is a derived view that aggregates across constituent Systems.

> **Updated from original D11:** Originally scoped to Module (Structural). Rescoped to System (Technical) during Build Track detailing (DR-026) — SREs operate Systems, not Modules. Observability, security, runbooks, DR procedures are all System-scoped. Module-level readiness is derived by aggregating across all Systems implementing the Module.

## Rationale

**Why draw from Vendor Value and Ecosystem?** These dimensions are the best-detailed in the model and have established patterns for personas, outcomes, frictions, barriers, and contracts. The operational domain has structural analogs to each: someone operates (persona), they need outcomes (targets), they suffer (pain), they face limits (constraints). Applying proven patterns reduces design risk.

**Why not merge with User Experience?** User Experience is "User-Centric" — it models the customer's experience. Operational models the vendor's infrastructure reality. Same structural patterns, different stakeholders, different concerns, different quality criteria. Merging would dilute both.

**Why Tenant in Run Track, not Operational?** The Definition Model captures "what the product IS" — including that it supports multi-tenancy. The Work Model captures "what work EXISTS" — including provisioning and managing individual tenants. Tenants are instances, not definitions.

**Why quality taxonomy, not entities?** AAARRR stages in Vendor Value are not individual entities — they classify other entities. Quality dimensions serve the same role in Operational: they type Operational Targets, Personas, Constraints, and Pains without being standalone entities.

**Why Operational Readiness in Operational, not Evolve Track?** Evolve Track assesses process health ("are our DoD criteria being followed?"). Operational Readiness assesses System health ("is this System production-ready in this environment?"). Different scope, different assessors, different triggers. Module-level readiness is derived by aggregating System-level assessments.

## Consequences

**Positive:**
- Operational is now structurally comparable to Vendor Value and Ecosystem, completing the model's coverage of operational concerns
- Operational tooling investment has a demand-side entity (Operational Persona → Operational Job → Capability)
- The product's operational reality is traceable: Service Commitment (Customer Value) → Operational Target → Module (Structural) → Deployment Environment
- Operational Pains feed the Discovery pipeline through Signals, connecting operational suffering to product improvement
- Tenant lifecycle is explicitly modeled as Run Track work, resolving the vendor/customer purpose duality
- UX Channel and Integration Module widening makes the model more accurate without creating new entities

**Negative:**
- Operational grows from 3 to 9 entities, increasing the model's surface area
- Two scope widenings (UX Channel, Integration Module) add cross-dimensional complexity
- Tenant in Run Track may require a dedicated entity file and operational procedures (Operating Model work)

**Mitigations:**
- Entity count (9) is comparable to Ecosystem (8) and smaller than Vendor Value (10) — proportional to domain complexity
- Scope widenings follow established patterns (Ecosystem modules reference Structural modules; Operational journeys reference User Experience channels)
- Tenant lifecycle details can be iteratively refined through Track 5 (Evolve)

---
