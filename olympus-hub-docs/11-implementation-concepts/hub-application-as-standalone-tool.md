# Hub Application as Standalone Tool

> **Category:** Composite Patterns

---

## Overview

**Hub Application as Standalone Tool** is a composite pattern where a Hub Application is registered as an HTTP Tool, allowing direct invocation without going through Signal Exchange. This enables synchronous tool calls with tool-native responses, useful for utility functions that don't need request lifecycle management.

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Tool** as a capability and **Automation** as processing logic. This pattern bridges them by exposing Hub Application logic as a directly callable tool.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Tool | Standalone Tool | Application exposed as tool |
| Automation | Hub Application | Application provides logic |

### Gap This Fills

The ontology treats tools and automations separately. This pattern addresses:
1. **Direct access**: How to call app logic without SX?
2. **Synchronous response**: How to get immediate results?
3. **Utility functions**: How to expose helper capabilities?

---

## Definition

**Hub Application as Standalone Tool** is a pattern where:
- A Hub Application is also registered as an HTTP Tool
- The tool endpoint bypasses Signal Exchange
- Responses are tool-native (not Request Updates)
- The same application can serve both SX requests and direct tool calls

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-scoped |
| **Lifecycle** | Deployed with Hub Application |
| **Ownership** | Developer creates; workbench owns |
| **Multiplicity** | One application; multiple access paths |

---

## Rationale

### Why This Design?

Standalone tools enable:
1. **Performance**: Skip SX overhead for simple calls
2. **Synchronous**: Immediate response for callers
3. **Flexibility**: Same code, two access patterns
4. **AI integration**: Direct tool for AI agents

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Separate tool implementation** | Code duplication |
| **Always through SX** | Overhead for simple cases |
| **External HTTP services** | Lose Hub integration |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0036](../decision-logs/0036-standalone-tool-via-tool-instance.md) | Standalone tool via ToolInstance variation |

---

## Structure

### ToolInstance for Standalone

```yaml
apiVersion: hub.olympus.io/v1
kind: ToolInstance
metadata:
  name: currency-converter-tool
  namespace: acme-bank
spec:
  definition_ref: http-tool
  
  # Mark as standalone Hub App tool
  standalone_app:
    enabled: true
    application_ref: currency-converter-app
    
  # Tool endpoint (exposed by the app)
  connection:
    type: http
    base_url: "${app.endpoint}"    # Resolved from app deployment
    endpoint: "/tool/convert"
    method: POST
    
  # Tool operations
  operations:
    - name: convert
      description: "Convert between currencies"
      parameters:
        - name: amount
          type: number
          required: true
        - name: from_currency
          type: string
          required: true
        - name: to_currency
          type: string
          required: true
      returns:
        type: object
        schema:
          converted_amount: number
          rate: number
          timestamp: string
```

### Application with Both Paths

```python
class CurrencyConverterApp(HubApplication):
    """
    Hub Application serving both:
    1. SX requests (scenario-triggered)
    2. Direct tool calls (standalone)
    """
    
    # SX request handler
    async def handle_request(self, update):
        """Handle scenario-triggered requests."""
        result = await self.convert_currency(
            update.payload.amount,
            update.payload.from_currency,
            update.payload.to_currency
        )
        return RequestUpdate(
            status="COMPLETED",
            payload=result
        )
    
    # Standalone tool endpoint
    @tool_endpoint("/tool/convert")
    async def handle_tool_call(self, params):
        """Handle direct tool invocation."""
        result = await self.convert_currency(
            params["amount"],
            params["from_currency"],
            params["to_currency"]
        )
        # Return tool-native response
        return ToolResponse(
            converted_amount=result["amount"],
            rate=result["rate"],
            timestamp=result["timestamp"]
        )
    
    # Shared logic
    async def convert_currency(self, amount, from_curr, to_curr):
        rate = await self.get_exchange_rate(from_curr, to_curr)
        return {
            "amount": amount * rate,
            "rate": rate,
            "timestamp": datetime.now().isoformat()
        }
```

---

## Behavior

### How It Works

```
Two access paths to same application:

PATH 1: Via Signal Exchange (Scenario)
─────────────────────────────────────
Signal → SX → Trigger → Request → App → Request Update → SX

PATH 2: Via Standalone Tool (Direct)
────────────────────────────────────
Tool call → Gateway → App /tool endpoint → Tool Response
```

### Response Differences

| Aspect | SX Request | Standalone Tool |
|--------|------------|-----------------|
| Response format | Request Update DTO | Tool-native response |
| Lifecycle | Request created, tracked | No request |
| Audit | Full request history | Tool invocation log |
| Async support | Yes | No (synchronous) |

### Tool Registration

```
When standalone_app.enabled = true:

1. ToolInstance created
2. Endpoint resolved from app deployment
3. Tool registered in workbench Tool Registry
4. Available via Direct Tool Dispatcher
5. Available to AI agents via tool discovery
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Tool Registry | ← registered in | Tool available |
| Direct Tool Dispatcher | ← invoked via | Dispatcher routes calls |
| Hub Application | → runs on | App serves requests |
| Signal Exchange | (bypassed) | Not involved in tool calls |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Synchronous only** | Tool calls are request-response |
| **No request lifecycle** | No Request created |
| **Tool response format** | Must return tool-native response |
| **Same application** | Both paths served by same app |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **No duplication** | Same code, two paths |
| ✅ **Performance** | Skip SX for direct calls |
| ✅ **Flexibility** | Choose path per use case |
| ✅ **AI-ready** | Tools for AI agents |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **No request history** | Use SX path when audit needed |
| ⚠️ **Sync only** | Use SX path for async |

---

## Examples

### Example 1: Lookup Tool

```yaml
# Fast lookup that doesn't need request lifecycle
spec:
  standalone_app:
    enabled: true
    application_ref: customer-lookup-app
    
  operations:
    - name: lookup_customer
      endpoint: "/tool/lookup"
      parameters:
        - name: customer_id
          type: string
```

### Example 2: Consumer Using Both Paths

```python
class DisputeHandler(HubApplication):
    async def handle_request(self, update):
        # Quick lookup via standalone tool
        customer = await self.dispatcher.invoke(
            tool_ref="customer-lookup",
            params={"customer_id": update.payload.customer_id}
        )
        
        # But send notification via SX (needs audit)
        await self.send_signal(
            signal_type="notification.requested",
            payload={"customer": customer, "message": "..."}
        )
```

---

## Implementation Notes

### For Developers

- Use standalone for utility functions
- Keep tool responses focused
- Document which path to use when
- Share logic between paths

### For Operators

- Monitor both SX and tool invocation metrics
- Review standalone tool latency
- Ensure tool endpoints are healthy

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Hub Application](./hub-application.md) | Application serving tool |
| [Direct Tool Dispatcher](./direct-tool-dispatcher.md) | Invokes standalone tools |
| [Scenario as Tool](./scenario-as-tool.md) | Similar but scenario-level |

---

## References

- [Hub Application as Standalone Tool Pattern](../09-composite-systems-and-patterns/hub-application-as-standalone-tool.md)
- [ADR-0036: Standalone Tool](../decision-logs/0036-standalone-tool-via-tool-instance.md)

