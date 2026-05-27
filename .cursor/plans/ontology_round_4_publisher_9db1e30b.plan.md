---
name: Ontology Round 4 Publisher
overview: "Incorporate all confirmed Round 4 answers into olympus-ontology.md: expand Publisher Org, add Specification Version Lifecycle, add Publisher-SRE responsibility matrix, update Weave Store with marketplace/enrollment/gating semantics, add RRSD version pinning, and update relationships/glossary."
todos:
  - id: publisher-org
    content: "Rewrite Publisher Org in §9: single-Publisher ownership, 1:N Product Specs, registration, visibility control, ongoing responsibility, SemVer obligation."
    status: completed
  - id: responsibility-matrix
    content: Add Publisher–SRE responsibility division subsection in §9 with confirmed table.
    status: completed
  - id: spec-version-lifecycle
    content: Add Specification Version Lifecycle Tags subsection in §14 with four tags, enforcement rules, and EoL migration deadline policy.
    status: completed
  - id: weave-store
    content: "Expand Weave Store in §11: marketplace role, acceptance gating, visibility enforcement, blacklist/EoL enforcement."
    status: completed
  - id: rrsd-version-pinning
    content: Update RRD and RRSD entities in §4 to state specific RRSD version pinning; multiple versions coexist.
    status: completed
  - id: relationships
    content: "Update §15: Publisher Org rows (registration, visibility), RRSD version pinning notes on RRD/RD rows."
    status: completed
  - id: glossary
    content: Add Specification Version Lifecycle entry and update RRSD entry in §17.
    status: completed
  - id: deferred-topics
    content: "Update §16: refine Publisher Org deferred scope; add Weave Store acceptance gating."
    status: completed
  - id: todo-update
    content: Mark all Round 4 questions as completed in todo.md.
    status: completed
isProject: false
---

# Ontology Revision Round 4 — Publisher Org

All changes target `[olympus-ontology.md](olympus-estate-ramki-docs/olympus-ontology.md)`. Section numbers refer to the current document.

## A. Publisher Org expansion (§9)

Current text (lines 964–979) is thin — "authors and publishes specifications and artifacts." Rewrite to capture:

- **Single-Publisher ownership**: A Product Specification and all its Module Specifications are authored by one Publisher Org. Module Specifications of other Publishers are not visible or accessible.
- **1:N Product Specs**: A Publisher Org may publish multiple Product Specifications.
- **Product Specification registration**: Before publishing, a Publisher registers Module and Product Specifications with the Weave Store, receives identifiers, and associates signing keys. (Registration is performed via Publisher Home — an operational app, not an ontology entity.)
- **Visibility control**: Publisher controls Product Specification visibility to specific Landlords, Sites, and Zones at registration time. Can expand or restrict later. Changes are prospective only — existing deployments, Tenants, and SREs are unaffected. Visibility is per Product Specification (not per version, not per Module Spec).
- **Ongoing responsibility**: Publisher is fully responsible for product quality, maintenance, technology obsolescence, bug resolution SLAs, roadmap, customer support, and incident participation. Specifies on-call and escalation matrix per Product Specification (captured via Publisher Home, not a descriptor).
- **SemVer obligation**: Minor versions must be strictly backward compatible. Major versions may remove capabilities or change contracts.

### Updated relationships

- Has: IDP Domain (1 : 1)
- Admitted by: World Owner Org (N : 1)
- Authors: Module Specification, Product Specification (1 : N, single-Publisher per Product)
- Publishes to: Weave Store (N : 1)
- Registers with: Weave Store (identifiers, signing keys)
- Controls visibility of: Product Specification (per Landlord, Site, Zone)

## B. Publisher–SRE responsibility matrix (§9 or new subsection)

Add a subsection after SRE Org (or between Publisher Org and SRE Org) titled "Publisher–SRE Responsibility Division." Include the confirmed table:


| Domain                      | Publisher                           | SRE                            | Shared                         |
| --------------------------- | ----------------------------------- | ------------------------------ | ------------------------------ |
| Functional defects          | Root cause, fix, publish patch      | Deploy patch via MDD update    | Incident bridge                |
| Performance                 | Realistic RRDs                      | Adequate RSDs; tune deployment | Diagnosis                      |
| Security vulnerabilities    | Patch and publish                   | Deploy; enforce blacklist      | Coordinated remediation        |
| Roadmap and features        | Build with feature flags            | Roll out via Blue-Green MDIs   | Feedback channeling            |
| Tenant Subscription issues  | Fix Questionnaire/TSD logic         | Elenchos/Weave health          | Product vs. platform diagnosis |
| Operator/Resource lifecycle | Correct Operators, RRSDs, RDs       | Healthy RPRP and Operator MDs  | Provisioning failures          |
| Technology obsolescence     | Migrate specs to supported runtimes | Coordinate rollout             | Timeline negotiation           |


## C. Specification Version Lifecycle (§14)

Add a new subsection "Specification Version Lifecycle Tags" in §14 (Lifecycle and Versioning), after the SemVer paragraph. This is new content:

- Four lifecycle tags applicable to both Product Specification and Module Specification versions independently:


| Tag                    | Meaning                              | Platform Enforcement                                                                                                       |
| ---------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| `blacklisted`          | Not suitable for use                 | Weave refuses new PDs/MDIs from this version. Existing PDs continue running.                                               |
| `deprecated`           | Superseded; migration recommended    | Informational only; no enforcement                                                                                         |
| `EoS` (End of Support) | Publisher stops bug fixes            | Contractual; no platform enforcement                                                                                       |
| `EoL` (End of Life)    | Must not be used for new deployments | Weave refuses new deployments. SREs must migrate existing PDs within deadline. Exceeding deadline is a contract violation. |


- EoL migration deadline: default is a **World-level policy**, overridable per Product Specification.
- Tags are set by the Publisher.

## D. Weave Store expansion (§11)

Update the Weave Store entity (lines 1285–1299) to add:

- **Marketplace role**: The Weave Store serves as a marketplace — Landlords discover and select Product Specifications for deployment through it.
- **Acceptance gating**: New Product/Module Specifications and new versions undergo acceptance gating before availability. Details out of scope.
- **Visibility enforcement**: Enforces Publisher-set visibility controls on Product Specifications (per Landlord, Site, Zone).
- **Blacklist/EoL enforcement**: Weave enforces version lifecycle tags — refuses new PDs from blacklisted or EoL versions at PDD translation time.

## E. RRSD version pinning (§4)

Update the RRD entity (lines 461–477) and RRSD entity (lines 478–494) to state:

- RRDs, RSDs, and Resource Descriptors all reference a **specific RRSD version**.
- Multiple RRSD versions coexist in the Weave Store; each version is treated as a different resource kind.
- Existing deployments referencing an older RRSD version are unaffected by new RRSD versions.

## F. Relationships Reference updates (§15)

### Identity and Organization

- Update `Publisher Org | publishes-to | Weave Store` to add note: "Signed OCI; single-Publisher per Product Spec"
- Add: `Publisher Org | registers-with | Weave Store | 1 : 1 | No | Identifiers, signing keys`
- Add: `Publisher Org | controls-visibility | Product Specification | 1 : N | No | Per Landlord, Site, Zone; prospective only`

### Specification Hierarchy

- Add note to `RRD | schema-from | RRSD` row: "References specific RRSD version"
- Add note to `Resource Descriptor | schema-from | RRSD` row: "References specific RRSD version"

## G. Glossary updates (§17)

- Add **Specification Version Lifecycle** entry summarizing the four tags and their enforcement.
- Update **RRSD** entry to note version pinning: RRDs/RSDs/RDs reference specific versions; multiple coexist.

## H. Deferred Topics update (§16)

- Update "Publisher Org internal structure" to note that ongoing responsibilities (quality, SLAs, roadmap, on-call) are now described in §9 and the responsibility matrix. Internal team structure, publication pipeline internals, and Publisher Home UI details remain out of scope.
- Add: "Weave Store acceptance gating details" as a deferred topic.

## I. Update todo.md

- Mark all Round 4 questions (Q1–Q21) as completed with summary.

