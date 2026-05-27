---
name: olympus ontology revision
overview: Revise [olympus-diagrams/olympus-ontology.md](/Users/ramki/Git/personal-projects/olympus-diagrams/olympus-ontology.md) to (a) apply the corrections you've already confirmed, (b) capture the new World/Estate/Tenant axis (Landlord, Tenant Org, Estate, Lease, Ownership, IDP Domain, Olympus World Product, Olympus-World-Connect, Weave Store), (c) add a per-entity "Relationships" subsection, and (d) add a comprehensive Relationships Reference matrix at the end so no context built in this thread is lost.
todos:
  - id: corrections
    content: Apply targeted corrections from prior round (§3, §4, §6, §8, §9, §10, §11, cardinality fixes)
    status: completed
  - id: world-identity-section
    content: Add new §8 — World, Identity, and Organizations (Org vs IDP Domain; 5 Org roles incl. Publisher Org and SRE Org; World Owner SRE Org; dual-role)
    status: completed
  - id: publisher-spec-descriptors
    content: Update §4 Specification Hierarchy — add Application Descriptor, Resource Descriptor, RRD as three distinct documents in Module Spec; add signed-OCI references; reflect Publisher authoring
    status: completed
  - id: tsd-provenance
    content: Correct TSD provenance in current §8/new §9 — TSD is produced by the Product's subscription request management (Tenant-initiated via Olympus World UI; widget from Product Spec); not authored by SREs
    status: completed
  - id: weave-store-publisher
    content: Update §10 Olympus Products — Weave Store packaging format (signed OCI), Publisher key registration, subscription initiation UI shell on Olympus World Product
    status: completed
  - id: tenancy-rewrite
    content: Rewrite §9 Tenancy Hierarchy — Landlord, Tenant Org, Tenant, Estate, Ownership, Lease (first-class), Product/Module Subscription, TSD, lifecycle states (pending user confirmation per §F)
    status: completed
  - id: olympus-products-section
    content: Add new §10 — Olympus Products and the World/Estate Layering (Olympus Estate Product, Olympus World Product, Olympus World Site, Olympus-World-Connect, Weave Store, Bootstrap Workstation, World Descriptor, Deployment Train stub)
    status: completed
  - id: modules-corrections
    content: Update §11 Olympus Estate Modules — Velos and Atlantis scope tightened
    status: completed
  - id: overlapping-expand
    content: Expand §12 Overlapping Hierarchies — add Tenancy and Olympus-Product-Layering axes, new join-point bullets
    status: completed
  - id: lifecycle-versioning
    content: Update §13 Lifecycle and Versioning — drop ArgoCD gloss, add Tenant Subscription Lifecycle + Readiness axes (pending §F)
    status: completed
  - id: per-entity-relationships
    content: Add inline 'Relationships' subsection at the end of every entity definition (existing and new)
    status: completed
  - id: relationships-reference
    content: Add new §14 — Relationships Reference matrix (Source / Edge / Target / Cardinality / Containment / Axis / Notes)
    status: completed
  - id: deferred-section
    content: Add new §15 — Deferred Topics (Publisher, SRE, Deployment Train, Provider-selection criteria, Blue-Green cut-over)
    status: completed
  - id: glossary-additions
    content: Add new disambiguation entries to §16 Glossary (Estate vs Olympus Estate Product, Org vs IDP Domain, World vs Estate, Olympus-World-Connect, dual-role, Deployment Train)
    status: completed
  - id: toc-update
    content: Update Table of Contents to reflect renumbering and new sections
    status: completed
  - id: ts-states-confirm
    content: Get user confirmation on (a) Lifecycle state set §F1 and (b) Readiness state set §F2 before writing them into §9 and §13
    status: completed
isProject: false
---

# Olympus Ontology Revision Plan

## A. Targeted corrections to existing sections

These are the items you confirmed in the prior round; applied as in-place edits, no new sections.

- **§3 Deployment Space** — Remove the "k8s namespace" bullet from Properties (k8s namespace is at MDI level, not Deployment Space).
- **§3 Auxiliary Entities → Service Catalog** — Drop the enforcement-mechanism examples ("IAM policies, SCPs, organization policies"); keep the generic "policies the CSP enforces."
- **§3 Worker Node** — Tighten scope to "dedicated to the Deployment Spaces it serves," remove any implication of "all in the Zone."
- **§4 Application kinds table** — Mark the table as non-exhaustive ("…or so"); drop the manufactured **Probe Application** row (or mark TBD); keep the user-confirmed examples (k8s Deployment/CronJob/DaemonSet, Flink Job, BPMN Workflow).
- **§5 Module Deployment Instance** — Add: "Each MDI has a dedicated Kubernetes namespace within the Deployment Space's K8s Control Plane."
- **§6 Three Roles in the Resource Lifecycle** — Keep as written; states are user-approved.
- **§6 Resource Lifecycle States** — Mark this list as **illustrative**, not normative.
- **§8 Tenant Subscription Descriptor** — Soften "created or modified" → "changes" (creation, amendment, termination, etc.).
- **§9 Olympus Estate Modules table**:
  - **Velos** — Tighten to "spawns Spaces and inter-Space network routes based on Space Specifications." Remove the "Enclaves" claim.
  - **Atlantis** — Drop "canonical Application Runtime for K8s Operator pattern." Keep "manages K8s Control Planes and provisions Worker Nodes; hosts platform Operators."
- **§10 Join Points** — Remove the trailing "and a k8s namespace" from the Deployment Space description.
- **§11 Module Deployment Lifecycle States** — Drop the "health and sync status models" gloss; just say "uses Argo CD Application status semantics."
- **Cardinality fix** — Tenant Subscription : Product Deployment is **N : 1** (multiple Tenant Subscriptions for the same Product Deployment). Update §8 and §10 accordingly.

## B. New entities to introduce

Each entity gets a definition block with: **Purpose / Role / Key attributes / Relationships** (the "Relationships" sub-block is the inline half of the hybrid format you chose).

### B1. Identity & organization (new)

- **Organization (Org)** — Generic concept; one of: World Owner Org, Landlord Org, Tenant Org, Publisher Org, SRE Org. Holds contracts, contacts, etc. (details out of scope here).
- **IDP Domain** — A domain in the World IDP. **Distinct entity** from Org with a 1:1 association — never conflated. The same IDP Domain can serve both a World Owner Org and a Landlord Org (i.e., one Org acts in two roles via a shared IDP Domain).
- **World Owner Org** — Owns the World. Acts also as a Landlord (dual role) so it can create shared/leasable Estates. Also operates a built-in **World Owner SRE Org** with cross-World access.
- **Landlord Org** — An Org that owns or leases Estates. Whitelists Tenants to its Estates. Assigns an SRE Org to each Product Deployment in its Estates.
- **Tenant Org** — A customer organization that holds one or more Tenants. Tenants are whitelisted by a Landlord to one or more of that Landlord's Estates.
- **Publisher Org** (NEW) — A standalone Org with its own IDP Domain; admitted to the World by the World Owner. Multiple Publisher Orgs may exist in a World. Publishes Module/Product Specifications and all referenced binary artifacts (containers, Helm/OCI charts, Operator binaries, JARs, npms, etc.) to the **Weave Store** as **signed OCI** artifacts. Registers the **public keys** of its signing keys with the Weave Store. Encouraged to publish Specs and binary artifacts independently and reference them by signed-OCI reference inside Application Descriptors and Resource Descriptors of a Module Specification (optimizes change-cost; supports typical build pipelines).
- **SRE Org** (NEW) — A standalone Org with its own IDP Domain. **Assigned per Product Deployment** by the Landlord that owns the Estate the Product Deployment runs in. SRE authoring authority covers: **MDDs** (Module Deployment Descriptors), **Blue/Green rollout decisions**, **Spec-version coexistence decisions** within an Enclave. SRE does **not** author TSDs (see §B5). The **World Owner SRE Org** is a built-in SRE Org with access to all Enclaves across the World, governed by internal roles and policies.

### B2. Tenancy axis (new + replacing the invented Tenant content in §8)

- **Estate** — A logical entity owned or leased by a Landlord. **Lives in the Tenancy axis, not in the Infrastructure hierarchy.** Has 1:N association to Enclaves (an Enclave belongs to exactly one Estate; an Estate may have many Enclaves potentially across Sites/Zones).
- **Ownership** — First-class entity. Attributes: `start, end, terms`. References a Landlord Org and an Estate. Exclusive (only one Ownership per owned Estate at any time).
- **Lease** — First-class entity. Attributes: `start, end, terms`. References a Landlord Org (lessee) and an Estate (leased). May be concurrent — some Estates support multiple concurrent Leases by different Landlords (those created by the World Owner for sharing); other Estates are owned and exclusive.
  - **Lease termination semantics:** When a Lease terminates, all dependent Tenant Subscriptions move to `inactive` with reason code `lease-terminated`.
- **Tenant** — A subscribing customer entity within a Tenant Org. Whitelisted by a Landlord to one or more of that Landlord's Estates (owned or leased). May subscribe to Products **deployed in Enclaves of those Estates**.
- **Product Subscription / Module Subscription** — Keep as defined; clarify that a Product Subscription is for a **Product Deployment** (in an Enclave of an accessible Estate), and **N Tenant/Product Subscriptions : 1 Product Deployment**.
- **Tenant Subscription Descriptor (TSD)** — Already present; tightened wording per §A.

### B3. Olympus Products & cross-World plumbing (new section, see §C2)

- **Olympus Estate Product** — A specialized Product Spec (already implied) deployed once per Zone (or per Enclave subset of an Estate). Its modules are Atlantis/Velos/Weave/Elenchos.
- **Olympus World Product** — A specialization/extension of Olympus Estate Product, deployed exclusively in an **Olympus World Site** (a Site reserved for the World Owner). One per World. Manages Orgs, Estates, Sites, and spawns Olympus Estate Product deployments in other Sites. Provides the Tenant-facing **subscription initiation mechanism** (UI shell that hosts each Product Deployment's Subscription Questionnaire).
- **Olympus World Site** — A Site like any other, but reserved for the World Owner's Olympus World Product deployment. Follows the same Site/Zone/Enclave/Space semantics.
- **Olympus-World-Connect** — The two-way bridge maintained by the Olympus World Product deployment to all Olympus Estate Product deployments across the World. Aggregates telemetry, propagates Deployment Trains, etc. Detailed scope is out of this document.
- **Weave Store** — World-level artifact repository. Holds container images, all packaged Module/Product Specifications, descriptors (MDD, TSD, RSD, Space Spec, Zone Spec, etc.), and any other binary artifacts referenced from those Specifications. **Defines the OCI-based packaging format** that Weave can accept; all Publisher submissions must be **signed OCI** artifacts. Holds the **registered public signing keys** of every Publisher Org admitted to the World. Referenced by Weave deployments across the World.
- **Bootstrap Workstation** — Transient device. Defined in the **World Descriptor**'s `BootstrapWorkstationDescriptor` (endpoints, identity, credentials). The World Site enables this workstation only for break-glass sessions.
- **World Descriptor** — Configuration document describing the World — World Owner Org, IDP Domain, Bootstrap Workstation Descriptor, etc. Drives the World's bootstrap.
- **Deployment Train** — Out-of-scope descriptor (handled by Olympus World Product) that defines how a Product or Module Deployment version promotes across Deployment Instances. **Mention only as a stub** with "scope: Olympus World Product (out of scope of this document)."

### B4. Specification-side gaps already in the doc but to be tightened

- **Application** — Existing definition is acceptable; add a note that the kind list is open-ended.
- **Operator** — Already present; no changes.
- **RRD / RSD / Service Catalog / Service Account / K8s Control Plane / Worker Node** — Already present; only the corrections in §A.

### B5. New Specification-side entities (Publisher's outputs)

These three are **distinct documents** that all live inside a Module Specification, addressing the descriptor terminology you confirmed:

- **Application Descriptor** (NEW) — One per Application in the Module Specification. References the Application's binary artifacts (container images, Helm charts, etc.) by **signed-OCI reference**. Authored by the Publisher.
- **Resource Descriptor** (NEW) — One per resource the Module **provides** to other modules (i.e., resources the Module's Operators can vend). Distinct from RRD. Authored by the Publisher.
- **Resource Requirement Document (RRD)** — Existing entity. One per resource the Module **requires** from another module or from the platform. Will be re-stated as the third member of the Descriptor triad in §4 to make the distinction explicit.

The Module Specification is therefore the composition of: Applications (each with an Application Descriptor), Resources Provided (each with a Resource Descriptor), Resources Required (each with an RRD), and Operators.

### B6. TSD provenance correction (NEW finding from this session)

The current doc implies TSDs are authored by SREs. **They are not.** TSDs are produced by the **subscription request management capabilities of the Product**, not by SREs:

- The Olympus World Product provides the mechanism for a Tenant to **initiate a Subscription** to a Product Deployment.
- The Product Deployment then presents a **Subscription Questionnaire (widget)** that collects Tenant input.
- The widget output is materialized as a **TSD** for that Tenant.
- Elenchos consumes the TSD to provision Tenant-scoped resources.

The Subscription Questionnaire/widget is **part of the Product Specification** (authored by the Publisher as part of the Subscription Management Operators already noted in §4). The Product Deployment instantiates it; Olympus World provides the chrome/UI shell that hosts it.

**Modeling decision (per your direction):** Subscription Request and Subscription Questionnaire are described **narratively** in the TSD section — not introduced as first-class entities. Only the TSD remains a first-class artifact.

In §8 (current TSD section) and §9 (new Tenancy Hierarchy):

- Remove any implication that SREs author TSDs.
- Add the narrative subscription-initiation flow.
- Add a one-line reference inside Product Specification's Subscription Management Operators noting the questionnaire is part of those Operators.

## C. New / restructured sections

### C1. Renumbering

Insert new sections between current §7 and §8, push everything down. Proposed order:

1. Infrastructure Hierarchy (unchanged)
2. Cloud Service Provider Hierarchy (unchanged)
3. Deployment Space (corrections)
4. Specification Hierarchy (corrections)
5. Deployment Hierarchy (corrections)
6. Resources vs. Deployments (mark lifecycle as illustrative)
7. Admin Enclave and Admin Space (unchanged)
8. **NEW — World, Identity, and Organizations**
9. **REWRITE — Tenancy Hierarchy** (Landlord, Tenant Org, Tenant, Estate, Ownership, Lease, Product/Module Subscription, TSD, lifecycle states)
10. **NEW — Olympus Products and the World/Estate Layering** (Olympus World Product, Olympus Estate Product, Olympus World Site, Olympus-World-Connect, Weave Store, Bootstrap Workstation, World Descriptor, Deployment Train stub)
11. Olympus Estate Modules (corrections; this section is now scoped to the **Estate** product's modules)
12. Overlapping Hierarchies (expand to **seven** axes — add Tenancy and Olympus-Product-layering)
13. Lifecycle and Versioning (corrections + add Tenant Subscription **lifecycle and readiness** axes)
14. **NEW — Relationships Reference** (matrix; see §D)
15. **NEW — Deferred Topics** (Publisher, SRE)
16. Glossary and Disambiguation (additions)

### C2. Section 8 — World, Identity, and Organizations (new)

Defines:

- World as a configured entity (per World Descriptor).
- Org vs. IDP Domain distinction (1:1, never conflated).
- **Five Org roles**: World Owner Org, Landlord Org, Tenant Org, **Publisher Org**, **SRE Org**.
- Same IDP Domain may back World Owner Org and Landlord Org (dual-role); World Owner also operates a built-in World Owner SRE Org.
- Org → IDP Domain → World relationships.
- Publisher Org admission by World Owner; SRE Org assignment by Landlord per Product Deployment.

Includes a small ASCII map:

```
World
 ├── World Owner Org    ── IDP Domain (may be shared)
 │     ├── (acts as Landlord Org for shared Estates)
 │     └── World Owner SRE Org   ── IDP Domain
 ├── Landlord Org(s)    ── IDP Domain(s)
 │     ├── Estate(s) (Owned or Leased)
 │     └── (assigns SRE Org per Product Deployment)
 ├── Publisher Org(s)   ── IDP Domain(s)
 │     └── Publishes to Weave Store (signed OCI)
 ├── SRE Org(s)         ── IDP Domain(s)
 │     └── Assigned per Product Deployment
 └── Tenant Org(s)      ── IDP Domain(s)
       └── Tenant(s)
```

### C3. Section 9 — Tenancy Hierarchy (rewrite of current §8)

Replaces the invented entity definitions with confirmed ones. Structure:

- Landlord-side: Landlord Org → Estate (with Ownership / Lease as first-class entities).
- Tenant-side: Tenant Org → Tenant → Product Subscription → Module Subscription.
- Bridge: Tenant whitelisted to Estate; Product Subscription pinned to a Product Deployment in an Enclave of an accessible Estate.
- **Subscription initiation flow (narrative)** — Tenant initiates a Subscription via the Olympus World Product UI; the Product Deployment presents its Subscription Questionnaire (widget shipped in the Product Spec by the Publisher); the widget output is materialized as a **TSD**; Elenchos consumes the TSD.
- **TSD provenance correction** — TSD is produced by the Product's subscription request management capability, **not** by SREs.
- **Tenant Subscription state — two orthogonal axes:** Lifecycle and Readiness (see §F).

Includes ASCII tree showing both sides joined at the Estate ↔ Tenant whitelist edge.

### C4. Section 10 — Olympus Products and the World/Estate Layering (new)

- Olympus Estate Product (per-Zone scope; subset of Enclaves possible).
- Olympus World Product (one per World; runs in Olympus World Site; specialization of Estate Product).
- Olympus World Site (a regular Site, exclusive to World Owner).
- Olympus-World-Connect (the bridge: telemetry aggregation, Deployment Trains, etc.).
- Weave Store (artifact repo at World scope).
- Bootstrap Workstation + World Descriptor (bootstrap chain).
- Deployment Train (stub).

Includes a layering diagram (ASCII) of: World → World Site → World Product Deployment → Olympus-World-Connect → Estate Product Deployments in other Sites.

### C5. Section 12 — Overlapping Hierarchies (expand)

Add two more axes to the table and the cross-cutting notes:

- **Tenancy** — Landlord Org → Estate → (Enclaves), and Tenant Org → Tenant → Product Subscription → Module Subscription.
- **Olympus Product Layering** — Olympus World Product → (Olympus Estate Product deployments) via Olympus-World-Connect.

Add new join-point bullets:

- **Estate ↔ Enclave** (1 : N; an Enclave belongs to exactly one Estate).
- **Tenant Subscription ↔ Product Deployment** (N : 1).
- **Olympus World Product ↔ Olympus Estate Product Deployments** (1 : N via Olympus-World-Connect).

## D. Per-entity Relationships subsections + comprehensive Reference (hybrid)

### D1. Inline per-entity "Relationships" subsection

For every entity (existing and new), add a small **Relationships** block at the end of its definition listing direct edges, e.g.:

> **Relationships**
>
> - Contains: Site (1 : N)
> - Configured by: World Descriptor (1 : 1)
> - Owned by: World Owner Org (1 : 1)

This replaces ad-hoc "Belongs to / Contains / Used by" bullets currently scattered through the doc; keeps narrative tight.

### D2. New Section 14 — Relationships Reference (matrix)

A single comprehensive table at the end indexing every relationship with these columns:

- **Source entity**
- **Edge / verb** (contains, uses, belongs-to, owns, leases, hosts, manages, tagged-to, federates, derives-from, satisfies, deploys, orchestrates, bridges, ...)
- **Target entity**
- **Cardinality** (1:1 / 1:N / N:1 / N:M)
- **Containment** (Yes/No — does this edge represent containment?)
- **Hierarchy axis** (Infrastructure / CSP / Specification / Deployment / Tenancy / Olympus-Product-Layering / Cross-cutting)
- **Notes** (e.g. "scoped to Zone", "via Operator MD")

Grouped by source-entity hierarchy. Goal: every fact stated in narrative is also reflected as a row, so the matrix is the lookup index of the ontology.

A condensed set of cross-axis edges to call out explicitly:

- Estate → Enclave (1 : N, Tenancy → Infrastructure)
- Tenant → Estate (N : M, via whitelist; Tenancy)
- Tenant Subscription → Product Deployment (N : 1; Tenancy → Deployment)
- Module Deployment → Module Specification (N : 1; Deployment → Specification)
- Resource → DC + Consuming MD + Operator MD + Resource Provider MD (4 tags)
- MDI → K8s Namespace (1 : 1; Deployment → Infrastructure-runtime)
- Olympus World Product Deployment → Olympus Estate Product Deployments (1 : N via Olympus-World-Connect)
- Lease / Ownership → (Landlord Org, Estate)
- IDP Domain → Org (1 : 1, but conceptually distinct)

## E. Updates to Glossary (§16)

Add disambiguation entries:

- **Estate vs. Olympus Estate Product** — Estate is a logical entity in the Tenancy axis; Olympus Estate Product is the meta-Product whose deployment runs the platform for an Estate's Enclaves.
- **Org vs. IDP Domain** — 1:1 but distinct entities; never conflated.
- **Olympus World vs. Olympus Estate** — World Product is a specialization of Estate Product; deployed exclusively in the Olympus World Site.
- **Olympus-World-Connect** — The bridge; out-of-scope details.
- **World Owner Org as Landlord** — Dual role to enable shared Estates.
- **Deployment Train** — Out-of-scope descriptor.
- **Lifecycle vs. Readiness (axis distinction)** — One-line note that Tenant Subscription state is reported as `(lifecycle, readiness)` and that the Readiness pattern may extend to other entities in a future revision.
- **Application Descriptor vs. Resource Descriptor vs. RRD** — Three distinct documents inside a Module Specification: Application Descriptor (per Application; references binary artifacts), Resource Descriptor (per resource the Module provides), RRD (per resource the Module requires).
- **Operator (entity) vs. Operator MD (runtime) vs. SRE Org (people-org)** — Operator is an Application kind; Operator MD is the Module Deployment in Admin Space that hosts an Operator; SRE Org is the human Org that authors MDDs and operates Product Deployments. Three different things — never conflated.
- **TSD provenance** — TSDs are produced by the Product's subscription request management capability (initiated by the Tenant via Olympus World UI; widget shipped by Publisher in the Product Spec); **not** authored by SREs.

## F. Tenant Subscription state — two orthogonal axes (confirmed)

A Tenant Subscription's state is described by **two independent axes** (consistent with the ArgoCD-style pattern already adopted for Module Deployments). A subscription is therefore reported as `(lifecycle, readiness)`.

### F1. Lifecycle axis — operational state (CONFIRMED)


| State          | Meaning                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `pending`      | Subscription requested; not yet provisioned                                                                                            |
| `provisioning` | Elenchos is provisioning Tenant-scoped resources from the TSD                                                                          |
| `active`       | Provisioned and operational                                                                                                            |
| `updating`     | Subscription change (plan/entitlement/config) being applied                                                                            |
| `suspended`    | Temporarily disabled (non-payment, policy, planned maintenance); resources retained                                                    |
| `degraded`     | Partial functionality; some Tenant-scoped resources unavailable                                                                        |
| `terminating`  | Deprovisioning in progress                                                                                                             |
| `inactive`     | Terminated; resources released. Reason codes include `lease-terminated`, `customer-cancelled`, `non-payment`, `policy-violation`, etc. |
| `archived`     | Record retained for audit; no resources                                                                                                |


### F2. Readiness axis — input/configuration state (CONFIRMED)

Captures whether the subscription is awaiting input from a counter-party. **Independent of the lifecycle axis** — a subscription can be `(active, waiting-tenant-input)` and still be operationally serving traffic for the parts of the Module that don't depend on the missing input.


| State                    | Meaning                                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ready`                  | All required inputs present; subscription is fully configured                                                                                    |
| `waiting-tenant-input`   | One or more Tenant-scoped RSDs/configurations are required from the Tenant before recently-changed module functionality can be fully provisioned |
| `waiting-landlord-input` | One or more inputs are required from the Landlord (e.g., new TSD-side terms not yet acknowledged)                                                |


Triggers for entering `waiting-*-input` (CONFIRMED):

- A Module Deployment update that introduces or changes a Tenant-scoped RRD.
- A Landlord-side TSD change requiring tenant acknowledgement.
- A policy/compliance change requiring re-input.
- A tenant opt-in to a newly available capability.

### F3. Scope decision (CONFIRMED)

The Readiness axis is being introduced **only on Tenant Subscription** in this revision. A short note in the Glossary will flag that the same orthogonal pattern (lifecycle + readiness) may extend to other entities (Module Deployment, Resource) in a future revision, but no other entity gets a Readiness axis right now.

All open items in §F are now confirmed. No further confirmation needed before writing.

## G. Deferred topics — new placeholder section

Section 15 — **Deferred Topics** with sub-stubs:

- **Publisher Org internal structure** — The Org and its publishing semantics are now in §8 (no longer fully deferred). Internal team/role structure of a Publisher remains out of scope.
- **SRE Org internal structure** — The Org and its assignment/authoring authority are now in §8 (no longer fully deferred). Internal on-call/team structure of an SRE Org remains out of scope.
- **Deployment Train semantics** — Out of scope; owned by Olympus World Product / Weave docs.
- **Estate-admin Resource Provider selection criteria** — Out of scope.
- **MDI promotion / Blue-Green cut-over** — Out of scope (Deployment Orchestration doc).

This makes the deferrals explicit so future revisions know what's missing.

## H. Table of Contents update

Update the ToC at the top of the doc to reflect the renumbering and new sections (§8, §9 rewrite, §10, §14, §15).

## I. Working approach (per your earlier feedback)

- I will **not** invent state names, role names, lifecycle stages, or attribute lists beyond what's explicitly captured here.
- I will **stop and ask** before writing any section that needs a detail not already in this plan.
- All edits will be in-place to [olympus-diagrams/olympus-ontology.md](/Users/ramki/Git/personal-projects/olympus-diagrams/olympus-ontology.md); no new files.

All open confirmation items have been resolved (Tenant Subscription Lifecycle + Readiness; Publisher Org structure + artifacts; SRE Org structure + authority; TSD provenance; descriptor terminology; Subscription initiation flow). Ready to execute on your go-ahead.