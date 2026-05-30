# Session Identity

Session identity defines how Workspace Sessions are uniquely identified, queried, and distinguished in the control plane. Session Management treats identity as a stable session ID plus a composite business key for discovery — without embedding Work Order identifiers.

## Session ID

Every session receives an opaque, globally unique `session_id` at creation time (UUID v7 or equivalent sortable ID recommended).

| Property | Rule |
|----------|------|
| **Immutability** | `session_id` never changes for the life of the record |
| **URL binding** | Session URL hostname or path segment derives from `session_id` (see Session Infrastructure networking) |
| **API path** | All session-scoped APIs use `/api/v1/sessions/{session-id}` |

The session ID is the primary key in the session store and the correlation ID across events, Infrastructure provision requests, and WO Runtime heartbeats.

## Composite business key

Orchestrator and admins often need to find "the active Development session for user X on Workbench Y." That query uses a composite key:

```
(user_id, workspace_type, workbench_id, instance_id?)
```

| Dimension | Description |
|-----------|-------------|
| `user_id` | Owner of the session (one person per session) |
| `workspace_type` | One of the six workspace types: `product-specification`, `ux-design`, `development`, `qa`, `release`, `governance` |
| `workbench_id` | Workbench scope within the Foundry |
| `foundry_id` | Tenant scope (required on all records and APIs) |
| `instance_id` | Optional disambiguator when multiple concurrent sessions per composite key are allowed |

### Default cardinality

By default, Foundry policy allows **at most one Active session** per `(foundry_id, user_id, workspace_type, workbench_id)`. Create requests when an Active session already exists return the existing session (idempotent get-or-create) or `409 Conflict` depending on API flag — implementers choose per WSSM-FR-0005.

When `instance_id` is supplied (explicit multi-session mode), multiple Active sessions may coexist for the same user and workbench if policy permits.

## Addressing in APIs

| Operation | Addressing |
|-----------|------------|
| Get one session | `GET /api/v1/sessions/{session-id}` |
| Query by business key | `GET /api/v1/sessions?user=&workspace_type=&workbench=&state=` |
| Admin list | `GET /api/v1/admin/sessions?foundry=&state=&page=&limit=` |

Query APIs never require Work Order fields. Filters are limited to session attributes and state.

## Session URL

After activation, `session_url` is stored on the session record (from Session Infrastructure). It is exposed in:

- Query API responses for Active and Stopped sessions (Stopped may return last URL for display; live access fails)
- `session-activated` and subsequent events

The URL is not the primary key; reprovisioning on resume may update underlying pod routing while keeping the same `session_id` and URL pattern.

## References to other entities

Session records store foreign **identifiers** only:

| Field | Source of truth |
|-------|-----------------|
| `foundry_id` | Management / Metadata Service |
| `workbench_id` | Management |
| `user_id` | Identity provider |

Session Management does **not** enforce foreign key constraints against Management tables. Callers (Orchestrator) are trusted to supply valid IDs. Invalid IDs surface as empty query results or orphaned sessions, not as database constraint errors.

## What identity excludes

Session identity intentionally omits:

- Work Order IDs, Epic keys, or Scenario names
- Orchestration item IDs
- Agent or task identifiers (WO Runtime local concern)

Heartbeat payloads may include `active_wos` as an **integer count** for capacity observability; those counts are not stored as session identity fields.

## Read next

- [session-lifecycle.md](session-lifecycle.md) — states tied to this identity
- [../platform-developer-guide/session-api.md](../platform-developer-guide/session-api.md) — query and create APIs
- [../../concepts/workspace-session.md](../../concepts/workspace-session.md) — platform concept
