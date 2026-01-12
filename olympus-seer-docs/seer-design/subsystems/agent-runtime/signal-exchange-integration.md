# Signal Exchange Integration

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-12

---

## Overview

Signal Exchange Integration describes how Seer runtime services connect to and receive request updates from Hub's Signal Exchange. The key component is the **sx-observer** service, which acts as a workbench-level observer for Signal Exchange.

---

## SX Observer Service Architecture

### Design Principles

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      SX OBSERVER ARCHITECTURE                                │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    SIGNAL EXCHANGE                                   │   │
│   │                                                                       │   │
│   │   • Does NOT accept subscriptions per scenario or per request        │   │
│   │   • Publishes all request updates to Atropos (workbench topic)       │   │
│   │   • Is UNAWARE of Agent Ingress Gateway                              │   │
│   │   • Only knows about sx-observer (the observer)                      │   │
│   │                                                                       │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  │ Atropos (event bus)                       │
│                                  │ workbench-level topic                     │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    SX-OBSERVER SERVICE                               │   │
│   │                                                                       │   │
│   │   • Workbench-level observer for Signal Exchange                     │   │
│   │   • Receives ALL request updates for the workbench                   │   │
│   │   • Filters relevant updates for relevant agents                     │   │
│   │   • Stores updates (store-and-forward)                               │   │
│   │   • Handles back-pressure                                            │   │
│   │   • Triggers agent scale-up when needed                              │   │
│   │   • Dispatches to Agent Ingress Gateway via Atropos                  │   │
│   │                                                                       │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  │ Atropos (agent-specific topics)           │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    AGENT INGRESS GATEWAY                             │   │
│   │                                                                       │   │
│   │   • Subscribes to agent-specific Atropos topics                      │   │
│   │   • Routes to deployed agent pods                                    │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Architecture Separation

| Component | Knows About | Does NOT Know About |
|-----------|-------------|---------------------|
| **Signal Exchange** | sx-observer | Agent Ingress Gateway |
| **sx-observer** | Signal Exchange, Agent Ingress Gateway | Individual agent pods |
| **Agent Ingress Gateway** | sx-observer, agent pods | Signal Exchange directly |

---

## Signal Exchange Subscription Model

### Workbench-Level Subscription

Signal Exchange does NOT accept subscriptions per scenario or per request:

- **One observer per workbench** — sx-observer subscribes at the workbench level
- **All updates delivered** — All request updates for the workbench flow through sx-observer
- **Filtering at sx-observer** — sx-observer filters and routes to appropriate agents

### Subscription Registration

```yaml
# sx-observer subscription (conceptual)
subscription:
  type: workbench-observer
  workbenchId: acme-disputes
  atroposTopic: sx.workbench.acme-disputes.updates
```

---

## Message Transport: Atropos

All message routing happens through **Atropos** (event bus):

### Signal Exchange → sx-observer

```
Topic: sx.workbench.{workbench_id}.updates

Message:
{
  "request_id": "req-12345",
  "update_type": "REQUEST_UPDATE",
  "scenario": "retail-fraud-triage",
  "payload": { ... }
}
```

### sx-observer → Agent Ingress Gateway

```
Topic: sx.agent.{agent_id}.dispatch

Message:
{
  "request_id": "req-12345",
  "update_type": "REQUEST_UPDATE",
  "payload": { ... },
  "envelope": {
    "source": "sx-observer",
    "workbench_id": "acme-disputes",
    "dispatched_at": "2026-01-12T10:30:00Z"
  }
}
```

---

## Store and Forward Capability

sx-observer stores requests/updates before forwarding to agents:

### Purpose

- **Reliable Delivery** — Updates are not lost if agents are temporarily unavailable
- **Scale-to-Zero Support** — Requests stored until agents scale up
- **Resilience** — Persistent storage ensures durability

### Store-and-Forward Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     STORE AND FORWARD FLOW                                   │
│                                                                              │
│   Signal Exchange                                                            │
│        │                                                                     │
│        │ Atropos                                                             │
│        ▼                                                                     │
│   ┌─────────────────┐                                                       │
│   │   sx-observer   │                                                       │
│   │                 │                                                       │
│   │   1. Receive    │                                                       │
│   │   2. Store      │──────▶ Durable Message Queue                          │
│   │   3. Filter     │                                                       │
│   │   4. Scale-up?  │──────▶ Trigger HPA if agents at zero                  │
│   │   5. Forward    │                                                       │
│   │                 │                                                       │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            │ Atropos (agent-specific topic)                                 │
│            ▼                                                                 │
│   Agent Ingress Gateway                                                      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Implementation Details

> **Note**: Specific implementation details (storage backend, queue type, retention policies) are deferred to detailed implementation stage. Common defaults will be applied.

---

## Back-Pressure Handling

sx-observer implements flow control to prevent overwhelming agents:

### Detection

- **Queue Buildup** — Monitor queue depth for agent-specific topics
- **Slow Processing** — Track dispatch latency and acknowledgment times
- **Agent Health** — Monitor agent health endpoints

### Response

| Condition | Action |
|-----------|--------|
| Queue depth exceeds threshold | Throttle dispatch rate |
| Agents overwhelmed | Pause dispatch temporarily |
| Persistent back-pressure | Signal to Signal Exchange (if supported) |

### Implementation Details

> **Note**: Specific thresholds, throttling algorithms, and configuration are deferred to detailed implementation stage.

---

## Scale-to-Zero and Scale-Up

sx-observer enables agent pods to scale down to zero while ensuring requests are not lost:

### Scale-to-Zero

When no requests are pending:

- Agent pods can scale to zero (no active pods)
- sx-observer continues to subscribe to workbench updates
- Requests are stored in the queue

### Scale-Up Trigger

When requests arrive and agents are at zero:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SCALE-UP FLOW                                            │
│                                                                              │
│   1. Request arrives at sx-observer                                         │
│   2. sx-observer stores request in queue                                    │
│   3. sx-observer checks agent replica count                                 │
│                                                                              │
│   IF replicas == 0:                                                          │
│      4. sx-observer triggers scale-up                                       │
│         • Via Kubernetes HPA custom metrics                                  │
│         • Or via custom scaling mechanism                                    │
│      5. Wait for agent pods to be ready                                     │
│      6. Dispatch stored requests                                            │
│                                                                              │
│   ELSE:                                                                      │
│      4. Dispatch immediately                                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Integration with HPA

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: fraud-analyst-acme-retail
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: fraud-analyst-acme-retail
  minReplicas: 0  # Scale-to-zero enabled
  maxReplicas: 10
  metrics:
    - type: External
      external:
        metric:
          name: sx_observer_pending_requests
          selector:
            matchLabels:
              agent: fraud-analyst-acme-retail
        target:
          type: Value
          value: "1"  # Scale up when pending > 0
```

### Implementation Details

> **Note**: Specific scaling mechanisms, warm-up times, and configuration are deferred to detailed implementation stage.

---

## Request Update Flow

### Complete Flow

```
Signal Exchange
      │
      │ Publishes request update to Atropos
      │ Topic: sx.workbench.{workbench_id}.updates
      ▼
sx-observer (subscribes to Atropos)
      │
      │ 1. Receives update
      │ 2. Stores in durable queue
      │ 3. Filters relevant updates
      │ 4. Checks agent availability
      │ 5. Triggers scale-up if needed
      │ 6. Publishes filtered update to Atropos
      │    Topic: sx.agent.{agent_id}.dispatch
      ▼
Agent Ingress Gateway (subscribes to Atropos)
      │
      │ Routes to deployed agent pod
      ▼
Agent Pod
```

### Filtering Logic

sx-observer filters updates based on:

| Filter Criteria | Source |
|-----------------|--------|
| Which scenarios the updates belong to | Request metadata |
| Which agents are subscribed to those scenarios | EmploymentSpec `workScope.scenarios` |
| Request context and agent assignments | Request metadata, assignment state |

```yaml
# EmploymentSpec defines scenario subscriptions
spec:
  workScope:
    workbench: acme-disputes
    scenarios:
      - retail-fraud-triage
      - wholesale-fraud-review
```

---

## Integration Points

### Signal Exchange

- Workbench-level observer registration
- Signal Exchange only knows about sx-observer

See: `olympus-hub-docs/04-subsystems/signal-exchange/README.md`

### Agent Ingress Gateway

- sx-observer dispatches to Agent Ingress Gateway
- Routing via Atropos agent-specific topics

See: `agent-ingress-gateway-integration.md`

### Kubernetes HPA / Custom Scaling

- sx-observer triggers scale-up when needed
- Integration with Kubernetes autoscaling

### EmploymentSpec

- `workScope.scenarios` defines which scenarios an agent subscribes to
- Used for filtering logic in sx-observer

---

## Related Documentation

- `agent-ingress-gateway-integration.md` - How Agent Ingress Gateway receives and routes requests
- `agent-ingress-gateway/README.md` - Agent Ingress Gateway subsystem
- `olympus-hub-docs/04-subsystems/signal-exchange/README.md` - Signal Exchange design
- `olympus-hub-docs/05-infrastructure/atropos.md` - Atropos event bus

---

*Signal Exchange Integration ensures reliable delivery of request updates from Signal Exchange to Employed Agents through the sx-observer service.*
