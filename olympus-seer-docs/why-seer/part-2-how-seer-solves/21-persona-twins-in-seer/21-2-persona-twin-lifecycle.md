# 21.2 Persona Twin Lifecycle

Persona Twins follow the standard three-layer agent lifecycle (Raw → Trained → Employed) established in Section 7, with special recognition, isolation, and trigger mechanisms that distinguish them from business agents. Twins are created from Persona Twin Blueprints that provide signal suggestions and OPA filter templates, enabling non-developers to create personal AI assistants.

This subsection describes how Persona Twins are created, trained, and employed using blueprints, how they are recognized and isolated from business agents, and how delegators own and manage their twins throughout the lifecycle.

## Purpose of this Subsection

This subsection describes the Persona Twin lifecycle, from blueprint-based creation through training and employment. It explains how Persona Twin Blueprints enable non-developer creation, how twins follow the standard agent lifecycle with special recognition, and how delegators own and manage their twins.

## Core Concepts & Definitions

### Blueprint-Based Creation

**Blueprint-based creation** enables collaborators to create Persona Twins by selecting from Persona Twin Blueprints that provide signal suggestions and OPA filter templates. Blueprints:
*   **Extend Trained Agent Blueprints**: Persona Twin Blueprints extend standard Trained Agent Blueprints with persona-specific metadata
*   **Provide signal suggestions**: Blueprints suggest common signals (task assignment, platform notifications, schedules)
*   **Provide filter templates**: Blueprints provide OPA filter templates for signal filtering
*   **Provide schedule suggestions**: Blueprints suggest common schedules (daily summaries, weekly reviews)
*   **Enable customization**: Collaborators can customize blueprints for their needs

Blueprint-based creation enables non-developers to create Persona Twins without writing specifications from scratch.

### Persona Twin Blueprint Structure

Persona Twin Blueprints extend Trained Agent Blueprints (not a separate CRD) with persona-specific metadata:

**Blueprint Structure**:
```yaml
apiVersion: seer.olympus.io/v1
kind: TrainedAgentBlueprint  # Extends standard blueprint
metadata:
  name: personal-assistant-blueprint
  labels:
    persona-twin-blueprint: "true"
spec:
  # Standard Trained Agent Blueprint fields
  # (knowledge, skills, guardrails, etc.)
  
  # Persona Twin extensions
  personaTwin:
    # Signal suggestions
    signalSuggestions:
      - type: "task_assignment"
        description: "Notify when tasks are assigned to you"
        opaFilterTemplate: |
          package persona_twin
          allow { input.event.type == "task_assigned"; input.event.assignee == delegator }
      
      - type: "platform_notification"
        description: "Notify about platform events"
        opaFilterTemplate: |
          package persona_twin
          allow { input.event.type == "platform_notification"; input.event.user == delegator }
    
    # Filter suggestions
    filterSuggestions:
      - name: "my-tasks-only"
        description: "Only tasks assigned to me"
        opaPolicy: |
          package persona_twin
          allow { input.task.assignee == delegator }
      
      - name: "high-priority-only"
        description: "Only high-priority items"
        opaPolicy: |
          package persona_twin
          allow { input.priority == "high" }
    
    # Schedule suggestions
    scheduleSuggestions:
      - name: "daily-summary"
        description: "Daily summary at 9 AM"
        schedule: "0 9 * * *"
        prompt: "Provide a summary of my tasks and notifications"
      
      - name: "weekly-review"
        description: "Weekly review on Fridays"
        schedule: "0 17 * * 5"
        prompt: "Review my week and suggest improvements"
```

**Extension Model**:
Persona Twin Blueprints extend Trained Agent Blueprints rather than being a separate CRD:
*   **Same CRD kind**: Uses `TrainedAgentBlueprint` with persona-specific metadata
*   **Extension field**: `personaTwin` field contains persona-specific extensions
*   **Backward compatible**: Standard Trained Agent Blueprints work without persona extensions
*   **Reuse**: Leverages existing Trained Agent Blueprint infrastructure

**Platform-Provided Blueprints**:
Hub Platform provides subscription blueprints for common use cases:
*   **Personal Assistant**: Task management, notifications, scheduling
*   **Knowledge Assistant**: Knowledge search, SOP lookup, policy queries
*   **Analytics Assistant**: Metrics, reports, trend analysis
*   **Custom blueprints**: Tenant admins can create custom blueprints

Platform-provided blueprints enable quick twin creation for common use cases.

### Standard Lifecycle

**Persona Twins follow the standard agent lifecycle** (Raw → Trained → Employed) established in Section 7:
*   **Raw Agent**: Container image with capabilities (deployable artifact)
*   **Trained Agent**: Configured via Training Spec (knowledge, skills, guardrails) based on blueprint
*   **Employed Agent**: Delegated via Employment Spec (authority for specific context)

The standard lifecycle ensures that Persona Twins maintain the same governance, audit, and operational controls as business agents.

### Special Recognition

**Special recognition** distinguishes Persona Twins from business agents through metadata labels and category:
*   **Metadata labels**: `persona-twin: "true"` label for recognition
*   **Category isolation**: `category: "persona-twin"` for filtering and isolation
*   **Delegator metadata**: `delegator` field identifies the collaborator who created the twin
*   **Directory filtering**: Directory queries support `personaTwin` filter

Special recognition enables the platform to distinguish Persona Twins from business agents while maintaining standard lifecycle processes.

### Delegator Ownership

**Delegator ownership** means that the collaborator who creates a Persona Twin owns and manages it throughout its lifecycle:
*   **Creation**: Delegator creates twin from blueprint
*   **Configuration**: Delegator configures signals, filters, and schedules
*   **Training**: Delegator trains twin in workbench
*   **Employment**: Delegator deploys twin (creates Employment Spec)
*   **Management**: Delegator manages twin (enable/disable, update, revoke)

Delegator ownership ensures that collaborators have full control over their personal AI assistants.

## Conceptual Models / Frameworks

### The Persona Twin Lifecycle Model

Persona Twins follow the standard lifecycle with special recognition:

```
Blueprint Selection
    ↓
Training Spec Creation (from blueprint)
    ├── Signal suggestions applied
    ├── Filter templates applied
    └── Customizations added
    ↓
Training (Raw → Trained)
    ├── Standard training process
    └── Special recognition (labels, category)
    ↓
Employment (Trained → Employed)
    ├── Authority delegation (from delegator)
    ├── Trigger activation
    └── Visibility configuration
    ↓
Operation
    ├── Responds to personal triggers
    ├── Operates within delegator authority
    └── Maintains audit trail
```

The lifecycle follows standard processes while maintaining special recognition and delegator ownership.

### The Blueprint-to-Twin Model

Blueprints enable twin creation:

```
Persona Twin Blueprint
    ├── Signal Suggestions
    │   ├── Task assignment
    │   ├── Platform notifications
    │   └── Schedules
    ├── Filter Templates
    │   ├── OPA policies for filtering
    │   └── Customizable by collaborator
    └── Training Configuration
        ├── Skills, knowledge, prompts
        └── Guardrails
            ↓
Collaborator Customization
    ├── Select signals
    ├── Apply filters
    ├── Configure schedules
    └── Customize training
            ↓
Training Spec Creation
    └── Standard lifecycle continues
```

Blueprints provide starting configurations that collaborators customize for their needs.

## Systemic and Enterprise Considerations

### Blueprint Management

Persona Twin Blueprints must be managed:
*   **Platform blueprints**: Hub Platform provides default blueprints
*   **Custom blueprints**: Tenant admins can create custom blueprints
*   **Versioning**: Blueprints are versioned and immutable once published
*   **Deprecation**: Deprecated blueprints should be marked and eventually removed

Blueprint management ensures that collaborators have access to current, supported blueprints.

### Lifecycle Consistency

Persona Twins must maintain lifecycle consistency:
*   **Standard processes**: Twins follow standard training and employment processes
*   **Governance compliance**: Twins maintain governance, audit, and policy compliance
*   **Operational controls**: Twins support standard operational controls (kill switches, throttling, etc.)
*   **Lifecycle transitions**: Twins follow standard lifecycle state transitions

Lifecycle consistency ensures that Persona Twins maintain enterprise standards while enabling personal productivity.

### Resource Management

Persona Twins must be managed for resource consumption:
*   **Proliferation monitoring**: Monitor twin proliferation to manage resource consumption
*   **Quotas**: Set quotas to manage resource consumption per twin
*   **Fair usage**: Enforce fair usage policies to prevent resource abuse
*   **Directory visibility**: Directory filtering enables admin visibility into twin proliferation

Resource management ensures that Persona Twins don't consume excessive resources.

## Common Misconceptions & Failure Modes

### Misconception: Blueprints Are Required

Some organizations assume that blueprints are required for Persona Twin creation. However, blueprints are convenience mechanisms; collaborators can create twins manually if needed.

**Failure mode**: Organizations assume that twin creation requires blueprints, limiting flexibility for advanced use cases.

### Misconception: Twins Don't Follow Standard Lifecycle

Some organizations assume that Persona Twins follow a different lifecycle than business agents. However, twins follow the standard lifecycle with special recognition, not a different lifecycle.

**Failure mode**: Organizations expect different lifecycle processes for twins, leading to confusion and inconsistent governance.

### Misconception: Delegators Can't Manage Twins

Some organizations assume that only admins can manage Persona Twins. However, delegators own and manage their twins throughout the lifecycle.

**Failure mode**: Organizations restrict twin management to admins, reducing delegator control and productivity.

## Practical Implications

### Blueprint Strategy

Organizations should develop a blueprint strategy that:
*   **Provides common blueprints**: Provide blueprints for common personal productivity use cases
*   **Enables customization**: Enable collaborators to customize blueprints for their needs
*   **Maintains best practices**: Encode best practices in blueprint configurations
*   **Supports evolution**: Support blueprint evolution as needs change

Blueprint strategy directly impacts twin creation efficiency and effectiveness.

### Lifecycle Management

Organizations should manage Persona Twin lifecycle with:
*   **Standard processes**: Use standard training and employment processes
*   **Governance integration**: Integrate twins into governance processes
*   **Operational controls**: Apply standard operational controls to twins
*   **Lifecycle monitoring**: Monitor twin lifecycle for issues and optimization

Lifecycle management ensures that Persona Twins maintain enterprise standards.

## Cross-References

*   **Section 7 (Agent Lifecycle)**: Describes the standard agent lifecycle that Persona Twins follow
*   **Section 21.1 (What Are Persona Twins?)**: Defines Persona Twins and their characteristics
*   **Section 21.3 (Use Cases)**: Describes use cases for Persona Twins

---

**References:**

*   `seer-design/implementation-concepts/persona-twin-blueprint.md` — Persona Twin Blueprint concept
*   `seer-design/implementation-concepts/persona-twins.md` — Persona Twins concept
