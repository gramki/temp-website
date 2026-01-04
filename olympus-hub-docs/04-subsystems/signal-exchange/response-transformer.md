# Response Transformer

> **Status:** 🔴 Stub — Placeholder for expansion

The Response Transformer transforms Hub Application responses for delivery back to I/O Gateways.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Transform Application responses for I/O Gateways |
| **Input** | Responses from Hub Applications |
| **Output** | Protocol-specific responses to I/O Gateways |
| **Scope** | Only for bidirectional Signal Providers (I/O Gateways) |

---

## Responsibilities

| Function | Description |
|----------|-------------|
| **Response Reception** | Receive responses from Hub Applications |
| **Transformation** | Apply output transformation rules |
| **Protocol Formatting** | Format for target I/O Gateway protocol |
| **Delivery** | Route response to correct I/O Gateway |

---

## Signal Provider Types

| Type | Response Handling |
|------|-------------------|
| **I/O Gateway** | Full response transformation and delivery |
| **Input-only Signal Provider** | No response path (fire-and-forget) |

---

## Response Flow

```
1. Hub Application produces response
2. Identify originating Signal Provider
3. If I/O Gateway (bidirectional):
   a. Load output transformation from trigger definition
   b. Apply transformation rules
   c. Format for Gateway protocol (HTTP, Event, File, etc.)
   d. Deliver to I/O Gateway
4. If input-only Signal Provider:
   a. No response delivery
   b. Log completion status
```

---

## Transformation Rules

Transformation is defined in trigger configuration:

```yaml
trigger:
  # ... other fields ...
  
  response:
    success:
      status: 202
      body:
        request_id: "$.request.id"
        status: "ACCEPTED"
    error:
      status: 400
      body:
        error: "$.error.message"
```

---

## I/O Gateway Protocols

| Gateway | Response Format |
|---------|-----------------|
| **Heracles** | HTTP response (status, headers, body) |
| **Atropos** | Event publication (response event) |
| **Dia** | File output (result file) |
| **Cronus** | Exception resolution status |

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Application Router](./application-router.md)
- [Signal Providers](../signal-providers/README.md)

---

*TODO: Detailed design — transformation DSL, protocol adapters, error responses*

