# Workspace Infrastructure Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/workspace-infrastructure`

**Purpose:** Workbench-level infrastructure visibility for active workspace runtime pods.

---

## Canonical Contract

This console shows runtime infrastructure for all workspace sessions in the workbench.

### Required views

| View | Behavior |
|------|----------|
| Running pods list | Show running pods across workspace sessions |
| Cluster grouping | Group pods by Kubernetes cluster |
| Resource totals | Aggregate CPU, memory, and storage by cluster |
| Pod-to-session link | Each pod row links back to the owning workspace session |

### Pod row fields

- Pod id
- Cluster
- Namespace
- CPU
- Memory
- Storage
- Linked session id

---

## Notes

- This console is infrastructure-observability focused and complements (does not replace) per-session coder pod detail in [workspace-session-details.md](workspace-session-details.md).
