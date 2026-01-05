# HTTP Tool Calling Application

> **Status:** 🟡 Draft — Under active development

The HTTP Tool Calling Application is a **simplified Hub Application** that calls an HTTP tool based on a Request and sends updates back to Signal Exchange based on the tool output. It provides stateless JavaScript transformation functions to map between Signal Exchange DTOs and tool parameters, eliminating the need to choose runtimes or write custom application code.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Simplify creation of simplistic applications that call HTTP tools |
| **Runtime** | Built-in Hub Application (no external runtime required) |
| **Transformation** | Stateless JavaScript functions for input/output mapping |
| **Update Delivery** | Automatically sends Request updates to Signal Exchange |
| **Use Case** | Simple HTTP tool invocations without full application development |

---

## When to Use

Use the HTTP Tool Calling Application when:

1. **Simple HTTP tool invocation** — You need to call an HTTP API/tool and return results
2. **No complex orchestration** — The flow is straightforward: receive request → call tool → return result
3. **Rapid prototyping** — Quick setup without choosing runtimes or writing custom code
4. **Lightweight integration** — Connect external HTTP services to Hub workflows
5. **Stateless transformations** — Input/output mapping can be expressed as pure JavaScript functions

**Do NOT use when:**
- You need complex orchestration or multi-step workflows
- You need stateful processing or session management
- You need conditional logic beyond simple transformations
- You need integration with other Hub Applications or services

---

## How It Works

```
Signal Exchange
   │
   │ REQUEST_INITIATION (with payload)
   ▼
┌─────────────────────────────────────────────────────────┐
│      HTTP Tool Calling Application                      │
│                                                         │
│  1. Receive Request from Signal Exchange               │
│  2. Extract payload from Request                       │
│  3. Execute input transformation function:             │
│     SX DTO → Tool Parameters                           │
│  4. Call HTTP tool with transformed parameters         │
│  5. Receive tool response                              │
│  6. Execute output transformation function:            │
│     Tool Output → Request Update DTO                    │
│  7. Send REQUEST_UPDATE to Signal Exchange             │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
         Signal Exchange
         (Request Update)
```

---

## Configuration

### Scenario Definition

```yaml
scenario:
  id: "http-tool-invocation-scenario"
  name: "HTTP Tool Invocation"
  
  # Use HTTP Tool Calling Application
  application:
    type: http_tool_calling_application    # Built-in type
  
  # Tool Configuration
  tool_config:
    # HTTP Tool Endpoint
    tool_endpoint: "https://api.example.com/tool"
    method: "POST"                          # GET | POST | PUT | PATCH | DELETE
    
    # Authentication (optional)
    auth:
      type: "bearer"                       # bearer | oauth2 | api_key | basic
      token: "${env.API_TOKEN}"            # Or reference to secret
    
    # Headers (optional)
    headers:
      Content-Type: "application/json"
      X-Custom-Header: "value"
    
    # Timeout (optional)
    timeout_ms: 30000                      # Default: 30000 (30 seconds)
    
    # Retry Policy (optional)
    retry:
      max_attempts: 3
      backoff: "exponential"              # linear | exponential
      retryable_status_codes: [500, 502, 503, 504]
  
  # Transformation Functions
  transformations:
    # Input: Transform Signal Exchange DTO to Tool Parameters
    input_transform: |
      function(input) {
        // input: Signal Exchange Request payload
        // Return: Object to send as tool request body/params
        
        return {
          customer_id: input.customer_id,
          amount: input.amount,
          currency: input.currency || "USD",
          metadata: {
            request_id: input.request_id,
            timestamp: new Date().toISOString()
          }
        };
      }
    
    # Output: Transform Tool Response to Request Update DTO
    output_transform: |
      function(toolResponse, originalRequest) {
        // toolResponse: HTTP tool response (status, headers, body)
        // originalRequest: Original Signal Exchange Request context
        // Return: Request Update payload for Signal Exchange
        
        if (toolResponse.status >= 200 && toolResponse.status < 300) {
          return {
            request_status: {
              status: "COMPLETED",
              status_reason: "Tool invocation successful"
            },
            response_status: {
              code: "COMPLETED",
              description: "Tool executed successfully",
              user_message: "Operation completed successfully"
            },
            payload: {
              content_type: "application/json",
              semantic_type: "com.example.ToolResponse",
              data: toolResponse.body
            }
          };
        } else {
          return {
            request_status: {
              status: "COMPLETED",
              status_reason: "Tool invocation failed"
            },
            response_status: {
              code: "FAILED",
              description: `Tool returned status ${toolResponse.status}`,
              user_message: "Operation failed. Please try again."
            },
            payload: {
              content_type: "application/json",
              semantic_type: "com.example.ToolError",
              data: {
                error: toolResponse.body,
                status_code: toolResponse.status
              }
            }
          };
        }
      }
```

---

## Transformation Functions

### Input Transformation

The **input transformation function** converts the Signal Exchange Request payload into parameters for the HTTP tool call.

**Function Signature:**
```javascript
function(input) {
  // input: Signal Exchange Request payload (from envelope.payload.data)
  // Return: Object to send as tool request body (for POST/PUT/PATCH) or query params (for GET)
  
  return {
    // Tool-specific parameters
  };
}
```

**Example:**
```javascript
function(input) {
  return {
    account_id: input.account_id,
    transaction_type: input.type,
    amount: parseFloat(input.amount),
    description: input.description || "No description",
    reference: input.correlation_id
  };
}
```

### Output Transformation

The **output transformation function** converts the HTTP tool response into a Request Update DTO for Signal Exchange.

**Function Signature:**
```javascript
function(toolResponse, originalRequest) {
  // toolResponse: {
  //   status: number,        // HTTP status code
  //   headers: object,       // Response headers
  //   body: any              // Response body (parsed if JSON)
  // }
  // originalRequest: {
  //   request_id: string,
  //   workbench_id: string,
  //   scenario_id: string,
  //   payload: object        // Original request payload
  // }
  // Return: Request Update payload (see Message Envelope spec)
  
  return {
    request_status: { ... },
    response_status: { ... },
    payload: { ... }
  };
}
```

**Example:**
```javascript
function(toolResponse, originalRequest) {
  const isSuccess = toolResponse.status >= 200 && toolResponse.status < 300;
  
  return {
    request_status: {
      status: isSuccess ? "COMPLETED" : "COMPLETED",  // Always COMPLETED (success or failure)
      status_reason: isSuccess 
        ? "Tool execution successful" 
        : `Tool returned error: ${toolResponse.status}`
    },
    response_status: {
      code: isSuccess ? "COMPLETED" : "FAILED",
      description: isSuccess 
        ? "Tool executed successfully" 
        : `HTTP ${toolResponse.status}: ${toolResponse.body?.error || "Unknown error"}`,
      user_message: isSuccess
        ? "Your request has been processed successfully"
        : "We encountered an error processing your request. Please try again."
    },
    payload: {
      content_type: "application/json",
      semantic_type: "com.example.ToolResult",
      data: {
        result: toolResponse.body,
        tool_status: toolResponse.status,
        processed_at: new Date().toISOString()
      }
    }
  };
}
```

### Transformation Function Requirements

| Requirement | Description |
|-------------|-------------|
| **Stateless** | Functions must be pure — no side effects, no external dependencies |
| **Synchronous** | Functions must return synchronously (no async/await) |
| **Error Handling** | Functions should handle errors gracefully and return valid DTOs |
| **Type Safety** | Functions should validate input types and return expected structures |

---

## Request Status Handling

The HTTP Tool Calling Application always sets Request status to **COMPLETED** after tool invocation, regardless of success or failure:

| Tool Response | Request Status | Response Status |
|---------------|----------------|-----------------|
| HTTP 2xx | COMPLETED | COMPLETED (success) |
| HTTP 4xx | COMPLETED | FAILED (client error) |
| HTTP 5xx | COMPLETED | FAILED (server error) |
| Network Error | COMPLETED | FAILED (network error) |
| Timeout | COMPLETED | TIMEOUT |

The distinction between success and failure is communicated via `response_status.code`, not `request_status.status`.

---

## Error Handling

### Tool Call Failures

| Failure Type | Behavior |
|--------------|----------|
| **Network Error** | Retry per retry policy, then return FAILED response |
| **HTTP Error (4xx/5xx)** | Return FAILED response with error details |
| **Timeout** | Return TIMEOUT response |
| **Transformation Error** | Return FAILED response with transformation error details |

### Transformation Function Errors

If a transformation function throws an error or returns invalid data:

1. Error is caught and logged
2. Request Update is sent with:
   - `request_status.status: "COMPLETED"`
   - `response_status.code: "FAILED"`
   - `response_status.description: "Transformation error: [error message]"`
   - Error details in payload

---

## Update Delivery to Signal Exchange

The HTTP Tool Calling Application automatically sends a `REQUEST_UPDATE` message to Signal Exchange after tool invocation:

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_UPDATE",
    "message_id": "uuid",
    "timestamp": "2026-01-05T10:35:00Z",
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001"
  },
  "request": {
    "workbench_id": "dispute-ops",
    "scenario_id": "http-tool-invocation-scenario",
    "id": "req-12345",
    "correlation_id": "corr-67890"
  },
  "update": {
    "update_type": "STATUS_CHANGE",
    "sequence": 1
  },
  "payload": {
    // Output of output_transform function
  }
}
```

The update includes:
- Request status change (to COMPLETED)
- Response status (COMPLETED, FAILED, or TIMEOUT)
- Tool response data (transformed by output_transform)

---

## Integration with Signal Exchange

The HTTP Tool Calling Application:

1. **Receives** `REQUEST_INITIATION` messages from Signal Exchange
2. **Processes** the request by calling the configured HTTP tool
3. **Sends** `REQUEST_UPDATE` messages back to Signal Exchange with results

The application uses Signal Exchange's standard message envelope format (see [Message Envelope](../signal-exchange/message-envelope.md)).

---

## Example: Credit Check Tool

```yaml
scenario:
  id: "credit-check-scenario"
  name: "Credit Check"
  
  application:
    type: http_tool_calling_application
  
  tool_config:
    tool_endpoint: "https://credit-api.example.com/v1/check"
    method: "POST"
    auth:
      type: "bearer"
      token: "${env.CREDIT_API_TOKEN}"
    headers:
      Content-Type: "application/json"
    timeout_ms: 10000
  
  transformations:
    input_transform: |
      function(input) {
        return {
          customer_id: input.customer_id,
          amount: input.loan_amount,
          purpose: input.loan_purpose || "general"
        };
      }
    
    output_transform: |
      function(toolResponse, originalRequest) {
        const result = toolResponse.body;
        const approved = result.status === "approved";
        
        return {
          request_status: {
            status: "COMPLETED",
            status_reason: approved ? "Credit check approved" : "Credit check declined"
          },
          response_status: {
            code: approved ? "COMPLETED" : "REJECTED",
            description: `Credit check ${approved ? "approved" : "declined"}`,
            user_message: approved
              ? "Your credit check has been approved"
              : `Credit check declined: ${result.reason || "Insufficient credit score"}`
          },
          payload: {
            content_type: "application/json",
            semantic_type: "com.example.CreditCheckResult",
            data: {
              approved: approved,
              credit_score: result.credit_score,
              limit: result.limit,
              reason: result.reason
            }
          }
        };
      }
```

---

## Limitations

| Limitation | Description |
|------------|-------------|
| **Single Tool Call** | Only one HTTP tool call per request (no chaining) |
| **No State Management** | Stateless — cannot maintain state between calls |
| **No Conditional Logic** | Simple transformation only — no branching or loops |
| **No External Dependencies** | Transformation functions cannot call external services |
| **Synchronous Only** | Tool calls are synchronous (waits for response) |

For more complex scenarios, use a full Hub Application runtime (Atlantis, Rhea, ChronoShift, etc.).

---

## Related Documentation

- [Signal Exchange](../signal-exchange/README.md) — Message delivery and updates
- [Message Envelope](../signal-exchange/message-envelope.md) — Request Update DTO format
- [Hub Applications](../../01-concepts/hub-applications.md) — Application concepts
- [Manual Task Application](./manual-task-application.md) — Another simplified application

---

*TODO: Detailed design — transformation function sandboxing, error handling strategies, retry policies, timeout handling*

