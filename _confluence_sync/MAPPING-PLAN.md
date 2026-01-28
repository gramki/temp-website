# Title Conflict Resolution Plan

## Summary
- **Total conflicts:** 15
- **Successfully synced:** 1,065 pages
- **Folders created:** 146
- **Resolution approach:** Updated source README titles directly (no mapping files needed)

## Conflict Analysis

### Pattern 1: Hub Subsystem READMEs vs Implementation Concepts (9 conflicts)
**Root cause:** README.md files in Hub subsystems have the same title as pages in `02-system-design/implementation-concepts/` folder.

**Conflicts:**
1. `artifact-registry/README.md` → "Artifact Registry" (conflicts with implementation-concepts/artifact-registry.md)
2. `ci-subsystem/README.md` → "CI Subsystem" (conflicts with implementation-concepts/ci-subsystem.md)
3. `ci-subsystem/test-runner.md` → "Hub Test Runner" (conflicts with implementation-concepts/hub-test-runner.md)
4. `hub-native-utilities/README.md` → "Hub Native Utilities" (conflicts with implementation-concepts/hub-native-utilities.md)
5. `memory-services/README.md` → "Memory Services" (conflicts with implementation-concepts/memory-services.md)
6. `ms-teams-integration/README.md` → "MS Teams Integration" (conflicts with implementation-concepts/ms-teams-integration.md)
7. `notification-services/README.md` → "Notification Services" (conflicts with implementation-concepts/notification-services.md)
8. `signal-exchange/README.md` → "Signal Exchange" (conflicts with implementation-concepts/message-envelope.md or similar)

**Solution:** ✅ **COMPLETED** - Updated source README titles to include "(Subsystem)" suffix

### Pattern 2: Seer Subsystem READMEs vs Core Concepts (4 conflicts)
**Root cause:** README.md files in Seer subsystems have the same title as pages in `01-concepts/` folder.

**Conflicts:**
1. `agent-analytics/README.md` → "Agent Analytics" (conflicts with concepts page)
2. `agent-runtime/README.md` → "Agent Runtime" (conflicts with concepts page)
3. `cognitive-operations-governance-workbench/README.md` → "Cognitive Operations Governance Workbench" (conflicts with concepts page)
4. `seer-sidecar/README.md` → "Seer Sidecar" (conflicts with concepts page)

**Solution:** ✅ **COMPLETED** - Updated source README titles to include "(Subsystem)" suffix

### Pattern 3: Special Cases (3 conflicts)
1. **MCP Channel:** `mcp-channel/README.md` → "MCP Channel" (conflicts with `01-concepts/mcp-channel.md`)
   - **Solution:** ✅ **COMPLETED** - Updated to "MCP Channel (Subsystem)"

2. **Model Gateway:** `model-gateway/README.md` → "Model Gateway" (conflicts with another location)
   - **Solution:** ✅ **COMPLETED** - Updated to "Model Gateway (Subsystem)"

3. **Ontology Reference:** `ontology-reference-before-refactor.md` → "Ontology of Human–AI Team Operations" (conflicts with `ontology-reference.md`)
   - **Solution:** ✅ **COMPLETED** - Updated to "Ontology Reference (Before Refactor)"

## Source File Updates Required

**Approach:** Update titles directly in source README files rather than using mapping files.

### Hub Subsystems (9 files to update)
1. `olympus-hub-docs/04-subsystems/artifact-registry/README.md` - Change H1 from "Artifact Registry" to "Artifact Registry (Subsystem)"
2. `olympus-hub-docs/04-subsystems/ci-subsystem/README.md` - Change H1 from "CI Subsystem" to "CI Subsystem (Subsystem)"
3. `olympus-hub-docs/04-subsystems/ci-subsystem/test-runner.md` - Change H1 from "Hub Test Runner" to "Hub Test Runner (CI Subsystem)"
4. `olympus-hub-docs/04-subsystems/hub-native-utilities/README.md` - Change H1 to "Hub Native Utilities (Subsystem)"
5. `olympus-hub-docs/04-subsystems/memory-services/README.md` - Change H1 to "Memory Services (Subsystem)"
6. `olympus-hub-docs/04-subsystems/ms-teams-integration/README.md` - Change H1 to "MS Teams Integration (Subsystem)"
7. `olympus-hub-docs/04-subsystems/notification-services/README.md` - Change H1 to "Notification Services (Subsystem)"
8. `olympus-hub-docs/04-subsystems/signal-exchange/README.md` - Change H1 to "Signal Exchange (Subsystem)"
9. `olympus-hub-docs/04-subsystems/mcp-channel/README.md` - Change H1 to "MCP Channel (Subsystem)"

### Seer Subsystems (5 files to update)
1. `olympus-seer-docs/seer-design/subsystems/agent-analytics/README.md` - Change H1 from "Agent Analytics" to "Agent Analytics (Subsystem)"
2. `olympus-seer-docs/seer-design/subsystems/agent-runtime/README.md` - Change H1 to "Agent Runtime (Subsystem)"
3. `olympus-seer-docs/seer-design/subsystems/cognitive-operations-governance-workbench/README.md` - Change H1 to "COG Workbench (Subsystem)"
4. `olympus-seer-docs/seer-design/subsystems/seer-sidecar/README.md` - Change H1 to "Seer Sidecar (Subsystem)"
5. `olympus-seer-docs/seer-design/subsystems/model-gateway/README.md` - Change H1 to "Model Gateway (Subsystem)"

### Special Cases (1 file to update)
1. `olympus-hub-docs/01-concepts/ontology-reference-before-refactor.md` - Change H1 from "Ontology of Human–AI Team Operations" to "Ontology Reference (Before Refactor)" or consider deleting if obsolete

## Resolution Summary ✅

All 15 conflicting files have been updated with unique titles:
- **14 files** now have "(Subsystem)" suffix
- **1 file** (ontology-reference-before-refactor.md) renamed to "Ontology Reference (Before Refactor)"

### Files Updated:
- ✅ All Hub subsystem READMEs (8 files)
- ✅ All Seer subsystem READMEs (5 files)  
- ✅ CI Subsystem test-runner.md
- ✅ ontology-reference-before-refactor.md

## Next Steps
1. ✅ **COMPLETED** - Updated all source README titles
2. **TODO** - Re-run sync to verify conflicts are resolved
3. **TODO** - Verify no folders are being merged incorrectly
4. **TODO** - Verify all pages sync successfully without conflicts
