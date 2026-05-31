# Phase 1 API Surface

**Status:** Authoritative route taxonomy for Phase 1 module APIs consumed by Web App, IDE, Orchestrator, and WO Runtime.

Entity fields and storage rules: [repository-contracts.md](repository-contracts.md). Event transport: [event-contracts.md](event-contracts.md).

---

## Route taxonomy

Phase 1 splits HTTP APIs by **what** is being accessed:

| Class | Scope | Pattern | Examples |
|-------|-------|---------|----------|
| **Artifact routes** | Git-backed Intent Repository content | `/workbenches/{workbenchId}/repos/{repoType}/...` | PDR, PSD, discovery charter |
| **Work-item routes** | Track orchestration and execution | `/workbenches/{workbenchId}/tracks/{track}/...` | Discovery Case, Product Intent, Work Order, Task |
| **Platform routes** | Workbench provisioning, catalog, sessions | Existing Management / Session paths | Unchanged base paths |

**Rule:** Artifact CRUD uses repo-based paths. Orchestration and execution records use track-based paths. Do not mix artifact paths with Work Item IDs.

---

## Standard response envelope

```json
{
  "data": { },
  "meta": {
    "workbenchId": "wb-checkout",
    "requestId": "uuid"
  }
}
```

Error envelope (all modules):

```json
{
  "error": {
    "code": "ENTITY_NOT_FOUND",
    "message": "Human-readable message",
    "details": { }
  }
}
```

All entity payloads in `data` include `title` and `description` (markdown) per [repository-contracts.md](repository-contracts.md).

---

## Artifact routes (Intent Repository)

Base: `/api/v1/workbenches/{workbenchId}/repos/intent`

| Method | Path | Description |
|--------|------|-------------|
| GET | `/artifacts` | List artifact metadata (filter by `artifactType`) |
| GET | `/artifacts/{artifactType}/{artifactId}` | Get artifact metadata + `artifactUri` |
| GET | `/artifacts/{artifactType}/{artifactId}/content` | Get markdown/file content at revision |
| POST | `/artifacts/{artifactType}` | Create artifact (Metadata Service assigns ID where applicable) |
| PUT | `/artifacts/{artifactType}/{artifactId}` | Update artifact content |
| GET | `/product-intents/{piId}/tree` | List folder tree under Product Intent |

**PDR (artifact-only):**

| Method | Path | Description |
|--------|------|-------------|
| POST | `/pdrs` | Record PDR under Discovery Case or Product Intent folder |
| GET | `/pdrs/{pdrId}` | Get PDR metadata and content |

Example create Discovery Case charter artifact:

```http
POST /api/v1/workbenches/wb-checkout/repos/intent/artifacts/discovery-case
Content-Type: application/json

{
  "artifactId": "DC-89",
  "title": "Offline mode for mobile checkout",
  "description": "## Question\nShould we offer offline mode?\n\n## Hypotheses\n- ...",
  "revision": "main"
}
```

Response includes canonical `artifactUri`:

```json
{
  "data": {
    "artifactId": "DC-89",
    "artifactType": "discovery-case",
    "artifactUri": "artifact://foundry-zeta/workshop-abc/wb-checkout/intent/discovery-case/DC-89@main",
    "title": "Offline mode for mobile checkout",
    "description": "..."
  }
}
```

Design and Code repos use the same pattern with `repoType` = `design` | `code`.

---

## Work-item routes (track-based)

Base: `/api/v1/workbenches/{workbenchId}/tracks`

### Discovery track

| Method | Path | Description |
|--------|------|-------------|
| POST | `/discovery/cases` | Create Discovery Case (Work Item + optional artifact link) |
| GET | `/discovery/cases` | List Discovery Cases |
| GET | `/discovery/cases/{dcId}` | Get case with `stage`, `workRepoKey`, `sourceRefs` |
| POST | `/discovery/cases/{dcId}/transition` | Manual stage transition |
| GET | `/discovery/cases/{dcId}/history` | Transition audit |

Example create:

```http
POST /api/v1/workbenches/wb-checkout/tracks/discovery/cases
Content-Type: application/json

{
  "title": "Offline mode for mobile checkout",
  "description": "Evaluate offline checkout for intermittent connectivity markets.",
  "sourceRefs": [
    { "type": "manual", "ref": "pm-initiated", "title": "PM question" }
  ]
}
```

### Build track

| Method | Path | Description |
|--------|------|-------------|
| POST | `/build/product-intents` | Create Product Intent |
| GET | `/build/product-intents` | List Product Intents |
| GET | `/build/product-intents/{piId}` | Get PI with stage and links |
| POST | `/build/product-intents/{piId}/transition` | Manual transition |
| GET | `/build/product-intents/{piId}/work-orders` | List WOs for PI |

### Work Orders and Tasks (execution)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/build/work-orders` | List WOs (filter: `orchestrationItemId`, `status`) |
| GET | `/build/work-orders/{woId}` | WO detail with `workRepoKey`, scenario |
| GET | `/build/work-orders/{woId}/tasks` | Task tree |
| GET | `/build/tasks/{taskId}` | Task with `agentType`, dependencies |
| POST | `/build/tasks/{taskId}/complete` | Complete human task |

Task example:

```json
{
  "data": {
    "id": "TASK-890",
    "title": "Analyze connectivity patterns",
    "description": "Review analytics for offline session gaps.",
    "agentType": "ai-agent",
    "workRepoItemKey": "CHKOUT-WO-456",
    "state": "in_progress",
    "dependencies": []
  }
}
```

---

## Orchestrator API (cross-workbench patterns)

Orchestrator retains global paths for workflow administration; work-item reads SHOULD prefer track routes above for Web App consistency.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/orchestration-items/{id}` | Resolve by platform ID (includes `title`, `description`) |
| POST | `/api/v1/orchestration-items/{id}/transition` | Stage transition with justification |
| GET | `/api/v1/work-orders?orchestration-item={id}` | List WOs (returns `workRepoKey`, not `jiraKey`) |
| GET | `/api/v1/workflows/{type}?workbench={id}` | Effective workflow |

---

## Session and Runtime (Execution Plane)

| Method | Path | Owner | Description |
|--------|------|-------|-------------|
| GET | `/api/v1/sessions?user=&workspace_type=&workbench=` | Session Management | Query active session |
| POST | `/api/v1/sessions` | Session Management | Create session |
| GET | `/health` | WO Runtime (in-pod) | Liveness |
| GET | `/work-orders` | WO Runtime (in-pod) | Attached WOs for session |
| GET | `/work-orders/{woId}/tasks` | WO Runtime | Task tree with `agentType` |

---

## Authorization by route class

| Route class | Required scope | Typical roles |
|-------------|----------------|---------------|
| Artifact write | Workbench membership + builder or above | builder, manager, admin |
| Discovery/Build create | Workbench membership + manager or above | manager, admin |
| Transition | Workbench manager or track owner | manager, admin |
| WO/Task read | Assignee or workbench member | builder+ |
| Human task complete | Assignee or session owner | builder |
| Admin/provisioning | Workbench admin | admin |

Cipher SDK JWT claims carry `foundryId`, `workshopId`, `workbenchId`, and role bindings. Cross-workbench access is denied unless explicitly granted at Foundry admin level.

---

## Event callbacks (Atropos)

Modules receive platform events via **Atropos HTTP callbacks**. Path convention and envelope: [event-contracts.md](event-contracts.md).

| Concern | Contract |
|---------|----------|
| Path format | `/{foundry-id}/foundry.{module}.{event-semantic-name}` |
| Envelope | `foundryId`, `workshopId`, `workbenchId`, `correlationId`, `entityRefs`, `payload` |
| HTTP correlation | State-changing REST responses SHOULD include `meta.correlationId` matching emitted events |

Example callback registration (conceptual): Orchestrator subscribes to `/foundry-zeta/foundry.wo-runtime.work-order-completed` at its internal webhook endpoint.

---

## Web App console mapping (summary)

| Console | Primary APIs |
|---------|--------------|
| Orchestration | `tracks/discovery/cases`, `tracks/build/product-intents` |
| Repositories & Tools | `repos/intent/...`, `repos/design/...` |
| Work / WO status | `tracks/build/work-orders`, Orchestrator events |
| Admin | Management workbench + integration APIs; label config uses `foundry-*` patterns |

Full UI-to-module matrix: `ui-module-contracts.md` (follow-on).

---

## Read next

- [repository-contracts.md](repository-contracts.md) — field schemas and URI rules
- [event-contracts.md](event-contracts.md) — Atropos paths and event envelope
- [integration/contract-gates.md](../integration/contract-gates.md) — milestone gates referencing this surface
