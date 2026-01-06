# Persona

> **Category:** UX Architecture

---

## Overview

A **Persona** is a distinct user archetype with specific responsibilities, goals, and interaction patterns within Hub. Unlike generic "user roles," Hub Personas represent coherent job functions that span across multiple systems and tools. Each Persona has dedicated UX surfaces, API channels, and notification preferences designed for their specific needs.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Role** as a functional responsibility played by an Agent in a Scenario, and **Agent** as the executor of work. However, these are scenario-scoped concepts. Persona is the broader, platform-level user archetype.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Role | Scenario Role | Role within a specific Scenario |
| Agent | User + Persona | User acting in a Persona capacity |
| (not covered) | Persona | Platform-level user archetype |

### Gap This Fills

The ontology focuses on scenario-level roles. Persona addresses:
1. **Cross-scenario identity**: Same user operates across multiple Scenarios
2. **UX design**: Each Persona gets tailored interfaces
3. **API organization**: APIs are organized by Persona
4. **Notification targeting**: Notifications are Persona-aware

---

## Definition

**Persona** is a platform-level user archetype characterized by:
- Distinct responsibilities and goals
- Dedicated UX applications (desks, consoles)
- Persona-scoped API channels (MCP, REST)
- Specific notification preferences and templates
- Appropriate access control policies

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Platform-wide; spans all Scenarios and Workbenches |
| **Lifecycle** | Defined by platform; user is assigned to Personas |
| **Ownership** | Platform defines Personas; Admin assigns users |
| **Multiplicity** | One user can have multiple Personas |

---

## Rationale

### Why This Design?

Hub follows a **Persona-Channel-UseCase** meta approach:
1. **Persona-first**: Design UX for who is using, not what they're doing
2. **Channel-aware**: Same Persona, different channels (web, Teams, API)
3. **Use-case specific**: Each Persona has distinct use cases

This enables:
- Coherent, role-appropriate interfaces
- API organization by consumer type
- Targeted notifications and workflows

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Role-based only** | Too granular; fragmented UX |
| **Single unified UI** | Overloaded; inappropriate for regulated environments |
| **Function-based APIs** | Confusing; mixing concerns |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0008](../../decision-logs/0008-persona-channel-usecase-meta-approach.md) | Persona-Channel-UseCase meta approach |
| [ADR-0011](../../decision-logs/0011-persona-scoped-api-channels.md) | MCP and REST APIs organized by Persona |

---

## Structure

### Hub Personas

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HUB PERSONAS                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PUBLISHER DOMAIN                    TENANT DOMAIN                          │
│   ────────────────                    ─────────────                          │
│                                                                              │
│   ┌────────────────┐                 ┌────────────────┐                     │
│   │      SRE       │                 │  Administrator │                     │
│   │ Hub operations │                 │ Tenant config  │                     │
│   └────────────────┘                 └────────────────┘                     │
│                                                                              │
│   ┌────────────────┐                 ┌────────────────┐                     │
│   │ Customer       │                 │    Auditor     │                     │
│   │ Success        │                 │  Compliance    │                     │
│   └────────────────┘                 └────────────────┘                     │
│                                                                              │
│                                      ┌────────────────┐                     │
│                                      │    Process     │                     │
│                                      │   Architect    │                     │
│                                      └────────────────┘                     │
│                                                                              │
│                                      ┌────────────────┐                     │
│                                      │   Developer    │                     │
│                                      └────────────────┘                     │
│                                                                              │
│                                      ┌────────────────┐                     │
│                                      │   Supervisor   │                     │
│                                      └────────────────┘                     │
│                                                                              │
│                                      ┌────────────────┐                     │
│                                      │     Agent      │                     │
│                                      └────────────────┘                     │
│                                                                              │
│   BUSINESS DOMAIN (via Workbench)                                           │
│   ───────────────────────────────                                           │
│                                                                              │
│   ┌────────────────┐  ┌────────────────┐  ┌────────────────┐               │
│   │   Business     │  │   Business     │  │   Business     │               │
│   │   Customer     │  │   Employee     │  │   System       │               │
│   └────────────────┘  └────────────────┘  └────────────────┘               │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Persona Definitions

| Persona | Domain | Responsibilities |
|---------|--------|------------------|
| **SRE** | Publisher | Hub infrastructure, deployments, monitoring |
| **Customer Success** | Publisher | Tenant onboarding, support, success metrics |
| **Administrator** | Tenant | Subscription config, users, resources |
| **Auditor** | Tenant | Compliance review, audit trails, reports |
| **Process Architect** | Tenant | Workbench design, Scenarios, SOPs |
| **Developer** | Tenant | Hub Applications, integrations, testing |
| **Supervisor** | Workbench | Queue management, escalations, team oversight |
| **Agent** | Workbench | Task execution, customer interaction |
| **Business Customer** | Business | Self-service requests, status tracking |
| **Business Employee** | Business | Internal requests, collaboration |
| **Business System** | Business | Automated requests, integrations |

---

## Behavior

### Persona-Channel Matrix

| Persona | Web Console | MS Teams | MCP | REST API |
|---------|-------------|----------|-----|----------|
| **SRE** | SRE Ops Center | - | ✓ | ✓ |
| **Administrator** | Hub Control Center | - | ✓ | ✓ |
| **Process Architect** | Workbench Studio | - | ✓ | ✓ |
| **Developer** | Workbench Studio | - | ✓ | ✓ |
| **Supervisor** | Supervisor Desk | Me_Bot | ✓ | ✓ |
| **Agent** | Agent Desk | Me_Bot | ✓ | ✓ |
| **Business User** | Neutrino | Ask_Bot | - | ✓ |

### Persona Assignment

```
1. User created in Cipher IAM
2. User assigned to Tenant
3. User granted Persona-level permissions
4. User can access Persona-appropriate:
   ├── UX applications
   ├── API channels
   └── Notification streams
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Channel | → accesses | Persona determines available channels |
| Notification Services | → receives | Notifications targeted by Persona |
| Access Control | → governed by | Permissions scoped to Persona |
| API Channels | → authenticated as | APIs organized by Persona |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Single primary** | User has one primary Persona for UX context |
| **Multi-Persona possible** | User can hold multiple Personas (e.g., Agent + Supervisor) |
| **Persona determines access** | API/UX access based on Persona assignment |
| **Notification targeting** | Notifications routed to appropriate Persona channel |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Coherent UX** | Each Persona gets tailored interface |
| ✅ **Clear API organization** | APIs grouped by consumer |
| ✅ **Targeted notifications** | Right message to right person |
| ✅ **Appropriate access** | Permissions match responsibilities |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Multiple consoles** | Consistent design language across consoles |
| ⚠️ **Role confusion** | Clear Persona definitions and boundaries |

---

## Examples

### Example 1: Agent Persona

```yaml
persona:
  type: agent
  
  ux_applications:
    - name: Agent Desk
      purpose: Task execution, customer interaction
    - name: Hub Home
      purpose: Personal dashboard
      
  channels:
    - type: web
      application: agent-desk
    - type: ms_teams
      bot: me_bot
    - type: mcp
      scope: agent
    - type: rest
      base_path: /api/v1/agent
      
  notifications:
    - task_assigned
    - task_escalated
    - request_updated
    - mention_in_chat
    
  permissions:
    - view_assigned_tasks
    - complete_tasks
    - add_memos
    - access_knowledge_bank
    - view_request_history
```

### Example 2: Multi-Persona User

```yaml
user:
  id: "user-alice"
  email: "alice@acme.com"
  
  personas:
    primary: supervisor
    additional:
      - agent  # Can also work as agent when needed
      
  access:
    - supervisor_desk
    - agent_desk  # Via agent persona
    - supervisor_apis
    - agent_apis
```

---

## Implementation Notes

### For Developers

- Design APIs with specific Persona in mind
- Use Persona context for authorization decisions
- Notifications should be Persona-appropriate in tone and detail

### For Operators

- Assign Personas based on job function, not individual tasks
- Monitor Persona distribution for capacity planning
- Review multi-Persona assignments for appropriateness

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Channel](./channel.md) | Personas access Hub through Channels |
| [Notification Services](./notification-services.md) | Notifications targeted by Persona |
| [Headless Access Service](./headless-access-service.md) | Backend services adapt to Persona |

---

## References

- [UX Architecture](../../06-ux-architecture/README.md)
- [User Management](../../04-subsystems/user-management/README.md)
- [Personas and Journeys](../../08-personas-and-journeys/README.md)
- [ADR-0008: Persona-Channel-UseCase](../../decision-logs/0008-persona-channel-usecase-meta-approach.md)

