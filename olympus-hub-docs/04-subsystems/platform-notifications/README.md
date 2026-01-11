# Platform Notifications Subsystem

> **Status:** 🟡 WIP — Design Complete

The Platform Notifications subsystem handles **platform-to-tenant notifications** — notifications originating from platform services rather than business domain events.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Deliver platform-originated notifications to tenants |
| **Scope** | Platform-level (cross-tenant) |
| **Sources** | Marketplace, Subscription Management, Platform Operations |
| **Delivery** | Via Cipher Notification Service (CNS) |

---

## Distinction from Notification Services

| Aspect | Notification Services | Platform Notifications |
|--------|----------------------|------------------------|
| **Source** | Signal Exchange (Request Updates) | Platform Services |
| **Scope** | Workbench/Scenario | Platform/Tenant |
| **Triggers** | Business domain events | Platform events |
| **Recipients** | Agents, business users | Tenant admins, publishers, subscribers |

→ See [ADR-0101: Platform Notifications Subsystem](../../decision-logs/0101-platform-notifications-subsystem.md)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PLATFORM NOTIFICATIONS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PLATFORM SERVICES                                                         │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│   │   Marketplace   │  │  Subscription   │  │    Platform     │             │
│   │    Services     │  │   Management    │  │   Operations    │             │
│   └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
│            │                    │                    │                       │
│            └────────────────────┴────────────────────┘                       │
│                                 │                                            │
│                                 ▼                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                  PLATFORM NOTIFICATION SERVICE                       │   │
│   │                                                                      │   │
│   │  ┌─────────────────────────────────────────────────────────────┐    │   │
│   │  │  Event Handlers                                              │    │   │
│   │  │  • Marketplace Handler                                       │    │   │
│   │  │  • Subscription Handler                                      │    │   │
│   │  │  • Operations Handler                                        │    │   │
│   │  └─────────────────────────────────────────────────────────────┘    │   │
│   │                              │                                       │   │
│   │                              ▼                                       │   │
│   │  ┌─────────────────────────────────────────────────────────────┐    │   │
│   │  │  Notification Dispatch                                       │    │   │
│   │  │  • Resolve recipients                                        │    │   │
│   │  │  • Render templates                                          │    │   │
│   │  │  • Send to CNS                                               │    │   │
│   │  └─────────────────────────────────────────────────────────────┘    │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                 │                                            │
│                                 ▼                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                CIPHER NOTIFICATION SERVICE (CNS)                     │   │
│   │                                                                      │   │
│   │               Email  │  SMS  │  Push  │  Webhook                    │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Notification Categories

### Marketplace Notifications

| Event | Recipients | Description |
|-------|------------|-------------|
| Publisher Registration Approval | Tenant Admin | Registration approved/rejected |
| Package Publishing Status | Developer, Admin | Package published/rejected |
| Package Subscription Status | User, Admin | Subscription approved/rejected |
| New Version Available | Subscribers | New package version published |
| Security Vulnerability | Publisher, Subscribers | Issue detected |
| Blacklisting | Affected parties | Package blacklisted |
| Out-of-Sync Resources | Developer | Resources need update |
| Withdrawn Blueprint | Subscribers | Blueprint no longer supported |

→ See [Marketplace Notifications](./marketplace-notifications.md)

### Subscription Notifications

| Event | Recipients | Description |
|-------|------------|-------------|
| Renewal Reminder | Tenant Admin | Subscription expiring |
| Usage Alert | Tenant Admin | Approaching quota |
| Quota Exceeded | Tenant Admin | Quota limit reached |

→ See [Subscription Notifications](./subscription-notifications.md)

### Platform Operations Notifications

| Event | Recipients | Description |
|-------|------------|-------------|
| Maintenance Announcement | All Tenants | Scheduled maintenance |
| Feature Announcement | All Tenants | New features available |
| Policy Update | Tenant Admins | Platform policy changes |

---

## Components

| Component | Description | Documentation |
|-----------|-------------|---------------|
| Marketplace Notifications | Marketplace event notifications | [marketplace-notifications.md](./marketplace-notifications.md) |
| Subscription Notifications | Subscription lifecycle notifications | [subscription-notifications.md](./subscription-notifications.md) |

---

## Delivery

Platform Notifications uses **Cipher Notification Service (CNS)** for delivery:

- Same delivery infrastructure as Notification Services
- Supports Email, SMS, Push, Webhook
- Delivery assurance and retry mechanisms
- Callback handling for delivery status

---

## Recipient Resolution

| Recipient Type | Resolution |
|----------------|------------|
| **Tenant Admin** | From tenant subscription configuration |
| **Publisher** | From publisher registration |
| **Subscribers** | From package subscription records |
| **Developers** | From workbench access records |

---

## Related Documentation

- [Notification Services](../notification-services/README.md) — Business domain notifications
- [Marketplace Subsystem](../marketplace/README.md) — Source of Marketplace events
- [ADR-0101: Platform Notifications Subsystem](../../decision-logs/0101-platform-notifications-subsystem.md)

