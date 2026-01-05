# Notification Services

> **Status:** 🟡 Draft — Under active development

The Notification Services subsystem provides a single Notification Service that translates Request Updates from Signal Exchange into notifications for respective personas (agents, business users, supervisors, tenant admins) using one or more notification mechanisms (Email, SMS, Push Notification, Webhook) based on Scenario specifications and recipient preferences.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Translate Request Updates into persona-specific notifications |
| **Role** | Observer module of Signal Exchange |
| **Channel** | "Notification" channel |
| **Mechanisms** | Email, SMS, Push Notification, Webhook (transport+scheme composite) |
| **Integration** | Cipher Notification Service (CNS) for actual delivery |

---

## Architecture

Notification Services is a **single service** with persona-specific handlers. It acts as an observer module of Signal Exchange.

```
┌─────────────────────────────────────────────────────────────────┐
│                    SIGNAL EXCHANGE                                │
│                                                                  │
│  Sends REQUEST_UPDATE messages to registered observer modules    │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              NOTIFICATION SERVICES (Observer Module)              │
│                    (Single Service)                               │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │         Notification Service (Main Observer)              │   │
│  │                                                           │   │
│  │  • Receives all Request Updates from Signal Exchange     │   │
│  │  • Queries Hub control plane for Scenario specifications │   │
│  │  • Filters updates based on Scenario specifications       │   │
│  │  • Resolves recipients (consults Request, Scenario,       │   │
│  │    Workbench objects)                                     │   │
│  │  • Determines persona types                               │   │
│  │  • Routes to persona-specific handlers                    │   │
│  └───────────────┬──────────────────────────────────────────┘   │
│                  │                                                │
│      ┌───────────┼───────────┐                                    │
│      │           │           │                                    │
│      ▼           ▼           ▼                                    │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐                      │
│  │ Agent │ │Business│ │Super-  │ │Tenant  │                      │
│  │Handler│ │User    │ │visor   │ │Admin   │                      │
│  │       │ │Handler │ │Handler │ │Handler │                      │
│  └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘                      │
│      │         │         │         │                             │
│      └─────────┴─────────┴─────────┘                             │
│                  │                                                │
│                  ▼                                                │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │         Cipher Notification Service (CNS)                │   │
│  │                                                           │   │
│  │  • Receives notification requests                        │   │
│  │  • Routes to appropriate service providers               │   │
│  │  • Handles delivery, retries, failures                   │   │
│  │  • Sends callbacks for delivery status, read receipts,   │   │
│  │    and CTA responses                                     │   │
│  └───────────────┬──────────────────────────────────────────┘   │
│                  │                                                │
│                  ▼                                                │
│         Service Providers (Email, SMS, Push, Webhook)            │
│                  │                                                │
│                  ▼                                                │
│              Recipients (Agents, Users, etc.)                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Responsibilities

The Notification Service (single service with persona-specific handlers) is responsible for:

1. **Translating Request Updates into notifications** for respective personas
2. **Using one or more notification mechanisms** as per Scenario specifications and recipient preferences
3. **Overlapping supported mechanisms** in scenario specification with recipient preferences (default: intersection)
4. **Sending notifications** to respective personas using supported notification mechanisms (multiple mechanisms sent in parallel)
5. **Receiving callbacks/reverse-notifications** from Cipher Notification Service for:
   - Delivery failures
   - Read receipts
   - CTA (Call-to-Action) responses initiated from notifications
6. **Registering as Signal Provider** with Signal Exchange for CTA signal creation

---

## Observer Registration

The Notification Service registers as an observer module with Signal Exchange:

```json
{
  "subscription": {
    "id": "sub-notification-services",
    "observer_type": "module",
    "observer_id": "notification-services",
    
    "scope": {
      "type": "tenant",              // Subscribe to all requests in tenant
      "tenant_id": "acme-bank"
    },
    
    "filters": {
      "update_types": [
        "STATUS_CHANGE",
        "TASK_LIFECYCLE",
        "DECISION",
        "THOUGHT",
        "MEMO",
        "MEMORY_UPDATE",
        "PROGRESS",
        "MILESTONE",
        "ERROR",
        "REMINDER_NOTIFICATION"
      ]
    },
    
    "delivery": {
      "channel": "webhook",
      "endpoint": "https://hub/notification-services/updates",
      "format": "full"
    }
  }
}
```

---

## Notification Flow

```
1. Signal Exchange sends REQUEST_UPDATE to Notification Service
   └─> Notification Service receives update

2. Notification Service processes update:
   └─> Queries Workbench Management for Scenario specification
   └─> Filters update based on Scenario notification requirements
   └─> Resolves recipients by consulting Request, Scenario, and Workbench objects:
       • task-assignee: from TASK_LIFECYCLE payload
       • subject: from request.subject
       • supervisor: from workbench configuration
       • all-assignees: from request task assignments
       • all-actors: from request history (efficiently tracked by Signal Exchange)
   └─> Determines persona type for each recipient (from user role/profile)

3. For each recipient:
   └─> Routes to appropriate persona-specific handler
   └─> Loads user preferences (scoped to workbench, with tenant fallback)
   └─> Applies user preference event filters (after scenario filtering)
   └─> Overlaps scenario-supported mechanisms with user preferences
   └─> Selects mechanisms to use (default: intersection)
   └─> Renders templates with:
       • Complete Request Update DTO
       • User profile object (from Cipher)
   └─> Sends notification request(s) to Cipher Notification Service
       (multiple mechanisms sent in parallel, each recipient sent individually)

4. Cipher Notification Service:
   └─> Routes to appropriate service providers
   └─> Handles delivery, retries, failures
   └─> Sends callbacks for delivery status, read receipts, CTA responses

5. Callbacks from CNS:
   └─> Received by originating persona-specific handler
   └─> Processed:
       • Delivery failures → Signal sent to SX → Preconfigured trigger translates to MEMO
       • CTA responses → Signal sent to SX (Notification Service acts as Signal Provider)
```

---

## Scenario Notification Specification

Notification requirements are defined in Scenario specifications:

```yaml
scenario:
  id: "dispute-filing"
  name: "Dispute Filing"
  
  notifications:
    - event: "STATUS_CHANGE"
      recipients:
        - "subject"                    # Customer who filed dispute
        - "supervisor"                  # Supervisor of workbench
      templates:
        sms:
          template: "{{request.status}} - Your dispute {{request.id}} status: {{request.status_reason}}"
        email:
          template: |
            Subject: Dispute {{request.id}} - {{request.status}}
            
            Your dispute has been updated:
            Status: {{request.status}}
            Reason: {{request.status_reason}}
            
            View details: {{request.url}}
    
    - event: "TASK_LIFECYCLE"
      recipients:
        - "task-assignee"               # Agent assigned to task
        - "all-assignees"               # All agents assigned to any task in request
      templates:
        email:
          template: |
            Subject: New Task Assignment - {{task.id}}
            
            You have been assigned a new task:
            Task: {{task.id}}
            Queue: {{task.queue_id}}
            Priority: {{task.priority}}
        push:
          template: "New task assigned: {{task.id}}"
    
    - event: "MILESTONE"
      recipients:
        - "subject"
        - "all-actors"                  # All agents who have acted on request
      templates:
        email:
          template: |
            Subject: Milestone Reached - {{milestone.name}}
            
            {{milestone.description}}
        sms:
          template: "Milestone: {{milestone.name}}"
```

### Recipient Types

| Recipient Type | Resolution Source | Description |
|----------------|-------------------|-------------|
| **task-assignee** | TASK_LIFECYCLE payload | Agent assigned to the specific task (from `task.agent_id` in TASK_LIFECYCLE event) |
| **subject** | Request object | Subject of the request (from `request.subject` - customer, entity, etc.) |
| **supervisor** | Workbench configuration | Supervisor of the workbench (from workbench supervisor configuration) |
| **all-assignees** | Request task assignments | All agents assigned to any task in the request (from request's task assignment history) |
| **all-actors** | Request history | All agents who have acted on the request (efficiently tracked by Signal Exchange in request history) |

**Recipient Resolution:**
The Notification Service consults Request, Scenario, and Workbench objects to resolve recipient types to actual user IDs. This resolution happens in the main observer component before routing to persona-specific handlers.

### Template Format

Templates use **Mustache** syntax for variable substitution:
- Templates are defined per mechanism (sms, email, push, webhook)
- Templates are versioned with the Scenario (no independent versioning)
- To change a template, the Scenario version must be bumped

### Template Rendering Context

When rendering templates, the following data is available:
- **Complete Request Update DTO** — Full Request Update message from Signal Exchange
- **User Profile Object** — User profile information from Cipher (name, roles, preferences, etc.)

**Available Template Variables:**
- `{{request.*}}` — Request fields (id, status, status_reason, etc.)
- `{{task.*}}` — Task fields (if TASK_LIFECYCLE event)
- `{{milestone.*}}` — Milestone fields (if MILESTONE event)
- `{{user.*}}` — User profile fields (name, email, phone, etc.)
- `{{workbench.*}}` — Workbench fields
- `{{scenario.*}}` — Scenario fields

---

## User Preferences

User preferences are stored by the Notification Service in its own store, scoped to:
- **Tenant Subscription** (fallback/default preferences)
- **Workbench** (workbench-specific preferences take precedence)

**Precedence:** Workbench-scoped preferences take precedence over tenant-scoped preferences. If a user is in multiple workbenches, each workbench can have its own preferences.

### Preference Structure

**Workbench-Scoped Preferences (takes precedence):**
```json
{
  "user_id": "user-12345",
  "tenant_id": "acme-bank",
  "subscription_id": "sub-prod-001",
  "workbench_id": "dispute-ops",
  
  "preferences": {
    "mechanisms": {
      "email": {
        "enabled": true,
        "priority": 1,
        "address": "user@example.com"
      },
      "sms": {
        "enabled": true,
        "priority": 2,
        "phone": "+1234567890"
      },
      "push": {
        "enabled": false
      },
      "webhook": {
        "enabled": false
      }
    },
    "time_windows": {
      "email": "always",
      "sms": "09:00-18:00"
    },
    "event_filters": {
      "min_priority": "normal"
    }
  }
}
```

**Tenant-Scoped Preferences (fallback/default):**
```json
{
  "user_id": "user-12345",
  "tenant_id": "acme-bank",
  "subscription_id": "sub-prod-001",
  "workbench_id": null,  // Tenant-level, no workbench scope
  
  "preferences": {
    "mechanisms": {
      "email": {
        "enabled": true,
        "priority": 1,
        "address": "user@example.com"
      },
      "sms": {
        "enabled": false
      },
      "push": {
        "enabled": true,
        "priority": 2
      },
      "webhook": {
        "enabled": false
      }
    },
    "time_windows": {
      "email": "always",
      "push": "09:00-18:00"
    },
    "event_filters": {
      "min_priority": "normal"
    }
  }
}
```

**Preference Resolution:**
- Notification Service first checks for workbench-scoped preferences
- If not found, falls back to tenant-scoped preferences
- Workbench preferences take precedence when both exist

### Mechanism Overlap Logic

**Default: Intersection**
- Only mechanisms that are both:
  - Supported in Scenario specification
  - Enabled in user preferences
- Are used for notification delivery

**Example:**
- Scenario supports: `[email, sms, push]`
- User preferences: `[email, sms]` (push disabled)
- Result: `[email, sms]` (intersection)

**Multiple Mechanisms:**
- When multiple mechanisms are selected, they are sent **in parallel** (not sequentially)
- Each mechanism is independent — failure of one does not affect others

**Multiple Recipients:**
- Each recipient receives notifications **individually** (not batched)
- Each recipient's preferences are applied independently

> **Note:** The overlap logic details can evolve. Default is intersection.

### Event Filters

User preference event filters (e.g., `min_priority`) are applied **after** scenario filtering:
- Scenario specification determines which events need notifications
- User preference filters can further restrict which notifications the user receives
- User filters can override scenario requirements (user opt-out capability)

---

## Persona-Specific Handlers

The Notification Service uses persona-specific handlers to process notifications for different user types. Persona type is determined from user role/profile information available in Cipher.

### Agent Notification Handler

Handles notifications for agents (human and AI agents):
- Task assignments
- Task updates
- Escalations
- Work reminders

### Business User Notification Handler

Handles notifications for business users (customers, external users):
- Request status updates
- Milestones
- Completion notifications
- Action required notifications

### Supervisor Notification Handler

Handles notifications for supervisors:
- Escalations
- High-priority requests
- Team performance updates
- Exception reports

### Tenant Admin Notification Handler

Handles notifications for tenant administrators:
- System alerts
- Configuration changes
- Resource usage alerts
- Compliance notifications

> **Note:** A user may have multiple personas (e.g., agent and supervisor). In such cases, the Notification Service determines the appropriate handler based on the context of the notification and user's roles.

---

## Cipher Notification Service Integration

The Notification Service dispatches notifications to **Cipher Notification Service (CNS)**, which:
- Routes to appropriate service providers (Email provider, SMS provider, Push provider, Webhook endpoint)
- Handles delivery, retries, and failures
- Provides delivery assurances through multiple providers and retry mechanisms
- Sends callbacks for delivery status, read receipts, and CTA responses

### Notification Request to CNS

```json
{
  "notification_request": {
    "id": "notif-req-12345",
    "recipient": {
      "user_id": "user-12345",
      "mechanism": "email",
      "address": "user@example.com"
    },
    "content": {
      "subject": "Dispute DSP-2026-12345 - Status Update",
      "body": "Your dispute has been updated...",
      "template_id": "dispute-status-email-v1"
    },
    "callback_url": "https://hub/notification-services/dispute-ops/callbacks",  // Resolved from request.workbench_id
    "correlation": {
      "request_id": "req-12345",
      "workbench_id": "dispute-ops",
      "scenario_id": "dispute-filing"
    },
    "cta": {
      "enabled": true,
      "actions": [
        {
          "id": "view-details",
          "label": "View Details",
          "url": "https://hub/requests/req-12345"
        },
        {
          "id": "approve",
          "label": "Approve",
          "url": "https://hub/requests/req-12345/approve?cta=approve&corr={{correlation_tracker}}"
        }
      ]
    }
  }
}
```

---

## Callbacks and Reverse Notifications

Cipher Notification Service sends callbacks to the originating Notification Service via registered callback URLs. **Callback URLs are registered by Notification Service with CNS per workbench.**

### Callback URL Registration

Notification Service registers callback URLs with Cipher Notification Service:
- **Scope:** Per workbench
- **Format:** `https://hub/notification-services/{workbench_id}/callbacks`
- **Resolution:** The `{workbench_id}` placeholder is resolved from `request.workbench_id` when sending notification requests to CNS
- **Registration:** Done during Notification Service initialization or workbench configuration

### Callback Types

#### 1. Delivery Status

```json
{
  "callback_type": "delivery_status",
  "notification_request_id": "notif-req-12345",
  "status": "delivered",              // delivered | failed | bounced
  "timestamp": "2026-01-05T10:30:00Z",
  "correlation": {
    "request_id": "req-12345",
    "correlation_tracker": "ct-abc123"
  }
}
```

#### 2. Read Receipt

Read receipts are supported for mechanisms that provide read tracking (typically Email and Push notifications). SMS and Webhook mechanisms may not support read receipts.

```json
{
  "callback_type": "read_receipt",
  "notification_request_id": "notif-req-12345",
  "read_at": "2026-01-05T10:35:00Z",
  "mechanism": "email",  // Mechanism that generated the read receipt
  "correlation": {
    "request_id": "req-12345",
    "correlation_tracker": "ct-abc123"
  }
}
```

#### 3. CTA Response

```json
{
  "callback_type": "cta_response",
  "notification_request_id": "notif-req-12345",
  "cta_action_id": "approve",
  "user_id": "user-12345",
  "timestamp": "2026-01-05T10:40:00Z",
  "correlation": {
    "request_id": "req-12345",
    "correlation_tracker": "ct-abc123"
  }
}
```

### CTA Handling

When a user clicks a CTA in a notification:

1. **CTA creates a new signal** — Notification Service acts as a Signal Provider (registered with Signal Exchange)
2. **Correlation context** — The notification request sent to CNS includes requisite context from the Request Update (request_id, workbench_id, scenario_id, etc.)
3. **Correlation tracker** — CNS generates appropriate correlation tracker in CTA URL string and reflects it back in the callback
4. **Signal creation** — Notification Service creates a signal with:
   - Correlation to original request (using correlation tracker from CNS callback)
   - CTA action information
   - User context
5. **Signal routing** — Signal is sent to Signal Exchange in normalized format, which routes to appropriate Scenario
6. **Request update** — The signal updates the existing request (correlated via correlation tracker)

### Delivery Failure Handling

**Cipher Notification Service Responsibility:**
- Handles delivery failures and retries
- Uses multiple providers to deliver notifications
- Retries as configured to meet delivery assurances

**Notification Service Responsibility:**
- Receives final failure notification after all retry attempts
- Creates a **signal** and sends it to Signal Exchange
- Signal Exchange has a **preconfigured built-in trigger** that translates the callback signal to a MEMO
- MEMO is created against the request scope
- No further action taken by Hub/Signal Exchange

**Flow:**
```
Delivery Failure Callback → Notification Service
  └─> Creates signal (Notification Service as Signal Provider)
  └─> Sends to Signal Exchange
  └─> Preconfigured trigger matches signal
  └─> Trigger translates to MEMO update
  └─> MEMO created against request scope
```

**Example MEMO (result of trigger translation):**
```json
{
  "update_type": "MEMO",
  "payload": {
    "memo": {
      "scope": "request",
      "scope_id": "req-12345",
      "content": {
        "title": "Notification Delivery Failed",
        "body": "Failed to deliver email notification to user@example.com after all retry attempts"
      }
    }
  }
}
```

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Scenario Notification Specification](./scenario-notification-spec.md) | Notification specification format in scenarios | 🔴 Stub |
| [User Preferences](./user-preferences.md) | User preference storage and management | 🔴 Stub |
| [Persona Services](./persona-services.md) | Agent, Business User, Supervisor, Tenant Admin services | 🔴 Stub |
| [Cipher Notification Service Integration](./cipher-integration.md) | Integration with CNS, callbacks, CTA handling | 🔴 Stub |

---

## Related Documentation

- [Signal Exchange](../signal-exchange/README.md) — Observer notifications
- [Observer Notifications](../signal-exchange/observer-notifications.md) — Observer module registration
- [Message Envelope](../signal-exchange/message-envelope.md) — Request Update formats
- [Scenario Definitions](../workbench-management/scenario-definitions.md) — Scenario specification format
- [Cipher IAM](../supporting-systems/cipher-iam.md) — Authentication and authorization

---

*TODO: Detailed design — template rendering, preference overlap algorithms, callback processing, CTA signal generation*

