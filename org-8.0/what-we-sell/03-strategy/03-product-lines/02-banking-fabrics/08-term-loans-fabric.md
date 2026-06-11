# Chapter 03.02.08: Term Loans Fabric — Product Note

**The authoritative system of record for unsecured term loans — personal loans, auto loans (unsecured), and other amortizing credit products — owning principal, amortization schedules, disbursement, and repayment through payoff.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Term Loans Fabric owns unsecured term loans — credit products with a fixed principal, defined repayment schedule, and finite term. Unlike revolving credit, term loans have a disbursement event, a fixed amortization schedule, and a target payoff date.

In scope: loan booking and disbursement, principal and interest tracking, amortization schedule management, payment processing and application, prepayment handling, late payment tracking, interest accrual methods, loan modification (rate changes, term extensions), payoff calculation and processing. Out of scope: secured loans with collateral (Mortgage Fabric), the credit decision (Underwriting Fabric), collections on defaulted loans (Collections Fabric), and loan product definitions (Product Fabric).

---

## Source of Truth

- **Entities owned:** Term loan accounts, disbursement records, amortization schedules, payment records, principal balances, accrued interest, prepayment records, loan modification records, payoff quotes
- **Key invariants:** Principal balance reflects disbursement minus payments applied to principal. Amortization schedule is recalculated on any prepayment or modification. Payments are applied per defined allocation (interest first, then principal, unless otherwise specified). Payoff amount includes all accrued interest through the payoff date.
- **Configurable vs. compliance floor:** Interest rates, amortization methods (equal installment, declining balance), prepayment penalties, grace periods, and late fee structures are configurable. Principal accuracy, interest calculation precision, Truth in Lending disclosure compliance, and payoff quote accuracy are the compliance floor.

---

## Scope Highlights

- Books term loans with principal, rate, term, and amortization schedule at disbursement
- Manages disbursement: single disbursement, staged disbursement, disbursement to external accounts
- Maintains amortization schedules with principal and interest components per payment
- Processes loan payments with proper allocation to interest, principal, fees, and escrow (if applicable)
- Handles prepayment: full prepayment (payoff), partial prepayment, prepayment penalty calculation, schedule recalculation
- Supports loan modifications: rate changes, term extensions, forbearance, payment deferral

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Loan Booking** — Loan creation, disbursement processing, initial schedule generation, first payment date setting
2. **Amortization Engine** — Schedule calculation (equal installment, declining balance), recalculation on events, schedule versioning
3. **Payment Processing** — Payment receipt, allocation rules, due date tracking, grace period handling
4. **Prepayment Management** — Payoff quote generation, partial prepayment, penalty calculation, schedule adjustment
5. **Loan Servicing** — Interest accrual, escrow management (where applicable), late fee assessment, statement data
6. **Loan Modification** — Rate change processing, term extension, forbearance, deferral, modification audit

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Underwriting Fabric | Loan approvals come from Underwriting; Term Loans books approved loans |
| Line and Limits Fabric | Approved loan amounts may be tracked as committed lines; Term Loans tracks the actual loan position |
| Product Fabric | Loan product configurations (rates, terms, fees) are defined in Product Fabric |
| Accounting Fabric | Term Loans triggers accounting entries for disbursement, interest accrual, and payments received |
| Customer Record Fabric | Loans are linked to customers; Customer Record owns the customer identity |
| Collections Fabric | Delinquent loans are handed to Collections; Term Loans tracks payment status |
| Demand Deposit Fabric | Loan disbursements and payments often flow through deposit accounts |
| Statement Fabric | Statement Fabric generates loan statements; Term Loans provides payment and balance data |
| Mortgage Fabric | Mortgage Fabric handles secured term loans; Term Loans handles unsecured |

---

## References

_To be added._
