# 11.3 Coordination Patterns

Seer provides structured patterns for agent coordination through Hub's composite system architecture. These patterns define how agents invoke each other, share context, and manage work across boundaries.

## Pattern Overview

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Scenario-as-Tool** | Invoke a scenario synchronously like a tool | Reusable procedures |
| **Scenario-as-Agent** | Scenario completes tasks in another scenario's queue | Automated task handling |
| **Workbench-as-Machine** | Cross-workbench invocation | Domain separation |
| **Parent-Child Requests** | Nested request hierarchy | Context inheritance |

## Scenario-as-Tool

A scenario can be exposed as a callable tool, enabling other agents to invoke it synchronously.

### How It Works

```
Agent in Scenario A
    ↓ invokes
"dispute-resolution" tool
    ↓ maps to
Scenario B (Dispute Resolution)
    ↓ executes
Returns result to Agent
```

### When to Use

| ✅ Use When | ❌ Avoid When |
|-------------|---------------|
| Synchronous, request-response needed | Long-running with human tasks |
| Reusable procedure across scenarios | Asynchronous updates required |
| Lightweight invocation | Full request context needed |

### Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsTool
metadata:
  name: eligibility-check-tool
spec:
  scenario_ref: eligibility-check
  tool:
    name: check-eligibility
    version: "1.0.0"
  operations:
    - signal_type: eligibility.check.requested
      operation:
        name: check
        description: "Check customer eligibility"
```

### Context Handling

Within the same workbench:
- Child request created with `parent_request_id`
- Child can access parent's compiled context
- Lifecycle bound to parent (cancelled if parent cancels)

## Scenario-as-Agent

A scenario can be enrolled as an agent in another scenario's task queue, enabling it to complete tasks automatically.

### How It Works

```
Scenario A creates task → Task Queue
                              ↓
          Task assigned to Scenario-Agent B
                              ↓
          Scenario B processes task
                              ↓
          Task completed via Agent API
                              ↓
          Scenario A receives completion
```

### When to Use

| ✅ Use When | ❌ Avoid When |
|-------------|---------------|
| Automating tasks in existing scenarios | Need synchronous invocation |
| Gradual automation (humans + AI) | Simple procedure call |
| Reusing automation across queues | No task queue involved |

### Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsAgent
metadata:
  name: evidence-review-agent
spec:
  source:
    workbench: evidence-automation
    scenario: evidence-review-automation
  agent:
    id: scenario-agent-evidence-review
    skills: [document_analysis]
    capacity:
      max_concurrent_tasks: 10
  deployments:
    - target_workbench: dispute-operations
      task_queues:
        - queue_id: evidence-review-queue
          allocation_weight: 50
```

### Flexibility

Scenario-as-Agent enables gradual automation:

```
evidence-review-queue:
  - Evidence Bot: 50% weight
  - Human Analyst: 50% weight
```

Adjust weights without code changes as confidence grows.

## Workbench-as-Machine

A workbench can be published as a "machine" that other workbenches can invoke.

### How It Works

```
Workbench A (Customer Service)
    ↓ invokes
Machine: Workbench B (Dispute Resolution)
    ↓
Independent request in Workbench B
    ↓
Result returned to Workbench A
```

### Key Difference from Scenario-as-Tool

| Aspect | Scenario-as-Tool | Workbench-as-Machine |
|--------|------------------|----------------------|
| **Scope** | Same workbench | Cross-workbench |
| **Context** | Parent-child with shared context | Independent, explicit context |
| **Lifecycle** | Coupled | Decoupled |
| **Governance** | Shared policies | Separate policy domains |

### When to Use

| ✅ Use When | ❌ Avoid When |
|-------------|---------------|
| Cross-domain operations | Within same business domain |
| Clear domain separation needed | Tight context coupling required |
| Different governance requirements | Simple tool invocation |

### Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchAsMachine
metadata:
  name: dispute-workbench-machine
spec:
  source_workbench: dispute-operations
  machine:
    id: dispute-machine
    description: "Dispute resolution capabilities"
  exposed_tools:
    scenarios:
      - scenario_id: standard-dispute
        as_tool: dispute-resolution
```

## Parent-Child Requests

Requests can form hierarchies for context inheritance and lifecycle management.

### How It Works

```
Parent Request (Fraud Investigation)
    │
    ├── Child Request (Document Verification)
    │       └── Grandchild Request (Signature Check)
    │
    └── Child Request (Customer Notification)
```

### Context Inheritance

| Aspect | Behavior |
|--------|----------|
| **Context access** | Children can access parent's compiled context |
| **Result isolation** | Child results don't pollute parent context |
| **Lifecycle** | Children cancelled if parent cancelled |

### Traceability

```
Parent Request: req-001
    ↓
Child Request: req-002 (parent_request_id: req-001)
    ↓
All CAF records link to both req-001 and req-002
```

Enables end-to-end traceability across nested operations.

## Pattern Selection Guide

| Need | Recommended Pattern |
|------|---------------------|
| Reuse procedure across scenarios | Scenario-as-Tool |
| Automate tasks without changing scenario | Scenario-as-Agent |
| Cross-workbench with domain separation | Workbench-as-Machine |
| Nested operations with context sharing | Parent-Child Requests |
| Human + AI in same queue | Scenario-as-Agent with mixed enrollment |

---

**References:**
*   `olympus-hub-docs/09-composite-systems-and-patterns/scenario-as-a-tool.md`
*   `olympus-hub-docs/09-composite-systems-and-patterns/scenario-as-an-agent.md`
*   `olympus-hub-docs/09-composite-systems-and-patterns/workbench-as-a-machine.md`
