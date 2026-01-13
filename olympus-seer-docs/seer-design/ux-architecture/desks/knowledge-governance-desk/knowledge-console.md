# Knowledge Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Knowledge Governance Desk](./README.md)  
> **Primary Persona:** [Knowledge & Memory Owner (KMO)](../../../personas-and-needs/roles.md#4-knowledge--memory-owner-kmo)

---

## Purpose

The Knowledge Console enables the **Knowledge & Memory Owner (KMO)** ([role definition](../../../personas-and-needs/roles.md#4-knowledge--memory-owner-kmo)) to govern knowledge sources, manage knowledge graphs, and define accuracy thresholds.

---

## Sections

### Knowledge Sources

Manage registered knowledge sources.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ KNOWLEDGE SOURCES                                          [12 Sources]     │
├─────────────────────────────────────────────────────────────────────────────┤
│ [+ Register Source] [Sync All] [Quality Report]                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Source              │ Type      │ Status    │ Last Sync    │ Quality       │
│ ───────────────────────────────────────────────────────────────────────────│
│ Policy Documents    │ Vector DB │ ✅ Active  │ 2 hours ago │ 98%           │
│ Product Catalog     │ API       │ ✅ Active  │ 5 min ago   │ 95%           │
│ HR Knowledge Base   │ Vector DB │ ✅ Active  │ 1 hour ago  │ 92%           │
│ Compliance Rules    │ Graph     │ ✅ Active  │ 1 day ago   │ 99%           │
│ Customer Data       │ API       │ ⚠️ Stale   │ 3 days ago  │ 88%           │
│ Legacy Docs         │ Vector DB │ ⚫ Archived │ N/A         │ —             │
│                                                                             │
│ [View Selected] [Edit] [Deactivate]                                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Knowledge Graph

Visualize knowledge relationships.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ KNOWLEDGE GRAPH: Expense Policies                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│              ┌────────────────┐                                             │
│              │ Expense Policy │                                             │
│              │    (v2.3)      │                                             │
│              └───────┬────────┘                                             │
│         ┌────────────┼────────────┐                                         │
│         │            │            │                                         │
│    ┌────▼────┐  ┌────▼────┐  ┌────▼────┐                                   │
│    │ Travel  │  │ Meals   │  │ Software│                                   │
│    │ Rules   │  │ Rules   │  │ Rules   │                                   │
│    └────┬────┘  └────┬────┘  └─────────┘                                   │
│         │            │                                                      │
│    ┌────▼────┐  ┌────▼────┐                                                │
│    │ Domestic│  │ Per Diem│                                                │
│    │ Limits  │  │ Limits  │                                                │
│    └─────────┘  └─────────┘                                                │
│                                                                             │
│ Entities: 45 │ Relationships: 78 │ Last Updated: 2 hours ago                │
│                                                                             │
│ [Edit Graph] [Add Entity] [Export] [Validate]                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Quality Thresholds

Define accuracy and freshness requirements.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUALITY THRESHOLDS                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ACCURACY REQUIREMENTS                                                       │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Source Type      │ Min Accuracy │ Current │ Status                         │
│ Compliance Docs  │ 99%          │ 99.2%   │ ✅ Meeting                      │
│ Policy Docs      │ 95%          │ 98.0%   │ ✅ Meeting                      │
│ Product Info     │ 90%          │ 95.0%   │ ✅ Meeting                      │
│ General KB       │ 85%          │ 92.0%   │ ✅ Meeting                      │
│                                                                             │
│ FRESHNESS REQUIREMENTS                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Source Type      │ Max Age      │ Sync Frequency │ Status                   │
│ Customer Data    │ 1 hour       │ 15 min         │ ✅ Fresh                 │
│ Product Catalog  │ 6 hours      │ 1 hour         │ ✅ Fresh                 │
│ Policy Docs      │ 24 hours     │ 6 hours        │ ✅ Fresh                 │
│ Compliance Rules │ 7 days       │ Daily          │ ⚠️ Needs sync            │
│                                                                             │
│ [Edit Thresholds] [Schedule Sync] [Alert Configuration]                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Access Controls

Manage knowledge access by agent role.

---

## Key Features

- **Multi-source knowledge registration**
- **Knowledge graph visualization and editing**
- **Quality monitoring with threshold alerts**
- **Sync scheduling and management**
- **Access control configuration**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Knowledge quality metrics visibility |
| **Predictable** | Quality thresholds ensure consistency |
| **Directable** | Knowledge source controls |
| **Authority Enforceable** | Access controls on knowledge |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
