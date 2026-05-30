# Workspace Folder Structure

The Workspace Folder Structure defines how Foundry materializes repositories and work artifacts on disk inside a builder's Workspace Session — as a multi-root VS Code workspace rooted at `$HOME/<workbench>-<workspace>/`.

## What it is

When WO Runtime provisions a session, it lays out a predictable directory tree. The IDE Explorer reflects this structure with read-only versus writable indicators.

### Root layout

```
$HOME/<workbench>-<workspace>/
├── .foundry/                    # Session metadata, plugin state
├── workbench-knowledge/          # Read-only: workbench ACE knowledge repos
│   ├── domain/
│   ├── practices/
│   └── ontology/
├── user-work-catalog/            # Writable: builder-authored scenarios (User tier)
│   └── work-catalog/{track}/{oi-type}/{workspace}/scenarios/
├── workspace-work-catalog/       # Read-only: computed effective catalog
│   └── work-catalog/             # Foundry → Workshop → Workbench → User merge
└── work-orders/
    └── WO-{id}/
        ├── work-context/         # OI-scoped artifacts (see below)
        │   └── .sync/            # Sync log and manifests (WO Runtime)
        └── repos/                # Product repos cloned for this WO
            ├── {product}-intent/
            ├── {product}-design/
            └── {product}-{component}/   # Code repos as needed
```

| Path | Mutability | Source |
|------|------------|--------|
| `.foundry/` | WO Runtime | Session config, local state pointers |
| `workbench-knowledge/` | Read-only | Workshop workbench paths: domain, practices, ontology |
| `user-work-catalog/` | Writable | Clone/sync of `user-work-catalog-{userId}/` |
| `workspace-work-catalog/` | Read-only | Computed resolution for this workspace |
| `work-orders/WO-{id}/repos/` | Writable (WO branch) | Cloned per Model B (clone per WO) |

### Workspace-type → repo mapping

WO Runtime clones only repos relevant to the active Workspace type into `work-orders/WO-{id}/repos/`:

| Workspace Type | Repos cloned under `repos/` | Notes |
|----------------|----------------------------|-------|
| Product Specification | Intent, Design | Specification and architecture context |
| Development | All Code repos in workbench scope, Design | Full implementation surface |
| QA | Code (read-oriented), Quality (Tests) | Validation and test authoring |
| UX Design | Design (+ assets per workbench policy) | Design-first workspaces |
| Release | Intent, Design, selected Code | Release-oriented subset |
| Governance | Practices, Domain (from workbench-knowledge; rarely extra product repos) | Ritual and policy work |

`workbench-knowledge/` is always present at session root regardless of WO; it is not re-cloned per WO.

### WO branch lifecycle (Model B)

For each repo under `work-orders/WO-{id}/repos/`:

1. WO Runtime clones the repo at session-appropriate default branch
2. Creates local branch `wo/WO-{id}` in **all** cloned repos
3. Builder and agents work on that branch
4. On WO completion, pushes `wo/WO-{id}` to remote **only if** the repo has unpushed commits
5. Opens PR **only** for repos with changes

Concurrent WOs use isolated `wo/WO-{id}` branches; no cross-WO branch sharing.

### work-context

`work-context/` holds **artifacts produced by all completed tasks across all Work Orders in the parent Orchestration Item (OI)** — not only tasks in the current WO.

| Aspect | Behavior |
|--------|----------|
| **Scope** | Parent OI — includes sibling WO task outputs |
| **Location** | One `work-context/` per `work-orders/WO-{id}/` (per-WO folder, OI-wide content) |
| **Sync owner** | WO Runtime |
| **Structure** | OI-type based convention — hierarchy varies per OI Workflow/Scenario; not platform-enforced paths |
| **Updates** | Event notifications when tasks complete in any assigned WO in the OI; periodic polling fallback |

Builders read work-context for cross-WO continuity (specs, analysis outputs, prior decisions). WO Runtime retrieves artifacts from completed work items and materializes them under the convention for that OI type.

#### `.sync/` folder

WO Runtime maintains `work-context/.sync/`:

| File / entry | Purpose |
|--------------|---------|
| `last-sync.json` | Timestamp, OI ID, trigger (event \| poll) |
| `sync-log.ndjson` | Append-only log of sync runs |
| `manifest-{timestamp}.json` | Per-run change manifest (added/updated/removed paths) |

The IDE may surface last sync time and pending changes in the Explorer (see IDE-UX-104).

Example work-context layout (illustrative — actual paths follow OI convention):

```
work-context/
├── .sync/
│   ├── last-sync.json
│   ├── sync-log.ndjson
│   └── manifest-2026-05-30T10-00-00Z.json
├── specifications/
│   └── auth-requirements.md
└── analysis/
    └── threat-model-summary.md
```

Track and OI identifiers are **not** required in the path; structure is defined by the OI Workflow/Scenario convention for that OI type.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **WO Runtime** | Provision folders, clone repos, branches, work-context sync |
| **IDE** | Multi-root workspace, Explorer labels, read-only badges |
| **Management** | Git repo inventory, work catalog resolution |
| **Session Infrastructure** | Persistent volume at `$HOME/<workbench>-<workspace>/` |

## ACE/UPIM alignment

| UPIM / ACE Repository | Local path |
|----------------------|------------|
| Domain, Practices, Ontology | `workbench-knowledge/` |
| Intent, Design, Code, Quality | `work-orders/WO-{id}/repos/{repo}/` |
| Work Catalog (effective) | `workspace-work-catalog/` |
| Work Catalog (user) | `user-work-catalog/` |
| Work artifacts (OI scope) | `work-context/` |

See [../../../ace/repositories.md](../../../ace/repositories.md) and [../../management/platform-developer-guide/git-infrastructure.md](../../management/platform-developer-guide/git-infrastructure.md).

## Related concepts

- [Foundry Workspace Panel](foundry-workspace-panel.md) — Quick links into repos in this structure
- [Scenario Authoring](scenario-authoring.md) — Writes under `user-work-catalog/`
- [Task Graph View](task-graph-view.md) — Task tree separate from work-context tree
- [Work Order](../../concepts/work-order.md) — Each WO gets `work-orders/WO-{id}/`

## Further reading

- [../platform-developer-guide/ux-requirements.md](../platform-developer-guide/ux-requirements.md) — IDE-UX-099 to IDE-UX-104
- [../../work-order-runtime/platform-developer-guide/requirements.md](../../work-order-runtime/platform-developer-guide/requirements.md) — WOR-FR-0044 to WOR-FR-0058
- [../../work-order-runtime/platform-developer-guide/ide-integration.md](../../work-order-runtime/platform-developer-guide/ide-integration.md) — Workspace Folder Protocol
- [../../management/platform-developer-guide/git-infrastructure.md](../../management/platform-developer-guide/git-infrastructure.md) — WO Branch Management
