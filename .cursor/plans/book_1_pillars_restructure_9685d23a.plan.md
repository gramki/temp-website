---
name: Book 1 Pillars Restructure
overview: Add Operational Pillars to Book 1 and update the ontology with the Tenant support model, request taxonomy, and escalation topology confirmed in our discussion.
todos:
  - id: ontology-support-model
    content: "Update ontology: Publisher Org (Tenant support), Landlord Org (governance not service), Product Ops Module, escalation topology, request taxonomy, relationships, glossary, todo.md"
    status: completed
  - id: create-pillar-dir
    content: Create part3-operational-pillars directory and 10 placeholder files
    status: completed
  - id: rename-dirs
    content: Rename part3-guides to part4-guides and part4-reference to part5-reference
    status: completed
  - id: renumber-guides
    content: Renumber 4 guide chapter files (09-12 to 19-22) and update internal headings
    status: completed
  - id: renumber-reference
    content: Renumber 5 reference chapter files (13-17 to 23-27) and update internal headings
    status: completed
  - id: update-book1-readme
    content: Rewrite book1 README with new 5-part 27-chapter structure and links
    status: completed
  - id: update-repo-readme
    content: Update repo root README with new part listing for Book 1
    status: completed
isProject: false
---

# Book 1 Restructure — Add Operational Pillars

## Current Structure (17 chapters)

- Part I: The Olympus Model (Ch 1-3)
- Part II: Architecture (Ch 4-8)
- Part III: Guides (Ch 9-12)
- Part IV: Reference (Ch 13-17)

## New Structure (27 chapters)

- Part I: The Olympus Model (Ch 1-3) -- unchanged
- Part II: Architecture (Ch 4-8) -- unchanged
- **Part III: Operational Pillars (Ch 9-18)** -- NEW
  - Ch 9: Cross-Pillar Workflows (introduction to Part III)
  - Ch 10: Security and Compliance (SecOps)
  - Ch 11: Financial Operations (FinOps)
  - Ch 12: Service Management and Incident Response (ITSM)
  - Ch 13: Continuous Delivery and Change (CD Ops)
  - Ch 14: Observability
  - Ch 15: Reliability and Resilience
  - Ch 16: Publisher Experience (DevEx)
  - Ch 17: Tenant Servicing and Product Support
  - Ch 18: Agentic Operations (forward-looking)
- Part IV: Guides (Ch 19-22) -- was Part III, renumbered
  - Ch 19: Publisher Guide (was Ch 9)
  - Ch 20: SRE Guide (was Ch 10)
  - Ch 21: Landlord and Tenant Guide (was Ch 11)
  - Ch 22: CIO / Enterprise Architecture Guide (was Ch 12)
- Part V: Reference (Ch 23-27) -- was Part IV, renumbered
  - Ch 23: Entity Reference (was Ch 13)
  - Ch 24: Descriptor Reference (was Ch 14)
  - Ch 25: Relationships Matrix (was Ch 15)
  - Ch 26: Lifecycle and Versioning Reference (was Ch 16)
  - Ch 27: Glossary (was Ch 17)

## Changes Required

### O. Ontology Updates (`olympus-ontology.md`)

The Tenant support model discussed in this session introduces new semantics that should be captured in the ontology before the book structure references them.

#### O1. Publisher Org (§9, line 974)

Current "Ongoing responsibility" bullet mentions "customer support" but does not state:

- The Publisher is the **Tenant's primary support contact** for product-related issues.
- The Publisher's support team operates the **Product Operations Module** tooling.
- The escalation topology: **Tenant -> Publisher -> SRE -> World SRE**.

Add a new bullet after "Ongoing responsibility":

- **Tenant support**: The Publisher is the Tenant's primary support contact for all product-related issues (functional, configuration, business). The Publisher's support organization operates the Product Operations Module (see §4) to service Tenants. When the Publisher determines an issue is infrastructure- or deployment-related, it escalates to the SRE Org. Platform-level issues escalate further to the World SRE Org.

#### O2. Landlord Org (§9, line 940)

Current text describes governance actions (APDs, SRE assignment) but does not explicitly state that the Landlord does **not** provide product support. Add:

- **Governance, not service**: The Landlord governs Tenant access (via APDs) and assigns SRE Orgs to Product Deployments. The Landlord does not provide product support to Tenants — that responsibility belongs to the Publisher. Tenants interact with the Landlord for administrative/governance matters (access requests, new Tenant onboarding) but contact the Publisher for product issues.

#### O3. Product Operations Module (§4, line 374)

Current description: "Applications and services for support teams to service and support customers". Clarify whose support teams:

- Change to: "Applications and services for the **Publisher's support organization** to service and support Tenants. The Publisher staffs, operates, and is accountable for these tools."

#### O4. Request Taxonomy — new subsection in §9

Add a subsection "Support and Request Taxonomy" after the Publisher-SRE Responsibility Division table (line ~1017). Content:

Three distinct request types flow through the Olympus operating model:

- **Product Support Request** (Tenant -> Publisher): Functional issues, configuration guidance, capacity adjustment requests, feature requests. Handled by Publisher's support organization using Product Operations Module tooling.
- **Deployment Service Request** (Publisher/Landlord -> SRE): Infrastructure changes, deployment updates, patch rollouts, resource sizing adjustments. Handled by SRE via ITSM processes.
- **Governance Request** (Tenant -> Landlord): Access to new Estates or Product Deployments, new Tenant onboarding, APD modifications. Handled by Landlord administration.

Escalation topology for product issues: Tenant -> Publisher -> SRE -> World SRE.

#### O5. Relationships Reference (§15)

- Add: `Publisher Org | supports | Tenant | 1 : N | No | Via Product Subscription; primary support contact`
- Add: `Tenant | raises-governance-request | Landlord Org | N : 1 | No | Access requests, onboarding`

#### O6. Glossary (§17)

Add a new entry:

**Product Support Request / Deployment Service Request / Governance Request**: Three distinct request types in the Olympus operating model. Product Support Requests flow from Tenant to Publisher (product issues). Deployment Service Requests flow from Publisher or Landlord to SRE (infrastructure/deployment changes). Governance Requests flow from Tenant to Landlord (access/administrative changes). These must not be conflated.

#### O7. todo.md

Add Round 5 Q&A section recording the Tenant support model discussion and answers. Mark as answered.

---

### A. Create new directory and 10 placeholder files

Create `book1-concepts-and-usage/part3-operational-pillars/` with:

- `09-cross-pillar-workflows--placeholder.md` — Names 4-5 key end-to-end workflows that span multiple pillars (resource requirement changes, EoL migration, new product onboarding, lease termination cascade, Tenant support escalation). Each traced through the relevant pillar chapters.
- `10-security-and-compliance--placeholder.md` — Tenant isolation (Enclaves, Spaces, DS network boundaries), APD two-tier model, RBAC+OPA, Space types for regulatory separation, artifact signing, Zero Trust, version blacklisting as security response.
- `11-financial-operations--placeholder.md` — DC Service Catalogs (quotas, budgets), CSP Subscription billing boundaries, four-part resource tagging for attribution, Deployment Space catalogs as subsets, RRD/RSD as cost levers.
- `12-service-management-and-incident-response--placeholder.md` — SRE-scoped ITSM: Deployment Service Requests, incident response, Publisher-SRE incident bridge, subscription lifecycle administration, lease termination cascade.
- `13-continuous-delivery-and-change--placeholder.md` — PDD/MDD versioning and rollout, Blue-Green MDI orchestration, Deployment Train promotions, version lifecycle tag compliance (EoL deadlines, blacklist remediation), feature flag strategy.
- `14-observability--placeholder.md` — What Publishers should instrument, what SREs should monitor, tenant-scoped vs platform-scoped observability, alerting ownership per responsibility matrix, Olympus-World-Connect telemetry.
- `15-reliability-and-resilience--placeholder.md` — Zone isolation blast radius, Blue-Green MDIs for far-DR, Deployment Space isolation, Admin Enclave criticality, break-glass procedures, Resource Provider GC semantics.
- `16-publisher-experience--placeholder.md` — Publisher lifecycle: design, register, publish, maintain. Weave Store as app-store model, RRSD as resource brochure, SemVer as simplifying contract, visibility control as go-to-market, feature flags.
- `17-tenant-servicing-and-product-support--placeholder.md` — Publisher as Tenant's primary support contact, Product Support Requests (Tenant to Publisher), escalation topology (Tenant to Publisher to SRE to World SRE), Governance Requests (Tenant to Landlord), Product Operations Module as Publisher's support tooling, request taxonomy, support SLAs.
- `18-agentic-operations--placeholder.md` — Forward-looking: AI agents in the Olympus operating model, autonomous remediation within responsibility boundaries, agent-driven subscription management, intelligent resource sizing, guardrails within APD model.

### B. Rename existing Part III and Part IV directories

- `part3-guides/` -> `part4-guides/`
- `part4-reference/` -> `part5-reference/`

### C. Renumber existing placeholder files

Rename all files in the former Part III (guides):

- `09-publisher-guide--placeholder.md` -> `19-publisher-guide--placeholder.md`
- `10-sre-guide--placeholder.md` -> `20-sre-guide--placeholder.md`
- `11-landlord-and-tenant-guide--placeholder.md` -> `21-landlord-and-tenant-guide--placeholder.md`
- `12-cio-enterprise-architecture-guide--placeholder.md` -> `22-cio-enterprise-architecture-guide--placeholder.md`

Rename all files in the former Part IV (reference):

- `13-entity-reference--placeholder.md` -> `23-entity-reference--placeholder.md`
- `14-descriptor-reference--placeholder.md` -> `24-descriptor-reference--placeholder.md`
- `15-relationships-matrix--placeholder.md` -> `25-relationships-matrix--placeholder.md`
- `16-lifecycle-and-versioning-reference--placeholder.md` -> `26-lifecycle-and-versioning-reference--placeholder.md`
- `17-glossary--placeholder.md` -> `27-glossary--placeholder.md`

### D. Update chapter heading inside each renamed file

Each renamed placeholder file has a `# Chapter N:` heading that needs updating to the new chapter number.

### E. Update [book1-concepts-and-usage/README.md](book1-concepts-and-usage/README.md)

Rewrite the Structure section to reflect the new 5-part, 27-chapter layout with correct links and part descriptions.

### F. Update [README.md](README.md) (repo root)

Update the Book 1 entry to list 5 parts instead of 4:

- Part I: The Olympus Model (3 chapters)
- Part II: Architecture (5 chapters)
- Part III: Operational Pillars (10 chapters)
- Part IV: Role-Specific Guides (4 chapters)
- Part V: Reference (5 chapters)

