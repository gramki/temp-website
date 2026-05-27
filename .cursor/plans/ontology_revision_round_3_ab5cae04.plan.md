---
name: Ontology Revision Round 3
overview: Apply the 21 confirmed answers from Round 3 Q&A to olympus-ontology.md. This round introduces targeted precision fixes (two-tier APD model, K8s CP Enclave scoping, RPRP, PDD creation flow, Velos dual-role clarification, World Admin Estate, RRSD authorship correction, OEP 1:1 per Zone) rather than the structural rewrites of Round 2.
todos:
  - id: apd-two-tier
    content: Rewrite APD model to two-tier (Tenant-level by Landlord + TSD/MSS-level by Tenant Admins) across sections 5, 10, 15, 17.
    status: completed
  - id: tenant-split
    content: Expand Tenant and Tenant Org definitions in section 10 with clear responsibility split.
    status: completed
  - id: resource-gc
    content: "Expand Resource GC in section 7: Elenchos notifies RPs, RPs handle lifecycle per contract."
    status: completed
  - id: sre-pdd
    content: Update SRE Org in section 9 to state assignment captured in PDD (N:1 stays).
    status: completed
  - id: pdd-flow
    content: "Add PDD creation flow narrative in section 6: Landlord questionnaire -> Weave baseline -> SRE refines."
    status: completed
  - id: rprp
    content: Add RPRP as Enclave sub-entity in section 7 or 6; add to section 15 relationships.
    status: completed
  - id: velos-dual-role
    content: Clarify Velos as both Operator and RP for all CSP resources (infra + app level) in sections 7, 12.
    status: completed
  - id: cp-enclave-scope
    content: Add K8s CP Enclave scoping constraint in sections 3, 15.
    status: completed
  - id: world-admin-estate
    content: Add World Admin Estate entity/narrative in sections 8, 10, 15.
    status: completed
  - id: space-multiplicity
    content: Add Space same-type multiplicity note in section 1.
    status: completed
  - id: rrsd-authorship
    content: Fix RRSD authorship to Publisher Org (of RP Module Spec) in sections 4, 5, 15.
    status: completed
  - id: oep-one-per-zone
    content: Fix OEP to exactly one per Zone in section 11.
    status: completed
  - id: todo-update
    content: Mark all Round 3 questions as completed in todo.md.
    status: completed
isProject: false
---

# Ontology Revision Round 3

All changes target `[olympus-ontology.md](/Users/ramki/Git/personal-projects/olympus-diagrams/olympus-ontology.md)`. Section numbers refer to the current document.

## A. Two-tier APD model (Q1, Q2, Q3, Q15)

The biggest model change. Currently APD is described as single-scope, Landlord-authored. Must be rewritten to a two-tier model.

### Changes to section 10 (Tenancy Hierarchy)

- **Tenant entity**: Expand definition to distinguish Tenant (business entity: billing contacts, admin contacts, subscriptions, Tenant-level APDs) from Tenant Org (identity container: User Profiles, Machine identities in IDP Domain). Add that Tenant-level APDs are authored by the Landlord and attached directly to the Tenant entity, independent of any TSD.
- **Tenant Org entity**: Expand to state it encapsulates User Profiles and Machine identities that translate to Auth Profiles in its IDP Domain. The Org is the collection of users/machines that avail subscription services.
- **Module Subscription entity**: Add that Module Subscription Section is its descriptor form (analogous to MSD for Module Specification).
- **APD entity**: Rewrite to describe APD as a single entity type that operates at two scopes:
  - **Tenant-level APD**: Authored by Landlord, attached to Tenant. Controls which Estates, Enclaves, and Product Deployments the Tenant can access. Ceiling for all access.
  - **TSD/MSS-level APD**: Authored by Tenant Admins. Can only narrow what the Landlord granted. Lives within Module Subscription Sections.
  - OE modules (particularly Velos) evaluate both tiers independently: Tenant-level as ceiling, TSD/MSS-level as further restriction. Tenant-level APDs are not injected into TSDs.
- **Module Subscription Section entity**: Fix "Contains APDs authored by the Landlord" to "Contains APDs authored by Tenant Admins (narrowing Tenant-level access)."

### Changes to section 5 (Descriptor Taxonomy)

- Policy Descriptors table: Update APD description to note two scopes and two authorship sources.

### Changes to section 15 (Relationships Reference)

- Update Tenancy rows: `Tenant | associated-with | APD` note should say "Tenant-level; authored by Landlord"
- Update `Module Subscription Section | contains | APD` note should say "TSD-level; authored by Tenant Admins; narrows Tenant-level"

### Changes to section 17 (Glossary)

- Update or add an APD entry clarifying the two-tier model.

## B. Tenant and Tenant Org responsibility split (Q1)

### Changes to section 10

- **Tenant**: Add purpose: encapsulates business entity information (billing contacts, admin contacts, intervention contacts for subscriptions).
- **Tenant Org**: Add purpose: encapsulates User Profiles and Machine identities; these translate to Auth Profiles in the associated IDP Domain. The Org is the identity container through which users/machines avail subscription services.

## C. Tenant-scoped resource GC (Q4)

### Changes to section 7 (Resources vs. Deployments)

- Expand "Resource Garbage Collection" paragraph: Elenchos notifies Resource Providers of subscription state changes and ensures RPs acknowledge the change. The RP handles actual lifecycle per its advertised contract. SREs rely on the RP's contract and any tools/levers the RP offers for intervention.

## D. SRE Org assignment in PDD (Q5, Q21)

### Changes to section 9 (World, Identity, and Organizations)

- **SRE Org**: Update to state the SRE Org assignment is captured in the PDD. Cardinality stays N:1 (one SRE Org per PD).

## E. PDD creation flow (Q6, Q19)

### Changes to section 6 (Deployment Hierarchy)

- **PDD entity**: Add a "Product Deployment Initiation" narrative paragraph after the PDD definition:
  - Landlord requests a Product Deployment through a Weave-provided questionnaire.
  - Weave creates a baseline PDD from the questionnaire inputs.
  - The SRE entitled in the baseline PDD refines it and initiates deployment.
  - Weave translates the finalized PDD into a Product Deployment.
  - The questionnaire is not an ontology entity.

## F. Resource Provider Resolution Policy (Q7, Q18)

### New sub-entity under section 6 or section 7

- Add **Resource Provider Resolution Policy (RPRP)** as a sub-entity of the Enclave:
  - Per (Enclave, Resource Kind) policy that resolves which Resource Provider serves a given RSD based on (Landlord, Enclave, Tenant, Product Deployment).
  - Velos maintains the RPRP registry for CSP resources. Elenchos maintains the registry for non-CSP resources.
  - Default for CSP resources: configured by World SRE.
  - Default for non-CSP resources: resolve within same Enclave only.
  - Cross-Enclave resolution: explicitly requested in PDD, reviewed and whitelisted by World SRE, who provisions enablement infrastructure.
  - Schema content is out of scope.

### Changes to section 15 (Relationships Reference)

- Add row: `Enclave | has | RPRP | 1 : N`

## G. Velos dual-role for CSP resources (Q8, Q9)

### Changes to section 7 (Resources vs. Deployments)

- "Three Roles" table: Update the Operator MD row to note that for CSP resources, the Velos MD serves as **both** the Operator MD and the Resource Provider MD.
- Clarify that Zone-local Velos provisions both infrastructure-level CSP resources (VPCs, subnets, IAM) and application-level CSP resources (databases, queues, caches).

### Changes to section 12 (Olympus Estate Modules)

- Velos table entry: Add that Velos is both Operator and Resource Provider for all CSP resources (infrastructure and application level).

## H. K8s Control Plane scoped to Enclave (Q11, Q16)

### Changes to section 3 (Deployment Space)

- **K8s Control Plane** entity: Add constraint: "Scoped to a single Enclave — a Control Plane cannot serve Deployment Spaces from multiple Enclaves. Multiple Control Planes may exist within an Enclave."
- Keep existing: "serves one or more Deployment Spaces" and "Worker Nodes may be drawn from multiple DCs" — both still hold, now within Enclave scope.

### Changes to section 15 (Relationships Reference)

- Deployment Space rows: Add note on `K8s Control Plane` "Scoped to single Enclave"

## I. World Admin Estate (Q12, Q17)

### Changes to section 10 (Tenancy Hierarchy)

- **Estate entity**: Add that the **World Admin Estate** is a single, World-spanning Estate owned by the World Owner (acting as Landlord). All Admin Enclaves across all Zones belong to this Estate.

### Changes to section 8 (Admin Enclave and Admin Space)

- Add a sentence: "The Admin Enclave belongs to the **World Admin Estate**, a single Estate owned by the World Owner (as Landlord) that contains all Admin Enclaves across the entire World."

### Changes to section 15 (Relationships Reference)

- Add note to Estate rows about World Admin Estate.

## J. Space multiplicity within Enclave (Q10)

### Changes to section 1 (Infrastructure Hierarchy)

- **Space** entity: Add "An Enclave can have multiple Spaces of the same type, though typically one per type. The topology is a World SRE decision informed by workload isolation strategy."

## K. RRSD authorship correction (Q13)

### Changes to section 4 (Specification Hierarchy)

- **RRSD** entity: Change "published by a Resource Provider" to "authored by the Publisher Org that builds the Resource Provider and packaged within the Module Specification that includes the Resource Provider Application and its Operator."

### Changes to section 5 (Descriptor Taxonomy)

- Specification Descriptors table: Change RRSD "Authored By" from "Resource Provider" to "Publisher Org (of the RP Module Specification)"

### Changes to section 15 (Relationships Reference)

- Fix `RRSD | published-by | Resource Provider` to `RRSD | packaged-in | Module Specification (of RP)`

## L. OEP exactly one per Zone (Q14, Q20)

### Changes to section 11 (Olympus Products)

- **OEP entity**: Change "one or more deployments per Zone" to "exactly one deployment per Zone." Add: "An Estate may span Enclaves across multiple Zones; each Zone's single OEP Deployment manages only the Enclaves of that Estate that reside in its Zone."
- Relationships: Change `Deployed in: Zone/Site (one or more deployments per Zone)` to `Deployed in: Zone (exactly one per Zone)`

## M. Update todo.md

- Mark all Round 3 and follow-on questions as answered/completed.

