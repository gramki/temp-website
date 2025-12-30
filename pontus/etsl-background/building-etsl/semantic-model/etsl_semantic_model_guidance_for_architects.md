# ETSL Guidance for Semantic Model Architects  
## Designing Semantic Models That Can Be Reliably Enforced

---

## 1. Purpose of This Document

This document provides **guidance for ETSL Semantic Model Architects** on how to design semantic models that are:

- Enforceable in data engineering pipelines
- Stable over time
- Auditable and regulator-defensible
- Evolvable without semantic drift

It complements the [engineer-focused document on asserting semantics in pipelines](./etsl_semantic_model_assertion_guidance_for_data_engineers.md) and focuses on **what architects must encode (and avoid)** so that enforcement is possible and meaningful.

---

## 2. The Architect’s Prime Responsibility

> **Semantic Model Architects define the constitutional rules of enterprise truth.**

Your work determines:
- What can be asserted as true
- What constitutes integrity
- What violations mean
- Where authority lies

If a semantic expectation cannot be enforced or audited, it is incomplete.

---

## 3. What Semantic Models Must Enable (Hard Requirements)

Every ETSL Semantic Model must enable:

1. **Mechanical translation** into executable assertions  
2. **Unambiguous interpretation** by engineers  
3. **Deterministic enforcement** at scale  
4. **Audit and explanation** without code archaeology  

If any of these fail, the model is not production-grade.

---

## 4. Design Principles for Enforceable Semantics

### 4.1 Be Normative, Not Descriptive

Avoid language like:
- “Typically”
- “Usually”
- “In most cases”

Instead use:
- MUST
- MUST NOT
- REQUIRED
- ALLOWED

Semantics are contracts, not commentary.

---

### 4.2 Encode Constraints Explicitly

Do not rely on implied understanding.

Bad:
```text
An account has an owner.
```

Good:
```text
Each Account MUST have exactly one active OWNS relationship at any point in time.
```

Explicit constraints enable enforcement.

---

### 4.3 Treat Time as First-Class

Every semantic construct must answer:
- When does it become true?
- When does it cease to be true?

Avoid timeless assertions unless truly immutable.

Time-free semantics cannot be audited.

---

### 4.4 Separate Meaning from Enforcement Strategy

Semantic models define **what must hold**, not **how it is checked**.

Avoid:
- SQL-like phrasing
- Implementation hints
- Pipeline assumptions

This preserves portability and longevity.

---

## 5. Designing Semantic Artifacts for Compilation

### 5.1 Use Structured, Declarative Formats

Recommended characteristics:
- YAML or equivalent
- No executable logic
- No loops or conditionals
- Strong typing via semantic types

The model should be parseable by tooling and reviewable by humans.

---

### 5.2 Canonical Semantic Artifact Template (Architect View)

```yaml
artifact_type: etsl_semantic_state
entity: Account
version: 1.0

description: >
  Authoritative state of a financial account.

keys:
  - account_id

attributes:
  account_id:
    semantic_type: AccountId
    required: true

  status:
    semantic_type: AccountStatus
    required: true
    allowed_values: [OPEN, FROZEN, CLOSED]

relationships:
  - name: OWNS
    from: Party
    to: Account
    cardinality: exactly_one_active
    temporal: true

invariants:
  - name: account_must_have_owner
    rule: Account MUST have exactly one active OWNS relationship.

authority:
  asserted_by: [CoreBanking]

temporal:
  effective_from_required: true
```

Architects own:
- Completeness
- Clarity
- Enforceability

---

## 6. Designing Semantic Types (Critical and Often Missed)

Semantic types are not data types.

Example:
- `MoneyAmount`
- `AccountId`
- `LegalEntityId`

They:
- Encode meaning
- Enable consistent enforcement
- Prevent accidental misuse

Avoid leaking physical types (`string`, `int`) into semantics.

---

## 7. Common Architect Anti-Patterns

### 7.1 “We’ll Let Engineering Handle That”

If a constraint matters semantically, it must appear in the model.

Unmodeled semantics always leak into code.

---

### 7.2 Overloading Relationships

Using one relationship to mean multiple things signals semantic debt.

Prefer:
- Precise relationship types
- Explicit evolution

---

### 7.3 Encoding Business Logic as Semantics

Semantic models define **truth conditions**, not **process logic**.

Avoid:
- Workflow steps
- Procedural descriptions
- Decision trees

---

## 8. Designing for Evolution (Without Drift)

### 8.1 Version Semantic Artifacts Explicitly

- Version numbers are mandatory
- Changes must be classified:
  - additive
  - breaking
  - clarifying

Never silently change meaning.

---

### 8.2 Prefer Additive Evolution

- Add new relationship types
- Add new semantic types
- Add new invariants cautiously

Avoid mutating existing semantics.

---

### 8.3 Use Friction as a Signal

Repeated engineering friction indicates:
- Missing semantic clarity
- Under-specified constraints
- Ontology gaps

Treat friction as feedback, not resistance.

---

## 9. Architect ↔ Engineer Interaction Model

### 9.1 Design-Time Collaboration

Before approval:
- Engineers validate enforceability
- Architects validate semantic intent

This avoids late surprises.

---

### 9.2 Runtime Feedback Loop

When invariants fail:
- Engineers report violations
- Architects decide:
  - data error
  - pipeline error
  - semantic change

Semantics evolve slowly; data moves fast.

---

## 10. Governance Rituals Architects Must Lead

1. **Semantic Design Review**
2. **Semantic Change Review**
3. **Quarterly Semantic Health Check**
4. **Cross-Domain Alignment Review**

Without rituals, ETSL degrades.

---

## 11. Validation Checklist for Architects

Before approving a semantic artifact:

- Is every constraint explicit?
- Is time modeled where required?
- Can this be enforced mechanically?
- Can violations be explained?
- Can this survive platform changes?

If any answer is “no”, revise.

---

## 12. Final Guidance

> **If semantics are vague, enforcement will be arbitrary.  
> If semantics are precise, enforcement becomes mechanical.**

That is the architect’s leverage.

---

## 13. Closing Note

Semantic Model Architects are not documenting systems —  
they are defining the *conditions under which enterprise truth exists*.

Design accordingly.

---
