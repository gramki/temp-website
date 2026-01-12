# Agent Session Supervision

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

Agent Session Supervision provides **supervisory oversight** for agent sessions, managing supervisory policies, observations, and escalations for failed or stuck agents.

**Key Capabilities:**
- Real-time supervision via Signal Exchange event observation
- Analytical supervision via Agent Analytics data mart queries
- OPA policy evaluation for supervisory decisions
- Observation/Exception generation via Cronus Gateway
- Workbench routing for Ops Center display

---

## Architecture

Agent Session Supervisor operates in two modes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  AGENT SESSION SUPERVISOR ARCHITECTURE                     │
│                                                                              │
│   ┌──────────────────────┐         ┌──────────────────────┐                 │
│   │  Realtime Supervisor │         │ Analytical Supervisor│                 │
│   │  • SX event observation│         │  • SQL on analytics data│               │
│   │  • OPA policy evaluation│        │  • Periodic execution│                 │
│   └──────────┬───────────┘         └──────────┬───────────┘                 │
│              │                                 │                             │
│              └──────────────┬──────────────────┘                             │
│                             │                                                 │
│                    ┌────────▼────────┐                                        │
│                    │ Observation     │                                        │
│                    │ Service         │                                        │
│                    └────────┬────────┘                                        │
│                             │                                                 │
│                    ┌────────▼────────┐                                        │
│                    │ Cronus Gateway  │                                        │
│                    │ (Observations/  │                                        │
│                    │  Exceptions)    │                                        │
│                    └─────────────────┘                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Two Supervisor Types** — Realtime and Analytical supervisors for different use cases
- **Cronus Integration** — Uses Hub's existing Observation/Exception model via Cronus Gateway
- **Deployment Model** — Supervisors deployed via Deployment CRDs referencing Spec CRDs
- **Lifecycle Pattern** — Follows same pattern as Trained/Employed Agent lifecycle managers
- **No Enforcement** — Supervisors generate observations; enforcement handled by external systems

---

## Supervisor Types

### Realtime Supervisor

Observes Signal Exchange events in real-time:

| Capability | Description |
|------------|-------------|
| **Event Observation** | Observes SX events for agent sessions |
| **OPA Policy Evaluation** | Evaluates OPA policies on events |
| **Real-time Generation** | Generates Observations/Exceptions immediately |
| **Use Cases** | Stuck agents, failed requests, policy violations |

### Analytical Supervisor

Runs templated SQL queries on Agent Analytics data mart:

| Capability | Description |
|------------|-------------|
| **SQL Execution** | Runs templated SQL queries periodically |
| **Data Mart Queries** | Queries Agent Analytics data mart |
| **Periodic Execution** | Runs on schedule (cron-based) |
| **Use Cases** | Trend analysis, pattern detection, historical issues |

---

## Supervisor Spec Structure

Supervisor Specs define supervisory policies:

| Component | Description |
|-----------|-------------|
| **Supervisory Policies** | OPA policies for realtime supervisors |
| **SQL Templates** | Templated SQL queries for analytical supervisors |
| **Observation Rules** | Rules for generating Observations/Exceptions |
| **Workbench Routing** | Routing configuration for observations |

---

## Observation Service

Observation Service generates Observations/Exceptions:

| Capability | Description |
|------------|-------------|
| **Observation Generation** | Generate Observations via Cronus Gateway |
| **Exception Generation** | Generate Exceptions via Cronus Gateway |
| **Workbench Routing** | Route observations to appropriate workbenches |
| **Ops Center Display** | Display observations in Hub Ops Center |

---

## Cronus Integration

Agent Session Supervisor integrates with Cronus Gateway:

| Aspect | Description |
|--------|-------------|
| **Observation Model** | Uses Hub's existing Observation/Exception model |
| **No New Model** | No new model required; leverages existing Hub model |
| **Workbench Routing** | Observations routed to workbenches via Cronus |
| **Ops Center** | Observations displayed in Hub Ops Center |

---

## Deployment Model

Supervisors follow a deployment model:

| Component | Description |
|-----------|-------------|
| **Spec CRD** | Supervisor Spec CRD defines supervisory policies |
| **Deployment CRD** | Deployment CRD references Spec CRD |
| **Clear Separation** | Spec definition separate from deployment configuration |
| **Seer Operator** | Seer Operator reconciles CRDs to Kubernetes state |

---

## Related

### Agent Session Supervisor Subsystem
- [Agent Session Supervisor README](../subsystems/agent-session-supervisor/README.md) — Subsystem overview
- [Supervisor Spec Manager](../subsystems/agent-session-supervisor/supervisor-spec-manager.md) — Spec structure, validation
- [Realtime Supervisor Service](../subsystems/agent-session-supervisor/realtime-supervisor-service.md) — SX event observation, OPA evaluation
- [Analytical Supervisor Service](../subsystems/agent-session-supervisor/analytical-supervisor-service.md) — Templated SQL execution
- [Observation Service](../subsystems/agent-session-supervisor/observation-service.md) — Cronus Observations/Exceptions generation

### Related Systems
- [Agent Health Monitor](../subsystems/agent-health-monitor/README.md) — Can trigger supervisors on SLO deviations
- [Agent Analytics](../subsystems/agent-analytics/README.md) — Uses Agent Analytics data mart for analytical supervisors
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — SX event source for realtime supervisors
- [Cronus Gateway](../../../olympus-hub-docs/04-subsystems/signal-providers/cronus-business-exceptions.md) — Observations/Exceptions publishing

---

*For detailed implementation, see [Agent Session Supervisor README](../subsystems/agent-session-supervisor/README.md).*
