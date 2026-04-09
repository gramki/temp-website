# Deployment Artifacts: From Build to Production

This document analyzes the deployment artifact model — how the information model separates "what is built," "what operator-facing systems are added for observability and maintainability," "what specifies deployment," and "what is deployed" — and explains the rationale behind SDD, MDD, and PDD as deployment descriptors distinct from Module Package and Product Package.

---

## The Problem Being Solved

When a multi-system product moves from build to production, four distinct concerns emerge:

1. **Functional composition (Build Track):** Which System Versions are verified to work together? This is the Module Version and Product Version problem — addressed by the Build Track's three-tier versioning model.

2. **Operator-facing systems (Run Track):** What operator-facing systems (probes, reconcilers, dashboards, log shippers, automation) and operational wiring are added to make the composition observable and maintainable? This is the Module Package and Product Package problem — the Run Track adds operator-facing systems to build artifacts for observability and maintainability.

3. **Environment-specific specification:** How is this deployable composition configured for a *specific* environment? Resource sizing, replica counts, monitoring thresholds, deployment scripts, compliance windows — all vary by environment. This is the **deployment descriptor** problem.

4. **Deployment execution:** The act of applying the specification to the environment — canary rollout, health verification, rollback on failure. This is the Deployment entity problem.

Without a clean separation of these four concerns, organizations conflate them — embedding environment-specific configuration in the deployable artifact, mixing deployment scripts with operational wiring, and losing the ability to independently version and manage each concern.

---

## The Four-Layer Model

At each composition level (Atomic, Integrated, Complete), four layers exist:

```
Layer 1: Build Artifact         → What is functionally verified
Layer 2: Run Artifact           → What operator-facing systems are added for observability and maintainability (environment-independent)
Layer 3: Deployment Descriptor  → How it is deployed to a specific environment
Layer 4: Deployment             → The act of applying the descriptor
```

| Layer | Atomic | Integrated | Complete |
|---|---|---|---|
| **Build Artifact** | System Version | Module Version | Product Version |
| **Run Artifact** | (System Version deployed directly) | Module Package | Product Package |
| **Deployment Descriptor** | SDD | MDD | PDD |
| **Deployment** | Apply SDD | Apply MDD | Apply PDD |

Each layer has its own lifecycle, its own version, and its own ownership:

- **Build artifacts** are produced by the Build Track and version functionally (what changed in the code).
- **Run artifacts** are produced by the Run Track and version by operator-facing additions (which operator-facing systems are included, what operational wiring is defined).
- **Deployment descriptors** are produced by Deployment Planning Tasks and version by **deployment progression** (how deployment configuration evolves for a specific environment).
- **Deployments** are operational acts that apply descriptor versions to environments.

---

## Three Independent Version Streams at the Integrated Level

At the integrated composition level, three independent version streams co-exist:

| Version Stream | What It Versions | Who Owns It | Example |
|---|---|---|---|
| **Module Version** | Functional composition — which product System Versions integrate together | Build Track (Tech Lead, QA) | Payments Module v2.3.0 |
| **Module Package** | Operator-facing systems — which operator-facing System Versions and wiring are included | Run Track (SRE, Platform Eng) | Payments Module Package v2.3.0 |
| **MDD** | Deployment specification — how this composition deploys to this environment | Run Track (DevOps, SRE) | Payments MDD v3.1 (production-latam) |

These streams are independent because they change at different rates and for different reasons:

- Module Version changes when **product code** changes (new feature, bug fix, API change).
- Module Package changes when **operational systems** change (new probe added, reconciler upgraded, operational wiring updated).
- MDD changes when **deployment configuration** changes (resource limits adjusted, new migration script added, monitoring threshold tuned, rollback procedure updated) — even when neither the Module Version nor the Module Package has changed.

A common scenario: the same Module Package is deployed to three environments (staging, production-us, production-latam) via three different MDDs, each with environment-specific resource sizing, monitoring thresholds, and deployment scripts. When production-latam's monitoring threshold needs adjustment, only the LATAM MDD version increments — the Module Package and Module Version remain unchanged.

---

## SDD: The Atomic Deployment Specification

The System Deployment Descriptor (SDD) specifies how a single System Version is deployed to a single environment. It maps the System Version to one or more **runtime-defined artifacts** — Kubernetes Services, Pod specs, Deployments, CRDs, Helm releases, or any other infrastructure primitives defined by the runtime platform.

**Key characteristics:**

- **Platform-specific naming:** SDD references runtime artifacts using the platform's vocabulary (K8s Deployment, ECS Task Definition, Lambda function configuration). The information model does not prescribe the platform; it describes what the platform must provide.
- **Environment-specific sizing:** Resource limits, replica counts, autoscaling policies, availability zone distribution — all specific to the target environment.
- **Composed by reference into MDD:** SDDs are not standalone deployment units in integrated deployments. They are composed by reference into an MDD, which adds Module-level coordination. For atomic-level deployments, an SDD can be applied directly.
- **Independent versioning:** SDD versions reflect deployment progression — resource tuning, network policy changes, secrets rotation — independent of the System Version's functional version.

**Every deployable has a corresponding deployment descriptor.** System Versions have SDDs. Module Packages have MDDs. Product Packages have PDDs. The descriptor is not optional — it is where all environment-specific deployment knowledge is captured.

---

## MDD: The Integrated Deployment Specification

The Module Deployment Descriptor (MDD) specifies how a Module Package is deployed to a specific environment. It is the most operationally significant deployment descriptor because it:

1. **Composes SDDs by reference** — one SDD per System (product + operational) in the Module Package, providing coordinated deployment of all systems within the Module.
2. **Adds Module-level environment configuration** — monitoring thresholds, alerting rules, scaling coordination, probe schedules, cross-system communication config specific to this environment.
3. **Includes deployment scripts** — pre-rollout scripts (database migrations, cache warming), validation scripts (health checks, smoke tests), and rollback scripts (migration reversals, state restoration).

**MDD is a "system" in its own right.** It contains executable logic (scripts, applications), not just configuration. Creating or modifying MDD scripts is engineering work — performed as sub-tasks of Deployment Planning Tasks. An MDD is authored, tested, reviewed, and versioned like code.

**Multiple MDDs per environment are valid.** This is not an error condition — it is an intentional design choice. Reasons include:

- **Fault isolation:** Separate deployment descriptors for different fault domains within the same environment (e.g., zone-a vs. zone-b).
- **Service quality differentiation:** Different resource allocations or configurations for different tenant segments within the same environment.
- **Deployment stages:** A canary MDD (limited traffic, enhanced monitoring) and a full-rollout MDD (production traffic, standard monitoring) for the same environment.
- **Product-level isolation:** Different products sharing a Module may need isolated deployments in the same environment, each with their own MDD.

**MDD version is independent of Module Version and Module Package version.** The MDD versions by deployment progression — a new migration script, a resource limit adjustment, a monitoring threshold change — even when the Module Package it references has not changed. This independence is critical for operational agility: the Run Track can iterate on deployment configuration without requiring new builds.

---

## PDD: The Complete Deployment Specification

The Product Deployment Descriptor (PDD) specifies how a Product Package is deployed to a specific environment. It is the highest-order deployment descriptor:

1. **Composes MDDs by reference** — one MDD per Module Package in the Product Package.
2. **Adds cross-module environment configuration** — product-wide monitoring dashboards, cross-module alerting, product-level scaling coordination.
3. **Defines deployment ordering** — which MDDs must be deployed before others (e.g., deploy Compliance before Payments).
4. **Includes product-level deployment scripts** — cross-module health verification, end-to-end smoke tests, coordinated rollback procedures.

PDD is the deployment descriptor for full product releases. It orchestrates the deployment of all Module Packages (via their MDDs) with product-wide coordination and verification.

---

## Deployment Descriptors vs. Tenant Configuration

A critical boundary exists between deployment-time configuration (in descriptors) and runtime-discovered configuration (in tenant systems):

| Concern | Where It Lives | When It Is Applied |
|---|---|---|
| Resource sizing (CPU, memory, replicas) | SDD / MDD | Deployment time |
| Monitoring thresholds | MDD / PDD | Deployment time |
| Deployment scripts (migrations, smoke tests) | MDD / PDD | Deployment time |
| Network policies, service mesh config | SDD | Deployment time |
| **Tenant-specific feature enablement** | **Tenant Subscription / Runtime config** | **Runtime** |
| **Tenant-specific rate limits** | **Tenant Subscription / Runtime config** | **Runtime** |
| **Tenant-specific branding/settings** | **Tenant Configuration / Runtime config** | **Runtime** |

**Tenant configuration is runtime-discovered, not deployment-time.** Deployment descriptors configure the *platform* (how the systems run in an environment). Tenant configuration configures the *behavior* for specific tenants within that platform (what features are enabled, what rate limits apply). These concerns have different lifecycles — a new tenant can be onboarded without redeploying, and a deployment can change resource limits without affecting tenant settings.

The MDD should never contain tenant-specific values. If it does, it is a sign that tenant configuration has been conflated with deployment configuration.

---

## Change Management Unit

The Operating Model determines which descriptor level serves as the atomic unit of change management:

- **SDD-centric change management:** Each System Version deployment is independently reviewed and approved. Appropriate for organizations with fine-grained change control or when individual systems have different risk profiles.
- **MDD-centric change management:** The MDD is the unit of change approval — deploying a Module Package's worth of changes as a coordinated unit. Appropriate for organizations that think in Module-level increments and want coordinated deployment with Module-level scripts and verification.

Most organizations will operate with MDD-centric change management (reviewing and approving integrated deployment as a unit) while allowing atomic SDD-level deployments for hotfixes and urgent patches that bypass the integrated deployment flow.

---

## Pros and Cons

### Pros

1. **Clean separation of concerns.** Build artifacts, run artifacts, deployment specifications, and deployment acts are distinct entities with distinct owners and lifecycles. No conflation of "what is deployed" with "how it is deployed."

2. **Independent versioning.** Deployment configuration can evolve without requiring new builds or new operator-facing system changes. Resource tuning, script updates, and monitoring changes are deployment progression, not functional changes.

3. **Multi-environment reuse.** A single Module Package (environment-independent) can be deployed to multiple environments via different MDDs — each with environment-appropriate configuration. No need to rebuild or re-enrich for each environment.

4. **Script formalization.** Pre-rollout, validation, and rollback scripts are first-class artifacts within the descriptor — versioned, reviewed, and traceable. No more ad-hoc migration scripts that live outside the model.

5. **Composability.** SDDs compose into MDDs; MDDs compose into PDDs. Each level adds coordination and environment-specific logic appropriate to its scope.

6. **Audit trail.** "What was deployed to production-latam on Feb 15?" is answerable by MDD/PDD version — which references the Module Package version, which references the Module Version, which references the System Versions. Full traceability from deployment specification to code.

### Cons

1. **More entities.** Three new entity types (SDD, MDD, PDD) increase the model's entity count. Teams must understand the four-layer model and know which entity to modify for which concern.

2. **Tooling investment.** MDD assembly (composing SDDs, managing scripts, validating configuration) requires tooling. Without automation, MDD maintenance becomes manual ceremony.

3. **Assembly complexity.** Keeping SDDs, MDDs, and PDDs in sync with their referenced artifacts (System Versions, Module Packages, Product Packages) requires discipline and ideally automated validation.

4. **Descriptor versioning overhead.** Three independent version streams at the integrated level (Module Version, Module Package, MDD) are powerful but require clear naming conventions and version governance to avoid confusion.

5. **Learning curve.** New team members must understand the distinction between Module Package (what) and MDD (how/where). The four-layer model is conceptually clean but requires onboarding.

---

## Dos and Don'ts for Run Track Participants

### Do

- **Do** use the MDD as the unit of deployment discussion. "We're deploying MDD v3.1 to production-latam" is precise and traceable.
- **Do** version MDD independently from Module Package. A monitoring threshold change is an MDD version bump, not a Module Package change.
- **Do** include migration scripts in the MDD, not alongside it. The MDD *is* the deployment specification — scripts are part of it.
- **Do** use separate MDDs for different fault domains or tenant segments within the same environment when isolation is needed.
- **Do** treat MDD scripts as code — review them, test them, version them.
- **Do** reference SDDs by version in the MDD. If a System's resource configuration changes, the SDD version changes, and the MDD references the new SDD version.

### Don't

- **Don't** put environment-specific values in Module Package. If you're adding a monitoring threshold or replica count to Module Package, it belongs in the MDD.
- **Don't** put tenant-specific configuration in the MDD. Tenant config is runtime-discovered, not deployment-time. The MDD configures the platform, not tenant behavior.
- **Don't** deploy Module Packages directly without an MDD. The Module Package is environment-independent — deploying it directly means environment-specific configuration is being applied ad-hoc, outside the model.
- **Don't** conflate MDD versioning with Module Version. A new MDD version does not imply new code — it may be a resource adjustment, a script update, or a threshold change.
- **Don't** create one giant MDD for all modules. MDDs are per-Module Package, per-environment. Cross-module concerns belong in the PDD.

---

## Relationship to Existing Model

| Entity | Role | Layer |
|---|---|---|
| System Version | Atomic build artifact — verified, quality-gated | Build (Layer 1) |
| Module Version | Integrated build artifact — integration-verified composition | Build (Layer 1) |
| Product Version | Complete build artifact — certified composition | Build (Layer 1) |
| Module Package | Integrated run artifact — adds operator-facing systems for observability and maintainability (environment-independent) | Run (Layer 2) |
| Product Package | Complete run artifact — adds operator-facing systems for observability and maintainability (environment-independent) | Run (Layer 2) |
| **SDD** | **Atomic deployment specification — environment-specific System Version deployment** | **Descriptor (Layer 3)** |
| **MDD** | **Integrated deployment specification — environment-specific Module Package deployment** | **Descriptor (Layer 3)** |
| **PDD** | **Complete deployment specification — environment-specific Product Package deployment** | **Descriptor (Layer 3)** |
| Deployment | Operational act — applies a descriptor to an environment | Deployment (Layer 4) |
| Deployment Planning Task | Work entity — produces deployment descriptors | Work (produces Layer 3) |

---
