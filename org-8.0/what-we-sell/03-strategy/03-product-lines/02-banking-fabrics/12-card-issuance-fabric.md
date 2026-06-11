# Chapter 03.02.12: Card Issuance Fabric — Product Note

**The system of record for consumer card identity and lifecycle — managing the physical and virtual instruments that represent payment credentials from issuance through expiration, replacement, and closure.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Card Issuance Fabric owns the identity, state, and lifecycle of consumer payment cards issued by the bank. This includes plastic cards (embossed, instant-issue, co-branded), virtual cards, and supplementary cards tied to a primary account. The fabric governs card ordering, personalization, activation, status management (block, unblock, hot-card), PIN lifecycle, and reissuance workflows. It does not govern the underlying credit or deposit account (owned by Credit or Deposit Fabrics), card transaction authorization (Card Issuer Transaction Processing Fabric), or tokenized representations of the card (Issuer Tokenization Fabric).

---

## Source of Truth

- **Entities owned:** Card, Card Order, Card Status, PIN Block, Card-to-Account Linkage, Supplementary Card Relationship, Card Personalization Record, Reissuance Request
- **Key invariants:**
  - Every card has exactly one authoritative status at any point in time (active, inactive, blocked, expired, closed)
  - A card cannot authorize transactions unless its status is active and not expired
  - PIN state is always known — set, unset, or locked — and PIN attempt counters are atomically maintained
  - Card numbers are unique and conform to issuer BIN ranges and Luhn validation
  - Supplementary cards inherit and respect primary card restrictions
- **Configurable vs. compliance floor:**
  - *Configurable:* Card designs, embossing rules, reissuance triggers, PIN retry limits, activation channels, replacement fee policies, virtual card validity periods
  - *Compliance floor:* PCI DSS controls on card data at rest and in transit; card status must reflect real-time blocking decisions; lost/stolen reports must propagate to authorization within mandated timeframes; cardholder verification requirements for PIN changes

---

## Scope Highlights

- Card ordering and personalization — coordinating with embossing vendors, instant-issuance devices, and digital-first issuance flows
- Card activation across channels — IVR, mobile app, branch, first-use activation
- Status management — voluntary blocks, fraud blocks, temporary holds, permanent closure
- PIN lifecycle — initial PIN set, PIN change, PIN reset, PIN unblock after lockout
- Reissuance orchestration — expiry-driven, damage replacement, lost/stolen, account number change migrations
- Supplementary and add-on card management — linking to primary, inheriting controls, independent blocking

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Card Ordering and Fulfillment
2. Card Personalization and Embossing
3. Activation and Status Management
4. PIN Lifecycle Management
5. Reissuance and Replacement
6. Supplementary Card Management
7. Card Inventory and BIN Management

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Revolving Credit Fabric | Card Issuance creates the payment instrument; Revolving Credit owns the credit facility the card draws against |
| Demand Deposit Fabric | For debit cards, Card Issuance owns the card; Demand Deposit owns the account balance |
| Issuer Tokenization Fabric | Card Issuance owns the PAN; Tokenization Fabric owns token provisioning and token-to-PAN mapping |
| Card Issuer Transaction Processing Fabric | Card Issuance provides card status for authorization decisions; Transaction Processing owns the auth/clearing/settlement |
| Card Authentication Fabric | Card Issuance provides card and cardholder data; Authentication Fabric owns 3DS and SCA flows |
| Product Fabric | Product Fabric defines card product catalog and eligibility; Card Issuance instantiates cards against those products |

---

## References

_To be added._
