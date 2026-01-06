# Hub Native Utilities

> **Category:** Application Architecture

---

## Overview

**Hub Native Utilities** are platform-provided applications and tools that simplify common integration patterns. Rather than requiring developers to build custom Hub Applications for every use case, Hub provides built-in utilities like HTTP Tool Calling Application and Direct Tool Dispatcher that handle standard scenarios with configuration only.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Automation** as the blueprint for how operations run. Hub Native Utilities are pre-built automations that developers configure rather than code.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Automation | Hub Native Utility | Pre-built automation available to configure |
| Tool | Built-in tool wrappers | Utilities that simplify tool usage |

### Gap This Fills

The ontology focuses on concepts. Hub Native Utilities address:
1. **Developer efficiency**: Common patterns pre-built
2. **Reduced complexity**: Configuration over coding
3. **Consistent behavior**: Platform-maintained implementations
4. **Faster time-to-value**: No custom code for standard cases

---

## Definition

**Hub Native Utilities** are platform-provided components that:
- Implement common automation patterns
- Are configured via CRDs rather than custom code
- Run on Hub-managed infrastructure
- Integrate seamlessly with Signal Exchange and Tool Registry

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-level; configured per workbench |
| **Lifecycle** | Platform-provided; configured by developers |
| **Ownership** | Hub maintains; developers configure |
| **Multiplicity** | Multiple utilities; multiple instances per workbench |

---

## Rationale

### Why This Design?

Pre-built utilities enable:
1. **Faster development**: No code for common patterns
2. **Reduced errors**: Proven implementations
3. **Consistent integration**: Standard SX interaction
4. **Lower maintenance**: Platform-maintained

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Custom code for everything** | Slow; error-prone; duplicated effort |
| **Third-party integrations** | Inconsistent; no SX integration |

---

## Structure

### Available Utilities

| Utility | Purpose | Configuration |
|---------|---------|---------------|
| **HTTP Tool Calling Application** | Invoke HTTP API and return result | Endpoint, auth, transforms |
| **Direct Tool Dispatcher** | Invoke tools without SX flow | Tool reference, credentials |
| **Webhook Relay** | Forward signals to external system | Target URL, format |
| **Scheduled Signal Generator** | Generate signals on schedule | Cron, signal template |

### HTTP Tool Calling Application

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: payment-validator
spec:
  type: http_tool_calling_application
  
  tool_config:
    tool_endpoint: "https://api.payment.acme.com/validate"
    method: "POST"
    auth:
      type: bearer
      token: "${env.PAYMENT_API_TOKEN}"
    timeout_ms: 30000
    retry:
      max_attempts: 3
      retryable_status_codes: [500, 502, 503]
    
  transformations:
    input_transform: |
      function(input) {
        return {
          amount: input.amount,
          account: input.account_id
        };
      }
    output_transform: |
      function(response, request) {
        return {
          request_status: { status: "COMPLETED" },
          payload: { valid: response.body.is_valid }
        };
      }
```

### Direct Tool Dispatcher

```yaml
apiVersion: hub.olympus.io/v1
kind: DirectToolDispatcherConfig
metadata:
  name: core-banking-dispatcher
spec:
  tools:
    - tool_ref: core-banking/account-lookup
      access_level: workbench
    - tool_ref: core-banking/transaction-history
      access_level: scenario
      
  credential_escalation:
    enabled: true
    credential_ref: elevated-service-account
    
  observability:
    trace_level: full
```

---

## Behavior

### How It Works

**HTTP Tool Calling Application:**
```
1. Signal triggers Request
2. SX routes to HTTP Tool Calling Application
3. Utility extracts data from Request
4. Applies input_transform function
5. Invokes configured HTTP endpoint
6. Applies output_transform to response
7. Returns Request Update to SX
```

**Direct Tool Dispatcher:**
```
1. Hub Application needs synchronous tool call
2. Calls Direct Tool Dispatcher with tool reference
3. Dispatcher resolves tool from registry
4. Applies credential escalation if configured
5. Invokes tool directly (bypasses SX)
6. Returns result to calling application
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Signal Exchange | ↔ | Utilities receive requests, send updates |
| Tool Registry | → | Resolve tool definitions |
| Olympus Watch | → | Observability integration |
| Environment | ← | Read configuration and secrets |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Configuration-based** | No custom code in utility configuration |
| **Transform limitations** | JavaScript functions must be stateless |
| **Platform-managed** | Utilities run on Hub infrastructure |
| **Versioned** | Utility versions managed by platform |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **No code required** | Configuration only |
| ✅ **Proven implementation** | Platform-tested |
| ✅ **Integrated** | Works with SX, observability |
| ✅ **Maintained** | Platform handles updates |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Limited flexibility** | Custom Hub App for complex cases |
| ⚠️ **Transform constraints** | Stateless JS; no external calls |

---

## Examples

### Example 1: Simple API Integration

```yaml
# Validate transaction with external fraud service
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: fraud-check
spec:
  type: http_tool_calling_application
  
  tool_config:
    tool_endpoint: "https://fraud.vendor.com/check"
    method: "POST"
    auth:
      type: oauth2
      token_url: "https://fraud.vendor.com/oauth/token"
      client_id_ref: fraud-client-id
      client_secret_ref: fraud-client-secret
    
  transformations:
    input_transform: |
      function(input) {
        return {
          transaction_id: input.txn_id,
          amount: input.amount,
          merchant: input.merchant_id
        };
      }
    output_transform: |
      function(response, request) {
        var status = response.body.risk_score > 0.8 ? "FLAGGED" : "CLEARED";
        return {
          request_status: { status: "COMPLETED" },
          payload: { 
            fraud_status: status,
            risk_score: response.body.risk_score
          }
        };
      }
```

### Example 2: Using Direct Tool Dispatcher

```python
# In a custom Hub Application
class DisputeHandler(HubApplication):
    async def handle_request(self, update):
        # Use Direct Tool Dispatcher for sync call
        result = await self.dispatcher.invoke(
            tool_ref="core-banking/transaction-history",
            params={
                "customer_id": update.payload.data.customer_id,
                "days": 90
            }
        )
        
        # Process result
        transactions = result.data.transactions
        # ... analysis logic ...
```

---

## Implementation Notes

### For Developers

- Start with utilities for simple integrations
- Use custom Hub Application when logic is complex
- Keep transform functions simple and stateless
- Test transforms with sample data before deployment

### For Operators

- Monitor utility health alongside custom applications
- Review transform execution times
- Check retry patterns for failed calls

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Hub Application](./hub-application.md) | Utilities are specialized Hub Applications |
| [Direct Tool Dispatcher](./direct-tool-dispatcher.md) | One of the utilities |
| [Signal Exchange](./signal-exchange.md) | Utilities integrate with SX |

---

## References

- [Hub Native Utilities Subsystem](../04-subsystems/hub-native-utilities/README.md)
- [HTTP Tool Calling Application](../04-subsystems/hub-native-utilities/http-tool-calling-application.md)
- [Direct Tool Dispatcher](../04-subsystems/hub-native-utilities/direct-tool-dispatcher.md)

