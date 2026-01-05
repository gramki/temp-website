# Message Envelope

> **Status:** 🟡 Draft — Under active development

The Signal Exchange enforces a **standard message envelope** for all communication with Hub Applications, regardless of application-specific payloads.

---

## Scope

This document defines the DTOs for **Signal Exchange ↔ Hub Application** communication:

```
┌────────────────────┐                    ┌────────────────────┐
│  Signal Provider   │                    │   Hub Application  │
└─────────┬──────────┘                    └─────────┬──────────┘
          │                                         │
          │ Signal Provider DTOs                    │ Application DTOs
          │ (see signal-provider-interactions.md)   │ (this document)
          │                                         │
          ▼                                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                       SIGNAL EXCHANGE                            │
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │           MESSAGE ENVELOPE (This Document)               │   │
│   │                                                          │   │
│   │   • Request Initiation DTO    (Exchange → App)           │   │
│   │   • Request Update DTO        (Exchange → App)           │   │
│   │   • Request Response DTO      (App → Exchange)           │   │
│   │   • Async Update DTO          (App → Exchange)           │   │
│   │                                                          │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

For **Signal Provider ↔ Signal Exchange** DTOs, see [Signal Provider Interactions](./signal-provider-interactions.md).

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Purpose** | Standard contract for all Hub Application communication |
| **Scope** | Signal Exchange ↔ Hub Application messages |
| **Payload** | Application-specific and Scenario-specific payloads are embedded within the envelope |

The envelope provides:
- Consistent request lifecycle tracking
- Standardized response status reporting
- Protocol-agnostic application integration
- User-reportable status information

---

## Message Dispatch vs Request Status

Signal Exchange tracks two distinct state machines:

### Message Dispatch State (per message)

Tracks delivery of individual messages (initiation, updates) to Hub Applications:

```
[CREATED] → [DISPATCHED] → [ACKNOWLEDGED | FAILED]
```

| State | Description |
|-------|-------------|
| **CREATED** | Message created, queued for dispatch |
| **DISPATCHED** | Message sent to Hub Application |
| **ACKNOWLEDGED** | Application acknowledged receipt |
| **FAILED** | Delivery failed after retries |

### Request Status (per request)

Tracks the overall business status of the Request:

```
[ACTIVE] ←→ [PENDING] → [COMPLETED]
    │                        │
    └────────────────────────┴─→ [CANCELLED]
```

| Status | Description |
|--------|-------------|
| **ACTIVE** | Request is being actively processed |
| **PENDING** | Waiting for external input, event, or human action |
| **COMPLETED** | Request finished (success or failure in response_status) |
| **CANCELLED** | Request terminated without completion |

> **Note:** Escalation applies to **Tasks** within a request's processing flow, not to the Request itself. See [Task Management](../task-management/README.md).

---

## Message Types

| Type | Direction | Purpose |
|------|-----------|---------|
| `REQUEST_INITIATION` | Relay → App | New request dispatch |
| `REQUEST_UPDATE` | Relay → App | Signal-driven update to active request |
| `REQUEST_RESPONSE` | App → Relay | Synchronous response |
| `ASYNC_UPDATE` | App → Relay | Asynchronous intermediate update |

---

## Request Envelope (Signal Exchange → Application)

### Initiation Message

Sent when a new Request is created:

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_INITIATION",
    "message_id": "uuid",
    "timestamp": "2026-01-04T10:30:00Z"
  },
  "request": {
    "id": "req-12345",
    "correlation_id": "corr-67890",
    "workbench_id": "dispute-ops",
    "scenario_id": "dispute-filing",
    "request_type": "BusinessRequest",
    "created_at": "2026-01-04T10:30:00Z"
  },
  "environment": {
    // Request-specific environment (see below)
  },
  "payload": {
    // Application-specific and Scenario-specific payload
    // Transformed from Signal via Trigger transformation
  }
}
```

### Update Message

Sent when subsequent signals update an existing Request:

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_UPDATE",
    "message_id": "uuid",
    "timestamp": "2026-01-04T10:35:00Z"
  },
  "request": {
    "id": "req-12345",
    "correlation_id": "corr-67890",
    "current_state": "IN-PROGRESS"
  },
  "environment": {
    // Request-specific environment (refreshed for update)
  },
  "update": {
    "update_type": "SIGNAL_UPDATE",     // SIGNAL_UPDATE | USER_INPUT | SYSTEM_EVENT
    "update_source": "atropos",
    "update_id": "upd-99999"
  },
  "payload": {
    // Update-specific payload
  }
}
```

---

## Request-Specific Environment

While every Hub Application has access to the base Environment configured for the Scenario, the Signal Exchange prepares and packs **request-specific overrides** in the `environment` block. This contains runtime context specific to the individual request.

### Environment Structure

```json
{
  "environment": {
    "base": {
      "tenant_id": "acme-bank",
      "environment_name": "production",
      "workbench_id": "dispute-ops",
      "scenario_id": "dispute-filing"
    },
    
    "subject": {
      "user_id": "user-12345",
      "user_type": "customer",
      "session_id": "sess-67890",
      "channel": "mobile-app",
      "locale": "en-US",
      "timezone": "America/New_York"
    },
    
    "auth": {
      "access_token": "eyJhbGciOiJS...",
      "token_type": "Bearer",
      "expires_at": "2026-01-04T11:30:00Z",
      "scopes": ["dispute:read", "dispute:write", "account:read"],
      "delegations": [
        {
          "delegator": "user-99999",
          "scope": "dispute:write",
          "expires_at": "2026-01-05T00:00:00Z"
        }
      ]
    },
    
    "identity": {
      "agent_spiffe_id": "spiffe://hub.acme.com/agent/dispute-agent-01",
      "acting_as": "user-12345",
      "impersonation": false
    },
    
    "observability": {
      "trace_id": "trace-abc123",
      "span_id": "span-def456",
      "trace_bucket": "high-priority",
      "sampling_rate": 1.0
    },
    
    "feature_flags": {
      "new_dispute_flow": true,
      "ai_document_analysis": true,
      "expedited_processing": false
    },
    
    "quotas": {
      "max_attachments": 10,
      "max_attachment_size_mb": 25,
      "priority_tier": "standard"
    },
    
    "routing": {
      "preferred_region": "us-east-1",
      "fallback_regions": ["us-west-2", "eu-west-1"]
    }
  }
}
```

### Environment Components

| Component | Description |
|-----------|-------------|
| **base** | Tenant, environment, workbench, scenario context |
| **subject** | User/subject information initiating the request |
| **auth** | Access tokens, scopes, delegations for downstream calls |
| **identity** | Agent SPIFFE identity, acting-as relationships |
| **observability** | Trace IDs, buckets, sampling configuration |
| **feature_flags** | Request-scoped feature flag overrides |
| **quotas** | Request-scoped quota limits |
| **routing** | Request-scoped routing preferences |

### Environment Preparation

Signal Exchange prepares the request-specific environment by:

| Step | Description |
|------|-------------|
| 1. **Base Resolution** | Load Scenario's base environment from Workbench |
| 2. **Subject Extraction** | Extract user/subject info from signal or auth context |
| 3. **Token Refresh** | Obtain/refresh access tokens for downstream services |
| 4. **Scope Calculation** | Calculate effective scopes based on user, delegations, scenario |
| 5. **Flag Resolution** | Resolve feature flags for user + scenario combination |
| 6. **Trace Propagation** | Propagate or generate trace context |
| 7. **Quota Lookup** | Look up applicable quotas for subject + scenario |

### Environment Refresh on Updates

For `REQUEST_UPDATE` messages, the environment is **refreshed**:
- Tokens may be renewed if expired
- Feature flags re-evaluated (may have changed)
- Subject context preserved from initiation
- New trace span created under same trace ID

---

## Response Envelope (Application → Signal Exchange)

### Synchronous Response

Applications **must** respond using the standard envelope:

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_RESPONSE",
    "message_id": "uuid",
    "timestamp": "2026-01-04T10:32:00Z"
  },
  "request": {
    "id": "req-12345",
    "correlation_id": "corr-67890"
  },
  "request_status": {
    "status": "ACTIVE",                 // ACTIVE | PENDING | COMPLETED | CANCELLED
    "status_reason": "Awaiting document verification"
  },
  "response_status": {
    "code": "ACCEPTED",
    "description": "Dispute case opened successfully",
    "user_message": "Your dispute has been registered. Case ID: DSP-2026-12345"
  },
  "payload": {
    // Application-specific response payload
  }
}
```

### Asynchronous Update

Long-running Applications (workflows, durable workflows, case management) send intermediate updates via `ASYNC_UPDATE` messages. All updates from Applications are routed through Signal Exchange using this message type.

The `update_type` field discriminates the sub-type of the async update:

```
ASYNC_UPDATE
    ├── STATUS_CHANGE      (Request status transition)
    ├── TASK_LIFECYCLE     (Task events)
    ├── DECISION           (Decision records)
    ├── THOUGHT            (Reasoning/rationale)
    ├── MEMO               (Scoped notes)
    ├── MEMORY_UPDATE      (Subject/Org/Session memory)
    ├── PROGRESS           (Progress indicators)
    ├── MILESTONE          (Checkpoints)
    └── ERROR              (Recoverable errors)
```

### ASYNC_UPDATE Base Envelope

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "ASYNC_UPDATE",
    "message_id": "uuid",
    "timestamp": "2026-01-04T12:45:00Z"
  },
  "request": {
    "id": "req-12345",
    "correlation_id": "corr-67890"
  },
  "update": {
    "update_type": "STATUS_CHANGE",   // Discriminator for sub-type
    "sequence": 5                      // Ordering for concurrent updates
  },
  "user_notification": {               // Optional: trigger observer notification
    "enabled": true,
    "title": "...",
    "message": "...",
    "priority": "normal"
  },
  "payload": {
    // Sub-type specific payload (see below)
  }
}
```

---

## ASYNC_UPDATE Sub-Types

### STATUS_CHANGE

Request status transition:

```json
{
  "update": { "update_type": "STATUS_CHANGE", "sequence": 1 },
  "payload": {
    "request_status": {
      "status": "PENDING",
      "status_reason": "Awaiting customer document upload"
    }
  }
}
```

### TASK_LIFECYCLE

Task created, assigned, acted upon, or status changed:

```json
{
  "update": { "update_type": "TASK_LIFECYCLE", "sequence": 2 },
  "payload": {
    "task": {
      "id": "task-12345",
      "queue_id": "dispute-review-queue",
      "event": "PICKED",                // CREATED | PICKED | ACTED | STATUS_CHANGE | ESCALATED
      "agent_id": "agent-67890",
      "agent_type": "human",
      "previous_status": "QUEUED",
      "current_status": "IN_PROGRESS"
    }
  }
}
```

### DECISION

Decision record with optional evidence reference:

```json
{
  "update": { "update_type": "DECISION", "sequence": 3 },
  "payload": {
    "decision": {
      "id": "dec-99999",
      "type": "DISPUTE_VALIDITY",
      "outcome": "VALID",
      "rationale": "Documentation supports customer claim",
      "evidence_ref": "evidence://caf/bundles/evb-88888",
      "decided_by": {
        "agent_id": "agent-67890",
        "agent_type": "ai"
      }
    }
  }
}
```

### THOUGHT

Reasoning or rationale comment by agent or system:

```json
{
  "update": { "update_type": "THOUGHT", "sequence": 4 },
  "payload": {
    "thought": {
      "id": "thot-77777",
      "author": {
        "agent_id": "seer-agent-01",
        "agent_type": "ai"
      },
      "content": "Customer has a history of valid disputes. Prioritizing based on loyalty tier.",
      "context": {
        "relates_to": "task-12345",
        "context_type": "task_assignment"
      }
    }
  }
}
```

### MEMO

Semi-structured note for future reference (scoped, visibility-controlled):

```json
{
  "update": { "update_type": "MEMO", "sequence": 5 },
  "payload": {
    "memo": {
      "id": "memo-66666",
      "scope": "subject",              // request | subject | object
      "scope_id": "customer-12345",
      "author": {
        "agent_id": "human-agent-99",
        "agent_type": "human"
      },
      "content": {
        "title": "Preferred Resolution Method",
        "body": "Customer prefers phone callbacks over email.",
        "tags": ["preference", "contact"]
      },
      "visibility": {
        "level": "role",               // author | team | role
        "roles": ["dispute_agent", "customer_service"]
      },
      "retention": {
        "policy": "subject_lifetime"
      }
    }
  }
}
```

> **Note:** Memos are NOT Memory Updates. Different retention and access semantics.

### MEMORY_UPDATE

Subject, Org, or Session memory update (NOT Agent memory):

```json
{
  "update": { "update_type": "MEMORY_UPDATE", "sequence": 6 },
  "payload": {
    "memory": {
      "type": "subject",               // subject | org | session
      "subject_id": "customer-12345",
      "operation": "upsert",
      "entries": [
        {
          "key": "preferred_contact_method",
          "value": "phone",
          "source": "request-12345",
          "confidence": 0.95
        }
      ]
    }
  }
}
```

### PROGRESS

Progress indicator update:

```json
{
  "update": { "update_type": "PROGRESS", "sequence": 7 },
  "payload": {
    "progress": {
      "percent_complete": 60,
      "current_step": "manager_review",
      "total_steps": 5,
      "completed_steps": 3
    }
  }
}
```

### MILESTONE

Significant checkpoint reached:

```json
{
  "update": { "update_type": "MILESTONE", "sequence": 8 },
  "payload": {
    "milestone": {
      "id": "ms-55555",
      "name": "Document Verification Complete",
      "description": "All required documents verified"
    }
  }
}
```

### ERROR

Recoverable error or warning:

```json
{
  "update": { "update_type": "ERROR", "sequence": 9 },
  "payload": {
    "error": {
      "code": "DOCUMENT_UNREADABLE",
      "severity": "warning",           // warning | error
      "message": "Uploaded document is partially unreadable",
      "recoverable": true,
      "suggested_action": "Request customer to re-upload"
    }
  }
}
```

---

See [Request Lifecycle](../request-management/request-lifecycle.md) for additional details on update semantics.

---

## Async Update Processing

Signal Exchange processes async updates by:
1. Updating Request state (if state change)
2. Recording update in Request history
3. Dispatching to registered **observer modules** (NOT to agents/tasks directly)

**Critical Principle:** Signal Exchange dispatches Request Updates to observer modules only. It does NOT:
- Dispatch to individual agents or tasks
- Attribute updates to specific tasks or agents
- Determine which agent should be notified

Observer modules (e.g., MS Teams module, Ops Center) receive the full Request Update and parse it to determine:
- Which tasks are affected (from `TASK_LIFECYCLE` payload)
- Which agents should be notified (from task assignment info)
- What action to take (add to group, post message, etc.)

See [Observer Notifications](./observer-notifications.md) for notification dispatch details.

---

## Request Status vs Response Status

| Aspect | Request Status | Response Status |
|--------|----------------|-----------------|
| **Purpose** | Business state of the Request | Semantic outcome of the operation |
| **Values** | `ACTIVE`, `PENDING`, `COMPLETED`, `CANCELLED` | Application-defined codes |
| **Persistence** | Tracked by Signal Exchange | Recorded for audit and reporting |
| **User-Facing** | Yes — visible in dashboards | Yes — `user_message` is reportable |

---

## Response Status Codes

Standard response status codes (extensible by Application):

### Success Codes

| Code | Description |
|------|-------------|
| `ACCEPTED` | Request accepted, processing initiated |
| `COMPLETED` | Request completed successfully |
| `PARTIAL` | Partially completed, some items failed |

### Failure Codes

| Code | Description |
|------|-------------|
| `REJECTED` | Request rejected (validation, policy, etc.) |
| `FAILED` | Processing failed (error during execution) |
| `TIMEOUT` | Processing timed out |
| `CANCELLED` | Request cancelled by user or system |

### In-Progress Codes

| Code | Description |
|------|-------------|
| `PROCESSING` | Actively processing |
| `AWAITING_INPUT` | Waiting for additional input |
| `AWAITING_APPROVAL` | Waiting for human approval |
| `QUEUED` | Queued for processing |

---

## Response Status Structure

```yaml
response_status:
  code: string              # Status code (ACCEPTED, COMPLETED, FAILED, etc.)
  description: string       # Technical description for logs/debugging
  user_message: string      # Human-readable message for end users
  details:                  # Optional additional details
    - field: string
      issue: string
      suggestion: string
  retry_after: duration     # Optional: suggest retry timing
  reference_id: string      # Optional: external reference (e.g., case ID)
```

---

## State Transitions

### Message Dispatch Transitions

```
CREATED → DISPATCHED (by Signal Exchange)
DISPATCHED → ACKNOWLEDGED (by Application)
DISPATCHED → FAILED (after retry exhaustion)
```

### Request Status Transitions

```
(initial) → ACTIVE (on first message acknowledgment)
ACTIVE → PENDING (waiting for input/event)
PENDING → ACTIVE (input received, processing resumes)
ACTIVE → COMPLETED (processing finished)
ACTIVE → CANCELLED (request terminated)
PENDING → CANCELLED (request terminated while waiting)
```

### Terminal States

- `COMPLETED` — cannot transition further
- `CANCELLED` — cannot transition further

---

## Envelope Versioning

| Field | Description |
|-------|-------------|
| `version` | Envelope version (e.g., "1.0") |
| **Backward Compatibility** | Signal Exchange supports older envelope versions |
| **Forward Compatibility** | Unknown fields are preserved but not processed |

---

## Integration with Response Transformer

The Response Transformer:
1. Receives the Application's response envelope
2. Extracts `response_status` for user-facing reporting
3. Transforms `payload` to I/O Gateway protocol format
4. Delivers formatted response to I/O Gateway

---

## Example: Dispute Filing Flow

```
1. Signal arrives (customer files dispute)
2. Signal Exchange creates initiation message (dispatch: CREATED)
3. Signal Exchange dispatches to Seer Case Agent (dispatch: DISPATCHED)
4. Seer acknowledges (dispatch: ACKNOWLEDGED)
5. Seer responds: { request_status: ACTIVE, response_status: ACCEPTED }
6. Signal Exchange updates Request status to ACTIVE
7. Response Transformer sends to Heracles: HTTP 202, "Case opened"
...
8. Seer awaits document upload
9. Seer sends async update: { request_status: PENDING, response_status: AWAITING_INPUT }
10. Signal Exchange updates Request status to PENDING
...
11. Customer uploads document (new signal → update message)
12. Signal Exchange dispatches update to Seer
13. Seer resumes: { request_status: ACTIVE, response_status: PROCESSING }
...
14. Seer completes case
15. Seer responds: { request_status: COMPLETED, response_status: COMPLETED }
16. Signal Exchange updates Request status to COMPLETED
```

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Application Router](./application-router.md)
- [Response Transformer](./response-transformer.md)
- [Request Management](../request-management/README.md)

---

*TODO: Detailed design — envelope validation, versioning strategy, error envelope format*

