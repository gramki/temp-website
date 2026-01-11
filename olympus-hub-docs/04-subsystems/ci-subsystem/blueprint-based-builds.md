# Blueprint-Based Builds

> **Status:** 🟡 WIP — Design Complete

This document describes how the CI subsystem handles builds for Hub Applications that reference Marketplace Blueprints instead of building from source.

---

## Overview

When a `HubApplicationSpec` references a `HubApplicationBlueprintSpec` from the Marketplace (instead of specifying a `container`), the CI subsystem executes the Blueprint's **build recipe** to produce the final application container.

| Aspect | Description |
|--------|-------------|
| **Trigger** | HubApplicationSpec with `blueprint` field detected |
| **Input** | Blueprint from Marketplace + subscriber files from Git |
| **Process** | Execute Blueprint's build recipe |
| **Output** | Application container in subscriber's Artifact Registry |

---

## Build Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     BLUEPRINT-BASED BUILD FLOW                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SUBSCRIBER WORKBENCH                                                       │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   HubApplicationSpec                    Git Repository               │   │
│   │   ┌────────────────────┐               ┌────────────────────┐       │   │
│   │   │ blueprint:         │               │ /routes/           │       │   │
│   │   │   ref: camel-dsl   │               │   route-1.xml      │       │   │
│   │   │   version: ^3.0.0  │               │   route-2.xml      │       │   │
│   │   │ inputs:            │               │ /config/           │       │   │
│   │   │   dsl: ./routes/   │               │   app.yaml         │       │   │
│   │   │   config: ./config/│               │                    │       │   │
│   │   └─────────┬──────────┘               └─────────┬──────────┘       │   │
│   │             │                                    │                   │   │
│   └─────────────│────────────────────────────────────│───────────────────┘   │
│                 │                                    │                       │
│                 ▼                                    ▼                       │
│   CI SUBSYSTEM                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   1. RESOLVE BLUEPRINT                                               │   │
│   │   ┌────────────────────────────────────────────────────────────────┐ │   │
│   │   │ • Parse HubApplicationSpec                                     │ │   │
│   │   │ • Resolve blueprint.ref from Marketplace                       │ │   │
│   │   │ • Fetch HubApplicationBlueprintSpec                            │ │   │
│   │   │ • Verify package subscription exists                           │ │   │
│   │   └────────────────────────────────────────────────────────────────┘ │   │
│   │                              │                                       │   │
│   │                              ▼                                       │   │
│   │   2. VALIDATE INPUTS                                                 │   │
│   │   ┌────────────────────────────────────────────────────────────────┐ │   │
│   │   │ • Check required inputs provided                               │ │   │
│   │   │ • Verify file paths exist in Git                               │ │   │
│   │   │ • Validate file patterns match                                 │ │   │
│   │   └────────────────────────────────────────────────────────────────┘ │   │
│   │                              │                                       │   │
│   │                              ▼                                       │   │
│   │   3. PREPARE BUILD ENVIRONMENT                                       │   │
│   │   ┌────────────────────────────────────────────────────────────────┐ │   │
│   │   │ • Create sandboxed build container                             │ │   │
│   │   │ • Pull base container from Marketplace                         │ │   │
│   │   │ • Mount subscriber files (read-only)                           │ │   │
│   │   │ • Apply resource limits (CPU, memory, time)                    │ │   │
│   │   └────────────────────────────────────────────────────────────────┘ │   │
│   │                              │                                       │   │
│   │                              ▼                                       │   │
│   │   4. EXECUTE RECIPE                                                  │   │
│   │   ┌────────────────────────────────────────────────────────────────┐ │   │
│   │   │ • For copy-only: Copy files to destinations                    │ │   │
│   │   │ • For buildpack: Run platform-approved builder                 │ │   │
│   │   │ • Create new OCI layer with subscriber content                 │ │   │
│   │   └────────────────────────────────────────────────────────────────┘ │   │
│   │                              │                                       │   │
│   │                              ▼                                       │   │
│   │   5. PUSH RESULT                                                     │   │
│   │   ┌────────────────────────────────────────────────────────────────┐ │   │
│   │   │ • Tag container with version                                   │ │   │
│   │   │ • Push to subscriber's Artifact Registry                       │ │   │
│   │   │ • OCI layer deduplication applied                              │ │   │
│   │   │ • Log build metadata                                           │ │   │
│   │   └────────────────────────────────────────────────────────────────┘ │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│   SUBSCRIBER ARTIFACT REGISTRY                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  ┌─────────────────────┐                                            │   │
│   │  │ payment-integrations│  ◄── New container with:                   │   │
│   │  │ :1.0.0              │      • Base layers from Blueprint          │   │
│   │  └─────────────────────┘      • New layer with subscriber files     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Recipe Execution

### copy-only Recipe

The simplest and safest recipe type. Copies subscriber files to specified destinations in the container.

**Blueprint Recipe:**
```yaml
buildRecipe:
  type: "copy-only"
  copyTargets:
    - source: "dsl"
      destination: "/app/routes"
    - source: "config"
      destination: "/app/config"
```

**Execution Steps:**
1. Pull base container image
2. Create new OCI layer
3. For each `copyTarget`:
   - Read files from subscriber's Git at `inputs.<source>.path`
   - Copy to `destination` in the new layer
4. Finalize layer and push

**Security:** No commands executed; purely declarative file operations.

### buildpack Recipe

Uses Cloud Native Buildpacks (CNB) for scenarios requiring compilation or transformation.

**Blueprint Recipe:**
```yaml
buildRecipe:
  type: "buildpack"
  buildpack:
    builder: "hub-drools-builder:1.0"
    env:
      RULES_DIR: "/app/rules"
```

**Execution Steps:**
1. Pull base container image
2. Invoke platform-approved buildpack
3. Buildpack processes subscriber files
4. Buildpack produces output layer
5. Push resulting container

**Security:** Only platform-vetted builders allowed. Builder list maintained by Hub Platform team.

---

## Sandboxed Build Environment

All recipe execution occurs in an isolated environment:

| Control | Description |
|---------|-------------|
| **Container Isolation** | Build runs in dedicated container |
| **Network Disabled** | No network access during build |
| **Resource Limits** | CPU, memory, and time limits enforced |
| **Read-Only Base** | Blueprint container accessed read-only |
| **Read-Only Inputs** | Subscriber files mounted read-only |
| **Write Isolation** | Only output layer can be written |
| **Audit Logging** | All operations logged to Olympus Watch |

### Resource Limits

| Resource | Default Limit | Configurable |
|----------|---------------|--------------|
| CPU | 2 cores | Yes (subscription-level) |
| Memory | 4 GB | Yes (subscription-level) |
| Build Time | 10 minutes | Yes (subscription-level) |
| Disk | 10 GB | No |

---

## OCI Layer Deduplication

When multiple subscribers build from the same Blueprint:

```
Marketplace Artifact Repository:
┌────────────────────────────────────┐
│ camel-dsl-runtime:3.0.0            │
│ ├── Layer 1: Base OS (sha:abc123)  │ ◄─── Shared
│ ├── Layer 2: Runtime (sha:def456)  │ ◄─── Shared
│ └── Layer 3: Camel (sha:ghi789)    │ ◄─── Shared
└────────────────────────────────────┘

Subscriber A Registry:                 Subscriber B Registry:
┌────────────────────────────────┐    ┌────────────────────────────────┐
│ payment-routes:1.0.0           │    │ order-routes:1.0.0             │
│ ├── Layer 1 (ref: sha:abc123)  │    │ ├── Layer 1 (ref: sha:abc123)  │
│ ├── Layer 2 (ref: sha:def456)  │    │ ├── Layer 2 (ref: sha:def456)  │
│ ├── Layer 3 (ref: sha:ghi789)  │    │ ├── Layer 3 (ref: sha:ghi789)  │
│ └── Layer 4: A's routes (new)  │    │ └── Layer 4: B's routes (new)  │
└────────────────────────────────┘    └────────────────────────────────┘
```

**Benefits:**
- Base layers stored once (referenced by SHA)
- Only subscriber-specific layer stored per build
- Minimal registry storage growth
- Efficient transfer (only new layer pulled on deployment)

---

## Blueprint Resolution

When CI encounters a Blueprint reference:

1. **Parse version constraint** — Semver range (e.g., `^3.0.0`)
2. **Query Marketplace** — Find matching HubApplicationBlueprintSpec
3. **Verify subscription** — Confirm workbench has active package subscription
4. **Fetch Blueprint** — Download BlueprintSpec and container reference
5. **Validate compatibility** — Check recipe type is supported

### Version Resolution

| Constraint | Matches | Example |
|------------|---------|---------|
| `^3.0.0` | 3.x.x (>=3.0.0 <4.0.0) | 3.0.0, 3.1.0, 3.2.5 |
| `~3.1.0` | 3.1.x (>=3.1.0 <3.2.0) | 3.1.0, 3.1.5 |
| `3.0.0` | Exact match | 3.0.0 only |
| `>=3.0.0` | 3.0.0 and above | 3.0.0, 4.0.0, 5.2.1 |

---

## Build Triggers

Blueprint-based builds are triggered by:

| Trigger | Description |
|---------|-------------|
| **Git Push** | Changes to subscriber input files (routes, config) |
| **On Demand** | Manual trigger via UI/CLI |
| **Promotion** | As part of promotion validation |
| **Blueprint Update** | When a new Blueprint version is subscribed |

### CITrigger Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: CITrigger
metadata:
  name: build-payment-routes
  namespace: acme-bank
spec:
  workbench: payment-ops-dev
  
  trigger:
    type: git_push
    paths:
      - "routes/**"
      - "config/**"
  
  actions:
    - type: blueprint_build
      target:
        application: payment-routes
```

---

## Error Handling

| Error | Behavior |
|-------|----------|
| **Blueprint not found** | Build fails with clear error |
| **No active subscription** | Build fails; user prompted to subscribe |
| **Required input missing** | Build fails; lists missing inputs |
| **File pattern mismatch** | Warning logged; build continues |
| **Build timeout** | Build aborted; logs preserved |
| **Recipe execution failure** | Build fails; detailed error in logs |

---

## Build Metadata

Each Blueprint-based build records:

```yaml
buildMetadata:
  type: blueprint
  blueprint:
    name: camel-dsl-runtime
    version: 3.0.0
    packageUri: marketplace://packages/camel-suite-v3.0.0
    packageSha: sha256:abc123...
  recipe:
    type: copy-only
    executionTime: 12s
  inputs:
    - name: dsl
      path: ./routes/
      fileCount: 5
    - name: config
      path: ./config/
      fileCount: 2
  output:
    image: registry.hub.olympus.io/acme-bank/payment-routes
    tag: 1.0.0
    sha: sha256:xyz789...
  timestamp: 2026-01-11T10:30:00Z
```

---

## Related Documentation

- [Hub Application Blueprints](../marketplace/hub-application-blueprints.md) — Blueprint model
- [Build Recipe](../../02-system-design/implementation-concepts/build-recipe.md) — Concept definition
- [ADR-0102: Hub Application Blueprints](../../decision-logs/0102-hub-application-blueprints.md) — Decision record
- [Artifact Registry](../artifact-registry/README.md) — Container storage
- [Runtime CI](./runtime-ci.md) — Traditional source-based builds
