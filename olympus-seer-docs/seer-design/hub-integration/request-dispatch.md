# Request Dispatch to Seer Agents

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Seer-Hub Integration](./README.md)

---

## Overview

When a Hub Request is updated, the update is dispatched to the Seer Employed Agent via a multi-hop path: **Signal Exchange → Seer Runtime Service → Agent Pod**. Each update translates to an HTTPS invocation of the agent.

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
│   │ 1. Identifies   │                                                        │
│   │    observers    │                                                        │
│   │ 2. Routes to    │                                                        │
│   │    Seer Runtime │                                                        │
│   │    Service      │                                                        │
│   └────────┬────────┘                                                        │
│            │ HTTPS                                                           │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Seer Runtime    │                                                        │
│   │ Service         │                                                        │
│   │                 │                                                        │
│   │ 1. Validates    │                                                        │
│   │    request      │                                                        │
│   │ 2. Identifies   │                                                        │
│   │    target pod   │                                                        │
│   │ 3. Routes to    │                                                        │
│   │    agent        │                                                        │
│   └────────┬────────┘                                                        │
│            │ HTTPS (service mesh)                                            │
│            ▼                                                                  │
│   ┌─────────────────┐                                                        │
│   │ Agent Pod       │                                                        │
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

When an Employed Agent is deployed, Seer Runtime Service registers as an **observer** with Signal Exchange:

```yaml
# Observer registration
observer:
  type: seer-runtime
  endpoint: https://seer-runtime.olympus.svc/dispatch
  filters:
    workbench: acme-disputes
    scenario: dispute-resolution
    requestTypes:
      - NEW_CASE
      - USER_MESSAGE
      - TASK_COMPLETED
      - CONTEXT_UPDATE
```

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

### 2. Agent-Initiated Context Assembly

If `context.compiled: false`, agent invokes CAE:

```python
# Agent code
from seer_sdk import ContextAssemblyEngine

cae = ContextAssemblyEngine.from_environment()

context = cae.compile(
    request_id=invocation.request.request_id,
    update_id=invocation.update.update_id,
    retrievers=[
        "memory.precedent",
        "memory.case_history",
        "knowledge.policies"
    ],
    token_budget=8000
)
```

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

## Service Mesh Details

The dispatch uses Atlantis/K8s service mesh:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      SERVICE MESH ROUTING                                     │
│                                                                               │
│   ┌─────────────────┐                                                        │
│   │ Seer Runtime    │                                                        │
│   │ Service         │                                                        │
│   │                 │                                                        │
│   │ K8s Service:    │                                                        │
│   │ seer-runtime    │                                                        │
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
- [Employed Agent](./employed-agent.md) — Deployment details
- [Context Assembly](./context-assembly.md) — CAE invocation
- [Runtime & Deployment](../subsystems/runtime-deployment.md) — Seer runtime

---

*Request dispatch bridges Hub's Signal Exchange with Seer's agent runtime, enabling real-time agent invocation.*

