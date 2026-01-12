# Agent Health & SLOs

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

Agent Health & SLOs provides **Service Level Objective (SLO) tracking and monitoring** for agents, addressing health-related concerns across multiple personas: cost governance (ARE), behavior monitoring (COS), and feedback tracking (PA/APO).

**Key Principle**: Agent Health Monitor **tracks and monitors** SLOs—it does **not enforce** them. Enforcement is handled by supervisors (if configured) or external systems.

---

## SLO Types by Persona

Agent Health Monitor supports three SLO types aligned with persona needs:

| SLO Type | Persona | Purpose |
|----------|---------|---------|
| **Cost SLOs** | ARE (Agent Reliability Engineer) | Cost governance, budget adherence |
| **Behavior SLOs** | COS (Cognitive Operations Steward) | Behavior monitoring, quality tracking |
| **Feedback SLOs** | PA/APO (Process Architect/Automation Product Owner) | Feedback collection, user satisfaction |

---

## Architecture

Agent Health Monitor uses **Agent Analytics data mart** for SLO evaluation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENT HEALTH MONITOR ARCHITECTURE                       │
│                                                                              │
│   Agent Analytics Data Mart → SLO Tracking Service → SLO Manager           │
│                                                                              │
│   • Historical data for trend analysis                                       │
│   • Efficient aggregation for SLO evaluation                                │
│   • Burn rate calculation                                                   │
│   • Deviation detection and alerting                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Tracking Only** — SLO Manager and Tracking Service only manage and track; no enforcement
- **Agent Analytics Integration** — Uses Agent Analytics data mart for SLO evaluation
- **Historical Data** — Leverages historical data for trend analysis and burn rate calculation
- **Lifecycle Pattern** — Follows same pattern as Supervisor lifecycle managers
- **Supervisor Integration** — Can trigger supervisors on SLO deviations (if configured)

---

## Health Spec Structure

Health Specs define SLOs for agents:

| Component | Description |
|-----------|-------------|
| **SLO Definitions** | Cost, behavior, and feedback SLOs |
| **Thresholds** | SLO thresholds and burn rate parameters |
| **Evaluation Windows** | Time windows for SLO evaluation |
| **Alerting Configuration** | Alert rules for SLO deviations |

---

## SLO Tracking

SLO Tracking Service evaluates SLOs using Agent Analytics data:

| Capability | Description |
|------------|-------------|
| **Trend Analysis** | Historical trend analysis for SLO metrics |
| **Burn Rate Calculation** | Calculate burn rate for time-based SLOs |
| **Deviation Detection** | Detect when SLOs deviate from thresholds |
| **Alerting** | Generate alerts for SLO deviations |

---

## Human Feedback Service

Human Feedback Service collects and routes feedback:

| Capability | Description |
|------------|-------------|
| **Feedback Collection** | Collect feedback from users and stakeholders |
| **Feedback Routing** | Route feedback to appropriate owners (Training Feedback Services) |
| **Metric Calculation** | Calculate feedback-based metrics for SLOs |
| **Integration** | Integrate with Training Feedback Services for improvement |

---

## Supervisor Integration

Agent Health Monitor can trigger supervisors on SLO deviations:

| Integration Point | Description |
|-------------------|-------------|
| **Agent Session Supervisor** | Trigger supervisors on SLO deviations (if configured) |
| **Observation Generation** | Generate Observations/Exceptions via Cronus |
| **Workbench Routing** | Route observations to appropriate workbenches |

---

## Related

### Agent Health Monitor Subsystem
- [Agent Health Monitor README](../subsystems/agent-health-monitor/README.md) — Subsystem overview
- [Health Spec Manager](../subsystems/agent-health-monitor/health-spec-manager.md) — Spec structure, SLO definitions
- [SLO Manager](../subsystems/agent-health-monitor/slo-manager.md) — SLO definition and threshold management
- [SLO Tracking Service](../subsystems/agent-health-monitor/slo-tracking-service.md) — SLO deviation tracking
- [Human Feedback Service](../subsystems/agent-health-monitor/human-feedback-service.md) — Feedback collection and routing

### Related Systems
- [Agent Analytics](../subsystems/agent-analytics/README.md) — Uses Agent Analytics data mart for SLO evaluation
- [Agent Session Supervisor](../subsystems/agent-session-supervisor/README.md) — Can trigger supervisors on SLO deviations
- [Training Feedback Services](../subsystems/trained-agent-lifecycle-manager/training-feedback-services.md) — Routes feedback for Training Spec improvements

---

*For detailed implementation, see [Agent Health Monitor README](../subsystems/agent-health-monitor/README.md).*
