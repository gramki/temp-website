# Scenario Design Desk

> **Status:** 🔴 Stub — Placeholder for expansion

**Scenario Design Desk** is the normative design environment for **Process Architects** to define scenarios, SOPs, knowledge structures, and operational patterns within a Workbench.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Primary Persona** | Process Architect |
| **Scope** | Workbench |
| **Access** | Web, MCP (Creator Gateway) |

---

## Purpose

The Process Architect owns the **normative design** of automation — what should happen, not how it's implemented. This desk provides tools to:

1. **Define** — Create scenarios with signals, triggers, goals, and SOPs
2. **Structure** — Organize knowledge, roles, and escalation patterns
3. **Validate** — Ensure designs are complete and consistent
4. **Handoff** — Transfer designs to Developers for implementation

---

## Consoles

### Scenario Console

Design and manage operational scenarios.

| Capability | Description |
|------------|-------------|
| **Scenario Builder** | Define Signal → Trigger → Scenario → Goals flows |
| **Signal Designer** | Specify signal sources and schemas |
| **Trigger Designer** | Define matching conditions and transformations |
| **Goal Definition** | Specify scenario goals and SLAs |
| **Role Mapping** | Map organizational roles to scenario roles |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SCENARIO BUILDER                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Visual Canvas                                                       │    │
│  │                                                                      │    │
│  │  ┌───────────┐      ┌───────────┐      ┌───────────┐                │    │
│  │  │  Signal   │ ───▶ │  Trigger  │ ───▶ │  Scenario │                │    │
│  │  │ card.net  │      │ dispute   │      │ resolution│                │    │
│  │  │ disputes  │      │ filed     │      │           │                │    │
│  │  └───────────┘      └───────────┘      └─────┬─────┘                │    │
│  │                                              │                       │    │
│  │                                              ▼                       │    │
│  │                                        ┌───────────┐                 │    │
│  │                                        │   Goals   │                 │    │
│  │                                        │ • Resolve │                 │    │
│  │                                        │   SLA:10D │                 │    │
│  │                                        └───────────┘                 │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  [Save Draft]  [Validate]  [Submit for Implementation]                      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### SOP Console

Create and manage Standard Operating Procedures.

| Capability | Description |
|------------|-------------|
| **SOP Editor** | Rich text editor for procedure documentation |
| **Step Definition** | Define procedure steps with roles and conditions |
| **Decision Trees** | Build decision logic for complex procedures |
| **Checklist Builder** | Create operational checklists |
| **Version Control** | Track SOP versions and changes |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SOP EDITOR                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SOP: Dispute Triage Procedure                           v2.1 (Draft)       │
│  ────────────────────────────────────────────────────────────────────────    │
│                                                                              │
│  ## Step 1: Initial Assessment                                              │
│  Role: Triage Agent                                                         │
│                                                                              │
│  1. Review dispute documentation                                            │
│  2. Classify dispute type:                                                  │
│     - [ ] Fraud-related → Escalate to Fraud Team                           │
│     - [ ] Merchant dispute → Standard process                              │
│     - [ ] Card-not-present → Enhanced review                               │
│                                                                              │
│  ## Step 2: Documentation Review                                            │
│  ...                                                                         │
│                                                                              │
│  [Insert Step]  [Add Decision Point]  [Add Checklist]                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Knowledge Console

Organize knowledge assets for the Workbench.

| Capability | Description |
|------------|-------------|
| **Knowledge Browser** | Navigate SOPs, policies, reference manuals |
| **Content Manager** | Upload and organize knowledge documents |
| **Taxonomy Editor** | Define knowledge categories and tags |
| **Retrieval Config** | Configure knowledge retrieval settings |
| **Access Policies** | Define who can view/edit knowledge |

### Memory Console

Configure Enterprise Memory structure.

| Capability | Description |
|------------|-------------|
| **Schema Designer** | Define memory record schemas |
| **Store Configuration** | Configure memory stores and retention |
| **Access Policies** | Define memory access rules |
| **Linking Rules** | Configure how memories link to entities |

### Escalation Console

Design escalation patterns.

| Capability | Description |
|------------|-------------|
| **Escalation Matrix Builder** | Define time-based and rejection-based escalation |
| **Level Definition** | Specify escalation levels and assignees |
| **Notification Rules** | Configure escalation notifications |
| **SLA Integration** | Link escalation to SLA breaches |

---

## Key Workflows

### 1. Scenario Design

```
Process Architect      Scenario Console         Workbench
 │                           │                       │
 ├─── Open Scenario ────────▶│                       │
 │                           │                       │
 ├─── Define Signals ───────▶│                       │
 ├─── Define Triggers ──────▶│                       │
 ├─── Define Goals ─────────▶│                       │
 ├─── Map Roles ────────────▶│                       │
 │                           │                       │
 ├─── Validate ─────────────▶│                       │
 │◀── Validation Result ─────┤                       │
 │                           │                       │
 ├─── Submit for Impl ──────▶│                       │
 │                           ├─── Notify Developer ─▶│
 │                           │                       │
```

### 2. SOP Creation

```
Process Architect       SOP Console           Knowledge Services
 │                           │                       │
 ├─── Create SOP ───────────▶│                       │
 │                           │                       │
 ├─── Edit Content ─────────▶│                       │
 ├─── Add Steps ────────────▶│                       │
 ├─── Add Checklists ───────▶│                       │
 │                           │                       │
 ├─── Publish ──────────────▶│                       │
 │                           ├─── Index SOP ────────▶│
 │◀── Published ─────────────┤                       │
 │                           │                       │
```

### 3. Design Handoff to Developer

```
Process Architect      Scenario Console         Developer
 │                           │                       │
 ├─── Complete Design ──────▶│                       │
 │                           │                       │
 ├─── Generate Spec ────────▶│                       │
 │                           ├─── Create Draft CRD ─▶│
 │                           │                       │
 │                           ├─── Notify Developer ─▶│
 │                           │                       │
 │◀── Handoff Complete ──────┤                       │
 │                           │                       │
```

---

## Design Artifacts

### Scenario Normative Specification

The PA produces a normative specification that guides Developer implementation:

```yaml
scenario_normative_spec:
  id: "dispute-triage"
  name: "Dispute Triage"
  
  # Signal sources
  signals:
    - source: "card-network"
      topic: "disputes"
      description: "Dispute events from card networks"
  
  # Trigger conditions
  triggers:
    - name: "dispute-filed"
      condition: "event.type == 'DISPUTE_FILED'"
  
  # Operational goals
  goals:
    - id: "resolve-dispute"
      description: "Resolve the dispute within SLA"
      sla: "P10D"
  
  # Roles involved
  roles:
    - id: "triage-agent"
      description: "Initial dispute assessment"
    - id: "resolution-specialist"
      description: "Final resolution authority"
  
  # SOPs
  sops:
    - ref: "sop-dispute-triage"
    - ref: "sop-dispute-resolution"
  
  # Escalation patterns
  escalation:
    time_based:
      - after: "PT4H"
        level: 2
    rejection_based:
      - on: "cannot_resolve"
        to: "supervisor"
  
  # Automation approach (from APO)
  automation_approach:
    type: "conventional"  # conventional | agentic | hybrid
```

---

## Integration with Other Desks

| Related Desk | Handoff |
|--------------|---------|
| **Automation Product Desk** | APO → PA: Charter approved, design begins |
| **Automation Development Desk** | PA → Developer: Normative spec for implementation |
| **Supervisor Desk** | PA → Supervisor: Escalation matrix handoff |

---

## Channel Support

| Channel | Access |
|---------|--------|
| **Web** | Full desk access |
| **MCP** | Scenario query, SOP retrieval via Creator Gateway |
| **REST** | Programmatic access to scenarios and SOPs |

---

## Related Documentation

- [Process Architect Persona](../../08-personas-and-journeys/personas/process-architect.md)
- [Scenario Development Journey](../../08-personas-and-journeys/journeys/scenario-development.md)
- [Automation Product Desk](./automation-product-desk.md) — Upstream: Charter definition
- [Automation Development Desk](./automation-development-desk.md) — Downstream: Implementation
- [Knowledge Services](../../04-subsystems/knowledge-services/README.md) — Knowledge storage

---

*TODO: Detailed scenario templates, SOP authoring guidelines, knowledge taxonomy standards*

