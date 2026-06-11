# Chapter 03.02.15: Transfers Fabric — Product Note

**The system of record for funds movement between accounts — orchestrating internal transfers, ACH, wire transfers, and real-time payment rails while enforcing limits, cutoff times, and regulatory holds.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Transfers Fabric owns the initiation, validation, routing, and settlement of money movement that originates from or terminates at a bank account. This includes internal book transfers (account-to-account within the bank), external ACH transfers (credits and debits), domestic and international wire transfers (Fedwire, CHIPS, SWIFT), and real-time payments (RTP, FedNow, IMPS). The fabric governs transfer initiation, limit enforcement, cutoff time management, routing decisions, exception handling, and status tracking through completion or rejection. It does not own the accounts themselves (Demand Deposit or Term Deposit Fabrics), card-based payments (Card Issuer Transaction Processing), or bill payments (Bill Payments Fabric).

---

## Source of Truth

- **Entities owned:** Transfer Order, Transfer Status, Routing Instruction, Cutoff Schedule, Transfer Limit Profile, Recurring Transfer, Beneficiary Record, Transfer Exception
- **Key invariants:**
  - A transfer order has exactly one authoritative status at any time (pending, processing, completed, failed, returned, reversed)
  - Available balance checks occur atomically at initiation — insufficient funds reject the transfer, not create an overdraft (unless product allows)
  - Cutoff times are enforced per rail — a wire submitted after cutoff is queued for next business day, not silently delayed
  - International transfers include required regulatory data (purpose codes, originator/beneficiary details) — incomplete data blocks submission
  - Return and reversal handling maintains account integrity — returned ACH credits are debited atomically
- **Configurable vs. compliance floor:**
  - *Configurable:* Per-customer and per-product transfer limits, cutoff time buffers, ACH batch windows, preferred routing for multi-rail scenarios, fee structures, hold periods for new payees
  - *Compliance floor:* OFAC/sanctions screening before release; Regulation E protections for consumer ACH; BSA/AML thresholds for wire reporting; real-time payment irrevocability per network rules; audit trail for every transfer decision

---

## Scope Highlights

- Transfer initiation and validation — capturing originator intent, validating beneficiary details, checking limits and balances
- Multi-rail routing — selecting optimal rail (internal, ACH, wire, RTP) based on speed, cost, and destination reachability
- Cutoff time and scheduling — managing same-day vs. next-day processing, weekend/holiday calendars, and scheduling for recurring transfers
- Limit enforcement — daily, per-transaction, and velocity limits with real-time decrement and reset
- Exception and return handling — processing ACH returns, wire rejects, RTP timeouts, and their account-level impacts
- Beneficiary management — storing, validating, and fraud-screening recurring transfer recipients

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Transfer Initiation and Validation
2. Multi-Rail Routing Engine
3. Cutoff and Schedule Management
4. Limit Enforcement
5. ACH Processing (Origination and Receipt)
6. Wire Processing (Domestic and International)
7. Real-Time Payments (RTP, FedNow)
8. Return and Exception Handling
9. Beneficiary Registry

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Demand Deposit Fabric | Transfers Fabric initiates debits/credits; Demand Deposit owns account balances and executes the posting |
| Line and Limits Fabric | Line and Limits may define transfer limits at customer or product level; Transfers Fabric enforces them per transaction |
| Accounting Fabric | Transfers Fabric provides settlement events; Accounting Fabric posts to GL and manages nostro/vostro reconciliation |
| Issuer Fraud and Risk Fabric | Fraud Fabric provides risk scores and alerts; Transfers Fabric may hold or block transfers based on fraud signals |
| Bill Payments Fabric | Bill Payments uses Transfers Fabric as a rail for biller payments; the two fabrics are distinct in initiation model |
| Regulatory Compliance Fabric | Transfers Fabric provides transaction data; Compliance Fabric handles CTR/SAR filing and OFAC reporting |

---

## References

_To be added._
