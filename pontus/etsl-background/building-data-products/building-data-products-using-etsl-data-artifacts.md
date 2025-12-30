# Building Data Products using ETSL Data Artifacts  
## From Enterprise Truth to Consumer-Aligned Value
### Architectural Guidance for Product Managers, Architects, and Engineers

**Audience:** Product Managers, Product Architects, Data Architects, Data Engineers, CIOs  
**Status:** Architectural Guidance Document

> ⚡ **Quick Reference:** For a one-page cheat sheet, see [Building Data Products — Quick Reference](building-data-products-quick-reference.md)

---

## Table of Contents

### Foundations
- [0. How to Read This Document](#0-how-to-read-this-document)
- [1. Why Data Products Need ETSL](#1-why-data-products-need-etsl)
- [2. What a Data Product Is (and Is Not) in an ETSL World](#2-what-a-data-product-is-and-is-not-in-an-etsl-world)

### Building Data Products
- [3. Constituents of a Data Product](#3-constituents-of-a-data-product)
- [4. Types of Data Products Built on ETSL](#4-types-of-data-products-built-on-etsl)
- [5. Data Applications in Data Product Engineering](#5-data-applications-in-data-product-engineering)

### Consuming ETSL Truth
- [6. Consuming ETSL Data Artifacts Correctly](#6-consuming-etsl-data-artifacts-correctly)
- [7. Designing Data Products Without Breaking Truth](#7-designing-data-products-without-breaking-truth)
- [8. Data Product Contracts in an ETSL World](#8-data-product-contracts-in-an-etsl-world)

### Co-existence and Operations
- [9. Co-existence with Data Mesh & Domain Products](#9-co-existence-with-data-mesh--domain-products)
- [10. Operational Systems as Consumers and Producers](#10-operational-systems-as-consumers-and-producers)

### Anti-Patterns and First Products
- [11. Common Anti-Patterns in ETSL-Based Data Products](#11-common-anti-patterns-in-etsl-based-data-products)
- [12. First Data Products on ETSL: What "Good" Looks Like](#12-first-data-products-on-etsl-what-good-looks-like)

### Organization and Governance
- [13. Organizational & Workflow Implications](#13-organizational--workflow-implications)
- [14. ETSL vs Common Data Product Engineering Practices](#14-etsl-vs-common-data-product-engineering-practices)
- [15. Summary: What Changes and What Doesn't](#15-summary-what-changes-and-what-doesnt)

### Appendices
- [Appendix A: Data Product Design Checklist (ETSL-Aware)](#appendix-a-data-product-design-checklist-etsl-aware)
- [Appendix B: Terminology Declaration Template](#appendix-b-terminology-declaration-template)
- [Appendix C: Mapping Existing Products to ETSL Dependency Patterns](#appendix-c-mapping-existing-products-to-etsl-dependency-patterns)

### Reference
- [Glossary](#glossary)

---

## 0. How to Read This Document

This document explains **how Data Products are conceived, built, and evolved when an Enterprise Truth & Semantics Layer (ETSL) exists**.

It is written to help:
- **Product Managers** understand what ETSL changes (and what it does not)
- **Architects** design data products without re‑solving enterprise truth
- **Engineers** implement data products safely on top of stabilized semantics

### What This Document Assumes You Already Know

This document assumes familiarity with:

| Concept | Where to Find It |
|---------|------------------|
| What ETSL is and why it exists | *ETSL One‑Page Onboarding Primer* |
| Tier‑1 semantic primitives (Assertion, Authority, State, Data Product) | *Tier‑1 ETSL Canonical Terminology* |
| Tier‑2 classifications (Transforming, Serving, Operational) | *Tier‑2 ETSL Canonical Classifications* |
| How ETSL Data Artifacts are built | *Building ETSL Data Artifacts in a Large Enterprise* |
| How ETSL and Data Mesh co-exist | *ETSL ↔ Data Mesh: Co‑existence & Evolution* |

If you are unfamiliar with these concepts, **read the Onboarding Primer first**.

This document does not restate ETSL foundations. It focuses on **how Data Products consume and interpret ETSL truth**.

### Prerequisite Reading (Normative)
- *ETSL One‑Page Onboarding Primer*  
- *Tier‑1 ETSL Canonical Terminology*  
- *Tier‑2 ETSL Canonical Classifications*  
- *Building ETSL Data Artifacts in a Large Enterprise*  
- *ETSL ↔ Data Mesh: Co‑existence & Evolution*  

### How to Use This Document in Practice

| If You Are... | Start Here | Focus On |
|---------------|------------|----------|
| **Product Manager** | Sections 1–2, 12, 15 | What changes for your roadmap and stakeholder conversations |
| **Architect** | Sections 3–5, 7–9, 13 | Design patterns, boundaries, and co-existence with domain products |
| **Data Engineer** | Sections 5–6, 8, 11 | Consumption patterns, contracts, and anti-patterns to avoid |
| **CIO / Executive** | Sections 1, 14–15 | Why this matters and what success looks like |

Practitioners may return to specific sections during execution. The appendices provide reusable checklists and templates.

### Explicit Non‑Goals
- This document does **not** define ETSL semantics  
- This document does **not** explain how ETSL Data Artifacts are produced  
- This document does **not** prescribe tools, platforms, or pipelines  

---

## 1. Why Data Products Need ETSL

In large enterprises—especially banks—data products are often built:
- directly on systems of record,
- on domain‑specific marts,
- or on replicated operational datasets.

Over time this leads to:
- semantic drift,
- inconsistent metrics and decisions,
- duplicated reconciliation logic,
- audit and regulatory exposure that surfaces only during regulatory reviews or production incidents.

ETSL exists so that **every Data Product does not need to independently rediscover what is true**.

### A Banking Example: The Drift Problem

Consider two data products built independently in a large bank:

**Product A: "Available Credit" for Real-Time Authorization**

The card authorization team builds a Data Product to determine available credit for transaction approvals. They consume the credit limit from the underwriting system, subtract the current balance from the card processor, and apply a buffer for pending transactions. The product is fast and serves millions of authorizations daily.

**Product B: "Customer Exposure Summary" for Relationship Managers**

The retail banking team builds a dashboard showing relationship managers each customer's total exposure across products. They pull limits from risk systems, balances from the core banking ledger, and pending transactions from the payments hub. The product helps RMs have informed conversations.

**What Goes Wrong**

After six months:
- A customer calls complaining that they were declined at a merchant despite their RM showing available credit. The products disagree on the customer's limit—one uses the underwriting system, the other uses the risk-adjusted limit.
- A compliance review asks for total customer exposure as of a regulatory reporting date. Both products claim to answer this, but their numbers differ by 15%. Each team defends their methodology.
- A new fraud detection initiative needs "available credit" as a feature. They now have two conflicting definitions—and neither team can explain why they differ without code archaeology.
- A regulator asks: "Which is the authoritative credit limit?" Neither team can answer definitively.

This is not a failure of either team. Both built valid products for their use cases. The problem is that **each product independently reconciled enterprise truth**—and reconciled it differently.

### Before ETSL vs After ETSL

**Before ETSL:**
- Each Data Product team sources data from whichever system seems appropriate
- Reconciliation logic (which limit? which balance?) is embedded in product code
- Authority is implicit—no one can explain "why this value?" without reading pipelines
- Cross-product consistency is accidental; inconsistency is discovered late
- Auditors and regulators receive different answers depending on which product they query

**After ETSL:**
- Data products consume ETSL Data Artifacts that already carry authority-qualified truth
- Reconciliation is done once, upstream, by governed logic
- Products interpret truth for their use cases—they do not re-derive it
- Cross-product consistency is designed: products that need the same fact get the same fact
- Auditors receive consistent answers because all products trace back to the same ETSL truth

The operational complexity of building a Data Product does not change. What changes is **where truth is decided**—and that decision happens once, not in every product.

> ETSL stabilizes meaning so data products can focus on delivering value.

---

## 2. What a Data Product Is (and Is Not) in an ETSL World

A **Data Product** is a **consumer‑aligned interpretation of enterprise truth**, designed for a specific use case or decision.

These terms are defined precisely in *Tier‑1 ETSL Canonical Terminology*:
- **Data Product**: A consumer-aligned, governed data asset that interprets ETSL Data Artifacts to serve a specific use case or decision
- **ETSL Data Artifact**: A governed, authority-qualified, time-aware representation of enterprise truth
- **Source-Aligned Data Product**: A domain-owned Data Product that closely reflects the semantics of an operational system

### A Data Product:
- Interprets ETSL Data Artifacts  
- Is scoped to a consumer or journey  
- Evolves quickly and independently  

### A Data Product is not:
- A source of enterprise truth  
- An ETSL Data Artifact  
- An authority on semantics  

ETSL deliberately enables **many overlapping data products**, as long as they agree on truth—even if they disagree on presentation, thresholds, or business interpretation.

### Contrast Examples: Avoiding Common Misclassifications

The following examples illustrate what is—and is not—a Data Product in an ETSL world.

---

**Example 1: "Customer 360" Domain Mart — NOT an ETSL Data Artifact**

A retail banking team maintains a "Customer 360" table that aggregates customer demographics, product holdings, channel preferences, and recent interactions. It is refreshed nightly and powers dashboards for relationship managers.

*Is this an ETSL Data Artifact?* **No.**

The Customer 360 mart is a **Data Product**—specifically, a consumer-aligned interpretation. It aggregates information for a specific use case (RM conversations). It contains derived and filtered data (e.g., "preferred channel," "engagement score") that are not authority-qualified enterprise truths.

*What would be ETSL Data Artifacts?*
- Party identity (name, identifiers, verification status) with authority
- Account ownership relationships with effective dates
- Product holding facts with temporal validity

The Customer 360 consumes these ETSL artifacts and interprets them for its audience. It does not define enterprise truth about who the customer is.

---

**Example 2: Credit Limit Exposure Report — A Correct Data Product**

The treasury team builds a report showing aggregated credit exposure by product type, geography, and customer segment. It consumes ETSL Credit Limit facts (authority-qualified, with effective dates) and ETSL Account Ownership relationships.

*Is this an ETSL Data Artifact?* **No.**

This is a **Data Product**—a correct interpretation of ETSL truth. It aggregates, slices, and presents ETSL facts for treasury's decision-making needs. The product does not redefine what a credit limit is or assert new authority over limits. It interprets.

*Why this is correct:*
- It consumes ETSL artifacts rather than going directly to source systems
- It does not embed reconciliation logic—ETSL has already reconciled
- It can evolve its aggregation logic without affecting enterprise truth

---

**Example 3: Fraud Detection Feature Set — A Data Product, Not Truth**

The fraud detection team builds a feature store containing signals like "velocity of transactions," "deviation from typical spending," and "credit utilization ratio." These features are consumed by ML models for real-time fraud scoring.

*Is this an ETSL Data Artifact?* **No.**

Features are **derived interpretations** of truth, not truth itself. A "credit utilization ratio" is computed from ETSL-provided limit and balance facts, but the ratio itself is not an authority-qualified enterprise fact. It is a model input.

*What could go wrong if treated as truth:*
- Other teams might consume the feature as if it were authoritative utilization
- Changes to the feature's calculation would silently affect downstream systems
- Audit would struggle to explain "why this score?" without tracing through feature logic

*The correct pattern:*
The feature set is a **Feature-Oriented Data Product**. It consumes ETSL Data Artifacts, derives features, and serves ML consumers. The ETSL artifacts remain the source of truth; the features are interpretations.

---

### The Core Distinction

| | ETSL Data Artifact | Data Product |
|---|---|---|
| **Purpose** | Stabilize enterprise truth | Serve a use case |
| **Authority** | Explicitly modeled | Inherited from ETSL |
| **Evolution** | Slow, governed | Fast, product-team-owned |
| **Reconciliation** | Happens here | Does not happen here |
| **Consumers** | Data Products, Operational Systems | Humans, Applications, Models |

---

## 3. Constituents of a Data Product

### 3.1 Builder View

From a builder's perspective, a Data Product consists of:
- Inputs (ETSL Data Artifacts, sometimes other Data Products)
- Transforming Data Applications
- Serving Data Applications
- Explicit contracts (schema, freshness, scope)
- Versioning and lifecycle policies

The builder's responsibility is **interpretation**, not truth determination.

#### Builder Checklist

Before releasing a Data Product, builders should confirm:

| # | Checkpoint | Why It Matters |
|---|------------|----------------|
| 1 | ETSL Data Artifacts identified for cross-domain truth | Avoid re-deriving truth locally |
| 2 | Lineage preserved from product outputs back to ETSL artifacts | Audit and explainability |
| 3 | Temporal consumption pattern explicit (current state, as-of, full history) | Prevents misuse of time-sensitive data |
| 4 | Authority metadata not discarded | Consumers may need to trace decisions |
| 5 | Semantic contract inherited, not redefined | Prevents drift |
| 6 | Freshness expectations documented | Consumers know what they are getting |
| 7 | Tier-2 classification declared (Transforming / Serving / Operational) | Governance expectations clear |
| 8 | Escalation path defined for semantic gaps | Prevents local workarounds |

### 3.2 Consumer View

From a consumer's perspective, a Data Product provides:
- A stable interface (table, API, feature set)
- Clear semantic guarantees (inherited from ETSL)
- Documented assumptions and limitations
- Known freshness and completeness bounds

Consumers should never need to reason about authority or reconciliation—even when outcomes differ from what they expected.

#### Consumer Checklist

When adopting a Data Product, consumers should verify:

| # | Checkpoint | Why It Matters |
|---|------------|----------------|
| 1 | Product consumes ETSL artifacts for truth-sensitive inputs | Trust in semantic correctness |
| 2 | Freshness bounds acceptable for use case | Avoid stale data in time-critical decisions |
| 3 | Temporal assumptions match use case | Point-in-time vs historical queries |
| 4 | Lineage documentation available | Required for audit and compliance |
| 5 | Contract versioning understood | Prepare for breaking changes |
| 6 | Escalation path known | Where to go when semantics seem wrong |

### 3.3 What Consumers May Assume vs Must Not Assume

**What consumers MAY assume:**

- Semantic correctness: Values conform to ETSL semantic contracts
- Authority is resolved: If the product consumes ETSL, reconciliation has already happened
- Temporal coherence: Effective dates are meaningful and consistent
- Lineage exists: The product can trace its outputs back to ETSL artifacts

**What consumers MUST NOT assume:**

- Immutability: ETSL Data Artifacts evolve (corrections, late arrivals); products may reflect these changes
- Real-time freshness: Unless explicitly documented, products may have latency
- Authority exposure: The product may not expose which authority asserted a value (check documentation)
- Full history: The product may serve current state only; historical queries may require different access patterns
- Direct ETSL access: Consumers consume the product, not the underlying ETSL artifacts—abstraction boundaries exist for a reason

> **Key insight:** Data Products shield consumers from ETSL complexity while inheriting ETSL correctness. This is the value proposition.

---

## 4. Types of Data Products Built on ETSL

ETSL does not collapse Data Product diversity. Common types include:

- **Analytical Data Products** (dashboards, reports, exploration)
- **Consumer‑Aligned Data Products** (journey, portfolio, risk views)
- **Feature‑Oriented Data Products** (ML features)—often reused across multiple models with subtly different assumptions
- **Operationally‑Consumed Data Products**

Each type differs in change cadence, stability expectations, and tolerance for evolution. ETSL provides a **shared truth substrate**, not uniform outputs.

---

### 4.1 Analytical Data Products

**What it looks like:**
A monthly credit portfolio dashboard showing limit utilization, delinquency trends, and concentration risk by industry segment. Consumed by credit risk committees and executive leadership.

**Typical consumers:**
- Risk committees
- Finance and treasury
- Executive reporting
- Regulatory reporting teams

**Expected change cadence:** Slow to moderate. Layout and metrics evolve quarterly; underlying data refresh is daily or monthly.

**ETSL artifacts consumed:**
- Credit Limit facts (authority-qualified)
- Account Ownership relationships
- Party identity and classification

**Failure mode if it tries to become "truth":**
The dashboard team starts defining "delinquency" locally because ETSL doesn't provide it in their preferred format. Over time, their definition drifts from what Risk uses in regulatory reports. Two "official" delinquency numbers now exist, neither traceable to authority.

---

### 4.2 Consumer-Aligned Data Products

**What it looks like:**
A "Unified Customer View" for customer service agents, showing party identity, product holdings, recent interactions, open cases, and applicable offers. Designed for real-time agent desktop use.

**Typical consumers:**
- Customer service agents (voice, chat, branch)
- Relationship managers
- Complaint resolution teams

**Expected change cadence:** Moderate to fast. UX and data fields evolve frequently to support new products, campaigns, or service channels.

**ETSL artifacts consumed:**
- Party identity (name, identifiers, verification status)
- Account Ownership and control relationships
- Product holding facts

**Failure mode if it tries to become "truth":**
The agent desktop team creates a local "customer master" to merge data faster. They apply their own matching logic. Now two customers who ETSL correctly distinguishes (e.g., a parent and adult child at the same address) are merged in the agent view. Agents make decisions based on incorrect identity, triggering compliance issues.

---

### 4.3 Feature-Oriented Data Products

**What it looks like:**
A feature set for fraud detection models, including transaction velocity, spending deviation, device fingerprint consistency, and credit utilization ratio. Served in real-time and batch for model training and inference.

**Typical consumers:**
- Fraud detection models (real-time and batch)
- Model training pipelines
- Model monitoring systems

**Expected change cadence:** Fast. Features are experimented with continuously; new signals are added and deprecated frequently.

**ETSL artifacts consumed:**
- Credit Limit facts
- Account state (open, frozen, closed)
- Party verification status

**Failure mode if it tries to become "truth":**
The fraud team defines "account status" as a feature, but uses their own logic to infer "at risk" status from balance and transaction patterns. Other teams consume this feature as if it were ETSL-authoritative account status. When ETSL's actual account state (from Operations authority) differs, confusion ensues. Model explainability suffers because the feature cannot be traced to authoritative state.

---

### 4.4 Operationally-Consumed Data Products

**What it looks like:**
A credit decisioning Data Product that provides pre-computed eligibility indicators, risk scores, and limit recommendations for real-time lending decisions. Consumed by the loan origination system at application time.

**Typical consumers:**
- Loan origination systems
- Card authorization engines
- Underwriting workflows

**Expected change cadence:** Slow. Changes are high-risk and require extensive testing, since they affect real-time operational decisions with financial and regulatory impact.

**ETSL artifacts consumed:**
- Party identity and verification status
- Credit Limit facts
- Existing exposure relationships

**Failure mode if it tries to become "truth":**
The decisioning product embeds authority rules (e.g., "if Fraud says block, override Risk's limit"). This logic should live in ETSL's reconciliation layer. Now authority precedence is split between ETSL and the operational product. When precedence rules change, two systems must be updated—and they may not stay in sync.

---

### Summary: Types and Their Boundaries

| Type | Change Cadence | Stability Expectation | Failure Mode |
|------|----------------|----------------------|--------------|
| Analytical | Slow | High | Redefines metrics locally |
| Consumer-Aligned | Moderate-Fast | Moderate | Creates local "masters" |
| Feature-Oriented | Fast | Low | Treats features as truth |
| Operationally-Consumed | Slow | Very High | Embeds authority/reconciliation |

> All types consume ETSL truth. None of them define it.

---

## 5. Data Applications in Data Product Engineering

Data Products are realized through **Data Applications**. These are classified in *Tier‑2 ETSL Canonical Classifications* based on their role in the data architecture.

### 5.1 Tier-2 Classifications in Data Product Building

| Classification | Role in Data Products | Examples |
|----------------|----------------------|----------|
| **Transforming Data Application** | Consumes ETSL Data Artifacts or other Data Products; produces derived datasets, aggregates, or features | ETL pipelines, feature engineering jobs, aggregation services |
| **Serving Data Application** | Exposes Data Product outputs via APIs, queries, or services; meets consumer SLAs | Query APIs, dashboard backends, real-time feature serving |
| **Data-Driven Operational Application** | Consumes Data Products for operational decisions; may emit Derived Assertions back to ETSL | Credit decisioning engines, fraud scoring, automated compliance checks |

Each Data Product typically involves one or more Transforming Data Applications (to prepare the data) and one or more Serving Data Applications (to expose it). Some products are consumed by Data-Driven Operational Applications, which close the feedback loop.

### 5.2 What Is In-Scope vs Out-of-Scope

**In-scope for this document:**
- Transforming Data Applications that consume ETSL artifacts
- Serving Data Applications that expose Data Products
- Data-Driven Operational Applications that consume Data Products and produce decisions

**Out-of-scope for this document:**
- **ETSL Core Data Applications** — applications that normalize assertions, apply authority, perform reconciliation, and derive ETSL Data Artifacts. These are covered in *Building ETSL Data Artifacts in a Large Enterprise*.

The boundary is clear: **ETSL Core Data Applications produce truth. Data Product applications interpret truth.**

### 5.3 Guardrails: Preventing Semantic Drift

Data Product applications operate on a foundation of ETSL-stabilized truth. To preserve this foundation, teams must observe strict guardrails:

**1. Do not redefine enterprise semantics—even when upstream data appears incomplete or contradictory**

If ETSL defines "credit limit" as the Risk-approved maximum exposure, the Data Product must not redefine it as "the higher of Risk limit and Operations temporary increase." Interpretations (e.g., "effective limit for display purposes") must be clearly labeled as product-specific derivations, not enterprise truth.

**2. Do not embed authority rules**

Authority precedence (which assertion prevails) is governed by ETSL's Authority Registry, not by Data Product code. If a Transforming Data Application contains logic like "if Fraud says X, ignore Risk's value," authority rules have leaked into the product layer. This creates ungoverned reconciliation.

**3. Do not override ETSL-derived state**

If ETSL produces an account state of "frozen," the Data Product must not override it to "active" for convenience. If the product believes ETSL is wrong, the correction path is upstream—through ETSL governance, not local fixes.

**4. Preserve temporal semantics**

ETSL artifacts carry `effective_from`, `effective_to`, and as-of queryability. Data Products must not flatten these into "current only" unless explicitly documented. Products that discard temporal semantics cannot support historical queries, regulatory reconstruction, or audit.

**5. Maintain lineage to ETSL artifacts**

Every Data Product output must be traceable back to the ETSL Data Artifacts it consumed. This lineage is required for audit, explainability, and impact analysis when ETSL artifacts evolve.

### 5.4 Escalation: When to Engage ETSL

Transforming Data Applications may discover semantic gaps—truths they need but ETSL does not yet provide. The correct response is escalation, not workaround.

**When to escalate:**
- The application needs a fact type that ETSL does not model
- The application needs a relationship that ETSL does not govern
- The application discovers conflicting assertions that ETSL does not reconcile
- The application requires authority clarification

**How to escalate:**
- Data Product teams may propose additions to ETSL Semantic Artifacts through the established review process (see *Building ETSL Data Artifacts*, Section 13)
- Proposals are reviewed by ETSL Semantic Model Architects for coherence and cross-domain impact
- The central team does not solely manufacture semantics—they review and govern to ensure cohesion

**What is NOT an escalation:**
- Derivable values (e.g., ratios, aggregates, computed scores) belong in Data Products, not ETSL Semantic Artifacts
- Use-case-specific interpretations do not require ETSL expansion

> **Principle:** If it is derivable, it stays in the product. If it is foundational truth, it belongs in ETSL.

---

## 6. Consuming ETSL Data Artifacts Correctly

When consuming ETSL Data Artifacts, teams must:
- respect authority‑qualified state,
- handle temporal semantics correctly—especially during boundary moments such as end-of-day, limit changes, or temporary overrides,
- avoid snapshot‑only reasoning.

ETSL artifacts are precise; most errors arise from ignoring time, scope, or authority—typically when teams default to "latest snapshot" reasoning under delivery pressure.

### 6.1 Temporal Consumption Patterns

ETSL Data Artifacts carry temporal semantics: `effective_from`, `effective_to`, and as-of queryability. Data Products may consume these in different ways depending on use case:

| Pattern | When to Use | What the Product Receives |
|---------|-------------|--------------------------|
| **Current state only** | Real-time operational decisions | Point-in-time derived state as of "now" |
| **As-of query** | Historical reporting, regulatory reconstruction | State as it was at a specified point in time |
| **Full temporal history** | Audit trails, trend analysis, ML training | All assertions with validity windows |

The product must document which pattern it uses. Consumers must understand what they are getting.

### 6.2 Worked Example: Available Credit for Card Authorization

A card authorization product needs to determine "available credit" in real-time to approve or decline transactions. This is a derived value that ETSL does not provide directly—but its components come from ETSL.

**The components (from ETSL):**

| ETSL Artifact | What It Provides | Authority |
|---------------|------------------|-----------|
| Credit Limit Fact | Maximum approved credit ($10,000) | CreditRiskManagement |
| Temporary Limit Override | Temporary increase ($15,000, valid June 1–30) | RetailOperations |
| Current Balance State | Outstanding balance as of last settlement ($3,200) | CardProcessor |
| Authorization Hold Facts | Pending transactions not yet settled ($450) | CardProcessor |

**What ETSL provides:**

ETSL provides each of these as authority-qualified, time-aware facts:
- The Credit Limit Fact carries the Risk authority's assessed limit
- The Temporary Limit Override carries Operations authority, with explicit validity dates
- ETSL's reconciliation rules determine the "current limit" based on authority precedence

As of June 15, ETSL's derived current limit is $15,000 (temporary override active).

**What the Data Product does:**

The authorization product consumes:
- Current credit limit from ETSL: $15,000
- Current balance from ETSL: $3,200
- Authorization holds from ETSL: $450

It then computes: Available Credit = $15,000 − $3,200 − $450 = **$11,350**

This computation is the product's interpretation. The product does not redefine what "limit" means or apply its own reconciliation logic.

**Timeline scenario:**

| Date | Event | ETSL State | Product Output |
|------|-------|------------|----------------|
| May 15 | Customer has Risk-approved limit | Limit: $10,000 (CreditRiskManagement) | Available: $6,800 |
| June 1 | Operations grants temporary increase | Limit: $15,000 (RetailOperations override) | Available: $11,800 |
| June 15 | Customer makes purchases | Balance: $3,200, Holds: $450 | Available: $11,350 |
| July 1 | Temporary override expires | Limit: $10,000 (Risk limit restored) | Available: $6,350 |

The product's logic remains constant. ETSL handles the authority transition; the product simply consumes the current state.

### 6.3 Common Consumption Mistakes

**Mistake 1: Treating `effective_from` as `created_at`**

*What happens:* A product uses `effective_from` to filter "recent" data, assuming it indicates when the record was created in ETSL.

*Why it's wrong:* `effective_from` indicates when the fact became true in reality, not when it entered ETSL. A limit set on January 1 but ingested on January 5 has `effective_from` of January 1. Using it as a creation timestamp produces incorrect results.

*Consequence:* Historical queries return wrong answers. Regulatory reconstruction fails.

---

**Mistake 2: Ignoring authority metadata**

*What happens:* A product consumes credit limit values but discards the authority field because "we only need the number."

*Why it's wrong:* Authority may affect downstream interpretation. A limit from Collections (restriction context) may have different implications than a limit from Risk (normal assessment).

*Consequence:* Audit cannot explain why decisions were made. Compliance cannot determine if appropriate authority governed the decision.

---

**Mistake 3: Caching ETSL state without respecting freshness**

*What happens:* A product caches ETSL-derived state for performance but does not refresh when ETSL state changes (corrections, late arrivals, overrides).

*Why it's wrong:* ETSL artifacts evolve. Corrections to historical assertions, late-arriving data, and authority changes all update ETSL state.

*Consequence:* The product serves stale or incorrect data. Decisions made on cached data cannot be explained or defended.

---

**Mistake 4: Snapshot-only reasoning for time-sensitive decisions**

*What happens:* A product consumes only "current" ETSL state and cannot answer "what was true on date X?"

*Why it's wrong:* Regulatory, audit, and dispute resolution all require historical queries. If the product cannot answer "what limit did we use when we approved this transaction three months ago?", it fails its compliance obligations.

*Consequence:* Audit failures, regulatory findings, customer disputes that cannot be resolved.

---

### 6.4 The Consumption Contract

When consuming ETSL Data Artifacts, the Data Product team commits to:

| Commitment | Rationale |
|------------|-----------|
| Consume authority-qualified state, not raw values | Respect ETSL's reconciliation |
| Document temporal consumption pattern | Consumers know what they are getting |
| Preserve lineage to ETSL artifacts | Audit and explainability |
| Refresh when ETSL evolves | Do not serve stale truth |
| Escalate semantic gaps, not workaround | Keep truth upstream |

### 6.5 A Banking Story: Misuse and Correction

**The ETSL Artifact**

ETSL provides a Credit Limit Fact for account A-4521:

- **Value:** $20,000
- **Authority:** CreditRiskManagement
- **Effective from:** 2024-01-15
- **Effective to:** (open—still current)
- **Override context:** None

On March 1, Operations grants a temporary increase:

- **Value:** $30,000
- **Authority:** RetailOperations
- **Effective from:** 2024-03-01
- **Effective to:** 2024-03-31
- **Override context:** Temporary increase (references original fact)

ETSL's reconciliation rules determine that during March, the current limit is $30,000 (temporary override active). After March 31, the limit reverts to $20,000.

**The Misuse**

A fraud detection product needs credit limits as a feature. The team queries ETSL on March 15 and retrieves the current limit: $30,000. They cache this value for performance.

Six weeks later, the cached limit is still $30,000—even though ETSL now shows $20,000 (the override expired). The fraud model scores a transaction as low-risk because the customer appears to have $10,000 more headroom than they actually do. A fraudulent transaction is approved.

During the investigation, the fraud team cannot explain why they used $30,000. They say, "That's what we had in cache." Audit asks: "Did you respect ETSL's temporal semantics?" The answer is no.

**The Correction**

The fraud team redesigns their consumption pattern:

1. **Query ETSL at decision time**, not at cache-population time. For real-time fraud scoring, this means consuming the current-state endpoint with each transaction.
2. **If caching is required for performance**, implement a refresh mechanism that respects ETSL's effective dates. When an override's `effective_to` passes, the cache must invalidate.
3. **Preserve authority metadata** in the feature set. If the model uses a limit from RetailOperations (temporary), that context is available for explainability.
4. **Document the temporal pattern** in the product contract: "Credit limit reflects ETSL current state as of transaction time, refreshed per-transaction."

After correction, the fraud model uses $20,000 for transactions in April—correctly reflecting that the override expired. Decisions are explainable, and audit can trace the limit used to the authoritative ETSL state at decision time.

**The Lesson**

ETSL artifacts are not static values to cache indefinitely. They carry authority and time. Products that ignore these dimensions make decisions on stale or incorrect truth—and discover the error only during audit or incident review.

---

## 7. Designing Data Products Without Breaking Truth

Data Products interpret ETSL truth for specific use cases. This interpretation has boundaries. Crossing them damages enterprise semantic integrity.

### 7.1 DO: Allowed Interpretations

The following are legitimate Data Product activities:

| Activity | Example | Why It's Safe |
|----------|---------|---------------|
| **Derive aggregates** | Sum credit limits across accounts for a customer | Aggregation does not redefine what a limit is |
| **Calculate indicators** | Compute utilization ratio (balance / limit) | The ratio is explicitly a derived metric, not truth |
| **Apply segmentation** | Filter customers by geography or product type | Filtering is a view, not a redefinition |
| **Apply context filters** | Show only "active" accounts for a service agent | Filtering scope does not change account state |
| **Reshape for consumers** | Flatten relationships into a denormalized table | Reshaping for convenience is interpretation |
| **Add derived labels** | Tag customers as "high value" based on AUM | The label is product-specific, not enterprise truth |
| **Compute time-based trends** | Show limit changes over last 12 months | Historical aggregation respects ETSL temporality |

These activities are **interpretations**. They add value for consumers without claiming to define enterprise truth.

### 7.2 DON'T: Forbidden Moves

The following are architectural violations:

| Forbidden Move | Example | Why It Breaks Truth |
|----------------|---------|---------------------|
| **Override authoritative facts** | "ETSL says limit is $10K, but we'll use $15K because that's what the customer expects" | Creates competing truth; audit fails |
| **Fix perceived data issues locally** | "ETSL has wrong address; we'll correct it in our product" | Correction belongs upstream; local fix causes divergence |
| **Silently reinterpret semantics** | "We'll call this 'credit limit' but compute it differently" | Same name, different meaning = semantic drift |
| **Apply undocumented reconciliation** | "If Risk and Ops disagree, we'll take the higher value" | Reconciliation rules must be governed, not embedded |
| **Discard authority metadata** | "We only need the number, not who asserted it" | Breaks audit trail and explainability |
| **Flatten temporal semantics** | "We'll only keep current state, not history" | Destroys regulatory reconstruction capability |

These are not implementation details—they are **architectural failures** that silently corrupt enterprise truth.

### 7.3 ESCALATE: When to Engage ETSL

Some situations cannot be resolved within the Data Product layer. These require escalation to ETSL governance—even if that correction takes longer than a local workaround.

**Escalation triggers:**

| Trigger | Example | Escalation Action |
|---------|---------|-------------------|
| **Semantic gap** | "We need 'beneficial owner' but ETSL doesn't provide it" | Propose addition to ETSL Semantic Artifacts |
| **Contested definition** | "Risk and Operations define 'delinquency' differently" | Request Authority Review to clarify which definition governs |
| **Authority dispute** | "Two ETSL artifacts carry different authorities for the same fact" | Request reconciliation rule clarification |
| **Temporal ambiguity** | "ETSL provides current state, but we need historical" | Request temporal expansion of ETSL artifact |
| **Cross-product inconsistency** | "Two products using ETSL produce different answers" | Investigate whether products are consuming correctly, or ETSL needs clarification |

### 7.4 Worked Example: Escalation for "Delinquency Status"

**Situation:**

A consumer collections product needs "customer delinquency status" to prioritize outreach. The team finds that ETSL does not provide this as a fact.

**Initial (incorrect) response:**

The team computes delinquency locally: "If any account has a payment > 30 days past due, the customer is delinquent." They embed this logic in their Transforming Data Application and serve it as part of their product.

**What goes wrong:**

Six months later, a regulatory reporting product also needs delinquency status. They compute it differently: "Delinquent if 60+ days past due on primary residence loan only." Now two products report different delinquency numbers to the same regulator. Audit asks: "Which is the enterprise definition of delinquency?" No one can answer.

**Correct response:**

The collections team recognizes that "delinquency status" is cross-domain truth (used by Collections, Risk, Regulatory Reporting, and Marketing). They escalate:

1. **Propose** a new ETSL fact type: `DelinquencyStatusFact` with authority and temporal semantics
2. **Engage** ETSL Semantic Model Architects to review cross-domain impact
3. **Collaborate** with Risk, Regulatory, and Collections to agree on authority and definition
4. **Wait** for ETSL to provide the governed artifact before building on it

**Outcome:**

Delinquency status is now an ETSL Data Artifact, authority-qualified (Collections authority for operational status, Risk authority for regulatory status). All products consume the same truth. Regulatory consistency is achieved.

> **Principle:** If the gap affects multiple domains, it belongs in ETSL. If it's derivable and use-case-specific, it stays in the product.

---

## 8. Data Product Contracts in an ETSL World

Data Products still require contracts, but in an ETSL world, some contracts are owned locally while others are inherited. Understanding this distinction prevents redundant governance and ensures semantic consistency.

### 8.1 Types of Contracts

| Contract Type | Owned By | Scope | Example |
|---------------|----------|-------|---------|
| **Schema/Interface Contract** | Data Product Team | Structure, field names, types, nullability | "This API returns `customer_id`, `limit_amount`, `effective_date`" |
| **Service/SLA Contract** | Data Product Team | Freshness, availability, latency, completeness | "Data refreshed hourly; 99.5% availability; P95 latency < 200ms" |
| **Semantic Contract** | ETSL (inherited) | What terms mean, authority, temporal rules | "Credit limit is the Risk-approved maximum exposure, authority-qualified" |

### 8.2 Schema/Interface Contracts

The Data Product team defines and owns the interface contract:

- **Field names and types**: What the product exposes
- **Nullability and optionality**: Which fields are guaranteed
- **Response structure**: For APIs, the shape of the payload
- **Pagination and filtering**: Query parameters and limits

These are **product-specific**. Different products consuming the same ETSL artifacts may expose different interfaces for their consumers.

*Example:* Two products consume the ETSL Party Identity artifact. One exposes a flat JSON structure for a mobile app; the other exposes a hierarchical structure for a CRM integration. Both are valid—the interface is product-specific.

### 8.3 Service/SLA Contracts

The Data Product team defines and owns operational expectations:

| Dimension | What to Document | Example |
|-----------|------------------|---------|
| **Freshness** | How current is the data? | "Reflects ETSL state as of last hourly refresh" |
| **Availability** | Uptime commitment | "99.5% monthly availability" |
| **Latency** | Response time for queries/APIs | "P95 < 200ms for single-record lookups" |
| **Completeness** | Coverage bounds | "Includes all active accounts; excludes closed > 7 years" |
| **Error handling** | Behavior on failures | "Returns cached state on ETSL unavailability, flagged as stale" |

These are **product-specific**. Different products may have different SLAs based on their consumers' needs.

### 8.4 Semantic Contracts (Inherited from ETSL)

Semantic contracts define **what terms mean**. In an ETSL world, these are inherited, not redefined:

- What is a "credit limit"? (Defined by ETSL, not the product)
- Which authority's limit is current? (Governed by ETSL reconciliation rules)
- What are the temporal semantics? (Effective dates, validity windows from ETSL)
- How are conflicts resolved? (Authority precedence from ETSL)

The Data Product does not renegotiate these definitions. It consumes them.

*Benefit:* When the definition of "credit limit" needs clarification, the change happens once in ETSL. All consuming products inherit the updated semantics without renegotiating individually.

### 8.5 Versioning Guidance

Data Products evolve. Versioning determines what changes require what level of coordination.

**Changes that can be local (product-team-owned):**

| Change Type | Example | Impact |
|-------------|---------|--------|
| Add optional fields | Add `last_updated_at` to response | Non-breaking; consumers unaffected |
| Improve performance | Reduce latency from 500ms to 200ms | Positive; no coordination needed |
| Add new aggregations | Provide pre-computed weekly averages | New capability; existing consumers unaffected |
| Deprecate unused fields | Remove `legacy_code` with warning period | Managed with deprecation notice |

These changes are governed by the product team's normal release process.

**Changes that require coordination (potential semantic impact):**

| Change Type | Example | Why Coordination Needed |
|-------------|---------|------------------------|
| Change field semantics | `limit` now includes temporary overrides | Consumers may expect different behavior |
| Change temporal pattern | Switch from "current only" to "as-of queryable" | May affect consumer caching strategies |
| Change ETSL artifact consumption | Switch from Risk limit to Ops limit | Semantic shift; consumers expecting Risk authority |
| Remove fields carrying authority | Drop `authority` field from response | Breaks audit trail for consumers |

These changes require:
1. Consumer impact assessment
2. Coordination with affected teams
3. Version bump (major version for breaking changes)

**Changes that require ETSL engagement:**

| Change Type | Example | Escalation Path |
|-------------|---------|-----------------|
| Semantic gap discovery | Product needs fact ETSL doesn't provide | Propose to ETSL Semantic Model Architects |
| Authority ambiguity | Unclear which authority governs consumed fact | Request Authority Review |
| Reconciliation confusion | Product unsure which ETSL state to consume | Request clarification from ETSL core team |

These are not product versioning issues—they are ETSL governance issues.

### 8.6 Contract Documentation

Every Data Product should document:

| Element | What to Include |
|---------|-----------------|
| **Interface contract** | Schema, fields, types, response structure |
| **SLA contract** | Freshness, availability, latency, completeness |
| **Semantic inheritance** | Which ETSL artifacts are consumed; which terms are inherited |
| **Versioning policy** | How breaking changes are communicated |
| **Lineage** | Traceability from product outputs to ETSL artifacts |

This documentation enables consumers to understand what they are getting—and what they can rely on.

---

## 9. Co‑existence with Data Mesh & Domain Products

ETSL does not eliminate domain‑owned data products, source‑aligned marts, or mesh‑style ownership. The choice between domain products and ETSL is driven by **cross‑domain truth sensitivity**, not ideology.

For the full coexistence philosophy and pattern definitions, see *ETSL and Data Mesh: Co‑existence, Complementarity, and Enterprise Evolution* (`../conceptual/etsl-and-data-mesh-coexistence-guidance.md`).

### 9.1 Banking Examples by Pattern

The three coexistence patterns—domain-first, ETSL-first, and hybrid—appear frequently in banking. The following examples illustrate each:

**Domain-First: Branch Performance Dashboard**

A retail banking dashboard showing branch-level performance: transactions processed, wait times, staffing levels, customer satisfaction scores.

- *Source:* Branch operations systems (domain-owned)
- *Consumers:* Branch managers, regional operations leads
- *ETSL involvement:* None—purely operational data within Retail
- *Risk:* If the product later needs customer identity, it may need to integrate with ETSL

---

**ETSL-First: Regulatory Exposure Report**

A consolidated customer exposure report for regulatory capital calculations, consumed by Risk, Finance, Regulatory Affairs, and external regulators.

- *Source:* ETSL Data Artifacts (Credit Limit Facts, Account Ownership Relationships, Party Identity)
- *ETSL involvement:* Essential—multiple domains and regulators depend on consistent numbers
- *Why it works:* Exposure aggregation requires consistent party identity; regulators require explainability

---

**Hybrid: Unified Customer Service Agent Desktop**

A customer service product providing agents with a unified view: identity, accounts, recent transactions, open cases, and service preferences.

- *From ETSL:* Party Identity, Account Ownership Relationships, Credit Limits
- *From Domain Products:* Recent transactions (Card Processor), Open cases (CRM), Channel preferences (Digital)
- *ETSL involvement:* Moderate—identity and ownership are cross-domain; transactions and cases are domain-local
- *Risk:* Teams must clearly distinguish which inputs require ETSL vs domain products

---

### 9.2 How Teams Decide

| Question | If Yes... | If No... |
|----------|-----------|----------|
| Does the product need cross-domain truth? | ETSL-first or hybrid | Domain-first may suffice |
| Are there regulatory or audit requirements? | ETSL provides traceability | Domain products may be acceptable |
| Do multiple domains consume this product? | ETSL ensures consistency | Domain ownership is appropriate |
| Is there known semantic dispute about this data? | ETSL reconciliation resolves it | Local semantics may be stable |

### 9.3 Avoiding Ideological Fights

Teams sometimes argue about ETSL vs domain products based on organizational politics rather than requirements. This is wasteful.

**Practical guidance:**

- **Start with the use case.** What truth does the product need? Who consumes it?
- **Assess cross-domain sensitivity.** If "only my domain," ETSL may be unnecessary overhead.
- **Check for existing ETSL artifacts.** If ETSL already provides what you need, use it—don't rebuild.
- **Escalate genuine gaps.** If you need truth that ETSL should provide but doesn't, propose it.

> **Principle:** Where ETSL Data Artifacts meet the requirements, teams are encouraged to use them. Building ETSL Data Artifacts from Domain Data Products is a business-context-informed decision, not an ideological mandate.

---

## 10. Operational Systems as Consumers and Producers

Many operational systems:
- consume data products,
- make decisions—often in response to real-time customer actions or regulatory controls,
- emit derived assertions back into ETSL.

These systems are classified as **Data-Driven Operational Applications** in *Tier-2 ETSL Canonical Classifications*.

These systems:
- must preserve lineage,
- must respect ETSL semantics,
- must not bypass truth boundaries.

This closes the enterprise truth loop safely—preventing silent divergence between decisions and reported state.

### 10.1 The Feedback Loop

Data-Driven Operational Applications are not passive consumers. They make decisions that become new enterprise truths. This creates a feedback loop:

```
ETSL Data Artifacts → Data Product → Operational Application → Decision → Derived Assertion → ETSL
```

The loop must be governed. Untracked decisions create orphaned assertions with no lineage.

### 10.2 Worked Example: Credit Decisioning and the Feedback Loop

**The Scenario**

A credit decisioning system determines whether to approve a loan application. It consumes data products built on ETSL and makes a decision that becomes enterprise truth.

**Step 1: Consumption**

The credit decisioning system consumes a Data Product that provides:
- Party identity and verification status (from ETSL Party Identity artifact)
- Existing credit limits and utilization (from ETSL Credit Limit Facts)
- Account ownership relationships (from ETSL Account Ownership artifact)
- Applicant's existing exposure (aggregated by the Data Product)

The Data Product has consumed ETSL truth and reshaped it for the decisioning use case.

**Step 2: Decision**

Based on the consumed data, policy rules, and the applicant's request, the system decides:
- **Decision:** Approve loan with limit of $50,000
- **Basis:** Applicant verified, existing exposure within policy, income sufficient

This decision is an operational output with material consequences.

**Step 3: Derived Assertion**

The approved loan becomes a new enterprise truth:
- A new Credit Limit Fact: $50,000 for the new loan account
- A new Account Ownership Relationship: Applicant owns the new account
- Decision context: Approval timestamp, policy version, input data snapshot

This must be recorded as a **Derived Assertion**—an assertion produced by a system whose behavior was influenced by Data Products.

**Step 4: ETSL Ingress**

The Derived Assertion enters ETSL through the ingress layer:
- Authority: The enterprise function the decisioning system acts on behalf of (e.g., ConsumerLending), as specified in the Authority Registry
- Lineage: References to the Data Product outputs and ETSL artifacts that informed the decision
- Temporal semantics: Effective date of the new account and limit

### 10.3 Why Lineage Matters

Without lineage from the decision back to ETSL:

| Problem | Consequence |
|---------|-------------|
| Auditors ask: "Why did you approve this loan?" | Cannot trace to input data or policy version |
| Customer disputes the limit | Cannot show what exposure data informed the decision |
| Model drift investigation | Cannot connect decision outcomes to input features |
| Regulatory reconstruction | Cannot recreate the decision context at a past point in time |

Lineage is not optional metadata—it is the audit trail that makes the enterprise defensible.

### 10.4 What Must Be Recorded

When a Data-Driven Operational Application emits a Derived Assertion, it must record at minimum:

| Element | Purpose |
|---------|---------|
| **Decision identifier** | Unique ID for traceability |
| **Decision outcome** | What was decided (approved, declined, limit set, etc.) |
| **Authority** | The enterprise function the system represents |
| **Timestamp** | When the decision was made |
| **Input references** | Which Data Product outputs were consumed |
| **ETSL artifact references** | Which ETSL artifacts ultimately informed the decision |
| **Policy version** | Which decision rules were applied |

This context travels with the Derived Assertion into ETSL.

### 10.5 What Goes Wrong Without Governance

If the feedback loop is not modeled:

**Scenario: Ungoverned Credit Decision**

The credit decisioning system approves a loan but does not emit a Derived Assertion. Instead, the loan is recorded directly in the loan origination system.

Six months later, the account becomes delinquent. An investigation asks:
- "What was the customer's exposure when we approved this loan?"
- "Which credit limits were considered?"
- "Who authorized this limit?"

The answers require manual reconstruction across multiple systems. The origination system has the outcome but not the inputs. ETSL has no record that this decision occurred. Audit fails.

**With Governance:**

The decisioning system emits a Derived Assertion with full lineage. The Derived Assertion enters ETSL as a new Credit Limit Fact. The investigation can trace:
- Decision → Derived Assertion → Input Data Product → ETSL Artifacts

The answer is available in minutes, not weeks.

### 10.6 Governance Scope

Authority associated with any operational system providing assertions or Derived Assertions is specified in the **Authority Registry**. This is enterprise-specific information and cannot be generalized or equated to the system or application itself.

The governance of Data Product–consuming operational applications is essential in many enterprises. However, the specific governance structures (approval workflows, audit requirements, change control) are enterprise-specific and outside the scope of this document.

> **Principle:** Decisions create new truth. If the truth matters, the decision must be recorded—with lineage, authority, and context.

---

## 11. Common Anti‑Patterns in ETSL‑Based Data Products

Anti-patterns in Data Product engineering often seem reasonable at the time. They become costly failures only later—when audit asks questions, when products diverge, or when new teams cannot onboard. Understanding **why** teams fall into these patterns helps prevent them.

---

### Anti-Pattern 1: Rebuilding Enterprise Truth Inside Products

**What it looks like:**
A Data Product team decides to "build customer identity from scratch" using their own matching logic, rather than consuming the ETSL Party Identity artifact.

**Why teams do it:**
- ETSL doesn't exist yet for this domain (perceived)
- ETSL's artifact doesn't have exactly the fields they want
- "It's faster to build it ourselves"
- Distrust of central teams

**Consequences:**
- Two definitions of "customer" now exist
- Cross-product consistency is accidental
- When ETSL evolves, the product is out of sync
- Audit cannot trace customer identity to authoritative source
- Onboarding new consumers requires explaining local logic

---

### Anti-Pattern 2: Embedding Authority Logic in Pipelines

**What it looks like:**
A Transforming Data Application contains code like: "If Risk limit and Ops limit both exist, take the higher one." Authority precedence is decided in pipeline logic, not governed by ETSL.

**Why teams do it:**
- The product needs a single value; pipeline code is the obvious place
- Authority Registry doesn't exist or isn't consulted
- "We know the business rule"

**Consequences:**
- Authority decisions are hidden in code
- Auditors cannot explain "why this value?" without code review
- When authority rules change, multiple pipelines must be updated
- Different products may implement different precedence, causing divergence

---

### Anti-Pattern 3: Assuming ETSL Outputs Are Immutable

**What it looks like:**
A Data Product caches ETSL state and never refreshes, assuming "truth doesn't change."

**Why teams do it:**
- Performance optimization
- Simplifies architecture
- "Credit limits don't change often"

**Consequences:**
- ETSL corrections are not reflected in the product
- Late-arriving assertions are missed
- Authority overrides (e.g., fraud blocks) are not applied
- Product serves stale data; decisions are made on outdated truth
- Regulatory reconstruction returns incorrect historical state

---

### Anti-Pattern 4: Feature Stores Redefining Semantics

**What it looks like:**
A feature engineering team creates a feature called "credit_limit" but computes it using their own logic (e.g., average of last 3 limits, or inferred from utilization patterns).

**Why teams do it:**
- ML models need features; feature stores are the standard place
- "We need predictive features, not just raw values"
- Semantic precision seems like overhead

**Consequences:**
- Other teams consume "credit_limit" as if it were ETSL truth
- Model explainability fails: "What limit did the model use?"
- Regulatory review discovers the feature differs from authoritative limits
- Feature drift goes undetected because there's no semantic anchor

---

### Anti-Pattern 5: Compliance Logic Diverging Across Products

**What it looks like:**
Multiple Data Products implement AML/KYC checks independently. Each uses slightly different thresholds, sources, or logic.

**Why teams do it:**
- Each product has different consumer requirements
- Compliance rules seem simple enough to implement locally
- Central compliance team is slow or unavailable

**Consequences:**
- Inconsistent compliance decisions across channels
- Regulatory examination finds different outcomes for similar customers
- Remediation requires fixing multiple products
- Audit cannot determine "the" compliance posture at a point in time

---

### Anti-Pattern 6: Ignoring Temporal Semantics

**What it looks like:**
A Data Product consumes only "current" ETSL state. Historical queries return "we don't have that."

**Why teams do it:**
- "We only need current data"
- Temporal storage is expensive
- Source systems don't provide history (perceived)

**Consequences:**
- Regulatory reconstruction fails
- Dispute resolution cannot recreate past state
- Model training uses only current snapshot, ignoring temporal patterns
- Audit asks "what was true on date X?" and the answer is "unknown"

---

### Anti-Pattern 7: Treating Derived Values as Authoritative

**What it looks like:**
A Data Product computes "risk score" from ETSL inputs and serves it as if it were ETSL truth. Other products consume it as authoritative.

**Why teams do it:**
- The score is useful and widely needed
- "Promoting" it feels efficient
- No clear guidance on what can be elevated

**Consequences:**
- Risk score now has no governed authority
- Changes to computation silently affect downstream consumers
- Audit asks "who authorized this score?" and there's no answer
- Semantic drift as different teams build on the ungoverned value

---

### Anti-Pattern 8: Bypassing ETSL for "Speed"

**What it looks like:**
A new product team decides ETSL is too slow or bureaucratic. They source data directly from SORs, promising to "align later."

**Why teams do it:**
- Delivery pressure
- ETSL onboarding feels slow
- "We'll fix it in v2"

**Consequences:**
- The product launches with local semantics
- "Later" never comes; technical debt accumulates
- Other products build on this one, propagating the drift
- Alignment becomes a major migration, not a small fix

---

### Anti-Pattern 9: Discarding Authority Metadata

**What it looks like:**
A Serving Data Application returns credit limits but does not expose which authority asserted them.

**Why teams do it:**
- "Consumers only need the number"
- Simplifies the API
- Authority seems like implementation detail

**Consequences:**
- Consumers cannot distinguish Risk-set limits from Ops overrides
- Audit cannot trace decisions to authority
- Compliance cannot verify appropriate authority governed the value
- Explainability fails

---

### Anti-Pattern 10: Local "Fixes" to ETSL Data

**What it looks like:**
A Data Product team notices ETSL data seems wrong (e.g., an address is outdated). They "correct" it in their product rather than escalating.

**Why teams do it:**
- Customer is complaining
- Escalation feels slow
- "We know the right answer"

**Consequences:**
- The fix is local; other products still see the "wrong" data
- ETSL is never corrected; the root cause persists
- Two versions of truth now exist
- Audit cannot determine which is authoritative

---

---

### Case Study: Regulatory Audit Failure

**The Situation**

A bank's regulatory reporting team builds a Data Product to calculate Tier 1 capital ratios. They consume credit exposure data from a risk mart that was built before ETSL existed. The mart contains "credit limits" but no authority metadata—just numbers.

**The Failure**

During a regulatory examination, auditors ask: "For customer X, what was the credit limit used in this capital calculation, and who authorized that limit?"

The reporting team can trace the number to the risk mart. But the risk mart cannot trace it further—the mart was built from multiple upstream sources with embedded reconciliation logic. The auditors find:
- Three different source systems contributed to the limit value
- The reconciliation rule ("take the highest") was never documented
- No authority is recorded; no one can say who was empowered to assert this limit
- The calculation used a limit that no single system actually authorized

**The Consequence**

The regulator issues a finding: "Material weakness in data lineage and authority traceability." The bank must remediate within 90 days. Remediation requires:
- Rebuilding the risk mart to consume ETSL Credit Limit Facts
- Retroactively documenting authority for historical data (partially impossible)
- Implementing lineage from reporting product back to ETSL
- Re-filing regulatory reports with corrected methodology

Cost: millions in remediation, reputational damage, increased regulatory scrutiny for future examinations.

**The ETSL Correction**

Had the reporting product consumed ETSL Credit Limit Facts from the start:
- Every limit would carry authority (CreditRiskManagement, RetailOperations, etc.)
- Reconciliation rules would be explicit and governed
- Lineage would trace from regulatory report → Data Product → ETSL artifact → source assertion
- The auditor's question would be answered in minutes, not weeks

---

### Case Study: ML Feature Drift Leading to Model Failure

**The Situation**

A fraud detection team builds a Feature-Oriented Data Product serving signals to real-time fraud models. One key feature is "credit utilization ratio" (current balance / credit limit). The team computes this locally:
- Balance from the card processor
- Limit from... wherever they can get it quickly (a domain mart, not ETSL)

The model performs well in testing and goes live.

**The Failure**

Six months later, model performance degrades. Fraud catch rates drop 20%. The team investigates.

They discover:
- The domain mart they used for limits was deprecated three months ago
- The mart now returns stale data (last refresh: 90 days ago)
- Limits have changed significantly for many customers (Risk reviews, temporary increases, collections restrictions)
- The "credit utilization ratio" feature is computed on 90-day-old limits
- The model is making decisions based on stale features

Worse: when they try to retrain the model, they cannot recreate historical features accurately. The training data used the stale mart; the labels reflect decisions made on incorrect inputs. The model learned the wrong patterns.

**The Consequence**

The fraud team must:
- Rebuild the feature pipeline to consume ETSL Credit Limit Facts
- Discard 6 months of training data (contaminated by stale features)
- Retrain from scratch with correct features
- Explain to stakeholders why fraud losses increased

Model explainability is compromised: for any fraud decision in the past 6 months, the team cannot accurately state what limit was used.

**The ETSL Correction**

Had the feature product consumed ETSL from the start:
- Credit limits would always reflect current, authority-qualified state
- Feature freshness would be governed by ETSL's refresh cadence (documented)
- Historical features could be reconstructed using ETSL's as-of queryability
- Model explainability would trace features → ETSL artifacts → authoritative assertions

Feature drift is not a data engineering problem—it is a semantic governance failure.

---

### Summary: Why These Patterns Are Dangerous

These anti-patterns share common traits:
- They seem efficient in the short term
- They create hidden divergence
- They surface late—usually during audits, incident reviews, regulatory examinations, or model validation exercises
- They are expensive to remediate once established

The case studies above are not hypothetical. Variants occur regularly in banks that lack semantic governance.

> **Principle:** Short-term convenience creates long-term semantic debt. Build on ETSL truth; escalate gaps; preserve lineage.

---

## 12. First Data Products on ETSL: What "Good" Looks Like

Good first data products:
- have a clear consumer,
- reuse existing ETSL artifacts,
- avoid broad "360" ambitions,
- demonstrate cross‑team reuse.

Success is measured in **reduced disagreement**—fewer reconciliation conversations—not just adoption.

### 12.1 Selection Criteria for First Data Products

Before building the first Data Product on ETSL, teams should assess fit:

| Criterion | Question | Why It Matters |
|-----------|----------|----------------|
| **Clear consumer** | Who will use this product? | Products without consumers are exercises, not value |
| **Cross-domain dependency** | Does the product need truth from multiple domains? | ETSL's value is cross-domain consistency |
| **Repeated disagreement** | Is there known semantic dispute today? | ETSL resolves disputes; products demonstrate resolution |
| **Reuse potential** | Will other initiatives benefit from this product? | Reuse validates ETSL investment |
| **ETSL artifact availability** | Do the required ETSL artifacts exist? | Building on non-existent truth requires artifact work first |
| **Tractable scope** | Can v1 deliver value without solving everything? | Ambitious scope delays delivery and undermines confidence |

If most answers are unclear, the use case may not be ready—or the ETSL foundation may need more work.

### 12.2 Good First Product Examples

**Example 1: Unified Customer Service Agent Desktop**

A Data Product that provides customer service agents with a unified view of the customer: identity, accounts, limits, and recent activity.

| Dimension | Description |
|-----------|-------------|
| **Consumer** | Customer service agents (voice, chat, branch) |
| **ETSL artifacts consumed** | Party Identity, Account Ownership, Credit Limits |
| **Cross-domain value** | Agents see consistent identity regardless of product line |
| **Previous pain** | Agents previously looked up customers in 3–4 systems with conflicting data |
| **Success indicator** | Reduced call handling time; fewer escalations due to identity confusion |

*Why this is a good first product:*
- Clear, identifiable consumer group
- Consumes existing ETSL artifacts (no new semantic work required)
- Demonstrates immediate value (agent productivity)
- Cross-domain: identity spans Retail, Cards, Loans

---

**Example 2: Fraud Detection Feature Set**

A Data Product that provides fraud models with authoritative features: party verification status, credit utilization, account age, and ownership changes.

| Dimension | Description |
|-----------|-------------|
| **Consumer** | Fraud detection models (real-time and batch) |
| **ETSL artifacts consumed** | Party Identity, Account Ownership, Credit Limits, Account State |
| **Cross-domain value** | Features are consistent across fraud use cases (card, ACH, wire) |
| **Previous pain** | Fraud teams built features independently; model explainability failed audit |
| **Success indicator** | Models can explain "what data informed this score?"; reduced feature drift |

*Why this is a good first product:*
- High-stakes use case (fraud detection)
- Demonstrates lineage and explainability value
- Reusable across multiple fraud models
- Consumes ETSL for authority-qualified inputs

---

### 12.3 Good v1 vs Over-Ambitious: A Comparison

**The Over-Ambitious Product**

A team decides their first ETSL-based Data Product will be "Enterprise Customer 360"—a comprehensive view of every customer across all products, channels, and relationships.

*Scope:*
- Party identity, verification, beneficial ownership
- All accounts across Retail, Cards, Loans, Wealth, Corporate
- All relationships (joint owners, guarantors, POA)
- All transactions, interactions, cases
- All limits, exposures, and risk indicators
- Real-time and historical

*After six months:*
- Only 3 of 8 data domains have been integrated
- Ongoing disputes about what "customer" means in each domain
- No consumer is using the product because it's "not complete yet"
- Stakeholder fatigue; ETSL credibility is questioned
- Team is stuck in integration complexity

---

**The Good v1 Product**

A different team decides their first ETSL-based Data Product will be "Customer Identity and Limits for Service Agents"—a focused view supporting agent conversations.

*Scope:*
- Party identity (name, identifiers, verification status) from ETSL
- Account ownership (primary accounts only) from ETSL
- Credit limits for active accounts from ETSL
- Recent interaction summary from CRM domain product (not ETSL)

*After three months:*
- Product is live and used by 500 agents
- Agent feedback is positive: "I can finally trust customer identity"
- Documented reduction in identity-related escalations
- Clear lineage from product to ETSL artifacts
- Team has credibility to expand scope

---

**The Difference**

| Dimension | Over-Ambitious | Good v1 |
|-----------|----------------|---------|
| **Scope** | Everything | Focused on one use case |
| **Consumers** | "Everyone" | Specific: service agents |
| **ETSL dependency** | Requires ETSL artifacts that don't exist | Uses existing artifacts |
| **Time to value** | 12+ months (never?) | 3 months |
| **Stakeholder confidence** | Declining | Building |
| **Reuse demonstration** | Not yet | Already happening |

**Lesson:** A focused product that works is worth more than a comprehensive product that doesn't ship. Scope for delivery, not coverage.

### 12.4 What Success Looks Like

Success for first Data Products is measured in outcomes, not adoption metrics:

| Indicator | What It Means |
|-----------|---------------|
| **Reduced disagreement** | Consumers no longer debate "which number is right?" |
| **Fewer reconciliation pipelines** | Teams stop building their own truth-derivation logic |
| **Faster onboarding** | New teams can consume the product without reverse-engineering semantics |
| **Audit satisfaction** | Auditors can trace product outputs to authoritative ETSL sources |
| **Cross-team reuse** | Multiple initiatives consume the same product |

> **Principle:** The first Data Product proves the pattern. It does not need to solve every problem.

---

## 13. Organizational & Workflow Implications

ETSL reshapes collaboration:
- ETSL teams stabilize meaning,
- product teams interpret meaning,
- engineers implement applications.

Clear hand‑offs reduce friction and speed delivery.

### 13.1 The Interaction Model

Building Data Products on ETSL involves multiple roles with distinct responsibilities:

| Role | Primary Responsibility | Interacts With |
|------|----------------------|----------------|
| **ETSL Semantic Model Architects** | Define and govern ETSL Semantic Artifacts, Authority Registry, reconciliation rules | Data Product Architects, Domain Architects |
| **ETSL Data Artifact Producers** | Implement ETSL Core Data Applications, produce ETSL Data Artifacts | ETSL Architects, Data Product Teams |
| **Data Product Architects** | Design Data Products that consume ETSL truth, define product contracts | ETSL Architects, Product Managers, Data Engineers |
| **Data Product Engineers** | Implement Transforming and Serving Data Applications | Data Product Architects, ETSL core team (for questions) |
| **Operational System Owners** | Manage Data-Driven Operational Applications that consume products and emit Derived Assertions | Data Product Teams, ETSL core team |
| **Domain Architects** | Own domain data products, collaborate on ETSL artifact boundaries | ETSL Architects, Data Product Architects |

### 13.2 Typical Workflow: Building a New Data Product

**Phase 1: Discovery**
- Product team identifies need and consumer
- Reviews available ETSL Data Artifacts
- Consults with ETSL Semantic Model Architects on gaps
- Determines if product is ETSL-first, domain-first, or hybrid

**Phase 2: Design**
- Product Architect designs data flow and contracts
- Documents ETSL artifacts to consume
- Documents domain products to consume (if hybrid)
- Defines temporal consumption pattern (current, as-of, historical)
- Declares Tier-2 classification

**Phase 3: Review (Lightweight)**
- Data Product Design Review with ETSL Architect (1 hour)
- Confirms ETSL consumption is correct
- Identifies any semantic gaps requiring escalation
- Validates lineage expectations

**Phase 4: Implementation**
- Data Product Engineers build Transforming and Serving Applications
- Implement lineage tracking
- Validate against ETSL semantic contracts

**Phase 5: Validation**
- Consumer validation: does the product meet use case needs?
- Semantic validation: does consumption respect ETSL semantics?
- Lineage validation: can outputs be traced to ETSL inputs?

### 13.3 Recommended Rituals

Rituals keep collaboration lightweight and prevent drift. These should be proportional to risk—not bureaucratic.

**1. Data Product Design Review**

| Aspect | Guidance |
|--------|----------|
| **When** | Before implementation begins |
| **Who** | Data Product Architect + ETSL Semantic Architect |
| **Duration** | 1 hour |
| **Output** | Confirmed ETSL artifact consumption; identified gaps; escalation actions |

*Purpose:* Catch semantic misalignment early, before code is written.

---

**2. Semantic Escalation Path**

| Aspect | Guidance |
|--------|----------|
| **When** | Product team discovers semantic gap, contested definition, or authority ambiguity |
| **Who** | Data Product Architect → ETSL Semantic Architect |
| **Process** | Documented proposal (e.g., PR on Semantic Artifacts) |
| **Output** | ETSL expansion, clarification, or rejection with rationale |

*Purpose:* Gaps are resolved upstream, not worked around locally.

---

**3. Contract/Version Change Review**

| Aspect | Guidance |
|--------|----------|
| **When** | Data Product makes changes with potential semantic impact |
| **Who** | Data Product Architect + affected consumers + ETSL Architect (if semantic) |
| **Triggers** | Changing ETSL artifact consumption, changing field semantics, removing authority metadata |
| **Output** | Approved change plan; consumer notification; version bump |

*Purpose:* Semantic changes are coordinated, not silently deployed.

---

**4. Quarterly Semantic Health Check**

| Aspect | Guidance |
|--------|----------|
| **When** | Quarterly |
| **Who** | ETSL core team + Data Product leads |
| **Activities** | Review product-ETSL consumption patterns; identify drift; prioritize backlog |
| **Output** | Drift detection; action items; lessons learned |

*Purpose:* Catch gradual drift before it becomes systemic.

### 13.4 Avoiding Bureaucracy

The goal is **governance without overhead**. Rituals should:

| Should Be | Should Not Be |
|-----------|---------------|
| Lightweight (hours, not weeks) | Multi-week approval cycles |
| Proportional to risk | Same overhead for trivial and critical changes |
| Explicit and recorded | Tribal knowledge or undocumented decisions |
| Enabling (helps teams succeed) | Blocking (gate-keeping for its own sake) |

> **Principle:** Governance exists to enable correct products, not to slow delivery. If rituals feel bureaucratic, they need adjustment.

---

## 14. ETSL vs Common Data Product Engineering Practices

ETSL-based Data Product engineering differs from common patterns in important ways. Understanding these differences helps teams explain ETSL's value and avoid falling back into familiar anti-patterns.

For comprehensive comparisons with detailed tables covering each practice, see the companion document:
- *[Comparative Perspectives: ETSL-Based Data Products vs Common Practices](etsl-data-products-vs-other-approaches.md)*

That document provides in-depth comparisons for:
1. Classic Data Warehouse / Data Lake
2. Data Mesh (Domain-Owned Products)
3. Metrics-First / Semantic Layer Tools
4. Feature Stores & ML-Centric Products
5. Event-Driven / Streaming-First Products
6. API-First Data Products
7. Derived Operational Data as Truth

### 14.1 Summary Comparison

| Practice | How Truth Is Handled | ETSL Difference |
|----------|---------------------|-----------------|
| **SOR-centric marts / Data Warehouse** | Truth is implicit; "gold tables" become de facto truth | ETSL makes truth explicit, governed, and traceable |
| **Pure Data Mesh** | Domains own semantics; cross-domain consistency is socially enforced | ETSL provides a semantic spine that domains can align to |
| **Metrics-first / Semantic Layers** | Metrics become shared truth | ETSL treats metrics as products, not truth; facts are the foundation |
| **Feature Store-first ML** | Features are treated as canonical | ETSL treats features as derived; truth is the foundation for features |
| **Streaming / Event-first** | Events are the source of truth | ETSL distinguishes events, facts, and state explicitly |
| **API-first Data Products** | API contracts define the product | ETSL: APIs serve products; semantics are inherited from ETSL |
| **Derived Operational Data** | Derived outputs treated as facts | ETSL requires Derived Assertions to carry lineage and authority |

### 14.2 What Changes and What Stays the Same

**What changes with ETSL:**
- Truth is stabilized once, upstream, before products are built
- Authority is explicit and governed, not embedded in pipelines
- Reconciliation happens in ETSL, not duplicated in every product
- Cross-product consistency is designed, not accidental
- Audit and regulatory defensibility are built-in

**What stays the same:**
- Data products are still diverse (analytical, consumer-aligned, feature-oriented, operational)
- Domain teams still own their products
- Speed of iteration for products remains high
- Products still interpret, aggregate, and reshape for their consumers
- Engineering patterns (ETL, streaming, APIs) are unchanged

### 14.3 How to Explain ETSL Data Products in One Minute

For stakeholders, executives, and new team members, use this framing:

> *"ETSL separates enterprise truth from data products.*
> *Truth is modeled once, governed centrally, and qualified by authority.*
> *Data Products are purpose-built interpretations of that truth for analytics, decisions, and applications—and can evolve quickly without redefining reality."*

This framing enables:
- Faster onboarding of experienced engineers
- Clear answers to "why are we doing this?"
- Easier architectural reviews
- Less ideological resistance

### 14.4 Key Insight

> **ETSL changes where truth is decided, not how products are built.**

Data Product teams still build pipelines, APIs, dashboards, and feature stores. What changes is that they build on a foundation of governed truth—rather than rediscovering and reconciling truth in every product.

---

## 15. Summary: What Changes and What Doesn't

### What Changes

- **Truth is stabilized once.** ETSL reconciles assertions upstream. Products consume truth; they don't derive it.
- **Authority is explicit.** Every fact carries the enterprise function that asserted it. Audit can trace any value to its source.
- **Reconciliation happens once.** Products no longer embed competing reconciliation logic. Cross-product consistency is designed.
- **Semantic gaps are escalated, not worked around.** Gaps become ETSL improvements, not local fixes that drift.
- **Lineage is mandatory.** From Data Product output back to ETSL artifact, the chain is preserved.

### What Doesn't Change

- **Diversity of Data Products.** Analytical, consumer-aligned, feature-oriented, operational—all remain.
- **Speed of iteration.** Products evolve fast; truth evolves slow. That's the design.
- **Domain ownership.** Domains still own their products. ETSL provides truth; domains interpret it.
- **Engineering patterns.** Pipelines, APIs, feature stores, dashboards—these are unchanged.
- **Consumer focus.** Products are still built for specific use cases and consumers.

### Why This Matters for Banks

Banks operate in a uniquely demanding environment:
- **Regulatory scrutiny:** Auditors and regulators expect explainable, traceable data. ETSL provides the lineage.
- **Cross-domain decisions:** Credit, risk, compliance, and customer service all need consistent truth. ETSL delivers it.
- **Speed of delivery:** Banks cannot afford 12-month data projects for every initiative. ETSL-based products ship faster because truth is already resolved.

Without ETSL, every Data Product team rebuilds the same reconciliation logic, arrives at different answers, and defends their methodology in audit. With ETSL, reconciliation is done once, correctly, and products focus on value.

### The Foundational Principle

> **ETSL decides what is true.  
> Data Products decide how to use it.**

This separation is not bureaucracy—it is the foundation for scalable, auditable, and trustworthy enterprise data.

---

## Appendix A: Data Product Design Checklist (ETSL‑Aware)

Use this checklist during Data Product design and review.

### Pre-Design Questions

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | Who is the consumer of this product? | Named consumer(s) or use case |
| 2 | Does the product require cross-domain truth? | Yes → consider ETSL; No → domain-first may suffice |
| 3 | Are there known semantic disputes for this data? | Yes → ETSL resolves them; No → lower risk |
| 4 | Do required ETSL Data Artifacts exist? | Yes → consume them; No → escalate or scope down |

### Design Validation

| # | Checkpoint | Pass Criteria |
|---|------------|---------------|
| 1 | ETSL artifacts identified | All cross-domain truth sourced from ETSL |
| 2 | Temporal pattern documented | Current, as-of, or historical—explicit |
| 3 | Tier-2 classification declared | Transforming / Serving / Operational |
| 4 | Authority metadata preserved | Not discarded from consumed artifacts |
| 5 | Lineage design complete | Traceable from outputs to ETSL inputs |
| 6 | No semantic redefinition | Product interprets, does not redefine |
| 7 | Escalation path known | Where to go for semantic gaps |
| 8 | Contract types documented | Schema, SLA, semantic inheritance |

### Post-Implementation Validation

| # | Checkpoint | Pass Criteria |
|---|------------|---------------|
| 1 | Consumer validation complete | Consumer confirms fit for purpose |
| 2 | Semantic validation complete | Consumption respects ETSL contracts |
| 3 | Lineage validation complete | Audit can trace outputs to ETSL |
| 4 | Freshness documented | Consumers know data currency |

---

## Appendix B: Terminology Declaration Template

Every Data Product **must** include a terminology declaration. This ensures consistent use of ETSL vocabulary and enables governance.

### Mandatory Elements

The following elements are **required** for every Data Product:

| Element | Status | Rationale |
|---------|--------|-----------|
| Tier-1 terms used | Required | Ensures semantic vocabulary is consistent |
| Tier-2 classification | **Mandatory** | Determines review rigor, change tolerance, and audit expectations |
| ETSL artifacts consumed | Required | Establishes lineage and semantic inheritance |
| Semantic inheritance declaration | Required | Confirms no local redefinitions |

> **Misclassification is an architectural defect.**
>
> A Data Product that declares itself as "Transforming" but actually embeds operational decision logic is misclassified. Misclassification undermines governance: review expectations are wrong, change tolerance is miscalibrated, and audit assumptions fail. Treat misclassification with the same severity as a semantic contract violation.

### Template

```
Data Product Name: [Product Name]
Version: [Version]
Date: [Date]

Tier-1 Terms Used:
-------------------------------------------------
| Term              | Canonical Meaning (Tier-1)  | How Used in This Product       |
|-------------------|-----------------------------|---------------------------------|
| Data Product      | Consumer-aligned...         | This product is a Data Product  |
| ETSL Data Artifact| Governed, authority-...     | Consumed as input               |
| Derived Assertion | Assertion produced by...    | [If applicable]                 |
| [Add others]      |                             |                                 |

Tier-2 Classification (MANDATORY):
-------------------------------------------------
| Application Layer | Classification              | Confirmed |
|-------------------|-----------------------------|-----------|
| Transformation    | Transforming Data Application | [ ] Yes   |
| Serving           | Serving Data Application      | [ ] Yes   |
| Operational (if applicable) | Data-Driven Operational Application | [ ] Yes |

Classification Rationale:
[Brief explanation of why this classification applies]

ETSL Artifacts Consumed:
-------------------------------------------------
| Artifact Name         | Authority       | Temporal Pattern Used |
|-----------------------|-----------------|-----------------------|
| Party Identity        | Various         | Current state         |
| Credit Limit Facts    | CreditRiskMgmt  | Current state         |
| Account Ownership     | RetailOps       | Full history          |
| [Add others]          |                 |                       |

Semantic Inheritance:
-------------------------------------------------
This product inherits semantic contracts from ETSL for the above artifacts.
Local semantic redefinitions: None
```

---

## Appendix C: Mapping Existing Products to ETSL Dependency Patterns

Use this framework to classify existing Data Products and plan alignment.

### Classification Framework

| Pattern | Description | ETSL Involvement | Migration Priority |
|---------|-------------|------------------|-------------------|
| **Domain-only** | Consumes only domain sources; serves domain-local use cases | None | Low—align only if cross-domain need emerges |
| **ETSL-dependent** | Consumes ETSL Data Artifacts for all truth-sensitive inputs | Full | Already aligned |
| **Hybrid** | Consumes ETSL for cross-domain truth; domain products for local context | Partial | Medium—ensure ETSL inputs are correct |
| **Unaligned** | Should consume ETSL but doesn't; uses local reconciliation | Should be full | High—creates semantic risk |

### Assessment Checklist

For each existing Data Product:

| # | Question | Answer | Implication |
|---|----------|--------|-------------|
| 1 | Does this product serve cross-domain use cases? | Yes/No | If Yes, consider ETSL alignment |
| 2 | Does this product embed reconciliation logic? | Yes/No | If Yes, high risk of semantic drift |
| 3 | Do other products consume this as if it were truth? | Yes/No | If Yes, may need ETSL migration |
| 4 | Are there known disagreements with other products? | Yes/No | If Yes, ETSL resolves |
| 5 | Is this product subject to audit or regulatory scrutiny? | Yes/No | If Yes, lineage to ETSL is valuable |

### Migration Guidance

Migration should be **use-case driven**, not mandated.

| Trigger | Action |
|---------|--------|
| Cross-domain dependency emerges | Assess ETSL artifact availability; align consumption |
| Audit finding or regulatory concern | Prioritize lineage and authority traceability |
| Product disagreement discovered | Investigate root cause; consider ETSL for reconciled truth |
| New consumer requests same data | Consider promoting to ETSL-aligned product for reuse |

---

## Glossary

This document uses terminology defined in the canonical ETSL lexicon:

- **Tier-1 ETSL Canonical Terminology** (`../terminology/tier-1-etsl-canonical-terminology.md`) — Core semantic primitives: Assertion, Authority, Reconciliation, State, Data Product, Data Artifact, Data Application
- **Tier-2 ETSL Canonical Classifications** (`../terminology/tier-2-etsl-canonical-classifications.md`) — Behavioral classifications: ETSL Core Data Application, Transforming/Serving Data Applications, Candidate Assertion, ETSL Ingress Boundary

### Terms Specific to This Document

**Consumer-Aligned Data Product**
> A Data Product designed for specific consumers or use cases (e.g., customer service agents, risk committees). Interprets truth for audience needs.

**Analytical Data Product**
> A Data Product serving dashboards, reports, and exploration. Typically slow-changing with high stability expectations.

**Feature-Oriented Data Product**
> A Data Product providing ML features. Features are derived interpretations of truth, not truth itself.

**Operationally-Consumed Data Product**
> A Data Product consumed by operational systems for real-time decisions. High stability expectations; changes are high-risk.

**Semantic Contract**
> The explicit specification of what may be asserted, how it must be structured, what authority governs it, and what invariants apply. Data Products inherit semantic contracts from ETSL.

**Schema/Interface Contract**
> The Data Product's definition of structure, field names, types, and response shapes. Owned by the product team.

**Service/SLA Contract**
> Operational expectations: freshness, availability, latency, completeness. Owned by the product team.

### Quick Reference

| Term | Role |
|------|------|
| **ETSL Data Artifact** | Stabilizes enterprise truth |
| **Data Product** | Interprets truth for consumers |
| **Transforming Data Application** | Builds data products |
| **Serving Data Application** | Exposes data products |
| **Data-Driven Operational Application** | Acts on products; may emit assertions |

---

*End of Document*

---
