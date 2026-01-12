# Agent Session Supervisor

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13

## Overview

Agent Session Supervisor provides supervisory oversight for agent sessions, managing supervisory policies, observations, and escalations for failed or stuck agents.

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [SCOPE.md](./SCOPE.md) | Design scope, coverage summary, key decisions | Overview |
| [Supervisor Spec Manager](./supervisor-spec-manager.md) | Spec structure, validation, deployment configuration | C2 |
| [Realtime Supervisor Service](./realtime-supervisor-service.md) | SX event observation, OPA policy evaluation | C2 |
| [Analytical Supervisor Service](./analytical-supervisor-service.md) | Templated SQL execution on analytics data mart | C2 |
| [Observation Service](./observation-service.md) | Cronus Observations/Exceptions generation | C2 |
| [Supervisor Operators](./supervisor-operators.md) | Lifecycle management, state transitions | C2 |
| [Supervisor Levers](./supervisor-levers.md) | Runtime controls, enable/disable, suspend | C2 |
| [Supervisor Directory](./supervisor-directory.md) | Registry, search, version tracking | C2 |

---

## Architecture

```mermaid
flowchart TB
    subgraph Supervisor[Agent Session Supervisor]
        SSM[Supervisor Spec Manager]
        RTS[Realtime Supervisor Service]
        ASS[Analytical Supervisor Service]
        OS[Observation Service]
        SO[Supervisor Operators]
        SL[Supervisor Levers]
        SD[Supervisor Directory]
    end
    
    subgraph ExternalSystems[External Systems]
        SignalExchange[Signal Exchange]
        AgentAnalytics[Agent Analytics]
        Cronus[Cronus Gateway]
        SeerOp[Seer Operator]
    end
    
    SignalExchange --> RTS
    AgentAnalytics --> ASS
    RTS --> OS
    ASS --> OS
    OS --> Cronus
    SSM --> SeerOp
    SO --> SD
    SL --> SD
```

---

## Key Design Decisions

### Two Supervisor Types

- **Realtime Supervisor**: Observes SX events, evaluates OPA policies, generates real-time Observations/Exceptions
- **Analytical Supervisor**: Runs templated SQL on analytics data mart periodically, generates analytical Observations/Exceptions

### Cronus Integration

- **Generates Observations/Exceptions via Cronus Gateway** (Hub model)
- **Uses Hub's existing Observation/Exception model**—no new model required
- **Workbench routing** via Cronus for Ops Center display

### Deployment Model

- **Supervisors deployed via Deployment CRDs** referencing Spec CRDs
- **Deployment CRD corresponds to Spec CRD** where templatized definition is stored
- **Clear separation** between spec definition and deployment configuration

### Lifecycle Pattern

- **Follows same pattern** as Trained/Employed Agent lifecycle managers
- **Spec Manager handles validation** and structure management
- **Seer Operator reconciles** CRDs to Kubernetes state

---

## Related

- [Agent Health Monitor](../agent-health-monitor/README.md) — Can trigger supervisors on SLO deviations (if configured)
- [Agent Analytics](../agent-analytics/README.md) — Uses Agent Analytics data mart for analytical supervisors
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — SX event source for realtime supervisors
- [Cronus Gateway](../../../olympus-hub-docs/04-subsystems/signal-providers/cronus-business-exceptions.md) — Observations/Exceptions publishing
