# Outcome Tracking

> **Status:** 🟡 Draft

---

## Overview

**Outcome Tracking** measures whether automation achieves the success criteria defined in the Intent. This closes the loop from Ideation → Design → Build → Deploy → Run → **Measure** → (back to) Ideation.

---

## Outcome Model

```yaml
apiVersion: hub.olympus.io/v1
kind: AutomationOutcome
metadata:
  id: outcome-33333
  name: dispute-auto-triage-outcomes
  namespace: acme-bank
spec:
  # Source
  charter_id: charter-11111
  intent_id: intent-67890
  workbench_id: wb-dispute-auto-triage
  
  # Tracking Period
  tracking_start: "2026-04-01"    # Go-live date
  tracking_end: null              # Ongoing
  
  # Success Criteria Actuals
  metrics:
    - metric_id: "triage-time"
      name: "Average triage time"
      unit: "minutes"
      baseline: 15
      target: 3
      
      actuals:
        - period: "2026-04"
          value: 8
          status: improving
        - period: "2026-05"
          value: 5
          status: improving
        - period: "2026-06"
          value: 3.2
          status: near_target
    
    - metric_id: "misrouting-rate"
      name: "Misrouting rate"
      unit: "percent"
      baseline: 20
      target: 2
      
      actuals:
        - period: "2026-04"
          value: 12
          status: improving
        - period: "2026-05"
          value: 6
          status: improving
        - period: "2026-06"
          value: 3
          status: near_target

status:
  overall_status: on_track        # on_track | at_risk | off_track | achieved | failed
  
  last_updated: "2026-06-30T00:00:00Z"
  updated_by: system              # system (automated) or apo@acme.com (manual)
  
  # Value Realization
  value_realized:
    quantitative:
      - description: "Agent time saved"
        value: 2400
        unit: "hours/month"
      - description: "Cost reduction"
        value: 50000
        unit: "USD/month"
    qualitative:
      - "Improved agent satisfaction"
      - "Faster customer resolution"
```

---

## Outcome Lifecycle

```
                    ┌──────────────┐
                    │   TRACKING   │
                    └──────┬───────┘
                           │
                           │ Periodic measurement
                           ▼
    ┌──────────────────────┴──────────────────────┐
    │                                              │
    ▼                                              ▼
┌──────────────┐                          ┌──────────────┐
│   ACHIEVED   │                          │    FAILED    │
│              │                          │              │
│ All targets  │                          │ Targets not  │
│ met          │                          │ achievable   │
└──────────────┘                          └──────────────┘
        │                                         │
        │                                         │
        ▼                                         ▼
  New Ideas for                            Retrospective
  enhancement                              + New Ideas
```

| Status | Description |
|--------|-------------|
| `on_track` | Metrics trending toward targets |
| `at_risk` | Some metrics lagging |
| `off_track` | Unlikely to meet targets |
| `achieved` | All targets met |
| `failed` | Targets not achievable |

---

## Measurement Sources

| Source | Metrics |
|--------|---------|
| **Hub Analytics** | Request volume, processing time, completion rates |
| **Task Management** | Task duration, queue depth, escalation rates |
| **CAF** | Decision quality, override rates |
| **Feedback Services** | Bug/issue volume, satisfaction signals |
| **External Systems** | Business KPIs from source systems |

### Automated Collection

```
Hub Analytics              Outcome Tracking           APO Dashboard
      │                          │                          │
      ├─── Metrics snapshot ────▶│                          │
      │    (daily/weekly)        │                          │
      │                          ├─── Update actuals        │
      │                          │                          │
      │                          ├─── Calculate status ────▶│
      │                          │                          │
```

### Manual Input

Some metrics require manual input:

```yaml
actuals:
  - period: "2026-06"
    value: 85
    status: on_track
    source: manual
    entered_by: apo@acme.com
    notes: "Survey results from customer satisfaction"
```

---

## Value Realization Reporting

### Quantitative Value

| Category | Examples |
|----------|----------|
| **Time Savings** | Hours saved, throughput increase |
| **Cost Reduction** | Direct cost savings, avoided hires |
| **Revenue Impact** | Faster processing, reduced churn |
| **Risk Reduction** | Error reduction, compliance improvement |

### Qualitative Value

| Category | Examples |
|----------|----------|
| **Experience** | Agent satisfaction, customer satisfaction |
| **Capability** | New services enabled, scalability |
| **Strategic** | Competitive advantage, market position |

---

## Feedback Loop to Ideation

Outcome tracking generates new Ideas:

### Success → Enhancement Ideas

```
Outcome: ACHIEVED
      │
      ├─── "Can we extend to international disputes?"
      │    → New Idea submitted
      │
      ├─── "Can we add document classification?"
      │    → New Idea submitted
      │
```

### Failure → Correction Ideas

```
Outcome: OFF_TRACK
      │
      ├─── "Triage accuracy for fraud disputes low"
      │    → New Idea: "Specialized fraud triage agent"
      │
      ├─── "Edge cases overwhelming agents"
      │    → New Idea: "Edge case knowledge base"
      │
```

### Automatic Idea Suggestions

When patterns emerge:

```
Outcome Tracking                 Ideation Services
      │                                │
      ├─── Pattern detected ──────────▶│
      │    "High override rate for     │
      │     category X disputes"       │
      │                                ├─── Suggest Idea
      │                                │    (APO reviews)
      │                                │
```

---

## APO Dashboard

The Outcomes Console shows:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AUTOMATION OUTCOMES DASHBOARD                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  DISPUTE AUTO-TRIAGE (Charter #11111)                                       │
│  Status: ●● ON TRACK                                                        │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  METRIC: Average Triage Time                                          │  │
│  │                                                                        │  │
│  │  Baseline: 15 min  │  Target: 3 min  │  Current: 3.2 min             │  │
│  │                                                                        │  │
│  │  [████████████████████████████████████████░░] 94%                     │  │
│  │                                                                        │  │
│  │  Apr     May     Jun     Jul     Aug                                  │  │
│  │   8       5      3.2      -       -                                   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  METRIC: Misrouting Rate                                              │  │
│  │                                                                        │  │
│  │  Baseline: 20%  │  Target: 2%  │  Current: 3%                        │  │
│  │                                                                        │  │
│  │  [████████████████████████████████████░░░░░░] 85%                     │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  VALUE REALIZED                                                             │
│  • Agent time saved: 2,400 hours/month                                     │
│  • Cost reduction: $50,000/month                                           │
│                                                                              │
│  [View Details]  [Export Report]  [Create Idea]                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## APIs

### REST (Creator Channel)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/outcomes` | List outcomes |
| `GET` | `/outcomes/{outcome_id}` | Get outcome details |
| `POST` | `/outcomes/{outcome_id}/actuals` | Add metric actual |
| `PUT` | `/outcomes/{outcome_id}/status` | Update status |
| `GET` | `/outcomes/{outcome_id}/report` | Generate report |

### MCP (Creator Channel)

| Tool | Description |
|------|-------------|
| `list_outcomes` | List outcomes |
| `get_outcome_details` | Get details with metrics |
| `record_metric_actual` | Record metric value |
| `generate_outcome_report` | Create summary report |

---

## Related Documentation

- [Charter Acceptance](./charter-acceptance.md) — Source of Outcomes
- [Idea Management](./idea-management.md) — Feedback loop destination
- [Hub Analytics](../hub-analytics/README.md) — Metric source
- [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md)

