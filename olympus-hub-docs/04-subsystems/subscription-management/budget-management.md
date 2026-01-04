# Budget Management

> **Status:** 🔴 Stub — Placeholder for expansion

Manages quotas, limits, usage tracking, and budget controls for tenant subscriptions.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Enforce resource limits and track usage |
| **Scope** | Quotas, usage metering, alerts, billing integration |
| **Enforcement** | Soft limits (warnings) and hard limits (blocking) |

---

## Quota Categories

| Category | Examples |
|----------|----------|
| **Storage** | Data store GB, memory store GB, knowledge store GB |
| **Compute** | vCPU hours, container hours, workflow executions |
| **Requests** | API calls, signals processed, requests handled |
| **Users** | Active users, concurrent users, agents |
| **Workbenches** | Active workbenches, scenarios per workbench |
| **Integrations** | Machines registered, I/O gateways configured |

---

## Quota Model

```yaml
quotas:
  tenant_id: "acme-bank"
  tier: "professional"
  
  storage:
    data_store_gb:
      limit: 100
      used: 45
      unit: "GB"
    memory_store_gb:
      limit: 10
      used: 3.5
      unit: "GB"
    knowledge_store_gb:
      limit: 50
      used: 12
      unit: "GB"
  
  compute:
    vcpu_hours_monthly:
      limit: 1000
      used: 423
      unit: "vCPU-hours"
    workflow_executions_monthly:
      limit: 10000
      used: 2340
      unit: "executions"
  
  requests:
    signals_monthly:
      limit: 1000000
      used: 234567
      unit: "signals"
    api_calls_monthly:
      limit: 5000000
      used: 1234567
      unit: "calls"
  
  entities:
    active_users:
      limit: 100
      used: 45
      unit: "users"
    workbenches:
      limit: 10
      used: 3
      unit: "workbenches"
    machines:
      limit: 20
      used: 8
      unit: "machines"
```

---

## Limit Enforcement

| Type | Behavior |
|------|----------|
| **Soft Limit** | Warning at 80%, alert at 90% |
| **Hard Limit** | Block at 100% (configurable overage) |
| **Burst Limit** | Allow temporary overage with throttling |
| **Reserved** | Guaranteed minimum allocation |

---

## Usage Tracking

| Metric | Frequency |
|--------|-----------|
| **Storage** | Hourly |
| **Compute** | Per-minute |
| **Requests** | Real-time |
| **Users** | Daily |

---

## Alerts and Notifications

| Threshold | Action |
|-----------|--------|
| 80% | Warning notification to admins |
| 90% | Urgent alert to admins |
| 100% | Hard limit enforcement, escalation |

---

## Billing Integration

| Function | Description |
|----------|-------------|
| **Metering** | Usage data for billing |
| **Overages** | Track and bill overages |
| **Invoicing** | Generate usage reports for billing |
| **Cost Allocation** | Attribute costs to workbenches/scenarios |

---

## Related Documentation

- [Subscription Management Overview](./README.md)
- [Resource Management](./resource-management.md)
- [Tenant Subscription Lifecycle](./tenant-subscription-lifecycle.md)

---

*TODO: Detailed design — metering pipeline, billing integration, cost optimization*

