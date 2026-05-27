---
name: Versioning tiers as systems
overview: "Enrich the three-tier versioning model to capture two missing insights: (1) Module Versions and Product Versions are composite systems in their own right with emergent properties, not just verification checkpoints; (2) each tier serves as a communication bridge at progressively broader organizational scope — System Version (Build+Run), Module Version (Build+Run+Product), Product Version (all teams+customers)."
todos:
  - id: seed-rewrite
    content: Rewrite narrative seed 'Three-tier versioning' to add composite-system nature and communication-bridge role
    status: completed
  - id: module-version
    content: Enhance track2-module-version.md definition and purpose with composite-system and communication-bridge framing
    status: completed
  - id: product-version
    content: Enhance track2-product-version.md definition and purpose with composite-system and ubiquitous-language framing
    status: completed
  - id: dr004
    content: Update DR-004 consequences with communication-bridge and composite-system insights
    status: completed
  - id: faq-q13
    content: Enhance FAQ Q13 with communication-bridge framing
    status: completed
  - id: op-readiness
    content: Update Operational Readiness note to reference composite-system framing
    status: completed
  - id: draft-work-model
    content: Enrich Build Track artifact descriptions in draft-work-model.md with composite-system and communication-bridge framing
    status: completed
  - id: work-exec-framework
    content: Update Delivery Artifacts table in draft-work-execution-framework.md to note composite-system nature
    status: completed
  - id: faq-q86
    content: Enhance FAQ Q86 (three-tier versioning rationale) with composite-system and communication-bridge reasoning
    status: completed
  - id: dr026
    content: Update DR-026 decisions S4/S5 with composite-system and communication-bridge insights
    status: completed
  - id: versioning-alternatives
    content: Write a detailed document explaining alternative approaches to Module/Product versioning (monorepo, contract testing, GitOps, release trains, formal SBOM), with pros/cons, deploy-time composition gaps, and suitability of our approach for enterprise software
    status: completed
isProject: false
---

# Versioning Tiers as Composite Systems and Communication Bridges

Two insights are currently missing from the versioning model:

1. **Composite system nature** -- Module Version and Product Version are not just verification checkpoints. They are composite systems (in the systems-thinking sense) with emergent operational properties (end-to-end latency, integrated failure modes, cross-system data consistency) that don't exist at the constituent level. All three tiers are operable and observable.
2. **Communication bridge role** -- Each tier provides a shared vocabulary at a different organizational scope: System Version is Build+Run language, Module Version bridges Build+Run+Product, Product Version is the ubiquitous language across all teams and customers. This is why Modules and Products must be real operational entities, not abstract groupings.

## Files to Update

### 1. Narrative seed: Three-tier versioning (lines 821-823)

**File:** [narrative-seeds.md](org-8.0/product-information-model/narrative-seeds.md)

Rewrite the seed to cover three aspects:

- **Verification scope** (current content, kept but not as the sole framing): System-level quality gates, Module-level integration verification, Product-level certification
- **Composite system nature** (new): each tier is a system -- System Version is an atomic system, Module Version is a composite system of Systems with emergent properties, Product Version is a higher-order composite system of Modules
- **Communication bridge** (new): System Version = Build+Run vocabulary, Module Version = Build+Run+Product vocabulary, Product Version = ubiquitous vocabulary across all teams and customers. Module Version and Product Version enable cross-functional teams to use one language about the product.

### 2. Module Version entity definition

**File:** [track2-module-version.md](org-8.0/product-information-model/entities/work-model/track2-module-version.md)

- Add to the Definition section: Module Version represents a **composite system** -- not just a verification record, but an operable entity with emergent properties (end-to-end latency, integrated failure modes, cross-system data consistency) that don't exist at the individual System level.
- Add to Purpose: Module Version serves as the **shared vocabulary between Build, Run, and Product teams**. Product managers reason in Modules ("Payments capability v4.1"); SREs monitor integrated capability health; Build teams know which Systems compose it. Without Module Version, these teams have no common reference point.

### 3. Product Version entity definition

**File:** [track2-product-version.md](org-8.0/product-information-model/entities/work-model/track2-product-version.md)

- Add to the Definition section: Product Version represents the **highest-order composite system** -- the full product with its own emergent properties (end-to-end user journeys, cross-module workflows, product-wide availability and compliance posture).
- Add to Purpose: Product Version is the **ubiquitous language** across Build, Run, Win, and customer-facing teams. Win teams reference it in support cases ("customer X is on v3.2"), Release Notes are written against it, compliance certifies it, customers identify what they're running. It is the lingua franca that enables cross-team and external communication.

### 4. DR-004 (Three-Layer Versioning)

**File:** [DR-004-three-layer-versioning.md](org-8.0/product-information-model/decisions/DR-004-three-layer-versioning.md)

- Update Consequence 2 (line 53) which already mentions "Each layer serves a distinct audience" -- expand to explicitly frame this as a communication bridge with progressively broader scope.
- Add a new positive consequence: each tier is a composite system with emergent operational properties, not just a verification artifact.

### 5. FAQ Q13 (Why four separate concepts?)

**File:** [draft-modeling-faqs.md](org-8.0/product-information-model/draft-modeling-faqs.md)

- Enhance the existing answer (lines 160-177) to note that the tiers are also communication bridges: System Version (Build+Run), Module Version (Build+Run+Product), Product Version (all teams+customers). Each tier provides a shared vocabulary at a progressively broader organizational scope.

### 6. Operational Readiness note

**File:** [dim7-operational-readiness.md](org-8.0/product-information-model/entities/definition-model/dim7-operational-readiness.md)

- Enhance the existing "Module-level operational concern remains legitimate" note (lines 14-15) to reference the composite-system framing: Module-level readiness is legitimate precisely because a Module Version is a composite system with emergent operational properties, not merely an aggregation of System readiness scores.

### 7. Build Track summary in draft-work-model.md

**File:** [draft-work-model.md](org-8.0/product-information-model/draft-work-model.md)

- Enrich the artifact descriptions (lines 79-87) for System Version, Module Version, and Product Version. Currently they use only "unit of deployment/integration/certification" language. Add brief notes that Module Version and Product Version are composite systems and serve as communication bridges at progressively broader organizational scope.

### 8. Delivery Artifacts table in draft-work-execution-framework.md

**File:** [draft-work-execution-framework.md](org-8.0/product-information-model/draft-work-execution-framework.md)

- Update the descriptions in the Delivery Artifacts table (lines 115-117) to note that Module Version and Product Version are operable composite systems, not just verification records. Keep changes concise since this is a table.

### 9. FAQ Q86 (Why three-tier versioning?)

**File:** [draft-modeling-faqs.md](org-8.0/product-information-model/draft-modeling-faqs.md)

- Enhance the answer (lines 931-933) beyond the current verification-risk framing. Add: each tier is a composite system with emergent properties, and each serves as a communication bridge at progressively broader organizational scope (Build+Run, Build+Run+Product, all teams+customers).

### 10. DR-026 decisions S4 and S5

**File:** [DR-026-build-track-detailing.md](org-8.0/product-information-model/decisions/DR-026-build-track-detailing.md)

- Update decisions S4 (System Version rename) and S5 (three-tier versioning) rationale to include the composite-system insight and communication-bridge role. These are the authoritative decision records for the three-tier model.

### 11. Versioning Alternatives Analysis (new document)

**File:** [versioning-alternatives-analysis.md](org-8.0/product-information-model/versioning-alternatives-analysis.md) (new)

A standalone document analyzing alternative approaches to composition management and versioning, explaining why our model exists and where it sits on the spectrum. Structure:

- **The problem being solved:** Independent systems version and deploy independently; how do you verify composition, track what's running, and give cross-functional teams a shared vocabulary?
- **Alternative approaches** (each with mechanism, who uses it, pros, cons, and the deploy-time composition gap it leaves):
  - Monorepo + continuous integration (Google, Meta) — build-time coupling, deploy-time composition untracked, shared-library blocking problem
  - Consumer-driven contract testing (Pact) — pairwise verification, no whole-composition artifact
  - GitOps manifest repos (ArgoCD, Flux) — infrastructure-level BOM, not capability-level, not verified
  - Release trains / release bundles (SAFe) — time-boxed, informal, no versioned artifact
  - Canary + production verification (Netflix) — accepts production risk, mitigates with blast-radius control
  - Formal SBOM (AUTOSAR, DO-178C, aerospace) — rigorous but heavyweight
  - Service catalogs (Backstage) — metadata only, no composition or versioning
  - No formal composition management (most startups) — works small, breaks at scale
- **Our approach:** Module Version (composite system + Build/Run/Product bridge) and Product Version (composite system + ubiquitous language across all teams + customers). Three-tier model with BOM.
- **Suitability for enterprise software:** Why this approach fits enterprise contexts (correctness matters, regulatory traceability, multiple coordinating teams, customers need stable version references) while acknowledging cons (tooling investment, process overhead, cultural adoption, velocity impact risk, Module boundary stability assumption).
- **Key insight from discussion:** Even monorepo organizations face the deploy-time composition problem — independent rollout phases produce their own dependency graphs. Module Version and Product Version address a gap that exists regardless of repo strategy.

