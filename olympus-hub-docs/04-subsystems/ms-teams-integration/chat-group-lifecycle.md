# Chat Group Lifecycle

> **Status:** 🟡 WIP

This document details how MS Teams chat groups are created, managed, and archived for Hub Requests.

---

## Design Rationale

### Chat Groups as Collaboration Surfaces

Traditional task management captures **what** was done, not **how** teams collaborated:

| Traditional Approach | Chat Group Approach |
|---------------------|---------------------|
| Task assignments logged | Full collaboration captured |
| Status updates recorded | Context and reasoning preserved |
| Handoffs are implicit | Handoffs are explicit conversations |
| Knowledge silos | Shared understanding |

### Bot as Orchestrator

When multiple participants need to coordinate:

| Aspect | Implementation |
|--------|----------------|
| **Group creation** | Group Orchestration Bot creates group on request creation |
| **Membership management** | Bot adds members via Graph API as tasks are assigned |
| **System updates** | Bot posts status changes, assignments, milestones |
| **Archival** | Bot triggers archive on schedule after completion |

---

## Lifecycle States

```
┌─────────────────────────────────────────────────────────────────┐
│                    CHAT GROUP LIFECYCLE                          │
│                                                                  │
│   REQUEST CREATED                                                │
│         │                                                        │
│         ▼                                                        │
│   ┌─────────────────┐                                           │
│   │ GROUP CREATED   │ ◄─── Group Orchestration Bot creates group│
│   │ (Initial        │      with initial members                  │
│   │  Members)       │                                           │
│   └────────┬────────┘                                           │
│            │                                                     │
│            ▼                                                     │
│   ┌─────────────────┐                                           │
│   │ ACTIVE          │ ◄─── Members collaborate, tasks assigned  │
│   │ (Dynamic        │      New assignees added automatically    │
│   │  Membership)    │                                           │
│   └────────┬────────┘                                           │
│            │                                                     │
│            ▼                                                     │
│   ┌─────────────────┐                                           │
│   │ COMPLETED       │ ◄─── Request reaches terminal state       │
│   │ (No new tasks,  │      Group remains accessible             │
│   │  collaboration  │                                           │
│   │  continues)     │                                           │
│   └────────┬────────┘                                           │
│            │                                                     │
│            ▼ (after configured period)                          │
│   ┌─────────────────┐                                           │
│   │ ARCHIVED        │ ◄─── Group archived, history preserved    │
│   │ (Read-only)     │      in Hub Request record                │
│   └─────────────────┘                                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Group Creation

### Trigger

A chat group is created when:
1. A **Request is created** for a scenario with Teams integration enabled
2. The scenario's `chat_group.enabled` is `true`

### Initial Membership

| Member Type | When Added | Condition |
|-------------|------------|-----------|
| **Group Orchestration Bot** | Immediately | Always — orchestrator presence |
| **Scenario Default Participants** | Immediately | As configured in scenario manifest |
| **Request Subject** | Immediately | If `auto_add_subject: true` |
| **Request Originator** | Immediately | If employee-originated |
| **Supervisor** | Immediately | If `auto_add_supervisor: true` |

### Group Naming

```
Format: {scenario-short-name} - {request-id}
Example: "Dispute Resolution - DSP-2024-0042"
```

### Initial Message

```
┌─────────────────────────────────────────────────────────────────┐
│ [Dispute Ops Hub] — Today at 2:34 PM                            │
│                                                                  │
│ 📋 Request Created                                               │
│                                                                  │
│ Request: DSP-2024-0042                                          │
│ Scenario: Dispute Resolution                                     │
│ Subject: John Smith (john.smith@customer.com)                   │
│ Priority: High                                                   │
│                                                                  │
│ Initial participants have been added. You'll be notified        │
│ as the request progresses.                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Dynamic Membership

### Adding Members on Task Assignment

When a Hub Application creates and assigns a task:

```
┌─────────────────────────────────────────────────────────────────┐
│                      TASK ASSIGNMENT FLOW                        │
│                                                                  │
│   Hub Application                                                │
│         │                                                        │
│         │ Creates task, assigns to Agent Bob                     │
│         ▼                                                        │
│   Signal Exchange                                                │
│         │                                                        │
│         │ Dispatches TASK_LIFECYCLE update                       │
│         ▼                                                        │
│   MS Teams Module                                                │
│         │                                                        │
│         │ 1. Add Bob to chat group via Graph API                 │
│         │ 2. Post assignment notification                        │
│         ▼                                                        │
│   Chat Group                                                     │
│         │                                                        │
│         │ [Dispute Ops Hub]: Task "Review Transaction"           │
│         │                    assigned to @Bob                    │
│         │                                                        │
└─────────────────────────────────────────────────────────────────┘
```

### Member Removal Policy

| Scenario | Action |
|----------|--------|
| Task completed | Member **NOT** removed |
| Task reassigned | New assignee added, original stays |
| Request completed | All members stay until archive |
| Member leaves voluntarily | Allowed, can rejoin if needed |
| Member mutes group | Allowed |

**Rationale:** Agents may need to reference past context or be re-engaged. Automatic removal would lose collaboration continuity.

---

## Message Capture

### All Messages Become Request Updates

Every message in the chat group is captured as an update to the Request:

```
┌─────────────────────────────────────────────────────────────────┐
│                    MESSAGE → UPDATE FLOW                         │
│                                                                  │
│   Agent Alice types in chat group                                │
│         │                                                        │
│         ▼                                                        │
│   MS Teams (message sent)                                        │
│         │                                                        │
│         ▼                                                        │
│   MS Teams Module                                                │
│         │                                                        │
│         │ Receives message via bot subscription                  │
│         ▼                                                        │
│   Signal Exchange                                                │
│         │                                                        │
│         │ Records as ASYNC_UPDATE (type: MEMO or THOUGHT)        │
│         ▼                                                        │
│   Request Record                                                 │
│         │                                                        │
│         │ Message preserved with:                                │
│         │ - Author                                               │
│         │ - Timestamp                                            │
│         │ - Content                                              │
│         │ - Channel: MS_TEAMS                                    │
│         │                                                        │
└─────────────────────────────────────────────────────────────────┘
```

### Update Classification

| Message Type | Update Classification |
|--------------|----------------------|
| Agent explaining reasoning | `THOUGHT` |
| Status/progress mention | `PROGRESS` |
| Reference note for future | `MEMO` |
| Decision announcement | `DECISION` (if via Me_Bot command) |
| General discussion | `MEMO` |

---

## System Updates

### What the Group Orchestration Bot Posts

| Event | Message Format |
|-------|---------------|
| **Request created** | Initial summary with participants |
| **Task assigned** | "@{agent} has been assigned: {task_name}" |
| **Task completed** | "Task '{task_name}' completed by @{agent}" |
| **Task escalated** | "⚠️ Task '{task_name}' escalated by @{agent}" |
| **Status change** | "Request status: {old} → {new}" |
| **Milestone reached** | "✅ Milestone: {milestone_name}" |
| **Request completed** | "🎉 Request completed: {outcome}" |

---

## Cross-Channel Update Relay

When an agent makes an update to a Request through a **different channel** (e.g., Agent Desk, Mobile), the MS Teams module relays that update to the chat group. The message attribution depends on credential sharing:

### Message Attribution Logic

| Condition | Message Appears As |
|-----------|-------------------|
| Agent has shared Teams credentials with module | Posted **as the agent** (their identity) |
| Agent has NOT shared credentials | Posted **by Group Orchestration Bot**, with on-behalf-of attribution in body |

### With Credential Sharing (Agent Identity)

```
┌─────────────────────────────────────────────────────────────────┐
│ [Alice] — 3:15 PM                                               │
│ I've reviewed the documentation and approved the claim.         │
│ (Updated via Agent Desk)                                        │
└─────────────────────────────────────────────────────────────────┘
```

The message is posted using Alice's Teams identity, appearing as if she typed it directly.

### Without Credential Sharing (Bot Proxy)

```
┌─────────────────────────────────────────────────────────────────┐
│ [Dispute Ops Hub] — 3:15 PM                                     │
│ 📝 Update from @Alice (via Agent Desk):                         │
│                                                                  │
│ "I've reviewed the documentation and approved the claim."       │
└─────────────────────────────────────────────────────────────────┘
```

The Group Orchestration Bot posts on behalf of Alice, clearly indicating the origin.

### Credential Sharing

Agents can choose to share their Teams credentials with the MS Teams module to enable seamless cross-channel identity:

| Aspect | Details |
|--------|---------|
| **Opt-in** | Credential sharing is voluntary per agent |
| **Scope** | Per workbench (agent may share for some workbenches, not others) |
| **Storage** | Credentials stored securely in Cipher IAM |
| **Revocation** | Agent can revoke at any time |

### Why This Matters

- **Conversation continuity** — Team members see consistent authorship
- **Accountability** — Clear attribution regardless of source channel
- **Flexibility** — Agents can work from any channel without context loss

### Example Timeline

```
┌─────────────────────────────────────────────────────────────────┐
│ Dispute Resolution - DSP-2024-0042                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ [Dispute Ops Hub] — 2:34 PM                                     │
│ 📋 Request Created                                               │
│ Subject: John Smith | Priority: High                            │
│                                                                  │
│ [Dispute Ops Hub] — 2:34 PM                                     │
│ Task "Initial Review" assigned to @Alice                        │
│                                                                  │
│ [Alice] — 2:41 PM                                               │
│ Looking at this now. Transaction seems suspicious based on      │
│ location data.                                                  │
│                                                                  │
│ [Alice] — 2:52 PM                                               │
│ Confirmed fraud pattern. Escalating for compliance review.      │
│                                                                  │
│ [Dispute Ops Hub] — 2:52 PM                                     │
│ ⚠️ Task "Initial Review" escalated by @Alice                    │
│ Task "Compliance Review" assigned to @Bob                       │
│                                                                  │
│ [Bob] — 3:15 PM                                                 │
│ Thanks Alice. I'll need to check against recent fraud alerts.  │
│                                                                  │
│ [Dispute Ops Hub] — 4:02 PM                                     │
│ ✅ Task "Compliance Review" completed by @Bob                   │
│ Decision: Confirmed fraud, card blocked                         │
│                                                                  │
│ [Dispute Ops Hub] — 4:02 PM                                     │
│ 🎉 Request completed: Resolved - Fraud Confirmed                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Completion and Archival

### Request Completion

When a Request reaches a terminal state (Completed, Cancelled):

1. Group Orchestration Bot posts completion message
2. Group remains **active and accessible**
3. Participants can still collaborate (late notes, follow-ups)
4. No new tasks will be assigned

### Archival Schedule

```yaml
chat_groups:
  archive_after_days: 90  # Days after request completion
```

| State | Behavior |
|-------|----------|
| **Before archive** | Full read/write access |
| **After archive** | Read-only in Teams, full history in Hub |

### Archive Process

1. **Archive trigger** — Scheduled job runs after configured period
2. **Group update** — Bot posts "This group is now archived"
3. **Teams action** — Group converted to read-only
4. **Hub preservation** — All messages already in Request record

---

## Observer Notifications

### Signal Exchange Dispatch Model

**Important:** Signal Exchange dispatches Request Updates to **registered observers** (like the MS Teams module), NOT to individual agents or tasks. Signal Exchange operates at the Request level and cannot direct updates to specific tasks or agents.

| Component | Responsibility |
|-----------|----------------|
| **Signal Exchange** | Dispatches Request Updates to registered observers |
| **MS Teams Module** | As an observer, receives updates and determines which agents to notify |
| **Hub Application** | Originates updates (task assignments, decisions, etc.) |

### How MS Teams Module Determines Agent Notifications

The MS Teams module, as an observer of Request Updates:
1. Receives Request Update from Signal Exchange
2. Parses the update content (e.g., TASK_LIFECYCLE with assignee info)
3. Determines which agents are affected
4. Takes appropriate action (add to group, post message, etc.)

### Notification Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                  REQUEST UPDATE FLOW                             │
│                                                                  │
│   Hub Application                                                │
│         │                                                        │
│         │ Request Update (contains task/agent info)              │
│         ▼                                                        │
│   Signal Exchange                                                │
│         │                                                        │
│         │ Dispatch to registered observers                       │
│         │ (Request-level, not agent/task-level)                  │
│         │                                                        │
│         ├─────────────────────┬──────────────────────────────   │
│         │                     │                                  │
│         ▼                     ▼                                  │
│   MS Teams Module         Other Observers                        │
│         │                 (WebSocket, Webhook,                   │
│         │                  Email, Push)                          │
│         │                                                        │
│         │ Parse update, determine affected agents                │
│         ▼                                                        │
│   Chat Group Actions                                             │
│   (Add members, post messages)                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Note:** Agents in the Teams chat group may receive the same update through multiple channels. This is by design — channels are not mutually exclusive.

---

## Configuration Reference

### Workbench Level

```yaml
ms_teams_integration:
  chat_groups:
    enabled: true
    auto_add_subject: true        # Add subject to group
    auto_add_supervisor: false    # Add supervisor automatically
    archive_after_days: 90        # Days after completion
    
    default_participants:
      - role: "quality-analyst"   # Always add this role
```

### Scenario Level Override

```yaml
scenario:
  name: "VIP Customer Dispute"
  
  ms_teams:
    chat_group:
      auto_add_supervisor: true   # Override: always add supervisor
      default_participants:
        - role: "vip-relationship-manager"
        - role: "compliance-officer"
```

---

## Related Documentation

- [Bot Architecture](./bot-architecture.md) — Bot types and capabilities
- [Message Flow](./message-flow.md) — Signal routing paths
- [Signal Exchange](../signal-exchange/README.md) — Update dispatching

---

*Last updated: 2026-01-05*

