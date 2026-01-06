# ADR-0026: Signal Exchange Built-in Reminder Capability

## Status

**Accepted**

## Date

2026-01-06

## Context

Many Hub Application workflows involve waiting for external events:
- User actions (document uploads, approvals, responses)
- External system responses (API callbacks, file arrivals)
- Agent actions (reviews, decisions)

When these events don't occur within expected timeframes, applications need mechanisms to:
1. Detect stalled work
2. Trigger alternative paths
3. Escalate or follow up

### Traditional Approach Problems

Applications traditionally must:
1. **Maintain scheduling infrastructure** (Quartz, Celery, etc.)
2. **Handle lifecycle management** (cancel reminders on Request completion)
3. **Coordinate across instances** (ensure reminders fire only once)
4. **Integrate with Request lifecycle** (manual cancellation on completion)

This adds significant complexity to every application needing time-based triggers.

## Decision

**Signal Exchange provides a built-in reminder capability** that applications can use via standard Request Updates:

1. **REMIND Update**: Applications schedule reminders by sending a REMIND update to Signal Exchange

2. **REMINDER_NOTIFICATION Message**: Signal Exchange sends notification to application when scheduled time arrives

3. **Request-Scoped Lifecycle**: Reminders are automatically cancelled when Request reaches terminal state (COMPLETED, CANCELLED)

4. **Once or Recurring**: Support for one-time reminders or cron-based recurring schedules

### Message Flow

```
Application                    Signal Exchange
    │                                │
    │ ── REMIND ───────────────────> │
    │    (schedule reminder)         │
    │                                │
    │    ... time passes ...         │
    │                                │
    │ <── REMINDER_NOTIFICATION ──── │
    │    (reminder fires)            │
    │                                │
```

### REMIND Payload

```json
{
  "update_type": "REMIND",
  "payload": {
    "reminder": {
      "reminder_schedule_id": "rem-doc-upload-48h",
      "kind": "document_upload_timeout",
      "schedule": {
        "type": "once",
        "when": "2026-01-08T10:00:00Z"
      },
      "reminder_payload": {
        "data": {
          "action": "check_document_upload",
          "alternative_path": "escalate"
        }
      }
    }
  }
}
```

### Automatic Lifecycle

| Request Status | Reminder Behavior |
|----------------|-------------------|
| ACTIVE, PENDING | Reminder fires as scheduled |
| COMPLETED, CANCELLED | Reminder suppressed (not sent) |
| Request cancelled after reminder scheduled | All pending reminders auto-cancelled |

## Alternatives Considered

### Alternative 1: Applications Manage Own Schedulers
Each application deploys and manages its own scheduling infrastructure.

- **Pros**: Full control, no dependency on SX
- **Cons**: Duplicated infrastructure, lifecycle management burden, distributed coordination complexity

### Alternative 2: External Scheduler Service
Hub provides a separate Scheduler Service that applications call.

- **Pros**: Centralized scheduling, reusable
- **Cons**: Separate integration, not Request-aware, manual lifecycle management

### Alternative 3: Workflow Runtime Timers
Use workflow runtime (Rhea, ChronoShift) built-in timers.

- **Pros**: Integrated with workflow state
- **Cons**: Only available for workflow runtimes, not universal across application types

## Consequences

### Positive
- **No Scheduling Infrastructure**: Applications don't deploy/manage schedulers
- **Automatic Lifecycle**: Reminders auto-cancelled on Request completion
- **Reliable Delivery**: Signal Exchange ensures reminder delivery
- **Request-Scoped**: Reminders automatically tied to Request lifecycle
- **Universal**: Available to all Hub Applications, regardless of runtime

### Negative
- **SX Dependency**: Applications depend on SX for time-based triggers
- **Approximate Timing**: Reminders delivered "as close to but not before" scheduled time
- **Request-Level Only**: Cannot attribute reminders to specific tasks or agents

### Neutral
- Applications must include `kind` attribute for semantic typing
- Original request payload included in reminder notification
- At-least-once delivery semantics (applications handle idempotently)

## Use Cases

| Use Case | Reminder Type | Example |
|----------|---------------|---------|
| **User Action Timeout** | Once | Wait 48h for document upload |
| **Recurring Check-in** | Recurring | Daily case review at 9 AM |
| **Escalation Trigger** | Once | Escalate if not resolved in 4 hours |
| **External API Timeout** | Once | Retry if no response in 30 minutes |
| **Agent Work Reminder** | Once | Remind agent to follow up |

## Simplified Application Code

**Before (custom scheduler):**
```python
scheduler = connect_to_scheduler()
reminder_id = scheduler.schedule(
    when=datetime.now() + timedelta(hours=48),
    callback=check_document_upload,
    request_id=request_id
)
store_reminder_id(request_id, reminder_id)

# On Request completion:
scheduler.cancel(reminder_id)
```

**After (SX reminders):**
```python
send_request_update(
    request_id=request_id,
    update_type="REMIND",
    payload={
        "reminder": {
            "reminder_schedule_id": "rem-doc-upload-48h",
            "kind": "document_upload_timeout",
            "schedule": {"type": "once", "when": deadline.isoformat()},
            "reminder_payload": {"data": {"action": "check_document_upload"}}
        }
    }
)
# Signal Exchange handles scheduling, lifecycle, and delivery
```

## Related Decisions

- [ADR-0004: Reminder Kind Attribute](./0004-reminder-kind-attribute.md)
- [ADR-0003: Signal Exchange Responsibility Boundaries](./0003-signal-exchange-responsibility-boundaries.md)
- [ADR-0020: Request-Level Granularity](./0020-request-level-granularity.md)

