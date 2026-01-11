# ADR-0102: Hub Application Blueprints with Build Recipes

## Status

Accepted

## Date

2026-01-11

## Context

Hub Marketplace enables publishers to share various artifact types including ScenarioBlueprintSpec, ToolBlueprintSpec, MachineBlueprintSpec, and RawAgentBlueprintSpec. However, a common pattern exists where publishers want to share **reusable application containers** (DSL runtimes, interpreters, low-code engines) that subscribers can extend with lightweight configuration or DSL files.

### Example Use Cases

1. **Apache Camel DSL Runtime** — Publisher provides the Camel runtime; subscriber provides XML/YAML route definitions
2. **GraphQL Mashup Engine** — Publisher provides the GraphQL execution engine; subscriber provides schema and resolver definitions
3. **Rule Engine Runtime** — Publisher provides the rule engine; subscriber provides business rules in DSL format
4. **Workflow DSL Interpreter** — Publisher provides the interpreter; subscriber provides workflow definitions

### Challenge

Without a dedicated mechanism:
- Subscribers would need to build their own containers from scratch
- No reuse of proven, tested runtime containers
- No standardized way to combine base containers with subscriber-specific logic
- Each subscriber reinvents the wheel

### Question

How should Hub support publishing reusable application containers that subscribers can extend with their own configuration/DSL files?

## Decision

**Introduce `HubApplicationBlueprintSpec` as a new BlueprintSpec type** with a **Build Recipe mechanism** that defines how the CI subsystem should combine the Blueprint's base container with subscriber-provided files.

### Build Recipe Types

Support two constrained recipe types:

| Recipe Type | Description | Security Level |
|-------------|-------------|----------------|
| `copy-only` | Only copies files to specified destinations in the container | Safe (no arbitrary commands) |
| `buildpack` | Uses platform-approved Cloud Native Buildpack (CNB) builders | Controlled (vetted builders only) |

### HubApplicationBlueprintSpec Structure

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
    
    # For copy-only
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
  
  description: "Apache Camel DSL runtime for integration workflows"
```

### HubApplicationSpec with Blueprint Reference

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-integrations
spec:
  # Blueprint reference instead of container
  blueprint:
    ref: "camel-dsl-runtime"
    version: "^3.0.0"
  
  # Inputs for the recipe
  inputs:
    dsl:
      path: "./routes/"
    config:
      path: "./config/"
  
  scenarios:
    - payment-integration
```

### CI Integration

The CI subsystem recognizes `HubApplicationSpec` resources with Blueprint references and:

1. Resolves the Blueprint from Marketplace
2. Pulls the base container
3. Executes the recipe (copy-only or buildpack)
4. Produces a new container layer with subscriber files
5. Pushes to subscriber's Artifact Registry

### Security Model

- **Constrained Recipes**: Only platform-defined recipe types allowed (no arbitrary Dockerfiles)
- **Sandboxed Builds**: Recipe execution runs in isolated environment
- **No Network Access**: Build environment has no network connectivity
- **Resource Limits**: CPU, memory, and time limits enforced
- **OCI Layer Deduplication**: Base container layers shared; only new layer stored

## Alternatives Considered

### Alternative 1: Runtime Mount (Files mounted at runtime)

Subscriber files mounted as volumes at container startup.

**Pros:**
- No build step required
- Immediate updates

**Cons:**
- Not in Artifact Registry (breaks audit trail)
- Runtime-specific mounting mechanisms
- Security concerns with runtime injection
- No versioning of subscriber files

**Why rejected:** Files not in OCI format; breaks Artifact Registry model and audit requirements.

### Alternative 2: Layer Build (CI adds layer to base container)

CI builds a new container layer on top of Blueprint container.

**Pros:**
- Full container in Artifact Registry
- OCI format preserved
- Subscriber files versioned

**Cons:**
- Without recipes, CI doesn't know how to combine files
- Potential for arbitrary build logic (security risk)

**Why rejected:** Need structured mechanism (recipes) for CI to know what to do.

### Alternative 3: Full Dockerfile Support

Allow publishers to provide arbitrary Dockerfiles.

**Pros:**
- Maximum flexibility

**Cons:**
- Major security risk (arbitrary commands)
- Platform cannot sandbox effectively
- Inconsistent behaviors

**Why rejected:** Security risks outweigh flexibility benefits.

## Consequences

### Positive

- Enables reusable application container publishing
- Leverages OCI layer deduplication (no registry bloat)
- Secure: constrained recipes prevent arbitrary code execution
- Maintains Artifact Registry as single source of truth
- Clear separation: Publisher owns runtime, Subscriber owns logic

### Negative

- New CRD type to manage
- CI subsystem complexity increases
- Recipe types may need expansion over time

### Neutral

- Subscribers must provide files in expected format
- Build time increases slightly (recipe execution)
- Platform maintains approved buildpack list

## Implementation Notes

- Start with `copy-only` recipe type (safest, covers most DSL use cases)
- Add `buildpack` support for scenarios requiring compilation
- Platform maintains and vets approved buildpack list
- Consider `custom` recipe type (with platform review) as future escape hatch
- CI subsystem documentation must cover Blueprint-based builds

## References

- [Hub Application](../02-system-design/implementation-concepts/hub-application.md)
- [Marketplace Subsystem](../04-subsystems/marketplace/README.md)
- [Build Recipe](../02-system-design/implementation-concepts/build-recipe.md)
- [BlueprintSpec](../02-system-design/implementation-concepts/blueprintspec.md)
- [CI Subsystem](../04-subsystems/ci-subsystem/README.md)
