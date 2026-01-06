# ADR-0022: Workbench-Scoped User Preferences with Tenant Fallback

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub users (agents, supervisors, business users) receive notifications across multiple workbenches. Users may have different notification preferences for different contexts:
- An agent may want SMS for urgent disputes but email-only for routine inquiries
- A supervisor may want push notifications for their primary workbench but digest emails for secondary workbenches

The question is how to scope user notification preferences:
- Global (single preference set per user)
- Tenant-scoped (one preference set per tenant subscription)
- Workbench-scoped (separate preferences per workbench)

## Decision

User notification preferences are **scoped to workbenches with tenant-level fallback**:

1. **Workbench-Scoped Preferences** (highest priority)
   - User can set preferences per workbench
   - Applied when user receives notifications for that workbench

2. **Tenant-Scoped Preferences** (fallback)
   - Default preferences for the tenant subscription
   - Applied when no workbench-specific preferences exist

3. **Resolution Order**
   - First, check for workbench-scoped preferences
   - If not found, use tenant-scoped preferences
   - Workbench preferences take full precedence (no merging)

### Preference Structure

**Workbench-Scoped:**
```json
{
  "user_id": "user-12345",
  "tenant_id": "acme-bank",
  "subscription_id": "sub-prod-001",
  "workbench_id": "dispute-ops",    // Workbench-specific
  "preferences": { ... }
}
```

**Tenant-Scoped (fallback):**
```json
{
  "user_id": "user-12345",
  "tenant_id": "acme-bank",
  "subscription_id": "sub-prod-001",
  "workbench_id": null,             // Tenant-level, no workbench
  "preferences": { ... }
}
```

### Preference Elements

- **Mechanisms**: Which notification channels (email, sms, push, webhook) with enabled/disabled and priority
- **Time Windows**: When to send via each mechanism (e.g., "sms": "09:00-18:00")
- **Event Filters**: Minimum priority level, specific event types to receive

## Alternatives Considered

### Alternative 1: Global User Preferences Only
Single preference set per user across all contexts.

- **Pros**: Simple, consistent experience
- **Cons**: No flexibility for different contexts, user may be overwhelmed or miss critical notifications

### Alternative 2: Tenant-Scoped Only (No Workbench Override)
Preferences at tenant level, same for all workbenches.

- **Pros**: Simpler than workbench-scoped
- **Cons**: Users in multiple workbenches can't differentiate

### Alternative 3: Merged Preferences (Workbench + Tenant)
Workbench preferences merge with tenant preferences.

- **Pros**: Inheritance of common settings
- **Cons**: Complex merge logic, unpredictable results, harder to debug

## Consequences

### Positive
- **Context-Specific**: Users can tune preferences per workbench
- **Sensible Defaults**: Tenant preferences provide baseline
- **Simple Resolution**: Clear precedence (workbench > tenant, no merging)
- **Multi-Workbench Support**: Users in multiple workbenches have appropriate preferences for each

### Negative
- **Management Overhead**: Users must set preferences per workbench if they want customization
- **Storage**: Separate preference records per workbench per user
- **UX Complexity**: Preference UI must support workbench selection

### Neutral
- Preferences stored by Notification Services in its own store
- Workbench preferences completely override tenant preferences (no partial merge)

## Storage Responsibility

Notification Services maintains its own preference store:
- Scoped by tenant_id, subscription_id, user_id, workbench_id
- Provides API for preference management
- Consulted during notification delivery

## Event Filter Application

User preference event filters are applied **after** scenario filtering:
1. Scenario specification determines which events generate notifications
2. User preference filters can further restrict which notifications user receives
3. Users can effectively opt out of certain notification types

## Related Decisions

- [ADR-0005: Notification Services Architecture](./0005-notification-services-architecture.md)
- [ADR-0019: Signal Exchange Observer Pattern](./0019-signal-exchange-observer-pattern.md)

