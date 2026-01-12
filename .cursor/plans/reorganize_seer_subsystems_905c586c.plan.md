---
name: Reorganize Seer Subsystems
overview: "Reorganize Seer design documentation structure: extract concepts, requirements, create subsystem folders with brief capability outlines (not detailed designs), preserve existing content, create OPDA capabilities tracker."
todos:
  - id: create-opda-concept
    content: Create OPDA capabilities concept document with detailed checklist from scratchpad files (observability, predictability, directability, authority)
    status: completed
  - id: extract-concepts
    content: Extract conceptual content from existing subsystem files to implementation-concepts folder (preserve existing content)
    status: completed
  - id: extract-requirements
    content: Extract requirements from existing files to requirements-enterprise-agentic-platform folder
    status: completed
  - id: create-subsystem-folders
    content: Create folder structure for each of 14 subsystems from scratchpad
    status: completed
  - id: create-subsystem-outlines
    content: Create brief README outlines for each subsystem based on scratchpad capabilities (not detailed designs)
    status: completed
    dependencies:
      - create-subsystem-folders
  - id: preserve-existing-content
    content: Move and preserve existing detailed content to appropriate subsystem folders
    status: completed
    dependencies:
      - create-subsystem-folders
  - id: handle-agent-evaluation
    content: Rephrase agent-evaluation.md as parked capabilities required, to be detailed under Agent Test Runner subsystem
    status: completed
  - id: update-references
    content: Update README files and cross-references to reflect new structure
    status: completed
    dependencies:
      - create-subsystem-outlines
      - preserve-existing-content
---

# Reorganize Seer Design Documentation

## Approach: Structure First, Details Later

**Key Principle**: This iteration focuses on **organization and structure**, not detailed design. Create brief capability outlines based on scratchpad, preserve existing content, and defer detailed subsystem design to subsequent sessions.

## Current State Analysis

The `olympus-seer-docs/seer-design/subsystems/` folder contains 11 files mixing:

- **Concepts**: How things work conceptually
- **Requirements**: What must be supported
- **Subsystem Designs**: Concrete service/system components (some detailed, some not)

## Target Structure

Based on `olympus-hub-docs/scratchpad/seer-subsystems.md`:

### 14 Subsystems (from scratchpad):

1. Cipher IAM Extensions for Agents
2. Agent Runtime
3. Seer Sidecar
4. Agent Lifecycle Manager (with 5 sub-components)
5. Agent Ingress Gateway
6. Model Gateway
7. Agent Health Monitor
8. Agent Session Supervisor
9. Context Compiler
10. Seer Agent SDK
11. Raw Agent Lifecycle Manager
12. Trained Agent Lifecycle Manager
13. Agent Analytics
14. Agent Test Runner

## Reorganization Plan

### Phase 1: Create OPDA Capabilities Concept Tracker

**`implementation-concepts/opda-capabilities.md`** (NEW - Published Tracker)

- Consolidate content from scratchpad files:
  - `olympus-hub-docs/scratchpad/agent-observability.md`
  - `olympus-hub-docs/scratchpad/agent-predicatbility.md`
  - `olympus-hub-docs/scratchpad/agent-directability.md`
  - `olympus-hub-docs/scratchpad/agent-authority-controls.md`
- Format: Concept note with fine-grained checklist
- Structure by capability area (Observability, Predictability, Directability, Authority)
- Each capability marked: ✅ Documented (Seer/Hub) or ❌ Not Yet Documented
- Include references to Seer and Hub documentation
- This is the **published tracker** (scratchpad is not published)

### Phase 2: Extract Concepts (Preserve Existing)

Move conceptual content to `implementation-concepts/`, preserving existing detailed content:

1. **`implementation-concepts/context-assembly.md`**

   - Extract: Three-source model, retrieval flow concepts from `context-assembly-engine.md`
   - Preserve: Detailed content in original file for later migration

2. **`implementation-concepts/agent-observability.md`**

   - Extract: Observability architecture concepts from `agent-observability.md`
   - Preserve: Detailed SDK/implementation content for later migration

3. **`implementation-concepts/guardrails.md`**

   - Extract: Two-layer model concepts from `guardrails.md`
   - Preserve: Detailed implementation content for later migration

4. **`implementation-concepts/authority-enforcement.md`**

   - Extract: Enforcement architecture concepts from `authority-enforcement.md`
   - Preserve: Detailed implementation content for later migration

5. **`implementation-concepts/agent-lifecycle.md`**

   - Extract: Three-layer agent model concepts from `agent-lifecycle-service.md`
   - Preserve: Detailed service content for later migration

### Phase 3: Extract Requirements

Move requirements to `requirements-enterprise-agentic-platform/`:

- Extract embedded requirements (must/should/shall) from all subsystem files
- Move scope/requirements sections
- Create consolidated requirements document

### Phase 4: Create Subsystem Folder Structure

Create folders for all 14 subsystems:

```
subsystems/
├── cipher-iam-extensions/
├── agent-runtime/
├── seer-sidecar/
├── agent-lifecycle-manager/
│   ├── employment-spec-manager.md
│   ├── delegation-chain-sync-service.md
│   ├── agent-levers-service.md
│   ├── agent-ecosystem-integration-services.md
│   └── employed-agent-directory.md
├── agent-ingress-gateway/
├── model-gateway/
├── agent-health-monitor/
├── agent-session-supervisor/
├── context-compiler/
├── seer-agent-sdk/
├── raw-agent-lifecycle-manager/
├── trained-agent-lifecycle-manager/
├── agent-analytics/
└── agent-test-runner/
```

### Phase 5: Create Brief Subsystem Outlines

For each subsystem, create `README.md` with:

- **Brief overview** (1-2 paragraphs)
- **Capabilities list** (from scratchpad, as bullet points)
- **References** to existing detailed content (if any)
- **Status**: Draft/Placeholder
- **Note**: "Detailed design to be added in subsequent sessions"

**Do NOT**:

- Write detailed designs
- Create API specifications
- Design data models
- Write implementation details

**Example structure for each README**:

```markdown
# [Subsystem Name]

> **Status**: 🟡 Draft — Capability outline
> **Last Updated**: [date]

## Overview

[1-2 paragraph overview based on scratchpad]

## Capabilities

Based on `olympus-hub-docs/scratchpad/seer-subsystems.md`:

- [Capability 1 from scratchpad]
- [Capability 2 from scratchpad]
- ...

## Existing Content

[If applicable: Reference to existing detailed content that will be migrated]

## Related

- [Concept references]
- [Requirements references]
- [Related subsystems]

---

*Detailed design to be added in subsequent sessions.*
```

### Phase 6: Preserve and Organize Existing Content

Move existing detailed content to appropriate subsystem folders:

1. **`model-gateway/README.md`**

   - Move existing `model-gateway.md` content here
   - Update with brief outline structure
   - Preserve all existing detailed content

2. **`context-compiler/README.md`**

   - Create outline from scratchpad
   - Reference existing `context-assembly-engine.md` for detailed content
   - Move detailed content to this folder later

3. **`seer-sidecar/README.md`**

   - Create outline from scratchpad
   - Reference existing `guardrails.md` and `authority-enforcement.md` for detailed content
   - Move detailed content to this folder later

4. **`agent-lifecycle-manager/README.md`**

   - Create outline from scratchpad
   - Reference existing `agent-lifecycle-service.md` and `agent-lifecycle-api.md`
   - Create sub-component outlines
   - Move detailed content to sub-component files later

5. **`agent-runtime/README.md`**

   - Create outline from scratchpad
   - Reference existing `runtime-deployment.md` for detailed content
   - Move detailed content to this folder later

6. **`seer-agent-sdk/README.md`**

   - Create outline from scratchpad
   - Reference existing SDK content from `agent-observability.md` and `context-assembly-engine.md`
   - Move detailed SDK content to this folder later

7. **`agent-analytics/README.md`**

   - Create outline from scratchpad
   - Reference existing `agent-observability.md` and `observability-extensions-to-watch.md`
   - Move `observability-extensions-to-watch.md` to this folder

8. **`agent-test-runner/parked-capabilities.md`**

   - Rephrase `agent-evaluation.md` as parked capabilities
   - Reference from `agent-test-runner/README.md`

9. **Other subsystems**: Create brief outlines only (no existing content to preserve)

### Phase 7: Update References

1. Update `subsystems/README.md` with new folder structure
2. Update `seer-design/README.md` if it references subsystems
3. Update cross-references in moved files
4. Update OPDA capabilities tracker with new subsystem references

## Implementation Order

1. **Create OPDA capabilities tracker** (Phase 1)
2. **Extract concepts** (Phase 2) - preserve originals
3. **Extract requirements** (Phase 3)
4. **Create subsystem folders** (Phase 4)
5. **Create brief subsystem outlines** (Phase 5)
6. **Preserve existing content** (Phase 6)
7. **Handle agent evaluation** (Phase 6)
8. **Update references** (Phase 7)

## Key Principles

- **Structure First**: Focus on organization, not detailed design
- **Preserve Existing**: Don't lose any existing detailed content
- **Brief Outlines**: Capability lists from scratchpad, not designs
- **Defer Details**: Mark subsystems as "detailed design to be added"
- **SDK Contracts**: Only in `seer-agent-sdk/` (reference from others)
- **OPDA Tracker**: Published concept document with checklist

## What NOT to Do

- ❌ Write detailed subsystem designs
- ❌ Create API specifications
- ❌ Design data models
- ❌ Write implementation details
- ❌ Remove existing content
- ❌ Create SDK contracts for subsystems other than seer-agent-sdk

## What TO Do

- ✅ Create folder structure
- ✅ Create brief capability outlines
- ✅ Preserve all existing detailed content
- ✅ Extract concepts and requirements
- ✅ Create OPDA capabilities tracker
- ✅ Update references and README files