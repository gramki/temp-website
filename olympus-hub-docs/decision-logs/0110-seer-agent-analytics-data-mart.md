# ADR-0110: Seer Agent Analytics as Data Mart (Separate from Runtime Observability)

**Status**: Accepted  
**Date**: 2026-01-13  
**Category**: seer

---

## Context

Seer agents generate significant operational data (metrics, logs, traces, cost, behavior, feedback) that needs to be analyzed for different purposes:

1. **Historical Analysis** — Trend analysis, reporting, compliance, business intelligence
2. **Runtime Observability** — Real-time monitoring, alerting, debugging, incident response

We needed to decide how to organize this data and the systems that consume it:

- Single unified system for both historical and runtime needs?
- Separate systems with different data models and access patterns?
- How to align with Hub's existing analytics and observability patterns?

Key concerns: data volume, query patterns, latency requirements, storage costs, integration with existing Hub infrastructure.

---

## Decision

We separate Agent Analytics (historical data mart) from Observability Extensions to Watch (runtime observability) as **two distinct subsystems**:

### Agent Analytics — Historical Data Mart

**Purpose**: Historical analysis, reporting, compliance, business intelligence

| Aspect | Description |
|--------|-------------|
| **Data Model** | Star schema (facts and dimensions), optimized for analytical queries |
| **Storage** | Olympus LakeStack Pontus (data warehouse) |
| **Data Freshness** | Batch processing (hourly/daily aggregates) |
| **Query Pattern** | Complex analytical queries, aggregations, time-series analysis |
| **Consumers** | Report Center, Analytical Supervisors, SLO Tracking, Business Users |
| **ETSL Integration** | Registers agent operational data as assertions for enterprise semantic consistency |
| **Retention** | Long-term (years) for compliance and trend analysis |

### Observability Extensions to Watch — Runtime Observability

**Purpose**: Real-time monitoring, alerting, debugging, incident response

| Aspect | Description |
|--------|-------------|
| **Data Model** | Time-series metrics, log streams, distributed traces |
| **Storage** | Olympus Watch (Prometheus, log aggregation, Jaeger) |
| **Data Freshness** | Real-time (seconds to minutes) |
| **Query Pattern** | Simple queries, dashboards, alert rules |
| **Consumers** | SRE personas (AI Platform Engineer, LLMOps Engineer, SRE for Agentic Systems, Security Architect) |
| **Extension Model** | Extends Watch with Seer-specific dashboards, alerts, operational tools |
| **Retention** | Short-term (days to weeks) for operational needs |

### Clear Separation of Concerns

| Concern | Agent Analytics | Observability Extensions to Watch |
|---------|----------------|----------------------------------|
| **When** | Historical (past hours/days/months) | Real-time (current/very recent) |
| **What** | Aggregated, dimensional data | Raw metrics, logs, traces |
| **Why** | Business intelligence, compliance, trend analysis | Operational monitoring, incident response |
| **Who** | Business users, analysts, supervisors | SRE engineers, operators |

---

## Consequences

### Positive

1. **Optimized for Use Case** — Each system optimized for its specific query patterns and latency requirements
2. **Cost Efficiency** — Data mart uses cost-effective batch processing; Watch handles high-volume real-time streams
3. **Clear Boundaries** — Developers and operators understand which system to use for which purpose
4. **Hub Pattern Alignment** — Follows Hub Analytics pattern (data mart) and Watch pattern (observability extensions)
5. **Independent Evolution** — Each subsystem can evolve independently based on its specific needs
6. **ETSL Integration** — Agent Analytics integrates with ETSL for enterprise semantic consistency

### Negative

1. **Data Duplication** — Some data exists in both systems (though at different granularities)
2. **Two Systems to Operate** — Requires understanding and operating both subsystems
3. **Data Synchronization** — Need to ensure data flows correctly from Watch to Analytics
4. **Potential Confusion** — Users need to understand when to use which system

### Neutral

1. **Data Flow** — Watch collects raw data; Agent Analytics aggregates and stores for historical analysis
2. **Shared Data Sources** — Both systems consume from same sources (Watch, Sidecar, Model Gateway, Runtime)
3. **Complementary** — Systems complement each other rather than compete

---

## Alternatives Considered

### 1. Single Unified System

Combine historical analytics and runtime observability into one system.

**Rejected because:**
- Different query patterns (analytical vs. time-series) require different optimizations
- Different latency requirements (batch vs. real-time)
- Different retention policies (years vs. days/weeks)
- Would require complex system trying to serve both needs

### 2. Watch-Only Approach

Use only Watch for both historical and runtime needs.

**Rejected because:**
- Watch not optimized for complex analytical queries
- Long-term retention in Watch would be expensive
- No ETSL integration for enterprise semantic consistency
- No structured data mart for business intelligence

### 3. Analytics-Only Approach

Use only Agent Analytics for both historical and runtime needs.

**Rejected because:**
- Batch processing cannot meet real-time monitoring requirements
- Data mart not optimized for operational dashboards and alerts
- Would require building new observability infrastructure

---

## Related

- [Agent Analytics Subsystem](../../olympus-seer-docs/seer-design/subsystems/agent-analytics/README.md)
- [Observability Extensions to Watch Subsystem](../../olympus-seer-docs/seer-design/subsystems/observability-extensions-to-watch/README.md)
- [ADR-0076: Seer Observability via Watch](./0076-seer-observability-watch-based.md) — Runtime observability foundation
- [Hub Analytics](../../04-subsystems/hub-analytics/README.md) — Analogous Hub data mart pattern
- [Olympus LakeStack](../../05-infrastructure/olympus-lakestack.md) — Pontus and Report Center infrastructure
