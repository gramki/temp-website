# Information-Centric Work Patterns

> **Information-centric work** is work where the primary inputs, transformations, and outputs are information rather than physical matter.
> — [Glossary](../01-concepts/glossary.md#information-centric-work)

---

## The Core Insight

**Scenarios rarely embody a single work pattern.** Real-world operations are hybrids — a loan application starts in a queue, becomes an artifact under review, and may escalate to a case requiring investigation.

Traditional BPM models processes as task sequences with routing logic. Hub models work as **situations requiring attention**, where the nature of that attention — the pattern — may evolve as work progresses.

Understanding this distinction is fundamental to modeling work in Hub.

→ **[Pattern Composition in Scenarios](./pattern-composition.md)** — How patterns combine, transition, and nest within real operations

---

## Purpose of This Section

This section describes the fundamental patterns of information-centric work and how they map to Hub's ontology. Each pattern represents a distinct way that attention is applied to work.

Understanding these patterns helps you:

- **Recognize** which Hub concepts apply to your domain
- **Design** Scenarios that reflect how work actually operates
- **Anticipate** how work will transition between patterns
- **Choose** appropriate collaboration models for different phases

---

## The Seven Patterns

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

## How Patterns Compose

Real work combines patterns. Here are common compositions:

| Scenario Type | Pattern Flow |
|---------------|--------------|
| **Loan Origination** | Queue (intake) → Artifact (documents) → Review (underwriting) ↔ Case (exceptions) |
| **Incident Response** | Event (alert) → Review (triage) → Case (investigation) → Review (PIR) → Queue (remediation) |
| **Product Development** | Generative (discovery) → Artifact (spec) → Queue (dev tasks) → Review (gates) |
| **Customer Onboarding** | Queue (provisioning) → Case (the customer) → Review (go-live) → Event (health monitoring) |

Patterns may:
- **Sequence**: One pattern completes, another begins
- **Escalate**: Simple pattern insufficient, complex pattern takes over
- **Nest**: One pattern contains another (Case contains Queue tasks)
- **Parallel**: Multiple patterns active simultaneously (Investigation + Communication)

→ See **[Pattern Composition](./pattern-composition.md)** for detailed examples with diagrams

---

## Resolution Models — Agency Is Not Required

**Work Patterns describe the nature of the situation; Resolution Models describe who resolves it.**

Designing a Scenario requires agency — it's cognitive work. Resolving a Scenario may not, if the situation is repeatable and deterministic.

**Evolution of Agency Requirements:**

```
Novel Situation          Understood Situation         Automatable Situation
     │                          │                            │
     ▼                          ▼                            ▼
Agency Essential ───────→ Agency Helpful ───────→ Agency Optional
(Cognitive work)          (Supervision/review)     (Exception only)
     │                          │                            │
     └──────────────────────────┴────────────────────────────┘
                    Learning and formalization
```

**Machines as Implicit Infrastructure:**

All resolution models may involve Machines providing capabilities (tools, commands, data access). The model describes the primary actors making decisions and driving resolution, not every participant. Machines are infrastructure for resolution, not actors in resolution.

**Any pattern can have solutions ranging from pure automation to pure agent work.** For example, a Queue-Based work pattern can be resolved through:

| Resolution Model | Description | Example |
|------------------|-------------|---------|
| **Pure Automation** | Machines process items entirely | Automated data validation and routing |
| **Automation with Exception Escalation** | Machines handle routine; agents handle exceptions | Auto-processing with human review for flagged items |
| **Human-AI Teaming** | Agents collaborate on complex items | Complex loan applications requiring judgment |

**Common Resolution Models by Pattern:**

| Pattern | Common Resolution Models |
|---------|------------------------|
| Queue-Based | Pure Automation, Automation with Exception Escalation, Human-AI Teaming |
| Case-Based | Human-AI Teaming, AI-Autonomous, Human-Supervised AI |
| Conversation-Based | Human-AI Teaming, AI-Autonomous |
| Event-Driven | Pure Automation, Automation with Exception Escalation |
| Artifact-Centric | Agent-Assisted Automation, Human-AI Teaming |
| Review-Based | Human-Supervised AI, Human-AI Teaming |
| Generative/Design | Human-AI Teaming, Pure Human Collaboration |

For the comprehensive list of resolution models, see [Glossary — Resolution Model](../01-concepts/glossary.md#resolution-model).

**Hub's value proposition isn't "agents everywhere" or "automate humans out" — it's operational infrastructure for whatever resolution model fits.**

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

| Pattern | Primary Operation Type | Notes |
|---------|------------------------|-------|
| Queue-Based | Procedure | Deterministic processing with SLAs |
| Case-Based | Case | Non-deterministic, emergent resolution |
| Conversation-Based | Case or Procedure | Depends on conversation complexity |
| Event-Driven | Procedure or Case | Simple response vs. investigation |
| Artifact-Centric | Workflow | Multi-step with handoffs |
| Review-Based | Procedure | Structured evaluation criteria |
| Generative/Design | Case | Exploratory, non-linear |

---

## Choosing Patterns

### Starting Point

| If your work... | Likely Entry Pattern |
|-----------------|---------------------|
| Receives items from a stream | Queue-Based |
| Reacts to events or alerts | Event-Driven |
| Starts with a request or inquiry | Conversation-Based |
| Begins with a problem to solve | Case-Based |
| Creates something from scratch | Generative/Design or Artifact-Centric |

### Core Work

| If the core activity is... | Likely Core Pattern |
|---------------------------|---------------------|
| Processing with known steps | Queue-Based |
| Investigating unknowns | Case-Based |
| Building a deliverable | Artifact-Centric |
| Exploring possibilities | Generative/Design |
| Maintaining dialogue | Conversation-Based |

### Decision Points

| If decisions require... | Likely Decision Pattern |
|------------------------|------------------------|
| Formal evaluation against criteria | Review-Based |
| Expert judgment | Case-Based |
| Stakeholder alignment | Conversation-Based |

---

## Agent Behavior by Pattern

Different patterns call for different agent behaviors:

| Pattern | Human Agent Focus | AI Agent Focus |
|---------|-------------------|----------------|
| Queue-Based | Prioritization, exceptions | Throughput, SLA monitoring |
| Case-Based | Investigation strategy | Hypothesis, correlation |
| Conversation-Based | Relationship, judgment | Intent, recommendations |
| Event-Driven | Escalation decisions | Pattern recognition, prediction |
| Artifact-Centric | Quality, completeness | Generation, validation |
| Review-Based | Evaluation, approval | Criteria checking, scoring |
| Generative/Design | Selection, direction | Option generation, comparison |

---

## Related

### Composition
- **[Pattern Composition](./pattern-composition.md)** — How patterns combine in real scenarios

### Definitions
- [Glossary: Information-Centric Work](../01-concepts/glossary.md#information-centric-work)
- [Glossary: Operation](../01-concepts/glossary.md#operation)
- [Glossary: Scenario](../01-concepts/glossary.md#scenario)

### Ontology
- [Ontology Reference](../01-concepts/ontology-reference.md)
- [Ontology: Execution Layer](../01-concepts/ontology-3-execution-layer.md) — Procedure, Workflow, Case
