# Request Dispatch to Seer Agents

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-12  
> **Parent**: [Seer-Hub Integration](./README.md)

---

## Overview

When a Hub Request is updated, the update is dispatched to the Seer Employed Agent via a multi-hop path using **Atropos event bus**: **Signal Exchange → sx-observer → Agent Ingress Gateway → Agent Pods**. Each update translates to an HTTPS invocation of the agent.

**Key Design Points**:
- Signal Exchange is **unaware of Agent Ingress Gateway** — all routing goes through sx-observer
- **sx-observer** acts as workbench-level observer, filtering and routing updates
- **Agent Ingress Gateway** is a Heracles configuration layer (not a separate service)
- All message routing uses **Atropos** event bus

---

## Dispatch Flow

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      REQUEST UPDATE DISPATCH                                  │
│                                                                               │
│   ┌─────────────────┐                                                        │
│   │ Request Update  │  (e.g., new case, user message, task result)           │
│   │                 │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Signal Exchange │                                                        │
│   │                 │                                                        │
│   │ 1. Publishes to  │                                                        │
│   │    Atropos       │                                                        │
│   │    (workbench    │                                                        │
│   │    topic)        │                                                        │
│   │ 2. Unaware of    │                                                        │
│   │    Agent Ingress │                                                        │
│   │    Gateway       │                                                        │
│   └────────┬────────┘                                                        │
│            │ Atropos: sx.workbench.{workbench_id}.updates                     │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ sx-observer     │                                                        │
│   │ (per workbench) │                                                        │
│   │                 │                                                        │
│   │ 1. Receives all │                                                        │
│   │    updates       │                                                        │
│   │ 2. Stores in     │                                                        │
│   │    durable queue │                                                        │
│   │ 3. Filters by    │                                                        │
│   │    scenario/agent│                                                        │
│   │ 4. Triggers      │                                                        │
│   │    scale-up if   │                                                        │
│   │    needed        │                                                        │
│   │ 5. Publishes to  │                                                        │
│   │    Atropos       │                                                        │
│   │    (agent topic) │                                                        │
│   └────────┬────────┘                                                        │
│            │ Atropos: sx.agent.{agent_id}.dispatch                            │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Agent Ingress   │                                                        │
│   │ Gateway         │                                                        │
│   │ (Heracles Config)│                                                       │
│   │                 │                                                        │
│   │ 1. Subscribes to│                                                        │
│   │    agent topics │                                                        │
│   │ 2. Routes to     │                                                        │
│   │    agent pods    │                                                        │
│   │ 3. Load balances │                                                        │
│   │    via K8s       │                                                        │
│   │    Service       │                                                        │
│   └────────┬────────┘                                                        │
│            │ HTTPS (K8s Service)                                              │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Agent Pods      │                                                        │
│   │                 │                                                        │
│   │ Raw Agent       │                                                        │
│   │ Container       │                                                        │
│   │                 │                                                        │
│   │ /invoke         │◄── Receives payload                                    │
│   └─────────────────┘                                                        │
│                                                                               │
│   K8s/Atlantis Service Mesh Orchestration                                    │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Observer Registration

When a workbench is set up, **sx-observer** registers as a **workbench-level observer** with Signal Exchange. Signal Exchange does NOT accept subscriptions per scenario or per request — one observer per workbench receives all request updates.

### Workbench-Level Subscription

```yaml
# sx-observer subscription (conceptual)
subscription:
  type: workbench-observer
  workbenchId: acme-disputes
  atroposTopic: sx.workbench.acme-disputes.updates
```

### Agent-Level Filtering

sx-observer filters updates based on:
- Which scenarios the updates belong to (from request metadata)
- Which agents are subscribed to those scenarios (from EmploymentSpec `workScope.scenarios`)
- Request context and agent assignments

```yaml
# EmploymentSpec defines scenario subscriptions
spec:
  workScope:
    workbench: acme-disputes
    scenarios:
      - retail-fraud-triage
      - wholesale-fraud-review
```

### Agent Ingress Gateway Subscription

Agent Ingress Gateway subscribes to agent-specific Atropos topics:

```
Topic: sx.agent.{agent_id}.dispatch
```

**Key Points**:
- Signal Exchange only knows about sx-observer (not Agent Ingress Gateway)
- sx-observer filters and routes to appropriate agents
- Agent Ingress Gateway subscribes to agent-specific topics

---

## Invocation Payload

Each request update is dispatched as an HTTPS POST to the agent's `/invoke` endpoint:

### Request Structure

```json
{
  "invocation_id": "inv-123e4567-e89b",
  "timestamp": "2026-01-08T14:30:00Z",
  
  "request": {
    "request_id": "req-abc123",
    "workbench_id": "acme-disputes",
    "scenario_id": "dispute-resolution",
    "tenant_id": "acme",
    "created_at": "2026-01-08T14:00:00Z"
  },
  
  "update": {
    "update_id": "upd-xyz789",
    "type": "USER_MESSAGE",
    "timestamp": "2026-01-08T14:30:00Z",
    "payload": {
      "message": "The transaction was unauthorized",
      "channel": "chat",
      "user_id": "user-456"
    }
  },
  
  "context": {
    "compiled": false,
    "context_ref": "ctx-ref-001"
  },
  
  "employment": {
    "employed_agent_id": "emp-fraud-analyst-001",
    "training_version": "v1.7.0",
    "raw_version": "v2.4.1"
  }
}
```

### Key Fields

| Field | Description |
|-------|-------------|
| `invocation_id` | Unique identifier for this invocation |
| `request` | Hub Request metadata |
| `update` | The specific update that triggered invocation |
| `context` | Reference to compiled context (if pre-compiled) |
| `employment` | Employed Agent metadata for traceability |

---

## Update Types

| Update Type | Description | Typical Source |
|-------------|-------------|----------------|
| `NEW_CASE` | New case/request created | External system, user |
| `USER_MESSAGE` | User sends a message | Chat channel |
| `TASK_COMPLETED` | A task was completed | Human agent, other AI |
| `TASK_FAILED` | A task failed | System |
| `CONTEXT_UPDATE` | Context was updated | Application, other agent |
| `EVIDENCE_ADDED` | New evidence attached | Investigation tool |
| `ESCALATION` | Request escalated | Human, system |
| `TIMEOUT` | Timer expired | Scheduler |

---

## Agent Response

The agent responds synchronously or asynchronously:

### Synchronous Response

```json
{
  "status": "completed",
  "updates": [
    {
      "type": "context_update",
      "payload": {
        "fraud_likelihood": 0.87,
        "risk_factors": ["velocity", "new_device"]
      }
    },
    {
      "type": "task_emit",
      "payload": {
        "task_type": "human_review",
        "title": "Review high-risk transaction",
        "priority": "high"
      }
    }
  ],
  "memory_writes": [
    {
      "store": "case-entities",
      "key": "fraud_assessment",
      "value": { "score": 0.87, "timestamp": "..." }
    }
  ]
}
```

### Asynchronous Processing

For long-running operations, agent can:
1. Respond immediately with `status: "processing"`
2. Post updates to Signal Exchange when complete

```json
{
  "status": "processing",
  "estimated_completion": "2026-01-08T14:35:00Z",
  "callback_id": "cb-123"
}
```

---

## Context Handling

The agent can obtain context in two ways:

### 1. Pre-compiled Context (Optional)

If `context.compiled: true`, the payload includes compiled context:

```json
{
  "context": {
    "compiled": true,
    "data": {
      "case_history": [...],
      "precedents": [...],
      "policies": [...]
    }
  }
}
```

### 2. Agent-Initiated Context Compilation

If `context.compiled: false`, agent invokes Context Compilation Service:

```python
# Agent code
from seer_sdk import ContextCompiler

compiler = ContextCompiler.from_environment()

# Context Compilation Service automatically selects retrievers
# based on Training Spec selector criteria matching request update metadata
context = compiler.compile(
    request_id=invocation.request.request_id,
    update_id=invocation.update.update_id
    # Retrievers are automatically selected from Training Spec
    # based on update metadata (updateType, taskType, contextKeys, etc.)
)
```

**Note**: The Context Compilation Service automatically selects retrievers based on Training Spec retriever configurations that match the request update metadata. Agents can optionally override token budgets, but retriever selection is handled automatically.

---

## Error Handling

| Error Type | Handling |
|------------|----------|
| **Agent unavailable** | Retry with backoff, then escalate |
| **Timeout** | Record timeout, retry or escalate |
| **Agent error** | Log error, optionally retry |
| **Validation failure** | Reject update, notify sender |

### Retry Policy

```yaml
retry:
  max_attempts: 3
  backoff:
    initial: 1s
    multiplier: 2
    max: 30s
  on_failure: escalate_to_human
```

---

## Traceability

Every invocation is traceable:

| Trace Field | Source |
|-------------|--------|
| `invocation_id` | Generated per invocation |
| `request_id` | Hub Request |
| `update_id` | Specific update |
| `employed_agent_id` | Employed Agent |
| `training_version` | TrainingSpec |
| `raw_version` | Raw Agent container |

Traces are stored in:
- **Hub**: Request history
- **Seer**: Agent observability
- **CAF**: Episodic memory (decisions, actions)

---

## Store-and-Forward and Scale-to-Zero

### Store-and-Forward

sx-observer implements store-and-forward capability:
- **Reliable Delivery**: Updates stored in durable queue before forwarding
- **Scale-to-Zero Support**: Requests stored until agents scale up
- **Resilience**: Persistent storage ensures updates are not lost

### Scale-to-Zero and Scale-Up

When no requests are pending, agent pods can scale to zero. When requests arrive:
1. sx-observer stores request in queue
2. sx-observer checks agent replica count
3. If replicas == 0, sx-observer triggers scale-up (via Kubernetes HPA)
4. Once pods are ready, stored requests are dispatched

### Service Mesh Details

The dispatch uses Atlantis/K8s service mesh for final routing:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      SERVICE MESH ROUTING                                     │
│                                                                               │
│   ┌─────────────────┐                                                        │
│   │ Agent Ingress   │                                                        │
│   │ Gateway         │                                                        │
│   │ (Heracles)      │                                                        │
│   │                 │                                                        │
│   │ Path:           │                                                        │
│   │ /seer/.../      │                                                        │
│   │ agents/{id}/    │                                                        │
│   │ dispatch        │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Deployed Agent  │                                                        │
│   │ Service         │                                                        │
│   │                 │                                                        │
│   │ K8s Service:    │                                                        │
│   │ fraud-analyst-  │                                                        │
│   │ emp-001         │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│     ┌──────┴──────┐                                                          │
│     ▼             ▼                                                          │
│ ┌───────┐    ┌───────┐                                                       │
│ │ Pod 1 │    │ Pod 2 │   (if scaled)                                         │
│ └───────┘    └───────┘                                                       │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — Observer pattern
- [Agent Runtime: Signal Exchange Integration](../subsystems/agent-runtime/signal-exchange-integration.md) — sx-observer architecture
- [Agent Runtime: Agent Ingress Gateway Integration](../subsystems/agent-runtime/agent-ingress-gateway-integration.md) — Agent Ingress Gateway integration
- [Agent Ingress Gateway](../subsystems/agent-ingress-gateway/README.md) — Agent Ingress Gateway overview
- [Employed Agent](./employed-agent.md) — Deployment details
- [Context Assembly](./context-assembly.md) — Context Compilation Service invocation
- [Runtime & Deployment](../subsystems/agent-runtime/runtime-deployment.md) — Seer runtime
- [Atropos Event Bus](../../../olympus-hub-docs/05-infrastructure/atropos.md) — Atropos event bus

---

*Request dispatch bridges Hub's Signal Exchange with Seer's agent runtime via sx-observer and Agent Ingress Gateway, enabling reliable, scalable agent invocation with scale-to-zero support.*

