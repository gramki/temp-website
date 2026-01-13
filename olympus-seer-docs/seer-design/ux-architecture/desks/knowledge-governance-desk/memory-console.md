# Memory Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Knowledge Governance Desk](./README.md)  
> **Primary Persona:** [Knowledge & Memory Owner (KMO)](../../../personas-and-needs/roles.md#4-knowledge--memory-owner-kmo)

---

## Purpose

The Memory Console enables the **Knowledge & Memory Owner (KMO)** ([role definition](../../../personas-and-needs/roles.md#4-knowledge--memory-owner-kmo)) to manage the multi-level memory system, configure retention policies, and monitor memory utilization across agents.

---

## Sections

### Memory Hierarchy

Overview of the three-tier memory system.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ MEMORY HIERARCHY                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ ENTERPRISE MEMORY (Level 3)                              Governance: KMO │ │
│ │ Promoted learnings available to all agents                              │ │
│ │ Entries: 2,450 │ Size: 45 GB │ Last Promotion: 2 hours ago              │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                            ▲                                                │
│                            │ Promotion                                      │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ AGENT CLASS MEMORY (Level 2)                   Governance: APO + KMO    │ │
│ │ Shared learnings across agents of same type                             │ │
│ │ Classes: 12 │ Total Entries: 8,200 │ Avg per Class: 683                 │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                            ▲                                                │
│                            │ Promotion                                      │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ AGENT INSTANCE MEMORY (Level 1)                     Governance: Agent   │ │
│ │ Individual agent working memory                                         │ │
│ │ Agents: 45 │ Total Entries: 125,000 │ Avg per Agent: 2,778              │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ [View Details] [Configure Promotion] [Analytics]                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Retention Policies

Configure memory retention by level and type.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ RETENTION POLICIES                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ LEVEL 1: Agent Instance Memory                                              │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Type                │ Retention   │ Conditions           │ Actions          │
│ Task Context        │ 24 hours    │ Task completed       │ Archive/Delete   │
│ Session State       │ 7 days      │ Session ended        │ Delete           │
│ Learning Candidates │ 30 days     │ Not promoted         │ Archive          │
│                                                                             │
│ LEVEL 2: Agent Class Memory                                                 │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Type                │ Retention   │ Conditions           │ Actions          │
│ Promoted Learnings  │ 180 days    │ Promotion threshold  │ Review/Promote   │
│ Shared Patterns     │ 1 year      │ Usage frequency      │ Archive          │
│                                                                             │
│ LEVEL 3: Enterprise Memory                                                  │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Type                │ Retention   │ Conditions           │ Actions          │
│ Enterprise Facts    │ Permanent   │ N/A                  │ Version          │
│ Policy Rules        │ Permanent   │ Policy change        │ Version          │
│ Deprecated          │ 2 years     │ Superseded           │ Archive          │
│                                                                             │
│ [Edit Policies] [Preview Cleanup] [Execute Cleanup]                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Utilization Monitor

Memory usage across the system.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ MEMORY UTILIZATION                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ OVERALL                                          Used: 78 GB / 100 GB (78%) │
│ ████████████████████████████████████████░░░░░░░░░░░░                        │
│                                                                             │
│ BY LEVEL                                                                    │
│ ──────────────────────────────────────────────────────────────────────────  │
│ L3 Enterprise    ████████████████░░░░░░░░░░░░░░   45 GB / 50 GB  (90%)  ⚠️ │
│ L2 Agent Class   ██████████░░░░░░░░░░░░░░░░░░░░   23 GB / 30 GB  (77%)  ✅ │
│ L1 Instance      ████░░░░░░░░░░░░░░░░░░░░░░░░░░   10 GB / 20 GB  (50%)  ✅ │
│                                                                             │
│ TOP CONSUMERS                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ 1. customer-service-agent    │ 5.2 GB │ 45,000 entries                     │
│ 2. invoice-processor         │ 3.8 GB │ 32,000 entries                     │
│ 3. compliance-checker        │ 3.1 GB │ 28,000 entries                     │
│                                                                             │
│ [Detailed Report] [Forecast] [Cleanup Recommendations]                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Hierarchical memory visualization**
- **Retention policy management**
- **Utilization monitoring with alerts**
- **Cleanup scheduling and execution**
- **Memory promotion configuration**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Memory utilization visibility |
| **Predictable** | Retention policies ensure consistency |
| **Directable** | Memory cleanup controls |
| **Authority Enforceable** | Memory access governance |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
