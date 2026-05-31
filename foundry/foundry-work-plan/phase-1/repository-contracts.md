# Phase 1 Repository Contracts

**Status:** Authoritative SSOT for Phase 1 entity storage, field naming, labels, and artifact URIs.

Normative platform modules implement these contracts. Jira is the current **Work Repository adapter**; contract field names are vendor-neutral.

**Related:** [api-surface.md](api-surface.md) (HTTP routes), [module-boundaries.md](module-boundaries.md) (ownership), [integration/contract-gates.md](../integration/contract-gates.md) (milestones).

---

## Entity storage model

Phase 1 distinguishes **Work Artifacts** (Git Intent Repository content) from **Work Items** (operational records in the Work Repository).

| Entity | Work Artifact (Intent Repository) | Work Item (Work Repository) | Notes |
|--------|-----------------------------------|----------------------------|-------|
| **Discovery Case** | Yes — charter, synthesis artifacts | Yes — orchestration record | Dual representation; IDs linked via `foundry-id-{entityId}` |
| **Product Intent** | Yes — folder tree, PSDs, mockups | Yes — Build-track orchestration record | Dual representation |
| **PDR** | Yes — artifact only | No | Stored under Intent folder; not a Work Item |
| **Work Order** | No | Yes | WO Runtime execution unit |
| **Task** | No | Yes | Sub-tree under Work Order |

**Storage backends (Phase 1):**

| Store | Backing | Serving |
|-------|---------|---------|
| Intent Repository | Git (GitHub) | Metadata Service (IDs, commit tracking) + Git read/write APIs |
| Work Repository | External adapter (Jira in Phase 1) | Orchestrator + WO Runtime via adapter APIs |
| Orchestrator state | Postgres | Orchestrator REST API |

---

## Universal field conventions

All Phase 1 entities exposed via Management or Orchestrator APIs include:

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `title` | string | Yes | Short human-readable label (≤ 255 chars) |
| `description` | string (markdown) | Yes | Long-form body; markdown supported in UI |

Work Items additionally carry Work Repository binding fields (see below). Work Artifacts carry `artifactUri` when registered with Metadata Service.

---

## Work Repository contract fields (`workRepo*`)

API schemas and event payloads use vendor-neutral names. The Jira adapter maps to Jira issue keys, projects, and statuses internally.

| Contract field | Purpose | Example |
|----------------|---------|---------|
| `workRepoProject` | Work Repository project key for this Workbench | `CHKOUT-WO` |
| `workRepoKey` | Issue key for an orchestration item or WO | `CHKOUT-WO-123` |
| `workRepoItemKey` | Issue key for a Task or sub-item | `CHKOUT-WO-456` |
| `workRepoStatus` | Normalized status in Work Repository | `in-progress` |
| `workRepoType` | Adapter issue type name (informational) | `Work Order` |

**Rules:**

- New API schemas MUST NOT use `jira*` field names.
- Adapter documentation MAY describe Jira-specific mapping under "Work Repository adapter (Jira)" sections only.

---

## Work Repository labels (`foundry-*`)

All external Work Repository labels use a uniform `foundry-` prefix:

| Label pattern | Purpose | Example |
|---------------|---------|---------|
| `foundry-tenant-{foundryId}` | Foundry scope | `foundry-tenant-foundry-zeta` |
| `foundry-workshop-{workshopId}` | Workshop scope | `foundry-workshop-workshop-abc` |
| `foundry-workbench-{workbenchId}` | Workbench scope (shared Jira projects) | `foundry-workbench-wb-checkout` |
| `foundry-track-{track}` | Track affinity | `foundry-track-discovery` |
| `foundry-kind-{kind}` | Entity kind | `foundry-kind-work-order` |
| `foundry-id-{entityId}` | Platform entity ID | `foundry-id-DC-89` |

Orchestrator custom attributes on Work Items align with this namespace (e.g. `foundry-scenario`, `foundry-orchestration-item`, `foundry-wo-group`).

Shared Jira projects (Operations, Feedback, Work) filter by `foundry-workbench-{workbenchId}`. Dedicated Work Order projects scope by project key instead of label.

---

## Entity schemas (Phase 1)

### Discovery Case

Dual: Work Item + optional Intent Repository artifacts (charter, synthesis).

```yaml
DiscoveryCase:
  id: string              # DC-89 from Metadata Service
  title: string
  description: string     # markdown
  workbenchId: string
  track: discovery
  stage: string           # workflow stage
  workRepoKey: string     # when mirrored in Work Repository
  artifactUri: string     # optional root artifact in Intent Repository
  sourceRefs:             # optional typed upstream references
    - type: signal | fir | bug | operational-problem | manual | other
      ref: string         # external or platform ID
      title: string       # optional display
  createdAt: timestamp
  updatedAt: timestamp
```

### Product Intent

Dual: Work Item + Intent Repository folder tree.

```yaml
ProductIntent:
  id: string              # PI-456
  title: string
  description: string     # markdown
  workbenchId: string
  track: build
  stage: string
  workRepoKey: string
  artifactUri: string     # Intent folder root
  parentDiscoveryCaseId: string  # optional handoff link
  createdAt: timestamp
  updatedAt: timestamp
```

### PDR (Product Decision Record)

Artifact-only in Intent Repository (no Work Item).

```yaml
ProductDecisionRecord:
  id: string              # platform or file-derived ID
  title: string
  description: string     # markdown body
  artifactUri: string
  discoveryCaseId: string
  decision: go | pivot | park | drop
  productIntentId: string # when proceed-to-build
```

### Work Order

Work Item only.

```yaml
WorkOrder:
  id: string              # WO-1234
  title: string
  description: string     # markdown
  workbenchId: string
  orchestrationItemId: string
  orchestrationItemType: discovery-case | product-intent
  workspace: string
  scenario: string
  workRepoKey: string
  workRepoProject: string
  workRepoStatus: string
  assignee: string        # optional
  woGroup: string         # optional group label
  createdAt: timestamp
  updatedAt: timestamp
```

### Task

Work Item only.

```yaml
Task:
  id: string              # TASK-890 or workRepoItemKey
  title: string
  description: string     # markdown
  workOrderId: string
  parentTaskId: string    # optional
  agentType: human | ai-agent
  workRepoItemKey: string
  workRepoStatus: string
  scenario: string        # optional override
  dependencies: string[]  # sibling task IDs
  state: blocked | ready | in_progress | completed | failed | cancelled
  syncScope: synced | local   # local for Personal Work / workspace-local tasks
  createdAt: timestamp
  updatedAt: timestamp
```

---

## ID generation

Metadata Service assigns IDs per `(workbenchId, type)`:

| Type | Prefix | Scope | Example |
|------|--------|-------|---------|
| `discovery-case` | DC | Workbench | DC-89 |
| `product-intent` | PI | Workbench | PI-456 |
| `work-order` | WO | Workbench | WO-1234 |
| `release-intent` | RI | Workbench | RI-78 |
| `run-case` | RC | Workbench | RC-45 |

Work Repository item keys follow adapter conventions (Jira project key + sequence in Phase 1).

---

## Artifact URI (Phase 1 canonical)

Foundry Platform Phase 1 uses containment-scoped URIs aligned to Foundry → Workshop → Workbench:

```text
artifact://{foundry-id}/{workshop-id}/{workbench-id}/{repo-type}/{artifact-type}/{artifact-id}@{revision}
```

| Component | Description | Example |
|-----------|-------------|---------|
| `{foundry-id}` | Foundry code | `foundry-zeta` |
| `{workshop-id}` | Workshop code | `workshop-abc` |
| `{workbench-id}` | Workbench ID | `wb-checkout` |
| `{repo-type}` | Repository type | `intent`, `design`, `code` |
| `{artifact-type}` | Category within repo | `discovery-case`, `pdr`, `psd`, `product-intent` |
| `{artifact-id}` | Stable artifact ID | `DC-89`, `PI-456` |
| `{revision}` | Git commit SHA or semver | `a1b2c3d` |

**Examples:**

```text
artifact://foundry-zeta/workshop-abc/wb-checkout/intent/discovery-case/DC-89@a1b2c3d
artifact://foundry-zeta/workshop-abc/wb-checkout/intent/pdr/PDR-DC-89-go@b4c5d6e
artifact://foundry-zeta/workshop-abc/wb-checkout/intent/product-intent/PI-456@main
```

ACE landscape-scoped URIs in [../../ace/repositories.md](../../ace/repositories.md) remain valid for enterprise topology; Phase 1 platform APIs and Metadata Service use the containment form above. See ACE doc for mapping notes.

---

## Authorization (summary)

Role-based access via Team Management; Cipher SDKs supply role assertions (`admin`, `manager`, `builder`) scoped to Workbench.

| Role | Artifacts (Intent Repository routes) | Work Items (track routes) |
|------|--------------------------------------|---------------------------|
| **admin** | Full CRUD | Full CRUD + manual transitions |
| **manager** | CRUD on assigned work | Create OIs, transition, assign WOs |
| **builder** | Read; write via WO/session | Read assigned WOs/tasks; complete human tasks |
| **viewer** | Read-only | Read-only |

Detail per route: [api-surface.md](api-surface.md).

---

## Migration appendix (legacy aliases)

During transition from Jira-coupled naming:

| Legacy | Canonical | Notes |
|--------|-----------|-------|
| `jiraKey` | `workRepoKey` | Orchestration items, WOs |
| `jira_key` (SQLite) | `workRepoItemKey` | WO Runtime local state |
| `jiraProject` | `workRepoProject` | Workbench config |
| `workbench:{id}` label | `foundry-workbench-{workbenchId}` | Re-label shared Jira projects |
| `workbench:WB-123` | `foundry-workbench-wb-checkout` | Use stable workbench ID |
| `foundry.sessions.{foundry_id}` (topic) | `/{foundry-id}/foundry.session-management.{event}` | Atropos path — see [event-contracts.md](event-contracts.md) |
| `orchestrator.events.{workbench}` (topic) | `/{foundry-id}/foundry.orchestrator.{event}` | Atropos path |

**Re-labeling guidance:** When provisioning or syncing Workbench integrations, apply the full `foundry-*` label set. Existing issues may retain legacy labels until touched; Orchestrator SHOULD write canonical labels on create/update.

APIs MAY accept legacy field aliases in request bodies for one release cycle; responses MUST emit canonical `workRepo*` names only.

---

## Read next

- [api-surface.md](api-surface.md) — HTTP route taxonomy
- [event-contracts.md](event-contracts.md) — Atropos event paths and envelope
- [open-questions.md](open-questions.md) — remaining unresolved items
- [../../foundry-platform/management/platform-developer-guide/requirements.md](../../foundry-platform/management/platform-developer-guide/requirements.md) — Management implementation
- [../../foundry-platform/orchestrator/platform-developer-guide/requirements.md](../../foundry-platform/orchestrator/platform-developer-guide/requirements.md) — Orchestrator implementation
