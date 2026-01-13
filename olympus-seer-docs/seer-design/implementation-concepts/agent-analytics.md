# Agent Analytics

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

Agent Analytics provides a **data mart for agent operational data**, answering questions based on historic health, cost, effectiveness, feedback, and behavior of agents—not runtime observability.

**Key Principle**: Agent Analytics is a **data mart** (analogous to Hub Analytics) that houses operational data for agents. Runtime observability is provided by Observability Extensions to Watch (separate subsystem).

---

## Architecture

Agent Analytics follows the Hub Analytics pattern:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENT ANALYTICS ARCHITECTURE                            │
│                                                                              │
│   Data Sources → Operational Data Service → Data Mart Service → LakeStack   │
│                                                                              │
│   • Watch (metrics, logs)                                                   │
│   • Seer Sidecar (guardrail events)                                         │
│   • Model Gateway (token usage, cost)                                      │
│   • Agent Runtime (deployment events)                                       │
│                                                                              │
│   → Pontus (data mart storage)                                              │
│   → ETSL (enterprise semantic consistency)                                   │
│   → Report Center (reporting integration)                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Data Mart Model** — Agent Analytics is a data mart, not runtime observability
- **LakeStack Integration** — Uses Pontus infrastructure for data mart construction and storage
- **ETSL Integration** — Leverages ETSL for enterprise-wide semantic consistency
- **Separation from Observability** — Clear separation between historical analysis and real-time monitoring
- **Hub Analytics Pattern** — Follows Hub Analytics pattern for consistency across Olympus products

---

## Data Sources

Agent Analytics collects data from multiple sources:

| Data Source | Data Type | Purpose |
|-------------|-----------|---------|
| **Olympus Watch** | Metrics, logs | Operational telemetry |
| **Seer Sidecar** | Guardrail events | Safety and compliance events |
| **Model Gateway** | Token usage, cost | LLM usage and cost tracking |
| **Agent Runtime** | Deployment events | Lifecycle events |

---

## Operational Data Service

Operational Data Service collects and processes data:

| Capability | Description |
|------------|-------------|
| **Data Collection** | Collect data from various sources |
| **Aggregation** | Aggregate data for efficient storage |
| **Validation** | Validate data quality and completeness |
| **Staging** | Stage data for data mart construction |

---

## Data Mart Service

Data Mart Service constructs the data mart:

| Capability | Description |
|------------|-------------|
| **Data Mart Construction** | Build data mart from operational data |
| **ETSL Integration** | Integrate with ETSL for semantic consistency |
| **Data Product Creation** | Create data products for consumption |
| **Pontus Integration** | Store data mart in Pontus infrastructure |

---

## Report Integration Service

Report Integration Service integrates with LakeStack Report Center:

| Capability | Description |
|------------|-------------|
| **Report Center Integration** | Integrate with LakeStack Report Center |
| **Catalog Sync** | Sync data products to report catalog |
| **Access Mapping** | Map access controls for reports |
| **Context Injection** | Inject context for report generation |

---

## Separation from Observability

Clear separation between Agent Analytics and Observability:

| Aspect | Agent Analytics | Observability Extensions to Watch |
|--------|-----------------|-----------------------------------|
| **Purpose** | Historical data mart for analytics and reporting | Runtime observability for AREs and Cognitive Operations Stewards |
| **Data Type** | Aggregated, historical data | Real-time metrics, logs, traces |
| **Retention** | Long-term (months/years) | Short-term (days/weeks) |
| **Use Cases** | Trend analysis, reporting, SLO evaluation | Real-time monitoring, alerting, debugging |

---

## Related

### Agent Analytics Subsystem
- [Agent Analytics README](../subsystems/agent-analytics/README.md) — Subsystem overview
- [Operational Data Service](../subsystems/agent-analytics/operational-data-service.md) — Data collection, aggregation, validation
- [Data Mart Service](../subsystems/agent-analytics/data-mart-service.md) — Data mart construction, ETSL integration
- [Report Integration Service](../subsystems/agent-analytics/report-integration-service.md) — LakeStack Report Center integration

### Related Systems
- [Observability Extensions to Watch](../subsystems/observability-extensions-to-watch/README.md) — Runtime observability (separate subsystem)
- [Seer Sentinels](../subsystems/seer-sentinels/README.md) — Uses Agent Analytics data mart for analytical sentinels
- [Agent Health Monitor](../subsystems/agent-health-monitor/README.md) — Uses Agent Analytics data mart for SLO evaluation
- [Hub Analytics](../../../olympus-hub-docs/04-subsystems/hub-analytics/README.md) — Analogous Hub subsystem
- [Olympus LakeStack](../../../olympus-hub-docs/05-infrastructure/olympus-lakestack.md) — LakeStack Pontus and Report Center infrastructure

---

*For detailed implementation, see [Agent Analytics README](../subsystems/agent-analytics/README.md).*
