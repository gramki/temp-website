# Chapter 03.02.18: UPI Issuer Transaction Processing Fabric — Product Note

**The system of record for UPI transaction lifecycle from the issuing bank's perspective — managing payment and collect requests, mandate execution, and NPCI settlement while enforcing account limits, fraud rules, and real-time payment guarantees.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

UPI Issuer Transaction Processing Fabric owns the real-time processing of Unified Payments Interface (UPI) transactions where the bank acts as the issuing (payer's) bank. This includes handling pay requests (customer-initiated push payments), collect requests (payee-initiated pull requests requiring customer approval), mandate registration and execution (recurring payments), and settlement with NPCI. The fabric validates VPA-to-account mappings, enforces transaction limits, executes fraud checks, debits accounts in real time, and manages dispute and callback flows. It does not own the account itself (Demand Deposit Fabric), the VPA registry (may be part of this fabric or separate), or fraud models (Issuer Fraud and Risk Fabric).

---

## Source of Truth

- **Entities owned:** UPI Transaction, Pay Request, Collect Request, Mandate Registration, Mandate Execution, VPA-to-Account Mapping, Transaction Status, Settlement Position, Callback Record
- **Key invariants:**
  - Every UPI transaction completes (success or failure) within NPCI-mandated timeframes (typically <30 seconds end-to-end)
  - Account debits for successful transactions are atomic and irrevocable — funds leave the account exactly once
  - Collect requests require explicit customer authorization before debit — implicit approval is prohibited
  - Mandate executions respect registered amount limits, frequency, and validity period — violations reject the execution
  - Settlement positions reconcile with NPCI within the settlement cycle — breaks trigger exception workflows
- **Configurable vs. compliance floor:**
  - *Configurable:* Per-customer and per-product transaction limits, VPA formats, mandate approval workflows, decline reason messaging, settlement timing preferences
  - *Compliance floor:* NPCI operating circular compliance; real-time fraud screening; customer authentication for collect and mandate approval; accurate settlement with NPCI; RBI-mandated transaction limits; audit trail for every transaction

---

## Scope Highlights

- Pay request processing — receiving PSP-originated requests, validating VPA and account, checking limits, executing debit, responding
- Collect request handling — receiving collect requests, presenting to customer for approval, executing on approval, managing timeouts
- Mandate lifecycle — registration, modification, revocation, and pause/resume of recurring payment authorizations
- Mandate execution — processing scheduled mandate debits with pre-notification, limit validation, and customer override handling
- Settlement — calculating net positions with NPCI, funding/receiving settlement, reconciling to transaction records
- Callback and dispute — handling transaction status inquiries, reversals, and dispute flows per NPCI guidelines

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Pay Request Processing
2. Collect Request Handling
3. Mandate Registration and Management
4. Mandate Execution Engine
5. VPA Management
6. Settlement with NPCI
7. Callback and Reversal Handling
8. NPCI Connectivity and Message Handling

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Demand Deposit Fabric | Demand Deposit owns the account; UPI Transaction Processing debits/credits the account for transactions |
| Issuer Fraud and Risk Fabric | Fraud Fabric provides real-time risk scores; UPI Transaction Processing incorporates them in transaction decisions |
| Transfers Fabric | Both handle fund movement; UPI Transaction Processing is specific to UPI rail, Transfers Fabric handles ACH/wire/RTP |
| Accounting Fabric | UPI Transaction Processing provides transaction and settlement data; Accounting posts to GL |
| Bill Payments Fabric | Bill Payments may use UPI as a payment rail for billers accepting UPI; UPI Transaction Processing executes the payment |

---

## References

_To be added._
