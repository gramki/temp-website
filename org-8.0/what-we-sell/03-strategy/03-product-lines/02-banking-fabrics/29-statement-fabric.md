# Chapter 03.02.29: Statement Fabric — Product Note

**The system of record for statement generation and delivery — owning statement cycles, document rendering, delivery preferences, and archival across all account types.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Statement Fabric is the authoritative system for periodic account statements: cycle definition, statement generation from account data, document rendering (PDF, accessible formats), delivery orchestration (mail, email, in-app), and long-term archival. It governs the statement lifecycle across deposit accounts, credit accounts, loans, and investment accounts — providing a unified statement capability rather than per-product implementations.

Out of scope: transaction posting and balance calculation (respective account fabrics), tax document generation (Taxation Fabric), and regulatory filings (Regulatory Compliance Fabric). This fabric produces customer-facing statements, not internal reports or regulatory submissions.

---

## Source of Truth

- **Entities owned:** Statement cycle definition, statement document, statement delivery record, delivery preference, statement archive record, combined statement configuration, statement template, reprint request, e-statement enrollment
- **Key invariants:** Statement data reflects account state as of cycle cut-off with no retroactive modification; delivery preferences are honored per customer consent; archived statements are immutable and retrievable for regulatory retention periods (7+ years); statement generation completes within SLA of cycle close; e-statement opt-in/opt-out is auditable
- **Configurable vs. compliance floor:** Cycle dates, statement formats, combined statement groupings, delivery channels, and template branding are configurable per product and customer segment. Compliance floor: Regulation E/Z statement content requirements, TILA disclosures, accessibility standards (ADA/WCAG), and retention requirements per jurisdiction

---

## Scope Highlights

- Statement cycle management: defining cycles, triggering generation, and handling cycle exceptions
- Document generation: pulling account data, applying templates, rendering PDFs and accessible formats
- Delivery orchestration: routing to print vendors, email delivery, in-app availability, and delivery confirmation tracking
- Customer preferences: e-statement enrollment, combined statement configuration, and delivery address management
- Archival and retrieval: long-term storage, customer self-service access, and reprint fulfillment

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Statement Cycle Management
2. Document Generation and Rendering
3. Delivery Orchestration
4. Customer Preference Management
5. Archival and Retrieval
6. Combined and Consolidated Statements

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Demand Deposit Fabric | Deposit Fabric provides account/transaction data; Statement Fabric generates deposit statements |
| Revolving Credit Fabric | Credit Fabric provides billing data; Statement Fabric generates credit card statements |
| Term Loans Fabric | Loan Fabric provides amortization data; Statement Fabric generates loan statements |
| Taxation Fabric | Taxation Fabric generates tax documents (1099, TDS); Statement Fabric generates account statements |
| Customer Record Fabric | Customer Fabric provides addresses and preferences; Statement Fabric uses them for delivery |

---

## References

_To be added._
