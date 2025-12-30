# ETSL Guidance for Semantic Model Architects  
## Modeling Authority in Enterprise Truth & Semantics Layer (ETSL)

---

## 1. Purpose of This Document

This document provides **authoritative guidance for ETSL Semantic Model Architects** on **modeling, governing, and operationalizing Authority** across:

- Facts
- Relationships
- State

It explains:
- What Authority represents in practice
- What it explicitly does *not* represent
- How to discover and capture Authority in real enterprises
- How Authority evolves safely over time
- How Authority participates in state derivation and explanation

This document is semantic and architectural.  
It does **not** prescribe IAM, RBAC, or system design.

---

## 2. Why Authority Is Central to ETSL

ETSL exists to establish **enterprise truth**, not just data consistency.

Truth without Authority is:
- Accidental
- Non-defensible
- Non-auditable

> **Authority is what turns data into enterprise truth.**

Without explicit Authority:
- Overrides are indistinguishable from bugs
- Pipelines silently redefine reality
- Regulatory explanations collapse into code archaeology

---

## 3. What Authority Represents (Precisely)

### 3.1 Canonical Definition

> **Authority represents the formally recognized enterprise mandate under which a class of truth may be asserted, overridden, or revoked.**

Authority is:
- Organizational and functional
- Stable over time
- Auditable
- Delegable

---

## 4. What Authority Is NOT (Hard Boundaries)

### ❌ Authority is not a system
Systems change; truth must not.

Systems **act on behalf of authority**, they do not define it.

---

### ❌ Authority is not a person
People rotate; mandates persist.

People **exercise authority**, they do not embody it.

---

### ❌ Authority is not a team name
Teams reorganize; authority survives reorganizations.

Teams **operate within authority**, they are not the authority.

---

## 5. The Authority Stack (Mental Model)

In real enterprises, four layers exist:

```
Person
  ↓ acts as
Role
  ↓ within
System / Process
  ↓ exercising
Authority
```

**Only the bottom layer belongs in ETSL semantics.**

Upper layers may appear as *references* for audit, never as truth-defining attributes.

---

## 6. Discovering Authority in Practice

### 6.1 Where Authority Actually Lives

Authority is usually found in:
- Policy documents
- Regulatory charters
- Risk and compliance frameworks
- Delegation-of-authority matrices
- Audit and control ownership maps

Not in:
- System architecture diagrams
- Code repositories
- Org charts alone

---

### 6.2 Questions Architects Must Ask

To identify Authority, ask:

- Which function is accountable if this fact is wrong?
- Which function can override this assertion?
- Which function must defend this truth to a regulator?
- Which function signs off policy governing this truth?

The answers point to **Authority**, not systems.

---

## 7. Capturing Authority as a Semantic Artifact

### 7.1 Authority Registry (Required)

Authorities must be **explicitly enumerated**.

Example semantic artifact:

```yaml
authority: CreditRiskManagement
description: >
  Enterprise function responsible for asserting
  and governing credit exposure and risk limits.

can_assert:
  - CreditLimitFact
  - RiskRatingFact

can_override:
  - ProvisionalCreditLimitFact

precedence: high
```

This registry is:
- Semantic
- Versioned
- Governed

It is **not** IAM.

---

## 8. Authority in ETSL Constructs

### 8.1 Authority in Facts

Facts assert truth.

```text
Fact:
  subject: Account A123
  predicate: CreditLimit
  value: 20000
  effective_from: 2024-01-01
  authority: CreditRiskManagement
```

Meaning:
- This truth is valid because Credit Risk is empowered to assert it.

---

### 8.2 Authority in Relationships

Relationships assert control, obligation, or entitlement.

```text
Relationship:
  type: OWNS
  from: Party P
  to: Account A
  effective_from: T
  authority: RetailAccountOperations
```

This prevents:
- Unauthorized domains asserting ownership
- Analytical inference masquerading as truth

---

### 8.3 Authority in State (Derived but Critical)

State is derived, but **authority does not disappear**.

State represents:
> *Which authoritative assertions currently prevail*

```text
AccountState:
  owner: Party P
  credit_limit: 20000
  status: ACTIVE
  derived_from_authorities:
    - RetailAccountOperations
    - CreditRiskManagement
```

State must remain **explainable by authority**.

---

## 9. Authority-Aware State Derivation (Guidance)

### 9.1 Why Authority Matters in State Derivation

Conflicts arise when:
- Multiple facts assert the same predicate
- Different domains claim control
- Overrides occur without new events

Authority resolves:
- Which fact wins
- Why it wins
- Who is accountable

---

### 9.2 Canonical Authority Resolution Rules

Architects must define:
- Authority precedence
- Override permissions
- Conflict resolution rules

Example:

```text
If multiple CreditLimit facts exist:
  Prefer assertions from CreditRiskManagement
  over AutomatedScoring
```

These rules are semantic, not technical.

---

### 9.3 State Derivation Must Be:

- Deterministic
- Authority-aware
- Explainable

If a state cannot answer:
> *Which authority caused this value to be present?*

Then the model is incomplete.

---

## 10. Authority Evolution (Handled Carefully)

### 10.1 Why Authority Evolves

- Regulatory changes
- Organizational maturity
- New control functions
- Mergers and acquisitions

Authority evolution is expected — **semantic drift is not**.

---

### 10.2 Safe Authority Evolution Rules

- Add new authorities; do not rename casually
- Version authority definitions
- Preserve historical meaning
- Never retroactively reinterpret past authority

Authority evolution must be **additive and explicit**.

---

## 11. Interaction with Data Engineering

### 11.1 Architect Responsibilities

- Define allowed authorities
- Define which authorities can assert what
- Define precedence and overrides
- Own semantic change decisions

---

### 11.2 Engineer Responsibilities (Awareness Only)

- Validate authority presence
- Enforce authority rules mechanically
- Surface violations
- Never infer authority

---

## 12. Common Authority Anti-Patterns

- Using system names as authority
- Embedding user IDs as authority
- Allowing pipelines to infer authority
- Treating overrides as data corrections
- Omitting authority from state

Each breaks auditability.

---

## 13. Validation Checklist for Architects

Before approving authority modeling:

- Is authority functional and stable?
- Is it independent of systems and people?
- Is it enumerated and governed?
- Can it be defended to a regulator?
- Can it resolve conflicts deterministically?

If any answer is “no”, revise.

---

## 14. Canonical Guidance (Safe to Publish)

> **Authority in ETSL represents the enterprise function empowered to assert, override, or revoke a class of truth. Systems, processes, and people act on behalf of authority but do not define it. Authority must be explicit, governed, and preserved across facts, relationships, and derived state to ensure enterprise truth remains auditable and defensible.**

---

## 15. Closing Note

Semantic Model Architects do not merely describe data.  
They define **who is allowed to say what is true**.

Authority is the backbone of that responsibility.

---
