# Zeta AI Product Strategy

> **Enterprise Agentic AI Platform — Design Documentation**

This repository contains the design documentation for Zeta's enterprise agentic AI platform, including the foundational meta-model, Olympus Hub (operations management), and Olympus Seer (agent runtime).

---

## 🏛️ Repository Structure

```
zeta-ai-product-strategy/
│
├── aosm-meta-model/          # Foundational framework for Agent-Oriented Systems
├── olympus-hub-docs/         # Operations Management Platform
├── olympus-seer-docs/        # Agent Lifecycle & Runtime Engine
│
├── ibuki/                    # Agentic banking product concepts
├── pontus/                   # Data products and ETSL
├── quark/                    # Agentic operations
├── tachyon/                  # CLM and servicing
├── neutrino/                 # Customer interaction channels
├── cipher/                   # Identity and access management
├── foundry/                  # Development infrastructure
│
├── gtm-strategy/             # Go-to-market themes
├── market-study/             # Market research and analysis
└── org-8.0/                  # Organizational model
```

---

## 🎯 Core Documentation Areas

### 1. AOSM Meta-Model — Foundational Framework

> **Path:** [aosm-meta-model/](./aosm-meta-model/)

The **Agent-Oriented Systems Modeling (AOSM)** meta-model provides the theoretical foundation for designing human-AI collaborative systems.

| Document | Description |
|----------|-------------|
| [Agent-Oriented System](./aosm-meta-model/agent-oriented-system.md) | Complete AOSM framework: goals, roles, responsibilities, PIDA, RASCI |
| [Raw, Trained, Employed Agents](./aosm-meta-model/raw-trained-employed-agents.md) | Zeta's agent lifecycle model extending AOSM |

**Key Concepts:**
- **Human-AI Teams (HAT)** — Collaborative units of interdependent agents
- **Goal-Role-Responsibility Chain** — Goals → Roles → Responsibilities → Capabilities → Agents
- **PIDA Responsibilities** — Perception, Interpretation, Decision, Action
- **Four Components of Autonomy** — Authority, Availability, Capability, Capacity
- **RASCI Accountability** — Accountable role must always be human

---

### 2. Olympus Hub — Operations Management Platform

> **Path:** [olympus-hub-docs/](./olympus-hub-docs/)

**Olympus Hub** is an operations management platform for enterprises to model, manage, and optimize business operations through human-AI collaboration.

| Section | Description | Path |
|---------|-------------|------|
| **Need & Value** | Primers for CIO, Process Architect, Developer | [00-hub-need-and-value/](./olympus-hub-docs/00-hub-need-and-value/) |
| **Core Concepts** | Ontology, "Everything is Ops" philosophy | [01-concepts/](./olympus-hub-docs/01-concepts/) |
| **System Design** | Architecture, implementation concepts | [02-system-design/](./olympus-hub-docs/02-system-design/) |
| **Subsystems** | Signal Exchange, Memory, Registry, Task Management | [04-subsystems/](./olympus-hub-docs/04-subsystems/) |
| **Infrastructure** | Platform dependencies, gateways, data services | [05-infrastructure/](./olympus-hub-docs/05-infrastructure/) |
| **UX Architecture** | Desks, consoles, interaction channels | [06-ux-architecture/](./olympus-hub-docs/06-ux-architecture/) |
| **Personas & Journeys** | Who uses Hub and how | [08-personas-and-journeys/](./olympus-hub-docs/08-personas-and-journeys/) |
| **Composite Patterns** | Scenario as Agent, multi-workbench patterns | [09-composite-systems-and-patterns/](./olympus-hub-docs/09-composite-systems-and-patterns/) |
| **Guides** | Practical how-to guides | [10-guides/](./olympus-hub-docs/10-guides/) |

**The Operational Pattern:**
```
Signal → Trigger → Request → Scenario → Hub Application → Activities → Actions
```

**Four-Layer Architecture:**

| Layer | Question | Concepts |
|-------|----------|----------|
| **Perception** | What's happening? | Domain, Signal, Trigger, Scenario |
| **Normative** | What ought to be done? | Role, Goal, SOP, Decision |
| **Execution** | How is it done? | Workflow, Case, Activities, Agent |
| **Automation** | How is it codified? | Runtime, Tools, Actuators |

📖 **Start here:** [Hub README](./olympus-hub-docs/README.md)

---

### 3. Olympus Seer — Agent Lifecycle & Runtime Engine

> **Path:** [olympus-seer-docs/](./olympus-seer-docs/)

**Olympus Seer** is the control plane and runtime for enterprise AI agents — managing agent definition, lifecycle, deployment, and execution.

| Section | Description | Path |
|---------|-------------|------|
| **Seer Design** | Subsystems, Hub integration, CRD specifications | [seer-design/](./olympus-seer-docs/seer-design/) |
| **Requirements** | Enterprise agentic platform requirements | [requirements-enterprise-agentic-platform/](./olympus-seer-docs/requirements-enterprise-agentic-platform/) |
| **Agentic AI Concepts** | Agent memory, enterprise knowledge foundations | [agentic-ai-concepts/](./olympus-seer-docs/agentic-ai-concepts/) |

**Key Seer Subsystems:**
- **Agent Lifecycle Service** — Definition, versioning, deployment
- **Model Gateway** — LLM abstraction and routing
- **Context Assembly Engine** — Token budgeting, retrieval
- **Guardrails** — Behavioral constraints, sidecar enforcement
- **Authority Enforcement** — OPA policies, tool authorization
- **Agent Observability** — Logging, tracing, metrics

📖 **Start here:** [Seer Design README](./olympus-seer-docs/seer-design/README.md)

---

## 👥 Navigation by Persona

### For Enterprise CIOs & CTOs

**Question:** *Should we adopt this platform for our operations?*

| Start Here | Then Explore |
|------------|--------------|
| [CIO Primer](./olympus-hub-docs/00-hub-need-and-value/primer-cio.md) | [Applicability Guide](./olympus-hub-docs/01-concepts/olympus-hub-applicability-guide.md) |
| [Strategic Value](./olympus-hub-docs/00-hub-need-and-value/primer-strategic-value.md) | [AOSM Overview](./aosm-meta-model/agent-oriented-system.md) |

---

### For Enterprise Architects & Solution Architects

**Question:** *How does this platform fit into our enterprise architecture?*

| Start Here | Then Explore |
|------------|--------------|
| [AOSM Meta-Model](./aosm-meta-model/agent-oriented-system.md) | [Hub Architecture](./olympus-hub-docs/02-system-design/hub-architecture.md) |
| [Ontology Reference](./olympus-hub-docs/01-concepts/ontology-reference.md) | [Platform Dependencies](./olympus-hub-docs/05-infrastructure/olympus-platform-dependencies.md) |
| [Raw, Trained, Employed](./aosm-meta-model/raw-trained-employed-agents.md) | [Seer Subsystems](./olympus-seer-docs/seer-design/subsystems/README.md) |

---

### For Process Architects & Business Analysts

**Question:** *Can this platform capture and automate my business processes?*

| Start Here | Then Explore |
|------------|--------------|
| [Process Architect Primer](./olympus-hub-docs/00-hub-need-and-value/primer-process-architect.md) | [Scenario Development Journey](./olympus-hub-docs/08-personas-and-journeys/journeys/scenario-development.md) |
| [Introduction ("Everything is Ops")](./olympus-hub-docs/01-concepts/introduction.md) | [Implementation Concepts](./olympus-hub-docs/02-system-design/implementation-concepts/README.md) |

---

### For Developers & Agent Engineers

**Question:** *How do I build and deploy agents on this platform?*

| Start Here | Then Explore |
|------------|--------------|
| [Developer Primer](./olympus-hub-docs/00-hub-need-and-value/primer-developer.md) | [Hub Integration](./olympus-seer-docs/seer-design/hub-integration/README.md) |
| [Agent Lifecycle](./olympus-seer-docs/seer-design/subsystems/agent-lifecycle-service.md) | [Training Spec CRD](./olympus-seer-docs/seer-design/hub-integration/training-spec-crd.md) |
| [Designing an Agent](./olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md) | [Guardrails Guide](./olympus-seer-docs/seer-design/guides/guardrails-best-practices.md) |

---

### For Operations & Reliability Engineers

**Question:** *How do I operate and monitor agents in production?*

| Start Here | Then Explore |
|------------|--------------|
| [Agent Observability](./olympus-seer-docs/seer-design/subsystems/agent-observability.md) | [Production Readiness](./olympus-seer-docs/seer-design/personas-and-needs/needs/production-readiness.md) |
| [AE Deliverables to ARE](./olympus-seer-docs/seer-design/personas-and-needs/ae-deliverables-to-are.md) | [Hub Analytics](./olympus-hub-docs/04-subsystems/hub-analytics/README.md) |

---

### For AI/ML Engineers & Knowledge Architects

**Question:** *How do memory and knowledge work in this platform?*

| Start Here | Then Explore |
|------------|--------------|
| [Agent Memory Concepts](./olympus-seer-docs/agentic-ai-concepts/agent-memory/README.md) | [Memory Services](./olympus-hub-docs/04-subsystems/memory-services/README.md) |
| [Enterprise Knowledge](./olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/README.md) | [Knowledge Services](./olympus-hub-docs/04-subsystems/knowledge-services/README.md) |
| [Context Assembly Engine](./olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md) | [Enterprise Memory](./olympus-seer-docs/agentic-ai-concepts/enterprise-memory/README.md) |

---

### For Compliance & Audit Professionals

**Question:** *How does this platform ensure accountability and auditability?*

| Start Here | Then Explore |
|------------|--------------|
| [RASCI in AOSM](./aosm-meta-model/agent-oriented-system.md#28-accountability-elements-rasci) | [Cognitive Audit Fabric](./olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md) |
| [Authority Enforcement](./olympus-seer-docs/seer-design/subsystems/authority-enforcement.md) | [Audit Investigation Journey](./olympus-hub-docs/08-personas-and-journeys/journeys/audit-investigation.md) |

---

## 🔗 How Hub and Seer Work Together

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ENTERPRISE AGENTIC PLATFORM                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                         OLYMPUS HUB                                   │   │
│  │               Operations Management Platform                          │   │
│  │                                                                       │   │
│  │   • Workbenches (operational domains)                                 │   │
│  │   • Scenarios (business processes)                                    │   │
│  │   • Signal Exchange (routing & triggers)                              │   │
│  │   • Task Management (assignment & tracking)                           │   │
│  │   • Human Agents (supervisors, agents)                                │   │
│  │                                                                       │   │
│  │                            ▼ deploys to ▼                             │   │
│  │                                                                       │   │
│  │  ┌────────────────────────────────────────────────────────────────┐  │   │
│  │  │                      OLYMPUS SEER                               │  │   │
│  │  │              Agent Lifecycle & Runtime Engine                   │  │   │
│  │  │                                                                 │  │   │
│  │  │   • Agent Definitions (Raw → Trained → Employed)                │  │   │
│  │  │   • Runtime Deployment                                          │  │   │
│  │  │   • Model Gateway (LLM routing)                                 │  │   │
│  │  │   • Guardrails & Authority                                      │  │   │
│  │  │   • Context Assembly                                            │  │   │
│  │  │   • Observability                                               │  │   │
│  │  └────────────────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│                    ▲ grounded in ▲                                          │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                       AOSM META-MODEL                                 │   │
│  │              Agent-Oriented Systems Modeling Framework                │   │
│  │                                                                       │   │
│  │   • Human-AI Teams (HAT)                                              │   │
│  │   • Goals → Roles → Responsibilities → Capabilities                   │   │
│  │   • PIDA (Perception, Interpretation, Decision, Action)               │   │
│  │   • Four Components of Autonomy                                       │   │
│  │   • RASCI Accountability                                              │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Relationship:**
- **AOSM** provides the theoretical framework for designing human-AI systems
- **Hub** implements the operational layer — workbenches, scenarios, signals, tasks
- **Seer** implements the agent layer — lifecycle, runtime, guardrails, observability
- Agents defined and deployed via Seer execute within Hub's operational context

---

## 📝 Document Status Legend

| Status | Meaning |
|--------|---------|
| ✅ Complete | Ready for use |
| 🟡 WIP | Work in progress, usable but incomplete |
| ⚠️ Notes | Raw notes, needs structuring |
| 🔴 Stub | Placeholder only |

---

## 🗂️ Other Documentation Areas

| Area | Description | Path |
|------|-------------|------|
| **Ibuki** | Agentic banking products (EON, relationship-aware tools) | [ibuki/](./ibuki/) |
| **Pontus** | Data products and ETSL framework | [pontus/](./pontus/) |
| **Quark** | Agentic operations design | [quark/](./quark/) |
| **Tachyon** | CLM and customer servicing | [tachyon/](./tachyon/) |
| **Market Study** | Enterprise gaps, customer needs, CIO research | [market-study/](./market-study/) |
| **GTM Strategy** | Go-to-market themes and positioning | [gtm-strategy/](./gtm-strategy/) |

---

## 🚀 Quick Start

1. **Understand the foundation** — Read [AOSM Overview](./aosm-meta-model/agent-oriented-system.md)
2. **Explore Hub** — Start with [Hub Introduction](./olympus-hub-docs/01-concepts/introduction.md)
3. **Explore Seer** — Start with [Seer Design README](./olympus-seer-docs/seer-design/README.md)
4. **Find your persona** — Use the [Navigation by Persona](#-navigation-by-persona) section above
5. **Deep dive** — Follow the recommended reading paths for your role

---

## 📚 External References

- Sterling, L., & Taveter, K. (2009). *The Art of Agent-Oriented Modeling*
- *Integrating Artificial and Human Intelligence through Agent-Oriented Systems Design* (CRC Press)
- Stevenson et al. (2023). Four Components of Autonomy

---

*Last updated: January 2026*
