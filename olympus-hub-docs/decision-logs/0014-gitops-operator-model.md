# ADR-0014: GitOps-Based Operator Model for Hub Resources

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub manages a complex ecosystem of resources including workbenches, scenarios, applications, tools, machines, data stores, and task queues. These resources have interdependencies, require versioning, and need consistent configuration across environments.

Traditional approaches include:
1. **Imperative APIs** — Direct API calls to create/update resources
2. **Console-based management** — UI-driven configuration
3. **Script-based automation** — Custom scripts for provisioning
4. **GitOps with operators** — Declarative specifications reconciled by operators

Hub serves enterprise customers who require:
- Audit trails for all configuration changes
- Reproducible environments
- Version-controlled configurations
- Rollback capabilities
- Multi-environment promotion (dev → staging → prod)

## Decision

Hub adopts a **GitOps-based operator model** where:

1. **Declarative Specifications**: All Hub resources are expressed as Custom Resource Definitions (CRDs) in YAML format

2. **Git as Source of Truth**: CRDs are stored in Git repositories, providing:
   - Full version history
   - Pull request-based reviews
   - Branch-based environment management
   - Merge conflict resolution

3. **Operator Reconciliation**: Hub ships with operators that:
   - Watch for CRD changes via Git webhooks
   - Continuously reconcile declared state with actual state
   - Handle dependencies between resources
   - Provide status feedback

4. **Idempotent Operations**: Running the same specification multiple times produces the same result

5. **Atomic Transactions**: Specifications either fully apply or fully roll back

## Alternatives Considered

### Alternative 1: Imperative API Only
- **Pros**: Simple, immediate feedback, familiar to developers
- **Cons**: No audit trail, difficult to reproduce, prone to configuration drift

### Alternative 2: Console-Only Management
- **Pros**: User-friendly, visual feedback
- **Cons**: Not scriptable, no version control, manual and error-prone at scale

### Alternative 3: Terraform/Pulumi Provider
- **Pros**: Industry-standard IaC tools, existing ecosystem
- **Cons**: Additional learning curve, external tool dependency, may not fit Hub's semantic model

## Consequences

### Positive
- **Auditability**: Every change tracked in Git with author, timestamp, and context
- **Reproducibility**: Environments can be recreated from Git state
- **Review Process**: Changes require PR approval before deployment
- **Rollback**: `git revert` restores previous configuration
- **Multi-Environment**: Branches/directories represent environments

### Negative
- **Learning Curve**: Teams must learn CRD syntax and GitOps practices
- **Indirection**: Changes not immediately applied (async reconciliation)
- **Tooling Required**: Git repositories, CI/CD pipelines, webhook infrastructure
- **Debugging Complexity**: Issues may arise in operator reconciliation

### Neutral
- Operators must be maintained and upgraded alongside Hub
- CRD schemas evolve with Hub features
- Console and APIs remain available for read operations and quick edits

## Related Decisions

- [ADR-0015: Persona-Based Operator Grouping](./0015-persona-based-operator-grouping.md)
- [ADR-0002: Scenario Specification Types](./0002-scenario-specification-types.md)

