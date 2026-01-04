# Publisher Consoles

> **Status:** 🔴 Stub — Placeholder for expansion

The **Publisher Consoles** are applications for Hub System (Publisher Domain) personas — SRE and Customer Success teams who operate the Hub platform itself.

---

## SRE Operations Center

### Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | SRE |
| **Scope** | Hub System (all tenants) |
| **Purpose** | Monitor, maintain, and operate Hub infrastructure |

### Capabilities

| Capability | Description |
|------------|-------------|
| **Infrastructure Monitoring** | Health dashboards, metrics, alerts |
| **Tenant Overview** | Usage across all tenants |
| **Capacity Management** | Resource utilization, scaling decisions |
| **Incident Management** | Incident tracking, resolution workflows |
| **Deployment Management** | Release management, rollouts |
| **Security Monitoring** | Security events, access anomalies |

### Screen Structure

```
SRE Operations Center
├── Dashboard
│   ├── System Health
│   ├── Active Incidents
│   └── Recent Deployments
│
├── Infrastructure
│   ├── Compute (Atlantis)
│   ├── Data Stores
│   ├── Event Bus (Atropos)
│   └── Gateways
│
├── Tenants
│   ├── Tenant List
│   ├── Usage Summary
│   └── Resource Allocation
│
├── Incidents
│   ├── Active Incidents
│   ├── Incident History
│   └── Runbooks
│
└── Operations
    ├── Deployments
    ├── Scheduled Maintenance
    └── Configuration
```

---

## Customer Success Center

### Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | Customer Success Executive |
| **Scope** | Hub System (all tenants) |
| **Purpose** | Onboard tenants, support adoption, review usage |

### Capabilities

| Capability | Description |
|------------|-------------|
| **Tenant Onboarding** | Create subscriptions, initial setup |
| **Usage Analytics** | Adoption metrics, feature usage |
| **Health Monitoring** | Tenant health scores, at-risk indicators |
| **Support Coordination** | Support tickets, escalation tracking |
| **Success Planning** | Adoption milestones, success metrics |

### Screen Structure

```
Customer Success Center
├── Dashboard
│   ├── Tenant Health Overview
│   ├── Onboarding Pipeline
│   └── Support Summary
│
├── Tenants
│   ├── Tenant List
│   ├── Tenant Details
│   ├── Usage Analytics
│   └── Health Scores
│
├── Onboarding
│   ├── New Tenant Wizard
│   ├── Onboarding Checklists
│   └── Templates
│
├── Support
│   ├── Active Tickets
│   ├── Escalations
│   └── Knowledge Base
│
└── Analytics
    ├── Adoption Metrics
    ├── Feature Usage
    └── Trend Analysis
```

---

## Related Documentation

- [SRE Persona](../08-personas-and-journeys/personas/sre.md)
- [Customer Success Persona](../08-personas-and-journeys/personas/customer-success.md)

---

*TODO: Detailed screen specifications, monitoring dashboards, onboarding workflows*

