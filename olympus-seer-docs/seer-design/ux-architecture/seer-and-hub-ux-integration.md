# Seer and Hub UX Integration

> **Status:** 🔴 Planning  
> **Last Updated:** 2026-01-09  
> **Related:** [Desk Requirements](./desk-requirements.md) | [Hub UX Architecture](../../../olympus-hub-docs/06-ux-architecture/README.md)

---

## Overview

Seer is an **extension to Hub**, not a standalone platform. All Seer desks operate within the context of Hub Workbenches.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              HUB PLATFORM                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                         WORKBENCH (AOS)                              │   │
│   ├─────────────────────────────────────────────────────────────────────┤   │
│   │                                                                      │   │
│   │   ┌──────────────────────┐    ┌──────────────────────┐              │   │
│   │   │     HUB DESKS        │    │    SEER DESKS        │              │   │
│   │   │  ┌────────────────┐  │    │  ┌────────────────┐  │              │   │
│   │   │  │ Workbench      │  │    │  │ Agent Design   │  │              │   │
│   │   │  │ Studio         │  │    │  │ Desk           │  │              │   │
│   │   │  ├────────────────┤  │    │  ├────────────────┤  │              │   │
│   │   │  │ Agent Desk     │  │    │  │ Agent Dev      │  │              │   │
│   │   │  │                │  │    │  │ Desk           │  │              │   │
│   │   │  ├────────────────┤  │    │  ├────────────────┤  │              │   │
│   │   │  │ Supervisor     │  │    │  │ Agent Ops      │  │              │   │
│   │   │  │ Desk           │  │    │  │ Desk           │  │              │   │
│   │   │  └────────────────┘  │    │  └────────────────┘  │              │   │
│   │   └──────────────────────┘    └──────────────────────┘              │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Core Principle: Workbench = AOS

Each **Workbench** in Hub represents an **Agent-Oriented System (AOS)**.

| Concept | Definition |
|---------|------------|
| **Workbench** | A scoped environment for a business domain |
| **AOS** | A collection of agents, scenarios, and knowledge working together |
| **Seer Desks** | Specialized views for designing, building, and operating agents within the AOS |

All stakeholders collaborate **within Workbench scope**. A user may have access to multiple Workbenches, but each desk view is scoped to one Workbench at a time.

---

## AOS Lifecycle Stages

Hub+Seer support the complete lifecycle of an AOS:

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ DESIGN  │───▶│  BUILD  │───▶│ DEPLOY  │───▶│   RUN   │───▶│ EVOLVE  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │              │
     ▼              ▼              ▼              ▼              ▼
  Define         Implement      Release       Operate       Improve
  intent,        agents,        to            safely,       based on
  architecture   test           production    monitor       learnings
```

### Stage Definitions

| Stage | Focus | Key Activities |
|-------|-------|----------------|
| **Design** | Intent and architecture | Charter agents, define patterns, design knowledge |
| **Build** | Implementation | Develop agents, integrate tools, test |
| **Deploy** | Production release | Gate review, staged rollout, ARE handoff |
| **Run** | Operations | Monitor health, respond to incidents, control |
| **Evolve** | Continuous improvement | Analyze patterns, promote learnings, adjust autonomy |

---

## Desk Enablement by Stage

Not all desks are relevant at every stage. Workbenches are **tagged with their current stage**, and desks are enabled accordingly.

### Desk Availability Matrix

| Desk | Design | Build | Deploy | Run | Evolve |
|------|:------:|:-----:|:------:|:---:|:------:|
| **Automation Portfolio Desk** (APO) | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Agent Design Desk** (CSA) | ✓ | ✓ | — | — | ✓ |
| **Agent Development Desk** (AE) | — | ✓ | ✓ | — | ✓ |
| **Knowledge Governance Desk** (KMO) | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Agent Operations Desk** (ARE) | — | — | ✓ | ✓ | ✓ |
| **Cognitive Health Desk** (COS) | — | — | — | ✓ | ✓ |
| **Agent Compliance Desk** (ARAO) | ✓ | — | ✓ | ✓ | ✓ |

### Stage Transitions

| Transition | Gate | Key Approvals |
|------------|------|---------------|
| Design → Build | Architecture Approved | CSA sign-off |
| Build → Deploy | Production Readiness | ARE + ARAO sign-off |
| Deploy → Run | Deployment Complete | ARE confirmation |
| Run → Evolve | Learning Triggers | COS + KMO identification |
| Evolve → Design | Major Changes | APO + CSA decision |

---

## Persona-to-Stage Mapping

### Primary Focus by Stage

| Stage | Primary Personas | Supporting Personas |
|-------|-----------------|---------------------|
| **Design** | APO, CSA | KMO, ARAO |
| **Build** | AE | CSA, KMO, APO |
| **Deploy** | ARE | AE, ARAO |
| **Run** | ARE, COS | APO, ARAO |
| **Evolve** | COS, KMO | APO, CSA, AE |

### Cross-Stage Collaboration

```
          DESIGN              BUILD              DEPLOY               RUN               EVOLVE
            │                   │                   │                  │                   │
    APO ────┼───────────────────┼───────────────────┼──────────────────┼───────────────────┼────▶
            │                   │                   │                  │                   │
    CSA ────┼───────────────────┼───────────────────│──────────────────│───────────────────┼────▶
            │                   │                   │                  │                   │
    AE  ────│───────────────────┼───────────────────┼──────────────────│───────────────────┼────▶
            │                   │                   │                  │                   │
    KMO ────┼───────────────────┼───────────────────┼──────────────────┼───────────────────┼────▶
            │                   │                   │                  │                   │
    ARE ────│───────────────────│───────────────────┼──────────────────┼───────────────────┼────▶
            │                   │                   │                  │                   │
    COS ────│───────────────────│───────────────────│──────────────────┼───────────────────┼────▶
            │                   │                   │                  │                   │
   ARAO ────┼───────────────────│───────────────────┼──────────────────┼───────────────────┼────▶
            │                   │                   │                  │                   │
```

**Legend:** `─────` = Active in stage | `│` = Transition point

---

## Hub + Seer Desk Integration

### Hub Desks (Existing)

| Hub Desk | Purpose | Lifecycle Focus |
|----------|---------|-----------------|
| **Hub Control Center** | Tenant administration | All stages |
| **Workbench Studio** | Scenario design, knowledge | Design, Build |
| **Agent Desk** | Task execution (human agents) | Run |
| **Supervisor Desk** | Queue management, escalations | Run |
| **Steward Desk** | Runtime monitoring | Run, Evolve |

### Seer Desks (Extension)

| Seer Desk | Purpose | Lifecycle Focus |
|-----------|---------|-----------------|
| **Agent Portfolio Desk** | Agent intent and outcomes | All stages |
| **Agent Design Desk** | Cognitive architecture | Design, Build, Evolve |
| **Agent Development Desk** | Agent implementation | Build, Deploy, Evolve |
| **Knowledge Governance Desk** | Knowledge and memory | All stages |
| **Agent Operations Desk** | Agent operations | Deploy, Run, Evolve |
| **Cognitive Health Desk** | Behavioral monitoring | Run, Evolve |
| **Agent Compliance Desk** | Governance and audit | Design, Deploy, Run, Evolve |

---

## Integration Points

### Shared Components

| Component | Hub Owns | Seer Extends |
|-----------|----------|--------------|
| **Workbench Context** | Workbench identity, access | Agent-specific views |
| **Knowledge Base** | Storage, search | Agent access policies, CAE integration |
| **Task System** | Task queues, assignment | Agent task handling, escalation |
| **Observability** | Watch infrastructure | Agent-specific metrics, AHS/CHR |
| **User Management** | Identity, permissions | Role-based desk access |

### Cross-Desk Navigation

Users navigate between Hub and Seer desks within the same Workbench:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          WORKBENCH NAVIGATION                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │ 🏠 Workbench Home                                                   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────┐    ┌─────────────────────────┐                 │
│  │ HUB DESKS               │    │ SEER DESKS              │                 │
│  │ ├── Workbench Studio    │    │ ├── Agent Portfolio     │                 │
│  │ ├── Agent Desk          │    │ ├── Agent Design        │                 │
│  │ ├── Supervisor Desk     │    │ ├── Agent Development   │                 │
│  │ └── Steward Desk        │    │ ├── Knowledge Gov       │                 │
│  │                         │    │ ├── Agent Operations    │                 │
│  │                         │    │ ├── Cognitive Health    │                 │
│  │                         │    │ └── Agent Compliance    │                 │
│  └─────────────────────────┘    └─────────────────────────┘                 │
│                                                                              │
│  Desk availability based on: User Role + Workbench Stage                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Workbench Stage Configuration

### Stage Assignment

Workbenches are tagged with their current lifecycle stage:

```yaml
workbench:
  id: "claims-processing-wb"
  name: "Claims Processing"
  stage: "run"  # design | build | deploy | run | evolve
  
  stage_history:
    - stage: "design"
      entered: "2025-08-01"
      exited: "2025-09-15"
    - stage: "build"
      entered: "2025-09-15"
      exited: "2025-11-01"
    - stage: "deploy"
      entered: "2025-11-01"
      exited: "2025-11-15"
    - stage: "run"
      entered: "2025-11-15"
      exited: null  # current stage
```

### Stage Transition Rules

| Transition | Required Conditions |
|------------|---------------------|
| → Design | Workbench created |
| → Build | At least one agent charter approved |
| → Deploy | All agents pass production readiness |
| → Run | Deployment confirmed, ARE accepting |
| → Evolve | Manual trigger by APO or COS |

---

## Access Control

### Role-to-Desk Permissions

Users are assigned roles, and roles grant access to desks:

| Role | Primary Desk | Additional Desk Access |
|------|--------------|------------------------|
| APO | Agent Portfolio | — |
| CSA | Agent Design | Agent Portfolio (read) |
| AE | Agent Development | Agent Design (read), Agent Portfolio (read) |
| KMO | Knowledge Governance | — |
| ARE | Agent Operations | Agent Development (read), Compliance (read) |
| COS | Cognitive Health | Agent Operations (read), Knowledge (read) |
| ARAO | Agent Compliance | All desks (audit read) |

### Stage-Based Access

Even with role access, desk availability depends on stage:

```
Access = Role Permission ∩ Stage Enablement
```

Example: An AE has Agent Development Desk permission, but if the Workbench is in "Run" stage, the Development Desk is disabled.

---

## Console Sharing Across Desks

Some consoles appear in multiple desks with different permissions:

| Console | Appears In | Permissions |
|---------|------------|-------------|
| **Agent Catalog** | All desks | View (all), Edit (APO) |
| **Knowledge Browser** | KMO, AE, CSA, COS | Edit (KMO), View (others) |
| **Health Dashboard** | ARE, COS, APO | Full (ARE), View (others) |
| **Compliance Evidence** | ARAO, ARE | Full (ARAO), View (ARE) |

---

## Related Documentation

- [Desk Requirements](./desk-requirements.md) — Detailed desk specifications
- [Hub UX Architecture](../../../olympus-hub-docs/06-ux-architecture/README.md) — Hub desk patterns
- [Role Definitions](../personas-and-needs/roles.md) — Persona definitions
- [Hub Integration Overview](../hub-integration/README.md) — Technical integration

---

*Status: 🔴 Planning — Integration model defined, implementation TBD*

