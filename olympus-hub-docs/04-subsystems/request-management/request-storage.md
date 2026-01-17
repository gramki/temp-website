# Request Storage

> **Status:** 🔴 Stub — Placeholder for expansion

Request Storage provides **request-scoped storage**—a data context that lives for the duration of the request.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Store request-scoped data |
| **Scope** | Request lifetime |
| **Access** | Automation systems, agents, operations |

---

## Request Scope Storage

From Todo notes:
> *"Request Scope Storage"*

Request-scoped storage provides:
- Temporary data during request processing
- Shared context across activities
- Working memory for operations

---

## Storage Model

```yaml
request_storage:
  request_id: string
  tenant_id: string
  
  # Structured data
  data:
    key: value  # Key-value pairs
  
  # Documents
  documents:
    - id: string
      name: string
      content_type: string
      storage_ref: string
  
  # Delegation context (request-scoped authority)
  delegations:
    certificates:
      - id: string             # Delegation Certificate ID
        template: string       # Template name
        delegator:
          id: string
          type: string         # "business-user" | "system"
        attached_at: datetime
        expires_at: datetime
        attachment_type: string  # "proactive" | "reactive" | "inherited"
        source_request_id: string  # For inherited: parent request
    
    pending_requests:
      - request_id: string
        template: string
        requested_by: string   # Agent SPIFFE ID
        requested_at: datetime
        timeout_at: datetime
        status: string         # "pending" | "granted" | "denied" | "timeout"
  
  # Metadata
  created_at: datetime
  updated_at: datetime
  expires_at: datetime  # cleanup after request completes
```

---

## Storage Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Working Data** | Intermediate computation results | Calculation outputs |
| **Context Data** | Shared context across activities | Entity snapshots |
| **Collected Data** | Data gathered during request | Form responses |
| **Documents** | Attached documents | Evidence files |
| **Delegation Context** | Certificates and pending authority requests | Request-scoped delegation |

### Delegation Context

Delegation context stores the request-scoped authority information:

| Component | Description |
|-----------|-------------|
| **Certificates** | References to Delegation Certificates in Cipher |
| **Pending Requests** | Authority requests awaiting user consent |

→ See [Delegation Context](./delegation-context.md) for APIs and lifecycle.

---

## Lifecycle

| Event | Storage Action |
|-------|----------------|
| **Request Created** | Storage initialized |
| **During Processing** | Read/write as needed |
| **Request Completed** | Retention policy applied |
| **After Retention** | Archived or deleted |

---

## Related Documentation

- [Request Management Overview](./README.md)
- [Request Lifecycle](./request-lifecycle.md)
- [Storage Architecture](../../07-data-architecture/storage-architecture.md)

---

*TODO: Detailed design — storage backends, access patterns, retention policies*

