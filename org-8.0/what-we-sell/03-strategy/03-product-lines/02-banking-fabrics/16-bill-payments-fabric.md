# Chapter 03.02.16: Bill Payments Fabric — Product Note

**The system of record for consumer and business bill payment — managing biller directories, payment scheduling, confirmation, remittance delivery, and exception handling for utility, loan, and general biller payments.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Bill Payments Fabric owns the bill payment experience from the payer's bank perspective. This includes biller discovery and enrollment, payment scheduling (one-time and recurring), payment execution across available rails (ACH, check, real-time, card), confirmation and remittance delivery, and exception handling when payments fail or are returned. The fabric maintains the biller directory (direct billers, aggregator-reachable billers, check-payable billers) and manages the customer's enrolled billers and payment history. It does not own the funds transfer mechanics (Transfers Fabric), the underlying account (Demand Deposit Fabric), or the biller's receivables system.

---

## Source of Truth

- **Entities owned:** Biller, Biller Directory Entry, Customer-Biller Enrollment, Bill Payment Order, Payment Schedule (Recurring), Payment Confirmation, Payment Exception, Remittance Record
- **Key invariants:**
  - Every payment has a traceable biller identifier and customer account reference — ambiguous payments are rejected at initiation
  - Scheduled payments execute on the scheduled date (or next business day) — silent skips are prohibited
  - Payment confirmations include a reference number usable for dispute resolution with the biller
  - Recurring payments respect customer-specified end dates and maximum payment limits
  - Failed payments generate timely customer notifications with clear exception reasons
- **Configurable vs. compliance floor:**
  - *Configurable:* Supported billers, payment lead times, recurring payment rules, early-pay discounts, payment method preferences, notification channels
  - *Compliance floor:* Regulation E consumer protections for electronic payments; timely notification of failed payments; accurate remittance data to billers per NACHA and network rules; audit trail for payment lifecycle

---

## Scope Highlights

- Biller directory management — aggregating billers from bill pay networks, maintaining direct biller connections, and handling check-payable billers
- Customer biller enrollment — capturing account numbers, validating biller reachability, storing biller nicknames
- Payment scheduling — same-day, future-dated, and recurring payment setup with calendar and limit awareness
- Payment routing — selecting optimal rail (electronic direct, electronic aggregator, expedited, check) based on biller capability and customer preference
- Confirmation and remittance — providing payment confirmation to customers and remittance data to billers
- Exception handling — processing returned payments, notifying customers, and managing re-presentment or alternative payment methods

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Biller Directory Management
2. Customer Biller Enrollment
3. Payment Scheduling Engine
4. Payment Routing and Execution
5. Confirmation and Notification
6. Remittance Delivery
7. Exception and Return Handling
8. Recurring Payment Management

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Transfers Fabric | Bill Payments uses Transfers Fabric as the execution rail for ACH and wire payments; Bill Payments owns the biller context |
| Demand Deposit Fabric | Bill Payments initiates debits; Demand Deposit owns the account and balance |
| Statement Fabric | Bill Payments provides payment history; Statement Fabric includes it in customer statements |
| Issuer Fraud and Risk Fabric | Fraud Fabric may flag suspicious biller enrollments or high-risk payments; Bill Payments consumes risk signals |
| Card Issuer Transaction Processing Fabric | For card-funded bill payments, Transaction Processing handles the card payment; Bill Payments provides the biller context |

---

## References

_To be added._
