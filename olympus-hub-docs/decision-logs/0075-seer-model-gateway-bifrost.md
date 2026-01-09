# ADR-0075: Seer Model Gateway Based on Bifrost

**Status**: Accepted  
**Date**: 2026-01-08  
**Category**: seer

---

## Context

AI agents need access to Large Language Models (LLMs). We needed to decide how agents access LLMs:
1. Direct access (each agent manages own LLM connections)
2. Shared gateway (centralized access point)
3. Per-workbench gateways

Key concerns: governance, budgets, fallback, observability, security.

---

## Decision

Seer provides a **platform-level Model Gateway** based on **Bifrost OSS**:

### Deployment Model
- **Single platform deployment** (not per-agent or per-workbench)
- Shared across all Seer agents in the platform
- Integrated with Atlantis and Hub Deployment semantics

### Access Control
- **Hub IAM**: Agent identity verified via JWT
- **OPA Policies**: Fine-grained model access control
- **Virtual Keys**: One per Employed Agent (tracks usage)

### Model Selection
- Raw Agent specifies whitelist of supported models
- Training Spec subsets the whitelist
- Employment Spec can further subset
- Agent requests model by name → Gateway routes

### Budget Enforcement

| Level | Enforcement |
|-------|-------------|
| **Workbench** | Total token budget for all agents |
| **(Workbench, Agent)** | Per-agent budget within workbench |

### Fallback Strategy
- Tenant admin configures provider fallback order
- Gateway automatically routes on provider failure
- Exponential backoff with circuit breaker

### Observability
- Token usage metrics via Prometheus → Watch
- Request/response logging (operational, not CAF)
- Latency, error rate, model distribution

---

## Consequences

### Positive
- Centralized governance, budgets, and audit
- Virtual keys isolate agent usage
- Fallback provides resilience
- Bifrost is mature OSS project
- OpenAI-compatible API for agent simplicity

### Negative
- Single point of failure (mitigated by HA deployment)
- Cross-tenant security requires careful isolation
- Gateway latency adds to LLM latency

### Neutral
- LLM calls are operational logs (not audited to CAF)
- Model catalog managed at platform level
- Agents access via environment variable (endpoint URL)

---

## Related

- [Model Gateway Subsystem](../../olympus-seer-docs/seer-design/subsystems/model-gateway.md)
- [Bifrost OSS](https://github.com/bifrost-ai/bifrost)
- [Training Spec CRD](../../olympus-seer-docs/seer-design/hub-integration/training-spec-crd.md)

