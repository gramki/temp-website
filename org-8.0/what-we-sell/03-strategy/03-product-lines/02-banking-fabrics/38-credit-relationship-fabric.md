# Chapter 03.02.38: Credit Relationship Fabric — Product Note

**The credit relationship and exposure orchestration infrastructure — owning consolidated credit exposure tracking, cross-product repayment schedules, and relationship-level credit limits across revolving, term, and mortgage lending.**

---

## The Architectural Problem

Legacy core banking systems manage credit and lending products on completely separate, disconnected platforms. Personal loans reside on an installment core, credit cards on a card processing platform, and mortgages on a specialized mortgage servicing system. Because these systems do not communicate, banks are blind to a customer's total credit exposure in real-time. 

This fragmentation prevents banks from offering relationship-centric credit experiences. It is impossible to offer consolidated repayment options (e.g., a single monthly payment covering a credit card, personal loan, and mortgage), dynamic credit limit adjustments based on overall relationship health, or cross-collateralized lending structures. To assess exposure, banks must run slow, offline batch reconciliations, which increases credit risk, delays decisioning, and frustrates customers who expect their entire credit relationship to be recognized and rewarded.

---

## What It Governs

Credit Relationship Fabric is the authoritative domain-specific Banking Fabric for customer-level credit portfolio aggregation, consolidated exposure tracking, and relationship-based repayment rules. It sits above individual credit ledgers, orchestrating how multiple credit products combine to form a single, cohesive credit relationship.

In scope: real-time consolidated credit exposure tracking, relationship-level credit limit management, cross-product repayment orchestration, and cross-collateralization linking. Out of scope: individual revolving credit ledgers (Revolving Credit Fabric), individual term loan amortization schedules (Term Loans Fabric), core mortgage servicing (Mortgage Fabric), and initial credit underwriting decisions (Underwriting Fabric).

---

## Source of Truth

- **Entities owned:** Credit relationship profile, consolidated credit exposure trackers, relationship-level credit limits, cross-product repayment schedules, cross-collateralization links, exposure risk classifications.
- **Key invariants:**
  - Consolidated credit exposure must be computed in real-time across all active credit, loan, and mortgage accounts for a given Party_ID.
  - Relationship-level credit limits cannot exceed the maximum exposure approved by Underwriting Fabric.
  - Cross-collateralization links must be legally bound and verified before collateral value is applied to relationship credit limits.
  - Consolidated repayment payments must be distributed across linked accounts according to defined priority rules.
- **Configurable vs. compliance floor:** Repayment priority rules, exposure thresholds, dynamic limit adjustment parameters, and cross-collateralization ratios are fully configurable. Compliance floor: Accurate exposure calculation, adherence to credit reporting regulations (e.g., FCRA in the US), and compliance with lending disclosure requirements (e.g., Regulation Z/Truth in Lending in the US).

---

## Scope Highlights

- **Consolidated Credit Exposure:** Aggregates outstanding balances, available credit, and total limits across credit cards, loans, and mortgages in real-time.
- **Cross-Product Repayment Orchestration:** Coordinates consolidated repayment schedules, allowing customers to make a single payment that is distributed across multiple credit products.
- **Relationship-Level Credit Limits:** Manages consolidated credit limits, allowing credit limits on one product to dynamically adjust based on the performance and utilization of other products.
- **Cross-Collateralization Management:** Links and manages collateral (e.g., deposit balances, home equity) across multiple credit products to optimize borrowing power and reduce risk.

---

## Capability Domains

### 1. Consolidated Credit Exposure

The authoritative system for tracking and aggregating credit exposure across a customer's entire credit portfolio.

| Capability | What It Delivers |
|---|---|
| Real-time exposure aggregator | Subscribes to balance and limit-change events from Revolving Credit, Term Loans, and Mortgage Fabrics, maintaining real-time consolidated exposure views. |
| Exposure risk classifier | Analyzes consolidated utilization and repayment behaviors to assign relationship-level credit risk classifications. |
| Portfolio exposure monitor | Monitors consolidated exposure against regulatory and bank-defined concentration limits, emitting alerts when thresholds are breached. |

### 2. Cross-Product Repayment Orchestration

Coordinates consolidated repayment schedules and payment distribution.

| Capability | What It Delivers |
|---|---|
| Consolidated payment scheduler | Orchestrates a single, consolidated payment schedule for customers with multiple credit products, generating unified payment demands. |
| Payment distribution engine | Distributes consolidated payments across linked credit accounts based on defined priority rules (e.g., pay off highest interest rate first, or cover past-due balances first). |
| Repayment holiday coordinator | Manages relationship-level repayment holidays or relief programs, applying them consistently across linked credit products. |

### 3. Relationship-Level Credit Limits

Manages consolidated credit limits and exposure thresholds.

| Capability | What It Delivers |
|---|---|
| Consolidated limit manager | Maintains and manages relationship-level credit limits that span multiple credit products (e.g., a shared limit across a credit card and a personal line of credit). |
| Dynamic limit adjuster | Automatically adjusts credit limits on individual products based on the customer's overall relationship health and consolidated utilization. |
| Exposure cap enforcer | Enforces maximum exposure caps approved by Underwriting Fabric, preventing automated limit increases from exceeding approved risk boundaries. |

### 4. Cross-Collateralization Management

Links and manages collateral across multiple credit products.

| Capability | What It Delivers |
|---|---|
| Collateral linker | Establishes and manages the legal and technical links between collateral assets (e.g., deposit balances, investment portfolios, property) and multiple credit accounts. |
| Collateral valuation engine | Tracks the real-time value of linked collateral and calculates available borrowing power across credit products. |
| Collateral release coordinator | Manages the release or substitution of collateral, ensuring that collateral is never released if doing so would violate exposure invariants. |

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| **Revolving Credit Fabric** | Credit Relationship queries credit card balances and limits, and applies relationship-level limit adjustments back to Revolving Credit. |
| **Term Loans Fabric** | Credit Relationship queries personal/auto loan balances and schedules, and coordinates consolidated repayment distribution to Term Loans. |
| **Mortgage Fabric** | Credit Relationship queries mortgage balances and collateral, and incorporates them into consolidated exposure and cross-collateralization views. |
| **Underwriting Fabric** | Underwriting Fabric provides the risk assessment and maximum exposure limits; Credit Relationship enforces these limits during lifecycle limit adjustments. |
| **Customer Record Fabric** | Customer Record owns the core customer identity (Party_ID); Credit Relationship links multiple credit accounts to a single Party_ID. |
| **Accounting Fabric** | Credit Relationship coordinates with Accounting Fabric to ensure consolidated payment distributions are accurately recorded in the general ledger. |

---

## References

- [Revolving Credit Fabric](07-revolving-credit-fabric.md) — Authoritative revolving credit account ledger
- [Term Loans Fabric](08-term-loans-fabric.md) — Personal, auto, and installment loans ledger
- [Mortgage Fabric](09-mortgage-fabric.md) — Home loans and property-backed lending
- [Underwriting Fabric](10-underwriting-fabric.md) — Credit decisioning and risk assessment
