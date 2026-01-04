# MCP Gateways

> **Status:** 🔴 Stub — Placeholder for expansion

Hub exposes **Model Context Protocol (MCP) Gateways** to enable AI agents and assistants to interact with Hub capabilities programmatically.

---

## Overview

MCP Gateways provide structured access to Hub for AI systems like ChatGPT, Claude, Gemini, and custom AI agents. Each gateway is scoped to a specific persona and purpose.

---

## Gateway Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MCP GATEWAY ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  AI ASSISTANTS                                                               │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐           │
│  │ ChatGPT │  │ Claude  │  │ Gemini  │  │ Custom  │  │  Seer   │           │
│  │ Agent   │  │ Agent   │  │ Agent   │  │ Agents  │  │ Agents  │           │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘           │
│       │            │            │            │            │                  │
│       └────────────┴─────┬──────┴────────────┴────────────┘                  │
│                          │                                                   │
│                          ▼                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     MCP ORCHESTRATOR                                 │    │
│  │  (Authentication, Authorization, Routing, Rate Limiting)            │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                          │                                                   │
│       ┌──────────────────┼──────────────────┬──────────────────┐            │
│       ▼                  ▼                  ▼                  ▼            │
│  ┌─────────┐       ┌─────────┐       ┌─────────┐       ┌─────────┐         │
│  │ Tenant  │       │ Creator │       │  Agent  │       │Supervisor│         │
│  │ Admin   │       │ Gateway │       │ Gateway │       │ Gateway │         │
│  │ Gateway │       │         │       │         │       │         │         │
│  └─────────┘       └─────────┘       └─────────┘       └─────────┘         │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    SCENARIO MCP GATEWAY                              │    │
│  │                  (Data Plane - Request Initiation)                   │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │    │
│  │  │  Service    │  │  Business   │  │   System    │                  │    │
│  │  │  Request    │  │  Request    │  │   Request   │                  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Control Plane Gateways

### Tenant Admin MCP Gateway

| Aspect | Description |
|--------|-------------|
| **Persona** | Administrator |
| **Scope** | Tenant Subscription |
| **Purpose** | Subscription management via AI assistant |

**Capabilities:**
- Query subscription status
- List workbenches, users, machines
- View usage and budget
- Initiate configuration changes (with approval)

---

### Creator MCP Gateway

| Aspect | Description |
|--------|-------------|
| **Persona** | Process Architect, Developer |
| **Scope** | Workbench |
| **Purpose** | Design and development assistance |

**Capabilities:**
- Query scenario definitions
- Access knowledge base
- Generate scenario drafts
- Test trigger configurations
- Debug application issues

---

### Agent MCP Gateway

| Aspect | Description |
|--------|-------------|
| **Persona** | Agent |
| **Scope** | Workbench |
| **Purpose** | Task processing via AI assistant |

**Capabilities:**
- List assigned tasks
- Query task details and context
- Access knowledge base
- Invoke registered tools
- Record decisions and thoughts
- Complete or escalate tasks

---

### Supervisor MCP Gateway

| Aspect | Description |
|--------|-------------|
| **Persona** | Supervisor |
| **Scope** | Workbench |
| **Purpose** | Operations management via AI assistant |

**Capabilities:**
- Query queue metrics
- List agents and availability
- View SLA status
- Reassign tasks
- Manage escalations
- Generate reports

---

## Data Plane Gateway

### Scenario MCP Gateway

| Aspect | Description |
|--------|-------------|
| **Purpose** | Request initiation and updates |
| **Scope** | Scenario-specific |
| **Access** | Authorized systems and applications |

**Request Types Supported:**
- **Service Request** — Customer-facing operations
- **Business Request** — Internal business operations
- **System Request** — System/data integrity issues

**Capabilities:**
- Initiate requests
- Query request status
- Send request updates
- Receive notifications

---

## Tool Exposure

MCP Gateways expose Hub capabilities as MCP tools:

| Category | Example Tools |
|----------|--------------|
| **Task Tools** | `list_tasks`, `get_task`, `complete_task`, `escalate_task` |
| **Request Tools** | `get_request`, `list_requests`, `add_memo`, `add_thought` |
| **Knowledge Tools** | `search_knowledge`, `get_sop`, `get_policy` |
| **Entity Tools** | `get_entity`, `search_entities` |
| **Queue Tools** | `get_queue_metrics`, `reassign_task` |

---

## Security Model

| Aspect | Mechanism |
|--------|-----------|
| **Authentication** | OAuth 2.0, SPIFFE/SPIRE for workloads |
| **Authorization** | OPA policies per gateway |
| **Scoping** | Tools scoped to persona capabilities |
| **Audit** | All MCP invocations logged |
| **Rate Limiting** | Per-client rate limits |

---

## Related Documentation

- [MCP Orchestrator](../05-infrastructure/mcp-orchestrator.md)
- [Heracles Gateway](../05-infrastructure/heracles-gateway.md)
- [Tool Registry](../04-subsystems/registry-services/tool-registry.md)

---

*TODO: Detailed tool specifications, authorization policies, sample invocations*

