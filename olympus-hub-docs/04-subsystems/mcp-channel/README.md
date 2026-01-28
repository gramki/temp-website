# MCP Channel (Subsystem)

> **Status:** 🟡 Draft — Under active development  
> **Last Updated:** 2026-01-17

The MCP Channel is a **platform service** that enables AI agents and assistants to interact with Hub capabilities via the Model Context Protocol (MCP). It provides persona-scoped access surfaces through MCP Servers, which are workbench-scoped configuration resources that expose Hub scenarios, requests, tasks, and tools to AI agents.

---

## Overview

The MCP Channel subsystem is responsible for:

| Function | Description |
|----------|-------------|
| **MCP Server Management** | CRD-based configuration for exposing Hub capabilities via MCP |
| **Client Routing** | Route MCP client requests to appropriate MCP Servers |
| **Session Management** | Manage MCP sessions (authentication, lifecycle, termination) |
| **Tool Discovery** | Expose tools, prompts, and resources per MCP Server template |
| **Resource Subscriptions** | Manage session-bound resource subscriptions for real-time updates |
| **Passthrough Invocation** | Gateway pattern for stateless tool invocation (machine-template) |
| **Directory Service** | Expose MCP Server directory for collaborators |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP CLIENT (AI Agent)                        │
│              (ChatGPT, Claude, Gemini, Custom)                  │
└────────────────────────────┬────────────────────────────────────┘
                             │ MCP Protocol
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    HERACLES GATEWAY                             │
│                    (API Gateway)                                │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      MCP ROUTER                                 │
│         (Authentication, Authorization, Routing)               │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MCP CHANNEL                                  │
│                  (Platform Service)                             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              MCP OPERATOR                                │   │
│  │  (Watches CRDs, Provisions Endpoints)                   │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐   │
│  │              MCP SERVER REGISTRY                         │   │
│  │  (business-user-template, supervisor-template, etc.)    │   │
│  └─────────────────────────┼───────────────────────────────┘   │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐   │
│  │         SESSION MANAGER                                  │   │
│  │  (OAuth, Session Lifecycle, Resource Subscriptions)      │   │
│  └─────────────────────────┼───────────────────────────────┘   │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐   │
│  │         DIRECTORY SERVICE                               │   │
│  │  (For Collaborators: list_mcp_servers, etc.)            │   │
│  └─────────────────────────┴───────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                     │
        ▼                    ▼                     ▼
┌──────────────┐   ┌──────────────────┐   ┌──────────────────┐
│   SCENARIO   │   │  TOOL REGISTRY   │   │  HTTP TOOL       │
│   TEMPLATES  │   │  (machine-       │   │  CALLING APP     │
│              │   │   template)      │   │  (passthrough)   │
└──────────────┘   └──────────────────┘   └──────────────────┘
```

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **MCP Channel** | Platform service providing infrastructure for MCP Servers |
| **MCP Server** | Workbench-scoped CRD that exposes Hub capabilities via MCP |
| **Template Kind** | CRD kind that implies persona and capabilities (e.g., `business-user-template`) |
| **MCP Operator** | Kubernetes operator that provisions endpoints based on MCP Server CRDs |
| **Prompt Templates** | Developer-defined prompts for task solving and guidance |
| **Resources** | Request-scoped entities exposed for subscription (requests, tasks, queues, etc.) |
| **Sessions** | MCP session lifecycle (OAuth, termination, resource subscriptions) |
| **Directory Service** | Service for collaborators to discover available MCP Servers |

---

## Template Kinds

The MCP Channel subsystem supports **seven template kinds** organized into two categories:

### Scenario-Based Templates (Request Lifecycle)

These templates expose Hub scenarios, requests, tasks, and resources with full request lifecycle management.

| Template Kind | Persona(s) | Tools | Prompts | Resources | Sessions |
|---------------|------------|-------|---------|-----------|----------|
| `business-user-template` | Business Customer, Employee, System | Request initiation/participation | Task solvers, guidance | Requests | Yes |
| `supervisor-template` | Supervisor | Queue mgmt, SLAs, directability | Queue analysis | Queues, escalations | Yes |
| `agent-template` | Agent (Human/AI) | Task processing, knowledge | Task solvers | Tasks, requests | Yes |
| `creator-template` | Process Architect, Developer | Scenario design, feedback | Design guides | Scenarios, feedback | Yes |
| `admin-template` | Administrator | Subscription mgmt | Resource optimization | Workbenches | Yes |
| `auditor-template` | Auditor | Decision investigation | Investigation guides | Audit trails | Yes |

### Tool-Based Templates (Passthrough)

These templates expose Tool Registry tools directly, with no request lifecycle.

| Template Kind | Purpose | Tools | Prompts | Resources | Sessions |
|---------------|---------|-------|---------|-----------|----------|
| `machine-template` | Expose Machine tools via MCP | From Tool Registry | None | None | Stateless |

---

## Core Responsibilities

### MCP Server Management

- **CRD-based Configuration**: MCP Servers defined as Kubernetes CRDs
- **Template Kinds**: Seven template kinds for different personas and use cases
- **Access Control**: OPA-based policies for authorization
- **Tool Discovery**: Expose tools, prompts, and resources per template

### Client Routing

- **Protocol Translation**: MCP protocol to Hub internal APIs
- **Authentication**: OAuth 2.0 via MCP Router
- **Authorization**: OPA policy evaluation per request
- **Session Management**: OAuth session lifecycle

### Resource Subscriptions

- **Session-bound Subscriptions**: Resources subscribed per MCP session
- **Real-time Updates**: JSON-RPC notifications for resource changes
- **Transport Options**: SSE (default) and Streamable HTTP (fallback)

### Passthrough Invocation

- **Machine Template**: Expose Tool Registry tools without request lifecycle
- **Gateway Pattern**: MCP Router acts as gateway for stateless tool calls
- **HTTP Tool Calling**: Native HTTP tool invocation via HTTP Tool Calling Application

---

## Integration Points

### Inbound

| Source | Interface | Description |
|--------|-----------|-------------|
| **MCP Router** | MCP Protocol | Client requests, tool calls, resource subscriptions |
| **MCP Operator** | Kubernetes API | CRD watch, endpoint provisioning |
| **Cipher IAM** | OAuth 2.0 | Authentication, token validation |
| **Tool Registry** | Internal API | Tool discovery for machine-template |

### Outbound

| Target | Interface | Description |
|--------|-----------|-------------|
| **Signal Exchange** | Internal API | Request creation/updates (scenario-based templates) |
| **HTTP Tool Calling Application** | HTTP | Tool invocation (machine-template) |
| **Request Lifecycle Manager** | Internal API | Request status, timeline queries |
| **Task Management** | Internal API | Task operations (agent/supervisor templates) |
| **Knowledge Services** | Internal API | Knowledge base access (agent/creator templates) |

---

## Subsystem Documents

| Document | Description | Status |
|----------|-------------|--------|
| [MCP Server CRD](./mcp-server-crd.md) | CRD specification for all template kinds | 🟡 Draft |
| [Machine Template](./machine-template.md) | Passthrough pattern for Tool Registry tools | 🟡 Draft |
| [MCP Operator](./mcp-operator.md) | Operator for endpoint provisioning | 🟡 Draft |
| [Session Management](./session-management.md) | OAuth, session lifecycle, subscriptions | 🟡 Draft |
| [Prompt Templates](./prompt-templates.md) | Prompt template format and compilation | 🟡 Draft |
| [Resource Management](./resource-management.md) | Resource types, subscriptions, notifications | 🟡 Draft |
| [Directory Service](./directory-service.md) | Directory for collaborators | 🟡 Draft |

---

## Related Documentation

- [MCP Channels](../../06-ux-architecture/tenant-domain/mcp-channels.md) — UX architecture for MCP Channels
- [MCP Router](../../05-infrastructure/mcp-router.md) — Infrastructure component for routing
- [Tool Registry](../registry-services/tool-registry.md) — Tool catalog for machine-template
- [HTTP Tool Calling Application](../hub-native-utilities/http-tool-calling-application.md) — Passthrough invocation
- [Signal Exchange](../signal-exchange/README.md) — Request lifecycle for scenario-based templates
- [ADR-0131](../../decision-logs/0131-mcp-server-crd-design.md) — MCP Server CRD Design
- [ADR-0132](../../decision-logs/0132-mcp-template-kinds.md) — MCP Template Kinds
- [ADR-0135](../../decision-logs/0135-machine-template-passthrough.md) — Machine Template Passthrough Pattern

---

*TODO: Detailed design — endpoint provisioning, session persistence, resource subscription lifecycle, tool invocation patterns*
