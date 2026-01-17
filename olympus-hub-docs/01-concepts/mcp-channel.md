# MCP Channel

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

An MCP Channel is a **platform service** that enables AI agents and assistants to interact with Hub capabilities via the Model Context Protocol (MCP). It provides persona-scoped access surfaces through MCP Servers, which are workbench-scoped configuration resources.

---

## What is an MCP Channel?

An MCP Channel is a **platform service** (infrastructure) that:

- Provides MCP protocol infrastructure (authentication, routing, session management)
- Exposes MCP Servers as endpoints
- Manages resource subscriptions and real-time notifications
- Provides directory services for collaborators

**Key Distinction:**
- **MCP Channel** = Platform service (infrastructure)
- **MCP Server** = Workbench-scoped CRD (configuration)

---

## Relationship to Other Channels

MCP is one of several **channel types** in Hub:

| Channel Type | Protocol | Use Case | Persona Focus |
|--------------|----------|----------|---------------|
| **REST Channels** | HTTP/REST | Web/mobile/system clients | Persona-scoped APIs |
| **Web Console** | Web UI | Browser-based interaction | Persona-specific consoles |
| **MS Teams** | MS Teams Bot | Collaboration platform | Persona-specific bots |
| **MCP** | MCP Protocol | AI agent integration | Persona-scoped MCP Servers |

All channels are **persona-scoped** and provide access to the same underlying Hub capabilities through different protocols and interfaces.

---

## MCP as Persona-Scoped Access Surface

MCP Channels provide **persona-scoped access** to Hub:

- Each persona has access to MCP Servers configured for their role
- Access control via OPA policies evaluates persona, workbench, and permissions
- MCP Servers are configured per workbench (except admin-template which is tenant-scoped)

**Example:**
- Business Customer persona → `business-user-template` MCP Servers
- Supervisor persona → `supervisor-template` MCP Servers
- Developer persona → `creator-template` MCP Servers

---

## Two Categories of Templates

MCP Servers use **template kinds** that fall into two categories:

### Scenario-Based Templates (Request Lifecycle)

These templates expose Hub scenarios, requests, tasks, and resources with full request lifecycle management:

- `business-user-template` — Request initiation and participation
- `supervisor-template` — Queue management, agent oversight
- `agent-template` — Task processing, knowledge access
- `creator-template` — Scenario design, development
- `admin-template` — Subscription/resource management
- `auditor-template` — Compliance, investigation

**Characteristics:**
- Full request lifecycle (create, update, complete)
- Prompt templates for task solving and guidance
- Resource subscriptions for real-time updates
- Session management (OAuth, lifecycle)

### Tool-Based Templates (Passthrough)

These templates expose Tool Registry tools directly, with no request lifecycle:

- `machine-template` — Expose Machine tools via MCP

**Characteristics:**
- Stateless tool invocation
- No request lifecycle
- No prompts, no resources, no sessions
- Direct passthrough to HTTP Tool Calling Application

---

## Control Plane vs Data Plane

MCP Channels operate in both planes:

| Plane | Templates | Purpose |
|-------|-----------|---------|
| **Control Plane** | supervisor-template, agent-template, creator-template, admin-template, auditor-template | Hub administration, operations, design |
| **Data Plane** | business-user-template | Request initiation and participation |

---

## Architecture Relationship

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP CLIENT (AI Agent)                        │
└────────────────────────────┬────────────────────────────────────┘
                             │ MCP Protocol
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      MCP ROUTER                                  │
│         (Authentication, Authorization, Routing)                │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MCP CHANNEL                                  │
│                  (Platform Service)                             │
│  - Session Management                                           │
│  - Resource Subscriptions                                       │
│  - Directory Service                                            │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MCP SERVERS                                  │
│              (Workbench-scoped CRDs)                            │
│  - business-user-template                                       │
│  - supervisor-template                                          │
│  - agent-template                                               │
│  - creator-template                                             │
│  - admin-template                                               │
│  - auditor-template                                             │
│  - machine-template                                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [MCP Channel Subsystem](../../04-subsystems/mcp-channel/README.md) — Detailed subsystem documentation
- [MCP Channels](../../06-ux-architecture/tenant-domain/mcp-channels.md) — UX architecture
- [MCP Router](../../05-infrastructure/mcp-router.md) — Infrastructure component
- [Channel Concept](./channel.md) — General channel concept

---

*TODO: Expand with examples, use cases, and integration patterns*
