# Chapter 03.02.31: Regulatory Compliance Fabric — Product Note

**The system of record for regulatory reporting and filings — owning call reports, HMDA, CRA, and other mandated regulatory submissions distinct from tax filings and internal audit.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Regulatory Compliance Fabric is the authoritative system for external regulatory reporting: generating and filing periodic regulatory reports (Call Reports, FR Y-9C, HMDA LAR, CRA data), managing filing calendars, tracking submission status, and maintaining audit trails for examiner review. It governs the bank's reporting obligations to prudential regulators (Fed, OCC, FDIC), fair lending regulators, and equivalent authorities in other jurisdictions.

Out of scope: tax filings (Taxation Fabric), internal policy compliance and audit trails (Internal Audit Fabric), AML/BSA transaction monitoring (handled by respective fraud/risk fabrics), and credit bureau reporting (Credit Bureau Fabric). This fabric focuses on regulatory filings to bank supervisors, not tax authorities or credit bureaus.

---

## Source of Truth

- **Entities owned:** Regulatory filing record, filing calendar, Call Report data set, HMDA LAR record, CRA data record, filing submission record, examiner request, attestation record, regulatory amendment, data quality exception
- **Key invariants:** Filed reports are immutable once submitted (amendments filed separately); filing deadlines are enforced with escalation; data aggregations trace to source systems with audit linkage; attestations are captured from authorized officers; every filing has a complete audit trail from data extraction through submission confirmation
- **Configurable vs. compliance floor:** Filing thresholds (small bank exemptions), report format preferences where options exist, and internal review workflows are configurable. Compliance floor: mandatory filing schedules (Call Report quarterly, HMDA annually), data accuracy requirements per regulatory instructions, and officer attestation requirements

---

## Scope Highlights

- Call Report generation: Schedule RC/RI data aggregation, validation, and FFIEC filing
- HMDA reporting: Loan Application Register compilation, geocoding, rate spread calculation, and submission
- CRA data collection: small business lending, community development data, and assessment area reporting
- Filing calendar management: tracking deadlines, triggering workflows, and escalating approaching due dates
- Examiner support: responding to data requests, providing supporting documentation, and tracking exam findings

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Call Report and Financial Statement Filing
2. HMDA Data Collection and Submission
3. CRA Data Reporting
4. Filing Calendar and Deadline Management
5. Data Quality and Validation
6. Examiner Request Management

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Accounting Fabric | Accounting provides GL balances; Regulatory Fabric aggregates for Call Report schedules |
| Taxation Fabric | Taxation handles tax filings; Regulatory Fabric handles prudential/fair lending filings |
| Internal Audit Fabric | Audit Fabric handles internal compliance; Regulatory Fabric handles external regulatory submissions |
| Underwriting Fabric | Underwriting provides loan decision data; Regulatory Fabric reports for HMDA |
| Term Loans Fabric | Loan Fabric provides origination data; Regulatory Fabric reports for CRA/HMDA |
| Credit Bureau Fabric | Bureau Fabric handles credit reporting; Regulatory Fabric handles bank regulator filings |

---

## References

_To be added._
