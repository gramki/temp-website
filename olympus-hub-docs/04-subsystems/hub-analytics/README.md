# Hub Analytics

> **Status:** 🔴 Stub — Placeholder for expansion

The **Hub Analytics** subsystem provides operational data, aggregations, and analytics for Maintainers and Supervisors. It also integrates with Olympus LakeStack Report Center to enable reports in Hub's Report Consoles.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Operational analytics + Report Center integration |
| **Consumers** | Agent Desk, Supervisor Desk, Steward Desk |
| **Dependency** | [Olympus LakeStack](../../05-infrastructure/olympus-lakestack.md) |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           HUB ANALYTICS                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  REPORT SOURCES                                                              │
│  ┌─────────────────────────┐     ┌─────────────────────────────────────┐   │
│  │  Hub Operational Data   │     │  Business Domain Reports            │   │
│  │  • Request metrics      │     │  • Enterprise machine reports       │   │
│  │  • Task metrics         │     │  • Domain-specific analytics        │   │
│  │  • Queue metrics        │     │  • External system reports          │   │
│  │  • Application health   │     │  (Published via LakeStack)          │   │
│  └───────────┬─────────────┘     └──────────────────┬──────────────────┘   │
│              │                                       │                      │
│              └───────────────────┬───────────────────┘                      │
│                                  │                                          │
│                                  ▼                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                  OLYMPUS LAKESTACK                                   │   │
│  │  ┌─────────────────────────────────────────────────────────────┐    │   │
│  │  │  Report Center                                               │    │   │
│  │  │  • Report Builder (Build reports)                            │    │   │
│  │  │  • Report Publisher (Publish to catalogs)                    │    │   │
│  │  │  • Report Dispatcher (Schedule, trigger, deliver)           │    │   │
│  │  └─────────────────────────────────────────────────────────────┘    │   │
│  └───────────────────────────────────┬─────────────────────────────────┘   │
│                                      │                                      │
│                                      ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │               HUB ANALYTICS INTEGRATION LAYER                        │   │
│  │                                                                      │   │
│  │  • Catalog Integration — Maps LakeStack reports to Hub consoles     │   │
│  │  • Access Control — Applies Hub's RBAC to report access             │   │
│  │  • Context Binding — Injects workbench/request context              │   │
│  │  • Embedding — Renders reports in Hub console frames                │   │
│  └───────────────────────────────────┬─────────────────────────────────┘   │
│                                      │                                      │
│         ┌────────────────────────────┼────────────────────────────┐        │
│         ▼                            ▼                            ▼        │
│  ┌─────────────┐            ┌─────────────┐            ┌─────────────┐    │
│  │  Agent Desk │            │ Supervisor  │            │   Steward   │    │
│  │   Reports   │            │    Desk     │            │    Desk     │    │
│  │   Console   │            │   Reports   │            │   Reports   │    │
│  └─────────────┘            └─────────────┘            └─────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Components

### Operational Data Service

Provides aggregated operational metrics from Hub's internal data:

| Metric Category | Examples |
|-----------------|----------|
| **Request Metrics** | Volume, latency, completion rates, SLA compliance |
| **Task Metrics** | Assignment rates, resolution times, escalation rates |
| **Queue Metrics** | Depths, wait times, throughput |
| **Application Health** | Error rates, processing times, availability |
| **Agent Performance** | Task counts, efficiency, quality scores |

### Report Center Integration

Integrates with Olympus LakeStack Report Center:

| Capability | Description |
|------------|-------------|
| **Catalog Sync** | Sync published reports from LakeStack to Hub report catalog |
| **Access Mapping** | Map LakeStack report permissions to Hub roles |
| **Context Injection** | Pass workbench/user context to parameterized reports |
| **Embedding** | Render reports within Hub console frames |

### Business Domain Reports

Enables external reports from enterprise systems:

| Source | Example |
|--------|---------|
| **Machine Reports** | Card network reports, core banking analytics |
| **Enterprise BI** | Reports from corporate BI tools via LakeStack |
| **Partner Reports** | Third-party analytics shared via LakeStack |

---

## Report Distribution

Reports appear in the Reports Console of each desk:

| Desk | Report Types |
|------|--------------|
| **Agent Desk** | Business domain reports, Operational reports (as needed) |
| **Supervisor Desk** | Operational reports, Business domain reports |
| **Steward Desk** | Operational reports (workbench/application health) |

### Report Catalog Structure

```yaml
report_catalog:
  workbench_id: "dispute-operations"
  
  operational_reports:
    - id: "queue-health-dashboard"
      source: hub_analytics
      desks: [supervisor, steward]
    - id: "sla-compliance-report"
      source: hub_analytics
      desks: [supervisor, steward, agent]
      
  business_reports:
    - id: "dispute-trend-analysis"
      source: lakestack
      machine: "card-network"
      desks: [supervisor, agent]
    - id: "merchant-performance"
      source: lakestack
      machine: "merchant-services"
      desks: [agent]
```

---

## Key Principles

| Principle | Description |
|-----------|-------------|
| **LakeStack Native** | Leverages Olympus LakeStack (Pontus) for all report building and publishing |
| **Hub Integration** | Hub Analytics provides the glue between LakeStack and Hub consoles |
| **ETSL Integration** | Registers Operations Data into ETSL as assertions for enterprise-wide semantic consistency |
| **Extension Model** | Detailed extension approaches are defined by LakeStack (out of scope) |
| **Context-Aware** | Reports receive Hub context (workbench, user, request) for filtering |

---

---

## ETSL Integration

Hub Analytics integrates Hub's Operations Data into the **Enterprise Truth & Semantics Layer (ETSL)** for enterprise-wide semantic consistency.

### Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Assertion Registration** | Registers Operations Data (requests, tasks, decisions) into ETSL as assertions |
| **Data Product Creation** | Creates ETSL Data Products for operations analytics |
| **Operations Data Marts** | Uses Pontus infrastructure to build Operations Data Marts |
| **Serving Layer Integration** | Integrates with Pontus serving mechanisms (Report Center and others) |

### Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       HUB ANALYTICS - ETSL INTEGRATION                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  HUB OPERATIONS DATA                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Requests │ Tasks │ Decisions │ Activities │ Signals │ Sessions    │    │
│  └───────────────────────────────────┬─────────────────────────────────┘    │
│                                      │                                       │
│                                      ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    HUB ANALYTICS SUBSYSTEM                          │    │
│  │                                                                      │    │
│  │   ┌─────────────────────┐    ┌─────────────────────────────────┐   │    │
│  │   │ Assertion           │    │ Data Product                    │   │    │
│  │   │ Registration        │    │ Creation                        │   │    │
│  │   └──────────┬──────────┘    └────────────────┬────────────────┘   │    │
│  │              │                                │                     │    │
│  └──────────────┼────────────────────────────────┼─────────────────────┘    │
│                 │                                │                          │
│                 ▼                                ▼                          │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                    OLYMPUS LAKESTACK (PONTUS)                        │   │
│  │                                                                       │   │
│  │   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐  │   │
│  │   │      ETSL       │  │  Operations     │  │   Report Center    │  │   │
│  │   │   (Assertions)  │  │  Data Marts     │  │   (Serving)        │  │   │
│  │   └─────────────────┘  └─────────────────┘  └─────────────────────┘  │   │
│  │                                                                       │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### What Hub Analytics Does NOT Do

| Aspect | Hub Analytics Role |
|--------|-------------------|
| **ETSL Semantic Modeling** | Does not define ETSL semantic artifacts — that's ETSL's responsibility |
| **Authority Modeling** | Does not model ETSL authority — references existing ETSL authority definitions |
| **Direct ETSL Consumption** | Hub Applications do not directly consume ETSL Data Artifacts |

### ETSL Data Products → Hub

ETSL Data Products (created by other systems or by Hub Analytics) may be exposed to Hub Workbenches as:
- **Enterprise Memory** — organizational knowledge from ETSL
- **Enterprise Knowledge** — authoritative facts from ETSL

Hub is **agnostic** to whether tenants use ETSL but **advocates** this approach for semantic consistency.

---

## Related Documentation

- [Olympus LakeStack](../../05-infrastructure/olympus-lakestack.md) — Analytics platform (Pontus)
- [Storage Architecture — ETSL Integration](../../07-data-architecture/storage-architecture.md#etsl-and-pontus-integration-touch-points) — Detailed touch points
- [Agent Desk](../../06-ux-architecture/tenant-domain/agent-desk.md) — Reports Console
- [Supervisor Desk](../../06-ux-architecture/tenant-domain/supervisor-desk.md) — Reports Console
- [Steward Desk](../../06-ux-architecture/tenant-domain/steward-desk.md) — Reports Console

---

*TODO: Detailed integration specifications, report catalog schema, embedding protocols, ETSL assertion schemas*

