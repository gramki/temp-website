# Publishing Hub Application Blueprints

> **Audience:** Developers publishing reusable application containers to Marketplace

This guide walks through creating and publishing a `HubApplicationBlueprintSpec` — a reusable application container that subscribers can extend with their own DSL or configuration files.

---

## Prerequisites

Before publishing a Hub Application Blueprint:

1. **Publisher Registration** — Your tenant must be registered as a Marketplace publisher
2. **Reusable Container** — A container that can be extended with subscriber files
3. **Build Recipe Design** — Understanding of what files subscribers will provide
4. **Package Manifest** — Package metadata and visibility configuration

---

## Step 1: Design Your Blueprint

### Identify the Extension Pattern

Determine what subscribers will provide:

| Pattern | Example | Recipe Type |
|---------|---------|-------------|
| **DSL Files** | Camel routes, Drools rules | `copy-only` |
| **Configuration** | YAML/JSON config files | `copy-only` |
| **Source Code** | Compiled languages, code gen | `buildpack` |

### Define Inputs

For each subscriber input:
- Name (identifier)
- Description (documentation)
- Required or optional
- File pattern (*.xml, *.yaml, etc.)

### Design Container Structure

Ensure your base container:
- Has predictable file destinations for subscriber files
- Includes entrypoint that reads from those locations
- Is self-contained (all runtime dependencies included)

---

## Step 2: Create the HubApplicationBlueprintSpec

### Example: Apache Camel DSL Runtime

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: HubApplicationBlueprintSpec
metadata:
  name: camel-dsl-runtime
  namespace: acme-dev

spec:
  # Base container
  container:
    image: "camel-dsl-runtime"
    tag: "3.21.0"
    runtime: "rhea"

  # Build recipe
  buildRecipe:
    type: "copy-only"
    copyTargets:
      - source: "routes"
        destination: "/app/routes"
      - source: "config"
        destination: "/app/config"

  # Expected inputs from subscriber
  inputs:
    - name: "routes"
      description: "Camel route definitions (XML or YAML format)"
      required: true
      filePattern: "*.{xml,yaml}"
    - name: "config"
      description: "Optional configuration files"
      required: false
      filePattern: "*.yaml"

  # Documentation
  description: |
    Apache Camel DSL runtime for integration workflows.
    Supports XML and YAML route definitions.
  
  usageInstructions: |
    ## Getting Started
    
    1. Subscribe to this Blueprint package
    2. Create a HubApplicationSpec referencing this Blueprint
    3. Provide your Camel routes in the `routes` input
    4. Optionally provide configuration in the `config` input
    
    ## Route Format
    
    Routes can be defined in XML:
    ```xml
    <route id="payment-route">
      <from uri="direct:payment"/>
      <to uri="http://payment-service/process"/>
    </route>
    ```
    
    Or YAML:
    ```yaml
    - route:
        id: payment-route
        from:
          uri: direct:payment
        steps:
          - to: http://payment-service/process
    ```
```

### Example: Buildpack-Based Rule Engine

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: HubApplicationBlueprintSpec
metadata:
  name: drools-rule-engine
  namespace: acme-dev

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
        OUTPUT_DIR: "/app/compiled"

  inputs:
    - name: "rules"
      description: "DRL rule files to compile"
      required: true
      filePattern: "*.drl"
    - name: "types"
      description: "Java type definitions for rules"
      required: false
      filePattern: "*.java"

  description: "Drools business rule engine with DRL compilation support"
  
  usageInstructions: |
    Provide your Drools Rule Language (DRL) files.
    The buildpack will compile them during the build process.
```

---

## Step 3: Create the Package Manifest

Include the Blueprint in a package manifest:

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageManifest
metadata:
  name: camel-integration-suite
  namespace: acme-dev

spec:
  packageName: "Camel Integration Suite"
  version: "1.0.0"
  
  shortDescription: "Apache Camel runtime for Hub integration workflows"
  
  longDescription: |
    Complete integration solution based on Apache Camel.
    
    Includes:
    - Camel DSL runtime (HubApplicationBlueprintSpec)
    - Pre-built components for common integrations
    - Support for XML and YAML route definitions
  
  # Blueprint references
  blueprints:
    hubApplications:
      - name: camel-dsl-runtime
  
  # Visibility
  visibility:
    mode: "public"
  
  # Categorization
  categories:
    - "integration"
    - "middleware"
  industryTags:
    - "cross-industry"
  keywords:
    - "camel"
    - "integration"
    - "dsl"
    - "routing"
```

---

## Step 4: Publish to Marketplace

### Via Automation Developer Desk

1. Open **Marketplace Console** from Automation Developer Desk
2. Navigate to **My Packages**
3. Select the Package Manifest
4. Click **Publish to Marketplace**
5. Review package contents
6. Submit for admin approval

### Via CLI

```bash
# Validate the Blueprint
hub marketplace validate --manifest camel-integration-suite

# Initiate publishing (requires admin approval)
hub marketplace publish --manifest camel-integration-suite

# Check publishing status
hub marketplace status --manifest camel-integration-suite
```

---

## Step 5: Admin Approval

After submission:

1. Tenant Admin receives notification
2. Admin reviews package contents in Hub Control Center
3. Admin signs containers with publisher certificate
4. Admin approves submission

After approval:
1. Marketplace performs security scanning
2. Package quarantined until cleared
3. Package added to catalog
4. Subscribers can now discover and subscribe

---

## Best Practices

### Container Design

| Practice | Description |
|----------|-------------|
| **Minimal base** | Keep base container lean; only include runtime essentials |
| **Clear destinations** | Use predictable paths for subscriber files |
| **Environment variables** | Allow configuration via env vars, not just files |
| **Health checks** | Include health endpoints for runtime monitoring |
| **Versioning** | Follow semver; tag containers with version |

### Build Recipe Design

| Practice | Description |
|----------|-------------|
| **Prefer copy-only** | Use `copy-only` unless compilation is required |
| **Document inputs** | Clear descriptions and file patterns |
| **Validate early** | Container should validate inputs at startup |
| **Sensible defaults** | Make optional inputs truly optional |

### Documentation

| Include | Example |
|---------|---------|
| **Quick start** | 3-step getting started guide |
| **Input format** | Examples of valid input files |
| **Configuration options** | Available env vars and settings |
| **Troubleshooting** | Common issues and solutions |

---

## Versioning

### Semantic Versioning

Follow semver for Blueprint versions:

| Version Change | When |
|----------------|------|
| **MAJOR (X.0.0)** | Breaking changes to input format or behavior |
| **MINOR (0.X.0)** | New features, backward compatible |
| **PATCH (0.0.X)** | Bug fixes, security updates |

### Updating Published Blueprints

```bash
# Update version in HubApplicationBlueprintSpec
# Update version in PackageManifest
# Republish

hub marketplace publish --manifest camel-integration-suite
```

Subscribers will be notified of new versions and can update at their discretion.

---

## Related Documentation

- [Hub Application Blueprints](../04-subsystems/marketplace/hub-application-blueprints.md) — Technical reference
- [Blueprint-Based Builds](../04-subsystems/ci-subsystem/blueprint-based-builds.md) — CI integration
- [Package Manifest Reference](./package-manifest-reference.md) — Full manifest schema
- [Marketplace Publisher Registration](./marketplace-publisher-registration.md) — Publisher setup
