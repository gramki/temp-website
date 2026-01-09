# Hub Win Operations Center

> **Status:** 🔴 Stub — Placeholder for expansion

**Hub Win Operations Center** is the operational console for Customer Success (Win) teams to manage tenant subscriptions, monitor usage, and provide customer assistance.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | [Customer Success Executive](../08-personas-and-journeys/personas/customer-success.md) |
| **Scope** | All tenant subscriptions (Publisher domain) |
| **Purpose** | Subscription management, usage monitoring, customer assistance |
| **Access** | Web, MCP (Publisher Admin Channel) |

---

## Scope Distinction

| Level | Application | Scope |
|-------|-------------|-------|
| **Publisher** | Hub Win Operations Center | All tenant subscriptions |
| **Tenant** | Hub Control Center | Single tenant's subscription |

The Win Operations Center operates at the **publisher level**, providing oversight across all customer subscriptions.

---

## Key Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Subscription Lifecycle** | Create, modify, renew tenant subscriptions |
| **Usage Monitoring** | Track usage patterns, quotas, limits |
| **Customer Health** | Adoption metrics, engagement indicators |
| **Support Assistance** | Help tenants with configuration, best practices |
| **Billing Coordination** | Usage reports, billing inquiries |
| **Onboarding** | New tenant setup, initial configuration |

---

## Console Types

### Subscription Consoles

| Console | Purpose |
|---------|---------|
| **Subscription Dashboard** | Overview of all tenant subscriptions |
| **Subscription Details** | Deep-dive into individual subscriptions |
| **Provisioning Console** | Create and configure new subscriptions |
| **Renewal Console** | Upcoming renewals, expiration tracking |

### Usage & Health Consoles

| Console | Purpose |
|---------|---------|
| **Usage Analytics** | Usage trends, quota utilization |
| **Adoption Dashboard** | Feature adoption, engagement metrics |
| **Health Scores** | Customer health indicators |
| **Alerts Console** | Usage anomalies, risk indicators |

### Support Consoles

| Console | Purpose |
|---------|---------|
| **Support Queue** | Active customer inquiries |
| **Knowledge Base** | Customer-facing documentation |
| **Best Practices** | Configuration recommendations |

---

## Sample Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      HUB WIN OPERATIONS CENTER                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────┐  │
│  │  ACTIVE TENANTS      │  │  HEALTH SCORE        │  │  SUPPORT TICKETS │  │
│  │       47             │  │      8.4 / 10        │  │      5 Open      │  │
│  │  +3 this month       │  │  🟢 Healthy          │  │  🟡 1 Urgent     │  │
│  └──────────────────────┘  └──────────────────────┘  └──────────────────┘  │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  TENANT SUBSCRIPTIONS                                               │    │
│  │                                                                     │    │
│  │  Tenant              │ Plan    │ Health │ Usage  │ Renewal  │ Risk │    │
│  │  ────────────────────────────────────────────────────────────────── │    │
│  │  ACME Bank           │ Enterprise │ 9.2  │  78%   │ 180 days │  🟢 │    │
│  │  Global Insurance    │ Enterprise │ 8.8  │  65%   │  45 days │  🟢 │    │
│  │  Metro Retail        │ Standard   │ 6.5  │  42%   │  30 days │  🟡 │    │
│  │  First Credit        │ Enterprise │ 9.0  │  82%   │ 220 days │  🟢 │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  ATTENTION REQUIRED                                        [View All]│    │
│  │  ─────────────────────────────────────────────────────────────────  │    │
│  │  🟡 Metro Retail: Low adoption, renewal in 30 days                  │    │
│  │  🔵 Global Insurance: Quota approaching 90%                         │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Future: Win Team Workbench

In future, Customer Success teams may have a dedicated **Hub instance** with workbenches to manage customer relationships. This would enable:
- Scenario-based customer engagement
- Automated health monitoring workflows
- CS task queues and assignments

---

## Related Documentation

- [Customer Success Persona](../08-personas-and-journeys/personas/customer-success.md)
- [Subscription Management](../04-subsystems/subscription-management/README.md)
- [Hub SRE Operations Center](./hub-sre-ops-center.md) — SRE counterpart

---

*TODO: Detailed console specifications, health score algorithms, integration with CRM*

