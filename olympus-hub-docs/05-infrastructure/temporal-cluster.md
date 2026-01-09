# Temporal — Durable Workflow Engine

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Temporal** is the durable workflow execution engine that powers the ChronoShift Automation Runtime in Olympus Hub, providing fault-tolerant, long-running workflow orchestration.

---

## Purpose in Olympus Hub

Temporal provides:

- **Durable Execution** — Workflows survive process and infrastructure failures
- **Long-Running Operations** — Support for multi-day/week workflows
- **State Management** — Automatic workflow state persistence
- **Retry Logic** — Built-in retry policies with exponential backoff
- **Visibility** — Workflow history and state inspection

---

## Integration with ChronoShift

ChronoShift is Hub's Temporal-based Automation Runtime:

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Signal Exchange  │────►│   ChronoShift    │────►│    Temporal      │
│                  │     │    Runtime       │     │    Cluster       │
└──────────────────┘     └──────────────────┘     └──────────────────┘
                                  │
                                  ▼
                         Durable Workflow
                           Application
```

---

## Hub Application Types

ChronoShift hosts **Durable Workflow Applications**:

| Application Type | Use Case |
|------------------|----------|
| **Case Workflows** | Long-running case management with human tasks |
| **Saga Workflows** | Distributed transactions with compensation |
| **Scheduled Workflows** | Recurring operations with state |
| **Integration Workflows** | Multi-system orchestration |

---

## Cluster Architecture

```
┌───────────────────────────────────────────────────────────┐
│                    Temporal Cluster                        │
│                                                            │
│  ┌────────────┐   ┌────────────┐   ┌────────────┐        │
│  │  Frontend  │   │  Frontend  │   │  Frontend  │        │
│  │  Service   │   │  Service   │   │  Service   │        │
│  └────────────┘   └────────────┘   └────────────┘        │
│                                                            │
│  ┌────────────┐   ┌────────────┐   ┌────────────┐        │
│  │  History   │   │  History   │   │  History   │        │
│  │  Service   │   │  Service   │   │  Service   │        │
│  └────────────┘   └────────────┘   └────────────┘        │
│                                                            │
│  ┌────────────┐   ┌────────────┐                          │
│  │  Matching  │   │  Matching  │                          │
│  │  Service   │   │  Service   │                          │
│  └────────────┘   └────────────┘                          │
│                                                            │
│  ┌────────────────────────────────────────────┐          │
│  │              Persistence Layer              │          │
│  │      (PostgreSQL / Cassandra / MySQL)       │          │
│  └────────────────────────────────────────────┘          │
└───────────────────────────────────────────────────────────┘
```

---

## Namespace Strategy

Each Hub tenant gets isolated Temporal namespaces:

```
olympus-hub-<tenant-id>-<workbench-id>
```

Example:
- `olympus-hub-acme-disputes`
- `olympus-hub-acme-onboarding`

---

## Workflow Patterns

### Request-Workflow Binding

Each Hub Request can be bound to a Temporal workflow:

```go
// Workflow started by ChronoShift runtime
func DisputeResolutionWorkflow(ctx workflow.Context, request HubRequest) error {
    // Long-running dispute handling
    // Human tasks via Hub Task Management
    // Decisions recorded via Hub Memory Services
}
```

### Human Task Integration

Temporal workflows integrate with Hub Task Management:

```go
// Wait for human task completion
taskResult := workflow.ExecuteActivity(ctx, WaitForHubTask, taskConfig)
```

### Signal Handling

Workflows receive Hub signals as Temporal signals:

```go
// Handle async updates from Signal Exchange
workflow.GetSignalChannel(ctx, "hub-update").Receive(ctx, &update)
```

---

## Retry Policies

Default retry configuration for Hub workflows:

```go
retryPolicy := &temporal.RetryPolicy{
    InitialInterval:    time.Second,
    BackoffCoefficient: 2.0,
    MaximumInterval:    time.Hour,
    MaximumAttempts:    0, // Unlimited
}
```

---

## Visibility

Temporal provides workflow visibility:

- **List Workflows** — Query by status, type, start time
- **Workflow History** — Complete event history
- **Search Attributes** — Custom indexed attributes

Hub-specific search attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `TenantId` | Keyword | Tenant identifier |
| `WorkbenchId` | Keyword | Workbench identifier |
| `RequestId` | Keyword | Hub Request ID |
| `ScenarioName` | Keyword | Scenario name |

---

## Security

- **Namespace Isolation** — Tenant workloads isolated by namespace
- **mTLS** — Encrypted cluster communication
- **Authorization** — Per-namespace access control
- **Audit Logging** — Workflow operations logged

---

## Monitoring

Temporal metrics exported to Olympus Watch:

- `temporal_workflow_started_total`
- `temporal_workflow_completed_total`
- `temporal_workflow_failed_total`
- `temporal_activity_execution_latency`
- `temporal_task_queue_depth`

---

## Related Documentation

- [ChronoShift Temporal](../04-subsystems/automation-runtimes/chronoshift-temporal.md) — Automation Runtime
- [Request Lifecycle](../04-subsystems/request-management/request-lifecycle.md) — Request states
- [Task Management](../04-subsystems/task-management/README.md) — Human task integration

---

## References

- [Temporal Documentation](https://docs.temporal.io/)
- [Temporal Go SDK](https://docs.temporal.io/dev-guide/go)

---

*Expand this document with deployment guide, worker configuration, and operational procedures.*

