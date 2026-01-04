# UX Architecture & User Interfacing Applications

This section covers the user experience architecture for Olympus Hub, including the applications and components that enable human interaction with Operations.

## Overview

Hub serves multiple user personas through different interfacing applications:

| Persona | Application | Purpose |
|---------|-------------|---------|
| **Business Operations** | Ops Center | Manage operations, cases, tasks, exceptions |
| **Subject/Customer** | Neutrino Channels | Self-service and assisted interactions |
| **Tenant Executives** | Product Center, Report Center | Configuration, analytics, reporting |
| **Workbench Designers** | Workbench Studio | Define workbenches, triggers, scenarios |
| **Developers** | IDE + Development Tools | Build Hub Applications and Triggers |

## Key Components

### Angelos — UI Component Framework

Angelos provides reusable UI components for building operational interfaces:
- Task forms and wizards
- Case/Request detail views
- Notification templates
- Action buttons and CTAs

### Hercules Launcher

Hercules is a launch URL service that enables deep-linking into Hub applications:

```
┌─────────────────────────────────────────────────────────────────┐
│                    HERCULES LAUNCHER                             │
│                                                                  │
│  Input:                                                          │
│  • Sandbox                                                       │
│  • Angelos Component                                             │
│  • Invocation Parameters                                         │
│  • Authorization Context (optional)                              │
│    - Subject JID                                                 │
│    - Invocation-specific-use Token                               │
│                                                                  │
│  Output:                                                         │
│  • Launch URL for CTA buttons, notifications, etc.               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Launch URL Capabilities:**
- Bearer URL (like Google Docs "anyone with link") for pre-authenticated access
- Bound to specific Subject for authorized operations
- Scoped to Web Stack Subscription of tenant
- Works for both Consumer (Neutrino) and Tenant Executive (Ops Center) use cases

### Neutrino Channels

Neutrino provides customer-facing interaction channels:
- Web portals
- Mobile apps
- IVR systems
- Chat interfaces

Integration with Hub enables:
- Service Request initiation (self-service and assisted)
- Task completion by Subjects (customers)
- Notification delivery
- Case status tracking

## User Interaction Patterns

### Subject Participation in Operations

For Service Requests, the Subject (customer) may participate in the Operation:

| Interaction | Description | Delivery |
|-------------|-------------|----------|
| **Notification** | Inform subject of status, updates | Push, Email, SMS |
| **Task** | Action required from subject | Hercules Launch URL |
| **CTA** | Optional actions available | Hercules Launch URL |

### Case/Request Specification

Each Case or Request specification can include:
- **Notification Templates** — Pre-defined messages for status updates
- **Hercules Launch URL RSD** — Declarative mechanism to create Launch URLs for Tasks and CTAs

## Documents

| Document | Description | Status |
|----------|-------------|--------|
| [User Interaction Channels](./user-interaction-channels.md) | Subject interaction patterns | ⚠️ Notes |
| [Hercules Launcher](./hercules-launcher.md) | Launch URL service design | 📝 Planned |
| [Angelos Components](./angelos-components.md) | UI component framework | 📝 Planned |
| [Ops Center UX](./ops-center-ux.md) | Operations console design | 📝 Planned |
| [Neutrino Integration](./neutrino-integration.md) | Customer channel integration | 📝 Planned |

## Related Documentation

- [Hub Architecture](../02-system-design/hub-architecture.md) — System context
- [Request Types](../01-concepts/ontology-reference.md#request) — Service/Business/System requests and subject participation
- [Task Management](../02-system-design/hub-architecture.md#111-task-management) — Task lifecycle

---

*Status: 🟡 WIP - Structure defined, content in progress*

