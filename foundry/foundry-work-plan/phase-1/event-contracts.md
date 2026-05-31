# Phase 1 Event Contracts

**Status:** Authoritative SSOT for Foundry platform event transport, routing, and envelope schema.

Entity field naming and storage: [repository-contracts.md](repository-contracts.md). HTTP routes: [api-surface.md](api-surface.md).

---

## Event bus

Foundry uses **[Atropos](https://atropos.olympus.tech/home/overview/)** (Olympus event fabric) as the platform event bus.

| Property | Phase 1 decision |
|----------|------------------|
| **Primary delivery** | HTTP callbacks (webhooks to module endpoints) |
| **Persistence** | All events stored and forwarded by Atropos |
| **Retention** | Default **7 days** (tenant-configurable) |
| **Ephemeral-only events** | None in Phase 1 — every platform event is persisted |

Modules register callback URLs against Atropos path patterns. Internal routing may use Atropos topics; **path convention below is the contract** for publishers and subscribers.

---

## Atropos path convention

Every Foundry event path uses a **tenant-first slash convention**:

```text
/{foundry-id}/foundry.{module}.{event-semantic-name}
```

| Segment | Rule | Example |
|---------|------|---------|
| `/{foundry-id}` | **Required first segment** — tenant identifier | `/foundry-zeta` |
| `foundry` | Fixed product namespace | `foundry` |
| `{module}` | Publishing module (kebab-case) | `orchestrator`, `wo-runtime`, `session-management` |
| `{event-semantic-name}` | Event type (kebab-case); matches envelope `type` | `work-order-completed`, `session-activated` |

**Full path examples:**

```text
/foundry-zeta/foundry.orchestrator.work-order-assigned
/foundry-zeta/foundry.wo-runtime.work-order-completed
/foundry-zeta/foundry.wo-runtime.work-order-failed
/foundry-zeta/foundry.wo-runtime.task-blocked
/foundry-zeta/foundry.session-management.session-activated
/foundry-zeta/foundry.session-management.session-stopped
/foundry-zeta/foundry.management.catalog-published
```

**Workbench scoping** lives in the **envelope** (`workbenchId`, `workshopId`), not in the path — so tenant-level subscriptions stay simple and one callback endpoint can filter by envelope fields.

**Subscriptions:** modules register HTTP callbacks for path patterns, e.g. `/foundry-zeta/foundry.orchestrator.*` or specific event paths.

---

## Canonical event envelope

All Foundry platform events share this envelope. Field names use camelCase in JSON payloads.

```yaml
event:
  type: string                    # semantic name; matches last segment of Atropos path
  timestamp: string               # ISO8601 UTC
  correlationId: string           # end-to-end trace id (required on platform-emitted events)
  causationId: string | null      # prior event id that caused this one

  # Containment (required on every Foundry event)
  foundryId: string
  workshopId: string
  workbenchId: string

  # Publisher
  sourceModule: string            # orchestrator | wo-runtime | session-management | management | work-repo-adapter

  # Actor (when applicable)
  userId: string | null

  # Entity references (when event references platform entities)
  entityRefs:
    - entityType: string          # discovery-case | product-intent | work-order | task | pdr
      entityId: string            # DC-89, WO-1234, PI-456
      artifactUri: string | null  # per repository-contracts.md containment URI
      workRepoKey: string | null  # vendor-neutral Work Repository key

  payload: object                 # event-type-specific body
  metadata: object                # adapter hints, policy, errors, transition context
```

**Rules:**

- `entityRefs` carries both Intent Repository (`artifactUri`) and Work Repository (`workRepoKey`) bindings when an event touches dual-nature entities (Discovery Case, Product Intent).
- Contract field names MUST NOT use vendor-branded prefixes (`jira*`).
- `correlationId` SHOULD propagate across Orchestrator, WO Runtime, Session Management, and Web App refresh handlers.

---

## Delivery semantics

| Property | Guarantee |
|----------|-----------|
| Delivery | At-least-once |
| Ordering | Per partition key (`workbenchId`, `sessionId`, or `correlationId`) — best-effort |
| Idempotency | Consumers MUST dedupe; key on `(type, entityId, timestamp)` or Atropos-assigned `eventId` when present |
| Latency | Target under 500ms from state commit to callback delivery (module NFRs may tighten) |
| Durability | Outbox-after-DB-commit recommended for publishers |

---

## Phase 1 minimum event set (contract gates)

These events are **required** for milestone gates. Full module-specific catalogs live in module READMEs — not duplicated here.

| Gate | Path (example) | Publisher | Primary consumer | Purpose |
|------|----------------|-----------|------------------|---------|
| G4 | `/…/foundry.orchestrator.work-order-assigned` | Orchestrator | WO Runtime | WO created and assigned |
| G5 | `/…/foundry.session-management.session-activated` | Session Management | Orchestrator | Session ready; WO assignment may proceed |
| G6 | `/…/foundry.wo-runtime.work-order-completed` | WO Runtime | Orchestrator | WO terminal success |
| G6 | `/…/foundry.wo-runtime.work-order-failed` | WO Runtime | Orchestrator | WO terminal failure |
| G6 | `/…/foundry.wo-runtime.task-blocked` | WO Runtime | Orchestrator | Recoverable task failure |
| G10 | `/…/foundry.orchestrator.orchestration-item-created` | Orchestrator | Web App, Management | Cross-track handoff (PI seeded from DC) |
| G11 | `/…/foundry.orchestrator.governance-verdict-recorded` | Orchestrator | Web App, Management | Governance transition verdict |

### G4 — work-order-assigned (payload minimum)

```json
{
  "type": "work-order-assigned",
  "foundryId": "foundry-zeta",
  "workshopId": "workshop-payments",
  "workbenchId": "wb-checkout",
  "sourceModule": "orchestrator",
  "entityRefs": [{
    "entityType": "work-order",
    "entityId": "WO-1234",
    "artifactUri": null,
    "workRepoKey": "CHKOUT-WO-456"
  }],
  "payload": {
    "title": "Frame discovery case",
    "description": "…",
    "scenario": "frame-discovery-case",
    "workspace": "product-specification",
    "orchestrationItemId": "DC-89",
    "orchestrationItemType": "discovery-case",
    "assigneeHint": { "userId": "…" }
  }
}
```

Atropos path: `/foundry-zeta/foundry.orchestrator.work-order-assigned`

### G6 — work-order-completed (payload minimum)

```json
{
  "type": "work-order-completed",
  "foundryId": "foundry-zeta",
  "workshopId": "workshop-payments",
  "workbenchId": "wb-checkout",
  "sourceModule": "wo-runtime",
  "correlationId": "corr-abc123",
  "entityRefs": [{
    "entityType": "work-order",
    "entityId": "WO-1234",
    "workRepoKey": "CHKOUT-WO-456"
  }],
  "payload": {
    "status": "completed",
    "outputs": [{ "type": "artifact", "artifactUri": "artifact://foundry-zeta/…" }]
  }
}
```

Atropos path: `/foundry-zeta/foundry.wo-runtime.work-order-completed`

### G5 — session-activated (payload minimum)

```json
{
  "type": "session-activated",
  "foundryId": "foundry-zeta",
  "workshopId": "workshop-payments",
  "workbenchId": "wb-checkout",
  "sourceModule": "session-management",
  "payload": {
    "sessionId": "sess-uuid",
    "sessionUrl": "https://…",
    "workspaceType": "product-specification",
    "userId": "user-uuid"
  }
}
```

Atropos path: `/foundry-zeta/foundry.session-management.session-activated`

---

## Module event catalogs (pointers)

Detailed publish/subscribe lists are owned by each module. Phase 1 does **not** maintain a full emit/consume matrix.

| Module | Document |
|--------|----------|
| Session Management | [session-events.md](../../foundry-platform/workspace-session-management/concepts/session-events.md) |
| Orchestrator | [orchestrator/requirements.md](../../foundry-platform/orchestrator/platform-developer-guide/requirements.md) |
| WO Runtime | [wo-runtime/requirements.md](../../foundry-platform/work-order-runtime/platform-developer-guide/requirements.md) |
| Work Repository adapter | Orchestrator webhook ingress (work-repo adapter → Orchestrator) |

---

## Work Repository adapter ingress

Work Repository changes (Phase 1: Jira adapter) arrive as **HTTP callbacks** to Orchestrator webhook endpoints, not as Foundry-emitted Atropos paths. Adapter payloads are normalized to internal workflow events and MAY re-publish on Atropos with `sourceModule: work-repo-adapter` when fan-out is needed.

---

## Callback endpoint contract

Subscribers expose HTTPS POST endpoints registered with Atropos:

```http
POST {module-callback-url}
Content-Type: application/json
X-Atropos-Path: /foundry-zeta/foundry.wo-runtime.work-order-completed
X-Foundry-Event-Type: work-order-completed

{ … canonical envelope … }
```

Modules MUST validate callback authenticity per Atropos/Olympus platform policy (signature or mTLS — configured at Foundry provisioning).

Link to REST APIs: state-changing operations that emit events SHOULD return `correlationId` in HTTP response `meta` for client correlation. See [api-surface.md](api-surface.md).

---

## Migration appendix (legacy topic names)

Deprecated dot-notation topic strings MUST NOT appear in new docs. Map as follows:

| Legacy (deprecated) | Atropos path |
|---------------------|--------------|
| `foundry.sessions.{foundry_id}` | `/foundry-{id}/foundry.session-management.{event}` |
| `orchestrator.events.{workbench}` | `/foundry-{id}/foundry.orchestrator.{event}` |
| `orchestrator.wo-runtime` | `/foundry-{id}/foundry.wo-runtime.{event}` |
| `foundry.session-infrastructure.{foundry_id}` | `/foundry-{id}/foundry.session-infrastructure.{event}` |
| `metadata.changes` | `/foundry-{id}/foundry.management.metadata-changed` |

Implementations MAY bridge legacy topics during transition; documentation and new integrations MUST use Atropos paths only.

---

## Read next

- [integration/contract-gates.md](../integration/contract-gates.md) — milestone gates referencing these events
- [repository-contracts.md](repository-contracts.md) — `entityRefs`, `workRepo*`, artifact URIs
- [api-surface.md](api-surface.md) — HTTP routes and `correlationId` in responses
