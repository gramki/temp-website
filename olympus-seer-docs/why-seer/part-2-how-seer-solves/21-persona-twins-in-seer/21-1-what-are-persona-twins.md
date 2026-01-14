# 21.1 What Are Persona Twins?

Persona Twins are AI agents that collaborators create to handle tasks, notifications, and scheduled activities on their behalf. Unlike Business Scenarios that handle organizational workflows, Persona Twin Scenarios are personal productivity agents that respond to personal triggers and operate within the delegator's authority boundaries.

Persona Twins enable any collaborator (not just developers) to create personal AI assistants for delegation, extending Seer's agent capabilities to personal productivity. Twins follow the standard three-layer agent lifecycle (Raw → Trained → Employed) with special recognition, isolation, and trigger mechanisms that distinguish them from business agents.

## Purpose of this Subsection

This subsection defines Persona Twins and explains their characteristics. It describes authority inheritance, personal triggers, privacy options, and workbench scope. It also distinguishes Persona Twins from business agents and explains how they enable personal productivity while maintaining governance and audit requirements.

## Core Concepts & Definitions

### Persona Twin Definition

**Persona Twin** is an AI agent that a collaborator creates to handle tasks, notifications, and scheduled activities on their behalf, operating within the same authority boundaries as the delegator. Persona Twins are:
*   **Personal productivity agents**: Handle personal tasks and notifications, not organizational workflows
*   **Delegator-owned**: Created and managed by the collaborator (delegator) who uses them
*   **Workbench-scoped**: Operate within a single workbench, one twin per scenario
*   **Authority-inheriting**: Inherit authority from their delegator (same as delegator)

Persona Twins enable collaborators to delegate routine work to AI assistants while maintaining full accountability and governance.

### Authority Inheritance

**Authority inheritance** means that Persona Twins inherit authority from their delegator. The delegator is both the delegator and the accountable human:
*   **Same authority**: Twins have the same authority as their delegator (roles, groups, scopes)
*   **Authority narrowing**: Twins cannot exceed delegator authority; if delegator loses a role, twin loses it too
*   **Accountable human**: Delegator is the accountable human for twin actions
*   **OPA policy enforcement**: OPA policies can further restrict twin actions beyond delegator authority

Authority inheritance ensures that twins operate within the delegator's authority boundaries, maintaining governance and accountability.

### Personal Triggers

**Personal triggers** are triggers that respond to events specific to the delegator:
*   **Task assignment**: Tasks assigned to the delegator create Requests in the twin's scenario
*   **Platform notifications**: Platform notifications for the delegator create Requests in the twin's scenario
*   **Scheduled activities**: Personally configured schedules (via Kale scheduler) create Requests in the twin's scenario

Personal triggers enable twins to respond to delegator-specific events, distinguishing them from business scenarios that respond to organizational events.

### Privacy

**Privacy** is the capability for Persona Twin Scenarios to have private visibility, keeping personal workflows confidential. Private visibility:
*   **Delegator-only access**: Private twins visible only to delegator and admins
*   **Scenario-level control**: Privacy controlled at scenario level, not agent level
*   **Audit still maintained**: Private scenarios still auditable for compliance

Privacy enables collaborators to create personal workflows without exposing them to other workbench members.

### Workbench Scope

**Workbench scope** means that Persona Twins operate within a single workbench, one twin per scenario. This ensures:
*   **Isolation**: Personal workflows isolated from business scenarios
*   **Clear boundaries**: Clear separation between personal and business agents
*   **Workbench governance**: Twins subject to workbench-level governance

Workbench scope enables personal productivity while maintaining organizational boundaries.

## Conceptual Models / Frameworks

### The Persona Twin Model

Persona Twins operate within delegator authority:

```
Delegator (Collaborator)
    ├── Authority (Roles, Groups, Scopes)
    │
    └── Persona Twin
        ├── Inherits Authority (same as delegator)
        ├── Personal Triggers (tasks, notifications, schedules)
        ├── Private Visibility (optional)
        └── Workbench Scope (one twin per scenario)
```

Twins inherit authority and respond to personal triggers while maintaining governance and audit requirements.

### The Authority Inheritance Model

Authority inheritance ensures twins operate within delegator boundaries:

*   **Delegator authority**: Roles, groups, scopes
*   **Twin authority**: Same as delegator (cannot exceed)
*   **OPA restrictions**: OPA policies can further restrict twin actions
*   **Dynamic updates**: If delegator loses authority, twin loses it too

This model ensures that twins cannot exceed delegator authority, maintaining governance and accountability.

## Systemic and Enterprise Considerations

### Governance Requirements

Persona Twins must maintain governance:
*   **Authority enforcement**: Twins must respect authority constraints and guardrails
*   **Audit trail**: All twin actions must be auditable
*   **Policy compliance**: Twins must comply with workbench and subscription policies
*   **Lifecycle management**: Twins follow standard agent lifecycle with special recognition

Governance ensures that Persona Twins maintain enterprise standards while enabling personal productivity.

### Isolation Requirements

Persona Twins must be isolated from business scenarios:
*   **Metadata labels**: `persona-twin: "true"` label for recognition
*   **Category isolation**: `category: "persona-twin"` for filtering
*   **Visibility control**: Private visibility option for personal workflows
*   **Directory filtering**: Directory queries support `personaTwin` filter

Isolation ensures that personal workflows don't interfere with business scenarios and vice versa.

### Trigger Requirements

Persona Twins require personal trigger mechanisms:
*   **Task assignment signals**: Signal Exchange must support task assignment signals
*   **Platform notification signals**: Notification Services must support platform notification signals
*   **Schedule support**: Kale scheduler must support personal schedules
*   **OPA filter support**: Triggers must support OPA filters for personalization

Trigger requirements ensure that twins can respond to delegator-specific events.

## Common Misconceptions & Failure Modes

### Misconception: Persona Twins Are Business Agents

Some organizations assume that Persona Twins are business agents. However, Persona Twins are personal productivity agents that handle personal tasks and notifications, not organizational workflows.

**Failure mode**: Organizations try to use Persona Twins for business scenarios, resulting in inappropriate use and governance confusion.

### Misconception: Persona Twins Exceed Delegator Authority

Some organizations assume that Persona Twins can have authority beyond their delegator. However, twins inherit authority from their delegator and cannot exceed it.

**Failure mode**: Organizations expect twins to have additional authority, leading to confusion when twins cannot perform actions that require authority the delegator doesn't have.

### Misconception: Persona Twins Don't Need Governance

Some organizations assume that Persona Twins, being personal, don't need governance. However, twins must maintain the same governance, audit, and policy compliance as business agents.

**Failure mode**: Organizations skip governance for Persona Twins, resulting in compliance violations and audit gaps.

### Misconception: Persona Twins Replace Business Agents

Some organizations assume that Persona Twins can replace business agents. However, Persona Twins are for personal productivity, while business agents are for organizational workflows.

**Failure mode**: Organizations try to use Persona Twins for business scenarios, resulting in inappropriate use and governance confusion.

## Practical Implications

### Persona Twin Strategy

Organizations should develop a Persona Twin strategy that:
*   **Defines use cases**: Identify which personal productivity use cases benefit from twins
*   **Establishes policies**: Define policies for twin creation, usage, and governance
*   **Provides blueprints**: Provide Persona Twin Blueprints for common use cases
*   **Monitors proliferation**: Monitor twin proliferation to manage resource consumption

Persona Twin strategy directly impacts personal productivity and resource utilization.

### Blueprint Selection

Organizations should provide Persona Twin Blueprints that:
*   **Serve common use cases**: Provide blueprints for common personal productivity use cases
*   **Enable customization**: Enable collaborators to customize blueprints for their needs
*   **Maintain best practices**: Encode best practices in blueprint configurations
*   **Support evolution**: Support blueprint evolution as needs change

Blueprint selection directly impacts twin creation efficiency and effectiveness.

### Governance Integration

Organizations should integrate Persona Twins into governance:
*   **Authority management**: Manage twin authority through delegator authority management
*   **Audit requirements**: Ensure twin actions are auditable
*   **Policy compliance**: Ensure twins comply with workbench and subscription policies
*   **Lifecycle management**: Manage twin lifecycle through standard agent lifecycle processes

Governance integration ensures that Persona Twins maintain enterprise standards.

## Cross-References

*   **Section 6.8 (Designed for Enterprise Personas)**: Establishes persona-specific design that Persona Twins extend
*   **Section 6.10 (Persona Twins: Personal AI Assistants)**: Introduces Persona Twins as a design philosophy element
*   **Section 7 (Agent Lifecycle)**: Describes the standard agent lifecycle that Persona Twins follow
*   **Section 8 (Identity & Authority)**: Describes authority delegation that Persona Twins use

---

**References:**

*   `seer-design/implementation-concepts/persona-twins.md` — Persona Twins concept
*   `seer-design/implementation-concepts/persona-twin-blueprint.md` — Persona Twin Blueprint concept
