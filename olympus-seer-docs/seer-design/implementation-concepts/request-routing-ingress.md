# Request Routing & Ingress

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

Request Routing & Ingress provides **request routing to deployed Employed Agents** via Agent Ingress Gateway, which is a **Heracles configuration layer** (not a separate service). It routes requests from Signal Exchange to agent pods through sx-observer.

**Key Characteristics:**
- Configuration on Heracles (not a separate service)
- Signal Exchange is unaware of Agent Ingress Gateway
- All routing goes through sx-observer
- Agents update requests directly via Hub APIs

---

## Architecture

Agent Ingress Gateway is a Heracles configuration layer:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENT INGRESS GATEWAY ARCHITECTURE                       │
│                                                                              │
│   Signal Exchange                                                           │
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
│   └─────────────────────────────────────────────────────────────────────┘   │
│        │                                                                     │
│        │ K8s Service                                                         │
│        ▼                                                                     │
│   Agent Pods                                                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Heracles Configuration Layer** — Agent Ingress Gateway is configuration on Heracles, not a separate service
- **Signal Exchange Isolation** — Signal Exchange is completely unaware of Agent Ingress Gateway
- **Agent Direct Response** — Agents update requests directly via Hub APIs
- **Subscription-Based Routing** — Routing based on agent subscriptions to scenarios
- **Store-and-Forward** — sx-observer provides store-and-forward capability

---

## Subscription Lifecycle

Agent subscriptions manage request routing:

| State | Description |
|-------|-------------|
| **Active** | Agent receives request updates |
| **Paused** | Agent subscription paused (no updates) |
| **Terminated** | Agent subscription terminated |

---

## Request Routing

Request routing flow:

| Step | Description |
|------|-------------|
| **Signal Exchange** | Publishes request updates to workbench-level Atropos topic |
| **sx-observer** | Receives all request updates for workbench |
| **Filtering** | Filters by scenario and agent subscriptions |
| **Agent Topics** | Routes to agent-specific Atropos topics |
| **Heracles Ingress** | Routes to agent pods via cluster-ingress |
| **Agent Pods** | Agents receive requests via dispatch endpoint |

---

## Subscription Policies

Subscription-scoped policies enforce access control:

| Policy Type | Description |
|-------------|-------------|
| **Access Control** | Which agents can subscribe to which scenarios |
| **Rate Limiting** | Request rate limits per subscription |
| **Authorization** | Authorization checks before routing |

---

## sx-observer

sx-observer is the bridge between Signal Exchange and agents:

| Capability | Description |
|------------|-------------|
| **Event Reception** | Receives all request updates for workbench |
| **Filtering** | Filters by scenario and agent subscriptions |
| **Store-and-Forward** | Provides store-and-forward capability |
| **Scale-Up Trigger** | Triggers scale-up when agents at zero |

---

## Agent Direct Response

Agents update requests **directly via Hub APIs**:

| Aspect | Description |
|--------|-------------|
| **Direct Updates** | Agents update requests directly (not through ingress) |
| **Hub APIs** | Uses Hub Request Management APIs |
| **Simplified Path** | Simplifies response path and reduces latency |
| **No Ingress Return** | Responses do not flow back through Agent Ingress Gateway |

---

## Related

### Agent Ingress Gateway Subsystem
- [Agent Ingress Gateway README](../subsystems/agent-ingress-gateway/README.md) — Subsystem overview
- [Architecture](../subsystems/agent-ingress-gateway/architecture.md) — Heracles relationship, sx-observer integration
- [Subscription Lifecycle](../subsystems/agent-ingress-gateway/subscription-lifecycle.md) — Subscription management, state machine
- [Request Routing](../subsystems/agent-ingress-gateway/request-routing.md) — Routing logic, filtering algorithms
- [Subscription Policies](../subsystems/agent-ingress-gateway/subscription-policies.md) — Subscription-scoped policies, policy evaluation
- [Heracles Integration](../subsystems/agent-ingress-gateway/heracles-integration.md) — Cluster-ingress configuration, authentication
- [Signal Exchange Integration](../subsystems/agent-ingress-gateway/signal-exchange-integration.md) — sx-observer integration, Atropos topics

### Related Systems
- [Agent Runtime](../subsystems/agent-runtime/README.md) — Ingress path provisioning, agent pod deployment
- [Seer Sidecar](../subsystems/seer-sidecar/README.md) — Additional policy enforcement at pod level
- [Cipher IAM Extensions](../subsystems/cipher-iam-extensions/README.md) — sx-observer authentication
- [Heracles Gateway](../../../olympus-hub-docs/05-infrastructure/heracles-gateway.md) — Heracles documentation
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — Signal Exchange documentation

---

*For detailed implementation, see [Agent Ingress Gateway README](../subsystems/agent-ingress-gateway/README.md).*
