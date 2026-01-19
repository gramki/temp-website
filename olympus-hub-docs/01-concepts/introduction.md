# Introduction to Olympus Hub

## What is Olympus Hub?

Olympus Hub is a platform for modeling, managing, and automating **information-centric work** through governed collaboration.

All operations in information-centric work are situations that need attention, decision, or action. Hub models each such operation as a **Scenario** — a goal-oriented definition of what needs to be achieved, not a step-by-step procedure.

> **Vision:** To empower organizations to reimagine information-centric work through governed AI-Human collaboration.
>
> **Mission:** We build the infrastructure that makes AI-Human collaboration operational: context that grounds, structure that guides, memory that learns, and governance that secures trust.

**Grounded in Theory:** Hub implements concepts from Agent-Oriented Systems Modeling (AOSM), providing a principled approach to human-AI teamwork. It uses scenario-oriented thinking rather than traditional workflow design.

For the full vision narrative, see [Vision and Mission](../00-_why/vision.md). For theoretical foundations, see [Design Philosophy](../02-system-design/hub-design-philosophy.md). For terminology, see [Glossary](./glossary.md).

---

## What Hub Provides

Hub is an **operational platform** with six dimensions:

| Dimension | What It Provides |
|-----------|------------------|
| **Scenario-Oriented Operations** | Scenarios define goals; Requests are collaboration surfaces; signal-driven execution |
| **Domain Encapsulation** | Workbenches isolate business domains with their own entities, knowledge, and governance |
| **Resolution Spectrum** | Pure automation through human collaboration; Hub Agent as participation pattern |
| **Persona-Channel Framework** | Multi-surface access (Web, Teams, MCP, REST); persona-focused applications |
| **Automation Platform** | Hub Applications codify logic; Machines connect to systems; Runtimes host execution |
| **Infrastructure Foundation** | Context that grounds, structure that guides, memory that learns, governance that secures trust |

The last dimension — the infrastructure foundation — is what makes the first five work. Without context, agents are strangers. Without memory, organizations can't learn.

---

## The Problem Hub Solves

AI models are powerful. They can reason, learn, and act. But when organizations try to deploy AI into real operations, they discover what's missing.

**Where does the AI get domain knowledge?** Without context, an AI that knows nothing about your business is just a clever stranger.

**How does it know the process?** Without structure, AI integrated ad-hoc into systems creates fragmentation, not transformation.

**What happens when it's uncertain?** Without governance, there's no consistent model for escalation, override, or accountability.

**How do we improve over time?** Without memory, every decision starts from scratch. Organizations can't learn.

These aren't AI problems. They're infrastructure problems.

**Hub provides the operational platform that connects AI capability to business reality.**

---

## The Infrastructure Foundation

The four pillars of Hub's infrastructure make everything else possible:

### Context That Grounds

Knowledge banks that capture domain understanding. Entity models that represent business objects. Relationships that connect concepts. Grounding mechanisms that anchor every AI interaction in your specific reality.

*AI agents that understand your world, not just the world in general.*

### Structure That Guides

Scenarios that define goals. Triggers that determine when to engage. Authority definitions that set boundaries. Escalation paths that ensure oversight. A unified ontology that makes all of this coherent.

*AI agents that operate within clear boundaries, predictably and systematically.*

### Memory That Learns

Episodic memory that recalls past interactions. Semantic memory that retains knowledge. Procedural memory that captures how things are done. Preference memory that remembers what matters to whom.

*AI agents that learn from experience — and organizational knowledge that isn't lost.*

### Governance That Secures Trust

Authority definitions, traceable decision records, auditable action logs, compliance mechanisms, human override capabilities. Security through workbench isolation, agent identity, and access control. Privacy through consent-aware handling and data residency.

*AI collaboration that organizations — and their customers — can trust.*

---

## How Hub Works

### The Operational Pattern

Every operation in Hub follows the same fundamental flow:

```
Signal → Trigger → Scenario → Request → Resolution (Agent collaboration when required) → Outcome
```

1. **Signals** emerge from the environment — events, requests, observations, schedules, or human intent
2. **Triggers** interpret these signals and determine what should happen
3. **Scenarios** define the goals to be achieved and the rules of engagement
4. **Requests** become collaboration surfaces where agents (human and AI) work together when needed
5. **Resolution** occurs through agents collaborating (when required) or pure automation, using shared context and tools
6. **Outcomes** are recorded, decisions are traced, and learning is captured

### The Four-Layer Ontology

Hub models work across four interconnected layers:

| Layer | Question | What It Contains |
|-------|----------|------------------|
| **Perception** | What's happening? | Signals, Triggers, Scenarios |
| **Normative** | What ought to be done? | Roles, Goals, SOPs, Responsibilities |
| **Execution** | How is it done? | Requests, Activities, Actions, Agent collaboration (when required) |
| **Automation** | How is it codified? | Hub Applications, Machines, Tools, Runtimes |

This ontology applies universally — whether you're processing a loan application, responding to a security incident, or managing a customer service case.

### Workbenches: The Operational Unit

A **Workbench** is Hub's fundamental unit of organization. Each Workbench encapsulates:

- A business domain (e.g., IT Operations, Lending, Claims)
- The entities relevant to that domain
- The scenarios that operate within it
- The agents (human and AI) who collaborate there
- The knowledge, memory, and governance specific to that domain

Workbenches provide isolation while enabling composition. An enterprise might have dozens of Workbenches, each governing its own domain, with controlled interactions between them.

---

## What Hub Enables

### Information-Centric Work

Hub is designed for **information-centric work** — work where the primary inputs, transformations, and outputs are information rather than physical matter.

**Examples of information-centric work:**
- Processing a request and making a disposition decision
- Translating requirements into a design or implementation
- Drafting, reviewing, and approving documents or code
- Investigating an issue and determining root cause
- Coordinating between parties to resolve a problem

This includes software development, financial services, healthcare administration, IT operations, HR, legal, and enterprise knowledge work. It's where AI can contribute most — and where the infrastructure for governed collaboration matters most.

→ See [Glossary — Information-Centric Work](./glossary.md#information-centric-work) for the formal definition.

### How Work Gets Resolved

Hub unifies what enterprises traditionally separate. What's called "integration" (machine-to-machine) and "collaboration" (humans working together) are both ways of getting work done. Hub provides the same infrastructure for all of them.

**The Resolution Spectrum:**

| Resolution Model | Who Participates | Traditional Term |
|------------------|------------------|------------------|
| **Pure Automation** | Machines only | Integration, ETL, batch processing |
| **Automation with Escalation** | Machines + agents for exceptions | Integration with exception handling |
| **Human-AI Teaming** | Humans and AI throughout | AI-assisted operations |
| **AI-Autonomous** | AI agents within governance | Intelligent automation |
| **Pure Human** | Humans with platform support | Traditional teamwork, collaboration |

Not all work requires agents. Many Scenarios resolve entirely through machines — the "happy path" is pure automation. Agents engage when judgment is needed: business exceptions, authority thresholds, novel situations.

For the full taxonomy, see [Glossary — Resolution Model](./glossary.md#resolution-model).

**When Agents Participate, They Share:**

- **Context** — Same view of the Request and its state
- **Tools** — Access to the same Machines and capabilities
- **Goals** — Working toward the same Scenario outcomes
- **Memory** — Shared knowledge and episodic context

This isn't AI replacing humans or humans supervising AI. It's genuine teaming — each contributing what they do best, governed by shared rules. Organizations can start anywhere on the spectrum and evolve.

**Across All Work Types:**

| Work Type | Typical Resolution Model |
|-----------|-------------------------|
| **Pure automation** | Machine-only, agents for exceptions |
| **Structured processes** | Automation with checkpoints |
| **Semi-structured work** | Human-AI teaming |
| **Exploratory work** | Human-led with AI assistance |
| **Creative work** | Human collaboration with tool support |

The governance model adapts — structured work may be highly automated; exploratory work may have minimal automation but rich context and memory support.

### Persona-Channel Framework

Hub meets users where they work through a **persona-focused, channel-agnostic** architecture:

**Persona-Focused:** Each role has dedicated applications optimized for their work:
- **Agent Desk** — Task processing for agents handling work
- **Supervisor Desk** — Queue management, SLAs, escalations
- **Workbench Studio** — Scenario design for Process Architects
- **Hub Control Center** — Administration and operations

**Channel-Agnostic:** The same capabilities are accessible through multiple channels:

| Channel | Use Case |
|---------|----------|
| **Web Console** | Primary interface for desk applications |
| **MS Teams** | Collaboration platform integration (bots, notifications) |
| **MCP** | AI agent integration (Model Context Protocol) |
| **REST APIs** | System-to-system integration |

**Multi-Surface Collaboration:** Hub can extend into natural work contexts — MS Teams, document editors, IDEs — bringing collaboration surfaces to where work happens, rather than requiring users to come to Hub.

→ See [Persona](../02-system-design/implementation-concepts/persona.md) and [Channel](../02-system-design/implementation-concepts/channel.md) for details.

---

## What Hub Is Not

### Not a Workflow Engine

Traditional workflow engines define rigid sequences of steps. Hub defines **goals and governance** — agents (human and AI) determine how to achieve them. Hub is goal-oriented, not procedure-oriented.

### Not an AI Model Provider

Hub doesn't provide AI models. It provides the infrastructure that makes AI models **operationally useful** — context, structure, memory, and governance. Hub integrates with AI model providers through Olympus Seer.

### Not a Replacement for Enterprise Systems

Hub doesn't replace your ERP, CRM, ITSM, or other enterprise systems. It provides the **collaboration layer** where humans and AI work together, connecting to those systems through Machines and integrations.

### Not Just for "Operations"

While Hub excels at operational work, it's not limited to traditional "ops." Any information-centric work that benefits from context, structure, memory, and governance can be modeled in Hub — including research, analysis, and creative collaboration.

---

## Hub + Seer: The Complete Picture

Olympus Hub works together with **Olympus Seer**, the AI Agent platform:

| Concern | Who Handles It |
|---------|----------------|
| **Agent Governance** — Lifecycle, identity, authority, runtime | Seer |
| **Operations Governance** — Scenarios, requests, collaboration, audit | Hub |
| **AI Models** — Selection, invocation, prompt management | Seer |
| **Business Context** — Entities, knowledge, memory, processes | Hub |

Together, Hub and Seer provide the complete infrastructure for governed AI-Human collaboration.

For details on Seer, see the [Seer Documentation](../../olympus-seer-docs/why-seer/README.md).

---

## Next Steps

| Document | What You'll Learn |
|----------|-------------------|
| [Glossary](./glossary.md) | Foundational terminology (Information-Centric Work, Operation, Operational Platform) |
| [Vision and Mission](../00-_why/vision.md) | The full vision narrative and mission explanation |
| [Ontology Reference](./ontology-reference.md) | Deep dive into the four-layer ontology |
| [Workbench Anatomy](../02-system-design/workbench-anatomy.md) | How Workbenches are structured |
| [Hub Architecture](../02-system-design/hub-architecture.md) | System design overview |
| [Persona](../02-system-design/implementation-concepts/persona.md) | Hub personas and their applications |
| [Channel](../02-system-design/implementation-concepts/channel.md) | Multi-channel access architecture |
| [MCP Channel](./mcp-channel.md) | AI agent integration via Model Context Protocol |
| [Applicability Guide](./olympus-hub-applicability-guide.md) | Where Hub delivers value |

---

*This document provides the conceptual introduction. For detailed system specifications, see the [System Design](../02-system-design/README.md) documentation.*
