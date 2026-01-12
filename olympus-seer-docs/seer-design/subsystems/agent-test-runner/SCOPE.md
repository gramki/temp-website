# Agent Test Runner - Scope and Design Status

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13

---

## Scope

The **Agent Test Runner** subsystem extends Hub Test Runner to provide testing capabilities for agents. It is responsible for:

1. **Test Deployment Jobs** — Temporary Employed Agent deployment in sandbox workbench instances
2. **Behavior Validations** — Consistency and quality checks (MVP scope)
3. **Health Validations** — Pod health, model connectivity, memory stability (MVP scope)
4. **Safety Validations** — Guardrail enforcement, prohibited action blocking (MVP scope)

---

## Intended Depth

This design documentation is at **C2 (Container) level** in the C4 architecture model:

| Aspect | Coverage |
|--------|----------|
| **Functional Scope** | Complete — what each component does |
| **Integration Points** | Complete — hand-offs between containers |
| **Conceptual Models** | Complete — illustrated with YAML examples |
| **Operational Flows** | Complete — sequence diagrams for key operations |
| **Data Models** | Conceptual only — no detailed schemas |
| **API Specifications** | Not included — deferred to implementation |

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Test Deployment Jobs](./test-deployment-jobs.md) | Temporary Employed Agent deployment for testing | ✅ Complete |
| [Behavior Validations](./behavior-validations.md) | Consistency and quality validations | ✅ Complete |
| [Health Validations](./health-validations.md) | Pod health, connectivity, stability checks | ✅ Complete |
| [Safety Validations](./safety-validations.md) | Guardrail enforcement validation | ✅ Complete |

---

## MVP Scope vs. Parked Scope

### ✅ MVP Scope (Validations)

| Validation Type | Description | Go/No-Go Check |
|-----------------|-------------|---------------|
| **Behavior Consistency** | Agent responds consistently to same inputs | Pass/Fail |
| **Behavior Quality** | Basic output quality checks (completeness, format) | Pass/Fail |
| **Health** | Pod health, model connectivity, memory stability | Pass/Fail |
| **Safety** | Guardrail enforcement, prohibited actions blocked | Pass/Fail |

### 🔴 Parked Scope (Evaluations) - Deferred per ADR-0077

| Evaluation Type | Description | Status |
|-----------------|-------------|--------|
| **Quality Scoring** | Accuracy, relevance, safety, coherence scores | Parked |
| **Benchmark Suites** | Standard tests for agent capabilities | Parked |
| **Regression Testing** | Detect behavior changes across versions | Parked |
| **Adversarial Testing** | Edge cases and attack scenarios | Parked |
| **CI/CD Quality Gates** | Automated quality gates for deployments | Parked |

See [parked-capabilities.md](./parked-capabilities.md) for detailed information on deferred capabilities.

---

## Coverage Summary

### ✅ Test Deployment Jobs (test-deployment-jobs.md)

- **Temporary Employment Spec Generation**
  - Employment Spec structure for testing
  - Minimal authority configuration
  - Sandbox workbench assignment
  - Test-specific configuration
  
- **Sandbox Deployment**
  - Deployment flow and steps
  - Sandbox workbench configuration
  - Readiness checks
  - Test environment setup
  
- **Teardown Service**
  - Teardown triggers (test completion, timeout, error)
  - Teardown flow and steps
  - Resource cleanup
  - Test data cleanup

### ✅ Behavior Validations (behavior-validations.md)

- **Consistency Checks**
  - Deterministic response validation
  - Response stability checks
  - Decision consistency validation
  - Consistency test examples
  
- **Quality Checks**
  - Completeness validation
  - Format validation
  - Required fields checks
  - Field type validation
  
- **Assertion Types**
  - Response consistency assertions
  - Variance check assertions
  - Completeness assertions
  - Format validation assertions

### ✅ Health Validations (health-validations.md)

- **Pod Health Checks**
  - Pod status validation
  - Readiness/liveness probe checks
  - Container status checks
  - Resource usage validation
  
- **Model Connectivity Checks**
  - Model Gateway connection validation
  - Model availability checks
  - Authentication validation
  - Test inference validation
  
- **Memory Stability Checks**
  - Memory usage validation
  - Memory growth checks
  - Memory leak detection
  - GC behavior validation

### ✅ Safety Validations (safety-validations.md)

- **Guardrail Enforcement Checks**
  - Inbound guardrail validation
  - Outbound guardrail validation
  - Guardrail response validation
  - Guardrail configuration validation
  
- **Prohibited Action Blocking Checks**
  - Action blocking validation
  - Action allowance validation
  - Action escalation validation
  
- **Assertion Types**
  - Guardrail enforcement assertions
  - Action blocking assertions
  - Action allowance assertions
  - Action escalation assertions

---

## Integration Patterns

| Pattern | Use Case | Components |
|---------|----------|------------|
| **Extends Hub Test Runner** | Test execution framework | Test Suite CRD, execution engine |
| **Temporary Deployment** | Test agent deployment | Employment Spec generation, sandbox deployment |
| **Sandbox Isolation** | Test environment isolation | Sandbox workbench, synthetic data |
| **Go/No-Go Checks** | MVP validations | Pass/fail assertions |

---

## Implementation Details Deferred

The following implementation details are deferred to the detailed implementation stage:

| Area | Deferred Details |
|------|------------------|
| **Data Models** | Detailed Test CRD schema, database schemas |
| **API Specifications** | REST/gRPC endpoints, request/response schemas |
| **Storage** | Test result storage, indexing strategies |
| **Test Execution** | Specific execution algorithms, parallelization |
| **Assertion Engine** | Assertion evaluation algorithms, matching logic |
| **Teardown** | Specific cleanup algorithms, resource tracking |
| **Error Handling** | Specific retry policies, circuit breakers |
| **Observability** | Specific metrics, dashboard layouts |

These will be addressed during implementation with common defaults applied.

---

## Related Subsystems

| Subsystem | Relationship |
|-----------|--------------|
| [Hub Test Runner](../../../olympus-hub-docs/04-subsystems/ci-subsystem/test-runner.md) | Extends Hub Test Runner with agent-specific capabilities |
| [Trained Agent Lifecycle Manager](../trained-agent-lifecycle-manager/README.md) | Training Specs for test deployment |
| [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) | Temporary Employment Spec management |
| [Agent Runtime](../agent-runtime/README.md) | Agent pod deployment |
| [Seer Sidecar](../seer-sidecar/README.md) | Guardrail enforcement validation |

---

## Related Hub Documentation

- `olympus-hub-docs/04-subsystems/ci-subsystem/test-runner.md` — Hub Test Runner foundation
- `olympus-hub-docs/decision-logs/0077-seer-evaluation-deferred.md` — ADR on evaluation deferral

---

## Related Implementation Concepts

- [Agent Development Lifecycle](../../guides/agent-development-lifecycle.md) — Agent testing in development lifecycle
- [DevOps Workbench Pattern](../../../olympus-hub-docs/09-composite-systems-and-patterns/devops-workbench.md) — Testing in DevOps workbench

---

*This scope document reflects the completed C2-level design of the Agent Test Runner subsystem, with MVP validations complete and advanced evaluations deferred to post-MVP.*
