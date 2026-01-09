# APM (Application Performance Monitoring)

> **Category:** DevOps and Lifecycle

---

## Overview

**APM (Application Performance Monitoring)** provides observability for Hub Applications and Scenarios through Olympus Watch. Developers configure alerts on logs, metrics, probes, and SLOs using CRDs. APM integrates with the workbench-apm-operator to manage monitoring configurations.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't address observability. APM is an implementation concept for monitoring running automations.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Automation | Monitored application | APM observes applications |
| (not covered) | APM | Observability |

### Gap This Fills

The ontology focuses on operations. APM addresses:
1. **Monitoring**: How are applications observed?
2. **Alerting**: How are issues detected?
3. **SLOs**: How is performance measured?

---

## Definition

**APM** is the observability subsystem that:
- Collects metrics from Hub Applications
- Aggregates logs for analysis
- Runs health probes
- Evaluates SLO compliance
- Triggers alerts via configured channels

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-level; per-application metrics |
| **Lifecycle** | Configured by Developer; runs continuously |
| **Ownership** | Developer configures; Olympus Watch hosts |
| **Multiplicity** | Multiple configurations per workbench |

---

## Structure

### APM CRDs

| CRD | Purpose |
|-----|---------|
| **LogAlertSpec** | Alert on log patterns |
| **MetricAlertSpec** | Alert on metric thresholds |
| **ProbeSpec** | Health check configuration |
| **SLOAlertSpec** | SLO violation alerts |
| **NotificationChannelConfig** | Alert delivery channels |

### LogAlertSpec

```yaml
apiVersion: hub.olympus.io/v1
kind: LogAlertSpec
metadata:
  name: error-rate-alert
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-prod
  
  # Log query
  query:
    source: dispute-handler
    level: ERROR
    pattern: ".*database connection.*"
    
  # Threshold
  threshold:
    count: 10
    window_minutes: 5
    
  # Alert config
  alert:
    severity: critical
    channel_ref: ops-pagerduty
    message: "High database error rate in dispute-handler"
```

### MetricAlertSpec

```yaml
apiVersion: hub.olympus.io/v1
kind: MetricAlertSpec
metadata:
  name: latency-alert
spec:
  workbench_ref: dispute-ops-prod
  
  # Metric
  metric:
    name: request_duration_seconds
    source: dispute-handler
    aggregation: p95
    
  # Threshold
  threshold:
    operator: greater_than
    value: 2.0
    window_minutes: 5
    
  # Alert
  alert:
    severity: warning
    channel_ref: ops-slack
```

### SLOAlertSpec

```yaml
apiVersion: hub.olympus.io/v1
kind: SLOAlertSpec
metadata:
  name: availability-slo
spec:
  workbench_ref: dispute-ops-prod
  
  # SLO definition
  slo:
    name: "Dispute Handler Availability"
    target: 99.9
    window: monthly
    
  # Calculation
  indicator:
    type: availability
    good_events: "response_code < 500"
    total_events: "all requests"
    
  # Burn rate alerts
  burn_rate_alerts:
    - window_hours: 1
      burn_rate: 14.4
      severity: critical
    - window_hours: 6
      burn_rate: 6
      severity: warning
```

---

## Behavior

### How It Works

```
1. Applications emit telemetry
   ├── Logs to Olympus Watch
   ├── Metrics to metric store
   └── Traces to trace store

2. APM evaluates continuously
   ├── Log queries against log stream
   ├── Metric queries against metrics
   └── SLO calculations

3. On threshold breach
   ├── Create alert
   ├── Route to notification channel
   └── Record in alert history

4. Alert delivered
   └── Slack, PagerDuty, email, etc.
```

### Probes

```yaml
apiVersion: hub.olympus.io/v1
kind: ProbeSpec
metadata:
  name: health-probe
spec:
  application_ref: dispute-handler
  
  # Probe configuration
  probes:
    - type: liveness
      path: /health/live
      interval_seconds: 30
      timeout_seconds: 5
      
    - type: readiness
      path: /health/ready
      interval_seconds: 10
      
  # On failure
  on_failure:
    alert_channel: ops-slack
    restart_policy: never  # handled by runtime
```

### Notification Channels

```yaml
apiVersion: hub.olympus.io/v1
kind: NotificationChannelConfig
metadata:
  name: ops-pagerduty
spec:
  type: pagerduty
  
  config:
    integration_key_ref: pagerduty-key
    severity_mapping:
      critical: critical
      warning: warning
      info: info
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Olympus Watch | ↔ integrated | Metrics, logs, traces |
| workbench-apm-operator | ← reconciled by | Operator manages CRDs |
| Notification Channels | → alerts to | Alert delivery |
| Hub Application | ← observes | Collects telemetry |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Workbench-scoped** | APM config per workbench |
| **Olympus Watch integration** | Requires Watch |
| **Channel required** | Alerts need notification channel |
| **Resource limits** | Query complexity limits |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Integrated** | Part of Hub platform |
| ✅ **CRD-based** | GitOps managed |
| ✅ **SLO support** | Burn rate alerting |
| ✅ **Flexible channels** | Multiple notification targets |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Learning curve** | Templates; examples |
| ⚠️ **Alert fatigue** | Tune thresholds |

---

## Examples

### Example 1: Basic Alert Setup

```yaml
# Alert on high error rate
kind: MetricAlertSpec
spec:
  metric:
    name: error_rate
    source: dispute-handler
  threshold:
    operator: greater_than
    value: 0.01
  alert:
    severity: warning
    channel_ref: dev-slack
```

### Example 2: Dashboard Query

```
# Query for dispute processing latency
sum(rate(request_duration_seconds_sum{app="dispute-handler"}[5m])) 
/ 
sum(rate(request_duration_seconds_count{app="dispute-handler"}[5m]))
```

---

## Implementation Notes

### For Developers

- Define SLOs early in development
- Set meaningful alert thresholds
- Use appropriate severity levels
- Include runbook links in alerts

### For Operators

- Review alert volume regularly
- Tune thresholds based on experience
- Ensure notification channels work
- Maintain runbooks

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Hub Application](./hub-application.md) | Applications being monitored |
| [Operator](./operator.md) | workbench-apm-operator |
| [CI Subsystem](./ci-subsystem.md) | Related observability |

---

## References

- [Developer Operators](../../04-subsystems/operators/developer-operators.md#workbench-apm-operator)
- [Olympus Watch](../../04-subsystems/observability/olympus-watch.md)

