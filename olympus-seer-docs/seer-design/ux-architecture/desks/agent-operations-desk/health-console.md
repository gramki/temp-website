# Health Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Operations Desk](./README.md)  
> **Primary Persona:** [Agent Reliability Engineer (ARE)](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)

---

## Purpose

The Health Console provides the **Agent Reliability Engineer (ARE)** ([role definition](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)) with comprehensive visibility into agent fleet health, SLA performance, and resource utilization.

For detailed context on ARE's operational needs, see [ARE: Operational Predictability & Production Readiness](../../../personas-and-needs/needs/are-operational-predictability.md).

---

## Sections

### Fleet Dashboard

Enterprise-wide agent health overview.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ FLEET HEALTH DASHBOARD                                   Last Updated: Now  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ OVERALL STATUS                                                              │
│ ┌───────────────────┬───────────────────┬───────────────────┐              │
│ │   🟢 HEALTHY      │   🟡 DEGRADED     │   🔴 CRITICAL     │              │
│ │      38           │       5           │       2           │              │
│ │   (84%)           │   (11%)           │   (5%)            │              │
│ └───────────────────┴───────────────────┴───────────────────┘              │
│                                                                             │
│ KEY METRICS                                                                 │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Fleet AHS: 0.89 (target: 0.85) ✅    │ Active Tasks: 1,247                  │
│ Avg Response Time: 2.3s              │ Queue Depth: 342                     │
│ Error Rate: 0.8% (target: <2%) ✅    │ Throughput: 450/min                  │
│                                                                             │
│ AGENTS REQUIRING ATTENTION                                                  │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Agent               │ Status     │ AHS   │ Issue                            │
│ ───────────────────────────────────────────────────────────────────────────│
│ order-validator-03  │ 🔴 Critical │ 0.52  │ High error rate (15%)           │
│ expense-approver-07 │ 🔴 Critical │ 0.61  │ SLA breach (p95 > 30s)          │
│ invoice-proc-02     │ 🟡 Degraded │ 0.78  │ Elevated latency                │
│ data-enricher-05    │ 🟡 Degraded │ 0.79  │ Queue backlog                   │
│                                                                             │
│ [View All] [Drill Down] [Create Incident]                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Agent Health Score (AHS)

Real-time composite health metrics.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AGENT HEALTH SCORE: invoice-processor-01                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ COMPOSITE AHS: 0.91                                          Status: 🟢     │
│ ████████████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░     │
│                                                                             │
│ COMPONENT SCORES                                                            │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Availability (30%)     │ 0.99  │ ████████████████████████████████████████   │
│ Success Rate (25%)     │ 0.96  │ ███████████████████████████████████████    │
│ Latency (20%)          │ 0.85  │ █████████████████████████████████████      │
│ Resource Usage (15%)   │ 0.82  │ ████████████████████████████████████       │
│ Error Budget (10%)     │ 0.90  │ ██████████████████████████████████████     │
│                                                                             │
│ HISTORY (7 Days)                                                            │
│ ──────────────────────────────────────────────────────────────────────────  │
│ 1.0 │                    ▄▄▄▄▄▄▄▄▄▄▄▄▄                                     │
│ 0.9 │▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█████████████████▄▄▄▄▄▄▄▄▄▄▄                       │
│ 0.8 │███████████████████████████████████████████████▄▄▄                    │
│ 0.7 │                                                                      │
│     └─────────────────────────────────────────────────────                 │
│       M    T    W    T    F    S    S                                       │
│                                                                             │
│ [Configure Weights] [Set Thresholds] [Export Report]                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### SLA Performance

Track SLA compliance by agent and tier.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SLA PERFORMANCE                                            Period: 7 Days   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BY TIER                                                                     │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Tier       │ Target    │ Actual    │ Compliance │ Status                    │
│ Critical   │ 99.9%     │ 99.95%    │ 100%       │ ✅ Meeting                │
│ High       │ 99.5%     │ 99.2%     │ 98.5%      │ ⚠️ At risk               │
│ Standard   │ 99.0%     │ 99.3%     │ 100%       │ ✅ Meeting                │
│ Background │ 95.0%     │ 98.5%     │ 100%       │ ✅ Exceeding              │
│                                                                             │
│ SLA BREACHES (Last 7 Days)                                                  │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Time                │ Agent              │ SLA         │ Resolution         │
│ Jan 12, 14:22       │ expense-approver-07│ p95 > 30s   │ Scaled up          │
│ Jan 11, 09:15       │ order-validator-03 │ Error > 2%  │ Rollback           │
│ Jan 10, 23:45       │ data-enricher-01   │ Timeout     │ Auto-recovered     │
│                                                                             │
│ [Configure SLAs] [Breach Details] [Trend Analysis]                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Resource Utilization

Monitor compute, memory, and token consumption.

---

## Key Features

- **Real-time fleet health visibility**
- **Composite AHS with configurable weights**
- **SLA tracking and breach alerting**
- **Resource utilization monitoring**
- **Drill-down to individual agents**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Fleet health visibility |
| **Predictable** | SLA targets and monitoring |
| **Directable** | Threshold configuration |
| **Authority Enforceable** | N/A (operational focus) |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
