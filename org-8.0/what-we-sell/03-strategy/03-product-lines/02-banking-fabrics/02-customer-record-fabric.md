# Chapter 03.02.02: Customer Record Fabric — Product Note

**The authoritative system of record for customer identity, relationships, and lifecycle — the master that answers "who is this customer and how do they relate to accounts, products, and other parties?"**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Customer Record Fabric owns the customer master — the single source of truth for who customers are, their identifying information, their relationships to other parties, and their lifecycle state. Every channel, product, and process that needs to know "who is this?" queries this fabric.

In scope: customer identity (individuals and entities), KYC data, demographic and contact information, relationship structures (households, beneficial owners, authorized signers), party roles, customer lifecycle (prospect, active, dormant, closed), and cross-product customer views. Out of scope: identity verification and authentication (Trust Fabric), credit decisioning (Underwriting Fabric), and account/product records (domain fabrics).

---

## Source of Truth

- **Entities owned:** Customer records (individuals, entities), party identifiers, KYC profiles, demographic data, contact information, relationship structures (households, corporate hierarchies, beneficial ownership), authorized parties, customer lifecycle states
- **Key invariants:** Every customer has a unique, immutable identifier. KYC verification status is authoritative and timestamped. Relationship structures are acyclic where required (e.g., beneficial ownership chains). Regulatory-required data elements are present before account opening is permitted.
- **Configurable vs. compliance floor:** Party types, relationship types, demographic attributes, and lifecycle state definitions are configurable per jurisdiction and bank policy. Unique identification, KYC data completeness for regulated activities, and relationship integrity are the non-negotiable compliance floor.

---

## Scope Highlights

- Maintains the customer master with individual and entity party types
- Stores and maintains KYC data elements required for regulatory compliance (identity documents, verification status, risk rating)
- Models relationships: household memberships, corporate structures, beneficial ownership, authorized signers, powers of attorney
- Provides cross-product customer views — "show me everything this customer has with the bank"
- Tracks customer lifecycle from prospect through active relationship to closure
- Supports customer merge and de-duplication with audit trail

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Party Management** — Customer creation, identity management, party types (individual, entity), unique identification
2. **KYC Data Management** — Identity documents, verification status, periodic review, risk rating, sanctions screening hooks
3. **Relationship Modeling** — Household structures, corporate hierarchies, beneficial ownership, authorized parties, role assignments
4. **Demographic and Contact** — Addresses, phone numbers, email, communication preferences, demographic attributes
5. **Customer Lifecycle** — State transitions (prospect → active → dormant → closed), lifecycle events, reactivation
6. **Cross-Product Views** — Customer-centric aggregation across all products and accounts, relationship summarization

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Trust Fabric | Trust Fabric handles identity verification and authentication; Customer Record Fabric stores the verified identity and KYC data as system of record |
| Product Fabric | Product eligibility may depend on customer attributes; Customer Record Fabric provides the customer data, Product Fabric owns eligibility rules |
| Demand Deposit Fabric | Deposit accounts are linked to customers; Customer Record Fabric owns the customer, Demand Deposit owns the account |
| Revolving Credit Fabric | Credit products are linked to customers; Customer Record Fabric owns the customer identity and relationships |
| Underwriting Fabric | Credit decisions reference customer data; Customer Record Fabric provides it, Underwriting Fabric makes decisions |
| Truth Fabric | Customer Record Fabric is authoritative for customer identity; Truth Fabric governs cross-fabric semantic agreement on customer-related terms |

---

## References

_To be added._
