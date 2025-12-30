# ETSL Guidance for Semantic Model Architects  
## Designing Semantic Models That Can Be Reliably Enforced

---

## 1. Purpose of This Document

This document provides **guidance for ETSL Semantic Model Architects** on how to design semantic models that are:

- Enforceable in data engineering pipelines
- Stable over time
- Auditable and regulator-defensible
- Evolvable without semantic drift

It complements the [engineer-focused document on asserting semantics in pipelines](./etsl-semantic-model-assertion-guidance-for-engineers.md) and focuses on **what architects must encode (and avoid)** so that enforcement is possible and meaningful.

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

## 8. ETSL Versioning and Evolution

ETSL Semantic Artifacts are long-lived enterprise assets. Unlike application code, they cannot be refactored freely—downstream Data Products, operational systems, and audit trails depend on semantic stability.

This section provides comprehensive guidance on versioning, evolving, and deprecating ETSL Semantic Artifacts.

---

### 8.1 Versioning Scheme (Mandatory)

All ETSL Semantic Artifacts MUST carry an explicit version using **semantic versioning**:

```
MAJOR.MINOR.PATCH
```

| Component | When to Increment | Example |
|-----------|-------------------|---------|
| **MAJOR** | Breaking change to semantics | Removing an attribute, changing cardinality from `exactly_one` to `zero_or_more` |
| **MINOR** | Additive, backward-compatible change | New optional attribute, new relationship type, new allowed value |
| **PATCH** | Clarification, documentation, typo fix | Improving description, fixing example |

**Example:**

```yaml
artifact_type: etsl_semantic_state
entity: Account
version: 2.3.1  # MAJOR.MINOR.PATCH
```

---

### 8.2 Change Classification (Required for All Changes)

Every change to a Semantic Artifact MUST be classified:

| Classification | Definition | Review Required | Consumer Impact |
|----------------|------------|-----------------|-----------------|
| **Breaking** | Changes meaning, removes capability, or invalidates existing data | Mandatory architectural review | Consumers MUST update |
| **Additive** | Adds new capability without changing existing semantics | Standard review | Consumers MAY adopt |
| **Clarifying** | Improves documentation without changing behavior | Lightweight review | No consumer impact |

**Breaking changes include:**
- Removing an attribute or relationship
- Changing an attribute from optional to required
- Changing cardinality constraints
- Renaming semantic types
- Changing invariant logic
- Changing authority assignments

**Additive changes include:**
- Adding optional attributes
- Adding new allowed values to enumerations
- Adding new relationship types
- Adding new invariants (with caution—see below)

---

### 8.3 The Invariant Evolution Problem

Adding a new invariant is technically additive but **semantically dangerous**.

A new invariant may:
- Retroactively invalidate existing data
- Cause reconciliation failures for in-flight assertions
- Break Data Products that assumed the prior constraint set

**Guidance:**
- New invariants SHOULD be introduced as **warnings** before becoming **errors**
- Allow a grace period for data remediation
- Document the effective date when the invariant becomes enforced

---

### 8.4 Deprecation Lifecycle

Semantic constructs (attributes, relationships, invariants) follow a deprecation lifecycle:

```
ACTIVE → DEPRECATED → REMOVED
```

| Stage | Meaning | Duration |
|-------|---------|----------|
| **ACTIVE** | In use, fully supported | Indefinite |
| **DEPRECATED** | Still valid, but discouraged; consumers should migrate | Minimum 2 release cycles or 90 days |
| **REMOVED** | No longer valid; assertions using this construct fail | After deprecation period |

**In the Semantic Artifact:**

```yaml
attributes:
  legacy_account_type:
    semantic_type: AccountTypeCode
    deprecated: true
    deprecated_since: 2.0.0
    removal_planned: 3.0.0
    migration_guidance: "Use account_classification instead"
```

---

### 8.5 Handling Breaking Changes in Production

When a breaking change is unavoidable:

1. **Announce early** — Communicate to all known consumers with timeline
2. **Provide migration path** — Document how consumers should adapt
3. **Support dual versions** — Run old and new versions in parallel during transition
4. **Set a sunset date** — The old version has an explicit end-of-life
5. **Validate before cutover** — Ensure all consumers have migrated

**Dual-version pattern:**

```yaml
# v2 artifact (new)
artifact_type: etsl_semantic_state
entity: Account
version: 2.0.0
supersedes: 1.5.0

# v1 artifact (deprecated)
artifact_type: etsl_semantic_state
entity: Account
version: 1.5.0
deprecated: true
sunset_date: 2025-06-30
```

---

### 8.6 How Data Products Handle Semantic Evolution

Data Products consuming ETSL Data Artifacts must declare:

1. **Which semantic version they depend on**
2. **Whether they tolerate minor/patch updates automatically**
3. **How they handle deprecated constructs**

**Consumer declaration pattern:**

```yaml
data_product: CustomerExposureDashboard
etsl_dependencies:
  - artifact: Account
    version: "^2.0.0"  # Compatible with 2.x.x
    tolerance: minor   # Auto-accept minor updates
  - artifact: Party
    version: "1.5.0"   # Pinned to exact version
    tolerance: none
```

**Tolerance levels:**
- `none` — Exact version match required
- `patch` — Accept patch updates (2.0.0 → 2.0.1)
- `minor` — Accept minor updates (2.0.0 → 2.1.0)
- `major` — Accept any version (not recommended for production)

---

### 8.7 Version Registry and Discovery

Enterprises SHOULD maintain a **Semantic Artifact Registry** that:

- Catalogs all published semantic versions
- Tracks which consumers depend on which versions
- Alerts consumers when deprecation or breaking changes are planned
- Provides diff views between versions

This registry is analogous to a package registry for semantic contracts.

---

### 8.8 Evolution Anti-Patterns

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| **Silent semantic changes** | Consumers discover breakage in production |
| **Removing deprecated constructs without warning** | No migration path for consumers |
| **Changing meaning without version bump** | Audit trails become unreliable |
| **Overloading existing constructs** | "Account status" starts meaning different things |
| **Versioning too aggressively** | Consumer fatigue; no one keeps up |
| **Never deprecating** | Semantic debt accumulates indefinitely |

---

### 8.9 Governance for Semantic Evolution

| Activity | Frequency | Owner |
|----------|-----------|-------|
| **Semantic change request review** | Per change | Semantic Model Architect |
| **Breaking change approval** | Per change | Architecture Review Board |
| **Deprecation announcement** | Per deprecation | Semantic Model Architect |
| **Quarterly semantic health review** | Quarterly | Cross-domain governance |
| **Annual semantic debt assessment** | Annually | Enterprise Architecture |

---

### 8.10 Evolution Checklist

Before releasing a semantic change:

- [ ] Version number updated correctly (MAJOR/MINOR/PATCH)
- [ ] Change classification documented (breaking/additive/clarifying)
- [ ] Deprecation annotations added where applicable
- [ ] Migration guidance provided for breaking changes
- [ ] Consumer impact assessed and communicated
- [ ] Sunset date set for deprecated constructs
- [ ] Registry updated with new version

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

Before approving a Semantic Artifact:

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
