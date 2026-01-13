# Using Composite Applications

> **Status:** 🟡 Draft

This guide explains how to create and deploy Hub Composite Applications for multi-agent collaboration patterns.

---

## Overview

Hub Composite Applications enable multiple Hub Applications to participate in the same Request without explicit orchestration. Applications coordinate through shared Request state (blackboard pattern) rather than task assignment.

**Use Cases:**
- **Blackboard Pattern**: Multiple specialists contribute independently
- **PEC Loop**: Planner-Executor-Critic cycles
- **Market-Based**: Agents bid/react to broadcasts
- **Role-Specialized Committees**: Multiple perspectives on decisions

---

## Creating a Composite Application

### Step 1: Define Constituent Applications

First, create the individual Hub Applications that will participate in the composite:

```yaml
# risk-assessment-agent.yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: risk-assessment-agent
  namespace: acme-disputes
spec:
  display_name: "Risk Assessment Agent"
  runtime:
    type: seer
  seerTrainingRef:
    name: risk-analyst-v1
    version: "1.0.0"
```

```yaml
# compliance-check-agent.yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: compliance-check-agent
  namespace: acme-disputes
spec:
  display_name: "Compliance Check Agent"
  runtime:
    type: seer
  seerTrainingRef:
    name: compliance-officer-v1
    version: "1.0.0"
```

### Step 2: Create Composite Application Spec

Create the `HubCompositeApplicationSpec` that groups the applications:

```yaml
# dispute-investigation-composite.yaml
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
  
  applications:
    - name: risk-agent
      ref:
        name: risk-assessment-agent
        version: "1.0.0"
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow { input.update_type == "REQUEST_CREATED" }
          allow { input.update_type == "DOCUMENT_UPLOADED" }
          allow { input.update_type == "TRANSACTION_DATA_ADDED" }
    
    - name: compliance-agent
      ref:
        name: compliance-check-agent
        version: "1.0.0"
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow { input.update_type == "REQUEST_CREATED" }
          allow { input.update_type == "DOCUMENT_UPLOADED" }
          allow { input.update_type == "RISK_ASSESSMENT_COMPLETE" }
  
  metadata:
    topology_pattern: "blackboard"
```

### Step 3: Reference Composite in Scenario Automation Spec

Update your `ScenarioAutomationSpec` to reference the composite:

```yaml
# scenario-automation-spec.yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAutomationSpec
metadata:
  name: dispute-investigation-automation
  namespace: acme-disputes
spec:
  normative_ref:
    name: dispute-investigation-normative
    version: "1.0.0"
  
  application:
    # Use composite_ref instead of ref
    composite_ref:
      name: dispute-investigation-composite
      version: "1.0.0"
  
  triggers:
    - ref: dispute-filed-trigger
      required: true
```

### Step 4: Deploy Scenario

Deploy the scenario as usual. The Composite Deployment Operator will:
1. Resolve the composite (flatten nested composites)
2. Create `HubCompositeApplicationDeployment`
3. Create child `HubApplicationDeployment` for each app
4. Populate routing table with flattened app list + OPA filters

```bash
hub sync scenario dispute-investigation
```

---

## OPA Filter Examples

### Example 1: Update Type Filter (PEC Loop)

**Planner Agent** - Only reacts to request creation and critic feedback:

```rego
package composite.filter

default allow = false

allow {
    input.update_type == "REQUEST_CREATED"
}

allow {
    input.update_type == "CRITIC_FEEDBACK"
}
```

**Executor Agent** - Only reacts to plan creation and critic feedback:

```rego
package composite.filter

default allow = false

allow {
    input.update_type == "PLAN_CREATED"
}

allow {
    input.update_type == "CRITIC_FEEDBACK"
}
```

**Critic Agent** - Only reacts to execution completion and plan creation:

```rego
package composite.filter

default allow = false

allow {
    input.update_type == "EXECUTION_COMPLETE"
}

allow {
    input.update_type == "PLAN_CREATED"
}
```

### Example 2: State-Based Filter (Blackboard)

**Risk Agent** - Only processes when risk data is available:

```rego
package composite.filter

default allow = false

allow {
    input.update_type == "REQUEST_CREATED"
}

allow {
    input.update_type == "DOCUMENT_UPLOADED"
}

allow {
    input.update_type == "TRANSACTION_DATA_ADDED"
}

# Only process if request has transaction data
allow {
    input.update_type == "STATE_UPDATE"
    input.request_state.metadata.transaction_id != null
}
```

### Example 3: Time-Based Filter

**Business Hours Agent** - Only processes during business hours:

```rego
package composite.filter

import rego.v1

default allow = false

allow {
    input.update_type == "REQUEST_CREATED"
    hour := time.clock(input.timestamp)[0]
    hour >= 9
    hour < 17
}

allow {
    input.update_type == "STATE_UPDATE"
    hour := time.clock(input.timestamp)[0]
    hour >= 9
    hour < 17
}
```

### Example 4: Payload-Based Filter (Market-Based)

**Product Specialist** - Only bids on product-related inquiries:

```rego
package composite.filter

default allow = false

allow {
    input.update_type == "INQUIRY_BROADCAST"
    contains(input.update_payload.inquiry_text, "product")
}

allow {
    input.update_type == "INQUIRY_BROADCAST"
    contains(input.update_payload.inquiry_text, "catalog")
}

allow {
    input.update_type == "TASK_ASSIGNED"
    input.update_payload.task.category == "product"
}
```

---

## OPA Filter Input Structure

Filters receive the following input structure:

```json
{
  "update_type": "REQUEST_CREATED",
  "request_state": {
    "id": "req-123",
    "status": "ACTIVE",
    "scenario_id": "dispute-investigation",
    "workbench_id": "acme-disputes",
    "created_at": "2026-01-15T10:00:00Z",
    "metadata": {
      "transaction_id": "txn-456",
      "customer_id": "cust-789"
    }
  },
  "update_payload": {
    "memo": "Dispute filed by customer",
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

---

## Deployment Workflow

### 1. Create Application Specs

```bash
# Create individual applications
hub apply -f risk-assessment-agent.yaml
hub apply -f compliance-check-agent.yaml
```

### 2. Create Composite Spec

```bash
hub apply -f dispute-investigation-composite.yaml
```

### 3. Create Scenario Automation Spec

```bash
hub apply -f scenario-automation-spec.yaml
```

### 4. Create Scenario Deployment Spec

```yaml
# scenario-deployment-spec.yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioDeploymentSpec
metadata:
  name: dispute-investigation-deployment
  namespace: acme-disputes
spec:
  automation_ref:
    name: dispute-investigation-automation
    version: "1.0.0"
  workbenchInstance:
    name: acme-disputes-sandbox
  activation:
    status: active
```

```bash
hub apply -f scenario-deployment-spec.yaml
```

### 5. Sync Scenario

```bash
hub sync scenario dispute-investigation
```

This triggers:
- Composite Deployment Operator creates `HubCompositeApplicationDeployment`
- Child `HubApplicationDeployment` resources created
- Routing table populated with app list + filters

---

## Troubleshooting

### Composite Deployment Fails

**Symptom**: `HubCompositeApplicationDeployment` status shows `Failed`

**Check**:
1. All referenced `HubApplicationSpec` resources exist
2. No circular references in nested composites
3. OPA filter syntax is valid
4. All child deployments succeeded

**Resolution**:
- Fix the failing child deployment
- Composite will automatically retry when child succeeds

### App Not Receiving Updates

**Symptom**: One app in composite doesn't receive updates

**Check**:
1. OPA filter is too restrictive
2. Filter syntax error (check operator logs)
3. App deployment is in `Active` state

**Resolution**:
- Review OPA filter policy
- Test filter with sample input
- Check Application Router logs for filter evaluation results

### Update Conflicts

**Symptom**: Multiple apps updating same request state causes conflicts

**Behavior**: Latest update wins (timestamp-based). Rejected updates recorded in request history.

**Resolution**:
- Design apps to update different aspects of request
- Use OPA policies to prevent illegal state transitions
- Review request history to understand conflicts

---

## Best Practices

1. **Filter Design**: Keep filters simple and focused on `update_type` when possible
2. **Naming**: Use descriptive names for apps in composite (e.g., `risk-agent`, not `app1`)
3. **Testing**: Test OPA filters independently before deploying composite
4. **Observability**: Monitor request history to see which apps contributed updates
5. **Conflict Avoidance**: Design apps to update different aspects of request state

---

## Related Documentation

- [Hub Composite Application](../../02-system-design/implementation-concepts/hub-composite-application.md) - Concept documentation
- [ADR-0125: Hub Composite Applications](../../decision-logs/0125-hub-composite-applications.md) - Design decision
- [ADR-0126: Composite Routing Table Schema](../../decision-logs/0126-composite-routing-table-schema.md) - Routing schema
- [Multi-Agent Topologies](../../../olympus-seer-docs/agentic-ai-concepts/multi-agent-topologies.md) - Topology patterns

---

*Composite Applications enable sophisticated multi-agent collaboration while maintaining Hub's request-level governance and observability.*
