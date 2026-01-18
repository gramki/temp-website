# ADR-0088: DevOps Workbench as Composite Pattern

## Status
Accepted

## Date
2026-01-09

## Context

Building automation in Hub involves repetitive, pattern-based activities performed by Automation Product Owner, Process Architect, and Developer personas:

- **Automation Product Owner**: Triaging ideas, drafting intents, reviewing feedback
- **Process Architect**: Reviewing intents, drafting scenarios, generating SOPs
- **Developer**: Developing applications, diagnosing test failures, managing deployments

These activities are exactly the kind of work Hub was designed to automate. The question was: **How do we structure automation of the automation development process itself?**

### Options Considered

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A. Inline Automation** | DevOps scenarios within each business workbench | Simple; no cross-workbench | Duplicated; pollutes business domain |
| **B. Platform Feature** | Built-in DevOps automation at subscription level | Standardized; no setup | Inflexible; cannot customize |
| **C. DevOps Workbench** | Separate workbench dedicated to DevOps automation | Clean separation; customizable; reusable | More complexity; cross-workbench routing |

## Decision

We adopt **Option C: DevOps Workbench as a Composite Pattern**.

A **DevOps Workbench (D)** is a dedicated workbench that:

1. Is optionally associated with one or more Business Workbenches (A)
2. Receives development lifecycle signals from A via Atropos
3. Contains DevOps Scenarios that automate Automation Product Owner, Process Architect, and Developer activities
4. Enrolls AI Assistant Agents alongside human personas in task queues
5. Operates in its own IAM domain, separate from business workbenches

### Key Characteristics

| Characteristic | Design Choice |
|----------------|---------------|
| **Workbench Type** | Explicit `workbench_type: devops` marker |
| **Scope** | Cross-workbench; can span subscriptions |
| **Ownership** | Tenant owns D; multiple A workbenches can share D |
| **Signal Flow** | A → D via Atropos |
| **Resource Access** | D → A via `{workbench-name}-gateway` Machine |
| **Customization** | Full tenant control over scenarios and agents |

### Platform Provision

| Asset | Description |
|-------|-------------|
| Default DevOps Workbench | One per subscription, using standard scenarios |
| DevOps Blueprint | Template for creating custom DevOps workbenches |
| Standard Scenarios | Platform-provided for common activities |
| AI Agent Templates | Pre-configured assistant agents |

## Consequences

### Positive

- **Clean Separation**: DevOps activities don't pollute business workbench scope
- **Customization**: Tenants can tailor DevOps automation to domain needs
- **Reusability**: Multiple business workbenches can share DevOps capability
- **AI Integration**: AI agents operate in their own IAM domain with appropriate permissions
- **Consistency with Hub Patterns**: Uses existing Hub primitives (Scenarios, Signals, Tasks)

### Negative

- **Cross-Workbench Complexity**: Requires signal routing and credential management
- **Configuration Overhead**: Tenants must configure bindings between A and D
- **Operator Requirements**: Two operators needed (one in A, one in D)

### Neutral

- DevOps Workbench is optional; workbenches without devops_ref operate normally
- Platform provides default DevOps WB, reducing setup burden for simple cases

## Related

- [DevOps Workbench Pattern](../09-composite-systems-and-patterns/devops-workbench/README.md)
- [ADR-0089: Bidirectional DevOps Workbench Binding](./0089-bidirectional-devops-workbench-binding.md)
- [ADR-0090: Signal Routing via Atropos for DevOps](./0090-signal-routing-via-atropos-devops.md)

