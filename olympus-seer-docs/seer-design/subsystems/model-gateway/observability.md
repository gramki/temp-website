# Observability

> **Status**: 🟢 Complete  
> **Last Updated**: 2026-01-12

---

## Overview

Model Gateway provides comprehensive observability through Prometheus metrics, structured logging, and distributed tracing. All observability data flows to Olympus Watch for visualization and alerting.

---

## Metrics

### Prometheus Metrics

Model Gateway exposes Prometheus-compatible metrics at `/metrics`:

#### Token Usage

```prometheus
# Total tokens used (counter)
seer_model_tokens_total{agent="fraud-analyst", model="gpt-4o", type="input"} 125000
seer_model_tokens_total{agent="fraud-analyst", model="gpt-4o", type="output"} 45000

# Tokens per request (histogram)
seer_model_tokens_bucket{agent="fraud-analyst", model="gpt-4o", type="input", le="100"} 500
seer_model_tokens_bucket{agent="fraud-analyst", model="gpt-4o", type="input", le="500"} 900
seer_model_tokens_bucket{agent="fraud-analyst", model="gpt-4o", type="input", le="1000"} 1100
seer_model_tokens_bucket{agent="fraud-analyst", model="gpt-4o", type="input", le="+Inf"} 1234
```

#### Request Metrics

```prometheus
# Request count by status (counter)
seer_model_requests_total{agent="fraud-analyst", model="gpt-4o", status="success"} 1234
seer_model_requests_total{agent="fraud-analyst", model="gpt-4o", status="error"} 12
seer_model_requests_total{agent="fraud-analyst", model="gpt-4o", status="timeout"} 3

# Request latency (histogram)
seer_model_latency_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="0.5"} 200
seer_model_latency_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="1"} 900
seer_model_latency_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="5"} 1200
seer_model_latency_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="30"} 1230
seer_model_latency_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="+Inf"} 1234

# Time to first token (streaming) (histogram)
seer_model_ttft_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="0.1"} 100
seer_model_ttft_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="0.5"} 800
seer_model_ttft_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="1"} 1100
```

#### Cost Metrics

```prometheus
# Cost in USD (counter)
seer_model_cost_usd{agent="fraud-analyst", model="gpt-4o"} 145.50
seer_model_cost_usd{agent="fraud-analyst", model="gpt-4o-mini"} 12.30

# Budget remaining (gauge)
seer_model_budget_remaining_usd{agent="fraud-analyst"} 354.50
seer_model_budget_remaining_usd{workbench="acme-disputes"} 8750.00

# Budget utilization percentage (gauge)
seer_model_budget_utilization_percent{agent="fraud-analyst"} 29.1
seer_model_budget_utilization_percent{workbench="acme-disputes"} 12.5
```

#### Fallback and Circuit Breaker Metrics

```prometheus
# Fallback events (counter)
seer_model_fallback_total{chain="reasoning", from="gpt-4o", to="claude-3-5-sonnet", reason="429"} 15
seer_model_fallback_total{chain="reasoning", from="gpt-4o", to="claude-3-5-sonnet", reason="timeout"} 3

# Circuit breaker state (gauge: 0=closed, 1=open, 2=half-open)
seer_model_circuit_state{model="gpt-4o"} 0
seer_model_circuit_state{model="claude-3-5-sonnet"} 1

# Circuit breaker events (counter)
seer_model_circuit_opened_total{model="gpt-4o"} 2
seer_model_circuit_closed_total{model="gpt-4o"} 2
```

#### Policy Metrics

```prometheus
# Policy evaluation count (counter)
seer_policy_evaluations_total{policy="model-gateway", result="allow"} 12345
seer_policy_evaluations_total{policy="model-gateway", result="deny"} 123

# Policy evaluation latency (histogram)
seer_policy_evaluation_duration_seconds_bucket{policy="model-gateway", le="0.001"} 10000
seer_policy_evaluation_duration_seconds_bucket{policy="model-gateway", le="0.01"} 12000

# Violation breakdown (counter)
seer_policy_violations_total{policy="access"} 50
seer_policy_violations_total{policy="budget"} 30
seer_policy_violations_total{policy="rate_limit"} 25
```

### Metric Labels

| Label | Description | Example |
|-------|-------------|---------|
| `agent` | Employed Agent ID | `fraud-analyst-acme-retail` |
| `model` | Model name | `gpt-4o` |
| `workbench` | Workbench ID | `acme-disputes` |
| `subscription` | Subscription ID | `acme-seer-subscription` |
| `status` | Request status | `success`, `error`, `timeout` |
| `type` | Token type | `input`, `output` |

---

## Watch Integration

### Metrics Flow

```
Model Gateway → Prometheus Exporter → Watch Scraper → Watch Metrics Store
                                                            ↓
                                                   Dashboards & Alerts
```

### Dashboards

Olympus Watch provides pre-built dashboards:

| Dashboard | Metrics | Purpose |
|-----------|---------|---------|
| **LLM Overview** | Requests, tokens, latency | Platform-wide view |
| **Agent Performance** | Per-agent metrics | Agent-level monitoring |
| **Cost Tracking** | Budget usage, cost by model | Financial governance |
| **Model Comparison** | Latency, error rates by model | Model selection |
| **Fallback Analysis** | Fallback events, circuit breakers | Reliability |

### Alerts

| Alert | Condition | Severity |
|-------|-----------|----------|
| **High Error Rate** | Error rate > 5% for 5 min | Warning |
| **Budget Threshold** | Usage > 75% of limit | Warning |
| **Budget Exhausted** | Usage > 95% of limit | Critical |
| **High Latency** | P95 latency > 30s for 5 min | Warning |
| **Circuit Breaker Open** | Any circuit open | Warning |
| **All Models Failing** | All models in chain failing | Critical |

---

## Logging

### Log Format

LLM calls are logged as **operational logs** (not CAF audit logs):

```json
{
  "timestamp": "2026-01-12T14:30:00.123Z",
  "level": "INFO",
  "service": "model-gateway",
  "event": "llm_request",
  
  "request": {
    "request_id": "req-12345",
    "agent_id": "fraud-analyst-acme-retail",
    "virtual_key": "vk_acme_fraud_analyst_retail_001",
    "model": "gpt-4o",
    "workbench": "acme-disputes"
  },
  
  "response": {
    "status": "success",
    "input_tokens": 500,
    "output_tokens": 150,
    "latency_ms": 1250,
    "cost_usd": 0.0195
  },
  
  "trace": {
    "trace_id": "abc123def456",
    "span_id": "span-789"
  }
}
```

### Log Levels

| Level | Usage |
|-------|-------|
| **DEBUG** | Detailed request/response (disabled in prod) |
| **INFO** | Normal operations, request completion |
| **WARN** | Fallback triggered, budget threshold |
| **ERROR** | Request failure, provider errors |

### Log Retention

| Log Type | Retention | Storage |
|----------|-----------|---------|
| **Access Logs** | 30 days | Watch Log Store |
| **Error Logs** | 90 days | Watch Log Store |
| **Audit Logs** | N/A | Not applicable (LLM calls not audited) |

> **Note**: LLM calls are **not** logged to CAF. Request/response content is not stored for audit.

---

## Cost Tracking and Attribution

### Cost Attribution

All costs are attributed to:

| Level | Attribution | Purpose |
|-------|-------------|---------|
| **Agent** | Via virtual key | Individual accountability |
| **Workbench** | Via agent's workbench | Aggregate cost control |
| **Subscription** | Via workbench's subscription | Billing |

### Cost Calculation

```python
def calculate_cost(response, model_pricing):
    """Calculate cost for an LLM response."""
    input_cost = response.input_tokens * model_pricing.input_per_million / 1_000_000
    output_cost = response.output_tokens * model_pricing.output_per_million / 1_000_000
    return input_cost + output_cost


# Pricing table (updated periodically)
MODEL_PRICING = {
    "gpt-4o": {"input_per_million": 2.50, "output_per_million": 10.00},
    "gpt-4o-mini": {"input_per_million": 0.15, "output_per_million": 0.60},
    "claude-3-5-sonnet": {"input_per_million": 3.00, "output_per_million": 15.00},
    "claude-3-5-haiku": {"input_per_million": 0.25, "output_per_million": 1.25},
}
```

### Cost Reports

Watch generates cost reports:

| Report | Frequency | Content |
|--------|-----------|---------|
| **Daily Summary** | Daily | Usage by agent, model, cost |
| **Weekly Trend** | Weekly | Cost trends, anomalies |
| **Monthly Invoice** | Monthly | Billing-ready report |

---

## Tracing

### Distributed Tracing

Model Gateway participates in distributed tracing via Istio and Jaeger:

```
Agent Pod → Model Gateway → LLM Provider
    ↓           ↓              ↓
 span-1      span-2         span-3
    └──────────┴──────────────┘
              trace-id
```

### Trace Context

| Header | Purpose |
|--------|---------|
| `x-request-id` | Request correlation |
| `traceparent` | W3C trace context |
| `x-b3-traceid` | Jaeger/Zipkin trace ID |
| `x-b3-spanid` | Jaeger/Zipkin span ID |

### Span Attributes

Model Gateway spans include:

```json
{
  "span.kind": "client",
  "llm.model": "gpt-4o",
  "llm.provider": "openai",
  "llm.input_tokens": 500,
  "llm.output_tokens": 150,
  "llm.latency_ms": 1250,
  "seer.agent_id": "fraud-analyst-acme-retail",
  "seer.virtual_key": "vk_acme_fraud_analyst_retail_001"
}
```

---

## Configuration

### Observability Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: model-gateway-observability
  namespace: seer-system
data:
  config.yaml: |
    metrics:
      enabled: true
      port: 9090
      path: /metrics
      
      # Custom labels
      labels:
        environment: production
        cluster: us-west-2
    
    logging:
      level: INFO
      format: json
      
      # Sensitive field redaction
      redact:
        - request.messages  # Don't log message content
        - response.content  # Don't log response content
    
    tracing:
      enabled: true
      samplingRate: 0.1  # 10% sampling in production
      
      # Propagation
      propagators:
        - w3c
        - b3
```

---

## Related Documentation

- [Architecture](./architecture.md) — Model Gateway architecture
- [Governance](./governance.md) — Budget and cost controls
- [Olympus Watch](https://watch.olympus.tech/) — Observability platform

---

*Observability provides comprehensive monitoring, logging, and tracing for Model Gateway operations.*
