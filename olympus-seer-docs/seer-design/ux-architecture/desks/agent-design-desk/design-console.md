# Design Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Design Desk](./README.md)  
> **Primary Persona:** [Cognitive Systems Architect (CSA)](../../../personas-and-needs/roles.md#2-cognitive-systems-architect-csa)

---

## Purpose

The Design Console is the primary workspace for the **Cognitive Systems Architect (CSA)** ([role definition](../../../personas-and-needs/roles.md#2-cognitive-systems-architect-csa)) to create cognitive architectures, manage approved patterns, document failure modes, and define design-time constraints.

---

## Sections

### Pattern Library

Approved cognitive patterns with constraints and usage guidance.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PATTERN LIBRARY                                              [6 Patterns]   │
├─────────────────────────────────────────────────────────────────────────────┤
│ [+ New Pattern] [Import] [Compare]               [Filter: Active ▼]         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Pattern          │ Status   │ Usage │ Version │ Last Updated               │
│ ───────────────────────────────────────────────────────────────────────────│
│ 📋 ReAct         │ ✅ Active │ 8     │ v2.1    │ Dec 15, 2025               │
│ 📋 Chain-of-Thought │ ✅ Active │ 5     │ v1.3    │ Nov 20, 2025            │
│ 📋 Reflection    │ ✅ Active │ 3     │ v1.1    │ Oct 10, 2025               │
│ 📋 Orchestration │ ✅ Active │ 2     │ v1.0    │ Sep 5, 2025                │
│ 📋 Decomposition │ 📝 Draft  │ 0     │ v0.5    │ Jan 10, 2026               │
│ 📋 Planning      │ ⚠️ Deprecated │ 1  │ v1.2    │ Aug 1, 2025              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Pattern Detail View:**
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PATTERN: ReAct                                              Version: v2.1   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ DESCRIPTION                                                                 │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Reason-Act-Observe loop for general-purpose agent reasoning. Agent         │
│ alternates between reasoning about the situation, taking action, and       │
│ observing results until task completion.                                    │
│                                                                             │
│ STRUCTURE                                                                   │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ┌─────────┐      ┌─────────┐      ┌─────────┐                              │
│ │ REASON  │ ───→ │   ACT   │ ───→ │ OBSERVE │ ─┐                           │
│ └─────────┘      └─────────┘      └─────────┘  │                           │
│      ↑                                          │                           │
│      └──────────────────────────────────────────┘                           │
│                                                                             │
│ CONSTRAINTS                                                                 │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • Max iterations: 10                                                        │
│ • Max time per iteration: 30s                                               │
│ • Must emit trace per step                                                  │
│ • Must validate tool permissions before ACT                                 │
│ • Must handle tool failures gracefully                                      │
│                                                                             │
│ WHEN TO USE                                                                 │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • General-purpose tasks requiring tool use                                  │
│ • Tasks with clear action-observation cycles                                │
│ • When intermediate feedback improves accuracy                              │
│                                                                             │
│ [Edit] [View History] [Deprecate] [Export]                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Architecture Builder

Visual design tool for creating agent cognitive architectures.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ARCHITECTURE BUILDER                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ Design: expense-approver-v2                              [Save] [Validate]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │                         CANVAS                                          │ │
│ │                                                                         │ │
│ │    ┌───────────┐                                                        │ │
│ │    │  INPUT    │                                                        │ │
│ │    │ Expense   │                                                        │ │
│ │    │ Request   │                                                        │ │
│ │    └─────┬─────┘                                                        │ │
│ │          │                                                              │ │
│ │    ┌─────▼─────┐                                                        │ │
│ │    │  EXTRACT  │ ← Tool: expense_parser                                 │ │
│ │    │  Details  │                                                        │ │
│ │    └─────┬─────┘                                                        │ │
│ │          │                                                              │ │
│ │    ┌─────▼─────┐     ┌───────────┐                                      │ │
│ │    │  REASON   │────→│ ESCALATE  │ if amount > ceiling                  │ │
│ │    │  (ReAct)  │     │ to Human  │                                      │ │
│ │    └─────┬─────┘     └───────────┘                                      │ │
│ │          │                                                              │ │
│ │    ┌─────▼─────┐                                                        │ │
│ │    │  DECIDE   │                                                        │ │
│ │    │ Approve/  │                                                        │ │
│ │    │ Reject    │                                                        │ │
│ │    └───────────┘                                                        │ │
│ │                                                                         │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ COMPONENT PALETTE          │ PROPERTIES                                     │
│ ─────────────────────────  │ ────────────────────────────────────────────── │
│ [INPUT] [REASON] [ACT]     │ Selected: REASON (ReAct)                       │
│ [DECIDE] [ESCALATE]        │ Pattern: ReAct v2.1                            │
│ [OUTPUT] [BRANCH]          │ Max Iterations: 5                              │
│ [TOOL] [KNOWLEDGE]         │ Timeout: 30s                                   │
│                            │ Confidence Threshold: 0.85                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Failure Mode Catalog

Document and manage failure semantics for patterns and designs.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ FAILURE MODE CATALOG                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ Pattern: [ReAct ▼]  Agent: [All ▼]                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Failure Mode         │ Detection          │ Response           │ Escalation│
│ ───────────────────────────────────────────────────────────────────────────│
│ Reasoning Loop       │ >10 iterations     │ Terminate + report │ ARE       │
│ Tool Timeout         │ >30s tool call     │ Retry (2x) → fail  │ AE        │
│ Low Confidence       │ <0.7 confidence    │ Escalate to human  │ Auto      │
│ Tool Not Found       │ Tool lookup fails  │ Graceful error     │ AE        │
│ Context Overflow     │ >token budget      │ Truncate oldest    │ None      │
│ Authority Violation  │ OPA deny           │ Escalate to human  │ ARAO      │
│                                                                             │
│ [+ Add Failure Mode] [Import from Template]                                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Constraint Definitions

Define and manage design-time constraints.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CONSTRAINT DEFINITIONS                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ STRUCTURAL CONSTRAINTS                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ Every design must have explicit INPUT and OUTPUT nodes                    │
│ ☑ REASON nodes must precede ACT nodes                                       │
│ ☑ ESCALATE paths must be defined for all DECIDE nodes                       │
│ ☑ Maximum depth of 5 nested reasoning loops                                 │
│                                                                             │
│ BEHAVIORAL CONSTRAINTS                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ All tool calls must have timeout defined                                  │
│ ☑ Retry count must be ≤ 3 for any operation                                │
│ ☑ Total execution time bounded by SLA tier                                  │
│ ☑ Token budget must be specified per design                                 │
│                                                                             │
│ OBSERVABILITY CONSTRAINTS                                                   │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ Every step must emit trace event                                          │
│ ☑ Decisions must include confidence and rationale                           │
│ ☑ Tool calls must log request/response                                      │
│                                                                             │
│ [+ Add Constraint] [Edit] [Validate Design]                                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Visual Design Editor**: Drag-and-drop architecture building
- **Pattern Templates**: Start from approved patterns
- **Constraint Validation**: Real-time constraint checking
- **Version Control**: Full history of design changes
- **Export/Import**: Share designs across teams

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Trace requirements, observability constraints |
| **Predictable** | Pattern constraints, behavioral guarantees |
| **Directable** | Escalation paths, intervention points |
| **Authority Enforceable** | Authority boundary definitions |

---

## REST API

```
Base: /api/seer/csa/v1

# Patterns
GET    /patterns                - List patterns
POST   /patterns                - Create pattern
GET    /patterns/{id}           - Get pattern
PUT    /patterns/{id}           - Update pattern

# Designs
GET    /designs                 - List designs
POST   /designs                 - Create design
GET    /designs/{id}            - Get design
PUT    /designs/{id}            - Update design
POST   /designs/{id}/validate   - Validate design

# Failure Modes
GET    /failure-modes           - List failure modes
POST   /failure-modes           - Create failure mode

# Constraints
GET    /constraints             - List constraints
POST   /constraints             - Create constraint
```

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
