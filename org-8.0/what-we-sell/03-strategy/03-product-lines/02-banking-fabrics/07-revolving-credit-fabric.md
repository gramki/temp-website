# Chapter 03.02.07: Revolving Credit Fabric — Product Note

**The authoritative system of record for revolving credit products — credit cards and lines of credit — owning balances, utilization, billing cycles, minimum payments, and the continuous lifecycle of reusable credit.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Revolving Credit Fabric owns credit card accounts and lines of credit — products where the customer has an approved credit limit, can draw against it repeatedly, repay, and draw again. Unlike term loans with fixed amortization, revolving credit has continuous utilization, variable balances, and recurring billing cycles.

In scope: credit account state (balance, available credit, utilization), transaction posting to credit accounts, billing cycle management, statement generation triggers, minimum payment calculation, payment allocation, interest calculation on carried balances, fee assessment, promotional and deferred interest programs. Out of scope: the credit line approval (Underwriting Fabric), the credit limit itself (Line and Limits Fabric), card issuance and plastics (Card Issuance Fabric), and transaction authorization (Card Issuer Transaction Processing Fabric).

---

## Source of Truth

- **Entities owned:** Revolving credit accounts (credit cards, HELOCs, personal lines of credit), current balances (purchase, cash, balance transfer, fees, interest), utilization state, billing cycles, statements, minimum payment amounts, payment history, promotional balance segments
- **Key invariants:** Current balance plus available credit equals credit limit (at any point in time). Minimum payment is calculated per regulatory and product rules. Payments are allocated per defined hierarchy (regulatory requirements first, then product rules). Interest accrues only on balances carried past the grace period.
- **Configurable vs. compliance floor:** Interest rates, billing cycle dates, minimum payment formulas, payment allocation priorities (within regulatory bounds), grace periods, and promotional terms are configurable. CARD Act payment allocation rules (US), regulatory minimum payment requirements, and interest calculation accuracy are the compliance floor.

---

## Scope Highlights

- Maintains revolving credit account balances across multiple balance types (purchases, cash advances, balance transfers, fees, interest)
- Processes transactions posted from authorization systems, updating balances and available credit
- Manages billing cycles: cycle cut, statement generation trigger, payment due date calculation
- Calculates minimum payment based on regulatory rules and product configuration
- Applies payments according to regulatory-compliant allocation hierarchy
- Computes interest on carried balances with support for variable rates and promotional segments

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Account Management** — Account creation, account types (card, HELOC, personal LOC), account attributes, account lifecycle
2. **Balance Management** — Multi-segment balances, balance posting, available credit calculation, utilization tracking
3. **Billing Cycle Engine** — Cycle configuration, statement cut processing, due date calculation, cycle-over-cycle tracking
4. **Payment Processing** — Payment receipt, allocation hierarchy, regulatory allocation rules, overpayment handling
5. **Interest Calculation** — APR application, grace period logic, promotional rates, deferred interest, interest posting
6. **Fee Assessment** — Annual fees, late fees, overlimit fees, cash advance fees, fee waiver processing

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Line and Limits Fabric | Credit limits are maintained in Line and Limits; Revolving Credit tracks utilization and available credit |
| Underwriting Fabric | Credit approvals and limit decisions come from Underwriting; Revolving Credit operates within approved limits |
| Card Issuance Fabric | Card plastics and virtual cards are managed by Card Issuance; Revolving Credit owns the underlying credit account |
| Card Issuer Transaction Processing Fabric | Authorizations are processed there; settled transactions are posted to Revolving Credit |
| Accounting Fabric | Revolving Credit triggers accounting entries for balances, interest income, and fee income |
| Customer Record Fabric | Credit accounts are linked to customers; Customer Record owns the customer identity |
| Collections Fabric | Delinquent accounts are handed to Collections; Revolving Credit tracks payment status |
| Statement Fabric | Statement Fabric generates and delivers statements; Revolving Credit provides statement data |
| Issuer Disputes Fabric | Disputes on credit card transactions flow through Disputes; balance adjustments come back to Revolving Credit |

---

## References

_To be added._
