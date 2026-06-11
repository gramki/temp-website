# Chapter 03.02.09: Mortgage Fabric — Product Note

**The authoritative system of record for secured term loans — mortgages, home equity loans, and other collateral-backed lending — owning principal, collateral, escrow, lien position, and the extended lifecycle through payoff or foreclosure.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Mortgage Fabric owns secured term loans where real property serves as collateral — primarily residential and commercial mortgages, but also home equity loans (HELOCs with term loan structure). The collateral relationship, escrow obligations, and lien management distinguish these from unsecured term loans.

In scope: mortgage loan booking and disbursement, collateral linkage and valuation tracking, lien position management, escrow account management (taxes, insurance), payment processing with escrow allocation, interest accrual, prepayment and payoff processing, loan modification, subordination processing, release of lien. Out of scope: unsecured term loans (Term Loans Fabric), the credit decision (Underwriting Fabric), property appraisal (external service), title insurance (external service), and collections/foreclosure proceedings (Collections Fabric).

---

## Source of Truth

- **Entities owned:** Mortgage loan accounts, collateral records, lien positions, escrow accounts, escrow disbursement records, amortization schedules, payment records, payoff records, subordination records, lien release records
- **Key invariants:** Every mortgage has linked collateral with recorded lien position. Escrow balance reflects contributions minus disbursements. Lien position cannot be subordinated without explicit authorization and re-recording. Payoff releases lien only after funds are confirmed.
- **Configurable vs. compliance floor:** Interest rates, escrow requirements, prepayment terms, and modification programs are configurable. RESPA escrow rules (US), lien recording requirements, payoff statement accuracy, and fair servicing requirements are the compliance floor.

---

## Scope Highlights

- Books mortgage loans with principal, rate, term, collateral linkage, and lien position
- Manages collateral: property identification, initial valuation, periodic revaluation triggers, LTV tracking
- Maintains escrow accounts: property tax collection, insurance premium collection, escrow analysis, shortage/surplus handling
- Processes payments with allocation to principal, interest, escrow, and fees
- Handles prepayment and payoff: payoff quote generation, partial prepayment, satisfaction and lien release
- Supports loan modifications: rate modifications, term extensions, principal forbearance, loss mitigation programs

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Loan Booking** — Mortgage creation, disbursement, closing document data capture, first payment date setting
2. **Collateral Management** — Property linkage, valuation tracking, LTV monitoring, collateral release conditions
3. **Lien Management** — Lien position recording, subordination processing, satisfaction recording, lien release
4. **Escrow Management** — Escrow account setup, contribution calculation, disbursement processing, annual analysis
5. **Payment Processing** — Payment receipt, allocation (PITI), late fee assessment, partial payment handling
6. **Payoff and Release** — Payoff quote generation, payoff processing, satisfaction preparation, lien release

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Term Loans Fabric | Term Loans handles unsecured term loans; Mortgage Fabric handles secured loans with collateral |
| Underwriting Fabric | Mortgage approvals come from Underwriting; Mortgage Fabric books approved loans |
| Revolving Credit Fabric | HELOCs (revolving) are in Revolving Credit; home equity term loans may be in Mortgage Fabric |
| Accounting Fabric | Mortgage Fabric triggers accounting entries for disbursement, interest, escrow, and payments |
| Customer Record Fabric | Mortgages are linked to borrowers; Customer Record owns the customer identity |
| Collections Fabric | Delinquent mortgages enter Collections; foreclosure proceedings are managed there |
| Statement Fabric | Statement Fabric generates mortgage statements; Mortgage Fabric provides payment and escrow data |
| Regulatory Compliance Fabric | HMDA reporting data originates from mortgage origination and servicing |
| Taxation Fabric | Mortgage interest and property tax data feed tax reporting |

---

## References

_To be added._
