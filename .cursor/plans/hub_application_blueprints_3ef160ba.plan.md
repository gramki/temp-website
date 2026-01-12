---
name: Hub Application Blueprints
overview: Extend Marketplace documentation to support Hub Application Blueprints with build recipe mechanism, and document all new Marketplace-related implementation concepts including Hub Package, BlueprintSpec, Package Subscription, Build Recipe, and Publisher.
todos:
  - id: adr-blueprints
    content: Create ADR-0102 for Hub Application Blueprints
    status: pending
  - id: impl-hub-package
    content: Create hub-package.md implementation concept
    status: pending
  - id: impl-blueprintspec
    content: Create blueprintspec.md implementation concept
    status: pending
  - id: impl-pkg-sub
    content: Create package-subscription.md implementation concept
    status: pending
  - id: impl-recipe
    content: Create build-recipe.md implementation concept
    status: pending
  - id: impl-publisher
    content: Create publisher.md implementation concept
    status: pending
  - id: impl-readme
    content: Update implementation-concepts README
    status: pending
  - id: mp-hub-app-doc
    content: Create hub-application-blueprints.md for Marketplace
    status: pending
  - id: mp-updates
    content: Update Marketplace blueprints-and-packages.md and README
    status: pending
  - id: hub-app-update
    content: Update hub-application.md with blueprint field
    status: pending
  - id: blueprint-note
    content: Update blueprint.md with disambiguation note
    status: pending
  - id: runtime-update
    content: Update automation-runtimes README
    status: pending
  - id: ci-builds-doc
    content: Create blueprint-based-builds.md for CI subsystem
    status: pending
  - id: ci-readme
    content: Update CI subsystem README
    status: pending
  - id: ops-update
    content: Update marketplace-operators.md
    status: pending
  - id: pub-guide
    content: Create publishing-hub-application-blueprints.md guide
    status: pending
  - id: sub-guide
    content: Create using-hub-application-blueprints.md guide
    status: pending
  - id: exploration
    content: Update hub-marketplace-exploration.md with Topic 15
    status: pending
---

# Hub Application Blueprints Documentation Plan

## Summary

Add support for `HubApplicationBlueprintSpec` as a new publishable artifact type in Marketplace, with a build recipe mechanism supporting `copy-only` and `buildpack` recipe types. Additionally, document all new Marketplace-related implementation concepts that have been introduced.

---

## Key Design Decisions

| Decision | Choice |

|----------|--------|

| **New Blueprint Type** | `HubApplicationBlueprintSpec` |

| **Build Approach** | Recipe-based (Publisher defines, CI executes) |

| **Recipe Types** | `copy-only` (safe default), `buildpack` (platform-approved builders) |

| **CI Integration** | CI recognizes Blueprint references, executes recipes |

| **Security Model** | Constrained recipes + sandboxed builds |

---

## Phase 1: Decision Log

Create ADR for Hub Application Blueprints:

| File | Purpose |

|------|---------|

| [`decision-logs/0102-hub-application-blueprints.md`](olympus-hub-docs/decision-logs/0102-hub-application-blueprints.md) | Document decision to add HubApplicationBlueprintSpec with recipe-based builds |

---

## Phase 2: Implementation Concepts (NEW)

Create implementation concept documents for new Marketplace-related concepts:

| File | Purpose |

|------|---------|

| [`02-system-design/implementation-concepts/hub-package.md`](olympus-hub-docs/02-system-design/implementation-concepts/hub-package.md) | Define Hub Package as atomic unit of Marketplace publishing |

| [`02-system-design/implementation-concepts/blueprintspec.md`](olympus-hub-docs/02-system-design/implementation-concepts/blueprintspec.md) | Define BlueprintSpec transformation (ScenarioNormativeSpec → ScenarioBlueprintSpec, etc.) |

| [`02-system-design/implementation-concepts/package-subscription.md`](olympus-hub-docs/02-system-design/implementation-concepts/package-subscription.md) | Define Package Subscription composite (package, tenant, workbench) |

| [`02-system-design/implementation-concepts/build-recipe.md`](olympus-hub-docs/02-system-design/implementation-concepts/build-recipe.md) | Define Build Recipe mechanism for Blueprint-based applications |

| [`02-system-design/implementation-concepts/publisher.md`](olympus-hub-docs/02-system-design/implementation-concepts/publisher.md) | Define Publisher entity and registration |

### Update Implementation Concepts README

| File | Changes |

|------|---------|

| [`02-system-design/implementation-concepts/README.md`](olympus-hub-docs/02-system-design/implementation-concepts/README.md) | Add new "Marketplace Architecture" section with 5 new concepts |

**New section to add:**

```markdown
### Marketplace Architecture

| Concept | Description | Status |
|---------|-------------|--------|
| [Hub Package](./hub-package.md) | Atomic unit of Marketplace publishing | ✅ Complete |
| [BlueprintSpec](./blueprintspec.md) | Transformed CRD for package distribution | ✅ Complete |
| [Package Subscription](./package-subscription.md) | Subscription to a Marketplace package | ✅ Complete |
| [Build Recipe](./build-recipe.md) | CI mechanism for Blueprint-based builds | ✅ Complete |
| [Publisher](./publisher.md) | Entity that publishes packages | ✅ Complete |
```

---

## Phase 3: Marketplace Subsystem Updates

### Update Existing Files

| File | Changes |

|------|---------|

| [`04-subsystems/marketplace/blueprints-and-packages.md`](olympus-hub-docs/04-subsystems/marketplace/blueprints-and-packages.md) | Add HubApplicationBlueprintSpec to Blueprint types table; add Build Recipe section; reference implementation concepts |

| [`04-subsystems/marketplace/README.md`](olympus-hub-docs/04-subsystems/marketplace/README.md) | Add Hub Application Blueprints to package content types; reference new implementation concepts |

### Create New File

| File | Purpose |

|------|---------|

| [`04-subsystems/marketplace/hub-application-blueprints.md`](olympus-hub-docs/04-subsystems/marketplace/hub-application-blueprints.md) | Detailed documentation of HubApplicationBlueprintSpec, build recipes, recipe types, security model |

---

## Phase 4: Implementation Concept Updates

**HubApplicationSpec CRD is defined in:** [`02-system-design/implementation-concepts/hub-application.md`](olympus-hub-docs/02-system-design/implementation-concepts/hub-application.md)

| File | Changes |

|------|---------|

| [`02-system-design/implementation-concepts/hub-application.md`](olympus-hub-docs/02-system-design/implementation-concepts/hub-application.md) | Add `blueprint` field to HubApplicationSpec structure; add "Blueprint-Based Applications" section; reference BlueprintSpec and Build Recipe concepts |

| [`02-system-design/implementation-concepts/blueprint.md`](olympus-hub-docs/02-system-design/implementation-concepts/blueprint.md) | Add disambiguation note: Blueprint (workbench template) vs BlueprintSpec (Marketplace artifact); cross-reference to BlueprintSpec concept |

---

## Phase 5: Automation Runtimes Updates

| File | Changes |

|------|---------|

| [`04-subsystems/automation-runtimes/README.md`](olympus-hub-docs/04-subsystems/automation-runtimes/README.md) | Add note in "Hub Application" section that applications can be built from Marketplace Blueprints |

---

## Phase 6: CI Subsystem Updates

| File | Changes |

|------|---------|

| [`04-subsystems/ci-subsystem/README.md`](olympus-hub-docs/04-subsystems/ci-subsystem/README.md) | Add Blueprint-based builds section; reference new detailed doc and Build Recipe concept |

| [`04-subsystems/ci-subsystem/blueprint-based-builds.md`](olympus-hub-docs/04-subsystems/ci-subsystem/blueprint-based-builds.md) | **New file**: CI flow for Blueprint-based applications, recipe execution, sandboxing |

---

## Phase 7: Operators Update

| File | Changes |

|------|---------|

| [`04-subsystems/operators/marketplace-operators.md`](olympus-hub-docs/04-subsystems/operators/marketplace-operators.md) | Add `HubApplicationBlueprintSpec` to BlueprintSpec types table |

---

## Phase 8: Guides

### Publisher Guide

| File | Purpose |

|------|---------|

| [`10-guides/publishing-hub-application-blueprints.md`](olympus-hub-docs/10-guides/publishing-hub-application-blueprints.md) | Step-by-step guide for publishing Hub Application Blueprints |

### Subscriber Guide

| File | Purpose |

|------|---------|

| [`10-guides/using-hub-application-blueprints.md`](olympus-hub-docs/10-guides/using-hub-application-blueprints.md) | Guide for using Hub Application Blueprints in HubApplicationSpec |

---

## Phase 9: Exploration Document Update

| File | Changes |

|------|---------|

| [`scratchpad/hub-marketplace-exploration.md`](olympus-hub-docs/scratchpad/hub-marketplace-exploration.md) | Add new topic (Topic 15) covering Hub Application Blueprints discussion and decisions |

---

## File Summary

| Category | New Files | Updated Files |

|----------|-----------|---------------|

| Decision Logs | 1 | - |

| Implementation Concepts | **5** | **3** |

| Marketplace Subsystem | 1 | 2 |

| Automation Runtimes | - | 1 |

| CI Subsystem | 1 | 1 |

| Operators | - | 1 |

| Guides | 2 | - |

| Scratchpad | - | 1 |

| **Total** | **10** | **9** |

---

## New Implementation Concepts Detail

### 1. Hub Package

**Key aspects to document:**

- Atomic unit of publishing (self-sufficient, cohesive)
- Contains BlueprintSpecs + package manifest container
- Versioning (semver)
- Relationship to containers and CRDs
- Lifecycle (create → publish → subscribe → update → unsubscribe)

### 2. BlueprintSpec

**Key aspects to document:**

- Transformation: `ScenarioNormativeSpec` → `ScenarioBlueprintSpec`
- All six BlueprintSpec types (Scenario, Tool, Machine, RawAgent, HubApplication, Workbench)
- Purpose: Distribution format (immutable, signed, versioned)
- Distinction from Blueprint (template) vs BlueprintSpec (distributed artifact)
- Derived resource creation pattern

### 3. Package Subscription

**Key aspects to document:**

- Composite: (package-listing, tenant, workbench)
- Lifecycle states (pending, active, pending-unsubscription, unsubscribed)
- Scope: Workbench-level tracking
- BlueprintSpec visibility in workbench
- Automatic subscription during cross-workbench promotion
- Orphaned package subscriptions when publisher blacklists

### 4. Build Recipe

**Key aspects to document:**

- Purpose: Define how CI combines Blueprint container with subscriber inputs
- Recipe types: `copy-only`, `buildpack`
- Structure: inputs, outputs, constraints
- Security: constrained recipes, sandboxed execution
- Integration with CI subsystem
- OCI layer deduplication benefits

### 5. Publisher

**Key aspects to document:**

- Entity that publishes packages to Marketplace
- Registration and approval process
- Signing certificates for artifacts
- Publisher identity in federated IAM
- Blacklisting capabilities
- Package listing visibility controls
- Relationship to tenant

---

## CRD Structures to Document

### HubApplicationBlueprintSpec (New)

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: HubApplicationBlueprintSpec
metadata:
  name: camel-dsl-runtime
spec:
  container:
    image: "camel-dsl-runtime"
    tag: "3.0.0"
    runtime: "rhea"
  
  buildRecipe:
    type: "copy-only"
    copyTargets:
      - source: "dsl"
        destination: "/app/routes"
      - source: "config"
        destination: "/app/config"
  
  inputs:
    - name: "dsl"
      description: "DSL route definitions"
      required: true
      filePattern: "*.xml"
    - name: "config"
      description: "Configuration files"
      required: false
  
  description: "Apache Camel DSL runtime for integration workflows"
```

### HubApplicationSpec (Updated - with Blueprint reference)

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-integrations
spec:
  # Option B: Blueprint reference (new)
  blueprint:
    ref: "camel-dsl-runtime"
    version: "^3.0.0"
  
  inputs:
    dsl:
      path: "./routes/"
    config:
      path: "./config/"
  
  runtime:
    type: rhea
  scenarios:
    - payment-integration
```