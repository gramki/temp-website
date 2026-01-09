# Seer UX Architecture: Desk Requirements

> **Status:** 🔴 Planning — Requirements captured, details TBD  
> **Last Updated:** 2026-01-09  
> **Related:** [Role Definitions](../personas-and-needs/roles.md) | [Hub UX Architecture](../../../olympus-hub-docs/06-ux-architecture/README.md)

---

## Overview

This document captures the UX requirements for Seer personas. Each persona requires:
- **Desk** — Primary operational console
- **Consoles** — Functional views within the desk
- **Journeys** — Key workflows the persona must complete
- **Channels** — Access methods (Web, CLI, MCP, REST)

Seer UX follows the same (Persona, Channel, Use Case) meta approach as Hub.

---

## Persona-to-Desk Mapping

| Persona | Desk | Primary Focus |
|---------|------|---------------|
| Agent Product Owner (APO) | **Agent Portfolio Desk** | Business outcomes, autonomy management |
| Cognitive Systems Architect (CSA) | **Agent Design Studio** | Architecture, patterns, validation |
| Agent Engineer (AE) | **Agent Development Workbench** | Build, test, deploy |
| Knowledge & Memory Owner (KMO) | **Knowledge Governance Desk** | Curate, govern, promote |
| Agent Reliability Engineer (ARE) | **Agent Operations Desk** | Observe, control, recover |
| Cognitive Operations Steward (COS) | **Cognitive Health Desk** | Monitor, detect, route |
| AI Risk & Audit Owner (ARAO) | **Agent Compliance Desk** | Approve, audit, enforce |

---

## 1. Agent Product Owner (APO) — Agent Portfolio Desk

### Purpose
Manage agent portfolio, track business outcomes, and govern autonomy requests.

### Consoles

| Console | Purpose |
|---------|---------|
| **Agent Catalog** | View all agents, their status, and ownership |
| **Outcomes Dashboard** | Track business KPIs per agent |
| **Autonomy Registry** | View/manage autonomy levels and proposals |
| **Improvement Backlog** | Prioritize agent improvements |
| **Stakeholder Reports** | Generate executive summaries |

### Key Journeys

| Journey | Description |
|---------|-------------|
| **Agent Chartering** | Define new agent purpose, scope, success criteria |
| **Autonomy Proposal** | Propose autonomy level, submit for ARAO approval |
| **Outcome Review** | Assess agent value delivery, adjust priorities |
| **Feedback Triage** | Review COS/ARE feedback, prioritize responses |

### Channels

| Channel | Use Case |
|---------|----------|
| Web | Primary access |
| Email | Notifications, reports |
| REST API | Integration with portfolio tools |

---

## 2. Cognitive Systems Architect (CSA) — Agent Design Studio

### Purpose
Design agent architectures, define patterns, validate implementations.

### Consoles

| Console | Purpose |
|---------|---------|
| **Pattern Library** | Browse and manage approved cognitive patterns |
| **Agent Architecture Viewer** | Visualize agent designs |
| **Design Validation Console** | Review AE implementations against designs |
| **Multi-Agent Topology** | View and design agent interactions |
| **Failure Mode Catalog** | Document and track failure semantics |

### Key Journeys

| Journey | Description |
|---------|-------------|
| **Pattern Definition** | Create new cognitive pattern, document constraints |
| **Architecture Review** | Review agent design before implementation |
| **Implementation Validation** | Validate AE work matches design |
| **Failure Analysis** | Investigate design-related issues from COS |

### Channels

| Channel | Use Case |
|---------|----------|
| Web | Primary access |
| CLI | Pattern tooling, validation scripts |
| MCP | AI-assisted design |

---

## 3. Agent Engineer (AE) — Agent Development Workbench

### Purpose
Build, test, and deploy agents with proper operability contracts.

### Consoles

| Console | Purpose |
|---------|---------|
| **Agent Builder** | Code, prompts, workflows |
| **Tool Integration Console** | Manage tool bindings |
| **Test Runner** | Execute behavioral and integration tests |
| **Telemetry Configurator** | Define and validate observability |
| **Deployment Manager** | Version, release, rollback |
| **ARE Handoff Console** | Validate and submit operability contracts |

### Key Journeys

| Journey | Description |
|---------|-------------|
| **Agent Implementation** | Build agent per CSA design |
| **Tool Integration** | Bind and test external tools |
| **Production Readiness** | Complete checklist, submit for ARE review |
| **Incident Support** | Investigate issues flagged by COS/ARE |

### Channels

| Channel | Use Case |
|---------|----------|
| Web | Primary access |
| CLI | Development tooling |
| IDE Plugin | In-editor development |
| MCP | AI-assisted coding |

---

## 4. Knowledge & Memory Owner (KMO) — Knowledge Governance Desk

### Purpose
Curate knowledge, govern memory, manage enterprise learning.

### Consoles

| Console | Purpose |
|---------|---------|
| **Knowledge Catalog** | Browse, search, manage knowledge sources |
| **Memory Governance Console** | Set retention, decay, access policies |
| **Tool Registry** | Curate tool availability and access |
| **Promotion Queue** | Review COS-flagged patterns for promotion |
| **Quality Dashboard** | Track knowledge freshness, accuracy, coverage |

### Key Journeys

| Journey | Description |
|---------|-------------|
| **Knowledge Onboarding** | Add new knowledge source, validate, publish |
| **Memory Policy Definition** | Define retention, decay, access rules |
| **Promotion Review** | Evaluate COS-flagged patterns for promotion |
| **Conflict Resolution** | Resolve conflicting knowledge/memories |

### Channels

| Channel | Use Case |
|---------|----------|
| Web | Primary access |
| REST API | Knowledge pipeline integration |
| MCP | AI-assisted curation |

---

## 5. Agent Reliability Engineer (ARE) — Agent Operations Desk

### Purpose
Operate agents safely, monitor health, respond to incidents.

### Consoles

| Console | Purpose |
|---------|---------|
| **System Health Dashboard** | AHS, CHR, availability, latency |
| **Agent Control Panel** | Kill switches, bounds, levers |
| **Incident Console** | Triage, contain, recover |
| **Cost Observatory** | Token usage, API costs, budget tracking |
| **SLO Tracker** | SLO status, burn rates, alerts |
| **Deployment Console** | Production readiness gates, rollbacks |

### Key Journeys

| Journey | Description |
|---------|-------------|
| **Production Gate** | Review and approve agent for production |
| **Incident Response** | Detect, contain, recover from incidents |
| **Cost Intervention** | Investigate and resolve cost anomalies |
| **Capacity Planning** | Plan and request capacity from provider |

### Channels

| Channel | Use Case |
|---------|----------|
| Web | Primary access |
| Mobile | On-call alerting |
| CLI | Operational tooling |
| PagerDuty/Slack | Incident notifications |
| REST API | Automation, integration |

---

## 6. Cognitive Operations Steward (COS) — Cognitive Health Desk

### Purpose
Monitor agent behavior, detect drift, route issues to owners.

### Consoles

| Console | Purpose |
|---------|---------|
| **Behavior Monitor** | Consistency, confidence, quality signals |
| **Drift Detection Console** | Track deviation from baselines |
| **Pattern Discovery** | Identify patterns for enterprise learning |
| **Issue Router** | Triage and route to APO/CSA/AE/KMO/ARAO |
| **User Feedback Console** | Review overrides, escalations, sentiment |

### Key Journeys

| Journey | Description |
|---------|-------------|
| **Drift Investigation** | Investigate detected drift, determine cause |
| **Pattern Flagging** | Flag pattern to KMO for promotion review |
| **Issue Routing** | Triage issue, route to appropriate owner |
| **Behavioral Baseline** | Establish and update behavior baselines |

### Channels

| Channel | Use Case |
|---------|----------|
| Web | Primary access |
| Slack/Teams | Issue notifications |
| REST API | Automated detection pipelines |

---

## 7. AI Risk & Audit Owner (ARAO) — Agent Compliance Desk

### Purpose
Approve autonomy, ensure compliance, maintain audit readiness.

### Consoles

| Console | Purpose |
|---------|---------|
| **Autonomy Approval Queue** | Review and approve/reject proposals |
| **Compliance Dashboard** | Policy adherence, violation tracking |
| **Audit Evidence Console** | Access decision records, evidence bundles |
| **Security Posture Console** | AI security controls, penetration test results |
| **Risk Register** | Track and manage agent-related risks |

### Key Journeys

| Journey | Description |
|---------|-------------|
| **Autonomy Review** | Evaluate APO proposal, approve or reject |
| **Compliance Investigation** | Investigate COS-flagged compliance concern |
| **Audit Preparation** | Gather evidence, prepare for external audit |
| **Security Assessment** | Validate AI security controls |

### Channels

| Channel | Use Case |
|---------|----------|
| Web | Primary access |
| Email | Approval notifications |
| REST API | GRC tool integration |

---

## Shared Components

### Cross-Desk Consoles

Some consoles appear in multiple desks with appropriate permissions:

| Console | APO | CSA | AE | KMO | ARE | COS | ARAO |
|---------|-----|-----|-----|-----|-----|-----|------|
| Agent Catalog | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Knowledge Base | Read | Read | Read | Full | Read | Read | Read |
| Audit Trail | Read | — | — | — | Read | Read | Full |
| Alerts & Notifications | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### Common Channels

| Channel | Description |
|---------|-------------|
| **Seer Web Portal** | Primary web access for all desks |
| **Seer CLI** | Command-line tools for AE, ARE |
| **Seer MCP Server** | AI assistant access |
| **Seer REST API** | Programmatic access |
| **Watch Integration** | Observability dashboards (via [Observability Extensions](../subsystems/observability-extensions-to-watch.md)) |

---

## Integration with Hub

Seer desks integrate with Hub desks where responsibilities overlap:

| Seer Persona | Hub Integration Point |
|--------------|----------------------|
| ARE | Hub SRE Ops Center (infrastructure layer) |
| AE | Workbench Studio (scenario binding) |
| KMO | Knowledge Base Console (content sync) |
| COS | Steward Desk (behavior alerts) |

---

## Next Steps

Each desk requires detailed specification:
1. Console wireframes
2. Data requirements
3. API contracts
4. Permission model
5. Alert definitions
6. Integration specifications

These will be documented in subsequent discussions.

---

*Status: 🔴 Planning — Requirements captured for detailed design*

