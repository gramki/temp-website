# Chapter 03.02.05: Demand Deposit Fabric — Product Note

**The authoritative system of record for demand deposit accounts — checking, savings, and money market — owning balances, holds, transactions, and interest accrual for accounts where funds are available on demand.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Demand Deposit Fabric owns demand deposit accounts and their state — account balances, posted transactions, pending transactions, holds, and interest accrual for checking, savings, and money market accounts. These are accounts where the customer can access funds on demand, distinguishing them from term deposits with fixed maturity.

In scope: account creation and lifecycle, balance management (ledger balance, available balance, memo-posted), transaction posting, hold management, interest accrual and posting, overdraft state, dormancy tracking. Out of scope: term deposits with maturity dates (Term Deposit Fabric), the payment rails that move funds (Transfers Fabric), card transactions (Card Issuer Transaction Processing Fabric), and product definitions (Product Fabric).

---

## Source of Truth

- **Entities owned:** Demand deposit accounts (checking, savings, money market), account balances, posted transactions, memo-posted transactions, holds (administrative, legal, regulatory), interest accrual records, overdraft positions, account lifecycle states
- **Key invariants:** Available balance is always ledger balance minus holds minus pending debits. Transactions are immutable once posted — corrections require offsetting entries. Interest accrual follows the account's configured method and is posted per schedule. Accounts cannot be closed with non-zero balances or pending holds.
- **Configurable vs. compliance floor:** Interest rates, accrual methods, hold policies, dormancy thresholds, and overdraft parameters are configurable per product and jurisdiction. Balance integrity, transaction immutability, hold enforcement, and regulatory reporting completeness are the compliance floor.

---

## Scope Highlights

- Maintains demand deposit accounts with full balance state (ledger, available, memo-posted)
- Processes deposits, withdrawals, and internal transfers with real-time balance updates
- Manages holds: pending transaction holds, administrative holds, legal/garnishment holds, regulatory holds
- Calculates and posts interest based on configured accrual methods (daily, monthly, tiered)
- Tracks overdraft state: overdraft occurrence, linked overdraft protection, overdraft fees
- Manages account lifecycle: opening, active use, dormancy, escheatment preparation, closure

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Account Management** — Account creation, account types (checking, savings, money market), account lifecycle, account attributes
2. **Balance Engine** — Ledger balance, available balance, memo-posting, real-time balance computation
3. **Transaction Processing** — Debits, credits, posting, transaction categorization, statement preparation
4. **Hold Management** — Pending holds, administrative holds, legal holds, hold priorities, automatic release
5. **Interest Accrual** — Rate configuration, accrual methods (daily balance, average balance, tiered), interest posting
6. **Dormancy and Escheatment** — Inactivity tracking, dormancy fees, escheatment preparation, state reporting

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Accounting Fabric | Demand Deposit triggers accounting entries for all balance-affecting transactions; Accounting Fabric records the ledger impact |
| Product Fabric | Deposit account configurations (rates, fees, features) are defined in Product Fabric; Demand Deposit Fabric instantiates accounts |
| Customer Record Fabric | Accounts are linked to customers; Customer Record owns the customer, Demand Deposit owns the account |
| Transfers Fabric | Transfers Fabric orchestrates fund movements; Demand Deposit Fabric posts the debits and credits to accounts |
| Line and Limits Fabric | Transaction limits for deposit accounts are maintained in Line and Limits; Demand Deposit queries before posting |
| Term Deposit Fabric | Matured term deposits may roll into demand deposits; Term Deposit initiates, Demand Deposit receives |
| Statement Fabric | Statement Fabric generates account statements; Demand Deposit provides transaction and balance data |
| Collections Fabric | Overdrawn accounts may enter collections; Demand Deposit tracks overdraft, Collections manages recovery |

---

## References

_To be added._
