# ADR-0004: Semantic Typing for Reminder Requests via Kind Attribute

## Status

Accepted

## Date

2026-01-05

## Context

Hub Applications can schedule reminders with Signal Exchange to receive a `REMINDER_NOTIFICATION` at a specified time. This helps agents or applications continue parked work when waiting on external input.

When a reminder notification arrives, the receiving application needs to understand:
- What type of reminder this is
- What action should be taken
- How to interpret the reminder payload

Without a semantic type, applications would need to parse the payload to determine the reminder's purpose.

## Decision

**Add a `kind` attribute to reminder requests that allows the requesting application/agent to add a semantic/business-domain-informed type to the reminder.**

The `kind` attribute:
- Is set by the application when scheduling the reminder
- Is echoed back in the `REMINDER_NOTIFICATION`
- Provides semantic context for interpreting the reminder
- Is a free-form string defined by the application (e.g., `document_upload_timeout`, `approval_deadline`, `follow_up_call`)

Example:
```json
{
  "reminder": {
    "kind": "document_upload_timeout",
    "schedule": { "type": "once", "when": "2026-01-06T10:00:00Z" },
    "reminder_payload": { ... }
  }
}
```

## Consequences

### Positive
- **Easy interpretation**: Applications can switch on `kind` to handle different reminder types
- **Self-documenting**: The kind describes the reminder's purpose
- **Flexible**: Applications define their own kind vocabulary
- **Efficient processing**: No need to parse payload to determine action

### Negative
- **No enforced vocabulary**: Applications must manage their own kind values
- **Potential inconsistency**: Different applications may use different conventions

### Neutral
- Best practice is to use namespaced kinds (e.g., `com.acme.dispute.document_timeout`)

## Related

- [Message Envelope](../04-subsystems/signal-exchange/message-envelope.md)
- [Reminder Capability](../04-subsystems/signal-exchange/reminder-capability.md)

