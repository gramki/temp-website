# Versioning and Composition Management: Alternative Approaches

This document analyzes alternative approaches to the composition management problem — how organizations track, verify, and communicate what's running together in production — and explains why UPIM's three-tier versioning model (System Version → Module Version → Product Version) is designed for enterprise software contexts.

---

## The Problem Being Solved

When a product is composed of independently built and deployed systems (microservices, services, components), three challenges arise:

1. **Integration verification:** How do you verify that independently built systems work together — before production?
2. **Composition tracking:** How do you know what's running in production, that those versions are compatible, and what exactly was deployed on a given date?
3. **Cross-team vocabulary:** How do Build, Run, Product, Win, and customer-facing teams refer to the same thing without ad-hoc translation?

These challenges are universal in multi-system products. Different organizations address them through different architectural and process choices — each with distinct trade-offs.

---

## Alternative Approaches

### 1. Monorepo + Continuous Integration

**Who uses it:** Google (Blaze/Bazel), Meta (Buck), some large-scale engineering organizations.

**Mechanism:** All products and shared libraries live in a single repository. Dependencies are source-level — you import directories, not versioned artifacts. A distributed build system (Bazel) resolves the full dependency graph. Every commit is tested against all affected targets before landing.

**How it addresses the three challenges:**
- **Integration verification:** Continuous at HEAD. Every commit is tested against all dependents. The repo *is* the integration verification.
- **Composition tracking:** Implicit — the repo state at any commit SHA defines the composition. No explicit BOM needed.
- **Cross-team vocabulary:** Partially addressed through build targets and service names. No formal capability-level vocabulary.

**Pros:**
- Subsystem reuse is trivial — just import the directory. No version negotiation.
- Integration testing is automatic and continuous.
- Atomic cross-product changes — update a shared library and all consumers in one commit.
- No compatibility matrices or version ranges to manage.

**Cons:**
- **Build-time coupling:** A change to a shared library blocks until *all* dependents build and test successfully. If Product B is failing for unrelated reasons, the shared-library author is blocked. The more widely a library is reused, the harder it is to change.
- **Deploy-time composition gap:** Even in a monorepo, independently deployable build targets roll out at different times. Production runs A@SHA-100 + B@SHA-105 + C@SHA-90 — a combination never tested together in CI. The monorepo's "everything at HEAD" testing is a build-time truth, not a production-time truth. Each service's rollout phase produces its own dependency graph that must be tracked for compatibility.
- **Massive CI infrastructure:** Requires distributed build systems, test sharding, and build caching at scale. Most organizations cannot afford this.
- **Organizational coupling:** All teams are coupled through source-level dependencies. Different deployment cadences (weekly vs. quarterly) create friction — slow teams constrain fast teams unless decoupled by feature flags.
- **Acquisitions and boundaries:** External systems, acquired codebases, and partner integrations are not in the monorepo. At organizational boundaries, you're back to artifact-level versioning.

**Deploy-time composition gap:** The monorepo eliminates the build-time version negotiation problem but does not solve the deploy-time composition problem. During canary rollouts, different production instances run different versions of the same service. Cross-service calls during rollout may hit canary or baseline instances nondeterministically. The actual production composition at any moment is a cross-product of all rollout states — a combination that was never explicitly tested. Google mitigates this through canary traffic analysis, rollback automation, and blast-radius control — but these are operational mitigations, not formal verification.

---

### 2. Consumer-Driven Contract Testing (Pact, Spring Cloud Contract)

**Who uses it:** Many microservice organizations; popularized by ThoughtWorks and the Pact community.

**Mechanism:** Each service defines contracts with its consumers. A consumer specifies what it expects from a provider (request/response pairs). The provider runs the consumer's contract tests against its own codebase. If contracts pass, services are independently deployable.

**How it addresses the three challenges:**
- **Integration verification:** Pairwise — each consumer-provider pair is verified independently. No whole-composition verification.
- **Composition tracking:** Not addressed. No BOM, no composition artifact.
- **Cross-team vocabulary:** Not addressed. Service-level only.

**Pros:**
- Lightweight and decentralized — no centralized integration testing environment needed.
- Enables independent deployment — if contracts pass, each service can deploy independently.
- Catches breaking API changes before deployment.
- Well-supported tooling ecosystem (Pact, Spring Cloud Contract).

**Cons:**
- **Pairwise only:** Verifies A→B and B→C independently, but does not verify A→B→C as a flow. Emergent multi-service interaction failures (timing, ordering, cascading failures) are not caught.
- **No composition artifact:** "What versions work together?" has no formal answer. Compatibility is implied by passing contracts, not declared in a BOM.
- **No capability-level vocabulary:** PMs and Win teams cannot reference a contract test result. No Module Version or Product Version equivalent.
- **Contract drift:** If consumer contracts are not updated as consumer code evolves, contracts become stale and provide false confidence.

**Deploy-time composition gap:** Contract testing verifies interface compatibility at rest, not runtime composition under load. A system that passes all contracts may still fail in production when multiple services interact under realistic traffic patterns.

---

### 3. GitOps Manifest Repositories (ArgoCD, Flux)

**Who uses it:** Kubernetes-native organizations, cloud-native teams using declarative infrastructure.

**Mechanism:** A Git repository of deployment manifests (Helm values, Kustomize overlays, ArgoCD Application CRDs) declares what container image versions should be deployed together. The Git repository is the source of truth for "desired state."

**How it addresses the three challenges:**
- **Integration verification:** Not directly addressed. The manifest declares what *should* be deployed, not what's *verified to work together*.
- **Composition tracking:** Partially addressed — the manifest repo serves as an infrastructure-level BOM. "What was deployed on Feb 1?" is answerable from Git history.
- **Cross-team vocabulary:** Not addressed. Manifests use container image names and tags — infrastructure-level, not capability-level.

**Pros:**
- Declarative and auditable — Git history provides full deployment history.
- Automated reconciliation — ArgoCD/Flux continuously sync desired state to actual state.
- Familiar to cloud-native teams.

**Cons:**
- **Infrastructure-level, not capability-level:** Manifests describe container images, not functional Modules or product capabilities. No Module boundary in the manifest.
- **Not verified:** The manifest says "deploy these versions together" but doesn't prove they work together. Integration testing is a separate concern.
- **No cross-team vocabulary:** PMs and Win teams don't read Helm charts. No shared vocabulary for capability-level composition.

**Deploy-time composition gap:** GitOps tracks desired state, not verified composition. A manifest can declare a combination of image versions that has never been integration-tested.

---

### 4. Release Trains / Release Bundles (SAFe, enterprise vendors)

**Who uses it:** SAFe organizations, large enterprise software vendors with coordinated release cycles.

**Mechanism:** Multiple teams plan and deliver work on a shared cadence (Program Increment in SAFe). At the end of each cadence, all services/components are bundled into a coordinated release. System/integration demos verify the composition.

**How it addresses the three challenges:**
- **Integration verification:** Partially — System Demos and Integration Demos verify the composition at cadence boundaries. Not continuous.
- **Composition tracking:** Informal — "what's in PI 12?" requires archaeology. No formal versioned BOM artifact.
- **Cross-team vocabulary:** Partially — the PI or release train name provides a shared reference, but it's a time boundary, not a versioned composition.

**Pros:**
- Coordination across teams — everyone plans and delivers on the same cadence.
- Provides natural integration verification points (System Demos).
- Familiar organizational structure in enterprise contexts.

**Cons:**
- **Time-boxed, not versioned:** A PI is a time boundary, not a versioned artifact. "What was in PI 12?" requires reconstructing from multiple sources.
- **No formal BOM:** The composition is implicit in the cadence, not declared as a versioned artifact.
- **Cadence coupling:** All teams must align to the same cadence, which constrains fast-moving teams and creates artificial urgency for slow-moving ones.
- **Ceremony overhead:** SAFe's PI Planning events require significant organizational investment.

**Deploy-time composition gap:** Release trains coordinate planning and delivery, but deployment may still happen incrementally across services. The train defines what *should* be released together, not what's actually running in each environment.

---

### 5. Canary + Production Verification (Netflix, large cloud-native)

**Who uses it:** Netflix (Spinnaker), Google (Borg), large-scale cloud-native organizations with sophisticated deployment infrastructure.

**Mechanism:** Deploy to production with traffic shaping — canary deployments route a small percentage of traffic to the new version. Automated analysis compares canary metrics against baseline. If metrics are healthy, roll forward; if not, roll back.

**How it addresses the three challenges:**
- **Integration verification:** In production — the canary IS the integration test. If the new version works with the current production versions of all other services, it passes.
- **Composition tracking:** Tracked by deployment tooling (Spinnaker, Borg), not by a formal composition artifact.
- **Cross-team vocabulary:** Not addressed. Service-level deployment vocabulary only.

**Pros:**
- Verifies integration under real production conditions — traffic patterns, data distribution, scale.
- Fast feedback — canary results are available in minutes/hours.
- No separate integration testing environment needed.
- Catches issues that pre-production testing misses (realistic traffic, real data).

**Cons:**
- **Accepts production risk:** Canary traffic is real customer traffic. If the canary is broken, some customers are affected (albeit a small percentage).
- **No pre-deployment verification:** You discover integration failures in production, not before. For fintech (payments, compliance, settlement), this risk profile may be unacceptable.
- **No capability-level vocabulary:** Canary metrics are per-service, not per-capability or per-product.
- **Rollback complexity:** Multi-service canaries (coordinated deployment of multiple services) are significantly more complex than single-service canaries.

**Deploy-time composition gap:** This approach deliberately *does not* close the deploy-time gap. It accepts the gap and mitigates it operationally. For organizations where the cost of a production-discovered integration failure is low (relative to the velocity benefit of CD), this is a rational trade-off. For enterprise fintech, the cost of "5% of payments went to the wrong bank during canary" may be prohibitive.

---

### 6. Formal Software Bill of Materials (AUTOSAR, DO-178C, aerospace/medical)

**Who uses it:** Aerospace (DO-178C, ARP4754A), automotive (AUTOSAR), medical devices (IEC 62304), regulated industries requiring formal certification.

**Mechanism:** Rigorous composition manifests with full traceability from requirements to verified components. Every component version is formally declared, tested, and certified. Composition integrity is verified through formal methods, and the resulting BOM is a compliance artifact.

**How it addresses the three challenges:**
- **Integration verification:** Formal — every combination is explicitly tested and certified. No implicit composition.
- **Composition tracking:** Complete — the BOM is a formal, auditable, legally binding artifact.
- **Cross-team vocabulary:** Complete — the BOM provides the definitive reference for all teams and regulatory bodies.

**Pros:**
- Maximum rigor — composition integrity is formally proven.
- Full traceability from requirements through components to verified composition.
- Regulatory compliance built in.

**Cons:**
- **Heavyweight process:** Formal verification, certification, and documentation overhead is enormous.
- **Slow deployment velocity:** Formal certification takes weeks or months, not hours.
- **Justified only for safety-critical systems:** The overhead is proportional to the cost of failure (lives, not revenue).
- **Not designed for continuous deployment:** The formal SBOM model assumes discrete release cycles, not CD.

---

### 7. Service Catalogs (Backstage, Port, Cortex)

**Who uses it:** Spotify (Backstage), many platform engineering organizations.

**Mechanism:** Centralized catalog of services with metadata: ownership, dependencies, documentation links, deployment status, health indicators.

**How it addresses the three challenges:**
- **Integration verification:** Not addressed. Service catalogs track metadata, not composition integrity.
- **Composition tracking:** Partially — catalogs know what services exist and who owns them, but don't track version compositions or compatibility.
- **Cross-team vocabulary:** Partially — provides a service-level reference, but not capability-level or product-level.

**Pros:**
- Centralized visibility into service ownership and metadata.
- Good developer experience — engineers can discover services and their documentation.
- Extensible plugin ecosystem.

**Cons:**
- **No composition management:** "Which versions work together?" is not answerable from a service catalog.
- **Service-level only:** PMs and Win teams don't use service catalogs. No capability-level or product-level vocabulary.
- **Metadata, not verification:** Catalogs describe services; they don't verify compositions.

---

### 8. No Formal Composition Management

**Who uses it:** Most startups, early-stage products, small engineering teams.

**Mechanism:** Each service has its own CI/CD pipeline. Services deploy independently. "What's running in production" is reconstructed from deployment logs, container registries, and tribal knowledge.

**How it addresses the three challenges:**
- **Integration verification:** Ad-hoc — integration bugs are discovered in staging or production.
- **Composition tracking:** Not addressed — "what exactly was running on Feb 1?" requires forensic investigation across deployment logs.
- **Cross-team vocabulary:** Not addressed — each team uses its own language.

**Pros:**
- Zero overhead — no composition artifacts, no BOMs, no integration verification process.
- Maximum deployment velocity — each service deploys whenever ready.
- Appropriate for small teams where everyone knows what's deployed.

**Cons:**
- **Breaks at scale:** When the product grows beyond a handful of services, composition tracking becomes a significant pain point. Incident investigation ("what was deployed when this broke?") becomes forensic work.
- **No reproducibility:** "Deploy the exact same thing to DR" requires manual reconstruction.
- **No cross-team communication:** As teams grow, vocabulary fragmentation becomes a real coordination problem.

---

## Where Our Model Sits

```
Lightweight / CD-native                                           Heavyweight / Regulated
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  No formal       Contract    GitOps/     Canary +       Our model       Formal SBOM
│  composition     testing     Manifests   production     (Module +       (AUTOSAR,
│  (startups)      (Pact)      (ArgoCD)    verification   Product         DO-178C)
│                                          (Netflix)      Version)
│                                                                               │
│  ← Deploy fast, verify in prod            Verify before prod, deploy with confidence →
│  ← Service-level vocabulary               Capability + product-level vocabulary →
```

---

## Our Approach: Three-Tier Versioning with Composite Systems

UPIM's model introduces three artifact tiers, each of which is a **composite system** and a **communication bridge**:

| Tier | Nature | Verification Scope | Communication Bridge |
|---|---|---|---|
| **System Version** | Atomic system (single deployable) | Quality gates: tests, security, performance | Build + Run vocabulary |
| **Module Version** | Composite system (of Systems) | Integration verification: APIs, events, data consistency | Build + Run + Product vocabulary |
| **Product Version** | Higher-order composite system (of Modules) | Certification: end-to-end tests, compliance, compatibility | Ubiquitous language across all teams + customers |

**Why composite systems, not just verification checkpoints:** Module Version and Product Version are not paperwork. They are systems in the systems-thinking sense, with emergent operational properties at each composition level — end-to-end latency, integrated failure modes, cross-module workflows — that do not exist at the constituent level. SREs operate them, PMs reason about them, Win teams reference them.

**Why communication bridges:** System Version is the shared vocabulary between engineers and SREs ("deploy payments-service v2.3.3 to LATAM staging"). Module Version bridges Build, Run, and Product teams ("Payments Module v4.1 includes the new compliance flow"). Product Version is the lingua franca across all teams and customers ("customer X is running Product v3.2"). Without these tiers, cross-functional teams resort to ad-hoc translation between service names, feature names, and marketing labels.

### Three Deployment Levels

All three tiers are deployable — not just verifiable:

| Deployment Level | Build Track Artifact | Run Track Artifact | Deployment Descriptor | What Gets Applied |
|---|---|---|---|---|
| **Atomic** | System Version | (deployed directly) | **SDD** | Environment-specific System Version deployment specification |
| **Integrated** | Module Version | **Module Package Version** | **MDD** | Environment-specific Module Package Version deployment specification (composes SDDs) |
| **Complete** | Product Version | **Product Package Version** | **PDD** | Environment-specific Product Package Version deployment specification (composes MDDs) |

System Version is the **atomic deployment unit** — deployed via SDD (System Deployment Descriptor). Module Package Version is the **integrated deployment unit** — the Run Track adds operator-facing systems (probes, automation, reconcilers, dashboards, log shippers) and operational wiring to Module Version; deployed via MDD (Module Deployment Descriptor). Product Package Version is the **complete deployment unit** — the Run Track assembles Module Package Versions with cross-module operational wiring; deployed via PDD (Product Deployment Descriptor).

Module Package Version and Product Package Version are **environment-independent** — they define *what* is deployed. Deployment descriptors (SDD, MDD, PDD) define *how* and *where* — environment-specific configuration, deployment scripts, and runtime artifact references. This separation enables a single Module Package Version to be deployed to multiple environments via different MDDs, and supports three independent version streams at the integrated level: Module Version (functional), Module Package Version (operator-facing systems), MDD (deployment progression). See `deployment-artifacts-analysis.md` (same folder) for the full four-layer model and rationale. **DR-029** introduces Deployment Train and Station as structured promotion path entities for deployment workflows.

### Binding Configuration: Legal Composition

Module Version includes a **binding configuration** that constrains the composition to its legal form. This is not mere wiring — it represents scoped, deliberate build-time choices: which adapter variant to include, which protocol version to bind, which capability set to activate. Not all possible combinations of System Versions are valid. The binding configuration determines what this composition is intended to deliver and what it is not. Environment-independent (environment-specific configuration is applied at the deployment descriptor level — MDD — by the Run Track).

### The Run Track as Engineering Track

The deployed composition is richer than the built composition. The Run Track is not just an operational track — it is also an engineering track that builds its own operational Systems:

- **Custom probes** — synthetic transaction probes for end-to-end path verification
- **Reconciliation jobs** — daily settlement reconciliation against bank files
- **Cert rotation automation** — automated certificate lifecycle management
- **Environment-specific adapters** — adapters for region-specific infrastructure

These operational Systems are legitimate Dim 5 Systems with code, repos, CI/CD pipelines, tests, and System Versions. They serve Operational Personas (Dim 7) and are built through the Run Track's own Epic/Story/Task hierarchy (Run Epics and Run Stories). The Run Track's operational System Versions enrich Module Versions into Module Package Versions — the deployable composition is a collaboration between Build Track (product systems) and Run Track (operational systems).

**Environment-specific work is not just configuration.** A common misconception is that the difference between a Module Version and what's deployed is "just config." In practice, the Run Track may introduce code — operational subsystems — per environment. LATAM production may need a custom payment probe that exercises BRL corridors. US production may need a different reconciliation schedule against different bank file formats. These are code artifacts, not configuration values.

---

## Suitability for Enterprise Software

Our model is designed for enterprise software contexts where:

1. **Correctness outweighs velocity in high-stakes domains.** For fintech (payments, FX, compliance, settlement), "5% of payments went to the wrong bank during canary" is not an acceptable integration verification strategy. Pre-deployment composition verification is a business requirement.

2. **Multiple teams must coordinate.** Enterprise products involve Build, Run, Product, Win, and customer-facing teams — each with different vocabularies. Module Version and Product Version provide the shared reference points that enable cross-functional coordination without ad-hoc translation.

3. **Regulatory and compliance traceability.** Auditors ask "what was deployed, and was it tested?" A formal Product Version with BOM provides a defensible answer. Most alternative approaches cannot answer this question without forensic reconstruction.

4. **Customers need stable version references.** Enterprise customers reference "Product v3.2" in support cases, contracts, and compliance documentation. Win teams need a version to reference. Without Product Version, "which version is customer X running?" requires reconstructing from deployment logs across dozens of systems.

5. **Multi-module, multi-system products.** The value of Module Version and Product Version scales with product complexity. Single-module products may not need them; products with 5+ Modules and 20+ Systems benefit significantly.

6. **Independent deployment cadences.** Teams move at different speeds. Module A ships weekly; Module B ships monthly. The versioned-artifact model gives each team deployment independence while providing composition infrastructure to verify compatibility when they do integrate.

---

## Acknowledged Cons

1. **Tooling investment.** Module Version and Product Version require tooling to assemble, verify, and track compositions. BOM assembly, integration verification automation, and composition tracking do not materialize for free. Without tooling, the model becomes manual ceremony.

2. **Process overhead.** Maintaining Module Version as a formal artifact adds process steps to the delivery pipeline. If integration verification is slow (weeks, not minutes), Module Version verification becomes a bottleneck.

3. **Cultural adoption.** Teams must actually use Module Version and Product Version as their shared vocabulary, not just produce them as artifacts nobody reads. The communication-bridge value depends on organizational buy-in.

4. **Module boundary stability.** Module Versions are meaningful only if Module boundaries (Dim 8) are stable. Frequent Module restructuring (Systems reassigned between Modules) destabilizes composition history and undermines the traceability story.

5. **Combinatorial verification cost.** With many-to-many System-to-Module mappings, a System Version change that participates in 3 Modules requires 3 Module Version re-verifications. This scales with the breadth of reuse.

6. **Not necessary for all products.** Small products, single-Module products, and internal tools may not need the overhead. The model adds value primarily for multi-module, multi-system enterprise products.

---

## Key Insight: The Deploy-Time Composition Gap Is Universal

Even organizations with the strongest build-time integration (monorepo + Bazel) face the composition problem at deployment time. Independent rollout phases produce their own dependency graphs — each service canaries at different times, and the cross-product of all rollout states is a combination that was never explicitly tested.

The monorepo eliminates version negotiation but replaces it with build-time coupling (unrelated failures block shared-library changes). It also does not close the deploy-time gap — that gap is mitigated operationally (canary analysis, rollback), not through formal composition verification.

Our model accepts version negotiation as a cost (teams upgrade when ready, not atomically at HEAD) but provides the composition infrastructure — Module Version and Product Version as composite systems and communication bridges — to manage the resulting version diversity safely. For enterprise software where correctness, traceability, and cross-team communication matter, this trade-off is well-suited.

---
