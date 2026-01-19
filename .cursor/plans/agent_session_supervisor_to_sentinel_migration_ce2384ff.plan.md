---
name: Agent Session Supervisor to Sentinel Migration
overview: Rename the Agent Session Supervisor subsystem to Agent Session Sentinel across all seer-docs to avoid conflict with Hub's Supervisor persona. This includes directory rename, file renames, content updates, and updating all cross-references.
todos:
  - id: rename-directory
    content: Rename directory from agent-session-supervisor to agent-session-sentinel
    status: completed
  - id: rename-files
    content: "Rename 6 files: supervisor-spec-manager.md, realtime-supervisor-service.md, analytical-supervisor-service.md, supervisor-operators.md, supervisor-levers.md, supervisor-directory.md to their sentinel equivalents"
    status: completed
    dependencies:
      - rename-directory
  - id: update-subsystem-core
    content: "Update core subsystem files: README.md, SCOPE.md with all terminology changes (Supervisor → Sentinel, supervisor → sentinel, supervisory → sentinel, etc.)"
    status: completed
    dependencies:
      - rename-files
  - id: update-subsystem-services
    content: "Update service files: sentinel-spec-manager.md, realtime-sentinel-service.md, analytical-sentinel-service.md, observation-service.md, sentinel-operators.md, sentinel-levers.md, sentinel-directory.md with terminology and YAML/CRD name changes"
    status: completed
    dependencies:
      - rename-files
  - id: update-mermaid-diagrams
    content: "Update all mermaid diagrams across all files: node labels, subgraph labels, node IDs (AgentSessionSupervisor → AgentSessionSentinel, Supervisor Spec Manager → Sentinel Spec Manager, etc.)"
    status: completed
    dependencies:
      - update-subsystem-core
      - update-subsystem-services
  - id: update-yaml-examples
    content: "Update all YAML examples: CRD kind (SupervisorSpec → SentinelSpec), field names (supervisor_id → sentinel_id, supervisor_type → sentinel_type), comments and descriptions"
    status: completed
    dependencies:
      - update-subsystem-services
  - id: update-code-examples
    content: "Update code examples: package names (seer.supervisor.* → seer.sentinel.*), variable names, function references"
    status: completed
    dependencies:
      - update-subsystem-services
  - id: update-cross-references
    content: "Update all cross-references in other files: subsystems/README.md, implementation-concepts files, agent-health-monitor files, agent-analytics files, editorial review file - update file paths and terminology"
    status: completed
    dependencies:
      - update-subsystem-core
  - id: update-file-paths
    content: "Update all markdown links and file path references: ../agent-session-supervisor/ → ../agent-session-sentinel/, supervisor-*.md → sentinel-*.md"
    status: completed
    dependencies:
      - update-cross-references
  - id: verify-hub-persona
    content: Verify no Hub Supervisor persona references were accidentally changed - check agentic-automation-lifecycle.md and any links to hub-docs supervisor persona
    status: completed
    dependencies:
      - update-cross-references
      - update-file-paths
---

# Agent Session Supervisor to Sentinel Migration Plan

## Overview

Migrate the **Agent Session Supervisor** subsystem to **Agent Session Sentinel** to eliminate naming conflict with Hub's Supervisor persona. This affects:
- 1 directory rename
- 6 file renames within the subsystem
- 9 files in the subsystem directory (content updates)
- ~15+ files with cross-references
- CRD names, YAML examples, mermaid diagrams, and code references

## Scope

**Files to Rename:**
1. Directory: `olympus-seer-docs/seer-design/subsystems/agent-session-supervisor/` → `agent-session-sentinel/`
2. Files within directory:
   - `supervisor-spec-manager.md` → `sentinel-spec-manager.md`
   - `realtime-supervisor-service.md` → `realtime-sentinel-service.md`
   - `analytical-supervisor-service.md` → `analytical-sentinel-service.md`
   - `supervisor-operators.md` → `sentinel-operators.md`
   - `supervisor-levers.md` → `sentinel-levers.md`
   - `supervisor-directory.md` → `sentinel-directory.md`

**Content Updates Required:**

### Terminology Mapping
- "Agent Session Supervisor" → "Agent Session Sentinel"
- "Supervisor Spec Manager" → "Sentinel Spec Manager"
- "Realtime Supervisor Service" → "Realtime Sentinel Service"
- "Analytical Supervisor Service" → "Analytical Sentinel Service"
- "Supervisor Operators" → "Sentinel Operators"
- "Supervisor Levers" → "Sentinel Levers"
- "Supervisor Directory" → "Sentinel Directory"
- "SupervisorSpec" (CRD) → "SentinelSpec"
- "SupervisorSpec CRD" → "SentinelSpec CRD"
- "supervisor" (lowercase, when referring to subsystem) → "sentinel"
- "supervisors" (plural, when referring to subsystem instances) → "sentinels"
- "supervisory" (when referring to subsystem) → "sentinel" (e.g., "supervisory policies" → "sentinel policies")
- "supervision" (when referring to subsystem) → "sentinel oversight" or "sentinel monitoring"

### Files Requiring Updates

#### Subsystem Files (9 files)
1. `agent-session-sentinel/README.md` - Main subsystem overview
2. `agent-session-sentinel/SCOPE.md` - Scope document
3. `agent-session-sentinel/sentinel-spec-manager.md` - Spec manager
4. `agent-session-sentinel/realtime-sentinel-service.md` - Realtime service
5. `agent-session-sentinel/analytical-sentinel-service.md` - Analytical service
6. `agent-session-sentinel/observation-service.md` - Observation service (references supervisors)
7. `agent-session-sentinel/sentinel-operators.md` - Operators
8. `agent-session-sentinel/sentinel-levers.md` - Levers
9. `agent-session-sentinel/sentinel-directory.md` - Directory

#### Cross-Reference Files (~15+ files)
1. `seer-design/subsystems/README.md` - Subsystem index
2. `seer-design/implementation-concepts/agent-session-supervision.md` - Concept doc (may need title/content update)
3. `seer-design/implementation-concepts/agent-analytics.md` - Reference to subsystem
4. `seer-design/implementation-concepts/agent-health-slos.md` - Reference to subsystem
5. `seer-design/subsystems/agent-health-monitor/README.md` - References and mermaid diagrams
6. `seer-design/subsystems/agent-health-monitor/SCOPE.md` - Reference
7. `seer-design/subsystems/agent-health-monitor/slo-tracking-service.md` - References and mermaid diagrams
8. `seer-design/subsystems/agent-health-monitor/slo-manager.md` - References and mermaid diagrams
9. `seer-design/subsystems/agent-health-monitor/health-operators.md` - Pattern reference
10. `seer-design/subsystems/agent-analytics/README.md` - Reference
11. `seer-design/subsystems/agent-analytics/SCOPE.md` - Reference
12. `seer-design/subsystems/EDITORIAL-REVIEW-ANALYTICS-SUPERVISOR-HEALTH.md` - Editorial review (update title and content)

### Special Update Categories

#### Mermaid Diagrams
- Update node labels: `AgentSessionSupervisor` → `AgentSessionSentinel`
- Update subgraph labels: `Supervisor[Agent Session Supervisor]` → `Sentinel[Agent Session Sentinel]`
- Update node IDs: `SSM[Supervisor Spec Manager]` → `SSM[Sentinel Spec Manager]`
- Update all component references in diagrams

#### YAML Examples
- Update CRD kind: `kind: SupervisorSpec` → `kind: SentinelSpec`
- Update API version references if needed
- Update field names: `supervisor_id` → `sentinel_id`, `supervisor_type` → `sentinel_type`
- Update comments and descriptions in YAML

#### Code References
- Update variable names in code examples
- Update function/class names if present
- Update package names: `package seer.supervisor.*` → `package seer.sentinel.*`

#### File Path References
- Update all markdown links: `../agent-session-supervisor/` → `../agent-session-sentinel/`
- Update all file references: `supervisor-spec-manager.md` → `sentinel-spec-manager.md`
- Update all relative paths in cross-references

### Exclusions (DO NOT CHANGE)

**Hub Supervisor Persona References:**
- References to Hub's Supervisor persona (human role) should remain unchanged
- Example: `olympus-seer-docs/seer-design/personas-and-needs/journeys/agentic-automation-lifecycle.md` line 265 references Hub Supervisor persona - DO NOT CHANGE
- Any references linking to `olympus-hub-docs/08-personas-and-journeys/personas/supervisor.md` should remain unchanged

**Context-Based Decisions:**
- If "supervisor" appears in context clearly referring to Hub persona (e.g., "Supervisor deploys scenarios"), leave unchanged
- If "supervisor" appears in context of Seer subsystem (e.g., "supervisor observes SX events"), change to "sentinel"

## Implementation Order

1. **Rename directory and files** (preserves git history)
2. **Update subsystem files** (core content)
3. **Update cross-references** (external files)
4. **Update mermaid diagrams** (visual consistency)
5. **Update YAML/code examples** (technical accuracy)
6. **Verify no Hub persona references were changed** (safety check)

## Verification Checklist

- [ ] All file renames completed
- [ ] All markdown links updated
- [ ] All mermaid diagrams updated
- [ ] All YAML examples updated (CRD names, field names)
- [ ] All code examples updated (package names, variable names)
- [ ] No Hub Supervisor persona references changed
- [ ] All cross-references in other subsystems updated
- [ ] Editorial review document updated
- [ ] Subsystem index updated