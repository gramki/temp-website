# Why Seer? Writing Plan Summary

**Date:** 2026-01-17  
**Review Scope:** Content changes, decisions, subsystems since last edit (2026-01-15)

---

## Executive Summary

After reviewing recent ADRs and design decisions, **3 critical gaps** and **5 enhancement opportunities** have been identified in the Why Seer? outline.

**Overall Status:** ✅ Good coverage of most recent work, but missing 3 important topics

---

## Critical Gaps (Must Add)

### 1. Request-Scoped Authority Delegation (HIGH PRIORITY)
- **Status:** ❌ NOT COVERED
- **ADR:** 0127 (2026-01-17)
- **Where:** Add Section 8.6 to Part 2
- **Why Critical:** Explains how business users (customers, end-users) delegate authority to agents — completely different from enterprise delegation
- **Tasks:** 6 writing tasks

### 2. Agent Identity Model (HIGH PRIORITY)
- **Status:** ⚠️ PARTIALLY COVERED
- **ADR:** 0129 (2026-01-17)
- **Where:** Enhance Section 8.1 and 8.2
- **Why Critical:** Clarifies two-layer identity model (Deployment Identity vs Agent Persona) — fundamental concept
- **Tasks:** 3 writing tasks

### 3. MCP Server CRD Design (HIGH PRIORITY)
- **Status:** ❌ NOT COVERED
- **ADR:** 0131 (2026-01-17)
- **Where:** Add Section 23.4 to Part 2
- **Why Critical:** Explains multi-server-per-workbench capability and template-based persona inference
- **Tasks:** 5 writing tasks

---

## Enhancements Needed (Should Add)

### 4. Composite Routing Table Schema
- **Status:** ⚠️ Technical detail missing
- **ADR:** 0126 (2026-01-15)
- **Where:** Enhance Section 22.3
- **Priority:** MEDIUM
- **Tasks:** 1 writing task

### 5. Section 5.9 Multi-Agent Coordination
- **Status:** ⚠️ Missing composite application requirement
- **Where:** Add to Section 5.9
- **Priority:** MEDIUM
- **Tasks:** 1 writing task

### 6-8. Optional Enhancements (LOW PRIORITY)
- Request Sentinel enrollment details (Section 19.1)
- COGW signal forwarding details (Section 19.5)
- Persona Twin Blueprint structure (Section 21.2)

---

## What's Already Covered ✅

- ✅ Hub Composite Applications (Section 22)
- ✅ Request Sentinels (Section 19.1)
- ✅ COGW Workbench Type (Section 19.5)
- ✅ Persona Twins (Section 21)
- ✅ All sections from 2026-01-15 update

---

## Execution Plan

### Phase 1: Critical Gaps (Week 1)
1. Request-Scoped Authority Delegation (6 tasks)
2. Agent Identity Model updates (3 tasks)
3. MCP Server CRD (5 tasks)

**Total:** 14 high-priority tasks

### Phase 2: Enhancements (Week 2)
1. Composite Routing details (1 task)
2. Section 5.9 update (1 task)
3. Cross-reference validation (1 task)

**Total:** 3 medium-priority tasks

### Phase 3: Optional (Week 3)
1. Request Sentinel details (1 task)
2. COGW details (1 task)
3. Persona Twin Blueprint details (1 task)

**Total:** 3 low-priority tasks

---

## Total Work

- **High Priority:** 14 tasks
- **Medium Priority:** 3 tasks
- **Low Priority:** 3 tasks
- **Review:** 1 task
- **Grand Total:** 21 tasks

---

## Key ADRs Reviewed

| ADR | Topic | Status |
|-----|-------|--------|
| 0125 | Hub Composite Applications | ✅ Covered |
| 0126 | Composite Routing Table | ⚠️ Needs mention |
| 0116 | Request Sentinel Type | ✅ Covered (could enhance) |
| 0118 | COGW Workbench Type | ✅ Covered (could enhance) |
| 0121 | Persona Twin Blueprints | ✅ Covered (could enhance) |
| **0131** | **MCP Server CRD** | ❌ **NOT COVERED** |
| **0127** | **Request-Scoped Delegation** | ❌ **NOT COVERED** |
| **0129** | **Agent Identity Model** | ⚠️ **NEEDS ENHANCEMENT** |

---

## Next Steps

1. **Review this summary** and approve priorities
2. **Begin Phase 1** with Request-Scoped Authority Delegation
3. **Track progress** in `writing-plan-2026-01-17.md`

---

**Full Details:** See `writing-plan-2026-01-17.md` for complete task breakdown, dependencies, and quality checklist.
