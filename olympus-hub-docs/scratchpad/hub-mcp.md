# Hub MCP Server Design: Brainstorming

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17  
> **Purpose:** Brainstorm how Hub can expose MCP Servers per workbench to enable users to use Hub capabilities via their personal AI agents

---

## Problem Statement

**Goal:** Enable business users to interact with Hub capabilities through their personal AI agents (ChatGPT, Claude, Gemini, custom agents) using MCP (Model Context Protocol).

**Key Requirements:**
1. **MCP is a Channel** — persona-focused, like Web Console or MS Teams
2. **Multiple MCP Servers per Persona per Workbench** — Developers can publish multiple MCP Servers to segregate:
   - Functional boundaries (e.g., payments vs. disputes)
   - Privilege boundaries (e.g., read-only vs. write access)
   - Business-needs influenced reasons
3. **Request Initiation Tools** — MCP Server publishes tools to create Service Requests, Business Requests, and System Requests
4. **Request Participation Tools** — MCP Server publishes tools to interact with existing requests (query status, send updates, upload documents, etc.)
5. **Tools Mirror REST APIs** — MCP tools should mirror the REST APIs available for business users (`/api/business/v1`)
6. **Request Initiation vs. Participation** — These are distinct concerns with different tool sets
7. **Prompt Guidance** — MCP server can push prompts to guide subsequent AI agent calls
8. **Streaming Updates** — Request updates are streamed to the AI agent

**Important:** Each request type (Service/Business/System) is associated with distinct scenarios, but the MCP tools are about **request operations**, not scenario operations. The scenario is the backend that processes the request.

---

## MCP Constructs Overview

MCP (Model Context Protocol) provides constructs mapped to Hub capabilities for both Business Users and Collaborators:

### Business User Mappings

| MCP Construct | Purpose | Hub Mapping |
|---------------|---------|-------------|
| **Tools** | Request & Task Operations | **Request Initiation**: create_service_request, create_business_request, create_system_request<br/>**Request Query**: list_active_requests, list_historic_requests, get_request_status, get_request_timeline<br/>**Request Participation**: send_request_update, upload_document, list_documents, download_document<br/>**Task Operations**: list_my_tasks, get_task_details, complete_task, upload_task_document<br/>**Authority Management**: update_authority_request, get_authority_request_status |
| **Prompts** | Task Solving Guidance | **Prompt Templates**: Developer-defined prompt templates for each task type (referenced from Scenario), structured for MCP Router list-prompts response, compiled with full request context when client requests |
| **Resources** | Request Tracking | **Request Resources**: Each request exposed as resource (e.g., `request://REQ-123`) containing all data available to subscribing user<br/>**Resource Lifecycle**: Managed by MCP Channel (subscribe, unsubscribe, notifications on changes) |
| **Notifications** | Real-time Updates | Request/task/authority notifications sent via JSON-RPC notifications |
| **Resource Subscriptions** | Update Subscriptions | Client subscribes to request resources; server sends `notifications/resources/updated` when request changes<br/>**Session-bound**: Subscriptions are MCP-session bound (cannot persist beyond session) |

### Collaborator Mappings

| MCP Construct | Supervisor | Agent | Creator | Admin | Auditor |
|---------------|------------|-------|---------|-------|---------|
| **Tools** | Queue mgmt, SLAs, directability, feedback | Task processing, knowledge, directability | Scenario design, knowledge mgmt, feedback inbox | Subscription mgmt, resources | Decision investigation, compliance |
| **Prompts** | Queue analysis, escalation handling | Task solver prompts (per task type) | Design guides, feedback triage | Resource optimization | Investigation guides |
| **Resources** | Queues, escalations, SLA alerts | Tasks, requests | Scenarios, feedback | Workbenches | Audit trails |
| **Notifications** | Queue updates, SLA breaches | Task assignments, updates | Scenario changes, feedback | Resource alerts | None (on-demand) |

---

## Hub Concepts to Map

### Core Concepts

| Hub Concept | Description | MCP Mapping |
|-------------|-------------|-------------|
| **Workbench** | Domain operational environment | MCP Server scoped to Workbench (except admin-template which is tenant-scoped) |
| **Persona** | User role | Implicit in MCP Server template kind (e.g., `business-user-template`, `supervisor-template`); access control via OPA policy |
| **Scenario** | Operational situation that processes requests | **Backend** — not directly exposed as tool; request initiation tools create requests that activate scenarios |
| **Request Type** | Service Request, Business Request, System Request | **Request Initiation Tools** — one tool per request type |
| **Request** | Runtime instance of work | **Request Participation Tools** — tools to interact with existing requests |
| **Request Update** | Append-only history entry | **Resource subscriptions** — real-time updates via JSON-RPC notifications |
| **Task** | Unit of work assigned to agent | **Task Tools** (Agent/Supervisor templates) — claim, complete, abandon, reassign |
| **Queue** | Task routing construct | **Queue Tools** (Supervisor template) — metrics, balancing, reassignment |
| **Knowledge** | SOPs, policies, decision criteria | **Knowledge Tools** (Agent/Creator templates) — search, retrieve, manage |
| **Escalation** | Directability task from AI rejection | **Directability Tools** (Agent/Supervisor templates) — acknowledge, override, retry |
| **Feedback** | Production-to-development signals | **Feedback Tools** — promote (Agent/Supervisor), inbox (Creator) |
| **Channel** | Interaction interface | MCP is a Channel type (like REST, Web Console) |

### Existing Patterns

| Pattern | Description | Relevance |
|---------|-------------|-----------|
| **REST Channels** | Persona-scoped REST APIs (e.g., `/api/business/v1`) | **MCP Tools should mirror REST APIs** — same operations, different protocol |
| **MCP Channels** | Persona-scoped MCP access (already exists) | How do MCP Servers relate to MCP Channels? |
| **Request Updates** | Append-only history with streaming | Resource subscriptions for real-time updates |
| **Request Types** | Service/Business/System Request classification | **Request Initiation Tools** — one tool per request type |

---

## Design Questions

### Q1: MCP Server Scope and Identity

**Question:** What is the scope and identity of an MCP Server in Hub?

**Options:**
- **Option A:** One MCP Server per Workbench per Persona
  - Simple, one-to-one mapping
  - All scenarios in workbench exposed in one server
  - **Problem:** Cannot segregate by functional/privilege boundaries
  
- **Option B:** Multiple MCP Servers per Workbench per Persona
  - Developer can create multiple servers (e.g., `payments-mcp-server`, `disputes-mcp-server`)
  - Each server can expose different scenarios
  - **Problem:** How to manage server discovery? How to route?

- **Option C:** MCP Server as a first-class Hub concept (like Scenario, Tool)
  - Defined via CRD: `MCPServer` resource
  - Scoped to Workbench + Persona
  - Can reference multiple Scenarios
  - **Problem:** New concept to introduce

**Decision:** Option C — MCP Server as first-class concept (CRD-based)

**Design:**
- Defined via CRD: `business-user-template` (or other persona-specific template kinds)
- Template kind implies persona (no explicit persona field)
- Scoped to Workbench
- Access control via OPA policy (evaluates access token claims, scopes, delegation-templates)
- Can reference multiple Scenarios

**Rationale:**
- Aligns with requirement: "Developer may choose to publish multiple MCP Servers"
- Enables segregation by functional/privilege boundaries via OPA policies
- Consistent with Hub's pattern of explicit configuration (CRDs)

---

### Q2: Request Initiation Tools

**Question:** How do Request Initiation Tools work?

**Request Types:**
- **Service Request** — Customer-facing work (always has customer subject)
- **Business Request** — Business operations (optional subject)
- **System Request** — System/data integrity issues (optional subject)

**MCP Tool Mapping:**
- **Option A:** One tool per request type
  - `create_service_request(scenario_id, subject_id, payload)`
  - `create_business_request(scenario_id, payload)`
  - `create_system_request(scenario_id, payload)`
  - **Pros:** Clear separation, mirrors REST API structure
  - **Cons:** Three separate tools

- **Option B:** Single tool with request_type parameter
  - `create_request(request_type, scenario_id, payload)`
  - **Pros:** One tool, fewer tools
  - **Cons:** Less discoverable, parameter-heavy

**REST API Reference:** `/api/business/v1/requests` (POST)

**Initial Direction:** Option A — one tool per request type (mirrors REST API structure)

**Flow:**
1. AI agent calls `create_service_request(scenario_id="dispute-filing", subject_id="CUST-123", payload={...})`
2. MCP Server maps to REST API: `POST /api/business/v1/requests`
3. Request created, Scenario activated (via implicit Trigger)
4. Request ID returned to AI agent
5. AI agent can use Request Participation Tools to interact with the request

**Note:** When scenarios are included in MCP Server CRD, corresponding requests are automatically included. No need to specify request_type - it's derived from the scenario.

---

### Q3: Request Participation Tools

**Question:** What tools are needed to interact with existing requests?

**REST API Reference:** `/api/business/v1/requests/{request_id}/*`

**Required Tools (mirroring REST APIs):**

| REST API | MCP Tool | Description |
|----------|----------|-------------|
| `GET /requests` | `list_my_requests(filters?)` | List user's requests |
| `GET /requests/{id}` | `get_request_status(request_id)` | Get request status and details |
| `GET /requests/{id}/timeline` | `get_request_timeline(request_id)` | Get request progress timeline |
| `POST /requests/{id}/updates` | `send_request_update(request_id, update_type, payload)` | Send update to request |
| `POST /requests/{id}/documents` | `upload_document(request_id, document)` | Upload document to request |
| `GET /requests/{id}/documents` | `list_request_documents(request_id)` | List request documents |
| `GET /requests/{id}/documents/{doc_id}` | `download_document(request_id, doc_id)` | Download document |

**Design Questions:**
- Should all REST endpoints have corresponding MCP tools?
- How to handle pagination (list_my_requests)?
- How to handle file uploads (upload_document)?

**Decision:**
- Mirror all Business User REST APIs as MCP tools
- **Pagination**: Cursor-based (returns next cursor, client passes to next call)
- **File uploads**: Base64 encoding (other mechanisms may be considered later)

---

### Q4: Request Context Management

**Question:** How does the AI agent maintain context about which Request(s) it's working on?

**Options:**
- **Option A:** Request ID passed as parameter to all tools
  - Explicit but verbose
  - `get_request_status(request_id="REQ-123")`
  - `send_request_update(request_id="REQ-123", ...)`
  - **Pros:** Clear, stateless
  - **Cons:** Verbose, agent must remember request_id

- **Option B:** MCP Server maintains "active request" context
  - Simpler tool calls: `get_request_status()` (no request_id needed)
  - **Problem:** What if agent works on multiple requests?
  - **Pros:** Simpler API
  - **Cons:** Stateful, doesn't support multiple concurrent requests

- **Option C:** Request ID in MCP session metadata + explicit parameter
  - Session can have multiple "active" requests
  - Tools can reference by request_id or use "current" request
  - **Pros:** Supports multiple requests, flexible
  - **Cons:** More complex

**Initial Direction:** Option A — explicit request_id parameter (stateless, clear, mirrors REST API)

---

### Q5: MCP Prompts for Guidance

**Question:** How do MCP Prompts guide subsequent AI agent calls?

**Decision:**
- **Task solver prompts**: Essential and highly recommended
- **Other prompts** (progress, errors, guidance): At developer/PA discretion
- **Push vs. Available**: Only list for now (no server push)
  - *Aside: Can MCP server push prompts? TBD — may be explored in future.*

**MCP Prompt Templates:**
- Parameterized prompt templates
- Structured for semantic/structural equivalence with MCP Router list-prompts response
- Available via `prompts/list()` — client pulls, server does not push
- Compiled with request context when client requests them

**Prompt Categories:**
| Category | Required? | Description |
|----------|-----------|-------------|
| **Task Solver Prompts** | Essential (highly recommended) | Guidance for completing specific task types |
| **Scenario Guidance** | Optional (developer discretion) | How to use this scenario |
| **Progress/Status** | Optional (developer discretion) | What's happening, what to expect |
| **Error Handling** | Optional (developer discretion) | What went wrong, how to fix |
| **Next Actions** | Optional (developer discretion) | What to do next for this request |

**Design:**
- Prompt templates are available in prompt catalog (via `prompts/list()`)
- Scenario defines prompt templates (per task type, associated with trigger)
- MCP Server CRD references prompt templates as `prompt_templates`
- Prompt template structure must match MCP Router list-prompts response format
- Request context used to compile prompt templates when client requests them

---

### Q6: Request Resources and Subscriptions

**Question:** How are requests exposed as resources and how do clients subscribe to updates?

**Design:**
- **Each request is exposed as a resource** (e.g., `request://REQ-123`)
- **Resource contains all data** available to the subscribing user (status, timeline, documents, etc.)
- **MCP Channel manages complete resource lifecycle** (create, update, delete, subscribe, unsubscribe)

**Resource Subscription:**
- Client subscribes via: `resources/subscribe("request://REQ-123")`
- **Session-bound**: Subscriptions are MCP-session bound (cannot persist beyond session)
  - MCP protocol does not support persistent subscriptions
  - All subscriptions cleared on session disconnect
  - Client must re-subscribe on reconnection
- Server sends `notifications/resources/updated` when request changes
- Client calls `resources/read("request://REQ-123")` to fetch updated data
  - Resource contains all data available to subscribing user (status, timeline, documents, etc.)
- Client can unsubscribe via: `resources/unsubscribe("request://REQ-123")`

**Resource Lifecycle (Managed by MCP Channel):**
- Resource created when request is created (or when user first accesses it)
- Resource updated when Request Update occurs
- Resource deleted when request is completed/cancelled (or after retention period)
- MCP Channel manages all lifecycle operations (create, update, delete, subscribe, unsubscribe)

**Resource Discovery:**
- Client discovers available requests via `list_active_requests()` and `list_historic_requests()` tools
- Resources automatically available for requests user has access to
- Client can subscribe to multiple requests (multiple subscriptions per MCP session)
- Resources include requests created through other channels (not just MCP)

---

### Q7: MCP Server vs. MCP Channel

**Question:** How do MCP Servers relate to existing MCP Channels?

**Decision:** MCP Server is a **configuration layer** (Workbench-scoped CRD). MCP Channel is a **platform service**.

**Architecture:**
```
┌─────────────────────────────────────────────────────────────────┐
│                 MCP Channel (Platform Service)                  │
│  - Handles transport, protocol, authentication                 │
│  - Exposes directory for collaborators (NOT for MCP Clients)   │
│  - Routes requests to appropriate endpoints                    │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │ MCP Operator provisions endpoints
                              │ based on CRD
                              │
┌─────────────────────────────────────────────────────────────────┐
│               MCP Server CRD (Workbench-scoped Config)          │
│  - Defines scenarios, tools, prompt templates                  │
│  - OPA-based access control                                    │
│  - Session configuration                                       │
└─────────────────────────────────────────────────────────────────┘
```

**Key Points:**
- **MCP Server CRD**: Configuration layer, scoped to a Workbench
- **MCP Channel**: Platform service providing infrastructure
- **MCP Operator**: Provisions endpoints at MCP Channel based on CRD
- **Directory**: MCP Channel exposes directory for **collaborators** (not MCP Clients)
- **Client Configuration**: Clients are **injected** MCP server configuration based on directory info

---

### Q8: Multiple MCP Servers Discovery

**Question:** How does an AI agent discover and select which MCP Server to use?

**Decision:** Directory for collaborators; Clients are injected configuration.

**Design:**
- Hub MCP Channel exposes a **directory** of available MCP Servers
- Directory is for **collaborators** (Supervisors, Developers, Admins) — NOT for MCP Clients
- MCP Clients are **injected** server configuration based on directory information
- Client does not discover servers; it's given configuration by the system

**Scenario:** Workbench has multiple MCP Servers:
- `payments-mcp-server` (exposes payment scenarios)
- `disputes-mcp-server` (exposes dispute scenarios)
- `read-only-mcp-server` (exposes query-only scenarios)

**Considered Options (for reference):**
- **Option A:** AI agent connects to workbench MCP endpoint, gets list of servers
  - MCP Router returns available servers
  - Agent selects server(s) to use
  - **Pros:** Explicit selection

- **Option B:** All servers exposed as one unified tool catalog
  - MCP Router aggregates tools from all servers
  - Agent sees all tools, doesn't need to select servers
  - **Pros:** Simpler for agent
  - **Cons:** Loses server boundaries

- **Option C:** Server selection via MCP connection parameters
  - Agent connects to `/mcp/{workbench}/{server-name}`
  - **Pros:** Explicit routing
  - **Cons:** Agent must know server names

**Initial Direction:** Option A — explicit server discovery and selection

---

## Proposed Architecture

### MCP Server CRD (C2-Level Overview)

**Key Design Principles:**
- **Template-based**: Uses `business-user-template` kind (persona implicit in template)
- **Scenario-based exposure**: When scenarios are included, corresponding requests are automatically included
- **OPA-based access control**: Access limited via OPA policies using access token claims, scopes, delegation-templates
- **MCP-compatible prompts**: Prompt templates structured for semantic/structural equivalence with MCP Router list-prompts response

**CRD Structure (Conceptual):**

```yaml
apiVersion: hub.olympus.io/v1
kind: business-user-template  # Template kind implies persona
metadata:
  name: payments-mcp-server
  namespace: acme-bank
spec:
  # Server identity
  server:
    name: payments-mcp-server
    display_name: "Payments MCP Server"
    description: "MCP server for payment-related request operations"
    version: "1.0.0"
  
  # Workbench scope
  workbench_ref: payments-workbench
  
  # Scenarios to expose
  # When scenarios are included, corresponding requests are automatically included
  # No need to specify request_type - it's derived from scenario
  exposed_scenarios:
    - scenario_ref: bill-payment
    - scenario_ref: recurring-payment
  
  # Prompt templates
  # Structure must be semantically/structurally equivalent to MCP Router list-prompts response
  prompt_templates:
    # Task solver prompts (referenced from Scenario definitions)
    - name: verify_kyc_documents_solver
      scenario_ref: bill-payment
      task_type: verify_kyc_documents
      # Template structure matches MCP prompt format
      # (exact structure TBD - must match MCP Router output)
    
    # General guidance prompts
    - name: how_to_initiate_request
      description: "Guidance on how to initiate a request"
      # Template structure matches MCP prompt format
  
  # Access control via OPA policy
  # Policy uses access token claims, scopes, delegation-templates, etc.
  access_policy:
    # OPA Rego policy
    # Evaluates against access token claims, user profile, etc.
    # (exact policy structure TBD - C3 level detail)
  
  # Session configuration
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50  # Maximum concurrent resource subscriptions per session
```

**Key Points:**
- **Template kind** (`business-user-template`) implies persona - no explicit persona field
- **Scenarios** automatically include their requests - no request_type specification needed
- **Prompt templates** structure must match MCP Router's list-prompts response format
- **Access control** via OPA policy, not persona field
- **Detailed schemas** (C3/C4 level) to be defined later

---

## Collaborator MCP Server Templates

Beyond Business Users, Hub exposes MCP Servers to **Collaborators** — personas who configure, operate, or administer Hub capabilities. Each collaborator persona has a corresponding template kind.

### Template Kinds Overview

| Template Kind | Persona(s) | Plane | Primary Purpose |
|---------------|------------|-------|-----------------|
| `business-user-template` | Business Customer, Business Employee, Business System | Data | Request initiation & participation |
| `supervisor-template` | Supervisor | Control | Queue management, agent oversight, SLAs |
| `agent-template` | Agent (Human/AI) | Control | Task processing, knowledge access |
| `creator-template` | Process Architect, Developer | Control | Scenario design, development, testing |
| `admin-template` | Administrator | Control | Subscription/resource management |
| `auditor-template` | Auditor | Control | Compliance, investigation, reporting |

---

### Supervisor MCP Server Template

**Purpose:** Enable AI assistants to help Supervisors manage operations.

**CRD Structure (Conceptual):**

```yaml
apiVersion: hub.olympus.io/v1
kind: supervisor-template
metadata:
  name: operations-supervisor-mcp
  namespace: acme-bank
spec:
  server:
    name: operations-supervisor-mcp
    display_name: "Operations Supervisor MCP"
    version: "1.0.0"
  
  workbench_ref: payments-workbench
  
  # Scopes to expose (Supervisor can see all scenarios in workbench)
  # By default: all scenarios in workbench; can be filtered
  scenario_scope: all  # or list specific scenarios
  
  # Capabilities to expose
  capabilities:
    queue_management: true      # Queue metrics, reassignment
    agent_oversight: true       # Agent status, availability, workload
    sla_monitoring: true        # SLA status, alerts, escalations
    directability: true         # Handle escalation tasks
    feedback_promotion: true    # Promote feedback to dev workbenches
    reporting: true             # Generate reports
  
  # Prompt templates
  prompt_templates:
    - name: queue_analysis
      description: "Analyze queue health and recommend actions"
      category: guidance
    - name: escalation_handling
      description: "Guide through escalation resolution"
      category: task_solver
  
  access_policy:
    # OPA policy for Supervisor role
  
  session:
    inactivity_timeout: 60m
    max_subscriptions: 100
```

**Default Tools (Supervisor):**

| Category | Tools |
|----------|-------|
| **Queue Management** | `get_queue_metrics`, `list_queues`, `reassign_task`, `balance_queues` |
| **Agent Oversight** | `list_agents`, `get_agent_status`, `get_agent_workload`, `set_agent_availability` |
| **SLA Monitoring** | `get_sla_status`, `list_sla_breaches`, `list_at_risk_requests` |
| **Directability** | `acknowledge_escalation`, `override_decision`, `change_context_rerun`, `reassign_for_retry`, `fail_scenario` |
| **Feedback** | `promote_feedback`, `list_promoted_feedback`, `get_feedback_status` |
| **Reporting** | `generate_daily_report`, `get_performance_summary` |
| **Request Visibility** | `list_requests`, `get_request_status`, `get_request_timeline` |

**Resources (Supervisor):**
- Queues as resources (`queue://{queue_id}`) — subscribe for real-time queue updates
- Escalations as resources (`escalation://{task_id}`) — subscribe for escalation updates
- SLA alerts as resources (`sla-alert://{alert_id}`)

---

### Agent MCP Server Template

**Purpose:** Enable AI assistants to help Agents (human or AI) process tasks.

**CRD Structure (Conceptual):**

```yaml
apiVersion: hub.olympus.io/v1
kind: agent-template
metadata:
  name: dispute-agent-mcp
  namespace: acme-bank
spec:
  server:
    name: dispute-agent-mcp
    display_name: "Dispute Agent MCP"
    version: "1.0.0"
  
  workbench_ref: disputes-workbench
  
  # Task queues this agent can work (optional - filter from agent's enrollment)
  task_queue_scope:
    - dispute-triage-queue
    - dispute-resolution-queue
  
  # Capabilities
  capabilities:
    task_processing: true       # Claim, work, complete tasks
    knowledge_access: true      # Query knowledge base
    tool_invocation: true       # Invoke registered tools
    decision_recording: true    # Record decisions, thoughts
    directability: true         # Handle escalation tasks
    feedback_promotion: true    # Promote feedback
  
  prompt_templates:
    - name: dispute_triage_solver
      description: "Guide through dispute triage task"
      category: task_solver
      task_type: dispute_triage
    - name: evidence_review_solver
      description: "Guide through evidence review task"
      category: task_solver
      task_type: evidence_review
  
  access_policy:
    # OPA policy for Agent role + queue enrollment
  
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50
```

**Default Tools (Agent):**

| Category | Tools |
|----------|-------|
| **Task Processing** | `list_my_tasks`, `get_task`, `claim_task`, `complete_task`, `abandon_task` |
| **Decision Recording** | `add_thought`, `add_memo`, `record_decision`, `add_evidence_review` |
| **Knowledge Access** | `search_knowledge`, `get_sop`, `get_policy`, `get_decision_criteria` |
| **Tool Invocation** | `list_available_tools`, `invoke_tool` |
| **Directability** | `acknowledge_escalation`, `override_decision`, `change_context_rerun` |
| **Request Context** | `get_request`, `get_request_timeline`, `get_related_entities` |

**Resources (Agent):**
- Tasks as resources (`task://{task_id}`) — subscribe for task updates
- Requests as resources (`request://{request_id}`) — subscribe for request updates

---

### Creator MCP Server Template

**Purpose:** Enable AI assistants to help Process Architects and Developers design and build.

**CRD Structure (Conceptual):**

```yaml
apiVersion: hub.olympus.io/v1
kind: creator-template
metadata:
  name: scenario-design-mcp
  namespace: acme-bank
spec:
  server:
    name: scenario-design-mcp
    display_name: "Scenario Design MCP"
    version: "1.0.0"
  
  workbench_ref: disputes-workbench
  
  # Creator capabilities
  capabilities:
    scenario_design: true       # Query, draft, validate scenarios
    knowledge_management: true  # Manage knowledge base
    trigger_testing: true       # Test trigger configurations
    application_debugging: true # Debug Hub Applications
    feedback_inbox: true        # Receive/process feedback from production
  
  prompt_templates:
    - name: scenario_design_guide
      description: "Guide through scenario design best practices"
      category: guidance
    - name: trigger_configuration_help
      description: "Help configure triggers for a scenario"
      category: guidance
    - name: feedback_triage_guide
      description: "Guide through triaging production feedback"
      category: guidance
  
  access_policy:
    # OPA policy for PA/Developer roles
  
  session:
    inactivity_timeout: 120m  # Longer for design work
    max_subscriptions: 50
```

**Default Tools (Creator):**

| Category | Tools |
|----------|-------|
| **Scenario Design** | `list_scenarios`, `get_scenario`, `create_scenario_draft`, `validate_scenario`, `get_scenario_diff` |
| **Knowledge Management** | `list_knowledge_items`, `create_knowledge_draft`, `update_knowledge`, `link_knowledge_to_scenario` |
| **Trigger Configuration** | `list_triggers`, `test_trigger`, `get_trigger_matches`, `debug_trigger` |
| **Application Development** | `list_applications`, `get_application_logs`, `debug_application`, `invoke_application_test` |
| **Feedback Inbox** | `list_feedback_inbox`, `get_feedback_details`, `accept_feedback`, `reject_feedback`, `resolve_feedback` |
| **Validation** | `validate_sop`, `check_scenario_coverage`, `lint_configuration` |

**Resources (Creator):**
- Scenarios as resources (`scenario://{scenario_id}`) — subscribe for scenario changes
- Feedback items as resources (`feedback://{feedback_id}`) — subscribe for feedback updates

---

### Admin MCP Server Template

**Purpose:** Enable AI assistants to help Administrators manage subscription and resources.

**CRD Structure (Conceptual):**

```yaml
apiVersion: hub.olympus.io/v1
kind: admin-template
metadata:
  name: tenant-admin-mcp
  namespace: acme-bank-system
spec:
  server:
    name: tenant-admin-mcp
    display_name: "Tenant Administration MCP"
    version: "1.0.0"
  
  # Scoped to tenant (not a specific workbench)
  tenant_scope: true
  
  capabilities:
    subscription_management: true   # View subscription status
    workbench_management: true      # List, create workbenches
    user_management: true           # List users, roles
    resource_monitoring: true       # Usage, budgets, quotas
    configuration_changes: true     # Initiate changes (with approval)
  
  prompt_templates:
    - name: resource_optimization
      description: "Analyze resource usage and suggest optimizations"
      category: guidance
    - name: user_access_review
      description: "Guide through user access review"
      category: guidance
  
  access_policy:
    # OPA policy for Administrator role
  
  session:
    inactivity_timeout: 30m
    max_subscriptions: 20
```

**Default Tools (Admin):**

| Category | Tools |
|----------|-------|
| **Subscription** | `get_subscription_status`, `get_subscription_limits`, `get_billing_summary` |
| **Workbench Management** | `list_workbenches`, `get_workbench`, `create_workbench`, `archive_workbench` |
| **User Management** | `list_users`, `get_user_roles`, `list_role_assignments` |
| **Resource Monitoring** | `get_usage_summary`, `get_quota_status`, `list_resource_alerts` |
| **Configuration** | `list_pending_changes`, `approve_change`, `reject_change` |

---

### Auditor MCP Server Template

**Purpose:** Enable AI assistants to help Auditors review compliance and investigate decisions.

**CRD Structure (Conceptual):**

```yaml
apiVersion: hub.olympus.io/v1
kind: auditor-template
metadata:
  name: compliance-auditor-mcp
  namespace: acme-bank
spec:
  server:
    name: compliance-auditor-mcp
    display_name: "Compliance Auditor MCP"
    version: "1.0.0"
  
  workbench_ref: all  # Cross-workbench access for auditors
  
  capabilities:
    decision_investigation: true  # Review decisions, rationale
    compliance_reporting: true    # Compliance metrics, reports
    audit_trail_access: true      # Full audit trail access
    evidence_collection: true     # Collect evidence for audits
  
  prompt_templates:
    - name: decision_investigation_guide
      description: "Guide through investigating a specific decision"
      category: guidance
    - name: compliance_report_generator
      description: "Generate compliance report for a period"
      category: guidance
  
  access_policy:
    # OPA policy for Auditor role
  
  session:
    inactivity_timeout: 60m
    max_subscriptions: 100
```

**Default Tools (Auditor):**

| Category | Tools |
|----------|-------|
| **Decision Investigation** | `get_decision`, `get_decision_rationale`, `get_decision_context`, `trace_decision_chain` |
| **Audit Trail** | `get_request_audit_trail`, `get_entity_history`, `search_audit_logs` |
| **Compliance Reporting** | `get_compliance_metrics`, `generate_compliance_report`, `list_policy_violations` |
| **Evidence Collection** | `export_request_evidence`, `create_audit_snapshot`, `list_related_requests` |

---

## MCP Channel Capabilities for Collaborators

### Directory Service

MCP Channel exposes a **Directory Service** for collaborators to discover available MCP Servers:

**Purpose:** Collaborators (not MCP Clients) browse available MCP Servers.

**Tools:**

| Tool | Description | Available To |
|------|-------------|--------------|
| `list_mcp_servers` | List all MCP Servers accessible to the collaborator | All Collaborators |
| `get_mcp_server_info` | Get details about a specific MCP Server | All Collaborators |
| `get_client_config` | Generate client configuration for an MCP Server | All Collaborators |

**Directory Entry Structure:**
```json
{
  "servers": [
    {
      "name": "payments-mcp-server",
      "display_name": "Payments MCP Server",
      "workbench": "payments-workbench",
      "template_kind": "business-user-template",
      "version": "1.0.0",
      "scenarios": ["bill-payment", "recurring-payment"],
      "endpoint": "mcp://hub.acme.io/payments/payments-mcp-server"
    }
  ]
}
```

**Client Injection:**
- Directory is for **collaborators** to browse and manage
- MCP Clients are **injected** configuration (not self-discovered)
- Injection mechanism depends on client type (Cursor, Claude Desktop, custom)

---

### Collaborator-Specific Capabilities

Beyond per-template tools, MCP Channel provides **shared capabilities** for collaborators:

| Capability | Description | Templates |
|------------|-------------|-----------|
| **Directability** | Handle escalation tasks from AI agent rejections | Agent, Supervisor |
| **Feedback Loop** | Promote feedback to dev, receive/process incoming feedback | Agent, Supervisor, Creator |
| **Knowledge Base** | Query and manage knowledge | Agent, Creator |
| **Notifications** | Real-time updates via resource subscriptions | All |
| **Cross-Workbench Access** | Auditors can access multiple workbenches | Auditor |
| **Configuration Management** | View/manage CRDs (per role permissions) | Supervisor, Creator, Admin |

---

### Configuration Management Tools (Collaborators)

Collaborators may need to view or manage MCP Server configurations:

| Tool | Description | Available To |
|------|-------------|--------------|
| `list_mcp_server_crds` | List MCP Server CRDs in workbench | Supervisor, Creator, Admin |
| `get_mcp_server_crd` | Get specific CRD details | Supervisor, Creator, Admin |
| `create_mcp_server_crd` | Create new MCP Server (draft) | Creator |
| `update_mcp_server_crd` | Update MCP Server configuration | Creator, Admin |
| `delete_mcp_server_crd` | Delete MCP Server | Admin |
| `validate_mcp_server_crd` | Validate CRD before applying | Creator |

---

### Cross-Template Resource Subscriptions

Collaborators can subscribe to resources across their access scope:

| Resource Type | URI Pattern | Templates |
|---------------|-------------|-----------|
| **Request** | `request://{request_id}` | All (per access) |
| **Task** | `task://{task_id}` | Agent, Supervisor |
| **Queue** | `queue://{queue_id}` | Supervisor |
| **Escalation** | `escalation://{task_id}` | Agent, Supervisor |
| **Scenario** | `scenario://{scenario_id}` | Creator |
| **Feedback** | `feedback://{feedback_id}` | Creator |
| **SLA Alert** | `sla-alert://{alert_id}` | Supervisor |
| **MCP Server** | `mcp-server://{server_name}` | Creator, Admin |

---

### MCP Server → MCP Channel Integration

```
AI Agent
  │
  ├─▶ MCP Router (Heracles)
  │     │
  │     ├─▶ Authenticate (JWT)
  │     ├─▶ Authorize (OPA)
  │     └─▶ Route to MCP Channel
  │
  └─▶ Business User MCP Channel
        │
        ├─▶ Discover MCP Servers (for workbench, filtered by OPA policy)
        │     └─▶ List: payments-mcp-server, disputes-mcp-server
        │
        └─▶ Connect to MCP Server
              │
              ├─▶ Tools (request initiation & participation)
              ├─▶ Prompt Templates (from server config, MCP-compatible structure)
              ├─▶ Resources (request data - one resource per request)
              └─▶ Notifications (request updates via JSON-RPC notifications & resource subscriptions)
```

### Request Initiation Flow

```
1. AI Agent calls tool: create_service_request(
     scenario_id="bill-payment",
     subject_id="CUST-123",
     payload={ bill_id: "BILL-123", amount: 100.00 }
   )
   │
2. MCP Server receives tool call
   │
3. MCP Server maps to REST API: POST /api/business/v1/requests
   │
4. MCP Server calls Business User REST API (via Heracles)
   │
5. REST API creates Request (Service Request type)
   │
6. Request activates Scenario (via implicit Trigger)
   │
7. Request ID returned to MCP Server
   │
8. MCP Server returns to AI Agent: { request_id: "REQ-456", status: "created" }
   │
9. AI Agent stores request_id for subsequent interactions
```

### Request Participation Flow

```
1. AI Agent calls tool: get_request_status(request_id="REQ-456")
   │
2. MCP Server receives tool call
   │
3. MCP Server maps to REST API: GET /api/business/v1/requests/REQ-456
   │
4. MCP Server calls Business User REST API (via Heracles)
   │
5. REST API returns request status
   │
6. MCP Server returns to AI Agent: { 
     request_id: "REQ-456",
     status: "IN_PROGRESS",
     scenario: "bill-payment",
     ...
   }
```

### Request Update Flow

```
1. AI Agent calls tool: send_request_update(
     request_id="REQ-456",
     update_type="additional_info",
     payload={ note: "Payment method updated" }
   )
   │
2. MCP Server receives tool call
   │
3. MCP Server maps to REST API: POST /api/business/v1/requests/REQ-456/updates
   │
4. MCP Server calls Business User REST API (via Heracles)
   │
5. REST API creates Request Update
   │
6. Signal Exchange dispatches update to observers
   │
7. Update confirmation returned to MCP Server
   │
8. MCP Server returns to AI Agent: { success: true, update_id: "UPD-789" }
```

### Request Update Notification Flow

```
1. Request Update occurs (e.g., TASK_CREATED)
   │
2. Signal Exchange dispatches to observers
   │
3. MCP Server (as observer) receives update
   │
4. MCP Server checks: Is this request subscribed to in active MCP session?
   │
5. If yes, MCP Server sends notification via resource subscription:
   │   notifications/resources/updated { uri: "request://REQ-456" }
   │   (Sent via SSE or chunked HTTP, depending on transport)
   │
6. AI Agent receives notification
   │
7. AI Agent calls resources/read("request://REQ-456") to fetch updated request data
   │
8. AI Agent can react to update (e.g., call get_request_status tool)
```

---

## Open Questions Summary

This section consolidates all open questions that need decisions or clarifications:

### All Questions Resolved ✅

| # | Question | Decision |
|---|----------|----------|
| 1 | **MCP Server ↔ MCP Channel Relationship** | MCP Server = config layer (Workbench-scoped CRD). MCP Channel = platform service. MCP Operator provisions endpoints at MCP Channel based on CRD. |
| 2 | **Multi-Server Discovery** | Hub MCP Channel exposes a directory for **collaborators** (not MCP Clients). Clients are **injected** MCP server configuration based on directory info. |
| 3 | **Pagination Strategy** | Cursor-based pagination |
| 4 | **File Upload Mechanism** | Base64 encoding (other mechanisms may be considered later) |
| 5 | **Prompts Beyond Task Solvers** | Task solver prompts are **essential and highly recommended**. Other prompts (progress, errors, guidance) at developer/PA discretion. |
| 6 | **Prompt "Push" Mechanism** | Only list prompts for now (no push). *Aside: Can MCP server push prompts? TBD.* |
| 7 | **Session Configuration** | `inactivity_timeout` + `max_subscriptions`. Other details deferred. |
| 8 | **CRD Structure** | Uses template kind, OPA-based access control, scenarios auto-include requests, prompt templates match MCP Router format |
| 9 | **Prompt Template Structure** | See "Prompt Template Format" section below for examples |
| 10 | **Collaborator MCP Server Templates** | Six template kinds: `business-user-template`, `supervisor-template`, `agent-template`, `creator-template`, `admin-template`, `auditor-template` |
| 11 | **MCP Channel Capabilities for Collaborators** | Directory service (for collaborators), configuration management tools, cross-template resource subscriptions, directability, feedback loop |

### Deferred to C3/C4 (Not Blocking C2 Design)

| Topic | Note |
|-------|------|
| Exact OPA policy structure | Rego policy format — C3 detail |
| REST API payload mapping | Tool parameters → REST — C3 detail |
| Exact tool parameter schemas | Per-template tool definitions — C3 detail |
| Client injection mechanism | How clients receive MCP Server config — C3 detail |

---

## Detailed Open Questions

### Q9: Request Query Tools (Active + Historic)

**Question:** How do clients query both active and historic requests?

**Design:**
- **Separate tools** for active vs historic requests
- **Default tools** automatically available based on exposed scenarios in MCP Server CRD

**Tools:**
- `list_active_requests(filters, cursor?)` — List active requests for exposed scenarios
  - Filters: scenario_id, status, subject_id, date_range, etc.
  - Returns: IN_PROGRESS, PENDING, ASSIGNED, ON_HOLD requests
  - Pagination: Cursor-based (returns `next_cursor`, pass to subsequent call)
  
- `list_historic_requests(filters, cursor?)` — List completed/cancelled requests
  - Same filters as active requests
  - Returns: COMPLETED, CANCELLED requests
  - Pagination: Cursor-based

- `get_request_status(request_id)` — Get current status of any request (active or historic)

- `get_request_timeline(request_id)` — Get timeline of any request (active or historic)

**Default Behavior:**
- Tools automatically filter by scenarios exposed in MCP Server CRD
- User only sees requests they have access to (based on OPA policy evaluation)
- Both active and historic requests are queryable

### Q10: Scenario Discovery for Request Initiation

**Question:** How does the AI agent discover which scenarios are available for request initiation?

**REST API Reference:** `/api/business/v1/scenarios` (GET)

**Tools:**
- `list_available_scenarios()` — List scenarios user can initiate requests for
  - Returns scenarios exposed in MCP Server CRD (filtered by OPA policy)
  - Includes scenario metadata (description, required parameters, etc.)
  
- `get_scenario_info(scenario_id)` — Get detailed scenario information
  - Required parameters for request initiation
  - Request type (derived from scenario)
  - Available subject types

---

### Q11: Task Solver Prompts

**Question:** How are task solver prompts defined and used?

**Design:**
- **Every task type has a solver prompt template** defined in Scenario definition
- **MCP Server CRD references prompt templates** for exposed scenarios
- **Prompt templates structured** for semantic/structural equivalence with MCP Router list-prompts response
- **Prompt compiled when client requests** it (not pre-compiled)
- **Full request context available** for prompt compilation (everything available to Hub Application)

**Flow:**
1. Developer defines task solver prompt template in Scenario definition (per task type, associated with trigger)
2. Developer references prompt template in MCP Server CRD for exposed scenarios
3. Client calls `prompts/list()` to see available prompts (MCP Router returns prompt templates)
4. Client calls `prompts/get_task_solver(task_id)` when user needs to complete task
5. MCP Server compiles prompt template with full request context:
   - Request data (all entities, history, timeline)
   - Task details and requirements
   - Subject information
   - Related entities
   - Any other context available to Hub Application
6. Client receives compiled prompt and uses it to guide AI agent

**Tools:**
- `prompts/list()` — List available prompt templates (MCP Router returns templates from CRD)
- `prompts/get_task_solver(task_id)` — Get compiled task solver prompt for specific task
  - Returns prompt compiled with full request context
  - Includes task requirements, available actions, guidance

**Prompt Template Structure:**
- Defined in Scenario definition (per task type, associated with trigger)
- Referenced in MCP Server CRD as `prompt_templates`
- Structure must be semantically/structurally equivalent to MCP Router's list-prompts response
- Compiled at request time with request context

---

## Prompt Template Format

> **For Developers:** This section defines the prompt template format required for MCP Server CRDs.
> Templates must be semantically and structurally equivalent to MCP Router's `prompts/list` response.

### MCP Prompt Structure (from MCP Protocol)

The MCP protocol defines prompts with the following structure:
```json
{
  "name": "prompt-name",
  "description": "Human-readable description of what this prompt does",
  "arguments": [
    {
      "name": "argument_name",
      "description": "Description of this argument",
      "required": true
    }
  ]
}
```

### Hub Prompt Template Format

Hub prompt templates extend this structure with Hub-specific metadata:

```yaml
prompt_templates:
  # Task Solver Prompt (Essential - Highly Recommended)
  - name: verify_kyc_documents
    description: "Guide the user through completing KYC document verification task"
    category: task_solver  # task_solver | guidance | error_handling | progress
    scenario_ref: kyc-verification
    task_type: verify_kyc_documents  # Links to Scenario's task type
    arguments:
      - name: task_id
        description: "The task ID to get solver guidance for"
        required: true
    template: |
      You are helping a user complete a KYC document verification task.
      
      ## Task Details
      - Task ID: {{task_id}}
      - Request: {{request.id}} ({{request.status}})
      - Subject: {{subject.name}} ({{subject.id}})
      
      ## Required Documents
      {{#each task.required_documents}}
      - {{this.type}}: {{this.status}}
      {{/each}}
      
      ## Available Actions
      - `approve_document(document_id)` - Approve a verified document
      - `reject_document(document_id, reason)` - Reject a document with reason
      - `request_additional_info(message)` - Ask subject for more information
      - `complete_task(outcome)` - Mark task as complete
      
      ## Guidance
      Review each document carefully. Verify identity matches across all documents.
      If any document is unclear or suspicious, reject with specific reason.

  # General Guidance Prompt (Optional - Developer Discretion)
  - name: how_to_file_dispute
    description: "Explains how to file a dispute using this MCP server"
    category: guidance
    scenario_ref: dispute-filing
    arguments: []  # No arguments needed
    template: |
      To file a dispute:
      
      1. Call `create_service_request` with:
         - scenario_id: "dispute-filing"
         - subject_id: Your customer ID
         - payload: { transaction_id, dispute_reason, amount }
      
      2. Track your request using `get_request_status(request_id)`
      
      3. Respond to any information requests via `send_request_update`
      
      4. Subscribe to updates: `resources/subscribe("request://REQ-xxx")`

  # Error Handling Prompt (Optional - Developer Discretion)
  - name: request_error_help
    description: "Help diagnose and resolve request errors"
    category: error_handling
    arguments:
      - name: request_id
        description: "The request ID experiencing issues"
        required: true
      - name: error_type
        description: "The type of error encountered"
        required: false
    template: |
      Request {{request_id}} encountered an issue.
      
      ## Error Analysis
      {{#if error_type}}
      Error type: {{error_type}}
      {{/if}}
      
      ## Troubleshooting Steps
      1. Check request status: `get_request_status("{{request_id}}")`
      2. Review timeline: `get_request_timeline("{{request_id}}")`
      3. Look for pending tasks: Check if any tasks are awaiting input
      
      ## Common Issues
      - **AUTHORIZATION_REQUIRED**: Need to complete delegation flow
      - **DOCUMENT_MISSING**: Upload required documents
      - **VALIDATION_ERROR**: Check payload format
```

### Prompt Compilation

When client calls `prompts/get(name, arguments)`:
1. MCP Server retrieves the prompt template
2. If `task_id` is provided, loads full request context:
   - Request data (all entities, history, timeline)
   - Task details and requirements
   - Subject information
   - Related entities
3. Compiles template with Mustache/Handlebars
4. Returns compiled prompt to client

### MCP Router Compatibility

The above YAML structure maps to MCP Router's `prompts/list` response:

```json
{
  "prompts": [
    {
      "name": "verify_kyc_documents",
      "description": "Guide the user through completing KYC document verification task",
      "arguments": [
        { "name": "task_id", "description": "The task ID to get solver guidance for", "required": true }
      ]
    },
    {
      "name": "how_to_file_dispute",
      "description": "Explains how to file a dispute using this MCP server",
      "arguments": []
    },
    {
      "name": "request_error_help",
      "description": "Help diagnose and resolve request errors",
      "arguments": [
        { "name": "request_id", "description": "The request ID experiencing issues", "required": true },
        { "name": "error_type", "description": "The type of error encountered", "required": false }
      ]
    }
  ]
}
```

**Key Points:**
- Hub stores additional metadata (`category`, `scenario_ref`, `task_type`, `template`)
- MCP Router exposes only MCP-compliant fields (`name`, `description`, `arguments`)
- Template compilation happens server-side; client receives compiled string
- Mustache/Handlebars used for template rendering (same as Tool Specifications)

---

### Q12: Tool Parameters vs. REST API Payloads

**Question:** How do MCP tool parameters map to REST API request payloads?

**REST API Example:**
```json
POST /api/business/v1/requests
{
  "scenario_id": "bill-payment",
  "request_type": "service_request",
  "subject_id": "CUST-123",
  "payload": {
    "bill_id": "BILL-123",
    "amount": 100.00,
    "payment_method": "checking_account"
  }
}
```

**MCP Tool Call:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "create_service_request",
    "arguments": {
      "scenario_id": "bill-payment",
      "subject_id": "CUST-123",
      "payload": {
        "bill_id": "BILL-123",
        "amount": 100.00,
        "payment_method": "checking_account"
      }
    }
  }
}
```

**Design:**
- Direct mapping — tool parameters = REST API payload
- MCP Server translates tool call to REST API call
- Tool parameters validated against REST API schema

---

### Q13: Task Participation

**Question:** How do business users participate in task completion?

**Design:**
- **For Business Users**: Task participation primarily as **subject** of requests
  - Tasks assigned to user as the request subject
  - User can view, complete, and upload documents for subject tasks
  
- **For Other Personas** (Agents, Supervisors): Task participation as **assignees**
  - Tasks assigned to user as an agent/assignee
  - Full task operations available (complete, hold, resume, abandon, etc.)

**Tools (Business Users):**
- `list_my_tasks()` — List tasks assigned to user (as subject)
- `get_task_details(task_id)` — Get task details and requirements
- `complete_task(task_id, outcome, payload)` — Complete a task
- `upload_task_document(task_id, document)` — Upload document for task
- `get_task_solver(task_id)` — Get task solver prompt template (via prompts/get_task_solver)

**Task Completion Flow:**
1. User's AI agent calls `list_my_tasks()` to see assigned tasks
2. Agent calls `get_task_details(task_id)` to understand requirements
3. Agent calls `prompts/get_task_solver(task_id)` to get compiled prompt template
4. User provides information/actions through AI agent
5. Agent calls `complete_task(task_id, outcome, payload)` to complete task
6. Task completion triggers Request Update in Hub
7. Request continues processing

### Q14: Error Handling

**Question:** How are errors from Scenario/Request processing communicated to AI agent?

**Error Scenarios:**
- Signal validation fails
- Request creation fails
- Tool invocation fails
- Request processing error

**Design:**
- **Immediate errors**: Tool returns error in response (standard MCP JSON-RPC error)
  - For tool call failures (validation, authorization, etc.)
  - Immediate feedback to AI agent
  
- **Asynchronous errors**: Error sent via JSON-RPC notification
  - `notifications/request/error` for request-level errors that occur after tool call completes
  - Includes request_id, error details, recovery suggestions

---

### Q15: Delegation and Authority

**Question:** How does request-scoped authority delegation work with MCP?

**Existing:** [Request-Scoped Delegation](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md) requires:
- Channel to capture user consent
- Channel to request Delegation Certificate/Token from Cipher

**MCP Context:**
- MCP is a Channel
- User's AI agent acts on user's behalf
- Agent may need delegated authority for certain tool calls

**Two Delegation Options:**

**Option 1: Out-of-Band Browser Link (Default)**
1. Agent calls tool requiring delegation (e.g., `create_service_request` with payment authority)
2. MCP Server responds with `AUTHORITY_REQUEST` notification:
   ```json
   {
     "method": "notifications/authority/request",
     "params": {
       "request_id": "auth-req-123",
       "template": "personal-finance-assistant",
       "reason": "Payment initiation requires delegation",
       "browser_link": "https://hub.example.com/auth/delegate?request=auth-req-123",
       "expires_at": "2026-01-17T22:00:00Z"
     }
   }
   ```
3. User opens browser link, authenticates, grants certificate
4. MCP Server receives certificate from Cipher
5. MCP Server sends `AUTHORITY_GRANTED` notification to client
6. Agent can retry original tool call (now with delegation token)

**Option 2: Client-Provided Certificate (Alternative)**
1. Agent calls tool requiring delegation
2. MCP Server responds with `AUTHORITY_REQUEST` notification
3. Client implements its own authentication/authorization flow
4. Client calls `update_authority_request(auth_request_id, certificate)` tool:
   ```json
   {
     "method": "tools/call",
     "params": {
       "name": "update_authority_request",
       "arguments": {
         "auth_request_id": "auth-req-123",
         "certificate": {
           "certificate_id": "cert-456",
           "delegator": "user-67890",
           "template": "personal-finance-assistant",
           "expires_at": "2026-01-17T22:00:00Z"
         }
       }
     }
   }
   ```
5. MCP Server validates certificate with Cipher
6. MCP Server sends `AUTHORITY_GRANTED` notification
7. Agent can retry original tool call

**Tools:**
- `update_authority_request(auth_request_id, certificate)` — Client-provided certificate flow
- `get_authority_request_status(auth_request_id)` — Check status of authority request

**Design:**
- **Out-of-band browser link** is the default (simpler for most clients)
- **Client-provided certificate** is alternative (for clients with custom auth flows)
- **Delegation token** automatically attached to subsequent tool calls in same MCP session
- **Certificate validation** happens server-side (MCP Server validates with Cipher)

---

## Transport Requirements

### Dual Transport Support (SSE + Bidirectional Chunking)

For MCP Servers to push updates to clients, Hub must support **both** transport mechanisms with automatic fallback:

**1. Server-Sent Events (SSE) - Default**
- **Mechanism:** JSON-RPC notifications sent via `text/event-stream`
- **Connection:** Client establishes persistent GET connection for server→client updates
- **Client→Server:** Separate HTTP POST requests for tool calls
- **Advantages:** Simple, low latency, works well when middleware supports it
- **Disadvantages:** Requires middleware support (some proxies/CDNs buffer)
- **Use Case:** Default when infrastructure supports SSE

**2. Streamable HTTP (Bidirectional Chunking) - Fallback**
- **Mechanism:** JSON-RPC 2.0 over HTTP with chunked transfer encoding
- **Connection:** Single persistent connection for both directions
- **Bidirectional:** Client sends tool calls; server sends notifications via chunked responses
- **Advantages:** Better middleware compatibility, works with proxies/load balancers/CDNs
- **Disadvantages:** Slightly more complex than SSE
- **Use Case:** Fallback when SSE has middleware compatibility issues

### Transport Selection Strategy

**Default to SSE, Fallback to Chunking:**
1. Client attempts SSE connection first
2. If SSE fails or middleware buffers/breaks connection → automatically fallback to Streamable HTTP
3. Client can also explicitly request Streamable HTTP if known issues with SSE

**Hub Implementation:**
- MCP Router must support both SSE and Streamable HTTP transports
- Heracles Gateway must:
  - Support SSE (`text/event-stream`) with proper headers
  - Support chunked transfer encoding and disable proxy buffering
  - Detect SSE failures and suggest fallback
- MCP Server must:
  - Maintain connection (SSE or chunked) and send notifications when Request Updates occur
  - Support both transport mechanisms

### Additional Transport Options

**3. WebSockets (Future/Under Discussion)**
- **Status:** SEP (Specification Enhancement Proposal) under discussion in MCP
- **Advantages:** Full-duplex, low latency, better for real-time bidirectional communication
- **Disadvantages:** More complex setup, scaling challenges, not yet standardized in MCP
- **Use Case:** Future option when low-latency bidirectional updates are critical

**4. Long Polling - Last Resort**
- **Status:** Fallback when streaming isn't supported
- **Advantages:** Works over plain HTTP, minimal infrastructure requirements
- **Disadvantages:** Higher latency, more overhead, server load from reconnections
- **Use Case:** Only when neither SSE nor chunking are feasible

### Transport Comparison

| Transport | Bidirectional | Middleware Compatibility | Stateful | Latency | Complexity | Default? |
|-----------|---------------|-------------------------|----------|---------|------------|---------|
| **SSE** | ⚠️ (separate POST for client→server) | ⚠️ Variable (some buffer) | Stateful | Low | Low | ✅ **Yes (default)** |
| **Streamable HTTP** | ✅ (chunked responses) | ✅ Good | Can be stateless | Low | Medium | ✅ **Fallback** |
| **WebSockets** | ✅ Full-duplex | ✅ Good | Stateful | Very Low | High | ❌ Future |
| **Long Polling** | ⚠️ (via reconnection) | ✅ Good | Stateless | High | Low | ❌ Last resort |

### Recommendation for Hub

**Dual Support:** Support both **SSE (default)** and **Streamable HTTP (fallback)**:
- **SSE as default:** Simpler, lower latency when middleware supports it
- **Streamable HTTP as fallback:** Better compatibility when SSE has issues
- **Automatic detection:** Client/MCP Router detects SSE issues and falls back to chunking
- **Explicit selection:** Clients can explicitly request Streamable HTTP if needed

**Future:** Consider **WebSockets** when:
- Low-latency bidirectional updates are critical
- MCP specification standardizes WebSocket transport
- Infrastructure supports WebSocket scaling

### Notification Flow (SSE - Default)

```
1. Client connects to MCP Server (via MCP Router)
   │   Transport: SSE (text/event-stream) - default
   │   Connection: GET /mcp/{server}/events (SSE stream)
   │
2. Client subscribes to request resource: resources/subscribe("request://REQ-456")
   │   (Sent via separate POST request)
   │   Note: Resource contains all data available to subscribing user
   │
3. Request Update occurs in Hub
   │
4. MCP Server (as Signal Exchange observer) receives update
   │
5. MCP Server sends JSON-RPC notification via SSE:
   │   data: {"jsonrpc":"2.0","method":"notifications/resources/updated","params":{"uri":"request://REQ-456"}}
   │   (Sent as SSE event in the text/event-stream)
   │
6. Client receives notification (via SSE stream)
   │
7. Client calls resources/read("request://REQ-456") to fetch updated request data
   │   (Sent via separate POST request)
```

### Notification Flow (Streamable HTTP - Fallback)

```
1. Client connects to MCP Server (via MCP Router)
   │   Transport: Streamable HTTP (chunked transfer encoding) - fallback
   │   Connection: POST /mcp/{server}/stream (chunked response)
   │
2. Client subscribes to request resource: resources/subscribe("request://REQ-456")
   │   (Sent in same chunked stream)
   │   Note: Resource contains all data available to subscribing user
   │
3. Request Update occurs in Hub
   │
4. MCP Server (as Signal Exchange observer) receives update
   │
5. MCP Server sends JSON-RPC notification via chunked HTTP response:
   │   notifications/resources/updated { uri: "request://REQ-456" }
   │   (Sent as chunk in the ongoing HTTP response stream)
   │
6. Client receives notification (via chunked transfer encoding)
   │
7. Client calls resources/read("request://REQ-456") to fetch updated request data
   │   (Sent in same chunked stream)
```

**Key Points:**
- **SSE (default):** Simpler, separate GET for server→client, POST for client→server
- **Streamable HTTP (fallback):** Single bidirectional stream, better middleware compatibility
- **Automatic fallback:** Client/MCP Router detects SSE issues and switches to chunking
- **Connection maintained:** Via MCP transport session ID in both cases

---

## Session Management

### MCP Session Scope

**MCP Session is relevant only up to MCP Gateway:**
- Session established between client and MCP Gateway
- Session ID managed by MCP Gateway (via Heracles)
- Session state does not persist beyond gateway

### Session Establishment

**OAuth Flow:**
- Client handles OAuth flow (user logs in using client-provided mechanisms)
- Client obtains access token from OAuth provider
- Client presents access token to MCP Gateway for session establishment
- MCP Gateway validates access token and creates MCP session
- **Discussion starts after client has access token** (client implementation not in scope)

### Session Termination

**Termination Triggers:**
- **Client-initiated**: Client explicitly terminates session
- **Server-initiated**: Server terminates if client socket is broken
- **Inactivity timeout**: Session terminated after inactivity period (configurable in MCP Server CRD)
  - Example: `session.inactivity_timeout: 30m`

**Session Limits:**
- **Max subscriptions**: Maximum concurrent resource subscriptions per session (configurable in CRD)
  - Example: `session.max_subscriptions: 50`
- Other session limits can be expanded as needed

### Session-Bound Subscriptions

**Resource Subscriptions:**
- All resource subscriptions are MCP-session bound
- Subscriptions cannot persist beyond session
- On session disconnect: All subscriptions cleared
- On reconnection: Client must re-subscribe to resources

---

## Next Steps

1. **Finalize MCP Server CRD:** Complete schema for request initiation and participation tools
2. **Design MCP Router Integration:** How MCP Servers register with MCP Router and expose tools
3. **Map All REST APIs:** Ensure all Business User REST APIs have corresponding MCP tools
4. **Design Request Update Notifications:** JSON-RPC notifications and resource subscriptions for real-time updates
5. **Design Transport Layer:** Dual support for SSE (default) and Streamable HTTP (fallback) for server→client push
6. **Design Prompt System:** How prompts guide AI agent behavior for request operations
7. **Design Delegation Flow:** How request-scoped delegation works with MCP (MCP Server as Channel)
8. **Design Scenario Discovery:** How AI agents discover available scenarios for request initiation

---

## Related Documentation

- [MCP Channels](../../06-ux-architecture/tenant-domain/mcp-channels.md)
- [MCP Router](../../05-infrastructure/mcp-router.md)
- [Scenario as Tool](../../02-system-design/implementation-concepts/scenario-as-tool.md)
- [Channel](../../02-system-design/implementation-concepts/channel.md)
- [Request Update](../../02-system-design/implementation-concepts/request-update.md)
- [Request-Scoped Delegation](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)
