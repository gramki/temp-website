# Chapter 03.02.04: Line and Limits Fabric — Product Note

**The authoritative system of record for credit lines, transaction limits, and velocity controls — the fabric that answers "how much is this customer permitted to do?" across all products and channels.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Line and Limits Fabric owns credit lines and all forms of limits that constrain customer behavior — transaction limits, daily limits, velocity limits, channel limits, and their inheritance relationships. When any system needs to check "can this customer do this much?", it queries this fabric.

In scope: credit lines (approved limits), transaction limits (per-transaction caps), periodic limits (daily, weekly, monthly), velocity limits (frequency constraints), channel-specific limits, limit inheritance (customer-level flowing to account-level), temporary limit changes, limit utilization tracking. Out of scope: the credit decision that established the line (Underwriting Fabric), the transactions that consume limits (domain fabrics), and fraud-based transaction blocking (Issuer Fraud and Risk Fabric).

---

## Source of Truth

- **Entities owned:** Credit lines, transaction limits, velocity limits, limit groups, limit hierarchies, temporary limit adjustments, limit utilization records, limit exception approvals
- **Key invariants:** Utilization cannot exceed the approved limit without explicit exception. Limit changes are effective-dated and audited. Temporary limits expire automatically. Limit inheritance follows defined hierarchy — account limits cannot exceed customer limits unless explicitly overridden.
- **Configurable vs. compliance floor:** Limit amounts, limit types, inheritance rules, and temporary adjustment policies are configurable per product and customer segment. Utilization integrity (accurate tracking), limit enforcement (no silent breaches), and audit completeness are the compliance floor.

---

## Scope Highlights

- Maintains credit lines with approved limits, current utilization, and available credit
- Defines transaction limits: per-transaction caps by amount, transaction type, channel, merchant category
- Enforces velocity limits: transaction count or amount over rolling time windows (hourly, daily, weekly)
- Supports limit inheritance: customer-level limits that flow to accounts, with account-level overrides where permitted
- Manages temporary limit changes: promotional increases, emergency limits, scheduled expirations
- Tracks real-time utilization for immediate limit enforcement

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Credit Line Management** — Line creation, limit amounts, utilization tracking, available credit calculation
2. **Transaction Limits** — Per-transaction caps, limit types, channel-specific limits, merchant category limits
3. **Velocity Controls** — Frequency limits, rolling window calculations, count and amount-based velocity
4. **Limit Hierarchy** — Customer-to-account inheritance, limit groups, override rules, hierarchy resolution
5. **Temporary Adjustments** — Promotional limits, emergency increases, scheduled expiration, adjustment audit
6. **Utilization Engine** — Real-time utilization tracking, limit check API, reservation and release

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Underwriting Fabric | Underwriting approves credit lines and limit amounts; Line and Limits Fabric stores and enforces them |
| Revolving Credit Fabric | Credit card and LOC transactions consume credit lines; Revolving Credit triggers utilization updates in Line and Limits |
| Demand Deposit Fabric | Transaction limits on deposit accounts are enforced; Line and Limits provides limits, Demand Deposit processes transactions |
| Card Issuer Transaction Processing Fabric | Authorization checks query Line and Limits for available credit and transaction limits |
| Transfers Fabric | Transfer limits (daily ACH, wire limits) are maintained here; Transfers Fabric queries before processing |
| Issuer Fraud and Risk Fabric | Fraud Fabric may trigger emergency limit reductions; Line and Limits is authoritative for the limit state |
| Customer Record Fabric | Limits are associated with customers; Customer Record provides the customer identity |

---

## References

_To be added._
