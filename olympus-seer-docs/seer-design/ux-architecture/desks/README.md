# Seer Desks

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Related:** [UX Architecture Overview](../README.md) | [Desk Requirements](../desk-requirements.md)

---

## Overview

**Desks** are persona-specific workspaces in Seer. Each desk is the primary operational console for a Seer persona, providing all the capabilities they need to fulfill their responsibilities.

---

## Desk-to-Persona Mapping

| Desk | Persona | Primary Focus |
|------|---------|---------------|
| [Agent Portfolio Desk](./agent-portfolio-desk/README.md) | Automation Product Owner (APO) | Business outcomes, autonomy management |
| [Agent Design Desk](./agent-design-desk/README.md) | Cognitive Systems Architect (CSA) | Architecture, patterns, validation |
| [Agent Development Desk](./agent-development-desk/README.md) | Agent Engineer (AE) | Build, test, deploy |
| [Knowledge Governance Desk](./knowledge-governance-desk/README.md) | Knowledge & Memory Owner (KMO) | Curate, govern, promote |
| [Agent Operations Desk](./agent-operations-desk/README.md) | Agent Reliability Engineer (ARE) | Observe, control, recover |
| [Cognitive Health Desk](./cognitive-health-desk/README.md) | Cognitive Operations Steward (COS) | Monitor, detect, route |
| [Agent Compliance Desk](./agent-compliance-desk/README.md) | AI Risk & Audit Owner (ARAO) | Approve, audit, enforce |

---

## Desk Architecture

### Structure

Each desk follows a consistent structure:

```
desk/
├── README.md           # Desk overview, purpose, key journeys
├── console-1.md        # Console specification
├── console-2.md        # Console specification
└── console-3.md        # Console specification
```

### Consoles

Each desk contains 2-4 **consoles** — focused functional views within the desk:

| Desk | Console 1 | Console 2 | Console 3 |
|------|-----------|-----------|-----------|
| Agent Portfolio | Portfolio Console | Outcomes Console | Autonomy Console |
| Agent Design | Design Console | Topology Console | Validation Console |
| Agent Development | Development Console | Test Console | Release Console |
| Knowledge Governance | Knowledge Console | Memory Console | Learning Console |
| Agent Operations | Health Console | Control Console | Incident Console |
| Cognitive Health | Behavior Console | Patterns Console | Issues Console |
| Agent Compliance | Autonomy Console | Compliance Console | Security Console |

---

## OPDA Integration

Each desk demonstrates **OPDA** (Observable, Predictable, Directable, Authority Enforceable) capabilities:

| OPDA | Description | Desk Integration |
|------|-------------|------------------|
| **Observable** | Can we see what agents are doing? | Dashboards, traces, metrics |
| **Predictable** | Will agents behave consistently? | Baselines, trends, forecasting |
| **Directable** | Can humans guide agents? | Control levers, overrides, configurations |
| **Authority Enforceable** | Are agents within approved limits? | Approval workflows, policy enforcement |

### Per-Desk OPDA

| Desk | O | P | D | A |
|------|---|---|---|---|
| Agent Portfolio | Outcomes metrics | Trend analysis | Autonomy proposals | Autonomy approval workflow |
| Agent Design | Design metrics | Pattern compliance | Design constraints | Validation sign-off |
| Agent Development | Test results, telemetry | Behavioral tests | Code/prompt changes | Release approval |
| Knowledge Governance | Usage metrics | Quality trends | Knowledge curation | Promotion approvals |
| Agent Operations | Health metrics | SLO forecasting | Control levers | Deployment gates |
| Cognitive Health | Behavior quality | Drift detection | Issue routing | Baseline updates |
| Agent Compliance | Compliance status | Risk assessment | Approval decisions | Autonomy approvals |

---

## Channel Access

Each desk is accessible through multiple channels:

| Channel | Description | Primary Users |
|---------|-------------|---------------|
| **Web UI** | Full-featured browser interface | All personas |
| **REST API** | Programmatic access | Integrations, automation |
| **MCP** | AI assistant integration | All personas via AI assistants |
| **CLI** | Command-line tools | AE, ARE |

See [REST Channels](../rest-channels/README.md) for API documentation.

---

## Common Consoles

Some consoles are shared across desks:

| Common Console | Used By | Purpose |
|----------------|---------|---------|
| [Agent Behavior Console](../common-consoles/agent-behavior-console.md) | COS, ARE, AE | Analyze agent reasoning |

---

## Documentation Format

Each desk document follows this structure:

### README.md (Desk Overview)
1. **Purpose** — What the desk is for
2. **Primary Persona** — Who uses it
3. **Consoles** — List of consoles
4. **Key Journeys** — Critical workflows
5. **Channel Access** — How to access
6. **OPDA Integration** — How OPDA is demonstrated
7. **Integration Points** — Connections to other desks

### Console Documents
1. **Purpose** — What the console does
2. **Sections** — UI sections with capabilities
3. **Key Features** — Important features
4. **Data Sources** — Where data comes from
5. **Actions** — What users can do
6. **Indicative Wireframe** — Visual mockup
7. **REST API** — Supporting APIs
8. **OPDA Contribution** — How this console supports OPDA

---

## Documentation Index

Each desk folder contains detailed documentation:

- [x] [Agent Portfolio Desk](./agent-portfolio-desk/README.md) — Complete
- [x] [Agent Design Desk](./agent-design-desk/README.md) — Complete
- [x] [Agent Development Desk](./agent-development-desk/README.md) — Complete
- [x] [Knowledge Governance Desk](./knowledge-governance-desk/README.md) — Complete
- [x] [Agent Operations Desk](./agent-operations-desk/README.md) — Complete
- [x] [Cognitive Health Desk](./cognitive-health-desk/README.md) — Complete
- [x] [Agent Compliance Desk](./agent-compliance-desk/README.md) — Complete

---

*Status: 🟡 Draft — Structure and detailed console specs complete*
