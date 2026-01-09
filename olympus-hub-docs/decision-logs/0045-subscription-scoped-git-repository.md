# ADR-0045: Subscription-Scoped Git Repository with Main Branch Only

## Status

Accepted

## Date

2026-01-06

## Context

Hub manages all CRDs and configurations declaratively. A versioned storage mechanism is needed to track changes, enable rollback, and support promotion workflows.

### Constraints

- All Hub resources must be stored declaratively
- Version history is required for audit and rollback
- Concurrent development by multiple developers must be supported
- Platform should manage Git infrastructure (not rely on customer Git)

### Requirements

- Single source of truth for subscription resources
- Enforceable folder structure
- Support for promotion between workbenches/subscriptions
- Audit trail for all changes

## Decision

Each Hub subscription will have **one platform-managed Git repository** using **main branch only**. Developers requiring concurrent development should use separate DEV workbench instances.

### Key Points

- One Git repo per subscription (per-workbench repos may be added in future)
- Main branch only; no feature branches currently supported
- Platform-managed Git with optional mirror to customer repositories
- Enforceable standard folder structure
- Manual sync triggers (Git is storage, not GitOps reconciliation)

## Alternatives Considered

### Alternative 1: Customer-Provided Git

Use customer's existing GitHub/GitLab repositories.

**Pros:**
- Familiar tooling for developers
- Existing CI/CD integration

**Cons:**
- Complex permission management
- Inconsistent configurations
- Security boundary concerns

**Why rejected:** Platform-managed Git ensures consistent structure and security.

### Alternative 2: Per-Workbench Repositories

Separate Git repository for each workbench.

**Pros:**
- Better isolation
- Simpler per-workbench management

**Cons:**
- More complex promotion (cross-repo)
- Harder to share subscription-level resources
- More repos to manage

**Why rejected:** Subscription scope provides better balance; per-workbench may be added later.

### Alternative 3: Full GitOps with Branches

Support feature branches with GitOps-style reconciliation.

**Pros:**
- Modern DevOps practices
- Familiar to developers

**Cons:**
- Complex merge conflict handling
- Branch management overhead
- Harder to ensure promotion consistency
- Complicates audit trail for compliance

**Why rejected:** Main-branch-only is a deliberate simplification for compliance, not a limitation. Hub's target audience (small teams in regulated enterprises) benefits from simpler audit trails over branch flexibility.

## Consequences

### Positive

- Consistent repository structure across subscriptions
- Simplified promotion (same repo for source and some targets)
- Clear, linear audit trail via Git history
- Platform controls security and access
- Compliance-friendly: single source of truth, no merge complexity

### Negative

- Less familiar to developers used to branching workflows
- Concurrent development requires separate workbenches

### Neutral

- Optional mirror to customer repositories for visibility
- Standard folder structure enforced
- Separate workbenches provide equivalent isolation to branches

## Implementation Notes

- Concurrent development pattern: Use separate DEV workbench instances
- Repository can push to additional remotes (customer Git) on promotion complete
- For small teams, a single DEV workbench is typically sufficient

## References

- [Git Repository](../04-subsystems/artifact-registry/git-repository.md)
- [Promotion Model](../04-subsystems/artifact-registry/promotion-model.md)


