# Agent Session Sentinel - Scope and Design Status

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13

---

## Scope

The **Agent Session Sentinel** subsystem provides sentinel oversight for agent sessions, managing sentinel policies, observations, and escalations. It is responsible for:

1. **Sentinel Specification Management** — Spec structure, validation, deployment configuration
2. **Realtime Sentinel Oversight** — SX event observation, OPA policy evaluation, real-time observation generation
3. **Analytical Sentinel Oversight** — Templated SQL execution on analytics data mart, periodic observation generation
4. **Observation Generation** — Cronus Observations/Exceptions generation and routing
5. **Lifecycle Management** — Registration, validation, versioning, state transitions
6. **Operational Controls** — Enable/disable, suspend, emergency controls
7. **Sentinel Registry** — Search, version tracking, deployment status

---

## Intended Depth

This design documentation is at **C2 (Container) level** in the C4 architecture model:

| Aspect | Coverage |
|--------|----------|
| **Functional Scope** | Complete — what each component does |
| **Integration Points** | Complete — hand-offs between containers |
| **Conceptual Models** | Complete — illustrated with YAML examples |
| **Operational Flows** | Complete — sequence diagrams for key operations |
| **Data Models** | Conceptual only — no detailed schemas |
| **API Specifications** | Not included — deferred to implementation |

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Sentinel Spec Manager](./sentinel-spec-manager.md) | Spec structure, validation, deployment configuration | ✅ Complete |
| [Realtime Sentinel Service](./realtime-sentinel-service.md) | SX event observation, OPA policy evaluation | ✅ Complete |
| [Analytical Sentinel Service](./analytical-sentinel-service.md) | Templated SQL execution on analytics data mart | ✅ Complete |
| [Observation Service](./observation-service.md) | Cronus Observations/Exceptions generation | ✅ Complete |
| [Sentinel Operators](./sentinel-operators.md) | Lifecycle management, state transitions | ✅ Complete |
| [Sentinel Levers](./sentinel-levers.md) | Runtime controls, enable/disable, suspend | ✅ Complete |
| [Sentinel Directory](./sentinel-directory.md) | Registry, search, version tracking | ✅ Complete |

---

## Coverage Summary

### ✅ Sentinel Spec Manager (sentinel-spec-manager.md)

- **Sentinel Spec Structure**
  - Core components (sentinel type, name, target scope, policy definition, observation configuration, deployment configuration)
  - Spec structure validation rules
  - Required fields and field types
  
- **Sentinel Type Configuration**
  - Realtime Sentinel (SX events, OPA policies)
  - Analytical Sentinel (SQL templates, periodic execution)
  
- **Deployment Configuration**
  - Deployment CRD structure
  - Deployment flow and integration

### ✅ Realtime Sentinel Service (realtime-sentinel-service.md)

- **SX Event Observation**
  - Event subscription configuration
  - Event types observed
  - Event observation flow
  
- **OPA Policy Evaluation**
  - OPA input context structure
  - OPA policy examples
  - Policy evaluation flow
  
- **Observation Generation**
  - Observation conditions
  - Observation generation flow

### ✅ Analytical Sentinel Service (analytical-sentinel-service.md)

- **Templated SQL Execution**
  - SQL template structure
  - Template variables
  - SQL execution flow
  
- **Periodic Execution**
  - Schedule configuration
  - Execution modes (scheduled, on-demand, event-driven)
  
- **Result Processing**
  - Result structure
  - Result to observation mapping
  - Result processing flow

### ✅ Observation Service (observation-service.md)

- **Observation Generation**
  - Observation structure
  - Observation generation flow
  
- **Exception Generation**
  - Exception structure
  - Exception generation flow
  
- **Cronus Integration**
  - Cronus publishing
  - Cronus integration flow

### ✅ Sentinel Operators (sentinel-operators.md)

- **Registration Service**
  - Registration flow and steps
  - CRD creation and Kubernetes registration
  - State initialization
  
- **Validation Orchestration**
  - Validation checks (structure, policy syntax, target scope, deployment config)
  - Validation flow coordination
  - Validation results and error handling
  
- **Version Management**
  - Version assignment rules
  - Version compatibility tracking
  - Version history maintenance
  
- **State Transition Service**
  - Lifecycle states (Drafted → Validated → Deployed → Suspended → Archived)
  - State transition rules and enforcement
  - Transition flow diagrams

### ✅ Sentinel Levers (sentinel-levers.md)

- **Enable/Disable Control**
  - Enable and disable actions
  - Enable/disable flow
  
- **Suspend Control**
  - Suspend and resume actions
  - Suspend flow
  
- **Emergency Control**
  - Emergency disable, suspend, archive
  - Emergency control flow

### ✅ Sentinel Directory (sentinel-directory.md)

- **Sentinel Registry**
  - Registry entry structure
  - Registry indexes (by sentinel ID, workbench, type, state, deployment status)
  
- **Search & Discovery**
  - Search queries (by workbench, type, agent, state, deployment status)
  - Search examples and results
  
- **Version Tracking**
  - Version history
  - Version compatibility
  
- **Deployment Status Tracking**
  - Deployment status (healthy, degraded, unhealthy, unknown)
  - Status update flow

---

## Integration Patterns

| Pattern | Use Case | Components |
|---------|----------|------------|
| **CRD-Based** | Control plane changes | SentinelSpec CRD updates, state transitions |
| **Event-Driven** | Real-time sentinel oversight | SX event observation, policy evaluation |
| **Periodic** | Analytical sentinel oversight | Scheduled SQL execution |
| **Query-Based** | Discovery and search | Directory queries |
| **Orchestration** | Validation and state management | Operators coordinate validation across systems |

---

## Implementation Details Deferred

The following implementation details are deferred to the detailed implementation stage:

| Area | Deferred Details |
|------|------------------|
| **Data Models** | Detailed SentinelSpec CRD schema, database schemas |
| **API Specifications** | REST/gRPC endpoints, request/response schemas |
| **Storage** | Database selection, indexing strategies, retention policies |
| **OPA Policy Schema** | Complete OPA policy schema, Rego syntax details |
| **SQL Template Syntax** | Complete SQL template syntax, variable substitution |
| **Error Handling** | Specific retry policies, circuit breakers |
| **Observability** | Specific metrics, dashboard layouts |

These will be addressed during implementation with common defaults applied.

---

## Related Subsystems

| Subsystem | Relationship |
|-----------|--------------|
| [Agent Analytics](../agent-analytics/README.md) | Uses Agent Analytics data mart for analytical sentinels |
| [Agent Health Monitor](../agent-health-monitor/README.md) | Can trigger sentinels on SLO deviations (if configured) |
| [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) | Observes SX events for realtime sentinels |
| [Cronus Gateway](../../../olympus-hub-docs/04-subsystems/signal-providers/cronus-business-exceptions.md) | Publishes Observations/Exceptions |
| [Seer Operator](../../hub-integration/training-spec-crd.md) | CRD reconciliation to Kubernetes state |

---

## Related Hub Documentation

- `olympus-hub-docs/04-subsystems/signal-exchange/README.md` — Signal Exchange (SX event source)
- `olympus-hub-docs/04-subsystems/signal-providers/cronus-business-exceptions.md` — Cronus model for Observations/Exceptions

---

*This scope document reflects the completed C2-level design of the Agent Session Sentinel subsystem.*
