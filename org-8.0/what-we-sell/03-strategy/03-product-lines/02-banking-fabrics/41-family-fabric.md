# Chapter 03.02.41: Family Fabric — Product Note

**The household and family financial orchestration infrastructure — owning the family graph, delegated permissions, shared wallets, and parental controls for the Family Financial Operating System (FFOS).**

---

## The Architectural Problem

Legacy core banking systems are strictly individual-centric. They operate on a single-customer model where accounts are owned by one or at most two individuals (joint accounts). There is no native architectural concept of a "household" or "family graph" that allows for complex, multi-member financial relationships. 

As a result, banks cannot support modern family-oriented financial products. They cannot offer pocket-money delegation for children, real-time parental spending controls, shared savings goals with dynamic contribution rules, or multi-generational wealth planning. To support these, banks are forced to build custom, fragile application-layer workarounds that do not scale and fail to enforce strict legal and regulatory compliance boundaries. This leaves families with disjointed experiences, requiring them to use third-party fintech apps to manage their household finances while the bank loses visibility into the household's total financial footprint.

---

## What It Governs

Family Fabric is the authoritative domain-specific Banking Fabric for household modeling, family relationships, delegated permissions, and parental controls. It provides the core engine for the Family Financial Operating System (FFOS), enabling banks to offer cohesive, multi-member financial products.

In scope: family graph and household profiles, delegated permission records, shared wallet configurations, parental control settings, and allowance/pocket-money schedules. Out of scope: individual customer profiles (Customer Record Fabric), individual account transaction ledgers (Demand Deposit/Revolving Credit Fabrics), core authentication (Trust Fabric), and physical card issuance (Card Issuance Fabric).

---

## Source of Truth

- **Entities owned:** Family graph, household profiles, family relationship links (parent, child, guardian, dependent), delegated permission records, shared wallet configurations, parental control settings, allowance/pocket-money schedules, minor account links.
- **Key invariants:**
  - Minor accounts must be linked to at least one verified guardian or parent profile (Party_ID).
  - Delegated permissions must be explicitly authorized by the account owner, immutably logged, and instantly revocable.
  - Spending limits and merchant category restrictions set by parents must be enforced in real-time during transaction authorization.
  - Shared wallet contributions must be tracked and balanced across participating accounts.
- **Configurable vs. compliance floor:** Family structures, allowance schedules, delegated permission levels, and spending limits are fully configurable. Compliance floor: Strict legal guardianship verification, COPPA compliance for minor data, and compliance with consumer protection regulations (e.g., Regulation E for unauthorized transactions).

---

## Scope Highlights

- **Family Graph & Household Modeling:** Establishes and manages the family graph, linking individual customer profiles into a cohesive household structure.
- **Delegated Permissions & Consent:** Manages delegated access, allowing family members to view balances, initiate transfers, or manage cards on behalf of others.
- **Shared Wallets & Goals:** Coordinates shared savings goals and multi-member funding pools with dynamic contribution and withdrawal rules.
- **Parental Controls & Allowance:** Manages pocket-money schedules, spending limits, and merchant restrictions for minor accounts.

---

## Capability Domains

### 1. Family Graph & Household Modeling

The authoritative system for managing the family graph and household profiles.

| Capability | What It Delivers |
|---|---|
| Family graph manager | Establishes and maintains the relationships (parent, child, guardian, dependent) between individual customer profiles (Party_IDs). |
| Household profile manager | Aggregates family graphs into household profiles to support household-level analytics and relationship pricing (via Deposit/Credit Relationship Fabrics). |
| Guardian verifier | Verifies and records legal guardianship documents and relationships before linking minor accounts. |

### 2. Delegated Permissions & Consent

Manages delegated access, viewing rights, and transaction permissions.

| Capability | What It Delivers |
|---|---|
| Delegated access manager | Maintains the authoritative ledger of delegated permissions (e.g., view balance, initiate transfers, lock card) across family accounts. |
| Consent capture coordinator | Coordinates with Trust Fabric to capture and log explicit consent from account owners before granting delegated access. |
| Real-time permission resolver | Exposes high-performance APIs to resolve active permissions during channel requests or transaction authorization. |

### 3. Shared Wallets & Goals

Coordinating shared savings goals and multi-member funding pools.

| Capability | What It Delivers |
|---|---|
| Shared wallet coordinator | Configures and manages shared wallets, defining contribution rules (e.g., split 50/50, or percentage-based) and withdrawal permissions. |
| Goal tracker | Tracks progress toward shared family savings goals, calculating individual contributions and projecting completion dates. |
| Joint ledger synchronizer | Coordinates with Demand Deposit Fabric to ensure shared wallet transactions are accurately posted to participating accounts. |

### 4. Parental Controls & Allowance

Managing pocket-money schedules, spending limits, and merchant restrictions.

| Capability | What It Delivers |
|---|---|
| Allowance scheduler | Automates pocket-money and allowance transfers from parent accounts to minor accounts based on configured schedules (e.g., weekly, monthly). |
| Parental control enforcer | Maintains spending limits, daily transaction caps, and merchant category code (MCC) restrictions for minor accounts. |
| Authorization rules resolver | Exposes high-performance APIs to Card Issuer Txn Processing Fabric to enforce parental controls during real-time transaction authorization. |

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| **Customer Record Fabric** | Customer Record owns individual customer profiles (Party_ID); Family Fabric links these profiles into a household graph. |
| **Trust Fabric** | Trust Fabric manages the authentication and consent capture for delegated access; Family Fabric stores the resolved permission states. |
| **Card Issuer Txn Processing Fabric** | Card Issuer Txn Processing queries Family Fabric for parental controls and spending limits during real-time authorization. |
| **Demand Deposit Fabric** | Family Fabric coordinates shared wallets, allowance transfers, and minor savings accounts with checking/savings accounts. |
| **Deposit Relationship Fabric** | Deposit Relationship consumes the family graph to calculate household-level aggregated balances for relationship pricing. |
| **Credit Relationship Fabric** | Credit Relationship consumes the family graph to evaluate household-level credit exposure and co-signing relationships. |

---

## References

- [Customer Record Fabric](02-customer-record-fabric.md) — Customer master data and identity
- [Card Issuer Txn Processing Fabric](17-card-issuer-txn-processing-fabric.md) — Authorization, clearing, and settlement
- [Demand Deposit Fabric](05-demand-deposit-fabric.md) — Authoritative demand deposit account ledger
- [Deposit Relationship Fabric](37-deposit-relationship-fabric.md) — Deposit relationship and portfolio aggregation
