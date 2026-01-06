# Direct Tool Dispatcher

> **Category:** Application Architecture

---

## Overview

The **Direct Tool Dispatcher** is a Hub Native Utility that enables synchronous tool invocation without going through Signal Exchange. Hub Applications use this dispatcher when they need immediate tool results within their processing flow, rather than the async request-update model of SX.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Tool** as a capability that performs specific operations. Direct Tool Dispatcher provides an alternative invocation path for tools when synchronous behavior is needed.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Tool | Tool invocation | Dispatcher provides sync access to tools |
| (not covered) | Synchronous invocation | Alternative to SX async flow |

### Gap This Fills

The ontology describes tools conceptually. Direct Tool Dispatcher addresses:
1. **Synchronous needs**: When async response is too slow
2. **Credential management**: How to escalate privileges for tool calls
3. **Observability**: How to trace direct calls

---

## Definition

**Direct Tool Dispatcher** is a platform utility that:
- Invokes tools synchronously on behalf of Hub Applications
- Bypasses Signal Exchange for direct access
- Manages credentials and privilege escalation
- Integrates with Olympus Watch for observability
- Handles retry logic per tool configuration

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-level; executes in subscription context |
| **Lifecycle** | Platform utility; always available |
| **Ownership** | Platform-owned; configured per workbench |
| **Multiplicity** | One dispatcher; many tools available |

---

## Rationale

### Why This Design?

Direct invocation is needed when:
1. **Immediate response**: Lookup before decision in same request
2. **Tight loops**: Multiple tool calls in rapid succession
3. **Non-request context**: Tool call outside SX flow

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Always use SX** | Too slow for sync needs |
| **Direct HTTP from app** | No credential management; no observability |
| **Tool-specific SDKs** | Inconsistent; duplicated logic |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0035](../decision-logs/0035-direct-tool-dispatcher-context.md) | Dispatcher executes in subscription/workbench context |

---

## Structure

### Dispatcher Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: DirectToolDispatcherConfig
metadata:
  name: workbench-dispatcher
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-prod
  
  # Available tools
  tools:
    - tool_ref: core-banking/account-lookup
      access_level: workbench
      
    - tool_ref: core-banking/transaction-history
      access_level: scenario
      credential_escalation:
        enabled: true
        credential_ref: elevated-service-account
        
    - tool_ref: document-store/retrieve
      access_level: workbench
      
  # Default retry policy
  default_retry:
    max_attempts: 3
    backoff: exponential
    
  # Observability
  observability:
    trace_level: full
    log_payloads: false  # For sensitive data
```

### Invocation Interface

```python
# Hub Application using dispatcher
result = await self.dispatcher.invoke(
    tool_ref="core-banking/transaction-history",
    params={
        "customer_id": "CUST-001",
        "days": 90
    },
    options={
        "timeout_ms": 5000,
        "retry": True
    }
)

# Result structure
{
    "success": True,
    "data": {
        "transactions": [...]
    },
    "metadata": {
        "tool_ref": "core-banking/transaction-history",
        "duration_ms": 234,
        "trace_id": "trace-xyz"
    }
}
```

---

## Behavior

### How It Works

```
1. Hub Application calls dispatcher.invoke()
   ├── tool_ref: Which tool to call
   ├── params: Tool parameters
   └── options: Timeout, retry settings

2. Dispatcher resolves tool from Tool Registry
   └── Gets tool endpoint, auth requirements

3. Dispatcher checks access control
   ├── Is caller authorized for this tool?
   └── Apply credential escalation if configured

4. Dispatcher invokes tool
   ├── Apply timeout
   ├── Retry on failure per policy
   └── Trace to Olympus Watch

5. Dispatcher returns result
   └── Success or error with details
```

### Access Control

```
Access control layers:

1. Gateway level (if external call)
   └── Already enforced before reaching app

2. Dispatcher level
   ├── Check caller identity
   ├── Check tool access configuration
   └── Apply credential escalation if permitted

3. Tool level (optional)
   └── Tool may have its own validation
```

### Credential Escalation

```yaml
# When application needs higher privileges for tool
credential_escalation:
  enabled: true
  credential_ref: elevated-service-account
  
# Credential stored in workbench environment
# Admin provisions the credential
# Dispatcher uses it for tool invocation
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Hub Application | ← called by | Applications invoke dispatcher |
| Tool Registry | → queries | Resolve tool definitions |
| Tool Instances | → invokes | Execute actual tool calls |
| Olympus Watch | → traces | Observability integration |
| Environment | ← reads | Credentials and config |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Sync only** | Dispatcher is for synchronous calls |
| **Workbench scoped** | Tools available per workbench config |
| **Timeout required** | All calls have timeout |
| **Traced** | All invocations logged to Olympus Watch |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Synchronous access** | Immediate results for app logic |
| ✅ **Credential management** | Centralized escalation |
| ✅ **Observability** | Built-in tracing |
| ✅ **Retry handling** | Configurable retry policies |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Bypasses SX** | For appropriate use cases only |
| ⚠️ **Blocking calls** | Timeout prevents indefinite waits |

---

## Examples

### Example 1: Lookup Before Decision

```python
class DisputeHandler(HubApplication):
    async def handle_request(self, update):
        customer_id = update.payload.data.customer_id
        
        # Sync lookup of customer tier
        tier_result = await self.dispatcher.invoke(
            tool_ref="crm/customer-tier",
            params={"customer_id": customer_id}
        )
        
        # Use tier to determine routing
        if tier_result.data.tier == "platinum":
            queue = "priority-disputes"
        else:
            queue = "standard-disputes"
        
        # Create task with determined queue
        await self.create_task(
            task_type="investigate",
            target_queue=queue
        )
```

### Example 2: Multiple Rapid Lookups

```python
class InvestigationHandler(HubApplication):
    async def gather_context(self, customer_id, txn_id):
        # Multiple sync calls for context gathering
        customer = await self.dispatcher.invoke(
            tool_ref="crm/customer-profile",
            params={"customer_id": customer_id}
        )
        
        transaction = await self.dispatcher.invoke(
            tool_ref="core-banking/transaction-detail",
            params={"transaction_id": txn_id}
        )
        
        history = await self.dispatcher.invoke(
            tool_ref="core-banking/transaction-history",
            params={"customer_id": customer_id, "days": 90}
        )
        
        return {
            "customer": customer.data,
            "transaction": transaction.data,
            "history": history.data
        }
```

---

## Implementation Notes

### For Developers

- Use dispatcher for sync needs within request handling
- Set appropriate timeouts for tool calls
- Handle errors gracefully; tools may fail
- Don't use for long-running operations

### For Operators

- Configure tool access per workbench security requirements
- Manage credential escalation carefully
- Monitor dispatcher invocation latency
- Review tool usage patterns

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Hub Native Utilities](./hub-native-utilities.md) | Dispatcher is a native utility |
| [Hub Application](./hub-application.md) | Applications use dispatcher |
| [Signal Exchange](./signal-exchange.md) | Alternative to SX for sync needs |

---

## References

- [Direct Tool Dispatcher Subsystem](../04-subsystems/hub-native-utilities/direct-tool-dispatcher.md)
- [ADR-0035: Dispatcher Context](../decision-logs/0035-direct-tool-dispatcher-context.md)

