# CI Subsystem

> **Category:** DevOps and Lifecycle

---

## Overview

The **CI Subsystem** provides build and test infrastructure for Hub Applications. Each Automation Runtime includes runtime-specific CI capabilities, while the Hub Test Runner provides integration testing. CI is CRD-based and subscription-standardized, with platform-provided defaults.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't address build and test infrastructure. CI Subsystem is an implementation concept for automation development.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Automation | Hub Application | CI builds applications |
| (not covered) | CI Subsystem | Build and test |

### Gap This Fills

The ontology focuses on runtime. CI Subsystem addresses:
1. **Building**: How are applications built?
2. **Testing**: How are applications validated?
3. **Integration**: How does CI connect to registry?

---

## Definition

**CI Subsystem** is the build and test infrastructure that:
- Provides runtime-specific CI for each Automation Runtime
- Runs unit tests as part of the build process
- Publishes built artifacts to Artifact Registry
- Integrates with Olympus Watch for logs

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Subscription-level; standardized per runtime |
| **Lifecycle** | Triggered by developer; runs builds |
| **Ownership** | Platform provides; developer uses |
| **Multiplicity** | One CI config per runtime per subscription |

---

## Structure

### CI Architecture

```
CI Subsystem
├── Runtime CI (per runtime)
│   ├── Atlantis CI (containers)
│   ├── Rhea CI (workflows)
│   ├── Seer CI (AI agents)
│   └── Perseus CI (batch)
│
└── Hub Test Runner (integration)
    └── Tests against I/O Gateway
```

### CI Configuration

```yaml
# CI defaults provided by platform
# Overrides by admin are future feature

ci_config:
  runtime: atlantis
  subscription: acme-dev
  
  build:
    trigger: on_demand    # on_demand | on_push | scheduled
    timeout_minutes: 30
    
  test:
    unit_tests: enabled
    coverage_threshold: 80
    
  publish:
    registry: snapshot
    tag_with_sha: true
```

### Runtime-Specific CI

| Runtime | Build | Test | Output |
|---------|-------|------|--------|
| **Atlantis** | Docker build | Python/Node tests | OCI container |
| **Rhea** | BPMN validation | Process simulation | Workflow package |
| **Seer** | Agent validation | Prompt testing | Agent package |
| **Perseus** | Batch validation | Sample data tests | Batch package |

---

## Behavior

### CI Flow

```
1. Developer triggers CI
   └── Via CLI, UI, or configured trigger

2. Runtime CI executes
   ├── Fetch source (from reference or sync)
   ├── Build artifact
   ├── Run unit tests
   └── Collect coverage

3. On success:
   ├── Publish to snapshot registry
   ├── Tag with version and SHA
   └── Log to Olympus Watch

4. On failure:
   ├── Log errors
   └── Notify developer
```

### CI Output

```
Build result:
├── Container image (pushed to registry)
├── Build logs (in Watch)
├── Test results (in CI console)
└── Coverage report (if configured)
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Artifact Registry | → pushes | Built artifacts |
| Git Repository | ← reads | Source code/CRDs |
| Olympus Watch | → logs | Build logs |
| Developer | ← used by | Triggers builds |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Runtime-specific** | CI varies by runtime |
| **Subscription-scoped** | CI config per subscription |
| **Tests required** | Unit tests part of build |
| **Registry publish** | Successful builds publish |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Integrated** | Part of Hub platform |
| ✅ **Standardized** | Consistent per runtime |
| ✅ **Observable** | Logs in Olympus Watch |
| ✅ **Registry integration** | Direct publish |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Less customization** | External CI for complex needs |
| ⚠️ **Runtime-tied** | Consistent within runtime |

---

## Examples

### Example 1: Triggering Build

```bash
# Trigger CI for Hub Application
hub ci build \
  --app dispute-handler \
  --version 1.1.0-dev.1 \
  --workbench dispute-ops-dev
```

### Example 2: CI Result

```
Build: dispute-handler v1.1.0-dev.1
Status: SUCCESS
Duration: 2m 34s

Tests:
├── Unit tests: 45 passed, 0 failed
├── Coverage: 87%
└── Lint: passed

Artifact:
└── registry.../snapshot/dispute-handler:1.1.0-dev.1
```

---

## Implementation Notes

### For Developers

- Run CI before requesting promotion
- Review test failures promptly
- Maintain good test coverage
- Use consistent versioning

### For Operators

- Monitor CI queue and duration
- Review failed builds for patterns
- Manage CI resource allocation

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Artifact Registry](./artifact-registry.md) | CI publishes to registry |
| [Hub Test Runner](./hub-test-runner.md) | Integration testing |
| [Automation Runtime](./automation-runtime.md) | Runtime-specific CI |

---

## References

- [CI Subsystem](../../04-subsystems/ci-subsystem/README.md)
- [Runtime CI](../../04-subsystems/ci-subsystem/runtime-ci.md)

