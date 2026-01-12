# Session Notes: Agent Runtime Detailed Design

**Date**: 2026-01-12  
**Focus**: Completing detailed design for the Agent Runtime subsystem

---

## Objective

Execute the detailed design plan for the Agent Runtime subsystem, addressing 5 open design gaps that had been identified and received inputs in prior sessions.

---

## Work Completed

### 1. Content Migration

**Migrated `runtime-deployment.md`** to `agent-runtime/runtime-deployment.md`:
- Moved file to proper subsystem folder structure
- Updated 12 cross-references across the seer-docs codebase
- Deleted original file

### 2. New Design Documents Created

| Document | Description |
|----------|-------------|
| `iam-provisioning.md` | IAM profile creation flow, lifecycle management, roles/groups inheritance logic (wildcard vs CSV), bot mode (no delegator), credential injection via zone-vault |
| `authority-change-respawning.md` | Authority change detection architecture (Seer Operator + IAM Observer Service), respawning triggers and process, zero-downtime rolling updates |
| `signal-exchange-integration.md` | sx-observer service architecture, workbench-level observer pattern, store-and-forward capability, back-pressure handling, scale-to-zero support, Atropos message routing |
| `agent-ingress-gateway-integration.md` | Request dispatch flow, response path (agents update directly via Hub APIs), external resource references (Workbench Data Store), error handling with DLQ in Atropos |

### 3. Enhancements to Existing Documents

**Enhanced `runtime-deployment.md`** with:
- Ingress Path Provisioning section (path pattern, authentication)
- Ingress Lifecycle section (creation, updates, cleanup)
- Integration with Heracles section (cluster-ingress configuration)

### 4. Documentation Updates

- **Updated `SCOPE.md`** — Marked all items complete, updated status to 🟢 Design Complete
- **Updated `README.md`** — Added links to all new documents, architecture diagram
- **Updated `subsystems/README.md`** — Changed Agent Runtime status to complete

### 5. Decision Log

**Created ADR-0104**: Seer Agent Runtime Detailed Design
- Documents architectural decisions for IAM provisioning, authority change detection, Signal Exchange integration, and ingress configuration
- Updated ADR-0074 with cross-references to new documentation

---

## Key Architectural Decisions Documented

### IAM Profile Provisioning
- Profile created **before** pod deployment
- Roles/groups inheritance from delegator (wildcard `*` or CSV subset)
- **Bot mode** for agents without delegator (base identity only)
- Kill switch includes immediate IAM revocation

### Authority Change Detection
- **Seer Operator** only watches CRD changes
- **IAM Observer Service** (in Agent Lifecycle Manager) watches Cipher IAM
- Flow: IAM Change → IAM Observer → CRD Update → Seer Operator → Respawn

### Signal Exchange Integration
- **sx-observer** as workbench-level observer
- Signal Exchange **unaware** of Agent Ingress Gateway
- All routing via **Atropos** (event bus)
- **Store-and-forward** enables scale-to-zero
- sx-observer triggers scale-up when requests arrive

### Response Handling
- Agents update requests **directly via Hub APIs** (not via sx-observer)
- External resources stored in **Workbench Data Store** (URIs returned)
- **DLQ in Atropos** for failed dispatches with configurable retries

---

## Files Changed

### Created (7 files)
- `olympus-seer-docs/seer-design/subsystems/agent-runtime/iam-provisioning.md`
- `olympus-seer-docs/seer-design/subsystems/agent-runtime/authority-change-respawning.md`
- `olympus-seer-docs/seer-design/subsystems/agent-runtime/signal-exchange-integration.md`
- `olympus-seer-docs/seer-design/subsystems/agent-runtime/agent-ingress-gateway-integration.md`
- `olympus-hub-docs/decision-logs/0104-seer-agent-runtime-detailed-design.md`

### Modified (15+ files)
- `olympus-seer-docs/seer-design/subsystems/agent-runtime/runtime-deployment.md` (migrated + enhanced)
- `olympus-seer-docs/seer-design/subsystems/agent-runtime/SCOPE.md`
- `olympus-seer-docs/seer-design/subsystems/agent-runtime/README.md`
- `olympus-seer-docs/seer-design/subsystems/README.md`
- Various cross-reference updates across seer-docs

### Deleted (1 file)
- `olympus-seer-docs/seer-design/subsystems/runtime-deployment.md` (moved to agent-runtime/)

---

## Commit

```
[SPE-2586] feat(seer): complete agent runtime subsystem detailed design

- Migrate runtime-deployment.md to agent-runtime folder
- Create iam-provisioning.md with IAM profile lifecycle and delegation
- Create authority-change-respawning.md with detection and respawning
- Create signal-exchange-integration.md with sx-observer architecture
- Create agent-ingress-gateway-integration.md with routing and data store
- Enhance runtime-deployment.md with ingress path configuration
- Add ADR-0104 documenting architectural decisions
- Update all cross-references to new file locations
- Mark agent-runtime subsystem as design complete
```

**Stats**: 56 files changed, 6404 insertions

---

## Final Structure

```
olympus-seer-docs/seer-design/subsystems/agent-runtime/
├── README.md                           ← Overview and architecture
├── SCOPE.md                            ← Coverage summary (🟢 Complete)
├── runtime-deployment.md               ← Core runtime (migrated + enhanced)
├── iam-provisioning.md                 ← IAM profile lifecycle (NEW)
├── authority-change-respawning.md      ← Authority detection (NEW)
├── signal-exchange-integration.md      ← sx-observer architecture (NEW)
└── agent-ingress-gateway-integration.md ← Request routing (NEW)
```

---

## Deferred to Implementation

The following implementation details were explicitly deferred:
- sx-observer: Storage backend, queue type, retention policies
- Back-pressure handling: Thresholds, throttling algorithms
- Scale-up: Specific mechanisms, warm-up times, HPA configuration
- Load balancing: Specific algorithms beyond K8s Service defaults
- Observability: Specific metrics and dashboard layouts

---

## Next Steps

The Agent Runtime subsystem is now design complete. Potential next subsystems to detail:
1. **Agent Lifecycle Manager** — Employment spec management, IAM Observer Service
2. **Cipher IAM Extensions** — IAM profile API details
3. **Agent Ingress Gateway** — Full subsystem design
4. **Seer Sidecar** — Guardrails and policy enforcement

---

*Session completed successfully with all planned design documents created and committed.*
