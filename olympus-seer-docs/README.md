# Olympus Seer Documentation

**Enterprise AI Agent Platform — Control Plane & Runtime**

---

## What Is Olympus Seer?

Olympus Seer is Zeta's **agent control plane and runtime** for enterprise AI agents. It provides the infrastructure to build, deploy, govern, and operate AI agents as first-class enterprise products — with the identity, authority, lifecycle management, and auditability that regulated industries require.

Seer answers the question:

> *"How do we build, deploy, govern, and run AI agents at enterprise scale?"*

### Seer + Hub

Seer operates alongside **Olympus Hub**, which provides the operational substrate for information-centric work:

| Platform | Focus | What It Provides |
|----------|-------|------------------|
| **Seer** | Agent Governance | Agent lifecycle, identity, authority, context assembly, guardrails |
| **Hub** | Operational Substrate | Scenarios, signals, requests, tasks, collaboration, memory |

Seer agents run **within** Hub's operational context. Hub provides the "what needs to be done"; Seer provides "how agents do it safely."

---

## Documentation Structure

```
olympus-seer-docs/
├── README.md                              ← You are here
│
├── why-seer/                              # "Why Seer?" Book
│   ├── 00-front-matter/                   # Preface, How to Use, TOC
│   ├── part-1-background/                 # The Problem Space (5 sections)
│   ├── part-2-how-seer-solves/            # The Solution (19 sections)
│   └── appendices/                        # Glossary, References, AOSM
│
├── seer-design/                           # Technical Design Documentation
│   ├── introduction.md                    # Product introduction
│   ├── subsystems/                        # 10+ subsystem specifications
│   ├── hub-integration/                   # How Seer integrates with Hub
│   ├── implementation-concepts/           # Core implementation concepts
│   ├── personas-and-needs/                # Enterprise roles and needs
│   ├── ux-architecture/                   # Desks and channels
│   └── guides/                            # Practical guidance
│
├── agentic-ai-concepts/                   # Foundational AI Agent Concepts
│   ├── agent-memory/                      # Memory types and management
│   ├── enterprise-knowledge/              # Knowledge management
│   └── designing-an-agent.md              # Agent design guide
│
└── requirements-enterprise-agentic-platform/  # Platform Requirements
    └── ...                                # Strategic guidance documents
```

---

## Where to Start

### By Role

| Role | Start Here |
|------|------------|
| **Executives & Decision Makers** | [Why Seer? → Preface](./why-seer/00-front-matter/00-1-preface.md) |
| **Enterprise Architects** | [Why Seer? → Part 1: Background](./why-seer/part-1-background/_part-overview.md) |
| **Developers & Engineers** | [Seer Design → Introduction](./seer-design/introduction.md) |
| **Security & Compliance** | [Why Seer? → Identity & Authority](./why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/_section-overview.md) |
| **Product Managers** | [Why Seer? → Summary](./why-seer/part-2-how-seer-solves/13-summary-why-seer/_section-overview.md) |

### By Interest

| I want to... | Go to... |
|--------------|----------|
| Understand why Seer exists | [Why Seer?](./why-seer/README.md) |
| Learn Seer's technical design | [Seer Design](./seer-design/README.md) |
| Understand agent memory | [Agentic AI Concepts → Agent Memory](./agentic-ai-concepts/agent-memory/README.md) |
| See platform requirements | [Requirements](./requirements-enterprise-agentic-platform/README.md) |
| Build an agent | [Seer Design → Guides](./seer-design/guides/README.md) |

---

## The "Why Seer?" Book

The `why-seer/` folder contains a **textbook-style documentation** explaining:

- **Part 1: The Problem** — Why enterprise AI agents require capabilities that cloud-managed AI services don't provide
- **Part 2: The Solution** — How Seer addresses these requirements with a purpose-built architecture

### Book Structure

| Section | Content |
|---------|---------|
| **Front Matter** | Preface, How to Use, Table of Contents |
| **Part 1: Background** | Enterprise agent platforms, accountability gaps, memory requirements, audit requirements, building agents |
| **Part 2: How Seer Solves** | Design philosophy, agent lifecycle, identity & authority, memory & audit, context assembly, governance, observability, model gateway, tools & actions, multi-agent patterns, and more |
| **Appendices** | Glossary, Seer-Hub division, AOSM foundations, further reading |

### Key Concepts

| Concept | Definition | Where to Learn |
|---------|------------|----------------|
| **OPD Triad** | Observability, Predictability, Directability — what makes agents enterprise-ready | [Section 1.3](./why-seer/part-1-background/01-what-is-enterprise-agent-platform/01-3-opd-triad.md) |
| **Raw → Trained → Employed** | Three-layer agent lifecycle model | [Section 5.1](./why-seer/part-1-background/05-building-enterprise-agent/05-1-agent-lifecycle.md) |
| **ESPP Taxonomy** | Memory types: Episodic, Semantic, Procedural, Preference | [Section 3.2](./why-seer/part-1-background/03-memory-requirements/03-2-espp-taxonomy.md) |
| **CAF** | Cognitive Audit Fabric — enterprise memory control plane | [Section 4.3](./why-seer/part-1-background/04-audit-requirements/04-3-cognitive-audit-fabric.md) |
| **Request-Scoped Delegation** | Business users delegate temporary authority to agents | [Section 3.6](./why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-6-request-scoped-delegation.md) |
| **Agent Persona** | Business identity vs. Deployment Identity (two-layer model) | [Section 3.1](./why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-1-agent-identity.md) |

→ **[Read the full "Why Seer?" book](./why-seer/README.md)**

---

## Seer Design Documentation

The `seer-design/` folder contains **technical design documentation** for architects, developers, and operators:

### Core Sections

| Section | Description |
|---------|-------------|
| [Introduction](./seer-design/introduction.md) | Product overview, Seer + Hub architecture |
| [Subsystems](./seer-design/subsystems/README.md) | Agent Lifecycle Manager, Guardrails, Authority Enforcement, Context Compiler, Model Gateway, Sentinels, COGW |
| [Hub Integration](./seer-design/hub-integration/README.md) | How Seer agents operate within Hub |
| [Implementation Concepts](./seer-design/implementation-concepts/) | Delegation chains, agent identity, authority enforcement, guardrails, context assembly |
| [Personas & Needs](./seer-design/personas-and-needs/roles.md) | Enterprise roles (APO, CSA, AE, KMO, ARE, COS, ARAO) |
| [UX Architecture](./seer-design/ux-architecture/README.md) | Desks and channels for enterprise personas |
| [Guides](./seer-design/guides/README.md) | Practical guidance for building and operating agents |

→ **[Read the Seer Design documentation](./seer-design/README.md)**

---

## Foundational Concepts

### Agentic AI Concepts

The `agentic-ai-concepts/` folder contains foundational concepts for understanding AI agents:

| Topic | Description |
|-------|-------------|
| [Agent Memory](./agentic-ai-concepts/agent-memory/README.md) | Memory types (episodic, semantic, procedural, preference), context building, governance |
| [Enterprise Knowledge](./agentic-ai-concepts/enterprise-knowledge/) | Knowledge management, retrieval, and integration |
| [Designing an Agent](./agentic-ai-concepts/designing-an-agent.md) | Step-by-step guide to agent design |
| [Enterprise Agent Platform](./agentic-ai-concepts/enterprise-agent-platform.md) | What makes an enterprise agent platform |
| [Multi-Agent Topologies](./agentic-ai-concepts/multi-agent-topologies.md) | Patterns for multi-agent systems |

### Platform Requirements

The `requirements-enterprise-agentic-platform/` folder contains strategic guidance for building an enterprise agent platform:

- Executive summary, problem statement, system requirements
- CSP offerings and gaps
- Solution principles and conceptual architecture
- Platform components and services

→ **[Read the Requirements documentation](./requirements-enterprise-agentic-platform/README.md)**

---

## Related Documentation

| Resource | Description |
|----------|-------------|
| [Olympus Hub Documentation](../olympus-hub-docs/README.md) | Operational platform for information-centric work |
| [AOSM Meta-Model](../aosm-meta-model/) | Theoretical foundations for agent-oriented systems |

---

## Quick Reference

| Resource | Link |
|----------|------|
| 📖 Why Seer? Table of Contents | [why-seer/00-front-matter/00-3-table-of-contents.md](./why-seer/00-front-matter/00-3-table-of-contents.md) |
| 📚 Glossary | [why-seer/appendices/appendix-a-glossary.md](./why-seer/appendices/appendix-a-glossary.md) |
| 🔗 Seer + Hub Division | [why-seer/appendices/appendix-b-seer-hub-division.md](./why-seer/appendices/appendix-b-seer-hub-division.md) |
| 📐 AOSM Foundations | [why-seer/appendices/appendix-c-aosm-foundations.md](./why-seer/appendices/appendix-c-aosm-foundations.md) |

---

*Olympus Seer is part of the Zeta AI Product Strategy. For Hub documentation, see [olympus-hub-docs](../olympus-hub-docs/README.md).*
