# Change-to-Deployment Workflow: Analysis and Guide

This document provides a comprehensive analysis of the change-to-deployment workflow — from the moment a deployable artifact is ready through governed change management, promotion across environments, post-deployment verification, and release activation. It covers the entity architecture, the end-to-end process, the design rationale, and the trade-offs of the approach.

---

## 1. Why a Structured Deployment Workflow Matters

Enterprise SaaS products — particularly in regulated domains like fintech — face a fundamental tension: the need for deployment velocity (ship fast, iterate, respond to market) versus the need for deployment governance (audit trails, compliance, tenant assurance, rollback safety). Ad-hoc deployment practices resolve this tension poorly: either velocity wins and governance is bypassed, or governance wins and deployments become a bottleneck.

A structured deployment workflow resolves this tension by making governance a first-class concern in the information model, not an afterthought bolted onto CI/CD pipelines. The workflow must answer six questions:

1. **What is being deployed?** — the deployable composition and its operator-facing support systems
2. **How is it deployed to each environment?** — environment-specific deployment specifications
3. **Who approves the change?** — change management governance
4. **Through which environments does it progress?** — the promotion path
5. **How do we know the deployment succeeded?** — structured post-deployment verification
6. **What is the durable record?** — audit trail for compliance

---

## 2. The Four-Layer Deployment Model

The deployment workflow separates concerns into four layers, each with a distinct responsibility:

```
Layer 1: Specification (Definition Model, Dim 7)
  Module Package spec, Product Package spec
  "What operator-facing systems and wiring accompany a Module/Product"

Layer 2: Versioned Instance (Work Model, Track 3 — Artifacts)
  Module Package Version, Product Package Version
  "Which specific operator-facing system versions accompany this Module/Product Version"

Layer 3: Deployment Specification (Work Model, Track 3 — Artifacts)
  SDD, MDD, PDD
  "How this version is deployed to this environment"

Layer 4: Deployment Execution (Work Model, Track 3 — Work Entities + Artifacts)
  Change Request → Deployment Plan → Deployment Task → Deployment (record)
  "The governed, auditable act of applying a descriptor"
```

### Layer Independence

Each layer has a distinct responsibility. Changes at one layer do not necessarily require changes at others:

- Adding a new probe to a Module Package spec (Layer 1) requires new Module Package Versions (Layer 2) and updated MDDs (Layer 3), but the deployment workflow (Layer 4) is unchanged.
- Changing deployment strategy from canary to blue-green (Layer 3) requires a new MDD version but no changes to Layers 1 or 2.
- Introducing a new Deployment Train (Layer 4 governance) requires no changes to Layers 1–3.

### Three Independent Version Streams (at the integrated level)

At the Module level, three version streams evolve independently:

| Stream | What It Versions | Example Change |
|---|---|---|
| **Module Version** (Track 2) | Functional composition — which tenant-serving System Versions compose this Module | New payments-service version with rate-lock feature |
| **Module Package Version** (Track 3) | Operator-facing composition — which probes, reconcilers, dashboards accompany this Module | New healthcheck probe version with latency monitoring |
| **MDD** (Track 3) | Deployment specification — how the composition is deployed to a specific environment | New rollback script, changed scaling threshold for production |

A monitoring threshold change is an MDD version bump, not a Module Package Version change. A new reconciler is a Module Package Version change, not a Module Version change. A new API endpoint is a Module Version change, not a Package change.

---

## 3. Module Version vs. Module Package Version: The Boundary

A Module Version is a **functionally complete, commercially viable assembly** — it includes all Systems that serve tenants: product logic, tenant subscription lifecycle management (provisioning, activation, configuration by tier, upgrade, downgrade, termination), commercialization logic, and integration adapters. Module Version is the Build Track's primary output — a verified, integrated composition of System Versions.

A Module Package Version adds **only operator-facing systems** — observability probes, dashboards, automated maintenance jobs, health checks, reconcilers, and log shippers. These systems serve operators, not tenants. They are built by the Run Track's engineering function (Run Epics, Run Stories) and are critical for observing and maintaining the Module in production — but they do not participate in any tenant-facing workflow.

| Aspect | Module Version (Track 2) | Module Package Version (Track 3) |
|---|---|---|
| **Track** | Build Track | Run Track |
| **Contains** | All tenant-serving Systems — product logic, subscription lifecycle, commercialization, adapters | Only operator-facing Systems — probes, dashboards, reconcilers, log shippers, maintenance jobs |
| **Serves** | Tenants and customers | Operators and SREs |
| **Nature** | Functionally complete assembly | Operator-facing complement to Module Version |
| **Deployable alone?** | Yes, via SDDs (atomic systems deploy independently) | Not alone — always accompanies a Module Version |
| **Example Systems** | payments-service, payment-gateway, subscription-manager, tier-config-service | payments-healthcheck, payment-reconciler, payments-dashboard-agent, payments-log-shipper |

> **Boundary test.** If a System participates in a tenant-facing workflow (processing a payment, provisioning a subscription, configuring a tier), it belongs in the Module Version. If it participates only in an operator-facing workflow (monitoring health, reconciling settlements, shipping logs), it belongs in the Module Package Version.

### Module Package Specification (Definition Model, Dim 7)

The Module Package specification is the stable **template** — it defines which operator-facing systems and wiring always accompany a Module. It lives in the Definition Model (Dim 7) because this is an operator-facing concern, not visible to customers.

The Module Package Version (Work Model, Track 3) is the **versioned instance** — specific System Versions assembled at a specific point in time. This follows the same pattern as Module (Dim 8) → Module Version (Track 2): the Definition Model defines *what the thing is*; the Work Model tracks *specific instances produced by work*.

| Aspect | Module Package (Dim 7) | Module Package Version (Track 3) |
|---|---|---|
| Model | Definition Model | Work Model |
| Nature | Specification / Template | Versioned Instance / Artifact |
| Contains | Catalog of operator-facing systems (probes, dashboards, reconcilers, log shippers) | Specific versions of those operator-facing systems |
| Changes when | Operator-facing systems catalog changes (new probe added, reconciler removed) | Any constituent System Version is updated |
| Versioned? | Status lifecycle (Draft → Active → Superseded) | Explicitly versioned (e.g., v2.3.0) |
| Environment-specific? | No | No (environment-specificity is on MDD) |

---

## 4. Deployment Descriptors: SDD, MDD, PDD

Deployment descriptors are environment-specific specifications that define *how* a composition is deployed to a specific environment. They operate at three levels:

| Descriptor | Level | What It Specifies |
|---|---|---|
| **SDD** (System Deployment Descriptor) | Atomic | How a single System Version is deployed — resource limits, replicas, env vars, network policies |
| **MDD** (Module Deployment Descriptor) | Integrated | How a Module Package Version is deployed — composes SDDs, adds Module-level config, includes pre-rollout/validation/rollback scripts |
| **PDD** (Product Deployment Descriptor) | Complete | How a Product Package Version is deployed — composes MDDs, adds cross-module orchestration, deployment ordering |

Key properties:
- Descriptors are **environment-specific** — a single Module Package Version has different MDDs for production-us, production-latam, and staging
- Descriptors have their **own version stream** — independent of functional (Module Version) and operator-facing (Module Package Version) changes
- MDD scripts (migration, validation, rollback) are **engineering artifacts** — they are authored, tested, reviewed, and versioned like code

---

## 5. The Change Request → Deployment Flow

### Standard Flow

```
1. Trigger: Module Package Version is Ready, or Release Plan requires deployment
   ↓
2. Change Request created (scoped to Deployment Train)
   - Type: Standard
   - CAB review and approval
   ↓
3. Deployment Plan (deliberation)
   - Run team scopes the rollout
   - Identifies verification needs, maintenance prerequisites
   - Determines promotion path through Train stations
   ↓
4. Deployment Planning Tasks produced
   - Create SDD/MDD/PDD versions for each target environment
   - Author pre-rollout, validation, and rollback scripts
   - Create Verification Tasks for post-deployment validation
   - May create Maintenance Tasks (prerequisites)
   ↓
5. Deployment Drill Task (optional)
   - Rehearse full procedure in non-production environment
   - Must pass before actual deployment proceeds
   ↓
6. Deployment Tasks execute (per station in the Train)
   - Apply descriptor to target environment
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

### Emergency-Technical Flow (from Incident)

The emergency flow spans two tracks with complementary fast-paths:

**Build Track fast-path (DR-031):**
```
Incident (SEV-0/SEV-1) → Incident Response Task → Bug (P0, Run provenance)
  → Technical Task (sprint bypass, immediate allocation)
    → System Version (Emergency gate profile: peer review + security scan + smoke tests;
       full regression + benchmarks deferred)
      → SDD
```

**Run Track fast-path (DR-029):**
```
Change Request (Emergency-Technical)
  - Abbreviated soak times
  - Documented waiver for bypassed stations
  - Drill may be skipped with justification
  ↓
Deployment Task → Deployment → Verification Task
  ↓
Change Request Complete
```

**Deferred-gate obligation (DR-031):** The Bug stays at `Fixed` (not `Closed`) until a subsequent Standard System Version passes all deferred quality gates. This prevents emergency hotfixes from permanently lowering quality standards.

### Emergency-Business Flow (from Release Plan acceleration)

```
Business exigency (campaign deadline, festival day)
  ↓
Change Request (Emergency-Business)
  - Originates from Release Plan acceleration
  - Compressed Train (abbreviated soak, fast-track stations)
  - ODR documents the waiver and business justification
  ↓
Standard deployment flow but with compressed timelines
```

---

## 6. Deployment Train and Station Design

### What Is a Deployment Train?

A Deployment Train is a reusable, ordered promotion path — the defined sequence of environments a deployment progresses through, with governance, approval, and soak requirements at each stop. Trains are Definition Model entities (Dim 7), not ad-hoc workflows.

### Contractual Significance

A Deployment Train is not just an internal workflow — it carries contractual significance:

- **Tenant assurance.** Tenants may rely on the Train's promotion path to plan changes to their dependent applications. When code reaches a staging station, tenant integration teams can begin testing.
- **Commercial contracts.** Contracts may reference Trains for safety and compliance guarantees (e.g., "all production changes traverse staging with minimum 72-hour soak").
- **Operating model enforcement.** A Regulated-governance Train may reject Emergency-Business changes that bypass required stations, while a Standard-governance Train may accept them with documented waivers.

### Station Design

Each Station in a Train is a checkpoint targeting a specific Deployment Environment with defined:

- **Entry criteria**: what must be true before a deployment can enter (e.g., previous station soak complete)
- **Exit/promotion criteria**: what must be verified before promotion (e.g., 72h soak with zero P1s)
- **Approval requirements**: who must sign off (automated, CAB, compliance officer)
- **Soak time**: minimum stabilization window
- **Verification requirements**: which Verification Task types are mandatory at this station

The same Deployment Environment can be a Station in multiple Trains with different governance requirements. For example, Staging EU-West might be a Station in both the PCI Regulated Train (72h soak, security scan required) and the Fast-Track Train (no minimum soak, automated approval).

### Governance Levels

| Level | Example Train | Characteristics |
|---|---|---|
| **Standard** | Fast-Track Train | Automated approvals, minimal soak, self-service |
| **Regulated** | PCI Regulated Train | CAB approval, 72h soak, compliance officer sign-off, mandatory drill |
| **Critical** | Core Infrastructure Train | VP approval, 1-week soak, mandatory drill, canary only, compliance + security sign-off |

### Tenant Visibility

Tenants derive visibility into deployment progress through their Deployment Environment: if a tenant's subscription is provisioned in production-latam, and production-latam is a Station on the PCI Regulated Train, the tenant has derived visibility into that Train's progress. Notification of Change Requests and their updates to environments where tenant subscriptions reside is an Operating Model decision, not a model constraint.

---

## 7. Deployment Task vs. Deployment (Artifact)

The model separates "work to be done" from "record of what was done" — consistent with every other track in the Work Model:

| Aspect | Deployment Task (Work Entity) | Deployment (Work Artifact) |
|---|---|---|
| What it is | Work to be done | Record of what was done |
| Statuses | Ready → Executing → Complete / Failed | Active → Superseded → Rolled Back |
| Lifecycle | Transient — exists while work is in progress | Durable — persists as audit trail |
| Relationships | Governed by Deployment Plan, applies descriptor | Produced by Deployment Task, enables Customer Release |
| Analogy | Specification Task produces a PSD | The PSD is the artifact |

A rollback is a new Deployment Task that produces a new Deployment record pointing to a previous descriptor version. The original Deployment's status changes to `Rolled Back`; the rollback Deployment is `Active`.

---

## 8. Change Request Design

### Types

| Type | Trigger | Governance | Example |
|---|---|---|---|
| **Standard** | Release Plan, Module Package Version ready | Full Train traversal, CAB approval | "Deploy Payments v2.3.0 through PCI Regulated Train" |
| **Emergency-Technical** | Incident, SEV-0/SEV-1 Bug | Abbreviated soak, documented waivers for bypassed stations | "Hotfix for payment processing failure in production-latam" |
| **Emergency-Business** | Business exigency, campaign deadline | Compressed Train, fast-track stations, ODR documenting waiver | "Accelerate FX feature for LATAM campaign launch" |

### Scope

Change Requests are scoped to a Deployment Train or a specific Station (and transitively to a Package or descriptor). This scoping connects the change to the governance framework — the Train determines what approval, soak, and verification requirements apply.

### Completion Criteria

A Change Request is complete only when:
1. All Deployment Tasks have succeeded (descriptors applied to target environments)
2. All Verification Tasks have passed (post-deployment validation evidence collected)
3. Audit trail is documented

Deployment success alone is not sufficient — verification must also pass.

### Relationship to Customer Release

A single Customer Release may span multiple Deployment Trains when different modules follow different promotion paths. For example, an "LATAM Expansion" release might include payment modules on a PCI Regulated Train and a marketing portal on a Fast-Track Train. The Customer Release is the commercial unit; the Deployment Train is the operational promotion unit.

---

## 9. Pros and Cons of This Approach

### Advantages

**Separation of concerns across four layers.** Each layer (specification, versioned instance, deployment descriptor, execution) evolves independently. A monitoring threshold change does not require a new Module Package Version. A new probe does not require a new MDD. This reduces unnecessary coupling and prevents version inflation.

**Auditable change management.** Every deployment to a governed environment is traceable: Change Request → Deployment Plan → Deployment Task → Deployment record → Verification evidence. Regulated environments (PCI-DSS, SOC 2, LGPD) require this audit chain. The model makes it structural, not a process overlay.

**Contractual deployment governance.** Deployment Trains with Stations provide a formal, reusable construct that commercial contracts can reference. Tenants and partners can rely on promotion paths for planning. This is difficult to achieve with ad-hoc promotion workflows because there is no entity to reference in a contract.

**Clean work/artifact separation.** Deployment Task (transient work) vs. Deployment (durable record) follows the pattern used in every other track. This makes the model internally consistent and allows lifecycle management tools to treat all work entities and artifacts uniformly.

**Structured verification.** Verification Tasks make post-deployment validation explicit, trackable, and auditable. Compliance teams can query "which verifications passed for this deployment?" without parsing CI/CD logs. Change Request closure requires verification to pass — deployment success alone is insufficient.

**Emergency change handling.** The three Change Request types (Standard, Emergency-Technical, Emergency-Business) acknowledge that not all changes follow the same governance path. Emergency changes still create Change Requests and Deployment records — they don't bypass the model, they traverse it with documented waivers.

**Operator-facing systems modeled explicitly.** The Module Package specification (Dim 7) and Module Package Version (Track 3) give operator-facing systems (probes, dashboards, reconcilers) a structured home with clear ownership (Run Track) and a clear boundary (operator-facing only, not tenant-serving).

### Disadvantages and Trade-offs

**Entity proliferation.** The model introduces several new entities: Deployment Train, Station, Deployment Plan, Deployment Task, Verification Task, Deployment Drill Task, Module Package (spec), Product Package (spec). Teams must learn and maintain these entities. For small organizations with simple deployment needs, this may be over-engineering.

**Overhead for low-risk deployments.** A configuration change to a non-production environment still requires a Change Request (even if approval is automated). Organizations deploying 20+ times per day to development environments may find the Change Request → Deployment Plan → Deployment Task chain heavyweight. Mitigation: Standard-governance Trains can have fully automated approval with minimal soak, and operating models may define exemptions for non-governed environments.

**Module Package boundary requires judgment, not rigid rules.** Everything an operator does ultimately benefits tenants — directly or indirectly. The distinction is not "who benefits" but "who builds it and whose workflow it automates." Systems built by operators to automate their own work (self-healing, pod restarts, reconciliation, log shipping) belong in the Module Package Version — even though tenants indirectly benefit from the resulting reliability. Product/Module Versions may also address operator needs: the product team might build an admin console, an operational dashboard, or a deployment API as first-class product capabilities. The difference is ownership and provenance: if the Run Track builds it to solve their own pains and needs, it goes in the Package. If the Build Track builds it as a product capability (even one targeted at an operator persona), it goes in the Module Version. Both paths are valid — operators should have the ability to solve their own pains through their own engineering, and the product should also invest in operator experience as a first-class concern.

**Deployment Train rigidity.** A Deployment Train defines a fixed ordered sequence of Stations. In practice, some deployments may need to skip stations (e.g., a hotfix that goes straight to production after minimal staging). The model accommodates this via Emergency Change types with documented waivers, but teams may feel the Train structure is overly prescriptive. Mitigation: Trains are reusable but not mandatory — different modules can use different Trains, and Trains can be designed with varying governance levels.

**Deployment Drill adoption.** Deployment Drill Tasks are optional, but their value is highest for exactly the deployments where teams are least likely to want the overhead (complex DB migrations, first-time deployments to new regions). Cultural adoption may lag behind model availability.

**Verification Task completeness.** The model requires all Verification Tasks to pass before Change Request closure, but it does not prescribe what constitutes adequate verification. A team could create a trivial "smoke test" Verification Task and technically satisfy the model. The quality of verification is an Operating Model concern, not a model constraint — but the model's structural assurance is only as strong as the verification it governs.

---

## 10. Guidance for Run Track Participants

### Do

- **Do** scope every deployment-related change to a Deployment Train or Station via a Change Request
- **Do** create Verification Tasks during Deployment Planning — verification is not optional in regulated environments
- **Do** use Deployment Drill Tasks for high-risk deployments (DB migrations, multi-module orchestration, first deployment to new environments)
- **Do** document Emergency Change justifications via ODRs — every bypassed station or abbreviated soak needs a documented waiver
- **Do** treat MDD scripts (pre-rollout, validation, rollback) as engineering work — they are code, not configuration
- **Do** use the boundary test: tenant-serving Systems belong in Module Version; operator-facing Systems belong in Module Package Version

### Don't

- **Don't** deploy without a Change Request — even Emergency changes need a CR (just with a different type and abbreviated approval)
- **Don't** conflate "deployment succeeded" with "Change Request is complete" — all Verification Tasks must also pass
- **Don't** modify Module Package Versions to be environment-specific — environment-specific configuration belongs on the MDD/PDD
- **Don't** skip Deployment Planning for "simple" deployments — the planning is where you discover maintenance prerequisites, verification needs, and risks
- **Don't** assume a single Train fits all modules — PCI-regulated payment modules and non-PCI marketing portals may need different Trains with different governance levels
- **Don't** put tenant-serving systems in Module Package Version — subscription management, provisioning, tier configuration belong in Module Version

---

## 11. Entity Summary

| Entity | Model | Role |
|---|---|---|
| **Module Package** (spec) | Definition Model, Dim 7 | Template: which operator-facing systems accompany a Module |
| **Product Package** (spec) | Definition Model, Dim 7 | Template: which cross-module operator-facing systems accompany a Product |
| **Deployment Train** | Definition Model, Dim 7 | Reusable promotion path with contractual and governance significance |
| **Station** | Definition Model, Dim 7 | Checkpoint within a Train — entry/exit criteria, approval, soak time |
| **Module Package Version** | Work Model, Track 3 | Versioned instance of Module Package spec — operator-facing systems assembled |
| **Product Package Version** | Work Model, Track 3 | Versioned instance of Product Package spec — cross-module operator-facing layer |
| **SDD / MDD / PDD** | Work Model, Track 3 | Environment-specific deployment specifications at three composition levels |
| **Change Request** | Work Model, Track 3 | Auditable change management envelope (Standard / Emergency-Technical / Emergency-Business) |
| **Deployment Plan** | Work Model, Track 3 | Deliberation activity — scopes rollout, produces planning tasks, identifies verification needs |
| **Deployment Task** | Work Model, Track 3 | Work entity — applies a descriptor to an environment |
| **Deployment** (artifact) | Work Model, Track 3 | Durable record that a descriptor was applied |
| **Verification Task** | Work Model, Track 3 | Post-deployment verification — criteria, evidence, pass/fail |
| **Deployment Drill Task** | Work Model, Track 3 | Optional rehearsal of a Deployment Plan in non-production |

---

## 12. Decision Records

The design decisions underpinning this workflow are recorded in:

- **DR-026** — System Version as the atomic deployment unit
- **DR-027** — Composition levels and Run Track engineering (Module Package, Product Package)
- **DR-028** — Deployment descriptors (SDD, MDD, PDD)
- **DR-029** — Change-to-deployment workflow redesign (13 decisions: D1–D13)

---
