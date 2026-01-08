# Scenario Specification Types

> **Category:** Configuration Model

---

## Overview

Hub separates Scenario definitions into **three specification types** that align with the ontology layers and persona responsibilities: **Normative** (what ought to be done), **Automation** (how it's automated), and **Deployment** (how it's deployed). This separation enables independent evolution, clear ownership, and a structured development journey.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Scenario** as a recognizable operational situation requiring response. However, it doesn't specify how Scenarios are configured in practice. The three specification types map directly to ontology layers:

| Ontology Layer | Specification Type | Focus |
|----------------|-------------------|-------|
| **Normative** | Scenario Normative Spec | What ought to be done |
| **Automation** | Scenario Automation Spec | How it's codified |
| **Execution** | Scenario Deployment Spec | How it's deployed |

### Gap This Fills

The ontology describes Scenarios conceptually. Specification Types address:
1. **Separation of concerns**: Different aspects, different owners
2. **Evolution path**: Change what without changing how
3. **Development journey**: Architect → Developer → Supervisor

---

## Definition

**Scenario Specification Types** are three complementary CRD types that together define a complete Scenario:

1. **Normative Specification**: Business requirements, roles, goals, SOPs
2. **Automation Specification**: Technical implementation, triggers, applications
3. **Deployment Specification**: Runtime settings, queues, SLAs, activation

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-scoped; part of a single Workbench |
| **Lifecycle** | Created sequentially: Normative → Automation → Deployment |
| **Ownership** | Process Architect → Developer → Supervisor |
| **Multiplicity** | Each Scenario has exactly one of each type |

---

## Rationale

### Why This Design?

**Separation of concerns:**
- Business analysts focus on requirements (Normative)
- Developers focus on implementation (Automation)
- Operations focus on deployment (Deployment)

**Change independence:**
- Change SOP without touching code
- Change implementation without affecting requirements
- Change deployment without code changes

**Compliance:**
- Clear audit of who changed what
- Requirements traceable to implementation

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Single specification** | Mixed concerns; unclear ownership |
| **Two specifications** | Insufficient separation for regulated environments |
| **More than three** | Over-engineering; diminishing returns |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0002](../../decision-logs/0002-scenario-specification-types.md) | Three specification types for Scenarios |

---

## Structure

### Normative Specification (Process Architect)

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioNormativeSpec
metadata:
  name: standard-dispute
  namespace: acme-bank
spec:
  display_name: "Standard Dispute Resolution"
  version: "2.0.0"
  
  # Business description
  description: |
    Handles standard customer disputes for unauthorized
    charges, billing errors, and service issues.
  
  # Roles involved
  roles:
    - name: dispute-analyst
      type: agent
      goals:
        - "Investigate dispute within 24 hours"
        - "Document findings completely"
      responsibilities:
        - "Review transaction history"
        - "Contact customer for clarification"
        - "Make fair determination"
        
    - name: supervisor
      type: supervisor
      goals:
        - "Ensure SLA compliance"
        - "Handle escalations"
  
  # Standard Operating Procedures
  sops:
    - ref: sop-dispute-investigation
    - ref: sop-customer-communication
  
  # Decision criteria
  decision_criteria:
    - name: liability-determination
      description: "Criteria for determining transaction liability"
      document_ref: dispute-liability-matrix
  
  # Evidence requirements
  evidence_requirements:
    - type: transaction-history
      mandatory: true
    - type: customer-statement
      mandatory: true
    - type: merchant-response
      mandatory: false
  
  # Escalation rules
  escalation_rules:
    - condition: "high_value"
      threshold: 5000
      escalate_to: supervisor
  
  # Compliance requirements
  compliance:
    - regulation: "Reg E"
      requirements:
        - "10-day provisional credit for $500+"
```

### Automation Specification (Developer)

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioAutomationSpec
metadata:
  name: standard-dispute
  namespace: acme-bank
spec:
  # Reference to normative spec
  normative_ref: standard-dispute
  version: "2.0.0"
  
  # Hub Application
  application:
    ref: dispute-handler
    version: "1.5.0"
    
  # Triggers that activate this scenario
  triggers:
    - ref: dispute-filed-trigger
    - ref: dispute-document-uploaded-trigger
    
  # Tool bindings
  tools:
    - name: transaction-lookup
      ref: core-banking-transactions
    - name: customer-notification
      ref: email-sender
      
  # Notification templates
  notifications:
    - event: task_assigned
      template_ref: analyst-task-notification
    - event: request_completed
      template_ref: customer-resolution-notification
```

### Deployment Specification (Supervisor)

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioDeploymentSpec
metadata:
  name: standard-dispute
  namespace: acme-bank
spec:
  # Reference to automation spec
  automation_ref: standard-dispute
  version: "2.0.0"
  
  # Task queue mappings
  task_queues:
    - task_type: investigate
      queue_ref: tier-1-disputes
    - task_type: review
      queue_ref: supervisor-review
      
  # Agent enrollment
  agents:
    default_pool: dispute-analysts
    
  # SLA parameters
  sla:
    target_completion_hours: 72
    warning_threshold_hours: 48
  
  # Scenario Escalation Matrix (for application-level exceptions)
  # Handles rejections from guardrails, policies, and applications
  scenario_escalation:
    # Accountable human for this scenario
    accountable_human:
      type: workbench_role
      value: supervisor
    
    # Escalation levels for application exceptions
    levels:
      - level: 0
        name: "Senior Analyst Review"
        candidates:
          type: iam_role
          value: senior-dispute-analyst
        threshold_minutes: null  # Immediate on rejection
        notification:
          recipients:
            - role: accountable_human
          template: rejection_escalation_l0
          
      - level: 1
        name: "Supervisor Intervention"
        candidates:
          type: workbench_role
          value: supervisor
        threshold_minutes: 60  # If not resolved in 60 min
        notification:
          recipients:
            - role: supervisor
            - role: process_architect
          template: rejection_escalation_l1
          urgency: high
    
    # Resolution options enabled
    resolution_options:
      allow_context_change: true
      allow_decision_override: true
      allow_scenario_fail: true
      allow_corrective_action: true
    
  # Activation settings
  activation:
    enabled: true
    start_date: "2026-01-01"
    end_date: null  # No end date
    
  # Environment overrides
  environment:
    variables:
      MAX_RETRIES: "3"
```

#### Scenario Escalation vs Task Queue Escalation

| Aspect | Task Queue Escalation Matrix | Scenario Escalation Matrix |
|--------|------------------------------|----------------------------|
| **Trigger** | Time-based (task age) | Rejection-based (guardrail, policy, application) |
| **Purpose** | Bring in help for stalled tasks | Handle application-level exceptions |
| **Scope** | Task-level | Request/Scenario-level |
| **Configured By** | Supervisor (in Task Queue config) | Supervisor (in Scenario Deployment) |
| **Resolution** | Any assignee can complete task | Override, context change, fail, or corrective action |

See [Agent Directability](./agent-directability.md) for the full directability model.

---

## Behavior

### Development Journey

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SCENARIO DEVELOPMENT JOURNEY                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PHASE 1: DESIGN                 PHASE 2: BUILD                            │
│   (Process Architect)             (Developer)                                │
│                                                                              │
│   ┌─────────────────────┐        ┌─────────────────────┐                    │
│   │  Scenario           │        │  Scenario           │                    │
│   │  Normative Spec     │───────▶│  Automation Spec    │                    │
│   │                     │        │                     │                    │
│   │  • Roles & Goals    │        │  • Hub Application  │                    │
│   │  • SOPs             │        │  • Triggers         │                    │
│   │  • Decision Criteria│        │  • Tool Bindings    │                    │
│   │  • Compliance       │        │  • Notifications    │                    │
│   └─────────────────────┘        └──────────┬──────────┘                    │
│                                             │                                │
│                                             ▼                                │
│                                  PHASE 3: DEPLOY                             │
│                                  (Supervisor)                                │
│                                                                              │
│                                  ┌─────────────────────┐                    │
│                                  │  Scenario           │                    │
│                                  │  Deployment Spec    │                    │
│                                  │                     │                    │
│                                  │  • Task Queues      │                    │
│                                  │  • Agent Enrollment │                    │
│                                  │  • SLA Parameters   │                    │
│                                  │  • Activation       │                    │
│                                  └─────────────────────┘                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Specification Dependencies

```
ScenarioNormativeSpec
        │
        │ referenced by
        ▼
ScenarioAutomationSpec
        │
        │ referenced by
        ▼
ScenarioDeploymentSpec
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Workbench | ↑ contained by | All specs belong to a Workbench |
| Hub Application | ← referenced by | Automation spec binds Application |
| TriggerSpec | ← referenced by | Automation spec lists triggers |
| TaskQueue | ← referenced by | Deployment spec maps queues |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Sequential creation** | Normative must exist before Automation; Automation before Deployment |
| **Version alignment** | All three specs should have compatible versions |
| **Reference validity** | Referenced resources must exist |
| **Single per Scenario** | Exactly one of each spec type per Scenario |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Clear ownership** | Each persona owns their specification |
| ✅ **Independent evolution** | Change one without touching others |
| ✅ **Audit clarity** | Who changed what is clear |
| ✅ **Gradual rollout** | Enable/disable via Deployment spec |
| ✅ **Reuse** | Same Normative spec, different Automation |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Three files to manage** | Workbench Studio provides unified view |
| ⚠️ **Version coordination** | Promotion promotes all three together |
| ⚠️ **Learning curve** | Clear documentation; examples |

---

## Examples

### Example: Complete Scenario Definition

```
dispute-ops-dev/
├── scenarios/
│   └── standard-dispute/
│       ├── normative.yaml      # ScenarioNormativeSpec
│       ├── automation.yaml     # ScenarioAutomationSpec
│       └── deployment.yaml     # ScenarioDeploymentSpec
```

---

## Implementation Notes

### For Process Architects

- Focus on business requirements, not implementation
- Define clear roles, goals, and SOPs
- Document decision criteria thoroughly
- Specify compliance requirements explicitly

### For Developers

- Reference the Normative spec, don't duplicate
- Ensure Hub Application implements all required behaviors
- Configure appropriate triggers and tools
- Set up notification templates

### For Supervisors

- Configure queues with appropriate escalation
- Set realistic SLA parameters
- Control activation timing
- Review before enabling in production

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [CRD](./crd.md) | Specifications are CRD types |
| [Hub Application](./hub-application.md) | Referenced in Automation spec |
| [Promotion](./promotion.md) | All three specs promoted together |

---

## References

- [Scenario Definitions](../../04-subsystems/workbench-management/scenario-definitions.md)
- [Process Architect Operator](../../04-subsystems/operators/process-architect-operator.md)
- [Developer Operators](../../04-subsystems/operators/developer-operators.md)
- [ADR-0002: Scenario Specification Types](../../decision-logs/0002-scenario-specification-types.md)

