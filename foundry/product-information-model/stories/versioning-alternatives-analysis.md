# Versioning and Composition Management: Alternative Approaches

This document analyzes how organizations track, verify, and communicate what runs together in production — and explains why UPIM adopts a **three-tier versioning model** aligned to operational deployment boundaries: **Component Version → System Version → Product Version**.

---

## The Problem Being Solved

When a product is built from many independently versioned artifacts (services, workers, adapters, frontends), three challenges recur:

1. **Integration verification:** How do you prove that independently built artifacts work together — before production?
2. **Composition tracking:** How do you know what is running in an environment, that those versions are compatible, and what exactly was deployed on a given date?
3. **Cross-team vocabulary:** How do Build, Run, Product, Win, and customer-facing teams refer to the same composition without ad-hoc translation?

These challenges are universal in multi-system products. Different organizations solve them with different architectural and process choices — each with distinct trade-offs.

---

## Alternative Approaches

### 1. Monorepo + Continuous Integration

**Who uses it:** Google (Blaze/Bazel), Meta (Buck), some large-scale engineering organizations.

**Mechanism:** All products and shared libraries live in a single repository. Dependencies are source-level. A distributed build system resolves the full dependency graph. Every commit is tested against affected targets before landing.

**How it addresses the three challenges:**
- **Integration verification:** Continuous at HEAD. The repository state at a commit is the integration surface.
- **Composition tracking:** Implicit — commit SHA defines composition. No explicit BOM.
- **Cross-team vocabulary:** Build targets and service names; no formal capability-level vocabulary.

**Pros:** Trivial reuse; automatic integration testing; atomic cross-product changes; no compatibility matrices.

**Cons:** Build-time coupling when shared libraries change; deploy-time composition gap (services still roll out independently); massive CI infrastructure; organizational coupling; acquisitions and partners sit outside the monorepo.

**Deploy-time composition gap:** Even in a monorepo, production runs combinations never tested together in CI. Rollout phases produce cross-products of canary states. Operational mitigations (traffic analysis, rollback) replace formal composition verification — they do not eliminate the gap.

---

### 2. Consumer-Driven Contract Testing (Pact, Spring Cloud Contract)

**Who uses it:** Many microservice organizations.

**Mechanism:** Consumers define expected provider behavior. Providers run consumer contract tests. Passing contracts enable independent deployment.

**How it addresses the three challenges:**
- **Integration verification:** Pairwise only (A→B, B→C), not full flows.
- **Composition tracking:** Not addressed.
- **Cross-team vocabulary:** Service-level only.

**Pros:** Lightweight; decentralized; catches breaking API changes.

**Cons:** No whole-composition verification; no formal BOM; no product-level reference; contract drift.

**Deploy-time composition gap:** Interface compatibility at rest ≠ runtime behavior under load and realistic traffic.

---

### 3. GitOps Manifest Repositories (ArgoCD, Flux)

**Who uses it:** Kubernetes-native and cloud-native teams.

**Mechanism:** Git holds desired deployment state (Helm values, Kustomize, Application CRDs). Git history is the deployment record.

**How it addresses the three challenges:**
- **Integration verification:** Not directly — declares desired state, not verified composition.
- **Composition tracking:** Partial — manifest repo as infrastructure-level BOM.
- **Cross-team vocabulary:** Container images and tags; not capability-level.

**Pros:** Declarative; auditable; automated reconciliation.

**Cons:** Infrastructure-level, not product-capability level; unverified combinations possible; PMs and Win teams do not read manifests.

---

### 4. Release Trains / Release Bundles (SAFe, enterprise vendors)

**Who uses it:** SAFe organizations, large enterprise software vendors.

**Mechanism:** Shared cadence (Program Increment). Coordinated demos verify composition at cadence boundaries.

**How it addresses the three challenges:**
- **Integration verification:** At cadence boundaries, not continuous.
- **Composition tracking:** Informal — "what was in PI 12?" requires archaeology.
- **Cross-team vocabulary:** PI name as time boundary, not versioned composition.

**Pros:** Cross-team coordination; natural integration checkpoints.

**Cons:** Time-boxed, not versioned; no formal BOM; cadence coupling; ceremony overhead.

---

### 5. Canary + Production Verification (Netflix, large cloud-native)

**Who uses it:** Netflix (Spinnaker), Google (Borg), sophisticated deployment platforms.

**Mechanism:** Traffic-shaped rollout; automated canary analysis; roll forward or back on metrics.

**How it addresses the three challenges:**
- **Integration verification:** In production — canary is the test.
- **Composition tracking:** Deployment tooling, not a formal composition artifact.
- **Cross-team vocabulary:** Per-service only.

**Pros:** Real traffic and data; fast feedback; no separate integration environment.

**Cons:** Production risk; unacceptable for high-stakes domains; no product-level vocabulary; multi-service canaries are complex.

**Deploy-time composition gap:** Deliberately accepted and mitigated operationally. Rational when failure cost is low relative to velocity; often prohibitive for regulated fintech.

---

### 6. Formal Software Bill of Materials (AUTOSAR, DO-178C, aerospace/medical)

**Who uses it:** Safety-critical and heavily regulated industries.

**Mechanism:** Rigorous BOMs with requirements-to-component traceability; formal certification.

**How it addresses the three challenges:** All three — completely.

**Pros:** Maximum rigor; regulatory compliance built in.

**Cons:** Heavyweight; slow velocity; justified only when failure cost is extreme.

---

### 7. Service Catalogs (Backstage, Port, Cortex)

**Who uses it:** Platform engineering organizations.

**Mechanism:** Centralized service metadata — ownership, dependencies, docs, health.

**How it addresses the three challenges:**
- **Integration verification:** Not addressed.
- **Composition tracking:** Partial — existence and ownership, not version compatibility.
- **Cross-team vocabulary:** Service-level only.

**Pros:** Visibility; discoverability; extensible.

**Cons:** No composition management; no product-level vocabulary.

---

### 8. No Formal Composition Management

**Who uses it:** Startups, early-stage products, small teams.

**Mechanism:** Independent CI/CD per service; production state reconstructed from logs and tribal knowledge.

**Pros:** Zero overhead; maximum velocity.

**Cons:** Breaks at scale; no reproducibility; vocabulary fragmentation.

---

## Where Our Model Sits

```
Lightweight / CD-native                                           Heavyweight / Regulated
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  No formal       Contract    GitOps/     Canary +       Our model       Formal SBOM
│  composition     testing     Manifests   production     (Component +      (AUTOSAR,
│  (startups)      (Pact)      (ArgoCD)    verification   System +         DO-178C)
│                                          (Netflix)      Product Version)
│                                                                               │
│  ← Deploy fast, verify in prod            Verify before prod, deploy with confidence →
│  ← Service-level vocabulary               Product + operational vocabulary →
```

---

## Our Approach: Three-Tier Versioning on Operational Boundaries

UPIM versions compositions at three tiers. Each tier is a **composite system** in the systems-thinking sense — with emergent properties (latency, failure modes, workflows) that do not exist at the tier below — and a **communication bridge** across organizational scopes.

| Tier | Entity | What It Versions | Verification Scope | Communication Bridge |
|---|---|---|---|---|
| **Atomic** | **Component Version** | One deployable artifact (image, bundle, package) | Quality gates: unit/integration tests, security, performance | Engineers, CI/CD, artifact registries |
| **Integrated** | **System Version** | All Component Versions that deploy together as one operational unit | Integration verification within the System boundary: APIs, events, data consistency across Components | Build + Run + SRE ("deploy Payments System v3.1") |
| **Complete** | **Product Version** | All System Versions that constitute the product release | Certification: end-to-end tests, compliance, cross-System compatibility | Ubiquitous language — Product, Win, customers, auditors ("customer X runs Product v3.2") |

**Component** (Technical) is the atomic build and artifact unit — what CI/CD produces and tags. **System** (Technical) is the operational deployment boundary — what SRE versions and applies as a whole. **Product** (Structural) is the commercial and customer-facing whole.

### Why There Is No Module Version

**Module** (Structural) is a **functional and commercial boundary** — what the product *does* for customers ("Payments Module," "Compliance Module"). It is not an operational deployment boundary.

A Module may be realized by **multiple Systems** (many-to-many). Deploying "the Payments Module" in production is not a single atomic act — SRE deploys **Systems** (each with its own System Version), not Modules. Versioning at the Module tier would imply a deployable artifact that does not exist in operations: there is no single "Module deployment" independent of the Systems that realize it.

Treating Module as a versioning tier also duplicated System Version awkwardly after DR-035: both tried to name "what integrates before production," but at different granularities that did not match how teams actually deploy. **System Version** is the integrated tier because it matches the unit SRE operates. **Product Version** is the complete tier because it matches what customers and contracts reference.

Modules remain essential in the Definition Model — for capabilities, entitlement, PSD structure, and Epic scoping — but **composition verification and deployment versioning align to System and Product**, not Module.

| Concern | Module (Structural) | System (Technical) |
|---|---|---|
| Primary question | What business capability does this deliver? | What do we deploy and operate as one unit? |
| Versioned artifact? | No | Yes (System Version) |
| Deployed by SRE? | Indirectly (via constituent Systems) | Yes |
| Customer vocabulary | "Payments Module" (commercial) | Usually internal ("Payments System") |

### Composite Systems, Not Paperwork

System Version and Product Version are not administrative checkpoints. They are compositions whose behavior in production is more than the sum of their parts — integrated failure modes, cross-Component workflows, product-wide compliance posture. SREs operate System Versions; PMs and Win teams reason about Product Versions.

### Binding Configuration

**System Version** carries **binding configuration** — build-time choices that constrain the composition to a legal form: which adapter variant, protocol version, capability flags. Not every combination of Component Versions is valid. Binding configuration records the intended, scoped composition. Environment-specific values belong in **Deployment Specifications** (see `deployment-artifacts-analysis.md`), not in the version artifact.

**Product Version** may carry product-level binding (cross-System orchestration constraints, feature matrices) where certification requires it.

### Operator-Facing Systems Without a Separate Version Tier

Probes, reconcilers, dashboards, and automation are **ordinary Systems** in the Product Specification (Technical), distinguished by **Purpose / Serving Persona** — typically Operational Personas (Operational) rather than end-user Personas (User Experience).

They are built through Run Track engineering (Run Epics, Run Stories) and produce **Component Versions** and **System Versions** like any other System. They are **included in System Version and Product Version** composition — not segregated into a parallel "Run Artifact" or "Module Package" layer (superseded by DR-036).

Example: `payment-reconciler` may appear as a Component in `payments-system` with Serving Persona = Settlement Operator. When Payments System v3.1 is released, that Component Version is part of the System Version BOM — not a separate package version stream.

### Relationship to Deployment

Version tiers answer **what** is verified and released. **Deployment Specifications** answer **how** that release applies to a specific environment. **Deployment execution** is the governed act of applying a specification. See `deployment-artifacts-analysis.md` and `change-to-deployment-analysis.md`.

| Version Tier | Typical Deployment Specification |
|---|---|
| System Version | **System Deployment Specification** (per System, per environment) |
| Product Version | **Product Deployment Specification** (product-wide, per environment) |

There is no Module Deployment Specification — deployment scope is **System** or **Product**, matching Change Request scope in the Run Track.

---

## Suitability for Enterprise Software

This model fits enterprise contexts where:

1. **Correctness outweighs velocity in high-stakes domains.** Pre-deployment composition verification is a business requirement; production canary as the primary integration test is insufficient.

2. **Multiple teams must coordinate.** System Version and Product Version are shared reference points across Build, Run, Product, and Win.

3. **Regulatory traceability.** Auditors ask what was deployed and whether it was tested. Product Version with a BOM provides a defensible answer.

4. **Customers need stable references.** Contracts and support cases reference Product versions, not dozens of image tags.

5. **Multi-System products.** Value scales with System and Component count.

6. **Independent cadences.** Teams ship Components on different schedules; System and Product versions provide composition infrastructure when paths converge.

---

## Acknowledged Trade-offs

1. **Tooling investment.** BOM assembly, integration verification, and composition tracking require automation. Without tooling, the model becomes ceremony.

2. **Process overhead.** Formal System and Product versions add pipeline steps. Slow verification becomes a bottleneck.

3. **Cultural adoption.** Tiers must be used as vocabulary, not shelf artifacts.

4. **System boundary stability.** Frequent System restructuring (Components moved between Systems) destabilizes composition history.

5. **Combinatorial verification cost.** A Component Version in multiple Systems may require multiple System Version re-verifications.

6. **Not necessary for all products.** Small or single-System products may operate with Component + System versions only, or lighter process — the model adds most value at scale.

---

## Key Insight: The Deploy-Time Composition Gap Is Universal

Even organizations with the strongest build-time integration face composition uncertainty at deployment time. Independent rollouts produce combinations never explicitly tested together.

Our model accepts artifact-level version negotiation (teams upgrade when ready) and provides **System Version** and **Product Version** as verified composition artifacts and communication bridges. For enterprise software where correctness, traceability, and cross-team alignment matter, versioning on **operational boundaries** (Component → System → Product) — not functional Module boundaries — is the deliberate design choice recorded in **DR-036**.

---
