# Agent Runtime (Subsystem)

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

## Overview

Agent Runtime provides the runtime environment for deployed Employed Agents. It handles deployment, scaling, lifecycle operations, IAM profile provisioning, and Signal Exchange integration for agents running in the Seer platform.

---

## Capabilities

Based on `olympus-hub-docs/scratchpad/seer-subsystems.md`:

- ✅ Operators to deploy Employed Agent (Ingress Paths, IAM Profile provisioning, etc.)
- ✅ Operators for Scaling Agents
- ✅ Operators for respawning agents after Authority Enforcement Changes at any level
- ✅ Signal Exchange integration via sx-observer service
- ✅ Hub SX integration (Agent Ingress Gateway)

---

## Design Documents

| Document | Description |
|----------|-------------|
| [Runtime Deployment](./runtime-deployment.md) | Core runtime architecture, deployment flow, pod architecture, networking, security, observability, ingress path provisioning |
| [IAM Provisioning](./iam-provisioning.md) | IAM profile creation, lifecycle, roles/groups inheritance, bot mode, credential injection |
| [Authority Change Respawning](./authority-change-respawning.md) | Authority change detection architecture, respawning triggers and process |
| [Signal Exchange Integration](./signal-exchange-integration.md) | sx-observer service, store-and-forward, back-pressure handling, scale-to-zero, Atropos routing |
| [Agent Ingress Gateway Integration](./agent-ingress-gateway-integration.md) | Request dispatch, response handling, external resource references, Workbench Data Store, error handling |
| [SCOPE.md](./SCOPE.md) | Scope document with coverage summary and related documentation |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AGENT RUNTIME ARCHITECTURE                            │
│                                                                              │
│   Signal Exchange                                                            │
│        │                                                                     │
│        │ Atropos (workbench topic)                                           │
│        ▼                                                                     │
│   ┌─────────────────┐                                                       │
│   │   sx-observer   │ ← Store-and-forward, filtering, scale-up triggers     │
│   │   (per workbench)│                                                       │
│   └────────┬────────┘                                                       │
│            │ Atropos (agent topics)                                          │
│            ▼                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │               AGENT INGRESS GATEWAY                                  │   │
│   │                                                                       │   │
│   │   ┌───────────────────────────────────────────────────────────┐     │   │
│   │   │                  EMPLOYED AGENT PODS                       │     │   │
│   │   │                                                            │     │   │
│   │   │   ┌─────────┐   ┌─────────┐   ┌─────────┐                │     │   │
│   │   │   │  Pod 1  │   │  Pod 2  │   │  Pod N  │                │     │   │
│   │   │   └─────────┘   └─────────┘   └─────────┘                │     │   │
│   │   │                                                            │     │   │
│   │   └───────────────────────────────────────────────────────────┘     │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Design Decisions

### Signal Exchange Integration

- Signal Exchange is **unaware of Agent Ingress Gateway**
- sx-observer acts as workbench-level observer
- All routing via **Atropos** (event bus)
- Agents update requests **directly via Hub APIs** (not via sx-observer)

### IAM Profile Provisioning

- IAM profile created **before** pod deployment
- Roles/groups inheritance from delegator (wildcard or CSV subset)
- Bot mode for agents without delegator
- Kill switch includes IAM revocation

### Authority Change Respawning

- Seer Operator only watches CRDs
- IAM Observer Service (in Agent Lifecycle Manager) watches IAM changes
- Authority changes propagated via CRD updates

---

## Related Subsystems

- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) - Employment spec management, IAM Observer Service
- [Agent Ingress Gateway](../agent-ingress-gateway/README.md) - Request routing
- [Cipher IAM Extensions](../cipher-iam-extensions/README.md) - IAM profile provisioning
- [Seer Sidecar](../seer-sidecar/README.md) - Policy enforcement

## Related Concepts

- [Agent Runtime Concept](../../implementation-concepts/agent-runtime.md) — Runtime execution environment concept

---

## Related Hub Documentation

- `olympus-hub-docs/04-subsystems/signal-exchange/README.md` - Signal Exchange
- `olympus-hub-docs/05-infrastructure/atropos.md` - Atropos event bus
- `olympus-hub-docs/05-infrastructure/atlantis.md` - Atlantis (EKS)
- `olympus-hub-docs/04-subsystems/signal-providers/heracles-api-gateway.md` - Heracles

---

*Agent Runtime provides secure, observable, and scalable execution for Employed Agents.*
