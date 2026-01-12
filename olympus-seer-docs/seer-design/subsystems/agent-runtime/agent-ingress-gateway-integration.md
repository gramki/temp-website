# Agent Ingress Gateway Integration

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-12

---

## Overview

Agent Ingress Gateway Integration describes how the Agent Ingress Gateway receives requests from sx-observer and routes them to deployed Employed Agents. This document covers request routing, response handling, and integration with the Workbench Data Store.

---

## Request Update Dispatch

### Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    REQUEST UPDATE DISPATCH                                   │
│                                                                              │
│   sx-observer                                                                │
│        │                                                                     │
│        │ Atropos (agent-specific topics)                                     │
│        │ Topic: sx.agent.{agent_id}.dispatch                                 │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                AGENT INGRESS GATEWAY                                 │   │
│   │                                                                       │   │
│   │   • Subscribes to agent-specific Atropos topics                      │   │
│   │   • Routes updates to deployed agent pods                            │   │
│   │   • Load balancing across pod replicas                               │   │
│   │                                                                       │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                KUBERNETES SERVICE                                    │   │
│   │                                                                       │   │
│   │   service: fraud-analyst-acme-retail                                 │   │
│   │   selector: app=fraud-analyst-acme-retail                            │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│   ┌───────────┐  ┌───────────┐  ┌───────────┐                               │
│   │ Agent Pod │  │ Agent Pod │  │ Agent Pod │                               │
│   │    (1)    │  │    (2)    │  │   (N)     │                               │
│   └───────────┘  └───────────┘  └───────────┘                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Points

- **Signal Exchange is unaware of Agent Ingress Gateway** — All routing is via sx-observer
- **Routing based on agent subscriptions** — From EmploymentSpec `workScope.scenarios`
- **Load balancing** — Via Kubernetes Service across agent pod replicas

---

## Request Routing (Initial Requests)

### Flow

1. **sx-observer receives request from Signal Exchange** (via Atropos)
2. **sx-observer filters and routes to Agent Ingress Gateway** (via Atropos)
3. **Agent Ingress Gateway routes to deployed agent pods** (via K8s Service)

### All Communication via sx-observer

```
Signal Exchange → (Atropos) → sx-observer → (Atropos) → Agent Ingress Gateway → Agents
```

**Note**: Signal Exchange is completely unaware of Agent Ingress Gateway.

---

## SX Observer Service Lifecycle

### Registration

During workbench instance setup:

1. sx-observer is deployed for the workbench
2. sx-observer subscribes to workbench-level Atropos topic
3. sx-observer begins receiving request updates

### Updates

When agents are deployed or retired:

1. sx-observer filtering logic is updated
2. Agent-specific Atropos topics are created/removed
3. Agent Ingress Gateway subscriptions are updated

### Cleanup

On workbench retirement:

1. sx-observer stops subscribing to Atropos
2. Pending requests are drained
3. sx-observer resources are cleaned up

---

## Request Dispatch Integration

### Atropos Subscription

Agent Ingress Gateway subscribes to agent-specific Atropos topics:

```
Topic: sx.agent.{agent_id}.dispatch
```

### Request Transformation

| Aspect | Behavior |
|--------|----------|
| **Default** | No transformation — Atropos payload dispatched as-is |
| **Envelope** | Additional envelope details added by sx-observer |
| **Optional** | Any transformation is optional, left to developer requirements |

### Message Format

```json
{
  "request_id": "req-12345",
  "update_type": "REQUEST_UPDATE",
  "payload": {
    "content": "...",
    "context": { ... }
  },
  "envelope": {
    "source": "sx-observer",
    "workbench_id": "acme-disputes",
    "scenario": "retail-fraud-triage",
    "dispatched_at": "2026-01-12T10:30:00Z"
  }
}
```

---

## Response Path

### Direct Request Updates

Agents update requests **directly through agent APIs**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      RESPONSE PATH                                           │
│                                                                              │
│   Agent Pod                                                                  │
│        │                                                                     │
│        │ Direct API call (not via sx-observer)                               │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    AGENT APIs (Hub)                                  │   │
│   │                                                                       │   │
│   │   • Request Update API                                               │   │
│   │   • Decision Submission API                                          │   │
│   │   • Evidence Attachment API                                          │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   NOTE: sx-observer does NOT forward responses from agents to                │
│         Signal Exchange. Agents handle responses directly.                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Points

- **Agents update requests directly** — Not via sx-observer → Signal Exchange
- **Signal Exchange does NOT forward agent responses** — Agents use Hub APIs directly
- **Simplified response path** — Agent SDK provides APIs for request updates

---

## Agent Response Handling - External Resource References

### Overview

Agents can return references to external resources instead of inline content:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 EXTERNAL RESOURCE REFERENCES                                 │
│                                                                              │
│   Agent generates large output (file, image, stream)                        │
│                          │                                                   │
│                          ▼                                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │               WORKBENCH DATA STORE                                   │   │
│   │               (Hub-provided Object and Stream store)                 │   │
│   │                                                                       │   │
│   │   • Object Store (files, images)                                     │   │
│   │   • Stream Store (large text streams)                                │   │
│   │                                                                       │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  │ URI returned to agent                     │
│                                  ▼                                           │
│   Agent includes URI in response                                             │
│   (via direct agent API call)                                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Resource Types

| Type | Example | Store |
|------|---------|-------|
| Files | PDF reports, documents | Object Store |
| Images | Generated charts, screenshots | Object Store |
| Large Text | Analysis reports, logs | Stream Store |

### Response Format with Resource References

```json
{
  "status": "success",
  "updates": [
    {
      "type": "DECISION",
      "content": {
        "summary": "Fraud detected",
        "details_ref": {
          "uri": "wds://acme-disputes/objects/report-12345.pdf",
          "type": "application/pdf",
          "size": 245678,
          "content_type": "application/pdf"
        },
        "evidence_refs": [
          {
            "uri": "wds://acme-disputes/objects/screenshot-001.png",
            "type": "image/png"
          }
        ]
      }
    }
  ]
}
```

---

## Workbench Data Store Integration

### Overview

Hub provides Object and Stream store for workbench resources:

| Store | Purpose | Example Use |
|-------|---------|-------------|
| **Object Store** | File storage | Reports, images, documents |
| **Stream Store** | Streaming data | Large text outputs, logs |

### Access Methods

Agents can access stores through:

1. **As Tools** — Store operations exposed as agent tools
2. **SDK APIs** — Direct API calls via Seer Agent SDK
3. **Service Endpoints** — Direct HTTP endpoints

### Resource Lifecycle

- **Creation** — Agent writes to Workbench Data Store
- **Access** — Resources accessed via URIs
- **Cleanup** — Hub services manage resource cleanup

### References

For detailed information on:
- Retention policies
- Access permissions
- Store configuration

See: Hub documentation for stores and agent memory

---

## Error Handling

### Dead Letter Queue (DLQ)

sx-observer maintains a **Dead Letter Queue in Atropos** for failed dispatches:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ERROR HANDLING                                          │
│                                                                              │
│   sx-observer                                                                │
│        │                                                                     │
│        │ Dispatch attempt                                                    │
│        ▼                                                                     │
│   Agent Ingress Gateway                                                      │
│        │                                                                     │
│        │ Delivery failed?                                                    │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    RETRY LOGIC                                       │   │
│   │                                                                       │   │
│   │   IF retry_count < threshold:                                        │   │
│   │       Retry with backoff                                             │   │
│   │   ELSE:                                                              │   │
│   │       Move to DLQ                                                    │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    DEAD LETTER QUEUE (Atropos)                       │   │
│   │                                                                       │   │
│   │   • Failed messages stored for replay                                │   │
│   │   • Can be manually replayed                                         │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Retry Configuration

| Configuration | Level | Default Source |
|---------------|-------|----------------|
| **Retry thresholds** | Per Employed Agent | EmploymentSpec |
| **Default retries** | Workbench Instance | Workbench config |

### Non-Retriable Failures

Non-retriable failures are:

1. **Logged as Cronus Exception** to the Workbench
2. **Moved to DLQ** for potential manual replay
3. **Alerted** via observability (if configured)

---

## Load Balancing

Load balancing details are not required at this design stage:

- **Default**: Kubernetes Service load balancing
- **Implementation**: Details to be determined during detailed design

---

## Observability

Assume best practices for:

- **Metrics** — Dispatch latency, error rates, queue depth
- **Tracing** — End-to-end request tracing
- **Logging** — Structured logging for debugging

Implementation details to be determined during detailed design.

---

## Related Documentation

- `signal-exchange-integration.md` - How sx-observer receives requests from Signal Exchange
- `agent-ingress-gateway/README.md` - Agent Ingress Gateway subsystem
- `seer-agent-sdk/README.md` - SDK for agent response handling
- `olympus-hub-docs/04-subsystems/workbench-data-store/README.md` - Workbench Data Store

---

*Agent Ingress Gateway Integration ensures reliable routing of requests from sx-observer to Employed Agents and proper handling of agent responses.*
