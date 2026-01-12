# Agent Testing

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

Agent Testing extends Hub Test Runner to provide **testing capabilities for agents**, including jobs to deploy temporary Employed Agents in sandbox workbench instances and validations for behavior (consistency, quality), health, and safety.

**Key Principle**: Agent Test Runner **extends Hub Test Runner** rather than being a separate system, reusing Hub Test Runner infrastructure and test execution framework.

---

## Architecture

Agent Test Runner extends Hub Test Runner:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENT TEST RUNNER ARCHITECTURE                           │
│                                                                              │
│   Agent Test Runner (extends Hub Test Runner)                              │
│        │                                                                     │
│        ├── Test Deployment Jobs (temporary Employed Agents)                  │
│        ├── Behavior Validations (consistency, quality)                     │
│        ├── Health Validations (pod health, connectivity)                    │
│        └── Safety Validations (guardrail enforcement)                        │
│                                                                              │
│   Sandbox Workbench Instance → Temporary Employed Agent → Test Execution   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Extends Hub Test Runner** — Reuses Hub Test Runner infrastructure and test execution framework
- **Temporary Deployment Model** — Creates temporary Employment Specs in sandbox workbench instances
- **MVP Scope: Go/No-Go Validations** — Focuses on pass/fail checks rather than quality scoring
- **Sandbox Isolation** — All tests run in sandbox workbench instances with isolated data
- **Automatic Teardown** — Automatic teardown after test execution completes

---

## Test Deployment Jobs

Test Deployment Jobs create temporary Employed Agents:

| Capability | Description |
|------------|-------------|
| **Temporary Employment Specs** | Combine Training Specs with minimal employment configuration |
| **Sandbox Deployment** | Deploy temporary Employed Agents in sandbox workbench instances |
| **Realistic Context** | Tests run in realistic deployment context |
| **Automatic Teardown** | Automatic teardown after test execution completes |

---

## Validation Types

### Behavior Validations

| Validation | Description | Go/No-Go Check |
|------------|-------------|----------------|
| **Behavior Consistency** | Agent responds consistently to same inputs | Pass/Fail |
| **Behavior Quality** | Basic output quality checks (completeness, format) | Pass/Fail |

### Health Validations

| Validation | Description | Go/No-Go Check |
|------------|-------------|----------------|
| **Pod Health** | Agent pod health and stability | Pass/Fail |
| **Model Connectivity** | Model Gateway connectivity and response | Pass/Fail |
| **Memory Stability** | Memory services connectivity and stability | Pass/Fail |

### Safety Validations

| Validation | Description | Go/No-Go Check |
|------------|-------------|----------------|
| **Guardrail Enforcement** | Guardrails are enforced correctly | Pass/Fail |
| **Prohibited Action Blocking** | Prohibited actions are blocked | Pass/Fail |

---

## MVP Scope

MVP focuses on **go/no-go validations** (pass/fail) rather than quality scoring:

| Scope | Description |
|-------|-------------|
| **Behavior** | Consistency and basic quality checks |
| **Health** | Pod health, model connectivity, memory stability |
| **Safety** | Guardrail enforcement, prohibited action blocking |
| **Deferred** | Advanced evaluations (quality scoring, benchmarks, regression) deferred to post-MVP per ADR-0077 |

---

## Sandbox Isolation

All tests run in **sandbox workbench instances** with isolation:

| Aspect | Description |
|--------|-------------|
| **Isolated Data** | Tests use synthetic or anonymized data |
| **Network Isolation** | Network isolation prevents external calls |
| **Test Data Reset** | Test data reset between test runs |
| **No Production Impact** | No impact on production agents or data |

---

## Parked Capabilities

Advanced evaluation capabilities are **deferred to post-MVP**:

| Capability | Status |
|------------|--------|
| **Quality Scoring** | Deferred to post-MVP |
| **Benchmarks** | Deferred to post-MVP |
| **Regression Testing** | Deferred to post-MVP |
| **Adversarial Testing** | Deferred to post-MVP |
| **CI/CD Quality Gates** | Deferred to post-MVP |

See [parked-capabilities.md](../subsystems/agent-test-runner/parked-capabilities.md) for details.

---

## Related

### Agent Test Runner Subsystem
- [Agent Test Runner README](../subsystems/agent-test-runner/README.md) — Subsystem overview
- [Test Deployment Jobs](../subsystems/agent-test-runner/test-deployment-jobs.md) — Temporary Employed Agent deployment
- [Behavior Validations](../subsystems/agent-test-runner/behavior-validations.md) — Consistency and quality validations
- [Health Validations](../subsystems/agent-test-runner/health-validations.md) — Pod health, connectivity checks
- [Safety Validations](../subsystems/agent-test-runner/safety-validations.md) — Guardrail enforcement validation
- [Parked Capabilities](../subsystems/agent-test-runner/parked-capabilities.md) — Deferred evaluation capabilities

### Related Systems
- [Hub Test Runner](../../../olympus-hub-docs/04-subsystems/ci-subsystem/test-runner.md) — Foundation test execution framework
- [Trained Agent Lifecycle Manager](../subsystems/trained-agent-lifecycle-manager/README.md) — Training Specs for test deployment
- [Agent Lifecycle Manager](../subsystems/agent-lifecycle-manager/README.md) — Temporary Employment Spec management
- [Agent Runtime](../subsystems/agent-runtime/README.md) — Agent pod deployment
- [Seer Sidecar](../subsystems/seer-sidecar/README.md) — Guardrail enforcement validation
- [ADR-0077: Agent Evaluation Deferred](../../../olympus-hub-docs/decision-logs/0077-seer-evaluation-deferred.md) — Evaluation deferral rationale

---

*For detailed implementation, see [Agent Test Runner README](../subsystems/agent-test-runner/README.md).*
