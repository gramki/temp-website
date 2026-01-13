# Topology Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Design Desk](./README.md)  
> **Primary Persona:** [Cognitive Systems Architect (CSA)](../../../personas-and-needs/roles.md#2-cognitive-systems-architect-csa)

---

## Purpose

The Topology Console enables the **Cognitive Systems Architect (CSA)** ([role definition](../../../personas-and-needs/roles.md#2-cognitive-systems-architect-csa)) to design multi-agent systems, define interaction contracts, and analyze failure propagation across agent networks.

---

## Sections

### Agent Graph

Visual map of agent relationships and interactions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AGENT TOPOLOGY: finance-operations                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│    ┌─────────────────┐                                                      │
│    │  ORCHESTRATOR   │                                                      │
│    │ finance-router  │                                                      │
│    └────────┬────────┘                                                      │
│             │                                                               │
│    ┌────────┼────────┬────────────┐                                         │
│    │        │        │            │                                         │
│    ▼        ▼        ▼            ▼                                         │
│ ┌──────┐ ┌──────┐ ┌──────┐  ┌──────────┐                                   │
│ │invoice│ │expense│ │order │  │compliance│                                  │
│ │proc.  │ │approv.│ │valid.│  │checker   │                                  │
│ └──┬───┘ └──────┘ └──┬───┘  └──────────┘                                   │
│    │                 │                                                      │
│    ▼                 ▼                                                      │
│ ┌──────┐         ┌──────┐                                                   │
│ │ po   │         │vendor│                                                   │
│ │lookup│         │check │                                                   │
│ └──────┘         └──────┘                                                   │
│                                                                             │
│ Legend: ─▶ Delegation │ ═▶ Collaboration │ ┄▶ Advisory                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Interaction Contracts

Define message formats and protocols between agents.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ INTERACTION CONTRACT                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ Provider: finance-router  │  Consumer: invoice-processor                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ REQUEST SCHEMA                                                              │
│ ──────────────────────────────────────────────────────────────────────────  │
│ {                                                                           │
│   "type": "task_assignment",                                                │
│   "required": ["task_id", "task_type", "invoice_data"],                    │
│   "task_type": "invoice_approval",                                          │
│   "timeout": "30s"                                                          │
│ }                                                                           │
│                                                                             │
│ RESPONSE SCHEMA                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ {                                                                           │
│   "type": "task_result",                                                    │
│   "required": ["task_id", "status", "decision"],                           │
│   "status": ["completed", "escalated", "failed"]                           │
│ }                                                                           │
│                                                                             │
│ TIMING                                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • Timeout: 30s                                                              │
│ • Acknowledgment required: Yes (within 5s)                                  │
│ • Retry policy: 2 attempts with exponential backoff                        │
│                                                                             │
│ [Edit] [Validate] [Test Contract]                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Coordination Patterns

Define and apply coordination patterns.

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Hierarchical** | Single orchestrator delegates | Workflow coordination |
| **Peer-to-Peer** | Agents communicate directly | Collaboration |
| **Marketplace** | Agents bid for work | Load distribution |
| **Pipeline** | Sequential processing | Data transformation |

### Blast Radius Analysis

Model failure propagation across the agent network.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ BLAST RADIUS ANALYSIS                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ Scenario: invoice-processor fails                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ DIRECT IMPACT                                                               │
│ • Invoice processing halted                                                 │
│ • PO lookup requests queued                                                 │
│                                                                             │
│ CASCADE IMPACT                                                              │
│ • finance-router: Degraded (can route to other agents)                     │
│ • po-lookup: Idle (no incoming requests)                                   │
│                                                                             │
│ UNAFFECTED                                                                  │
│ • expense-approver                                                          │
│ • order-validator                                                           │
│ • compliance-checker                                                        │
│                                                                             │
│ MITIGATION                                                                  │
│ • Circuit breaker isolates failure                                          │
│ • finance-router falls back to human routing                               │
│ • Estimated recovery: Automatic (restart) or manual                        │
│                                                                             │
│ [Simulate Other Failures] [Export Analysis]                                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Drag-and-drop topology builder**
- **Contract validation between agents**
- **Simulation mode for interaction testing**
- **Dependency analysis and impact modeling**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Agent interaction visibility |
| **Predictable** | Contract guarantees, failure isolation |
| **Directable** | Coordination patterns, escalation routing |
| **Authority Enforceable** | Inter-agent authority boundaries |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
