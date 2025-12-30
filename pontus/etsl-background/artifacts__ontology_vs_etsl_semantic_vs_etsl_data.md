# Ontology Artifacts vs ETSL Semantic Artifacts vs ETSL Data Artifacts
## Meaning, Truth, and Implementation in Enterprise Data Architecture

---

## 1. Purpose of This Document

This document clarifies and **formally distinguishes three commonly conflated artifact classes** in modern enterprise data architectures:

1. **Ontology Artifacts**
2. **ETSL Semantic Artifacts**
3. **ETSL Data Artifacts (Implementation / Data Artifacts)**

It is intended for:
- CIOs and Chief Architects
- ETSL Modelling Architects
- Senior Platform and Data Engineering Leaders

The goal is to:
- Eliminate semantic and architectural confusion
- Establish clear boundaries of responsibility
- Enable scalable governance, engineering, and evolution

---

## 2. Why This Distinction Matters

Most large enterprises fail to establish a durable “enterprise truth layer” not because of tooling gaps, but because **these three artifact classes are mixed together**:

- Conceptual meaning leaks into schemas
- Operational truth is inferred instead of asserted
- Engineering artifacts quietly redefine semantics

This document provides a **clean separation of concerns**.

---

## 3. Definitions (Authoritative)

### 3.1 Ontology Artifact

An **Ontology Artifact** is a **conceptual modeling artifact** that defines:

- Entity *types*
- Relationship *types*
- Conceptual constraints
- Vocabulary and meaning

Ontology artifacts answer:

> *What kinds of things and relationships make sense in this enterprise domain?*

They operate in the **space of meaning and possibility**.

---

### 3.2 ETSL Semantic Artifact

An **ETSL Semantic Artifact** is a **normative semantic contract** that defines:

- What kinds of **truths may be asserted**
- What **relationships may be asserted as facts**
- What **facts, events, and states are semantically valid**
- What **authority, integrity, and temporal rules** govern those assertions

ETSL Semantic Artifacts answer:

> *What kinds of truths may be asserted about enterprise reality, and under what conditions?*

They operate in the **space of truth, validity, and enforceability**.

---

### 3.3 ETSL Data Artifact (Implementation / Data Artifact)

An **ETSL Data Artifact** is a **concrete realization** of ETSL semantics in data systems, such as:

- Fact records
- Event records
- State tables or documents
- Relationship instances
- Materialized views derived from ETSL truth

ETSL Data Artifacts answer:

> *What is actually recorded, stored, and operated on in systems?*

They operate in the **space of data, execution, and storage**.

> ETSL Data Artifacts may be materialized in physical storage, streams, or in-memory representations, but their semantics are independent of such physical concerns.

---

## 4. Core Distinction (In One Paragraph)

> **Ontology Artifacts define conceptual meaning and possibility.  
> ETSL Semantic Artifacts define the forms of truth that may be asserted in enterprise reality.  
> ETSL Data Artifacts are the concrete data instances that realize those truths in operational systems.**

Each layer progressively narrows freedom and increases enforceability.

---

## 5. Side-by-Side Comparison

| Dimension | Ontology Artifact | ETSL Semantic Artifact | ETSL Data Artifact |
|--------|------------------|------------------------|-------------------|
| Primary role | Meaning | Truth contract | Realized data |
| Question answered | What does this mean? | What can be asserted as true? | What is stored / processed? |
| Level | Entity & relationship types | Assertable truth forms | Entity instances |
| Time | Optional / abstract | Mandatory | Concrete timestamps |
| Authority | Implicit | Explicit | Recorded / referenced |
| Integrity rules | Conceptual | Enforced semantically | Enforced technically |
| Enforcement | None | Required | Required |
| Storage concern | None | None | Yes |
| Audience | Modellers, analysts | ETSL architects, governance | Engineers, systems |
| Evolves via | Conceptual debate | Controlled governance | Engineering change |

---

## 6. Concrete Example (All Three Layers)

### 6.1 Ontology Artifact (Conceptual)

```text
Party MAY OWN Account
Contract MAY GOVERN Account
```

Meaning:
- Ownership and governance are meaningful relationships
- No assertion about existence, time, or authority

It does not say:
	•	Which party
	•	Which account
	•	When
	•	Under whose authority
	•	Whether it is currently valid

**OWL (Web Ontology Language) style representation:**

```owl
<!-- Class declarations -->
Class: Party
Class: Account
Class: Contract

<!-- Object property declarations -->
ObjectProperty: owns
    Domain: Party
    Range: Account

ObjectProperty: governs
    Domain: Contract
    Range: Account
```

---

### 6.2 ETSL Semantic Artifact (Normative)

```text
Relationship Type: OWNS
From: Party
To: Account
Temporal: Required
Authority: Required
Constraints:
  - Ownership must be exclusive
```

Meaning:
- Ownership is an assertable truth
- Assertions must carry time and authority
- Integrity constraints apply

Still:
	•	No instances
	•	No storage
	•	No schemas

But now the model is binding.

#### Why ETSL Semantic Artifacts are not Ontology Artifacts

A common misconception is:

“ETSL semantics are just operational ontology”

This is incorrect.

Ontology artifacts are:
	•	Descriptive
	•	Explain meaning
	•	Allow ambiguity
	•	Support reasoning and classification

ETSL semantic artifacts are:
	•	Prescriptive
	•	Define allowed assertions
	•	Eliminate ambiguity
	•	Support enforcement and audit

Ontology tolerates ambiguity.
ETSL semantic artifacts exist to eliminate it.

> Enterprise ontology artifacts describe the conceptual relationships that may exist between types of entities and their intended meaning. ETSL semantic artifacts operate at a different level, defining the forms of truth and relationships that may be asserted in enterprise reality, including their temporal validity, authority, and integrity constraints. Ontology establishes meaning; ETSL semantic artifacts establish what can be asserted as true.

---

### 6.3 ETSL Data Artifact (Data)

```text
Relationship Instance:
  relationship_id: R-123
  type: OWNS
  from_party: P-456
  to_account: A-789
  effective_from: 2023-04-01
  authority: CoreBanking
```

Meaning:
- This ownership exists in enterprise reality

---

#### 6.4 A useful mental model (more precise than before)

Earlier we used grammar vs sentences.
Here is a more accurate refinement:
	•	Ontology defines the vocabulary and grammar of the enterprise
	•	ETSL semantic artifacts define the legal forms of statements that may be made
	•	ETSL data artifacts (facts, state, etc.) are the actual statements

So:

```text
Ontology → Semantic Possibility
ETSL Semantic Artifacts → Assertable Truth Forms
ETSL Data → Actual Truth
```
Each layer narrows freedom.

#### 6.5 What should never happen (important guardrail)

❌ Ontology artifacts defining:
	•	temporal rules
	•	authority rules
	•	lifecycle validity
	•	integrity enforcement

❌ ETSL semantic artifacts:
	•	redefining conceptual meaning
	•	introducing new vocabulary casually
	•	drifting away from ontology alignment

Ontology informs ETSL semantics.
ETSL semantics constrain enterprise truth.

## 7. Common Failure Modes When These Are Conflated

### 7.1 Ontology Treated as Truth
- No time or authority
- Audit depends on code
- Entitlements break

### 7.2 ETSL Semantic Artifacts Treated as Schemas
- Semantics leak into pipelines
- Truth redefined per system
- Governance collapses

### 7.3 ETSL Data Artifacts Redefining Semantics
- “Latest row wins” becomes truth
- Projections become authoritative
- Corrections become destructive

---

## 8. Governance Implications

### Ontology Governance
- Focused on meaning
- Slow, consensus-driven
- Human-centric

### ETSL Semantic Governance
- Focused on enforceability
- Explicit authority
- Change-controlled

### ETSL Data Artifact Governance
- Focused on correctness and performance
- Automated validation
- Operational monitoring

Each requires **different processes and owners**.

---

## 9. A Rule of Thumb That Prevents Most Confusion

> If an artifact explains what *could exist*, it is ontology.  
> If it defines what *may be asserted as true*, it is an ETSL semantic artifact.  
> If it records what *does exist*, it is an ETSL data artifact.

---

## 10. Closing Note

> Ontology gives the enterprise its language.  
> ETSL Semantic Artifacts give it its constitution.  
> ETSL Data Artifacts give it memory and execution.

Keeping these layers distinct is not bureaucracy — it is the foundation of scalable, defensible enterprise truth.

---
