# Agent Observability

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-11

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

Observability operates at two layers:

1. **Agent-Level Observability** — SDK-based instrumentation within agent pods
2. **Platform-Level Observability** — SRE personas dashboards and operational tools

Both layers feed into Olympus Watch for unified observability.

---

## Key Principles

- **Built on Watch** — No Seer-specific observability infrastructure
- **SDK-Based** — Auto-instrumentation for common operations (LLM calls, tool invocations, memory operations)
- **Structured Logging** — JSON format with required fields (timestamp, level, agent_id, request_id, trace_id)
- **PII Redaction** — Automatic redaction with configurable patterns per workbench
- **Trace Context Propagation** — W3C Trace Context via Istio sidecar
- **Span Granularity** — Fine-grained spans for agent.request, llm.call, tool.invoke, memory.*, context.assemble

---

## Observability vs CAF

| Aspect | Observability (Watch) | CAF (Enterprise Memory) |
|--------|----------------------|------------------------|
| **Purpose** | Operational telemetry | Enterprise memory and audit |
| **Retention** | Short-term (days/weeks) | Long-term (years) |
| **Content** | Metrics, logs, traces | Decisions, outcomes, interventions |
| **Personas** | SRE, Platform Engineers | Business stakeholders, auditors |

---

## Related

- [Seer Agent SDK: Observability APIs (Python)](../subsystems/seer-agent-sdk/python-sdk/observability-apis.md) — Python SDK observability APIs
- [Seer Agent SDK: Observability APIs (Java)](../subsystems/seer-agent-sdk/java-sdk/observability-apis.md) — Java SDK observability APIs
- [Seer Agent SDK: README](../subsystems/seer-agent-sdk/README.md) — SDK overview
- [Agent Observability](../subsystems/agent-observability.md) — Full observability design (platform-level)
- `olympus-hub-docs/05-infrastructure/olympus-watch.md` - Olympus Watch platform
- `olympus-hub-docs/04-subsystems/supporting-systems/hub-application-apm.md` - Hub Application APM

---

*For detailed SDK implementation, see [Seer Agent SDK: Observability APIs](../subsystems/seer-agent-sdk/python-sdk/observability-apis.md) (Python) and [Seer Agent SDK: Observability APIs](../subsystems/seer-agent-sdk/java-sdk/observability-apis.md) (Java).*
