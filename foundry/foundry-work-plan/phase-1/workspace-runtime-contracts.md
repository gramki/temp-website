# Phase 1 Workspace Runtime Contracts

**Status:** Authoritative SSOT for in-session execution: session ↔ Work Order attachment, parallel scheduling, context compilation, and Git branch lifecycle.

Normative implementation requirements: [work-order-runtime/platform-developer-guide/requirements.md](../../foundry-platform/work-order-runtime/platform-developer-guide/requirements.md).

---

## Session ↔ Work Order attachment

| Rule | Detail |
|------|--------|
| **Ownership** | One person per Workspace Session; sessions are not shared |
| **Cardinality** | Multiple Work Orders MAY attach to one session (default max 20) |
| **Assignment** | Orchestrator assigns WOs after session is Active; WO Runtime discovers via Work Repository poll and Atropos events |
| **Isolation** | Each WO gets `work-orders/WO-{id}/` with separate repo checkouts and `wo/WO-{id}` branches |

### Parallel WO execution

**All attached Work Orders with pending ready tasks MAY execute in parallel.** There is no FIFO or priority ordering across WOs on the same session.

Scheduling waits only at the **task** level:

- Tasks with unmet dependencies remain pending
- Tasks in `blocked` state (agent failure, quota, external wait) do not schedule until unblocked
- Concurrent agent cap (`max concurrent agents`, default 10) may defer spawns but does not serialize WOs

WO Runtime treats each attached WO independently for task-tree scheduling; ready tasks across all attached WOs compete for agent slots under session limits.

---

## Context compilation

Agents receive merged knowledge from four levels (most general → most specific):

1. **Workshop** — domain, practices, standards (Workshop Definition Repository)
2. **Workbench** — product architecture, conventions (workbench settings + repos)
3. **Scenario** — task-specific guidance (Work Catalog)
4. **Work Order** — OI graph, linked artifacts, WO state

Merge rule: closer level wins on file collision (WO > Scenario > Workbench > Workshop).

Full specification: [context-compilation.md](../../foundry-platform/work-order-runtime/concepts/context-compilation.md).

---

## Agent execution (Phase 1 demo)

WO Runtime task execution is **real** in Phase 1. Individual agent **skills** MAY use stubs; capable-agent routing and harness preparation are real.

See [phase-1-scope.md](phase-1-scope.md#real-vs-mocked).

---

## Git per-WO branches and cleanup

| Phase | Policy |
|-------|--------|
| Active WO | `work-orders/WO-{id}/` retained on session volume; branch `wo/WO-{id}` per cloned repo |
| Terminal WO, no commits | Do not push remote branch |
| Terminal WO, unpushed commits | Push `wo/WO-{id}`, open PR |
| Post-terminal | After configurable retention, WO Runtime MAY archive local `work-orders/WO-{id}/`; audit metadata kept in Local State Store |

Full specification: [git-infrastructure.md](../../foundry-platform/management/platform-developer-guide/git-infrastructure.md#wo-branch-management), WOR-FR-0051–0053.

---

## Read next

- [workspace-session-management/README.md](../../foundry-platform/workspace-session-management/README.md) — session lifecycle (Orchestrator bridge)
- [work-order-runtime/README.md](../../foundry-platform/work-order-runtime/README.md) — execution engine overview
- [golden-path.md](golden-path.md#part-c--builder-session-flow-any-wo) — builder session demo flow
