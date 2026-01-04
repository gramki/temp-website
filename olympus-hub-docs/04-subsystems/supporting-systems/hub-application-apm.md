# Hub Application APM

> **Status:** 🔴 Stub — Placeholder for expansion

Hub Application APM provides observability for all Hub Applications through integration with **Olympus Watch**.

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Purpose** | Unified observability for Hub Applications |
| **Platform** | Olympus Watch |
| **Signals** | Logs, Traces, Metrics |
| **Scope** | All Hub Applications across all workbenches |

---

## What is Olympus Watch?

Olympus Watch is a unified, outside-in observability platform for SaaS products. It collects, stores, and analyzes metrics, logs, and traces from various services across the stack.

**Scale:**
- 57.5 billion metrics processed per day
- 533 million traces per day
- 1.5 TB access logs managed per day

**Key Experiences:**
- CS Navigator
- User Diagnostics Navigator
- Zone Navigator
- Signals Navigator

---

## Signals Collected

| Signal | Description | Use Cases |
|--------|-------------|-----------|
| **Logs** | Application logs, debug output, error messages | Debugging, troubleshooting, incident analysis |
| **Traces** | Distributed traces across services | Request flow analysis, latency diagnosis |
| **Metrics** | Application and business metrics | Performance monitoring, alerting, dashboards |

---

## Integration

Hub Applications automatically integrate with Watch through:

1. **Standard instrumentation** — Hub provides base instrumentation
2. **Application-specific telemetry** — Developers add custom metrics/logs as needed
3. **Correlation** — Traces correlated with Request IDs for end-to-end visibility

---

## Distinction from Other Systems

| System | Purpose | What it Captures |
|--------|---------|------------------|
| **Watch (APM)** | Operational telemetry | Logs, traces, metrics |
| **Cipher Audit Service** | Traditional audit | Who did what, when |
| **Enterprise Memory** | Cognitive record | Why, with what evidence, rationale |
| **Operations Data** | Hub state | Request, task, activity lifecycle |

---

## Related Documentation

- [Storage Architecture](../../07-data-architecture/storage-architecture.md) — Where APM fits in data architecture
- [Olympus Watch](https://watch.olympus.tech/) — Watch documentation

---

*TODO: Detailed design — instrumentation patterns, trace context propagation, custom metrics*

