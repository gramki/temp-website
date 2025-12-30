# Appendix: Using Industry Reference Models for ETSL
## BIAN, FIBO, ISO 20022, and Beyond
### Guidance for ETSL Semantic Model Architects

---

## 1. Purpose of This Appendix

This appendix provides **practical guidance** on how ETSL Semantic Model Architects should leverage **industry reference models** while building an enterprise-specific ETSL for a bank.

It covers:
- Major industry efforts and their maturity
- How each maps to ETSL needs
- What work remains even when standards exist
- How to adapt, profile, and extend industry models safely
- How to avoid inconsistency and semantic drift over time

This appendix is intended to be read alongside:
- ETSL Ontology vs Semantic vs Data Artifacts
- ETSL Authority Modeling Guidance
- ETSL Semantic Modeling Guidance for Architects

---

## 2. Core Position (Read This First)

> **Industry models provide shared meaning.  
> ETSL provides enterprise truth.  
> They are complementary, not interchangeable.**

Most industry standards stop at **conceptual or message semantics**.  
ETSL must add:
- Truth contracts
- Authority
- Temporal validity
- Integrity and override semantics

---

## 3. Major Industry Reference Models

### 3.1 BIAN (Banking Industry Architecture Network)

**Primary focus**
- Banking capability and service landscape
- Domain decomposition
- Service boundaries and interaction patterns

**Maturity**
- High as a reference architecture
- Widely adopted by large banks for capability mapping

**Relevance to ETSL**
- Strong for:
  - Identifying semantic domains
  - Informing authority boundaries
  - Understanding ownership of truth by function
- Weak for:
  - Instance-level facts, events, and state
  - Authority, precedence, and overrides

**ETSL Usage Guidance**
- Treat BIAN as a **domain and capability map**
- Use it to:
  - Partition semantic ownership
  - Seed authority discovery
- Do not treat BIAN artifacts as ETSL semantic artifacts

---

### 3.2 FIBO (Financial Industry Business Ontology – OMG / EDMC)

**Primary focus**
- Formal ontology of financial concepts
- Legal entities, instruments, contracts, markets

**Maturity**
- High conceptual maturity
- Broad but heavy-weight
- Strong in capital markets and legal semantics

**Relevance to ETSL**
- Strong for:
  - Canonical meaning of financial instruments
  - Cross-enterprise conceptual consistency
- Weak for:
  - Operational banking states
  - Enterprise-specific lifecycle and authority

**ETSL Usage Guidance**
- Use FIBO as a **conceptual anchor**
- Map ETSL semantic types to FIBO concepts
- Add ETSL-specific:
  - Time
  - Authority
  - Invariants

---

### 3.3 ISO 20022

**Primary focus**
- Financial messaging standard
- Business Process Catalogue + Data Dictionary
- Rich underlying business model

**Maturity**
- Very high
- Operationally dominant in payments and securities

**Relevance to ETSL**
- Strong for:
  - External-facing semantics
  - Event and transaction vocabulary
  - Party, account, payment constructs
- Insufficient for:
  - Enterprise truth governance
  - Authority and overrides
  - State completeness

**ETSL Usage Guidance**
- Use ISO 20022 as:
  - Canonical external semantic vocabulary
  - Input/output boundary model
- Derive ETSL facts/events from ISO messages
- Do not equate ISO message semantics with enterprise truth

---

### 3.4 FIX / FpML (Capital Markets & Derivatives)

**Primary focus**
- Trading and derivatives semantics

**Maturity**
- Very high in their respective domains

**Relevance to ETSL**
- Highly relevant if the bank has:
  - Trading, OMS/EMS, derivatives operations
- Limited relevance for retail/core banking ETSL

**ETSL Usage Guidance**
- Anchor ETSL semantics where these standards dominate
- Treat them as upstream semantic authorities for meaning, not truth

---

### 3.5 Other Domain-Specific Models (e.g., MISMO)

**Primary focus**
- Vertical-specific data and process semantics

**Maturity**
- High within their ecosystems

**ETSL Usage Guidance**
- Adopt selectively
- Apply the same profiling and extension discipline

---

## 4. Summary: Industry Models vs ETSL Needs

| Aspect | Industry Models | ETSL |
|-----|-----------------|------|
| Purpose | Shared meaning | Enterprise truth |
| Level | Conceptual / message | Truth contracts |
| Authority | Implicit | Explicit |
| Time | Often optional | Mandatory |
| Integrity | Advisory | Enforced |
| Overrides | Rarely modeled | First-class |
| Audience | Industry-wide | Enterprise-specific |

---

## 5. What Work Still Belongs to ETSL Semantic Architects

Even with mature standards, architects must do **four essential things**.

---

### 5.1 Select Upstream Anchors by Domain

A realistic ETSL uses multiple anchors:

- ISO 20022 → payments semantics
- FIBO → instruments, legal entities
- BIAN → domain decomposition
- FIX/FpML → markets where applicable

This selection must be **explicit and documented**.

---

### 5.2 Define an Enterprise Profile

Never adopt standards wholesale.

Instead:
- Define what is adopted as-is
- Define what is constrained more tightly
- Define what is extended

This creates an **enterprise profile**, not a fork.

---

### 5.3 Translate Meaning into Truth Contracts

Industry models define *what things mean*.  
ETSL must define *what can be asserted as true*.

Architects must add:
- Authority registry
- Allowed assertions
- Precedence and overrides
- State completeness rules
- Temporal semantics

This is the irreducible ETSL value-add.

---

### 5.4 Maintain Explicit Traceability

Every ETSL Semantic Artifact should declare:
- Upstream anchor (if any)
- Version of the upstream model
- Nature of relationship:
  - adopted
  - constrained
  - extended
  - enterprise-defined

Example:
```text
ETSL.AccountStatus
  anchored_to: iso20022:AccountStatus
  profile: enterprise-constrained
```

---

## 6. Profiling and Extension Strategy (Recommended)

### 6.1 Profiles, Not Forks

- Profiles narrow or specialize meaning
- Forks diverge and accumulate debt

Always prefer profiles.

---

### 6.2 Extension Namespace Discipline

Use explicit namespaces:
- `etsl.std.*` → anchored to standards
- `etsl.ent.*` → enterprise-specific

Never mix the two implicitly.

---

## 7. Avoiding Inconsistency During ETSL Evolution

### 7.1 One-Way Semantic Influence

```
Industry Model → ETSL Semantic Model → ETSL Data
```

Reverse influence is forbidden.

---

### 7.2 Upstream Rebase Ritual

On a fixed cadence (e.g., quarterly):
- Review new versions of standards
- Decide: adopt / defer / ignore
- Record rationale

Do not silently drift.

---

### 7.3 Conformance and Linting

Automated checks should ensure:
- Anchored semantics still map correctly
- Enterprise extensions do not collide conceptually
- Deprecated anchors are flagged

---

## 8. Decision Matrix (Quick Reference)

| Need | Recommended Anchor |
|----|-------------------|
| Payments semantics | ISO 20022 |
| Banking domains | BIAN |
| Legal entities & instruments | FIBO |
| Trading & markets | FIX / FpML |
| Enterprise truth & authority | ETSL only |

---

## 9. Governance Checklist for Architects

Before approving semantic changes:
- Is the concept anchored or enterprise-defined?
- Is the anchor version recorded?
- Are extensions explicit?
- Does authority remain clear?
- Does state derivation remain deterministic?

If any answer is “no”, revise.

---

## 10. Closing Guidance

> **Industry models give you a shared language.  
ETSL gives you an enterprise constitution.**

Respect both — but never confuse their roles.

---
