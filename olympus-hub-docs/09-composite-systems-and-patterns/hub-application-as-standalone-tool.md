# Hub Application as Standalone Tool

> **Status:** 🟡 Draft — Architecture defined

## Overview

A **Standalone Tool** is where the Workbench itself acts as the machine hosting the tool — there is no external machine involved. Any Hub Application can be registered as a Standalone HTTP Tool, enabling direct invocation from other applications without being mediated through Signal Exchange.

This pattern provides:
- **Direct invocation** of Hub Applications as tools
- **No SX/Request overhead** for function-like operations
- **Dual-mode applications** that support both SX flow AND direct invocation
- **Optimal path** for tool-use patterns within or across workbenches

---

## The Premise

### Why Standalone Tools?

Hub Applications are powerful automations that can:
- Execute complex business logic
- Access knowledge bases and memory stores
- Invoke other tools
- Make decisions with CAF compliance

Sometimes these capabilities should be **directly invocable as tools** rather than requiring the full Scenario/Request lifecycle:

| Scenario/Request Flow | Standalone Tool Flow |
|-----------------------|----------------------|
| Signal → Trigger → Request → Application | Application invoked directly |
| Full lifecycle management | Stateless invocation |
| Suitable for operational scenarios | Suitable for function calls |
| Observer notifications, task management | No lifecycle events |

### The Value

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    STANDALONE TOOL VALUE PROPOSITION                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                         WITHOUT STANDALONE TOOLS                        │ │
│  │                                                                         │ │
│  │   App-A                Signal Exchange           App-B                  │ │
│  │     │                        │                      │                   │ │
│  │     │ ─ Create Request ────> │                      │                   │ │
│  │     │                        │ ─ Trigger ─────────> │                   │ │
│  │     │                        │                      │                   │ │
│  │     │                        │ <── Updates ──────── │                   │ │
│  │     │ <── Request Complete ─ │                      │                   │ │
│  │                                                                         │ │
│  │   Overhead: Signal processing, Request lifecycle, Trigger evaluation   │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                         WITH STANDALONE TOOLS                           │ │
│  │                                                                         │ │
│  │   App-A           Direct Tool Dispatcher          App-B (as Tool)      │ │
│  │     │                        │                      │                   │ │
│  │     │ ─ Invoke Tool ───────> │ ─ Direct Call ─────> │                   │ │
│  │     │ <── Tool Response ──── │ <── Response ─────── │                   │ │
│  │                                                                         │ │
│  │   Benefit: Direct invocation, tool-native response, minimal overhead   │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## How It Works

### Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        WORKBENCH A                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                  HUB APPLICATION (Standalone Tool)                   │   │
│   │                                                                      │   │
│   │  ┌─────────────────────────────────────────────────────────────────┐│   │
│   │  │                 DUAL-MODE OPERATION                             ││   │
│   │  │                                                                 ││   │
│   │  │   Path 1: Scenario/Request Flow (via SX)                        ││   │
│   │  │   • Triggered by signals                                        ││   │
│   │  │   • Creates/updates Requests                                    ││   │
│   │  │   • Full lifecycle management                                   ││   │
│   │  │                                                                 ││   │
│   │  │   Path 2: Standalone Tool Flow (via Dispatcher)                 ││   │
│   │  │   • Direct HTTP invocation                                      ││   │
│   │  │   • Tool-native request/response                                ││   │
│   │  │   • No Request lifecycle                                        ││   │
│   │  │                                                                 ││   │
│   │  └─────────────────────────────────────────────────────────────────┘│   │
│   │                                                                      │   │
│   │  Registered as: StandaloneTool (machine = workbench)                │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│                              ▲                                               │
│                              │ Direct Tool Dispatcher                        │
│                              │                                               │
│   ┌──────────────────────────┼──────────────────────────────────────────┐   │
│   │                          │                                           │   │
│   │  ┌─────────────────┐  ┌─┴───────────────┐  ┌─────────────────┐     │   │
│   │  │ Other Hub Apps  │  │ I/O Gateway     │  │ External Clients│     │   │
│   │  │ (within WB-A)   │  │ (for external)  │  │ (via Heracles)  │     │   │
│   │  └─────────────────┘  └─────────────────┘  └─────────────────┘     │   │
│   │                                                                      │   │
│   │              INVOCATION SOURCES                                      │   │
│   └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Key Concepts

1. **Workbench as Machine**: The tool's "machine" is the workbench itself — no external system required
2. **Direct Tool Dispatcher**: Platform utility that routes tool invocations to the application
3. **Tool-Native Response**: Application returns tool-format responses, not Request Updates
4. **Dual-Mode**: Same application can serve both SX flow and direct tool invocation

---

## When to Use This Pattern

### Use When:

| Use Case | Example |
|----------|---------|
| **Reusable Business Logic** | Fraud scoring, eligibility checks, validation |
| **Cross-Application Services** | An app provides utility functions for other apps |
| **Low-Latency Requirements** | Tool calls need minimal overhead |
| **Function-Like Operations** | Stateless, request-response pattern |
| **No Lifecycle Needed** | Operation doesn't need Request tracking |

### Avoid When:

| Situation | Better Alternative |
|-----------|--------------------|
| Operation needs task assignment | Use Scenario with Task Management |
| Need full audit trail as Request | Use normal SX → Request flow |
| Multi-step, stateful process | Use Scenario |
| Need observer notifications | Use Scenario |

---

## Implementation Guide

### Step 1: Create the Hub Application

The Hub Application should support both modes:

```python
# Example: Fraud Detection Hub Application

class FraudDetectionApp:
    """
    Hub Application that can operate in two modes:
    1. Scenario Mode: Receives Request, creates Tasks, updates Request
    2. Tool Mode: Direct invocation, returns tool response
    """
    
    def __init__(self):
        self.model = load_fraud_model()
    
    # Scenario Mode Entry Point
    async def handle_request(self, request: Request) -> RequestUpdate:
        """Called when triggered via Signal Exchange"""
        transaction = request.payload.get("transaction")
        
        # Analyze and create task for review
        risk_score = self.analyze(transaction)
        
        if risk_score > 0.8:
            # Create task for human review
            await self.create_task(request.id, "fraud-review", {
                "transaction": transaction,
                "risk_score": risk_score
            })
        
        return RequestUpdate(
            status="IN_PROGRESS",
            memo=f"Fraud analysis complete. Risk score: {risk_score}"
        )
    
    # Tool Mode Entry Point
    async def handle_tool_invocation(self, params: dict) -> dict:
        """Called when invoked as a Standalone Tool"""
        transaction = params.get("transaction")
        
        # Direct analysis, return tool response
        risk_score = self.analyze(transaction)
        
        return {
            "risk_score": risk_score,
            "risk_level": self.categorize_risk(risk_score),
            "factors": self.get_risk_factors(transaction),
            "recommendation": "review" if risk_score > 0.8 else "approve"
        }
    
    def analyze(self, transaction: dict) -> float:
        """Core analysis logic - shared by both modes"""
        return self.model.predict(transaction)
```

### Step 2: Define Standalone Tool Specification

Register the application as a Standalone Tool:

```yaml
apiVersion: hub.olympus.io/v1
kind: ToolInstance
metadata:
  name: fraud-detection-tool
  namespace: acme-bank
  labels:
    workbench: fraud-operations
spec:
  # Tool Identity
  tool:
    name: fraud-detection-tool
    display_name: "Fraud Detection Tool"
    version: "1.0.0"
    description: "Analyzes transactions for fraud risk"
  
  # Standalone Tool Configuration
  machine:
    type: standalone           # Key: machine is the workbench itself
    # No machine_ref needed - workbench hosts this tool
  
  # Source Application
  application_ref: fraud-detection-app
  
  # Tool Interface
  interface:
    protocol: http
    method: POST
    path: /tools/fraud-detection
    
    # Request Schema
    input_schema:
      type: object
      properties:
        transaction:
          type: object
          properties:
            id: { type: string }
            amount: { type: number }
            merchant: { type: string }
            location: { type: object }
            timestamp: { type: string, format: date-time }
          required: [id, amount]
      required: [transaction]
    
    # Response Schema
    output_schema:
      type: object
      properties:
        risk_score:
          type: number
          minimum: 0
          maximum: 1
        risk_level:
          type: string
          enum: [low, medium, high, critical]
        factors:
          type: array
          items: { type: string }
        recommendation:
          type: string
          enum: [approve, review, reject]
  
  # Dispatcher Configuration
  dispatcher_config:
    credential_mode: pass-through
    
    access_control:
      allowed_applications:
        - dispute-resolution-app
        - customer-service-app
      allowed_roles:
        - analyst
        - operator
    
    retry:
      max_attempts: 3
      backoff:
        type: exponential
        initial_delay_ms: 100
    
    timeout_ms: 5000
  
  # Observability
  observability:
    metrics_enabled: true
    tracing_enabled: true
```

### Step 3: Invoke from Other Applications

Other Hub Applications can invoke the standalone tool:

```python
# In another Hub Application
class DisputeResolutionApp:
    
    async def process_dispute(self, request: Request):
        transaction = request.payload.get("transaction")
        
        # Direct tool invocation (no SX/Request overhead)
        fraud_result = await tools.invoke(
            tool_id="fraud-detection-tool",
            params={"transaction": transaction}
        )
        
        if fraud_result["risk_level"] == "critical":
            # High fraud risk - different handling
            await self.escalate_to_fraud_team(request, fraud_result)
        else:
            # Normal dispute processing
            await self.process_normal_dispute(request)
```

---

## Operator Support

### StandaloneTool CRD

Standalone tools use the `ToolInstance` CRD with `machine.type: standalone`:

```yaml
apiVersion: hub.olympus.io/v1
kind: ToolInstance
metadata:
  name: {tool-name}
  namespace: {tenant-namespace}
spec:
  tool:
    name: {tool-name}
    display_name: "{Display Name}"
    version: "{version}"
    description: "{description}"
  
  # Standalone indicator
  machine:
    type: standalone
  
  # Application that implements the tool
  application_ref: {hub-application-id}
  
  # Tool interface
  interface:
    protocol: http
    method: POST
    path: /tools/{tool-path}
    input_schema: { ... }
    output_schema: { ... }
  
  # Dispatcher configuration
  dispatcher_config:
    credential_mode: pass-through | configured | escalation
    access_control: { ... }
    retry: { ... }
    timeout_ms: 5000
```

### Reconciliation Behavior

| Action | Behavior |
|--------|----------|
| **Create** | Register tool in Tool Registry, configure dispatcher route |
| **Update** | Update tool registration, update dispatcher config |
| **Delete** | Remove from Tool Registry, remove dispatcher route |

---

## Integration with Other Patterns

### Workbench as a Machine

When a workbench is exposed as a Machine, its standalone tools become available to other workbenches:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CROSS-WORKBENCH TOOL ACCESS                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   WORKBENCH-A                           WORKBENCH-B (as Machine)            │
│   ┌─────────────────────┐               ┌─────────────────────┐             │
│   │                     │               │                     │             │
│   │   Hub Application   │ ────────────> │  Standalone Tool    │             │
│   │                     │  Direct Tool  │  (Fraud Detection)  │             │
│   │                     │  Invocation   │                     │             │
│   │                     │               │  Standalone Tool    │             │
│   │                     │ ────────────> │  (Risk Scoring)     │             │
│   │                     │               │                     │             │
│   └─────────────────────┘               └─────────────────────┘             │
│                                                                              │
│   WB-B exposes its standalone tools via "Workbench as a Machine" pattern    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Decision Tools

Decision Tools are a special case of Standalone Tools:

| Type | Characteristics |
|------|-----------------|
| **Decision Tool** | Stateless, CAF-compliant, rule/DMN-based |
| **Standalone Tool** | General-purpose, may have any implementation |

Decision Tools automatically get CAF integration; Standalone Tools can optionally enable it.

---

## Best Practices

### Do's

| Practice | Rationale |
|----------|-----------|
| **Keep tool operations stateless** | Easier to test, retry, and scale |
| **Define clear input/output schemas** | Enables validation and documentation |
| **Use appropriate timeout** | Prevent hanging invocations |
| **Enable observability** | Debug and monitor tool usage |
| **Document dual-mode behavior** | Clarify when each mode is used |

### Don'ts

| Anti-Pattern | Issue |
|--------------|-------|
| **Long-running tool operations** | Use Scenario instead |
| **Storing state in tool** | Makes scaling difficult |
| **Exposing internal APIs** | Security and coupling concerns |
| **Skipping access control** | Security vulnerability |

---

## Troubleshooting

### Common Issues

| Issue | Cause | Resolution |
|-------|-------|------------|
| Tool not found | Not registered in Tool Registry | Check ToolInstance CRD status |
| Access denied | Caller not authorized | Update access_control in dispatcher_config |
| Timeout | Tool takes too long | Increase timeout or optimize tool |
| Credential error | Environment variables not set | Verify credential configuration |

### Debug Checklist

1. Verify ToolInstance CRD is applied and reconciled
2. Check Tool Registry for tool registration
3. Verify application is deployed and healthy
4. Check dispatcher logs in Olympus Watch
5. Verify caller has required permissions
6. Test tool endpoint directly (bypassing dispatcher)

---

## Related Documentation

- [Direct Tool Dispatcher](../04-subsystems/hub-native-utilities/direct-tool-dispatcher.md) — Dispatcher architecture
- [Tool Registry](../04-subsystems/registry-services/tool-registry.md) — Tool registration
- [Workbench as a Machine](./workbench-as-a-machine.md) — Cross-workbench tool exposure
- [Decision Tools](../04-subsystems/hub-native-utilities/decision-tools.md) — Stateless decision tools

---

*Hub Application as Standalone Tool enables efficient, direct invocation of application logic without the overhead of Signal Exchange and Request lifecycle, while maintaining access control and observability.*

