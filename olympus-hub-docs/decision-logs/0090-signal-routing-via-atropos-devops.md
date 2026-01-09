# ADR-0090: Signal Routing via Atropos for DevOps

## Status
Accepted

## Date
2026-01-09

## Context

The DevOps Workbench pattern requires routing development lifecycle events from Business Workbench (A) to DevOps Workbench (D). These events come from multiple subsystems:

- **Automation Ideation**: idea.submitted, intent.completed, charter.created
- **CI Subsystem**: test.failed, build.failed
- **Artifact Registry**: promotion.requested, artifact.published
- **Feedback Services**: feedback.promoted, problem.promoted

We needed to decide how to transport these signals reliably across workbenches, especially when A and D are in different subscriptions.

### Options Considered

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A. Direct API Calls** | A calls D's API directly | Simple | No standardization; tight coupling |
| **B. Shared Event Bus** | Central message bus for all workbenches | Decoupled | Single point of failure; complex ACLs |
| **C. Atropos Routing** | Use existing outbound gateway | Standardized; secure; existing infrastructure | Atropos configuration required |

## Decision

We adopt **Option C: Signal Routing via Atropos**, the existing outbound signal gateway.

### Architecture

```
A: Subsystems → DevOps Signal Aggregator → Atropos → HTTPS → D: Heracles → Signal Exchange
```

### Signal Aggregator

A new **DevOps Signal Aggregator** component in A:

1. Subscribes to configured subsystem event streams
2. Applies filter conditions (if configured)
3. Enriches with source workbench context
4. Normalizes to DevOps Event format
5. Routes to Atropos for delivery

### DevOps Event Format

All signals are normalized to a standard format:

```json
{
  "event_type": "devops_event",
  "event": {
    "type": "idea.submitted",
    "timestamp": "2026-01-09T15:30:00Z",
    "payload": { ... }
  },
  "source": {
    "workbench_id": "dispute-ops-dev",
    "subscription_id": "acme-bank",
    "subsystem": "automation-ideation"
  },
  "routing": {
    "via": "atropos",
    "correlation_id": "uuid",
    "binding_id": "dispute-devops-binding"
  }
}
```

### Delivery Guarantees

| Aspect | Guarantee |
|--------|-----------|
| **Semantics** | At-least-once delivery |
| **Retry** | Automatic with exponential backoff |
| **Idempotency** | D must handle duplicates (via event_id) |
| **Ordering** | Best-effort within source; no global order |
| **DLQ** | Failed signals moved to dead letter queue |

### Configuration

Signal routing is configured in `DevOpsWorkbenchBinding.spec.signal_routing`:

```yaml
signal_routing:
  enabled: true
  sources:
    - subsystem: automation-ideation
      events: [idea.submitted, intent.completed, charter.created]
    - subsystem: ci-subsystem
      events: [test.failed, build.failed]
  filters:
    - source: ci-subsystem
      condition: "event.payload.severity == 'critical'"
  rate_limit:
    max_signals_per_minute: 100
  retry:
    max_attempts: 3
```

### Trigger Mapping in D

DevOps Workbench defines triggers that map events to scenarios:

```yaml
triggers:
  - name: idea-triage-trigger
    signal_type: devops_event
    condition: "event.type == 'idea.submitted'"
    scenario: idea-triage
```

## Consequences

### Positive

- **Standardized Transport**: Uses existing Atropos infrastructure
- **Secure**: Credentials managed by binding; authenticated delivery
- **Configurable**: Filter, rate-limit, and batch signals as needed
- **Observable**: Metrics, logging, and DLQ for operational visibility
- **Decoupled**: A and D are loosely coupled via signal contract

### Negative

- **Latency**: Cross-subscription routing adds network latency
- **Complexity**: Signal aggregator is a new component in A
- **Atropos Dependency**: Requires Atropos to be available and configured

### Neutral

- Same pattern can be used for other cross-workbench signal routing scenarios
- Signal catalog is extensible for new subsystem events

## Related

- [Signal Routing via Atropos](../09-composite-systems-and-patterns/devops-workbench/signal-routing-via-atropos.md)
- [Atropos (Outbound Gateway)](../04-subsystems/io-gateways/atropos.md)
- [ADR-0088: DevOps Workbench as Composite Pattern](./0088-devops-workbench-composite-pattern.md)
- [ADR-0089: Bidirectional DevOps Workbench Binding](./0089-bidirectional-devops-workbench-binding.md)

