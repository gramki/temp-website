# ADR-0018: Dedicated APM Operator for Hub Observability

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub Applications and Scenarios require comprehensive observability including:
- **Log Monitoring**: Pattern-based alerts, error rate tracking, heartbeat detection
- **Metric Monitoring**: Latency, throughput, resource utilization, queue depth
- **Health Probes**: Liveness, readiness, dependency, and synthetic transaction checks
- **SLO Tracking**: Error budgets, burn rates, availability targets

Hub integrates with **Olympus Watch** — the unified observability platform. The question is how to expose observability configuration to developers.

Options included:
1. Embedding APM configuration in Scenario Automation Specifications
2. Using Olympus Watch's native configuration directly
3. Creating a dedicated APM operator with Hub-specific semantics

## Decision

Create a **dedicated workbench-apm-operator** under Developer Operators with the following CRDs:

| CRD | Purpose |
|-----|---------|
| `LogAlertSpec` | Log pattern matching, error rate alerts, absence detection |
| `MetricAlertSpec` | Threshold alerts, composite conditions, time-windowed analysis |
| `ProbeSpec` | Liveness, readiness, dependency, and synthetic probes |
| `SLOAlertSpec` | Service Level Objectives with error budget and burn rate alerts |
| `NotificationChannelConfig` | PagerDuty, Slack, email, webhook configurations |

These CRDs:
- Use Hub semantics (application_ref, scenario_ref, workbench_ref)
- Are reconciled into Olympus Watch native configurations
- Support Hub-specific concepts (task queues, requests, agents)

## Alternatives Considered

### Alternative 1: Embed in Scenario Automation Specification
```yaml
kind: ScenarioAutomationSpec
spec:
  observability:
    alerts:
      - ...
    probes:
      - ...
```

- **Pros**: All-in-one specification, clear association
- **Cons**: Bloated specification, different lifecycle (alerts may change independently), repetitive across scenarios

### Alternative 2: Use Olympus Watch Native Configuration
Developers write Olympus Watch AlertRules, PrometheusRules, etc. directly.

- **Pros**: Standard observability patterns, no abstraction layer
- **Cons**: Loses Hub context, requires Olympus Watch expertise, no Hub-specific validations

### Alternative 3: Console-Only APM Configuration
Configure alerts and SLOs via Hub Console UI only.

- **Pros**: User-friendly, visual feedback
- **Cons**: Not GitOps, not version controlled, manual and error-prone

## Consequences

### Positive
- **Developer Experience**: APM configs use Hub terminology (workbench, scenario, application)
- **GitOps Alignment**: Observability as code, version controlled
- **Hub Integration**: Alerts can reference Hub concepts (task queues, SLA breaches)
- **Abstraction**: Developers don't need to know Olympus Watch internals

### Negative
- **Additional Operator**: One more operator to maintain
- **Translation Layer**: APM specs translated to Olympus Watch configs (potential mismatch)
- **Learning Curve**: Hub-specific APM CRDs to learn

### Neutral
- All APM CRDs reconcile into Olympus Watch via API
- Notification channels shared at workbench or tenant level
- Dashboard generation available for SLOs

## CRD Summary

```
┌────────────────────────────────────────────────────────────────────┐
│                    WORKBENCH APM OPERATOR                           │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │
│  │  LogAlertSpec   │  │ MetricAlertSpec │  │  SLOAlertSpec   │    │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘    │
│           │                    │                    │              │
│           └────────────────────┼────────────────────┘              │
│                                │                                    │
│                                ▼                                    │
│                       ┌─────────────────┐                          │
│                       │  Olympus Watch  │                          │
│                       │  (Observability │                          │
│                       │   Platform)     │                          │
│                       └─────────────────┘                          │
│                                │                                    │
│                                ▼                                    │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Notification Channels: PagerDuty, Slack, Email, Webhook    │   │
│  └─────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────┘
```

## Related Decisions

- [ADR-0014: GitOps-Based Operator Model](./0014-gitops-operator-model.md)
- [ADR-0015: Persona-Based Operator Grouping](./0015-persona-based-operator-grouping.md)

