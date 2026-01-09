# Journey: Automation Lifecycle (Conventional)

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-09

This journey describes the complete lifecycle of a **conventional automation** capability — from initial business need through ongoing evolution. It covers rule-based, workflow-driven automation implemented as Hub Applications.

> **Note:** For agentic automation (AI agents, cognitive reasoning), see the [Agentic Automation Lifecycle](../../../olympus-seer-docs/seer-design/personas-and-needs/journeys/agentic-automation-lifecycle.md) in Seer documentation.

---

## Overview

A conventional automation capability progresses through five lifecycle stages:

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ IDEATE  │───▶│ DESIGN  │───▶│  BUILD  │───▶│   RUN   │───▶│ EVOLVE  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │              │
     ▼              ▼              ▼              ▼              ▼
  Business       Scenario       Implement      Operate        Improve
  case &         design &       & deploy       & monitor      based on
  charter        approach                                     learnings
```

| Stage | Primary Personas | Key Output |
|-------|-----------------|------------|
| **Ideate** | APO | Automation Charter |
| **Design** | Process Architect, APO | Scenario Definition |
| **Build** | Developer | Hub Application, Deployment |
| **Run** | Supervisor, Agent | Operational Execution |
| **Evolve** | APO, Process Architect | Improvements, Learnings |

---

## Stage 1: Ideate (APO)

The Automation Product Owner identifies a business need and creates the business case.

### Activities

1. **Identify Business Need**
   - What problem needs solving?
   - What pain points exist today?
   - What value would automation deliver?

2. **Create Automation Charter**
   - Business justification
   - Success criteria and KPIs
   - Scope and boundaries
   - Initial autonomy expectations

3. **Secure Stakeholder Alignment**
   - Present business case
   - Get funding/resource approval
   - Align on success metrics

### Output: Automation Charter

```yaml
automation_charter:
  id: "dispute-resolution-automation"
  name: "Dispute Resolution Automation"
  workbench: "dispute-resolution-wb"
  
  business_case:
    problem: "Manual dispute processing takes 4+ hours per case"
    opportunity: "60% of disputes are routine and follow standard patterns"
    value: "Reduce processing time to <30 minutes for routine cases"
  
  success_criteria:
    - metric: "Processing Time (routine)"
      baseline: "4 hours"
      target: "30 minutes"
    - metric: "Same-day Resolution Rate"
      baseline: "20%"
      target: "80%"
    - metric: "Customer Satisfaction"
      baseline: "72%"
      target: "85%"
  
  scope:
    in_scope:
      - "Routine card-present disputes"
      - "Standard documentation cases"
    out_of_scope:
      - "Legal disputes"
      - "Regulatory escalations"
      - "Fraud investigations"
  
  owner: "APO: Jane Smith"
  sponsor: "VP Operations"
  target_date: "2026-Q2"
```

### Gate: Charter Approved

| Criterion | Approver |
|-----------|----------|
| Business case valid | Sponsor |
| Resources allocated | Administrator |
| Workbench exists or requested | Administrator |

---

## Stage 2: Design (Process Architect + APO)

The Process Architect designs the scenario, with APO providing business context.

### Activities

1. **Scenario Design**
   - Define signals that trigger the scenario
   - Specify the operational flow
   - Create SOPs and decision criteria
   - See: [Scenario Development Journey](./scenario-development.md) Phase 1

2. **Automation Approach Decision**
   - APO proposes approach based on scenario characteristics
   - Process Architect validates feasibility
   - If agentic approach is chosen, transition to Seer lifecycle

### Automation Approach Decision

| Step | Who | Activity |
|------|-----|----------|
| 1 | APO | Propose approach based on scenario characteristics |
| 2 | Process Architect | Validate feasibility of proposed approach |
| 3 | APO + PA | Decide: Conventional or Agentic |

**Decision Criteria:**

| Criterion | → Conventional | → Agentic |
|-----------|---------------|-----------|
| Input variability | Low, structured | High, unstructured |
| Decision logic | Rules sufficient | Judgment required |
| Exception handling | Few, predictable | Many, contextual |
| Risk profile | Low tolerance for error | Acceptable with controls |
| Process nature | Scripted workflow | Expert reasoning |

> **Fork Point:** If the decision is "Agentic" or "Hybrid", the scenario transitions to the Seer [Agentic Automation Lifecycle](../../../olympus-seer-docs/seer-design/personas-and-needs/journeys/agentic-automation-lifecycle.md). The remainder of this document covers the conventional path.

### Output: Scenario Definition

```yaml
scenario_definition:
  id: "routine-dispute-triage"
  name: "Routine Dispute Triage"
  
  # From Process Architect
  signals:
    - description: "Dispute event from card network"
    - description: "Customer-initiated dispute"
  
  sop:
    id: "sop-routine-dispute-triage"
  
  goals:
    - id: "triage-dispute"
      sla: "PT30M"
  
  # Automation Approach
  automation_approach:
    type: "conventional"
    rationale: "Structured inputs, rule-based decision logic"
```

### Gate: Design Approved

| Criterion | Approver |
|-----------|----------|
| Scenario definition complete | Process Architect |
| APO confirms alignment | APO |

---

## Stage 3: Build (Developer)

The Developer implements the Hub Application based on the approved design.

### Activities

1. **Implementation**
   - Build Hub Application
   - Implement triggers and signal handling
   - Integrate with knowledge services and tools
   - See: [Scenario Development Journey](./scenario-development.md) Phases 2-4

2. **Testing**
   - Functional testing
   - Integration testing
   - UAT with stakeholders

3. **Deployment**
   - Staged rollout
   - Production activation
   - Handoff to operations

### Implementation Details

| Aspect | Conventional Automation |
|--------|------------------------|
| **Implementation** | Hub Application (workflow, rules) |
| **Runtime** | Rhea, Atlantis, or other Hub runtimes |
| **Testing** | Workflow testing, integration testing |
| **Production Gate** | Supervisor approval |

### Gate: Deployment Complete

| Criterion | Approver |
|-----------|----------|
| Testing passed | Developer |
| Production ready | Supervisor |
| APO accepts | APO |

---

## Stage 4: Run (Supervisor + Agent)

The automation executes in production, processing real requests.

### Activities

1. **Operational Execution**
   - Requests flow through the automation
   - Agents (human) complete assigned tasks
   - Escalations handled per SOP

2. **Monitoring**
   - Supervisor monitors queues and SLAs
   - APO tracks business outcomes
   - Issues detected and routed

3. **Incident Response**
   - Problems detected and contained
   - Root cause analysis
   - Fixes deployed

### Signals Produced

| Signal | Consumer | Purpose |
|--------|----------|---------|
| Operational metrics | Supervisor | Queue health, SLA tracking |
| Business outcomes | APO | Value realization tracking |
| System health | Administrator | Platform monitoring |
| Compliance events | Auditor | Audit trail verification |

### Feedback Loop

```
┌─────────────────────────────────────────────────────────────┐
│                       RUN STAGE                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Requests ──▶ Automation ──▶ Outcomes                      │
│                    │                                         │
│                    ▼                                         │
│   ┌─────────────────────────────────────────┐               │
│   │           SIGNALS PRODUCED               │               │
│   │                                          │               │
│   │  • Operational metrics (→ Supervisor)   │               │
│   │  • Business outcomes (→ APO)            │               │
│   │  • System health (→ Administrator)      │               │
│   │  • Compliance events (→ Auditor)        │               │
│   │                                          │               │
│   └─────────────────────────────────────────┘               │
│                    │                                         │
│                    ▼                                         │
│              EVOLVE STAGE                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Stage 5: Evolve (APO + Process Architect)

Based on operational learnings, the automation is improved.

### Activities

1. **Outcome Review**
   - APO assesses value delivery
   - Compare actuals to charter targets
   - Identify gaps and opportunities

2. **Feedback Triage**
   - Review issues from operations
   - Prioritize improvements
   - Balance new work vs. fixes

3. **Learning Integration**
   - SOP refinements by Process Architect
   - Rule updates by Developer
   - Process optimization by Supervisor

4. **Iteration**
   - Return to Design or Build stage
   - Incremental improvements
   - Major redesign if needed

### Evolution Triggers

| Trigger | Source | Response |
|---------|--------|----------|
| Success criteria not met | APO | Investigate root cause |
| Operational issues | Supervisor | Bug fix or redesign |
| SLA breaches | Supervisor | Process optimization |
| New requirements | Business | Charter update |
| Compliance findings | Auditor | Process review |

### Feedback Routing

| Issue Type | Route To |
|------------|----------|
| Business intent mismatch | APO |
| Process design issue | Process Architect |
| Implementation bug | Developer |
| Operational constraint | Supervisor |
| Compliance concern | Auditor |

---

## Persona Involvement by Stage

| Persona | Ideate | Design | Build | Run | Evolve |
|---------|:------:|:------:|:-----:|:---:|:------:|
| **APO** | ●● | ● | — | ● | ●● |
| **Process Architect** | ● | ●● | ● | — | ● |
| **Developer** | — | ● | ●● | — | ● |
| **Supervisor** | — | — | ● | ●● | ● |
| **Agent (Human)** | — | — | — | ●● | — |
| **Administrator** | ● | — | ● | ● | — |
| **Auditor** | — | — | — | ● | ● |

Legend: ●● Primary, ● Supporting, — Not involved

> **Note:** For agentic automation, additional Seer personas (CSA, AE, KMO, ARE, COS, ARAO) are involved. See the [Agentic Automation Lifecycle](../../../olympus-seer-docs/seer-design/personas-and-needs/journeys/agentic-automation-lifecycle.md).

---

## Stage Transitions

| Transition | Gate | Key Approvals |
|------------|------|---------------|
| Ideate → Design | Charter Approved | Sponsor, Administrator |
| Design → Build | Design Approved | Process Architect, APO |
| Build → Run | Deployment Complete | Developer, Supervisor |
| Run → Evolve | Continuous | APO triggers review |
| Evolve → Design | Redesign Needed | APO decision |

---

## Workbench Stage Mapping

The Automation Lifecycle maps to Workbench stages:

| Lifecycle Stage | Workbench Stage |
|-----------------|-----------------|
| Ideate | design |
| Design | design |
| Build | build |
| Run | run |
| Evolve | evolve |

A Workbench's stage determines which capabilities are enabled. See [Workbench Configuration](./workbench-configuration.md) for details.

---

## Agentic Path

When the automation approach decision in Stage 2 selects "Agentic" or "Hybrid", the scenario transitions to the Seer lifecycle. The key differences:

| Aspect | Conventional (Hub) | Agentic (Seer) |
|--------|-------------------|----------------|
| **Implementation** | Hub Application | AI Agent |
| **Runtime** | Rhea, Atlantis | Seer Runtime |
| **Additional Personas** | — | CSA, AE, KMO, ARE, COS, ARAO |
| **Production Gate** | Supervisor | ARE + ARAO |
| **Monitoring** | Supervisor | ARE + COS |

For the complete agentic journey, see: [Agentic Automation Lifecycle](../../../olympus-seer-docs/seer-design/personas-and-needs/journeys/agentic-automation-lifecycle.md)

---

## Related Journeys

- [Scenario Development](./scenario-development.md) — Detailed scenario creation (Design + Build)
- [Workbench Configuration](./workbench-configuration.md) — Workbench setup
- [Request Lifecycle](./request-lifecycle.md) — Request processing (Run)

---

## Related Documentation

- [Automation Product Owner](../personas/automation-product-owner.md) — APO role definition
- [Process Architect](../personas/process-architect.md) — PA role definition
- [Developer](../personas/developer.md) — Developer role definition
- [Supervisor](../personas/supervisor.md) — Supervisor role definition

---

*Status: 🟡 Draft — Journey defined, pending detailed walkthrough*

