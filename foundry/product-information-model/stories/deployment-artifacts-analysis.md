# Deployment Artifacts: From Build to Production

This document explains how UPIM separates **what is built and verified**, **how it is deployed to a specific environment**, and **the governed act of applying that specification** — using a **three-layer deployment model** aligned to DR-036.

---

## The Problem Being Solved

Moving a multi-System product from build to production involves distinct concerns that organizations often conflate:

1. **Build artifacts:** Which Component, System, and Product Versions are verified to work together?
2. **Deployment specifications:** How does a given version apply to *this* environment — sizing, scripts, policies, coordination?
3. **Deployment execution:** Who applies the specification, under what governance, and what is the durable record?

When these concerns merge into a single blob (image tag + Helm values + one-off scripts + tribal rollout knowledge), teams lose independent lifecycles, multi-environment reuse, and auditability.

---

## The Three-Layer Model

```
Layer 1: Build Artifacts          → What is built and verified (environment-independent)
Layer 2: Deployment Specifications → How a version deploys to a specific environment
Layer 3: Deployment Execution     → The governed act of applying a specification
```

| Layer | Scope | Primary Artifacts | Owner (typical) |
|---|---|---|---|
| **1 — Build** | Component → System → Product | Component Version, System Version, Product Version | Build Track |
| **2 — Specification** | Per environment | System Deployment Specification, Product Deployment Specification | Run Track (Deployment Planning) |
| **3 — Execution** | Per change / station | Change Request → Deployment Task → **Deployment** (record) | Run Track |

Each layer has its own lifecycle and versioning logic:

- **Build artifacts** version by **functional change** — what changed in code and composition.
- **Deployment specifications** version by **deployment progression** — resource tuning, script updates, rollout strategy changes — even when build artifacts are unchanged.
- **Deployments** are **events** — durable records that a specification version was applied at a point in time.

### What Was Removed (DR-036)

Earlier modeling used **four layers**, including a separate **Run Artifact** tier (Module Package, Product Package) and three descriptor acronyms (SDD, MDD, PDD). DR-036 collapses this:

| Retired construct | Replacement |
|---|---|
| Run Artifact layer (Module Package, Product Package) | Operator-facing Systems are ordinary Dim 5 Systems; their Component/System Versions appear in System Version and Product Version BOMs |
| SDD / MDD / PDD | **System Deployment Specification**, **Product Deployment Specification** |
| Module-level deployment descriptor | None — Module is not a deployment boundary |
| Separate "enrichment" version stream for ops Systems | Same Component → System → Product versioning; Purpose / Serving Persona distinguishes operator-facing Systems |

The **separation of build from environment-specific deployment** is preserved. What changed is *where operator-facing systems live* (in the build composition, not a parallel package) and *how many deployment-spec tiers exist* (System and Product only).

---

## Layer 1: Build Artifacts

Build artifacts are **environment-independent**. They answer: "What composition was verified?"

### Component Version (atomic)

A **Component Version** is the quality-gated output for one deployable artifact — container image, Lambda package, frontend bundle, etc. It is what CI/CD produces and tags.

- Scoped to one **Component** (Dim 5) within a parent **System**.
- Verified by atomic quality gates (tests, security scans, performance baselines).
- Listed in the parent **System Version** BOM.

### System Version (integrated)

A **System Version** is the verified composition of all **Component Versions** that deploy together as one operational unit — the release SRE applies when deploying "Payments System v3.1."

- Scoped to one **System** (Dim 5).
- Includes **binding configuration** — legal composition constraints (adapter variants, protocol bindings, capability activation).
- Integration-verified across Components within the System boundary.
- May include Components from **operator-facing Systems** (reconcilers, probes) when those Components belong to this System.

### Product Version (complete)

A **Product Version** is the certified composition of **System Versions** across the product — the reference Win teams, customers, and auditors use.

- Scoped to the **Product** (Dim 8).
- End-to-end and compliance verification across Systems.
- Commercially meaningful unit ("Product v3.2").

### Version Stream Independence (build tier)

| Artifact | Versions when… | Example |
|---|---|---|
| Component Version | One Component's code or artifact changes | `payments-service` 2.3.1 → 2.3.2 |
| System Version | Any constituent Component Version changes, or binding configuration changes | Payments System 3.1 → 3.2 |
| Product Version | Any constituent System Version changes, or product-level certification scope changes | Product 3.2 → 3.3 |

There is **no Module Version** in the build layer. Module (Dim 8) does not produce a deployable BOM; Systems do.

---

## Layer 2: Deployment Specifications

Deployment specifications are **environment-specific**. They answer: "How does this System Version or Product Version run *here*?"

### System Deployment Specification

A **System Deployment Specification** defines how one **System Version** is applied to one **Deployment Environment**:

- Maps the System Version to runtime primitives (Kubernetes workloads, ECS tasks, Lambda configs, etc.) — using platform vocabulary, not prescribing a platform.
- Per-Component deployment detail: resources, replicas, autoscaling, secrets references, network policy.
- System-level coordination: rollout strategy hooks, health checks spanning Components, System-scoped pre/post scripts.
- **Versioned independently** from System Version — a threshold or script change bumps the specification version, not the System Version.

Multiple specifications per System per environment are valid (canary vs. full, fault-domain splits, segment-specific sizing).

### Product Deployment Specification

A **Product Deployment Specification** defines how a **Product Version** is applied across the product in one environment:

- References **System Deployment Specifications** (by version) for each System in the Product Version.
- Adds cross-System coordination: deployment ordering, product-wide smoke tests, coordinated rollback, shared dashboards and alerting where product-scoped.
- Includes product-level scripts (cross-System health verification, orchestrated migrations).

Product-level deployment is used for coordinated product releases. Individual Systems may still deploy under **System**-scoped Change Requests when operating model allows — but full-product rollout uses the Product specification.

### Specifications vs. Tenant Configuration

| Concern | Where it lives | When applied |
|---|---|---|
| CPU, memory, replicas | Deployment Specification | Deployment time |
| Monitoring thresholds, alerting | Deployment Specification | Deployment time |
| Migrations, smoke tests, rollback scripts | Deployment Specification | Deployment time |
| Network policies, mesh config | Deployment Specification | Deployment time |
| Tenant feature flags, rate limits, branding | Tenant Subscription / runtime config | Runtime |

**Tenant configuration is runtime-discovered, not deployment-time.** Specifications configure the *platform in an environment*; tenant config configures *behavior per tenant*. A specification must not embed tenant-specific values.

### Two Independent Version Streams (operational tier)

At System scope, two streams evolve independently:

| Stream | What it versions | Example change |
|---|---|---|
| **System Version** (Build Track) | Functional composition — Component Versions + binding | New `payments-service` with rate-lock |
| **System Deployment Specification** (Run Track) | How that System Version deploys to `production-latam` | New rollback script; replica limit change |

The same **System Version** deploys to staging and production via **different specification versions** — appropriate sizing, policies, and scripts per environment.

---

## Layer 3: Deployment Execution

Execution is the **governed workflow** that applies a specification and records the outcome. It does not introduce a fourth artifact tier.

Typical chain (see `change-to-deployment-analysis.md`):

```
System Version or Product Version released (Build Track)
  → Change Request (System or Product deployment scope)
  → Deployment Planning → produces / updates Deployment Specifications
  → Deployment Task (per Train Station)
  → Verification Task
  → Deployment record (artifact)
```

**Deployment** (artifact) is the durable audit record: which specification version was applied, when, under which Change Request, with what outcome. **Deployment Task** is transient work.

Rollback is a new Deployment Task applying a prior specification version; the superseded Deployment moves to `Rolled Back` or `Superseded`.

---

## Change Management Unit

The Operating Model chooses the default approval grain:

| Grain | Unit of review | When appropriate |
|---|---|---|
| **System-centric** | System Deployment Specification + System Version | Independent System cadences; hotfixes to one System |
| **Product-centric** | Product Deployment Specification + Product Version | Coordinated product releases; regulatory full-stack proof |

Most regulated enterprises use **Product-centric** approval for production and **System-centric** approval for lower environments or isolated Systems — both are valid within the same model.

---

## Operator-Facing Systems in the Build Layer

Operator-facing systems (probes, reconcilers, log shippers, cert automation) are **Systems in the PSD** with **Purpose / Serving Persona** pointing at Operational Personas. They are not a separate "package" layer.

Implications:

- Run Track engineering produces **Component Versions** and contributes to **System Versions** like product engineering.
- A System Version BOM may mix tenant-serving and operator-serving Components when they deploy as one System.
- Environment-specific *code* for operations (e.g., a LATAM-only probe variant) is still a Component with its own version — not "configuration" smuggled outside the model.

This removes the false split between "what Build built" and "what Run added" at the artifact level. The split that remains is **Build artifacts vs. deployment specifications vs. execution** — not Build vs. Run duplicate version streams.

---

## Pros and Cons

### Pros

1. **Fewer parallel version streams.** No Module Package vs. Module Version vs. MDD confusion — build composition and deployment progression are clearly separated.

2. **Alignment with operations.** System Deployment Specification matches what SRE deploys; Product Deployment Specification matches coordinated releases.

3. **Independent deployment progression.** Tune production without rebuilding artifacts.

4. **Multi-environment reuse.** One System Version, many specification versions.

5. **Script formalization.** Migrations and rollback live in specifications — versioned and reviewed.

6. **Audit trail.** Deployment record → specification version → System/Product Version → Component Versions.

### Cons

1. **Learning curve.** Teams accustomed to SDD/MDD/PDD and Module Package must adopt new names and boundaries.

2. **Tooling investment.** Specification assembly and validation need automation.

3. **System boundary discipline.** Poor System boundaries make System Versions awkward — same as before, but more visible.

4. **Product specification weight.** Large products produce large Product Deployment Specifications; tooling or phased System deployment mitigates.

---

## Dos and Don'ts for Run Track Participants

### Do

- **Do** treat **System Deployment Specification** as the default unit of deployment conversation for a single System.
- **Do** version specifications independently from System Versions.
- **Do** include migration and validation scripts inside the specification.
- **Do** reference exact System Version and specification versions in Change Requests and Deployment records.
- **Do** model operator-facing capabilities as Systems with Operational Personas in the PSD.

### Don't

- **Don't** embed environment-specific values in System Version or Product Version.
- **Don't** embed tenant-specific values in Deployment Specifications.
- **Don't** invent a "Module deployment" tier — deploy Systems or Products.
- **Don't** maintain parallel informal scripts outside versioned specifications.
- **Don't** assume retired Module Package / MDD concepts still apply — see DR-036.

---

## Relationship to Model Entities

| Entity | Layer | Role |
|---|---|---|
| Component Version | 1 — Build | Atomic verified artifact |
| System Version | 1 — Build | Integrated verified composition |
| Product Version | 1 — Build | Complete certified composition |
| System Deployment Specification | 2 — Specification | Environment-specific System deployment |
| Product Deployment Specification | 2 — Specification | Environment-specific Product deployment |
| Deployment Planning Task | 2 — Work | Produces or updates specifications |
| Change Request | 3 — Execution | Governance envelope |
| Deployment Task | 3 — Work | Applies a specification |
| Deployment (artifact) | 3 — Execution | Durable apply record |
| Verification Task | 3 — Work | Post-deploy evidence |

For versioning rationale and why Module is excluded from the version stack, see `versioning-alternatives-analysis.md`. For end-to-end workflow, see `change-to-deployment-analysis.md`.

---
