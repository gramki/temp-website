# Model Management

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

Model Management provides **unified LLM/SLM access** for all agents in the Hub ecosystem through the Seer Model Gateway. It abstracts provider complexity, enforces governance, and provides observability for all model interactions.

**Key Capabilities:**
- Unified interface for 8+ providers, 1000+ models
- Provider fallback for high availability
- Budget enforcement at workbench and agent levels
- Virtual key management per Employed Agent
- OpenTelemetry-based observability

---

## Architecture

The Model Gateway is a **platform-level service** (single instance per Hub installation) that routes all agent LLM requests:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        MODEL GATEWAY ARCHITECTURE                            │
│                                                                              │
│   Agent Pods → Model Gateway → Provider APIs (OpenAI, Anthropic, etc.)    │
│                                                                              │
│   • Authentication via Virtual Keys                                          │
│   • Policy Enforcement via OPA                                               │
│   • Routing & Fallback (tenant-configured)                                   │
│   • Budget Enforcement (workbench + agent level)                             │
│   • Observability (Prometheus → Watch)                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Platform-Level Deployment** — Single Model Gateway instance shared across all tenants
- **Bifrost-Based** — Built on Bifrost OSS for proven LLM gateway capabilities
- **OpenAI-Compatible API** — Agents use standard OpenAI SDK with gateway endpoint
- **Virtual Key Authentication** — Each Employed Agent has a unique virtual key
- **Two-Level Budget Enforcement** — Workbench-level and agent-level budgets
- **Provider Fallback** — Automatic fallback to backup providers for high availability
- **LLM Calls as Operational Logs** — LLM calls are operational logs, not CAF events

---

## Virtual Key Management

Each Employed Agent receives a **virtual key** for Model Gateway access:

| Aspect | Description |
|--------|-------------|
| **Issuance** | Provisioned by Cipher IAM Extensions at Employment |
| **Purpose** | Authentication, budget tracking, cost attribution |
| **Scope** | Per-agent tracking and attribution |
| **Rotation** | On employment or rotation request |
| **Revocation** | On employment revocation |

---

## Budget Enforcement

Budget enforcement operates at two levels:

1. **Workbench-Level Budgets** — Aggregate control across all agents in a workbench
2. **Agent-Level Budgets** — Granular enforcement per Employed Agent

Budget evaluation:
- **Token-based budgets** — Track token usage across requests
- **Cost-based budgets** — Track monetary cost across providers
- **Time-based windows** — Daily, weekly, monthly budgets
- **Enforcement** — Requests rejected when budget exceeded

---

## Routing & Fallback

Model Gateway provides tenant-configured routing and fallback:

| Capability | Description |
|------------|-------------|
| **Model Selection** | Tenant-configured model selection hierarchy |
| **Provider Fallback** | Automatic fallback to backup providers on failure |
| **Circuit Breakers** | Circuit breakers prevent cascading failures |
| **Timeout Handling** | Configurable timeouts with fallback |
| **Whitelist Enforcement** | Only whitelisted models accessible |

---

## Policy Enforcement

Model Gateway integrates with OPA for policy enforcement:

| Policy Type | Description |
|-------------|-------------|
| **Model Access Control** | Which models agents can access |
| **Rate Limiting** | Request rate limits per agent/workbench |
| **Budget Enforcement** | Budget checks before request processing |
| **Provider Restrictions** | Provider-level access controls |

---

## Observability

Model Gateway provides comprehensive observability:

| Metric Type | Description |
|-------------|-------------|
| **Request Metrics** | Request count, latency, errors by agent |
| **Token Usage** | Token consumption by model, provider, agent |
| **Cost Tracking** | Cost accumulation by agent, workbench |
| **Provider Metrics** | Provider-specific metrics (latency, errors) |
| **Budget Utilization** | Budget consumption and remaining capacity |

All metrics flow to Olympus Watch for dashboard and alerting.

---

## LLM Calls as Operational Logs

**Key Design Decision**: LLM calls are **not** logged to CAF (Cognitive Audit Fabric).

| Aspect | Rationale |
|--------|-----------|
| **Operational Logs** | LLM calls are operational telemetry, not enterprise auditable events |
| **Request/Response Content** | Not stored for audit (privacy, cost, volume) |
| **Observability Only** | Metrics, logs, traces for operational monitoring |
| **CAF Events** | Only agent decisions and outcomes go to CAF |

---

## Related

### Model Gateway Subsystem
- [Model Gateway README](../subsystems/model-gateway/README.md) — Subsystem overview
- [Model Gateway Architecture](../subsystems/model-gateway/architecture.md) — Deployment model, Bifrost integration
- [Model Gateway Governance](../subsystems/model-gateway/governance.md) — Budget enforcement, virtual key management
- [Model Gateway Routing & Fallback](../subsystems/model-gateway/routing-fallback.md) — Fallback strategies, circuit breakers
- [Model Gateway Policy Enforcement](../subsystems/model-gateway/policy-enforcement.md) — OPA integration, policy evaluation

### Related Systems
- [Cipher IAM Extensions](../subsystems/cipher-iam-extensions/README.md) — Virtual key issuance, agent authentication
- [Agent Runtime](../subsystems/agent-runtime/README.md) — Endpoint discovery, credential injection
- [Agent Analytics](../subsystems/agent-analytics/README.md) — Cognitive metrics aggregation
- [ADR-0075: Model Gateway (Bifrost)](../../../olympus-hub-docs/decision-logs/0075-seer-model-gateway-bifrost.md) — Architecture decision

---

*For detailed implementation, see [Model Gateway README](../subsystems/model-gateway/README.md).*
