# Persona: Supervisor

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-08

---

## Overview

The **Supervisor** deploys Scenarios into production, manages Task Queues, and oversees agent operations within a Workbench.

The Supervisor is the **primary owner of Agent Directability** in Hub—they define all escalation matrices and are responsible for handling interventions when AI agent outputs are rejected. See [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md) for the full directability model.

| Attribute | Value |
|-----------|-------|
| **Category** | Hub Persona — Workbench Operations |
| **Scope** | Workbench |
| **Domain** | Tenant Identity Domain |
| **Primary Console** | Ops Center |

---

## Objectives

| Objective | Description |
|-----------|-------------|
| **Deploy Scenarios** | Map tasks to queues and activate scenarios |
| **Manage Queues** | Configure escalation, eligibility, and capacity |
| **Define Directability** | Configure all escalation matrices for agent intervention |
| **Oversee Operations** | Monitor SLAs, agent efficiency, queue health |
| **Handle Escalations** | Address escalated tasks and agent issues |
| **Resolve Interventions** | Override decisions, modify context when agent outputs are rejected |

---

## Key Activities

### Deployment Phase

1. **Scenario Review**
   - Review Scenario Manifest from Development
   - Verify workforce capabilities match task requirements

2. **Queue Configuration**
   - Create or assign Task Queues
   - Configure escalation policies
   - Set SLA enforcement rules

3. **Scenario Activation**
   - Map tasks to queues
   - Enable triggers
   - Begin production operations

### Operations Phase

1. **Queue Monitoring**
   - Track queue depths and wait times
   - Identify bottlenecks
   - Adjust capacity as needed

2. **Agent Management**
   - Enroll/remove agents from queues
   - Review agent performance
   - Handle reassignments

3. **Escalation Handling**
   - Address escalated tasks
   - Override decisions when authorized
   - Coordinate with Process Architects on SOP issues

### Directability Phase

1. **Escalation Matrix Configuration**
   - Define Task Queue escalation matrices
   - Define Scenario escalation matrices
   - Set escalation thresholds and candidate levels
   - Configure accountable human notifications

2. **Intervention Resolution**
   - Receive rejection notifications from agents/guardrails
   - Review rejected decisions or actions
   - Choose resolution: override, context change, reassign, fail
   - Record resolution in CAF (Override/ContextIntervention/DirectiveResolution)

3. **Pattern Analysis**
   - Monitor intervention frequency by scenario/queue
   - Identify systematic issues requiring process changes
   - Feed observations to Enterprise Learning workflows

---

## Hub Capabilities Consumed

### Ops Center (Primary Interface)

| Capability | What It Provides |
|------------|------------------|
| **Queue Dashboard** | View queue depths, wait times, agent availability |
| **Scenario Deployment** | Map tasks to queues, activate scenarios |
| **Agent Management** | Enroll/remove agents, view performance |
| **Escalation Handling** | View escalated tasks, reassign, override |
| **SLA Monitoring** | Track SLA compliance, identify at-risk requests |
| **Operational Analytics** | Efficiency metrics, throughput analysis |

### Hub Services Accessed

| Service | Usage |
|---------|-------|
| **Task Management** | Create queues, configure escalation policies |
| **Workbench Management** | Deploy scenarios, map task types to queues |
| **Checklist Service** | Define and monitor operational checklists |
| **Routine Service** | Assign routines to agents |
| **Request Management** | View request status, handle escalations |
| **Memory Services** | Access Enterprise Memory for context |

### What They Manage

| Entity | Actions |
|--------|---------|
| **Task Queues** | Create, configure policies, set SLAs |
| **Agent Enrollment** | Add/remove agents, set capabilities |
| **Escalation Matrix** | Define escalation rules, timeout policies |
| **Checklists** | Deploy, monitor, analyze |
| **Routines** | Assign to agents, track completion |

---

## Key Journeys

- [Scenario Development](../journeys/scenario-development.md) — Deploy phase
- [Workbench Configuration](../journeys/workbench-configuration.md) — Supporting role

---

## Collaboration

| With | Activity |
|------|----------|
| **Process Architect** | Provide operational feedback, queue design input |
| **Developer** | Review Scenario Manifest, request clarifications |
| **Agent** | Assignment, coaching, escalation resolution |
| **Administrator** | Request queue capacity, user enrollment |

---

## Related Documentation

- [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md) — How Supervisors enable human intervention
- [Escalation Matrix](../../02-system-design/implementation-concepts/escalation-matrix.md) — Escalation configuration
- [Task Management](../../04-subsystems/task-management/README.md)
- [Cognitive Audit Fabric](../../04-subsystems/cognitive-audit-fabric/README.md) — Intervention records
- [Checklist Service](../../04-subsystems/hub-native-utilities/checklist-service.md)
- [Routine Service](../../04-subsystems/hub-native-utilities/routine-service.md)

---

