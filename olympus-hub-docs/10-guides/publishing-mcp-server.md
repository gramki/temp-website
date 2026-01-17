# Publishing an MCP Server

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

This guide explains how to publish an MCP Server for a workbench to enable AI agents to interact with Hub capabilities via the Model Context Protocol (MCP).

---

## Overview

By the end of this guide, you will be able to:

- Create an MCP Server CRD for a workbench
- Configure exposed scenarios and prompt templates
- Define OPA-based access control
- Publish and validate the MCP Server

---

## Prerequisites

Before you begin, ensure you have:

- [ ] **Workbench exists** — You have a workbench to publish the MCP Server for
- [ ] **Scenarios defined** — Scenarios you want to expose are already defined (for scenario-based templates)
- [ ] **Developer access** — You have Developer role in the workbench
- [ ] **kubectl access** — You can apply CRDs to the workbench namespace

### Required Knowledge

- Familiarity with Kubernetes CRDs
- Understanding of Hub scenarios and requests
- Basic knowledge of OPA policies (for access control)

### Related Documentation

- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md) — CRD specification
- [Journey: MCP Server Publishing](../../08-personas-and-journeys/journeys/mcp-server-publishing.md) — Journey overview

---

## Quick Start

If you're already familiar with MCP Servers, here's the quick version:

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
    version: "1.0.0"
  workbench_ref: payments-workbench
  exposed_scenarios:
    - scenario_ref: bill-payment
  access_policy:
    # OPA Rego policy
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50
```

```bash
kubectl apply -f payments-mcp-server.yaml
```

For detailed explanations, continue to the full guide below.

---

## Step-by-Step Guide

### Step 1: Choose Template Kind

**Choose the appropriate template kind based on your persona and use case:**

| Template Kind | Use When |
|---------------|----------|
| `business-user-template` | Exposing request initiation/participation to business users |
| `supervisor-template` | Exposing queue management and operations to supervisors |
| `agent-template` | Exposing task processing to agents |
| `creator-template` | Exposing scenario design tools to developers/PAs |
| `admin-template` | Exposing subscription management to administrators |
| `auditor-template` | Exposing compliance tools to auditors |
| `machine-template` | Exposing Tool Registry tools (stateless) — see [Exposing Machine Tools via MCP](./exposing-machine-tools-via-mcp.md) |

**What to expect:** You've selected the template kind that matches your use case.

**Verification:** Confirm the template kind provides the default tools and capabilities you need.

---

### Step 2: Define Exposed Scenarios

**For scenario-based templates, list the scenarios to expose:**

```yaml
spec:
  exposed_scenarios:
    - scenario_ref: bill-payment
    - scenario_ref: recurring-payment
```

**Key Points:**
- When scenarios are included, corresponding requests are automatically included
- No need to specify `request_type` — it's derived from the scenario
- Scenarios must exist in the workbench

**What to expect:** MCP Server will expose tools for initiating and participating in requests for these scenarios.

**Verification:** Verify scenarios exist: `kubectl get scenarios -n <namespace>`

---

### Step 3: Create Prompt Templates (Optional)

**Define prompt templates for task solving and guidance:**

```yaml
spec:
  prompt_templates:
    # Task solver prompt (referenced from Scenario)
    - name: verify_kyc_documents
      scenario_ref: kyc-verification
      task_type: verify_kyc_documents
    
    # General guidance prompt
    - name: how_to_initiate_request
      description: "Guidance on how to initiate a request"
```

**Key Points:**
- Task solver prompts are **essential and highly recommended**
- Task solver prompts are defined in Scenario definitions and referenced here
- Guidance prompts are optional (developer/PA discretion)
- See [MCP Prompt Template Authoring](./mcp-prompt-template-authoring.md) for details

**What to expect:** AI agents can use these prompts to guide task completion.

**Verification:** Verify prompt templates compile correctly (test via MCP client).

---

### Step 4: Configure OPA Policy

**Define access control policy:**

```yaml
spec:
  access_policy:
    # OPA Rego policy
    # Evaluates against access token claims, scopes, delegation-templates
    # (exact policy structure TBD - C3 level detail)
```

**Key Points:**
- Policy evaluates access token claims, scopes, delegation-templates
- Policy can restrict by workbench, scenario, user role, etc.
- Exact OPA Rego policy structure is C3-level detail

**What to expect:** Only authorized users can access the MCP Server.

**Verification:** Test access control with different user roles.

---

### Step 5: Apply CRD

**Apply the MCP Server CRD:**

```bash
kubectl apply -f payments-mcp-server.yaml
```

**MCP Operator will:**
1. Validate CRD structure
2. Provision endpoint at MCP Channel
3. Register tools, prompts, resources
4. Update CRD status: `Provisioned`

**What to expect:** CRD status shows `Provisioned` after a few seconds.

**Verification:** Check CRD status: `kubectl get business-user-template payments-mcp-server -n acme-bank -o yaml`

---

### Step 6: Verify via MCP Client

**Test the MCP Server using an MCP client:**

1. **Connect to MCP Server**: Use Cursor, Claude Desktop, or custom client
2. **List Tools**: Verify tools are available
3. **List Prompts**: Verify prompt templates are available
4. **Test Tool Call**: Call a tool (e.g., `create_service_request`)
5. **Test Prompt**: Get a compiled prompt template
6. **Test Resource Subscription**: Subscribe to a request resource

**What to expect:** All operations work correctly.

**Verification:** Verify tool calls succeed, prompts compile, resources update.

---

## Complete Example

### Scenario: Payments MCP Server

**Goal:** Expose payment scenarios to business users via MCP.

#### Configuration

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
    # (C3 detail)
  
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50
```

#### Result

After applying, the MCP Server is available at:
- Endpoint: `/mcp/payments-workbench/payments-mcp-server`
- Tools: Request initiation, participation, task operations
- Prompts: Guidance prompts for request operations
- Resources: Request resources for subscription

---

## Common Variations

### Variation A: Supervisor Template

If publishing for supervisors:

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
  
  scenario_scope: all  # All scenarios in workbench
  
  prompt_templates:
    - name: queue_analysis
      description: "Analyze queue health and recommend actions"
      category: guidance
  
  access_policy:
    # OPA Rego policy for Supervisor role
  
  session:
    inactivity_timeout: 60m
    max_subscriptions: 100
```

### Variation B: Agent Template

If publishing for agents:

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
  
  task_queue_scope:
    - dispute-triage-queue
    - dispute-resolution-queue
  
  prompt_templates:
    - name: dispute_triage_solver
      scenario_ref: dispute-filing
      task_type: dispute_triage
      category: task_solver
  
  access_policy:
    # OPA Rego policy for Agent role
  
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50
```

---

## Troubleshooting

### Issue: CRD Status Shows "Failed"

**Symptom:** CRD status shows `phase: Failed`

**Cause:** CRD validation failed or endpoint provisioning failed

**Solution:**
1. Check CRD for syntax errors
2. Verify scenarios exist
3. Check MCP Operator logs: `kubectl logs -n <namespace> <mcp-operator-pod>`
4. Review CRD status conditions for error details

---

### Issue: Tools Not Available in MCP Client

**Symptom:** MCP client cannot see tools

**Cause:** Access control policy too restrictive, or endpoint not provisioned

**Solution:**
1. Verify CRD status is `Provisioned`
2. Check OPA policy allows your access token
3. Verify workbench access
4. Check MCP Router logs for authorization failures

---

### Issue: Prompts Not Compiling

**Symptom:** Prompt templates fail to compile

**Cause:** Template syntax error or missing context variables

**Solution:**
1. Verify Mustache/Handlebars syntax
2. Check context variables are available (request, task, subject)
3. Test template compilation manually
4. Review prompt template format: [Prompt Templates](../../04-subsystems/mcp-channel/prompt-templates.md)

---

## Best Practices

| Practice | Rationale |
|----------|-----------|
| **Start with essential prompts** | Task solver prompts are highly recommended for good AI agent experience |
| **Test access control early** | Verify OPA policy works before publishing |
| **Use descriptive server names** | Makes directory browsing easier for collaborators |
| **Version your CRDs** | Track changes and enable rollback |
| **Document prompt templates** | Help AI agents understand when to use each prompt |

---

## Next Steps

Now that you've published an MCP Server, you may want to:

- [MCP Prompt Template Authoring](./mcp-prompt-template-authoring.md) — Learn to author effective prompts
- [Exposing Machine Tools via MCP](./exposing-machine-tools-via-mcp.md) — Expose Tool Registry tools (machine-template)
- [Journey: MCP Server Publishing](../../08-personas-and-journeys/journeys/mcp-server-publishing.md) — Understand the full journey

---

## Related Documentation

- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md) — CRD specification
- [MCP Channel Subsystem](../../04-subsystems/mcp-channel/README.md) — Subsystem overview
- [ADR-0131: MCP Server CRD Design](../../decision-logs/0131-mcp-server-crd-design.md) — Design decision
