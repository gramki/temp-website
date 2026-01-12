# Metrics Service

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12  
> **Design Level**: C2 (Container)

---

## Overview

The Metrics Service collects and exports runtime metrics from the sidecar for observability. It instruments inbound and outbound traffic, guardrail execution, policy enforcement, and quota tracking.

**Key Principle**: The sidecar provides visibility into traffic it can intercept; compute metrics (CPU, memory, tokens) are collected by external systems.

---

## Metrics Collection Scope

### What Sidecar Can Collect

| Metric Category | Metrics |
|-----------------|---------|
| ✅ **Inbound Request Metrics** | Latency, throughput, error rates, request size |
| ✅ **Outbound Call Metrics** | Latency, throughput, error rates, call size |
| ✅ **Guardrail Metrics** | Execution time, response rates (Allow/Alert/Deny) |
| ✅ **Authority Enforcement Metrics** | Ceiling checks, violations |
| ✅ **Policy Enforcement Metrics** | Evaluation time, violation rates |
| ✅ **Resource Quota Metrics** | Request counts, call counts, rate limits |
| ✅ **Fair Usage Budget Metrics** | Consumption, exhaustion events |

### What Sidecar Cannot Collect

| Metric Category | Collected By |
|-----------------|--------------|
| ❌ CPU/memory usage | Kubernetes |
| ⚠️ Token consumption | Model Gateway (sidecar sees API calls) |
| ⚠️ Tool invocation details | Tool Gateway (sidecar sees calls) |

---

## Metrics Types

### Request Metrics

```yaml
# Inbound request metrics
seer_request_duration_seconds:
  type: histogram
  description: "Duration of inbound dispatch requests"
  labels: [agent_id, scenario_id]
  buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]

seer_request_total:
  type: counter
  description: "Total inbound dispatch requests"
  labels: [agent_id, scenario_id, status]

seer_request_size_bytes:
  type: histogram
  description: "Size of inbound dispatch requests"
  labels: [agent_id]
  buckets: [1024, 10240, 102400, 1048576]
```

### Outbound Call Metrics

```yaml
# Outbound Hub API call metrics
seer_outbound_call_duration_seconds:
  type: histogram
  description: "Duration of outbound Hub API calls"
  labels: [agent_id, api_pattern]
  buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5]

seer_outbound_call_total:
  type: counter
  description: "Total outbound Hub API calls"
  labels: [agent_id, api_pattern, status]

seer_outbound_call_size_bytes:
  type: histogram
  description: "Size of outbound Hub API calls"
  labels: [agent_id, api_pattern]
```

### Guardrail Metrics

```yaml
# Guardrail execution metrics
seer_guardrail_duration_seconds:
  type: histogram
  description: "Guardrail execution duration"
  labels: [guardrail, phase, api_pattern]
  buckets: [0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5]

seer_guardrail_result_total:
  type: counter
  description: "Guardrail results by response type"
  labels: [guardrail, phase, response]  # response: allow, alert, deny

seer_guardrail_error_total:
  type: counter
  description: "Guardrail errors"
  labels: [guardrail, error_code]

seer_guardrail_timeout_total:
  type: counter
  description: "Guardrail timeouts"
  labels: [guardrail, phase]
```

### Authority Enforcement Metrics

```yaml
# Authority ceiling metrics
seer_ceiling_evaluation_total:
  type: counter
  description: "Total ceiling evaluations"
  labels: [ceiling_type, decision]

seer_ceiling_violation_total:
  type: counter
  description: "Ceiling violations"
  labels: [ceiling_type, ceiling_name]

seer_delegation_chain_update_total:
  type: counter
  description: "Delegation chain updates"
  labels: [agent_id]
```

### Policy Enforcement Metrics

```yaml
# Policy evaluation metrics
seer_policy_evaluation_total:
  type: counter
  description: "Total policy evaluations"
  labels: [policy_id, decision]

seer_policy_evaluation_duration_seconds:
  type: histogram
  description: "Policy evaluation duration"
  labels: [policy_id]
  buckets: [0.001, 0.005, 0.01, 0.025, 0.05, 0.1]

seer_policy_violation_total:
  type: counter
  description: "Policy violations"
  labels: [policy_id, reason_code]
```

### Quota Metrics

```yaml
# Resource quota metrics
seer_quota_utilization_ratio:
  type: gauge
  description: "Current quota utilization (0-1)"
  labels: [quota_type]

seer_quota_exhaustion_total:
  type: counter
  description: "Quota exhaustion events"
  labels: [quota_type]

seer_rate_limit_remaining:
  type: gauge
  description: "Remaining rate limit in current window"
  labels: [endpoint_pattern]

# Fair usage budget metrics
seer_fair_usage_consumption:
  type: gauge
  description: "Current fair usage consumption"
  labels: [dimension, period]

seer_fair_usage_exhaustion_total:
  type: counter
  description: "Fair usage budget exhaustion events"
  labels: [dimension, action]
```

---

## Metrics Instrumentation

### Request/Response Instrumentation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INSTRUMENTATION FLOW                                      │
│                                                                              │
│   Inbound Request                                                           │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────┐                                                       │
│   │ Start Timer     │ ← Request received timestamp                          │
│   │ Record Size     │ ← Request size in bytes                               │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ Guardrail       │ ← Guardrail execution time                            │
│   │ Instrumentation │ ← Guardrail response (allow/alert/deny)               │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ Agent Invoke    │ ← Agent processing time                               │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ Outbound Calls  │ ← Per-call duration, size, status                     │
│   │ Instrumentation │ ← API pattern labels                                  │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ End Timer       │ ← Total request duration                              │
│   │ Record Status   │ ← Success/error status                                │
│   └─────────────────┘                                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Metrics Aggregation

| Aggregation Level | Scope |
|-------------------|-------|
| **Per-Agent** | Individual agent metrics |
| **Per-Workbench** | Aggregated across agents in workbench |
| **Per-Scenario** | Aggregated by scenario type |
| **Per-Tenant** | Tenant-level aggregations |

---

## Metrics Export

### Prometheus Format

Metrics are exported in Prometheus format via `/metrics` endpoint:

```
# HELP seer_request_duration_seconds Duration of inbound dispatch requests
# TYPE seer_request_duration_seconds histogram
seer_request_duration_seconds_bucket{agent_id="fraud-analyst-001",scenario_id="fraud-investigation",le="0.1"} 150
seer_request_duration_seconds_bucket{agent_id="fraud-analyst-001",scenario_id="fraud-investigation",le="0.25"} 200
seer_request_duration_seconds_sum{agent_id="fraud-analyst-001",scenario_id="fraud-investigation"} 45.5
seer_request_duration_seconds_count{agent_id="fraud-analyst-001",scenario_id="fraud-investigation"} 250

# HELP seer_guardrail_result_total Guardrail results by response type
# TYPE seer_guardrail_result_total counter
seer_guardrail_result_total{guardrail="pii-detector",phase="inbound",response="allow"} 240
seer_guardrail_result_total{guardrail="pii-detector",phase="inbound",response="deny"} 10
```

### Metrics Endpoint

```yaml
# Metrics endpoint configuration
metrics:
  port: 9090
  path: /metrics
  labels:
    service: seer-sidecar
    version: v1.0.0
```

---

## Integration Points

### Agent Observability Service
- Metrics export → Metrics collection and storage
- Prometheus scraping → Centralized metrics

### Agent Health Monitor
- Metrics data → Health status evaluation
- Error rates → Health alerts

### Agent Analytics
- Metrics data → Analytics and reporting
- Trend analysis → Capacity planning

### Prometheus
- Metrics endpoint → Metrics scraping
- Service discovery → Auto-discovery

### External Systems
- Kubernetes: CPU/memory metrics collected separately
- Model Gateway: Token consumption metrics collected separately
- Tool Gateway: Tool invocation metrics collected separately

---

## Observability Configuration

```yaml
# Sidecar metrics configuration
spec:
  metrics:
    enabled: true
    port: 9090
    path: /metrics
    
    # Metric filtering
    include:
      - "seer_request_*"
      - "seer_outbound_*"
      - "seer_guardrail_*"
      - "seer_policy_*"
      - "seer_quota_*"
      - "seer_fair_usage_*"
    
    # Label cardinality limits
    labels:
      maxCardinality: 1000
      
    # Histogram buckets
    histograms:
      defaultBuckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
```

---

## Related Documentation

- [Agent Observability](../agent-observability.md) — Centralized observability
- [Agent Health Monitor](../agent-health-monitor/README.md) — Health monitoring
- [Guardrail Service](./guardrail-service.md) — Guardrail metrics
- [Resource Quota Service](./resource-quota-service.md) — Quota metrics

---

*Metrics Service collects and exports runtime metrics from the sidecar, providing visibility into request traffic, guardrail execution, policy enforcement, and quota tracking in Prometheus format.*
