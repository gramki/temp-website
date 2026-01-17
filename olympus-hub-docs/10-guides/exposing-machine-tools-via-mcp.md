# Exposing Machine Tools via MCP

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

This guide explains how to expose Machine tools from the Tool Registry via MCP using the `machine-template`. This enables stateless tool invocation without request lifecycle overhead.

---

## Overview

By the end of this guide, you will be able to:

- Create a machine-template CRD to expose Tool Registry tools
- Choose between Machine reference and explicit tool list
- Configure OPA-based access control
- Publish and validate the MCP Server

---

## Prerequisites

Before you begin, ensure you have:

- [ ] **Machine registered** — Machine is registered in Tool Registry
- [ ] **Tools in Tool Registry** — Tools are available in Tool Registry
- [ ] **Developer access** — You have Developer role in the workbench
- [ ] **kubectl access** — You can apply CRDs to the workbench namespace

### Required Knowledge

- Understanding of Tool Registry two-level model (Tool Protocols + Tools)
- Familiarity with Kubernetes CRDs
- Basic knowledge of OPA policies (for access control)

### Related Documentation

- [Machine Template](../../04-subsystems/mcp-channel/machine-template.md) — Passthrough pattern
- [Tool Registry](../../04-subsystems/registry-services/tool-registry.md) — Tool catalog
- [HTTP Tool Calling Application](../../04-subsystems/hub-native-utilities/http-tool-calling-application.md) — Native HTTP tool invocation

---

## Quick Start

If you're already familiar with machine-template, here's the quick version:

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
    version: "1.0.0"
  workbench_ref: payments-workbench
  tool_source:
    machine_ref: acme-core-banking
  access_policy:
    # OPA Rego policy
```

```bash
kubectl apply -f core-banking-mcp.yaml
```

For detailed explanations, continue to the full guide below.

---

## When to Use machine-template

**Use machine-template when:**
- You need **stateless tool invocation** (no request lifecycle)
- Tools are **utility functions** (lookups, validations, calculations)
- You want **direct tool access** without Signal Exchange overhead
- Tools are already in **Tool Registry**

**Do NOT use when:**
- You need **request lifecycle** (create, track, complete requests)
- You need **prompt templates** for guidance
- You need **resource subscriptions** for real-time updates
- Operations require **audit trails** and request history

**Use scenario-based templates instead** for request-driven workflows.

---

## Step-by-Step Guide

### Step 1: Identify Tools

**Choose which tools to expose:**

#### Option A: Machine Reference

Expose all tools from a specific Machine:

```yaml
spec:
  tool_source:
    machine_ref: acme-core-banking
```

**Use when:** You want to expose all tools from a Machine.

**What to expect:** All tools from the Machine are exposed via MCP.

**Verification:** Verify Machine exists: `kubectl get machines -n <namespace>`

#### Option B: Explicit Tool List

Select specific tools by ID:

```yaml
spec:
  tool_source:
    tools:
      - get-account
      - get-transaction-history
      - validate-account
      - initiate-payment
```

**Use when:** You want fine-grained control over which tools are exposed.

**What to expect:** Only specified tools are exposed via MCP.

**Verification:** Verify tools exist in Tool Registry.

---

### Step 2: Create machine-template CRD

**Create the CRD:**

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
    # Evaluates against access token claims, scopes, etc.
    # (exact policy structure TBD - C3 level detail)
```

**Key Points:**
- No `exposed_scenarios` (scenario-based only)
- No `prompt_templates` (not supported)
- No `session` config (stateless)
- Only `tool_source` and `access_policy`

**What to expect:** CRD ready to apply.

**Verification:** Validate YAML syntax.

---

### Step 3: Configure OPA Policy

**Define access control policy:**

```yaml
spec:
  access_policy:
    # OPA Rego policy
    # Evaluates against access token claims, scopes
    # Policy can restrict by workbench, tool, user role
    # (exact policy structure TBD - C3 level detail)
```

**Key Points:**
- Policy evaluates access token claims, scopes
- Policy can restrict by workbench, tool, user role
- Same OPA model as scenario-based templates
- Exact OPA Rego policy structure is C3-level detail

**What to expect:** Only authorized users can access tools.

**Verification:** Test access control with different user roles.

---

### Step 4: Apply CRD

**Apply the CRD:**

```bash
kubectl apply -f core-banking-mcp.yaml
```

**MCP Operator will:**
1. Validate CRD structure
2. Resolve tool source (query Tool Registry)
3. Validate tools exist and are accessible
4. Provision endpoint at MCP Channel: `/mcp/payments-workbench/core-banking-mcp`
5. Register tools from Tool Registry
6. Configure passthrough routing to HTTP Tool Calling Application
7. Update CRD status: `Provisioned`

**What to expect:** CRD status shows `Provisioned` after a few seconds.

**Verification:** Check CRD status: `kubectl get machine-template core-banking-mcp -n acme-bank -o yaml`

---

### Step 5: Verify via MCP Client

**Test the MCP Server using an MCP client:**

1. **Connect to MCP Server**: Use Cursor, Claude Desktop, or custom client
2. **List Tools**: Verify tools are available (should match Tool Registry tools)
3. **Test Tool Call**: Call a tool (e.g., `get-account`)
4. **Verify Stateless**: Confirm no request lifecycle (no requests created)
5. **Test Access Control**: Verify OPA policy restricts access correctly

**What to expect:** Tools invoke correctly, no request lifecycle overhead.

**Verification:** Verify tool calls succeed, responses are tool-native.

---

## Complete Example

### Scenario: Core Banking Tools

**Goal:** Expose core banking API tools to AI agents for stateless lookups and operations.

#### Configuration

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
    description: "Expose core banking API tools to AI agents for account lookups and transactions"
    version: "1.0.0"
  
  workbench_ref: payments-workbench
  
  # Expose all tools from core banking machine
  tool_source:
    machine_ref: acme-core-banking
  
  access_policy:
    # OPA Rego policy for tool access
    # Only operators and analysts can access
    # (C3 detail)
```

#### Exposed Tools

After applying, the following tools are available:
- `get-account` — Retrieve account details
- `get-transaction-history` — Get transaction history
- `validate-account` — Validate account status
- `initiate-payment` — Initiate payment transaction
- `check-balance` — Check account balance

#### Client Usage

```json
{
  "method": "tools/call",
  "params": {
    "name": "get-account",
    "arguments": {
      "account_id": "ACC-12345"
    }
  }
}
```

**Response:**
```json
{
  "account_id": "ACC-12345",
  "account_type": "checking",
  "balance": 5000.00,
  "status": "active"
}
```

---

## Comparison with Scenario-Based Templates

| Aspect | machine-template | Scenario-Based Templates |
|--------|------------------|--------------------------|
| **Request Lifecycle** | None (stateless) | Full lifecycle (create, update, complete) |
| **Prompts** | Not supported | Task solvers, guidance prompts |
| **Resources** | Not supported | Requests, tasks, queues, etc. |
| **Sessions** | Stateless | Session-bound with subscriptions |
| **Tool Source** | Tool Registry | Hub scenarios, requests, tasks |
| **Invocation** | Direct HTTP passthrough | Via Signal Exchange |
| **Use Case** | Stateless utility functions | Request-driven workflows |
| **Performance** | Lower latency (no request overhead) | Higher latency (request lifecycle) |
| **Audit** | Tool invocation log only | Full request history |

---

## Troubleshooting

### Issue: Tools Not Found

**Symptom:** CRD status shows `Failed` with "tools not found" error

**Cause:** Tools don't exist in Tool Registry or Machine reference is invalid

**Solution:**
1. Verify Machine exists: `kubectl get machines -n <namespace>`
2. Verify tools exist in Tool Registry
3. Check tool IDs match exactly
4. Review MCP Operator logs: `kubectl logs -n <namespace> <mcp-operator-pod>`

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

### Issue: Tool Invocation Fails

**Symptom:** Tool calls return errors

**Cause:** Tool endpoint unavailable, authentication failure, or invalid parameters

**Solution:**
1. Verify Machine tools are healthy
2. Check HTTP Tool Calling Application logs
3. Verify tool parameters match Tool Registry schema
4. Review tool invocation flow: [Machine Template](../../04-subsystems/mcp-channel/machine-template.md)

---

## Best Practices

| Practice | Rationale |
|----------|-----------|
| **Use for stateless operations** | machine-template is optimized for stateless tool calls |
| **Group related tools** | Expose tools from same Machine together |
| **Test access control** | Verify OPA policy works before publishing |
| **Monitor tool performance** | Track tool invocation latency and errors |
| **Document tool usage** | Help AI agents understand when to use each tool |

---

## Next Steps

Now that you've exposed Machine tools via MCP, you may want to:

- [Publishing MCP Server](./publishing-mcp-server.md) — Learn about scenario-based templates
- [Machine Template](../../04-subsystems/mcp-channel/machine-template.md) — Passthrough pattern details
- [Tool Registry](../../04-subsystems/registry-services/tool-registry.md) — Tool catalog

---

## Related Documentation

- [Machine Template](../../04-subsystems/mcp-channel/machine-template.md) — Passthrough pattern
- [Tool Registry](../../04-subsystems/registry-services/tool-registry.md) — Tool catalog
- [HTTP Tool Calling Application](../../04-subsystems/hub-native-utilities/http-tool-calling-application.md) — Native HTTP tool invocation
- [ADR-0135: Machine Template Passthrough Pattern](../../decision-logs/0135-machine-template-passthrough.md) — Design decision
