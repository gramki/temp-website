# Trained Agent as Hub Application

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Seer-Hub Integration](./README.md)

---

## Overview

A **Trained Agent** is a Raw Agent configured with organizational knowledge, domain-specific skills, and defined responsibilities. In Hub terms, a Trained Agent corresponds to a **Hub Application Specification** with `runtime: seer`.

---

## CRD Relationship

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CRD HIERARCHY                                        │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  HubApplicationSpec                                                  │   │
│   │                                                                       │   │
│   │  metadata:                                                           │   │
│   │    name: fraud-case-analyst                                          │   │
│   │  spec:                                                               │   │
│   │    runtime: seer                      ◄── Selects Seer runtime       │   │
│   │    seerTrainingRef:                                                  │   │
│   │      name: fraud-analyst-v2           ◄── References TrainingSpec    │   │
│   │      namespace: tenant-acme                                          │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            │ references                                      │
│                            ▼                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  Seer TrainingSpec (managed by Seer Operator)                        │   │
│   │                                                                       │   │
│   │  metadata:                                                           │   │
│   │    name: fraud-analyst-v2                                            │   │
│   │  spec:                                                               │   │
│   │    rawAgentRef: fraud-analyst-base:v2.4.1                            │   │
│   │    systemPrompt: ...                                                 │   │
│   │    skillPrompts: ...                                                 │   │
│   │    toolRefs: ...                                                     │   │
│   │    knowledgeRefs: ...                                                │   │
│   │    guardrailRefs: ...                                                │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Operator Responsibilities

| Operator | Validates | Manages |
|----------|-----------|---------|
| **Hub Operator** | HubApplicationSpec schema, runtime reference | Application lifecycle in Hub |
| **Seer Operator** | TrainingSpec contents, guardrails, prompts | Training configuration |

> **Note**: Hub does not validate TrainingSpec contents — that's Seer Operator's responsibility.

---

## Reusability

Trained Agents (via their HubApplicationSpec) can be reused:

| Scope | Reuse Pattern |
|-------|---------------|
| **Within Workbench** | Multiple Scenarios reference same application |
| **Across Workbenches** | Same TrainingSpec, different HubApplicationSpecs |
| **Across Tenants** | Same Raw Agent, different TrainingSpecs |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         REUSE PATTERNS                                       │
│                                                                               │
│   ┌─────────────────┐                                                        │
│   │  Raw Agent      │◄─────────────────────────────────────────────────┐    │
│   │  (Base Image)   │                                                   │    │
│   └────────┬────────┘                                                   │    │
│            │                                                             │    │
│    ┌───────┴───────┬────────────────┬────────────────┐                 │    │
│    ▼               ▼                ▼                ▼                 │    │
│ ┌────────┐    ┌────────┐       ┌────────┐       ┌────────┐            │    │
│ │Training│    │Training│       │Training│       │Training│            │    │
│ │Spec A  │    │Spec B  │       │Spec C  │       │Spec D  │            │    │
│ │(Tenant │    │(Tenant │       │(Tenant │       │(Tenant │            │    │
│ │  1)    │    │  1)    │       │  2)    │       │  2)    │            │    │
│ └────────┘    └────────┘       └────────┘       └────────┘            │    │
│                                                                         │    │
│   Many Trained Agents can reference one Raw Agent                       │    │
│   Each Trained Agent belongs to exactly one Raw Agent                   │    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## HubApplicationSpec for Seer

### Schema

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: fraud-case-analyst
  namespace: acme-disputes
  labels:
    app.kubernetes.io/part-of: dispute-resolution
    seer.olympus.io/agent-type: case-worker
spec:
  # Runtime Selection
  runtime: seer
  
  # Reference to Seer TrainingSpec
  seerTrainingRef:
    name: fraud-analyst-v2
    namespace: acme-disputes
    version: "1.7.0"  # Semantic version of TrainingSpec
  
  # Hub-level configuration
  hubConfig:
    # Tool references (normative - resolved at employment)
    toolRefs:
      - name: get-transaction-history
        protocol: temenos-t24/get-transactions
      - name: check-fraud-rules
        protocol: fraud-engine/evaluate
    
    # Resource references (normative)
    resourceRefs:
      - name: dispute-knowledge
        type: knowledge-bank
        ref: dispute-policies-kb
      - name: fraud-patterns
        type: knowledge-bank
        ref: fraud-patterns-kb
    
    # Memory requirements (declared, mapped at employment)
    memoryRequirements:
      agentMemory:
        stores:
          - type: conversation
            name: case-dialog
            compaction: summarize
          - type: kv
            name: case-entities
          - type: log
            name: session-log
  
  # Application metadata
  metadata:
    description: "AI agent for fraud case analysis and resolution"
    version: "1.0.0"
    owner: disputes-team
```

### Key Fields

| Field | Description | Required |
|-------|-------------|----------|
| `runtime` | Must be `seer` for Seer agents | ✅ |
| `seerTrainingRef` | Reference to Seer TrainingSpec CRD | ✅ |
| `hubConfig.toolRefs` | Hub tool protocols (normative) | ❌ |
| `hubConfig.resourceRefs` | Hub resources (knowledge banks, etc.) | ❌ |
| `hubConfig.memoryRequirements` | Agent Memory store declarations | ❌ |

---

## TrainingSpec Contents

The TrainingSpec (managed by Seer Operator) contains:

| Component | Description | Ownership |
|-----------|-------------|-----------|
| **Raw Agent Reference** | Container image to use | Integral |
| **System Prompts** | Agent persona, role definition | Integral |
| **Skill Prompts** | Task-specific instructions | Integral |
| **Labels** | Classification, capabilities | Integral |
| **Guardrail References** | Safety constraints (immutable) | Referenced |
| **Tool Specifications** | Tool schemas, usage patterns | Referenced |
| **Knowledge Base References** | Accessible knowledge sources | Referenced |
| **Memory Training** | Memory usage patterns | Integral |

### Guardrail Immutability

> **Critical**: Training guardrails are **immutable** once published. They cannot be weakened, bypassed, or overridden at Employment.

---

## Tool and Resource Binding

TrainingSpec uses Hub's **two-level registry model**:

| Level | In TrainingSpec | Resolved At |
|-------|-----------------|-------------|
| **Normative (Abstract)** | Tool protocols, resource types | Employment |
| **Operative (Concrete)** | — | Deployment CRD |

### Example: Tool Protocol Reference

```yaml
# In TrainingSpec (normative)
toolRefs:
  - protocol: temenos-t24/get-transactions
    usage: "Retrieve customer transaction history"
    permissions:
      - read

# In EmploymentSpec (operative - resolved)
toolBindings:
  - protocol: temenos-t24/get-transactions
    instance: acme-core-banking/get-transactions
    endpoint: https://core.acme.bank/api/v1/transactions
```

---

## Lifecycle

TrainingSpec (and corresponding HubApplicationSpec) lifecycle:

```
[Drafted] → [Validated] → [Published] → [Active] → [Archived]
```

| State | Description | Can Deploy? |
|-------|-------------|-------------|
| **Drafted** | In development | ❌ |
| **Validated** | Tested in sandbox | ❌ |
| **Published** | Approved, available | ✅ |
| **Active** | In use by Employed Agents | ✅ |
| **Archived** | Superseded | ❌ (new) |

---

## Versioning

### Independent Versioning

Each layer versions independently:

```
Raw Agent:      v2.4.1
TrainingSpec:   v1.7.0
HubAppSpec:     v1.0.0
```

### Compatibility Declarations

```yaml
# TrainingSpec declares Raw Agent compatibility
spec:
  rawAgentRef:
    name: fraud-analyst-base
    version: "^2.0.0"  # Compatible with 2.x.x

# HubApplicationSpec declares TrainingSpec version
spec:
  seerTrainingRef:
    name: fraud-analyst-v2
    version: "~1.7.0"  # Compatible with 1.7.x
```

---

## Scenario Binding

Scenarios reference the HubApplicationSpec:

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioSpec
metadata:
  name: dispute-resolution
spec:
  automationSpec:
    applicationRef:
      name: fraud-case-analyst  # HubApplicationSpec
      runtime: seer
    role: case-worker
    triggers:
      - type: request-update
        filter: "update.type == 'NEW_CASE'"
```

---

## Related Documentation

- [Agent Lifecycle Service](../subsystems/agent-lifecycle-service.md) — Full TrainingSpec details
- [Raw Agent in Hub](./raw-agent.md) — Container layer
- [Employed Agent in Hub](./employed-agent.md) — Deployment layer
- [Hub Registry Services](../../../olympus-hub-docs/04-subsystems/registry-services/README.md) — Tool/Resource binding

---

*Trained Agents bridge Raw Agent capabilities with organizational knowledge, becoming Hub Applications.*

