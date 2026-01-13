# Agent Operations Desk

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Primary Persona:** [Agent Reliability Engineer (ARE)](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)  
> **Related:** [ARE Reference](../../../personas-and-needs/are.md) | [Production Readiness](../../../personas-and-needs/needs/production-readiness.md)

---

## Purpose

The Agent Operations Desk is the primary workspace for the **Agent Reliability Engineer (ARE)** ([role definition](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)). It provides capabilities to:

- Monitor agent and system health in real-time
- Control agents at runtime (kill switches, bounds, levers)
- Respond to and recover from incidents
- Manage production deployments

---

## Consoles

| Console | Purpose | Documentation |
|---------|---------|---------------|
| **Health Console** | AHS, CHR, metrics, SLOs | [health-console.md](./health-console.md) |
| **Control Console** | Levers, kill switches, bounds | [control-console.md](./control-console.md) |
| **Incident Console** | Triage, contain, recover, postmortem | [incident-console.md](./incident-console.md) |

---

## Key Journeys

| Journey | Description | Consoles Used |
|---------|-------------|---------------|
| **Production Gate** | Review and approve agent for production | Control Console |
| **Incident Response** | Detect, contain, recover from incidents | Incident Console, Control Console |
| **Cost Intervention** | Investigate and resolve cost anomalies | Health Console, Control Console |
| **Capacity Planning** | Plan and request capacity from provider | Health Console |
| **SLO Management** | Monitor and manage service level objectives | Health Console |

---

## OPDA Integration

The Agent Operations Desk demonstrates OPDA capabilities for ARE:

| OPDA | Capability | Console |
|------|------------|---------|
| **Observable** | Health metrics, AHS, CHR, SLO dashboards | Health Console |
| **Predictable** | SLO forecasting, burn rate prediction | Health Console |
| **Directable** | Control levers, kill switches, rollback | Control Console |
| **Authority Enforceable** | Deployment gates, cost ceilings | Control Console |

### How ARE Actions, Assesses, and Evidences OPDA

| OPDA | ARE Actions | ARE Assesses | ARE Evidences |
|------|-------------|--------------|---------------|
| **Observable** | Configure dashboards | Review health metrics | Health reports, traces |
| **Predictable** | Set SLO targets | Monitor burn rates | SLO compliance reports |
| **Directable** | Adjust control levers | Verify lever effects | Control audit logs |
| **Authority Enforceable** | Set deployment gates | Validate gate enforcement | Gate decision records |

---

## Channel Access

| Channel | Capabilities |
|---------|--------------|
| **Web UI** | Full desk access via Seer Portal |
| **REST API** | `/api/seer/are/v1` — [API Documentation](../../rest-channels/are-rest-channel.md) |
| **MCP** | `seer-are-mcp` server for AI assistant integration |
| **CLI** | Operational tooling |
| **Mobile** | On-call alerting |
| **PagerDuty/Slack** | Incident notifications |

---

## Integration Points

### Receives From

| Source | Data |
|--------|------|
| **AE** | Production readiness submissions |
| **COS** | System-relevant behavioral issues |
| **Platform** | Infrastructure alerts |
| **APO** | Operational constraints |

### Sends To

| Destination | Data |
|-------------|------|
| **AE** | Operational feedback, incident data |
| **COS** | Health data for behavioral correlation |
| **APO** | Operational risk assessments |
| **ARAO** | Compliance evidence |

---

## Indicative Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT OPERATIONS DESK                                      ARE: Sam K.     │
├─────────────────────────────────────────────────────────────────────────────┤
│  [Health] [Control] [Incident]                                  🔔 🔍 ⚙️    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ SYSTEM HEALTH                                    Last Updated: 30s   │   │
│  ├──────────────────────────────────────────────────────────────────────┤   │
│  │                                                                       │   │
│  │   System AHS     │    System CHR    │   Availability   │   Error Rate│   │
│  │   ████████░░     │    ███████░░░    │   ██████████     │   ██░░░░░░░░│   │
│  │      0.87        │      $12.50      │      99.8%       │      0.4%   │   │
│  │    [Healthy]     │    [Normal]      │    [Target]      │   [Target]  │   │
│  │                                                                       │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────┐  ┌──────────────────────────────┐  │
│  │ AGENT FLEET                         │  │ SLO STATUS                   │  │
│  │                                     │  │                              │  │
│  │ ✅ invoice-processor    AHS: 0.92  │  │ Availability: 99.8% ✅       │  │
│  │ ✅ customer-service     AHS: 0.88  │  │ Latency P95: 2.1s ✅         │  │
│  │ ⚠️ order-validator      AHS: 0.71  │  │ Error Rate: 0.4% ✅          │  │
│  │ ✅ expense-approver     AHS: 0.85  │  │ Cost Ceiling: 78% ✅         │  │
│  │ 🔴 data-enricher        AHS: 0.58  │  │                              │  │
│  │                                     │  │ Error Budget: 4.2 hrs left   │  │
│  │ [View All Agents →]                 │  │                              │  │
│  └─────────────────────────────────────┘  └──────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ ACTIVE INCIDENTS                                               [1]   │   │
│  ├──────────────────────────────────────────────────────────────────────┤   │
│  │ 🔴 INC-2026-0113-001 │ data-enricher │ Cost spike detected │ 15m    │   │
│  │    Status: Investigating │ Severity: P2 │ Owner: Sam K.              │   │
│  │    [View Details] [Contain] [Resolve]                                │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Console Summaries

### Health Console

Real-time visibility into agent and system health.

**Sections:**
- **System Dashboard** — AHS, CHR, availability, latency (aggregated)
- **Agent Dashboard** — Per-agent health metrics
- **SLO Tracker** — SLO status, error budgets, burn rates
- **Cost Observatory** — Token usage, API costs, budget tracking

**Key Features:**
- Customizable dashboards
- Drill-down from system to agent to task
- Burn rate alerts (2x, 5x, 10x)
- Cost anomaly detection

[Full specification →](./health-console.md)

---

### Control Console

Runtime control of agents and system.

**Sections:**
- **Agent Levers** — Per-agent: kill switch, bounds, tool toggles
- **System Levers** — System-wide: kill switch, cost ceiling, autonomy mode
- **Deployment Gates** — Production readiness review, approve/reject
- **Rollback Manager** — Quick rollback to previous versions

**Key Features:**
- One-click kill switch
- Lever change audit log
- Production readiness checklist (AE submission)
- Staged rollback with validation

[Full specification →](./control-console.md)

---

### Incident Console

Incident management from detection to resolution.

**Sections:**
- **Active Incidents** — Current incidents with status
- **Triage View** — Impact assessment, severity assignment
- **Containment Actions** — Quick actions: isolate, throttle, halt
- **Postmortem** — RCA documentation, prevention actions

**Key Features:**
- Incident timeline with events
- One-click containment actions
- Integration with PagerDuty/Slack
- Postmortem templates

[Full specification →](./incident-console.md)

---

## REST API Overview

The ARE REST channel provides programmatic access:

```
Base: /api/seer/are/v1

Health:
  GET    /health/system           - System health summary
  GET    /health/agents           - All agent health
  GET    /health/agents/{id}      - Agent health details
  GET    /slos                    - SLO status
  GET    /costs                   - Cost summary
  GET    /costs/agents/{id}       - Agent cost details

Control:
  GET    /agents/{id}/levers      - Get agent levers
  PUT    /agents/{id}/levers      - Update agent levers
  POST   /agents/{id}/kill        - Kill switch
  GET    /system/levers           - Get system levers
  PUT    /system/levers           - Update system levers
  POST   /system/kill             - System kill switch

Deployment:
  GET    /production-gates        - List pending gates
  GET    /production-gates/{id}   - Gate details
  POST   /production-gates/{id}/approve - Approve deployment
  POST   /production-gates/{id}/reject  - Reject deployment
  POST   /agents/{id}/rollback    - Trigger rollback

Incidents:
  GET    /incidents               - List incidents
  POST   /incidents               - Create incident
  GET    /incidents/{id}          - Incident details
  PUT    /incidents/{id}          - Update incident
  POST   /incidents/{id}/contain  - Containment action
  POST   /incidents/{id}/resolve  - Resolve incident
```

[Full API documentation →](../../rest-channels/are-rest-channel.md)

---

*Status: 🟡 Draft — Overview and console specifications complete*
