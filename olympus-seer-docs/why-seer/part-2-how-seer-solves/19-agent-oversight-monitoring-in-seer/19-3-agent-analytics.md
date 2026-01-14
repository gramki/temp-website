# 19.3 Agent Analytics

Agent Analytics provides a data mart for agent operational data, answering questions based on historic health, cost, effectiveness, feedback, and behavior of agents. Unlike Observability Extensions to Watch (Section 19.4) that provide runtime observability, Agent Analytics provides historical data for analytics, reporting, and pattern detection.

Agent Analytics is a data mart (analogous to Hub Analytics) that houses operational data for agents. It uses Pontus infrastructure for data mart construction and storage, leverages ETSL for enterprise-wide semantic consistency, and integrates with LakeStack Report Center for reporting and analytics.

## Purpose of this Subsection

This subsection describes how Seer implements historical analytics through Agent Analytics. It explains the data mart model, distinguishes Agent Analytics from runtime observability, describes LakeStack integration, and explains how Agent Analytics supports Analytical Sentinels and SLO tracking.

## Core Concepts & Definitions

### Data Mart Model

**Agent Analytics is a data mart**, not runtime observability. Data is collected, aggregated, and stored for historical analysis. Runtime observability is provided by Observability Extensions to Watch (separate subsystem, covered in Section 19.4).

The data mart model enables:
*   **Historical analysis**: Analyze trends, patterns, and drift over time
*   **Efficient aggregation**: Pre-aggregated data for fast query performance
*   **Long-term retention**: Data retained for compliance and historical analysis
*   **Enterprise-wide consistency**: ETSL ensures semantic consistency across enterprise

This separation ensures that runtime observability (real-time dashboards, operational tools) and historical analytics (trend analysis, reporting) serve different purposes without confusion.

### LakeStack Integration

Agent Analytics uses Pontus infrastructure (part of Olympus LakeStack) for data mart construction and storage:
*   **Pontus Data Infrastructure**: Provides data storage, processing, and management capabilities
*   **ETSL (Enterprise Transformation and Semantic Layer)**: Ensures enterprise-wide semantic consistency
*   **Report Center Integration**: Integrates with LakeStack Report Center for reporting and analytics

LakeStack integration enables Agent Analytics to leverage enterprise data infrastructure while maintaining consistency with other Olympus products (e.g., Hub Analytics).

### Data Sources

Agent Analytics collects data from multiple sources:
*   **Olympus Watch**: Metrics, logs, traces from Watch infrastructure
*   **Seer Sidecar**: Agent-specific metrics and operational data
*   **Model Gateway**: Model usage, cost, and performance data
*   **Agent Runtime**: Agent execution data, decision records, outcomes

Data from these sources is collected, validated, aggregated, and stored in the Agent Analytics data mart for historical analysis.

### Separation from Observability

Agent Analytics and Observability Extensions to Watch serve different purposes:

| Aspect | Agent Analytics | Observability Extensions to Watch |
|--------|----------------|----------------------------------|
| **Purpose** | Historical data mart for analytics and reporting | Runtime observability for operational monitoring |
| **Time Scale** | Historical (days, weeks, months) | Real-time (seconds, minutes) |
| **Use Case** | Trend analysis, drift detection, reporting | Operational dashboards, alerts, operational tools |
| **Personas** | Analysts, COS, PA/APO | ARE, Cognitive Operations Stewards, SRE |

This clear separation ensures that each subsystem serves its intended purpose without confusion.

## Conceptual Models / Frameworks

### The Data Mart Architecture

Agent Analytics follows a data mart architecture:

```
Data Sources (Watch, Sidecar, Model Gateway, Runtime)
    ↓
Operational Data Service (Collection, Validation, Aggregation)
    ↓
Data Mart Service (ETSL Integration, Data Product Creation)
    ↓
Pontus Data Infrastructure (Storage, Processing)
    ↓
Report Center Integration (Reporting, Analytics)
```

This architecture enables efficient data collection, processing, and analysis while maintaining enterprise-wide consistency.

### The Analytics vs. Observability Model

Agent Analytics and Observability Extensions to Watch operate at different time scales:

*   **Agent Analytics**: Historical data (days, weeks, months) for trend analysis and reporting
*   **Observability Extensions to Watch**: Real-time data (seconds, minutes) for operational monitoring

This separation ensures that each subsystem is optimized for its purpose.

## Systemic and Enterprise Considerations

### Data Retention Requirements

Agent Analytics must retain data for:
*   **Compliance**: Regulatory requirements may require long-term retention (years)
*   **Historical analysis**: Trend analysis and drift detection require historical data
*   **Baseline comparison**: SLO evaluation and drift detection require historical baselines

Data retention policies must balance compliance requirements with storage costs.

### Performance Requirements

Agent Analytics must be performant:
*   **Query performance**: Analytics queries must be fast enough for interactive use
*   **Aggregation efficiency**: Pre-aggregation must be efficient to support fast queries
*   **Scalability**: Data mart must scale to large volumes of operational data

Performance directly impacts analyst productivity and SLO evaluation efficiency.

### Integration with Other Systems

Agent Analytics integrates with:
*   **Analytical Sentinels**: Analytical Sentinels query Agent Analytics data marts for pattern detection
*   **Agent Health Monitor**: SLO Tracking Service uses Agent Analytics data marts for SLO evaluation
*   **LakeStack Report Center**: Report Center provides reporting and analytics interfaces

Integration ensures that Agent Analytics supports other Seer capabilities while providing standalone analytics capabilities.

## Common Misconceptions & Failure Modes

### Misconception: Agent Analytics Replaces Observability

Some organizations assume that Agent Analytics can replace runtime observability. However, Agent Analytics provides historical data for analytics, while Observability Extensions to Watch provide real-time data for operational monitoring. Both are necessary.

**Failure mode**: Organizations rely solely on Agent Analytics, missing real-time operational issues that require immediate attention.

### Misconception: Observability Replaces Agent Analytics

Some organizations assume that runtime observability can replace Agent Analytics. However, runtime observability provides real-time data, while Agent Analytics provides historical data for trend analysis and reporting. Both are necessary.

**Failure mode**: Organizations rely solely on runtime observability, missing historical trends and patterns that require historical analysis.

### Misconception: Data Mart Is Just a Database

Some organizations assume that Agent Analytics is just a database. However, Agent Analytics is a data mart with ETSL integration, data product creation, and Report Center integration that provides enterprise-wide semantic consistency and reporting capabilities.

**Failure mode**: Organizations treat Agent Analytics as a simple database, missing enterprise-wide consistency and reporting capabilities.

## Practical Implications

### Analytics Strategy

Organizations should develop an analytics strategy that:
*   **Defines use cases**: Identify which analytics use cases are important (trend analysis, drift detection, reporting)
*   **Plans data retention**: Plan data retention policies based on compliance and analysis needs
*   **Designs data products**: Design data products for common analytics use cases
*   **Integrates with reporting**: Integrate with Report Center for reporting and analytics interfaces

Analytics strategy directly impacts analyst productivity and decision-making effectiveness.

### Data Product Design

Organizations should design data products that:
*   **Serve common use cases**: Design data products for common analytics use cases (cost analysis, behavior analysis, feedback analysis)
*   **Maintain semantic consistency**: Use ETSL to ensure enterprise-wide semantic consistency
*   **Enable efficient queries**: Pre-aggregate data to enable fast queries
*   **Support reporting**: Design data products to support Report Center reporting

Data product design directly impacts query performance and analyst productivity.

## Cross-References

*   **Section 5.12.1 (Why Oversight Is Needed)**: Establishes the need for historical analytics that Agent Analytics provides
*   **Section 19.1 (Seer Sentinels)**: Describes how Analytical Sentinels use Agent Analytics data marts
*   **Section 19.2 (Agent Health Monitor)**: Describes how SLO Tracking Service uses Agent Analytics data marts
*   **Section 19.4 (Observability Extensions to Watch)**: Distinguishes runtime observability from historical analytics

---

**References:**

*   `seer-design/subsystems/agent-analytics/README.md` — Agent Analytics design
*   `seer-design/subsystems/agent-analytics/SCOPE.md` — Agent Analytics scope
*   `seer-design/subsystems/agent-analytics/operational-data-service.md` — Operational Data Service design
*   `seer-design/subsystems/agent-analytics/data-mart-service.md` — Data Mart Service design
