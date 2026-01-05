# MCP Gateways

> **Status:** 🔴 Stub — Placeholder for expansion

Hub exposes **Model Context Protocol (MCP) Gateways** to enable AI agents and assistants to interact with Hub capabilities programmatically.

---

## Overview

MCP Gateways provide structured access to Hub for AI systems like ChatGPT, Claude, Gemini, and custom AI agents. Each gateway is **named by the persona it serves** and scoped accordingly.

### Gateway Summary

| Gateway | Persona(s) | Plane | Purpose |
|---------|------------|-------|---------|
| **Tenant Admin** | Administrator | Control | Subscription management |
| **Creator** | Process Architect, Developer | Control | Design and development |
| **Agent** | Agent (Human/AI) | Control | Task processing |
| **Supervisor** | Supervisor | Control | Operations management |
| **Business User** | Business Customer, Business Employee, Business System | Data | Request initiation |

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
│  │         (Authentication, Authorization, Routing, Rate Limiting)      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                          │                                                   │
│       ┌─────────┬────────┼────────┬─────────┬──────────┐                    │
│       ▼         ▼        ▼        ▼         ▼          ▼                    │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────────┐       │
│  │ Tenant  │ │ Creator │ │  Agent  │ │Supervisor│ │  Business User  │       │
│  │  Admin  │ │ Gateway │ │ Gateway │ │ Gateway │ │     Gateway     │       │
│  │ Gateway │ │         │ │         │ │         │ │                 │       │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────────────┘       │
│       │           │           │           │               │                 │
│       │           │           │           │               │                 │
│  Control Plane Gateways                    Data Plane Gateway               │
│  (Hub Administration)                      (Request Initiation)             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

All gateways are behind the MCP Orchestrator, which handles authentication, authorization, routing, and rate limiting uniformly.

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

### Business User MCP Gateway

| Aspect | Description |
|--------|-------------|
| **Purpose** | Request initiation and updates for business domain actors |
| **Scope** | Scenario-specific within a Workbench |
| **Access** | Business domain actors (see personas below) |

---

#### Personas Served

This gateway serves **Business Domain Actors** — users who interact with Hub to initiate or participate in business operations:

| Persona | Description | Typical Interactions |
|---------|-------------|---------------------|
| **Business Customer** | End customer of the tenant's business | Self-serve requests, status queries, updates |
| **Business Employee** | Employee assisting customers or handling internal work | Assisted requests, business operations |
| **Business System Actor** | Automated systems initiating requests | System-triggered requests, integrations |

See [Personas - Business Domain](../08-personas-and-journeys/README.md#business-domain-actors) for details.

---

#### Request Types Supported

| Request Type | Description | Typical Persona |
|--------------|-------------|-----------------|
| **Service Request** | Customer-facing operations (always has customer subject) | Customer (self-serve), Employee (assisted), System |
| **Business Request** | Internal business operations | Employee, System |
| **System Request** | System/data integrity issues requiring business resolution | System only |

---

#### Capabilities

| Capability | Description |
|------------|-------------|
| **Initiate Request** | Start a new request for a scenario |
| **Query Request Status** | Get current status and progress |
| **Send Request Update** | Provide additional information or input |
| **Receive Notifications** | Subscribe to request lifecycle events |
| **Query Knowledge** | Access relevant knowledge base content |
| **Self-Serve Actions** | Customer-specific self-service capabilities (if configured) |

---

#### Access Control

| Aspect | Details |
|--------|---------|
| **Authentication** | Via Cipher IAM (customer, employee, or system identity) |
| **Authorization** | OPA policies per scenario's self-serve and access configuration |
| **Scoping** | Limited to scenarios the persona is authorized to interact with |
| **Tenant Isolation** | Strict tenant boundary enforcement |

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

