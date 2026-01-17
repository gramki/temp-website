# Session Notes: Agent Identity Model Clarification

**Date:** 2026-01-17  
**Session Type:** Design Clarification, Documentation Updates & Editorial Review  
**Status:** ✅ Complete

---

## Session Overview

This session resolved a foundational ambiguity in agent identity documentation by clarifying the **two-layer identity model** (Deployment Identity vs Agent Persona) and unifying scenario-scoped and request-scoped delegation as modes of the same mechanism. The work included consolidating design decisions, creating 2 ADRs, updating 15 documentation files across Hub and Seer, and performing comprehensive editorial review.

---

## Objectives

1. ✅ Consolidate confirmed design decisions (hybrid token, sub-personas)
2. ✅ Create ADR-0129: Agent Identity Model (Deployment vs Persona)
3. ✅ Create ADR-0130: Unified Delegation Model (scenario/request modes)
4. ✅ Update Seer design docs with two-layer identity model
5. ✅ Update Hub design docs with identity layers
6. ✅ Update request-scoped delegation doc with scenario-scoped mode
7. ✅ Update Hub Agent vs Seer Agent doc with refined identity model
8. ✅ Perform comprehensive editorial review

---

## Key Design Concepts

### The Problem

The documentation conflated two distinct identities:
1. **Deployment Identity (SPIFFE ID)**: Infrastructure-level, identifies the running pod/container
2. **Agent Persona**: Business-level identity derived from Scenario, identifies "who this agent is" in business terms

This conflation created confusion about:
- What identity is used for what purpose
- Where authority comes from
- How delegation works in different models
- How tokens should be structured

### The Solution: Two-Layer Identity Model

**Deployment Identity (SPIFFE ID)**:
- Infrastructure-level identity of the running agent pod
- **OAuth Client equivalent** — proves "this request is coming from this specific agent deployment"
- Used for: mTLS, service mesh authentication
- Provisioned by: SPIRE Agent during pod startup
- Lifetime: Tied to deployment lifecycle (created on deploy, rotated hourly, revoked on undeploy)

**Agent Persona**:
- Business-level identity derived from Scenario
- Represents "who is accountable for this action" in business terms
- Carried in **Delegation Access Tokens** (`sub` claim)
- Stored in: Cipher IAM (Scenario references it)
- Lifetime: Tied to Scenario lifecycle (survives redeployments)

### Unified Delegation Model

**Key Insight**: Scenario-scoped and request-scoped delegation use the **same mechanism** with different modes:

| Aspect | Scenario-Scoped Mode | Request-Scoped Mode |
|--------|---------------------|---------------------|
| **Certificate Source** | Scenario Identity Profile | Business User (via Channel) |
| **Certificate Timing** | Created at deployment | Created per-request |
| **Token Timing** | Per-request (from Certificate) | Per-request (from Certificate) |
| **Token Semantics** | Identical | Identical |
| **Token Structure** | Identical (`client_id`, `sub`, `delegated_by`) | Identical |

**Hybrid Token Issuance**: Both modes use same pattern — Certificate at source time, Token always per-request.

### Composite Application Sub-Personas

Each agent in a Composite Application gets its own **sub-persona**:
- Example: `dispute-analyst-agent`, `dispute-reviewer-agent`, `dispute-approver-agent`
- All derive from the same base Agent Persona (from Scenario)
- Each has distinct Deployment Identity (SPIFFE ID)
- Each receives different Delegation Access Tokens

---

## Key Decisions Confirmed

| Decision | Rationale |
|----------|-----------|
| **SPIFFE ID = OAuth Client** | Deployment is the "client" presenting tokens on behalf of principals |
| **Agent Persona = Business Identity** | Scenario-derived, carried in tokens, used for audit and authorization |
| **Token includes both identities** | `client_id` (SPIFFE) + `sub` (Persona) + `delegated_by` |
| **One deployment, multiple personas** | Via different Delegation Access Tokens per request |
| **One persona, multiple deployments** | For scaling (multiple pods) |
| **Unified delegation model** | Same mechanism, different modes (scenario-scoped vs request-scoped) |
| **Hybrid token issuance** | Certificate at source, Token always per-request |
| **Sub-personas for composites** | Each agent gets distinct sub-persona, all from same base persona |

---

## Work Completed

### Phase 0: Scratchpad Consolidation
- ✅ Added confirmed decisions (hybrid token, sub-personas)
- ✅ Removed answered questions and converted to confirmed decisions
- ✅ Added Composite Application sub-persona model diagram
- ✅ Updated status to RESOLVED

### Phase 1: Foundation (ADRs)
- ✅ **ADR-0129**: Agent Identity Model (Deployment vs Persona)
  - Two-layer identity model decision
  - SPIFFE ID = OAuth Client equivalent
  - Agent Persona = Business identity
  - Token structure includes both identities
- ✅ **ADR-0130**: Unified Delegation Model (scenario/request modes)
  - Same mechanism, different modes
  - Hybrid token issuance pattern
  - Employment Spec structure

### Phase 2: Seer Design Documentation (7 files)
1. ✅ `agent-identity-credentials.md` — Added two-layer identity model section
2. ✅ `agent-lifecycle.md` — Clarified identity layers in Employed Agent section
3. ✅ `cipher-iam-extensions/architecture.md` — Added two-layer identity model section
4. ✅ `profile-tags.md` — Added persona vs deployment tags, scenario-persona tag
5. ✅ `employment-spec-crd.md` — Updated with unified delegation model notes
6. ✅ `request-scoped-delegation.md` — Added scenario-scoped mode section, updated OAuth analogy
7. ✅ `authority-delegation.md` — Added delegation modes section

### Phase 3: Hub Design Documentation (3 files)
1. ✅ `agent-model.md` — Added identity layers section to AI Agent IAM
2. ✅ `scenario-as-agent.md` — Added identity model section
3. ✅ `cipher-iam-infrastructure.md` — Added agent identity model section

### Phase 4: Dependent Documentation (2 files)
1. ✅ `0WIP-hub-agent-vs-seer-agent.md` — Updated identity model differences section
2. ✅ `0WIP-agent-identity-ambiguity-resolution.md` — Finalized with ADR references, marked RESOLVED

### Phase 5: Cross-Cutting Updates (3 files)
1. ✅ `delegation-chains.md` — Added identity layers and delegation modes references
2. ✅ `agent-lifecycle-service.md` — Clarified two identity layers
3. ✅ `why-seer/03-1-agent-identity.md` — Updated identity layers section with two-layer model

### Editorial Review
- ✅ Comprehensive review performed
- ✅ All links verified
- ✅ Terminology consistency checked
- ✅ No blocking issues found
- ✅ Review document created: `EDITORIAL-REVIEW-2026-01-17-agent-identity.md`

---

## Statistics

| Metric | Count |
|--------|-------|
| **New ADRs** | 2 |
| **Updated Seer Docs** | 7 |
| **Updated Hub Docs** | 3 |
| **Updated Scratchpads** | 2 |
| **Cross-Cutting Updates** | 3 |
| **Total Files Changed** | 17 |
| **Lines Added** | ~1,200+ |
| **Linting Errors** | 0 |
| **Broken Links** | 0 |

---

## Key Terminology Established

| Term | Definition |
|------|------------|
| **Deployment Identity** | SPIFFE-based cryptographic identity of the running agent pod; OAuth Client equivalent |
| **Agent Persona** | Business identity derived from Scenario; represents "who" the agent is |
| **Delegation Access Token** | Per-request token carrying both persona context and delegated authority |
| **Scenario-Scoped Delegation** | Mode where authority derives from Scenario Identity Profile |
| **Request-Scoped Delegation** | Mode where authority derives from Business User consent |
| **Unified Delegation Model** | Single mechanism with two modes, same token semantics |
| **Hybrid Token Issuance** | Certificate at source time, Token always per-request |
| **Sub-Persona** | Distinct persona for each agent in Composite Applications |

---

## Design Critique Summary

From the scratchpad document, key concerns identified:

### High Priority
- **Identity Federation Complexity**: Managing two identity domains (Enterprise + Business User) requires careful federation
- **Token Lifecycle Management**: Per-request tokens require efficient refresh and revocation mechanisms

### Medium Priority
- **Composite Application Coordination**: Multiple sub-personas need clear coordination patterns
- **Delegation Chain Tracking**: Must track both Deployment Identity and Agent Persona in audit trails

### Low Priority
- **Performance**: Token issuance overhead per-request
- **Debugging**: Two identities may complicate troubleshooting

---

## Related Documentation

### ADRs Created
- [ADR-0129: Agent Identity Model](../../olympus-hub-docs/decision-logs/0129-agent-identity-model.md)
- [ADR-0130: Unified Delegation Model](../../olympus-hub-docs/decision-logs/0130-unified-delegation-model.md)

### Key Documents Updated
- [Agent Identity & Credentials](../../olympus-seer-docs/seer-design/implementation-concepts/agent-identity-credentials.md)
- [Request-Scoped Authority Delegation](../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)
- [Agent Model](../../olympus-hub-docs/02-system-design/agent-model.md)
- [Scenario as Agent](../../olympus-hub-docs/02-system-design/implementation-concepts/scenario-as-agent.md)

### Scratchpads
- [Agent Identity Ambiguity Resolution](../../olympus-hub-docs/scratchpad/0WIP-agent-identity-ambiguity-resolution.md) — ✅ RESOLVED
- [Hub Agent vs Seer Agent](../../olympus-hub-docs/scratchpad/0WIP-hub-agent-vs-seer-agent.md) — Updated with refined identity model

---

## Follow-Up Actions

### Immediate
- ✅ All documentation updates completed
- ✅ Editorial review completed
- ✅ Ready for commit

### Future Enhancements (Optional)
1. Consider updating `agent-identity-credentials.md` "Last Updated" date
2. Add side-by-side token comparison examples (scenario-scoped vs request-scoped)
3. Expand Composite Application sub-persona examples with detailed token flows

---

## Session Outcomes

**Problem Resolved**: ✅ The identity ambiguity has been fully resolved with clear two-layer model documented.

**Documentation Quality**: ✅ All changes meet quality standards, maintain consistency, and align with existing patterns.

**Architectural Clarity**: ✅ The unified delegation model provides clear guidance for implementation.

**Ready for Implementation**: ✅ All design decisions documented and ready for development teams.

---

## Lessons Learned

1. **Foundational Issues First**: Resolving identity ambiguity was critical before proceeding with Hub Agent vs Seer Agent documentation
2. **Unified Models Reduce Complexity**: Treating scenario-scoped and request-scoped as modes of the same mechanism simplifies both documentation and implementation
3. **OAuth Analogy is Powerful**: The "Agent as OAuth Client" analogy provides clear mental model for developers
4. **Two-Layer Identity Enables Flexibility**: Separation of deployment and persona identity enables powerful deployment patterns (one deployment, multiple personas)

---

*Session completed successfully. All documentation changes are production-ready.*
