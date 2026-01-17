# MCP Server CRD

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

MCP Servers are workbench-scoped Custom Resource Definitions (CRDs) that expose Hub capabilities via the Model Context Protocol (MCP). Each MCP Server uses a **template kind** that implies the persona and capabilities it provides.

---

## Overview

MCP Server CRDs enable developers to publish multiple MCP Servers per workbench, allowing segregation by:
- **Functional boundaries** (e.g., payments vs. disputes)
- **Privilege boundaries** (e.g., read-only vs. write access)
- **Business needs** (e.g., customer-facing vs. internal operations)

### Key Design Principles

| Principle | Description |
|-----------|-------------|
| **Template-based** | Template kind (e.g., `business-user-template`) implies persona |
| **Scenario-based exposure** | When scenarios are included, corresponding requests are automatically included |
| **OPA-based access control** | Access limited via OPA policies using access token claims, scopes, delegation-templates |
| **MCP-compatible prompts** | Prompt templates structured for semantic/structural equivalence with MCP Router list-prompts response |

---

## Template Kinds

The MCP Channel subsystem supports **seven template kinds** organized into two categories:

### Scenario-Based Templates

These templates expose Hub scenarios, requests, tasks, and resources with full request lifecycle management.

| Template Kind | Persona(s) | Default Tools | Resources | Sessions |
|---------------|------------|---------------|-----------|----------|
| `business-user-template` | Business Customer, Employee, System | Request initiation/participation | Requests | Yes |
| `supervisor-template` | Supervisor | Queue mgmt, SLAs, directability | Queues, escalations | Yes |
| `agent-template` | Agent (Human/AI) | Task processing, knowledge | Tasks, requests | Yes |
| `creator-template` | Process Architect, Developer | Scenario design, feedback | Scenarios, feedback | Yes |
| `admin-template` | Administrator | Subscription mgmt | Workbenches | Yes |
| `auditor-template` | Auditor | Decision investigation | Audit trails | Yes |

### Tool-Based Templates

| Template Kind | Purpose | Tools | Resources | Sessions |
|---------------|---------|-------|-----------|----------|
| `machine-template` | Expose Machine tools via MCP | From Tool Registry | None | Stateless |

> **Note:** `machine-template` has a dedicated document: [Machine Template](./machine-template.md)

---

## CRD Structure

### Common Structure (All Templates)

```yaml
apiVersion: hub.olympus.io/v1
kind: <template-kind>  # e.g., business-user-template, supervisor-template
metadata:
  name: <server-name>
  namespace: <workbench-namespace>
spec:
  # Server identity
  server:
    name: <server-name>
    display_name: "<Display Name>"
    description: "<Description>"
    version: "<version>"
  
  # Workbench scope (except admin-template which is tenant-scoped)
  workbench_ref: <workbench-id>
  
  # Access control via OPA policy
  access_policy:
    # OPA Rego policy
    # Evaluates against access token claims, scopes, delegation-templates, etc.
    # (exact policy structure TBD - C3 level detail)
  
  # Session configuration (not applicable to machine-template)
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50  # Maximum concurrent resource subscriptions per session
```

### Scenario-Based Template Extensions

Scenario-based templates (all except `machine-template`) include:

```yaml
spec:
  # ... common structure ...
  
  # Scenarios to expose
  # When scenarios are included, corresponding requests are automatically included
  # No need to specify request_type - it's derived from scenario
  exposed_scenarios:
    - scenario_ref: <scenario-id>
    - scenario_ref: <scenario-id>
  
  # Prompt templates (optional)
  prompt_templates:
    # Task solver prompts (referenced from Scenario definitions)
    - name: <prompt-name>
      scenario_ref: <scenario-id>
      task_type: <task-type>
      # Template structure matches MCP prompt format
      # (see prompt-templates.md for details)
    
    # General guidance prompts
    - name: <prompt-name>
      description: "<Description>"
      # Template structure matches MCP prompt format
```

---

## Template-Specific Examples

### business-user-template

**Purpose:** Enable business users to initiate and participate in requests via AI agents.

```yaml
apiVersion: hub.olympus.io/v1
kind: business-user-template
metadata:
  name: payments-mcp-server
  namespace: acme-bank
spec:
  server:
    name: payments-mcp-server
    display_name: "Payments MCP Server"
    description: "MCP server for payment-related request operations"
    version: "1.0.0"
  
  workbench_ref: payments-workbench
  
  exposed_scenarios:
    - scenario_ref: bill-payment
    - scenario_ref: recurring-payment
  
  prompt_templates:
    - name: how_to_initiate_request
      description: "Guidance on how to initiate a request"
    - name: request_troubleshooting
      description: "Help with request issues"
  
  access_policy:
    # OPA Rego policy for business user access
  
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50
```

**Default Tools:**
- Request Initiation: `create_service_request`, `create_business_request`, `create_system_request`
- Request Query: `list_active_requests`, `list_historic_requests`, `get_request_status`, `get_request_timeline`
- Request Participation: `send_request_update`, `upload_document`, `list_documents`, `download_document`
- Task Operations: `list_my_tasks`, `get_task_details`, `complete_task`
- Authority Management: `update_authority_request`, `get_authority_request_status`

---

### supervisor-template

**Purpose:** Enable AI assistants to help Supervisors manage operations.

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
  scenario_scope: all  # or list specific scenarios
  
  prompt_templates:
    - name: queue_analysis
      description: "Analyze queue health and recommend actions"
      category: guidance
    - name: escalation_handling
      description: "Guide through escalation resolution"
      category: task_solver
  
  access_policy:
    # OPA Rego policy for Supervisor role
  
  session:
    inactivity_timeout: 60m
    max_subscriptions: 100
```

**Default Tools:**
- Queue Management: `get_queue_metrics`, `list_queues`, `reassign_task`, `balance_queues`
- Agent Oversight: `list_agents`, `get_agent_status`, `get_agent_workload`, `set_agent_availability`
- SLA Monitoring: `get_sla_status`, `list_sla_breaches`, `list_at_risk_requests`
- Directability: `acknowledge_escalation`, `override_decision`, `change_context_rerun`, `reassign_for_retry`, `fail_scenario`
- Feedback: `promote_feedback`, `list_promoted_feedback`, `get_feedback_status`
- Reporting: `generate_daily_report`, `get_performance_summary`

---

### agent-template

**Purpose:** Enable AI assistants to help Agents (human or AI) process tasks.

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
    # OPA Rego policy for Agent role + queue enrollment
  
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50
```

**Default Tools:**
- Task Processing: `list_my_tasks`, `get_task`, `claim_task`, `complete_task`, `abandon_task`
- Decision Recording: `add_thought`, `add_memo`, `record_decision`, `add_evidence_review`
- Knowledge Access: `search_knowledge`, `get_sop`, `get_policy`, `get_decision_criteria`
- Tool Invocation: `list_available_tools`, `invoke_tool`
- Directability: `acknowledge_escalation`, `override_decision`, `change_context_rerun`
- Request Context: `get_request`, `get_request_timeline`, `get_related_entities`

---

### creator-template

**Purpose:** Enable AI assistants to help Process Architects and Developers design and build.

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
    # OPA Rego policy for PA/Developer roles
  
  session:
    inactivity_timeout: 120m  # Longer for design work
    max_subscriptions: 50
```

**Default Tools:**
- Scenario Design: `list_scenarios`, `get_scenario`, `create_scenario_draft`, `validate_scenario`, `get_scenario_diff`
- Knowledge Management: `list_knowledge_items`, `create_knowledge_draft`, `update_knowledge`, `link_knowledge_to_scenario`
- Trigger Configuration: `list_triggers`, `test_trigger`, `get_trigger_matches`, `debug_trigger`
- Application Development: `list_applications`, `get_application_logs`, `debug_application`, `invoke_application_test`
- Feedback Inbox: `list_feedback_inbox`, `get_feedback_details`, `accept_feedback`, `reject_feedback`, `resolve_feedback`
- Validation: `validate_sop`, `check_scenario_coverage`, `lint_configuration`

---

### admin-template

**Purpose:** Enable AI assistants to help Administrators manage subscription and resources.

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
  
  prompt_templates:
    - name: resource_optimization
      description: "Analyze resource usage and suggest optimizations"
      category: guidance
    - name: user_access_review
      description: "Guide through user access review"
      category: guidance
  
  access_policy:
    # OPA Rego policy for Administrator role
  
  session:
    inactivity_timeout: 30m
    max_subscriptions: 20
```

**Default Tools:**
- Subscription: `get_subscription_status`, `get_subscription_limits`, `get_billing_summary`
- Workbench Management: `list_workbenches`, `get_workbench`, `create_workbench`, `archive_workbench`
- User Management: `list_users`, `get_user_roles`, `list_role_assignments`
- Resource Monitoring: `get_usage_summary`, `get_quota_status`, `list_resource_alerts`
- Configuration: `list_pending_changes`, `approve_change`, `reject_change`

---

### auditor-template

**Purpose:** Enable AI assistants to help Auditors review compliance and investigate decisions.

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
  
  prompt_templates:
    - name: decision_investigation_guide
      description: "Guide through investigating a specific decision"
      category: guidance
    - name: compliance_report_generator
      description: "Generate compliance report for a period"
      category: guidance
  
  access_policy:
    # OPA Rego policy for Auditor role
  
  session:
    inactivity_timeout: 60m
    max_subscriptions: 100
```

**Default Tools:**
- Decision Investigation: `get_decision`, `get_decision_rationale`, `get_decision_context`, `trace_decision_chain`
- Audit Trail: `get_request_audit_trail`, `get_entity_history`, `search_audit_logs`
- Compliance Reporting: `get_compliance_metrics`, `generate_compliance_report`, `list_policy_violations`
- Evidence Collection: `export_request_evidence`, `create_audit_snapshot`, `list_related_requests`

---

## Access Control

All MCP Server CRDs use **OPA-based access control** via the `access_policy` field. The policy evaluates:

- **Access token claims** (user identity, roles, scopes)
- **Delegation templates** (for request-scoped delegation)
- **User profile** (workbench membership, permissions)
- **Request context** (for request-scoped operations)

The exact OPA Rego policy structure is a C3-level detail to be defined during implementation.

---

## Session Configuration

Session configuration applies to scenario-based templates only (not `machine-template`):

| Setting | Description | Default |
|---------|-------------|---------|
| `inactivity_timeout` | Session terminated after inactivity period | 30m |
| `max_subscriptions` | Maximum concurrent resource subscriptions per session | 50 |

---

## Related Documentation

- [Machine Template](./machine-template.md) — Passthrough pattern for Tool Registry tools
- [Prompt Templates](./prompt-templates.md) — Prompt template format specification
- [Session Management](./session-management.md) — Session lifecycle details
- [MCP Operator](./mcp-operator.md) — Endpoint provisioning
- [ADR-0131](../../decision-logs/0131-mcp-server-crd-design.md) — MCP Server CRD Design
- [ADR-0132](../../decision-logs/0132-mcp-template-kinds.md) — MCP Template Kinds

---

*TODO: C3-level details — exact OPA policy structure, prompt template schema validation, session persistence*
