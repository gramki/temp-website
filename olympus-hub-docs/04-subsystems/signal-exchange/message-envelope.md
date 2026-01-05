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
│   │   SX → HA (Signal Exchange to Hub Application):          │   │
│   │   • Request Initiation                                   │   │
│   │   • Request Update                                       │   │
│   │                                                          │   │
│   │   HA → SX (Hub Application to Signal Exchange):          │   │
│   │   • Request Update (with Hub-specified payloads)         │   │
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

### Envelope Contents Summary

All messages are scoped to a **Tenant** and **Subscription**. This context is always present in the envelope.

| Direction | Envelope Contains |
|-----------|-------------------|
| **SX → HA** | Tenant/Subscription scope, Origination info, Originator, Request metadata (incl. subject), Environment (Workbench/Scenario/Request scoped), Payload with content_type and semantic_type |
| **HA → SX** | Tenant/Subscription scope, Request identification (workbench, scenario, request-id), Hub-specified update payload, Optional piggyback_payload with content_type and object_type |

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
| `REQUEST_INITIATION` | Exchange → App | New request dispatch |
| `REQUEST_UPDATE` | Exchange → App | Signal-driven update to active request |
| `REQUEST_RESPONSE` | App → Exchange | Synchronous response |
| `REQUEST_UPDATE` | App → Exchange | Asynchronous update (same as REQUEST_UPDATE) |

> **Note:** In Signal Exchange ↔ Hub Application interactions, **Async Update and Request Update are the same concept**. Hub Applications send `REQUEST_UPDATE` messages for any intermediate updates, whether synchronous or asynchronous. The distinction between "sync" and "async" is a timing concern, not a message type concern.

---

## Signal Exchange → Hub Application (SX → HA)

Signal Exchange sends two message types to Hub Applications:
- **Request Initiation** — when a new Request is created
- **Request Update** — when subsequent signals update an existing Request

Both use a **standardized envelope format** containing:

| Envelope Section | Description |
|------------------|-------------|
| **origination** | How and where this message originated |
| **originator** | Who/what triggered this message |
| **request** | Request metadata including subject information |
| **environment** | Workbench, Scenario, and Request-scoped information |
| **payload** | Content type, semantic type, and payload data |

### Request Initiation Message

Sent when a new Request is created:

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_INITIATION",
    "message_id": "uuid",
    "timestamp": "2026-01-04T10:30:00Z",
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001"
  },
  
  "origination": {
    "signal_id": "sig-12345",
    "signal_provider_id": "sp-heracles-api",
    "trigger_id": "trg-dispute-filing",
    "channel": "mobile-app"
  },
  
  "originator": {
    "type": "signal_provider",           // signal_provider | system | schedule
    "id": "sp-heracles-api",
    "name": "Heracles API Gateway"
  },
  
  "request": {
    "id": "req-12345",
    "correlation_id": "corr-67890",
    "workbench_id": "dispute-ops",
    "scenario_id": "dispute-filing",
    "request_type": "BusinessRequest",   // ServiceRequest | BusinessRequest | SystemRequest
    "created_at": "2026-01-04T10:30:00Z",
    "subject": {                         // Present when request has a subject
      "type": "customer",
      "id": "cust-67890",
      "name": "John Doe",
      "segment": "premium"
    }
  },
  
  "environment": {
    // Workbench, Scenario, and Request-scoped information (see below)
  },
  
  "payload": {
    "content_type": "application/json",  // application/json | application/base64
    "semantic_type": "com.acme.dispute.DisputeFilingRequest",
    "data": {
      // Application-specific and Scenario-specific payload
      // Transformed from Signal via Trigger transformation
    }
  }
}
```

### Request Update Message (SX → HA)

Sent when subsequent signals update an existing Request:

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_UPDATE",
    "message_id": "uuid",
    "timestamp": "2026-01-04T10:35:00Z",
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001"
  },
  
  "origination": {
    "signal_id": "sig-23456",
    "signal_provider_id": "sp-atropos-events",
    "trigger_id": "trg-document-uploaded",
    "channel": "event-bus"
  },
  
  "originator": {
    "type": "signal_provider",
    "id": "sp-atropos-events",
    "name": "Atropos Event Bus"
  },
  
  "request": {
    "id": "req-12345",
    "correlation_id": "corr-67890",
    "workbench_id": "dispute-ops",
    "scenario_id": "dispute-filing",
    "current_status": "ACTIVE",
    "subject": {
      "type": "customer",
      "id": "cust-67890"
    }
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
    "content_type": "application/json",
    "semantic_type": "com.acme.dispute.DocumentUploadedEvent",
    "data": {
      // Update-specific payload
    }
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

## Hub Application → Signal Exchange (HA → SX)

Hub Applications send **Request Update** messages to Signal Exchange. All messages must:

1. **Comply with Signal Exchange's Request Update DTOs** — use the standardized envelope
2. **Contain Request identifying data** — workbench, scenario, request-id (as received from Signal Exchange)
3. **Use Hub-specified payloads** — for each update type (Task Lifecycle, Memo, Thought, etc.)
4. **Optionally include piggyback-payload** — additional custom payload from the Hub Application

### Compliance Requirements

| Requirement | Description |
|-------------|-------------|
| **Tenant/Subscription Scope** | Every message MUST include `tenant_id` and `subscription_id` as received in earlier SX → HA messages |
| **Request Identification** | Every message MUST include `workbench_id`, `scenario_id`, `request_id` as received in earlier SX → HA messages |
| **Hub-Specified Payloads** | Each `update_type` has a Hub-defined payload structure (see sub-types below) |
| **Piggyback Payload** | Applications MAY include additional custom data in `piggyback_payload` |
| **Piggyback Envelope** | Piggyback payload has its own `content_type` and `object_type` |

### Synchronous Response

Applications respond to `REQUEST_INITIATION` or `REQUEST_UPDATE` (from SX) with a synchronous response:

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_RESPONSE",
    "message_id": "uuid",
    "timestamp": "2026-01-04T10:32:00Z",
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001"
  },
  
  "request": {
    "workbench_id": "dispute-ops",
    "scenario_id": "dispute-filing",
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
    "content_type": "application/json",
    "semantic_type": "com.acme.dispute.DisputeFilingResponse",
    "data": {
      // Application-specific response payload
    }
  },
  
  "piggyback_payload": {                // Optional: additional custom payload
    "content_type": "application/json",
    "object_type": "com.acme.dispute.AuditContext",
    "data": {
      // Custom data from Hub Application
    }
  }
}
```

### Request Update (from Application)

Long-running Applications (workflows, durable workflows, case management) send intermediate updates via `REQUEST_UPDATE` messages.

> **Note:** Whether the update is sent synchronously (inline with a response) or asynchronously (at a later time) does not change the message type. Both use `REQUEST_UPDATE`.

The `update_type` field discriminates the sub-type of the update:

```
REQUEST_UPDATE (from Application)
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

### REQUEST_UPDATE Base Envelope (from Application)

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_UPDATE",
    "message_id": "uuid",
    "timestamp": "2026-01-04T12:45:00Z",
    "tenant_id": "acme-bank",            // Required: as received from SX
    "subscription_id": "sub-prod-001"    // Required: as received from SX
  },
  
  "request": {
    "workbench_id": "dispute-ops",       // Required: as received from SX
    "scenario_id": "dispute-filing",     // Required: as received from SX
    "id": "req-12345",                   // Required: as received from SX
    "correlation_id": "corr-67890"
  },
  
  "update": {
    "update_type": "STATUS_CHANGE",      // Discriminator for sub-type
    "sequence": 5                         // Ordering for concurrent updates
  },
  
  "user_notification": {                 // Optional: trigger observer notification
    "enabled": true,
    "title": "...",
    "message": "...",
    "priority": "normal"
  },
  
  "payload": {
    // Hub-specified payload for this update_type (see below)
  },
  
  "piggyback_payload": {                 // Optional: additional custom payload
    "content_type": "application/json",
    "object_type": "com.acme.dispute.CustomContext",
    "data": {
      // Custom data from Hub Application
    }
  }
}
```

---

## REQUEST_UPDATE Sub-Types (from Application)

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

## Request Update Processing

Signal Exchange processes Request Updates (from Hub Applications) by:
1. Updating Request state (if state change)
2. Recording update in Request history
3. Dispatching to registered **observer modules** (NOT to agents/tasks directly)

**Critical Principle:** Signal Exchange dispatches Request Updates to observer modules only. It does NOT:
- Dispatch to individual agents or tasks
- Attribute updates to specific tasks or agents
- Determine which agent should be notified

Observer modules (e.g., MS Teams module, Ops Center, originating Signal Provider) receive the full Request Update and parse it to determine:
- Which tasks are affected (from `TASK_LIFECYCLE` payload)
- Which agents should be notified (from task assignment info)
- What action to take (add to group, post message, etc.)

> **Note:** Originating Signal Providers are automatically registered as observers and receive Request Updates via their **Outgoing Message DTO**. See [Signal Provider Interactions](./signal-provider-interactions.md).

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

