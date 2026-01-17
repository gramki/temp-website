# Prompt Templates

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

Prompt templates provide guidance to AI agents for completing tasks and understanding Hub operations. They are structured for semantic and structural equivalence with MCP Router's `prompts/list` response format.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Guide AI agents through task completion and Hub operations |
| **Format** | MCP-compatible structure (semantic/structural equivalence) |
| **Compilation** | Mustache/Handlebars templates compiled with request context |
| **Categories** | Task solver (essential), guidance, error handling, progress |
| **Applicability** | Scenario-based templates only (machine-template does not support prompts) |

---

## Prompt Template Format

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

---

## Prompt Categories

| Category | Required? | Description | Example |
|----------|-----------|-------------|---------|
| **Task Solver** | Essential (highly recommended) | Guidance for completing specific task types | `verify_kyc_documents`, `dispute_triage` |
| **Guidance** | Optional (developer discretion) | How to use scenarios, general operations | `how_to_file_dispute`, `scenario_overview` |
| **Error Handling** | Optional (developer discretion) | What went wrong, how to fix | `request_error_help`, `authorization_help` |
| **Progress** | Optional (developer discretion) | What's happening, what to expect | `request_progress_update`, `task_status_explanation` |

---

## Prompt Compilation

When client calls `prompts/get(name, arguments)`:

```
1. MCP Server retrieves the prompt template
2. If task_id is provided, loads full request context:
   - Request data (all entities, history, timeline)
   - Task details and requirements
   - Subject information
   - Related entities
   - Any other context available to Hub Application
3. Compiles template with Mustache/Handlebars
4. Returns compiled prompt to client
```

### Context Available for Compilation

| Context Variable | Description | Available When |
|------------------|-------------|----------------|
| `request` | Full request data | Task solver prompts, request-scoped prompts |
| `task` | Task details and requirements | Task solver prompts |
| `subject` | Subject entity (customer, employee, etc.) | Request-scoped prompts |
| `scenario` | Scenario definition | All prompts |
| `related_entities` | Related entities (accounts, transactions, etc.) | Request-scoped prompts |
| `request.history` | Request update history | Request-scoped prompts |
| `request.timeline` | Request timeline | Request-scoped prompts |

---

## MCP Router Compatibility

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

## Task Solver Prompts

Task solver prompts are **essential and highly recommended**. They guide AI agents through completing specific task types.

### Definition

Task solver prompts are defined in Scenario definitions (per task type, associated with trigger) and referenced in MCP Server CRDs:

```yaml
# In Scenario definition
scenario:
  id: kyc-verification
  tasks:
    - type: verify_kyc_documents
      solver_prompt:
        name: verify_kyc_documents
        template: |
          # Prompt template content
```

```yaml
# In MCP Server CRD
spec:
  prompt_templates:
    - name: verify_kyc_documents
      scenario_ref: kyc-verification
      task_type: verify_kyc_documents
```

### Flow

```
1. Developer defines task solver prompt template in Scenario definition
2. Developer references prompt template in MCP Server CRD
3. Client calls prompts/list() to see available prompts
4. Client calls prompts/get_task_solver(task_id) when user needs to complete task
5. MCP Server compiles prompt template with full request context
6. Client receives compiled prompt and uses it to guide AI agent
```

---

## Related Documentation

- [MCP Server CRD](./mcp-server-crd.md) — CRD structure for prompt templates
- [ADR-0133](../../decision-logs/0133-mcp-prompt-template-format.md) — MCP Prompt Template Format
- [Guide: Prompt Template Authoring](../../10-guides/mcp-prompt-template-authoring.md) — How to author effective prompts

---

*TODO: C3-level details — exact template schema validation, context variable resolution, compilation performance*
