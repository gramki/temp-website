# Engagement Readiness Engineering

Engagement Readiness Engineering (ERE) is the function within ERC responsible for building and operating the systems, tools, and applications that make the Engagement lifecycle efficient, reliable, and consistent.

This function is distinct from **Engagement Engineering** (the discipline of assembling customer-specific product instantiations). ERE builds the infrastructure that enables Engagement Engineering to be practiced at scale — the tools, platforms, and automation that prepare teams and customers for successful Engagements. ERE also operates the [ERE Delivery Swarms](03-ai-architecture/agents.md) that work alongside engagement teams in discovery, induction analysis, and verification, and stewards the [Work Model Library](04-knowledge-engineering/README.md) that compounds structural patterns across Engagements.

---

## How to Use This Guide

This documentation set describes the ERE function: its objectives, the systems it builds, the governance it enforces, and the team that delivers it. Use the audience guide below to find your starting point.

### Audience Guide

| Role | Start Here | Then Explore |
|------|------------|--------------|
| **EPM / EPO** | [Overview](01-overview/README.md) | Document Governance → Governance Enforcement → Style Guide |
| **Product Manager** | [Overview](01-overview/README.md) | [Objectives](01-overview/objectives.md) → Systems → [Roadmap](08-roadmap/README.md) |
| **Engineer** | [Systems](02-systems/README.md) | AI Architecture → Document Governance → Content Bridge |
| **Knowledge Engineer** | [Knowledge Engineering](04-knowledge-engineering/README.md) | Governance → Style Guide |
| **ERC Leadership** | [Overview](01-overview/README.md) | Governance → [Team Structure](07-team-structure/README.md) → [Metrics](07-team-structure/success-metrics.md) |

---

## Contents

### Core Concepts

| # | Section | What It Covers |
|---|---------|----------------|
| 1 | [Overview](01-overview/README.md) | Function overview, positioning within ERC, philosophy |
| 2 | [Objectives](01-overview/objectives.md) | The five strategic objectives ERE pursues |

### Systems and Tools

| # | Section | What It Covers |
|---|---------|----------------|
| 3 | [Systems](02-systems/README.md) | Engagement Registry, Bootstrap Kit, Presales Toolkit, Delivery Toolkit, Knowledge Platform, Customer Portal, Content Bridge |
| 4 | [AI Architecture](03-ai-architecture/README.md) | AI-native design principles, agents, agent governance |
| 5 | [Knowledge Engineering](04-knowledge-engineering/README.md) | Knowledge as first-class function, ownership, lifecycle capture |
| 6 | [Document Governance](05-document-governance/README.md) | Git vs SharePoint, repo structures, governance rules |

### Governance and Operations

| # | Section | What It Covers |
|---|---------|----------------|
| 7 | [Governance Enforcement](06-governance-enforcement/README.md) | Progressive enforcement model, gates, compliance dashboards |
| 8 | [Team Structure](07-team-structure/README.md) | Initial and mature team composition, roles, capacity, metrics |
| 9 | [Roadmap](08-roadmap/README.md) | Four-phase evolution from Foundation to Full Enforcement |

### Reference

| # | Section | What It Covers |
|---|---------|----------------|
| 10 | [Markdown Style Guide](reference/markdown-style-guide.md) | Status indicators, ROAM, priorities, callouts |
| 11 | [Glossary](reference/glossary.md) | Terms and acronyms |
| 12 | [Open Questions](reference/open-questions.md) | Unresolved decisions and areas needing input |

---

## Relationship to the Engagement Operating Model

ERE is the **tooling arm** of the Engagement Operating Model. While the [Engagement Operating Model Guide](../engagement/README.md) defines the roles, processes, lifecycle phases, and governance structures that constitute how Engagements are explored, staffed, executed, and governed, ERE provides the systems that enable those processes to operate at scale.

| Engagement Operating Model | Engagement Readiness Engineering |
|---------------------------|----------------------------------|
| Defines roles (EPM, EA, AVA, etc.) | Provides tools those roles use (BRD Author, Governance Prep) |
| Defines lifecycle phases | Engagement Registry tracks state; enforces gates at each phase |
| Defines governance bodies (ERC, PAC) | Provides compliance dashboards and reporting |
| Defines Exploration and qualification | Provides Proposal Kit, RFP Kit, Estimation Workbench |
| Defines inner source contribution model | Captures and curates patterns via Knowledge Platform |
| Defines Engagement identity | Engagement Registry assigns `ENG-{CODE}`, `EXP-{CODE}` identifiers |

ERE reports to ERC and operates as the internal product team that builds the infrastructure enabling the operating model to scale.

---

## Key Principles

**Pragmatic Hybrid:** Configure existing platforms where commoditized (Jira, Confluence, etc.); build custom where differentiated.

**AI-Native:** Both assistive (drafting, suggestions, Q&A) and automative (routine execution) depending on task complexity.

**Progressive Enforcement:** Tools initially guide and assist; mandatory gates introduced as adoption matures and tooling proves reliable.

**Knowledge as First-Class:** Knowledge capture is not optional overhead — it is embedded in the Engagement lifecycle with required artifacts at each phase transition.

---

## Getting Started

1. Read the [Overview](01-overview/README.md) to understand ERE's positioning and scope
2. Review the [Objectives](01-overview/objectives.md) to understand what ERE is optimizing for
3. Explore the Systems sections relevant to your role
4. Understand the [Roadmap](08-roadmap/README.md) to see where ERE is headed
