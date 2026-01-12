# Seer-Hub Integration

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08

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
│   ┌───────────────┐     ┌───────────────┐     ┌───────────────┐             │
│   │ Signal        │────►│ Seer Runtime  │────►│ Agent Pod     │             │
│   │ Exchange      │     │ Service       │     │               │             │
│   │               │     │ (Observer)    │     │ Raw Agent     │             │
│   │ Dispatches    │     │               │     │ Container     │             │
│   │ to observer   │     │ Routes to pod │     │               │             │
│   └───────────────┘     └───────────────┘     └───────────────┘             │
│                                                                               │
│   K8s/Atlantis Service Mesh Orchestration                                    │
└──────────────────────────────────────────────────────────────────────────────┘
```

1. **Signal Exchange** dispatches request update to Seer Runtime Service (registered as observer)
2. **Seer Runtime Service** routes to the specific pod of the Employed Agent deployment
3. **Agent Pod** receives HTTPS invocation with request update payload

---

## Key Integration Points

| Integration Point | Hub Component | Seer Component | Protocol |
|-------------------|---------------|----------------|----------|
| **Agent Definition** | HubApplicationSpec | TrainingSpec | CRD reference |
| **Agent Deployment** | ScenarioDeployment | EmploymentSpec | Operator orchestration |
| **Request Dispatch** | Signal Exchange | Runtime Service | HTTPS (observer pattern) |
| **Context Assembly** | Memory Services | CAE (SDK/API) | Agent-initiated |
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
| [Request Dispatch](./request-dispatch.md) | SX → Runtime Service → Agent flow | 🟡 Draft |
| [Memory Integration](./memory-integration.md) | Agent Memory Services in Seer context | 🟡 Draft |
| [Context Assembly](./context-assembly.md) | CAE invocation patterns | 🟡 Draft |

### CRD Specifications

| Document | Description | Status |
|----------|-------------|--------|
| [Training Spec CRD](./training-spec-crd.md) | Full TrainingSpec CRD schema | 🟡 Draft |
| [Employment Spec CRD](./employment-spec-crd.md) | Full EmploymentSpec CRD schema | 🟡 Draft |

---

## Related Documentation

### Seer Internals
- [Agent Lifecycle Service](../subsystems/agent-lifecycle-service.md) — Raw/Trained/Employed model
- [Runtime & Deployment](../subsystems/agent-runtime/runtime-deployment.md) — Atlantis runtime
- [Context Assembly Engine](../subsystems/context-assembly-engine.md) — CAE design

### Hub Components
- [Hub Application Concepts](../../../olympus-hub-docs/01-concepts/hub-applications.md)
- [Workbench & Scenario Management](../../../olympus-hub-docs/04-subsystems/workbench-management/README.md)
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md)
- [Agent Memory Services](../../../olympus-hub-docs/04-subsystems/memory-services/agent-memory/README.md)

### AOSM Foundations
- [Raw, Trained, Employed Agents](../../../aosm-meta-model/raw-trained-employed-agents.md)

---

*This section bridges Seer's agent model with Hub's application lifecycle, enabling AI agents to operate as first-class Hub applications.*

