# Channel

> **Category:** UX Architecture

---

## Overview

A **Channel** is an interaction interface through which users access Hub capabilities. Hub supports multiple channels — web applications, MS Teams, MCP (for AI assistants), and REST APIs — each optimized for its context. The same business capabilities are exposed consistently across channels, while presentation adapts to channel-specific patterns.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't explicitly address how users interact with the system across different interfaces. Channels are an implementation concept that enables multi-surface interaction.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Agent (Human) | User + Channel | Agents interact via Channels |
| Action | Channel-specific interaction | Actions taken through Channel interface |

### Gap This Fills

The ontology focuses on operations. Channels address:
1. **Multi-surface access**: Same user, different devices
2. **Context optimization**: Right interface for each context
3. **AI integration**: AI assistants as first-class channel
4. **API access**: Programmatic interaction

---

## Definition

**Channel** is an interaction interface characterized by:
- Specific transport and protocol (HTTP, WebSocket, Bot Framework)
- Persona-appropriate UX or API
- Consistent business capability exposure
- Channel-specific presentation patterns

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Platform-wide; all Personas use Channels |
| **Lifecycle** | Platform-provided; always available |
| **Ownership** | Platform owns Channels; Tenants configure |
| **Multiplicity** | Multiple Channels available per Persona |

---

## Rationale

### Why This Design?

Multi-channel architecture enables:
1. **Context-appropriate UX**: Desktop web vs mobile vs chat
2. **AI-first**: AI assistants can interact natively
3. **Integration flexibility**: REST APIs for automation
4. **User preference**: Choice of interaction style

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Single channel (web only)** | Limits accessibility; no AI integration |
| **Per-function APIs** | Confusing; inconsistent experience |
| **Channel per feature** | Fragmented; maintenance burden |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0008](../../decision-logs/0008-persona-channel-usecase-meta-approach.md) | Persona-Channel-UseCase meta approach |
| [ADR-0009](../../decision-logs/0009-headless-services-with-channel-adapters.md) | Headless services with channel adapters |
| [ADR-0010](../../decision-logs/0010-ai-assistants-first-class-channel.md) | AI assistants as first-class channel |

---

## Structure

### Hub Channels

| Channel | Transport | Personas | Use Cases |
|---------|-----------|----------|-----------|
| **Web Console** | HTTP/WebSocket | All | Full-featured desktop experience |
| **MS Teams** | Bot Framework | Agent, Supervisor, Business User | In-flow collaboration, quick actions |
| **MCP** | Model Context Protocol | Agent, Supervisor, Admin, Developer | AI assistant integration |
| **REST API** | HTTP | All (programmatic) | System integration, automation |

### Channel Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CHANNEL ARCHITECTURE                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   CHANNELS                          HEADLESS SERVICES                        │
│   ────────                          ─────────────────                        │
│                                                                              │
│   ┌───────────────┐                ┌───────────────────────────────────┐    │
│   │  Web Console  │                │                                   │    │
│   │  (Angelos)    │───────────────▶│                                   │    │
│   └───────────────┘                │    HEADLESS ACCESS SERVICES       │    │
│                                    │                                   │    │
│   ┌───────────────┐                │    ┌───────────────────────┐     │    │
│   │  MS Teams     │                │    │  Agent Access Service  │     │    │
│   │  (Me_Bot)     │───────────────▶│    └───────────────────────┘     │    │
│   └───────────────┘                │                                   │    │
│                                    │    ┌───────────────────────┐     │    │
│   ┌───────────────┐                │    │  Supervisor Access    │     │    │
│   │  MCP Channel  │                │    │  Service              │     │    │
│   │  (AI Agents)  │───────────────▶│    └───────────────────────┘     │    │
│   └───────────────┘                │                                   │    │
│                                    │    ┌───────────────────────┐     │    │
│   ┌───────────────┐                │    │  Admin Access Service │     │    │
│   │  REST API     │                │    └───────────────────────┘     │    │
│   │  (Heracles)   │───────────────▶│                                   │    │
│   └───────────────┘                └───────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Web Console Applications

| Application | Personas | Purpose |
|-------------|----------|---------|
| **Hub Control Center** | Administrator | Tenant and subscription management |
| **Workbench Studio** | Process Architect, Developer | Scenario design and development |
| **Agent Desk** | Agent | Task execution, customer interaction |
| **Supervisor Desk** | Supervisor | Queue management, team oversight |
| **Steward Desk** | Workbench Admin | Workbench operations |
| **Hub Home** | Agent, Supervisor | Personal dashboard |

---

## Behavior

### Channel Selection

```
User Intent → Persona Context → Available Channels → Selected Channel

Example:
- Agent wants to check tasks
- Context: Mobile, between meetings
- Available: Web, MS Teams, MCP
- Selected: MS Teams (quick access, conversational)

Example:
- Developer building Scenario
- Context: Desktop, deep work
- Available: Web, REST API
- Selected: Web Console (full IDE features)
```

### Headless Services Pattern

```
1. User interacts via Channel
2. Channel adapter translates to service call
3. Headless Access Service processes request
4. Service returns data
5. Channel adapter renders for presentation
6. User sees channel-appropriate response
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Persona | ← accessed by | Personas access via Channels |
| Headless Services | → calls | Channels call backend services |
| Cipher IAM | → authenticates | All channels authenticate |
| Notification Services | ← receives | Notifications delivered via Channels |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Authentication** | All channel access authenticated |
| **Authorization** | Persona-appropriate access enforced |
| **Capability parity** | Core capabilities available across channels |
| **Presentation varies** | Same data, channel-appropriate rendering |
| **Delegation capable** | Channels can facilitate delegation from business users |

---

## Delegation Responsibilities

Channels play a critical role in **Request-Scoped Authority Delegation**, enabling business users to grant agents authority to act on their behalf.

### Channel vs. Signal Provider

| Aspect | Signal Provider | Channel |
|--------|----------------|---------|
| **Purpose** | Signal ingestion (events, files, API calls) | User interaction interface |
| **User Presence** | No user context; machine-to-machine | User is present and can interact |
| **Delegation Role** | **Cannot delegate** | **Can facilitate delegation** |

### Delegation Capabilities

| Capability | Description |
|------------|-------------|
| **Capture Consent** | Present Delegation Template to user, obtain explicit consent |
| **Request Credentials** | Request Delegation Certificates and Tokens from Cipher IAM Extensions |
| **Attach to Request** | Include Delegation Certificate/Token in Request initiation |
| **Handle Authority Requests** | Receive `AUTHORITY_REQUEST` updates, prompt user for consent |
| **Implicit Fulfillment** | Check existing Delegation Certificates before prompting user |

### Authority Request Flow

```
Agent needs authority → Sidecar posts AUTHORITY_REQUEST → Signal Exchange routes to Channel
    → Channel prompts user (or auto-fulfills) → User grants 
    → Channel requests Certificate from Cipher → Channel requests Token from Cipher
    → Channel posts AUTHORITY_GRANTED (with token) → Signal Exchange delivers to agent
```

### Observer Registration

Channels register as **observer modules** with Signal Exchange to receive `REQUEST_UPDATE` messages, including:
- `AUTHORITY_REQUEST`: Agent requesting delegation
- `AUTHORITY_GRANTED`: Confirmation of granted authority
- Other status updates relevant to user interaction

See [Request-Scoped Authority Delegation](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md) for complete design details.

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **User choice** | Interact via preferred channel |
| ✅ **AI integration** | AI assistants as first-class citizens |
| ✅ **Context-appropriate** | Right interface for each situation |
| ✅ **Consistent capabilities** | Same business logic, all channels |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Multiple surfaces** | Shared design system; headless backend |
| ⚠️ **Feature parity** | Clear channel capability matrix |

---

## Examples

### Example 1: Agent Checking Tasks

```
Channel: MS Teams (Me_Bot)

User: "Show my tasks"

Me_Bot: 
  Here are your assigned tasks:
  
  1. 🔴 URGENT: Dispute INV-2345 
     Customer: John Smith
     Amount: $1,500
     Due: 2 hours
     [View Details] [Start Work]
  
  2. 🟡 Normal: Refund REQ-5678
     Customer: Jane Doe
     Amount: $250
     Due: Tomorrow
     [View Details]
```

### Example 2: Same Task via Web Console

```
Channel: Web Console (Agent Desk)

┌─────────────────────────────────────────────────────────────────┐
│ My Tasks                                              [Refresh] │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ 🔴 URGENT                                      Due: 2 hours │ │
│ │                                                              │ │
│ │ Dispute INV-2345                                            │ │
│ │ Customer: John Smith                                        │ │
│ │ Amount: $1,500.00                                           │ │
│ │                                                              │ │
│ │ [Start Work] [View History] [Escalate] [Transfer]          │ │
│ └─────────────────────────────────────────────────────────────┘ │
│                                                                  │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ 🟡 Normal                                      Due: Tomorrow │ │
│ │ ...                                                          │ │
│ └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

---

## Implementation Notes

### For Developers

- Use headless services, not channel-specific logic
- Test capabilities across channels
- Consider channel limitations in UX design
- Support offline/degraded modes where appropriate

### For Operators

- Monitor channel health independently
- Configure channel-specific rate limits
- Review channel usage for capacity planning

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Persona](./persona.md) | Personas access Hub via Channels |
| [Headless Access Service](./headless-access-service.md) | Backend for all Channels |
| [Notification Services](./notification-services.md) | Delivers via Channels |
| [Request-Scoped Delegation](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md) | Channels facilitate delegation |
| [Observer Pattern](./observer-pattern.md) | Channels are observer modules |

---

## References

- [UX Architecture](../../06-ux-architecture/README.md)
- [MCP Channels](../../06-ux-architecture/tenant-domain/mcp-channels.md)
- [REST Channels](../../06-ux-architecture/tenant-domain/rest-channels.md)
- [MS Teams Integration](../../04-subsystems/ms-teams-integration/README.md)
- [ADR-0010: AI Assistants as First-Class Channel](../../decision-logs/0010-ai-assistants-first-class-channel.md)

