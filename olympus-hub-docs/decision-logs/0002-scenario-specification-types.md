# ADR-0002: Three Specification Types for Scenarios

## Status

Accepted

## Date

2026-01-05

## Context

Scenarios in Hub are complex constructs that span multiple concerns:
- Business process definitions (what should be done)
- Technical automation (how it's coded)
- Operational deployment (how it's run)

Different personas contribute to different aspects:
- **Process Architects** define business requirements, SOPs, decision criteria
- **Developers** implement automation, configure triggers, bind tools
- **Supervisors** manage task queues, agent enrollment, SLAs

A single monolithic Scenario specification would:
- Mix concerns across personas
- Make it difficult to version components independently
- Create unclear ownership boundaries

## Decision

**Split Scenario specifications into three types aligned with the Hub ontology layers:**

1. **Scenario Normative Specification** (Normative Layer)
   - Owner: Process Architect
   - Content: Roles, Goals, SOPs, Decision criteria, Evidence requirements, Escalation rules, Compliance requirements

2. **Scenario Automation Specification** (Automation Layer)
   - Owner: Developer
   - Content: Hub Application config, Triggers, Tool bindings, Runtime selection, Integration configurations

3. **Scenario Deployment Specification** (Execution Layer)
   - Owner: Supervisor
   - Content: Task queue mappings, Agent enrollment, SLA parameters, Activation settings

This maps to the Scenario Development journey: **Process Architect → Developer → Supervisor**

## Consequences

### Positive
- **Clear ownership**: Each persona owns their specification type
- **Independent versioning**: Normative spec can be updated without touching automation
- **Separation of concerns**: Business rules separate from technical implementation
- **Staged development**: Enables handoff workflow between personas
- **Audit clarity**: Changes to each aspect are tracked separately

### Negative
- **More files to manage**: Three specs instead of one
- **Coordination required**: Changes may need updates across specs
- **Learning curve**: Users must understand which spec to modify

### Neutral
- Operators for each specification type handle the translation to runtime configuration

## Related

- [Scenario Development Journey](../08-personas-and-journeys/journeys/scenario-development.md)
- [Process Architect Operator](../04-subsystems/operators/process-architect-operator.md)
- [Developer Operators](../04-subsystems/operators/developer-operators.md)
- [Supervisor Operators](../04-subsystems/operators/supervisor-operators.md)

