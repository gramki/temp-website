# Contract Gates — Phase 1

Interface contracts between delivery streams. Each gate must be agreed (platform architect) before the consumer stream depends on it for a milestone.

Detailed event schemas: [../phase-1/event-contracts.md](../phase-1/event-contracts.md) (authoritative). Entity/API schemas: [../phase-1/api-surface.md](../phase-1/api-surface.md) + [../phase-1/repository-contracts.md](../phase-1/repository-contracts.md).

## Gate index

| ID | Gate | Producer | Consumer | Blocks |
|----|------|----------|----------|--------|
| G0 | Work Catalog schema + publish path | Control Plane (WCM) | Work Catalog Authoring | M0 |
| G1 | Workbench + Metadata Service (IDs) | Control Plane (Management) | All | M0 |
| G2 | Work Catalog resolution API | Control Plane (WCM) | Orchestrator, Runtime | M0 |
| G3 | Validation on catalog publish | Control Plane (Validation) | Work Catalog Authoring | M0 |
| G4 | WO record + assignment event | Control Plane (Orchestrator) | Execution Plane | M1 |
| G5 | Session create / attach API | Execution Plane (WSSM) | Control Plane (Orchestrator) | M1 |
| G6 | WO Runtime task + completion API | Execution Plane (WOR) | Control Plane, Builder Experience | M1 |
| G7 | Authoritative scenario (first) | Work Catalog Authoring | Execution Plane | M1 |
| G8 | Product Intent entity + Build workflow | Control Plane + Work Catalog (Build) | All | M2 |
| G9 | Discovery Case entity + Discovery workflow | Control Plane + Work Catalog (Discovery) | All | M3 |
| G10 | Cross-track handoff (`create-orchestration-item`) | Control Plane (Orchestrator) | Builder Experience | M3 |
| G11 | Governance invoke + verdict API | Control Plane (Orchestrator) | Execution Plane, Experience | M4 |
| G12 | Traceability query API | Control Plane (Management) | Builder Experience | M4 |
| G13 | CI status on product PR | Release Engineering | Builder Experience, Runtime | M2 |
| G14 | Release package artifact | Release Engineering | Control Plane, Experience | M4 |

---

## G0 — Work Catalog schema + publish path

| | |
|---|---|
| **Producer** | Control Plane (WCM) |
| **Consumer** | Work Catalog Authoring (steward) |
| **Blocks** | M0 |

**Minimum contract:**

- Scenario schema version (`scenario/v1`) and workflow schema documented
- Publish path: git repo → Validation → effective catalog
- Error format on validation failure

**Reference:** [work-catalog-management](../../foundry-platform/management/platform-developer-guide/work-catalog-management/README.md)

---

## G1 — Workbench + Metadata Service

| | |
|---|---|
| **Producer** | Control Plane (Management) |
| **Consumer** | All streams |
| **Blocks** | M0 |

**Minimum contract:**

- Workbench provision API returns workbench ID, repo bindings, `workRepoProject`
- Metadata Service assigns IDs for `discovery-case`, `product-intent`, `work-order`
- All entity payloads include `title` and markdown `description`
- Work Repository labels use `foundry-*` namespace per [repository-contracts.md](../phase-1/repository-contracts.md)

---

## G2 — Work Catalog resolution

| | |
|---|---|
| **Producer** | Control Plane (WCM) |
| **Consumer** | Orchestrator, WO Runtime |
| **Blocks** | M0 |

**Minimum contract:**

- Resolve `(track, oi, workspace, scenario)` → effective definition
- Closest-wins hierarchy documented in [work-catalogues README](../../foundry-platform/work-catalogues/README.md)

---

## G4 — WO record + assignment

| | |
|---|---|
| **Producer** | Control Plane (Orchestrator) |
| **Consumer** | Execution Plane |
| **Blocks** | M1 |

**Minimum contract:**

- Atropos path: `/{foundry-id}/foundry.orchestrator.work-order-assigned` per [event-contracts.md](../phase-1/event-contracts.md)
- Envelope includes `foundryId`, `workshopId`, `workbenchId`, `entityRefs` with `workRepoKey`
- Payload: WO created with `wo_id`, `title`, `description`, `oi_type`, `oi_id`, `workspace`, `scenario`, `workRepoKey`, `inputs`
- Task records include `agentType` (`human` | `ai-agent`)
- Assignment hint (user, role, or queue)

---

## G5 — Session create / attach

| | |
|---|---|
| **Producer** | Execution Plane (WSSM) |
| **Consumer** | Control Plane (Orchestrator) |
| **Blocks** | M1 |

**Minimum contract:**

- Query active session for `(user, workspace, workbench)`
- Create session if none; return session ID and IDE URL
- Attach WO to session
- Atropos path on activation: `/{foundry-id}/foundry.session-management.session-activated` — Orchestrator MUST subscribe before WO assignment on new sessions

**Reference:** [workspace-session-management](../../foundry-platform/workspace-session-management/README.md), [event-contracts.md](../phase-1/event-contracts.md)

---

## G6 — WO Runtime task + completion

| | |
|---|---|
| **Producer** | Execution Plane (WOR) |
| **Consumer** | Control Plane, Builder Experience |
| **Blocks** | M1 |

**Minimum contract:**

- IDE API: list tasks, complete human task, WO status
- Atropos paths per [event-contracts.md](../phase-1/event-contracts.md):
  - `/{foundry-id}/foundry.wo-runtime.work-order-completed` — `wo_id`, `status`, `outputs`, `entityRefs`
  - `/{foundry-id}/foundry.wo-runtime.work-order-failed` — reason
  - `/{foundry-id}/foundry.wo-runtime.task-blocked` — recoverable failure

**Reference:** [ide-integration](../../foundry-platform/work-order-runtime/platform-developer-guide/ide-integration.md), [event-contracts.md](../phase-1/event-contracts.md)

---

## G8 — Product Intent + Build workflow

| | |
|---|---|
| **Producer** | Control Plane + Work Catalog (Build owner) |
| **Consumer** | All |
| **Blocks** | M2 |

**Minimum contract:**

- Product Intent CRUD + stage query
- Orchestrator runs authoritative [product-intent/workflow.yaml](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/workflow.yaml)
- All Build golden-path scenarios authoritative per [scenario-catalog.md](../phase-1/scenario-catalog.md)

---

## G9 — Discovery Case + Discovery workflow

| | |
|---|---|
| **Producer** | Control Plane + Work Catalog (Discovery owner) |
| **Consumer** | All |
| **Blocks** | M3 |

**Minimum contract:**

- Discovery Case CRUD + stage query via track routes (`/tracks/discovery/cases`)
- Optional typed `sourceRefs[]` on create (signal automation deferred; manual refs in-scope)
- Orchestrator runs authoritative [discovery-case/workflow.yaml](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/workflow.yaml)
- Parallel WO group completion semantics

---

## G10 — Cross-track handoff

| | |
|---|---|
| **Producer** | Control Plane (Orchestrator) |
| **Consumer** | Builder Experience |
| **Blocks** | M3 |

**Minimum contract:**

- Action: `create-orchestration-item` with common envelope per [orchestrator-rules.md](../phase-1/orchestrator-rules.md#create-orchestration-item-cross-track-handoff):
  - `track`, `orchestrationItem`, `title`, `seedFrom` (parent entity refs)
  - Containment IDs (`foundryId`, `workshopId`, `workbenchId`) inherited from parent OI unless overridden
- Parent Discovery Case linked to child Product Intent in traceability store
- User task outcome `proceed-to-build` triggers handoff

---

## G11 — Governance invoke + verdict

| | |
|---|---|
| **Producer** | Control Plane (Orchestrator) |
| **Consumer** | Execution Plane, Builder Experience |
| **Blocks** | M4 |

**Minimum contract:**

- `invoke-governance-scenario` with `on-reject: soft-block | hard-block`
- Verdict persisted: `decision`, `findings`, `reviewer`, `timestamp`
- Hard block prevents OI transition

**Reference:** [governance-mvp.md](../phase-1/governance-mvp.md)

---

## G12 — Traceability query

| | |
|---|---|
| **Producer** | Control Plane (Management) |
| **Consumer** | Builder Experience |
| **Blocks** | M4 |

**Minimum contract:**

- Query by OI ID returns parent/child links and `artifactUri` references (containment form)
- Minimum chain per [golden-path traceability](../phase-1/golden-path.md#traceability-phase-1-minimum)

---

## Gate approval process

1. Consumer stream drafts requirement against milestone DoD
2. Producer stream proposes API/event shape
3. Platform architect approves and records in `phase-1/event-contracts.md` or `api-surface.md`
4. Integration lead adds tracer test at milestone boundary

## Read next

- [dependency-graph.md](dependency-graph.md)
- [../milestones.md](../milestones.md)
- [../phase-1/open-questions.md](../phase-1/open-questions.md)
