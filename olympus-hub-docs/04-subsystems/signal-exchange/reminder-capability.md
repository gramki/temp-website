# Reminder Capability

> **Status:** 🟡 Draft — Under active development

The Reminder Capability in Signal Exchange provides a built-in scheduling mechanism for Hub Applications to receive time-based notifications, enabling applications to handle parked work and time-sensitive follow-ups without maintaining their own scheduling infrastructure.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Provide time-based stimuli for applications to continue parked work |
| **Scope** | Request-scoped (not task or agent-specific) |
| **Scheduling** | Once or recurring (cron-based) |
| **Delivery** | REMINDER_NOTIFICATION messages to Hub Applications |
| **Lifecycle** | Auto-cancelled when Request reaches terminal state |

---

## Purpose and Motivation

The reminder feature helps **agents and applications receive stimuli to continue parked work** when there is no input from external systems or agents they may be waiting on.

### Problem Statement

Many business processes involve waiting for external events:
- User actions (document uploads, approvals, responses)
- External system responses (API callbacks, file arrivals)
- Agent actions (reviews, decisions, escalations)

When these events don't occur within expected timeframes, applications need mechanisms to:
1. **Detect stalled work** — Identify when waiting periods have elapsed
2. **Trigger alternative paths** — Take different actions when primary paths stall
3. **Escalate or follow up** — Remind stakeholders or take corrective action

### Solution: Signal Exchange Reminders

Signal Exchange provides a **built-in reminder capability** that:
- Eliminates the need for applications to maintain scheduling infrastructure
- Provides reliable, Request-scoped reminder delivery
- Automatically handles lifecycle (cancellation on Request completion)
- Integrates seamlessly with existing Request Update mechanisms

---

## Use Cases

### 1. User Action Timeout

**Scenario:** Application is waiting for user to upload documents. If no upload occurs within 48 hours, application should send a reminder email and consider alternative processing.

**Solution:**
```yaml
# Application schedules reminder after 48 hours
update_type: REMIND
payload:
  reminder:
    reminder_schedule_id: "rem-doc-upload-48h"
    kind: "document_upload_timeout"  # Semantic type for reminder interpretation
    schedule:
      type: once
      when: "2026-01-12T10:00:00Z"  # 48 hours from now
    reminder_payload:
      data:
        action: "check_document_upload"
        timeout_hours: 48
        alternative_path: "escalate_to_manager"
```

**When reminder fires:**
- Application receives REMINDER_NOTIFICATION
- Application checks if documents were uploaded
- If not, application takes alternative path (escalate, send reminder email, etc.)

### 2. Recurring Follow-up

**Scenario:** Case requires daily check-ins. Application should be reminded every morning at 9 AM to review case status.

**Solution:**
```yaml
update_type: REMIND
payload:
  reminder:
    reminder_schedule_id: "rem-daily-checkin"
    kind: "daily_case_review"  # Semantic type for reminder interpretation
    schedule:
      type: recurring
      cron_expression: "0 9 * * 1-5"  # 9 AM Mon-Fri
    reminder_payload:
      data:
        action: "daily_case_review"
        case_id: "case-12345"
```

**When reminder fires:**
- Application receives REMINDER_NOTIFICATION every weekday morning
- Application performs daily case review
- Application can schedule next reminder or cancel if case is resolved

### 3. Escalation Trigger

**Scenario:** High-priority request requires resolution within 4 hours. If not resolved, escalate to supervisor.

**Solution:**
```yaml
update_type: REMIND
payload:
  reminder:
    reminder_schedule_id: "rem-escalation-4h"
    kind: "high_priority_escalation"  # Semantic type for reminder interpretation
    schedule:
      type: once
      when: "2026-01-05T14:00:00Z"  # 4 hours from now
    reminder_payload:
      data:
        action: "check_resolution_status"
        escalation_threshold_hours: 4
        escalate_to: "supervisor-queue"
        priority: "high"
```

**When reminder fires:**
- Application checks if request is resolved
- If not resolved, application escalates to supervisor
- Application may schedule additional reminders for further escalation

### 4. External System Timeout

**Scenario:** Application called external credit check API. If no response within 30 minutes, retry or use cached result.

**Solution:**
```yaml
update_type: REMIND
payload:
  reminder:
    reminder_schedule_id: "rem-credit-check-timeout"
    kind: "external_api_timeout"  # Semantic type for reminder interpretation
    schedule:
      type: once
      when: "2026-01-05T11:30:00Z"  # 30 minutes from now
    reminder_payload:
      data:
        action: "check_credit_response"
        api_call_id: "api-call-12345"
        fallback_action: "use_cached_result"
```

**When reminder fires:**
- Application checks if credit check response arrived
- If not, application uses cached result or retries
- Application continues processing

### 5. Agent Work Reminder

**Scenario:** Agent is waiting for customer response. If no response in 24 hours, agent should follow up via phone.

**Solution:**
```yaml
update_type: REMIND
payload:
  reminder:
    reminder_schedule_id: "rem-customer-followup"
    kind: "agent_customer_followup"  # Semantic type for reminder interpretation
    schedule:
      type: once
      when: "2026-01-06T10:00:00Z"  # 24 hours from now
    reminder_payload:
      data:
        action: "customer_followup"
        agent_id: "agent-12345"
        task_id: "task-67890"
        followup_method: "phone"
        customer_id: "cust-99999"
```

**When reminder fires:**
- Application receives reminder with agent and task context
- Application can create follow-up task or notify agent
- Agent receives notification to follow up with customer

---

## How Reminders Simplify Hub Application Design

### Without Reminders (Traditional Approach)

Applications must:
1. **Maintain scheduling infrastructure**
   - Deploy and manage scheduler services (Quartz, Celery, etc.)
   - Handle scheduler scaling and reliability
   - Manage scheduler state and persistence

2. **Handle lifecycle management**
   - Track which reminders are active
   - Cancel reminders when Request completes
   - Handle scheduler failures and recovery

3. **Coordinate across instances**
   - Ensure reminders fire only once in distributed deployments
   - Handle instance failures without losing reminders
   - Coordinate reminder state across application instances

4. **Integrate with Request lifecycle**
   - Manually cancel reminders on Request completion
   - Handle edge cases (Request cancelled while reminder pending)
   - Maintain reminder-to-Request mapping

### With Signal Exchange Reminders

Applications simply:
1. **Send REMIND update** — Schedule reminder with simple update message
2. **Receive REMINDER_NOTIFICATION** — Handle reminder when it fires
3. **Cancel if needed** — Send CANCEL_REMINDER update (optional)

**Benefits:**
- ✅ **No scheduling infrastructure** — Signal Exchange handles all scheduling
- ✅ **Automatic lifecycle** — Reminders auto-cancelled on Request completion
- ✅ **Reliable delivery** — Signal Exchange ensures reminder delivery
- ✅ **Request-scoped** — Reminders automatically tied to Request lifecycle
- ✅ **Simplified code** — Applications focus on business logic, not scheduling

### Example: Simplified Application Code

**Before (with custom scheduler):**
```python
# Application must:
# 1. Set up scheduler connection
# 2. Schedule reminder job
# 3. Store reminder ID for cancellation
# 4. Handle scheduler failures
# 5. Cancel reminder on Request completion
# 6. Handle distributed coordination

scheduler = connect_to_scheduler()
reminder_id = scheduler.schedule(
    when=datetime.now() + timedelta(hours=48),
    callback=check_document_upload,
    request_id=request_id
)
store_reminder_id(request_id, reminder_id)

# Later, on Request completion:
scheduler.cancel(reminder_id)
```

**After (with Signal Exchange reminders):**
```python
# Application simply sends update:
send_request_update(
    request_id=request_id,
    update_type="REMIND",
    payload={
        "reminder": {
            "reminder_schedule_id": "rem-doc-upload-48h",
            "kind": "document_upload_timeout",  # Semantic type for interpretation
            "schedule": {
                "type": "once",
                "when": (datetime.now() + timedelta(hours=48)).isoformat()
            },
            "reminder_payload": {
                "data": {"action": "check_document_upload"}
            }
        }
    }
)

# Signal Exchange handles:
# - Scheduling
# - Delivery
# - Lifecycle (auto-cancels on Request completion)
# - Reliability
```

---

## Dos and Don'ts

### ✅ Dos

1. **Use reminders for time-based stimuli**
   - Waiting for external events with timeouts
   - Recurring check-ins or reviews
   - Escalation triggers
   - Follow-up actions

2. **Include context in reminder payload**
   - Action to take when reminder fires
   - Relevant IDs (task_id, agent_id, etc.)
   - Business context needed for decision-making

3. **Cancel reminders when no longer needed**
   - If alternative path is taken before reminder fires
   - If condition that triggered reminder is resolved
   - Use CANCEL_REMINDER update

4. **Handle reminder notifications idempotently**
   - Reminders may be delivered multiple times (at-least-once semantics)
   - Check if action was already taken
   - Use sequence numbers to track recurring reminders

5. **Use reminder_schedule_id for tracking**
   - Store reminder_schedule_id if you need to cancel later
   - Use it to correlate reminder notifications with original requests

### ❌ Don'ts

1. **Don't use reminders for real-time coordination**
   - Reminders are for time-based stimuli, not event coordination
   - Use signals or direct updates for real-time communication

2. **Don't rely on exact timing**
   - Reminders are delivered "as close to but not before" scheduled time
   - May be slightly delayed due to system load
   - Don't use for time-critical operations requiring exact timing

3. **Don't use reminders for high-frequency polling**
   - Use event-driven mechanisms for frequent checks
   - Reminders are for longer intervals (minutes to days)

4. **Don't store large payloads in reminder_payload**
   - Keep reminder payloads lightweight
   - Include references (IDs) rather than full data
   - Original request payload is included automatically

5. **Don't create reminders for completed/cancelled Requests**
   - Signal Exchange will suppress these, but it's wasteful
   - Check Request status before scheduling reminders

6. **Don't use reminders as a state store**
   - Reminders are notifications, not data storage
   - Store business state in Request payload or external storage

7. **Don't create reminders with very short intervals**
   - For intervals less than a few minutes, use polling or event-driven mechanisms
   - Reminders are optimized for longer intervals

---

## Reminder Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│                    REMINDER LIFECYCLE                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Application sends REMIND update                         │
│     └─> Signal Exchange schedules reminder                  │
│                                                              │
│  2. Reminder scheduled (once or recurring)                  │
│     └─> Signal Exchange tracks reminder schedule            │
│                                                              │
│  3. Scheduled time arrives                                  │
│     ├─> If Request is ACTIVE/PENDING:                       │
│     │     └─> Send REMINDER_NOTIFICATION to Application     │
│     └─> If Request is COMPLETED/CANCELLED:                   │
│           └─> Suppress alarm (no notification sent)         │
│                                                              │
│  4. For recurring reminders:                                │
│     └─> Repeat step 3 per cron schedule                     │
│                                                              │
│  5. Reminder cancellation:                                  │
│     ├─> Explicit: Application sends CANCEL_REMINDER        │
│     ├─> Automatic: Request reaches COMPLETED/CANCELLED      │
│     └─> Signal Exchange sends REMINDER_CANCELLED update    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Integration Patterns

### Pattern 1: Timeout with Alternative Path

```yaml
# Application schedules reminder for timeout
REMIND → {
  schedule: { type: "once", when: "..." },
  reminder_payload: {
    data: {
      action: "check_timeout",
      alternative_path: "escalate"
    }
  }
}

# When reminder fires:
REMINDER_NOTIFICATION → Application checks condition
  ├─> If condition met: Take alternative path
  └─> If condition not met: Cancel reminder or reschedule
```

### Pattern 2: Recurring Health Check

```yaml
# Application schedules recurring reminder
REMIND → {
  kind: "recurring_health_check",
  schedule: { type: "recurring", cron_expression: "0 */6 * * *" },  # Every 6 hours
  reminder_payload: {
    data: {
      action: "health_check",
      check_items: ["status", "progress", "blockers"]
    }
  }
}

# Application handles each reminder:
REMINDER_NOTIFICATION → Application performs health check
  ├─> If healthy: Continue, reminder auto-repeats
  └─> If unhealthy: Take corrective action, may cancel reminder
```

### Pattern 3: Escalation Chain

```yaml
# Application schedules escalation reminders
REMIND → {
  reminder_schedule_id: "rem-escalate-1h",
  kind: "escalation_level_1",
  schedule: { type: "once", when: "+1 hour" },
  reminder_payload: { data: { escalation_level: 1 } }
}

# When first reminder fires:
REMINDER_NOTIFICATION → Application escalates to Level 1
  └─> Application schedules next escalation:
      REMIND → {
        reminder_schedule_id: "rem-escalate-2h",
        kind: "escalation_level_2",
        schedule: { type: "once", when: "+1 hour" },
        reminder_payload: { data: { escalation_level: 2 } }
      }
```

---

## Best Practices

### 1. Naming Conventions

Use descriptive `reminder_schedule_id` values:
- ✅ `rem-doc-upload-48h`
- ✅ `rem-escalation-level-1`
- ✅ `rem-daily-review-case-12345`
- ❌ `rem-1`
- ❌ `reminder`

### 2. Payload Design

Keep reminder payloads focused and actionable:
```json
{
  "action": "check_document_upload",        // Clear action
  "timeout_hours": 48,                      // Context
  "alternative_path": "escalate",          // What to do
  "task_id": "task-12345"                   // Relevant IDs
}
```

### 4. Error Handling

Handle reminder notifications robustly:
```python
def handle_reminder_notification(reminder):
    try:
        # Check if action still needed
        if not is_action_needed(reminder):
            return  # Action already taken
        
        # Perform action
        perform_action(reminder.reminder_payload.data)
        
    except Exception as e:
        # Log error, may reschedule or escalate
        log_error(reminder, e)
        # Optionally schedule retry reminder
```

### 5. Cancellation Strategy

Cancel reminders when no longer needed:
- When alternative path is taken
- When condition is resolved
- When Request is manually completed/cancelled (automatic)

---

## Related Documentation

- [Message Envelope](./message-envelope.md) — REMIND and REMINDER_NOTIFICATION message formats
- [Signal Exchange Overview](./README.md) — Signal Exchange capabilities
- [Request Management](../request-management/README.md) — Request lifecycle

---

*TODO: Detailed design — reminder storage, cron expression validation, timezone handling, reminder deduplication*

