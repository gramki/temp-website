# Journey: MCP Server Publishing

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

This journey describes how a **Developer** publishes an MCP Server to enable AI agents to interact with Hub capabilities. It covers two paths: scenario-based templates (with request lifecycle) and tool-based templates (stateless passthrough).

---

## Overview

An MCP Server is a workbench-scoped CRD that exposes Hub capabilities via the Model Context Protocol (MCP). The publishing journey involves:

- **Design**: Identifying what to expose (scenarios, tools, prompts)
- **Configuration**: Creating MCP Server CRD
- **Access Control**: Defining OPA policies
- **Publishing**: Applying CRD, MCP Operator provisions endpoints
- **Validation**: Testing via MCP client

**Two Paths:**
1. **Scenario-based**: Expose scenarios, requests, tasks (with request lifecycle)
2. **Tool-based**: Expose Machine tools (stateless passthrough)

---

## Personas Involved

| Persona | Role | Activities |
|---------|------|------------|
| **Developer** | Primary actor | Creates MCP Server CRD, configures access, publishes |
| **Process Architect** | Optional | Defines prompt templates (for scenario-based) |
| **Supervisor** | Validator | Tests MCP Server, validates access control |

---

## Path 1: Scenario-Based Templates

### Phase 1: Design

**Developer identifies what to expose:**

1. **Scenarios**: Which scenarios should be exposed via this MCP Server?
   - Example: `bill-payment`, `recurring-payment` for payments MCP Server
   - Note: When scenarios are included, corresponding requests are automatically included

2. **Tools**: Which tools should be available?
   - Default tools are provided by template kind
   - Additional tools can be configured (if supported)

3. **Prompts**: Which prompt templates should be included?
   - Task solver prompts (essential, referenced from Scenario definitions)
   - Guidance prompts (optional, developer/PA discretion)

4. **Access Control**: Who should have access?
   - Define OPA policy based on access token claims, scopes, delegation-templates

### Phase 2: Define CRD

**Developer creates MCP Server CRD:**

```yaml
apiVersion: hub.olympus.io/v1
kind: business-user-template  # Template kind implies persona
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
    # OPA Rego policy
  
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50
```

### Phase 3: Author Prompts (Optional)

**Process Architect or Developer creates prompt templates:**

1. **Task Solver Prompts**: Defined in Scenario definitions (per task type)
   - Referenced in MCP Server CRD
   - Compiled with full request context when client requests

2. **Guidance Prompts**: Created in MCP Server CRD
   - General guidance (how to use scenarios)
   - Error handling (what went wrong, how to fix)
   - Progress updates (what's happening, what to expect)

### Phase 4: Configure Access

**Developer defines OPA policy:**

- Policy evaluates access token claims, scopes, delegation-templates
- Policy can restrict by workbench, scenario, user role, etc.
- Exact policy structure is C3-level detail

### Phase 5: Publish

**Developer applies CRD:**

```bash
kubectl apply -f payments-mcp-server.yaml
```

**MCP Operator provisions endpoint:**
1. Operator detects CRD create/update
2. Validates CRD structure
3. Provisions endpoint at MCP Channel: `/mcp/payments-workbench/payments-mcp-server`
4. Registers tools, prompts, resources
5. Updates CRD status: `Provisioned`

### Phase 6: Validate

**Supervisor or Developer tests MCP Server:**

1. **Connect via MCP Client**: Use Cursor, Claude Desktop, or custom client
2. **Test Tool Calls**: Verify tools work correctly
3. **Test Prompts**: Verify prompt templates compile correctly
4. **Test Resources**: Verify resource subscriptions work
5. **Test Access Control**: Verify OPA policy restricts access correctly

**Output:** Published MCP Server accessible via MCP Channel

---

## Path 2: Tool-Based (machine-template)

### Phase 1: Identify Tools

**Developer identifies tools to expose:**

1. **Option A: Machine Reference**
   - Expose all tools from a specific Machine
   - Example: `machine_ref: acme-core-banking`

2. **Option B: Explicit Tool List**
   - Select specific tools by ID
   - Example: `tools: [get-account, get-transaction-history, validate-account]`

**Prerequisites:**
- Machine registered in Tool Registry
- Tools available in Tool Registry
- Developer has access to Machine/tools

### Phase 2: Define CRD

**Developer creates machine-template CRD:**

```yaml
apiVersion: hub.olympus.io/v1
kind: machine-template
metadata:
  name: core-banking-mcp
  namespace: acme-bank
spec:
  server:
    name: core-banking-mcp
    display_name: "Core Banking Tools"
    description: "Expose core banking API tools to AI agents"
    version: "1.0.0"
  
  workbench_ref: payments-workbench
  
  tool_source:
    machine_ref: acme-core-banking  # Option A
    # OR
    # tools:  # Option B
    #   - get-account
    #   - get-transaction-history
  
  access_policy:
    # OPA Rego policy
```

### Phase 3: Configure Access

**Developer defines OPA policy:**

- Policy evaluates access token claims, scopes
- Policy can restrict by workbench, tool, user role
- Same OPA model as scenario-based templates

### Phase 4: Publish

**Developer applies CRD:**

```bash
kubectl apply -f core-banking-mcp.yaml
```

**MCP Operator provisions endpoint:**
1. Operator detects CRD create/update
2. Validates CRD structure
3. Resolves tool source (queries Tool Registry)
4. Provisions endpoint at MCP Channel: `/mcp/payments-workbench/core-banking-mcp`
5. Registers tools from Tool Registry
6. Configures passthrough routing to HTTP Tool Calling Application
7. Updates CRD status: `Provisioned`

### Phase 5: Validate

**Supervisor or Developer tests MCP Server:**

1. **Connect via MCP Client**: Use Cursor, Claude Desktop, or custom client
2. **Test Tool Calls**: Verify tools invoke correctly
3. **Test Access Control**: Verify OPA policy restricts access correctly
4. **Verify Stateless**: Confirm no request lifecycle (no requests created)

**Output:** Published MCP Server accessible via MCP Channel

---

## Comparison: Scenario-Based vs Tool-Based

| Aspect | Scenario-Based | Tool-Based (machine-template) |
|--------|-----------------|-------------------------------|
| **Request Lifecycle** | Full lifecycle (create, update, complete) | None (stateless) |
| **Prompts** | Task solvers, guidance prompts | Not supported |
| **Resources** | Requests, tasks, queues, etc. | Not supported |
| **Sessions** | Session-bound with subscriptions | Stateless |
| **Use Case** | Request-driven workflows | Stateless utility functions |
| **Complexity** | Higher (request lifecycle) | Lower (direct tool calls) |

---

## Related Documentation

- [Guide: Publishing MCP Server](../../10-guides/publishing-mcp-server.md) — Step-by-step guide
- [Guide: Exposing Machine Tools via MCP](../../10-guides/exposing-machine-tools-via-mcp.md) — machine-template guide
- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md) — CRD specification
- [Machine Template](../../04-subsystems/mcp-channel/machine-template.md) — Passthrough pattern

---

*TODO: Expand with detailed examples, troubleshooting, and best practices*
