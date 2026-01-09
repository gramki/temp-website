# Agent Observability

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08

---

## Overview

Agent Observability provides **metrics, logs, traces, dashboards, and alerts** for Seer agents. It is built entirely on **Olympus Watch** — there is no Seer-specific observability layer.

**Key Capabilities:**
- Prometheus metrics with pre-built dashboards
- Structured logging with PII redaction
- Distributed tracing via OpenTelemetry + Jaeger
- Pre-built alert templates for common scenarios
- Multi-language SDK (Python, Node, Java)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     AGENT OBSERVABILITY ARCHITECTURE                         │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                         AGENT PODS                                   │   │
│   │                                                                       │   │
│   │   ┌───────────────────────────────────────────────────────────────┐ │   │
│   │   │                    RAW AGENT                                   │ │   │
│   │   │                                                                │ │   │
│   │   │   ┌─────────────────────────────────────────────────────────┐ │ │   │
│   │   │   │              SEER OBSERVABILITY SDK                      │ │ │   │
│   │   │   │                                                          │ │ │   │
│   │   │   │   • Auto-instrumentation                                 │ │ │   │
│   │   │   │   • Manual instrumentation APIs                          │ │ │   │
│   │   │   │   • Structured logging                                   │ │ │   │
│   │   │   │   • Span creation                                        │ │ │   │
│   │   │   └─────────────────────────────────────────────────────────┘ │ │   │
│   │   │                                                                │ │   │
│   │   │   stdout/stderr ───────────────────────────────────────────┐  │ │   │
│   │   │   :9090/metrics ───────────────────────────────────────┐   │  │ │   │
│   │   │   OTel spans ──────────────────────────────────────┐   │   │  │ │   │
│   │   └────────────────────────────────────────────────────│───│───│──┘ │   │
│   │                                                        │   │   │    │   │
│   │   ┌────────────────────────────────────────────────────│───│───│──┐ │   │
│   │   │                 ISTIO SIDECAR                      │   │   │  │ │   │
│   │   │                                                    │   │   │  │ │   │
│   │   │   • Request metrics (auto)                         │   │   │  │ │   │
│   │   │   • Trace context propagation (auto)               │   │   │  │ │   │
│   │   └────────────────────────────────────────────────────│───│───│──┘ │   │
│   │                                                        │   │   │    │   │
│   └────────────────────────────────────────────────────────│───│───│────┘   │
│                                                            │   │   │        │
│   ┌────────────────────────────────────────────────────────│───│───│────┐   │
│   │                    ATLANTIS INFRASTRUCTURE             │   │   │    │   │
│   │                                                        │   │   │    │   │
│   │   ┌──────────────────┐  ┌──────────────────┐  ┌───────▼───│───│──┐ │   │
│   │   │   Log Shipper    │  │    Prometheus    │  │   OTel    │   │  │ │   │
│   │   │   (DaemonSet)    │  │    (scrapes)     │  │ Collector │   │  │ │   │
│   │   │                  │  │                  │  │           │   │  │ │   │
│   │   │   • PII redaction│  │                  │  │           │   │  │ │   │
│   │   └────────┬─────────┘  └────────┬─────────┘  └─────┬─────│───│──┘ │   │
│   │            │                     │                  │     │   │    │   │
│   └────────────┼─────────────────────┼──────────────────┼─────│───│────┘   │
│                │                     │                  │     │   │        │
│                └─────────────────────┼──────────────────┘     │   │        │
│                                      │                        │   │        │
│                                      ▼                        │   │        │
│   ┌─────────────────────────────────────────────────────◄─────┴───┴────┐   │
│   │                       OLYMPUS WATCH                                 │   │
│   │                                                                     │   │
│   │   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐              │   │
│   │   │   Metrics   │   │    Logs     │   │   Traces    │              │   │
│   │   │ (Prometheus)│   │             │   │  (Jaeger)   │              │   │
│   │   └─────────────┘   └─────────────┘   └─────────────┘              │   │
│   │                                                                     │   │
│   │   ┌─────────────────────────────────────────────────────────────┐  │   │
│   │   │                    DASHBOARDS & ALERTS                       │  │   │
│   │   │   • Agent Health        • Request Latency                    │  │   │
│   │   │   • LLM Cost Tracking   • Error Rates                        │  │   │
│   │   └─────────────────────────────────────────────────────────────┘  │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Observability SDK

### Purpose

The Seer Observability SDK provides:

| Capability | Description |
|------------|-------------|
| **Auto-instrumentation** | Automatic spans for LLM calls, tool invocations, memory operations |
| **Manual instrumentation** | APIs for custom spans, metrics, and logs |
| **Structured logging** | Consistent log format across all agents |
| **Pre-built dashboards** | Standard dashboards in Watch |
| **Alert templates** | Common alert definitions |

### Language Support

| Language | Package | Status |
|----------|---------|--------|
| **Python** | `seer-observability` | ✅ Available |
| **Node.js** | `@seer/observability` | ✅ Available |
| **Java** | `io.olympus.seer:observability` | ✅ Available |

### SDK Requirement

SDK usage is **recommended but not required**:

| Without SDK | With SDK |
|-------------|----------|
| Basic request metrics (from Istio sidecar) | Rich agent-level metrics |
| Platform traces only | Custom spans for reasoning steps |
| Unstructured logs | Structured logs with context |
| Manual dashboard setup | Pre-built dashboards |

---

## SDK Usage

### Python

```python
from seer_observability import SeerObservability, span, log

# Initialize (typically at agent startup)
obs = SeerObservability(
    agent_id="fraud-analyst-acme-retail",
    service_name="fraud-analyst"
)

# Auto-instrumentation for LLM calls
@obs.auto_instrument
def analyze_transaction(transaction_id: str):
    # LLM calls, tool invocations, memory ops automatically traced
    ...

# Manual span creation
with span("custom_analysis", attributes={"transaction_id": tx_id}):
    result = perform_analysis()
    span.set_attribute("risk_score", result.risk_score)

# Structured logging
log.info("Transaction analyzed", 
    transaction_id=tx_id,
    risk_score=result.risk_score,
    decision="approve"
)

# Custom metrics
obs.metrics.counter("transactions_analyzed").inc()
obs.metrics.histogram("risk_score").observe(result.risk_score)
```

### Node.js

```typescript
import { SeerObservability, span, log } from '@seer/observability';

// Initialize
const obs = new SeerObservability({
    agentId: 'fraud-analyst-acme-retail',
    serviceName: 'fraud-analyst'
});

// Auto-instrumentation
const analyzeTransaction = obs.autoInstrument(async (transactionId: string) => {
    // Automatically traced
    ...
});

// Manual span
await span('custom_analysis', { transactionId }, async (s) => {
    const result = await performAnalysis();
    s.setAttribute('riskScore', result.riskScore);
});

// Structured logging
log.info('Transaction analyzed', {
    transactionId,
    riskScore: result.riskScore,
    decision: 'approve'
});
```

### Java

```java
import io.olympus.seer.observability.*;

// Initialize
SeerObservability obs = SeerObservability.builder()
    .agentId("fraud-analyst-acme-retail")
    .serviceName("fraud-analyst")
    .build();

// Auto-instrumentation via annotations
@AutoInstrument
public AnalysisResult analyzeTransaction(String transactionId) {
    // Automatically traced
    ...
}

// Manual span
try (Span span = obs.startSpan("custom_analysis")) {
    span.setAttribute("transactionId", transactionId);
    AnalysisResult result = performAnalysis();
    span.setAttribute("riskScore", result.getRiskScore());
}

// Structured logging
obs.log().info("Transaction analyzed")
    .field("transactionId", transactionId)
    .field("riskScore", result.getRiskScore())
    .field("decision", "approve")
    .emit();
```

---

## Metrics

### Metric Sources

| Source | Metrics Provided | Agent Responsibility |
|--------|------------------|---------------------|
| **Istio Sidecar** | Request count, latency, error rate | None (automatic) |
| **Model Gateway** | Token usage, LLM cost, model latency | None (automatic) |
| **Memory Services** | Store operations, latency | None (automatic) |
| **Tool Gateway** | Tool invocations, latency | None (automatic) |
| **Agent (SDK)** | Custom business metrics, internal operations | Developer implements |

### Standard Agent Metrics

Agents should expose `/metrics` endpoint (Prometheus format):

```prometheus
# Custom business metrics
fraud_transactions_analyzed_total{outcome="approved"} 1234
fraud_transactions_analyzed_total{outcome="declined"} 56
fraud_transactions_analyzed_total{outcome="escalated"} 89

# Risk score distribution
fraud_risk_score_bucket{le="0.3"} 800
fraud_risk_score_bucket{le="0.7"} 1100
fraud_risk_score_bucket{le="1.0"} 1379

# Internal operation metrics
agent_reasoning_steps_total 4567
agent_context_assembly_seconds_bucket{le="0.5"} 1200
```

### Prometheus Scraping

Prometheus (via Atlantis) scrapes agent `/metrics` endpoint:

```yaml
# Pod annotations for Prometheus discovery
metadata:
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "9090"
    prometheus.io/path: "/metrics"
```

---

## Tracing

### Trace Context Propagation

Trace context is propagated via:

1. **OpenTelemetry (W3C Trace Context)** — For explicit propagation
2. **Istio** — Automatic propagation through service mesh

Both methods are used; Istio handles inter-service propagation automatically, while OTel provides in-agent span creation.

### Span Granularity

Agents should emit spans for:

| Operation | Span Name | Attributes |
|-----------|-----------|------------|
| **Request handling** | `agent.request` | `request_id`, `agent_id` |
| **LLM call** | `llm.call` | `model`, `input_tokens`, `output_tokens` |
| **Tool invocation** | `tool.invoke` | `tool_name`, `duration_ms` |
| **Memory operation** | `memory.{operation}` | `store_name`, `operation` |
| **Context assembly** | `context.assemble` | `sources`, `token_count` |
| **Custom reasoning** | `agent.{step_name}` | Custom attributes |

### Trace Example

```
trace_id: abc123
├── agent.request (request_id=req-456)
│   ├── context.assemble (sources=3, tokens=2500)
│   │   ├── memory.search (store=episodic, results=5)
│   │   └── knowledge.retrieve (chunks=3)
│   ├── llm.call (model=gpt-4o, in=500, out=150)
│   ├── tool.invoke (tool=account.query, duration=45ms)
│   ├── llm.call (model=gpt-4o, in=800, out=200)
│   └── agent.decision (outcome=approve, confidence=0.92)
```

### Trace Storage

All traces flow to **Olympus Watch** (which uses Jaeger internally):

```
Agent → OTel Collector (Atlantis) → Watch (Jaeger)
```

---

## Logging

### Log Format

Seer SDK emits structured JSON logs:

```json
{
  "timestamp": "2026-01-08T14:30:00.123Z",
  "level": "INFO",
  "message": "Transaction analyzed",
  "service": "fraud-analyst",
  "agent_id": "fraud-analyst-acme-retail",
  "request_id": "req-456",
  "trace_id": "abc123",
  "span_id": "def789",
  "attributes": {
    "transaction_id": "tx-12345",
    "risk_score": 0.35,
    "decision": "approve"
  }
}
```

### Required Fields

| Field | Description | Source |
|-------|-------------|--------|
| `timestamp` | ISO 8601 timestamp | SDK |
| `level` | Log level (DEBUG, INFO, WARN, ERROR) | Developer |
| `message` | Human-readable message | Developer |
| `service` | Service name | SDK config |
| `agent_id` | Employed Agent ID | SDK config |
| `request_id` | Current request ID | SDK (from context) |
| `trace_id` | Trace ID | SDK (from OTel) |
| `span_id` | Current span ID | SDK (from OTel) |

### Log Shipping

```
Agent stdout → Atlantis Log Shipper (DaemonSet) → Watch
```

### PII Redaction

The Atlantis log shipper performs **automatic PII redaction**:

| Pattern | Redaction |
|---------|-----------|
| Email addresses | `[EMAIL_REDACTED]` |
| Phone numbers | `[PHONE_REDACTED]` |
| SSN/Tax IDs | `[SSN_REDACTED]` |
| Credit card numbers | `[CARD_REDACTED]` |
| Custom patterns | Configurable per workbench |

> **Important**: Agents should avoid logging PII, but the log shipper provides defense-in-depth redaction.

---

## Dashboards

### Pre-built Dashboards

Seer provides standard dashboards in Watch:

| Dashboard | Metrics Shown |
|-----------|---------------|
| **Agent Health** | Pod status, readiness, restarts, resource usage |
| **Request Metrics** | Throughput, latency percentiles, error rates |
| **LLM Usage** | Token consumption, cost by model, latency |
| **Tool Invocations** | Tool usage, success rates, latency |
| **Memory Operations** | Store operations, hit rates, latency |
| **Budget Tracking** | Spend vs. limit, projections, alerts |

### Dashboard Access

Dashboards are available in Watch at:

```
https://watch.olympus.tech/dashboards/seer/agents/{agent_id}
```

---

## Alerts

### Pre-built Alert Templates

Seer provides standard alert definitions:

| Alert | Condition | Severity |
|-------|-----------|----------|
| **Agent Down** | No healthy pods for > 5 minutes | Critical |
| **High Error Rate** | Error rate > 5% for 10 minutes | Warning |
| **Latency Degradation** | P99 latency > 2x baseline for 15 minutes | Warning |
| **Budget Threshold** | Spend > 75% / 90% of limit | Info / Warning |
| **LLM Fallback Active** | Primary model unavailable | Info |
| **Memory Store Errors** | Store error rate > 1% | Warning |

### Alert Configuration

Alerts are configured per workbench in Watch:

```yaml
# Alert configuration (in Watch)
apiVersion: watch.olympus.io/v1
kind: AlertRule
metadata:
  name: fraud-analyst-high-error-rate
spec:
  workbench: acme-disputes
  agents:
    - fraud-analyst-acme-retail
  
  condition:
    metric: seer_agent_errors_total
    threshold: 0.05  # 5%
    duration: 10m
    comparison: greater_than
  
  severity: warning
  
  notifications:
    - channel: slack
      target: "#acme-ops"
    - channel: email
      target: "acme-ops@company.com"
```

---

## Cognitive Operations Desk

For advanced decision tracing and agent reasoning visibility, see the **Cognitive Operations Desk** (documented separately in Hub UX Architecture):

- Agent reasoning step visualization
- Context assembly inspection
- Tool selection analysis
- Decision audit trails

> **Note**: This is a UI tool for operators and stewards, not an SDK component.

---

## CAF Relationship

Agent observability data does **not** flow to CAF (Cognitive Audit Fabric):

| Observability | Destination | Purpose |
|---------------|-------------|---------|
| Metrics | Watch | Operational monitoring |
| Logs | Watch | Debugging, troubleshooting |
| Traces | Watch (Jaeger) | Performance analysis |
| LLM calls | Watch | Cost tracking, debugging |

CAF is for **Enterprise Memory** (decisions, outcomes, learning) — not operational telemetry. See [Hub Enterprise Memory](../../../olympus-hub-docs/04-subsystems/memory-services/enterprise-memory/README.md) for CAF scope.

---

## Configuration Reference

### SDK Configuration

```python
# Python SDK configuration
obs = SeerObservability(
    agent_id="fraud-analyst-acme-retail",  # Required
    service_name="fraud-analyst",           # Required
    
    # Optional
    metrics_port=9090,                      # Default: 9090
    log_level="INFO",                       # Default: INFO
    trace_sample_rate=1.0,                  # Default: 1.0 (100%)
    
    # Auto-instrumentation
    auto_instrument_llm=True,               # Default: True
    auto_instrument_tools=True,             # Default: True
    auto_instrument_memory=True,            # Default: True
)
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTel collector endpoint | Set by Atlantis |
| `SEER_AGENT_ID` | Agent identifier | Required |
| `SEER_SERVICE_NAME` | Service name for traces | Required |
| `SEER_METRICS_PORT` | Prometheus metrics port | `9090` |
| `SEER_LOG_LEVEL` | Minimum log level | `INFO` |

---

## Related Documentation

- [Olympus Watch](https://watch.olympus.tech/) — Observability platform
- [Observability Extensions to Watch](./observability-extensions-to-watch.md) — Platform-level dashboards and tools for Seer SRE personas
- [Runtime Deployment](./runtime-deployment.md) — Pod configuration
- [Model Gateway](./model-gateway.md) — LLM metrics
- [Guardrails](./guardrails.md) — Guardrail metrics
- [Hub Enterprise Memory](../../../olympus-hub-docs/04-subsystems/memory-services/enterprise-memory/README.md) — CAF scope
- [ADR-0076: Observability via Watch](../../../olympus-hub-docs/decision-logs/0076-seer-observability-watch-based.md)

---

*Agent Observability provides comprehensive monitoring through Olympus Watch, with SDK support for custom instrumentation across Python, Node.js, and Java.*
