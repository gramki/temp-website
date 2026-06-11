# Chapter 03.02.17: Card Issuer Transaction Processing Fabric — Product Note

**The system of record for card transaction lifecycle from the issuing bank's perspective — managing authorization decisions, clearing message processing, and settlement with networks while enforcing cardholder limits, fraud rules, and account integrity.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Card Issuer Transaction Processing Fabric owns the real-time and batch processing of card transactions where the bank is the issuer. This includes authorization request handling (approve, decline, refer), clearing message processing (presentments, adjustments, reversals), and settlement with card networks (Visa, Mastercard, Amex, Discover, RuPay). The fabric makes authorization decisions by evaluating card status, available balance or credit, cardholder limits, velocity rules, and fraud signals — then posts cleared transactions to the account. It does not own the card itself (Card Issuance Fabric), the credit facility (Revolving Credit Fabric), or fraud detection models (Issuer Fraud and Risk Fabric), but consumes inputs from and provides outputs to each.

---

## Source of Truth

- **Entities owned:** Authorization Request, Authorization Response, Authorization Hold, Clearing Record, Settlement Batch, Transaction Posting, Reversal, Stand-In Decision
- **Key invariants:**
  - Every authorization request receives a response within network-mandated timeframes (typically <2 seconds)
  - Authorization holds decrement available balance/credit atomically and are released on clearing or expiry
  - Cleared transactions post to the account exactly once — duplicate presentments are detected and rejected
  - Settlement positions reconcile to clearing records within tolerance — breaks trigger exception workflows
  - Stand-in processing (when the issuer is unavailable) follows pre-configured rules and is reconciled post-event
- **Configurable vs. compliance floor:**
  - *Configurable:* Authorization rules (partial approval, decline thresholds), hold expiry periods, MCC-based rules, velocity limits, stand-in parameters, interchange optimization
  - *Compliance floor:* Network operating regulations compliance; Regulation E (debit) and Regulation Z (credit) protections; real-time fraud rule execution; accurate settlement with networks; audit trail for every authorization decision

---

## Scope Highlights

- Authorization processing — receiving ISO 8583 messages, evaluating decision criteria, responding with approval/decline/referral
- Hold management — creating, modifying, and releasing authorization holds as transactions move through lifecycle
- Clearing processing — matching presentments to authorizations, handling adjustments and chargebacks, preparing for posting
- Settlement — calculating net positions with networks, funding/receiving settlement, reconciling to cleared transactions
- Reversal and void handling — processing merchant-initiated reversals, timeout reversals, and their account impacts
- Stand-in and fallback — making decisions when primary systems are unavailable, with reconciliation on recovery

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Authorization Engine
2. Hold Management
3. Clearing and Matching
4. Settlement Processing
5. Reversal and Adjustment Handling
6. Stand-In Processing
7. Network Connectivity (ISO 8583, ISO 20022)
8. Interchange Management

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Card Issuance Fabric | Card Issuance provides card status; Transaction Processing uses it for authorization decisions |
| Revolving Credit Fabric | For credit cards, Revolving Credit owns the facility and billing; Transaction Processing posts transactions and manages holds against available credit |
| Demand Deposit Fabric | For debit cards, Demand Deposit owns the account; Transaction Processing posts transactions and manages holds against available balance |
| Issuer Tokenization Fabric | Tokenization provides token-to-PAN resolution; Transaction Processing uses it for tokenized transactions |
| Card Authentication Fabric | Authentication handles 3DS challenges; Transaction Processing receives authentication results for authorization |
| Issuer Fraud and Risk Fabric | Fraud Fabric provides real-time risk scores; Transaction Processing incorporates them in authorization decisions |
| Issuer Disputes Fabric | Transaction Processing provides transaction data; Disputes Fabric handles chargebacks and representments |
| Accounting Fabric | Transaction Processing provides cleared transactions; Accounting posts to GL and manages network settlement accounts |

---

## References

_To be added._
