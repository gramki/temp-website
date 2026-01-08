# REST Channels

> **Status:** 🟡 Draft — API structure defined

Hub exposes **REST Channels** via Heracles Gateway to enable web applications, mobile apps, and system integrations to interact with Hub capabilities programmatically. Each channel is scoped to a specific persona and provides a curated set of APIs.

---

## Overview

REST Channels provide persona-scoped RESTful APIs for Hub. All channels are served through the **Heracles Gateway**, which handles authentication, authorization, rate limiting, and routing.

### Channel Summary

| Channel | Persona(s) | Plane | Base Path | Purpose |
|---------|------------|-------|-----------|---------|
| **Tenant Admin** | Administrator | Control | `/api/admin/v1` | Subscription management |
| **Creator** | Process Architect, Developer | Control | `/api/creator/v1` | Design and development |
| **Agent** | Agent (Human/AI) | Control | `/api/agent/v1` | Task processing |
| **Supervisor** | Supervisor | Control | `/api/supervisor/v1` | Operations management |
| **Business User** | Business Customer, Employee, System | Data | `/api/business/v1` | Request initiation |
| **Auditor** | Auditor | Control | `/api/auditor/v1` | Compliance review |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         REST ARCHITECTURE                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  CLIENTS                                                                     │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐           │
│  │   Web   │  │ Mobile  │  │ System  │  │  CLI    │  │ Postman │           │
│  │   Apps  │  │  Apps   │  │ Clients │  │ Tools   │  │ / Test  │           │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘           │
│       │            │            │            │            │                  │
│       └────────────┴─────┬──────┴────────────┴────────────┘                  │
│                          │                                                   │
│                          ▼                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      HERACLES GATEWAY                                │    │
│  │          (Authentication, Authorization, Rate Limiting)             │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                          │                                                   │
│       ┌─────────┬────────┼────────┬─────────┬──────────┬───────┐            │
│       ▼         ▼        ▼        ▼         ▼          ▼       ▼            │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌───────┐   │
│  │ Tenant  │ │ Creator │ │  Agent  │ │Supervisor│ │ Business │ │Auditor│   │
│  │  Admin  │ │ Channel │ │ Channel │ │ Channel │ │   User   │ │Channel│   │
│  │ Channel │ │         │ │         │ │         │ │  Channel │ │       │   │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └──────────┘ └───────┘   │
│       │           │           │           │             │          │        │
│  Control Plane Channels                   │     Data Plane    Control      │
│  (Hub Administration)                     │     Channel       Plane        │
│                                           │                                 │
└───────────────────────────────────────────┴─────────────────────────────────┘
```

---

## Common Patterns

### Request/Response Format

All APIs use JSON request/response bodies:

```http
Content-Type: application/json
Accept: application/json
```

### Authentication

```http
Authorization: Bearer <JWT>
```

### Standard Response Envelope

```json
{
  "data": { ... },
  "meta": {
    "request_id": "req-12345",
    "timestamp": "2026-01-05T10:00:00Z"
  }
}
```

### Error Response

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request payload",
    "details": [
      { "field": "queue_id", "issue": "required" }
    ]
  },
  "meta": {
    "request_id": "req-12345",
    "timestamp": "2026-01-05T10:00:00Z"
  }
}
```

### Pagination

```http
GET /api/agent/v1/tasks?page=1&page_size=20
```

Response includes pagination metadata:
```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total_items": 150,
    "total_pages": 8
  }
}
```

---

## Control Plane Channels

---

## Tenant Admin REST Channel

**Base Path:** `/api/admin/v1`

| Aspect | Description |
|--------|-------------|
| **Persona** | [Administrator](../../08-personas-and-journeys/personas/administrator.md) |
| **Scope** | Tenant Subscription |
| **Purpose** | Subscription and resource management |

### Subscription APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/subscription` | Get subscription details |
| `GET` | `/subscription/usage` | Get current usage metrics |
| `GET` | `/subscription/budget` | Get budget and cost information |
| `PUT` | `/subscription/budget` | Update budget configuration |

### Workbench APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/workbenches` | List all workbenches |
| `POST` | `/workbenches` | Create a new workbench |
| `GET` | `/workbenches/{workbench_id}` | Get workbench details |
| `PUT` | `/workbenches/{workbench_id}` | Update workbench configuration |
| `DELETE` | `/workbenches/{workbench_id}` | Archive workbench |

### User Management APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/users` | List users in tenant |
| `POST` | `/users` | Provision a new user |
| `GET` | `/users/{user_id}` | Get user details |
| `PUT` | `/users/{user_id}` | Update user |
| `DELETE` | `/users/{user_id}` | Deactivate user |
| `GET` | `/users/{user_id}/roles` | Get user role assignments |
| `PUT` | `/users/{user_id}/roles` | Update user roles |

### User Group APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/groups` | List user groups |
| `POST` | `/groups` | Create user group |
| `GET` | `/groups/{group_id}` | Get group details |
| `PUT` | `/groups/{group_id}` | Update group |
| `GET` | `/groups/{group_id}/members` | List group members |
| `POST` | `/groups/{group_id}/members` | Add members to group |
| `DELETE` | `/groups/{group_id}/members/{user_id}` | Remove member |

### Machine & Gateway APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/machines` | List registered machines |
| `POST` | `/machines` | Register a machine |
| `GET` | `/machines/{machine_id}` | Get machine details |
| `PUT` | `/machines/{machine_id}` | Update machine configuration |
| `DELETE` | `/machines/{machine_id}` | Deregister machine |
| `GET` | `/gateways` | List I/O gateway configurations |
| `PUT` | `/gateways/{gateway_id}` | Update gateway configuration |

### Data Store APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/data-stores` | List allocated data stores |
| `POST` | `/data-stores` | Allocate new data store |
| `GET` | `/data-stores/{store_id}` | Get data store details |
| `PUT` | `/data-stores/{store_id}` | Update data store configuration |

---

## Creator REST Channel

**Base Path:** `/api/creator/v1`

| Aspect | Description |
|--------|-------------|
| **Persona** | [Process Architect](../../08-personas-and-journeys/personas/process-architect.md), [Developer](../../08-personas-and-journeys/personas/developer.md) |
| **Scope** | Workbench |
| **Purpose** | Design and development |

### Scenario APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/scenarios` | List scenarios in workbench |
| `POST` | `/scenarios` | Create a new scenario |
| `GET` | `/scenarios/{scenario_id}` | Get scenario definition |
| `PUT` | `/scenarios/{scenario_id}` | Update scenario |
| `GET` | `/scenarios/{scenario_id}/versions` | List scenario versions |
| `POST` | `/scenarios/{scenario_id}/versions` | Create new version |
| `GET` | `/scenarios/{scenario_id}/manifest` | Get deployment manifest |

### Trigger APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/triggers` | List triggers in workbench |
| `POST` | `/triggers` | Create a trigger |
| `GET` | `/triggers/{trigger_id}` | Get trigger definition |
| `PUT` | `/triggers/{trigger_id}` | Update trigger |
| `DELETE` | `/triggers/{trigger_id}` | Delete trigger |
| `POST` | `/triggers/{trigger_id}/test` | Test trigger with sample signal |

### Application APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/applications` | List applications |
| `POST` | `/applications` | Register an application |
| `GET` | `/applications/{app_id}` | Get application details |
| `PUT` | `/applications/{app_id}` | Update application |
| `GET` | `/applications/{app_id}/deployments` | List deployments |
| `POST` | `/applications/{app_id}/deploy` | Deploy application |

### Knowledge APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/knowledge/categories` | List knowledge categories |
| `POST` | `/knowledge/categories` | Create category |
| `GET` | `/knowledge/documents` | List documents |
| `POST` | `/knowledge/documents` | Upload document |
| `GET` | `/knowledge/documents/{doc_id}` | Get document |
| `PUT` | `/knowledge/documents/{doc_id}` | Update document |
| `DELETE` | `/knowledge/documents/{doc_id}` | Delete document |
| `GET` | `/knowledge/sops` | List SOPs |
| `POST` | `/knowledge/sops` | Create SOP |
| `GET` | `/knowledge/sops/{sop_id}` | Get SOP |
| `PUT` | `/knowledge/sops/{sop_id}` | Update SOP |

### Memory Configuration APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/memory/schemas` | List memory schemas |
| `POST` | `/memory/schemas` | Create memory schema |
| `GET` | `/memory/schemas/{schema_id}` | Get schema definition |
| `PUT` | `/memory/schemas/{schema_id}` | Update schema |

### Tool Registry APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tools` | List registered tools |
| `POST` | `/tools` | Register a tool |
| `GET` | `/tools/{tool_id}` | Get tool definition |
| `PUT` | `/tools/{tool_id}` | Update tool |
| `DELETE` | `/tools/{tool_id}` | Deregister tool |
| `POST` | `/tools/{tool_id}/test` | Test tool invocation |

### Task Type APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/task-types` | List task types in scenario |
| `POST` | `/task-types` | Create task type |
| `GET` | `/task-types/{type_id}` | Get task type definition |
| `PUT` | `/task-types/{type_id}` | Update task type |
| `GET` | `/task-types/{type_id}/solver-template` | Get solver template |
| `PUT` | `/task-types/{type_id}/solver-template` | Update solver template |

---

## Agent REST Channel

**Base Path:** `/api/agent/v1`

| Aspect | Description |
|--------|-------------|
| **Persona** | [Agent](../../08-personas-and-journeys/personas/agent.md) (Human/AI) |
| **Scope** | Workbench |
| **Purpose** | Task processing |

### Task APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tasks` | List assigned tasks |
| `GET` | `/tasks/{task_id}` | Get task details |
| `POST` | `/tasks/{task_id}/start` | Start work on task |
| `POST` | `/tasks/{task_id}/complete` | Complete task with outcome |
| `POST` | `/tasks/{task_id}/hold` | Place task on hold |
| `POST` | `/tasks/{task_id}/resume` | Resume task from hold |
| `POST` | `/tasks/{task_id}/abandon` | Abandon task |
| `POST` | `/tasks/{task_id}/reassign` | Reassign task |
| `GET` | `/tasks/{task_id}/history` | Get task history |
| `GET` | `/tasks/{task_id}/solver` | Get solver template for task |

### Request APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/requests` | List requests I'm involved with |
| `GET` | `/requests/{request_id}` | Get request details |
| `GET` | `/requests/{request_id}/timeline` | Get request timeline |
| `GET` | `/requests/{request_id}/tasks` | List tasks in request |
| `GET` | `/requests/{request_id}/memos` | Get request memos |
| `POST` | `/requests/{request_id}/memos` | Add memo to request |
| `GET` | `/requests/{request_id}/actors` | Get request actors |

### Task Creation APIs (if permitted)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/requests/{request_id}/tasks` | Create task in request |

### Memo & Thought APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/memos` | Create memo (request/task/subject scope) |
| `GET` | `/memos/{memo_id}` | Get memo |
| `POST` | `/thoughts` | Add private thought |
| `GET` | `/thoughts` | List my thoughts |

### Knowledge APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/knowledge/search` | Search knowledge base |
| `GET` | `/knowledge/sops/{sop_id}` | Get SOP |
| `GET` | `/knowledge/policies/{policy_id}` | Get policy |

### Memory APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/memory/enterprise` | Query enterprise memory |
| `GET` | `/memory/user` | Get my user memory |
| `PUT` | `/memory/user` | Update my user memory |
| `GET` | `/memory/subject/{subject_id}` | Get subject memory |

### Tool APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tools` | List available tools |
| `GET` | `/tools/{tool_id}` | Get tool specification |
| `POST` | `/tools/{tool_id}/invoke` | Invoke a tool |

### Entity APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/entities/search` | Search entities |
| `GET` | `/entities/{entity_type}/{entity_id}` | Get entity details |
| `GET` | `/entities/{entity_type}/{entity_id}/history` | Get entity history |

### Directability APIs

APIs for handling escalation tasks created when AI agent outputs are rejected.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/tasks/{task_id}/acknowledge` | Acknowledge escalation task |
| `POST` | `/tasks/{task_id}/override` | Override rejected decision |
| `POST` | `/tasks/{task_id}/change-context` | Change context and trigger re-run |
| `POST` | `/tasks/{task_id}/reassign-retry` | Reassign original task to different agent |
| `POST` | `/tasks/{task_id}/fail-scenario` | Fail the scenario |
| `POST` | `/tasks/{task_id}/corrective-action` | Create corrective action request |
| `GET` | `/tasks/{task_id}/rejection-context` | Get rejection details and options |

#### Override Request Body

```json
{
  "original_decision_id": "dec-11111",
  "new_decision": {
    "action": "approve_refund",
    "amount": 150.00
  },
  "rationale": "Customer history justifies approval",
  "rationale_category": "new_information"
}
```

#### Change Context Request Body

```json
{
  "additional_context": {
    "customer_tier": "platinum",
    "previous_disputes": []
  },
  "instructions": "Consider customer's long tenure"
}
```

See [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md) for the full directability model.

### Decision Recording APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/decisions` | Record a decision |
| `GET` | `/decisions/{decision_id}` | Get decision record |
| `POST` | `/decisions/{decision_id}/evidence` | Attach evidence |

---

## Supervisor REST Channel

**Base Path:** `/api/supervisor/v1`

| Aspect | Description |
|--------|-------------|
| **Persona** | [Supervisor](../../08-personas-and-journeys/personas/supervisor.md) |
| **Scope** | Workbench |
| **Purpose** | Operations management |

### Queue Management APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/queues` | List task queues |
| `POST` | `/queues` | Create task queue |
| `GET` | `/queues/{queue_id}` | Get queue details |
| `PUT` | `/queues/{queue_id}` | Update queue configuration |
| `DELETE` | `/queues/{queue_id}` | Archive queue |
| `GET` | `/queues/{queue_id}/metrics` | Get queue metrics |
| `GET` | `/queues/{queue_id}/tasks` | List tasks in queue |

### Escalation Matrix APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/queues/{queue_id}/escalation` | Get escalation matrix |
| `PUT` | `/queues/{queue_id}/escalation` | Update escalation matrix |

### Queue Agent Management APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/queues/{queue_id}/agents` | List agents in queue |
| `POST` | `/queues/{queue_id}/agents` | Add agent to queue |
| `DELETE` | `/queues/{queue_id}/agents/{user_id}` | Remove agent from queue |

### Task Management APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tasks` | List all tasks in workbench |
| `GET` | `/tasks/{task_id}` | Get task details |
| `POST` | `/tasks/{task_id}/reassign` | Reassign task (supervisor override) |
| `POST` | `/tasks/{task_id}/escalate` | Force escalate task |
| `POST` | `/tasks/{task_id}/cancel` | Cancel task |
| `PUT` | `/tasks/{task_id}/sla` | Extend SLA deadline |

### Agent Management APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/agents` | List agents in workbench |
| `GET` | `/agents/{user_id}` | Get agent details |
| `GET` | `/agents/{user_id}/tasks` | List agent's tasks |
| `GET` | `/agents/{user_id}/performance` | Get agent performance metrics |
| `PUT` | `/agents/{user_id}/availability` | Update agent availability |
| `GET` | `/agents/{user_id}/skills` | Get agent skills |
| `PUT` | `/agents/{user_id}/skills` | Update agent skills |

### Scenario Deployment APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/scenarios` | List scenarios (deployed and pending) |
| `GET` | `/scenarios/{scenario_id}` | Get scenario details |
| `POST` | `/scenarios/{scenario_id}/deploy` | Deploy scenario to production |
| `POST` | `/scenarios/{scenario_id}/activate` | Activate scenario |
| `POST` | `/scenarios/{scenario_id}/deactivate` | Deactivate scenario |
| `GET` | `/scenarios/{scenario_id}/task-mappings` | Get task-to-queue mappings |
| `PUT` | `/scenarios/{scenario_id}/task-mappings` | Update task-to-queue mappings |

### SLA Monitoring APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/sla/at-risk` | List at-risk requests |
| `GET` | `/sla/breached` | List SLA-breached requests |
| `GET` | `/sla/metrics` | Get SLA compliance metrics |

### Request Management APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/requests` | List all requests |
| `GET` | `/requests/{request_id}` | Get request details |
| `POST` | `/requests/{request_id}/cancel` | Cancel request |
| `GET` | `/requests/{request_id}/escalations` | Get escalation history |

### Checklist APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/checklists` | List checklists |
| `POST` | `/checklists` | Create checklist |
| `GET` | `/checklists/{checklist_id}` | Get checklist |
| `PUT` | `/checklists/{checklist_id}` | Update checklist |
| `GET` | `/checklists/{checklist_id}/assignments` | Get checklist assignments |
| `POST` | `/checklists/{checklist_id}/assign` | Assign checklist to agents |

### Routine APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/routines` | List routines |
| `POST` | `/routines` | Create routine |
| `GET` | `/routines/{routine_id}` | Get routine |
| `PUT` | `/routines/{routine_id}` | Update routine |
| `POST` | `/routines/{routine_id}/assign` | Assign routine to agents |

### Analytics APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/analytics/throughput` | Get throughput metrics |
| `GET` | `/analytics/efficiency` | Get efficiency metrics |
| `GET` | `/analytics/queue-health` | Get queue health dashboard data |

---

## Auditor REST Channel

**Base Path:** `/api/auditor/v1`

| Aspect | Description |
|--------|-------------|
| **Persona** | [Auditor](../../08-personas-and-journeys/personas/auditor.md) |
| **Scope** | Tenant or Workbench |
| **Purpose** | Compliance review and investigation |

### Decision Audit APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/decisions` | Search decisions |
| `GET` | `/decisions/{decision_id}` | Get decision record |
| `GET` | `/decisions/{decision_id}/evidence` | Get decision evidence |
| `GET` | `/decisions/{decision_id}/trail` | Get full audit trail |

### Request Audit APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/requests` | Search requests for audit |
| `GET` | `/requests/{request_id}` | Get request audit view |
| `GET` | `/requests/{request_id}/decisions` | Get all decisions in request |
| `GET` | `/requests/{request_id}/actors` | Get all actors involved |
| `GET` | `/requests/{request_id}/timeline` | Get complete timeline |

### Agent Audit APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/agents/{user_id}/decisions` | Get agent's decision history |
| `GET` | `/agents/{user_id}/activity` | Get agent activity log |

### Compliance Report APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/reports/compliance` | Get compliance summary |
| `GET` | `/reports/exceptions` | Get policy exceptions |
| `GET` | `/reports/sla-compliance` | Get SLA compliance report |

### Export APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/export/decisions` | Export decision records |
| `POST` | `/export/audit-trail` | Export audit trail for request |

---

## Data Plane Channel

---

## Business User REST Channel

**Base Path:** `/api/business/v1`

| Aspect | Description |
|--------|-------------|
| **Purpose** | Request initiation and updates for business domain actors |
| **Scope** | Scenario-specific within a Workbench |
| **Access** | Business domain actors (Customer, Employee, System) |

### Personas Served

| Persona | Description |
|---------|-------------|
| [**Business Customer**](../../08-personas-and-journeys/personas/business-domain/business-customer.md) | End customer self-serve |
| [**Business Employee**](../../08-personas-and-journeys/personas/business-domain/business-employee.md) | Employee-assisted requests |
| [**Business System Actor**](../../08-personas-and-journeys/personas/business-domain/business-system-actor.md) | System integrations |

### Request APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/scenarios` | List available scenarios |
| `GET` | `/scenarios/{scenario_id}` | Get scenario info (for request initiation) |
| `POST` | `/requests` | Initiate a new request |
| `GET` | `/requests` | List my requests |
| `GET` | `/requests/{request_id}` | Get request status |
| `GET` | `/requests/{request_id}/timeline` | Get request progress timeline |

### Request Update APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/requests/{request_id}/updates` | Send update to request |
| `POST` | `/requests/{request_id}/documents` | Upload document to request |
| `GET` | `/requests/{request_id}/documents` | List request documents |
| `GET` | `/requests/{request_id}/documents/{doc_id}` | Download document |

### Subject Task APIs (Self-Serve)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tasks` | List tasks assigned to me (as subject) |
| `GET` | `/tasks/{task_id}` | Get task details |
| `POST` | `/tasks/{task_id}/complete` | Complete subject task |
| `POST` | `/tasks/{task_id}/documents` | Upload document for task |

### Notification APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/notifications` | List my notifications |
| `GET` | `/notifications/{notification_id}` | Get notification details |
| `PUT` | `/notifications/{notification_id}/read` | Mark as read |
| `GET` | `/preferences/notifications` | Get notification preferences |
| `PUT` | `/preferences/notifications` | Update notification preferences |

### Knowledge APIs (Limited)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/knowledge/faqs` | Get FAQs |
| `GET` | `/knowledge/articles` | Search help articles |
| `GET` | `/knowledge/articles/{article_id}` | Get article |

### Profile APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/profile` | Get my profile |
| `PUT` | `/profile` | Update profile |
| `GET` | `/profile/preferences` | Get preferences |
| `PUT` | `/profile/preferences` | Update preferences |

---

## Access Control

### Scope Headers

All requests include scope context:

```http
X-Tenant-ID: acme-bank
X-Subscription-ID: sub-prod-001
X-Workbench-ID: dispute-ops        # For workbench-scoped channels
```

### Authorization Model

| Channel | Authorization |
|---------|---------------|
| **Tenant Admin** | Tenant admin role required |
| **Creator** | Workbench designer role required |
| **Agent** | Agent role + workbench enrollment |
| **Supervisor** | Supervisor role + workbench assignment |
| **Business User** | OPA policy per scenario self-serve config |
| **Auditor** | Auditor role + scope-specific permissions |

### Rate Limiting

| Channel | Default Limits |
|---------|----------------|
| **Tenant Admin** | 100 req/min |
| **Creator** | 200 req/min |
| **Agent** | 500 req/min |
| **Supervisor** | 300 req/min |
| **Business User** | 100 req/min per user |
| **Auditor** | 200 req/min |

---

## Versioning

- APIs are versioned in the path (e.g., `/api/agent/v1`, `/api/agent/v2`)
- Breaking changes require new version
- Deprecated versions supported for 12 months

---

## Related Documentation

- [MCP Channels](./mcp-channels.md) — MCP-based access for AI assistants
- [Heracles Gateway](../../05-infrastructure/heracles-gateway.md) — API Gateway
- [Personas and Journeys](../../08-personas-and-journeys/README.md) — Persona details

---

*TODO: OpenAPI specifications, detailed request/response schemas, webhook APIs*

