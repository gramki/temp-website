# Model Gateway - Scope and Design Status

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Scope

The **Model Gateway** subsystem provides unified LLM/SLM access for all agents in the Hub ecosystem. It is responsible for:

1. **Unified API** — OpenAI-compatible interface for all providers
2. **Model Catalog Management** — Provider configuration and model selection hierarchy
3. **Routing & Fallback** — Intelligent routing with automatic failover
4. **Budget Enforcement** — Two-level budget control (workbench and agent)
5. **Policy Enforcement** — OPA-based access control and rate limiting
6. **Observability** — Metrics, logging, and tracing integration

---

## Intended Depth

This design documentation is at **C2 (Container) level** with **C3 (Component) detail** for critical mechanisms:

| Aspect | Coverage |
|--------|----------|
| **Functional Scope** | Complete — what each component does |
| **Integration Points** | Complete — hand-offs between containers |
| **Conceptual Models** | Complete — illustrated with YAML/code examples |
| **C3 Detail Areas** | Complete — fallback algorithms, budget enforcement, policy evaluation |
| **Data Models** | Conceptual only — no detailed schemas |
| **API Specifications** | Conceptual only — patterns illustrated |

### C3 Detail Areas

The following areas are documented at C3 (Component) level:

| Area | Document | Details |
|------|----------|---------|
| **Fallback Algorithms** | routing-fallback.md | Circuit breaker state machine, trigger evaluation |
| **Budget Enforcement** | governance.md | Token cost calculation, budget check algorithm |
| **Policy Evaluation** | policy-enforcement.md | OPA input structure, combined policy evaluation |

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [README.md](./README.md) | Overview, architecture diagram, design summary | ✅ Complete |
| [architecture.md](./architecture.md) | Deployment model, Bifrost integration, components | ✅ Complete |
| [model-catalog.md](./model-catalog.md) | Provider configuration, model selection hierarchy | ✅ Complete |
| [routing-fallback.md](./routing-fallback.md) | Fallback strategies, circuit breakers (C3) | ✅ Complete |
| [governance.md](./governance.md) | Budget enforcement, virtual keys (C3) | ✅ Complete |
| [policy-enforcement.md](./policy-enforcement.md) | OPA integration, policy evaluation (C3) | ✅ Complete |
| [observability.md](./observability.md) | Metrics, logging, Watch integration | ✅ Complete |
| [agent-access.md](./agent-access.md) | OpenAI-compatible API, authentication | ✅ Complete |

---

## Coverage Summary

### ✅ Architecture (architecture.md)
- Platform-level deployment model
- Bifrost integration and customizations
- Component architecture (auth, OPA, routing, observability)
- Cipher IAM and Watch integration

### ✅ Model Catalog (model-catalog.md)
- Provider configuration by tenant admin
- Model selection hierarchy (Raw → Training → Employment)
- Whitelist enforcement at multiple points
- Subset validation logic

### ✅ Routing & Fallback (routing-fallback.md)
- Fallback configuration (chains, triggers)
- Fallback strategies (priority, round-robin, cost-optimized)
- **C3**: Fallback trigger logic and evaluation
- **C3**: Circuit breaker algorithm and state machine
- **C3**: Timeout handling

### ✅ Governance (governance.md)
- Two-level budget model (workbench, agent)
- Virtual key management and lifecycle
- **C3**: Token cost calculation
- **C3**: Budget tracking algorithm
- **C3**: Pre-request budget check
- Budget periods and reset

### ✅ Policy Enforcement (policy-enforcement.md)
- OPA integration and deployment model
- Policy types (access, budget, rate limit, validation)
- **C3**: Policy evaluation flow
- **C3**: Input document structure
- **C3**: Combined policy evaluation
- PEP integration with Cipher IAM

### ✅ Observability (observability.md)
- Prometheus metrics (tokens, requests, cost, fallback)
- Watch integration (dashboards, alerts)
- Structured logging (operational, not CAF)
- Cost tracking and attribution
- Distributed tracing

### ✅ Agent Access (agent-access.md)
- OpenAI-compatible API
- Endpoint discovery via environment variables
- Virtual key injection at deployment
- Authentication flow
- Framework integration (LangChain, LangGraph, Strands)

---

## Implementation Details Deferred

The following implementation details are deferred to the detailed implementation stage:

| Area | Deferred Details |
|------|------------------|
| **Model Pricing** | Specific pricing tables, update frequency |
| **Cache Configuration** | TTL values, cache invalidation patterns |
| **Streaming** | Detailed streaming protocol handling |
| **Custom Models** | SageMaker/custom model configuration |

These will be addressed during implementation with common defaults applied.

---

## Related Subsystems

- **[Cipher IAM Extensions](../cipher-iam-extensions/README.md)** — Virtual key management, agent authentication
- **[Agent Runtime](../agent-runtime/README.md)** — Endpoint discovery, credential injection
- **[Seer Sidecar](../seer-sidecar/README.md)** — Additional policy enforcement
- **[Agent Analytics](../agent-analytics/README.md)** — Cognitive metrics aggregation

---

## Related Documentation

- [Bifrost GitHub](https://github.com/maximhq/bifrost) — Upstream project
- [ADR-0075: Model Gateway (Bifrost)](../../../../olympus-hub-docs/decision-logs/0075-seer-model-gateway-bifrost.md) — Architecture decision
- [Olympus Watch](https://watch.olympus.tech/) — Observability platform

---

*This scope document reflects the completed detailed design of the Model Gateway subsystem.*
