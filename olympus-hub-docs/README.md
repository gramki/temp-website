# Olympus Hub

> **To empower organizations to reimagine information-centric work through governed AI-Human collaboration**

---

## What Is Hub?

**Olympus Hub** is an operational platform for information-centric work — the work that dominates modern enterprises, where inputs, transformations, and outputs are information rather than physical matter.

Hub provides the infrastructure where humans and AI collaborate as **agents** — not as tool and user, but as team members working together toward shared goals. It's where customer service resolves disputes, where finance reconciles transactions, where IT diagnoses incidents, where compliance reviews cases — all through governed collaboration.

Hub is not a replacement for your existing systems. It's the **operational layer** that makes them work together — providing the context, structure, memory, and governance that turns AI capability into operational value.

---

## The Shift We're Making

Traditional enterprise systems model work as **tasks, records, and procedures**. This works until you try to integrate AI — and discover that AI doesn't fit neatly into task-based workflows.

Hub models work differently:

- **Work is situations that need resolution** — not tasks to execute
- **Multiple agents collaborate toward goals** — humans, AI, rules, workflows
- **The organization learns from outcomes** — not just logs them

This is how work actually operates. We've just been modeling it wrong.

When you model work this way, AI integration becomes natural — because the model is already multi-agent, goal-oriented, and learning-focused. Hub provides the infrastructure for this model.

---

## Who Is This For?

| If you're a... | Start with... | Key question answered |
|----------------|---------------|----------------------|
| **Executive** evaluating Hub | [Executive Primer](./00-hub-need-and-value/primer-executive.md) | What business value does Hub deliver? |
| **CIO/CTO** assessing fit | [CIO Primer](./00-hub-need-and-value/primer-cio.md) | Should we adopt Hub? |
| **Process Architect** | [Process Architect Primer](./00-hub-need-and-value/primer-process-architect.md) | How does Hub model my work? |
| **Developer** | [Developer Primer](./00-hub-need-and-value/primer-developer.md) | How do I build on Hub? |
| **Zeta Leadership** | [Strategic Value Primer](./00-hub-need-and-value/primer-strategic-value.md) | Why should Zeta build this? |

---

## Reading Paths

### I want to understand the vision

1. [Vision and Mission](./00-_why/vision.md) — The aspiration and purpose
2. [Foundational Beliefs](./00-_why/foundational-beliefs.md) — The thinking behind Hub
3. [Design Philosophy](./02-system-design/hub-design-philosophy.md) — Theoretical foundations

### I want to evaluate Hub for my organization

1. [Executive Primer](./00-hub-need-and-value/primer-executive.md) — Business case and urgency
2. [CIO Primer](./00-hub-need-and-value/primer-cio.md) — Technical evaluation
3. [Applicability Guide](./01-concepts/olympus-hub-applicability-guide.md) — Fit assessment

### I want to model work with Hub

1. [Process Architect Primer](./00-hub-need-and-value/primer-process-architect.md) — Your role and value
2. [Scenario-Oriented Thinking](./11-decision-frameworks/scenario-oriented-thinking/scenario-oriented-thinking.md) — The design philosophy
3. [Scenario Specification Types](./02-system-design/implementation-concepts/scenario-specification-types.md) — How scenarios are defined

### I want to build on Hub

1. [Developer Primer](./00-hub-need-and-value/primer-developer.md) — Your role and value
2. [Hub Architecture](./02-system-design/hub-architecture.md) — How it all fits together
3. [Hub Development Flow](./10-guides/hub-development-flow/README.md) — How to develop

---

## Core Concepts

### The Operational Pattern

```
Signal → Trigger → Request → Scenario → Hub Application → Agents → Outcome
                                              ↑
                                    (Human, AI, Rules, Workflows)
```

**Signals** arrive from the environment. **Triggers** match them to **Scenarios**. **Requests** become collaboration surfaces where **Agents** work together toward resolution.

### The Four Pillars

| Pillar | What it provides |
|--------|------------------|
| **Context** | Domain knowledge, entity relationships, grounding |
| **Structure** | Scenarios, triggers, delegation, escalation |
| **Memory** | Organizational learning that accumulates |
| **Governance** | Accountability, audit, human oversight |

### Hub + Seer

Two systems, unified purpose:

- **Hub** governs operations — scenarios, requests, collaboration
- **Seer** governs AI agents — identity, runtime, capabilities

Together: trusted AI-Human collaboration at enterprise scale.

---

## Explore Further

### Why Hub
- [Vision and Mission](./00-_why/vision.md) — The aspiration
- [Foundational Beliefs](./00-_why/foundational-beliefs.md) — The thinking
- [Primers](./00-hub-need-and-value/README.md) — Value propositions by audience

### Concepts
- [Ontology Reference](./01-concepts/ontology-reference.md) — The conceptual foundation
- [Glossary](./01-concepts/glossary.md) — Key terminology
- [Applicability Guide](./01-concepts/olympus-hub-applicability-guide.md) — Where Hub fits

### Design
- [Hub Architecture](./02-system-design/hub-architecture.md) — System architecture
- [Design Philosophy](./02-system-design/hub-design-philosophy.md) — Theoretical foundations
- [Implementation Concepts](./02-system-design/implementation-concepts/README.md) — Hub-specific concepts

### Guides
- [Hub Development Flow](./10-guides/hub-development-flow/README.md) — Development model
- [Idea to Deployment](./10-guides/idea-to-deployment-guide.md) — The 10-stage pipeline
- [All Guides](./10-guides/README.md) — Complete guide index

---

## Full Documentation Index

### 00 - Why Hub

| Document | Description |
|----------|-------------|
| [Vision and Mission](./00-_why/vision.md) | Hub's aspiration and purpose |
| [Foundational Beliefs](./00-_why/foundational-beliefs.md) | The thinking behind Hub's design |

### 00 - Hub Need and Value

| Document | Audience |
|----------|----------|
| [Overview](./00-hub-need-and-value/README.md) | All |
| [Executive Primer](./00-hub-need-and-value/primer-executive.md) | Enterprise decision-makers |
| [CIO Primer](./00-hub-need-and-value/primer-cio.md) | CIOs, CTOs, Enterprise Architects |
| [Process Architect Primer](./00-hub-need-and-value/primer-process-architect.md) | Process Architects, Business Analysts |
| [Developer Primer](./00-hub-need-and-value/primer-developer.md) | Developers, Solution Architects |
| [Strategic Value Primer](./00-hub-need-and-value/primer-strategic-value.md) | Zeta Leadership (internal) |

### 01 - Core Concepts

| Document | Description |
|----------|-------------|
| [Introduction](./01-concepts/introduction.md) | High-level introduction |
| [Ontology Reference](./01-concepts/ontology-reference.md) | Four-layer ontology |
| [Glossary](./01-concepts/glossary.md) | Key terminology |
| [Applicability Guide](./01-concepts/olympus-hub-applicability-guide.md) | Fit assessment |
| [Collaborators](./01-concepts/collaborators.md) | Agent collaboration model |
| [MCP Channel](./01-concepts/mcp-channel.md) | MCP integration |

### 02 - System Design

| Document | Description |
|----------|-------------|
| [Hub Architecture](./02-system-design/hub-architecture.md) | System architecture |
| [Design Philosophy](./02-system-design/hub-design-philosophy.md) | Theoretical foundations |
| [Implementation Concepts](./02-system-design/implementation-concepts/README.md) | Hub-specific concepts (42+) |
| [Agent Model](./02-system-design/agent-model.md) | Agent participation patterns |
| [Views](./02-system-design/views/README.md) | Architectural perspectives |

### 03 - Information-Centric Work Patterns

| Document | Description |
|----------|-------------|
| [Overview](./03-information-centric-work/README.md) | Pattern index and introduction |
| [Queue-Based Work](./03-information-centric-work/queue-based-work.md) | Task stream processing |
| [Case-Based Work](./03-information-centric-work/case-based-work.md) | Investigation and resolution |
| [Conversation-Based Work](./03-information-centric-work/conversation-based-work.md) | Dialogue-centered work |
| [Event-Driven Operations](./03-information-centric-work/event-driven-operations.md) | Signal-triggered response |
| [Artifact-Centric Work](./03-information-centric-work/artifact-centric-work.md) | Single artifact lifecycle |
| [Review-Based Work](./03-information-centric-work/review-based-work.md) | Evaluation and assessment |
| [Generative/Design Work](./03-information-centric-work/generative-design-work.md) | Exploration and selection |

### 04 - Subsystems

| Subsystem | Description |
|-----------|-------------|
| [Signal Exchange](./04-subsystems/signal-exchange/README.md) | Signal routing (data plane) |
| [Workbench Management](./04-subsystems/workbench-management/README.md) | Workbench definitions (control plane) |
| [Automation Ideation](./04-subsystems/automation-ideation/README.md) | Idea → Intent → Charter |
| [Feedback Services](./04-subsystems/feedback-services/README.md) | Production feedback loop |
| [I/O Gateways](./04-subsystems/signal-providers/README.md) | Signal providers |
| [MS Teams Integration](./04-subsystems/ms-teams-integration/README.md) | Teams collaboration |
| [Automation Runtimes](./04-subsystems/automation-runtimes/README.md) | Hub Application hosts |
| [Memory Services](./04-subsystems/memory-services/README.md) | Agent and Enterprise Memory |
| [Cognitive Audit Fabric](./04-subsystems/cognitive-audit-fabric/README.md) | Decision audit |
| [Registry Services](./04-subsystems/registry-services/README.md) | Tool, Machine, Environment |
| [Knowledge Services](./04-subsystems/knowledge-services/README.md) | Enterprise Knowledge |
| [Task Management](./04-subsystems/task-management/README.md) | Task queues and lifecycle |
| [Request Management](./04-subsystems/request-management/README.md) | Request lifecycle |
| [Subscription Management](./04-subsystems/subscription-management/README.md) | Tenant administration |
| [User Management](./04-subsystems/user-management/README.md) | User personas |
| [Hub Native Utilities](./04-subsystems/hub-native-utilities/README.md) | Decision tools, routines |
| [Hub Analytics](./04-subsystems/hub-analytics/README.md) | Operational analytics |
| [Marketplace](./04-subsystems/marketplace/README.md) | Blueprints and packages |

### 05 - Infrastructure

| Document | Description |
|----------|-------------|
| [Platform Dependencies](./05-infrastructure/olympus-platform-dependencies.md) | Olympus Platform services |
| [Heracles Gateway](./05-infrastructure/heracles-gateway.md) | MCP gateway |
| [MCP Router](./05-infrastructure/mcp-router.md) | Tool orchestration |
| [Data Services](./05-infrastructure/) | Ganymede, Callisto, Europa |

### 06 - UX Architecture

| Document | Description |
|----------|-------------|
| [Overview](./06-ux-architecture/README.md) | UX meta approach |
| [Agent Desk](./06-ux-architecture/tenant-domain/agent-desk.md) | Agent application |
| [Supervisor Desk](./06-ux-architecture/tenant-domain/supervisor-desk.md) | Supervisor application |
| [Hub Home](./06-ux-architecture/tenant-domain/hub-home.md) | Landing experience |

### 07 - Data Architecture

| Document | Description |
|----------|-------------|
| [Overview](./07-data-architecture/README.md) | Data architecture |
| [Storage Architecture](./07-data-architecture/storage-architecture.md) | Layered storage model |

### 08 - Personas and Journeys

| Document | Description |
|----------|-------------|
| [Overview](./08-personas-and-journeys/README.md) | Persona and journey index |
| [Personas](./08-personas-and-journeys/personas/) | Process Architect, Developer, Supervisor, Agent, etc. |
| [Journeys](./08-personas-and-journeys/journeys/) | Scenario Development, Request Lifecycle, etc. |

### 09 - Composite Systems and Patterns

| Document | Description |
|----------|-------------|
| [Overview](./09-composite-systems-and-patterns/README.md) | Composite pattern philosophy |
| [DevOps Workbench](./09-composite-systems-and-patterns/devops-workbench/README.md) | Development automation |
| [Scenario as Agent](./09-composite-systems-and-patterns/scenario-as-an-agent.md) | Agent composition |

### 10 - Guides

| Document | Description |
|----------|-------------|
| [Overview](./10-guides/README.md) | Guide index |
| [Hub Development Flow](./10-guides/hub-development-flow/README.md) | Development model |
| [Idea to Deployment](./10-guides/idea-to-deployment-guide.md) | 10-stage pipeline |
| [Workbench Setup](./10-guides/workbench-setup-guide.md) | Workbench configuration |

### 11 - Decision Frameworks

| Document | Description |
|----------|-------------|
| [Overview](./11-decision-frameworks/README.md) | Decision framework index |
| [Scenario-Oriented Thinking](./11-decision-frameworks/scenario-oriented-thinking/scenario-oriented-thinking.md) | Core design approach |

### AOSM and Hub

| Document | Description |
|----------|-------------|
| [Overview](./aosm-and-hub/README.md) | AOSM implementation |
| [AOSM Concepts](./aosm-and-hub/) | Agent-Oriented Systems Modeling |

### Decision Logs

| Document | Description |
|----------|-------------|
| [Decision Log Index](./decision-logs/README.md) | Architecture Decision Records |

---

## Related Projects

| Project | Description |
|---------|-------------|
| **Olympus Seer** | AI Agent hosting platform — Agent lifecycle, runtime, control plane |
| **Neutrino** | Customer interaction channels |
| **Angelos** | UI component framework |
| **Cipher** | Identity and Access Management |

---

## Document Status Legend

| Status | Meaning |
|--------|---------|
| ✅ Complete | Ready for use |
| 🟡 WIP | Work in progress |
| ⚠️ Notes | Raw notes |
| 🔴 Stub | Placeholder |
