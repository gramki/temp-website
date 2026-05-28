# Change-to-Deployment Workflow: Analysis and Guide (Story)

This document provides a comprehensive analysis of the change-to-deployment workflow — from the moment a deployable artifact is ready through governed change management, promotion across environments, post-deployment verification, and release activation. It covers the entity architecture, the end-to-end process, the design rationale, and the trade-offs of the approach.

**Model authority:** DR-036 (Versioning and Deployment Model Simplification). Supersedes the four-layer model with Module Package, MDD, SDD, and PDD.

---

## 1. Why a Structured Deployment Workflow Matters

Enterprise SaaS products — particularly in regulated domains like fintech — face a fundamental tension: the need for deployment velocity (ship fast, iterate, respond to market) versus the need for deployment governance (audit trails, compliance, tenant assurance, rollback safety). Ad-hoc deployment practices resolve this tension poorly: either velocity wins and governance is bypassed, or governance wins and deployments become a bottleneck.

A structured deployment workflow resolves this tension by making governance a first-class concern in the information model, not an afterthought bolted onto CI/CD pipelines. The workflow must answer six questions:

1. **What is being deployed?** — the sealed build composition (System Version or Product Version)
2. **How is it deployed to each environment?** — System Deployment Specification or Product Deployment Specification
3. **Who approves the change?** — change management governance
4. **Through which environments does it progress?** — the Deployment Train promotion path
5. **How do we know the deployment succeeded?** — structured post-deployment verification
6. **What is the durable record?** — audit trail for compliance

---

## 2. The Three-Layer Deployment Model

The deployment workflow separates concerns into three layers (DR-036):

```
Layer 1: Build Artifacts (Track 2)
  Component Version → System Version → Product Version
  "What is built, composed, and verified — environment-independent"

Layer 2: Deployment Specifications (Track 3)
  System Deployment Specification, Product Deployment Specification
  "How a sealed version deploys to a specific environment"

Layer 3: Deployment Execution (Track 3)
  Change Request → Deployment Plan → Deployment Task → Deployment (record)
  "The governed, auditable act of applying a specification"
```

### Layer Independence

Each layer has a distinct responsibility. Changes at one layer do not necessarily require changes at others:

- A new Component Version (Layer 1) may require a new System Version, then updated System Deployment Specifications (Layer 2), then a Change Request and Deployment Tasks (Layer 3).
- Changing deployment strategy from canary to blue-green (Layer 2) requires a new System Deployment Specification version but no build artifact change.
- Introducing a new Deployment Train (Layer 3 governance) requires no changes to Layers 1–2.

### What Was Removed (DR-036)

| Retired construct | Replacement |
|---|---|
| Module Version | Product Version composes System Versions directly |
| Module Package / Product Package | Operational Systems are ordinary Dim 5 Systems in Product Specification |
| SDD / MDD / PDD | System Deployment Specification, Product Deployment Specification |
| Run Artifact layer | Same Component → System → Product versioning for all Systems |

---

## 3. System Version vs. Deployment Specification: The Boundary

A common confusion is conflating **what was built** with **how it is deployed**. DR-036 draws a hard line:

| Aspect | System Version (Track 2) | System Deployment Specification (Track 3) |
|---|---|---|
| **Nature** | Sealed, immutable BOM of Component Versions | Environment-specific deployment configuration |
| **Changes when** | Code, composition, or integration contracts change | Resource sizing, env vars, scripts, rollout strategy change |
| **Environment-specific?** | No — same System Version in all environments | Yes — one spec per System Version × environment |
| **Example** | payments-system v3.1.0 = {payments-service v2.3.1, reconciler v1.4.0, worker v1.2.0} | payments-system v3.1.0 → production-latam: 4Gi memory, 3 replicas, LATAM env vars |

**Product-level boundary:** Product Version is the certified composition of all System Versions. Product Deployment Specification composes System Deployment Specifications and adds cross-System ordering, smoke tests, and coordinated rollback.

**Operational Systems:** payments-monitoring-system v1.2.0 is a System Version like any other — included in Product Version v4.0.0. It deploys via its own System Deployment Specification, composed into the Product Deployment Specification. No separate "operator package" layer.

---

## 4. Deployment Specifications

### System Deployment Specification

References a **sealed System Version** and provides environment-specific configuration:

- Resource limits, replicas, autoscaling
- Environment variables and secrets references
- Runtime artifact mappings (K8s Deployment, Helm release, etc.)
- Network configuration
- Pre-rollout, validation, and rollback scripts

The System Version never changes between environments — only the specification does.

### Product Deployment Specification

References a **certified Product Version** and composes System Deployment Specifications:

- One System Deployment Specification per System in the Product Version BOM
- Deployment ordering (e.g., compliance-system before payments-system)
- Cross-System environment configuration
- Product-level scripts (health check, end-to-end smoke test, coordinated rollback)

### Two Independent Version Streams (at deployment level)

| Stream | What It Versions | Example Change |
|---|---|---|
| **Build artifacts** (Track 2) | Functional composition — which Component/System Versions are verified together | New payments-service with rate-lock feature → new System Version → new Product Version |
| **Deployment specifications** (Track 3) | How a fixed version deploys to an environment | New rollback script, changed replica count for production-latam |

A monitoring threshold change is a **System Deployment Specification** version bump, not a System Version change. A new API endpoint is a **System Version** change (new Component Version in the BOM).

---

## 5. The Change Request → Deployment Flow

### Standard Flow

```
1. Trigger: System Version Released, Product Version Certified, or Release Plan requires deployment
   ↓
2. Change Request created
   - Scoped to: System Deployment OR Product Deployment
   - Scoped to: Deployment Train (and optionally a Station)
   - Type: Standard
   - CAB review and approval
   ↓
3. Deployment Plan (deliberation)
   - Run team scopes the rollout
   - Identifies verification needs, maintenance prerequisites
   - Determines promotion path through Train stations
   ↓
4. Deployment Planning Tasks produced
   - Create or update System Deployment Specification(s) and/or Product Deployment Specification
   - Author pre-rollout, validation, and rollback scripts
   - Create Verification Tasks for post-deployment validation
   - May create Maintenance Tasks (prerequisites)
   ↓
5. Deployment Drill Task (optional)
   - Rehearse full procedure in non-production environment
   - Must pass before actual deployment proceeds (Regulated/Critical Trains)
   ↓
6. Deployment Tasks execute (per station in the Train)
   - Apply specification to target environment
   - Produce Deployment record (artifact)
   ↓
7. Verification Tasks execute
   - Validate deployment meets acceptance criteria
   - Produce evidence (metrics, test results, audit logs)
   ↓
8. Change Request Complete
   - All Deployment Tasks succeeded
   - All Verification Tasks passed
   - Audit trail documented
```

### System-Scoped vs. Product-Scoped Changes

| Scope | When to Use | Specification Produced |
|---|---|---|
| **System Deployment** | Single System update (hotfix to payments-system, new monitoring probe) | System Deployment Specification for that System Version × environment |
| **Product Deployment** | Full product release, coordinated multi-System rollout | Product Deployment Specification composing all System Deployment Specifications |

Deployment Train governance applies at the **Product level** — even System-scoped changes traverse the Train when they affect production environments on a regulated path.

### Emergency-Technical Flow (from Incident)

**Build Track fast-path (DR-031):**
```
Incident (SEV-0/SEV-1) → Incident Response Task → Bug (P0)
  → Technical Task (sprint bypass)
    → Component Version (Emergency gate profile)
      → System Version (Emergency gate profile)
        → System Deployment Specification
```

**Run Track fast-path (DR-029):**
```
Change Request (Emergency-Technical, System Deployment scope)
  - Abbreviated soak times
  - Documented waiver for bypassed stations
  - Drill may be skipped with justification
  ↓
Deployment Task → Deployment → Verification Task
  ↓
Change Request Complete
```

**Deferred-gate obligation (DR-031):** The Bug stays at `Fixed` until a subsequent Standard Component/System Version passes all deferred quality gates.

### Emergency-Business Flow

```
Business exigency (campaign deadline, festival day)
  ↓
Change Request (Emergency-Business, Product Deployment scope)
  - Compressed Train (abbreviated soak, fast-track stations)
  - ODR documents the waiver and business justification
  ↓
Standard deployment flow with compressed timelines
```

---

## 6. Deployment Train and Station Design

### What Is a Deployment Train?

A Deployment Train is a reusable, ordered promotion path — the defined sequence of environments a deployment progresses through, with governance, approval, and soak requirements at each stop. Trains are Definition Model entities (Dim 7).

**Product-level governance (DR-036):** Deployment Trains operate at the Product level. System-scoped deployments still traverse the Train when targeting environments on a regulated promotion path.

### Contractual Significance

- **Tenant assurance.** Tenants rely on the Train's promotion path to plan dependent application changes.
- **Commercial contracts.** Contracts may reference Trains for safety guarantees (e.g., "all production changes traverse staging with minimum 72-hour soak").
- **Operating model enforcement.** A Regulated-governance Train may reject Emergency-Business changes that bypass required stations.

### Station Design

Each Station targets a Deployment Environment with entry criteria, exit/promotion criteria, approval requirements, soak time, and mandatory Verification Task types.

### Governance Levels

| Level | Characteristics |
|---|---|
| **Standard** | Automated approvals, minimal soak, self-service |
| **Regulated** | CAB approval, 72h soak, compliance officer sign-off, mandatory drill |
| **Critical** | VP approval, 1-week soak, mandatory drill, canary only |

---

## 7. Deployment Task vs. Deployment (Artifact)

| Aspect | Deployment Task (Work Entity) | Deployment (Work Artifact) |
|---|---|---|
| What it is | Work to be done | Record of what was done |
| Statuses | Ready → Executing → Complete / Failed | Active → Superseded → Rolled Back |
| Lifecycle | Transient | Durable audit trail |
| Applies | System Deployment Specification or Product Deployment Specification | — |

A rollback is a **new Deployment Task** applying a previous specification version (or prior sealed System/Product Version via updated specs). The original Deployment status changes to `Rolled Back`; the rollback Deployment is `Active`.

---

## 8. Change Request Design

### Types

| Type | Trigger | Governance |
|---|---|---|
| **Standard** | Release Plan, Product Version certified | Full Train traversal, CAB approval |
| **Emergency-Technical** | Incident, SEV-0/SEV-1 Bug | Abbreviated soak, documented waivers |
| **Emergency-Business** | Business exigency | Compressed Train, ODR documenting waiver |

### Scope (DR-036)

Change Requests are scoped to:

- **System Deployment** — deploying one System via System Deployment Specification
- **Product Deployment** — deploying the full product via Product Deployment Specification
- **Deployment Train** and optionally a **Station**

### Completion Criteria

1. All Deployment Tasks succeeded
2. All Verification Tasks passed
3. Audit trail documented

### Relationship to Customer Release

Customer Release (Dim 1) references a Product Version. The Change Request and Deployment workflow is how that Product Version reaches production environments. Customer Release activation may be gated on Change Request completion for regulated environments.

---

## 9. Verification Tasks

Verification Tasks are mandatory work entities that produce evidence a deployment meets acceptance criteria:

- Smoke tests (System-scoped or cross-System via Product Deployment Specification scripts)
- SLO compliance checks against Operational Targets (Dim 7)
- Security and compliance scans
- Canary metric evaluation at promotion gates

Verification failure blocks Change Request completion even if Deployment Tasks succeeded.

---

## 10. Entity Summary

### Build Artifacts (Track 2)

| Entity | Role |
|---|---|
| Component Version | Atomic CI build artifact |
| System Version | Sealed BOM of Component Versions; Component-integration verified |
| Product Version | Certified composition of System Versions; cross-System verified |

### Deployment Specifications (Track 3)

| Entity | Role |
|---|---|
| System Deployment Specification | System Version + environment config |
| Product Deployment Specification | Product Version + composed System Deployment Specs + coordination |

### Deployment Execution (Track 3)

| Entity | Role |
|---|---|
| Change Request | Governance container; System or Product deployment scope |
| Deployment Plan | Deliberation scoping the rollout |
| Deployment Planning Task | Produces deployment specifications |
| Deployment Task | Applies specification to environment |
| Deployment | Durable record of what was applied |
| Verification Task | Post-deployment validation |

### Definition Model (Dim 5 / Dim 7)

| Entity | Role |
|---|---|
| Product Specification (Dim 5) | Declares all Systems composing the product |
| System (Dim 5) | Operational deployment grouping of Components |
| Deployment Environment (Dim 7) | Target for deployment specifications |
| Deployment Train / Station (Dim 7) | Promotion path governance |

### Removed Entities (DR-036)

Module Version, Module Package Specification, Module Package Version, Product Package Specification, Product Package Version, SDD, MDD, PDD.

---

## 11. Design Rationale

### Why remove Module Version?

Module (Dim 8) is essential for product language, PSD scoping, and entitlement — but it is not an operational versioning boundary. System Version already provides composed, verified packages. Product Version provides cross-System verification. Module Version duplicated integration ceremony without distinct deployment semantics.

### Why remove the Package layer?

Operator-facing Systems (probes, reconcilers, monitoring agents) are ordinary Systems: they have repos, CI, Component Versions, and System Versions. Segregating them into Module Package / Product Package created parallel version streams and entity overhead. `Purpose / Serving Persona(s)` on System is sufficient to distinguish operational from product-facing Systems.

### Why two deployment specification levels?

- **System Deployment Specification** — what SRE applies when deploying one System (the common hotfix and incremental update case)
- **Product Deployment Specification** — what coordinates a full product release with ordering, cross-System scripts, and end-to-end validation

Module-level deployment (MDD) is eliminated because Module is not a deployment boundary.

---

## 12. Decision Records

| DR | Relevance |
|---|---|
| **DR-026** | Original three-tier versioning — amended by DR-036 (Component Version atomic tier) |
| **DR-027** | Module Package — removed by DR-036 |
| **DR-028** | SDD/MDD/PDD — replaced by System/Product Deployment Specifications |
| **DR-029** | Change Request, Deployment Train, Station — scope updated for DR-036 |
| **DR-031** | Emergency gate profile on Component/System Versions |
| **DR-035** | System/Component redefinition — versioning consequence deferred to DR-036 |
| **DR-036** | **Authoritative** — versioning chain and deployment model simplification |

---

## 13. Trade-offs and Open Items

### Trade-offs

1. **Larger Product Version BOMs.** Operational Systems appear alongside product Systems — requires clear Purpose/Persona metadata.
2. **Product Deployment Specification complexity.** Full product deploys require composing many System Deployment Specifications.
3. **Follow-on entity updates.** Track 3 entity files (`track3-change-request.md`, `track3-deployment-planning-task.md`, etc.) may still reference retired MDD/Module Package concepts — see `1.TODO`.

### Dos and Don'ts

**Do:**
- Seal System Versions before creating deployment specifications
- Scope Change Requests explicitly to System Deployment or Product Deployment
- Keep deployment specification version streams independent from build artifact versions
- Include operational Systems in Product Specification and Product Version BOMs

**Don't:**
- Treat Component Versions as independently deployable to production
- Recreate Module Version or Package layers for "convenience"
- Embed environment-specific config in System Versions
- Assume retired SDD/MDD/PDD terminology still applies

---
