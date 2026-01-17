# MCP Prompt Template Authoring

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

This guide explains how to author effective MCP prompt templates for AI agents. Prompt templates guide AI agents through task completion and Hub operations.

---

## Overview

By the end of this guide, you will be able to:

- Author task solver prompts (essential)
- Create guidance prompts (optional)
- Structure prompts for MCP Router compatibility
- Use context variables effectively
- Apply Mustache/Handlebars syntax

---

## Prerequisites

Before you begin, ensure you have:

- [ ] **Scenario defined** — Scenario exists with task types (for task solver prompts)
- [ ] **MCP Server CRD** — MCP Server CRD created (to reference prompts)
- [ ] **Developer or Process Architect access** — You can create/update Scenario definitions and MCP Server CRDs

### Required Knowledge

- Understanding of Hub scenarios, tasks, and requests
- Basic knowledge of Mustache/Handlebars template syntax
- Familiarity with AI agent interaction patterns

### Related Documentation

- [Prompt Templates](../../04-subsystems/mcp-channel/prompt-templates.md) — Prompt template format specification
- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md) — CRD structure

---

## Quick Start

If you're already familiar with prompt templates, here's the quick version:

```yaml
prompt_templates:
  - name: verify_kyc_documents
    description: "Guide through KYC document verification"
    category: task_solver
    scenario_ref: kyc-verification
    task_type: verify_kyc_documents
    arguments:
      - name: task_id
        description: "Task ID to get guidance for"
        required: true
    template: |
      ## Task: Verify KYC Documents
      Task ID: {{task_id}}
      Request: {{request.id}}
      
      ## Required Documents
      {{#each task.required_documents}}
      - {{this.type}}: {{this.status}}
      {{/each}}
      
      ## Actions
      - `approve_document(document_id)`
      - `reject_document(document_id, reason)`
```

For detailed explanations, continue to the full guide below.

---

## Step-by-Step Guide

### Step 1: Understand Prompt Categories

**Prompt templates fall into four categories:**

| Category | Required? | Description | Example |
|----------|-----------|-------------|---------|
| **Task Solver** | Essential (highly recommended) | Guidance for completing specific task types | `verify_kyc_documents`, `dispute_triage` |
| **Guidance** | Optional | How to use scenarios, general operations | `how_to_file_dispute`, `scenario_overview` |
| **Error Handling** | Optional | What went wrong, how to fix | `request_error_help`, `authorization_help` |
| **Progress** | Optional | What's happening, what to expect | `request_progress_update`, `task_status_explanation` |

**What to expect:** You understand which category your prompt belongs to.

**Verification:** Confirm the category matches your prompt's purpose.

---

### Step 2: Author Task Solver Prompts

**Task solver prompts are essential and highly recommended.**

#### Define in Scenario

Task solver prompts are defined in Scenario definitions (per task type):

```yaml
# In Scenario definition
scenario:
  id: kyc-verification
  tasks:
    - type: verify_kyc_documents
      solver_prompt:
        name: verify_kyc_documents
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
```

#### Reference in MCP Server CRD

Reference the prompt in MCP Server CRD:

```yaml
spec:
  prompt_templates:
    - name: verify_kyc_documents
      scenario_ref: kyc-verification
      task_type: verify_kyc_documents
      category: task_solver
```

**What to expect:** AI agents can use this prompt to guide task completion.

**Verification:** Test prompt compilation via MCP client.

---

### Step 3: Author Guidance Prompts

**Guidance prompts are optional but helpful for AI agents.**

```yaml
spec:
  prompt_templates:
    - name: how_to_file_dispute
      description: "Explains how to file a dispute using this MCP server"
      category: guidance
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
```

**What to expect:** AI agents can use this prompt to understand how to use the MCP Server.

**Verification:** Test prompt via MCP client.

---

### Step 4: Use Context Variables

**Context variables are available for template compilation:**

| Variable | Description | Available When |
|----------|-------------|----------------|
| `{{request}}` | Full request data | Task solver prompts, request-scoped prompts |
| `{{task}}` | Task details and requirements | Task solver prompts |
| `{{subject}}` | Subject entity (customer, employee, etc.) | Request-scoped prompts |
| `{{scenario}}` | Scenario definition | All prompts |
| `{{related_entities}}` | Related entities (accounts, transactions, etc.) | Request-scoped prompts |
| `{{request.history}}` | Request update history | Request-scoped prompts |
| `{{request.timeline}}` | Request timeline | Request-scoped prompts |

**Example with context:**

```yaml
template: |
  ## Request Context
  Request ID: {{request.id}}
  Status: {{request.status}}
  Scenario: {{scenario.name}}
  
  ## Subject Information
  Name: {{subject.name}}
  ID: {{subject.id}}
  
  ## Related Entities
  {{#each related_entities.accounts}}
  Account: {{this.id}} ({{this.type}})
  {{/each}}
```

**What to expect:** Prompt compiled with full request context.

**Verification:** Test prompt compilation with actual request data.

---

### Step 5: Apply Mustache/Handlebars Syntax

**Use Mustache/Handlebars for template logic:**

#### Basic Variables

```yaml
template: |
  Task ID: {{task_id}}
  Request: {{request.id}}
```

#### Conditionals

```yaml
template: |
  {{#if error_type}}
  Error type: {{error_type}}
  {{/if}}
  
  {{#unless task.completed}}
  Task is still in progress.
  {{/unless}}
```

#### Loops

```yaml
template: |
  ## Required Documents
  {{#each task.required_documents}}
  - {{this.type}}: {{this.status}}
  {{/each}}
```

#### Nested Context

```yaml
template: |
  {{#each request.timeline}}
  - {{this.timestamp}}: {{this.event}}
    {{#if this.details}}
    Details: {{this.details}}
    {{/if}}
  {{/each}}
```

**What to expect:** Template renders correctly with context data.

**Verification:** Test template compilation with sample data.

---

## Complete Example

### Task Solver Prompt: Dispute Triage

```yaml
# In Scenario definition
scenario:
  id: dispute-filing
  tasks:
    - type: dispute_triage
      solver_prompt:
        name: dispute_triage
        template: |
          You are helping triage a payment dispute.
          
          ## Dispute Details
          - Dispute ID: {{request.id}}
          - Transaction: {{related_entities.transaction.id}}
          - Amount: ${{related_entities.transaction.amount}}
          - Customer: {{subject.name}} ({{subject.id}})
          
          ## Dispute Reason
          {{request.payload.dispute_reason}}
          
          ## Available Actions
          - `approve_dispute()` - Approve dispute and proceed
          - `reject_dispute(reason)` - Reject dispute with reason
          - `request_evidence(evidence_types)` - Request additional evidence
          - `escalate_to_supervisor(reason)` - Escalate to supervisor
          - `complete_task(outcome)` - Mark triage complete
          
          ## Decision Criteria
          {{#each scenario.decision_criteria}}
          - {{this.criterion}}: {{this.guidance}}
          {{/each}}
          
          ## Guidance
          Review transaction details and dispute reason carefully.
          Check customer history for patterns.
          If evidence is insufficient, request additional evidence before deciding.
```

```yaml
# In MCP Server CRD
spec:
  prompt_templates:
    - name: dispute_triage
      scenario_ref: dispute-filing
      task_type: dispute_triage
      category: task_solver
      arguments:
        - name: task_id
          description: "Task ID to get guidance for"
          required: true
```

---

## Best Practices

| Practice | Rationale |
|----------|-----------|
| **Start with task solver prompts** | Essential for good AI agent experience |
| **Be specific about actions** | List exact tool names and parameters |
| **Include decision criteria** | Help AI agents make informed decisions |
| **Use context variables** | Make prompts dynamic and relevant |
| **Test with real data** | Verify prompts compile correctly with actual request context |
| **Keep prompts focused** | One prompt per task type or use case |
| **Document prompt purpose** | Clear description helps AI agents choose the right prompt |

---

## Common Patterns

### Pattern A: Task Completion Guidance

```yaml
template: |
  ## Task: {{task.type}}
  
  ## Context
  Request: {{request.id}}
  Subject: {{subject.name}}
  
  ## Steps to Complete
  1. Review {{task.requirements}}
  2. Perform {{task.actions}}
  3. Record decision: `record_decision(decision)`
  4. Complete task: `complete_task(outcome)`
```

### Pattern B: Error Resolution

```yaml
template: |
  ## Error: {{error_type}}
  
  ## What Happened
  {{error.message}}
  
  ## How to Fix
  {{#each error.resolution_steps}}
  {{@index}}. {{this}}
  {{/each}}
  
  ## If Still Stuck
  Use `escalate_to_supervisor(reason)` to get help.
```

### Pattern C: Progress Explanation

```yaml
template: |
  ## Request Progress
  
  Current Status: {{request.status}}
  
  ## What's Happening
  {{request.current_activity}}
  
  ## Next Steps
  {{#each request.next_steps}}
  - {{this}}
  {{/each}}
  
  ## Expected Completion
  {{request.estimated_completion}}
```

---

## Troubleshooting

### Issue: Prompt Not Compiling

**Symptom:** Template compilation fails

**Cause:** Syntax error or missing context variable

**Solution:**
1. Verify Mustache/Handlebars syntax
2. Check context variables are available
3. Test template with sample data
4. Review template format: [Prompt Templates](../../04-subsystems/mcp-channel/prompt-templates.md)

---

### Issue: Context Variables Not Available

**Symptom:** Variables render as empty or undefined

**Cause:** Context not loaded or variable path incorrect

**Solution:**
1. Verify context is loaded (check task_id is provided)
2. Check variable path (e.g., `request.id` not `request_id`)
3. Test with actual request data
4. Review available context: [Prompt Templates](../../04-subsystems/mcp-channel/prompt-templates.md)

---

## Next Steps

Now that you've authored prompt templates, you may want to:

- [Publishing MCP Server](./publishing-mcp-server.md) — Publish your MCP Server with prompts
- [Prompt Templates](../../04-subsystems/mcp-channel/prompt-templates.md) — Reference documentation

---

## Related Documentation

- [Prompt Templates](../../04-subsystems/mcp-channel/prompt-templates.md) — Format specification
- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md) — CRD structure
- [ADR-0133: MCP Prompt Template Format](../../decision-logs/0133-mcp-prompt-template-format.md) — Design decision
