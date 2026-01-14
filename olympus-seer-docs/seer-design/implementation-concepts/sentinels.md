# Sentinels

> **Category:** DevOps and Lifecycle  
> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-15

---

## Overview

Sentinels provide **automated oversight and governance** for AI agents operating in Seer. They enable organizations to monitor agent behavior, detect anomalies, enforce policies, and take corrective actions—either by generating observations for human review or by participating directly in requests as AI agents themselves. Sentinels operate in three distinct modes: Realtime (event-driven policy evaluation), Analytical (periodic data analysis), and Request (AI agent participation in other agents' work).

---

## Ontology Context

### Relationship to Ontology

Sentinels implement the **Observability, Predictability, Directability (OPD)** principles from Agent-Oriented Systems Modeling (AOSM):

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|-------------|
| **Observability** | Realtime/Analytical Sentinels observe events and data | Sentinels make agent behavior visible |
| **Predictability** | Policy-based evaluation and pattern detection | Sentinels identify predictable failure modes |
| **Directability** | Request Sentinels can intervene and take actions | Sentinels enable automated correction |
| **Controlled Autonomy** | Sentinel policies define boundaries | Sentinels enforce autonomy limits |
| **RASCI Accountability** | Observations link to accountable humans | Sentinels support human accountability |

### Gap This Fills

The AOSM ontology defines the principles of observability and directability but doesn't specify how to implement automated oversight at scale. Sentinels fill this gap by providing:

1. **Automated Monitoring**: Human supervisors cannot monitor every agent decision; sentinels can
2. **Real-time Intervention**: Sentinels can act immediately, not just alert
3. **Pattern Detection**: Sentinels identify cross-request patterns humans might miss
4. **Policy Enforcement**: Sentinels enforce governance policies programmatically
5. **AI-on-AI Oversight**: Sentinels enable AI agents to oversee other AI agents

---

## Definition

**Sentinels** are automated oversight mechanisms that monitor, evaluate, and optionally intervene in agent operations. They operate in three types: **Realtime Sentinels** (event-driven OPA policy evaluation), **Analytical Sentinels** (periodic SQL-based pattern detection), and **Request Sentinels** (AI agents that observe and participate in other agents' requests).

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-level (Request Sentinels) or Subscription-level (COG Sentinels) |
| **Lifecycle** | Created via SentinelSpec CRD → Validated → Deployed → Suspended/Archived |
| **Ownership** | Cognitive Operations Steward (COS) defines policies; Agent Reliability Engineer (ARE) manages deployment |
| **Multiplicity** | Multiple sentinels per workbench; each sentinel can target multiple agents/workbenches |

---

## Rationale

### Why This Design?

**Three Sentinel Types for Different Use Cases**:
- **Realtime Sentinels**: Immediate response to runtime events (stuck agents, policy violations)
- **Analytical Sentinels**: Historical pattern detection (trends, anomalies over time)
- **Request Sentinels**: Active participation in request lifecycle (governance, quality assurance)

**Cronus Integration for Observations**:
- Realtime/Analytical sentinels use Hub's existing Observation/Exception model
- No new model required; leverages existing Hub infrastructure
- Observations route to Ops Center for human review

**Request Sentinels as Employed Agents**:
- Request Sentinels operate as full Employed Agents with delegated authority
- They create child requests, enabling proper scope and audit trail
- This enables AI-on-AI oversight patterns essential for enterprise scale

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Single Sentinel Type** | Different use cases require different operation models (real-time vs. periodic vs. request participation) |
| **New Observation Model** | Hub's existing Observation/Exception model is sufficient; no need for duplication |
| **Sentinels as External Services** | Request Sentinels need to participate in Hub Request model; Employed Agent pattern provides proper integration |

### Related ADRs

| ADR | Decision |
|-----|----------|
| *To be added* | *Sentinel architecture decisions* |

---

## Structure

### Key Attributes

```yaml
# Conceptual SentinelSpec structure
sentinel_spec:
  type: realtime | analytical | request
  name: string
  target:
    workbench_ids: [string]
    agent_ids: [string]  # Optional, empty = all agents
  
  # For Realtime/Analytical
  policy:
    opa_policy: string  # For realtime
    sql_template: string  # For analytical
  
  observation_config:
    generate_observation:
      condition: string
      observation_type: string
      severity: string
    
    generate_exception:
      condition: string
      exception_type: string
      criticality: string
  
  # For Request Sentinel
  sentinel_scenario_specs:
    normative_ref:
      name: string
      version: string
    automation_ref:
      name: string
      version: string
    deployment_ref:
      name: string
      version: string
```

### States

| State | Description | Transitions |
|-------|-------------|-------------|
| **Drafted** | Spec created, not validated | → Validated |
| **Validated** | Spec validated, ready for deployment | → Deployed, → Archived |
| **Deployed** | Sentinel deployed and active | → Suspended, → Archived |
| **Suspended** | Sentinel suspended (temporarily disabled) | → Deployed, → Archived |
| **Archived** | Sentinel archived (no longer active) | (terminal) |

---

## Behavior

### How It Works

#### Realtime Sentinel Flow

```
1. Signal Exchange publishes event (agent_session_update, etc.)
2. Realtime Sentinel Service receives event
3. OPA policy evaluated on event context
4. If policy condition met, Observation/Exception generated
5. Observation Service publishes to Cronus Gateway
6. Observation routes to Ops Center for human review
```

#### Analytical Sentinel Flow

```
1. Query Scheduler triggers periodic execution (cron-based)
2. SQL template rendered with template variables
3. Query executed on Agent Analytics data mart
4. Results processed for pattern detection
5. If conditions met, Observation/Exception generated
6. Observation Service publishes to Cronus Gateway
```

#### Request Sentinel Flow

```
1. Request created in target workbench
2. Signal Exchange evaluates enrollment filters
3. If filters match, Request Sentinel auto-enrolls
4. Child request created in sentinel's scenario
5. Request Sentinel operates as Employed Agent
6. Sentinel can observe parent request, take actions in child request
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| **Signal Exchange** | → | Realtime: Observes SX events; Request: Auto-enrollment |
| **Agent Analytics** | → | Analytical: Queries data mart |
| **Cronus Gateway** | → | Realtime/Analytical: Publishes Observations/Exceptions |
| **Hub Request Model** | ↔ | Request: Creates child requests, participates in request lifecycle |
| **Seer Operator** | ← | Receives CRD updates, reconciles to Kubernetes state |
| **Sentinel Directory** | ↔ | Registers specs, tracks versions, enables search |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Type-Specific Specs** | Realtime/Analytical sentinels require `policy` and `observation_config`; Request sentinels require `sentinel_scenario_specs` |
| **COG Sentinel Rules** | COG Sentinels (cross-workbench) must be `type: request` and defined in COGW workbench |
| **State Transitions** | Only valid state transitions allowed (Drafted → Validated → Deployed → Suspended/Archived) |
| **Deployment Dependency** | Sentinel must be in Validated state before deployment |
| **Request Sentinel Enrollment** | Request Sentinels only enroll in requests matching scenario filters and OPA update filter policy |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Automated Oversight** | Continuous monitoring without human intervention |
| ✅ **Real-time Detection** | Immediate identification of issues via Realtime Sentinels |
| ✅ **Pattern Detection** | Historical analysis via Analytical Sentinels |
| ✅ **Active Intervention** | Request Sentinels can take corrective actions |
| ✅ **Scalable Governance** | AI-on-AI oversight enables governance at enterprise scale |
| ✅ **Policy Enforcement** | Programmatic enforcement of governance policies |
| ✅ **Audit Trail** | All sentinel actions recorded in request history |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Sentinels Can Overhead** | Sentinels are lightweight; Request Sentinels only enroll when filters match |
| ⚠️ **False Positives** | Policy tuning and observation review process |
| ⚠️ **Request Sentinel Complexity** | Clear documentation and examples for common patterns |
| ⚠️ **Cross-Workbench Coordination** | COG Sentinels provide subscription-wide governance pattern |

---

## Examples

### Example 1: Realtime Sentinel - Stuck Agent Detection

**Use Case**: Detect when agents become stuck (no activity for 5+ minutes)

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: stuck-agent-detector
  namespace: acme-disputes
spec:
  type: realtime
  target:
    workbench_ids: ["acme-disputes"]
    agent_ids: []  # All agents
  
  policy:
    opa_policy: |
      package seer.sentinel.stuck_agent
      
      default allow = false
      
      allow {
        input.event_type == "agent_session_update"
        time.now_ns() - input.last_activity_ns > 300000000000  # 5 minutes
        input.session_status == "active"
      }
  
  observation_config:
    generate_observation:
      condition: "policy_result == true"
      observation_type: "agent_stuck"
      severity: "warning"
    
    generate_exception:
      condition: "policy_result == true AND inactivity_duration > 900000000000"  # 15 minutes
      exception_type: "agent_stuck_critical"
      criticality: "tier-1"
```

**Behavior**: When an agent session has no activity for 5 minutes, generates a warning observation. If inactivity exceeds 15 minutes, generates a critical exception.

---

### Example 2: Analytical Sentinel - Cost Anomaly Detection

**Use Case**: Detect when agent costs exceed thresholds over time periods

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: cost-anomaly-detector
  namespace: acme-disputes
spec:
  type: analytical
  target:
    workbench_ids: ["acme-disputes"]
  
  policy:
    sql_template: |
      SELECT 
        agent_id,
        workbench_id,
        SUM(token_cost) as total_cost,
        AVG(token_cost) as avg_cost
      FROM agent_sessions
      WHERE 
        workbench_id IN {{ .workbench_ids }}
        AND session_timestamp >= NOW() - INTERVAL '1 hour'
      GROUP BY agent_id, workbench_id
      HAVING SUM(token_cost) > 100.00  -- $100 threshold
      ORDER BY total_cost DESC
  
  observation_config:
    generate_observation:
      condition: "result_rows_count > 0"
      observation_type: "cost_anomaly"
      severity: "warning"
```

**Behavior**: Runs every hour, queries analytics data mart for agents exceeding $100 cost threshold, generates observations for review.

---

### Example 3: Request Sentinel - Token Usage Governance

**Use Case**: Monitor token usage across requests and intervene when budgets are exceeded

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: token-usage-governance
  namespace: acme-disputes
spec:
  type: request
  target:
    workbench_ids: ["acme-disputes"]
  
  sentinel_scenario_specs:
    normative_ref:
      name: token-governance-normative
      version: "1.0.0"
    automation_ref:
      name: token-governance-automation
      version: "1.0.0"
    deployment_ref:
      name: token-governance-deployment
      version: "1.0.0"
```

**Automation Spec** (enrollment filters):

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioAutomationSpec
metadata:
  name: token-governance-automation
spec:
  participation:
    mode: observe_and_participate
    filters:
      scenario_whitelist: ["*"]  # All scenarios
      on_request_update:
        enabled: true
        update_filter_policy: |
          allow { 
            input.payload.metrics.token_usage != null 
          }
```

**Behavior**: Auto-enrolls in all requests, monitors token usage metrics, creates child requests when budgets are exceeded to take corrective actions (pause, throttle, escalate).

---

## Implementation Notes

### For Developers

- **Sentinel Spec Structure**: Follow type-specific requirements (Realtime/Analytical use `policy` + `observation_config`; Request uses `sentinel_scenario_specs`)
- **OPA Policy Writing**: Policies receive SX event context; use Rego syntax for policy evaluation
- **SQL Template Variables**: Use Go template syntax (`{{ .variable }}`) for SQL template rendering
- **Request Sentinel Enrollment**: Enrollment filters use OPA policies; ensure filters are specific to avoid unnecessary enrollment

### For Operators

- **Sentinel Lifecycle**: Sentinels must be Validated before deployment; monitor state transitions
- **Observation Review**: Review observations in Ops Center; tune policies based on false positive rates
- **Request Sentinel Limits**: Configure enrollment limits (max concurrent, cooldown) to prevent overload
- **COG Sentinel Management**: COG Sentinels sync to target workbenches as read-only; local admins can enable/disable

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Sentinels](./sentinels.md) | *This document* |
| [Agent Health SLOs](./agent-health-slos.md) | Health SLOs can trigger sentinels on deviations |
| [Agent Analytics](./agent-analytics.md) | Analytical Sentinels query Agent Analytics data mart |
| [Cognitive Operations Governance](./cognitive-operations-governance.md) | COG Sentinels extend Request Sentinels for subscription-wide governance |
| [Request Routing & Ingress](./request-routing-ingress.md) | Request Sentinels enroll via Signal Exchange |
| [Agent Lifecycle](./agent-lifecycle.md) | Sentinels follow same lifecycle pattern as agents |

---

## References

- [Seer Sentinels Subsystem](../subsystems/seer-sentinels/README.md) — Complete subsystem documentation
- [Sentinel Spec Manager](../subsystems/seer-sentinels/sentinel-spec-manager.md) — Spec structure and validation
- [Realtime Sentinel Service](../subsystems/seer-sentinels/realtime-sentinel-service.md) — Event observation and OPA evaluation
- [Analytical Sentinel Service](../subsystems/seer-sentinels/analytical-sentinel-service.md) — SQL template execution
- [Observation Service](../subsystems/seer-sentinels/observation-service.md) — Cronus Observations/Exceptions generation
- [Sentinel Scenario Processing](../hub-integration/sentinel-scenario-processing.md) — Request Sentinel Hub integration
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — SX event source and auto-enrollment
- [Cronus Gateway](../../../olympus-hub-docs/04-subsystems/signal-providers/cronus-business-exceptions.md) — Observations/Exceptions model

---

*Sentinels provide automated oversight and governance for AI agents, enabling scalable monitoring, policy enforcement, and intervention at enterprise scale.*
