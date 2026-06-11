# Chapter 03.02.03: Product Fabric — Product Note

**The authoritative system of record for the bank's product catalog — what products exist, what they cost, who can have them, and how they are configured — enabling any channel to offer any product with consistent terms.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Product Fabric owns the product catalog and product configuration — the definitions of every banking product the institution offers, their pricing, eligibility criteria, features, and lifecycle. When a channel needs to display available products, check eligibility, or initiate issuance, it queries this fabric.

In scope: product definitions, pricing and fee structures, eligibility rules, product features and variants, product bundling, product lifecycle (active, sunset, grandfathered), issuance orchestration entry points, product change management. Out of scope: the actual product instances (accounts, loans, cards — owned by domain fabrics), credit decisioning (Underwriting Fabric), and customer data (Customer Record Fabric).

---

## Source of Truth

- **Entities owned:** Product definitions, product versions, pricing structures, fee schedules, eligibility rules, product features, product bundles, product lifecycle states, product-to-ledger mappings
- **Key invariants:** Every product has a unique identifier and version. Active products have complete, validated configurations. Pricing and eligibility rules are effective-dated — changes do not retroactively alter existing relationships. Product retirement follows defined sunset rules.
- **Configurable vs. compliance floor:** Product features, pricing, eligibility criteria, and bundling rules are highly configurable — this is the primary policy surface. Regulatory product constraints (e.g., maximum interest rates, required disclosures), version integrity, and effective-dating discipline are the compliance floor.

---

## Scope Highlights

- Maintains the product catalog with full configuration for each product type (deposits, loans, cards, etc.)
- Defines pricing structures: interest rates, fee schedules, promotional rates, relationship pricing tiers
- Specifies eligibility rules: who qualifies for which products based on customer attributes, existing relationships, credit criteria
- Supports product bundling: packages of related products with combined pricing or cross-product benefits
- Manages product lifecycle: launch, modification, sunset, grandfathering of existing customers
- Provides product comparison and recommendation data for channel presentation

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Catalog Management** — Product definitions, categories, hierarchies, search and discovery
2. **Pricing Engine** — Interest rate structures, fee schedules, promotional pricing, relationship-based pricing
3. **Eligibility Engine** — Rule-based eligibility evaluation, pre-qualification, cross-product eligibility dependencies
4. **Feature Configuration** — Product features, variants, options, add-ons, customization boundaries
5. **Bundling and Packaging** — Product bundles, cross-sell packages, combined pricing rules
6. **Product Lifecycle** — Version management, effective dating, sunset rules, grandfathering, migration paths

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Customer Record Fabric | Eligibility evaluation requires customer data; Product Fabric queries Customer Record Fabric for attributes |
| Underwriting Fabric | Credit product eligibility often requires credit decision; Product Fabric defines criteria, Underwriting Fabric makes the decision |
| Demand Deposit Fabric | Deposit product definitions live in Product Fabric; actual deposit accounts live in Demand Deposit Fabric |
| Term Deposit Fabric | FD/CD product definitions live in Product Fabric; actual term deposits live in Term Deposit Fabric |
| Revolving Credit Fabric | Credit card and LOC product definitions live in Product Fabric; actual credit accounts live in Revolving Credit Fabric |
| Term Loans Fabric | Loan product definitions live in Product Fabric; actual loans live in Term Loans Fabric |
| Accounting Fabric | Product definitions include posting rules that Accounting Fabric executes when product instances transact |
| Sourcing Fabric | Product Fabric provides product catalog for origination flows; Sourcing Fabric handles application and lead management |

---

## References

_To be added._
