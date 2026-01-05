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
| **LakeStack Native** | Leverages Olympus LakeStack for all report building and publishing |
| **Hub Integration** | Hub Analytics provides the glue between LakeStack and Hub consoles |
| **Extension Model** | Detailed extension approaches are defined by LakeStack (out of scope) |
| **Context-Aware** | Reports receive Hub context (workbench, user, request) for filtering |

---

## Related Documentation

- [Olympus LakeStack](../../05-infrastructure/olympus-lakestack.md) — Analytics platform
- [Agent Desk](../../06-ux-architecture/tenant-domain/agent-desk.md) — Reports Console
- [Supervisor Desk](../../06-ux-architecture/tenant-domain/supervisor-desk.md) — Reports Console
- [Steward Desk](../../06-ux-architecture/tenant-domain/steward-desk.md) — Reports Console

---

*TODO: Detailed integration specifications, report catalog schema, embedding protocols*

