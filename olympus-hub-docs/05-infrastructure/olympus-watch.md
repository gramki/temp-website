# Olympus Watch — Observability Platform

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Olympus Watch** is the unified observability platform for Olympus Hub, providing collection, storage, and analysis of logs, metrics, and traces across all Hub services and applications.

---

## Purpose in Olympus Hub

Olympus Watch provides:

- **Logs** — Centralized log aggregation and search
- **Metrics** — Time-series metrics collection and alerting
- **Traces** — Distributed tracing for request flows
- **Dashboards** — Pre-built and custom visualization
- **Alerting** — Proactive monitoring and incident detection

---

## Key Components

### Log Aggregation

- **Collection** — Fluent Bit/Fluentd agents on all nodes
- **Storage** — OpenSearch (Europa) for log storage
- **Search** — Full-text search with field-level indexing
- **Retention** — Configurable per log type and tenant

### Metrics Collection

- **Prometheus** — Time-series database for metrics
- **OpenTelemetry Collector** — Metrics pipeline
- **Exporters** — Service-specific metric exporters
- **Recording Rules** — Pre-aggregated metrics for dashboards

### Distributed Tracing

- **Jaeger/Tempo** — Trace storage and query
- **OpenTelemetry SDK** — Application instrumentation
- **Context Propagation** — W3C Trace Context headers
- **Sampling** — Adaptive sampling strategies

---

## Integration with Hub Subsystems

| Subsystem | Observability |
|-----------|---------------|
| **Signal Exchange** | Request routing traces, message latency metrics |
| **Automation Runtimes** | Application execution logs, resource metrics |
| **Hub Applications** | Application-specific logs, traces, custom metrics |
| **I/O Gateways** | Ingress/egress logs, traffic metrics |
| **Heracles Gateway** | Access logs, session metrics, error rates |

---

## Hub Application APM

Hub Applications report observability data through the Hub Application APM subsystem:

- **Structured Logs** — JSON-formatted application logs
- **Spans** — Request-scoped trace spans
- **Custom Metrics** — Application-defined counters, gauges, histograms

See: [Hub Application APM](../04-subsystems/supporting-systems/hub-application-apm.md)

---

## Standard Metrics

### Platform Metrics

| Metric | Description |
|--------|-------------|
| `hub_requests_total` | Total requests processed |
| `hub_request_duration_seconds` | Request latency histogram |
| `hub_active_sessions` | Current active MCP sessions |
| `hub_task_queue_depth` | Pending tasks per queue |

### Application Metrics

| Metric | Description |
|--------|-------------|
| `app_invocations_total` | Application invocation count |
| `app_execution_duration_seconds` | Application execution time |
| `app_errors_total` | Application error count by type |

---

## Standard Log Fields

All Hub logs include:

```json
{
  "timestamp": "2026-01-04T12:00:00Z",
  "level": "INFO",
  "service": "signal-exchange",
  "trace_id": "abc123...",
  "span_id": "def456...",
  "tenant_id": "tenant-001",
  "workbench_id": "wb-disputes",
  "request_id": "req-789",
  "message": "..."
}
```

---

## Alerting Rules

Pre-configured alerts for:

- **Availability** — Service health checks, pod restarts
- **Latency** — P95/P99 thresholds exceeded
- **Errors** — Error rate spikes
- **Capacity** — Resource utilization thresholds
- **SLA** — Task completion time violations

---

## Dashboards

### Platform Dashboards

- Hub System Overview
- Signal Exchange Performance
- Automation Runtime Health
- I/O Gateway Traffic

### Tenant Dashboards

- Workbench Operations
- Application Performance
- Task Processing
- SLA Compliance

---

## Multi-Tenancy

- **Tenant Isolation** — Logs and metrics labeled by tenant
- **Access Control** — Role-based dashboard access
- **Retention Policies** — Per-tenant data retention
- **Cost Attribution** — Usage metrics per tenant

---

## Related Documentation

- [Hub Application APM](../04-subsystems/supporting-systems/hub-application-apm.md) — Application observability integration
- [Europa](./europa-opensearch.md) — Log storage backend
- [Istio Service Mesh](./istio-service-mesh.md) — Service mesh observability

---

*Expand this document with deployment architecture, scaling considerations, and operational procedures.*

