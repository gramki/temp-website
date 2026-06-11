# Chapter 03.02.39: Card Relationship Fabric — Product Note

**The cardholder relationship and preference orchestration infrastructure — owning consolidated multi-card relationship views, unified cardholder preferences, and smart card routing rules across debit, credit, and prepaid cards.**

---

## The Architectural Problem

Legacy card processing platforms treat each card (debit, credit, or prepaid) as an isolated credential tied to a specific account. There is no architectural concept of a "cardholder relationship" that spans across different card products. Consequently, a customer who holds a debit card and two credit cards with the same bank must manage security controls, spending limits, and travel notifications for each card separately. 

This fragmentation results in a highly disjointed customer experience. For example, if a customer travels abroad, they must set travel notifications on three separate screens in their mobile app, and bank agents must navigate multiple systems to assist them. Furthermore, legacy systems cannot support advanced, multi-product card experiences — such as a single physical card that dynamically routes transactions to a checking account or a credit line based on transaction amount, merchant category, or real-time balance availability.

---

## What It Governs

Card Relationship Fabric is the authoritative domain-specific Banking Fabric for customer-level card portfolio orchestration, unified cardholder preferences, and smart transaction routing rules. It sits above individual card issuance and transaction processing systems, providing a unified cardholder relationship layer.

In scope: real-time consolidated cardholder views, unified preference and alert management, unified travel notifications, and smart card routing engine rules. Out of scope: physical card manufacturing and shipping (Card Issuance Fabric), core network authorization and clearing (Card Issuer Txn Processing Fabric), individual account ledgers (Demand Deposit/Revolving Credit Fabrics), and merchant-side acquiring (Payment Acquiring Fabric).

---

## Source of Truth

- **Entities owned:** Cardholder relationship profile, consolidated card portfolio, unified cardholder preferences, unified travel notifications, cross-card spending limits, smart card routing rules, cardholder-to-card relationship links.
- **Key invariants:**
  - Cardholder preferences and security controls must be applied consistently across all active cards linked to a Party_ID.
  - Unified travel notifications must be propagated to all active card networks (Visa, Mastercard, etc.) in real-time.
  - Smart card routing rules must resolve to a valid, active funding source (checking account or credit line) before transaction authorization.
  - Cross-card spending limits must be evaluated in real-time across all linked cards during authorization.
- **Configurable vs. compliance floor:** Cardholder preferences, spending limits, travel notification dates, and smart routing rules are fully configurable. Compliance floor: PCI DSS compliance for cardholder data, adherence to card network rules (Visa, Mastercard), and secure propagation of security preferences.

---

## Scope Highlights

- **Consolidated Cardholder View:** Aggregates all active debit, credit, and prepaid cards for a cardholder to provide a single, unified card portfolio view.
- **Unified Preference Management:** Manages cardholder preferences, alerts, and security controls (e.g., lock/unlock, transaction blocks) in a unified, cross-product way.
- **Unified Travel Notifications:** Coordinates travel notifications and propagates them to all card networks and fraud engines in real-time.
- **Smart Card Routing Engine:** Resolves funding sources for multi-product cards based on cardholder-defined rules (e.g., transactions over $100 route to credit; transactions under $100 route to debit).

---

## Capability Domains

### 1. Consolidated Cardholder View

The authoritative system for tracking and aggregating all active cards for a cardholder.

| Capability | What It Delivers |
|---|---|
| Card portfolio aggregator | Subscribes to card-lifecycle events from Card Issuance Fabric and maintains real-time consolidated card portfolio views for each Party_ID. |
| Card linker | Establishes and manages the relationships between a cardholder's Party_ID and their various card credentials (PANs, tokens). |
| Cardholder status monitor | Monitors the status of all cards in the portfolio, emitting alerts if multiple cards are reported lost/stolen or suspended. |

### 2. Unified Preference Management

Manages cardholder preferences, alerts, and security controls in a unified way.

| Capability | What It Delivers |
|---|---|
| Unified preference manager | Maintains cardholder preferences (e.g., preferred billing cycle, language, alert channels) and applies them consistently across all cards. |
| Unified card locker | Allows cardholders to lock or unlock all cards in their portfolio with a single action, propagating the lock state to processing engines. |
| Cross-card limit manager | Enforces cross-card spending limits (e.g., a maximum daily spend across all debit and credit cards in the portfolio). |

### 3. Unified Travel Notifications

Coordinating travel notifications and propagating them to card networks.

| Capability | What It Delivers |
|---|---|
| Travel notification manager | Captures cardholder travel plans (destinations, dates) and maintains the authoritative travel schedule. |
| Network travel propagator | Propagates travel notifications to card networks (Visa, Mastercard) and internal issuer fraud engines in real-time. |
| Travel-based fraud override | Automatically adjusts fraud risk scoring parameters for transactions initiated within the declared travel destination and dates. |

### 4. Smart Card Routing Engine

Resolves funding sources for multi-product cards based on cardholder rules.

| Capability | What It Delivers |
|---|---|
| Routing rules evaluator | Evaluates cardholder-defined rules (e.g., transaction amount, merchant category, time of day) to determine the target funding source. |
| Funding source resolver | Verifies balance availability on the target funding source (checking account via Demand Deposit, or credit line via Revolving Credit) before routing. |
| Routing decision responder | Exposes high-performance APIs to the Card Issuer Txn Processing Fabric to resolve the funding source during real-time authorization. |

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| **Card Issuance Fabric** | Card Issuance Fabric provisions cards and tokens; Card Relationship aggregates them into the cardholder's portfolio. |
| **Card Issuer Txn Processing Fabric** | Card Issuer Txn Processing queries Card Relationship for smart routing decisions and unified security preferences during real-time authorization. |
| **Demand Deposit Fabric** | Card Relationship queries checking/savings balances to validate debit-routing rules for multi-product cards. |
| **Revolving Credit Fabric** | Card Relationship queries credit card balances and limits to validate credit-routing rules for multi-product cards. |
| **Issuer Fraud and Risk Fabric** | Card Relationship propagates travel notifications and security preferences to the Fraud and Risk Fabric to optimize fraud detection. |
| **Customer Record Fabric** | Customer Record owns the core customer identity (Party_ID); Card Relationship links multiple cards to a single Party_ID. |

---

## References

- [Card Issuance Fabric](12-card-issuance-fabric.md) — Consumer and retail card issuance
- [Card Issuer Txn Processing Fabric](17-card-issuer-txn-processing-fabric.md) — Authorization, clearing, and settlement
- [Demand Deposit Fabric](05-demand-deposit-fabric.md) — Authoritative demand deposit account ledger
- [Revolving Credit Fabric](07-revolving-credit-fabric.md) — Authoritative revolving credit account ledger
