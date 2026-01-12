# Agent Analytics - Scope and Design Status

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13

---

## Scope

The **Agent Analytics** subsystem provides a data mart for agent operational data. It answers questions based on historic health, cost, effectiveness, feedback, and behavior of agents—not runtime observability.

The subsystem is responsible for:

1. **Operational Data Collection** — Collecting and aggregating agent operational data from multiple sources (Watch, Sidecar, Model Gateway, Runtime)
2. **Data Mart Construction** — Building and maintaining agent data marts using LakeStack Pontus infrastructure
3. **ETSL Integration** — Registering agent operational data as assertions into ETSL
4. **Report Integration** — Integrating with LakeStack Report Center for report serving and embedding

---

## Intended Depth

This design documentation is at **C2 (Container) level** in the C4 architecture model:

| Aspect | Coverage |
|--------|----------|
| **Functional Scope** | Complete — what each component does |
| **Integration Points** | Complete — hand-offs between containers |
| **Conceptual Models** | Complete — illustrated with YAML examples |
| **Operational Flows** | Complete — sequence diagrams for key operations |
| **Data Models** | Conceptual only — no detailed schemas |
| **API Specifications** | Not included — deferred to implementation |

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Operational Data Service](./operational-data-service.md) | Data collection, aggregation, validation, staging | ✅ Complete |
| [Data Mart Service](./data-mart-service.md) | Data mart construction, ETSL integration, data product creation | ✅ Complete |
| [Report Integration Service](./report-integration-service.md) | LakeStack Report Center integration, catalog sync, access mapping, context injection | ✅ Complete |

---

## Coverage Summary

### ✅ Operational Data Service (operational-data-service.md)

- **Data Collection**
  - Olympus Watch (metrics, logs, traces)
  - Seer Sidecar (guardrail, policy, quota metrics)
  - Model Gateway (model usage, cost metrics)
  - Agent Runtime (deployment, health metrics)
  
- **Data Aggregation**
  - Temporal aggregation (raw, minute, hour, day)
  - Dimensional aggregation (agent, workbench, training spec, scenario, model, tool)
  - Metric aggregation (count, sum, average, percentiles, min/max)
  
- **Data Validation**
  - Schema validation, range validation, required fields
  - Timestamp validation, reference validation
  - Data quality metrics tracking
  
- **Data Staging**
  - Staging structure with retention policies
  - Data partitioning strategy
  - Data flow to Data Mart Service

### ✅ Data Mart Service (data-mart-service.md)

- **Data Mart Construction**
  - Data mart structure (facts and dimensions)
  - Data mart build process
  - Data mart refresh strategies (incremental, full, on-demand)
  
- **ETSL Integration**
  - Assertion registration (agent performance, cost, behavior)
  - ETSL integration flow
  - What Data Mart Service does NOT do (semantic modeling, authority modeling)
  
- **Data Product Creation**
  - Data product types (performance, cost, behavior, feedback)
  - Data product structure and publishing
  - Data product serving mechanisms
  
- **Serving Layer Integration**
  - Report Center integration
  - Query API integration
  - Data Product API integration

### ✅ Report Integration Service (report-integration-service.md)

- **Catalog Sync**
  - Report catalog structure
  - Catalog sync process and frequency
  - Report filtering and mapping
  
- **Access Mapping**
  - Role mapping (LakeStack roles to Seer roles)
  - Access control flow and rules
  - Workbench and tenant isolation
  
- **Context Injection**
  - Context parameters (workbench, agent, scenario, time range)
  - Context injection flow
  - Context mapping to report parameters
  
- **Report Embedding**
  - Embedding methods (iframe, widget, data API)
  - Embedding flow and configuration
  - Report distribution across desks

---

## Integration Patterns

| Pattern | Use Case | Components |
|---------|----------|------------|
| **Data Collection** | Continuous data ingestion | Operational Data Service collects from multiple sources |
| **Data Aggregation** | Efficient storage and querying | Operational Data Service aggregates data temporally and dimensionally |
| **Data Mart Construction** | Analytical data marts | Data Mart Service builds data marts using Pontus |
| **ETSL Integration** | Enterprise semantic consistency | Data Mart Service registers assertions into ETSL |
| **Report Serving** | Report access and embedding | Report Integration Service integrates with Report Center |

---

## Implementation Details Deferred

The following implementation details are deferred to the detailed implementation stage:

| Area | Deferred Details |
|------|------------------|
| **Data Models** | Detailed database schemas, data mart table structures |
| **API Specifications** | REST/gRPC endpoints, request/response schemas |
| **Storage** | Database selection, indexing strategies, retention policies |
| **Data Collection** | Specific collection mechanisms, polling intervals, batch sizes |
| **ETSL Schemas** | Detailed ETSL assertion schemas, authority definitions |
| **Report Catalog** | Detailed report catalog schema, embedding protocols |
| **Error Handling** | Specific retry policies, circuit breakers |
| **Observability** | Specific metrics, dashboard layouts |

These will be addressed during implementation with common defaults applied.

---

## Related Subsystems

| Subsystem | Relationship |
|-----------|--------------|
| [Observability Extensions to Watch](../observability-extensions-to-watch/README.md) | Runtime observability (separate subsystem) |
| [Agent Session Supervisor](../agent-session-supervisor/README.md) | Uses Agent Analytics data mart for analytical supervisors |
| [Agent Health Monitor](../agent-health-monitor/README.md) | Uses Agent Analytics data mart for SLO evaluation |
| [Seer Sidecar](../seer-sidecar/metrics-service.md) | Metrics source for Operational Data Service |
| [Model Gateway](../model-gateway/observability.md) | Metrics source for Operational Data Service |

---

## Related Hub Documentation

- `olympus-hub-docs/04-subsystems/hub-analytics/README.md` — Analogous Hub subsystem
- `olympus-hub-docs/05-infrastructure/olympus-lakestack.md` — LakeStack Pontus and Report Center infrastructure
- `olympus-hub-docs/07-data-architecture/storage-architecture.md#etsl-and-pontus-integration-touch-points` — ETSL integration details

---

*This scope document reflects the completed C2-level design of the Agent Analytics subsystem.*
