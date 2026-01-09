# Workbench as a Machine

> **Status:** 🟡 Draft — Architecture defined

## Overview

A **Workbench can be published as a Machine** that other Workbenches can consume. This enables cross-workbench tool invocation where one workbench exposes its capabilities (Scenarios as Tools, Standalone Tools, Machine Tools) as a cohesive Machine interface.

This pattern provides:
- **Cross-workbench integration** without tight coupling
- **Transitive tool access** — expose tools from machines within the workbench
- **Unified machine interface** for all workbench capabilities
- **Direct tool invocation** bypassing SX/Request overhead

> **Note:** Cross-workbench invocations do **NOT** create parent-child request relationships. Context must be explicitly forwarded per the tool's contract. See [Request Hierarchy](../04-subsystems/request-management/request-hierarchy.md).

---

## The Premise

### Why Workbench as a Machine?

Enterprises have multiple workbenches serving different domains (Dispute Operations, Fraud Investigation, Customer Service). These domains often need to invoke each other's capabilities:

| Without This Pattern | With This Pattern |
|---------------------|-------------------|
| Each integration is custom | Standardized Machine interface |
| Direct coupling between applications | Loose coupling via Machine abstraction |
| Complex credential management | Unified access control |
| No visibility into available tools | Discoverable tool catalog |

### The Value

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              WORKBENCH AS A MACHINE — VALUE PROPOSITION                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   CUSTOMER SERVICE                      DISPUTE OPERATIONS                   │
│   WORKBENCH (WB-A)                      WORKBENCH (WB-B as Machine)         │
│   ┌─────────────────────────────┐       ┌─────────────────────────────┐     │
│   │                             │       │                             │     │
│   │   Customer Service App      │       │   ┌───────────────────────┐ │     │
│   │   ┌───────────────────────┐ │       │   │   EXPOSED TOOLS       │ │     │
│   │   │                       │ │       │   │                       │ │     │
│   │   │ "I need to check if   │ │ ────> │   │ • create-dispute      │ │     │
│   │   │  customer can file a  │ │       │   │   (Scenario as Tool)  │ │     │
│   │   │  dispute and create   │ │       │   │                       │ │     │
│   │   │  it if eligible"      │ │ ────> │   │ • check-eligibility   │ │     │
│   │   │                       │ │       │   │   (Standalone Tool)   │ │     │
│   │   └───────────────────────┘ │       │   │                       │ │     │
│   │                             │ <──── │   │ • get-transaction     │ │     │
│   │   Uses WB-B as a Machine    │       │   │   (Machine Tool)      │ │     │
│   │                             │       │   │                       │ │     │
│   └─────────────────────────────┘       │   └───────────────────────┘ │     │
│                                          │                             │     │
│                                          │   Published as Machine      │     │
│                                          │   "dispute-operations"      │     │
│                                          └─────────────────────────────┘     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## How It Works

### Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WORKBENCH AS A MACHINE — ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   CONSUMING WORKBENCH (WB-A)                                                │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   Hub Application                                                    │   │
│   │         │                                                            │   │
│   │         │ invoke tool: "dispute-ops/create-dispute"                  │   │
│   │         ▼                                                            │   │
│   │   Tool Registry (resolve machine: dispute-ops)                       │   │
│   │         │                                                            │   │
│   │         │ Machine endpoint: https://heracles.hub/.../dispute-ops     │   │
│   │         ▼                                                            │   │
│   │   Direct Tool Dispatcher                                             │   │
│   │         │                                                            │   │
│   └─────────┼────────────────────────────────────────────────────────────┘   │
│             │                                                                │
│             │ HTTP Request (with credentials)                                │
│             ▼                                                                │
│                                                                              │
│   PROVIDING WORKBENCH (WB-B as Machine)                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   HTTP I/O Gateway (Heracles)                                        │   │
│   │         │                                                            │   │
│   │         │ Authenticate, route to tool                                │   │
│   │         ▼                                                            │   │
│   │   Direct Tool Dispatcher                                             │   │
│   │         │                                                            │   │
│   │         │ Route to appropriate tool type                             │   │
│   │         ├─────────────────┬─────────────────┬────────────────────┐   │   │
│   │         ▼                 ▼                 ▼                    ▼   │   │
│   │   ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐  │   │
│   │   │ Scenarios │   │ Standalone│   │ Machine   │   │ Decision  │  │   │
│   │   │ as Tools  │   │ Tools     │   │ Tools     │   │ Tools     │  │   │
│   │   └───────────┘   └───────────┘   └───────────┘   └───────────┘  │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Tool Types Exposed

A Workbench-as-Machine can expose multiple types of tools:

| Tool Type | Description | Source |
|-----------|-------------|--------|
| **Scenarios as Tools** | Entire Scenarios with HTTP signals exposed as operations | Scenario Automation Spec |
| **Standalone Tools** | Hub Applications registered as standalone tools | ToolInstance with machine.type: standalone |
| **Machine Tools** | Tools from external machines used by this workbench | ToolInstance with external machine_ref |
| **Decision Tools** | Stateless decision/prediction tools | Decision/Prediction Tool Specs |

### Scenario as Tool — Granularity

When exposing a Scenario as a Tool:

- **Entire Scenario = One Tool** with multiple operations
- **Each HTTP Signal = One Operation** of that tool
- This prevents tool explosion while maintaining discoverability

```yaml
# Example: Dispute Scenario exposed as a Tool
tool:
  name: dispute-resolution
  display_name: "Dispute Resolution"
  operations:
    - name: create-dispute
      description: "Create a new dispute"
      signal_type: dispute.submitted
      
    - name: add-evidence
      description: "Add evidence to existing dispute"
      signal_type: dispute.evidence.submitted
      
    - name: get-status
      description: "Get dispute status"
      signal_type: dispute.status.query
```

---

## Implementation Guide

### Phase 1: Define Machine Specification (Publishing Time)

The Process Architect/Developer defines what the workbench will expose as a machine:

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchAsMachine
metadata:
  name: dispute-ops-machine
  namespace: acme-bank
spec:
  # Source Workbench
  workbench_ref: dispute-operations

  # Machine Identity
  machine:
    id: dispute-operations
    display_name: "Dispute Operations Service"
    version: "2.0.0"
    description: "Dispute resolution capabilities for enterprise use"

  # Machine Capabilities
  capabilities:
    produces_signals: false    # Machine doesn't emit signals to consumers
    accepts_commands: true     # Machine can receive tool invocations
    provides_data: true        # Machine can return data

  # Tools to Expose
  exposed_tools:
    
    # Scenario as Tool (entire scenario with operations)
    scenarios:
      - scenario_ref: standard-dispute
        tool:
          name: dispute-resolution
          display_name: "Dispute Resolution"
          description: "Create and manage disputes"
        operations:
          - signal_type: dispute.submitted
            operation_name: create
            description: "Create a new dispute"
            input_mapping:
              customer_id: "{{input.customer_id}}"
              transaction_id: "{{input.transaction_id}}"
              amount: "{{input.amount}}"
              type: "{{input.dispute_type}}"
            output_mapping:
              dispute_id: "{{request.id}}"
              status: "{{request.state}}"
              
          - signal_type: dispute.evidence.submitted
            operation_name: add-evidence
            description: "Add evidence to existing dispute"
            input_mapping:
              dispute_id: "{{input.dispute_id}}"
              evidence: "{{input.evidence}}"
              
          - signal_type: dispute.status.query
            operation_name: get-status
            description: "Get dispute status"
            input_mapping:
              dispute_id: "{{input.dispute_id}}"
    
    # Standalone Tools (Hub Applications as tools)
    standalone_tools:
      - tool_ref: fraud-detection-tool
        exposed_name: fraud-check
        description: "Check transaction for fraud risk"
        
      - tool_ref: eligibility-check-tool
        exposed_name: dispute-eligibility
        description: "Check if transaction is eligible for dispute"
    
    # Machine Tools (transitive exposure)
    machine_tools:
      - tool_ref: core-banking/get-transaction
        exposed_name: get-transaction
        description: "Get transaction details"
        # Note: credentials are resolved at invocation time
        
      - tool_ref: card-network/get-chargeback-status
        exposed_name: chargeback-status
        description: "Get chargeback status from card network"
    
    # Decision Tools
    decision_tools:
      - tool_ref: dispute-classification-rules
        exposed_name: classify-dispute
        description: "Classify dispute type based on transaction"

  # Access Control
  access_control:
    # Which workbenches can use this machine
    allowed_workbenches:
      - customer-service
      - fraud-investigation
      - mobile-banking
    
    # Role-based access
    allowed_roles:
      - service-operator
      - analyst
    
    # OPA policy for fine-grained control
    opa_policy_ref: policies/dispute-machine-access

  # Authentication for incoming requests
  authentication:
    methods:
      - type: oauth2_client_credentials
        issuer: https://auth.hub.acme.com
      - type: api_key
        header: X-API-Key
```

### Phase 2: Register Machine Instance (Deployment Time)

When the workbench is deployed, a concrete Machine Instance is registered:

```yaml
apiVersion: hub.olympus.io/v1
kind: MachineInstance
metadata:
  name: dispute-ops-prod
  namespace: acme-bank
spec:
  # Reference to Machine Definition
  definition_ref: dispute-ops-machine
  
  # Instance Identity
  instance:
    id: dispute-ops-prod
    display_name: "Dispute Operations (Production)"
    environment: production
  
  # Endpoints
  endpoints:
    primary:
      url: https://heracles.hub.acme.com/machines/dispute-ops
      region: us-east-1
    failover:
      url: https://heracles.hub.acme.com/machines/dispute-ops
      region: us-west-2
  
  # Credentials for this instance
  credentials:
    type: oauth2_client_credentials
    client_id_env: DISPUTE_OPS_CLIENT_ID
    client_secret_env: DISPUTE_OPS_CLIENT_SECRET
  
  # Health check
  health:
    endpoint: /health
    interval_seconds: 30
    
  # Rate limits
  rate_limits:
    requests_per_minute: 1000
    burst: 100
```

### Phase 3: Consume from Other Workbenches

Hub Applications in other workbenches can now use the machine:

```python
# In Customer Service Workbench

class CustomerServiceApp:
    
    async def handle_dispute_request(self, request: Request):
        customer_id = request.payload.get("customer_id")
        transaction_id = request.payload.get("transaction_id")
        
        # Step 1: Check eligibility (Standalone Tool)
        eligibility = await tools.invoke(
            tool_id="dispute-ops/dispute-eligibility",
            params={
                "customer_id": customer_id,
                "transaction_id": transaction_id
            }
        )
        
        if not eligibility["eligible"]:
            return RequestUpdate(
                status="COMPLETED",
                outcome="REJECTED",
                memo=f"Not eligible: {eligibility['reason']}"
            )
        
        # Step 2: Check fraud risk (Standalone Tool)
        fraud_check = await tools.invoke(
            tool_id="dispute-ops/fraud-check",
            params={"transaction_id": transaction_id}
        )
        
        # Step 3: Create dispute (Scenario as Tool)
        dispute = await tools.invoke(
            tool_id="dispute-ops/dispute-resolution",
            operation="create",
            params={
                "customer_id": customer_id,
                "transaction_id": transaction_id,
                "amount": request.payload.get("amount"),
                "dispute_type": eligibility["recommended_type"],
                "fraud_risk": fraud_check["risk_score"]
            }
        )
        
        return RequestUpdate(
            status="COMPLETED",
            outcome="SUCCESS",
            payload={
                "dispute_id": dispute["dispute_id"],
                "dispute_status": dispute["status"]
            }
        )
```

---

## Invocation Flow

### Cross-Workbench Tool Invocation

```
WB-A (Customer Service)                                WB-B (Dispute Ops)
Hub Application                                        
       │                                                      
       │ invoke: "dispute-ops/dispute-eligibility"           
       ▼                                                      
Tool Registry (WB-A)                                         
       │                                                      
       │ Resolve: Machine "dispute-ops" is WB-B              
       │ Get endpoint: https://heracles.../dispute-ops       
       ▼                                                      
Direct Tool Dispatcher (WB-A)                                
       │                                                      
       │ Resolve credentials:                                 
       │   - Pass-through: Forward WB-A App's token          
       │   - OR Configured: Use WB-A's client credentials    
       ▼                                                      
                        │                                     
                        │ HTTP POST /tools/dispute-eligibility
                        │ Authorization: Bearer {token}       
                        ▼                                     
                                           HTTP I/O Gateway (Heracles)
                                                  │
                                                  │ Authenticate caller
                                                  │ (WB-B validates WB-A's token)
                                                  ▼
                                           Direct Tool Dispatcher (WB-B)
                                                  │
                                                  │ Access control check
                                                  │ Route to tool
                                                  ▼
                                           Standalone Tool
                                           (eligibility-check-tool)
                                                  │
                                                  │ Execute logic
                                                  ▼
       │                                   Tool Response
       │ <──────────────────────────────────────────
       │                                                      
       ▼                                                      
Tool Response to Hub Application                             
```

### Authentication Options

| Mode | Description | Use Case |
|------|-------------|----------|
| **Pass-through** | WB-A app's credentials forwarded to WB-B | When WB-B should know the original caller |
| **Configured** | WB-A uses its own service credentials | When WB-A acts as a trusted intermediary |
| **Bot Token** | WB-A's registered bot identity | Standard machine-to-machine auth |

WB-B's admin must authorize the caller (whether bot identity or forwarded credentials) using:
- Identity-based access control
- Role-based access control
- OPA policies

---

## Transitive Tool Exposure

A workbench can expose tools from machines it uses:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TRANSITIVE TOOL EXPOSURE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   WB-C (Consumer)        WB-B (Machine)           Machine-X (Core Banking)  │
│   ┌───────────────┐      ┌───────────────┐        ┌───────────────┐         │
│   │               │      │               │        │               │         │
│   │   Hub App     │ ───> │ Exposes:      │ ─────> │ get-account   │         │
│   │               │      │ get-account   │        │ get-balance   │         │
│   │               │      │ (from X)      │        │ post-credit   │         │
│   │               │      │               │        │               │         │
│   └───────────────┘      └───────────────┘        └───────────────┘         │
│                                                                              │
│   WB-C invokes "wb-b/get-account"                                           │
│   WB-B's dispatcher routes to Machine-X's get-account                       │
│   WB-B handles credential resolution for Machine-X                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Note:** WB-C doesn't need direct access to Machine-X. It accesses Machine-X's tools through WB-B, which manages the credentials and access.

---

## Operator Support

### WorkbenchAsMachine Operator

| Action | Behavior |
|--------|----------|
| **Create** | Register Machine Definition in Machine Registry, configure I/O Gateway routes |
| **Update** | Update Machine Definition, refresh exposed tools |
| **Delete** | Remove Machine from registry, remove I/O Gateway routes |

### Validation Rules

1. **Workbench must exist** and be deployed
2. **Exposed scenarios must exist** with HTTP signal triggers
3. **Exposed standalone tools must exist** in Tool Registry
4. **Exposed machine tools must be accessible** by the workbench
5. **Access control must be valid** (workbenches/roles must exist)

---

## Related Patterns

### Hub Application as Standalone Tool

Standalone tools are a key component of Workbench-as-Machine. See [Hub Application as Standalone Tool](./hub-application-as-standalone-tool.md).

### Scenario as an Agent

Different from this pattern — Scenario-as-Agent is about task completion in task queues, while Workbench-as-Machine is about tool invocation. See [Scenario as an Agent](./scenario-as-an-agent.md).

### Scenario as a Tool

Scenarios can be exposed as tools with multiple operations. This is part of the Workbench-as-Machine specification.

---

## Best Practices

### Do's

| Practice | Rationale |
|----------|-----------|
| **Define clear tool contracts** | Enables consumers to integrate reliably |
| **Version your machine** | Allows backward-compatible evolution |
| **Use semantic operation names** | Makes the API intuitive |
| **Implement health checks** | Enables consumer-side monitoring |
| **Document all exposed tools** | Improves developer experience |

### Don'ts

| Anti-Pattern | Issue |
|--------------|-------|
| **Exposing internal implementation** | Creates tight coupling |
| **Mixing concerns in one tool** | Makes the API confusing |
| **Ignoring access control** | Security vulnerability |
| **Exposing all tools blindly** | Over-exposure, security risk |

---

## Troubleshooting

### Common Issues

| Issue | Cause | Resolution |
|-------|-------|------------|
| Machine not found | Not registered in Machine Registry | Check WorkbenchAsMachine CRD status |
| Tool not found | Tool not in exposed_tools list | Update WorkbenchAsMachine spec |
| Authentication failed | Invalid credentials | Verify credential configuration |
| Access denied | Caller not authorized | Check access_control settings |
| Timeout | Target tool slow | Increase timeout or optimize tool |

### Debug Checklist

1. Verify WorkbenchAsMachine CRD is applied and reconciled
2. Check Machine Registry for machine registration
3. Verify exposed tools are valid and accessible
4. Check I/O Gateway logs for routing issues
5. Verify caller credentials and access control
6. Test tool endpoint directly (bypass consumer workbench)

---

## Related Documentation

- [Direct Tool Dispatcher](../04-subsystems/hub-native-utilities/direct-tool-dispatcher.md) — Dispatcher architecture
- [Hub Application as Standalone Tool](./hub-application-as-standalone-tool.md) — Standalone tool pattern
- [Machine Registry](../04-subsystems/registry-services/machine-registry.md) — Machine registration
- [Developer Operators](../04-subsystems/operators/developer-operators.md) — Operator specifications

---

*Workbench as a Machine enables cross-workbench tool invocation with a standardized interface, combining Scenarios, Standalone Tools, and transitive Machine Tools into a cohesive, discoverable service.*

