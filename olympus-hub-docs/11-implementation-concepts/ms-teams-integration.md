# MS Teams Integration

> **Category:** Integration

---

## Overview

**MS Teams Integration** enables Hub capabilities within Microsoft Teams through persona-specific bots and chat group collaboration. The integration provides Me_Bot for personal tasks, Ask_Bot for Hub queries, and Group Orchestration Bot for team collaboration on requests.

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Channel** as an interaction interface. MS Teams Integration implements Hub access through the Teams platform.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Channel | MS Teams | Teams as Hub channel |
| Agent | Teams user | Users interact via Teams |

### Gap This Fills

The ontology focuses on abstract channels. MS Teams Integration addresses:
1. **Bot types**: What bots serve which purposes?
2. **Group collaboration**: How do teams work together?
3. **Deep linking**: How to navigate from Teams to Hub?

---

## Definition

**MS Teams Integration** is a channel implementation that:
- Provides persona-specific bots within Teams
- Enables chat group-based collaboration on requests
- Links Teams interactions to Hub operations
- Uses Hercules Launcher for deep linking

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-level; enabled per workbench |
| **Lifecycle** | Configured by Developer; used by agents |
| **Ownership** | Platform provides; workbench configures |
| **Multiplicity** | Three bot types per workbench |

---

## Structure

### Bot Types

| Bot | Purpose | Users |
|-----|---------|-------|
| **Me_Bot** | Personal task and notification management | Individual agents |
| **Ask_Bot** | Query Hub for information | All users |
| **Group Orchestration Bot** | Team collaboration on requests | Request participants |

### WorkbenchMSTeams CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchMSTeams
metadata:
  name: dispute-ops-teams
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-prod
  
  # Bot configuration
  bots:
    me_bot:
      enabled: true
      features:
        - task_notifications
        - task_actions
        - request_updates
        
    ask_bot:
      enabled: true
      features:
        - request_status
        - task_search
        - knowledge_query
        
    group_orchestration:
      enabled: true
      features:
        - request_chat_groups
        - participant_mentions
        - document_sharing
        
  # Deep linking
  launcher:
    hercules_base_url: "https://hub.acme.com"
    
  # Teams tenant
  teams_tenant:
    tenant_id: "acme-teams-tenant"
    app_registration_ref: hub-teams-app
```

### Bot Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MS TEAMS INTEGRATION                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   MICROSOFT TEAMS                     HUB                                   │
│                                                                              │
│   ┌───────────────┐                  ┌───────────────────────────────────┐ │
│   │ Agent's Chat  │                  │                                   │ │
│   │               │                  │  MS Teams Channel Adapter         │ │
│   │ ┌───────────┐ │                  │                                   │ │
│   │ │  Me_Bot   │◀├─────────────────▶│  ├── Agent Access Service        │ │
│   │ └───────────┘ │                  │  │                               │ │
│   │               │                  │  ├── Task Operations             │ │
│   │ "Show tasks"  │                  │  │                               │ │
│   │               │                  │  └── Notification Delivery       │ │
│   └───────────────┘                  │                                   │ │
│                                      │                                   │ │
│   ┌───────────────┐                  │                                   │ │
│   │ Request Group │                  │                                   │ │
│   │               │                  │                                   │ │
│   │ ┌───────────┐ │                  │  Group Orchestration Service     │ │
│   │ │Group Bot  │◀├─────────────────▶│                                   │ │
│   │ └───────────┘ │                  │  ├── Group Creation              │ │
│   │               │                  │  ├── Participant Management      │ │
│   │ @alice update │                  │  └── Request Updates             │ │
│   │               │                  │                                   │ │
│   └───────────────┘                  └───────────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Behavior

### Me_Bot Interactions

```
Agent interactions with Me_Bot:

"Show my tasks"
└── Returns task list with action buttons

"Complete task TASK-001"
└── Marks task complete

Notifications:
├── New task assigned → Push to personal chat
├── Task escalated → Notify of escalation
└── Request update → Inform of changes
```

### Group Orchestration

```
Request-based chat groups:

1. Request involves multiple participants
2. Group Orchestration creates Teams group
3. Participants added:
   ├── Agents working on request
   ├── Subject (customer, if applicable)
   └── Supervisor (if escalated)
4. Bot facilitates:
   ├── Status updates posted
   ├── Mentions route to right person
   └── Documents shared via Hub links
```

### Ask_Bot Queries

```
Information queries:

"What's the status of request REQ-001?"
└── Returns request status and recent updates

"How many disputes are pending?"
└── Returns queue statistics

"Find SOP for fraud investigation"
└── Queries Knowledge Bank, returns results
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Agent Access Service | → calls | Task operations |
| Notification Services | ← receives | Push to Teams |
| Hercules Launcher | → uses | Deep links |
| Signal Exchange | (via services) | Request operations |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Teams tenant required** | Must have Azure AD |
| **App registration** | Hub Teams app registered |
| **User mapping** | Hub users mapped to Teams |
| **Feature opt-in** | Features explicitly enabled |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Meet users where they are** | Teams is familiar |
| ✅ **Collaboration** | Group chat for requests |
| ✅ **Mobile access** | Teams mobile app |
| ✅ **Notifications** | Push to Teams |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Teams dependency** | Optional integration |
| ⚠️ **Limited UI** | Deep link to full Hub UI |

---

## Examples

### Example 1: Agent Task Flow

```
1. Task assigned to agent-alice

2. Me_Bot notification:
   "New task: Investigate dispute REQ-001
   Amount: $500
   SLA: 72 hours
   [View] [Start Work]"

3. Alice clicks "Start Work"
   └── Task marked IN_PROGRESS

4. Alice completes investigation via Teams
   └── "Complete task REQ-001-TASK-001 refund approved"

5. Task completed, request updated
```

### Example 2: Group Collaboration

```
Request REQ-001 escalated to supervisor

Group created:
├── agent-alice (original assignee)
├── agent-bob (senior, escalation level 1)
└── supervisor-carol (supervisor)

Bot posts:
"Request REQ-001 escalated to level 1.
@alice and @bob are now assigned.
[View Request]"
```

---

## Implementation Notes

### For Developers

- Configure appropriate bot features per workbench
- Test Teams flows thoroughly
- Ensure deep links work correctly

### For Operators

- Manage Teams app registration
- Monitor bot health
- Handle Teams tenant changes

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Channel](./channel.md) | Teams is a channel |
| [Hercules Launcher](./hercules-launcher.md) | Deep linking |
| [Notification Services](./notification-services.md) | Push to Teams |

---

## References

- [MS Teams Integration Subsystem](../04-subsystems/ms-teams-integration/README.md)
- [Developer Operators](../04-subsystems/operators/developer-operators.md)

