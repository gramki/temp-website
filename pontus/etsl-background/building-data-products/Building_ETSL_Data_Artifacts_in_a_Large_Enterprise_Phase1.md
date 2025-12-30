# Building ETSL Data Artifacts in a Large Enterprise  
## From Existing Data Estate to Enterprise Truth  
### Architectural Guidance for Architects and Data Engineers

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
- **Sections 17–18**: Preparation for data product engineering  

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
- **Traceable to assertion sources** — lineage back to the SOR or domain product that emitted the original claim
- **Designed for cross-domain reuse** — the same Party identity artifact serves Retail, Corporate, Compliance, and Risk
- **Stable relative to consumer data products** — ETSL Data Artifacts change slowly; data products built on them may evolve freely

### ETSL Data Artifacts ARE NOT

- **Raw ingested SOR tables** — those are assertion sources, not truth
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

A compliance team tracks beneficial ownership in their AML system. A data engineer suggests exposing this as a domain data product rather than bringing it into ETSL, because "it's just a compliance concern."

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
> A system, domain data product, or external feed that emits claims about enterprise reality.

- Examples: Core banking system, CRM, AML/KYC platform, external credit bureau feed
- Assertion sources are not truth by default—they emit candidates for reconciliation
- A single logical entity (e.g., "Customer") may have multiple assertion sources

**Candidate Assertion**
> A claim captured from an assertion source, prior to normalization or reconciliation.

- Preserves the original form and provenance
- Not yet authority-qualified
- May conflict with other candidate assertions for the same entity

**Normalized Assertion**
> A candidate assertion transformed to align with ETSL semantic contracts.

- Mapped to ETSL semantic types and vocabulary
- Carries attached authority
- Ready for reconciliation with other normalized assertions

**Derived Assertion**
> An assertion produced as a result of decisions, computations, or reconciliation—not directly emitted by an assertion source.

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
- Defines where "assertion source world" ends and "ETSL world" begins

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
- Scope: Party-level exposure facts, aggregated from multiple assertion sources

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
- No domain data product exists
- Domain product adds transformations that obscure provenance
- Regulatory or audit requirements demand direct lineage to source

### Worked Example: Consuming a Domain Data Product for KYC Status

The Compliance domain owns the KYC platform and publishes a source-aligned data product called "Party Verification Status." This product includes:
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

**Option B: Consume the domain data product**
- ETSL consumes the published "Party Verification Status" product
- Compliance domain remains accountable for data quality and semantics
- Product contract provides stability; internal platform changes are absorbed by the domain
- Domain maintains lineage documentation that ETSL can reference

ETSL chooses Option B. At ingress:
- The domain product is consumed as an assertion source
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

For each assertion source, document:

| Aspect | What to Capture |
|--------|-----------------|
| Source type | SOR feed or domain data product? |
| Entity scope | Which entities does this source assert? |
| Fact scope | Which facts or relationships? |
| Authority | Which enterprise function is this source acting on behalf of? |
| Temporal semantics | Does the source provide effective dates? |
| Conflict potential | Are other sources asserting the same facts? |

This mapping becomes input to the ETSL Ingress Layer design.

See *ETSL and Data Mesh: Co-existence, Complementarity, and Enterprise Evolution* for detailed patterns.

---

## 8. Designing the ETSL Ingress Layer

The ETSL Ingress Layer is the **controlled intake surface** where assertions enter the ETSL domain. It defines the boundary between "assertion source world" and "ETSL world."

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
| Domain data product | API or file-based consumption, contract validation |
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

### Building the Authority Registry Incrementally

For early ETSL adoption:

1. **Start narrow** — cover only the facts and relationships in scope
2. **Be explicit** — if authority is unclear, flag it for governance resolution
3. **Avoid system names** — systems act on behalf of authority; they are not authority
4. **Version the registry** — authority evolves; changes must be tracked

A v1 Authority Registry for a bank might have 10–20 entries. That is sufficient to demonstrate value and establish the pattern.

---

## 10. Reconciliation and Normalization Patterns

Reconciliation is unavoidable in any enterprise with multiple assertion sources. ETSL makes reconciliation **explicit, governed, and auditable**—rather than hidden in pipeline logic.

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

## 11. Producing the First ETSL Data Artifacts

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
- Identify 2–4 assertion sources for those use cases
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

### What "Done" Looks Like for v1

A v1 ETSL Data Artifact is "done" when:

1. **Lineage is complete** — traceable from artifact back to assertion sources
2. **Authority is explicit** — every fact/relationship carries its authority
3. **Temporal semantics are present** — effective dates, validity windows
4. **At least one consumer is using it** — validates cross-domain reuse
5. **Validation has passed** — semantic correctness, authority consistency, temporal coherence
6. **Documentation exists** — semantic contract, authority rules, reconciliation logic

---

## 12. Validating ETSL Data Artifacts

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

## 13. Operating Model During Early ETSL Adoption

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
| ETSL Semantic Architect | Semantic contracts, authority registry, reconciliation rules | Pipeline implementation |
| ETSL Data Engineer | Ingress, normalization, state derivation pipelines | Semantic definitions |
| Domain Architect | Domain-specific authority, source-aligned products | Cross-domain reconciliation |
| Domain Engineer | Ingress adapters, domain product maintenance | ETSL core infrastructure |

### Required Rituals

Without rituals, ETSL decays. Establish early:

**1. Assertion Onboarding Review**
- When: Each new assertion source is added
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

## 14. Co-existence with Existing Data Products

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
- ETSL consumes the product as an assertion source
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

## 15. Anti-Patterns to Avoid Early

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
| Hiding authority in code | Urgency | Audit failure | Explicit authority registry |
| Ignoring temporal semantics | Simplicity bias | No history | Time is mandatory |

---

## 16. Roadmap to Broader Adoption

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
- Add 1–2 new assertion sources
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
- Reduced semantic disputes in data product development

---

### Stage 4: Enable Data Products (Months 12+)

**Goal:** ETSL becomes the truth substrate for data product engineering.

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

### Key Insight

> **Alignment happens by gravity, not force.**

ETSL succeeds when domains choose to align because the value is obvious—not because a mandate requires it.

---

## 17. How This Enables Data Product Engineering

ETSL Data Artifacts provide a **stable truth substrate** for safe data product building. Without this substrate, every data product team must independently:
- Reconcile conflicting sources
- Determine authority
- Handle temporal semantics
- Defend audit and regulatory questions

This leads to duplication, inconsistency, and escalating costs.

### What ETSL Enables for Data Products

| Without ETSL | With ETSL |
|--------------|-----------|
| Each data product reconciles its own sources | Reconciliation is done once, reused many times |
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

## 18. Summary Principles

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
