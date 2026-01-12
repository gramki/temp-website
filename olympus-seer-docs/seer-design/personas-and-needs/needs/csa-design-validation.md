# CSA Need: Design Validation and Pattern Compliance

> **Status:** Reference Document  
> **Last Updated:** 2026-01-13  
> **Related:** [CSA Role Definition](../csa.md) | [Roles Overview](../roles.md#2-cognitive-systems-architect-csa)

---

## Overview

The **Cognitive Systems Architect (CSA)** ([role definition](../roles.md#2-cognitive-systems-architect-csa)) designs how cognition works across agents. A critical part of this role is **validating that implementations match designs** and **ensuring pattern compliance** across the agent portfolio.

This document details the design validation and pattern compliance needs for platform developers building CSA capabilities.

---

## The Validation Challenge

### Why Validation Matters

Agent implementations can drift from designs:
- **AE interprets design differently** than CSA intended
- **Incremental changes** accumulate into significant deviation
- **Prompt adjustments** change reasoning behavior unintentionally
- **Tool additions** alter cognitive flow

Without validation, the organization loses architectural integrity — agents become unpredictable and ungovernable.

### Validation Scope

| Aspect | Design Defines | Validation Checks |
|--------|----------------|-------------------|
| **Reasoning Pattern** | How agent reasons | Does implementation follow pattern? |
| **Cognitive Boundaries** | What agent thinks about | Does agent stay within boundaries? |
| **Decision Points** | Where choices are made | Are decisions at expected points? |
| **Failure Semantics** | How failures manifest | Do failures match design? |
| **Escalation Paths** | When/how to escalate | Does escalation work as designed? |

---

## Design-to-Implementation Validation

### Validation Workflow

```
CSA creates design
       ↓
AE implements agent
       ↓
AE submits for validation
       ↓
CSA reviews implementation
       ↓
Automated checks run
       ↓
Manual review where needed
       ↓
Approved / Changes requested
```

### What CSA Validates

#### 1. Reasoning Pattern Compliance

CSA validates that the implemented reasoning matches the designed pattern:

| Design Element | Validation Check |
|----------------|------------------|
| Pattern type (ReAct, CoT, etc.) | Implementation uses correct pattern |
| Reasoning steps | Steps match design specification |
| Step sequence | Steps execute in correct order |
| Step constraints | Each step respects defined constraints |
| Iteration limits | Loops bounded as designed |

**Example: ReAct Pattern Validation**

```yaml
design_spec:
  pattern: "ReAct"
  steps:
    - reason: "Analyze input and form plan"
    - act: "Execute one action"
    - observe: "Process action result"
  constraints:
    max_iterations: 10
    must_complete_in: 60s

validation_checks:
  - pattern_structure: "Implementation has reason-act-observe loop"
  - step_order: "Steps execute in correct sequence"
  - iteration_bound: "Loop terminates within 10 iterations"
  - time_bound: "Execution completes within 60 seconds"
```

#### 2. Cognitive Boundary Compliance

CSA validates that agents stay within designed cognitive boundaries:

| Boundary Type | Design Specifies | Validation Checks |
|---------------|------------------|-------------------|
| **Scope** | What problems agent addresses | Agent doesn't attempt out-of-scope work |
| **Decisions** | What agent can decide | Agent doesn't make unauthorized decisions |
| **Actions** | What agent can do | Agent doesn't take unauthorized actions |
| **Knowledge** | What agent can access | Agent doesn't access unauthorized knowledge |

#### 3. Failure Semantics Compliance

CSA validates that failures occur as designed:

| Failure Aspect | Design Specifies | Validation Checks |
|----------------|------------------|-------------------|
| **Classification** | How failures are categorized | Errors have correct classification |
| **Behavior** | What happens on failure | Failure leads to correct state |
| **Propagation** | How failures spread | Failures contained as designed |
| **Recovery** | How to recover | Recovery paths work as designed |

#### 4. Escalation Design Compliance

CSA validates that escalation works as designed:

| Escalation Aspect | Design Specifies | Validation Checks |
|-------------------|------------------|-------------------|
| **Triggers** | When to escalate | Correct conditions trigger escalation |
| **Targets** | Who receives escalation | Escalation reaches correct recipient |
| **Context** | What context is passed | All required context is included |
| **Timeouts** | What if no response | Timeout behavior is correct |

---

## Pattern Compliance

### Pattern Library

CSA maintains an approved pattern library:

| Pattern | Purpose | Constraints |
|---------|---------|-------------|
| **ReAct** | General-purpose reasoning | Max iterations, timeout |
| **Chain-of-Thought** | Step-by-step reasoning | Step limit, validation points |
| **Reflection** | Self-critique | Reflection depth limit |
| **Decomposition** | Break into subtasks | Subtask limit, depth limit |
| **Orchestration** | Coordinate sub-agents | Fan-out limit, timeout |

### Pattern Constraints

Each pattern has defined constraints that must be enforced:

```yaml
pattern: "ReAct"
constraints:
  structural:
    - "Must have reason step before act"
    - "Must have observe step after act"
    - "Loop must be explicit"
  
  behavioral:
    - "Max 10 iterations per task"
    - "Max 30 seconds per iteration"
    - "Must emit trace for each step"
  
  safety:
    - "Must check tool permissions before act"
    - "Must validate inputs before act"
    - "Must handle tool failures gracefully"
```

### Pattern Validation Tools

CSA needs automated tools to validate pattern compliance:

| Tool | Purpose |
|------|---------|
| **Structure Analyzer** | Verify implementation structure matches pattern |
| **Behavior Validator** | Test behavioral constraints |
| **Trace Analyzer** | Analyze reasoning traces for pattern compliance |
| **Constraint Checker** | Verify all constraints are implemented |

---

## Multi-Agent Design Validation

### What CSA Validates for Multi-Agent Systems

| Design Element | Validation Check |
|----------------|------------------|
| **Agent Graph** | Agents connected as designed |
| **Interaction Contracts** | Message formats match specification |
| **Coordination Pattern** | Coordination follows designed model |
| **Authority Boundaries** | Agents respect authority limits |
| **Failure Isolation** | Failures contained as designed |

### Contract Validation

CSA validates that agent-to-agent contracts are honored:

```yaml
contract:
  provider: "orchestrator-agent"
  consumer: "worker-agent"
  
  request_schema:
    type: "task_assignment"
    required: ["task_id", "task_type", "context"]
  
  response_schema:
    type: "task_result"
    required: ["task_id", "status", "result"]
  
  timing:
    timeout: 30s
    acknowledgment_required: true
    acknowledgment_timeout: 5s

validation_checks:
  - "Provider sends valid request schema"
  - "Consumer sends valid response schema"
  - "Timing constraints are met"
  - "Acknowledgments are sent"
```

---

## Design Review Process

### Pre-Implementation Review

Before AE implements, CSA reviews:

| Review Item | Purpose |
|-------------|---------|
| **Feasibility** | Can the design be implemented? |
| **Completeness** | Is the design sufficient for implementation? |
| **Clarity** | Can AE understand the design? |
| **Constraints** | Are constraints implementable? |

### Post-Implementation Review

After AE implements, CSA validates:

| Review Item | Method |
|-------------|--------|
| **Structure** | Automated structure analysis |
| **Behavior** | Automated behavioral testing |
| **Traces** | Manual trace review |
| **Edge Cases** | Manual edge case testing |

### Review Checklist

CSA uses a standard checklist for validation:

- [ ] Reasoning pattern matches design
- [ ] Cognitive boundaries are respected
- [ ] Decision points are at designed locations
- [ ] Failure semantics match design
- [ ] Escalation paths work correctly
- [ ] Telemetry emits required events
- [ ] Constraints are enforced
- [ ] Multi-agent contracts are honored

---

## Platform Requirements

### Design Specification Tools

CSA needs tools to create and manage designs:

| Tool | Purpose |
|------|---------|
| **Pattern Library** | Browse and use approved patterns |
| **Architecture Builder** | Visual design tool |
| **Constraint Editor** | Define and edit constraints |
| **Contract Designer** | Design agent-to-agent contracts |

### Validation Tools

CSA needs tools to validate implementations:

| Tool | Purpose |
|------|---------|
| **Design-Implementation Diff** | Compare design to implementation |
| **Structure Analyzer** | Automated structure validation |
| **Behavior Validator** | Automated behavioral testing |
| **Trace Analyzer** | Analyze reasoning traces |
| **Contract Validator** | Validate agent contracts |

### Review Workflow Tools

CSA needs tools to manage the review process:

| Tool | Purpose |
|------|---------|
| **Review Queue** | Pending reviews |
| **Checklist Tracker** | Track review progress |
| **Feedback Tool** | Provide feedback to AE |
| **Approval Workflow** | Approve or request changes |

---

## OPDA Requirements Summary

| OPDA Dimension | CSA Need |
|----------------|----------|
| **Observable** | See implementation details and behavior |
| **Predictable** | Validate designs produce predictable behavior |
| **Directable** | Define constraints that enable runtime control |
| **Authority Enforceable** | Design authority boundaries that can be enforced |

---

## Desk Support

These needs are supported through the **Agent Design Desk**:

| Console | Capabilities |
|---------|--------------|
| **Design Console** | Pattern library, architecture builder, failure mode catalog |
| **Topology Console** | Agent graph, interaction contracts, coordination patterns |
| **Validation Console** | Design review queue, diff view, checklist, sign-off |

See [Agent Design Desk](../../ux-architecture/desks/agent-design-desk/README.md) for detailed specifications.

---

## Anti-Patterns

| Pattern | Why It's Problematic |
|---------|---------------------|
| "Design as we build" | No design = no predictability |
| "Close enough to design" | Deviation accumulates |
| "We'll validate later" | Issues compound |
| "Trust the engineer" | Validation ensures quality |
| "Constraints are suggestions" | Constraints must be enforced |

---

## Success Criteria

CSA design validation needs are met when:

- [ ] Every agent has a documented design
- [ ] Designs use approved patterns
- [ ] Implementations are validated against designs
- [ ] Deviations are identified and resolved
- [ ] Pattern constraints are enforced
- [ ] Multi-agent contracts are validated
- [ ] Review workflow is streamlined

---

*End of document*
