# Prototype Mock Data

Static fixtures for no-backend prototype flows.

## Principles

- Data should be deterministic and resettable.
- Use realistic entity identifiers and relationships.
- Include both happy-path and failure-path records.

## Suggested fixture groups

- `workshops.*`
- `workbenches.*`
- `discovery-cases.*`
- `product-intents.*`
- `work-orders.*`
- `tasks.*`
- `governance-verdicts.*`
- `traceability-links.*`

## Current fixture files

- `workshops.json` - tenant and workshop definitions
- `workshop-metadata.json` - workshop-level description, ownership, health, and activity summary
- `workbenches.json` - workbench inventory per workshop
- `workbench-metadata.json` - workbench-level description, product code, ownership, health, and deployment summary
- `discovery-cases.json` - discovery journey entities
- `product-intents.json` - build journey entities
- `work-orders.json` - WO queue and execution records
- `tasks.json` - task-level execution records
- `teams.json` - staffing by workbench, with workshop-level shared UX and release managers
- `team-member-profiles.json` - optional richer profile records for workforce detail pages
- `workspace-sessions.json` - owner-led workspace session records with canonical session URL, remote IDE URL, and active coder pod linkage
- `session-activity-events.json` - session-scoped activity stream with typed taxonomy and filterable event records
- `coder-pods.json` - active coder pod + pod history per session, including monitoring URLs, health, and resources
- `session-employed-agents.json` - session agent and skill invocation usage grouped by supported time windows
- `session-token-usage.json` - session token usage with USD totals and model/agent-level breakdowns
- `activity-events.json` - cross-track chronological activity log for workbench wall
- `release-intents.json` - release-oriented orchestration items linked to product intents
- `repositories-tools.json` - repository and external tool references per workbench
- `current-user.json` - logged-in session user for global header profile menu
- `governance-verdicts.json` - governance outcomes and block semantics
- `traceability-links.json` - cross-entity lineage graph
- `scenarios/happyPath.json` - deterministic default startup context
- `scenarios/buildTrackTwoWorkOrders.json` - prioritized build-first scenario with two WOs

## Scenario presets

- `happyPath`
- `buildTrackTwoWorkOrders`

## Seed context (v0.1)

- Tenant: `Zeta`
- Workshops: `Tachyon`, `Photon`, `Electron`
- `Electron` intentionally has no workbenches yet
- `DDA` display name remains uppercase with slug `dda`

## Session fixture contracts

- `workspace-sessions.json` is the source of truth for session identity and ownership. `id`, `ownerId`, `workOrderIds`, and `activeCoderPodId` must always reference valid entities in `teams.json`, `work-orders.json`, and `coder-pods.json`.
- `session-activity-events.json` contains:
  - `eventTypes`: allowed taxonomy ids (`task_created`, `task_completed`, `work_order_assigned`, `work_order_status_changed`, `work_order_status_completed`, `repo_sync_started`, `repo_sync_completed`)
  - `sessionActivityEvents`: event records that must include `sessionId`, `eventType`, `actorId`, and `occurredAt`; optional `workOrderId`/`taskId` values must resolve to existing records.
- `coder-pods.json` contains one session entry per `sessionId` with `activePodId`, `activePod`, and `podHistory`. `activePod.id` must match `activePodId`.
- `session-employed-agents.json` standardizes usage windows (`all`, `today`, `last_24h`, `last_7d`). Each session entry maps a `windows` object to agent summaries and per-skill invocation counts.
- `session-token-usage.json` stores token and cost telemetry. `currency` is fixed to `USD`, and each session record includes aggregate totals plus model and agent breakdowns.
