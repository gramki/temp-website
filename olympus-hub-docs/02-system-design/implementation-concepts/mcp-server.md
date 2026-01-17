# MCP Server

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

An MCP Server is a **workbench-scoped configuration layer** that exposes Hub capabilities via the Model Context Protocol (MCP). It is defined as a Kubernetes CRD and provisions endpoints at the MCP Channel platform service.

---

## What is an MCP Server?

An MCP Server is a **configuration resource** (CRD) that:

- Defines what Hub capabilities are exposed via MCP
- Specifies which scenarios, tools, prompts, and resources are available
- Configures access control via OPA policies
- Manages session settings (for scenario-based templates)

**Key Distinction:**
- **MCP Server** = Workbench-scoped CRD (configuration)
- **MCP Channel** = Platform service (infrastructure)

---

## Relationship to MCP Channel

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP CHANNEL                                  │
│                  (Platform Service)                             │
│  - Infrastructure for MCP Servers                              │
│  - Session Management                                           │
│  - Resource Subscriptions                                       │
│  - Directory Service                                            │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ MCP Operator provisions endpoints
                             │ based on CRDs
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MCP SERVERS                                  │
│              (Workbench-scoped CRDs)                            │
│  - business-user-template                                       │
│  - supervisor-template                                          │
│  - agent-template                                               │
│  - creator-template                                             │
│  - admin-template                                               │
│  - auditor-template                                             │
│  - machine-template                                             │
└─────────────────────────────────────────────────────────────────┘
```

**Flow:**
1. Developer creates MCP Server CRD
2. MCP Operator watches CRD
3. MCP Operator provisions endpoint at MCP Channel
4. MCP Channel exposes MCP Server to clients

---

## CRD-Based Configuration

MCP Servers are defined as Kubernetes CRDs:

```yaml
apiVersion: hub.olympus.io/v1
kind: business-user-template  # Template kind
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
  
  prompt_templates:
    - name: how_to_initiate_request
      description: "Guidance on how to initiate a request"
  
  access_policy:
    # OPA Rego policy
  
  session:
    inactivity_timeout: 30m
    max_subscriptions: 50
```

**Key Points:**
- Template kind implies persona and capabilities
- Scenarios automatically include corresponding requests
- OPA-based access control
- Session configuration (for scenario-based templates)

---

## Two Categories

MCP Servers fall into two categories based on template kind:

### Scenario-Based Templates (Request Lifecycle)

These templates expose Hub scenarios, requests, tasks, and resources with full request lifecycle management:

- `business-user-template` — Request initiation and participation
- `supervisor-template` — Queue management, agent oversight
- `agent-template` — Task processing, knowledge access
- `creator-template` — Scenario design, development
- `admin-template` — Subscription/resource management
- `auditor-template` — Compliance, investigation

**Characteristics:**
- Full request lifecycle (create, update, complete)
- Prompt templates for task solving and guidance
- Resource subscriptions for real-time updates
- Session management (OAuth, lifecycle)

### Tool-Based Templates (Passthrough)

These templates expose Tool Registry tools directly, with no request lifecycle:

- `machine-template` — Expose Machine tools via MCP

**Characteristics:**
- Stateless tool invocation
- No request lifecycle
- No prompts, no resources, no sessions
- Direct passthrough to HTTP Tool Calling Application

---

## MCP Operator Provisions Endpoints

The MCP Operator watches MCP Server CRDs and provisions endpoints:

```
1. Operator detects CRD create/update
2. Validates CRD structure
3. Provisions endpoint at MCP Channel: /mcp/{workbench}/{server-name}
4. Registers tools, prompts, resources (per template kind)
5. Updates CRD status: Provisioned
```

**For machine-template:**
- Resolves tool source (queries Tool Registry)
- Registers tools from Tool Registry
- Configures passthrough routing to HTTP Tool Calling Application

---

## Tools, Prompts, Resources

MCP Servers expose different constructs per template kind:

| Template Kind | Tools | Prompts | Resources |
|---------------|-------|---------|-----------|
| `business-user-template` | Request initiation/participation | Task solvers, guidance | Requests |
| `supervisor-template` | Queue mgmt, SLAs, directability | Queue analysis | Queues, escalations |
| `agent-template` | Task processing, knowledge | Task solvers | Tasks, requests |
| `creator-template` | Scenario design, feedback | Design guides | Scenarios, feedback |
| `admin-template` | Subscription mgmt | Resource optimization | Workbenches |
| `auditor-template` | Decision investigation | Investigation guides | Audit trails |
| `machine-template` | From Tool Registry | None | None |

---

## machine-template Integration

The `machine-template` integrates with:

- **Tool Registry**: Tool discovery and resolution
- **HTTP Tool Calling Application**: Native HTTP tool invocation
- **MCP Router**: Gateway pattern (authentication, protocol translation)

**Flow:**
```
MCP Client → MCP Router (auth, protocol) → HTTP Tool Calling Application → Machine Tools
```

---

## Related Documentation

- [MCP Channel Subsystem](../../04-subsystems/mcp-channel/README.md) — Detailed subsystem documentation
- [MCP Server CRD](../../04-subsystems/mcp-channel/mcp-server-crd.md) — CRD specification
- [Machine Template](../../04-subsystems/mcp-channel/machine-template.md) — Passthrough pattern
- [MCP Channel Concept](../../01-concepts/mcp-channel.md) — Concept overview
- [ADR-0131: MCP Server CRD Design](../../decision-logs/0131-mcp-server-crd-design.md) — Design decision

---

*TODO: Expand with architectural details, integration patterns, and runtime behavior*
