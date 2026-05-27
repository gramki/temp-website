---
name: Dim 7 Operational Expansion
overview: Expand Dimension 7 (Operational) from 3 skeletal entities to 9 fully detailed entities with cross-dimensional connections, add Tenant to Run Track, widen UX Channel and Integration Module scope, and capture all supporting documentation (narrative seeds, decision record, FAQs).
todos:
  - id: narrative-seeds
    content: Add Dim 7 session to narrative-seeds.md with 13+ seeds capturing all discussion insights
    status: completed
  - id: definition-model
    content: Rewrite Dim 7 section in draft-definition-model.md with 9 entities, quality taxonomy, and deprecation notes
    status: completed
  - id: entity-files-new
    content: Create 9 new entity files (dim7-infrastructure-model through dim7-operational-readiness)
    status: completed
  - id: entity-files-deprecate
    content: Mark 3 old Dim 7 entity files as deprecated (environment, cluster-host, container-process)
    status: completed
  - id: scope-widenings
    content: Widen UX Channel (dim4-ux-channel.md) and Integration Module (dim6-integration-module.md) scope notes
    status: completed
  - id: work-model-tenant
    content: Add Tenant to Run Track in draft-work-model.md
    status: completed
  - id: work-execution-framework
    content: Add Tenant artifacts to draft-work-execution-framework.md
    status: completed
  - id: decision-record
    content: Create DR-023 and update decisions/README.md index
    status: completed
  - id: modeling-faqs
    content: Add Q66-Q73 to draft-modeling-faqs.md
    status: completed
  - id: readmes
    content: Update entities/README.md directory structure and main README.md Dim 7 row
    status: completed
isProject: false
---

# Dimension 7: Operational Dimension Expansion

## Summary of Decisions

From the discussion, the following design decisions were made (to be captured in DR-023):

- **D1:** 9 new entities for Dim 7 (Infrastructure Model, Operational Persona, Operational Job, Operational Journey, Deployment Environment, Operational Target/SLO, Operational Constraint, Operational Pain, Operational Readiness)
- **D2:** Deprecate Cluster/Host and Container/Process (below waterline, same pattern as Touchpoint in Dim 4 and Payload Schema in Dim 6)
- **D3:** Operational Quality Taxonomy as classification framework, not standalone entities (parallels AAARRR in Dim 2)
- **D4:** Tenant is a Run Track work entity (provisioned, managed, monitored as operational work), not a Definition Model entity
- **D5:** Customer remains implied (instance of Customer Segment), not a first-class entity
- **D6:** UX Channel (Dim 4) scope widened to serve all human personas including Operational Personas
- **D7:** Integration Module (Dim 6) scope widened to serve Operational Personas (Datadog, PagerDuty, Terraform integrations)
- **D8:** Operational Target carries Achievement Levers (paralleling Win Outcome in Dim 2)
- **D9:** Dim 7 is independent from Dim 4 — Operational Job and Operational Journey are independent entities, not widened Dim 4 entities
- **D10:** Operational Readiness is a per-module x per-environment assessment entity in Dim 7

## Implementation Tasks

### 1. Narrative Seeds

Add a new session to [narrative-seeds.md](org-8.0/product-information-model/narrative-seeds.md) titled "Dimension 7 — The Operational Dimension (Runtime & DevOps)". Seeds to capture:

- Dim 2 / Dim 6 parallels driving Dim 7 entity design (Win Stakeholder -> Operational Persona, Win Outcome -> Operational Target, Delivery Friction -> Operational Pain, Business Model -> Infrastructure Model)
- Operational Quality Taxonomy as classification framework not entities (parallels AAARRR)
- Tenant as Run Track work entity, not Definition Model (provisioned, managed, monitored)
- Customer vs Tenant vs Customer Segment distinction (Customer is implied, Tenant has purpose/exposure)
- Deployment Environment purpose duality resolved: vendor purpose on Environment, customer purpose on Tenant
- UX Channel universality: serves all human personas (Dim 4 User, Dim 7 Operator); Option A — stays in Dim 4, scope widened
- Dim 7 independence from Dim 4: parallel structures, not inheritance (Operational Job is not Dim 4 Job)
- Operational Persona archetypes organized by quality taxonomy, not job titles
- Operational Persona JTBDs: Run Track work entities are the operational jobs; Definition Model acknowledges them via Operational Job entity linked to Dim 8
- Third-party ops tools as product's integrated solution: Integration Modules (Dim 6) serve Operational Personas too
- Operational Readiness at module scope: per-module operational maturity, distinct from Evolve Track process assessment
- Operational Target with achievement levers: connects Dim 7 into the Initiative/Lever framework
- Cost targets: modeled through Infrastructure Model (Cost Model), Operational Target (Cost type), and Operational Pain

### 2. Update Definition Model

Rewrite the Dim 7 section in [draft-definition-model.md](org-8.0/product-information-model/draft-definition-model.md) (lines 330-345). Replace the 3 skeletal entities with the full 9-entity set, including:

- Introductory framing paragraph (what the dimension answers, quality taxonomy definition)
- Infrastructure Model (root)
- Operational Persona (with quality-taxonomy archetypes)
- Operational Job
- Operational Journey
- Deployment Environment (expanded, with Tenancy Architecture, vendor purpose)
- Operational Target (SLO) with Achievement Levers and Cost type
- Operational Constraint
- Operational Pain
- Operational Readiness (per-module)
- Deprecation notes for Cluster/Host, Container/Process, and original Environment
- Cost coverage explanation

### 3. Create Entity Files (9 new)

Create in `entities/definition-model/`:

- `dim7-infrastructure-model.md` — root entity, paralleling `dim2-business-model.md`
- `dim7-operational-persona.md` — paralleling `dim6-developer-persona.md` / `dim2-win-stakeholder.md`
- `dim7-operational-job.md` — paralleling `dim4-job.md`
- `dim7-operational-journey.md` — paralleling `dim4-user-journey.md`
- `dim7-deployment-environment.md` — expanded from current skeletal `dim7-environment.md`
- `dim7-operational-target.md` — paralleling `dim2-win-outcome.md` (with Achievement Levers)
- `dim7-operational-constraint.md` — paralleling `dim2-win-barrier.md`
- `dim7-operational-pain.md` — paralleling `dim2-delivery-friction.md`
- `dim7-operational-readiness.md` — new concept (per-module x per-environment)

All follow the entity template from `entities/README.md`.

### 4. Deprecate Old Entity Files (3)

Mark as deprecated (add deprecation header, do NOT delete):

- `dim7-environment.md` — superseded by `dim7-deployment-environment.md`
- `dim7-cluster-host.md` — below waterline; PSD/Run Track artifact
- `dim7-container-process.md` — below waterline; PSD/Run Track artifact

### 5. Update Existing Entity Files (2 scope widenings)

- [dim4-ux-channel.md](org-8.0/product-information-model/entities/definition-model/dim4-ux-channel.md) — widen Definition and Purpose to acknowledge it serves all human personas (Dim 4 User Personas AND Dim 7 Operational Personas). Add relationship row for Operational Persona (Dim 7). Update examples to include an operational example (e.g., "Monitoring Dashboard — Web Self-serve" for SRE).
- [dim6-integration-module.md](org-8.0/product-information-model/entities/definition-model/dim6-integration-module.md) — widen Definition and Purpose to acknowledge it serves Operational Personas (Datadog, PagerDuty, Terraform integrations). Add relationship row for Operational Persona (Dim 7). Add operational integration example.

### 6. Update Work Model

Update [draft-work-model.md](org-8.0/product-information-model/draft-work-model.md):

- In **Track 3: Run Track**, add **Tenant** as an operational entity (provisioned within Deployment Environment, belongs to Customer, carries customer-facing purpose). Add it alongside existing operational entities (Incident, Change Request, Maintenance Task, Deployment).
- Update Run Track Monitoring reference to mention Tenant health monitoring.

### 7. Update Work Execution Framework

Update [draft-work-execution-framework.md](org-8.0/product-information-model/draft-work-execution-framework.md):

- Add Tenant-related entries to the Cross-Track Artifact Inventory (Run Track row)
- Add "Tenant Provisioning Record" as a Delivery artifact type in the artifact type catalog

### 8. Create Decision Record

Create `decisions/DR-023-dim7-operational-dimension-expansion.md` with decisions D1-D10 listed above.

### 9. Update Decision Record Index

Add DR-023 row to [decisions/README.md](org-8.0/product-information-model/decisions/README.md).

### 10. Add Modeling FAQs

Add to [draft-modeling-faqs.md](org-8.0/product-information-model/draft-modeling-faqs.md) (Q66+):

- Q66: Why does Dim 7 need its own Operational Persona, Job, and Journey instead of widening Dim 4?
- Q67: Why is Tenant a Run Track work entity rather than a Dim 7 Definition Model entity?
- Q68: Why is Operational Quality a taxonomy not an entity set?
- Q69: Why does Operational Target carry Achievement Levers?
- Q70: What is the relationship between Dim 7 Operational Target (SLO), Dim 6 API Operation SLOs, and Dim 3 Service Commitment?
- Q71: Why deprecate Cluster/Host and Container/Process?
- Q72: How are infrastructure cost targets modeled?
- Q73: Why Operational Readiness at module scope rather than in Evolve Track?

### 11. Update Entity Catalog README

Update [entities/README.md](org-8.0/product-information-model/entities/README.md):

- Add 9 new dim7-* files to directory structure listing
- Mark 3 old dim7-* files as deprecated
- Update file count

### 12. Update Main README

Update [README.md](org-8.0/product-information-model/README.md):

- Update Dim 7 row in the Definition Model dimensions table from "Environments, clusters, containers" to the full entity set
- Update Run Track row to mention Tenant

