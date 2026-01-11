# Hub Application Blueprints

> **Status:** 🟡 WIP — Design Complete

Hub Application Blueprints enable publishers to share **reusable application containers** (DSL runtimes, interpreters, low-code engines) that subscribers can extend with their own configuration or DSL files.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **BlueprintSpec Type** | `HubApplicationBlueprintSpec` |
| **Purpose** | Publish reusable application containers with build recipes |
| **Key Concept** | Build Recipe (defines how CI combines base container with subscriber inputs) |
| **Recipe Types** | `copy-only`, `buildpack` |
| **Security Model** | Constrained recipes + sandboxed builds |

---

## Use Cases

Hub Application Blueprints are ideal for:

| Use Case | Description | Example |
|----------|-------------|---------|
| **DSL Runtimes** | Publish DSL interpreters, subscribers provide DSL files | Apache Camel routes, Drools rules |
| **Low-Code Engines** | Publish no-code/low-code engines, subscribers provide config | Workflow definitions, form configs |
| **API Mashup Engines** | Publish GraphQL/REST mashup engines, subscribers provide schemas | GraphQL resolvers, API composition |
| **Integration Runtimes** | Publish integration frameworks, subscribers provide adapters | MuleSoft flows, Spring Integration |

### Publisher Benefit

- Reuse proven, tested runtime containers
- Subscribers don't need to build containers from scratch
- Updates to runtime benefit all subscribers

### Subscriber Benefit

- Fast deployment — just provide configuration/DSL
- No container expertise required
- Leverage trusted, scanned base containers

---

## HubApplicationBlueprintSpec

### CRD Structure

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: HubApplicationBlueprintSpec
metadata:
  name: camel-dsl-runtime
  
spec:
  # Base container from publisher
  container:
    image: "camel-dsl-runtime"
    tag: "3.0.0"
    runtime: "rhea"  # Hub runtime type
  
  # Build recipe
  buildRecipe:
    type: "copy-only"  # or "buildpack"
    
    # For copy-only recipe
    copyTargets:
      - source: "dsl"
        destination: "/app/routes"
      - source: "config"
        destination: "/app/config"
  
  # Expected inputs from subscriber
  inputs:
    - name: "dsl"
      description: "DSL route definitions"
      required: true
      filePattern: "*.xml"
    - name: "config"
      description: "Configuration files"
      required: false
      filePattern: "*.yaml"
  
  # Documentation
  description: "Apache Camel DSL runtime for integration workflows"
  usageInstructions: |
    Provide your Camel route definitions in XML format.
    Configuration files are optional YAML files for runtime settings.
```

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `container.image` | string | Yes | Base container image name |
| `container.tag` | string | Yes | Container version tag |
| `container.runtime` | string | Yes | Hub runtime type (atlantis, rhea, seer, perseus) |
| `buildRecipe.type` | string | Yes | Recipe type: `copy-only` or `buildpack` |
| `buildRecipe.copyTargets` | array | For copy-only | Source-to-destination mappings |
| `buildRecipe.buildpack` | object | For buildpack | Buildpack configuration |
| `inputs` | array | Yes | Expected subscriber inputs |
| `description` | string | Yes | Blueprint description |
| `usageInstructions` | string | No | Detailed usage guide |

---

## Build Recipes

Build recipes define how the CI subsystem should combine the Blueprint's base container with subscriber-provided files.

### Recipe Types

| Recipe Type | Description | Security Level |
|-------------|-------------|----------------|
| `copy-only` | Only copies files to specified destinations | Safe (no arbitrary commands) |
| `buildpack` | Uses platform-approved CNB builders | Controlled (vetted builders only) |

### copy-only Recipe

The safest option — simply copies subscriber files into the container at specified destinations.

```yaml
buildRecipe:
  type: "copy-only"
  copyTargets:
    - source: "dsl"           # Matches input name
      destination: "/app/routes"
    - source: "config"
      destination: "/app/config"
```

**Execution:**
1. Pull base container from Marketplace
2. Create new OCI layer
3. Copy subscriber files to specified destinations
4. Push resulting container to subscriber's Artifact Registry

**Best for:** DSL files, configuration files, static assets

### buildpack Recipe

Uses Cloud Native Buildpacks (CNB) for scenarios requiring compilation or transformation.

```yaml
buildRecipe:
  type: "buildpack"
  buildpack:
    builder: "platform-approved-builder:1.0"
    env:
      DSL_DIR: "/app/routes"
      CONFIG_DIR: "/app/config"
```

**Execution:**
1. Pull base container from Marketplace
2. Run platform-approved buildpack
3. Buildpack processes subscriber files
4. Push resulting container to subscriber's Artifact Registry

**Best for:** Compiled languages, code generation, complex transformations

**Platform Approval:** Only buildpacks vetted and approved by Hub Platform team can be used.

---

## Subscriber Usage

Subscribers reference Hub Application Blueprints in their `HubApplicationSpec`:

### HubApplicationSpec with Blueprint Reference

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-integrations

spec:
  # Blueprint reference (instead of container)
  blueprint:
    ref: "camel-dsl-runtime"      # HubApplicationBlueprintSpec name
    version: "^3.0.0"             # Semver version range
  
  # Inputs for the recipe
  inputs:
    dsl:
      path: "./routes/"           # Path in workbench Git
    config:
      path: "./config/"
  
  # Standard HubApplicationSpec fields
  scenarios:
    - payment-integration
  
  # Runtime inherited from Blueprint if not specified
  # runtime:
  #   type: rhea
```

### Mutual Exclusivity

`HubApplicationSpec` uses either:
- `container` field (traditional build from source)
- `blueprint` field (Blueprint-based build)

Never both. The Blueprint approach replaces the container reference with a Blueprint reference plus inputs.

---

## CI Integration

When CI encounters a `HubApplicationSpec` with a Blueprint reference:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     BLUEPRINT-BASED CI BUILD FLOW                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. DETECT BLUEPRINT REFERENCE                                             │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  CI parses HubApplicationSpec                                      │    │
│   │  • Finds blueprint.ref field                                       │    │
│   │  • Resolves Blueprint from Marketplace Artifact Repository         │    │
│   │  • Fetches HubApplicationBlueprintSpec                             │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   2. VALIDATE INPUTS                                                        │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  CI validates subscriber inputs against Blueprint                  │    │
│   │  • Required inputs provided                                        │    │
│   │  • File patterns match                                             │    │
│   │  • Paths exist in workbench Git                                    │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   3. EXECUTE RECIPE                                                         │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  CI executes build recipe in sandboxed environment                 │    │
│   │  • Pull base container from Marketplace                            │    │
│   │  • Run recipe (copy-only or buildpack)                             │    │
│   │  • Produce new container with subscriber layer                     │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│   4. PUSH TO ARTIFACT REGISTRY                                              │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Result container pushed to subscriber's registry                  │    │
│   │  • OCI layer deduplication applies                                 │    │
│   │  • Base layers shared, only new layer stored                       │    │
│   │  • Container ready for deployment                                  │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ See [Blueprint-Based Builds](../ci-subsystem/blueprint-based-builds.md) for CI implementation details.

---

## Security Model

### Constrained Recipes

Only platform-defined recipe types are allowed:

| Recipe | Constraints |
|--------|-------------|
| `copy-only` | No commands executed; pure file copy |
| `buildpack` | Only platform-approved builders allowed |

No arbitrary Dockerfiles, shell scripts, or custom build logic.

### Sandboxed Build Environment

Recipe execution runs in an isolated environment:

| Control | Description |
|---------|-------------|
| **Network Isolation** | No network access during build |
| **Resource Limits** | CPU, memory, and time limits enforced |
| **Read-Only Base** | Base container accessed read-only |
| **Write Isolation** | Write access only to output layer |
| **Audit Logging** | All build operations logged |

### OCI Layer Deduplication

When subscribers build from the same Blueprint:

- Base container layers are **shared** in the registry
- Only the new layer (subscriber files) is stored per subscriber
- No "bloat" from replicated base containers
- Storage and transfer optimized

---

## Comparison with Other BlueprintSpecs

| BlueprintSpec Type | Contains | Subscriber Creates |
|-------------------|----------|-------------------|
| `ScenarioBlueprintSpec` | Scenario specifications | ScenarioNormativeSpec |
| `ToolBlueprintSpec` | Tool definitions | ToolDefinitionSpec |
| `MachineBlueprintSpec` | Machine definitions | MachineDefinitionSpec |
| `RawAgentBlueprintSpec` | Raw agent specs | RawAgentSpec |
| `HubApplicationBlueprintSpec` | Container + recipe | HubApplicationSpec (with inputs) |

The key difference: `HubApplicationBlueprintSpec` includes a **build recipe** that triggers a CI build step, producing a new container from the Blueprint.

---

## Examples

### Example 1: Apache Camel DSL Runtime

**Publisher creates:**

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: HubApplicationBlueprintSpec
metadata:
  name: camel-dsl-runtime
spec:
  container:
    image: "camel-dsl-runtime"
    tag: "3.21.0"
    runtime: "rhea"
  buildRecipe:
    type: "copy-only"
    copyTargets:
      - source: "routes"
        destination: "/app/routes"
  inputs:
    - name: "routes"
      description: "Camel route definitions (XML or YAML)"
      required: true
      filePattern: "*.{xml,yaml}"
  description: "Apache Camel runtime for integration patterns"
```

**Subscriber uses:**

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-routes
spec:
  blueprint:
    ref: "camel-dsl-runtime"
    version: "^3.21.0"
  inputs:
    routes:
      path: "./camel-routes/"
  scenarios:
    - payment-processing
```

### Example 2: Rule Engine with Buildpack

**Publisher creates:**

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: HubApplicationBlueprintSpec
metadata:
  name: drools-rule-engine
spec:
  container:
    image: "drools-rule-engine"
    tag: "8.0.0"
    runtime: "atlantis"
  buildRecipe:
    type: "buildpack"
    buildpack:
      builder: "hub-drools-builder:1.0"
      env:
        RULES_DIR: "/app/rules"
  inputs:
    - name: "rules"
      description: "DRL rule files"
      required: true
      filePattern: "*.drl"
  description: "Drools rule engine with compilation support"
```

---

## Related Documentation

- [ADR-0102: Hub Application Blueprints](../../decision-logs/0102-hub-application-blueprints.md) — Decision record
- [Blueprints and Packages](./blueprints-and-packages.md) — Package model
- [Blueprint-Based Builds](../ci-subsystem/blueprint-based-builds.md) — CI implementation
- [Build Recipe](../../02-system-design/implementation-concepts/build-recipe.md) — Concept definition
- [Hub Application](../../02-system-design/implementation-concepts/hub-application.md) — HubApplicationSpec
- [Publishing Hub Application Blueprints](../../10-guides/publishing-hub-application-blueprints.md) — Publisher guide
- [Using Hub Application Blueprints](../../10-guides/using-hub-application-blueprints.md) — Subscriber guide
