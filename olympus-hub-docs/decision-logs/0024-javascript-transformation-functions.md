# ADR-0024: JavaScript Transformation Functions for DTO Mapping

## Status

**Accepted**

## Date

2026-01-06

## Context

The HTTP Tool Calling Application needs to transform data between:
- **Input**: Signal Exchange Request DTO → HTTP Tool request parameters
- **Output**: HTTP Tool response → Signal Exchange Request Update DTO

These transformations vary per use case and need to be:
- Expressive enough for common data mapping needs
- Safe (sandboxed, no side effects)
- Fast (synchronous execution)
- Accessible to developers (familiar language)

## Decision

Use **stateless JavaScript functions** for input/output transformation in the HTTP Tool Calling Application:

1. **Pure Functions**: No side effects, no external dependencies, deterministic output

2. **Synchronous Execution**: Functions return synchronously (no async/await)

3. **Sandboxed Runtime**: Functions execute in isolated JavaScript sandbox (V8/QuickJS)

4. **Simple Signatures**:
   - Input: `function(input) → toolParams`
   - Output: `function(toolResponse, originalRequest) → requestUpdate`

### Input Transformation

```javascript
function(input) {
  // input: Signal Exchange Request payload (from envelope.payload.data)
  // Return: Object to send as tool request body/params
  
  return {
    customer_id: input.customer_id,
    amount: parseFloat(input.amount),
    currency: input.currency || "USD"
  };
}
```

### Output Transformation

```javascript
function(toolResponse, originalRequest) {
  // toolResponse: { status, headers, body }
  // originalRequest: { request_id, workbench_id, scenario_id, payload }
  // Return: Request Update payload for Signal Exchange
  
  return {
    request_status: {
      status: "COMPLETED",
      status_reason: "Tool invocation successful"
    },
    response_status: {
      code: toolResponse.status >= 200 && toolResponse.status < 300 
        ? "COMPLETED" : "FAILED"
    },
    payload: {
      content_type: "application/json",
      data: toolResponse.body
    }
  };
}
```

## Alternatives Considered

### Alternative 1: JSONPath/JMESPath Expressions
Use query languages like JSONPath for simple field mapping.

- **Pros**: Simple, no code execution
- **Cons**: Limited expressiveness, can't handle complex transformations, multiple expressions needed

### Alternative 2: JSONata
Use JSONata for declarative JSON transformations.

- **Pros**: Powerful, declarative, JSON-native
- **Cons**: Less familiar to most developers, learning curve, limited ecosystem

### Alternative 3: Python Functions
Use Python for transformations.

- **Pros**: Popular language, rich ecosystem
- **Cons**: Heavier runtime, harder to sandbox, slower startup

### Alternative 4: YAML/Declarative Mapping
Purely declarative field-to-field mapping.

- **Pros**: Simple, no code
- **Cons**: Can't handle any logic (conditionals, defaults, type conversions)

## Consequences

### Positive
- **Familiar Language**: JavaScript widely known among developers
- **Expressive**: Handle conditionals, defaults, type conversions, complex mappings
- **Lightweight**: V8/QuickJS provides fast, sandboxed execution
- **Inline Configuration**: Functions embedded in YAML configuration

### Negative
- **Security Concerns**: Must sandbox JavaScript execution carefully
- **Error Handling**: Runtime errors in functions need graceful handling
- **Testing Complexity**: Functions need separate testing approach
- **Language Lock-in**: JavaScript only (no Python, TypeScript, etc.)

### Neutral
- Standard JavaScript syntax (ES6+)
- No external library access (pure functions only)
- Error in transformation returns FAILED response with error details

## Function Requirements

| Requirement | Description |
|-------------|-------------|
| **Stateless** | No side effects, no external dependencies |
| **Synchronous** | Must return synchronously (no async/await) |
| **Pure** | Output determined solely by inputs |
| **Type-safe** | Should validate input types and return expected structures |
| **Error-handling** | Should handle errors gracefully |

## Sandbox Restrictions

Transformation functions **cannot**:
- Access network or file system
- Import external modules
- Use async/await or Promises
- Access global state
- Call setTimeout/setInterval
- Access DOM or browser APIs

## Related Decisions

- [ADR-0023: HTTP Tool Calling Application](./0023-http-tool-calling-application.md)

