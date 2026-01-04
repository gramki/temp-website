# Persona: Self-Serve User (Tenant Customer)

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **Self-Serve User** is a customer of the tenant who can initiate requests and interact with Hub-managed operations. They are external to the tenant's organization but have defined access through Self-Serve Policies.

| Attribute | Value |
|-----------|-------|
| **Scope** | Workbench (via Self-Serve Policy) |
| **Domain** | Tenant Customer Domain |
| **Primary Channel** | Neutrino Channels, Customer Portal |

---

## Objectives

| Objective | Description |
|-----------|-------------|
| **Initiate Requests** | Start service or business requests |
| **Track Status** | Monitor request progress |
| **Provide Input** | Respond to tasks assigned to Subject |
| **Receive Updates** | Get notifications on request changes |

---

## Access Model

Self-serve access is controlled by **Self-Serve Policies** on Scenarios:

```yaml
self_serve_policy:
  enabled: true
  allowed_user_groups:
    - "premium-customers"
    - "verified-users"
  
  # Can initiate requests
  can_initiate: true
  
  # Can receive tasks (as Subject of Request)
  can_receive_tasks: true
  
  # Channels available
  channels:
    - "customer-portal"
    - "mobile-app"
    - "chat"
```

---

## Key Activities

### Request Initiation

1. **Submit Request**
   - Through available channels (portal, mobile, chat)
   - Provide required information
   - Receive request confirmation

2. **Track Progress**
   - View request status
   - Receive notifications
   - Access history

### Task Completion (as Subject)

When tasks are routed to the Subject of a Request:

1. **Receive Task**
   - Notification via configured channel
   - Access task details

2. **Provide Response**
   - Submit required information
   - Acknowledge or confirm
   - Upload documents

---

## Channels

| Channel | Interface |
|---------|-----------|
| **Customer Portal** | Web application |
| **Mobile App** | Native mobile experience |
| **Chat** | Conversational interface |
| **Email** | Notification and simple responses |

---

## Related Documentation

- [Neutrino Channels](../../06-ux-architecture/user-interaction-channels.md)
- [Self-Serve Policies](../../04-subsystems/workbench-management/scenario-definitions.md)

---

*TODO: Detailed channel experiences, access patterns, notification flows*

