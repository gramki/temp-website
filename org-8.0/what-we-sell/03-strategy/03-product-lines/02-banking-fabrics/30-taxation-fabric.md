# Chapter 03.02.30: Taxation Fabric — Product Note

**The system of record for tax withholding and reporting — owning tax calculations, document generation (1099, 1098, TDS certificates), and regulatory tax filings across all taxable banking activities.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Taxation Fabric is the authoritative system for banking-related tax obligations: calculating and applying tax withholding (backup withholding, NRA withholding, TDS), generating customer tax documents (1099-INT, 1099-MISC, 1099-R, 1098, Form 16A/TDS certificates), and filing with tax authorities. It governs the bank's tax reporting and withholding responsibilities across deposits, loans, and payments — ensuring customers receive accurate tax documents and authorities receive required filings.

Out of scope: the bank's own corporate tax obligations, account interest calculation (respective account fabrics), and general regulatory reporting (Regulatory Compliance Fabric). This fabric focuses on customer-facing tax documentation and the withholding/reporting obligations tied to customer accounts.

---

## Source of Truth

- **Entities owned:** Tax withholding record, tax document (1099, 1098, TDS certificate), W-9/W-8 certification, tax identification number validation, withholding exemption, tax filing record, correction/amended filing, tax lot (for investment accounts), cost basis record
- **Key invariants:** Withholding is applied according to current tax rates and customer certification status; tax documents reflect calendar/fiscal year totals with no post-issuance modification (corrections filed separately); TIN validation is completed before account opening for reportable accounts; filing deadlines are met per IRS/tax authority requirements; amended documents are clearly marked and reference originals
- **Configurable vs. compliance floor:** Withholding rate overrides (where legally permitted), document delivery preferences, and filing consolidation are configurable. Compliance floor: IRS 1099/1098 filing requirements and deadlines, backup withholding rules for missing/invalid TINs, NRA withholding under tax treaties, and TDS rates per Income Tax Act (India)

---

## Scope Highlights

- Withholding calculation: backup withholding, NRA withholding, TDS on interest/payments per applicable rates
- Tax document generation: 1099-INT (interest), 1099-MISC (payments), 1098 (mortgage interest), TDS certificates
- Customer certification management: W-9, W-8BEN collection, TIN matching, and recertification workflows
- Regulatory filing: IRS FIRE filing, state filings, TDS returns to tax authorities
- Corrections and amendments: handling errors, issuing corrected documents, and filing amended returns

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Tax Withholding Calculation and Application
2. Tax Document Generation and Delivery
3. Customer Tax Certification (W-9/W-8/TIN)
4. Regulatory Filing and Transmission
5. Corrections and Amendments
6. Tax Lot and Cost Basis Tracking (Investment Accounts)

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Demand Deposit Fabric | Deposit Fabric provides interest paid; Taxation Fabric calculates withholding and generates 1099-INT |
| Term Deposit Fabric | Term Deposit Fabric provides interest/maturity data; Taxation Fabric reports on 1099-INT/TDS |
| Mortgage Fabric | Mortgage Fabric provides interest paid data; Taxation Fabric generates 1098 |
| Statement Fabric | Statement Fabric handles account statements; Taxation Fabric handles tax documents |
| Regulatory Compliance Fabric | Regulatory Fabric handles non-tax regulatory filings; Taxation Fabric handles tax-specific filings |
| Customer Record Fabric | Customer Fabric provides TIN and address; Taxation Fabric uses for document generation and filing |

---

## References

_To be added._
