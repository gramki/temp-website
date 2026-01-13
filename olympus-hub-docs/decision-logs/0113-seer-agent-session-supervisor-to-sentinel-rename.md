# ADR-0113: Seer Agent Session Supervisor to Sentinel Rename

**Status**: Accepted  
**Date**: 2026-01-13  
**Category**: seer

---

## Context

The Seer subsystem "Agent Session Supervisor" had a naming conflict with Hub's **Supervisor persona** (a human role that deploys scenarios, manages task queues, and oversees agent operations). As Seer is an extension to Hub, this conflict would manifest in multiple ways:

1. **Documentation Confusion** — References to "Supervisor" would be ambiguous (human role vs. automated system)
2. **API/UI Naming** — Would require disambiguation in interfaces
3. **Conceptual Clarity** — The automated monitoring system and human operational role serve different purposes
4. **Future Integration** — As Seer integrates more closely with Hub, naming conflicts would become more problematic

The Agent Session Supervisor subsystem provides automated monitoring and oversight for agent sessions—it observes events, evaluates policies, and generates observations/exceptions. This is fundamentally different from Hub's Supervisor persona, which is a human role responsible for operational management.

---

## Decision

We rename **Agent Session Supervisor** to **Agent Session Sentinel** across all seer-docs.

### Rationale for "Sentinel"

| Aspect | Rationale |
|--------|-----------|
| **Meaning** | A sentinel is a guard that keeps watch—exactly what this subsystem does |
| **Technical Precedent** | Common in systems for automated monitoring (e.g., Azure Sentinel, AWS GuardDuty's sentinel concept) |
| **No Human Confusion** | "Sentinel" strongly implies an automated, always-on watcher—not a human role |
| **Distinct from Hub** | Completely avoids the "Supervisor" terminology used for the human persona |
| **Professional Tone** | Appropriate for enterprise documentation |

### Scope of Changes

**Directory and Files:**
- Directory: `agent-session-supervisor/` → `agent-session-sentinel/`
- Files: All `supervisor-*.md` → `sentinel-*.md`

**Terminology:**
- "Agent Session Supervisor" → "Agent Session Sentinel"
- "Supervisor Spec Manager" → "Sentinel Spec Manager"
- "Realtime Supervisor Service" → "Realtime Sentinel Service"
- "Analytical Supervisor Service" → "Analytical Sentinel Service"
- "Supervisor Operators" → "Sentinel Operators"
- "Supervisor Levers" → "Sentinel Levers"
- "Supervisor Directory" → "Sentinel Directory"

**Technical Names:**
- CRD: `SupervisorSpec` → `SentinelSpec`
- CRD: `SupervisorDeployment` → `SentinelDeployment`
- Fields: `supervisor_id`, `supervisor_type` → `sentinel_id`, `sentinel_type`
- Package: `seer.supervisor.*` → `seer.sentinel.*`

**Conceptual Terms:**
- "supervisory oversight" → "sentinel oversight"
- "supervisory policies" → "sentinel policies"
- "supervisors" (subsystem instances) → "sentinels"

---

## Consequences

### Positive

1. **Eliminates Naming Conflict** — No ambiguity between Hub's Supervisor persona and Seer's automated monitoring system
2. **Clearer Conceptual Separation** — "Sentinel" clearly indicates automated monitoring vs. human operational role
3. **Better Documentation Clarity** — References to "Sentinel" are unambiguous in context
4. **Future-Proof** — Avoids conflicts as Seer integrates more closely with Hub
5. **Industry Alignment** — "Sentinel" aligns with common industry terminology for automated monitoring systems

### Negative

1. **Migration Effort** — Requires updating all documentation, code references, and cross-references
2. **Historical References** — Existing decision logs and documentation may reference old name (can be updated separately)
3. **Learning Curve** — Team members familiar with "Supervisor" need to adapt to "Sentinel"
4. **Decision Log Updates** — Existing ADRs (0111, 0112) reference old name (will be updated)

### Neutral

1. **Functionality Unchanged** — Rename is purely cosmetic; no functional changes
2. **API Compatibility** — Future implementation will use new names from start
3. **Documentation Only** — Changes are in documentation; no code changes required at this stage

---

## Alternatives Considered

### 1. Keep "Supervisor" with Disambiguation

Use "Agent Session Supervisor" but always disambiguate from Hub's Supervisor persona in documentation.

**Rejected because:**
- Requires constant disambiguation in all documentation
- Still creates confusion and ambiguity
- Doesn't solve the fundamental naming conflict
- Would require disambiguation in APIs/UI as well

### 2. Use "Agent Session Monitor"

Rename to "Agent Session Monitor" to emphasize monitoring function.

**Rejected because:**
- "Monitor" is less specific than "Sentinel"
- Doesn't convey the active oversight and policy evaluation aspects
- Less distinctive from other monitoring systems

### 3. Use "Agent Session Watchdog"

Rename to "Agent Session Watchdog" to emphasize vigilance.

**Rejected because:**
- "Watchdog" may sound informal for enterprise documentation
- Less professional tone than "Sentinel"
- "Sentinel" is more commonly used in enterprise systems

### 4. Use "Agent Behavior Observer"

Rename to emphasize observation function.

**Rejected because:**
- "Observer" is passive; subsystem is more active (evaluates policies, generates observations)
- Could overlap conceptually with Observation Service
- Less distinctive than "Sentinel"

---

## Implementation

### Migration Completed

**Files Updated (22 files):**
- 9 subsystem files (README, SCOPE, all service files)
- 13 cross-reference files (subsystem index, implementation concepts, related subsystems)

**Changes Applied:**
- Directory and file renames (using `git mv` to preserve history)
- All terminology updates
- All mermaid diagrams updated
- All YAML examples updated (CRD names, field names)
- All code examples updated (package names)
- All cross-references updated
- All file path references updated

**Verification:**
- Hub Supervisor persona references verified unchanged
- No broken links detected
- All terminology consistent

### Decision Logs to Update

The following decision logs reference the old name and will be updated separately:
- ADR-0111: Seer Agent Session Supervisor Cronus Integration
- ADR-0112: Seer Supervisor Dual-Mode Architecture

---

## Related

- [Agent Session Sentinel Subsystem](../../olympus-seer-docs/seer-design/subsystems/agent-session-sentinel/README.md) — Renamed subsystem
- [Hub Supervisor Persona](../../08-personas-and-journeys/personas/supervisor.md) — Human role (unchanged)
- [Editorial Review: Sentinel Migration](../../olympus-seer-docs/seer-design/subsystems/agent-session-sentinel/EDITORIAL-REVIEW-SENTINEL-MIGRATION.md) — Migration review
- ADR-0111: Seer Agent Session Supervisor Cronus Integration (references old name)
- ADR-0112: Seer Supervisor Dual-Mode Architecture (references old name)
