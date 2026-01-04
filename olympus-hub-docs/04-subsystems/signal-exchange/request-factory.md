# Request Factory

> **Status:** 🔴 Stub — Placeholder for expansion

The Request Factory creates new Requests or updates existing Requests based on transformed signal payloads.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Create and update Requests from transformed signals |
| **Input** | Transformed payloads from Trigger Evaluator |
| **Output** | Requests routed to Application Router |
| **State** | Interacts with Request Management for persistence |

---

## Responsibilities

| Function | Description |
|----------|-------------|
| **Request Creation** | Create new Request instances |
| **Request Updates** | Update existing Requests with new signal data |
| **Session Binding** | Bind Request to Application session |
| **Idempotency** | Prevent duplicate Request creation |
| **Request Typing** | Apply correct Request type (Service/Business/System) |

---

## Create vs Update Logic

```
Based on trigger configuration (create_or_update):

create_new:
  → Always create a new Request

update_existing:
  → Find existing Request by correlation key
  → If found → update
  → If not found → error or create (configurable)

create_or_update:
  → Find existing Request by correlation key
  → If found → update
  → If not found → create new
```

---

## Request Correlation

Requests can be correlated by:
- **Explicit correlation ID** in signal
- **Business entity ID** (e.g., customer_id, transaction_id)
- **Session ID** from I/O Gateway
- **Idempotency key** from trigger definition

---

## Request-Application Session

A Request represents a session with a Hub Application:

| Aspect | Description |
|--------|-------------|
| **Lifecycle** | Request lives as long as Application processes it |
| **Updates** | Subsequent signals can update the same Request |
| **State** | Request state reflects Application processing state |

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Trigger Evaluator](./trigger-evaluator.md)
- [Application Router](./application-router.md)
- [Request Management](../request-management/README.md)

---

*TODO: Detailed design — correlation strategies, session management, error handling*

