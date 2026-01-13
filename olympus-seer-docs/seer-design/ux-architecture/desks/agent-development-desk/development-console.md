# Development Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Development Desk](./README.md)  
> **Primary Persona:** [Agent Engineer (AE)](../../../personas-and-needs/roles.md#3-agent-engineer-ae)

---

## Purpose

The Development Console is the primary development environment for the **Agent Engineer (AE)** ([role definition](../../../personas-and-needs/roles.md#3-agent-engineer-ae)) to build agents with code, prompts, workflows, tool bindings, and telemetry.

---

## Sections

### Code & Prompts

Agent code and prompt management with versioning.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CODE & PROMPTS: invoice-processor v2.3.1                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ [System Prompt] [Task Prompts] [Tool Prompts] [Agent Code]                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ SYSTEM PROMPT                                            Version: 2.3.1     │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ You are an invoice processing agent for the Finance department.         ││
│ │                                                                         ││
│ │ Your responsibilities:                                                  ││
│ │ 1. Extract invoice details from submitted documents                     ││
│ │ 2. Validate against matching purchase orders                            ││
│ │ 3. Apply approval rules based on amount and vendor status               ││
│ │ 4. Route for human review when confidence < 85%                         ││
│ │                                                                         ││
│ │ Constraints:                                                            ││
│ │ - NEVER approve invoices > $1000 without matching PO                    ││
│ │ - ALWAYS escalate new vendors to human review                           ││
│ │ - Log all decisions with reasoning                                      ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ [Save] [Compare Versions] [Preview] [Run Test]                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Workflows

Visual workflow editor for reasoning flows.

### Tool Bindings

Connect and configure external tools.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TOOL BINDINGS                                               [5 Tools]       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Tool               │ Protocol │ Status  │ Last Tested │ Actions            │
│ ───────────────────────────────────────────────────────────────────────────│
│ extract_invoice    │ MCP      │ ✅ Ready │ 2 hours ago │ [Test] [Config]   │
│ lookup_po          │ REST     │ ✅ Ready │ 2 hours ago │ [Test] [Config]   │
│ check_vendor       │ REST     │ ✅ Ready │ 2 hours ago │ [Test] [Config]   │
│ validate_amount    │ Native   │ ✅ Ready │ 2 hours ago │ [Test] [Config]   │
│ record_decision    │ Hub API  │ ⚠️ Stale │ 1 week ago  │ [Test] [Config]   │
│                                                                             │
│ [+ Add Tool] [Test All] [Refresh Status]                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Telemetry

Configure observability contracts.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TELEMETRY CONFIGURATION                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ REQUIRED EVENTS (per ARE contract)                    Status                │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ task.started                                        ✅ Implemented        │
│ ☑ task.completed                                      ✅ Implemented        │
│ ☑ reasoning.step                                      ✅ Implemented        │
│ ☑ tool.invoked                                        ✅ Implemented        │
│ ☑ decision.made                                       ✅ Implemented        │
│ ☑ error.occurred                                      ✅ Implemented        │
│                                                                             │
│ CUSTOM EVENTS                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ invoice.extracted                                   ✅ Implemented        │
│ ☑ po.matched                                          ✅ Implemented        │
│ ☑ approval.threshold_check                            ✅ Implemented        │
│                                                                             │
│ Contract Compliance: ✅ All required events implemented                     │
│                                                                             │
│ [Validate Contract] [View Trace Sample] [Configure Custom Events]           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Feedback Inbox

Issues routed from COS/ARE for investigation.

---

## Key Features

- **Live preview of agent behavior**
- **Prompt versioning with diff view**
- **Tool binding validation (schema, auth, sandbox)**
- **Telemetry contract checker**
- **Scenario Replay for debugging**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Telemetry implementation |
| **Predictable** | Prompt versioning, test validation |
| **Directable** | Safety hook implementation |
| **Authority Enforceable** | Bound implementation |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
