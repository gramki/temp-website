# Information-Centric Work Patterns

> **Information-centric work** is work where the primary inputs, transformations, and outputs are information rather than physical matter.
> — [Glossary](../01-concepts/glossary.md#information-centric-work)

---

## Purpose of This Section

This section describes prominent patterns of information-centric work and how they map to Hub's ontology. Each pattern represents a common way work operates across industries and functions.

Understanding these patterns helps you:

- **Recognize** which Hub concepts apply to your domain
- **Design** Scenarios that fit how work actually operates
- **Choose** appropriate collaboration models for different situations

---

## Pattern Index

| Pattern | Focus | Key Characteristic |
|---------|-------|-------------------|
| [Queue-Based Work](./queue-based-work.md) | Throughput | Serial processing of work items with SLAs |
| [Case-Based Work](./case-based-work.md) | Investigation | Non-deterministic, collaborative resolution |
| [Conversation-Based Work](./conversation-based-work.md) | Dialogue | Real-time exchange toward understanding |
| [Event-Driven Operations](./event-driven-operations.md) | Reaction | Signal-triggered response |
| [Artifact-Centric Work](./artifact-centric-work.md) | Creation | Single artifact: draft → review → approve |
| [Review-Based Work](./review-based-work.md) | Evaluation | Assessing artifacts, decisions, or outcomes |
| [Generative/Design Work](./generative-design-work.md) | Exploration | Diverge → create variants → select → converge |

---

## How Patterns Map to Hub Ontology

Every pattern follows the same fundamental flow through Hub's ontology:

```
Work Pattern
    ↓
Scenario (goal-oriented definition)
    ↓
┌─────────────────────────────────────┐
│  Operation Type                      │
│  • Procedure (deterministic, single) │
│  • Workflow (deterministic, multi)   │
│  • Case (non-deterministic)          │
└─────────────────────────────────────┘
    ↓
Activities (steps within the operation)
    ↓
Tasks (delegated to Agents)
    ↓
Agents (Human, AI, Rules)
    ↓
Outcome
```

### Pattern → Operation Type Mapping

| Pattern | Primary Operation Type |
|---------|------------------------|
| Queue-Based | Procedure |
| Case-Based | Case |
| Conversation-Based | Case or Procedure |
| Event-Driven | Procedure or Case |
| Artifact-Centric | Workflow |
| Review-Based | Procedure |
| Generative/Design | Case |

---

## Patterns Are Not Exclusive

Real work often combines patterns:

- **Incident Response** = Event-Driven (trigger) + Case-Based (investigation)
- **Document Approval** = Artifact-Centric (lifecycle) + Review-Based (evaluation)
- **Design Sprint** = Generative (exploration) + Review-Based (selection)
- **Support Ticket** = Queue-Based (intake) + Conversation-Based (resolution)

The patterns describe the *primary* way work operates. Most scenarios involve elements of multiple patterns.

---

## Choosing the Right Pattern

| If your work... | Consider... |
|-----------------|-------------|
| Processes items from a stream with SLAs | Queue-Based |
| Requires investigation and evolving collaboration | Case-Based |
| Centers on real-time dialogue | Conversation-Based |
| Reacts to events or alerts | Event-Driven |
| Creates and iterates a single artifact | Artifact-Centric |
| Evaluates something for quality or approval | Review-Based |
| Explores options and selects among them | Generative/Design |

---

## Related

- [Glossary: Information-Centric Work](../01-concepts/glossary.md#information-centric-work)
- [Glossary: Operation](../01-concepts/glossary.md#operation)
- [Glossary: Scenario](../01-concepts/glossary.md#scenario)
- [Ontology Reference](../01-concepts/ontology-reference.md)
- [Ontology: Execution Layer](../01-concepts/ontology-3-execution-layer.md) — Procedure, Workflow, Case
