# Chapter 03.02.37: Deposit Relationship Fabric — Product Note

**The deposit relationship and portfolio orchestration infrastructure — owning relationship-level deposit aggregation, dynamic interest-bearing tiers, and deposit-specific servicing rules across checking, savings, and money market accounts.**

---

## The Architectural Problem

Legacy core banking systems treat deposit accounts as isolated transactional silos. Each checking, savings, or money market account operates on its own ledger with no awareness of other accounts owned by the same customer or household. Consequently, legacy systems fail to aggregate balances across a customer's entire portfolio to determine relationship-level pricing, fee waivers, or interest tiers. 

To compensate, banks resort to batch-processed, end-of-day database joins or external data warehouses to calculate relationship benefits. This results in stale data, delayed rewards, and an inability to dynamically adjust interest rates or waive fees based on real-time balance changes. Furthermore, legacy cores cannot support complex, multi-account deposit structures or dynamic relationship-based benefits without extensive custom coding, creating massive technical debt and limiting a bank's ability to compete on relationship-centric retail experiences.

---

## What It Governs

Deposit Relationship Fabric is the authoritative domain-specific Banking Fabric for customer-level deposit portfolio aggregation, relationship pricing, and servicing rules. It sits above individual demand deposit accounts, orchestrating how multiple accounts combine to form a single, cohesive deposit relationship.

In scope: real-time portfolio balance aggregation, customer relationship tier evaluation, dynamic interest rate overrides, relationship-level fee-waiver eligibility, and deposit-specific servicing rules. Out of scope: individual account transaction ledgers (Demand Deposit Fabric), core interest calculation and posting engines (Demand Deposit Fabric), base product catalog definitions (Product Fabric), and direct customer communication channels (Engagement Fabric).

---

## Source of Truth

- **Entities owned:** Deposit relationship profile, relationship tier definitions, aggregated deposit balance trackers, dynamic interest rate overrides, fee-waiver eligibility states, relationship-level benefits, account-to-party relationship links.
- **Key invariants:**
  - Aggregated balances must be computed in real-time across all active, linked deposit accounts for a given Party_ID.
  - Relationship tier transitions must trigger automatically and immutably when aggregated balances cross defined thresholds.
  - Dynamic rate overrides must be validated against product-defined compliance ceilings before application.
  - Relationship-level fee-waiver states must be synchronized with the respective transactional ledgers to prevent double-charging.
- **Configurable vs. compliance floor:** Tier thresholds, interest rate boosts/multipliers, fee-waiver rules, and relationship benefit catalogs are fully configurable per bank policy. Compliance floor: Accurate balance aggregation across accounts, strict audit trails for rate overrides, and compliance with deposit disclosure regulations (e.g., Regulation DD/Truth in Savings in the US).

---

## Scope Highlights

- **Real-Time Portfolio Aggregation:** Aggregates balances across checking, savings, and money market accounts instantly to provide a single, consolidated deposit relationship view.
- **Dynamic Relationship Tiers:** Automatically assigns and updates customer relationship tiers (e.g., Silver, Gold, Platinum) based on real-time aggregated balances.
- **Dynamic Rate & Fee Customization:** Applies relationship-level interest rate boosts and fee waivers dynamically based on the customer's active tier.
- **Relationship Servicing Rules:** Exposes servicing parameters and relationship-level rules to the Relationship Hub to guide agent-led or AI-led servicing.

---

## Capability Domains

### 1. Portfolio Balance Aggregation

The authoritative system for tracking and aggregating balances across a customer's entire deposit portfolio.

| Capability | What It Delivers |
|---|---|
| Real-time balance aggregator | Subscribes to balance-change events from Demand Deposit Fabric and maintains real-time aggregated balance views across checking, savings, and money market accounts. |
| Portfolio linking manager | Establishes and manages the relationships between a customer's Party_ID and their various Account_IDs, supporting joint accounts and multi-owner structures. |
| Aggregation rules engine | Evaluates which balance types (e.g., ledger, available, average daily balance) are included in relationship calculations based on product rules. |

### 2. Relationship Tier Engine

Evaluates and manages customer relationship tiers based on portfolio metrics.

| Capability | What It Delivers |
|---|---|
| Tier evaluator | Evaluates customer eligibility for relationship tiers (e.g., Gold, Platinum) based on real-time aggregated balances and relationship tenure. |
| Tier transition manager | Handles the transition of customers between tiers, emitting tier-change events that trigger downstream benefits or notifications. |
| Household aggregation | Extends balance aggregation to household structures (via Family Fabric) to support household-level relationship tiers. |

### 3. Dynamic Rate & Fee Customization

Applies relationship-level interest rate boosts and fee waivers.

| Capability | What It Delivers |
|---|---|
| Rate boost manager | Calculates and applies relationship-level interest rate boosts to checking or savings accounts based on the customer's active tier. |
| Fee waiver coordinator | Evaluates eligibility for fee waivers (e.g., monthly maintenance fees, ATM fees) and communicates waiver states to transactional ledgers. |
| Rate override auditor | Maintains a strict, immutable audit trail of all manual and automated interest rate overrides for compliance purposes. |

### 4. Relationship Servicing Rules

Exposes relationship-level servicing parameters to operational hubs.

| Capability | What It Delivers |
|---|---|
| Servicing rules resolver | Resolves relationship-level servicing rules (e.g., priority routing, dedicated RM assignment) based on the customer's active tier. |
| Benefit catalog manager | Maintains the catalog of active benefits associated with each relationship tier, exposing them to the Relationship Hub. |

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| **Demand Deposit Fabric** | Deposit Relationship queries balances from Demand Deposit and applies relationship-level rate boosts and fee waivers back to individual accounts. |
| **Customer Record Fabric** | Customer Record owns the core customer identity (Party_ID); Deposit Relationship links multiple accounts to a single Party_ID. |
| **Product Fabric** | Product Fabric defines base interest rates and fee schedules; Deposit Relationship applies relationship-level modifications and overrides. |
| **Influence Fabric** | Influence Fabric coordinates loyalty rewards and points; Deposit Relationship triggers rewards for relationship milestones (e.g., tier upgrades). |
| **Family Fabric** | Family Fabric provides household graphs; Deposit Relationship consumes these graphs to calculate household-level aggregated balances. |

---

## References

- [Demand Deposit Fabric](05-demand-deposit-fabric.md) — Authoritative demand deposit account ledger
- [Customer Record Fabric](02-customer-record-fabric.md) — Customer master data and identity
- [Family Fabric](41-family-fabric.md) — Family graph and household delegation
- [Product Fabric](03-product-fabric.md) — Base product configurations and pricing
