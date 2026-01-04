# Journey: Scenario Development

> **Status:** 🔴 Stub — Placeholder for expansion

This journey describes how a **Scenario** is designed, built, and deployed — from initial identification through production activation. It involves collaboration between **Process Architect**, **Developer**, and **Supervisor**.

---

## Overview

A **Scenario** is a Perception Layer concept representing a situational context that the organization must respond to. The development of a Scenario spans four phases:

| Phase | Primary Persona | Output |
|-------|-----------------|--------|
| **1. Design** | Process Architect | Scenario Definition, SOP |
| **2. Build** | Developer | Hub Application, Triggers |
| **3. Task Delegation** | Process Architect + Developer | Scenario Manifest |
| **4. Deploy** | Supervisor | Task Queue Mappings, Activation |

---

## Phase 1: Design (Process Architect)

The Process Architect identifies operational scenarios and defines how they should be handled.

### Activities

1. **Identify the Scenario**
   - What situational context requires a response?
   - Example: "Payment Dispute Filed", "Suspicious Login Detected", "Daily Settlement Required"

2. **Specify Signals (Notionally)**
   - What signals activate this scenario?
   - Not technical definitions — conceptual descriptions
   - Example: "A dispute event from the card network", "An alert from the fraud detection system"

3. **Define the SOP**
   - How should agents handle this scenario?
   - What decisions are required?
   - What actions must be taken?
   - What evidence must be captured?

4. **Define Goals and SLAs**
   - What must be achieved?
   - What are the time constraints?
   - Example: "Resolve dispute within 10 business days"

### Output: Scenario Definition

```yaml
scenario_definition:
  id: "payment-dispute-filed"
  name: "Payment Dispute Filed"
  domain: "dispute-resolution"
  
  # Notional signal description (not technical)
  signals:
    - description: "Dispute event received from card network"
      source: "Card Network Gateway"
    - description: "Customer-initiated dispute via portal"
      source: "Customer Portal"
  
  # SOP reference
  sop:
    id: "sop-dispute-resolution"
    knowledge_base: "dispute-kb"
  
  # Goals
  goals:
    - id: "resolve-dispute"
      description: "Resolve dispute fairly and within SLA"
      sla: "P10D"  # 10 days
  
  # Roles involved
  roles:
    - role: "dispute-analyst"
      responsibilities: ["investigate", "decide", "document"]
    - role: "dispute-supervisor"
      responsibilities: ["escalation", "review", "override"]
```

---

## Phase 2: Build (Developer)

The Developer takes the Scenario Definition and builds the automation to handle it.

### Activities

1. **Choose Automation Runtime**
   - Based on the nature of the Operation:
     - Structured workflow? → **Rhea**
     - Long-running case? → **Seer Case Automation** or **ChronoShift**
     - Simple procedure? → **Atlantis**
     - Batch processing? → **Perseus**

2. **Build Hub Application**
   - Implement the automation logic
   - Must honor Hub Request contracts:
     - Request initiation acknowledgment
     - Intermediate updates (status, decisions, thoughts, memos)
     - Request completion

3. **Define Triggers**
   - Connect Signals to the Application
   - Specify matching conditions
   - Define signal-to-request transformation
   - Configure response transformation (for I/O Gateways)

4. **Integrate with Hub Services**
   - Memory Services (read/write)
   - Knowledge Services (retrieval)
   - Tool invocations
   - Task creation

### Output: Hub Application + Triggers

```yaml
# Trigger Definition
trigger:
  id: "card-network-dispute-trigger"
  signal_source:
    provider: atropos
    topic: "card-network.disputes"
  
  conditions:
    - field: "$.event_type"
      operator: eq
      value: "DISPUTE_FILED"
  
  transformation:
    request_type: ServiceRequest  # Customer is always the subject in disputes
    mappings:
      - source: "$.dispute_id"
        target: "entity_id"
      - source: "$.cardholder_id"
        target: "subject_id"
  
  scenario_id: "payment-dispute-filed"
  application_id: "dispute-resolution-app"

# Application Configuration
application:
  id: "dispute-resolution-app"
  runtime: seer
  type: "Seer Case Orchestration Agent"
  
  # Application-specific configuration
  config:
    agent_definition: "dispute-resolution-agent"
    # ... runtime-specific config
```

---

## Phase 3: Task Delegation (Process Architect + Developer)

Automation rarely handles everything. Process Architect and Developer collaborate to identify what must be delegated to human agents.

### Why Task Delegation is Needed

| Reason | Example |
|--------|---------|
| **SOP Requirement** | "Final decision must be made by certified analyst" |
| **Discretionary Judgment** | "Assess customer intent" — cannot be automated |
| **Technical Limitation** | Document verification requires human review |
| **Pragmatic Choice** | Edge cases deferred to humans for v1 |

### Activities

1. **Identify Tasks to Delegate**
   - Review SOP requirements
   - Identify automation gaps
   - Define task types

2. **Define Task Specifications**
   - What information does the agent need?
   - What actions can the agent take?
   - What must be captured?

3. **Create Scenario Manifest**
   - Enumerate all delegated tasks
   - Specify task types and requirements
   - This becomes the contract for deployment

### Output: Scenario Manifest

```yaml
scenario_manifest:
  scenario_id: "payment-dispute-filed"
  application_id: "dispute-resolution-app"
  
  # Tasks that will be delegated to agents
  delegated_tasks:
    - task_type: "document-verification"
      description: "Verify submitted dispute documents"
      required_capabilities: ["document-analysis"]
      estimated_duration: "PT15M"
      can_be_automated_later: true
    
    - task_type: "merchant-contact"
      description: "Contact merchant for transaction details"
      required_capabilities: ["communication", "dispute-knowledge"]
      estimated_duration: "PT30M"
      can_be_automated_later: false  # Requires human judgment
    
    - task_type: "final-decision"
      description: "Make final dispute resolution decision"
      required_capabilities: ["dispute-certification", "decision-authority"]
      estimated_duration: "PT20M"
      can_be_automated_later: false  # SOP requires human
      requires_evidence_bundle: true
    
    - task_type: "customer-notification"
      description: "Notify customer of resolution"
      required_capabilities: ["communication"]
      estimated_duration: "PT10M"
      can_be_automated_later: true
  
  # Special task routing
  special_routing:
    - task_type: "subject-acknowledgment"
      route_to: subject  # Route to the customer (Subject of Request)
      description: "Customer acknowledges dispute details"
```

---

## Phase 4: Deploy (Supervisor)

The Supervisor activates the Scenario in the Workbench, mapping tasks to queues and agents.

### Activities

1. **Review Scenario Manifest**
   - Understand delegated tasks
   - Verify required capabilities exist in the workforce

2. **Map Tasks to Queues**
   - For each task type in manifest, assign to a Task Queue
   - Hub provides specialized queues:
     - **Standard Queue**: Allocate tasks to agents assigned to this queue using the chosen allocation algorithm (e.g., round-robin, availability, or skill-based assignment)
     - **Subject Queue**: Route to the Subject of the Request
     - **Designated Agent Queue**: Route to a specific agent field in the task

3. **Configure Queue Properties**
   - Escalation policies
   - SLA enforcement
   - Agent eligibility rules

4. **Activate Scenario**
   - Deploy to Workbench
   - Enable triggers
   - Begin processing signals

### Output: Task Queue Mappings

```yaml
scenario_deployment:
  scenario_id: "payment-dispute-filed"
  workbench_id: "dispute-operations"
  
  # Task Queue Mappings
  task_queue_mappings:
    - task_type: "document-verification"
      queue_id: "doc-verification-queue"
      escalation_after: "PT2H"
    
    - task_type: "merchant-contact"
      queue_id: "merchant-relations-queue"
      escalation_after: "PT4H"
    
    - task_type: "final-decision"
      queue_id: "senior-analyst-queue"
      requires_certification: "dispute-certification"
      escalation_after: "PT8H"
    
    - task_type: "customer-notification"
      queue_id: "customer-comms-queue"
      escalation_after: "PT1H"
    
    - task_type: "subject-acknowledgment"
      queue_type: subject  # Special: routes to customer
      channel: "customer-portal"
  
  # Activation
  status: active
  activated_at: "2026-01-04T10:00:00Z"
  activated_by: "supervisor-jane"
```

---

## Scenario Composition Summary

A fully deployed Scenario composes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              SCENARIO                                        │
│                     "Payment Dispute Filed"                                  │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  SIGNALS                          (What activates it)               │    │
│  │  • Card network dispute events                                      │    │
│  │  • Customer portal submissions                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    ↓                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  TRIGGERS                         (How signals connect)             │    │
│  │  • card-network-dispute-trigger                                     │    │
│  │  • customer-portal-dispute-trigger                                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    ↓                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  HUB APPLICATION                  (What automates it)               │    │
│  │  • dispute-resolution-app                                           │    │
│  │  • Runtime: Seer Case Orchestration Agent                          │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    ↓                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  TASK QUEUES                      (Where humans work)               │    │
│  │  • doc-verification-queue                                           │    │
│  │  • merchant-relations-queue                                         │    │
│  │  • senior-analyst-queue                                             │    │
│  │  • customer-comms-queue                                             │    │
│  │  • [Subject Queue: customer-portal]                                 │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    ↓                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  SOP & GOALS                      (How it should be done)           │    │
│  │  • SOP: Dispute Resolution Procedure                                │    │
│  │  • Goal: Resolve within 10 days                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Lifecycle States

```
                     (revise)
              ┌─────────────────┐
              ▼                 │
          [Draft] ──→ [Validated] ──→ [Published] ──→ [Deployed] ──→ [Active]
                          │
                          ▼
                      [Rejected]
                          │
                          └──→ (back to Draft for revision)
```

| State | Owner | Description |
|-------|-------|-------------|
| **Draft** | Process Architect | Initial design, can be revised |
| **Validated** | Developer | Application built and tested |
| **Rejected** | Developer | Validation failed, needs revision |
| **Published** | Developer | Ready for deployment |
| **Deployed** | Supervisor | Task queues mapped |
| **Active** | System | Processing signals |

---

## Related Documentation

- [Process Architect Persona](../personas/process-architect.md)
- [Developer Persona](../personas/developer.md)
- [Supervisor Persona](../personas/supervisor.md)
- [Scenario Definitions](../../04-subsystems/workbench-management/scenario-definitions.md)
- [Trigger Definitions](../../04-subsystems/workbench-management/trigger-definitions.md)
- [Task Management](../../04-subsystems/task-management/README.md)

---

*TODO: Detailed design — manifest schema, validation rules, deployment workflow*

