# ETSL Guidance for Engineers  
## Asserting Semantic Models in Data Engineering Pipelines

---

## 1. Purpose of This Document

This document provides **practical guidance for data engineers** on how to **assert and enforce ETSL Semantic Models** within data engineering pipelines.

It covers:
- How semantic model artifacts translate into executable assertions
- A recommended **ETSL Semantic Artifact template**
- How to design a **Semantic Compiler** (without prescribing implementation)
- The operating model and rituals between **Semantic Model Architects** and **Data Engineers**

This document assumes familiarity with:
- Facts, Events, and State modeling
- dbt or equivalent transformation frameworks
- CI/CD-based data pipelines

---

## 2. First Principles (Engineers Must Internalize These)

1. **Semantic models define what is allowed to be true.**
2. **Pipelines assert or violate semantics; they do not redefine them.**
3. **Schemas are implementations, not semantics.**
4. **All enforcement is downstream of semantic intent.**

If a pipeline change alters enterprise meaning, it is a **semantic change**, not an engineering refactor.

---

## 3. What Engineers Are Enforcing (and What They Are Not)

### Engineers Enforce:
- Shape of asserted data (columns, keys)
- Integrity constraints
- Temporal validity checks
- Relationship consistency
- State invariants

### Engineers Do NOT Define:
- New entity meanings
- New relationship semantics
- Authority rules
- Business meaning of facts

Those belong to ETSL Semantic Artifacts.

---

## 4. ETSL Semantic Artifact Template (Recommended)

Semantic artifacts must be **non-executable, storage-agnostic, and normative**.

### 4.1 Example: State Semantic Artifact (Illustrative)

```yaml
artifact_type: etsl_semantic_state
entity: Account

description: >
  Authoritative point-in-time representation of a financial account.

keys:
  - account_id

attributes:
  account_id:
    semantic_type: AccountId
    required: true

  status:
    semantic_type: AccountStatus
    required: true
    allowed_values:
      - OPEN
      - FROZEN
      - CLOSED

  owner_party_id:
    semantic_type: PartyId
    required: true

  closed_at:
    semantic_type: Timestamp
    required_if:
      condition: status == 'CLOSED'

relationships:
  - name: OWNS
    from: Party
    to: Account
    cardinality: one_to_many
    temporal: true

invariants:
  - name: unique_account
    rule: account_id must be unique

  - name: owner_exists
    rule: owner_party_id must reference a valid Party state

authority:
  asserted_by:
    - CoreBanking
    - AccountPlatform

temporal:
  effective_from_required: true
```

Key characteristics:
- No SQL
- No warehouse types
- No implementation details

---

## 5. Translating Semantic Artifacts into Pipeline Assertions

This translation must be **mechanical and one-way**.

### 5.1 What Gets Generated

From the semantic artifact, engineers (via tooling) generate:

- dbt model contracts
- dbt schema tests
- Custom invariant tests
- Documentation stubs

### 5.2 Typical Mappings

| Semantic Construct | Pipeline Assertion |
|------------------|-------------------|
| required: true | not_null test |
| keys | unique test |
| allowed_values | accepted_values test |
| relationships | relationships test |
| invariants | custom SQL test |
| semantic_type | mapped to warehouse type |

---

## 6. Designing the Semantic Compiler (Guidance Only)

The **Semantic Compiler** is a build-time tool that converts semantic artifacts into executable assertions.

### 6.1 Responsibilities of the Compiler

The compiler:
- Reads ETSL semantic artifacts
- Validates internal consistency
- Generates pipeline-specific assertion artifacts
- Emits traceability metadata

The compiler does NOT:
- Execute pipelines
- Infer semantics
- Modify semantic intent

---

### 6.2 Recommended Compiler Outputs

For dbt-based stacks:
- `schema.yml` files (generated)
- Model contracts (`contract.enforced: true`)
- Custom test macros
- Mapping reports (semantic → physical)

Generated artifacts must be clearly marked as **DO NOT EDIT**.

---

### 6.3 One-Way Dependency Rule

```text
ETSL Semantic Artifact → Compiler → Pipeline Assertions
```

Reverse dependency is forbidden.

If a test fails because semantics changed, the semantic artifact must be updated first.

---

## 7. What Cannot Be Fully Enforced in Pipelines (Be Honest)

Some semantic expectations exceed pipeline capabilities:

- Authority correctness (beyond presence)
- Multi-entity temporal reasoning
- Cross-domain reconciliation
- Legal interpretation of overrides

Pipelines can **assert structure and integrity**, not absolute correctness of meaning.

---

## 8. Operating Model: Architect ↔ Engineer Interaction

This is critical. Without it, ETSL decays.

---

### 8.1 Clear Role Boundaries

| Role | Responsibility |
|----|----------------|
| Semantic Model Architect | Defines meaning, truth contracts |
| Data Engineer | Enforces and operationalizes semantics |
| Platform Team | Provides tooling and guardrails |

No role substitutes for another.

---

### 8.2 Required Rituals

#### 1. Semantic Review (Design-Time)
- Architects present semantic artifacts
- Engineers review enforceability
- Gaps are identified early

#### 2. Pre-Merge Semantic Check (CI)
- Compiler validates semantic completeness
- Generated assertions are diffed
- Breaking semantic changes are flagged

#### 3. Pipeline Failure Triage
- Engineers surface invariant failures
- Architects decide:
  - data bug
  - pipeline bug
  - semantic evolution required

#### 4. Semantic Evolution Review (Periodic)
- Quarterly or half-yearly
- Review friction points
- Refine semantics cautiously

---

### 8.3 Feedback Loop (Healthy Pattern)

```text
Pipeline Failure
   ↓
Semantic Invariant Violated
   ↓
Architect Review
   ↓
Either:
  - Fix data / pipeline
  - Or evolve semantic model (versioned)
```

Semantics evolve **slowly and deliberately**.

---

## 9. Anti-Patterns to Avoid

- Editing generated assertion files
- Encoding semantics directly in SQL
- “Fixing” failing tests by weakening constraints
- Silent semantic drift via pipeline changes
- Treating semantic artifacts as documentation only

Each of these breaks ETSL integrity.

---

## 10. Practical Checklist for Engineers

Before merging pipeline changes:
- Are all semantic artifacts unchanged or intentionally updated?
- Are generated assertions updated automatically?
- Do failures indicate real semantic violations?
- Has semantic ownership been consulted?

If unsure, stop and escalate.

---

## 11. Final Guidance (Worth Printing)

> **Semantic models are the constitution.  
> Pipelines are the courts that enforce it.  
> Engineers do not reinterpret the law—they enforce it faithfully.**

---

## 12. Next Steps You May Want

- Create a semantic artifact repository
- Stand up a basic semantic compiler
- Add semantic checks to CI
- Formalize architect–engineer rituals

These steps matter more than tooling sophistication.

---
