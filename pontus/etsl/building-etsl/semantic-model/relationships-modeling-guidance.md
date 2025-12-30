# ETSL Guidance Document  
## Relationship Modeling for ETSL Modeling Architects

---

## 1. Purpose of This Document

This document provides **authoritative guidance** on **Relationship Modeling** within the Enterprise Truth & Semantics Layer (ETSL).

It is intended for:
- ETSL Modeling Architects
- Enterprise / Domain Architects
- Architects responsible for semantic integrity across domains

The focus is on:
- Modeling relationships as first-class semantic constructs
- Ensuring durability, correctness, and evolvability
- Avoiding common failure modes seen in large enterprises
- Clarifying the relationship between ETSL modeling and Enterprise Ontology practices

This document is **conceptual and semantic**, not physical or tooling-oriented.

---

## 2. Why Relationship Modeling Matters in ETSL

In large enterprises, **most semantic power does not live in attributes**.  
It lives in **relationships**.

Examples:
- Who owns what
- Who owes whom
- Who is authorized to act for whom
- What governs what
- What derives from what

Poorly modeled relationships lead to:
- Ambiguous truth
- Exploding join logic
- Hidden business rules in code
- Inconsistent interpretations across teams

> **ETSL succeeds or fails based on how relationships are modeled.**

---

## 3. What a Relationship Is in ETSL

### 3.1 Authoritative Definition

A **Relationship** is a semantically typed, time-bound, and governed association between two or more enterprise entities.

Key properties:
- First-class (not implicit)
- Typed (meaningful, not generic)
- Temporal (valid from / to)
- Governed (authority and constraints)

A relationship is **not**:
- A foreign key
- A join condition
- An implementation artifact

---

## 4. Relationship Modeling vs Enterprise Ontology

### 4.1 Similarities

ETSL Relationship Modeling and Enterprise Ontology share common foundations:

- Meaning-first modeling
- Explicit entities and relationships
- Relationships as first-class citizens

ETSL models are often **informed by enterprise ontologies**.

---

### 4.2 Key Differences

| Aspect | Enterprise Ontology | ETSL Relationship Modeling |
|-----|--------------------|----------------------------|
| Primary purpose | Conceptual understanding | Operational truth |
| Scope | Broad, explanatory | Precise, enforceable |
| Precision | Often abstract | Deliberately strict |
| Temporal semantics | Optional | Mandatory |
| Authority | Implicit | Explicit |
| Enforceability | Conceptual | Auditable |

Ontology answers *“What does this mean?”*  
ETSL answers *“What is true, when, and under whose authority?”*

---

### 4.3 Deep dive into differences

Enterprise ontology defines the conceptual relationship space of the enterprise — the types of relationships that may exist between classes of entities and their intended meaning. ETSL relationship modeling operates one level lower, asserting concrete, time-bound, and governed relationships between specific entity instances that exist in enterprise reality. Ontology informs what is meaningful; ETSL establishes what is true.

Refer to [Ontology vs Semantic vs Data Artifacts](../../conceptual/artifacts-ontology-vs-semantic-vs-data.md)

---

## 5. Core Principles of ETSL Relationship Modeling

### 5.1 Relationships Are Explicit

If a relationship affects:
- Integrity
- Authorization
- Obligation
- Entitlement
- Regulation

…it must be modeled explicitly.

Implicit relationships are **semantic debt**.

---

### 5.2 Relationships Are Typed, Not Generic

Avoid:
- `related_to`
- `associated_with`
- `linked_to`

Prefer:
- `OWNS`
- `GOVERNS`
- `GUARANTEES`
- `AUTHORIZES`
- `BENEFITS`

Typed relationships externalize meaning from code.

---

### 5.3 Relationships Are Temporal

Every relationship must define:
- Effective start
- Effective end

Time-free relationships:
- Break audits
- Break entitlement reasoning
- Break explainability

---

### 5.4 Relationships Have Direction

Relationships are **directional by default**.

Example:
- Party `OWNS` Account ≠ Account `OWNS` Party

Direction matters for:
- Reasoning
- Control
- Obligation flow

---

### 5.5 Relationships Are Governed

Each relationship type must define:
- Who can assert it
- Who can revoke it
- Applicable constraints

Governance prevents silent semantic corruption.

---

## 6. Canonical Relationship Structure

```text
Relationship {
  relationship_id
  type
  from_entity_id
  to_entity_id
  effective_from
  effective_to
  authority
  constraints (optional)
}
```

> The relationship itself is an enterprise entity.

---

## 7. Relationship Modeling DOs

- Model relationships as first-class constructs
- Use precise, business-meaningful types
- Encode temporal validity explicitly
- Model direction intentionally
- Assign authority and governance
- Keep relationship semantics stable
- Treat relationship changes as semantic events

---

## 8. Relationship Modeling DON’Ts

- Do not hide relationships inside attributes
- Do not rely on implicit joins
- Do not overload one relationship type
- Do not encode rules in SQL or pipelines
- Do not assume symmetry
- Do not make relationships permanent by default

---

## 9. What Poor Relationship Modeling Looks Like

### 9.1 Attribute-Based Relationships

```text
Account {
  owner_party_id
}
```

Problems:
- No history
- No multiplicity
- No authority
- No semantics

---

### 9.2 Generic Relationship Tables

```text
EntityRelationship {
  entity_a
  entity_b
  relationship_type = "LINKED"
}
```

Problems:
- Meaning pushed into code
- Impossible governance
- No reasoning capability

---

### 9.3 Time-Free Relationships

```text
Party OWNS Account
```

(with no temporal bounds)

Problems:
- Cannot answer “as of T”
- Cannot revoke
- Audit failure

---

### 9.4 Semantics Hidden in Pipelines

```sql
JOIN account a ON a.owner_id = p.id
WHERE a.status = 'ACTIVE'
```

Problems:
- Semantics duplicated
- Inconsistent interpretations
- No authoritative definition

---

## 10. Consequences of Poor Relationship Modeling

- Authorization logic duplicated
- Conflicting ownership semantics
- Inability to explain decisions
- Regulatory exposure
- Exponential data engineering cost

> Most enterprise data failures trace back to relationship modeling errors.

---

## 11. Iterating Relationship Models Safely

### 11.1 Expect Evolution

Relationship models will evolve as:
- Domains expand
- Edge cases emerge
- Regulatory clarity improves

---

### 11.2 Safe Evolution Rules

- Add new relationship types
- Version semantics explicitly
- Deprecate, don’t repurpose
- Preserve backward meaning

---

### 11.3 Semantic Pressure as a Signal

If engineers:
- Ask repeatedly “what does this mean?”
- Encode exceptions in code
- Add flags to compensate

…it indicates model insufficiency.

---

## 12. Relationship Review Checklist

Before approval, verify:

1. Semantic precision
2. Temporal bounds
3. Directionality
4. Authority definition
5. Audit support
6. Evolvability

If any fail, revise.

---

## 13. Relationship Modeling and Reasoning Readiness

Well-modeled relationships enable:
- Policy evaluation
- Entitlement inference
- Graph reasoning
- Agentic workflows

Poor models block all of the above.

---

## 14. Canonical Principles

1. Relationships are first-class.
2. Meaning must be explicit.
3. Time and authority are mandatory.
4. Ontology informs; ETSL enforces.
5. Iteration is expected; ambiguity is not.

---

## 15. Closing Note

> **Attributes describe entities.  
Relationships define enterprise reality.**

ETSL relationship modeling is where semantic rigor becomes operational power.

---
