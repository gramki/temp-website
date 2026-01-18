# Olympus Hub — Architecture Overview

> **Operational platform for governed, collaborative problem-solving by teams of Agents — Human or AI**

---

## Executive Summary

Olympus Hub is a platform for modeling, managing, and automating **information-centric work** through governed collaboration — whether Human-Human, Human-AI, or AI-AI.

All operations in information-centric work are situations that need attention, decision, or action. Hub models each such operation as a **Scenario** — a goal-oriented definition of what needs to be achieved, not a step-by-step procedure.

**What Hub Provides:**

| Dimension | What It Means |
|-----------|---------------|
| **Scenario-Oriented Operations** | Scenarios define goals; Requests are collaboration surfaces; signal-driven execution |
| **Domain Encapsulation** | Workbenches isolate business domains with their own entities, knowledge, and governance |
| **Collaboration Model** | Human-Human, Human-AI, AI-AI modalities; Hub Agent as participation pattern |
| **Persona-Channel Framework** | Multi-surface access (Web, Teams, MCP, REST); persona-focused applications |
| **Automation Platform** | Hub Applications codify logic; Machines connect to systems; Runtimes host execution |
| **Infrastructure Foundation** | Context that grounds, structure that guides, memory that learns, governance that secures trust |

**Core Proposition:** Enterprises define domain-specific **Workbenches** that encapsulate business domains. Teams of agents — human and AI alike — collaborate within these Workbenches to solve problems, achieve goals, and drive outcomes. Hub provides the unified operational model; **Olympus Seer** extends it with AI Agent capabilities (lifecycle, identity, runtime, model integration).

**Grounded in Theory:** Hub implements concepts from Agent-Oriented Systems Modeling (AOSM), providing a practical, opinionated platform for enterprise adoption. See [Design Philosophy](./hub-design-philosophy.md) for theoretical foundations. See [Glossary](../01-concepts/glossary.md) for terminology.

---

## Core Philosophy

### Collaboration as Foundation

Hub treats collaboration as the foundation of operational work. Three modalities are equally valid:

| Modality | Description |
|----------|-------------|
| **Human-Human** | Traditional teamwork — the bridge from current paradigms |
| **Human-AI** | Augmented collaboration — humans and AI agents working together |
| **AI-AI** | Autonomous coordination — AI agents collaborating under governance |

Hub provides a unified operational model for all three. There's no assumption that AI is always involved — Hub is powerful for operations automation with or without AI.

### Grounded in Agent-Oriented Systems

Hub implements concepts from **Agent-Oriented Systems Modeling (AOSM)**:

| AOSM Concept | Hub Implementation |
|--------------|-------------------|
| **Agent** | Human Agent, Rule-Based Agent, Workflow Agent, AI Agent |
| **Human-AI Team (HAT)** | Mixed teams collaborating on Requests |
| **OPD (Observability, Predictability, Directability)** | CAF audit, Scenarios, Override protocols |
| **PIDA (Perceive, Interpret, Decide, Act)** | Signal → Trigger → Scenario → Agent action |

Hub is a practical, opinionated implementation of AOSM for enterprise adoption — addressing multi-tenancy, security, compliance, memory governance, and integration concerns.

→ **Details:** [Design Philosophy](./hub-design-philosophy.md) | [AOSM Reference](../../aosm-meta-model/agent-oriented-system.md)

### Scenario-Oriented Thinking

Hub uses **scenario-oriented thinking** rather than traditional workflow design:

- **Scenarios define goals**, not procedures — agents determine how to achieve them
- **Scenarios are business situations**, not technical diagrams
- **Three specifications** govern each scenario: Normative (what ought to be), Automation (how it's codified), Deployment (how it runs)

This approach synthesizes Domain-Driven Design (DDD) and AOSM, keeping business intent explicit while enabling flexible automation.

→ **Details:** [Scenario-Oriented Thinking](../11-decision-frameworks/scenario-oriented-thinking/scenario-oriented-thinking.md)

### Workbench as Core Abstraction

The **Workbench** is the fundamental organizational unit in Olympus Hub:

| Property | Description |
|----------|-------------|
| **Domain Encapsulation** | Each Workbench encapsulates a specific business domain (e.g., Payments, Order Processing, HR Operations) |
| **System Agnostic** | Independent of underlying systems—connects to any enterprise application |
| **Entity-Centric** | Models the domain as a collection of Business Entities |
| **Action-Oriented** | Defines actions possible on those entities |
| **Agent-Enabled** | Provides the operational interface for human and AI agents |

→ **Details:** [Workbench Anatomy](./workbench-anatomy.md)

---

## System Model

### Signal-Driven Operations

All operations in Hub begin with **Signals**—inputs from the environment that indicate something requiring attention:

```
Signal → I/O Gateway → Signal Exchange → Hub Application → Task → Agent
```

| Component | Role |
|-----------|------|
| **Signal** | Input indicating change or event (Event, Exception, Observation, Request) |
| **I/O Gateway** | Senses signals from specific protocols (HTTP, events, files, schedules) |
| **Signal Exchange** | Central routing engine that matches signals to triggers |
| **Hub Application** | Automation artifact that processes the request |
| **Task** | Unit of work assigned to an agent |
| **Agent** | Human or AI executor who completes the work |

→ **Details:** [Signal Flow](./signal-flow.md)

### Scenarios and Operations

When a signal matches a **Trigger**, it creates a **Request** that activates a **Scenario**. The Scenario determines:
- Which **Roles** are involved
- Which **Automations** execute
- What **Goals** must be achieved
- Which **SOPs** govern the response

→ **Details:** [Architecture Layers](./architecture-layers.md) | [Scenario Specification Types](./implementation-concepts/scenario-specification-types.md)

### Hub Agent Model

**Hub Agent** is a participation pattern, not a technology. Any entity that satisfies these criteria is a Hub Agent:

1. **Participates in task queues** — receives work like any team member
2. **Can be assigned to Requests** — takes ownership of collaboration
3. **Has an IAM identity** — registered as Agent Persona in Cipher
4. **Produces Request updates** — reports decisions, memos, outcomes
5. **Can be enrolled/unenrolled** — Supervisor manages participation

The implementation technology varies:

| Agent Type | Suggested Runtime | Technology |
|------------|-------------------|------------|
| **Human Agent** | Consoles, Task Queues | Human judgment and action |
| **Rule-Based** | Rhea (suggested) | Business rules, decision tables |
| **Workflow** | Perseus (suggested) | Orchestration, state machines |
| **AI Agent (Seer)** | Atlantis | LLM-powered, tool-using agents |
| **External AI** | External | Any AI framework or stack |

**Note:** Runtimes are suggestions, not requirements. Organizations can build rule-based automation on Atlantis or workflows on Rhea — Hub doesn't mandate implementation technology.

→ **Details:** [Agent Model](./agent-model.md) | [Hub Agent vs Seer Agent](../11-decision-frameworks/hub-agent-vs-seer-agent/hub-agent-vs-seer-agent.md)

---

## Architectural Principles

| Principle | Description |
|-----------|-------------|
| **Framework Agnostic** | No dependency on specific enterprise systems |
| **Domain-Centric** | Workbenches encapsulate complete business domains |
| **Entity-Driven** | Operations centered on business entity lifecycle |
| **Modular** | Workbenches operate independently with clear interfaces |
| **Scalable** | Horizontal scaling for high-volume operations |
| **Secure** | Enterprise-grade security and multi-tenancy |
| **Observable** | Comprehensive monitoring across all components |
| **Resilient** | Fault tolerance and disaster recovery built-in |

---

## System Topology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              OLYMPUS HUB                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                 │
│   │  Workbench   │    │  Workbench   │    │  Workbench   │                 │
│   │  (Payments)  │    │  (Orders)    │    │    (HR)      │                 │
│   └──────┬───────┘    └──────┬───────┘    └──────┬───────┘                 │
│          │                   │                   │                          │
│          └───────────────────┼───────────────────┘                          │
│                              │                                               │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                       SIGNAL EXCHANGE                                 │   │
│   │              (Central routing and orchestration)                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│          ┌───────────────────┼───────────────────┐                          │
│          │                   │                   │                          │
│          ▼                   ▼                   ▼                          │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                 │
│   │  I/O Gateway │    │  I/O Gateway │    │  I/O Gateway │                 │
│   │  (Heracles)  │    │  (Atropos)   │    │    (Dia)     │                 │
│   │   HTTP/API   │    │    Events    │    │    Files     │                 │
│   └──────────────┘    └──────────────┘    └──────────────┘                 │
│                                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│   SUPPORTING SUBSYSTEMS                                                      │
│                                                                              │
│   ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐              │
│   │ Workbench  │ │ Operations │ │  Command   │ │ Automation │              │
│   │   Studio   │ │   Center   │ │  Registry  │ │  Runtimes  │              │
│   └────────────┘ └────────────┘ └────────────┘ └────────────┘              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Subsystem Map](./subsystem-map.md)

---

## Key Subsystems

| Subsystem | Purpose |
|-----------|---------|
| **Workbench Studio** | Design-time environment for defining Workbenches, entities, scenarios |
| **Operations Center** | Runtime environment hosting Workbenches, consoles, agent interfaces |
| **Signal Exchange** | Central routing engine matching signals to applications |
| **I/O Gateways** | Protocol-specific signal ingress/egress (Heracles, Atropos, Cronus, Dia, Kale) |
| **Command Registry** | Available commands (levers) that can be executed on entities |
| **Automation Runtimes** | Execution hosts for Hub Applications (Atlantis, Perseus, Rhea, ChronoShift) |

→ **Details:** [Subsystem Map](./subsystem-map.md) | [Subsystems Section](../04-subsystems/)

---

## Multi-Tenancy Model

Hub supports enterprise multi-tenancy with clear isolation boundaries:

```
Tenant (Enterprise)
  └── Subscription (Resource/Billing Boundary)
        └── Workbench (Domain Operational Environment)
              └── Hub Applications, Scenarios, Tasks
```

→ **Details:** [Tenant](./implementation-concepts/tenant.md) | [Subscription](./implementation-concepts/subscription.md) | [Deployment View](./views/deployment-view.md)

---

## Security Model

| Layer | Mechanism |
|-------|-----------|
| **Human IAM** | SSO integration (SAML/OIDC), RBAC scoped to Workbenches |
| **AI Agent IAM** | SPIFFE-based identity, fine-grained entity/action permissions |
| **Tool Authorization** | OAuth-like consent for agent tool access |
| **Cross-Agent** | Delegation, impersonation with explicit consent, scope limiting |
| **Audit** | Complete audit trail via Cognitive Audit Fabric |

→ **Details:** [Security View](./views/security-view.md) | [Cognitive Audit Fabric](./implementation-concepts/cognitive-audit-fabric.md)

---

## Persona-Channel Architecture

Hub uses a **persona-focused, channel-agnostic** architecture for user interaction.

### Design Principles

| Principle | What It Means |
|-----------|---------------|
| **Persona-Focused** | Each persona has dedicated applications optimized for their work |
| **Channel-Agnostic** | Same capabilities available through multiple delivery channels |
| **Use-Case Driven** | Interfaces organized by what users need to accomplish |

### Personas and Applications

| Persona | Primary Application | Focus |
|---------|---------------------|-------|
| **Agent** | Agent Desk | Task processing, decision-making |
| **Supervisor** | Supervisor Desk | Queue management, SLAs, escalations |
| **Process Architect** | Workbench Studio | Scenario design, SOPs |
| **Developer** | Workbench Studio | Hub Application implementation |
| **Administrator** | Hub Control Center | System administration |
| **Business User** | Neutrino | Request initiation, status |

### Channels

| Channel | Protocol | Use Case |
|---------|----------|----------|
| **Web Console** | Web UI | Primary interface for all personas |
| **MS Teams** | Bot Framework | Collaboration platform integration |
| **MCP** | Model Context Protocol | AI agent integration (first-class channel) |
| **REST APIs** | HTTP/REST | System-to-system, automation |

### Multi-Surface Collaboration

Hub can extend into natural work contexts through channel integration:
- **MS Teams** — Bots for persona-specific interactions (Me_Bot for agents, Ask_Bot for business users)
- **IDEs** — Future integration for developer workflows
- **Document Editors** — Future integration for document-centric work

This brings Hub's collaboration surface to where work happens, rather than requiring users to come to Hub.

→ **Details:** [Persona](./implementation-concepts/persona.md) | [Channel](./implementation-concepts/channel.md) | [MCP Channel](../01-concepts/mcp-channel.md)

---

## Enterprise Adoption

Hub addresses enterprise concerns that often block AI and automation adoption. The four pillars — context, structure, memory, governance — manifest in specific capabilities:

### What Hub Provides

| Concern | How Hub Addresses It |
|---------|---------------------|
| **Multi-tenancy** | Workbench isolation, subscription boundaries |
| **Security** | Human and Agent IAM, SPIFFE identity, access control |
| **Audit & Compliance** | Cognitive Audit Fabric (CAF), decision-grade records |
| **Governance** | OPD principles, authority limits, override protocols |
| **Integration** | Machines connect to any enterprise system |
| **Gradual Adoption** | Start human-only, progressively introduce AI |

### Memory and Knowledge Governance

A key differentiator: Hub separates **Enterprise Memory** from **Agentic Memory**.

| Dimension | Enterprise Memory | Agentic Memory |
|-----------|-------------------|----------------|
| **Scope** | Organization-wide | Session/Agent-scoped |
| **Lifecycle** | Curated, governed | Operational, transient |
| **Ownership** | Organization | Agent |
| **Purpose** | Institutional knowledge | Working memory |

Hub provides operational frameworks for memory evolution:

1. **Capture** — Agentic learning during interactions
2. **Validate** — Review and quality assurance
3. **Promote** — Elevate valuable learning to enterprise knowledge
4. **Govern** — Retention policies, access control, compliance

This is critical for operationalizing AI: organizations must govern what agents learn and what becomes institutional knowledge.

→ **Details:** [Memory Services](./implementation-concepts/memory-services.md) | [Knowledge Bank](../04-subsystems/knowledge-services/knowledge-bank.md)

---

## Hub + Seer: The Two-System Architecture

Hub and **Olympus Seer** together provide the complete platform for governed AI-Human collaboration:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         OLYMPUS PLATFORM                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────┐   ┌─────────────────────────────────────┐ │
│   │        OLYMPUS HUB          │   │          OLYMPUS SEER               │ │
│   │   (Operations Governance)   │   │      (AI Agent Governance)          │ │
│   ├─────────────────────────────┤   ├─────────────────────────────────────┤ │
│   │ • Workbenches & Domains     │   │ • Agent Lifecycle (Raw→Trained→     │ │
│   │ • Scenarios & Requests      │   │   Employed)                         │ │
│   │ • Entity Models & Knowledge │   │ • Agent Identity (SPIFFE)           │ │
│   │ • Memory (Enterprise/Agent) │   │ • Agent Runtime (Atlantis)          │ │
│   │ • Collaboration Surfaces    │   │ • AI Model Integration              │ │
│   │ • Governance & Audit (CAF)  │   │ • Tool Orchestration                │ │
│   └─────────────────────────────┘   └─────────────────────────────────────┘ │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Division of Responsibilities

| Concern | Hub | Seer |
|---------|:---:|:----:|
| What work is done (Scenarios, Requests, Goals) | ✓ | |
| Who can do it (Roles, Authority, Assignments) | ✓ | |
| How it's tracked (Audit, CAF, Compliance) | ✓ | |
| AI agent lifecycle | | ✓ |
| AI agent identity (SPIFFE) | | ✓ |
| AI model selection and routing | | ✓ |
| AI runtime hosting (Atlantis) | | ✓ |
| Enterprise and episodic memory | ✓ | |
| Agent-specific memory | | ✓ |

### Why Two Systems?

1. **Separation of concerns** — Operations governance is different from AI governance
2. **Flexibility** — Seer can integrate with any AI models; Hub can work with any agents (including non-AI)
3. **Enterprise trust** — Clear boundaries for what each system controls
4. **Independent evolution** — Each system can evolve without breaking the other

→ **Details:** [Seer Design Philosophy](../../olympus-seer-docs/why-seer/part-2-how-seer-solves/01-seer-design-philosophy/01-1-two-system-architecture.md)

---

## Document Map

This architecture overview connects to detailed documentation:

| Topic | Documents |
|-------|-----------|
| **How layers map** | [Architecture Layers](./architecture-layers.md) |
| **How signals flow** | [Signal Flow](./signal-flow.md) |
| **What's in a Workbench** | [Workbench Anatomy](./workbench-anatomy.md) |
| **How agents work** | [Agent Model](./agent-model.md) |
| **Subsystem boundaries** | [Subsystem Map](./subsystem-map.md) |
| **All concepts** | [Implementation Concepts](./implementation-concepts/README.md) |
| **All views** | [Architecture Views](./views/README.md) |

---

## Related Documentation

- [Glossary](../01-concepts/glossary.md) — Foundational terminology (Information-Centric Work, Operation, Operational Platform)
- [Vision and Mission](../00-_why/vision.md) — Why Hub exists
- [Introduction](../01-concepts/introduction.md) — Conceptual overview
- [Design Philosophy](./hub-design-philosophy.md) — Theoretical foundations (AOSM, DDD)
- [Ontology Reference](../01-concepts/ontology-reference.md) — Four-layer ontology
- [Persona](./implementation-concepts/persona.md) — Hub personas and applications
- [Channel](./implementation-concepts/channel.md) — Multi-channel access architecture
- [MCP Channel](../01-concepts/mcp-channel.md) — AI agent integration via Model Context Protocol
- [Seer Documentation](../../olympus-seer-docs/why-seer/README.md) — AI Agent platform
- [Personas and Journeys](../08-personas-and-journeys/) — Who uses Hub
- [Subsystems](../04-subsystems/) — Technical details
- [Guides](../10-guides/) — Practical how-tos
