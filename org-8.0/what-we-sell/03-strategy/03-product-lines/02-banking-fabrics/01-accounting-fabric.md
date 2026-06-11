# Chapter 03.02.01: Accounting Fabric — Product Note

**The authoritative system of record for all financial positions, movements, and accounting entries — the general ledger and sub-ledgers that form the bedrock of financial integrity.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Accounting Fabric owns the financial books of the institution — the general ledger, sub-ledgers, and all accounting entries that record financial positions and movements. Every transaction that affects the bank's financial statements flows through this fabric: deposits credited, loans disbursed, fees charged, interest accrued, provisions booked.

In scope: chart of accounts, account balances, journal entries, posting rules, sub-ledger management, period close, reconciliation infrastructure. Out of scope: the business events that trigger entries (handled by domain fabrics like Demand Deposit or Revolving Credit), regulatory reporting formats (Regulatory Compliance Fabric), and tax computation (Taxation Fabric).

---

## Source of Truth

- **Entities owned:** General ledger accounts, sub-ledger accounts, journal entries, accounting periods, chart of accounts, posting rules, balance snapshots
- **Key invariants:** Debits always equal credits for every entry and every account. Account balances reflect the sum of all posted entries. Entries are immutable once posted — corrections require reversing entries. Period close locks the books.
- **Configurable vs. compliance floor:** Chart of accounts structure, posting rules, sub-ledger hierarchies, and period close schedules are configurable per institution. Double-entry integrity, entry immutability, audit completeness, and balance accuracy are the non-negotiable compliance floor.

---

## Scope Highlights

- Maintains the general ledger with real-time and batch posting capabilities
- Manages sub-ledgers for detailed tracking (customer accounts, loan accounts, suspense) that roll up to GL accounts
- Enforces double-entry accounting discipline across all posting systems
- Provides balance inquiry at any point in time — current, period-end, or historical
- Supports multi-currency accounting with revaluation and translation
- Enables period close with pre-close validation, lock, and post-close adjustment windows

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Ledger Management** — Chart of accounts, account lifecycle, hierarchies, GL/sub-ledger relationships
2. **Entry Processing** — Journal entry creation, validation, posting, reversal, batch processing
3. **Balance Management** — Real-time balance computation, period snapshots, reconciliation checkpoints
4. **Period Close** — Close calendar, pre-close validation, lock enforcement, post-close adjustments
5. **Multi-Currency** — Currency accounts, revaluation rules, translation, gain/loss booking
6. **Reconciliation Infrastructure** — Inter-system reconciliation hooks, break identification, suspense management

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Demand Deposit Fabric | Demand Deposit owns deposit accounts and balances; triggers posting entries to Accounting Fabric for ledger reflection |
| Term Deposit Fabric | Term Deposit owns FD/CD accounts and interest accrual; Accounting Fabric records the entries |
| Revolving Credit Fabric | Revolving Credit owns credit card and LOC balances; Accounting Fabric records corresponding liabilities and income |
| Term Loans Fabric | Term Loans owns loan positions; Accounting Fabric records loan disbursement, repayment, and provision entries |
| Product Fabric | Product definitions include posting rules that Accounting Fabric executes |
| Taxation Fabric | Taxation computes tax obligations; Accounting Fabric records tax-related entries |
| Truth Fabric | Accounting Fabric is authoritative for financial positions; Truth Fabric governs cross-fabric semantic agreement on financial terms |

---

## References

_To be added._
