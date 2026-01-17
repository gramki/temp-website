# Agent Ingress Gateway

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

## Overview

Agent Ingress Gateway is a **Heracles configuration layer** that provides request routing to deployed Employed Agents. It is **not a separate service** but rather a set of ingress configurations and Atropos topic subscriptions that route requests from sx-observer to agent pods.

**Key Characteristics:**
- Configuration on Heracles (not a separate service)
- Signal Exchange is unaware of Agent Ingress Gateway
- All routing goes through sx-observer
- Agents update requests directly via Hub APIs

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENT INGRESS GATEWAY ARCHITECTURE                        │
│                                                                              │
│   Signal Exchange                                                            │
│        │                                                                     │
│        │ Atropos (workbench-level topic)                                     │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                      SX-OBSERVER                                     │   │
│   │  • Receives all request updates for workbench                       │   │
│   │  • Filters by scenario and agent subscriptions                      │   │
│   │  • Store-and-forward capability                                     │   │
│   │  • Triggers scale-up when agents at zero                            │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│        │                                                                     │
│        │ Atropos (agent-specific topics)                                     │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │            AGENT INGRESS GATEWAY (Heracles Config)                   │   │
│   │                                                                       │   │
│   │  • Cluster-ingress configuration (not public)                        │   │
│   │  • Path: /seer/.../agents/{agent_id}/dispatch                        │   │
│   │  • Subscription-scoped policies                                      │   │
│   │  • Load balancing via K8s Service                                    │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│        │                                                                     │
│        │ K8s Service                                                         │
│        ▼                                                                     │
│   ┌───────────┐   ┌───────────┐   ┌───────────┐                             │
│   │  Agent 1  │   │  Agent 2  │   │  Agent N  │                             │
│   │   Pod     │   │   Pod     │   │   Pod     │                             │
│   └───────────┘   └───────────┘   └───────────┘                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Architecture](./architecture.md) | Heracles relationship, sx-observer integration, request flow | ✅ Complete |
| [Subscription Lifecycle](./subscription-lifecycle.md) | Subscription management, state machine (C3) | ✅ Complete |
| [Request Routing](./request-routing.md) | Routing logic, filtering algorithms (C3) | ✅ Complete |
| [Subscription Policies](./subscription-policies.md) | Subscription-scoped policies, policy evaluation (C3) | ✅ Complete |
| [Heracles Integration](./heracles-integration.md) | Cluster-ingress configuration, authentication | ✅ Complete |
| [Response Handling](./response-handling.md) | Agent direct updates, Workbench Data Store | ✅ Complete |
| [Signal Exchange Integration](./signal-exchange-integration.md) | sx-observer integration, Atropos topics | ✅ Complete |
| [SCOPE.md](./SCOPE.md) | Coverage summary, design status | ✅ Complete |

---

## Key Design Decisions

### Heracles Configuration Layer
- Agent Ingress Gateway is **configuration on Heracles**, not a separate service
- Reduces operational complexity and leverages existing infrastructure
- Ingress paths provisioned per Employed Agent

### Signal Exchange Isolation
- Signal Exchange is **completely unaware** of Agent Ingress Gateway
- All communication flows through sx-observer
- sx-observer is the only observer registered with Signal Exchange

### Agent Direct Response
- Agents update requests **directly via Hub APIs**
- Responses do not flow back through Agent Ingress Gateway
- Simplifies response path and reduces latency

### Delegation Token Propagation
- `AUTHORITY_GRANTED` updates from Signal Exchange flow through sx-observer to agents
- Delegation tokens in `environment.auth.delegations` are propagated with request updates
- Agents receive new/refreshed tokens via standard dispatch path

---

## Related Subsystems

| Subsystem | Relationship |
|-----------|-------------|
| [Agent Runtime](../agent-runtime/README.md) | Ingress path provisioning, agent pod deployment |
| [Seer Sidecar](../seer-sidecar/README.md) | Additional policy enforcement at pod level |
| [Cipher IAM Extensions](../cipher-iam-extensions/README.md) | sx-observer authentication |

---

## Related Documentation

- [Agent Runtime: Agent Ingress Gateway Integration](../agent-runtime/agent-ingress-gateway-integration.md) — Runtime perspective
- [Agent Runtime: Signal Exchange Integration](../agent-runtime/signal-exchange-integration.md) — sx-observer details
- [Heracles Gateway](../../../../olympus-hub-docs/05-infrastructure/heracles-gateway.md) — Heracles documentation
- [Request-Scoped Authority Delegation](../../implementation-concepts/request-scoped-delegation.md) — End-to-end delegation design
- [Signal Exchange: Delegation Handling](../../../../olympus-hub-docs/04-subsystems/signal-exchange/delegation-handling.md) — Token refresh and routing

---

*Agent Ingress Gateway provides configuration-based request routing to agents via Heracles and sx-observer integration.*
