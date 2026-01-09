# ADR-0091: Git-Based CRD Publishing for DevOps Workbench

> **Status:** Accepted  
> **Date:** 2026-01-09  
> **Deciders:** Architecture Team  
> **Category:** DevOps Workbench

---

## Context

The DevOps Workbench enables AI agents to create and update specifications (CRDs) in the Business Workbench. We needed to decide how these write operations should be performed:

1. **REST API approach** — DevOps agents call a CRD creation API directly
2. **Git-based approach** — DevOps agents commit CRDs to the Business Workbench's Git repository

The choice affects:
- Approval workflows
- Audit trail
- Consistency with existing GitOps practices
- Human review experience

---

## Decision

**We will use Git-based CRD publishing.** DevOps agents in the DevOps Workbench commit CRDs to the Business Workbench's Git repository and create Pull Requests for human review.

### Implementation

1. **Two Machines in DevOps Workbench:**
   - `{workbench}-gateway` — For read operations (query knowledge, memory, scenarios)
   - `{workbench}-git` — For write operations (commit CRDs, create PRs)

2. **Git Tools Available:**
   - `git_create_branch` — Create feature branch for changes
   - `git_commit_crd` — Commit CRD file to branch
   - `git_push` — Push commits to remote
   - `git_create_pr` — Create Pull Request with reviewers

3. **Approval via Pull Request:**
   - No separate `CRDApprovalRequest` CRD needed
   - Human reviews PR in existing Git UI (GitHub, GitLab, etc.)
   - Merge triggers operator reconciliation

4. **Reviewer Assignment:**
   - Reviewers assigned based on CRD type
   - Process Architect reviews normative specs
   - Developer reviews automation specs
   - Tenant Admin reviews infrastructure specs

---

## Rationale

### Why Git-Based?

| Factor | REST API | Git-Based |
|--------|----------|-----------|
| **Consistency** | New workflow | Aligns with existing GitOps |
| **Review Experience** | New UI needed | Use existing Git UI |
| **Audit Trail** | Separate logging | Git history is audit trail |
| **Collaboration** | Limited | Comments, suggestions, edits in PR |
| **Rollback** | Custom mechanism | Git revert |
| **Versioning** | Custom versioning | Git commits/tags |

### Why Not REST API?

1. **Duplicates GitOps** — Hub already uses GitOps for CRD management; adding a REST path creates two mechanisms for the same thing
2. **Approval UX** — Would need to build a new approval UI; Git UI already handles PR review well
3. **Audit gaps** — REST calls would need separate audit logging; Git provides this automatically
4. **No collaboration** — REST API doesn't support inline comments, suggestions, or co-editing

---

## Consequences

### Positive

- **Consistent with GitOps philosophy** already established in Hub
- **Familiar workflow** for developers (PR-based review)
- **Rich collaboration** (comments, suggestions, inline edits)
- **Complete audit trail** via Git history
- **Easy rollback** via Git revert

### Negative

- **Git access required** — DevOps Workbench needs Git credentials for Business Workbench
- **Latency** — Git operations slower than direct API calls
- **Complexity** — Requires managing branches, handling merge conflicts

### Mitigations

- **Credential management** — Handled by DevOpsWorkbenchBinding operator with rotation
- **Conflict handling** — DevOps scenarios should rebase on main before committing
- **Branch cleanup** — Merged branches should be auto-deleted

---

## Alternatives Considered

### Alternative 1: REST API with CRDApprovalRequest

DevOps agents call a REST API to create CRDs; a `CRDApprovalRequest` CRD is created for human approval.

**Rejected because:**
- Creates parallel approval mechanism
- New UI needed for approval
- Doesn't leverage existing Git tooling

### Alternative 2: Direct CRD Application

DevOps agents apply CRDs directly without approval.

**Rejected because:**
- No human oversight
- Violates principle of human control
- Risk of AI errors going to production

### Alternative 3: Hybrid (Draft via API, Approve via Git)

DevOps agents create draft CRDs via API; humans promote to Git for activation.

**Rejected because:**
- Adds complexity
- Two-step workflow confusing
- Draft storage adds state management

---

## Related ADRs

- [ADR-0088: DevOps Workbench Composite Pattern](./0088-devops-workbench-composite-pattern.md)
- [ADR-0089: Bidirectional DevOps Workbench Binding](./0089-bidirectional-devops-workbench-binding.md)
- [ADR-0090: Signal Routing via Atropos for DevOps](./0090-signal-routing-via-atropos-devops.md)

---

## References

- [DevOps Workbench Binding](../09-composite-systems-and-patterns/devops-workbench/devops-workbench-binding.md)
- [DevOps Scenarios](../09-composite-systems-and-patterns/devops-workbench/devops-scenarios.md)
- [Hub Operators](../04-subsystems/operators/README.md)

