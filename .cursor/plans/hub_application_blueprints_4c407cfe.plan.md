---
name: Hub Application Blueprints
overview: Extend Marketplace documentation to support Hub Application Blueprints with build recipe mechanism, enabling publishers to share reusable application containers (DSL runtimes, interpreters) that subscribers can extend with their own configuration/DSL files.
todos:
  - id: adr-hub-app-blueprints
    content: Create ADR-0102 for Hub Application Blueprints decision
    status: pending
  - id: marketplace-hub-app-doc
    content: Create hub-application-blueprints.md with full spec and recipes
    status: pending
  - id: marketplace-updates
    content: Update blueprints-and-packages.md and README.md
    status: pending
  - id: ci-blueprint-builds
    content: Create blueprint-based-builds.md for CI subsystem
    status: pending
  - id: ci-readme-update
    content: Update CI subsystem README with Blueprint builds section
    status: pending
  - id: operators-update
    content: Update marketplace-operators.md with HubApplicationBlueprintSpec
    status: pending
  - id: publisher-guide
    content: Create publishing-hub-application-blueprints.md guide
    status: pending
  - id: subscriber-guide
    content: Create using-hub-application-blueprints.md guide
    status: pending
  - id: exploration-update
    content: Update hub-marketplace-exploration.md with discussion
    status: pending
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

## Phase 3: CI Subsystem Updates

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

## Phase 4: Operators Update

| File | Changes |
|------|---------|
| [`04-subsystems/operators/marketplace-operators.md`](olympus-hub-docs/04-subsystems/operators/marketplace-operators.md) | Add `HubApplicationBlueprintSpec` to BlueprintSpec types table |

---

## Phase 5: Guides

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

## Phase 6: Exploration Document Update

| File | Changes |
|------|---------|
| [`scratchpad/hub-marketplace-exploration.md`](olympus-hub-docs/scratchpad/hub-marketplace-exploration.md) | Add new topic covering Hub Application Blueprints discussion and decisions |

---

## File Summary

| Category | New Files | Updated Files |
|----------|-----------|---------------|
| Decision Logs | 1 | - |
| Marketplace Subsystem | 1 | 2 |
| CI Subsystem | 1 | 1 |
| Operators | - | 1 |
| Guides | 2 | - |
| Scratchpad | - | 1 |
| **Total** | **5** | **5** |

---

## CRD Structures to Document

### HubApplicationBlueprintSpec

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
    
    # For buildpack
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

### HubApplicationSpec (referencing Blueprint)

```yaml
apiVersion: hub.olympus.tech/v1
kind: HubApplicationSpec
metadata:
  name: payment-integrations
spec:
  # Reference to Blueprint instead of building from source
  blueprint:
    ref: "camel-dsl-runtime"  # HubApplicationBlueprintSpec name
    version: "^3.0.0"
  
  # Inputs for the recipe
  inputs:
    dsl:
      path: "./routes/"      # Path in workbench Git
    config:
      path: "./config/"
  
  # Standard HubApplicationSpec fields
  triggers:
    - ref: payment-received-trigger
  tools:
    - name: core-banking-api
```
