# Agent Health Monitor - Scope and Design Status

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13

---

## Scope

The **Agent Health Monitor** subsystem tracks and monitors health-related Service Level Objectives (SLOs) for agents, including cost SLOs (ARE), behavior SLOs (COS), and feedback SLOs (PA/APO). It is responsible for:

1. **Health Specification Management** — Spec structure, SLO definitions, validation, deployment configuration
2. **SLO Management** — SLO definition and threshold management for Cost, Behavior, and Feedback SLOs
3. **SLO Tracking** — SLO deviation tracking using Agent Analytics data mart, threshold evaluation, metric aggregation
4. **Human Feedback Service** — Feedback collection, routing to Training Feedback Services, feedback metric calculation
5. **Lifecycle Management** — Registration, validation, versioning, state transitions
6. **Operational Controls** — Enable/disable, suspend, emergency controls
7. **Health Registry** — Search, version tracking, SLO status

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
| [Health Spec Manager](./health-spec-manager.md) | Spec structure, SLO definitions, validation, deployment configuration | ✅ Complete |
| [SLO Manager](./slo-manager.md) | SLO definition and threshold management | ✅ Complete |
| [SLO Tracking Service](./slo-tracking-service.md) | SLO deviation tracking using Agent Analytics data mart | ✅ Complete |
| [Human Feedback Service](./human-feedback-service.md) | Feedback collection, routing, metric calculation | ✅ Complete |
| [Health Operators](./health-operators.md) | Lifecycle management, state transitions | ✅ Complete |
| [Health Levers](./health-levers.md) | Runtime controls, enable/disable, suspend | ✅ Complete |
| [Health Directory](./health-directory.md) | Registry, search, version tracking, SLO status | ✅ Complete |

---

## Coverage Summary

### ✅ Health Spec Manager (health-spec-manager.md)

- **Health Spec Structure**
  - Core components (health spec name, target scope, Cost SLOs, Behavior SLOs, Feedback SLOs, deployment configuration)
  - Spec structure validation rules
  - Required fields and field types
  
- **SLO Definition Validation**
  - SLO validation rules (name, threshold, window, evaluation, action)
  - SLO type validation (Cost, Behavior, Feedback)
  
- **Deployment Configuration**
  - Deployment CRD structure
  - Deployment flow and integration

### ✅ SLO Manager (slo-manager.md)

- **SLO Definition Management**
  - Cost SLOs (ARE): cost_per_request, daily_budget, total_cost, cost_anomaly_score
  - Behavior SLOs (COS): agent_health_score, error_rate, latency_p99, availability, success_rate
  - Feedback SLOs (PA/APO): user_satisfaction, override_rate, feedback_rating, escalation_rate
  
- **Threshold Configuration**
  - Threshold structure (absolute, relative, dynamic)
  - Burn rate alerts (warning, critical, emergency)
  
- **SLO Metadata**
  - SLO metadata structure
  - Persona mapping (ARE, COS, PA, APO)

### ✅ SLO Tracking Service (slo-tracking-service.md)

- **Metric Aggregation**
  - Aggregation methods (p50, p95, p99, max, sum, average, rate)
  - Aggregation flow from Agent Analytics data mart
  
- **Threshold Evaluation**
  - Evaluation process
  - Evaluation flow
  
- **Deviation Detection**
  - Deviation types (threshold breach, burn rate warnings)
  - Deviation detection flow
  
- **Supervisor Triggering**
  - Supervisor trigger configuration
  - Supervisor trigger flow

### ✅ Human Feedback Service (human-feedback-service.md)

- **Feedback Collection**
  - Feedback types (explicit, implicit, outcome)
  - Feedback structure
  - Feedback collection flow
  
- **Feedback Routing**
  - Routing rules (Training Spec improvements, agent behavior, capability gaps, safety concerns, performance issues)
  - Routing flow
  
- **Feedback Metric Calculation**
  - Metrics calculated (user_satisfaction, override_rate, feedback_rating, escalation_rate)
  - Metric calculation flow

### ✅ Health Operators (health-operators.md)

- **Registration Service**
  - Registration flow and steps
  - CRD creation and Kubernetes registration
  - State initialization
  
- **Validation Orchestration**
  - Validation checks (structure, SLO, target scope, deployment config)
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

### ✅ Health Levers (health-levers.md)

- **Enable/Disable Control**
  - Enable and disable actions
  - Enable/disable flow
  
- **Suspend Control**
  - Suspend and resume actions
  - Suspend flow
  
- **Emergency Control**
  - Emergency disable, suspend, archive
  - Emergency control flow

### ✅ Health Directory (health-directory.md)

- **Health Registry**
  - Registry entry structure
  - Registry indexes (by health spec ID, workbench, agent, state, SLO status, deployment status)
  
- **Search & Discovery**
  - Search queries (by workbench, agent, state, SLO status, deployment status)
  - Search examples and results
  
- **Version Tracking**
  - Version history
  - Version compatibility
  
- **SLO Status Tracking**
  - SLO status (compliant, deviating, critical, unknown)
  - Status update flow

---

## Integration Patterns

| Pattern | Use Case | Components |
|---------|----------|------------|
| **CRD-Based** | Control plane changes | HealthSpec CRD updates, state transitions |
| **Query-Based** | SLO evaluation | Agent Analytics data mart queries |
| **Event-Driven** | Feedback collection | Feedback events |
| **Orchestration** | Validation and state management | Operators coordinate validation across systems |

---

## Implementation Details Deferred

The following implementation details are deferred to the detailed implementation stage:

| Area | Deferred Details |
|------|------------------|
| **Data Models** | Detailed HealthSpec CRD schema, database schemas |
| **API Specifications** | REST/gRPC endpoints, request/response schemas |
| **Storage** | Database selection, indexing strategies, retention policies |
| **SLO Evaluation Algorithms** | Specific evaluation algorithms, burn rate calculations |
| **Feedback Storage** | Feedback database schema, aggregation algorithms |
| **Error Handling** | Specific retry policies, circuit breakers |
| **Observability** | Specific metrics, dashboard layouts |

These will be addressed during implementation with common defaults applied.

---

## Related Subsystems

| Subsystem | Relationship |
|-----------|--------------|
| [Agent Analytics](../agent-analytics/README.md) | Uses Agent Analytics data mart for SLO evaluation |
| [Seer Sentinels](../seer-sentinels/README.md) | Can trigger sentinels on SLO deviations (if configured) |
| [Training Feedback Services](../trained-agent-lifecycle-manager/training-feedback-services.md) | Routes feedback for Training Spec improvements |
| [Seer Operator](../../hub-integration/training-spec-crd.md) | CRD reconciliation to Kubernetes state |

---

## Related Hub Documentation

- `olympus-hub-docs/04-subsystems/feedback-services/README.md` — Hub Feedback Services

---

*This scope document reflects the completed C2-level design of the Agent Health Monitor subsystem.*
