# Design Gap Analysis: CAF, Memory, Knowledge, and ETSL

> **Purpose:** Verify if CAF, Memory Services, Knowledge Bank, and ETSL are properly integrated into Hub's design and how they relate to AOSM.

---

## 1. Current State Summary

### 1.1 What Exists in Hub Documentation

| Component | Status | Location | Description |
|-----------|--------|----------|-------------|
| **Memory Services** | 🟡 Partial | `02-system-design/implementation-concepts/memory-services.md`, `04-subsystems/memory-services/` | Three scopes defined (Enterprise, Agent, User); four types defined (Episodic, Semantic, Preference, Procedural) |
| **CAF** | 🟡 Partial | `02-system-design/implementation-concepts/cognitive-audit-fabric.md`, `04-subsystems/cognitive-audit-fabric/` | Control plane for Memory; policy enforcement, audit logging, retention, consent |
| **Knowledge Bank** | 🔴 Stub | `04-subsystems/knowledge-services/knowledge-bank.md` | RAG infrastructure; ingress pipelines, retrieval |
| **ETSL Integration** | 🟡 Touch Points | `07-data-architecture/storage-architecture.md` | Touch points documented; not deeply integrated |

### 1.2 Memory Type Taxonomy (from Seer docs)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MEMORY TYPES (ESPP)                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  EPISODIC           SEMANTIC           PREFERENCE         PROCEDURAL        │
│  "What happened"    "What is true"     "What is liked"    "How to do"       │
│                                                                              │
│  • Events           • Stable facts      • User prefs      • Workflows       │
│  • Interactions     • Concepts          • Learned biases  • Skills          │
│  • Decisions        • Relationships     • Risk appetite   • Policies        │
│  • Outcomes         • Domain models     • Style choices   • Escalation      │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Memory Scopes (from Hub docs)

| Scope | Definition | Sharing |
|-------|------------|---------|
| **Enterprise Memory** | Organization's lived cognition | Admin-configurable cross-workbench |
| **Agent Memory** | Session-scoped memory | Session-bound; private or shared in session |
| **User Memory** | Preferences and learned behaviors | Per-user; never cross-tenant |

### 1.4 Knowledge vs Memory (from Seer docs)

| Dimension | Knowledge | Memory |
|-----------|-----------|--------|
| **Purpose** | Look up facts | Recall over time |
| **Lifetime** | Independent | Days → years |
| **Owned by** | System | Agent |
| **Mental Model** | 📚 Library | 🗒️ Notebook |

---

## 2. Mapping to AOSM Concepts

### 2.1 AOSM Capability = KSA (Knowledge, Skills, Abilities)

| AOSM Concept | Hub Implementation | Gap/Issue |
|--------------|-------------------|-----------|
| **Knowledge (K)** | Knowledge Bank + Semantic Memory | ✓ Well-defined |
| **Skills (S)** | Procedural Memory + Training Spec | 🟡 Implicit — not explicitly called "Skills" |
| **Abilities (A)** | Raw Agent capabilities | 🟡 Implicit in agent model |

### 2.2 AOSM OPD and CAF

| OPD Requirement | CAF Implementation | Gap/Issue |
|-----------------|-------------------|-----------|
| **Observability** | Audit logging, decision records | ✓ Designed |
| **Predictability** | Guardrails, policies, procedures | ✓ Designed |
| **Directability** | Kill-switch, override, escalation | 🟡 Not explicitly linked to CAF |

### 2.3 AOSM PIDA and Memory

| PIDA Stage | Memory Role | Hub Implementation |
|------------|-------------|-------------------|
| **Perception** | Episodic (what happened) | ✓ Signal → Request → Memory |
| **Interpretation** | Semantic (what is true) | ✓ Knowledge Bank + Enterprise Memory |
| **Decision** | Decision Records + Evidence | ✓ CAF + Enterprise Memory |
| **Action** | Procedural (how to do) | ✓ Procedural Memory + Tools |

---

## 3. Identified Gaps

### 3.1 ETSL Integration Not Deep

**Issue:** ETSL is described at "touch points" level but not integrated into the core Memory/Knowledge flow.

**What ETSL provides:**
- Assertions (claims about facts at points in time)
- Authority modeling (who decides what is true)
- Reconciliation (resolving multiple assertions)
- State derivation
- Data Products

**Gap:** How does ETSL relate to:
- Enterprise Memory's Semantic memories?
- Knowledge Bank's facts?
- Decision Records as assertions?

**Question:** Should Enterprise Memory's semantic facts be modeled as ETSL assertions?

### 3.2 Memory → Knowledge Promotion Not Formalized

**Issue:** The promotion path from Memory to Knowledge is mentioned but not formalized.

From `hub-enterprise-memory.md`:
```
Enterprise Memory (observed patterns)
        │
        ▼
Review & Validation (human oversight)
        │
        ▼
Enterprise Knowledge (asserted facts, policies)
```

**Gap:** What is the formal mechanism? Is this CAF-governed?

### 3.3 CAF as "Control Plane" Relationship Unclear

**Issue:** CAF is defined as control plane for Memory Services, but:
- How does it control Knowledge Bank?
- How does it integrate with ETSL's authority model?
- Is CAF the enforcement point for AOSM's OPD requirements?

### 3.4 Procedural Memory vs. SOPs/Procedures

**Issue:** Procedural Memory (agent-owned skills) vs. SOPs (organization-defined) are different.

| Type | Owner | Source | Governance |
|------|-------|--------|------------|
| **Procedural Memory** | Agent | Learned from experience | Evolving |
| **SOPs** | Organization | Authored by Process Architect | Version-controlled |

**Gap:** How are these distinguished in Hub? Can Procedural Memory override SOPs?

### 3.5 Memory Types and RASCI

**Issue:** AOSM requires clear accountability for decisions. How do Memory types support this?

| Memory Type | RASCI Role |
|-------------|------------|
| Decision Records | Captures who was Responsible, Accountable |
| Evidence Bundles | Supports audit by Accountable |
| Outcome Records | Informs future decisions |

**Gap:** Is this mapping explicit in CAF design?

---

## 4. Questions for Design Clarification

### 4.1 Memory Architecture

**Q1:** Is the four-type memory model (ESPP: Episodic, Semantic, Preference, Procedural) consistently used across Hub?
- Hub Agent Memory uses it ✓
- Enterprise Memory uses different types (Decision, Outcome, Exception, Handoff) ❓

**Q2:** Should Enterprise Memory be restructured to use ESPP types?
- Decision Records → Episodic (what happened) + Semantic (what was decided)
- Outcome Records → Episodic
- Exception History → Episodic + Procedural (how exceptions are handled)

### 4.2 ETSL Integration

**Q3:** Should Enterprise Memory Semantic facts be ETSL assertions?
- ETSL provides authority and reconciliation
- Enterprise Memory is Workbench-scoped
- Conflict: How do cross-workbench assertions work?

**Q4:** Should Decision Records be ETSL assertions?
- Decisions are claims about what was decided
- ETSL models authority explicitly
- This would enable enterprise-wide decision visibility

### 4.3 CAF Scope

**Q5:** Should CAF govern Knowledge Bank, not just Memory Services?
- Knowledge is authoritative information
- Knowledge has access control, versioning, consent requirements
- Current docs show CAF → Memory, but not CAF → Knowledge

**Q6:** Should CAF explicitly implement AOSM OPD requirements?
- CAF already does Observability (audit)
- CAF could encode Predictability (behavior contracts)
- CAF could manage Directability (override policies)

### 4.4 Knowledge Bank

**Q7:** Where does Procedural Knowledge live?
- SOPs in Knowledge Bank?
- Workflows in Rhea?
- Procedures in Training Spec?
- All three need to be reconciled

**Q8:** How does Knowledge Bank relate to Training Spec's Knowledge component?
- Training Spec references Knowledge Bases
- But Knowledge Bank is Workbench-scoped, Training Spec is agent-scoped

---

## 5. Design Recommendations

### 5.1 Unify Memory Taxonomy

**Recommendation:** Use ESPP (Episodic, Semantic, Preference, Procedural) consistently across all memory types.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    UNIFIED MEMORY MODEL                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SCOPE          │  EPISODIC      │  SEMANTIC     │  PREFERENCE │ PROCEDURAL │
│  ──────────────────────────────────────────────────────────────────────────  │
│  Enterprise     │  Decision Rec  │  Learned Facts│  Org Style  │  SOPs      │
│                 │  Outcome Rec   │  Patterns     │             │  Playbooks │
│                 │  Exception Rec │               │             │            │
│  ──────────────────────────────────────────────────────────────────────────  │
│  Agent          │  Interactions  │  Context Facts│  Tone/Style │  Skills    │
│  (Session)      │  Tool Calls    │  Entity Data  │             │  Workflows │
│  ──────────────────────────────────────────────────────────────────────────  │
│  User           │  History       │  Profile Facts│  User Prefs │  Custom    │
│                 │                │               │             │  Workflows │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Formalize CAF as OPD Control Plane

**Recommendation:** Explicitly position CAF as the implementation of AOSM OPD requirements.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CAF as OPD Control Plane                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  OBSERVABILITY                                                               │
│  • Decision Records catalog                                                  │
│  • Evidence Bundles catalog                                                  │
│  • Audit logging                                                             │
│  • Explanation Service                                                       │
│                                                                              │
│  PREDICTABILITY                                                              │
│  • Behavior contracts (guardrails)                                           │
│  • Policy enforcement                                                        │
│  • Procedural memory governance                                              │
│                                                                              │
│  DIRECTABILITY                                                               │
│  • Override policies                                                         │
│  • Kill-switch mechanisms                                                    │
│  • Escalation rules                                                          │
│  • Consent management                                                        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 5.3 Clarify ETSL Integration Pattern

**Recommendation:** Define explicit integration points:

```
Enterprise Memory             ETSL
      │                         │
      │ Semantic Facts ─────────▶ Assertions (Workbench authority)
      │                         │
      │ Decision Records ───────▶ Decision Assertions
      │                         │
      └── Data Products ◀───────┴── Reconciled State
```

### 5.4 Extend CAF to Knowledge Bank

**Recommendation:** CAF should govern both Memory and Knowledge:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COGNITIVE AUDIT FABRIC                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│              ┌─────────────────────┐                                         │
│              │    CAF Control      │                                         │
│              │       Plane         │                                         │
│              └──────────┬──────────┘                                         │
│                         │                                                    │
│         ┌───────────────┴───────────────┐                                   │
│         │                               │                                    │
│         ▼                               ▼                                    │
│  ┌─────────────────┐           ┌─────────────────┐                          │
│  │ Memory Services │           │ Knowledge Bank  │                          │
│  │                 │           │                 │                          │
│  │ - Enterprise    │           │ - SOPs          │                          │
│  │ - Agent         │           │ - Policies      │                          │
│  │ - User          │           │ - Reference     │                          │
│  └─────────────────┘           └─────────────────┘                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Next Steps

1. **Validate gaps** with stakeholders — Are these real gaps or intentional design choices?
2. **Decide on ETSL integration depth** — Touch points vs. deep integration
3. **Clarify CAF scope** — Memory only vs. Memory + Knowledge
4. **Update Memory taxonomy** — Unified ESPP or keep separate models
5. **Document AOSM mapping** — Explicit KSA and OPD mapping

---

## 7. Impact on Journal Paper

If these gaps exist, the paper should:

1. **Acknowledge** that Hub's memory/knowledge architecture is evolving
2. **Propose** the unified model as contribution
3. **Position** CAF as OPD implementation
4. **Discuss** ETSL as enterprise truth layer (future scope)

Alternatively, if gaps are addressed:

1. **Document** the complete memory architecture
2. **Map** explicitly to AOSM KSA and OPD
3. **Present** as mature implementation

---

*Awaiting your input on which gaps are real vs. design choices.*



