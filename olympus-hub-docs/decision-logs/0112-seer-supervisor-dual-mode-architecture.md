# ADR-0112: Seer Supervisor Dual-Mode Architecture (Realtime vs Analytical)

**Status**: Accepted  
**Date**: 2026-01-13  
**Category**: seer

---

## Context

Agent Session Sentinel needs to detect various conditions requiring sentinel attention:
- **Real-time conditions** — Stuck agents, immediate policy violations, rapid cost escalation
- **Pattern-based conditions** — Behavioral drift over time, cost trends, historical anomalies

We needed to decide how to structure sentinels to handle these different detection needs:

1. **Single sentinel type** with configurable evaluation modes?
2. **Separate sentinel types** optimized for different evaluation patterns?
3. **Unified policy language** or different languages for different evaluation types?

Key concerns: evaluation latency, data sources, policy complexity, deployment model, operational simplicity.

---

## Decision

We implement a **dual-mode sentinel architecture** with two distinct sentinel types:

### Realtime Supervisor

**Purpose**: Detect conditions requiring immediate attention based on real-time events

| Aspect | Description |
|--------|-------------|
| **Data Source** | Signal Exchange (SX) events (real-time agent session events) |
| **Policy Language** | OPA (Open Policy Agent) Rego policies |
| **Evaluation Trigger** | On SX event arrival (event-driven) |
| **Latency** | Sub-second (real-time) |
| **Use Cases** | Stuck agent detection, immediate policy violations, rapid cost escalation, guardrail violations |
| **Deployment** | Always-on service processing SX events |

### Analytical Supervisor

**Purpose**: Detect patterns and trends requiring attention based on historical data

| Aspect | Description |
|--------|-------------|
| **Data Source** | Agent Analytics data mart (historical and aggregated data) |
| **Policy Language** | Templated SQL queries |
| **Evaluation Trigger** | Scheduled (cron) or on-demand |
| **Latency** | Minutes to hours (batch processing) |
| **Use Cases** | Behavioral drift detection, cost trend analysis, historical anomaly detection, compliance reporting |
| **Deployment** | Scheduled jobs or on-demand execution |

### Unified SentinelSpec CRD

Both sentinel types use the same `SentinelSpec` CRD with a `type` field:

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
spec:
  type: realtime  # or "analytical"
  
  # For Realtime: OPA policy
  policy:
    opa: |
      package seer.sentinel.realtime
      # OPA policy...
  
  # For Analytical: SQL template
  # policy:
  #   sql: |
  #     SELECT ... FROM agent_analytics...
```

### Sentinel Type Selection

| Condition | Sentinel Type | Rationale |
|-----------|----------------|----------|
| **Requires immediate response** | Realtime | Event-driven evaluation for rapid detection |
| **Based on real-time events** | Realtime | SX events provide immediate visibility |
| **Pattern-based detection** | Analytical | Historical data reveals patterns over time |
| **Requires aggregation** | Analytical | Data mart provides efficient aggregation |
| **Complex analytical queries** | Analytical | SQL more powerful for analytical queries |

---

## Consequences

### Positive

1. **Optimized for Use Case** — Each supervisor type optimized for its specific evaluation pattern
2. **Appropriate Latency** — Realtime for immediate needs, Analytical for pattern detection
3. **Right Tool for Job** — OPA for real-time policy evaluation, SQL for analytical queries
4. **Unified API** — Same `SentinelSpec` CRD for both types (simplifies developer experience)
5. **Flexible Deployment** — Realtime always-on, Analytical scheduled/on-demand
6. **Clear Separation** — Developers understand when to use which type

### Negative

1. **Two Sentinel Types** — Developers need to understand both types and when to use each
2. **Different Policy Languages** — OPA Rego vs. SQL (different skills required)
3. **Deployment Complexity** — Two different deployment models to operate
4. **Potential Overlap** — Some conditions could be detected by either type (requires judgment)

### Neutral

1. **Unified Lifecycle** — Both types follow same lifecycle management pattern (Spec Manager, Operators, Directory)
2. **Same Output Model** — Both generate Cronus Observations/Exceptions (via Observation Service)
3. **Complementary** — Types complement each other (realtime for immediate, analytical for patterns)

---

## Alternatives Considered

### 1. Single Sentinel Type with Configurable Evaluation

One sentinel type that can be configured for real-time or analytical evaluation.

**Rejected because:**
- Different data sources (SX events vs. data mart) require different architectures
- Different policy languages (OPA vs. SQL) serve different purposes
- Different latency requirements (real-time vs. batch) need different deployment models
- Would create a complex system trying to serve both needs

### 2. Analytical-Only Approach

Use only analytical sentinels with frequent scheduled execution.

**Rejected because:**
- Cannot meet sub-second latency requirements for immediate conditions
- SX events not available in data mart immediately
- Would require building real-time event processing in analytical framework

### 3. Realtime-Only Approach

Use only real-time sentinels with event history.

**Rejected because:**
- SX events don't provide historical aggregation needed for pattern detection
- Real-time event stream not optimized for complex analytical queries
- Would require maintaining event history in real-time system (expensive)

### 4. Three or More Sentinel Types

Add additional sentinel types (e.g., streaming, batch, hybrid).

**Rejected because:**
- Two types cover the main use cases (immediate vs. pattern-based)
- Additional types would add complexity without clear benefit
- Can evolve to additional types if needed in future

---

## Related

- [Agent Session Sentinel Subsystem](../../olympus-seer-docs/seer-design/subsystems/agent-session-sentinel/README.md)
- [Realtime Sentinel Service](../../olympus-seer-docs/seer-design/subsystems/agent-session-sentinel/realtime-sentinel-service.md) — SX event observation, OPA evaluation
- [Analytical Sentinel Service](../../olympus-seer-docs/seer-design/subsystems/agent-session-sentinel/analytical-sentinel-service.md) — SQL template execution on data mart
- [Sentinel Spec Manager](../../olympus-seer-docs/seer-design/subsystems/agent-session-sentinel/sentinel-spec-manager.md) — Unified SentinelSpec CRD
- [Signal Exchange](../../04-subsystems/signal-exchange/README.md) — SX event source for realtime sentinels
- [Agent Analytics](../../olympus-seer-docs/seer-design/subsystems/agent-analytics/README.md) — Data mart source for analytical sentinels
- [OPA (Open Policy Agent)](https://www.openpolicyagent.org/) — Policy engine for realtime supervisors
