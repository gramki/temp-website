# AI Agents

[← Back to AI-Native Architecture](README.md) | [← Back to ERE](../README.md)

ERE deploys two categories of AI agents: a **customer-facing Engagement Concierge** and **internal Specialized Drafting Agents** for specific domains.

---

## Customer-Facing: Engagement Concierge

The Customer Portal is paired with an **Engagement Concierge** — an AI agent that serves as the customer's intelligent interface to their Engagement.

### Capabilities

| Capability | Description |
|------------|-------------|
| **Answer questions** | Status, artifacts, decisions, next steps — anything about the customer's Engagement |
| **Accept requests** | Scope changes, meeting scheduling, artifact access — routes to appropriate workflows |
| **Proactive notifications** | Guidance and alerts based on lifecycle phase |
| **Continuous learning** | Improves response quality from customer interactions |

### Progressive Autonomy

The Concierge operates under the same progressive model as all ERE tools:

| State | Behavior |
|-------|----------|
| **Initial (Assistive)** | Answers questions, explains status, routes complex requests to humans |
| **Target (Automative)** | Processes routine requests autonomously (meeting scheduling, artifact access) |

**Progression criteria:**
- 90%+ accuracy on Q&A
- <5% escalation rate on routine requests
- Positive customer feedback trends

See [Agent Governance](agent-governance.md) for full progression criteria.

---

## Internal: Specialized Drafting Agents

Every drafting use case is supported by **skill-specific agents** fine-tuned for that domain. These agents share a common knowledge layer (Proposal Repository, Pattern Library, Case Studies) and are governed by the same progressive enforcement model.

### Agent Inventory

| Agent | Domain | Skills | Initial State |
|-------|--------|--------|---------------|
| **Proposal Agent** | Presales | Drafts proposals from templates, past wins, and customer context | Assistive — drafts sections for human review |
| **Architecture Agent** | Solution design | Generates solution architectures from requirements and archetypes | Assistive |
| **BRD Agent** | Requirements | Drafts BRDs from discovery notes; validates completeness against archetype | Assistive |
| **Estimation Agent** | Planning | Generates estimates from historical data; flags outliers | Assistive |
| **Governance Agent** | Compliance | Prepares gate review materials; checks artifact completeness | Assistive — flags missing artifacts |
| **Retrospective Agent** | Knowledge capture | Synthesizes learnings; extracts patterns; drafts case studies | Assistive |

### Shared Knowledge Layer

All agents access and contribute to:

| Knowledge Source | Purpose |
|------------------|---------|
| **Proposal Repository** | Past proposals with outcome data (won/lost, reasons, reuse potential) |
| **Pattern Library** | Reusable architecture patterns, integration recipes, Studio Component templates |
| **Case Studies** | Completed Engagement narratives with metrics and differentiators |
| **Archetype Definitions** | Reference architectures and gap analysis for each customer archetype |

### Agent Interaction Model

```
┌─────────────────────────────────────────────────────────────┐
│                    Shared Knowledge Layer                    │
│  (Proposal Repository, Pattern Library, Case Studies, etc.) │
└─────────────────────────────────────────────────────────────┘
         ▲           ▲           ▲           ▲           ▲
         │           │           │           │           │
    ┌────┴───┐  ┌────┴───┐  ┌────┴───┐  ┌────┴───┐  ┌────┴───┐
    │Proposal│  │  BRD   │  │  Est.  │  │  Gov.  │  │ Retro  │
    │ Agent  │  │ Agent  │  │ Agent  │  │ Agent  │  │ Agent  │
    └────────┘  └────────┘  └────────┘  └────────┘  └────────┘
         │           │           │           │           │
         ▼           ▼           ▼           ▼           ▼
┌─────────────────────────────────────────────────────────────┐
│                  Progressive Governance                      │
│            (Assistive → Automative based on metrics)         │
└─────────────────────────────────────────────────────────────┘
```

---

## Agent-to-Tool Mapping

Each agent is embedded in specific ERE tools:

| Agent | Primary Tools |
|-------|---------------|
| **Engagement Concierge** | Customer Portal |
| **Proposal Agent** | Proposal Kit, Proposal Repository |
| **Architecture Agent** | PoC App Builders, Pattern Library |
| **BRD Agent** | BRD Author & Validator |
| **Estimation Agent** | Estimation Workbench, Estimation & Planning Suite |
| **Governance Agent** | Governance Prep Suite |
| **Retrospective Agent** | Retrospective Synthesizer, Case Study Generator |

---

*See also: [Agent Governance](agent-governance.md) | [Presales Toolkit](../02-systems/presales-toolkit.md) | [Delivery Toolkit](../02-systems/delivery-toolkit.md)*
