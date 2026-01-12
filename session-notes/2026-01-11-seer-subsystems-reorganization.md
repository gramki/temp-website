# Seer Subsystems Reorganization

> **Date**: 2026-01-11  
> **Session Type**: Documentation Reorganization  
> **Status**: ✅ Completed

---

## Objective

Reorganize the Seer design documentation structure by:
1. Extracting concepts from subsystem files into a dedicated `implementation-concepts/` folder
2. Creating a proper subsystem folder structure based on the scratchpad list
3. Creating brief capability outlines for each subsystem (not detailed designs)
4. Preserving all existing detailed content
5. Creating a published OPDA capabilities tracker

---

## Key Decisions

### Structure Approach
- **Focus on organization, not detailed design** - This iteration creates structure and brief outlines only
- **Preserve existing content** - All detailed content remains in original files, referenced from new structure
- **Defer detailed design** - Subsystems marked as "Detailed design to be added in subsequent sessions"

### Subsystem Organization
- **14 subsystems** organized into dedicated folders (from scratchpad)
- **Agent Lifecycle Manager** has 5 sub-components as separate files
- **SDK contracts** limited to `seer-agent-sdk/` subsystem only
- **UX Channels** explicitly excluded (covered in `personas-and-needs/`)

### OPDA Capabilities Tracker
- Created as **published tracker** in `implementation-concepts/opda-capabilities.md`
- Consolidates content from 4 scratchpad files
- Fine-grained checklist format with ✅/❌ status markers
- References to both Seer and Hub documentation

---

## Work Completed

### 1. OPDA Capabilities Tracker
**File**: `olympus-seer-docs/seer-design/implementation-concepts/opda-capabilities.md`

- Consolidated capabilities from:
  - `agent-observability.md` (scratchpad)
  - `agent-predicatbility.md` (scratchpad)
  - `agent-directability.md` (scratchpad)
  - `agent-authority-controls.md` (scratchpad)
- Structured by capability area: Observability, Predictability, Directability, Authority
- Each capability marked: ✅ Documented (Seer/Hub) or ❌ Not Yet Documented
- Includes references to Seer and Hub documentation
- Serves as **published tracker** (scratchpad files are not published)

### 2. Concept Extraction
**Location**: `olympus-seer-docs/seer-design/implementation-concepts/`

Created 5 concept files extracting conceptual content from existing subsystem files:

- **`context-assembly.md`**
  - Three-source model (Enterprise Knowledge, Enterprise Memory, Agent Memory)
  - Retrieval flow and key principles
  - Extracted from `context-assembly-engine.md`

- **`agent-observability.md`**
  - Observability architecture (agent-level and platform-level)
  - Key principles and Watch integration
  - Observability vs CAF distinction
  - Extracted from `agent-observability.md`

- **`guardrails.md`**
  - Two-layer model (Behavioral Guidelines + Sidecar Guardrails)
  - Execution order and verification pattern
  - Key principles
  - Extracted from `guardrails.md`

- **`authority-enforcement.md`**
  - Enforcement architecture (3 enforcement points)
  - OPA policy model
  - Violation handling
  - Extracted from `authority-enforcement.md`

- **`agent-lifecycle.md`**
  - Three-layer agent model (Raw → Trained → Employed)
  - Lifecycle states and transitions
  - Key principles
  - Extracted from `agent-lifecycle-service.md`

### 3. Subsystem Folder Structure
**Location**: `olympus-seer-docs/seer-design/subsystems/`

Created 14 subsystem folders with README.md files:

1. **`cipher-iam-extensions/`** - Agent identity, authority delegation, IAM integration
2. **`agent-runtime/`** - Runtime environment, deployment, scaling operators
3. **`seer-sidecar/`** - Guardrails, metrics, policy enforcement, authority enforcement
4. **`agent-lifecycle-manager/`** - Employment spec management, delegation chain sync, agent levers, ecosystem integration, directory
   - Sub-components:
     - `employment-spec-manager.md`
     - `delegation-chain-sync-service.md`
     - `agent-levers-service.md`
     - `agent-ecosystem-integration-services.md`
     - `employed-agent-directory.md`
5. **`agent-ingress-gateway/`** - Subscription lifecycle, subscription-scoped policies, Signal Exchange integration
6. **`model-gateway/`** - Bifrost-based LLM gateway, routing, fallback, budgets
7. **`agent-health-monitor/`** - Cost SLOs, behavior SLOs, feedback SLOs, human feedback service
8. **`agent-session-supervisor/`** - Supervisory policies, observations, escalations
9. **`context-compiler/`** - Context compilation from memory, knowledge, session state
10. **`seer-agent-sdk/`** - SDK for Raw Agents (employment spec, prompts, context, metrics, tools, memory, knowledge)
11. **`raw-agent-lifecycle-manager/`** - Raw agent spec, validation, directory, operators, levers
12. **`trained-agent-lifecycle-manager/`** - Training spec, validation, directory, employed agent discovery, feedback services
13. **`agent-analytics/`** - Cognitive observability enhancements, platform-level dashboards
14. **`agent-test-runner/`** - Agent testing, behavior validation, health and safety checks

### 4. Brief Subsystem Outlines
Each subsystem README includes:
- **Status**: 🟡 Draft — Capability outline
- **Overview**: 1-2 paragraph overview based on scratchpad
- **Capabilities**: Bullet list from scratchpad
- **Existing Content**: References to detailed content (if applicable)
- **Related**: Links to concepts, requirements, related subsystems
- **Note**: "Detailed design to be added in subsequent sessions"

### 5. Agent Evaluation Handling
**File**: `agent-test-runner/parked-capabilities.md`

- Rephrased `agent-evaluation.md` as parked capabilities
- Referenced from `agent-test-runner/README.md`
- Maintains parking rationale and deferred capabilities list

### 6. Content Preservation
- **Moved**: `observability-extensions-to-watch.md` → `agent-analytics/observability-extensions-to-watch.md`
- **Preserved**: All other existing detailed content remains in original files
- **Referenced**: All subsystem READMEs reference existing detailed content for migration

### 7. Documentation Updates
**File**: `subsystems/README.md`

- Updated with new folder structure
- Added "Legacy Files" section mapping old files to new locations
- Updated governance distribution table
- Maintained ADR references

---

## File Structure Created

```
olympus-seer-docs/seer-design/
├── implementation-concepts/
│   ├── opda-capabilities.md (NEW - Published tracker)
│   ├── context-assembly.md (NEW)
│   ├── agent-observability.md (NEW)
│   ├── guardrails.md (NEW)
│   ├── authority-enforcement.md (NEW)
│   └── agent-lifecycle.md (NEW)
└── subsystems/
    ├── README.md (UPDATED)
    ├── cipher-iam-extensions/ (NEW)
    ├── agent-runtime/ (NEW)
    ├── seer-sidecar/ (NEW)
    ├── agent-lifecycle-manager/ (NEW)
    │   ├── README.md
    │   ├── employment-spec-manager.md
    │   ├── delegation-chain-sync-service.md
    │   ├── agent-levers-service.md
    │   ├── agent-ecosystem-integration-services.md
    │   └── employed-agent-directory.md
    ├── agent-ingress-gateway/ (NEW)
    ├── model-gateway/ (NEW)
    ├── agent-health-monitor/ (NEW)
    ├── agent-session-supervisor/ (NEW)
    ├── context-compiler/ (NEW)
    ├── seer-agent-sdk/ (NEW)
    ├── raw-agent-lifecycle-manager/ (NEW)
    ├── trained-agent-lifecycle-manager/ (NEW)
    ├── agent-analytics/ (NEW)
    │   └── observability-extensions-to-watch.md (MOVED)
    └── agent-test-runner/ (NEW)
        ├── README.md
        └── parked-capabilities.md (NEW - from agent-evaluation.md)
```

---

## Legacy Files (To Be Migrated)

The following files contain detailed content that will be migrated to appropriate subsystem folders in future sessions:

- `agent-lifecycle-service.md` → `agent-lifecycle-manager/`
- `agent-lifecycle-api.md` → `agent-lifecycle-manager/`
- `guardrails.md` → `seer-sidecar/`
- `authority-enforcement.md` → `seer-sidecar/` and `agent-ingress-gateway/`
- `context-assembly-engine.md` → `context-compiler/` and `seer-agent-sdk/`
- `runtime-deployment.md` → `agent-runtime/`
- `agent-observability.md` → `agent-analytics/` and `seer-agent-sdk/`
- `model-gateway.md` → `model-gateway/`
- `agent-identity-authority.md` → `cipher-iam-extensions/` (placeholder)

---

## Key Principles Applied

1. **Structure First, Details Later** - Focus on organization, not detailed design
2. **Preserve Existing** - Don't lose any existing detailed content
3. **Brief Outlines** - Capability lists from scratchpad, not designs
4. **Defer Details** - Mark subsystems as "detailed design to be added"
5. **SDK Contracts** - Only in `seer-agent-sdk/` (reference from others)
6. **OPDA Tracker** - Published concept document with checklist

---

## Next Steps

1. **Detailed Subsystem Design** - Each subsystem to be detailed in subsequent sessions
2. **Content Migration** - Move detailed content from legacy files to appropriate subsystem folders
3. **Requirements Extraction** - Extract requirements to `requirements-enterprise-agentic-platform/` (deferred)
4. **Persona-Based Documentation** - Add persona-specific use cases and journey integration

---

## Related Documents

- Plan: `/Users/ramki/.cursor/plans/reorganize_seer_subsystems_905c586c.plan.md` (deleted after completion)
- Scratchpad: `olympus-hub-docs/scratchpad/seer-subsystems.md`
- OPDA Scratchpads:
  - `olympus-hub-docs/scratchpad/agent-observability.md`
  - `olympus-hub-docs/scratchpad/agent-predicatbility.md`
  - `olympus-hub-docs/scratchpad/agent-directability.md`
  - `olympus-hub-docs/scratchpad/agent-authority-controls.md`

---

## Notes

- All existing detailed content preserved in original files
- No detailed designs written (as requested)
- All subsystem READMEs follow consistent structure
- OPDA capabilities tracker serves as published reference
- Structure ready for iterative detailing in subsequent sessions
