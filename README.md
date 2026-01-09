# Olympus Hub & Seer Design Documentation

> **Design documentation for Olympus Hub and Olympus Seer**

This repository contains the design documentation for **Olympus Hub** (operations management platform) and **Olympus Seer** (AI agent engine).

→ **For the broader Olympus platform:** See [Olympus Academy](http://academy.olympus.tech)

---

## 🎯 What's In This Repository?

This repository documents two products within the Olympus ecosystem:

| Product | Purpose | Documentation |
|---------|---------|---------------|
| **Olympus Hub** | Operations management platform for modeling, managing, and optimizing business operations through human-AI collaboration | [olympus-hub-docs/](./olympus-hub-docs/) |
| **Olympus Seer** | AI agent engine for hosting, governing, and operating AI agents with enterprise-grade controls | [olympus-seer-docs/](./olympus-seer-docs/) |

Both products are designed using **Agent-Oriented Systems Modeling (AOSM)** principles, documented in [aosm-meta-model/](./aosm-meta-model/).

---

## 🏛️ The AOSM Foundation

**Agent-Oriented Systems Modeling (AOSM)** is the meta-model that underpins Olympus. It defines:

- **Agents** — Entities (human or AI) that perceive, interpret, decide, and act
- **Goals** — What the system aims to achieve
- **Roles** — Responsibilities assigned to agents
- **Environments** — The context in which agents operate
- **Human-AI Teams (HAT)** — Collaborative structures of interdependent agents

### Key Principle: Controlled Autonomy

> AI agents act autonomously only to the extent beneficial to the human who controls them.

This principle ensures that AI augments human capability while maintaining accountability and governance.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           AOSM META-MODEL                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ENVIRONMENT                                                               │
│   └── DOMAIN                                                                │
│       └── SYSTEM (Human-AI Team)                                            │
│           ├── GOALS (What to achieve)                                       │
│           ├── ROLES (Responsibilities)                                       │
│           ├── AGENTS (Human + AI)                                           │
│           │   ├── Perceive → Interpret → Decide → Act (PIDA)                │
│           │   └── Controlled Autonomy                                        │
│           └── INTERACTIONS (Collaboration patterns)                          │
│                                                                              │
│   ────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│   OLYMPUS HUB                    OLYMPUS SEER                               │
│   ├── Workbenches                ├── Agent Lifecycle                         │
│   ├── Scenarios                  ├── Training & Employment                   │
│   ├── Signals & Triggers         ├── Guardrails & Authority                  │
│   ├── Hub Applications           ├── Runtime & Observability                 │
│   └── Human-AI Task Queues       └── Model Gateway                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

→ **Start Here:** [Agent-Oriented Systems](./aosm-meta-model/agent-oriented-system.md)

---

## 📚 Repository Structure

```
design-docs/
│
├── README.md                      # This file — repository overview
│
├── aosm-meta-model/               # AOSM Conceptual Foundation
│   ├── agent-oriented-system.md   # What is an Agent-Oriented System?
│   ├── raw-trained-employed-agents.md  # Zeta's agent lifecycle model
│   └── book-ref/                  # Reference material from AOSM literature
│
├── olympus-hub-docs/              # Olympus Hub Documentation
│   ├── README.md                  # Hub documentation index
│   ├── 00-hub-need-and-value/     # Value propositions and primers
│   ├── 01-concepts/               # Core concepts and ontology
│   ├── 02-system-design/          # Architecture and implementation concepts
│   ├── 04-subsystems/             # Detailed subsystem documentation
│   ├── 08-personas-and-journeys/  # Who uses Hub and how
│   ├── 09-composite-systems/      # Advanced composition patterns
│   ├── 10-guides/                 # Practical guides
│   └── decision-logs/             # Architecture Decision Records
│
├── olympus-seer-docs/             # Olympus Seer Documentation
│   ├── agentic-ai-concepts/       # AI agent concepts (memory, knowledge)
│   ├── requirements-enterprise-agentic-platform/  # Platform requirements
│   └── seer-design/               # Seer architecture and subsystems
│
├── session-notes/                 # Design session notes
│
└── _templates/                    # Documentation templates
```

---

## 🚀 Olympus Hub — Operations Management Platform

**Olympus Hub** enables enterprises to model, manage, and optimize business operations across any domain.

### Core Philosophy: "Everything is Ops"

Every business activity — from customer service to fraud detection to compliance — can be modeled as operations:

```
Signal → Trigger → Request → Scenario → Hub Application → Activities → Actions
```

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Workbench** | A scoped environment for a business domain (e.g., "Dispute Resolution") |
| **Scenario** | A workflow that defines how work should be done |
| **Signal** | An event that triggers a Scenario |
| **Hub Application** | Automation that executes Scenario logic |
| **Agent** | Human or AI that handles tasks within a Scenario |

### Four-Layer Ontology

| Layer | Question | Examples |
|-------|----------|----------|
| **Perception** | What's happening? | Signals, Triggers, Machines, Sensors |
| **Normative** | What ought to be done? | Goals, Roles, SOPs, Policies |
| **Execution** | How is it done? | Procedures, Workflows, Tasks, Agents |
| **Automation** | How is it codified? | Runtimes, Tools, Applications |

### Quick Start

1. **Understand the value:** [CIO Primer](./olympus-hub-docs/00-hub-need-and-value/primer-cio.md)
2. **Learn the concepts:** [Introduction](./olympus-hub-docs/01-concepts/introduction.md)
3. **Explore the architecture:** [Hub Architecture](./olympus-hub-docs/02-system-design/hub-architecture.md)
4. **See it in action:** [Idea-to-Deployment Guide](./olympus-hub-docs/10-guides/idea-to-deployment-guide.md)

→ **Full Documentation:** [Olympus Hub README](./olympus-hub-docs/README.md)

---

## 🤖 Olympus Seer — AI Agent Engine

**Olympus Seer** hosts, governs, and operates AI agents with enterprise-grade controls.

### Core Philosophy: "Enterprise-Ready AI Agents"

AI agents in the enterprise need more than just LLM capabilities — they need:
- **Identity and Authority** — Who is this agent? What can it do?
- **Guardrails** — What boundaries constrain its actions?
- **Observability** — What is it doing and why?
- **Governance** — How do we audit and control it?

### Agent Lifecycle: Raw → Trained → Employed

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│  Raw Agent  │ ───▶ │   Trained   │ ───▶ │  Employed   │
│             │      │    Agent    │      │    Agent    │
│ (Container) │      │  (+ Skills) │      │ (+ Context) │
└─────────────┘      └─────────────┘      └─────────────┘

RawAgentSpec         TrainingSpec         EmploymentSpec
└── Image            └── Knowledge        └── Workbench
└── Capabilities     └── Skills           └── Scenario
└── Health           └── Guardrails       └── Authority
                     └── Tools            └── Tool Bindings
```

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Raw Agent** | Base container with core capabilities |
| **Training Spec** | Configuration that adds knowledge, skills, and guardrails |
| **Employment Spec** | Deployment binding to a specific workbench and scenario |
| **Guardrails** | Constraints on agent behavior (input/output filters, action limits) |
| **Authority** | Delegated permissions defining what an agent can do |

### Quick Start

1. **Understand the need:** [Enterprise Agent Platform Requirements](./olympus-seer-docs/requirements-enterprise-agentic-platform/README.md)
2. **Learn the concepts:** [Seer Introduction](./olympus-seer-docs/seer-design/introduction.md)
3. **Explore agent memory:** [Agent Memory Concepts](./olympus-seer-docs/agentic-ai-concepts/agent-memory/README.md)
4. **See Hub integration:** [Seer-Hub Integration](./olympus-seer-docs/seer-design/hub-integration/README.md)

→ **Full Documentation:** [Olympus Seer README](./olympus-seer-docs/seer-design/README.md)

---

## 🔗 How Hub and Seer Work Together

Hub and Seer are designed to work together seamlessly:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         OLYMPUS PLATFORM                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   OLYMPUS HUB (Operations Management)                                       │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  Workbench: Dispute Resolution                                      │   │
│   │                                                                      │   │
│   │  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐               │   │
│   │  │  Scenario   │   │    Task     │   │  Human or   │               │   │
│   │  │  "Refund    │──▶│   Queue     │──▶│  AI Agent   │               │   │
│   │  │  Eligibility"│   │             │   │             │               │   │
│   │  └─────────────┘   └─────────────┘   └──────┬──────┘               │   │
│   │                                             │                       │   │
│   └─────────────────────────────────────────────┼───────────────────────┘   │
│                                                 │                            │
│                                                 │ If AI Agent                │
│                                                 ▼                            │
│   OLYMPUS SEER (AI Agent Engine)                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐               │   │
│   │  │  Employed   │   │  Guardrails │   │   Model     │               │   │
│   │  │   Agent     │──▶│  Enforced   │──▶│  Gateway    │               │   │
│   │  │             │   │             │   │  (Bifrost)  │               │   │
│   │  └─────────────┘   └─────────────┘   └─────────────┘               │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Integration Points

| Integration | Description |
|-------------|-------------|
| **Scenario as Agent** | Publish a Hub Scenario as an AI agent |
| **AI in Task Queues** | Enroll AI agents alongside humans in task queues |
| **Cognitive Audit Fabric** | AI decisions flow through Hub's audit infrastructure |
| **Memory Services** | Agents access Hub's enterprise and agent memory |
| **DevOps Workbench** | AI agents assist with automation development |

→ **See:** [DevOps Workbench Pattern](./olympus-hub-docs/09-composite-systems-and-patterns/devops-workbench/README.md)

---

## 📖 Reading Order for New Readers

### Understanding the Vision (30 min)

1. [AOSM: Agent-Oriented Systems](./aosm-meta-model/agent-oriented-system.md) — The meta-model foundation
2. [Hub Introduction](./olympus-hub-docs/01-concepts/introduction.md) — "Everything is Ops" philosophy
3. [Seer Premise](./olympus-seer-docs/seer-design/premise.md) — Why enterprise AI agents are different

### Understanding Hub (1 hour)

4. [Hub Ontology Reference](./olympus-hub-docs/01-concepts/ontology-reference.md) — Four-layer model
5. [Hub Architecture](./olympus-hub-docs/02-system-design/hub-architecture.md) — Technical architecture
6. [Personas and Journeys](./olympus-hub-docs/08-personas-and-journeys/README.md) — Who uses Hub

### Understanding Seer (1 hour)

7. [Enterprise Agent Platform Requirements](./olympus-seer-docs/requirements-enterprise-agentic-platform/README.md) — Why Seer exists
8. [Seer Design Overview](./olympus-seer-docs/seer-design/README.md) — Seer architecture
9. [Agent Lifecycle (Raw → Trained → Employed)](./aosm-meta-model/raw-trained-employed-agents.md) — Agent maturity model

### Seeing It All Together (30 min)

10. [Idea-to-Deployment Guide](./olympus-hub-docs/10-guides/idea-to-deployment-guide.md) — End-to-end workflow

---

## 🛠️ Documentation Conventions

### Status Markers

| Status | Meaning |
|--------|---------|
| ✅ Complete | Ready for use |
| 🟡 WIP/Draft | Work in progress, usable but incomplete |
| ⚠️ Notes | Raw notes, needs structuring |
| 🔴 Stub | Placeholder only |

### Document Types

| Type | Purpose | Template |
|------|---------|----------|
| **Concept** | Explain what something is | [implementation-concept.md](./_templates/implementation-concept.md) |
| **Subsystem** | Describe a Hub/Seer subsystem | [subsystem-readme.md](./_templates/subsystem-readme.md) |
| **Guide** | Walk through a process | [guide.md](./_templates/guide.md) |
| **ADR** | Record an architectural decision | [adr.md](./_templates/adr.md) |
| **Composite Pattern** | Describe an advanced composition | [composite-pattern.md](./_templates/composite-pattern.md) |

---

## 📂 Key Entry Points

| What You Want | Start Here |
|---------------|------------|
| **Understand the platform** | [This README](#-what-is-olympus) |
| **Evaluate Hub for your enterprise** | [CIO Primer](./olympus-hub-docs/00-hub-need-and-value/primer-cio.md) |
| **Build a Hub scenario** | [Developer Primer](./olympus-hub-docs/00-hub-need-and-value/primer-developer.md) |
| **Understand AI agent governance** | [Seer Guardrails](./olympus-seer-docs/seer-design/subsystems/guardrails.md) |
| **See how it all works together** | [Idea-to-Deployment Guide](./olympus-hub-docs/10-guides/idea-to-deployment-guide.md) |
| **Review architectural decisions** | [Decision Logs](./olympus-hub-docs/decision-logs/README.md) |

---

## 🧭 Navigation Tips

1. **Use the READMEs** — Each major folder has a README that indexes its contents
2. **Check the status** — Look for status markers to know document maturity
3. **Follow the links** — Documents are heavily cross-linked
4. **Check decision logs** — ADRs explain *why* design choices were made
5. **Session notes** — Recent design sessions are captured in `session-notes/`

---

## 📝 Contributing

This is an internal design documentation repository. When contributing:

1. **Use templates** — Start from `_templates/` for new documents
2. **Update indexes** — Add new documents to parent README files
3. **Create ADRs** — Record significant architectural decisions
4. **Mark status** — Use status markers to indicate document maturity

---

*Olympus Design Documentation — Building enterprise operations and AI agent platforms on AOSM principles.*

