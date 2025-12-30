# Representing ETSL Semantic Model Artifacts

## Tools, Techniques, and Guardrails Against Schema Conflation

---

### 1. First Principle (Non-negotiable)

**ETSL semantic model artifacts are not schemas.**  
They are contracts about meaning, truth, and authority.

If engineers can mistake an ETSL artifact for:
- a table definition,
- a JSON payload,
- or a Kafka schema,

then the representation is already wrong.

Everything that follows is about making that confusion impossible.

---

### 2. What exactly are “ETSL Semantic Model Artifacts”?

Before tools, clarity on what is being represented.

ETSL semantic artifacts include:

1. **Entity definitions**  
   *What kind of thing exists in enterprise reality*

2. **Relationship definitions**  
   *What specific relationships are meaningful and assertable*

3. **Fact types**  
   *What kinds of truths can be asserted*

4. **Event types**  
   *What kinds of occurrences can change reality*

5. **State models**  
   *What constitutes a valid, complete entity at a point in time*

6. **Invariants & constraints**  
   *What must always hold true*

7. **Authority rules**  
   *Who is allowed to assert what*

8. **Lifecycle semantics**  
   *When things begin, change, and cease to exist*

_None of these are storage-specific._

---

### 3. Tools & Techniques Used by Large Enterprises

#### 3.1 The Most Important “Tool”: Deliberate Non-executable Formats

Mature enterprises intentionally choose formats that:
- cannot be accidentally executed
- cannot be deployed directly
- cannot be confused with runtime artifacts

This is a feature, not a limitation.

---

#### 3.2 Common Representation Techniques (What Actually Works)

**1. Structured declarative documents (YAML / Markdown hybrids)**

Most common and most effective.

Used to express:
- Entity definitions
- Relationship types
- Invariants
- Authority rules

Why this works:
- Human readable
- Diffable
- Reviewable
- Not executable

**Example (illustrative):**
```yaml
entity: Account
description: >
  A financial account representing a contractual ledger
  between the enterprise and a party.

invariants:
  - must_have_owner: true
  - must_have_governing_contract: true

lifecycle:
  states:
    - CREATED
    - ACTIVE
    - CLOSED
```

>This is not a schema.  
>There are no types, lengths, or indexes.

---

**2. Semantic DSLs (lightweight, not Turing-complete)**

Some enterprises define a very small DSL for ETSL artifacts.

Characteristics:
- Declarative
- No loops
- No conditionals
- No computations

Purpose:
- Express semantics precisely
- Prevent logic from creeping in

This is often used for:
- Relationship semantics
- Authority rules
- Invariants

---

**3. UML / C4-style diagrams (conceptual only)**

Used for:
- Review
- Communication
- Alignment

_Not authoritative by themselves._

**Key rule:**

> Diagrams explain the model; they are not the model.

---

**4. Semantic registries (metadata systems)**

Some large enterprises store ETSL artifacts in:
- Metadata catalogs
- Custom semantic registries
- Versioned document stores

But:
- The registry is storage
- The artifacts remain declarative

---

### 4. How to Avoid Confusion with Data Engineering Schemas

This is the core operational problem you are calling out.

#### 4.1 The Root Cause of Conflation

Conflation happens when:
- Semantic artifacts and schemas look similar
- Live in the same repo
- Use the same formats
- Share the same naming conventions

---

#### 4.2 Hard Guardrails That Actually Work

**Guardrail 1: Different artifact classes, different repos**

Never mix ETSL semantic artifacts with:
- SQL
- Avro
- Protobuf
- OpenAPI
- Spark schemas

**Recommended separation:**
```text
enterprise-semantics/
└── etsl/
    ├── entities/
    ├── relationships/
    ├── facts/
    ├── events/
    ├── states/
    ├── invariants/
    └── authority/
```
Versus:
```text
data-platform/
└── schemas/
    ├── ingestion/
    ├── events/
    ├── state/
    └── projections/
```
>If they share a repo, they will be conflated.

---

**Guardrail 2: Semantic artifacts never specify storage concerns**

ETSL artifacts must never contain:
- data types (varchar, int)
- field lengths
- nullability rules
- partitioning
- indexes

>If they do, they are no longer semantic.

---

**Guardrail 3: One-way traceability**

**Allowed:**
```text
ETSL Semantic Artifact → implementation schema
```
**Forbidden:**
```text
schema → semantic definition
```

Semantics inform engineering.  
Engineering never defines semantics.

---

**Guardrail 4: Explicit “non-runtime” labeling**

Every ETSL artifact should carry a header like:
```text
Artifact Type: ETSL Semantic Model
Execution: Non-executable
Purpose: Defines enterprise meaning and integrity
```
>This sounds trivial. It is not.  
>It prevents accidental misuse.

---

### 5. Example Repository of ETSL Semantic Artifacts

Below is a realistic, enterprise-grade structure.

```text
enterprise-truth-model/
├── README.md
│
├── etsl/
│   ├── entities/
│   │   ├── Party.yaml
│   │   ├── Account.yaml
│   │   └── Contract.yaml
│   │
│   ├── relationships/
│   │   ├── OWNS.yaml
│   │   ├── GOVERNS.yaml
│   │   └── AUTHORIZES.yaml
│   │
│   ├── facts/
│   │   ├── AccountStatusFact.yaml
│   │   └── CreditLimitFact.yaml
│   │
│   ├── events/
│   │   ├── AccountOpened.yaml
│   │   └── LimitAdjusted.yaml
│   │
│   ├── states/
│   │   ├── AccountState.yaml
│   │   └── ObligationState.yaml
│   │
│   ├── invariants/
│   │   ├── AccountIntegrity.yaml
│   │   └── ObligationIntegrity.yaml
│   │
│   └── authority/
│       ├── AssertionRules.yaml
│       └── OverrideRules.yaml
│
└── governance/
    ├── review-process.md
    ├── versioning.md
    └── change-policy.md

```
_Nothing here can be deployed.  
That is by design._

---

### 6. How ETSL Artifacts Differ from Ontology Artifacts

This is the critical comparison you asked for.

#### 6.1 Ontology Artifacts

Ontology artifacts typically:
- Define entity types
- Define relationship types
- Express conceptual constraints
- Live in OWL / RDF / conceptual diagrams

They answer:

>“What kinds of things and relationships make sense?”

They are:
- Descriptive
- Conceptual
- Type-level

---

#### 6.2 ETSL Semantic Artifacts

ETSL artifacts:
- Define assertable facts
- Define enforceable relationships
- Define state completeness
- Define authority and time

They answer:

>“What is allowed to be asserted as true in enterprise reality?”

They are:
- Prescriptive
- Operationally binding
- Instance-level aware (even if not instance-specific)

---

### 7. Closing Guidance for ETSL Architects on ETSL Semantic Artifacts

- Use boring formats on purpose
- Make semantics non-executable
- Separate meaning from storage ruthlessly
- Treat ETSL semantic artifacts as constitutional law, not code
- Let engineers translate — never reinterpret

