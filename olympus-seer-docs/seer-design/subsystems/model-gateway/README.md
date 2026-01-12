# Model Gateway

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

## Overview

The Seer Model Gateway provides **unified LLM/SLM access** for all agents in the Hub ecosystem. It is based on [Bifrost](https://github.com/maximhq/bifrost), an open-source LLM gateway, adapted for Hub's authentication, governance, and observability requirements.

**Key Capabilities:**
- Unified interface for 8+ providers, 1000+ models
- Provider fallback for high availability
- Budget enforcement at workbench and agent levels
- Virtual key management per Employed Agent
- OpenTelemetry-based observability

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        MODEL GATEWAY ARCHITECTURE                            │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                         AGENT PODS                                   │   │
│   │                                                                       │   │
│   │   ┌───────────┐   ┌───────────┐   ┌───────────┐                     │   │
│   │   │  Agent 1  │   │  Agent 2  │   │  Agent N  │                     │   │
│   │   │           │   │           │   │           │                     │   │
│   │   │ base_url= │   │ base_url= │   │ base_url= │                     │   │
│   │   │ $MODEL_   │   │ $MODEL_   │   │ $MODEL_   │                     │   │
│   │   │ GATEWAY   │   │ GATEWAY   │   │ GATEWAY   │                     │   │
│   │   └─────┬─────┘   └─────┬─────┘   └─────┬─────┘                     │   │
│   │         │               │               │                            │   │
│   └─────────┼───────────────┼───────────────┼────────────────────────────┘   │
│             │               │               │                                │
│             └───────────────┼───────────────┘                                │
│                             │ OpenAI-compatible API                          │
│                             ▼                                                │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    MODEL GATEWAY (Bifrost)                           │   │
│   │                                                                       │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    AUTHENTICATION                            │   │   │
│   │   │                    (Cipher IAM Integration)                  │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                             │                                        │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    OPA POLICIES                              │   │   │
│   │   │                    • Model access control                    │   │   │
│   │   │                    • Rate limiting                           │   │   │
│   │   │                    • Budget enforcement                      │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                             │                                        │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    ROUTING & FALLBACK                        │   │   │
│   │   │                    (Tenant-configured)                       │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                             │                                        │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    OBSERVABILITY                             │   │   │
│   │   │                    (Prometheus → Watch)                      │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                             │                                        │   │
│   └─────────────────────────────┼───────────────────────────────────────┘   │
│                                 │                                            │
│              ┌──────────────────┼──────────────────┐                        │
│              │                  │                  │                        │
│              ▼                  ▼                  ▼                        │
│   ┌───────────────┐   ┌───────────────┐   ┌───────────────┐                │
│   │    OpenAI     │   │   Anthropic   │   │  AWS Bedrock  │   ...          │
│   └───────────────┘   └───────────────┘   └───────────────┘                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Architecture](./architecture.md) | Deployment model, Bifrost integration, component architecture | ✅ Complete |
| [Model Catalog](./model-catalog.md) | Provider configuration, model selection hierarchy, whitelist enforcement | ✅ Complete |
| [Routing & Fallback](./routing-fallback.md) | Fallback strategies, circuit breakers, timeout handling | ✅ Complete |
| [Governance](./governance.md) | Budget enforcement, virtual key management, quota mechanisms | ✅ Complete |
| [Policy Enforcement](./policy-enforcement.md) | OPA integration, policy evaluation flow, PEP integration | ✅ Complete |
| [Observability](./observability.md) | Metrics, logging, Watch integration, cost tracking | ✅ Complete |
| [Agent Access](./agent-access.md) | OpenAI-compatible API, endpoint discovery, authentication | ✅ Complete |
| [SCOPE.md](./SCOPE.md) | Coverage summary, design status, intended depth | ✅ Complete |

---

## Key Design Decisions

### Platform-Level Deployment
- Single Model Gateway instance per Hub installation
- Shared across all tenants
- Isolation via virtual keys, budgets, and policies

### Bifrost-Based Implementation
- Based on Bifrost OSS for proven LLM gateway capabilities
- Hub-specific customizations for IAM, OPA, and observability
- OpenAI-compatible API for agent simplicity

### Two-Level Budget Enforcement
- Workbench-level budgets for aggregate control
- Agent-level budgets for granular enforcement
- Virtual keys for per-agent tracking and attribution

### LLM Calls as Operational Logs
- LLM calls are **not** logged to CAF
- Treated as operational logs (not enterprise auditable events)
- Request/response content not stored for audit

---

## Related Subsystems

| Subsystem | Relationship |
|-----------|-------------|
| [Cipher IAM Extensions](../cipher-iam-extensions/README.md) | Virtual key issuance, agent authentication |
| [Agent Runtime](../agent-runtime/README.md) | Endpoint discovery, credential injection |
| [Seer Sidecar](../seer-sidecar/README.md) | Policy enforcement integration |
| [Agent Analytics](../agent-analytics/README.md) | Cognitive metrics aggregation |

---

## Related Documentation

- [Bifrost GitHub](https://github.com/maximhq/bifrost) — Upstream project
- [Bifrost Documentation](https://docs.getbifrost.ai/) — Feature documentation
- [ADR-0075: Model Gateway (Bifrost)](../../../../olympus-hub-docs/decision-logs/0075-seer-model-gateway-bifrost.md) — Architecture decision
- [Olympus Watch](https://watch.olympus.tech/) — Observability platform

---

*Model Gateway provides unified, governed, and observable LLM access for all Seer agents, based on Bifrost OSS.*
