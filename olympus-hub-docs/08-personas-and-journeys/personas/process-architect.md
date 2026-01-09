# Persona: Process Architect

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **Process Architect** designs the operational structure of a Workbench — defining Scenarios, SOPs, and the roles that participate in operations.

| Attribute | Value |
|-----------|-------|
| **Category** | Hub Persona — Workbench Designer |
| **Scope** | Workbench |
| **Domain** | Tenant Identity Domain |
| **Primary Console** | Workbench Studio |

---

## Objectives

| Objective | Description |
|-----------|-------------|
| **Design Scenarios** | Identify operational situations and define how they should be handled |
| **Specify SOPs** | Document procedures, decision criteria, and evidence requirements |
| **Structure Operations** | Define roles, goals, and SLAs for each Scenario |
| **Enable Compliance** | Ensure CAF requirements are met through SOP design |

---

## Key Activities

### Design Phase

1. **Scenario Identification**
   - Analyze business processes for triggerable situations
   - Define scenario boundaries and scope
   - Specify expected signals

2. **SOP Development**
   - Document step-by-step procedures
   - Define decision points and criteria
   - Specify evidence capture requirements

3. **Goal Definition**
   - Set measurable objectives
   - Define SLAs and escalation criteria
   - Align with organizational KPIs

### Collaboration

| With | Activity |
|------|----------|
| **Developer** | Hand off scenario design for implementation |
| **Supervisor** | Collaborate on task delegation and queue design |
| **Auditor** | Ensure compliance requirements are captured in SOPs |

---

## Hub Capabilities Consumed

### Workbench Studio (Primary Interface)

| Capability | What It Provides |
|------------|------------------|
| **Scenario Designer** | Define scenarios, goals, SLAs, roles involved |
| **SOP Editor** | Create and manage Standard Operating Procedures |
| **Knowledge Bank Management** | Organize knowledge categories, upload content, configure retrieval |
| **Memory Configuration** | Define memory store categories, visibility policies, retention |
| **Role Definitions** | Map organizational roles to workbench roles, define capabilities |
| **Checklist Designer** | Create workbench-level checklists for operational governance |

### Hub Services Accessed

| Service | Usage |
|---------|-------|
| **Knowledge Services** | Create/update knowledge base content |
| **Memory Services** | Configure Enterprise Memory structure |
| **Workbench Management** | Define and version Scenario definitions |
| **CAF** | Define decision record schemas, evidence requirements |

### What They Produce

| Output | Consumed By |
|--------|-------------|
| Scenario Definitions | Developer (for implementation) |
| SOPs | Agents (for execution guidance) |
| Knowledge Base Structure | Agents, Applications (for context) |
| Checklist Definitions | Supervisors (for deployment) |

---

## Key Journeys

- [Scenario Development](../journeys/scenario-development.md) — Primary journey
- [Workbench Configuration](../journeys/workbench-configuration.md) — Supporting role

---

## Related Documentation

- [Scenario Definitions](../../04-subsystems/workbench-management/scenario-definitions.md)
- [Knowledge Services](../../04-subsystems/knowledge-services/README.md)
- [Ontology - Perception Layer](../../01-concepts/ontology-1-perception-layer.md)

---

*TODO: Detailed responsibilities, workflow examples, access patterns*

