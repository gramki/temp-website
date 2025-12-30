Below I’ll unpack how large enterprises actually model ETSL, based on what has survived in global banks, capital markets firms, and large digital platforms. I’ll be very explicit about modeling primitives, artifacts, and invariants, not just patterns.

I’ll structure this into six concrete layers of modeling, moving from meaning → facts → state → storage, because that’s how successful enterprises do it (even if they don’t always admit it).

---

# How Large Enterprises Actually Model ETSL

## 0. A critical framing (before we start)

Large enterprises do **not** start with tables.  
They also do **not** start with pipelines.

They start—often implicitly—with this ordering:

**Language → Semantics → Facts → State → Storage → Views**

Most failures happen because teams start at **Storage** or **Views**.

---

## 1. Semantic Modeling: Enterprise Language First

### 1.1 Ubiquitous Language (but enterprise-wide)

Successful ETSL programs begin by naming things carefully:

- Party (not Customer)
- Account (not CASA / Loan / Wallet)
- Contract (not Product)
- Instrument (not Scheme)
- Obligation
- Entitlement
- Event
- Decision
- Policy

These terms are:

- Business-legible
- Cross-domain
- Durable over decades

This layer is usually undocumented formally—but it exists in the heads of senior architects and regulators.

---

### 1.2 Conceptual Entity Model (No attributes yet)

At this stage, enterprises define:

- What kinds of things exist
- How they relate
- What cannot exist without what

**Example (conceptual):**

```
Party
 ├─ owns → Account
 ├─ enters → Contract
 └─ holds → Entitlement

Contract
 ├─ creates → Obligation
 └─ governs → Account

Account
 ├─ records → Balance
 └─ participates in → Event
```

**Key rule:**  
No system names. No storage types. No use cases.

This model changes very slowly.

---

## 2. Fact Modeling: What Happened vs What Exists

This is one of the most important enterprise distinctions.

### 2.1 Facts are assertions, not rows

Large enterprises model facts as:

> A semantically typed assertion that something occurred or was established, at a point in time, by some authority.

**Examples:**

- “Account A was opened at T by System X”
- “Limit L was increased from 10k to 20k”
- “Contract C created Obligation O”

**Facts have:**

- Time
- Subject
- Predicate
- Authority
- Context

They are **append-only**.

---

### 2.2 Enterprises separate Facts from State

This is universal in mature systems:

| Concept | Meaning             |
| ------- | ------------------- |
| Fact    | What happened       |
| State   | What is currently true |

**Why this matters:**

- Regulation
- Corrections
- Replays
- Explainability

**State is derived. Facts are sacred.**

---

## 3. Event Modeling: Enterprise Events (not system events)

### 3.1 What enterprises call an “event”

Not:

- DB insert
- API call
- Kafka message

But:

> A business-meaningful transition in enterprise reality

**Examples:**

- AccountOpened
- ObligationCreated
- EntitlementGranted
- IdentityLinked
- RiskRatingUpdated
- DecisionOverridden

---

### 3.2 Event schema discipline

Enterprise events:

- Are semantically versioned
- Carry minimal payload
- Reference entities, not embed them
- Are stable for years

This allows:

- Reprocessing
- New projections
- New consumers

---

## 4. State Modeling: Authoritative Enterprise Reality

### 4.1 State is modeled per entity, not per use case

For each core entity, enterprises define:

- Identity
- Lifecycle states
- Valid transitions
- Invariants

**Example: Account State**

```yaml
Account {
  id
  owner_party_id
  status: {OPEN, FROZEN, CLOSED}
  current_balance
  governing_contract_id
  effective_from
  effective_to
}
```

This is **not**:

- A reporting table
- A transaction ledger
- A channel-specific view

---

### 4.2 Authority is explicit

Every state record answers:

- Who asserts this?
- Based on which facts?
- Since when?

This is how enterprises:

- Survive audits
- Handle disputes
- Support overrides

---

## 5. Relationship Modeling: The Hidden Backbone

Large enterprises treat relationships as first-class citizens.

**Examples:**

- Party ↔ Account
- Party ↔ Party (guardian, beneficiary)
- Account ↔ Contract
- Obligation ↔ Entitlement
- Decision ↔ Evidence

These are:

- Temporal
- Typed
- Governed

Often implemented as:

- Graph stores
- Relational link tables
- Hybrid models

Most semantic power of ETSL lives here, not in attributes.

---

## 6. Physical Modeling: Mapping Semantics to Storage

Only _now_ do enterprises choose storage.

### 6.1 Typical physical mapping

| Semantic Artifact       | Physical Form                        |
|------------------------|--------------------------------------|
| Enterprise Events      | Append-only log tables / streams     |
| Facts                 | Immutable fact tables                |
| Current State         | Normalized relational or document stores |
| Relationships         | Graph or associative tables          |
| Projections           | Warehouses, indexes, feature stores  |

**Key rule:**  
No storage is allowed to redefine semantics.

---

### 6.2 Temporal modeling everywhere

Everything important is:

- Time-bound
- Versioned
- Auditable

This enables:

- “As-of” queries
- Regulatory reconstruction
- AI explainability

---

## 7. What Enterprises Explicitly Avoid (Hard-won lessons)

### 7.1 They avoid “one big canonical schema”

Because:

- Domains evolve
- Use cases explode
- Ownership blurs

Instead:

- Canonical semantics
- Plural physical representations

---

### 7.2 They avoid truth in marts

Marts are:

- Disposable
- Recomposable
- Consumer-specific

Truth lives below them.

---

## 8. The Artifacts ETSL Produces (this is important)

Mature ETSL programs explicitly manage:

- Entity Definitions
- Event Schemas
- State Models
- Relationship Types
- Authority Rules
- Invariants
- Lineage Metadata

These artifacts are:

- Versioned
- Reviewed
- Governed

Often more important than the data itself.

---

Large enterprises model ETSL by first stabilizing enterprise semantics, then capturing facts and events immutably, deriving authoritative state explicitly, and only finally projecting that state into storage forms optimized for consumption.

---

One of the primary failure modes of enterprise data architecture is: _Implicit semantic assignment by confident subsystems._

---

## Why ETSL matters for any data or product platform

In an enterprise operating multiple data-driven products and platforms:

- Some systems produce facts or assertions
- Some systems consume enterprise state
- Some systems derive interpretations or projections

**Without ETSL:**

- Each system quietly defines its own version of truth
- Semantics drift is invisible until reconciliation or audit
- Pipelines become semantic contracts
- “Correctness” becomes use-case dependent

**With ETSL:**

- Semantic authority is centralized and explicit
- Fact creation is deliberate and attributable
- Derived representations are disposable
- Products evolve without redefining enterprise reality

**Hard guardrails ETSL enforces (universally)**

No participating system should:

- Define enterprise-level entities unilaterally
- Introduce new semantic meaning without registration
- Persist derived interpretations as authoritative truth
- Encode semantic assumptions inside pipelines

---

In an enterprise truth architecture, facts and events serve distinct but complementary roles. **Events** capture the occurrence of meaningful transitions in enterprise activity, while **facts** represent the authoritative assertions that define enterprise reality over time. Events explain causality; facts establish truth. Conflating the two leads either to fragile state reconstruction or to loss of explainability. Mature ETSL implementations therefore model both explicitly, govern them independently, and link them through clear semantic contracts.

---

In ETSL, state represents the authoritative, point-in-time realization of an enterprise entity, derived deterministically from facts and constrained by explicit invariants. Unlike facts, which assert individual truths, state encodes the completeness, consistency, and validity required for the entity to exist correctly at a given moment. State modeling therefore formalizes integrity expectations, lifecycle semantics, and authority precedence, making enterprise reality operationally usable, auditable, and defensible without reliance on procedural logic or pipelines.

---

Authority in ETSL represents the enterprise function or mandate empowered to assert a class of truth. Systems, processes, and people act on behalf of authority but do not replace it. Authority must be explicit, governed, and auditable across facts, relationships, and derived state.

⸻

## FAQ

- **What are the tools and techniques used for representing ETSL Semantic model artifacts? How to avoid confusion and conflation between the schema data engineers produce across various layers to that of the Semantic model? Give an example repository of Semantic model artifacts produced in one or other format? How are the ETSL model artifacts going to look different from Ontology artifacts?**
Ref: [model-representation](./etsl-semantic-model-representation.md)
Ref: [etsl-vs-ontology](./etsl-vs-ontology.md)
Ref: [artifacts-ontology-etsl-data](./artifacts__ontology_vs_etsl_semantic_vs_etsl_data.md)


- **How can the semantic model artifacts be translatable into assertions in the data engineering pipelines? Is there a way to enforce the semantic model expectations in DBTs?**
Ref: [semnatic-model-assertions-for-data-engineers](./etsl_semantic_model_assertion_guidance_for_data_engineers.md)
Ref: [semantic-model-guidance-for-architects](./etsl_semantic_model_guidance_for_architects.md)

- **Provide guidance on how to iterate on the models with evolving understanding of the enterprise and with evolution of the enterprise information**

- **There is a lot of insistence on 'Authority'. In practice, what should it represent - system, function, team, person? If authority should be asserted for facts, state, and relationships, how is that accomplished in practice?**
Ref: [authority-modeling-guidance](./etsl_authority_modeling_guidance_for_architects.md)

- Much of the semantic modeling looks to be common for an industry (not just Ontology). If yes, there should be some work done by industry bodies like BIAN capture this common model. Can you list down such attempts and their maturity, relevance for building ETSL for a bank? If there are some mature models, what is the work anticipated from Semantic Model Architect to adapt such models for a specific enterprise/bank? How to avoid inconsitency with such published industry work during evolution of proprietary semantic model.

Ref: [banking-industry-reference](./etsl_banking_industry_reference_models_for_semantic_modeling.md)

- We covered ETSL Semantic Artifacts and ETSL Data Artifacts. However, as evident from this discussion, the ETSL Data Artifacts do not represent the consumer-domain-aware and use-case-aware data products. The product managers, architects, and engineers of consumer domains also need some normative guidance on using the ETSL Data Artifacts for creating their products. Let us work on a guidance document for Building Data Products using ETSL Data Artifacts.

Before we proceed with that, we need to align oursleves on terminology of Data Products and its constituents. Share your perspective on this.

- Compare and constract ETSL with Data Mesh as the architectural reference for discussing data products. Clarify that data of SORs or Operational Systems is not truth by default. ETSL normalizes the truth from SOR assertions.
“In Data Mesh terms, Systems of Record produce source-aligned data. In ETSL, these are treated as assertions that must be normalized, authority-qualified, and reconciled before becoming enterprise truth.”
> ingestion in ETSL really means: Controlled intake of assertions into the enterprise truth boundary.

- Data Product Types and the approach to build, publish, and govern.
If a data product can change without coordinated downstream communication, it is analytical.
If a change requires consumer notification or versioning, it is consumer-aligned.
Analytical data products exist to learn.
Aggregated / consumer-aligned data products exist to act.

“Data Products are built and served by Data Applications. Operational systems that consume Data Products and act on them are Data-Driven Operational Applications. Any assertions produced by such systems re-enter ETSL as authority-qualified, lineage-aware enterprise truth.”

- ETSL Data Artifacts and use in transactional, near-real-time applications? Are events ETSL data artifacts? Is it practical to expect ETSL Data Artifacts fresh enough to serve as source for data prodcuts for transaction application use cases? Is there an alternative semantic required for near-real-time operational data products?
