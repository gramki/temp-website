# 1.9 Persona-Specific Desks: Purpose-Built Experiences

Seer provides dedicated **Desks** for each persona—purpose-built experiences that extend Hub's UX architecture. Rather than providing a generic interface that all personas must adapt to, Seer provides tailored experiences optimized for each persona's specific workflows.

## UX Architecture Principles

Seer's UX architecture shares principles with Hub:

| Principle | Description |
|-----------|-------------|
| **Persona-Focused** | Each persona has a dedicated Desk optimized for their work |
| **Channel-Agnostic** | Web, CLI, MCP, REST—same capabilities, multiple delivery mechanisms |
| **Journey-Driven** | Interfaces organized by workflows, not just screens |
| **Integrated with Hub** | Seer Desks integrate with Hub Workbenches seamlessly |

## Seer Desks (Agent-Oriented Personas)

Each agent-oriented persona has a dedicated Desk:

| Persona | Desk | Purpose |
|---------|------|---------|
| **APO** | Agent Portfolio Desk | Business outcomes, autonomy governance |
| **CSA** | Agent Design Desk | Architecture, patterns, validation |
| **AE** | Agent Development Desk | Build, test, deploy agents |
| **KMO** | Knowledge Governance Desk | Curate knowledge, govern memory |
| **ARE** | Agent Operations Desk | Observe, control, recover |
| **COS** | Cognitive Health Desk | Monitor behavior, detect drift |
| **ARAO** | Agent Compliance Desk | Approve autonomy, audit, enforce |

### Agent Portfolio Desk (APO)

The Agent Portfolio Desk enables APOs to manage their agent portfolio:

**Key Capabilities:**
- View all agents in their portfolio
- Track business outcomes and success metrics
- Configure autonomy levels
- Prioritize improvement initiatives
- Approve significant changes

### Agent Design Desk (CSA)

The Agent Design Desk supports cognitive architecture work:

**Key Capabilities:**
- Browse cognitive patterns and templates
- Design agent interaction models
- Validate designs before implementation
- Review architectural decisions

### Agent Development Desk (AE)

The Agent Development Desk is the primary interface for agent building:

**Key Capabilities:**
- Create and edit Training Specs
- Configure tool bindings
- Run tests and evaluations
- Debug agent behavior
- Manage deployments

### Knowledge Governance Desk (KMO)

The Knowledge Governance Desk supports knowledge and memory curation:

**Key Capabilities:**
- Manage knowledge sources
- Review and approve promotion requests
- Monitor knowledge quality
- Configure memory governance policies

### Agent Operations Desk (ARE)

The Agent Operations Desk provides operational control:

**Key Capabilities:**
- Monitor agent health and performance
- Execute kill switches and overrides
- Respond to incidents
- Review production readiness

### Cognitive Health Desk (COS)

The Cognitive Health Desk supports day-to-day behavioral monitoring:

**Key Capabilities:**
- Track behavioral metrics
- Detect drift and anomalies
- Route and manage feedback
- Tune operational parameters

### Agent Compliance Desk (ARAO)

The Agent Compliance Desk serves audit and compliance needs:

**Key Capabilities:**
- Review audit records
- Approve autonomy changes
- Generate compliance reports
- Package evidence for regulators

## Hub Desks Extended by Seer

Seer extends Hub's existing desk architecture for operational personas:

| Persona | Hub Desk | Seer Extension |
|---------|----------|----------------|
| **Agent (Human)** | Agent Desk | AI Agent collaboration |
| **Supervisor** | Supervisor Desk | AI Agent oversight |
| **Process Architect** | Scenario Design Desk | Agent scenario design |
| **Developer** | Automation Development Desk | Agent implementation |
| **Tenant Admin** | Hub Control Center | Agent platform configuration |

This extension model means that existing Hub users can work with AI agents through familiar interfaces enhanced with agent-specific capabilities.

## Multi-Channel Access

All Desk capabilities are available through multiple channels:

| Channel | Primary Users |
|---------|---------------|
| **Web Portal** | All personas |
| **CLI** | AE, ARE |
| **MCP Server** | AE, CSA (IDE integration) |
| **REST API** | All (programmatic access) |
| **Watch Dashboards** | ARE, COS |
| **Collaboration** | All (Slack, Teams, Email) |

This channel diversity ensures that personas can work in their preferred environments while maintaining consistent capabilities.

## Key Value

> *Each persona gets exactly the tools they need, organized the way they work, accessible through their preferred channel.*

Purpose-built desks reduce friction, improve efficiency, and ensure that each persona can focus on their specific responsibilities without navigating irrelevant capabilities.

---

**References:**
*   `olympus-seer-docs/seer-design/ux-architecture/desk-requirements.md`
*   `olympus-hub-docs/06-ux-architecture/README.md`
*   `olympus-seer-docs/WHY-SEER-OUTLINE-DRAFT.md` — Section 6.9
