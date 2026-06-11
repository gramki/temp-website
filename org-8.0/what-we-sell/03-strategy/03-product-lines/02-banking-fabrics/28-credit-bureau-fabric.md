# Chapter 03.02.28: Credit Bureau Fabric — Product Note

**The system of record for credit bureau interactions — owning bureau reporting, inquiry management, dispute handling, and the bank's data furnishing obligations to credit reporting agencies.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Credit Bureau Fabric is the authoritative system for all credit bureau interactions: furnishing account data to bureaus (Equifax, Experian, TransUnion, CIBIL, etc.), pulling credit reports for underwriting and account review, managing consumer disputes about reported data, and ensuring compliance with credit reporting regulations. It governs the bank's responsibilities as both a data furnisher and a data user in the credit reporting ecosystem.

Out of scope: credit decisioning logic (Underwriting Fabric), collections activity (Collections Fabric), and customer identity management (Customer Record Fabric). This fabric manages the bureau data exchange layer, not the lending decisions or account servicing that generate the reported data.

---

## Source of Truth

- **Entities owned:** Bureau tradeline (as furnished), credit inquiry record, bureau report (cached), consumer dispute (bureau-related), Metro 2 segment record, furnisher ID, dispute investigation record, correction submission, bureau response, reporting exception
- **Key invariants:** Furnished data reflects account status as of reporting date with no retroactive falsification; disputes are investigated and responded to within regulatory timelines (30 days FCRA, 21 days for expedited); inquiry records are immutable and auditable; corrections propagate to all bureaus where data was furnished; account closure/charge-off status is reported within required windows
- **Configurable vs. compliance floor:** Reporting frequency (monthly, real-time for some bureaus), bureau selection per product type, dispute workflow routing, and soft-pull vs. hard-pull policies are configurable. Compliance floor: FCRA/FACTA accuracy and dispute requirements, Metro 2 format compliance, CIBIL/RBI reporting requirements (India), and adverse action notice obligations

---

## Scope Highlights

- Data furnishing: Metro 2 file generation, tradeline updates, and transmission to bureaus on schedule
- Credit inquiry: hard and soft pulls for underwriting, account review, and prequalification
- Consumer dispute management: intake, investigation, response, and correction submission per FCRA
- Report caching and refresh: storing bureau reports, managing refresh cycles, and version control
- Regulatory compliance: FCRA accuracy requirements, dispute timeline enforcement, and adverse action documentation

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Data Furnishing and Metro 2 Reporting
2. Credit Inquiry Management
3. Consumer Dispute Handling
4. Bureau Connectivity and File Exchange
5. Report Caching and Retrieval
6. Regulatory Compliance and Audit

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Underwriting Fabric | Underwriting consumes bureau reports for decisioning; Bureau Fabric provides the reports |
| Collections Fabric | Collections activity generates status updates; Bureau Fabric reports delinquency and charge-off status |
| Customer Record Fabric | Customer Fabric provides identity data; Bureau Fabric uses it for inquiry matching and dispute resolution |
| Revolving Credit Fabric | Credit Fabric provides account balances and status; Bureau Fabric furnishes this data to bureaus |
| Term Loans Fabric | Loan Fabric provides installment account data; Bureau Fabric furnishes tradeline information |

---

## References

_To be added._
