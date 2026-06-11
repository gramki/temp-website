# Chapter 03.02.06: Term Deposit Fabric — Product Note

**The authoritative system of record for term deposits — certificates of deposit (CDs) and fixed deposits (FDs) — owning principal, maturity, interest schedules, and the lifecycle from booking through maturity or early withdrawal.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Term Deposit Fabric owns term deposit accounts — financial instruments where the customer commits funds for a fixed period in exchange for a guaranteed interest rate. This includes CDs (US), FDs (India and UK), and equivalent instruments globally.

In scope: term deposit booking, principal and maturity tracking, interest rate locking, interest calculation and accrual, interest payout schedules (at maturity, periodic), renewal management (auto-renewal, manual renewal, maturity instructions), early withdrawal processing with penalty calculation, partial withdrawal where permitted. Out of scope: demand deposits (Demand Deposit Fabric), the funding source account (Demand Deposit Fabric), and product definitions (Product Fabric).

---

## Source of Truth

- **Entities owned:** Term deposit accounts, principal amounts, maturity dates, locked interest rates, interest accrual records, payout schedules, maturity instructions, renewal records, early withdrawal records, penalty calculations
- **Key invariants:** Principal is locked until maturity unless early withdrawal is processed with applicable penalty. Interest rate is fixed at booking for the term (unless explicitly variable-rate). Maturity date is immutable once set. Interest accrual follows the locked rate and configured method.
- **Configurable vs. compliance floor:** Interest rates, term lengths, early withdrawal penalties, renewal options, and payout frequencies are configurable per product. Principal integrity, rate lock enforcement, penalty application for early withdrawal, and regulatory disclosure compliance are the compliance floor.

---

## Scope Highlights

- Books term deposits with principal, term, rate, and maturity date locked at inception
- Calculates and accrues interest based on locked rate and configured accrual method
- Supports multiple payout schedules: interest at maturity, monthly/quarterly interest payouts, cumulative compounding
- Manages maturity: maturity instructions (roll over, liquidate to account), auto-renewal with prevailing rates, grace periods
- Processes early withdrawal with penalty calculation, partial withdrawal where product permits
- Handles premature closure scenarios: death, court order, regulatory requirement

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Deposit Booking** — Term deposit creation, principal lock, rate lock, maturity date setting, confirmation generation
2. **Interest Management** — Rate lock, accrual calculation, compounding, payout schedules, interest posting
3. **Maturity Processing** — Maturity date tracking, maturity instructions, auto-renewal logic, grace period handling
4. **Early Withdrawal** — Penalty calculation, partial withdrawal, premature closure, regulatory exceptions
5. **Renewal Management** — Auto-renewal configuration, renewal rate determination, renewal confirmation, opt-out processing
6. **Regulatory Compliance** — TDS/withholding calculation hooks, disclosure generation, reporting data provision

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Demand Deposit Fabric | Term deposits are funded from and mature into demand deposits; Demand Deposit handles the funding account |
| Accounting Fabric | Term Deposit triggers accounting entries for principal, interest accrual, and payout; Accounting Fabric records them |
| Product Fabric | Term deposit product configurations (rates, terms, penalties) are defined in Product Fabric |
| Customer Record Fabric | Term deposits are linked to customers; Customer Record owns the customer identity |
| Taxation Fabric | Interest income is taxable; Taxation Fabric computes withholding, Term Deposit provides interest data |
| Statement Fabric | Statement Fabric generates deposit certificates and interest statements; Term Deposit provides the data |
| Sourcing Fabric | New term deposit applications may come through Sourcing Fabric; Term Deposit books the accepted deposits |

---

## References

_To be added._
