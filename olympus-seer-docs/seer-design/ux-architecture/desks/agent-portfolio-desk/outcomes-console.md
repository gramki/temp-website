# Outcomes Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Portfolio Desk](./README.md)  
> **Primary Persona:** [Automation Product Owner (APO)](../../../personas-and-needs/roles.md#1-automation-product-owner-apo)

---

## Purpose

The Outcomes Console enables the **Automation Product Owner (APO)** ([role definition](../../../personas-and-needs/roles.md#1-automation-product-owner-apo)) to track whether agents are delivering business value. It provides KPI dashboards, value tracking, ROI analysis, and stakeholder reporting.

---

## Sections

### KPI Dashboard

Business metrics per agent aligned with charter success criteria.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ KPI DASHBOARD: invoice-processor                      Time Range: [30d ▼]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ┌────────────────────────┐  ┌────────────────────────┐  ┌─────────────────┐ │
│ │ SAME-DAY PROCESSING    │  │ ERROR RATE             │  │ TIME SAVINGS    │ │
│ │                        │  │                        │  │                 │ │
│ │      97.2%             │  │       0.3%             │  │      82%        │ │
│ │   Target: 95% ✅       │  │   Target: <0.5% ✅     │  │  Target: 80% ✅ │ │
│ │   ↑2.1% vs last month  │  │   ↓0.1% vs last month  │  │  ↑5% vs last mo │ │
│ └────────────────────────┘  └────────────────────────┘  └─────────────────┘ │
│                                                                             │
│ ┌────────────────────────┐  ┌────────────────────────┐  ┌─────────────────┐ │
│ │ USER SATISFACTION      │  │ REQUESTS PROCESSED     │  │ AUTONOMY UTIL   │ │
│ │                        │  │                        │  │                 │ │
│ │      4.3/5.0           │  │      12,450            │  │      89%        │ │
│ │   Target: 4.0 ✅       │  │   ↑15% vs last month   │  │  Full autonomy  │ │
│ │   Based on 234 reviews │  │                        │  │  used 89% time  │ │
│ └────────────────────────┘  └────────────────────────┘  └─────────────────┘ │
│                                                                             │
│ [Configure KPIs] [Add KPI] [Export Dashboard]                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

**KPI Configuration:**
| Element | Description |
|---------|-------------|
| KPI Name | Metric name (from charter) |
| Target | Target value |
| Current | Current value |
| Trend | Change vs. previous period |
| Status | On track, At risk, Off track |

**Standard KPIs:**
- Business outcome achievement
- Error/defect rate
- Time/cost savings
- User satisfaction
- Autonomy utilization
- Request volume

### Value Tracker

Track and visualize the business value delivered by agents.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ VALUE TRACKER                                             Period: [Q4 2025] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ PORTFOLIO VALUE SUMMARY                                                     │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ Total Value Delivered:     $1,245,000                                       │
│ Total Cost (Operations):   $124,500                                         │
│ Net Value:                 $1,120,500                                       │
│ Portfolio ROI:             901%                                             │
│                                                                             │
│ VALUE BY AGENT                                                              │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ invoice-processor     ████████████████████████████████░░░░  $520,000 (42%) │
│ expense-approver      ██████████████████░░░░░░░░░░░░░░░░░░  $280,000 (22%) │
│ customer-service      ████████████████░░░░░░░░░░░░░░░░░░░░  $250,000 (20%) │
│ order-validator       ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░  $125,000 (10%) │
│ data-enricher         ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   $70,000  (6%) │
│                                                                             │
│ [View Details] [Export] [Configure Value Metrics]                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Value Metrics:**
| Metric | Calculation |
|--------|-------------|
| Time Saved | (Manual time - Agent time) × Volume × Hourly rate |
| Cost Saved | Manual cost - Agent operation cost |
| Error Cost Avoided | Error reduction × Error cost |
| Revenue Impact | Attributable revenue increase |
| Customer Value | Satisfaction improvement × Customer LTV |

### Comparison View

Compare agent performance to baseline (pre-agent state).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ COMPARISON VIEW: invoice-processor                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                          │ Baseline (Manual)  │ Current (Agent)  │ Change  │
│ ─────────────────────────────────────────────────────────────────────────── │
│ Processing Time          │ 15 minutes         │ 2.5 minutes      │ -83%    │
│ Error Rate               │ 2.1%               │ 0.3%             │ -86%    │
│ Same-Day Completion      │ 65%                │ 97%              │ +49%    │
│ Cost per Invoice         │ $8.50              │ $1.20            │ -86%    │
│ Human Hours/Month        │ 180 hrs            │ 32 hrs           │ -82%    │
│ User Satisfaction        │ 3.2/5.0            │ 4.3/5.0          │ +34%    │
│                                                                             │
│ TREND OVER TIME                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ Processing Time                                                             │
│   15m │━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                  │
│       │                                   ╲                                 │
│       │                                    ╲                                │
│       │                                     ━━━━━━━━━━━                     │
│  2.5m │                                              ━━━━━━━━━━             │
│       └────────────────────────────────────────────────────────             │
│         Jan    Feb    Mar    Apr    May    Jun    Jul    Aug                │
│         └── Baseline ──┘    └──── Agent Deployed ────────┘                  │
│                                                                             │
│ [Export Comparison] [Change Baseline] [Add Metrics]                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Stakeholder Reports

Generate and schedule reports for executives and stakeholders.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAKEHOLDER REPORTS                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ REPORT TEMPLATES                                                            │
│ ──────────────────────────────────────────────────────────────────────────  │
│ 📄 Executive Summary      │ High-level portfolio performance               │
│ 📄 Agent Performance      │ Detailed per-agent metrics                      │
│ 📄 ROI Analysis           │ Value vs. cost breakdown                        │
│ 📄 Trend Report           │ Month-over-month comparisons                    │
│ 📄 Custom Report          │ Build your own report                           │
│                                                                             │
│ SCHEDULED REPORTS                                                           │
│ ──────────────────────────────────────────────────────────────────────────  │
│ │ Report              │ Recipients      │ Schedule    │ Next Run          │ │
│ │ Executive Summary   │ C-Suite, VPs    │ Monthly     │ Feb 1, 2026       │ │
│ │ Agent Performance   │ Ops Team        │ Weekly      │ Jan 20, 2026      │ │
│ │ ROI Analysis        │ Finance         │ Quarterly   │ Apr 1, 2026       │ │
│                                                                             │
│ [+ New Report] [Schedule Report] [View Report History]                      │
│                                                                             │
│ RECENT REPORTS                                                              │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • Executive Summary - January 2026       Generated: Jan 5, 2026  [View][📥]│
│ • Agent Performance - Week 1             Generated: Jan 7, 2026  [View][📥]│
│ • Custom: Q4 Review                      Generated: Dec 15, 2025 [View][📥]│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Report Features:**
- Template-based generation
- Customizable sections
- Export formats: PDF, PPT, Excel
- Scheduled delivery via email
- Interactive web version

---

## Key Features

### KPI Configuration

APO can define custom KPIs:

```yaml
kpi:
  name: "Same-Day Processing Rate"
  formula: "completed_same_day / total_requests * 100"
  target: 95
  unit: "%"
  threshold:
    green: ">= 95"
    yellow: ">= 85"
    red: "< 85"
  data_source: "agent_metrics"
  refresh: "hourly"
```

### Value Attribution

Connect agent activity to business value:

| Attribution Method | Description |
|-------------------|-------------|
| Direct | Agent completes task that has known value |
| Time-based | Time saved × cost per hour |
| Quality-based | Error reduction × error cost |
| Volume-based | Incremental capacity × per-unit value |

### Trend Analysis

- Historical performance over configurable periods
- Anomaly detection with alerts
- Forecasting based on trends
- Seasonality adjustment

### Outcome Alerts

Configure alerts for outcome changes:

| Alert Type | Trigger | Action |
|------------|---------|--------|
| KPI Off Track | KPI falls below threshold | Email + Dashboard flag |
| Trend Decline | 3+ periods of decline | Dashboard flag |
| Target Achieved | KPI meets target | Celebration notification |
| Anomaly | Unusual deviation | Investigation prompt |

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Real-time outcome metrics, trend visibility |
| **Predictable** | Forecasting, baseline comparison |
| **Directable** | KPI configuration, target adjustment |
| **Authority Enforceable** | Value justification for autonomy decisions |

---

## REST API

```
Base: /api/seer/apo/v1

# KPIs
GET    /agents/{id}/kpis              - Get agent KPIs
POST   /agents/{id}/kpis              - Create KPI
PUT    /agents/{id}/kpis/{kpi_id}     - Update KPI
DELETE /agents/{id}/kpis/{kpi_id}     - Delete KPI
GET    /agents/{id}/kpis/{kpi_id}/data - Get KPI data

# Outcomes
GET    /agents/{id}/outcomes          - Get outcome metrics
GET    /portfolio/outcomes            - Portfolio-wide outcomes
GET    /agents/{id}/outcomes/trends   - Trend data
GET    /agents/{id}/outcomes/forecast - Forecasted outcomes

# Value
GET    /agents/{id}/value             - Agent value metrics
GET    /portfolio/value               - Portfolio value summary
GET    /agents/{id}/value/breakdown   - Value breakdown

# Comparison
GET    /agents/{id}/comparison        - Baseline comparison
PUT    /agents/{id}/baseline          - Update baseline

# Reports
GET    /reports                       - List reports
POST   /reports/generate              - Generate report
GET    /reports/{id}                  - Get report
GET    /reports/{id}/download         - Download report
POST   /reports/schedule              - Schedule report
```

---

## Indicative Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ OUTCOMES CONSOLE                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ Agent: [invoice-processor ▼]  Period: [Last 30 days ▼]  [Export] [Report]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐              │
│ │ SAME-DAY        │  │ ERROR RATE      │  │ ROI             │              │
│ │     97.2%       │  │     0.3%        │  │     890%        │              │
│ │ Target: 95% ✅  │  │ Target: 0.5% ✅ │  │                 │              │
│ └─────────────────┘  └─────────────────┘  └─────────────────┘              │
│                                                                             │
│ VALUE DELIVERED THIS PERIOD                                                 │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│   Value: $52,000  │  Cost: $4,800  │  Net: $47,200  │  ROI: 883%           │
│                                                                             │
│ TREND                                                                       │
│ ──────────────────────────────────────────────────────────────────────────  │
│   $60k │                                          ▲                        │
│        │                                    ▲────▲                         │
│   $40k │                              ▲────▲                               │
│        │                        ▲────▲                                     │
│   $20k │                  ▲────▲                                           │
│        │            ▲────▲                                                 │
│    $0k └─────────────────────────────────────────────────────────          │
│          Week 1  Week 2  Week 3  Week 4                                    │
│                                                                             │
│ [View Details] [Configure KPIs] [Generate Report]                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
