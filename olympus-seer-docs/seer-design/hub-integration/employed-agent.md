# Employed Agent as Deployed Application

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Seer-Hub Integration](./README.md)

---

## Overview

An **Employed Agent** is a Trained Agent granted delegated authority and deployed to serve a specific Scenario. In Hub terms, an Employed Agent corresponds to a **Deployed Hub Application** created during Scenario Deployment.

---

## Deployment Flow

When a Scenario is deployed, Hub and Seer operators orchestrate Employed Agent creation:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      SCENARIO DEPLOYMENT → EMPLOYED AGENT                     │
│                                                                               │
│   ┌─────────────────┐                                                        │
│   │ ScenarioDeployment                                                       │
│   │ CRD             │                                                        │
│   │                 │                                                        │
│   │ scenarioRef:    │                                                        │
│   │   dispute-res   │                                                        │
│   │ workbench:      │                                                        │
│   │   acme-disputes │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Hub Operator    │                                                        │
│   │                 │                                                        │
│   │ 1. Validates    │                                                        │
│   │ 2. Creates      │                                                        │
│   │    deployment   │                                                        │
│   │    spec         │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Seer Operator   │                                                        │
│   │                 │                                                        │
│   │ 1. Picks up     │                                                        │
│   │    deployment   │                                                        │
│   │ 2. Creates      │                                                        │
│   │    EmploymentSpec                                                        │
│   │ 3. Materializes │                                                        │
│   │    Employed     │                                                        │
│   │    Agent        │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Atlantis        │                                                        │
│   │ Runtime         │                                                        │
│   │                 │                                                        │
│   │ Starts Pod      │                                                        │
│   │ from Raw Agent  │                                                        │
│   │ container       │                                                        │
│   └─────────────────┘                                                        │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## CRD Relationship

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DEPLOYMENT CRDs                                      │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  ScenarioDeployment (Hub)                                            │   │
│   │                                                                       │   │
│   │  spec:                                                               │   │
│   │    scenarioRef: dispute-resolution                                   │   │
│   │    workbench: acme-disputes                                          │   │
│   │    applicationDeployments:                                           │   │
│   │      - appRef: fraud-case-analyst                                    │   │
│   │        toolBindings: [...]         ◄── Operative (concrete)          │   │
│   │        resourceBindings: [...]                                       │   │
│   │        memoryBindings: [...]                                         │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            │ triggers                                        │
│                            ▼                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  Seer EmploymentSpec (created by Seer Operator)                      │   │
│   │                                                                       │   │
│   │  spec:                                                               │   │
│   │    trainingRef: fraud-analyst-v2:1.7.0                               │   │
│   │    workScope:                                                        │   │
│   │      workbench: acme-disputes                                        │   │
│   │      scenario: dispute-resolution                                    │   │
│   │    operationalEnv:                                                   │   │
│   │      toolEndpoints: {...}          ◄── Resolved from bindings        │   │
│   │      credentials: {...}                                              │   │
│   │    capacity:                                                         │   │
│   │      tokenBudget: 100000/day                                         │   │
│   │    delegation:                                                       │   │
│   │      principal: disputes-supervisor                                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Relationship Cardinality

| Relationship | Cardinality | Description |
|--------------|-------------|-------------|
| **ScenarioDeployment → Employed Agent** | 1:1 | Each deployment creates one Employed Agent |
| **Trained Agent → Employed Agents** | 1:N | Many deployments can use same Trained Agent |
| **Employed Agent → Scenario** | 1:1 | Each Employed Agent serves one Scenario |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CARDINALITY                                          │
│                                                                               │
│   ┌───────────────┐                                                          │
│   │ Trained Agent │                                                          │
│   │ (App Spec)    │                                                          │
│   └───────┬───────┘                                                          │
│           │                                                                   │
│     ┌─────┴─────┬─────────────┐                                              │
│     ▼           ▼             ▼                                              │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐                                         │
│ │Employed │ │Employed │ │Employed │                                         │
│ │Agent 1  │ │Agent 2  │ │Agent 3  │                                         │
│ │         │ │         │ │         │                                         │
│ │Scenario │ │Scenario │ │Scenario │                                         │
│ │Deploy A │ │Deploy B │ │Deploy C │                                         │
│ └─────────┘ └─────────┘ └─────────┘                                         │
│                                                                               │
│   Multiple Scenario Deployments can use the same Trained Agent               │
│   Each creates a separate Employed Agent instance                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Binding Resolution

At deployment time, normative references are resolved to operative instances:

### Tool Binding

```yaml
# From HubApplicationSpec (normative)
hubConfig:
  toolRefs:
    - protocol: temenos-t24/get-transactions

# In ScenarioDeployment (operative)
applicationDeployments:
  - appRef: fraud-case-analyst
    toolBindings:
      - protocol: temenos-t24/get-transactions
        machine: acme-core-banking
        instance: acme-get-transactions
        endpoint: https://core.acme.bank/api/v1/transactions
```

### Resource Binding

```yaml
# From HubApplicationSpec (normative)
hubConfig:
  resourceRefs:
    - name: dispute-knowledge
      type: knowledge-bank
      ref: dispute-policies-kb

# In ScenarioDeployment (operative)
applicationDeployments:
  - appRef: fraud-case-analyst
    resourceBindings:
      - name: dispute-knowledge
        instance: acme-dispute-kb-prod
        endpoint: https://kb.acme.hub/dispute-policies
```

### Memory Binding

```yaml
# From HubApplicationSpec (declared requirements)
hubConfig:
  memoryRequirements:
    agentMemory:
      stores:
        - type: conversation
          name: case-dialog
        - type: kv
          name: case-entities

# In ScenarioDeployment (mapped to workbench stores)
applicationDeployments:
  - appRef: fraud-case-analyst
    memoryBindings:
      - name: case-dialog
        workbenchStore: disputes-conversation-store
      - name: case-entities
        workbenchStore: disputes-kv-store
```

---

## Employment Constraints

What Employment can and cannot do:

| Employment Can Do | Employment Cannot Do |
|-------------------|----------------------|
| Restrict tool access | Enable tools not in Training |
| Narrow scope of actions | Expand authority beyond Training |
| Add delegator preferences | Override Training guardrails |
| Set resource quotas | Remove safety constraints |
| Specify work context | Grant capabilities not trained |
| Map to specific endpoints | Change tool protocols |

---

## Lifecycle

Employed Agent lifecycle:

```
[Requested] → [Approved] → [Active] → [Suspended] → [Revoked]
```

| State | Description | Serving Requests? |
|-------|-------------|-------------------|
| **Requested** | Deployment pending | ❌ |
| **Approved** | Authorized, starting | ❌ |
| **Active** | Serving requests | ✅ |
| **Suspended** | Temporarily paused | ❌ |
| **Revoked** | Permanently stopped | ❌ |

### Kill Switch

The Seer Lifecycle Service can issue kill switch commands:

| Command | Effect | Authority Retained? |
|---------|--------|---------------------|
| **Suspend** | Stops execution | ✅ Yes |
| **Revoke** | Permanent stop | ❌ No |

---

## Memory Provisioning

Memory stores are provisioned at employment time:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      MEMORY PROVISIONING                                      │
│                                                                               │
│   ┌─────────────────┐                                                        │
│   │ Employment      │                                                        │
│   │ (Deployment)    │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐     ┌─────────────────────────────────────────────┐   │
│   │ Memory Stores   │     │           Per Request Isolation              │   │
│   │ Provisioned     │     │                                               │   │
│   │                 │     │   Request A: agent/request-a/kv/...          │   │
│   │ • conversation  │────►│   Request B: agent/request-b/kv/...          │   │
│   │ • kv            │     │   Request C: agent/request-c/kv/...          │   │
│   │ • log           │     │                                               │   │
│   └─────────────────┘     │   Stores constant per Employed Agent         │   │
│                           │   Reads/writes scoped to Request             │   │
│                           └─────────────────────────────────────────────────┘│
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

- **Stores**: Constant per Employed Agent (defined in EmploymentSpec)
- **Isolation**: Hub Agent Memory scopes all reads/writes to Request
- **Lifecycle**: Stores persist for session + retention period

---

## Versioning

Complete Employed Agent version identifier:

```
raw:v2.4.1/trained:v1.7.0/employed:v3.2.0
```

Every action is traceable to:
1. Raw Agent version executing
2. Training Spec version in effect
3. Employment Spec governing authority
4. Accountable human (delegating principal)

---

## Related Documentation

- [Agent Lifecycle Service](../subsystems/agent-lifecycle-service.md) — Full EmploymentSpec details
- [Trained Agent in Hub](./trained-agent.md) — Application Spec layer
- [Request Dispatch](./request-dispatch.md) — How requests reach agents
- [Memory Integration](./memory-integration.md) — Agent Memory in deployment

---

*Employed Agents are the runtime instantiation — Trained Agents with delegated authority serving specific Scenarios.*

