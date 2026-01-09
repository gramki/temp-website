# Tenant Customers

> **Status:** 🔴 Stub — Placeholder for expansion

Tenant Customers are end-users of the tenant's services who may interact with Hub through self-serve capabilities and task participation.

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Scope** | Scenario-specific, per self-serve policy |
| **Domain** | Customer Domain (tenant's customers) |
| **Personas** | Self-Serve User |
| **Access** | Defined by scenario self-serve policy |

---

## Self-Serve Users

### Definition

**Self-Serve Users** are users in the tenant's customer domain who can:
1. Initiate requests by themselves (when enabled by policy)
2. Be assigned tasks as subjects of requests (when policy allows)

### Enabling Self-Serve

Self-serve is enabled per **Workbench** and **Scenario** through a **Self-Serve Policy**:

```yaml
scenario:
  id: "dispute-filing"
  workbench_id: "dispute-ops"
  
  self_serve_policy:
    enabled: true
    
    # Who can self-serve
    eligible_users:
      type: "customer_group"
      group_id: "retail-customers"
      
    # What they can do
    capabilities:
      initiate_request: true
      view_request_status: true
      upload_documents: true
      add_comments: true
      
    # Subject task assignment
    subject_task_assignment:
      enabled: true
      task_types:
        - "document_upload"
        - "information_request"
        - "verification"
      
    # Channels
    channels:
      - "mobile_app"
      - "web_portal"
      - "chat"
```

---

## Request Types and Subject Assignment

Self-serve and subject task assignment depends on request type:

| Request Type | Self-Serve Initiation | Subject Task Assignment |
|--------------|----------------------|------------------------|
| **Service Request** | ✅ If policy allows | ✅ If subject is explicit |
| **Business Request** | ✅ If policy allows | ✅ If subject is explicit |
| **System Request** | ❌ No subject | ❌ Not applicable |

### Subject Task Assignment

When a request has an **explicit Subject** (e.g., a customer), tasks can be assigned to that subject:

```
Request: Dispute Filing
Subject: Customer John Doe

Task: "Upload supporting documents"
  → Assigned to: John Doe (the Subject)
  → Channel: Mobile App push notification
  → Deadline: 7 days
```

---

## Self-Serve Capabilities

| Capability | Description |
|------------|-------------|
| **Initiate Request** | Start a new request for a scenario |
| **View Status** | See progress of their requests |
| **Upload Documents** | Attach files to requests |
| **Add Comments** | Provide additional information |
| **Complete Tasks** | Complete tasks assigned to them as subject |
| **View History** | See their past requests |

---

## Self-Serve Policy Configuration

```yaml
self_serve_policy:
  enabled: boolean
  
  # Eligibility
  eligible_users:
    type: enum           # customer_group | customer_segment | all_customers
    group_id: string     # If type is customer_group
    segment_criteria:    # If type is customer_segment
      - field: string
        operator: string
        value: any
  
  # Capabilities granted
  capabilities:
    initiate_request: boolean
    view_request_status: boolean
    upload_documents: boolean
    add_comments: boolean
    cancel_request: boolean
  
  # Subject task assignment
  subject_task_assignment:
    enabled: boolean
    task_types: array    # Which task types can be assigned
    notification_channels: array
    default_deadline: duration
    reminder_policy:
      - at: duration
        channel: string
  
  # Limits
  limits:
    max_open_requests: number
    rate_limit: string   # e.g., "5/day"
  
  # Channels
  channels:
    - channel_type: string
      config: object
```

---

## Customer Identity

Customer users are authenticated through:

| Method | Description |
|--------|-------------|
| **Tenant Identity Provider** | Tenant's own customer identity system |
| **Federated** | OIDC/SAML federation with Cipher |
| **Direct** | Cipher-managed customer accounts |

---

## Interaction Channels

Self-serve users interact through **Neutrino** channels:

| Channel | Use Case |
|---------|----------|
| **Mobile App** | Native mobile experience |
| **Web Portal** | Browser-based self-service |
| **Chat** | Conversational interface |
| **Email** | Notifications and updates |
| **SMS** | Alerts and task reminders |

---

## Example: Dispute Self-Serve Flow

```
1. Customer (Self-Serve User) logs into Mobile App
2. Customer initiates "File Dispute" request
3. Hub creates Request with Customer as Subject
4. Request processed by Seer Case Orchestration Agent
5. Agent creates Task "Upload supporting documents"
6. Task assigned to Customer (Subject)
7. Customer receives push notification
8. Customer uploads documents via Mobile App
9. Task marked complete
10. Processing continues
11. Customer can view status throughout
```

---

## Related Documentation

- [User Management Overview](./README.md)
- [Workbench Users](./workbench-users.md)
- [Request Management](../request-management/README.md)
- [Task Management](../task-management/README.md)
- [User Interaction Channels](../../06-ux-architecture/user-interaction-channels.md)

---

*TODO: Detailed design — customer identity integration, channel configuration, notification policies*

