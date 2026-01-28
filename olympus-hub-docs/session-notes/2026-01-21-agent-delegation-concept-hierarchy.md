# Agent Delegation Concept Hierarchy and Documentation Refinements

**Date:** 2026-01-21  
**Scope:** Create agent delegation concept hierarchy with narrative symmetry; refine foundational beliefs; sync READMEs

---

## Summary

This session created a comprehensive agent delegation documentation hierarchy covering the unified delegation model with scenario-scoped and request-scoped modes. The work also refined foundational beliefs for readability, synced system-design READMEs with folder contents, and ensured consistency across all delegation-related documents for accountability and inheritance semantics.

---

## Objectives

1. Create umbrella `agent-delegation.md` concept covering the unified delegation model
2. Create authoritative `scenario-scoped-delegation.md` in Seer and Hub perspective
3. Update `request-scoped-delegation.md` with purpose, contrast, and cross-references
4. Ensure narrative symmetry across all delegation documents
5. Refine foundational beliefs for readability
6. Sync system-design READMEs with folder contents
7. Ensure consistency for accountability and inheritance semantics

---

## Files Created

### New Documents (3 files)

1. **`olympus-hub-docs/02-system-design/implementation-concepts/agent-delegation.md`**
   - Umbrella concept for unified delegation model
   - Contrasts enterprise delegation vs business user delegation
   - Covers both scenario-scoped and request-scoped modes
   - Includes unified token structure and component roles
   - Notes on layered accountability and eventual consistency

2. **`olympus-seer-docs/seer-design/implementation-concepts/scenario-scoped-delegation.md`**
   - Authoritative source for scenario-scoped mode
   - Purpose, contrast with other delegation types
   - Certificate lifecycle (deployment-time)
   - Employment Spec configuration examples
   - Policy composition and token placement

3. **`olympus-hub-docs/02-system-design/implementation-concepts/scenario-scoped-delegation.md`**
   - Hub perspective on scenario-scoped mode
   - Hub components involved
   - Token refresh behavior
   - ScenarioDeploymentSpec integration
   - No Channel involvement (proactive only)

---

## Files Modified

### Foundational Beliefs (1 file)

1. **`olympus-hub-docs/00-_why/foundational-beliefs.md`**
   - Simplified "Agent proliferation without governance..." belief for readability
   - Refined "natural unit of work is the situation" framing

### System Design READMEs (2 files)

2. **`olympus-hub-docs/02-system-design/README.md`**
   - Added `hub-design-philosophy.md` to Architecture Overview table
   - Updated folder structure diagram
   - Added to "For Architects" reading order

3. **`olympus-hub-docs/02-system-design/implementation-concepts/README.md`**
   - Added missing implementation concepts:
     - `hub-application-deployment.md`
     - `mcp-server.md`
     - `agent-delegation.md`
     - `scenario-scoped-delegation.md`
   - Moved `request-scoped-delegation.md` to Agent Delegation section

### Delegation Documents (4 files)

4. **`olympus-hub-docs/02-system-design/implementation-concepts/request-scoped-delegation.md`**
   - Added Purpose section with use cases
   - Added Contrast with Other Delegation Types table
   - Added Authority Sync and Accountability rows
   - Added Mode Comparison cross-references
   - Updated Related Documentation section

5. **`olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md`**
   - Added Mode Comparison reference to scenario-scoped-delegation.md

6. **`olympus-seer-docs/seer-design/implementation-concepts/delegation-chains.md`**
   - Added cross-references to scenario-scoped and request-scoped delegation

7. **`olympus-hub-docs/02-system-design/implementation-concepts/agent-delegation.md`** (post-creation update)
   - Updated inheritance: "Shrinks with delegator; eventual consistency"
   - Updated accountability: "Layered: business user (action) + enterprise (agent)"
   - Added explanatory notes for layered accountability

---

## Key Concepts Documented

### Unified Delegation Model

Two modes sharing identical token semantics:

| Mode | Certificate Source | Certificate Timing | Token Timing |
|------|-------------------|-------------------|--------------|
| Scenario-Scoped | Scenario Identity Profile | At deployment | Per-request |
| Request-Scoped | Business User (via Channel) | Per-request | Per-request |

### Delegation Document Hierarchy

```
Agent Delegation (umbrella)
├── Enterprise Delegation
│   └── Delegation Chains (Seer) ← reference only
│
└── Business User Delegation (unified model)
    ├── Scenario-Scoped Delegation
    │   ├── Seer (authoritative)
    │   └── Hub (perspective)
    │
    └── Request-Scoped Delegation
        ├── Seer (authoritative)
        └── Hub (perspective)
```

### Narrative Symmetry

Each delegation document now includes:
- **Purpose** — What need does this mode address?
- **Contrast with Other Delegation Types** — Comparison table
- **Applicability** — When to use this mode
- **Components Involved** — Hub/Seer components
- **Token/Certificate Lifecycle** — How authority flows
- **Cross-references** — Navigation to related docs

### Layered Accountability

Business user delegation has two accountability layers:
1. **Action accountability** — The delegator (business user or Scenario Profile) is accountable for actions they authorized
2. **Agent accountability** — The enterprise (via designated accountable human) is accountable for the agent's behavior

### Eventual Consistency

Both scenario-scoped and request-scoped modes exhibit eventual consistency:
- If the delegator's authority shrinks, the effective authority of the delegation shrinks accordingly
- Enterprise delegation uses real-time shrinking; business user delegation uses eventual consistency

---

## Consistency Fixes

| Document | Issue | Fix |
|----------|-------|-----|
| Hub scenario-scoped-delegation.md | Missing Authority Sync and Accountability rows | Added rows + explanatory note |
| Hub request-scoped-delegation.md | Missing Authority Sync and Accountability rows | Added rows + explanatory note |
| Hub agent-delegation.md | Inheritance and Accountability not fully explained | Updated table + added notes |

---

## Commits

| Commit | Message |
|--------|---------|
| `fb7bea4` | `docs: refine foundational-beliefs readability` |
| `be8fa39` | `docs: sync system-design READMEs with folder contents` |
| `4294f75` | `feat(docs): add agent delegation concept hierarchy` |

---

## Related ADRs

- [ADR-0127: Request-Scoped Authority Delegation](../decision-logs/0127-request-scoped-authority-delegation.md)
- [ADR-0129: Agent Identity Model](../decision-logs/0129-agent-identity-model.md)
- [ADR-0130: Unified Delegation Model](../decision-logs/0130-unified-delegation-model.md)

---

## Next Steps

- [ ] Commit consistency fixes (accountability and inheritance updates)
- [ ] Consider adding delegation examples to guides
- [ ] Review delegation-related subsystem docs for consistency
