# Agent Test Runner: Parked Capabilities

> **Status**: 🔴 PARKED — Deferred to post-MVP  
> **Last Updated**: 2026-01-13  
> **See**: [ADR-0077](../../../../olympus-hub-docs/decision-logs/0077-seer-evaluation-deferred.md)  
> **Related**: [SCOPE.md](./SCOPE.md) — MVP scope vs. parked scope

## Overview

This document lists capabilities required for agent evaluation and testing that are **deferred to post-MVP**. The MVP scope focuses on go/no-go validations (behavior consistency/quality, health, safety), while advanced evaluation capabilities (quality scoring, benchmarks, regression testing) are parked.

See [SCOPE.md](./SCOPE.md) for the complete scope breakdown and MVP vs. parked capabilities.

---

## Parked Capabilities

| Capability | Description |
|------------|-------------|
| **Evaluation Frameworks** | Systematic testing of agent behavior against expected outcomes |
| **Benchmark Suites** | Standard tests for agent capabilities (reasoning, tool use, safety) |
| **Regression Testing** | Detect behavior changes across versions |
| **Quality Metrics** | Accuracy, relevance, safety, coherence scores |
| **Test Case Management** | Curate and version test scenarios |
| **CI/CD Integration** | Quality gates for agent deployments |

---

## Evaluation Types (Parked)

| Type | Purpose |
|------|---------|
| **Functional** | Does the agent perform the expected task correctly? |
| **Safety** | Does the agent stay within guardrails? |
| **Performance** | Latency, token efficiency, cost |
| **Regression** | Has behavior changed from baseline? |
| **Adversarial** | How does the agent handle edge cases and attacks? |

---

## Parking Rationale

Agent Evaluation capabilities are **deferred to post-MVP** for the following reasons:

1. **Evaluation patterns are immature**: The industry has not converged on best practices for agent evaluation
2. **MVP focus**: Initial deployment prioritizes core agent lifecycle, not advanced testing
3. **Dependency on production experience**: Effective evaluation requires understanding of real-world failure modes
4. **Framework diversity**: Different agentic frameworks have different testing idioms

### Interim Approach

- Developers use their framework's native testing tools
- Manual validation in development workbenches
- Observability-based monitoring in production

---

## MVP vs. Parked Scope

### ✅ MVP Scope (Implemented)

The MVP includes go/no-go validations:
- **Behavior Validations**: Consistency checks, basic quality checks (completeness, format)
- **Health Validations**: Pod health, model connectivity, memory stability
- **Safety Validations**: Guardrail enforcement, prohibited action blocking

See [SCOPE.md](./SCOPE.md) for detailed MVP scope.

### 🔴 Parked Scope (Deferred)

The following advanced evaluation capabilities are deferred to post-MVP:
- Quality scoring and benchmarks
- Regression testing across versions
- Adversarial testing
- CI/CD quality gates

---

## Related

- [SCOPE.md](./SCOPE.md) — Design scope, MVP vs. parked scope
- [README.md](./README.md) — Agent Test Runner overview
- [ADR-0077](../../../../olympus-hub-docs/decision-logs/0077-seer-evaluation-deferred.md) — ADR on evaluation deferral

---

*Work will resume after MVP when evaluation patterns mature.*
