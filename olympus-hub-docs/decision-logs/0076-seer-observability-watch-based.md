# ADR-0076: Seer Agent Observability via Olympus Watch

**Status**: Accepted  
**Date**: 2026-01-08  
**Category**: seer

---

## Context

AI agents require observability for debugging, performance monitoring, and operational health. We needed to decide the observability strategy:
1. Custom observability infrastructure
2. Existing Olympus Watch platform
3. Third-party SaaS (DataDog, New Relic)

Key concerns: metrics, logs, traces, dashboards, alerts, cost.

---

## Decision

Seer leverages **Olympus Watch** as the single observability platform:

### Observability Stack

| Capability | Technology | Collection Method |
|------------|------------|-------------------|
| **Metrics** | Prometheus | Scraped from agent `/metrics` endpoint |
| **Logs** | Watch Log Aggregation | Atlantis logshipper |
| **Traces** | OpenTelemetry + Jaeger | SDK instrumentation |
| **Dashboards** | Watch Dashboards | Pre-built templates |
| **Alerts** | Watch Alerting | Configurable thresholds |

### Seer Observability SDK

- **Languages**: Python, Node.js, Java
- **Type**: Optional but strongly recommended
- **Capabilities**:
  - Auto-instrumentation (LLM calls, tool invocations, memory ops)
  - Manual span/metric APIs
  - Pre-built dashboard/alert templates
  - Trace context propagation

### Standard Metrics

| Metric | Description |
|--------|-------------|
| `seer_agent_request_duration_seconds` | Request processing time |
| `seer_agent_llm_tokens_total` | LLM token usage (prompt + completion) |
| `seer_agent_tool_invocations_total` | Tool call count by tool |
| `seer_agent_memory_operations_total` | Memory read/write count |
| `seer_agent_guardrail_violations_total` | Guardrail trigger count |

### Structured Logging

```json
{
  "timestamp": "ISO8601",
  "level": "INFO|WARN|ERROR",
  "service": "seer-agent",
  "agent_id": "...",
  "request_id": "...",
  "trace_id": "...",
  "message": "...",
  "attributes": {}
}
```

### PII Handling
- Atlantis logshipper applies PII redaction rules
- Sensitive fields masked before storage
- Redaction rules configured at workbench level

---

## Consequences

### Positive
- Unified observability with other Olympus services
- Watch is mature, battle-tested platform
- SDK provides quick path to full observability
- Pre-built dashboards accelerate adoption
- PII redaction built into pipeline

### Negative
- SDK is optional (inconsistent observability if not used)
- OpenTelemetry adds overhead
- Watch costs scale with data volume

### Neutral
- Observability events do NOT go to CAF
- Decision tracing to be part of future "Cognitive Operations Desk"
- Raw Agent must expose `/metrics` and `/health` endpoints

---

## Related

- [Agent Observability Subsystem](../../olympus-seer-docs/seer-design/subsystems/agent-observability.md)
- [Olympus Watch Documentation](https://watch.olympus.tech/)
- [Runtime Deployment](../../olympus-seer-docs/seer-design/subsystems/runtime-deployment.md)

