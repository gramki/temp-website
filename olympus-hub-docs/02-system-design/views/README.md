# Architecture Views

> **Same system, different perspectives**

---

## Purpose

Architecture views present the Olympus Hub system from different perspectives, each tailored to specific stakeholder concerns. While the core architecture documents describe how the system works, views answer specific questions stakeholders commonly ask.

---

## Available Views

| View | Audience | Question Answered |
|------|----------|-------------------|
| [Data Flow View](./data-flow-view.md) | Data Engineers, Integration Architects | How does data move through the system? |
| [Runtime View](./runtime-view.md) | Developers, Operators | What runs where? |
| [Deployment View](./deployment-view.md) | Platform Engineers, DevOps | How is the system deployed and promoted? |
| [Security View](./security-view.md) | Security Architects, Auditors | How is the system secured? |
| [Persona Journey View](./persona-journey-view.md) | Product Managers, UX Designers | How do users experience the system? |
| [Integration View](./integration-view.md) | Enterprise Architects | How does Hub connect to external systems? |

---

## When to Use Views

### Use Views When:
- You need a focused perspective on one aspect
- You're communicating with a specific stakeholder group
- You want to answer a specific architectural question

### Use Core Docs When:
- You need to understand the complete system
- You're learning Hub architecture for the first time
- You need to understand how components interact

---

## View Relationship to Core Documents

```
                    ┌─────────────────────────┐
                    │   HUB ARCHITECTURE      │
                    │   (Executive Overview)  │
                    └───────────┬─────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│ Signal Flow   │     │  Workbench    │     │  Agent Model  │
│               │     │   Anatomy     │     │               │
└───────────────┘     └───────────────┘     └───────────────┘
        │                       │                       │
        │     CORE DOCUMENTS    │                       │
        ├───────────────────────┼───────────────────────┤
        │                       │                       │
        │       VIEWS (Curated Perspectives)            │
        │                                               │
        ▼                       ▼                       ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│  Data Flow    │     │   Runtime     │     │   Security    │
│     View      │     │     View      │     │     View      │
└───────────────┘     └───────────────┘     └───────────────┘
```

---

## Related Documentation

- [Hub Architecture](../hub-architecture.md) — Start here for overview
- [Implementation Concepts](../implementation-concepts/README.md) — Detailed concept documentation
- [Subsystems](../../04-subsystems/) — Technical subsystem details

