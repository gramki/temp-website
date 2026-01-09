# ADR-0023: HTTP Tool Calling Application as Built-in Hub Application

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub Applications run on various Automation Runtimes (Atlantis, Rhea, ChronoShift, Seer). For many simple use cases, developers need to:
- Call an HTTP API/tool
- Transform the response
- Send results back to Signal Exchange

This workflow is common but creating a full Hub Application requires:
- Choosing an Automation Runtime
- Writing application code
- Deploying and managing the application
- Understanding runtime-specific patterns

For simple HTTP tool invocations, this overhead is excessive.

## Decision

Hub provides a **built-in HTTP Tool Calling Application** as a native utility:

1. **No Runtime Selection Required**: Developers don't choose a runtime—the HTTP Tool Calling Application is built-in

2. **Configuration-Driven**: All behavior defined in YAML configuration:
   - Tool endpoint, method, authentication
   - Headers, timeout, retry policy
   - Input and output transformation functions

3. **JavaScript Transformation Functions**: Stateless JavaScript functions map between:
   - Signal Exchange Request DTO → HTTP Tool parameters (input)
   - HTTP Tool response → Request Update DTO (output)

4. **Automatic SX Integration**: Automatically:
   - Receives `REQUEST_INITIATION` from Signal Exchange
   - Sends `REQUEST_UPDATE` after tool invocation

### Configuration Structure

```yaml
scenario:
  application:
    type: http_tool_calling_application    # Built-in type
  
  tool_config:
    tool_endpoint: "https://api.example.com/tool"
    method: "POST"
    auth: { type: "bearer", token: "${env.API_TOKEN}" }
  
  transformations:
    input_transform: |
      function(input) {
        return { customer_id: input.customer_id };
      }
    
    output_transform: |
      function(toolResponse, originalRequest) {
        return {
          request_status: { status: "COMPLETED" },
          payload: { data: toolResponse.body }
        };
      }
```

## Alternatives Considered

### Alternative 1: Require Full Application for All Use Cases
Developers must create complete Hub Applications even for simple HTTP calls.

- **Pros**: Consistent model, full flexibility
- **Cons**: Excessive overhead for simple use cases, slow time-to-value

### Alternative 2: Low-Code Visual Builder
Provide a visual builder for simple HTTP integrations.

- **Pros**: User-friendly, no coding
- **Cons**: Additional tooling, not GitOps-friendly, limited expressiveness

### Alternative 3: Template-Based Generation
Generate full application code from templates.

- **Pros**: Produces standard applications
- **Cons**: Still requires deployment, maintenance burden, code bloat

## Consequences

### Positive
- **Rapid Development**: Simple HTTP integrations in minutes
- **No Runtime Overhead**: No separate application to deploy/manage
- **Declarative Configuration**: YAML-based, GitOps-friendly
- **Reduced Complexity**: Developers focus on transformation logic

### Negative
- **Limited Capability**: Single HTTP call only (no chaining, conditional logic)
- **Stateless Only**: Cannot maintain state between calls
- **JavaScript Only**: Transformation limited to JavaScript functions

### Neutral
- For complex scenarios, developers still use full Automation Runtimes
- Transformation functions are sandboxed for security

## When to Use

| Use Case | HTTP Tool Calling App? |
|----------|------------------------|
| Simple HTTP tool invocation | ✅ Yes |
| Single request-response flow | ✅ Yes |
| Lightweight integration | ✅ Yes |
| Multi-step workflow | ❌ No (use Rhea/ChronoShift) |
| Conditional logic | ❌ No (use full application) |
| Stateful processing | ❌ No (use full application) |

## Related Decisions

- [ADR-0024: JavaScript Transformation Functions for DTO Mapping](./0024-javascript-transformation-functions.md)
- [ADR-0025: Decision and Prediction Tools as Stateless Utilities](./0025-stateless-decision-prediction-tools.md)

