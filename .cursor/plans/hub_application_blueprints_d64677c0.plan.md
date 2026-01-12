---
name: Hub Application Blueprints
overview: Extend Marketplace documentation to support Hub Application Blueprints with build recipe mechanism, enabling publishers to share reusable application containers (DSL runtimes, interpreters) that subscribers can extend with their own configuration/DSL files.
todos:
  - id: adr-hub-app-blueprints
    content: Create ADR-0102 for Hub Application Blueprints decision
    status: completed
  - id: marketplace-hub-app-doc
    content: Create hub-application-blueprints.md with full spec and recipes
    status: completed
  - id: marketplace-updates
    content: Update blueprints-and-packages.md and README.md
    status: completed
  - id: hub-app-spec-update
    content: Update hub-application.md with blueprint field
    status: completed
  - id: automation-runtimes-update
    content: Update automation-runtimes README with Blueprint note
    status: completed
  - id: ci-blueprint-builds
    content: Create blueprint-based-builds.md for CI subsystem
    status: completed
  - id: ci-readme-update
    content: Update CI subsystem README with Blueprint builds section
    status: completed
  - id: operators-update
    content: Update marketplace-operators.md with HubApplicationBlueprintSpec
    status: completed
  - id: publisher-guide
    content: Create publishing-hub-application-blueprints.md guide
    status: completed
  - id: subscriber-guide
    content: Create using-hub-application-blueprints.md guide
    status: completed
  - id: exploration-update
    content: Update hub-marketplace-exploration.md with discussion
    status: completed
---

# Hub Application Blueprints Documentation Plan

## Summary

Add support for `HubApplicationBlueprintSpec` as a new publishable artifact type in Marketplace, with a build recipe mechanism supporting `copy-only` and `buildpack` recipe types.

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

## Phase 2: Marketplace Subsystem Updates

### Update Existing Files

| File | Changes |

|------|---------|

| [`04-subsystems/marketplace/blueprints-and-packages.md`](olympus-hub-docs/04-subsystems/marketplace/blueprints-and-packages.md) | Add HubApplicationBlueprintSpec to Blueprint types table; add Build Recipe section |

| [`04-subsystems/marketplace/README.md`](olympus-hub-docs/04-subsystems/marketplace/README.md) | Add Hub Application Blueprints to package content types |

### Create New File

| File | Purpose |

|------|---------|

| [`04-subsystems/marketplace/hub-application-blueprints.md`](olympus-hub-docs/04-subsystems/marketplace/hub-application-blueprints.md) | Detailed documentation of HubApplicationBlueprintSpec, build recipes, recipe types, security model |

**Key sections for `hub-application-blueprints.md`:**

- Overview and use cases (DSL runtimes, interpreters, low-code engines)
- HubApplicationBlueprintSpec CRD structure
- Build Recipe types (`copy-only`, `buildpack`)
- Publisher journey (creating and publishing)
- Subscriber journey (referencing in HubApplicationSpec)
- Security model (constrained recipes, sandboxed builds)
- Integration with CI subsystem

---

## Phase 3: Implementation Concept Updates

**HubApplicationSpec CRD is defined in:** [`02-system-design/implementation-concepts/hub-application.md`](olympus-hub-docs/02-system-design/implementation-concepts/hub-application.md)

| File | Changes |

|------|---------|

| [`02-system-design/implementation-concepts/hub-application.md`](olympus-hub-docs/02-system-design/implementation-concepts/hub-application.md) | Add `blueprint` field to HubApplicationSpec structure; add "Blueprint-Based Applications" section explaining the alternative source model |

**Changes to add:**

- New optional `blueprint` field in CRD (lines 90-129)
- New subsection under Structure: "Blueprint-Based Applications"
- Reference to Marketplace blueprints documentation

---

## Phase 4: Automation Runtimes Updates

| File | Changes |

|------|---------|

| [`04-subsystems/automation-runtimes/README.md`](olympus-hub-docs/04-subsystems/automation-runtimes/README.md) | Add note in "Hub Application" section (line 92) that applications can be built from Marketplace Blueprints |

**Minor addition:** A sentence noting that Hub Applications for any runtime can be sourced from Marketplace Blueprints, with the runtime determined by the Blueprint.

---

## Phase 5: CI Subsystem Updates

| File | Changes |

|------|---------|

| [`04-subsystems/ci-subsystem/README.md`](olympus-hub-docs/04-subsystems/ci-subsystem/README.md) | Add Blueprint-based builds section; reference new detailed doc |

| [`04-subsystems/ci-subsystem/blueprint-based-builds.md`](olympus-hub-docs/04-subsystems/ci-subsystem/blueprint-based-builds.md) | **New file**: CI flow for Blueprint-based applications, recipe execution, sandboxing |

**Key sections for `blueprint-based-builds.md`:**

- Build flow diagram (HubApplicationSpec refs Blueprint)
- Recipe execution engine
- `copy-only` recipe execution
- `buildpack` recipe execution
- Blueprint resolution from Marketplace
- Container output to subscriber registry
- Security/sandboxing

---

## Phase 6: Operators Update

| File | Changes |

|------|---------|

| [`04-subsystems/operators/marketplace-operators.md`](olympus-hub-docs/04-subsystems/operators/marketplace-operators.md) | Add `HubApplicationBlueprintSpec` to BlueprintSpec types table |

---

## Phase 7: Guides

### Publisher Guide

| File | Purpose |

|------|---------|

| [`10-guides/publishing-hub-application-blueprints.md`](olympus-hub-docs/10-guides/publishing-hub-application-blueprints.md) | Step-by-step guide for publishing Hub Application Blueprints |

**Key sections:**

- Prerequisites (reusable runtime container)
- Creating HubApplicationBlueprintSpec
- Defining build recipe (copy-only vs buildpack)
- Publishing workflow
- Example: Camel DSL runtime Blueprint

### Subscriber Guide

| File | Purpose |

|------|---------|

| [`10-guides/using-hub-application-blueprints.md`](olympus-hub-docs/10-guides/using-hub-application-blueprints.md) | Guide for using Hub Application Blueprints in HubApplicationSpec |

**Key sections:**

- Subscribing to Hub Application Blueprint package
- Creating HubApplicationSpec with Blueprint reference
- Providing DSL/config files
- CI build process
- Deployment

---

## Phase 8: Exploration Document Update

| File | Changes |

|------|---------|

| [`scratchpad/hub-marketplace-exploration.md`](olympus-hub-docs/scratchpad/hub-marketplace-exploration.md) | Add new topic (Topic 15) covering Hub Application Blueprints discussion and decisions |

---

## File Summary

| Category | New Files | Updated Files |

|----------|-----------|---------------|

| Decision Logs | 1 | - |

| Marketplace Subsystem | 1 | 2 |

| Implementation Concepts | - | 1 |

| Automation Runtimes | - | 1 |

| CI Subsystem | 1 | 1 |

| Operators | - | 1 |

| Guides | 2 | - |

| Scratchpad | - | 1 |

| **Total** | **5** | **7** |

---

## CRD Structures to Document

### HubApplicationBlueprintSpec (New)

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: HubApplicationBlueprintSpec
metadata:
  name: camel-dsl-runtime
spec:
  # Base container
  container:
    image: "camel-dsl-runtime"
    tag: "3.0.0"
    runtime: "rhea"  # Hub runtime type
  
  # Build recipe
  buildRecipe:
    type: "copy-only"  # or "buildpack"
    
    # For copy-only
    copyTargets:
      - source: "dsl"        # Input name
        destination: "/app/routes"
      - source: "config"
        destination: "/app/config"
    
    # For buildpack (alternative)
    buildpack:
      builder: "platform-approved-builder:1.0"
      env:
        DSL_DIR: "/app/routes"
  
  # Expected inputs from subscriber
  inputs:
    - name: "dsl"
      description: "DSL route definitions"
      required: true
      filePattern: "*.xml"
    - name: "config"
      description: "Configuration files"
      required: false
  
  # Documentation
  description: "Apache Camel DSL runtime for integration workflows"
  usageInstructions: |
    Provide your Camel route definitions in XML format...
```

### HubApplicationSpec (Updated - with Blueprint reference)

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-integrations
spec:
  # Option A: Traditional container reference
  # container:
  #   image: "registry.hub.olympus.io/..."
  #   tag: "1.0.0"
  
  # Option B: Blueprint reference (new)
  blueprint:
    ref: "camel-dsl-runtime"  # HubApplicationBlueprintSpec name
    version: "^3.0.0"
  
  # Inputs for the recipe (required when using blueprint)
  inputs:
    dsl:
      path: "./routes/"      # Path in workbench Git
    config:
      path: "./config/"
  
  # Standard fields continue...
  runtime:
    type: rhea  # Inherited from Blueprint if not specified
  scenarios:
    - payment-integration
```

---

## Build Recipe Security Model

### Constrained Recipe Types

| Recipe Type | Description | Security Level |

|-------------|-------------|----------------|

| `copy-only` | Only copies files to specified destinations | Safe (no arbitrary commands) |

| `buildpack` | Uses platform-approved CNB builders | Controlled (vetted builders only) |

### Sandboxed Build Environment

- Isolated container for build execution
- No network access during build
- Resource limits (CPU, memory, time)
- Read-only access to Blueprint container
- Write access only to output layer