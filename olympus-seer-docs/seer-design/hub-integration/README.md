# Seer-Hub Integration

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-12

---

## Overview

This section documents how **Seer AI agents operate within the Hub ecosystem**. Seer is one of Hub's supported **Application Runtimes** — when a Hub Application specifies `runtime: seer`, the Seer operator manages the agent lifecycle, deployment, and execution.

---

## Key Concepts

### Seer as a Hub Application Runtime

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         HUB ECOSYSTEM                                        │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    APPLICATION RUNTIMES                              │   │
│   │                                                                       │   │
│   │   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐               │   │
│   │   │   Seer      │   │  Temporal   │   │   Custom    │               │   │
│   │   │  (AI Agents)│   │ (Workflows) │   │  Runtimes   │               │   │
│   │   └─────────────┘   └─────────────┘   └─────────────┘               │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
│   Hub provides: Request Management, Signal Exchange, Memory Services,        │
│                 Tool Registry, Knowledge Bank, Task Management               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Agent Layers in Hub Context

Seer implements a **three-layer agent model** that maps to Hub's application lifecycle:

| Seer Layer | Hub Equivalent | CRD Relationship |
|------------|----------------|------------------|
| **Raw Agent** | Container artifact | Seer-managed (CI/CD by Seer) |
| **Trained Agent** | Application Specification | HubApplicationSpec → TrainingSpec |
| **Employed Agent** | Deployed Application | ScenarioDeployment → EmploymentSpec |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CRD HIERARCHY                                        │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  HubApplicationSpec (runtime: seer)                                  │   │
│   │      │                                                                │   │
│   │      └── references ──► Seer TrainingSpec CRD                        │   │
│   │                              │                                        │   │
│   │                              └── references ──► Raw Agent Image       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  ScenarioDeployment                                                  │   │
│   │      │                                                                │   │
│   │      └── creates ──► Seer EmploymentSpec                             │   │
│   │                          │                                            │   │
│   │                          └── materializes ──► Employed Agent Pod      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Operator Orchestration

### Deployment Flow

When a Scenario is deployed with a Seer agent:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      SCENARIO DEPLOYMENT FLOW                                 │
│                                                                               │
│   ┌───────────────┐                                                          │
│   │ Scenario      │                                                          │
│   │ Deployment    │                                                          │
│   │ CRD           │                                                          │
│   └───────┬───────┘                                                          │
│           │                                                                   │
│           ▼                                                                   │
│   ┌───────────────┐     ┌───────────────┐     ┌───────────────┐             │
│   │ Hub Operator  │────►│ Seer Operator │────►│ Atlantis      │             │
│   │               │     │               │     │ Runtime       │             │
│   │ Creates       │     │ Creates       │     │               │             │
│   │ deployment    │     │ EmploymentSpec│     │ Starts Pod    │             │
│   │ spec          │     │               │     │               │             │
│   └───────────────┘     └───────────────┘     └───────────────┘             │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

1. **Hub Operator** processes ScenarioDeployment, creates deployment spec for Seer agent
2. **Seer Operator** picks up spec, creates EmploymentSpec, materializes Employed Agent
3. **Atlantis Runtime** starts the agent container pod

### Request Dispatch Flow

When a Hub Request update reaches a Seer agent:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      REQUEST DISPATCH FLOW                                    │
│                                                                               │
│   ┌───────────────┐                                                          │
│   │ Request       │                                                          │
│   │ Update        │                                                          │
│   └───────┬───────┘                                                          │
│           │                                                                   │
│           ▼                                                                   │
│   ┌───────────────┐                                                          │
│   │ Signal        │                                                          │
│   │ Exchange      │                                                          │
│   │               │                                                          │
│   │ Publishes to  │                                                          │
│   │ Atropos       │                                                          │
│   │ (workbench    │                                                          │
│   │  topic)       │                                                          │
│   └───────┬───────┘                                                          │
│           │ Atropos                                                          │
│           ▼                                                                   │
│   ┌───────────────┐     ┌───────────────┐     ┌───────────────┐             │
│   │ sx-observer   │────►│ Agent Ingress │────►│ Agent Pods    │             │
│   │ (per          │     │ Gateway       │     │               │             │
│   │  workbench)   │     │ (Heracles)    │     │ Raw Agent     │             │
│   │               │     │               │     │ Container     │             │
│   │ Filters &     │     │ Routes to     │     │               │             │
│   │ routes        │     │ pods          │     │ /invoke       │             │
│   └───────────────┘     └───────────────┘     └───────────────┘             │
│                                                                               │
│   K8s/Atlantis Service Mesh Orchestration                                    │
└──────────────────────────────────────────────────────────────────────────────┘
```

1. **Signal Exchange** publishes request update to Atropos (workbench-level topic)
2. **sx-observer** receives all updates, filters by scenario/agent subscriptions, stores in queue, triggers scale-up if needed, and publishes to agent-specific Atropos topics
3. **Agent Ingress Gateway** subscribes to agent topics and routes to deployed agent pods via K8s Service
4. **Agent Pods** receive HTTPS invocation with request update payload

---

## Key Integration Points

| Integration Point | Hub Component | Seer Component | Protocol |
|-------------------|---------------|----------------|----------|
| **Agent Definition** | HubApplicationSpec | TrainingSpec | CRD reference |
| **Agent Deployment** | ScenarioDeployment | EmploymentSpec | Operator orchestration |
| **Request Dispatch** | Signal Exchange | sx-observer → Agent Ingress Gateway | Atropos → HTTPS |
| **Context Compilation** | Memory Services, Knowledge Services, Request Management | Context Compilation Service (SDK/API) | Agent-initiated |
| **Tool Invocation** | Tool Registry | Direct Tool Dispatcher | Tool protocol |
| **Memory Access** | Memory Services | Agent Memory SDK | SDK/Tool |

---

## Documents in This Section

### Concepts

| Document | Description | Status |
|----------|-------------|--------|
| [Raw Agent in Hub Context](./raw-agent.md) | Container requirements, framework flexibility | 🟡 Draft |
| [Trained Agent as Hub Application](./trained-agent.md) | HubApplicationSpec ↔ TrainingSpec mapping | 🟡 Draft |
| [Employed Agent as Deployed Application](./employed-agent.md) | ScenarioDeployment ↔ EmploymentSpec | 🟡 Draft |
| [Request Dispatch](./request-dispatch.md) | Signal Exchange → sx-observer → Agent Ingress Gateway → Agent flow | 🟡 Draft |
| [Memory Integration](./memory-integration.md) | Agent Memory Services in Seer context | 🟡 Draft |
| [Context Assembly](./context-assembly.md) | Context Compilation Service invocation patterns | 🟡 Draft |

### CRD Specifications

| Document | Description | Status |
|----------|-------------|--------|
| [Training Spec CRD](./training-spec-crd.md) | Full TrainingSpec CRD schema | 🟡 Draft |
| [Employment Spec CRD](./employment-spec-crd.md) | Full EmploymentSpec CRD schema | 🟡 Draft |

---

## Related Documentation

### Seer Internals
- [Agent Lifecycle Manager](../subsystems/agent-lifecycle-manager/README.md) — Employment spec management, delegation chain sync, agent levers, ecosystem integration, directory
- [Agent Runtime](../subsystems/agent-runtime/README.md) — Runtime environment, deployment, Signal Exchange integration
- [Agent Runtime: Signal Exchange Integration](../subsystems/agent-runtime/signal-exchange-integration.md) — sx-observer architecture
- [Agent Runtime: Agent Ingress Gateway Integration](../subsystems/agent-runtime/agent-ingress-gateway-integration.md) — Agent Ingress Gateway integration
- [Agent Ingress Gateway](../subsystems/agent-ingress-gateway/README.md) — Agent Ingress Gateway overview
- [Context Compilation Service](../subsystems/context-compiler/compilation-service.md) — Context compilation service design

### Hub Components
- [Hub Application Concepts](../../../olympus-hub-docs/01-concepts/hub-applications.md)
- [Workbench & Scenario Management](../../../olympus-hub-docs/04-subsystems/workbench-management/README.md)
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md)
- [Agent Memory Services](../../../olympus-hub-docs/04-subsystems/memory-services/agent-memory/README.md)

### AOSM Foundations
- [Raw, Trained, Employed Agents](../../../aosm-meta-model/raw-trained-employed-agents.md)

---

*This section bridges Seer's agent model with Hub's application lifecycle, enabling AI agents to operate as first-class Hub applications.*

