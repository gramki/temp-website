# Agent Session Sentinel Oversight

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

Agent Session Sentinel Oversight provides **sentinel oversight** for agent sessions, managing sentinel policies, observations, and escalations for failed or stuck agents.

**Key Capabilities:**
- Real-time sentinel oversight via Signal Exchange event observation
- Analytical sentinel oversight via Agent Analytics data mart queries
- OPA policy evaluation for sentinel decisions
- Observation/Exception generation via Cronus Gateway
- Workbench routing for Ops Center display

---

## Architecture

Agent Session Sentinel operates in two modes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  AGENT SESSION SENTINEL ARCHITECTURE                      │
│                                                                              │
│   ┌──────────────────────┐         ┌──────────────────────┐                 │
│   │  Realtime Sentinel │         │ Analytical Sentinel│                 │
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

- **Two Sentinel Types** — Realtime and Analytical sentinels for different use cases
- **Cronus Integration** — Uses Hub's existing Observation/Exception model via Cronus Gateway
- **Deployment Model** — Sentinels deployed via Deployment CRDs referencing Spec CRDs
- **Lifecycle Pattern** — Follows same pattern as Trained/Employed Agent lifecycle managers
- **No Enforcement** — Sentinels generate observations; enforcement handled by external systems

---

## Sentinel Types

### Realtime Sentinel

Observes Signal Exchange events in real-time:

| Capability | Description |
|------------|-------------|
| **Event Observation** | Observes SX events for agent sessions |
| **OPA Policy Evaluation** | Evaluates OPA policies on events |
| **Real-time Generation** | Generates Observations/Exceptions immediately |
| **Use Cases** | Stuck agents, failed requests, policy violations |

### Analytical Sentinel

Runs templated SQL queries on Agent Analytics data mart:

| Capability | Description |
|------------|-------------|
| **SQL Execution** | Runs templated SQL queries periodically |
| **Data Mart Queries** | Queries Agent Analytics data mart |
| **Periodic Execution** | Runs on schedule (cron-based) |
| **Use Cases** | Trend analysis, pattern detection, historical issues |

---

## Sentinel Spec Structure

Sentinel Specs define sentinel policies:

| Component | Description |
|-----------|-------------|
| **Sentinel Policies** | OPA policies for realtime sentinels |
| **SQL Templates** | Templated SQL queries for analytical sentinels |
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

Agent Session Sentinel integrates with Cronus Gateway:

| Aspect | Description |
|--------|-------------|
| **Observation Model** | Uses Hub's existing Observation/Exception model |
| **No New Model** | No new model required; leverages existing Hub model |
| **Workbench Routing** | Observations routed to workbenches via Cronus |
| **Ops Center** | Observations displayed in Hub Ops Center |

---

## Deployment Model

Sentinels follow a deployment model:

| Component | Description |
|-----------|-------------|
| **Spec CRD** | Sentinel Spec CRD defines sentinel policies |
| **Deployment CRD** | Deployment CRD references Spec CRD |
| **Clear Separation** | Spec definition separate from deployment configuration |
| **Seer Operator** | Seer Operator reconciles CRDs to Kubernetes state |

---

## Related

### Agent Session Sentinel Subsystem
- [Agent Session Sentinel README](../subsystems/agent-session-sentinel/README.md) — Subsystem overview
- [Sentinel Spec Manager](../subsystems/agent-session-sentinel/sentinel-spec-manager.md) — Spec structure, validation
- [Realtime Sentinel Service](../subsystems/agent-session-sentinel/realtime-sentinel-service.md) — SX event observation, OPA evaluation
- [Analytical Sentinel Service](../subsystems/agent-session-sentinel/analytical-sentinel-service.md) — Templated SQL execution
- [Observation Service](../subsystems/agent-session-sentinel/observation-service.md) — Cronus Observations/Exceptions generation

### Related Systems
- [Agent Health Monitor](../subsystems/agent-health-monitor/README.md) — Can trigger sentinels on SLO deviations
- [Agent Analytics](../subsystems/agent-analytics/README.md) — Uses Agent Analytics data mart for analytical sentinels
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — SX event source for realtime sentinels
- [Cronus Gateway](../../../olympus-hub-docs/04-subsystems/signal-providers/cronus-business-exceptions.md) — Observations/Exceptions publishing

---

*For detailed implementation, see [Agent Session Sentinel README](../subsystems/agent-session-sentinel/README.md).*
