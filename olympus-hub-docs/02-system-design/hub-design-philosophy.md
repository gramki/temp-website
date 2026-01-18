# Hub Design Philosophy

> For those who want to understand the theoretical foundations

---

## Why This Document

The [Architecture Overview](./hub-architecture.md) tells you **what** Hub is.

This document tells you **why** it's designed this way.

Read this if you want:
- Deeper understanding of Hub's conceptual foundations
- Context for design decisions
- Connections to established frameworks (AOSM, DDD)

---

## Theoretical Foundations

Hub doesn't invent its concepts from scratch. It builds on two established frameworks:

### Agent-Oriented Systems Modeling (AOSM)

**What is AOSM?**

AOSM is a meta-model for designing systems where humans and AI work together as agents pursuing goals. It comes from:

> Sterling, L., & Taveter, K. (2009). *The Art of Agent-Oriented Modeling*  
> *Integrating Artificial and Human Intelligence through Agent-Oriented Systems Design* (CRC Press)

**Key Concepts:**

| AOSM Concept | Definition | Hub Implementation |
|--------------|------------|-------------------|
| **Agent** | Entity that perceives environment and acts in pursuit of goals | Human Agent, Rule-Based Agent, Workflow Agent, AI Agent |
| **Human-AI Team (HAT)** | Two or more agents working interdependently | Mixed teams on Requests |
| **OPD** | Observability, Predictability, Directability — requirements for trusted autonomy | CAF audit, Scenarios with SOPs, Override protocols |
| **PIDA** | Perceive, Interpret, Decide, Act — the agent cognition cycle | Signal → Trigger → Scenario → Agent action |
| **Capability (KSA)** | Knowledge, Skills, Abilities an agent brings | Training Spec, Skill definitions, Tool access |

**Why AOSM Matters:**

Traditional BPM treats humans as "task boxes" — interchangeable resources that complete steps. AOSM treats agents as:
- **Goal-directed** — they pursue outcomes, not just execute steps
- **Autonomous within bounds** — they exercise judgment
- **Capable** — they bring knowledge and skills
- **Collaborative** — they work with other agents

This is essential for AI integration: AI agents aren't just faster task executors; they're collaborators with capabilities and limits.

→ **Full Reference:** [Agent-Oriented System](../../aosm-meta-model/agent-oriented-system.md)

---

### Domain-Driven Design (DDD)

**What is DDD?**

DDD is an approach to software design that keeps business concepts explicit and central. Key ideas:

| DDD Concept | Hub Implementation |
|-------------|-------------------|
| **Bounded Context** | Workbench — each domain has its own language, rules, entities |
| **Ubiquitous Language** | Normative Specification — business and tech share vocabulary |
| **Domain Events** | Signals — events that trigger scenarios |
| **Aggregates** | Scenarios — cohesive operational units with clear boundaries |

**Why DDD Matters:**

DDD solved a core problem: business intent gets lost when translated to code. Hub applies this insight:
- **Scenarios ARE business situations** — not technical workflow diagrams
- **Normative specs use business language** — stakeholders can read and validate them
- **Domain boundaries are explicit** — integration across domains is deliberate

---

## Design Principles

### Scenario-Oriented Thinking

Hub uses **scenarios** rather than **workflows** as the primary design unit.

| Workflow Thinking | Scenario Thinking |
|-------------------|-------------------|
| Define the steps | Define the goal |
| Prescribe the sequence | Prescribe the constraints |
| Human executes the flow | Agent achieves the outcome |
| Exceptions are errors | Exceptions are variations |

**The Three Specifications:**

Each scenario has three specification types:

1. **Normative Specification** — What ought to be done (goals, roles, SOPs, decision criteria)
2. **Automation Specification** — How it's codified (Hub Application, triggers, tool bindings)
3. **Deployment Specification** — How it runs (task queues, agent enrollment, SLA parameters)

This separation keeps business intent (normative) independent from technical implementation (automation, deployment).

→ **Details:** [Scenario-Oriented Thinking](../11-decision-frameworks/scenario-oriented-thinking/scenario-oriented-thinking.md)

---

### Agent Abstraction

Hub Agent is a **participation pattern**, not a technology.

**Why this matters:**

- Hub doesn't care if your agent is human, rule-based, workflow-based, or AI-powered
- The same operational model applies to all
- Organizations can start with humans, add AI incrementally
- Future technologies fit without redesigning Hub

**Implication:** Seer Agents (AI) are one type of Hub Agent. Hub works equally well with human-only teams.

→ **Details:** [Hub Agent vs Seer Agent](../11-decision-frameworks/hub-agent-vs-seer-agent/hub-agent-vs-seer-agent.md)

---

### Memory and Knowledge

Hub implements a structured approach to organizational memory:

**Memory Types (ESPP Taxonomy):**

| Type | What It Captures | Example |
|------|------------------|---------|
| **Episodic** | What happened | Past interactions, decisions, outcomes |
| **Semantic** | What is true | Domain knowledge, entity relationships |
| **Procedural** | How to do things | Workflows, skills, escalation patterns |
| **Preference** | What is preferred | User preferences, learned biases |

**Memory Scopes:**

| Scope | Ownership | Lifecycle |
|-------|-----------|-----------|
| **Enterprise Memory** | Organization | Curated, governed, persistent |
| **Agentic Memory** | Agent | Session-scoped, operational |
| **User Memory** | User | Personal, never cross-tenant |

**Why This Matters:**

Most AI platforms conflate these. Hub separates them because:
- Agents should learn (agentic memory)
- Organizations should govern what becomes institutional knowledge (enterprise memory)
- The promotion path (agentic → enterprise) must be explicit and auditable

---

### Governance by Design

Hub implements **OPD** (Observability, Predictability, Directability) from AOSM:

| Principle | Meaning | Hub Implementation |
|-----------|---------|-------------------|
| **Observability** | Humans can see what agents are doing | CAF audit, decision records, real-time dashboards |
| **Predictability** | Agent behavior follows defined patterns | Scenarios, SOPs, guardrails, authority limits |
| **Directability** | Humans can intervene and override | Kill-switch, escalation, re-assignment, policy changes |

The **Cognitive Audit Fabric (CAF)** is Hub's control plane for governance — providing decision-grade audit records that meet regulatory requirements.

---

## Enterprise Concerns Addressed

Hub is a practical, opinionated implementation of AOSM for enterprise use. It addresses:

| Concern | How Hub Addresses It |
|---------|---------------------|
| **Multi-tenancy** | Tenant → Subscription → Workbench isolation |
| **Security** | Human IAM (SSO), Agent IAM (SPIFFE), tool authorization |
| **Compliance** | CAF audit trail, decision records, retention policies |
| **Integration** | Machines connect to any enterprise system |
| **Scale** | Horizontal scaling, high-availability architecture |
| **Gradual Adoption** | Start human-only, add automation incrementally |
| **Memory Governance** | Explicit enterprise vs. agentic memory with promotion workflows |

---

## Further Reading

### AOSM Foundation
- [Agent-Oriented System](../../aosm-meta-model/agent-oriented-system.md) — Full AOSM reference
- [Raw, Trained, Employed Agents](../../aosm-meta-model/raw-trained-employed-agents.md) — Agent lifecycle model

### Decision Frameworks
- [Scenario-Oriented Thinking](../11-decision-frameworks/scenario-oriented-thinking/scenario-oriented-thinking.md) — Design approach
- [Hub Agent vs Seer Agent](../11-decision-frameworks/hub-agent-vs-seer-agent/hub-agent-vs-seer-agent.md) — Agent model

### Ontology
- [Ontology Reference](../01-concepts/ontology-reference.md) — Four-layer ontology
- [Perception Layer](../01-concepts/ontology-1-perception-layer.md)
- [Normative Layer](../01-concepts/ontology-2-normative-layer.md)
- [Execution Layer](../01-concepts/ontology-3-execution-layer.md)
- [Automation Layer](../01-concepts/ontology-4-automation-layer.md)

### Architecture
- [Hub Architecture](./hub-architecture.md) — System overview
- [Workbench Anatomy](./workbench-anatomy.md) — Core abstraction
