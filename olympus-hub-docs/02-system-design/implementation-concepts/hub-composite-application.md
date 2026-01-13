# Hub Composite Application

> **Category:** Application Architecture

---

## Overview

A **Hub Composite Application** enables multiple Hub Applications to participate in the same Request without explicit orchestration. Applications coordinate through shared Request state (blackboard pattern) rather than task assignment, supporting multi-agent topologies like Blackboard, Planner-Executor-Critic (PEC Loop), Market-Based, and Role-Specialized Committees.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Automation** as the blueprint for how an Operation should run. Hub Composite Application extends this by allowing multiple Automations to participate in the same Operation (Request) instance.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Automation | Hub Application code/config | Each constituent app is an Automation |
| Automation Runtime | Atlantis, Rhea, Seer, Perseus | Apps can span multiple runtimes |
| Operation | Request instance | Multiple apps operate on same Request |

### Gap This Fills

Standard Hub Applications support single-app-per-scenario patterns. Composite Applications enable:
1. **Multi-agent topologies** without explicit orchestrators
2. **Parallel perspectives** on the same request (risk, compliance, customer service)
3. **Event-driven coordination** through shared state rather than task assignment
4. **Cross-runtime composition** (Seer + Rhea + Atlantis in one composite)

---

## Definition

**Hub Composite Application** is a specification that groups multiple Hub Applications to participate in the same Request. Each application:
- Receives Request Updates from Signal Exchange (subject to OPA filters)
- Operates independently with its own session
- Can create tasks, produce updates, and modify request state
- Coordinates implicitly through shared Request state (blackboard pattern)

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-scoped; belongs to exactly one Workbench |
| **Lifecycle** | Deployed via Composite Deployment Operator; all-or-nothing deployment |
| **Ownership** | Developer creates; Supervisor manages runtime configuration |
| **Multiplicity** | One Workbench can have many Composite Applications |
| **Resolution** | Resolved at deployment time; Signal Exchange sees flattened app list |

---

## Rationale

### Why This Design?

Composite Applications enable multi-agent collaboration patterns that are difficult or impossible with single-app scenarios:

1. **Blackboard Pattern**: Multiple specialists contribute independently to shared state
2. **PEC Loop**: Planner-Executor-Critic cycles without explicit orchestration
3. **Market-Based**: Agents bid/react to broadcasts without central scheduler
4. **Role-Specialized Committees**: Multiple perspectives on high-stakes decisions

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Task-based coordination** | Requires explicit orchestrator; doesn't support event-driven patterns |
| **Workflow orchestration** | Too rigid; doesn't support dynamic multi-agent topologies |
| **Message bus with subscriptions** | Too low-level; loses Hub's request context and governance |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0125](../decision-logs/0125-hub-composite-applications.md) | Hub Composite Application design decision |
| [ADR-0126](../decision-logs/0126-composite-routing-table-schema.md) | Routing table multi-app schema |
| [ADR-0007](../decision-logs/0007-composite-pattern-technology-agnostic.md) | Hub Applications can be any technology |

---

## Structure

### Hub Composite Application Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: HubCompositeApplicationSpec
metadata:
  name: dispute-investigation-composite
  namespace: acme-disputes
  labels:
    hub.olympus.io/workbench: acme-disputes
spec:
  display_name: "Dispute Investigation Composite"
  description: "Multi-agent composite for dispute resolution"
  
  # Constituent applications
  applications:
    - name: risk-agent  # Local identifier within composite
      ref:
        name: risk-assessment-agent
        version: "1.0.0"
      # Optional OPA filter for update routing
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow { input.update_type == "REQUEST_CREATED" }
          allow { input.update_type == "DOCUMENT_UPLOADED" }
    
    - name: compliance-agent
      ref:
        name: compliance-check-agent
        version: "1.0.0"
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow { input.update_type in ["REQUEST_CREATED", "RISK_ASSESSMENT_COMPLETE"] }
    
    # Nested composite reference
    - name: customer-service-composite
      composite_ref:
        name: customer-service-composite
        version: "1.0.0"
  
  metadata:
    topology_pattern: "blackboard"  # blackboard | pec_loop | market_based | committee
```

### Hub Composite Application Deployment

```yaml
apiVersion: hub.olympus.io/v1
kind: HubCompositeApplicationDeployment
metadata:
  name: dispute-investigation-composite-sandbox
  namespace: acme-disputes
  labels:
    hub.olympus.io/workbench-instance: acme-disputes-sandbox
spec:
  compositeRef:
    name: dispute-investigation-composite
    version: "1.0.0"
  workbenchInstance:
    name: acme-disputes-sandbox

status:
  phase: Running  # Pending | Deploying | Running | Failed | Terminating
  
  # Child deployment status
  applicationDeployments:
    - name: risk-agent
      deploymentRef: risk-agent-deployment-sandbox
      phase: Running
    - name: compliance-agent
      deploymentRef: compliance-agent-deployment-sandbox
      phase: Running
```

**Ownership**: `HubCompositeApplicationDeployment` owns child `HubApplicationDeployment` resources via `ownerReference`.

---

## Behavior

### Deployment-Time Resolution

Composites are resolved at deployment time by the Composite Deployment Operator:

1. **Recursive Resolution**: Flattens nested composites to union of all apps
2. **Child Deployment Creation**: Creates `HubApplicationDeployment` for each app
3. **Routing Table Population**: Populates routing table with flattened app list + OPA filters

Signal Exchange doesn't know about composites - it just sees "Scenario X has apps [A, B, C] with filters [F1, F2, F3]".

### Request Update Routing

When a Request Update arrives:

1. **Application Router** looks up scenario in routing table
2. If scenario has multiple apps (composite):
   - For each app, evaluate OPA filter
   - If filter allows, dispatch update to app
3. If scenario has single app (standard):
   - Existing behavior (direct dispatch)

### OPA Filter Input Structure

Filters receive full context for evaluation:

```json
{
  "update_type": "REQUEST_CREATED",
  "request_state": {
    "id": "req-123",
    "status": "ACTIVE",
    "scenario_id": "dispute-investigation",
    "workbench_id": "acme-disputes",
    "created_at": "2026-01-15T10:00:00Z"
  },
  "update_payload": {
    "memo": "...",
    "task_lifecycle": {...},
    "decision_records": [...]
  },
  "timestamp": "2026-01-15T10:05:00Z",
  "app_identity": {
    "name": "risk-agent",
    "deployment_id": "risk-agent-deployment-sandbox"
  }
}
```

### Update Conflict Resolution

Multiple apps can update the same request concurrently:
- **Latest wins**: Timestamp-based resolution
- **Illegal updates rejected**: OPA policy determines legality
- **Rejected updates recorded**: History includes rejection reason and source app

---

## Use Cases

### Example 1: Planner-Executor-Critic (PEC Loop)

**Scenario**: High-Value Transaction Approval

**Composite Apps**:
- **Planner Agent** (Seer): Creates approval plan
- **Executor Agent** (Seer): Executes plan
- **Critic Agent** (Seer): Evaluates outcomes

**OPA Filters**:
- Planner: `update_type in ["REQUEST_CREATED", "CRITIC_FEEDBACK"]`
- Executor: `update_type in ["PLAN_CREATED", "CRITIC_FEEDBACK"]`
- Critic: `update_type in ["EXECUTION_COMPLETE", "PLAN_CREATED"]`

**Use Case**: Safety-sensitive actions requiring verification loops

### Example 2: Blackboard (Shared Memory Coordination)

**Scenario**: Complex Dispute Investigation

**Composite Apps**:
- **Risk Agent** (Seer): Fraud pattern evaluation
- **Compliance Agent** (Seer): Regulatory compliance check
- **Customer Service Agent** (Seer): Customer communication
- **Document Analyzer** (Atlantis): Document extraction

**OPA Filters**:
- Risk Agent: `update_type in ["REQUEST_CREATED", "DOCUMENT_UPLOADED"]`
- Compliance Agent: `update_type in ["REQUEST_CREATED", "RISK_ASSESSMENT_COMPLETE"]`
- Document Analyzer: `update_type == "DOCUMENT_UPLOADED"`

**Use Case**: Multi-specialist collaboration on knowledge-centric cases

### Example 3: Market-Based / Auction

**Scenario**: Dynamic Task Routing

**Composite Apps**:
- **Inquiry Router** (Rhea): Broadcasts inquiries
- **Product Specialist** (Seer): Bids on product inquiries
- **Technical Support** (Seer): Bids on technical issues
- **Task Assigner** (Atlantis): Evaluates bids, assigns tasks

**Use Case**: Dynamic resource allocation and load balancing

### Example 4: Role-Specialized Committees

**Scenario**: Credit Committee Decision

**Composite Apps**:
- **Risk Analyst** (Seer): Credit risk evaluation
- **Compliance Officer** (Seer): Regulatory compliance
- **Relationship Manager** (Seer): Customer relationship value
- **Coordinator** (Rhea): Aggregates perspectives

**Use Case**: High-stakes decisions requiring multiple perspectives

---

## Relationship to Multi-Agent Topologies

Hub Composite Applications support several multi-agent topologies documented in [Multi-Agent Topologies](../../../olympus-seer-docs/agentic-ai-concepts/multi-agent-topologies.md):

| Topology | Support | Notes |
|----------|---------|-------|
| **Blackboard** | ✅ Full | Shared state coordination via Request |
| **PEC Loop** | ✅ Full | Planner-Executor-Critic via update types |
| **Market-Based** | ✅ Full | Broadcast and bid via request updates |
| **Role-Specialized Committees** | ✅ Full | Multiple perspectives on same request |
| **Manager-Worker** | ⚠️ Partial | Requires explicit orchestrator (not composite) |
| **Hierarchical** | ⚠️ Partial | Requires explicit hierarchy (not composite) |

---

## Related Documentation

- [Hub Application](./hub-application.md) - Single application pattern
- [Hub Application Deployment](./hub-application-deployment.md) - Deployment model
- [Application Router](../../04-subsystems/signal-exchange/application-router.md) - Routing logic
- [Using Composite Applications](../../10-guides/using-composite-applications.md) - Developer guide
- [Multi-Agent Topologies](../../../olympus-seer-docs/agentic-ai-concepts/multi-agent-topologies.md) - Topology patterns

---

*Composite Applications enable sophisticated multi-agent collaboration while maintaining Hub's request-level governance and observability.*
