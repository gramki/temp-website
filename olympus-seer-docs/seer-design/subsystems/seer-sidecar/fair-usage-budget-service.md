# Fair Usage Budget Service

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12  
> **Design Level**: C2 (Container)

---

## Overview

The Fair Usage Budget Service tracks usage of the agent **by users/customers** (not resources consumed by the agent — see [Resource Quota Service](./resource-quota-service.md) for that). It enforces fair usage limits across multiple dimensions to prevent abuse and ensure equitable access.

**Key Principle**: Fair usage budgets protect against abuse by limiting how much any single user, customer, or signal source can consume of agent capacity.

---

## Budget Dimensions

| Dimension | Description | Example |
|-----------|-------------|---------|
| **Per Subject** | Per customer, account, or entity | 100 requests/day per customer |
| **Per Signal** | Per request type or scenario | 50 fraud investigations/day |
| **Per Time Period** | Hourly, daily, weekly, monthly | 1000 requests/month |
| **Per Action Type** | Per tool or API endpoint | 20 refund decisions/day |

---

## Budget Configuration

### Employment Spec Configuration

```yaml
# In EmploymentSpec
spec:
  fairUsage:
    # Per-subject budgets
    subjects:
      - dimension: customer_id
        budgets:
          - period: day
            limit: 100
            action: reject
          - period: hour
            limit: 20
            action: alert
      
      - dimension: account_id
        budgets:
          - period: day
            limit: 50
            action: reject
    
    # Per-signal budgets
    signals:
      - scenario: fraud-investigation
        budgets:
          - period: day
            limit: 500
            action: reject
      
      - scenario: "*"  # All scenarios
        budgets:
          - period: hour
            limit: 100
            action: alert
    
    # Per-action budgets
    actions:
      - pattern: "/api/agent/v1/decisions"
        budgets:
          - period: day
            limit: 200
            action: reject
      
      - pattern: "/api/agent/v1/requests/*/updates"
        budgets:
          - period: minute
            limit: 30
            action: throttle
    
    # Global time-based budgets
    global:
      - period: month
        limit: 10000
        action: escalate
```

---

## Budget Tracking Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FAIR USAGE TRACKING                                       │
│                                                                              │
│   Inbound Request                                                           │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                  EXTRACT DIMENSIONS                                 │  │
│   │   • customer_id from request context                                │  │
│   │   • scenario_id from dispatch                                       │  │
│   │   • account_id from request metadata                                │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                  CHECK BUDGETS                                      │  │
│   │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │  │
│   │   │ Per-Subject │  │ Per-Signal  │  │ Per-Action  │                │  │
│   │   │   Budget    │  │   Budget    │  │   Budget    │                │  │
│   │   └─────────────┘  └─────────────┘  └─────────────┘                │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                  UPDATE CONSUMPTION                                 │  │
│   │   • Increment counters per dimension                                │  │
│   │   • Track across time windows                                       │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Budget Aggregation Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| **Sum** | Total consumption across period | Request counts |
| **Max** | Maximum single value in period | Largest transaction amount |
| **Average** | Average across period | Average response time |
| **Count** | Number of occurrences | Error counts |

```yaml
# Aggregation configuration
spec:
  fairUsage:
    subjects:
      - dimension: customer_id
        budgets:
          - period: day
            aggregation: sum  # Sum of all requests
            limit: 100
          
          - period: day
            aggregation: max  # Largest single request
            field: amount
            limit: 10000
```

---

## Budget Reset Policies

| Period | Reset Timing |
|--------|--------------|
| **Minute** | Start of each minute |
| **Hour** | Start of each hour |
| **Day** | Midnight UTC (or configured timezone) |
| **Week** | Monday midnight UTC |
| **Month** | First day of month midnight UTC |

```yaml
# Reset configuration
spec:
  fairUsage:
    resetPolicy:
      timezone: "America/New_York"
      weekStart: monday
```

---

## Budget Exhaustion Policies

| Action | Behavior |
|--------|----------|
| **Reject** | Block operation when budget exceeded |
| **Alert** | Allow operation, send notification |
| **Throttle** | Slow down rate of requests |
| **Escalate** | Notify supervisor, allow with approval |

### Exhaustion Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    BUDGET EXHAUSTION HANDLING                                │
│                                                                              │
│   Budget Exceeded                                                           │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                  CHECK EXHAUSTION POLICY                            │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│   ┌───┼───────────────┬───────────────┬───────────────┐                    │
│   │   │               │               │               │                    │
│   ▼   ▼               ▼               ▼               ▼                    │
│ Reject  Alert       Throttle       Escalate                                │
│ ┌────┐ ┌────┐       ┌────┐        ┌────┐                                   │
│ │Block│ │Allow│      │Delay│       │Hold│                                   │
│ │with │ │with │      │next │       │for │                                   │
│ │error│ │notify│     │call │       │appr│                                   │
│ └────┘ └────┘       └────┘        └────┘                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Enforcement Scope

| Traffic Type | Budget Enforcement |
|--------------|-------------------|
| ✅ Inbound requests | Per-subject, per-signal budgets |
| ✅ Outbound Hub API calls | Per-action budgets |
| ✅ All traffic | Global time-based budgets |

---

## Integration Points

### Agent Lifecycle Manager
- Fair usage budget configuration → Budget limits
- Budget changes trigger configuration reload

### Agent Runtime
- Request processing → Budget consumption tracking
- Request context → Dimension extraction

### Istio Egress
- Outbound call tracking → Per-action budget updates

### Agent Health Monitor
- Budget exhaustion events → Health alerts
- Budget utilization → Health metrics and reporting

---

## Observability

### Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_fair_usage_consumption` | Current consumption | `dimension`, `period` |
| `seer_fair_usage_remaining` | Remaining budget | `dimension`, `period` |
| `seer_fair_usage_exhaustion_total` | Exhaustion events | `dimension`, `action` |
| `seer_fair_usage_rejection_total` | Rejections | `dimension` |

### Budget Status

```json
{
  "agent_id": "fraud-analyst-001",
  "fair_usage": {
    "subjects": {
      "customer_id:cust-123": {
        "day": {
          "limit": 100,
          "used": 75,
          "remaining": 25,
          "resets_at": "2026-01-13T00:00:00Z"
        }
      }
    },
    "signals": {
      "fraud-investigation": {
        "day": {
          "limit": 500,
          "used": 120,
          "remaining": 380,
          "resets_at": "2026-01-13T00:00:00Z"
        }
      }
    },
    "global": {
      "month": {
        "limit": 10000,
        "used": 4500,
        "remaining": 5500,
        "resets_at": "2026-02-01T00:00:00Z"
      }
    }
  }
}
```

---

## Related Documentation

- [Resource Quota Service](./resource-quota-service.md) — Agent resource consumption
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) — Budget configuration
- [Metrics Service](./metrics-service.md) — Metrics collection

---

*Fair Usage Budget Service tracks usage of the agent by users/customers across multiple dimensions (subject, signal, time period, action type) to prevent abuse and ensure equitable access.*
