# Runtime CI

## Overview

Each Hub Application Runtime provides its own CI (Continuous Integration) infrastructure for building and unit testing artifacts. Runtime CI is responsible for compiling source code, running runtime-specific tests, and publishing artifacts to the container registry.

---

## Runtime CI by Application Runtime

| Runtime | Language/Tech | Build System | Unit Test Framework |
|---------|---------------|--------------|---------------------|
| **Atlantis** | Java/Kotlin | Maven/Gradle | JUnit, Mockito |
| **Rhea** | BPMN/Workflow | Rhea Builder | Rhea Test Framework |
| **Seer** | Python/AI | pip/poetry | pytest |
| **Perseus** | Batch/ETL | Perseus Builder | Perseus Test Suite |
| **ChronoShift** | Durable Workflow | ChronoShift Builder | ChronoShift Tests |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         RUNTIME CI ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    SOURCE (Git Repository)                           │   │
│   │                                                                      │   │
│   │   ┌──────────────────┐    ┌──────────────────┐                      │   │
│   │   │ Hub Application  │    │ External Source  │                      │   │
│   │   │ Spec (CRD)       │    │ (DEV only)       │                      │   │
│   │   └──────────────────┘    └──────────────────┘                      │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              │ Trigger                                       │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    RUNTIME CI ENGINE                                 │   │
│   │                                                                      │   │
│   │   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐           │   │
│   │   │   Resolve    │──▶│    Build     │──▶│  Unit Test   │           │   │
│   │   │   Source     │   │   Artifact   │   │   Execute    │           │   │
│   │   └──────────────┘   └──────────────┘   └──────────────┘           │   │
│   │                              │                   │                   │   │
│   │                              │                   │                   │   │
│   │                              ▼                   ▼                   │   │
│   │                      ┌──────────────┐   ┌──────────────┐           │   │
│   │                      │   Package    │   │   Report     │           │   │
│   │                      │   Container  │   │   Results    │           │   │
│   │                      └──────────────┘   └──────────────┘           │   │
│   │                              │                                       │   │
│   └──────────────────────────────┼───────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    SNAPSHOT REGISTRY                                 │   │
│   │                                                                      │   │
│   │   image:1.2.3-beta.1+abc123                                         │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## CI Pipeline Definition

Runtime CI is configured via CRDs with standardized defaults:

```yaml
apiVersion: hub.olympus.io/v1
kind: RuntimeCIPipeline
metadata:
  name: dispute-handler-ci
  namespace: acme-bank
spec:
  # Target application
  application_ref: dispute-handler
  workbench: dispute-ops-dev
  
  # Runtime type
  runtime: atlantis
  
  # Source configuration
  source:
    type: hub_git  # hub_git | external_git (DEV only)
    path: workbenches/dispute-ops-dev/applications/dispute-handler
    
    # For external_git (DEV workbenches only)
    # external:
    #   repository: https://github.com/acme/dispute-handler.git
    #   branch: main
    #   credentials:
    #     secret_ref: github-creds
  
  # Build configuration (optional overrides)
  build:
    # Runtime-specific build config
    # Defaults provided by runtime
    
  # Unit test configuration
  unit_tests:
    enabled: true
    fail_on_test_failure: true
    
  # Artifact configuration
  artifact:
    version_strategy: semantic_with_sha  # semantic | sha | semantic_with_sha
    
status:
  last_build:
    version: "1.2.3-beta.1+abc123"
    status: success
    started_at: "2026-01-06T10:00:00Z"
    completed_at: "2026-01-06T10:05:32Z"
    tests:
      total: 45
      passed: 45
      failed: 0
```

---

## Runtime-Specific Configuration

### Atlantis (Java/Kotlin)

```yaml
spec:
  runtime: atlantis
  
  build:
    tool: maven  # maven | gradle
    jdk_version: "17"
    
    # Maven-specific
    maven:
      goals: ["clean", "package"]
      profiles: ["production"]
      
    # Gradle-specific
    # gradle:
    #   tasks: ["clean", "build"]
  
  unit_tests:
    tool: junit5
    include_patterns:
      - "**/Test*.java"
      - "**/*Test.java"
    exclude_patterns:
      - "**/IntegrationTest*.java"
```

### Rhea (BPMN/Workflow)

```yaml
spec:
  runtime: rhea
  
  build:
    validate_bpmn: true
    compile_expressions: true
    
  unit_tests:
    tool: rhea_test
    mock_services: true
```

### Seer (Python/AI)

```yaml
spec:
  runtime: seer
  
  build:
    tool: poetry  # pip | poetry
    python_version: "3.11"
    
  unit_tests:
    tool: pytest
    coverage_threshold: 80
```

---

## Build Outputs

### Container Image

```
<registry>/<subscription>/<workbench>/<application>:<version>

Example:
registry.hub.acme.com/sub-001/dispute-ops-dev/dispute-handler:1.2.3-beta.1+abc123
```

### Build Metadata

```yaml
build_metadata:
  application: dispute-handler
  version: "1.2.3-beta.1+abc123"
  runtime: atlantis
  
  source:
    commit_sha: abc123def456
    branch: main
    repository: hub://sub-001/dispute-ops-dev
  
  build:
    started_at: "2026-01-06T10:00:00Z"
    completed_at: "2026-01-06T10:05:32Z"
    duration_seconds: 332
    status: success
  
  tests:
    total: 45
    passed: 45
    failed: 0
    skipped: 0
    duration_seconds: 28
  
  artifacts:
    - type: container
      location: registry.hub.acme.com/sub-001/dispute-ops-dev/dispute-handler:1.2.3-beta.1+abc123
      size_mb: 245
```

---

## Triggers

| Trigger Type | Configuration |
|--------------|---------------|
| **Git Push** | Webhook on source changes |
| **On Demand** | Manual via UI/API |
| **Scheduled** | Cron expression |
| **Dependency Update** | When base image updates |

### Trigger Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: CITrigger
metadata:
  name: build-on-push
spec:
  pipeline_ref: dispute-handler-ci
  
  triggers:
    - type: git_push
      branches:
        - main
      paths:
        - "applications/dispute-handler/**"
    
    - type: scheduled
      schedule: "0 3 * * *"  # Daily at 3 AM
      
    - type: on_demand
      allowed_users:
        - developer@acme.com
      allowed_roles:
        - senior-developer
```

---

## Observability

### CI Views

The CI module provides dedicated views for:

| View | Content |
|------|---------|
| **Build History** | List of builds with status, duration |
| **Build Details** | Logs, artifacts, test results |
| **Pipeline Status** | Current state of all pipelines |
| **Metrics** | Build frequency, success rate, duration trends |

### Olympus Watch Integration

| Log Type | Destination |
|----------|-------------|
| Build Logs | Olympus Watch (streaming) |
| Test Logs | Olympus Watch (streaming) |
| Runtime Logs | Olympus Watch |

---

## Default Pipelines

Each subscription receives system-provided default pipelines per runtime:

```yaml
# System-provided defaults
defaults:
  atlantis:
    build:
      tool: maven
      jdk_version: "17"
    unit_tests:
      enabled: true
      tool: junit5
      
  rhea:
    build:
      validate_bpmn: true
    unit_tests:
      enabled: true
      mock_services: true
      
  seer:
    build:
      tool: poetry
      python_version: "3.11"
    unit_tests:
      enabled: true
      tool: pytest
```

> **Note:** Admin overrides for defaults are a future feature.

---

## External Source References (DEV Only)

DEV workbenches can reference external Git repositories:

```yaml
spec:
  source:
    type: external_git
    external:
      repository: https://github.com/acme/dispute-handler.git
      branch: feature/new-rules
      path: /src
      credentials:
        secret_ref: github-creds
```

| Constraint | Details |
|------------|---------|
| **DEV Only** | External sources not allowed in non-DEV workbenches |
| **Build Required** | Source must be built; promoted artifact is container |
| **Credentials** | Stored securely, managed by developer |

---

## Related Documentation

- [Artifact Registry](../artifact-registry/README.md) — Container storage
- [Hub Test Runner](./test-runner.md) — Integration testing
- [Developer Operators](../operators/developer-operators.md) — Application specs

