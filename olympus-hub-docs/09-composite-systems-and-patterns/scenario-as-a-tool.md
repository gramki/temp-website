# Scenario as a Tool

> **Status:** ✅ Documented — Core concepts defined

## Overview

A **Scenario can be exposed as a Tool** that Hub Applications can invoke directly. This pattern transforms a Scenario's HTTP signals into callable operations, enabling reuse of complex automation as simple tool invocations.

| Aspect | Description |
|--------|-------------|
| **Pattern Type** | Composition |
| **Primary Actors** | Developer, Hub Applications |
| **Key Benefit** | Reuse Scenario automation as callable procedures |
| **Complexity** | Low (when within same workbench) to Medium (cross-workbench) |

---

## The Premise

### Why Expose a Scenario as a Tool?

Scenarios encapsulate complex business processes with:
- Defined inputs (signals)
- Orchestrated workflows
- Multiple participants and tasks
- Well-defined outcomes

Sometimes you need to **invoke that capability programmatically** from another Hub Application without creating a formal Request lifecycle.

| Use Case | Example |
|----------|---------|
| **Reusable procedures** | "Check eligibility" logic used across multiple Scenarios |
| **Cross-domain operations** | Customer Service invoking Dispute Resolution |
| **Hybrid workflows** | Combining tool invocations with Request-based flows |

---

## Granularity Model

> **Key Decision:** [ADR-0042: Scenario as Tool Granularity](../decision-logs/0042-scenario-as-tool-granularity.md)

When exposing a Scenario as a Tool:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SCENARIO AS TOOL — GRANULARITY                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SCENARIO: "Dispute Resolution"                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   HTTP Signals:                                                      │   │
│   │   • dispute.submitted                                                │   │
│   │   • dispute.evidence.submitted                                       │   │
│   │   • dispute.status.query                                             │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│   EXPOSED AS TOOL: "dispute-resolution"                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   Operations (one per HTTP signal):                                  │   │
│   │   • create       ──▶ dispute.submitted                               │   │
│   │   • add-evidence ──▶ dispute.evidence.submitted                      │   │
│   │   • get-status   ──▶ dispute.status.query                            │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ONE TOOL with MULTIPLE OPERATIONS (prevents tool explosion)               │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Rules

- **Entire Scenario = One Tool** with a unified identity
- **Each HTTP Signal = One Operation** within that tool
- Operations are parameterized invocations of the same tool
- This maintains discoverability without overwhelming tool catalogs

---

## Usage Contexts

### Context 1: Within Same Workbench

A Hub Application in Workbench-A calls a Scenario in Workbench-A as a tool.

**How it works:**
1. Scenario is registered as a tool in the workbench's Tool Registry
2. Hub Application invokes via Direct Tool Dispatcher
3. Signal is sent to the Scenario, **child request** created
4. Child request has access to parent's context (by reference)
5. Response returned to invoking application

**Request Hierarchy:**

| Aspect | Behavior |
|--------|----------|
| **Child Request** | Created with `parent_request_id` linking to invoker's request |
| **Context Access** | Child can access parent context via compiled-context API |
| **Lifecycle** | Child is completed/cancelled when parent completes/cancels |
| **Result Isolation** | Child context is isolated — only result payload returns to parent |

→ See: [Request Hierarchy](../04-subsystems/request-management/request-hierarchy.md)

**Configuration:** Use `ScenarioAsTool` CRD directly.

→ See: [ScenarioAsTool CRD](#scenarioastool-crd) below

---

### Context 2: Cross-Workbench (via Machine)

A Hub Application in Workbench-A calls a Scenario in Workbench-B.

**How it works:**
1. Workbench-B is published as a Machine
2. Scenario is exposed as one of the Machine's tools
3. Workbench-A registers Workbench-B as a Machine
4. Hub Application invokes via Machine interface
5. A **separate request** is created in Workbench-B (NOT a child request)

**No Parent-Child Relationship:**

| Aspect | Behavior |
|--------|----------|
| **Request Relationship** | None — treated as external machine/tool invocation |
| **Context Sharing** | None implicit — invoker must explicitly forward context |
| **Lifecycle** | Independent — no cascade on parent completion/cancellation |
| **Contract** | Invoker provides context per recipient's tool contract |

```python
# Cross-workbench invocation — must explicitly forward context
result = await machine_client.invoke(
    machine="customer-service-workbench",
    tool="eligibility-check",
    input={
        "customer_id": "cust-12345",
        # Explicitly forwarded context (per tool contract)
        "context": {
            "case_id": current_request.id,
            "priority": "high"
        }
    }
)
```

**Configuration:** Use `WorkbenchAsMachine` CRD with `exposed_tools.scenarios`.

→ See: [Workbench as a Machine](./workbench-as-a-machine.md) for complete pattern

---

## ScenarioAsTool CRD

For exposing a Scenario as a tool within the same workbench:

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAsTool
metadata:
  name: dispute-resolution-tool
  namespace: acme-bank
spec:
  # Source Scenario
  scenario_ref: standard-dispute
  
  # Tool Identity
  tool:
    name: dispute-resolution
    display_name: "Dispute Resolution"
    version: "1.0.0"
    description: "Create and manage customer disputes"
  
  # Operations (map signals to tool operations)
  operations:
    - signal_type: dispute.submitted
      operation:
        name: create
        description: "Create a new dispute"
        input_schema:
          type: object
          properties:
            customer_id:
              type: string
            transaction_id:
              type: string
            amount:
              type: number
            dispute_type:
              type: string
              enum: [unauthorized, duplicate, not_received]
          required: [customer_id, transaction_id, amount, dispute_type]
        output_schema:
          type: object
          properties:
            dispute_id:
              type: string
            status:
              type: string
    
    - signal_type: dispute.evidence.submitted
      operation:
        name: add-evidence
        description: "Add evidence to existing dispute"
        input_schema:
          type: object
          properties:
            dispute_id:
              type: string
            evidence_type:
              type: string
            evidence_data:
              type: object
          required: [dispute_id, evidence_type]
    
    - signal_type: dispute.status.query
      operation:
        name: get-status
        description: "Query dispute status"
        input_schema:
          type: object
          properties:
            dispute_id:
              type: string
          required: [dispute_id]
        output_schema:
          type: object
          properties:
            dispute_id:
              type: string
            status:
              type: string
            last_updated:
              type: string
  
  # Access Control
  access:
    allowed_applications:
      - customer-service-app
      - fraud-detection-app
    allowed_roles:
      - dispute-operator
```

### Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `scenario_ref` | Yes | Reference to source Scenario |
| `tool.name` | Yes | Tool identifier (used in invocations) |
| `tool.display_name` | Yes | Human-readable name |
| `tool.version` | Yes | Semantic version |
| `operations[]` | Yes | List of operations to expose |
| `operations[].signal_type` | Yes | HTTP signal type this operation maps to |
| `operations[].operation.name` | Yes | Operation identifier |
| `operations[].operation.input_schema` | No | JSON Schema for input validation |
| `operations[].operation.output_schema` | No | JSON Schema for output documentation |
| `access` | No | Access control configuration |

---

## Invocation

### From Hub Application

```python
# Example: Invoking Scenario as Tool from another Hub Application

class CustomerServiceApp:
    def __init__(self, tool_client):
        self.tool_client = tool_client
    
    async def handle_dispute_request(self, customer_id: str, transaction_id: str):
        # Invoke the "dispute-resolution" tool, "create" operation
        result = await self.tool_client.invoke(
            tool="dispute-resolution",
            operation="create",
            input={
                "customer_id": customer_id,
                "transaction_id": transaction_id,
                "amount": 150.00,
                "dispute_type": "unauthorized"
            }
        )
        
        if result.success:
            dispute_id = result.output["dispute_id"]
            return {"message": f"Dispute {dispute_id} created successfully"}
        else:
            return {"error": result.error}
```

### Response Contract

When invoked as a tool, the Scenario returns a **tool-native response** (not a Request Update DTO):

```json
{
  "success": true,
  "output": {
    "dispute_id": "DSP-2026-001234",
    "status": "SUBMITTED",
    "created_at": "2026-01-06T15:30:00Z"
  }
}
```

---

## When to Use

### ✅ Use Scenario as Tool When:

- You need **synchronous, request-response** interaction
- The Scenario represents a **reusable procedure**
- You want to **avoid Request lifecycle overhead**
- Cross-application **code reuse** is valuable

### ❌ Avoid When:

- You need **long-running orchestration** with human tasks
- The process requires **asynchronous updates** and notifications
- You need **full Request context** (memos, history, actors)
- The process involves **task queues and escalation**

---

## Related Patterns

| Pattern | Relationship |
|---------|--------------|
| [Workbench as a Machine](./workbench-as-a-machine.md) | Scenario as Tool is one tool type exposed by a Machine |
| [Hub Application as Standalone Tool](./hub-application-as-standalone-tool.md) | Similar pattern for Hub Applications instead of Scenarios |
| [Scenario as an Agent](./scenario-as-an-agent.md) | Alternative: Scenario participates in task queues instead of being invoked as tool |

---

## Related Documentation

- [ADR-0042: Scenario as Tool Granularity](../decision-logs/0042-scenario-as-tool-granularity.md)
- [Developer Operators](../04-subsystems/operators/developer-operators.md) — ScenarioAsTool CRD
- [Direct Tool Dispatcher](../04-subsystems/hub-native-utilities/direct-tool-dispatcher.md)
- [Signal Exchange](../04-subsystems/signal-exchange/README.md) — HTTP Signals

