---
name: Rename agent-session-sentinel to seer-sentinels
overview: Rename the `agent-session-sentinel` subsystem to `seer-sentinels` including directory rename, all file path references, and terminology updates from "Agent Session Sentinel" to "Seer Sentinels" throughout the codebase.
todos:
  - id: rename-directory
    content: "Rename directory using git mv: agent-session-sentinel/ → seer-sentinels/"
    status: completed
  - id: update-core-subsystem-files
    content: "Update all 14 files in seer-sentinels/ directory: titles, terminology, and internal references from 'Agent Session Sentinel' to 'Seer Sentinels'"
    status: completed
    dependencies:
      - rename-directory
  - id: update-main-seer-docs
    content: "Update main Seer documentation files: README.md, subsystems/README.md, and implementation-concepts/agent-session-supervision.md with new name and paths"
    status: completed
    dependencies:
      - rename-directory
  - id: update-hub-integration-docs
    content: Update hub-integration/sentinel-scenario-processing.md with new paths and terminology
    status: completed
    dependencies:
      - rename-directory
  - id: update-related-subsystems
    content: Update cross-references in cognitive-operations-governance-workbench, agent-analytics, and agent-health-monitor subsystems (9 files total)
    status: completed
    dependencies:
      - rename-directory
  - id: update-decision-logs
    content: Update 5 decision log files in olympus-hub-docs/decision-logs/ with new paths and terminology (0111, 0112, 0113, 0116, 0117)
    status: completed
    dependencies:
      - rename-directory
  - id: update-session-notes
    content: Update 2 session notes files with new paths for consistency
    status: completed
    dependencies:
      - rename-directory
  - id: update-mermaid-diagrams
    content: "Update Mermaid diagram labels in 4 files: change 'Agent Session Sentinel' to 'Seer Sentinels' in subgraph and participant labels"
    status: completed
    dependencies:
      - update-core-subsystem-files
  - id: verify-all-references
    content: Search for remaining 'agent-session-sentinel' and 'Agent Session Sentinel' references and verify all markdown links are valid
    status: completed
    dependencies:
      - update-core-subsystem-files
      - update-main-seer-docs
      - update-hub-integration-docs
      - update-related-subsystems
      - update-decision-logs
      - update-session-notes
      - update-mermaid-diagrams
---

# Full Rename: agent-session-sentinel → seer-sentinels

## Scope

This plan covers a complete rename of the subsystem from `agent-session-sentinel` to `seer-sentinels`, including:

1. Directory rename: `olympus-seer-docs/seer-design/subsystems/agent-session-sentinel/` → `seer-sentinels/`
2. All file path references (68 occurrences across documentation)
3. Terminology updates: "Agent Session Sentinel" → "Seer Sentinels" (58+ occurrences)
4. Mermaid diagram label updates
5. Cross-references in related subsystems

## Impact Summary

- **Directory**: 1 directory with 14 files (including examples subdirectory)
- **File path references**: 68 occurrences across 25+ files
- **Terminology references**: 58+ occurrences of "Agent Session Sentinel"
- **Mermaid diagrams**: 5 diagrams with `Agent Session Sentinel` labels
- **Related subsystems**: 6 subsystems with cross-references

## Implementation Steps

### Phase 1: Directory and Core Files

1. **Rename directory** using `git mv` to preserve history:

- `olympus-seer-docs/seer-design/subsystems/agent-session-sentinel/` → `seer-sentinels/`

2. **Update core subsystem files** (within renamed directory):

- `README.md` - Title, overview, architecture diagram labels
- `SCOPE.md` - Title, all references to subsystem name
- All service files (sentinel-spec-manager.md, realtime-sentinel-service.md, etc.) - Update subsystem references
- `EDITORIAL-REVIEW-SENTINEL-MIGRATION.md` - Update path references

### Phase 2: Terminology Updates

Update "Agent Session Sentinel" to "Seer Sentinels" in:

3. **Main Seer documentation**:

- `olympus-seer-docs/seer-design/README.md` - Subsystem list entry
- `olympus-seer-docs/seer-design/subsystems/README.md` - Table entry and description
- `olympus-seer-docs/seer-design/implementation-concepts/agent-session-supervision.md` - Title, all references

4. **Hub integration docs**:

- `olympus-seer-docs/seer-design/hub-integration/sentinel-scenario-processing.md` - References

5. **Related subsystems** (update cross-references):

- `cognitive-operations-governance-workbench/` (3 files)
- `agent-analytics/` (2 files)
- `agent-health-monitor/` (4 files)
- `implementation-concepts/agent-analytics.md`
- `implementation-concepts/agent-health-slos.md`

6. **Decision logs**:

- `olympus-hub-docs/decision-logs/0111-seer-supervisor-cronus-integration.md`
- `olympus-hub-docs/decision-logs/0112-seer-supervisor-dual-mode-architecture.md`
- `olympus-hub-docs/decision-logs/0113-seer-agent-session-supervisor-to-sentinel-rename.md`
- `olympus-hub-docs/decision-logs/0116-request-sentinel-type.md`
- `olympus-hub-docs/decision-logs/0117-sentinel-scenario-spec-crds.md`

7. **Session notes** (update for consistency):

- `session-notes/2026-01-14-cogw-implementation.md`
- `session-notes/2026-01-14-request-sentinel-implementation.md`

8. **Editorial reviews**:

- `olympus-seer-docs/seer-design/subsystems/EDITORIAL-REVIEW-ANALYTICS-SUPERVISOR-HEALTH.md`

### Phase 3: File Path References

Update all 68 file path references from `agent-session-sentinel/` to `seer-sentinels/`:

9. **Relative path references** (using `../agent-session-sentinel/` or `./agent-session-sentinel/`):

- Update to `../seer-sentinels/` or `./seer-sentinels/` as appropriate

10. **Absolute path references** in documentation:

 - Update all markdown links with full paths
 - Update all file path mentions in text

### Phase 4: Mermaid Diagrams

11. **Update Mermaid diagram labels**:

 - `subgraph Sentinel[Agent Session Sentinel]` → `subgraph Sentinel[Seer Sentinels]`
 - `AgentSessionSentinel[Agent Session Sentinel]` → `AgentSessionSentinel[Seer Sentinels]`
 - Files to update:
 - `seer-sentinels/README.md`
 - `agent-health-monitor/slo-manager.md`
 - `agent-health-monitor/slo-tracking-service.md`
 - `agent-health-monitor/README.md`

### Phase 5: Verification

12. **Verify all changes**:

 - Search for any remaining `agent-session-sentinel` references
 - Search for any remaining "Agent Session Sentinel" references (except in historical context)
 - Verify all markdown links are valid
 - Check that Mermaid diagrams render correctly

## Terminology Mapping

| Old Term | New Term | Context |
|----------|----------|---------|
| `agent-session-sentinel/` | `seer-sentinels/` | Directory and path references |
| "Agent Session Sentinel" | "Seer Sentinels" | Subsystem name in text |
| "Agent Session Sentinel Oversight" | "Seer Sentinels Oversight" | Implementation concept title |
| `Sentinel[Agent Session Sentinel]` | `Sentinel[Seer Sentinels]` | Mermaid diagram labels |
| `AgentSessionSentinel[Agent Session Sentinel]` | `AgentSessionSentinel[Seer Sentinels]` | Mermaid participant labels |

## Files to Update

### Core Subsystem Files (14 files)

- `seer-sentinels/README.md`
- `seer-sentinels/SCOPE.md`
- `seer-sentinels/sentinel-spec-manager.md`
- `seer-sentinels/realtime-sentinel-service.md`
- `seer-sentinels/analytical-sentinel-service.md`
- `seer-sentinels/observation-service.md`
- `seer-sentinels/sentinel-operators.md`
- `seer-sentinels/sentinel-levers.md`
- `seer-sentinels/sentinel-directory.md`
- `seer-sentinels/sentinel-scenario-normative-spec.md`
- `seer-sentinels/sentinel-scenario-automation-spec.md`
- `seer-sentinels/sentinel-scenario-deployment-spec.md`
- `seer-sentinels/EDITORIAL-REVIEW-SENTINEL-MIGRATION.md`
- `seer-sentinels/examples/request-sentinel-example.md`

### Cross-Reference Files (25+ files)

- Main READMEs and indexes
- Related subsystem documentation
- Implementation concepts
- Hub integration docs
- Decision logs
- Session notes
- Editorial reviews

## Notes

- Use `git mv` for directory rename to preserve Git history
- Keep terminology consistent: "Seer Sentinels" (plural) for the subsystem name
- Historical decision logs (ADR-0113) may retain old name in historical context, but update current references
- Verify all relative paths are correct after directory move
- Mermaid diagram syntax must use valid identifiers (no spaces in node IDs)