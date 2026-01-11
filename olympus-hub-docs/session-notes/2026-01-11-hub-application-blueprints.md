# Session Notes: Hub Application Blueprints

**Date:** 2026-01-11  
**Topic:** Extending Marketplace to support Hub Application Blueprints with build recipes

---

## Session Objective

Extend the Marketplace subsystem to support publishing and subscribing to `HubApplicationBlueprintSpec` — reusable application containers (DSL runtimes, interpreters, low-code engines) that subscribers can extend with their own configuration or DSL files.

---

## Discussion Summary

### Problem Statement

Publishers want to share reusable application containers (e.g., Apache Camel DSL runtime, Drools rule engine) where:
- Publisher provides the base runtime container
- Subscriber provides lightweight configuration/DSL files
- Combined into a deployable application

### Key Questions Resolved

1. **How should subscribers combine their files with the Blueprint container?**
   - Solution: **Build Recipe** mechanism defined in `HubApplicationBlueprintSpec`
   
2. **What recipe types should be supported?**
   - `copy-only` — Safe default; copies files to specified destinations
   - `buildpack` — Uses platform-approved CNB builders for compilation scenarios

3. **How does CI package subscriber DSL files into OCI format?**
   - CI detects Blueprint reference in `HubApplicationSpec`
   - Executes build recipe in sandboxed environment
   - Produces new container layer with subscriber files
   - Pushes to subscriber's Artifact Registry

4. **Will the Artifact Registry bloat with replicated base containers?**
   - No — OCI layer deduplication means base layers are shared
   - Only subscriber-specific layer stored per build

5. **What about security concerns with build recipes?**
   - Constrained recipe types (no arbitrary Dockerfiles)
   - Sandboxed build environment (no network access)
   - Resource limits (CPU, memory, time)
   - Only platform-vetted buildpacks allowed

---

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| New BlueprintSpec type | `HubApplicationBlueprintSpec` | Distinct from other BlueprintSpecs due to build recipe |
| Build approach | Recipe-based | Publisher defines, CI executes; safe and predictable |
| Initial recipe types | `copy-only`, `buildpack` | Start safe, expand as needed |
| CI integration | Blueprint-aware build path | Recognizes `blueprint` field, executes recipe |
| Security model | Constrained + sandboxed | No arbitrary code execution in builds |

---

## Documentation Created

### Decision Log
- `decision-logs/0102-hub-application-blueprints.md`

### Subsystem Documentation
- `04-subsystems/marketplace/hub-application-blueprints.md` — Full technical reference
- `04-subsystems/ci-subsystem/blueprint-based-builds.md` — CI flow and recipe execution

### Guides
- `10-guides/publishing-hub-application-blueprints.md` — Publisher workflow
- `10-guides/using-hub-application-blueprints.md` — Subscriber workflow

### Updated Files
- `04-subsystems/marketplace/blueprints-and-packages.md` — Added HubApplicationBlueprintSpec
- `04-subsystems/marketplace/README.md` — Added to package types
- `02-system-design/implementation-concepts/hub-application.md` — Added `blueprint` field
- `04-subsystems/automation-runtimes/README.md` — Blueprint-sourced applications note
- `04-subsystems/ci-subsystem/README.md` — Blueprint builds component
- `04-subsystems/operators/marketplace-operators.md` — New BlueprintSpec type
- `scratchpad/hub-marketplace-exploration.md` — Topic 15 added

---

## CRD Structures Defined

### HubApplicationBlueprintSpec

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
  inputs:
    - name: "dsl"
      description: "DSL route definitions"
      required: true
      filePattern: "*.xml"
```

### HubApplicationSpec (with Blueprint reference)

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-routes
spec:
  blueprint:
    ref: "camel-dsl-runtime"
    version: "^3.0.0"
  inputs:
    dsl:
      path: "./routes/"
  scenarios:
    - payment-processing
```

---

## File Summary

| Category | New | Updated |
|----------|-----|---------|
| Decision Logs | 1 | — |
| Marketplace Subsystem | 1 | 2 |
| CI Subsystem | 1 | 1 |
| Implementation Concepts | — | 1 |
| Automation Runtimes | — | 1 |
| Operators | — | 1 |
| Guides | 2 | — |
| Scratchpad | — | 1 |
| **Total** | **5** | **7** |

---

## Open Items for Future Consideration

1. **Additional recipe types** — `custom` with platform review as escape hatch
2. **Buildpack governance** — Process for vetting and approving buildpacks
3. **Blueprint update propagation** — How subscribers are notified of security patches

---

## Session Outcome

Successfully extended Marketplace to support Hub Application Blueprints with a secure, recipe-based build mechanism. The design enables publishers to share reusable application containers while maintaining security through constrained recipes and sandboxed builds.
