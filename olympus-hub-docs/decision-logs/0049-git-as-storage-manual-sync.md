# ADR-0049: Git as Storage with Manual Sync Triggers

## Status

Accepted

## Date

2026-01-06

## Context

Hub uses Git to store CRDs and configurations. A decision is needed on how changes in Git are applied to workbenches: Should the platform continuously reconcile (GitOps), or should sync be triggered manually?

### Constraints

- Enterprises want control over when changes are deployed
- Accidental commits should not immediately affect production
- Audit requirements for deployment authorization
- Different workbenches may have different deployment cadences

### Requirements

- Controlled deployment timing
- Clear authorization for deployments
- Auditability of who triggered deployments
- Support for promotion workflows

## Decision

Git is **storage only**. Sync to target workbenches is triggered **manually** by authorized users. There is no continuous GitOps-style reconciliation.

### Sync Triggers

| Trigger | Initiator | Use Case |
|---------|-----------|----------|
| Manual via UI | Developer/Admin | On-demand deployment |
| Manual via API | Developer/Admin | Scripted deployment |
| Promotion Complete | System | After successful promotion |

### Sync Delegation

Admins can delegate sync trigger permissions to Developers per workbench.

## Alternatives Considered

### Alternative 1: Full GitOps Reconciliation

Continuous reconciliation from Git to workbenches.

**Pros:**
- Modern DevOps pattern
- Self-healing infrastructure
- No manual intervention

**Cons:**
- Less control over timing
- Accidental changes immediately applied
- Harder to stage changes
- Complex conflict resolution

**Why rejected:** Enterprises need explicit deployment control.

### Alternative 2: Branch-Based GitOps

Different branches map to different workbenches, reconcile per branch.

**Pros:**
- Clear environment separation
- Familiar git workflow

**Cons:**
- Merge management complexity
- Branch proliferation
- Still has timing control issues

**Why rejected:** Adds complexity without solving core control requirement.

### Alternative 3: Webhook-Triggered Sync

Git push triggers immediate sync to corresponding workbench.

**Pros:**
- Fast feedback
- Automated

**Cons:**
- Still lacks timing control
- Push = deploy (risky)
- Complex for multi-workbench

**Why rejected:** Push-to-deploy too risky for enterprise.

## Consequences

### Positive

- Full control over deployment timing
- Clear audit trail (who triggered sync)
- Mistakes in Git don't immediately affect running systems
- Supports approval workflows before deployment

### Negative

- Extra step for deployments
- Less "modern" than GitOps
- Potential for Git and runtime to drift

### Neutral

- Developers must explicitly trigger sync
- Sync trigger can be automated in CI/CD pipelines

## Implementation Notes

- Sync delegation allows admins to give developers deploy rights for DEV workbenches
- Promotion automatically triggers sync to target workbench
- Future: May add optional auto-sync per workbench

## References

- [Git Repository](../04-subsystems/artifact-registry/git-repository.md)
- [Promotion Model](../04-subsystems/artifact-registry/promotion-model.md)

