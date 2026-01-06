# CI Subsystem

> **Status:** 🟡 WIP — Core concepts defined

## Overview

The CI (Continuous Integration) Subsystem provides build and test infrastructure for Hub artifacts. It consists of two main components:

1. **Runtime-Specific CI**: Build and unit test capabilities provided by each Application Runtime
2. **Hub Test Runner**: Integration test execution for Scenarios and Tools

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CI SUBSYSTEM ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   RUNTIME-SPECIFIC CI                                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │   │
│   │   │ Atlantis │  │   Rhea   │  │   Seer   │  │  Perseus │           │   │
│   │   │    CI    │  │    CI    │  │    CI    │  │    CI    │           │   │
│   │   ├──────────┤  ├──────────┤  ├──────────┤  ├──────────┤           │   │
│   │   │• Build   │  │• Build   │  │• Build   │  │• Build   │           │   │
│   │   │• Unit    │  │• Unit    │  │• Unit    │  │• Unit    │           │   │
│   │   │  Test    │  │  Test    │  │  Test    │  │  Test    │           │   │
│   │   └──────────┘  └──────────┘  └──────────┘  └──────────┘           │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              │ Artifacts                                     │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    ARTIFACT REGISTRY                                 │   │
│   │             (Snapshot / Production Registries)                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              │ Deployed Artifacts                            │
│                              ▼                                               │
│   HUB TEST RUNNER                                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   ┌───────────────────┐    ┌───────────────────┐                    │   │
│   │   │   Test Suites     │    │   Test Execution  │                    │   │
│   │   │   (CRDs)          │───▶│   Engine          │                    │   │
│   │   └───────────────────┘    └───────────────────┘                    │   │
│   │                                    │                                 │   │
│   │                                    ▼                                 │   │
│   │                           ┌───────────────────┐                     │   │
│   │                           │   I/O Gateway     │                     │   │
│   │                           │   (Invoke)        │                     │   │
│   │                           └───────────────────┘                     │   │
│   │                                    │                                 │   │
│   │                                    ▼                                 │   │
│   │                           ┌───────────────────┐                     │   │
│   │                           │   Assertions &    │                     │   │
│   │                           │   Reports         │                     │   │
│   │                           └───────────────────┘                     │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Components

| Component | Description | Documentation |
|-----------|-------------|---------------|
| Runtime CI | Per-runtime build and unit test | [runtime-ci.md](./runtime-ci.md) |
| Hub Test Runner | Integration test execution | [test-runner.md](./test-runner.md) |
| Test CRDs | Test and TestSuite definitions | [test-crds.md](./test-crds.md) |

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Runtime CI** | Build and unit test infrastructure specific to each Application Runtime |
| **Hub Test Runner** | Platform-provided integration test execution engine |
| **Test** | CRD defining a single test case (input, expected output, assertions) |
| **Test Suite** | CRD grouping Tests with execution ordering |
| **Hub Environment** | Isolated environment for test execution with resettable resources |

---

## CI Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CI PIPELINE FLOW                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEVELOPMENT                 BUILD                    TEST                  │
│                                                                              │
│   ┌──────────┐           ┌──────────┐            ┌──────────┐               │
│   │          │  Trigger  │          │  Artifact  │          │               │
│   │  Source  │──────────▶│ Runtime  │───────────▶│ Snapshot │               │
│   │  Code    │           │   CI     │            │ Registry │               │
│   │          │           │          │            │          │               │
│   └──────────┘           └──────────┘            └──────────┘               │
│                               │                        │                     │
│                               │ Unit Test              │ Deploy              │
│                               │ Results                │ to DEV              │
│                               ▼                        ▼                     │
│                          ┌──────────┐            ┌──────────┐               │
│                          │          │            │          │               │
│                          │   CI     │            │   DEV    │               │
│                          │  Views   │            │ Workbench│               │
│                          │          │            │          │               │
│                          └──────────┘            └──────────┘               │
│                                                        │                     │
│   INTEGRATION TEST                                     │ Run Tests           │
│                                                        ▼                     │
│                                                  ┌──────────┐               │
│                                                  │          │               │
│                                                  │Hub Test  │               │
│                                                  │ Runner   │               │
│                                                  │          │               │
│                                                  └──────────┘               │
│                                                        │                     │
│                                                        │ Results             │
│                                                        ▼                     │
│                                                  ┌──────────┐               │
│                                                  │          │               │
│                                                  │  Test    │               │
│                                                  │ Reports  │               │
│                                                  │          │               │
│                                                  └──────────┘               │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Responsibilities

### Runtime CI

| Responsibility | Details |
|----------------|---------|
| **Build** | Compile, package Hub Application artifacts |
| **Unit Test** | Execute runtime-specific unit tests |
| **Artifact Push** | Push built artifacts to Snapshot registry |
| **Logs** | Stream build logs to Olympus Watch |

### Hub Test Runner

| Responsibility | Details |
|----------------|---------|
| **Integration Test** | Execute tests via I/O Gateway |
| **Standalone Tool Test** | Test tools in workbench |
| **Test Data Setup** | Pre-flight environment preparation |
| **Reporting** | Store and display test results |

---

## Enablement

CI features are enabled per subscription and workbench by Tenant Admin:

```yaml
apiVersion: hub.olympus.io/v1
kind: CIConfiguration
metadata:
  name: ci-config
  namespace: acme-bank
spec:
  # Subscription-level enablement
  subscription:
    runtime_ci:
      enabled: true
      runtimes:
        - atlantis
        - rhea
        - seer
    
    test_runner:
      enabled: true
  
  # Workbench-specific overrides
  workbenches:
    - name: dispute-ops-dev
      test_runner:
        enabled: true
        dedicated_environment: test-env-01
    
    - name: dispute-ops-prod
      test_runner:
        enabled: false  # No testing in prod
```

---

## CI Triggers

| Trigger | Configurable | Description |
|---------|--------------|-------------|
| **On Git Push** | Yes | Trigger build on source changes |
| **On Demand** | Yes | Manual trigger via UI/API |
| **Scheduled** | Yes | Cron-based execution |
| **On Promotion Request** | Yes | Validate before promotion |

### Trigger Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: CITrigger
metadata:
  name: build-on-push
  namespace: acme-bank
spec:
  workbench: dispute-ops-dev
  
  trigger:
    type: git_push  # git_push | on_demand | scheduled | promotion
    
    # For scheduled
    # schedule: "0 2 * * *"  # 2 AM daily
  
  actions:
    - type: runtime_ci
      runtime: atlantis
      target:
        application: dispute-handler
    
    - type: test_runner
      wait_for: runtime_ci  # Run after build
      test_suite: dispute-integration-tests
```

---

## Output and Observability

### Build Output

| Output | Location |
|--------|----------|
| Build Logs | CI Module Views + Olympus Watch |
| Unit Test Results | CI Module Views |
| Artifacts | Snapshot Registry |
| Build Metadata | CI Module (status, duration, version) |

### Test Output

| Output | Location |
|--------|----------|
| Test Results | Test Runner Views |
| Test Logs | Olympus Watch |
| Assertions | Test Runner Reports |

---

## Integration Points

| System | Integration |
|--------|-------------|
| **Artifact Registry** | Push built containers |
| **Git Repository** | Source for builds, trigger on push |
| **Olympus Watch** | Logs and observability |
| **Notification Services** | Build/test status notifications |
| **Promotion** | Gate promotion on test results (optional) |

---

## Practice Notes

### Machine and Tool Stubbing

> **Developer Responsibility:** Stubbing of Machines and Tools for testing is left to developers.

| What Can Be Promoted | What Cannot Be Promoted |
|----------------------|-------------------------|
| Machine/Tool Definitions (contracts) | Machine/Tool Instances (concrete) |
| Protocol specifications | Environment configurations |
| Normative specifications | Connection credentials |

Developers should:
- Create mock implementations for external dependencies
- Use dedicated test environments with stubbed services
- Configure test-specific Machine/Tool instances in test workbenches

---

## Related Documentation

- [Artifact Registry](../artifact-registry/README.md) — Build artifact storage
- [Developer Operators](../operators/developer-operators.md) — Application specifications
- [Signal Exchange](../signal-exchange/README.md) — I/O Gateway for test invocation

---

## Open Points

See [open-points.md](./open-points.md) for unresolved questions.


