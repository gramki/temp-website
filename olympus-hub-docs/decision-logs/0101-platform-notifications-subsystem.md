# ADR-0101: Platform Notifications Subsystem

## Status

Accepted

## Date

2026-01-11

## Context

Hub has two distinct categories of notifications:

1. **Business domain notifications** — Triggered by Request Updates (task assignments, status changes, milestones)
2. **Platform-to-tenant notifications** — Triggered by platform events (Marketplace updates, subscription changes, maintenance)

The existing Notification Services subsystem handles business domain notifications as an observer of Signal Exchange, translating Request Updates into persona-specific notifications.

### Question

Should Marketplace and other platform notifications be added to Notification Services, or should a separate subsystem handle them?

### Constraints

- Notification Services is tightly coupled to Signal Exchange and Request Updates
- Platform notifications have different sources (Marketplace, Subscription Management, Platform Operations)
- Platform notifications have different recipients (tenant admins, publishers, subscribers)
- Platform notifications don't follow the Request Update → persona flow

## Decision

**Create a separate Platform Notifications subsystem** for platform-to-tenant notifications. Notification Services remains focused on business domain notifications via Signal Exchange.

### Subsystem Separation

| Subsystem | Source | Scope | Recipients |
|-----------|--------|-------|------------|
| **Notification Services** | Signal Exchange (Request Updates) | Workbench/Scenario | Agents, business users, supervisors |
| **Platform Notifications** | Platform services | Platform/Tenant | Tenant admins, publishers, subscribers |

### Platform Notification Types

**Marketplace Notifications:**
- Publisher registration approval/rejection
- Package publishing approval/rejection
- Package subscription approval/rejection
- New package version availability
- Security vulnerability alerts
- Blacklisting notifications
- Out-of-sync Blueprint resource alerts
- Withdrawn Blueprint notifications

**Subscription Notifications:**
- Subscription renewal reminders
- Usage alerts / quota warnings
- Platform maintenance announcements
- Feature announcements
- Platform policy updates

## Alternatives Considered

### Alternative: Extend Notification Services

Add platform notification handling to existing Notification Services.

**Pros:**
- Single notification subsystem
- Shared delivery infrastructure

**Cons:**
- Conflates two different notification models
- Signal Exchange dependency not needed for platform notifications
- Different recipient resolution logic
- Different template management
- Overloaded subsystem

**Why rejected:** Different sources, scopes, and recipient models warrant separation. Clean architecture over forced consolidation.

## Consequences

### Positive

- Clear separation of concerns
- Each subsystem focused on its domain
- Independent evolution
- Simpler mental model
- No Signal Exchange dependency for platform notifications

### Negative

- Two notification subsystems to maintain
- Potential for some infrastructure duplication

### Neutral

- Both use Cipher Notification Service (CNS) for delivery
- Shared delivery mechanisms, different notification sources

## Implementation Notes

- Platform Notifications subscribes to events from:
  - Marketplace Services
  - Subscription Management
  - Platform Operations
- Uses CNS for actual delivery (same as Notification Services)
- Separate template management for platform notifications
- Tenant admin notification preferences may be shared

## References

- [Platform Notifications Subsystem](../04-subsystems/platform-notifications/README.md)
- [Notification Services](../04-subsystems/notification-services/README.md)
- [Marketplace Subsystem](../04-subsystems/marketplace/README.md)

