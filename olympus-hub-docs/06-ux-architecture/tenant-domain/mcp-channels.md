# MCP Channels

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-08

Hub exposes **MCP Channels** to enable AI agents and assistants to interact with Hub capabilities programmatically. Each channel is scoped to a specific persona and provides a curated set of tools.

MCP Channels include **Directability Methods** for handling escalation tasks created when AI agent outputs are rejected. See [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md) for the full directability model.

---

## Overview

MCP Channels provide persona-scoped access to Hub for AI systems like ChatGPT, Claude, Gemini, and custom AI agents. All channels are served through the **MCP Router**, which handles authentication, authorization, and routing.

### Channel Summary

| Channel | Persona(s) | Plane | Purpose |
|---------|------------|-------|---------|
| **Tenant Admin** | Administrator | Control | Subscription management |
| **Creator** | Process Architect, Developer | Control | Design and development |
| **Agent** | Agent (Human/AI) | Control | Task processing |
| **Supervisor** | Supervisor | Control | Operations management |
| **Business User** | Business Customer, Business Employee, Business System | Data | Request initiation |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MCP ARCHITECTURE                                     │
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
│  │                        MCP ROUTER                                    │    │
│  │         (Authentication, Authorization, Routing, Rate Limiting)      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                          │                                                   │
│       ┌─────────┬────────┼────────┬─────────┬──────────┐                    │
│       ▼         ▼        ▼        ▼         ▼          ▼                    │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────────┐       │
│  │ Tenant  │ │ Creator │ │  Agent  │ │Supervisor│ │  Business User  │       │
│  │  Admin  │ │ Channel │ │ Channel │ │ Channel │ │     Channel     │       │
│  │ Channel │ │         │ │         │ │         │ │                 │       │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────────────┘       │
│       │           │           │           │               │                 │
│  Control Plane Channels                   Data Plane Channel                │
│  (Hub Administration)                     (Request Initiation)              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Router ↔ Channel Integration

The **MCP Router** is the central infrastructure component that:
1. Receives requests from AI assistants via Heracles
2. Validates authentication (JWT)
3. Determines target MCP Channel from persona context
4. Applies channel-specific tool discovery filtering
5. Routes to channel-scoped tool providers
6. Aggregates responses and returns to client

See [MCP Router](../05-infrastructure/mcp-router.md) for infrastructure details.

| Responsibility | MCP Router | MCP Channel |
|----------------|------------|-------------|
| **Authentication** | JWT validation | N/A (handled by Router) |
| **Authorization** | OPA policy evaluation | Tool-specific policies |
| **Discovery** | Filter by channel scope | Define tool catalog |
| **Routing** | Select channel, forward | Expose tools to Router |

---

## Control Plane Channels

### Tenant Admin MCP Channel

| Aspect | Description |
|--------|-------------|
| **Persona** | [Administrator](../08-personas-and-journeys/personas/administrator.md) |
| **Scope** | Tenant Subscription |
| **Purpose** | Subscription management via AI assistant |

**Capabilities:**
- Query subscription status
- List workbenches, users, machines
- View usage and budget
- Initiate configuration changes (with approval)

---

### Creator MCP Channel

| Aspect | Description |
|--------|-------------|
| **Persona** | [Process Architect](../08-personas-and-journeys/personas/process-architect.md), [Developer](../08-personas-and-journeys/personas/developer.md) |
| **Scope** | Workbench |
| **Purpose** | Design and development assistance |

**Capabilities:**
- Query scenario definitions
- Access knowledge base
- Generate scenario drafts
- Test trigger configurations
- Debug application issues

---

### Agent MCP Channel

| Aspect | Description |
|--------|-------------|
| **Persona** | [Agent](../08-personas-and-journeys/personas/agent.md) (Human/AI) |
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

### Supervisor MCP Channel

| Aspect | Description |
|--------|-------------|
| **Persona** | [Supervisor](../08-personas-and-journeys/personas/supervisor.md) |
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

## Data Plane Channel

### Business User MCP Channel

| Aspect | Description |
|--------|-------------|
| **Purpose** | Request initiation and updates for business domain actors |
| **Scope** | Scenario-specific within a Workbench |
| **Access** | Business domain actors (see personas below) |

---

#### Personas Served

This channel serves **Business Domain Actors** — users who interact with Hub to initiate or participate in business operations:

| Persona | Description | Typical Interactions |
|---------|-------------|---------------------|
| [**Business Customer**](../08-personas-and-journeys/personas/business-domain/business-customer.md) | End customer of the tenant's business | Self-serve requests, status queries, updates |
| [**Business Employee**](../08-personas-and-journeys/personas/business-domain/business-employee.md) | Employee assisting customers or handling internal work | Assisted requests, business operations |
| [**Business System Actor**](../08-personas-and-journeys/personas/business-domain/business-system-actor.md) | Automated systems initiating requests | System-triggered requests, integrations |

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

MCP Channels expose Hub capabilities as MCP tools:

| Category | Example Tools |
|----------|--------------|
| **Task Tools** | `list_tasks`, `get_task`, `complete_task`, `escalate_task` |
| **Request Tools** | `get_request`, `list_requests`, `add_memo`, `add_thought` |
| **Knowledge Tools** | `search_knowledge`, `get_sop`, `get_policy` |
| **Entity Tools** | `get_entity`, `search_entities` |
| **Queue Tools** | `get_queue_metrics`, `reassign_task` |
| **Directability Tools** | `acknowledge_escalation`, `override_decision`, `change_context_rerun`, `fail_scenario` |
| **Feedback Tools** | `promote_feedback`, `list_promoted_feedback`, `list_feedback_inbox`, `accept_feedback`, `resolve_feedback` |

### Directability Tools

Tools for handling escalation tasks created when AI agent outputs are rejected.

| Tool | Description | Channels |
|------|-------------|----------|
| `acknowledge_escalation` | Acknowledge an escalation task for review | Agent, Supervisor |
| `override_decision` | Override a rejected decision with new value | Agent, Supervisor |
| `change_context_rerun` | Modify context and request agent re-run | Agent, Supervisor |
| `reassign_for_retry` | Reassign original task to different agent | Supervisor |
| `fail_scenario` | Fail the scenario due to unresolvable rejection | Supervisor |
| `create_corrective_action` | Create corrective action in different scenario | Supervisor |
| `get_rejection_context` | Get rejection details and resolution options | Agent, Supervisor |

#### Example: Override Decision

```json
{
  "method": "tools/call",
  "params": {
    "name": "override_decision",
    "arguments": {
      "task_id": "esc-task-12345",
      "original_decision_id": "dec-11111",
      "new_decision": {
        "action": "approve_refund",
        "amount": 150.00
      },
      "rationale": "Customer history justifies approval despite low model confidence",
      "rationale_category": "new_information"
    }
  }
}
```

#### Example: Change Context and Re-run

```json
{
  "method": "tools/call",
  "params": {
    "name": "change_context_rerun",
    "arguments": {
      "task_id": "esc-task-12345",
      "additional_context": {
        "customer_tier": "platinum",
        "previous_disputes": [],
        "account_age_years": 12
      },
      "instructions": "Consider customer's long tenure and clean history"
    }
  }
}
```

### Feedback Tools

Tools for promoting feedback to development workbenches and reviewing incoming feedback. See [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md).

#### Promotion Tools (Non-Development Workbenches)

| Tool | Description | Channels |
|------|-------------|----------|
| `promote_feedback` | Promote new feedback to development workbench | Agent, Supervisor, Creator |
| `list_promoted_feedback` | List feedback I've promoted with current status | Agent, Supervisor, Creator |
| `get_feedback_status` | Get status of a specific promoted feedback | Agent, Supervisor, Creator |

#### Inbox Tools (Development Workbenches Only)

| Tool | Description | Channels |
|------|-------------|----------|
| `list_feedback_inbox` | List all incoming feedback from production workbenches | Creator |
| `get_feedback_details` | Get full details of a feedback item | Creator |
| `accept_feedback` | Accept feedback for implementation | Creator |
| `reject_feedback` | Reject feedback with reason | Creator |
| `route_feedback` | Route feedback to PA or Developer | Creator |
| `resolve_feedback` | Mark feedback resolved with link to fix | Creator |
| `list_feedback_sources` | List linked production workbenches | Creator |

#### Example: Promote Feedback

```json
{
  "method": "tools/call",
  "params": {
    "name": "promote_feedback",
    "arguments": {
      "type": "Problem",
      "subtype": "Bug",
      "severity": "high",
      "title": "Escalation not triggering for priority disputes",
      "description": "When a dispute is marked as priority, the escalation should trigger at the 2-hour mark but is not firing.",
      "related_entities": {
        "requests": ["req-1234", "req-5678"],
        "scenarios": ["standard-dispute"]
      }
    }
  }
}
```

#### Example: Accept Feedback (APO in Development Workbench)

```json
{
  "method": "tools/call",
  "params": {
    "name": "accept_feedback",
    "arguments": {
      "feedback_id": "fb-12345",
      "notes": "Will include in v1.4.0 release, targeting 2026-01-15"
    }
  }
}
```

#### Example: Resolve Feedback (APO in Development Workbench)

```json
{
  "method": "tools/call",
  "params": {
    "name": "resolve_feedback",
    "arguments": {
      "feedback_id": "fb-12345",
      "resolution": {
        "scenario_version": "1.4.0",
        "release_notes": "Fixed escalation trigger timing for priority disputes",
        "deployment_date": "2026-01-15"
      }
    }
  }
}
```

---

## Security Model

| Aspect | Mechanism |
|--------|-----------|
| **Authentication** | OAuth 2.0, SPIFFE/SPIRE for workloads |
| **Authorization** | OPA policies per channel |
| **Scoping** | Tools scoped to persona capabilities |
| **Audit** | All MCP invocations logged |
| **Rate Limiting** | Per-client rate limits |

---

## Related Documentation

- [REST Channels](./rest-channels.md) — RESTful API access for web/mobile/system clients
- [MCP Router](../../05-infrastructure/mcp-router.md) — Infrastructure component for routing
- [Heracles Gateway](../../05-infrastructure/heracles-gateway.md) — API Gateway
- [Tool Registry](../../04-subsystems/registry-services/tool-registry.md) — Tool definitions
- [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md) — Production feedback architecture

---

*TODO: Detailed tool specifications, authorization policies, sample invocations*
