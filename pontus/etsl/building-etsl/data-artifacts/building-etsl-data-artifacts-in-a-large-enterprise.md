# Building ETSL Data Artifacts in a Large Enterprise  
## From Existing Data Estate to Enterprise Truth  
### Architectural Guidance for Architects and Data Engineers

> ⚡ **Quick Reference:** For a one-page cheat sheet, see [Building ETSL Data Artifacts — Quick Reference](building-etsl-data-artifacts-quick-reference.md)

---

## Table of Contents

### Foundations
- [1. Purpose and Audience](#1-purpose-and-audience)
- [2. Positioning ETSL Data Artifacts in the Enterprise Journey](#2-positioning-etsl-data-artifacts-in-the-enterprise-journey)
- [3. Reality Check: The Starting Point in Large Banks](#3-reality-check-the-starting-point-in-large-banks)
- [4. Clarifying the Target: What an ETSL Data Artifact Is (and Is Not)](#4-clarifying-the-target-what-an-etsl-data-artifact-is-and-is-not)
- [5. Terminology for the Transition Phase (Normative)](#5-terminology-for-the-transition-phase-normative)

### Scoping and Mapping
- [6. Identifying the First ETSL Use Cases](#6-identifying-the-first-etsl-use-cases)
- [7. Mapping the Existing Data Estate to ETSL Concepts](#7-mapping-the-existing-data-estate-to-etsl-concepts)
- [8. Designing the ETSL Ingress Layer](#8-designing-the-etsl-ingress-layer)

### Authority and Reconciliation
- [9. Authority Modeling in Practice](#9-authority-modeling-in-practice)
- [10. Reconciliation and Normalization Patterns](#10-reconciliation-and-normalization-patterns)
- [11. Reconciliation Failure and Error Handling](#11-reconciliation-failure-and-error-handling)

### Building and Operating
- [12. Producing the First ETSL Data Artifacts](#12-producing-the-first-etsl-data-artifacts)
- [13. Validating ETSL Data Artifacts](#13-validating-etsl-data-artifacts)
- [14. Operating Model During Early ETSL Adoption](#14-operating-model-during-early-etsl-adoption)

### Scaling and Avoiding Pitfalls
- [15. Co-existence with Existing Data Products](#15-co-existence-with-existing-data-products)
- [16. Anti-Patterns to Avoid Early](#16-anti-patterns-to-avoid-early)
- [17. Roadmap to Broader Adoption](#17-roadmap-to-broader-adoption)

### Enabling Data Products
- [18. How This Enables Data Product Engineering](#18-how-this-enables-data-product-engineering)
- [19. Summary Principles](#19-summary-principles)

### Reference
- [Glossary](#glossary)

---

## 1. Purpose and Audience

### Purpose

This document provides **practical, architectural guidance** for building **ETSL Data Artifacts** in a large enterprise—specifically a bank—starting from an existing, imperfect data estate.

It addresses the question:

> *How does an enterprise that already has SORs, data warehouses, lakes, and Data Mesh-style domain data products evolve toward ETSL Data Artifacts for its first cross-domain use cases?*

The focus is on:
- Incremental adoption over big-bang transformation
- Co-existence with existing practices and ownership structures
- Architectural correctness over short-term convenience
- Delivering **enterprise truth**, not just more data

This document is deliberately **not prescriptive about tooling or vendors**. The patterns described here are implementable across modern data platforms—whether built on cloud warehouses, streaming infrastructure, or hybrid architectures.

### Intended Audience

- **Enterprise and Platform Architects** — responsible for the overall data architecture and its evolution
- **Data Architects** — responsible for semantic modeling and governance structures
- **Senior Data Engineers** — responsible for implementing ingress, reconciliation, and state derivation
- **Transformation and Modernization Leads** — responsible for guiding incremental adoption

The document is written to be **architectural first**, with instructional guidance only where it materially aids execution. It assumes familiarity with:
- The distinction between ETSL Semantic Artifacts and ETSL Data Artifacts (see *Ontology vs ETSL Semantic vs ETSL Data Artifacts*)
- Authority modeling concepts (see *ETSL Authority Modeling Guidance for Architects*)
- Facts, Events, and State as distinct ETSL constructs

### What This Document Is Not

- **Not a semantic modeling primer** — foundational semantic concepts are covered in companion documents
- **Not a Data Mesh replacement** — ETSL complements Data Mesh; it does not subsume it
- **Not a Data Product engineering guide** — that guidance follows in *Building Data Products using ETSL Data Artifacts*
- **Not a tool- or vendor-specific implementation manual** — patterns are technology-agnostic

### How to Read This Document

Readers should approach this document in sequence on first reading. However, practitioners may return to specific sections during execution:

- **Sections 3–5**: Foundational understanding and terminology
- **Sections 6–8**: Identifying scope and designing ingress
- **Sections 9–10**: Authority and reconciliation (core ETSL mechanics)
- **Sections 11–13**: Building, validating, and operating early artifacts
- **Sections 14–16**: Scaling adoption and avoiding failure modes
- **Sections 17–18**: Preparation for Data Product engineering  

---

## 2. Positioning ETSL Data Artifacts in the Enterprise Journey

ETSL Data Artifacts sit **between** operational data sources and consumer-facing data products.

They are neither:
- raw ingested data, nor
- consumer- or use-case-aligned views.

They represent **enterprise truth**—normalized, authority-qualified, and reusable across domains.

### Where ETSL Data Artifacts Fit

In a mature enterprise data architecture:

```
┌─────────────────────────────────────────────────────────────┐
│  Data Products & Operational Applications                   │
│  (Consumer-facing, use-case-specific, interpretive)         │
└────────────────────────▲────────────────────────────────────┘
                         │ Consume and Interpret
┌────────────────────────┴────────────────────────────────────┐
│  ETSL Data Artifacts                                        │
│  (Enterprise truth: facts, relationships, state)            │
│  Authority-qualified, temporal, cross-domain reusable       │
└────────────────────────▲────────────────────────────────────┘
                         │ Normalize and Reconcile
┌────────────────────────┴────────────────────────────────────┐
│  Assertion Sources                                          │
│  (SORs, Domain Data Products, External Feeds)               │
│  Emit assertions; do not define enterprise truth            │
└─────────────────────────────────────────────────────────────┘
```

ETSL Data Artifacts establish a **stable truth substrate** that:
- Preserves semantic meaning across organizational boundaries
- Qualifies all assertions with authority and time
- Enables safe construction of data products without replicating reconciliation logic
- Supports regulatory and audit requirements natively

### Relationship to Other ETSL Documents

This document:
- **Builds directly on** *ETSL and Data Mesh: Co-existence, Complementarity, and Enterprise Evolution* — which establishes the co-existence philosophy and patterns for incremental adoption
- **Assumes familiarity with** *ETSL Authority Modeling Guidance for Architects* — which defines how authority is discovered, captured, and governed
- **Prepares the ground for** *Building Data Products using ETSL Data Artifacts* — which addresses how data products safely consume ETSL truth

Readers should not expect this document to re-explain foundational ETSL concepts. Where those concepts are essential, explicit cross-references are provided.

### Core Framing

> **ETSL Data Artifacts are not built green-field.  
> They are carved out of an existing, federated, and inconsistent data estate.**

This is not a weakness—it is the normal condition of every large bank. ETSL provides a disciplined way to introduce semantic clarity **incrementally**, without requiring a wholesale data transformation.

The key insight:

> *Enterprise truth is not discovered by cleaning up all the data.  
> It is constructed by making authority, time, and semantics explicit for a carefully chosen scope.*

ETSL Data Artifacts do not replace domain data products. They create a **shared semantic anchor** that domain products may—but are not required to—align with over time.

---

## 3. Reality Check: The Starting Point in Large Banks

Most large banks begin with:

- **Multiple Systems of Record (SORs) per domain** — Retail banking, corporate banking, treasury, and wealth management each maintain separate customer and account masters
- **Legacy data warehouses and lakes** — Often decades old, with accumulated business logic embedded in ETL and stored procedures
- **Domain-owned, source-aligned data products** — Published by domain teams for their own consumers, with local semantics
- **Embedded business logic in pipelines** — Transformations that quietly reconcile, deduplicate, or override without explicit authority
- **Implicit and undocumented authority** — No clear answer to "which system is right when they conflict?"
- **Conflicting definitions across teams** — "Customer" means different things to Retail, Corporate, and Compliance

### A Day in the Life: The Reality ETSL Addresses

Consider a typical scenario in a large bank.

A regulatory request arrives asking for consolidated exposure to a single corporate group. The request triggers a familiar sequence:

- The Risk team queries the credit system and finds exposure to three legal entities.
- The Corporate Banking team identifies five related entities in their client hierarchy, but two don't appear in the credit system.
- Treasury adds that one entity has derivative exposure not reflected in either system.
- Compliance notes that two entities were recently merged, but the core systems still treat them as separate.
- The data warehouse has a "golden customer" table, but it was built for retail, and the matching logic doesn't handle corporate hierarchies well.

Each team has done their job correctly. Each system holds valid data. Yet no one can answer the question without weeks of manual reconciliation, spreadsheet overlays, and escalation chains.

This is not a failure of any one system or team. It is the **natural outcome of federated evolution** in a complex organization.

ETSL does not propose to replace these systems or force a single schema. Instead, it provides a way to:
- Capture what each system asserts
- Make authority explicit
- Reconcile where needed, transparently
- Produce a defensible, auditable answer

The goal is not to eliminate complexity. The goal is to make complexity **visible, governed, and resolvable**.

### Concrete Banking Examples

**Party / Customer Identity**
- Core banking system holds retail customers
- CRM holds prospect and relationship data
- AML/KYC system holds identity verification status
- Corporate banking maintains separate legal entity hierarchies
- No single system owns "who is this customer across the bank"

**Account Ownership**
- Account opening happens in the core banking system
- Power of Attorney and joint ownership are managed in operations systems
- Beneficial ownership is tracked for compliance
- Different systems answer "who owns this account" differently

**Credit Limits**
- Underwriting system sets initial limits
- Credit Risk periodically reviews and adjusts
- Operations may apply temporary increases
- Collections may impose restrictions
- Each system believes it holds the authoritative limit

**Exposure Aggregation**
- Loan systems track outstanding balances
- Derivatives systems track counterparty exposure
- Treasury tracks liquidity positions
- No single view of "total exposure to Party X"

### Why This Is Normal

This fragmentation is not dysfunction—it is **normal organizational evolution**.

Each system was built to solve a real problem, by a real team, under real constraints. The resulting landscape reflects decades of acquisitions, regulatory mandates, product launches, and technology refreshes.

ETSL does not attempt to "clean everything up" upfront.

Instead, it introduces **a new layer of clarity**, selectively and incrementally—starting with the cross-domain truths that matter most.

---

## 4. Clarifying the Target: What an ETSL Data Artifact Is (and Is Not)

### ETSL Data Artifacts ARE

- **Explicit representations of enterprise facts, relationships, and state** — e.g., "Party P owns Account A since date T, under authority of Retail Operations"
- **Qualified by authority** — every assertion carries the enterprise function empowered to make it
- **Governed by temporal semantics** — effective dates, validity windows, and as-of-time queryability
- **Traceable to Assertion Sources** — lineage back to the SOR or domain product that emitted the original claim
- **Designed for cross-domain reuse** — the same Party identity artifact serves Retail, Corporate, Compliance, and Risk
- **Stable relative to consumer data products** — ETSL Data Artifacts change slowly; data products built on them may evolve freely

### ETSL Data Artifacts ARE NOT

- **Raw ingested SOR tables** — those are Assertion Sources, not truth
- **Domain source-aligned data products** — those serve domain-local needs and carry domain-local semantics
- **Aggregated metrics or KPIs** — those are derived interpretations, not foundational truth
- **Features or model inputs** — those are consumer-specific projections
- **Consumer-facing APIs or dashboards** — those interpret truth for specific audiences

### Banking Examples: Artifact vs Non-Artifact

| Concept | ETSL Data Artifact? | Why |
|---------|---------------------|-----|
| Party identity with authority-qualified name, DOB, and identifiers | ✅ Yes | Cross-domain truth, authority-qualified |
| Customer 360 dashboard | ❌ No | Consumer-facing interpretation |
| Account ownership relationship (Party → Account) with effective dates | ✅ Yes | Governed relationship, temporal, auditable |
| Account balance as of month-end | ❌ No | Derived metric / reporting view |
| Credit limit fact asserted by Credit Risk | ✅ Yes | Authority-qualified fact |
| Risk score for underwriting model | ❌ No | Feature / model input |

### Contrast Examples: Common Misconceptions

The following examples illustrate cases where teams often misjudge what belongs in ETSL.

**Example 1: "Current Balance" — Looks Like Truth, But Isn't**

A team proposes adding "current account balance" as an ETSL Data Artifact. After all, balance is a fundamental banking concept, and multiple systems need it.

*Why this is not an ETSL Data Artifact:*
- Balance is a continuously computed value, not an authority-qualified assertion
- It is derived from transactions, not asserted by an enterprise function
- Different consumers may need balance computed at different points in time (end-of-day, real-time, month-end)

*What belongs in ETSL instead:*
- The ownership relationship between Party and Account (authority-qualified, temporal)
- The account status (open, frozen, closed) with authority and effective dates
- The transactions themselves, if cross-domain truth about transaction history is needed

Balance is a **derived value** that belongs in data products, not in ETSL.

---

**Example 2: "Beneficial Owner" — Feels Inconvenient, But Correctly Belongs in ETSL**

A compliance team tracks beneficial ownership in their AML system. A data engineer suggests exposing this as a Domain Data Product rather than bringing it into ETSL, because "it's just a compliance concern."

*Why this correctly belongs in ETSL:*
- Beneficial ownership is a relationship asserted under regulatory authority
- It affects credit decisions, transaction monitoring, and reporting across domains
- Conflicts between stated ownership and beneficial ownership must be reconciled, not hidden

*The inconvenience:*
- Beneficial ownership relationships are complex (percentages, control vs ownership, layered structures)
- The compliance system uses domain-specific semantics that require normalization
- Reconciling with other ownership assertions requires explicit authority rules

Despite the inconvenience, beneficial ownership is **cross-domain truth** that must be governed centrally. The complexity is not a reason to avoid ETSL—it is the reason ETSL exists.

---

**Example 3: "Credit Limit Override" — Appears Transient, But Is Enterprise Truth**

Operations applies a temporary credit limit increase for a customer. A data engineer treats this as a transactional event that doesn't need ETSL treatment.

*Why this correctly belongs in ETSL:*
- The override changes what the enterprise accepts as the current limit
- It is asserted under Operations authority, distinct from the Risk-set limit
- Both the original limit and the override must be preserved for audit
- The relationship between them (override vs supersession) is semantically meaningful

*The inconvenience:*
- Overrides have temporal bounds (e.g., 30-day validity)
- They must be reconciled against risk-set limits when they expire
- Authority precedence must be explicitly modeled

Temporary does not mean unimportant. If an assertion affects enterprise decisions, it belongs in ETSL.

> **ETSL Data Artifacts represent what the enterprise accepts as true—not what is convenient to consume.**

The distinction matters because:
- **Data Products** may aggregate, filter, or reshape truth for specific use cases
- **ETSL Data Artifacts** must remain stable, authority-qualified, and semantically precise regardless of how they are consumed

---

## 5. Terminology for the Transition Phase (Normative)

To evolve an existing data estate toward ETSL, teams need **shared transitional vocabulary**.

The following terms are normative and should be used consistently across teams, documents, and systems.

### Key Terms

**Assertion Source**
> A system, Domain Data Product, or external feed that emits claims about enterprise reality.

- Examples: Core banking system, CRM, AML/KYC platform, external credit bureau feed
- Assertion sources are not truth by default—they emit candidates for reconciliation
- A single logical entity (e.g., "Customer") may have multiple Assertion Sources

**Candidate Assertion**
> A claim captured from an Assertion Source, prior to normalization or reconciliation.

- Preserves the original form and provenance
- Not yet authority-qualified
- May conflict with other candidate assertions for the same entity

**Normalized Assertion**
> A candidate assertion transformed to align with ETSL semantic contracts.

- Mapped to ETSL semantic types and vocabulary
- Carries attached authority
- Ready for reconciliation with other normalized assertions

**Derived Assertion**
> An assertion produced as a result of decisions, computations, or reconciliation—not directly emitted by an Assertion Source.

- Examples: "Authoritative credit limit after reconciliation," "Resolved beneficial owner"
- Must carry lineage to source assertions
- Authority is inherited or explicitly assigned

**Authority Registry**
> An explicit, governed mapping of entity types, fact types, and relationships to the enterprise functions empowered to assert them.

- Example entry: "CreditLimitFact → CreditRiskManagement (primary), RetailOperations (override)"
- The registry is semantic, not an IAM or RBAC system
- See *ETSL Authority Modeling Guidance for Architects* for governance

**Reconciliation Logic**
> The semantic rules that determine which assertions prevail when conflicts exist.

- Based on authority precedence, temporal validity, or explicit override rules
- Must be deterministic and auditable
- Is part of the ETSL semantic contract, not hidden in pipeline code

**ETSL Ingress Boundary**
> The controlled intake surface where assertions enter the ETSL domain.

- Responsible for: capture, provenance attachment, authority tagging, normalization
- Must NOT perform: reconciliation, business decisions, truth derivation
- Defines where "Assertion Source world" ends and "ETSL world" begins

### Why Shared Vocabulary Matters

Without consistent terminology:
- Teams reinvent concepts with different names
- Semantic intent is lost in translation
- Governance conversations collapse into confusion

These terms are not optional refinements—they are the **operating language** for ETSL adoption.

---

## 6. Identifying the First ETSL Use Cases

### Characteristics of Good Initial ETSL Scopes

Good initial ETSL use cases are:

- **Cross-domain by nature** — require coordination across organizational boundaries
- **High business or regulatory risk** — errors have material consequences
- **Known semantic disputes** — different teams already disagree on truth
- **Reused across multiple initiatives** — solving once avoids solving many times

Avoid starting with:
- Purely domain-local concerns (those are served by domain data products)
- Low-stakes analytics (those tolerate ambiguity)
- Concepts with no clear authority (those need governance work first)

### Banking-Oriented Examples

**Party / Customer Identity**
- Required by: AML, KYC, credit decisioning, relationship management, regulatory reporting
- Why ETSL: Multiple SORs assert identity; conflicts cause regulatory and operational risk
- Scope: Name, identifiers, identity verification status, beneficial ownership links

**Account Ownership and Control**
- Required by: Entitlements, transaction authorization, regulatory reporting, estate processing
- Why ETSL: Ownership is asserted by core banking, but control (POA, guardianship) lives elsewhere
- Scope: OWNS relationship, CONTROLS relationship, effective dates, authority

**Credit Limits**
- Required by: Underwriting, collections, fraud detection, real-time authorization
- Why ETSL: Limits are set by underwriting, adjusted by risk, overridden by operations—who is right?
- Scope: CreditLimitFact with authority, effective dates, override lineage

**Exposure Aggregation**
- Required by: Credit risk, counterparty risk, regulatory capital
- Why ETSL: Exposure spans loans, derivatives, guarantees—no single system holds the whole picture
- Scope: Party-level exposure facts, aggregated from multiple Assertion Sources

### Selection Criteria Checklist

Before selecting a use case, confirm:

| Criterion | Question |
|-----------|----------|
| Cross-domain | Does this require truth shared across multiple domains? |
| Risk | What is the cost of getting this wrong? |
| Conflict | Are there known disputes or inconsistencies today? |
| Reuse | Will multiple initiatives benefit from solving this once? |
| Authority | Can we identify who is empowered to assert truth? |

If any answer is unclear, the use case may need further scoping or governance work before ETSL adoption.

---

## 7. Mapping the Existing Data Estate to ETSL Concepts

### 7.1 Treating SORs as Assertion Sources

In ETSL:
- SORs **emit assertions**
- They **do not define enterprise truth** by default

This is a fundamental reframe. Most banks treat SORs as truth owners. ETSL recognizes that:
- Multiple SORs may assert conflicting statements about the same entity
- A SOR is authoritative only for what it is explicitly empowered to assert
- "Being a System of Record" does not confer universal truth-telling rights

**Example: Customer Identity**

| SOR | What It Asserts | Authority |
|-----|-----------------|-----------|
| Core Banking | Account holder name, address | Retail Operations |
| CRM | Relationship manager, segment | Sales |
| KYC Platform | Identity verification status | Compliance |
| Corporate Banking | Legal entity hierarchy | Corporate Ops |

Each system asserts what it knows. ETSL captures all assertions, tags authority, and reconciles where needed.

### 7.2 Consuming Domain Data Products

ETSL can consume **domain-published source-aligned data products**, not only raw SOR feeds.

This pattern:
- **Respects domain ownership** — domains remain accountable for their data quality
- **Reduces duplication** — ETSL does not rebuild what domains already publish
- **Lowers adoption friction** — domains are not asked to change their systems

**When to consume domain data products:**
- Domain already publishes a clean, documented source-aligned product
- Domain is willing to maintain stability and lineage
- ETSL team has visibility into domain product semantics

**When to consume raw SOR feeds:**
- No Domain Data Product exists
- Domain product adds transformations that obscure provenance
- Regulatory or audit requirements demand direct lineage to source

### Worked Example: Consuming a Domain Data Product for KYC Status

The Compliance domain owns the KYC platform and publishes a Source-Aligned Data Product called "Party Verification Status." This product includes:
- Party identifier
- Verification status (Verified, Pending, Failed, Expired)
- Verification date
- Verification authority (which regulatory regime)

The ETSL team needs Party verification status for cross-domain use cases: credit decisioning, transaction monitoring, and regulatory reporting.

**Option A: Consume raw KYC platform data**
- Requires direct integration with the KYC system
- ETSL team must understand KYC platform internals
- Changes to KYC platform schema require ETSL pipeline changes
- Compliance domain has no visibility into how their data is used

**Option B: Consume the Domain Data Product**
- ETSL consumes the published "Party Verification Status" product
- Compliance domain remains accountable for data quality and semantics
- Product contract provides stability; internal platform changes are absorbed by the domain
- Domain maintains lineage documentation that ETSL can reference

ETSL chooses Option B. At ingress:
- The domain product is consumed as an Assertion Source
- Authority is tagged as "Compliance" (the enterprise function, not the system)
- Provenance references the domain product, not the underlying platform
- Normalization maps domain vocabulary to ETSL semantic types

This approach:
- **Respects Data Mesh ownership** — Compliance owns their product; ETSL does not bypass them
- **Reduces friction** — No direct integration with domain systems required
- **Preserves semantic clarity** — Authority and provenance are explicit
- **Does not weaken ETSL semantics** — The assertion still carries authority, time, and lineage

For detailed patterns on ETSL and Data Mesh integration, see *ETSL and Data Mesh: Co-existence, Complementarity, and Enterprise Evolution*.

### 7.3 Mapping Patterns

For each Assertion Source, document:

| Aspect | What to Capture |
|--------|-----------------|
| Source type | SOR feed or Domain Data Product? |
| Entity scope | Which entities does this source assert? |
| Fact scope | Which facts or relationships? |
| Authority | Which enterprise function is this source acting on behalf of? |
| Temporal semantics | Does the source provide effective dates? |
| Conflict potential | Are other sources asserting the same facts? |

This mapping becomes input to the ETSL Ingress Layer design.

See *ETSL and Data Mesh: Co-existence, Complementarity, and Enterprise Evolution* for detailed patterns.

---

## 8. Designing the ETSL Ingress Layer

The ETSL Ingress Layer is the **controlled intake surface** where assertions enter the ETSL domain. It defines the boundary between "Assertion Source world" and "ETSL world."

### Purpose of the Ingress Layer

The ingress layer exists to:

| Function | Description |
|----------|-------------|
| **Capture assertions** | Receive data from SORs or domain products without loss |
| **Preserve provenance** | Record source, timestamp, and original form |
| **Attach authority** | Tag each assertion with the enterprise function it represents |
| **Normalize semantics** | Transform to ETSL vocabulary and semantic types |

### What Ingress Must NOT Do

Ingress is **semantic plumbing**, not intelligence.

| Anti-Pattern | Why It's Wrong |
|--------------|----------------|
| Infer missing authority | Authority must be explicit, not guessed |
| Resolve conflicts | Reconciliation is a separate, governed step |
| Apply business rules | Business decisions belong in reconciliation or state derivation |
| Filter "bad" data silently | All assertions should be captured; quality issues surface in validation |

### Normalization vs Semantic Interpretation (Critical Distinction)

The ingress layer performs **format normalization**, not **semantic interpretation**.

| Format Normalization (Allowed) | Semantic Interpretation (Not Allowed) |
|--------------------------------|---------------------------------------|
| Date format conversion (ISO 8601) | Deciding which date is "correct" |
| Character encoding standardization | Inferring meaning from text |
| Structural transformation to ETSL schema | Choosing between competing values |
| Semantic type tagging (based on explicit mapping) | Deriving semantic types from content |

**Format normalization** is mechanical, reversible, and governed by explicit mapping rules.  
**Semantic interpretation** constitutes truth-making and belongs in reconciliation.

> This distinction aligns with Tier-2's definition of ETSL Ingress Boundary: "Capture-only; No reconciliation or semantic interpretation; Provenance-preserving."

### Ingress Layer Responsibilities

**1. Capture**
- Accept data in source-native format
- Handle batch, streaming, or event-based ingestion
- Guarantee no data loss between source and ETSL

**2. Provenance Attachment**
- Record: source system, extraction timestamp, batch/event ID
- Preserve original payload (or reference) for audit

**3. Authority Tagging**
- Look up source in Authority Registry
- Attach the appropriate authority to each assertion
- Flag assertions where authority is ambiguous (for governance review)

**4. Normalization**
- Map source fields to ETSL semantic types
- Transform source vocabulary to ETSL vocabulary
- Validate structural conformance (not semantic correctness—that comes later)

> **Note:** For streaming ingress and out-of-order assertion handling, see *ETSL and Temporal Ordering* (`../../conceptual/etsl-and-temporal-ordering.md`).

### Example: Ingress for Customer Identity

```
Source: Core Banking System (CBS)
Authority: Retail Operations

CBS Record:
  cust_id: 12345
  name: "Jane Doe"
  dob: "1985-03-15"
  addr: "123 Main St"

After Ingress (Candidate Assertion):
  assertion_id: A-001
  source: CBS
  authority: RetailOperations
  captured_at: 2024-01-15T10:30:00Z
  entity_type: Party
  assertions:
    - predicate: LegalName
      value: "Jane Doe"
    - predicate: DateOfBirth
      value: "1985-03-15"
    - predicate: Address
      value: "123 Main St"
```

The candidate assertion is now ready for normalization and reconciliation downstream.

### Ingress Is Not One-Size-Fits-All

Different sources may require different ingress patterns:

| Source Type | Ingress Pattern |
|-------------|-----------------|
| Batch SOR extract | Scheduled capture, bulk provenance |
| Real-time event stream | Event-by-event capture, streaming normalization |
| Domain Data Product | API or file-based consumption, contract validation |
| External feed (e.g., credit bureau) | Adapter with external authority mapping |

### Common Early Mistakes in Ingress Design

Teams building their first ingress layers often make predictable mistakes. Understanding these helps avoid semantic damage that is costly to repair later.

**Mistake 1: Inferring Authority from Source System**

*Why teams do it:* It seems efficient—if data comes from the KYC system, authority must be Compliance. This avoids the overhead of maintaining an Authority Registry.

*Semantic damage:* Authority and source are not the same. A system may emit data on behalf of multiple authorities, or an authority may be exercised through multiple systems. Inferring authority embeds assumptions that will break when systems change, and makes audit explanations fragile.

**Mistake 2: Performing Reconciliation at Ingress**

*Why teams do it:* It feels natural to "clean up" conflicts early—why pass bad data downstream? Teams may deduplicate, merge, or pick "the best" value at ingress.

*Semantic damage:* Reconciliation is a governed, semantic act. Performing it silently at ingress hides authority decisions, destroys competing assertions, and makes the reconciliation logic invisible to governance. When auditors ask "why this value?", the answer is buried in ingress code.

**Mistake 3: Dropping "Incomplete" Assertions**

*Why teams do it:* If a source record is missing expected fields, it feels prudent to reject it. "Garbage in, garbage out."

*Semantic damage:* Incomplete assertions may still carry valuable truth. A party name without a date of birth is still a party name. Dropping assertions at ingress loses provenance and prevents downstream reconciliation from using partial information. Quality issues should surface in validation, not disappear silently.

**Mistake 4: Normalizing Too Aggressively**

*Why teams do it:* It seems helpful to standardize formats, merge similar values, or apply business rules early. This reduces downstream complexity.

*Semantic damage:* Over-normalization destroys information. Converting "Jane Doe" and "JANE DOE" to a canonical form loses the ability to trace back to the original assertion. Applying business rules (e.g., inferring account type from account number patterns) embeds assumptions that may not hold across all sources. Normalization should be structural, not semantic.

The key invariant: **every assertion entering ETSL carries source, authority, and time.**

---

### 8.6 Data Quality vs ETSL Quality: A Clear Boundary

A common question during ETSL adoption: *Does ETSL replace our data quality practices?*

**The answer is no.** ETSL and traditional Data Quality (DQ) are complementary, not competing. They operate at different layers and address different concerns.

---

#### The Boundary

| Concern | Owner | Where It Happens | Examples |
|---------|-------|------------------|----------|
| **Data Quality (DQ)** | Source systems, domain teams | Before ETSL ingress | Missing values, format errors, duplicates, referential integrity within source, timeliness of source feeds |
| **ETSL Quality** | ETSL Core | At and after ingress | Authority validation, semantic type conformance, temporal validity, reconciliation success, conflict rates |

**Source-aligned quality checks must exist before the ETSL ingress boundary.**

ETSL is concerned with **semantics and truth**—not the data sourcing problems that domain teams are responsible for resolving.

---

#### What ETSL Does Not Replace

- Completeness checks at source level
- Format validation and standardization at source
- Deduplication within source systems
- Referential integrity within domain boundaries
- Timeliness monitoring of source feeds
- Data profiling and anomaly detection at source

These remain the responsibility of source systems and domain data teams.

---

#### What ETSL Validates

At the ingress boundary, ETSL validates:

- **Authority**: Is the Assertion Source registered and valid for this assertion type?
- **Semantic conformance**: Does the assertion use defined semantic types correctly?
- **Temporal validity**: Are effective dates present and sensible?
- **Structural completeness**: Are ETSL-required fields (source, authority, time) present?

If an assertion fails ETSL validation, it is rejected with full provenance. **Remediation is the source team's responsibility.**

---

#### Two Distinct Metric Sets

| DQ Metrics (Source Team) | ETSL Quality Metrics (ETSL Team) |
|--------------------------|----------------------------------|
| Completeness at source | Reconciliation success rate |
| Format conformance | Conflict queue depth |
| Duplicate rate | Time-to-resolution for conflicts |
| Timeliness of feeds | Ingress rejection rate |
| Source-level referential integrity | SLA compliance for resolutions |

These are **not the same metrics** and should not be conflated. DQ metrics measure source health; ETSL Quality metrics measure semantic coherence and reconciliation health.

---

#### Alerts and Visibility

When ETSL rejects an assertion due to issues at the DQ/ETSL boundary (e.g., malformed data, missing authority), alerts are visible to **both** ETSL Operations and Source Domain teams.

- ETSL Operations monitors overall rejection rates and patterns
- Source teams are responsible for investigating and remediating their specific rejections

ETSL rejection rates can serve as a **signal** of upstream DQ issues, but ETSL does not own the remediation.

---

#### Anti-Pattern: Expecting ETSL to Fix DQ Problems

A common mistake is treating ETSL as a "cleaning layer" that will fix source data issues.

This fails because:
- ETSL is not designed for data transformation or cleansing
- Ingress is capture-only; semantic interpretation happens later
- Hiding DQ problems at the ETSL boundary destroys provenance

**If source data is broken, fix it at the source.** ETSL will reject it, preserve it in a dead-letter store, and alert—but it will not fix it.

---

## 9. Authority Modeling in Practice

Authority is the backbone of ETSL. Without explicit authority, assertions are just data—auditability, override handling, and conflict resolution all collapse.

### What Authority Represents

> **Authority is the enterprise function empowered to assert, override, or revoke a class of truth.**

Authority is:
- **Organizational and functional** — not a system, person, or team name
- **Stable over time** — survives system replacements and org changes
- **Auditable** — defensible to regulators and internal audit

For detailed guidance, see *ETSL Authority Modeling Guidance for Architects*.

### Discovering Authority in Practice

Authority is discovered from real organizational structures, not invented by data teams.

**Sources of authority discovery:**
- Delegation of authority matrices
- Risk and control frameworks
- Regulatory accountability mappings
- Policy ownership documents
- Audit and compliance charters

**Questions to ask:**
- Which function is accountable if this fact is wrong?
- Which function can override this assertion?
- Which function must defend this truth to a regulator?

### Worked Example: Credit Limit Authority

Credit limits are a classic multi-authority scenario.

**Assertion sources and their authorities:**

| Source | What It Asserts | Authority |
|--------|-----------------|-----------|
| Underwriting System | Initial credit limit at origination | CreditRiskManagement |
| Risk Review System | Periodic limit adjustments | CreditRiskManagement |
| Retail Operations | Temporary limit increases (customer request) | RetailOperations |
| Collections System | Limit restrictions for delinquent accounts | Collections |
| Fraud System | Emergency limit blocks | FraudOperations |

**Authority Registry Entry (Illustrative):**

```yaml
fact_type: CreditLimitFact
authorities:
  - authority: CreditRiskManagement
    can_assert: true
    can_override: true
    precedence: primary
  - authority: RetailOperations
    can_assert: true
    can_override: false
    precedence: secondary
    constraints:
      - temporal_limit: 30_days
      - requires_risk_approval_beyond_threshold: true
  - authority: Collections
    can_assert: true
    can_override: true
    precedence: override_in_context
    context: delinquency_active
  - authority: FraudOperations
    can_assert: true
    can_override: true
    precedence: emergency_override
```

**Key observations:**
- Multiple authorities can assert the same fact type
- Precedence rules determine which assertion prevails
- Some authorities have conditional or contextual override rights
- All of this is explicit and governed—not hidden in code

### Worked Example: Risk and Operations Both Assert Valid Truths

A customer with a $15,000 credit limit requests a temporary increase to $25,000 for a planned large purchase. Retail Operations approves the request and records the new limit in the operations system. Meanwhile, Credit Risk has not changed their assessed limit—they still consider $15,000 appropriate based on the customer's risk profile.

**What each authority asserts:**

*Credit Risk Management* asserts:
- Fact: CreditLimit = $15,000
- Effective from: 2024-01-01
- Basis: Risk assessment, income verification, credit score

*Retail Operations* asserts:
- Fact: CreditLimit = $25,000
- Effective from: 2024-06-01
- Effective to: 2024-07-01 (30-day temporary increase)
- Basis: Customer request, relationship manager approval

**Why both assertions are valid:**

Both assertions are legitimate exercises of authority:
- Credit Risk is empowered to set risk-based limits
- Retail Operations is empowered to grant temporary increases within policy bounds

Neither assertion is "wrong." They represent different aspects of enterprise reality:
- The risk-assessed limit (what Risk believes is appropriate)
- The operational limit (what the customer can actually use right now)

**How ETSL records both without forcing convergence:**

ETSL captures both assertions as facts:

```
Fact F1:
  subject: Account A-123
  predicate: CreditLimit
  value: 15000
  effective_from: 2024-01-01
  authority: CreditRiskManagement

Fact F2:
  subject: Account A-123
  predicate: CreditLimit
  value: 25000
  effective_from: 2024-06-01
  effective_to: 2024-07-01
  authority: RetailOperations
  relationship_to_F1: temporary_override
```

Current state derivation applies precedence rules:
- During June 2024: Operational limit ($25,000) is current (temporary override active)
- After July 2024: Risk limit ($15,000) becomes current again (override expired)

Both facts remain in ETSL. Neither is deleted or "corrected." The relationship between them is explicit.

This approach:
- Preserves the full audit trail
- Allows "as-of" queries at any point in time
- Makes authority visible to regulators and auditors
- Does not require Risk and Operations to agree on a single number

### Building the Authority Registry Incrementally

For early ETSL adoption:

1. **Start narrow** — cover only the facts and relationships in scope
2. **Be explicit** — if authority is unclear, flag it for governance resolution
3. **Avoid system names** — systems act on behalf of authority; they are not authority
4. **Version the registry** — authority evolves; changes must be tracked

A v1 Authority Registry for a bank might have 10–20 entries. That is sufficient to demonstrate value and establish the pattern.

---

## 10. Reconciliation and Normalization Patterns

Reconciliation is unavoidable in any enterprise with multiple Assertion Sources. ETSL makes reconciliation **explicit, governed, and auditable**—rather than hidden in pipeline logic.

### Core Principle

> **Reconciliation is a semantic act, not a technical merge.**

Reconciliation must answer:
- Which assertion prevails?
- Why does it prevail?
- Who is accountable for this decision?

If reconciliation logic cannot answer these questions, it is not ETSL-compliant.

### Common Reconciliation Patterns

**Pattern 1: Authority Precedence**

When multiple authorities assert the same fact, precedence rules determine which prevails.

```
If CreditRiskManagement and RetailOperations both assert CreditLimit:
  → Prefer CreditRiskManagement (higher precedence)
  → Preserve RetailOperations assertion for audit
```

**Pattern 2: Temporal Validity**

When assertions have overlapping or conflicting effective dates, temporal rules apply.

```
If two assertions cover the same time period:
  → Use assertion with later effective_from (most recent truth)
  → Or use assertion with higher authority precedence
```

**Pattern 3: Explicit Overrides**

Some assertions explicitly override others—this must be captured, not inferred.

```
If Collections asserts a limit restriction:
  → This is an override, not a conflict
  → Original limit remains for audit; override is current truth
  → Override carries lineage to what it overrides
```

**Pattern 4: Contextual Authority**

Authority may vary by context (e.g., delinquency, fraud, regulatory hold).

```
If account is in delinquency context:
  → Collections authority takes precedence over RetailOperations
  → Context must be explicitly modeled, not inferred
```

### A Story of Reconciliation: Account Ownership Through Time

The following narrative illustrates how ETSL reconciliation works in practice, following a single account through a sequence of real events.

**January 15:** Maria opens a savings account at the bank. The core banking system records Maria as the sole owner. ETSL captures this as an ownership assertion from Retail Operations, effective January 15.

**March 1:** Maria adds her husband Carlos as a joint owner. The operations system records the joint ownership. ETSL captures a new assertion: Carlos now co-owns the account, effective March 1. Maria's original ownership assertion remains—it is not overwritten.

**June 10:** Maria passes away. The estate processing system records Maria's death and initiates ownership transfer. ETSL captures an assertion from Estate Operations: Maria's ownership ends effective June 10. Carlos remains as owner.

**July 5:** A dispute arises. Carlos's attorney claims the joint ownership was never properly documented. The legal department issues a hold. ETSL captures an assertion from Legal: ownership status is "disputed," effective July 5. This is an override—it does not delete prior assertions, but it changes what the enterprise treats as current truth for operational purposes.

**August 20:** The dispute is resolved in Carlos's favor. Legal lifts the hold. ETSL captures an assertion: dispute resolved, Carlos confirmed as sole owner, effective August 20.

**What ETSL now contains:**

All five assertions are preserved:
1. Maria opens account (Retail Operations, Jan 15)
2. Carlos added as joint owner (Retail Operations, Mar 1)
3. Maria's ownership ends (Estate Operations, Jun 10)
4. Ownership disputed (Legal, Jul 5)
5. Dispute resolved, Carlos confirmed (Legal, Aug 20)

**What current state shows:**

As of today, ETSL derives that Carlos is the sole owner. But any historical query can be answered:
- "Who owned this account on February 1?" → Maria (sole owner)
- "Who owned this account on April 1?" → Maria and Carlos (joint owners)
- "Who owned this account on July 10?" → Disputed (Legal hold active)
- "Who owned this account on September 1?" → Carlos (sole owner, confirmed)

**Why this matters:**

A regulator asks: "Explain the ownership history of this account." The bank can answer immediately, with full authority attribution and temporal precision—without replaying transactions or consulting multiple systems.

This is what ETSL reconciliation enables: **truth over time, with accountability at every step.**

---

### Worked Example: Multi-Authority Credit Limit Reconciliation

**Scenario:**

An account has the following credit limit assertions:

| Assertion | Authority | Effective From | Value |
|-----------|-----------|----------------|-------|
| A1 | CreditRiskManagement | 2024-01-01 | $20,000 |
| A2 | RetailOperations | 2024-02-15 | $25,000 |
| A3 | Collections | 2024-03-01 | $5,000 |

**Reconciliation Logic (Illustrative):**

```
1. Check for override assertions:
   - A3 is from Collections (override authority in delinquency context)
   - Account is in delinquency → A3 is an active override

2. Determine current authoritative state:
   - Current limit: $5,000 (A3)
   - Override reason: Delinquency restriction
   - Original limit (for recovery): $20,000 (A1)

3. Preserve all assertions:
   - A1, A2, A3 are all retained
   - Current state is derived, not by deleting A1 or A2
```

**Resulting ETSL State (Illustrative):**

```yaml
entity: Account
account_id: A-789
current_credit_limit:
  value: 5000
  authority: Collections
  effective_from: 2024-03-01
  override_of: A1
  override_reason: delinquency_restriction
prior_assertions:
  - assertion_id: A1
    value: 20000
    authority: CreditRiskManagement
  - assertion_id: A2
    value: 25000
    authority: RetailOperations
```

### What Reconciliation Must NOT Do

| Anti-Pattern | Why It's Wrong |
|--------------|----------------|
| "Last write wins" | Ignores authority; creates non-deterministic truth |
| Delete conflicting assertions | Destroys audit trail |
| Infer authority from source | Authority must be explicit |
| Encode rules in SQL | Reconciliation logic must be governed, not hidden |

### Normalization vs Reconciliation

These are distinct steps:

| Step | Purpose | When |
|------|---------|------|
| **Normalization** | Transform to ETSL vocabulary and semantic types | At ingress |
| **Reconciliation** | Resolve conflicts and derive authoritative state | After normalization |

Normalization is largely mechanical. Reconciliation is semantic and governed.

---

## 11. Reconciliation Failure and Error Handling

Reconciliation does not always succeed. When multiple assertions conflict and cannot be automatically resolved, the system must handle the failure explicitly—not silently propagate ambiguity downstream.

This section provides guidance on **semantic error handling** for reconciliation failures and related assertion-level errors.

> **Scope Note:** This section addresses semantic error handling only. Technical infrastructure concerns (retries, circuit breakers, failover, platform resilience) are outside the scope of this document and belong to platform engineering guidance.

---

### 11.1 Core Principle: Don't Right-Shift Problems

ETSL's error handling philosophy is **fail fast, fail loud**:

- If an assertion cannot be validated, reject it at ingress
- If reconciliation cannot produce a deterministic result, stop and alert
- If authority is missing or unknown, do not proceed
- Never silently propagate ambiguity to downstream consumers

> **Problems that are deferred become problems that are hidden.**  
> Hidden problems become audit failures, regulatory findings, and production incidents.

---

### 11.2 Error Classification

ETSL distinguishes between errors that should **break the flow** and errors that allow **graceful continuation**:

| Error Class | Example | Response | Flow |
|-------------|---------|----------|------|
| **Validation Failure** | Missing required attribute, malformed assertion | Reject at ingress | Break |
| **Missing Authority** | Assertion from unregistered source | Reject; route to Authority Registry review | Break |
| **Semantic Inadequacy** | Assertion uses undefined semantic type | Reject; escalate to Semantic Architect | Break |
| **Reconciliation Conflict** | Two valid authorities assert conflicting values | Apply reconciliation pattern (see below) | Pattern-dependent |
| **Temporal Collision** | Overlapping effective periods for exclusive facts | Validate against semantic model; escalate if ambiguous | Break |
| **Stale Assertion** | Assertion arrives after superseding assertion processed | Apply based on effective time, not arrival time | Continue |

---

### 11.3 Reconciliation Failure Patterns

When reconciliation cannot produce a deterministic result (e.g., two authorities of equal precedence assert conflicting values), one of two patterns applies.

**The pattern is declared per attribute, fact, or relationship in the ETSL Semantic Artifact—not at the entity or domain level.**

---

#### Pattern B: Last-Known-Good Fallback

| Aspect | Behavior |
|--------|----------|
| **State emission** | Last successfully reconciled state remains authoritative |
| **Conflicting assertions** | Quarantined for resolution |
| **Consumer visibility** | Consumers see stable (potentially stale) truth |
| **Alert** | Persistent alert to Data Engineering and Operations |
| **Resolution** | Manual or policy-based intervention required |

**When to use:**
- Attributes where temporary staleness is acceptable
- Operational convenience data (e.g., preferred contact channel)
- Low-criticality facts that do not drive decisions

**Banking example:**
> A customer's `relationship_manager_id` is asserted differently by CRM and Core Banking. Pattern B applies: the last-known-good assignment remains visible while the conflict is quarantined. Operations receives an alert with SLA.

---

#### Pattern C: Conservative Rejection

| Aspect | Behavior |
|--------|----------|
| **State emission** | No state emitted until reconciliation succeeds |
| **Conflicting assertions** | Block state derivation |
| **Consumer visibility** | Consumers receive no update (or explicit "unavailable" status) |
| **Alert** | Persistent alert to Data Engineering and Operations |
| **Resolution** | Must be resolved before downstream consumption |

**When to use:**
- High-integrity attributes (regulatory, compliance, financial exposure)
- Facts that drive automated decisions
- Attributes where staleness creates risk

**Banking example:**
> A customer's `aml_verification_status` is asserted as VERIFIED by the KYC system and PENDING by the AML system. Pattern C applies: no state is emitted until the conflict is resolved. Downstream credit decisions that depend on AML status will not proceed with stale or ambiguous data.

---

#### Default Pattern

**The default reconciliation pattern is Conservative Rejection (Pattern C).**

This reflects the principle: don't shift problems to the right. Attributes that tolerate staleness must explicitly opt into Pattern B.

---

### 11.4 Declaring Patterns in Semantic Artifacts

Reconciliation patterns are declared per attribute in the ETSL Semantic Artifact:

```yaml
artifact_type: etsl_semantic_state
entity: Account
version: 2.1.0

attributes:
  account_status:
    semantic_type: AccountStatus
    required: true
    reconciliation_pattern: conservative_rejection  # Pattern C (default)
    resolution_sla: 4_hours
    
  credit_limit:
    semantic_type: MoneyAmount
    required: true
    reconciliation_pattern: conservative_rejection  # Pattern C
    resolution_sla: 2_hours
    
  preferred_contact_channel:
    semantic_type: ChannelCode
    required: false
    reconciliation_pattern: last_known_good  # Pattern B
    resolution_sla: 24_hours
    
  relationship_manager_id:
    semantic_type: EmployeeId
    required: false
    reconciliation_pattern: last_known_good  # Pattern B
    resolution_sla: 48_hours
```

Every attribute with a reconciliation pattern MUST have a `resolution_sla` indicating the time within which conflicts must be resolved.

---

### 11.5 Resolution SLAs

Every reconciliation conflict triggers an alert with an associated SLA.

| SLA Component | Description |
|---------------|-------------|
| **resolution_sla** | Time within which the conflict must be resolved |
| **Alert recipients** | Data Engineering and Operations teams |
| **Escalation** | Defined per enterprise policy (e.g., escalate to Data Architect after 50% of SLA) |

**SLA breach does not change system behavior.** If Pattern B is declared, the last-known-good remains visible regardless of SLA status. SLA breach is a governance and operational concern, not a semantic one.

The semantic model already declared tolerances. SLAs enforce operational discipline, not semantic behavior.

---

### 11.6 Ingress-Level Rejections

Certain errors are detected and rejected at the ETSL ingress boundary before reconciliation:

| Error | Detection Point | Response |
|-------|-----------------|----------|
| Malformed assertion (missing required fields) | Ingress validation | Reject; emit to dead-letter with full provenance |
| Unknown Assertion Source | Authority check | Reject; route to Authority Registry for review |
| Undefined semantic type | Schema validation | Reject; escalate to Semantic Architect |
| Invalid temporal semantics (e.g., effective_from in future for past event) | Temporal validation | Reject; emit to dead-letter |

All rejections MUST:
- Preserve the original assertion with full provenance
- Emit to a governed dead-letter store
- Trigger alerts with SLAs
- Be queryable for audit and remediation

---

### 11.7 Error Lineage and Traceability

Errors are first-class events in ETSL. Every error MUST carry:

| Field | Purpose |
|-------|---------|
| `error_id` | Unique identifier |
| `error_type` | Classification (validation, authority, reconciliation, temporal) |
| `source_assertions` | Original assertion(s) that triggered the error |
| `detection_time` | When the error was detected |
| `semantic_artifact_version` | Which semantic version was used for validation |
| `resolution_status` | OPEN, IN_PROGRESS, RESOLVED, ESCALATED |
| `resolution_sla` | Deadline for resolution |
| `resolution_details` | How and when resolved (populated after resolution) |

Error records are **immutable and append-only**. Resolution creates a new record linking to the original error.

---

### 11.8 Banking Examples: End-to-End Scenarios

#### Scenario 1: Credit Limit Conflict

**Situation:** The Underwriting system asserts `credit_limit = $50,000`. The Risk system asserts `credit_limit = $30,000`. Both are valid authorities for this attribute.

**Semantic declaration:** `credit_limit` is `conservative_rejection` with 2-hour SLA.

**Behavior:**
1. Reconciliation detects conflict
2. No `credit_limit` state is emitted
3. Alert sent to Data Engineering and Operations
4. Downstream Data Products querying credit limit receive "UNAVAILABLE" or no update
5. Resolution: Risk and Underwriting teams clarify; one assertion is withdrawn or authority precedence is established
6. Once resolved, reconciliation succeeds and state is emitted

---

#### Scenario 2: Customer Identity Mismatch

**Situation:** AML/KYC system asserts customer is VERIFIED. Core Banking asserts customer is PENDING_VERIFICATION.

**Semantic declaration:** `verification_status` is `conservative_rejection` with 4-hour SLA.

**Behavior:**
1. Reconciliation detects conflict
2. No `verification_status` state is emitted
3. Alert sent with 4-hour SLA
4. Credit decisions that depend on verification status cannot proceed
5. Resolution: Compliance team investigates; correct status is established
6. State is emitted after resolution

---

#### Scenario 3: Preferred Channel Disagreement

**Situation:** CRM asserts `preferred_channel = EMAIL`. Contact Center system asserts `preferred_channel = SMS`.

**Semantic declaration:** `preferred_channel` is `last_known_good` with 24-hour SLA.

**Behavior:**
1. Reconciliation detects conflict
2. Last-known-good value (e.g., EMAIL from prior state) remains authoritative
3. Conflicting assertions are quarantined
4. Alert sent with 24-hour SLA
5. Downstream systems continue to see EMAIL
6. Resolution: Data steward reviews and determines authoritative source
7. Once resolved, new state reflects resolved value

---

#### Scenario 4: Unknown Assertion Source

**Situation:** An assertion arrives from a system not registered in the Authority Registry.

**Behavior:**
1. Ingress validation detects unknown source
2. Assertion is rejected
3. Full assertion preserved in dead-letter store with provenance
4. Alert sent to Authority Registry owner
5. Resolution: Either register the source as valid authority, or identify as erroneous emission
6. If registered, assertion can be replayed

---

### 11.9 Monitoring and Alerting

Operational teams should monitor:

| Metric | What It Indicates |
|--------|-------------------|
| **Reconciliation success rate** | Overall health of assertion alignment |
| **Conflict queue depth** | Volume of unresolved conflicts |
| **Time-to-resolution** | How quickly conflicts are being resolved |
| **SLA breach rate** | Governance discipline |
| **Dead-letter queue growth** | Ingress-level rejection trends |
| **Pattern B staleness duration** | How long last-known-good values persist |

Alert thresholds are domain- and attribute-specific, defined during semantic modeling.

---

### 11.10 Summary: Error Handling Principles

1. **Fail fast, fail loud** — Don't propagate ambiguity downstream
2. **Pattern per attribute** — Reconciliation behavior is declared in the Semantic Artifact
3. **Default to conservative rejection** — Attributes must opt into staleness tolerance
4. **Every conflict has an SLA** — Resolution timelines are explicit and monitored
5. **Errors are first-class** — Full lineage, provenance, and resolution tracking
6. **Technical infrastructure is out of scope** — This is semantic error handling, not platform resilience

---

## 12. Producing the First ETSL Data Artifacts

The first ETSL Data Artifacts set the pattern for everything that follows. Getting them right—even if narrow in scope—is more valuable than getting them fast.

### Characteristics of a v1 ETSL Data Artifact

A v1 artifact should:

| Characteristic | Why It Matters |
|----------------|----------------|
| **Narrow concept** | Reduces complexity; allows focused governance |
| **Clear authority** | Demonstrates ETSL's core value proposition |
| **Time-aware** | Enables as-of queries and audit |
| **Reused by 2+ initiatives** | Proves cross-domain value |
| **Correct, even if incomplete** | Establishes trust; avoids early credibility loss |

### The First 90 Days: What Teams Actually Do

ETSL adoption follows a predictable rhythm. Here is what realistic progress looks like:

**Weeks 1–4: Foundation**
- Select 1–2 cross-domain use cases (see Section 6)
- Identify 2–4 Assertion Sources for those use cases
- Draft initial Authority Registry entries
- Design ingress layer for selected sources
- Establish team structure and review rituals

**Weeks 5–8: First Artifacts**
- Implement ingress for selected sources
- Produce first candidate assertions
- Implement normalization to ETSL semantic types
- Produce first normalized assertions
- Begin reconciliation design (even if simple precedence rules)

**Weeks 9–12: Validation and Demonstration**
- Produce first ETSL Data Artifacts (e.g., Party identity, Account ownership)
- Validate with domain SMEs and architects
- Demonstrate to at least one consuming initiative
- Document lessons learned
- Refine authority and reconciliation rules based on real feedback

### Example First Artifacts in Banking

| Artifact | Scope | Complexity |
|----------|-------|------------|
| Party Identity State | Name, identifiers, verification status | Medium |
| Account Ownership Relationship | Party → Account with effective dates | Low |
| Credit Limit Fact | Limit value with authority | Medium |
| Party-to-Party Relationship | Beneficial owner, guardian, signatory | Medium-High |

Start with lower-complexity artifacts to build confidence and momentum.

### Good v1 vs Over-Ambitious: A Credit Limit Example

**The Over-Ambitious Approach**

A team decides their first ETSL artifact will be "Enterprise Credit Exposure." They scope it to include:
- Credit limits across all products (cards, loans, lines of credit, overdrafts)
- Utilized amounts and available credit
- Limit adjustments from all sources (underwriting, risk, operations, collections, fraud)
- Aggregated exposure at party, household, and corporate hierarchy levels
- Real-time and batch reconciliation
- Integration with five different source systems

After three months, the team has:
- Incomplete ingress from two of five systems
- Ongoing disputes about authority between Risk and Operations
- No consuming initiative willing to commit to the unstable artifact
- Growing skepticism from stakeholders about ETSL's value

The artifact is technically impressive but semantically incomplete. It cannot be trusted.

**The Good v1 Approach**

A different team decides their first ETSL artifact will be "Credit Card Limit Fact." They scope it to include:
- Credit limit for card accounts only
- Limit assertions from two sources: Underwriting (initial) and Risk Review (adjustments)
- Authority modeled for these two sources only
- Effective dates for each assertion
- Simple precedence rule: Risk Review supersedes Underwriting

After three months, the team has:
- Complete ingress from both sources
- A working Authority Registry with two entries
- One consuming initiative (fraud detection) actively using the artifact
- Documented reconciliation logic
- Confidence from stakeholders that ETSL works

The artifact is narrow but correct. It can be trusted—and extended.

**The Difference**

| Dimension | Over-Ambitious | Good v1 |
|-----------|----------------|---------|
| Scope | All credit products | One product type |
| Sources | Five systems | Two systems |
| Authority | Disputed | Clear and documented |
| Consumer | None committed | One active user |
| Trust | Low (incomplete) | High (correct) |

**Lesson:** A narrow, correct artifact that is actually used is worth far more than an ambitious artifact that is never finished. Scope for correctness, not coverage.

### What "Done" Looks Like for v1

A v1 ETSL Data Artifact is "done" when:

1. **Lineage is complete** — traceable from artifact back to Assertion Sources
2. **Authority is explicit** — every fact/relationship carries its authority
3. **Temporal semantics are present** — effective dates, validity windows
4. **At least one consumer is using it** — validates cross-domain reuse
5. **Validation has passed** — semantic correctness, authority consistency, temporal coherence
6. **Documentation exists** — semantic contract, authority rules, reconciliation logic

---

## 13. Validating ETSL Data Artifacts

Validation is not optional. Without explicit validation, ETSL Data Artifacts lose their claim to "enterprise truth."

### Validation Dimensions

| Dimension | What It Checks | Example Failure |
|-----------|----------------|-----------------|
| **Semantic correctness** | Do assertions conform to ETSL semantic contracts? | AccountStatus value not in allowed set |
| **Authority consistency** | Does every assertion carry valid authority? | CreditLimitFact asserted by unknown authority |
| **Temporal coherence** | Are effective dates present and valid? | Ownership relationship with no effective_from |
| **Referential integrity** | Do relationships reference valid entities? | OWNS relationship referencing non-existent Party |
| **Invariant compliance** | Do state records satisfy ETSL invariants? | Account with no owner |

### Validation Is Collaborative

Validation is not a gate owned by a single team. It requires:

| Role | Validation Responsibility |
|------|---------------------------|
| **ETSL Core Team** | Semantic contract compliance, authority consistency |
| **Domain SMEs** | Business correctness, conflict identification |
| **Data Engineers** | Technical integrity, lineage completeness |
| **Consuming Initiatives** | Fitness for purpose, cross-domain coherence |

### Validation Checks (Illustrative)

**Semantic Correctness**
```
For each assertion:
  - Is the predicate defined in ETSL semantic model?
  - Is the value conformant to the semantic type?
  - Are required attributes present?
```

**Authority Consistency**
```
For each assertion:
  - Is the authority in the Authority Registry?
  - Is this authority permitted to assert this fact type?
  - Are override permissions respected?
```

**Temporal Coherence**
```
For each assertion:
  - Is effective_from present?
  - If effective_to is present, is it after effective_from?
  - Are there overlapping validity periods that violate invariants?
```

### What to Do When Validation Fails

| Failure Type | Response |
|--------------|----------|
| Data error | Fix at source or ingress; do not persist invalid assertion |
| Pipeline error | Fix pipeline; re-run ingress |
| Semantic model gap | Escalate to architects; evolve semantic model if needed |
| Authority ambiguity | Escalate to governance; resolve before persisting |

> **Invalid ETSL Data Artifacts are worse than missing data.** They undermine trust in the entire layer.

### Continuous Validation

Validation is not a one-time event. Implement:
- **Ingress-time validation** — catch errors early
- **Reconciliation-time validation** — ensure derived state is coherent
- **Periodic audits** — detect drift and degradation

---

## 14. Operating Model During Early ETSL Adoption

ETSL is not just a technical layer—it requires an operating model that sustains semantic clarity over time. Without governance rituals, ETSL degrades into another set of pipelines.

### Team Structure

**ETSL Core Team (Small and Focused)**
- 1–2 ETSL Semantic Architects
- 1–2 Senior Data Engineers
- Part-time governance/compliance liaison

The core team does not own all ETSL work—it owns the **semantic contracts and governance**.

**Domain Contributors (Federated)**
- Domain architects participate in authority modeling and reconciliation design
- Domain engineers implement ingress adapters for their sources
- Domain SMEs validate semantic correctness

### Roles and Responsibilities

| Role | Owns | Does Not Own |
|------|------|--------------|
| ETSL Semantic Architect | Semantic contracts, Authority Registry, reconciliation rules | Pipeline implementation |
| ETSL Data Engineer | Ingress, normalization, state derivation pipelines | Semantic definitions |
| Domain Architect | Domain-specific authority, source-aligned products | Cross-domain reconciliation |
| Domain Engineer | Ingress adapters, domain product maintenance | ETSL core infrastructure |

### Typical Tensions and How Rituals Resolve Them

ETSL adoption creates predictable friction between roles. Understanding these tensions—and designing rituals to address them—prevents escalation and builds trust.

**Tension 1: Central Architects vs Domain Teams**

*What happens:* ETSL architects define semantic contracts that domain teams find impractical. Domain teams feel dictated to; architects feel ignored.

*Root cause:* Architects may not understand domain constraints. Domains may not understand cross-domain requirements.

*How rituals help:* The **Assertion Onboarding Review** brings both parties together before implementation. Domain architects explain their constraints; ETSL architects explain cross-domain needs. Compromises are negotiated, not imposed.

**Tension 2: ETSL Architects vs Data Engineers**

*What happens:* Architects define semantic rules that engineers find impossible to enforce in pipelines. Engineers implement workarounds that drift from semantic intent.

*Root cause:* Semantic contracts may be too abstract. Engineers may lack visibility into why rules exist.

*How rituals help:* The **Reconciliation Review** includes both roles. Engineers surface enforcement challenges; architects clarify intent or adjust rules. The result is a semantic contract that can actually be implemented.

**Tension 3: Domain Teams vs Central Governance**

*What happens:* Domain teams see ETSL as "central IT" imposing overhead. They build shadow paths or delay engagement.

*Root cause:* ETSL is perceived as a gate, not a service. Governance feels bureaucratic rather than helpful.

*How rituals help:* Keeping rituals **lightweight and proportional** (hours, not weeks) prevents the perception of bureaucracy. The **Semantic Health Check** is quarterly, not weekly—enough to catch drift without constant overhead.

**Tension 4: Speed vs Correctness**

*What happens:* Teams under delivery pressure want to ship quickly. ETSL insists on authority modeling and validation. Friction results.

*Root cause:* Short-term delivery incentives conflict with long-term semantic stability.

*How rituals help:* By making governance **explicit and predictable**, teams can plan for it. The overhead is known upfront, not discovered as a surprise gate. And the v1 "narrow and correct" philosophy (see Section 11) gives teams a path to early delivery without compromising integrity.

### Required Rituals

Without rituals, ETSL decays. Establish early:

**1. Assertion Onboarding Review**
- When: Each new Assertion Source is added
- Who: ETSL architect, domain architect, data engineer
- Output: Approved ingress design, authority mapping

**2. Authority Review**
- When: New facts or relationships are added; conflicts emerge
- Who: ETSL architect, governance liaison, domain SMEs
- Output: Updated Authority Registry

**3. Reconciliation Review**
- When: New reconciliation rules are proposed; unexpected conflicts surface
- Who: ETSL architect, domain architects
- Output: Documented reconciliation logic

**4. Semantic Health Check (Quarterly)**
- When: Every quarter
- Who: ETSL core team, key domain representatives
- Output: Drift detection, backlog prioritization, lessons learned

### Governance vs Bureaucracy

ETSL governance should be:
- **Lightweight** — rituals take hours, not weeks
- **Explicit** — decisions are recorded and traceable
- **Proportional** — governance intensity matches risk

Avoid:
- Multi-week approval cycles for minor changes
- Governance bodies that never meet
- Rituals that exist on paper but not in practice

### Scaling the Operating Model

Early ETSL adoption (1–2 use cases) requires minimal structure:
- Core team of 3–4
- 2–3 rituals
- One governance forum

As ETSL grows:
- Add domain-embedded ETSL liaisons
- Establish formal semantic stewardship per domain
- Automate validation and drift detection

---

## 15. Co-existence with Existing Data Products

ETSL is designed for co-existence, not replacement. Domain data products continue to serve domain needs. ETSL provides a shared semantic anchor for cross-domain truth—nothing more.

### Core Principle

> **ETSL does not disrupt domain products. Engagement is opt-in and use-case driven.**

Domains are not required to:
- Rewrite their existing data products
- Abandon their source-aligned semantics
- Route all data through ETSL

Domains may choose to:
- Publish source-aligned products that ETSL consumes
- Align their semantics with ETSL over time
- Consume ETSL Data Artifacts for cross-domain use cases

### Co-existence Patterns

**Pattern 1: Domain Products Feed ETSL**

```
Domain SOR → Domain Source-Aligned Product → ETSL Ingress → ETSL Data Artifact
```

- Domain retains ownership of its product
- ETSL consumes the product as an Assertion Source
- No changes required to domain systems

**Pattern 2: ETSL and Domain Products in Parallel**

```
Domain SOR → Domain Source-Aligned Product → Domain Consumers
     └──────→ ETSL Ingress → ETSL Data Artifact → Cross-Domain Consumers
```

- Domain product serves domain-local use cases
- ETSL Data Artifact serves cross-domain use cases
- No forced convergence

**Pattern 3: Gradual Alignment**

```
Time T1: Domain Product uses domain-local semantics
Time T2: Domain Product aligns vocabulary to ETSL where practical
Time T3: Domain Product declares conformance to ETSL semantic types
```

- Alignment happens voluntarily, over time
- Driven by demonstrated value, not mandate

### What Triggers ETSL Engagement?

ETSL engagement is triggered by **need**, not ideology:

| Trigger | Example |
|---------|---------|
| Cross-domain dependency | Risk needs customer data from Retail and Corporate |
| Conflict resolution | Two systems disagree on credit limit |
| Regulatory requirement | Regulator asks for consolidated view of party exposure |
| Audit failure | Unable to explain why a decision was made |
| Data product proliferation | Multiple teams building the same thing differently |

If none of these triggers exist, the domain can continue without ETSL involvement.

### Explaining Co-existence to Stakeholders

> *"Domain data products continue to serve domain needs. ETSL provides a shared semantic anchor for cross-domain truth. Domains are not required to change—they are invited to align when cross-domain use cases demand it."*

This framing reduces resistance and builds trust.

For detailed patterns, see *ETSL and Data Mesh: Co-existence, Complementarity, and Enterprise Evolution*.

---

## 16. Anti-Patterns to Avoid Early

ETSL adoption fails in predictable ways. Understanding **why** teams fall into these patterns—and the **damage** they cause—helps prevent them.

---

### Anti-Pattern 1: Modeling Everything Upfront

**What it looks like:**
- Multi-month semantic modeling exercises before any data flows
- Attempts to define all entities, relationships, and facts enterprise-wide
- Waiting for "complete" authority mapping before starting

**Why teams fall into it:**
- Desire for completeness before action
- Fear of rework
- Traditional enterprise architecture habits

**Consequences:**
- Analysis paralysis—nothing ships
- Models become stale before implementation
- Stakeholder fatigue; ETSL loses credibility
- Real conflicts are not discovered until too late

**ETSL Principle Violated:**
> ETSL is grown, not imposed.

**Correction:** Start narrow. Build one artifact. Learn. Expand.

---

### Anti-Pattern 2: Centralizing Ingestion

**What it looks like:**
- All data must flow through a single central ingestion team
- Domains are not allowed to publish their own adapters
- Bottleneck forms at the "ETSL team"

**Why teams fall into it:**
- Desire for control and consistency
- Distrust of domain engineering quality
- Misunderstanding of ETSL as a centralized platform

**Consequences:**
- ETSL team becomes a bottleneck
- Adoption slows to the pace of the central team
- Domains disengage; shadow data paths emerge
- ETSL loses its federated advantage

**ETSL Principle Violated:**
> Authority is modeled, not centralized.

**Correction:** Enable domain teams to build ingress adapters. Govern semantics, not pipelines.

---

### Anti-Pattern 3: Treating ETSL as a Data Warehouse

**What it looks like:**
- ETSL becomes a place to "land all the data"
- Reporting and analytics are built directly on ETSL tables
- ETSL artifacts are denormalized for query performance

**Why teams fall into it:**
- Familiarity with warehouse patterns
- Pressure to deliver "one source of truth" quickly
- Conflation of ETSL with a data platform

**Consequences:**
- Semantic purity is compromised for query convenience
- Authority and temporal semantics are dropped
- ETSL becomes just another reporting layer
- Audit and regulatory defensibility are lost

**ETSL Principle Violated:**
> ETSL Data Artifacts represent what the enterprise accepts as true—not what is convenient to consume.

**Correction:** ETSL produces truth. Data products consume and reshape it for use cases.

---

### Anti-Pattern 4: Hiding Authority in Code

**What it looks like:**
- Reconciliation rules are embedded in SQL, Spark, or dbt
- Authority precedence is implicit in pipeline order
- No explicit Authority Registry exists

**Why teams fall into it:**
- Urgency to ship
- "We'll document it later"
- Lack of governance rituals

**Consequences:**
- Reconciliation logic becomes tribal knowledge
- Auditors cannot explain why a value exists
- Changes to logic have unpredictable effects
- Authority disputes cannot be resolved without code archaeology

**ETSL Principle Violated:**
> Reconciliation is semantic, not just technical.

**Correction:** Authority and reconciliation rules are semantic artifacts. They must be explicit, governed, and versioned.

---

### Anti-Pattern 5: Ignoring Temporal Semantics

**What it looks like:**
- Facts and relationships have no effective dates
- "Current" state is the only state
- Historical queries require replaying pipelines

**Why teams fall into it:**
- Simplicity bias
- Source systems don't provide effective dates
- "We only need current data"

**Consequences:**
- Cannot answer "what was true as of T?"
- Regulatory reconstruction becomes code archaeology
- Corrections overwrite history
- AI/ML explainability is impossible

**ETSL Principle Violated:**
> ETSL Data Artifacts are governed by temporal semantics.

**Correction:** If a source doesn't provide effective dates, ETSL must infer or assign them at ingress. Time is mandatory.

---

### Summary Table

| Anti-Pattern | Root Cause | Consequence | Correction |
|--------------|------------|-------------|------------|
| Modeling everything upfront | Fear of rework | Analysis paralysis | Start narrow |
| Centralizing ingestion | Desire for control | Bottleneck | Enable domains |
| Treating ETSL as warehouse | Familiarity | Semantic loss | Separate truth from consumption |
| Hiding authority in code | Urgency | Audit failure | Explicit Authority Registry |
| Ignoring temporal semantics | Simplicity bias | No history | Time is mandatory |

---

## 17. Roadmap to Broader Adoption

ETSL adoption follows a predictable maturity curve. Rushing through stages creates fragility; skipping stages creates gaps.

### Stage 1: Narrow Scope (Months 1–3)

**Goal:** Prove the pattern on 1–2 cross-domain use cases.

**Activities:**
- Select high-value, high-risk use cases (see Section 6)
- Build first ETSL Data Artifacts
- Establish Authority Registry for in-scope concepts
- Implement ingress and reconciliation for selected sources
- Validate with domain SMEs and at least one consumer

**Success Criteria:**
- 1–2 ETSL Data Artifacts in production
- Cross-domain consumer actively using them
- No major semantic or authority disputes unresolved

---

### Stage 2: Demonstrate Reuse (Months 4–6)

**Goal:** Prove that ETSL reduces duplication and conflict.

**Activities:**
- Onboard 2–3 additional consumers for existing artifacts
- Add 1–2 new Assertion Sources
- Expand Authority Registry incrementally
- Document reconciliation patterns for reuse
- Capture and communicate wins (time saved, disputes resolved)

**Success Criteria:**
- Multiple consumers using the same ETSL Data Artifacts
- Documented evidence of reuse (avoided rebuilds)
- Stakeholder awareness of ETSL value

---

### Stage 3: Voluntary Alignment (Months 6–12)

**Goal:** Attract domain participation without mandates.

**Activities:**
- Domains begin aligning source-aligned products to ETSL vocabulary
- New initiatives ask "should we use ETSL for this?"
- Authority Registry becomes a reference for governance discussions
- ETSL team transitions from "builder" to "enabler"

**Success Criteria:**
- Domains voluntarily aligning semantics
- New cross-domain initiatives start with ETSL consideration
- Reduced semantic disputes in Data Product development

---

### Stage 4: Enable Data Products (Months 12+)

**Goal:** ETSL becomes the truth substrate for Data Product engineering.

**Activities:**
- Data products are built on ETSL Data Artifacts by default
- Transforming Data Applications consume ETSL truth
- Data-Driven Operational Applications produce assertions that re-enter ETSL
- Platform provides tooling for artifact discovery and lineage

**Success Criteria:**
- Data products declare ETSL dependencies explicitly
- Semantic contracts are enforced in CI/CD
- ETSL is referenced in architecture reviews

---

### Adoption Curve Visualization

```
Maturity
    │
    │                              ┌── Enable Data Products
    │                         ┌────┘
    │                    ┌────┘ Voluntary Alignment
    │               ┌────┘
    │          ┌────┘ Demonstrate Reuse
    │     ┌────┘
    │─────┘ Narrow Scope
    └────────────────────────────────────────────────► Time
         M1-3        M4-6        M6-12        M12+
```

### The Journey: Outcomes, Confidence, and Mindset

Beyond timelines and activities, ETSL adoption involves a shift in how teams think about enterprise data. Each phase represents a different mindset.

**Phase 1: Proving (Early)**

*Outcome:* One or two ETSL Data Artifacts exist and are being used.

*Confidence level:* Cautious optimism. The team believes the pattern works but hasn't proven it at scale.

*Mindset:* "We are learning what ETSL means in our context." Teams accept that early artifacts may need revision. Mistakes are expected and used for learning. The goal is correctness, not coverage.

*What success feels like:* A cross-domain consumer says, "This is exactly what we needed—we didn't have to reconcile it ourselves."

---

**Phase 2: Stabilizing (Growing)**

*Outcome:* Multiple consumers rely on ETSL artifacts. Authority and reconciliation patterns are documented and repeatable.

*Confidence level:* Growing trust. Teams begin to rely on ETSL artifacts instead of building their own reconciliation.

*Mindset:* "We are building reusable truth." The focus shifts from proving the concept to hardening it. Governance rituals become routine. Engineers stop asking "why do we need ETSL?" and start asking "how do we extend it?"

*What success feels like:* A new initiative asks, "Can we use the Party artifact you already built?" instead of starting from scratch.

---

**Phase 3: Enabling (Mature)**

*Outcome:* ETSL is the default truth substrate for Data Product development. Semantic contracts are enforced in CI/CD. Domains voluntarily align.

*Confidence level:* High trust. Teams assume ETSL artifacts are correct and authoritative. Exceptions are rare and investigated.

*Mindset:* "We build on truth, not on hope." Data products are built faster because foundational reconciliation is already done. The ETSL team shifts from building artifacts to enabling others. Governance is lightweight because semantic discipline is internalized.

*What success feels like:* An auditor asks for the ownership history of an account. The answer is available in seconds, with full authority attribution, without involving any engineer.

### Key Insight

> **Alignment happens by gravity, not force.**

ETSL succeeds when domains choose to align because the value is obvious—not because a mandate requires it.

---

## 18. How This Enables Data Product Engineering

ETSL Data Artifacts provide a **stable truth substrate** for safe Data Product building. Without this substrate, every Data Product team must independently:
- Reconcile conflicting sources
- Determine authority
- Handle temporal semantics
- Defend audit and regulatory questions

This leads to duplication, inconsistency, and escalating costs.

### What ETSL Enables for Data Products

| Without ETSL | With ETSL |
|--------------|-----------|
| Each Data Product reconciles its own sources | Reconciliation is done once, reused many times |
| Authority is embedded in product code | Authority is explicit and governed |
| Temporal semantics are inconsistent | All products inherit consistent temporal rules |
| Audit requires code archaeology | Audit is semantic and traceable |
| Cross-product consistency is accidental | Cross-product consistency is designed |

### The Handoff to Data Product Engineering

This document establishes:
- How ETSL Data Artifacts are built
- How they are validated and governed
- How they co-exist with domain data products

The companion document, *Building Data Products using ETSL Data Artifacts*, addresses:
- How data products consume ETSL truth
- How Transforming Data Applications reshape truth for use cases
- How Data-Driven Operational Applications act on ETSL state
- How assertions from operational applications re-enter ETSL

### Key Distinctions (Preview)

| Concept | Role |
|---------|------|
| **ETSL Data Artifact** | Stable, authority-qualified truth |
| **Data Application** | Builds and serves data products |
| **Transforming Data Application** | Consumes ETSL truth, produces derived products |
| **Data Product** | Consumer-facing, use-case-specific interpretation |
| **Data-Driven Operational Application** | Acts on truth; may produce new assertions |

### The Boundary

> **ETSL stabilizes meaning. Data products deliver value.**

Data products may aggregate, filter, denormalize, and reshape ETSL truth for their consumers. They may not redefine authority, invent temporal semantics, or bypass reconciliation.

This separation is the foundation for scalable, auditable, and trustworthy enterprise data.

---

## 19. Summary Principles

The following principles are non-negotiable for ETSL adoption. They should guide every design decision, governance conversation, and stakeholder explanation.

### Foundational Principles

**1. ETSL is grown, not imposed**
> Start narrow. Demonstrate value. Expand through demonstrated gravity, not mandates.

**2. Authority is modeled, not centralized**
> Authority is discovered from organizational reality and made explicit. ETSL does not centralize data ownership—it makes ownership visible.

**3. Truth precedes interpretation**
> ETSL Data Artifacts represent what the enterprise accepts as true. Data products interpret that truth for specific use cases. The order matters.

**4. Co-existence is a feature, not a compromise**
> ETSL is designed to co-exist with Data Mesh, domain data products, and existing data estates. Forced convergence creates resistance; voluntary alignment creates durability.

**5. Semantics are explicit, not embedded**
> Authority, reconciliation, and temporal rules are semantic artifacts. They are governed, versioned, and auditable—not hidden in pipelines.

### Operational Principles

**6. Validation is mandatory**
> Invalid ETSL Data Artifacts undermine trust in the entire layer. Semantic correctness, authority consistency, and temporal coherence are checked continuously.

**7. Ingress is capture, not intelligence**
> The ingress layer captures assertions faithfully. It does not infer, reconcile, or decide. Intelligence lives in governed reconciliation and state derivation.

**8. Time is mandatory**
> Every fact, relationship, and state carries temporal semantics. "Current only" is not sufficient for regulatory, audit, or explainability requirements.

**9. Small and correct beats large and approximate**
> One well-governed ETSL Data Artifact is more valuable than a dozen ungoverned tables. Correctness establishes credibility.

**10. Rituals sustain clarity**
> Without governance rituals, ETSL degrades into pipelines. Semantic reviews, authority reviews, and periodic health checks are required.

---

### Closing Statement

> **ETSL does not attempt to own all data.  
> It provides a semantic anchor for the truths that matter most.**

For banks navigating regulatory complexity, cross-domain dependencies, and the pressure to adopt AI and automation safely, ETSL offers a path to **enterprise truth without enterprise upheaval**.

---

## Glossary

This document uses terminology defined in the canonical ETSL lexicon:

- **Tier-1 ETSL Canonical Terminology** (`../../terminology/tier-1-etsl-canonical-terminology.md`) — Core semantic primitives: Assertion, Authority, Reconciliation, State, Data Product, Data Artifact, Data Application
- **Tier-2 ETSL Canonical Classifications** (`../../terminology/tier-2-etsl-canonical-classifications.md`) — Behavioral classifications: ETSL Core Data Application, Transforming/Serving Data Applications, Candidate Assertion, ETSL Ingress Boundary

For the distinction between Ontology, Semantic Artifacts, and Data Artifacts, see *Ontology vs ETSL Semantic vs ETSL Data Artifacts* (`../../conceptual/artifacts-ontology-vs-semantic-vs-data.md`).

### Terms Specific to This Document

**Normalized Assertion**
> A candidate assertion transformed to align with ETSL semantic contracts. Mapped to ETSL semantic types, carries attached authority, and is ready for reconciliation.

**Reconciliation Logic**
> The explicit, governed rules that resolve conflicts between assertions. Part of the ETSL semantic contract, not hidden in pipeline code.

**Invariant**
> A condition that must always hold for an entity's state to be valid. Invariants are evaluated on state, explicitly documented, and non-negotiable.

**Assertion Onboarding Review**
> A governance ritual conducted when a new Assertion Source is added. Produces approved ingress design and authority mapping.

**Authority Review**
> A governance ritual conducted when new facts or relationships are added, or when conflicts emerge. Produces an updated Authority Registry.

**Reconciliation Review**
> A governance ritual conducted when new reconciliation rules are proposed or unexpected conflicts surface. Produces documented reconciliation logic.

**Semantic Health Check**
> A periodic (typically quarterly) governance ritual to detect drift, prioritize backlog, and capture lessons learned.

### Quick Reference

| Term | Meaning |
|------|---------|
| **Ontology** | Defines meaning and possibility |
| **ETSL Semantic Artifact** | Defines what may be asserted as true |
| **ETSL Data Artifact** | Records what is true |
| **Fact** | What is true |
| **Event** | What happened |
| **State** | Current truth, derived from facts |
| **Assertion Source** | Emits claims |
| **Authority** | Empowered to assert |
| **Reconciliation** | Resolves conflicts |
| **Data Product** | Interprets truth for consumers |

---

*End of Document*

---
