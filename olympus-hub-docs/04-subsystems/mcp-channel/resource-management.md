# Resource Management

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

Resources are request-scoped entities exposed for subscription, enabling real-time updates via JSON-RPC notifications. Resources are session-bound and managed by MCP Channel.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Expose Hub entities for real-time subscription and updates |
| **Lifecycle** | Managed by MCP Channel (create, update, delete, subscribe, unsubscribe) |
| **Subscription** | Session-bound (cannot persist beyond session) |
| **Notifications** | JSON-RPC notifications on resource changes |
| **Transport** | SSE (default) and Streamable HTTP (fallback) |
| **Applicability** | Scenario-based templates only (machine-template does not support resources) |

---

## Resource Types

Resources vary by template kind:

| Template Kind | Resource Types | URI Pattern |
|---------------|----------------|-------------|
| `business-user-template` | Requests | `request://{request_id}` |
| `supervisor-template` | Queues, Escalations, SLA Alerts | `queue://{queue_id}`, `escalation://{task_id}`, `sla-alert://{alert_id}` |
| `agent-template` | Tasks, Requests | `task://{task_id}`, `request://{request_id}` |
| `creator-template` | Scenarios, Feedback | `scenario://{scenario_id}`, `feedback://{feedback_id}` |
| `admin-template` | Workbenches | `workbench://{workbench_id}` |
| `auditor-template` | Audit Trails | `audit-trail://{trail_id}` |

---

## Resource URI Patterns

### Request Resources

Each request is exposed as **one resource** containing all available data:

```
request://{request_id}
```

**Resource Content:**
- Request status and metadata
- Request timeline
- Request history (updates)
- Associated documents
- Related entities
- Task information (if applicable)

**Example:**
```
request://REQ-12345
```

### Task Resources

```
task://{task_id}
```

**Resource Content:**
- Task status and metadata
- Task requirements
- Task context (request, scenario)
- Available actions

### Queue Resources

```
queue://{queue_id}
```

**Resource Content:**
- Queue metrics (pending, in-progress, completed)
- Agent assignments
- SLA status
- Recent activity

### Other Resource Types

| Resource Type | URI Pattern | Content |
|---------------|-------------|---------|
| Escalation | `escalation://{task_id}` | Escalation details, resolution options |
| SLA Alert | `sla-alert://{alert_id}` | Alert details, at-risk requests |
| Scenario | `scenario://{scenario_id}` | Scenario definition, status |
| Feedback | `feedback://{feedback_id}` | Feedback details, status |
| Workbench | `workbench://{workbench_id}` | Workbench configuration, status |
| Audit Trail | `audit-trail://{trail_id}` | Audit trail entries |

---

## Resource Lifecycle

### Lifecycle Operations

| Operation | Description | Trigger |
|-----------|-------------|---------|
| **Create** | Resource created when entity is created or first accessed | Request created, task assigned, etc. |
| **Update** | Resource updated when entity changes | Request update, task status change, etc. |
| **Delete** | Resource deleted when entity is completed/cancelled | Request completed, task closed, etc. |

### Lifecycle Management

Resources are managed by MCP Channel:

```
1. Entity created/updated in Hub
2. MCP Channel checks: Is this resource subscribed to in active sessions?
3. If yes:
   a. Update resource data
   b. Send notification: notifications/resources/updated { uri: "request://REQ-123" }
4. Client receives notification
5. Client calls resources/read("request://REQ-123") to fetch updated data
```

---

## Resource Subscriptions

### Subscription Model

**Session-bound subscriptions:**

- Subscriptions are tied to MCP session
- Cannot persist beyond session
- Client must re-subscribe on reconnection
- Maximum subscriptions per session: `max_subscriptions` (configurable in CRD)

### Subscription Flow

```
1. Client establishes MCP session
2. Client subscribes: resources/subscribe("request://REQ-123")
3. Server confirms subscription
4. Server sends notifications on resource changes:
   notifications/resources/updated {
     uri: "request://REQ-123"
   }
5. Client receives notification
6. Client calls resources/read("request://REQ-123") to fetch updated data
7. Client unsubscribes: resources/unsubscribe("request://REQ-123")
   OR
   Session terminates → all subscriptions automatically removed
```

### Multiple Subscriptions

Clients can subscribe to multiple resources:

```
resources/subscribe("request://REQ-123")
resources/subscribe("request://REQ-456")
resources/subscribe("task://TASK-789")
```

Each subscription is independent and receives its own notifications.

---

## Notification Mechanisms

### JSON-RPC Notifications

Server sends notifications when resources change:

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "request://REQ-123"
  }
}
```

### Transport Options

| Transport | Default | Characteristics |
|-----------|---------|-----------------|
| **SSE** | Yes (default) | Server-Sent Events, unidirectional, lower latency |
| **Streamable HTTP** | Fallback | Bidirectional chunked HTTP, better compatibility |

**Selection:**
- SSE used by default when middleware supports it
- Streamable HTTP used as fallback
- Automatic client fallback if SSE fails

---

## Resource Discovery

### Discovery Methods

| Method | Description |
|--------|-------------|
| **Tool-based** | Use tools to discover resources (e.g., `list_active_requests()`) |
| **Direct URI** | Client knows resource URI (e.g., from previous interaction) |
| **Notification** | Client receives notification about new resource |

### Example: Request Discovery

```
1. Client calls list_active_requests() tool
2. Tool returns list of requests with IDs
3. Client subscribes to specific requests:
   resources/subscribe("request://REQ-123")
   resources/subscribe("request://REQ-456")
4. Client receives notifications on changes
```

---

## Resource Access Control

Resources respect access control:

- **User Permissions**: User can only subscribe to resources they have access to
- **OPA Policy**: Access evaluated per resource subscription request
- **Template Scope**: Resources filtered by template kind and exposed scenarios

**Example:**
- Business user can subscribe to their own requests
- Supervisor can subscribe to queues in their workbench
- Agent can subscribe to tasks assigned to them

---

## Resource Data Model

### Request Resource Example

```json
{
  "uri": "request://REQ-123",
  "mimeType": "application/json",
  "contents": {
    "request_id": "REQ-123",
    "status": "IN_PROGRESS",
    "scenario": "bill-payment",
    "subject": {
      "id": "CUST-123",
      "name": "John Doe"
    },
    "timeline": [
      {
        "timestamp": "2026-01-17T10:00:00Z",
        "event": "REQUEST_CREATED",
        "details": "..."
      },
      {
        "timestamp": "2026-01-17T10:05:00Z",
        "event": "TASK_CREATED",
        "details": "..."
      }
    ],
    "documents": [
      {
        "id": "DOC-001",
        "name": "invoice.pdf",
        "type": "invoice"
      }
    ],
    "related_entities": {
      "account": "ACC-456",
      "transaction": "TXN-789"
    }
  }
}
```

---

## Related Documentation

- [Session Management](./session-management.md) — Session-bound subscriptions
- [MCP Server CRD](./mcp-server-crd.md) — Resource configuration
- [MCP Router](../../05-infrastructure/mcp-router.md) — Notification transport

---

*TODO: C3-level details — resource data schema, notification batching, subscription persistence*
