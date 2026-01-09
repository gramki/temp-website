# Neutrino Integration

> **Status:** 🔴 Stub — Placeholder for expansion

**Neutrino** is Olympus's customer-facing channel platform. Hub integrates with Neutrino to enable customer self-service and assisted interactions.

---

## Overview

Neutrino provides customer-facing channels:
- Web portals
- Mobile apps
- IVR systems
- Chat interfaces (web, WhatsApp, etc.)

Hub integration enables:
- Service Request initiation (self-serve)
- Task completion by Subjects (customers)
- Request status tracking
- Notification delivery

---

## Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                           CUSTOMER CHANNELS                                  │
│      ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐                    │
│      │   Web   │  │ Mobile  │  │   IVR   │  │  Chat   │                    │
│      │ Portal  │  │   App   │  │         │  │         │                    │
│      └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘                    │
│           │            │            │            │                          │
│           └────────────┴─────┬──────┴────────────┘                          │
│                              │                                               │
│                              ▼                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        NEUTRINO                                      │    │
│  │  • Session Management                                                │    │
│  │  • Channel Adapters                                                  │    │
│  │  • Customer Authentication                                           │    │
│  │  • Context Assembly                                                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                              │                                               │
│                              ▼                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     HUB INTEGRATION                                  │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │    │
│  │  │  Heracles   │  │   Request   │  │    Task     │                  │    │
│  │  │  (API)      │  │  Management │  │ Management  │                  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Capabilities

### Request Initiation

Customers can initiate Service Requests through Neutrino channels:

| Channel | Initiation Method |
|---------|-------------------|
| **Web Portal** | Forms, wizards, document upload |
| **Mobile App** | In-app forms, photo capture |
| **IVR** | Voice menu selections |
| **Chat** | Conversational intake |

### Request Tracking

Customers can track their Service Requests:

| Capability | Description |
|------------|-------------|
| **Status View** | Current request status |
| **Timeline** | History of updates |
| **ETA** | Expected resolution time |
| **Notifications** | Push, SMS, email updates |

### Subject Task Completion

Customers can complete tasks assigned to them as Subject:

| Task Type | Example |
|-----------|---------|
| **Document Upload** | Submit supporting documents |
| **Information Provision** | Answer questions, provide details |
| **Acknowledgment** | Confirm or accept information |
| **Decision** | Choose between options |

### Notifications

Hub can send notifications to customers via Neutrino:

| Notification Type | Channels |
|-------------------|----------|
| **Status Updates** | Push, SMS, Email |
| **Task Assignments** | Push, Email with Hercules link |
| **Reminders** | Push, SMS |
| **Completion** | Email, Push |

---

## Self-Serve Policy

Each Scenario can define a self-serve policy:

```yaml
self_serve_policy:
  enabled: true
  
  # Who can self-serve
  allowed_user_groups:
    - "verified-customers"
    - "premium-members"
  
  # Channels enabled
  channels:
    - "customer-portal"
    - "mobile-app"
    - "chat"
  
  # Capabilities
  can_initiate: true
  can_receive_tasks: true
  can_view_status: true
  can_cancel: true  # Within SLA window
```

---

## Integration Points

### Heracles Gateway

Neutrino communicates with Hub via Heracles:

| Endpoint | Purpose |
|----------|---------|
| `POST /requests` | Initiate Service Request |
| `GET /requests/{id}` | Get request status |
| `POST /tasks/{id}/complete` | Complete subject task |
| `GET /tasks/subject` | List tasks for subject |

### Hercules Launcher

Neutrino uses Hercules for deep links:

| Use Case | Link Type |
|----------|-----------|
| Task completion | Subject-bound URL |
| Status page | Authenticated URL |
| Document upload | Subject-bound URL |

### Notification Service

Hub sends notifications via Neutrino channels:

| Event | Notification |
|-------|--------------|
| Request created | Confirmation |
| Task assigned | Action required |
| Status change | Update |
| Request completed | Resolution |

---

## Related Documentation

- [Business Customer Persona](../08-personas-and-journeys/personas/business-domain/business-customer.md)
- [Request Lifecycle](../08-personas-and-journeys/journeys/request-lifecycle.md)
- [Heracles Gateway](../05-infrastructure/heracles-gateway.md)
- [Hercules Launcher](./hercules-launcher.md)

---

*TODO: Detailed API specifications, channel-specific UX patterns, notification templates*

