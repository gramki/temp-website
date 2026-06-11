# Chapter 03.02.34: BaaS Fabric — Product Note

**The system of record for Banking-as-a-Service operations — owning partner program management, API access governance, and the infrastructure that enables non-bank brands to offer banking products.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

BaaS Fabric is the authoritative system for Banking-as-a-Service program operations: partner (fintech/brand) onboarding, API access management, program configuration, usage metering, and the governance layer that enables embedded finance. It governs the bank's role as a BaaS provider — the partner lifecycle, API exposure, and program-level controls that allow third parties to offer banking products under the bank's charter, distinct from the underlying banking capabilities they consume.

Out of scope: the banking capabilities themselves (deposits, cards, payments — handled by respective fabrics), partner customer identity (Trust Fabric with delegation), and regulatory filings (Regulatory Compliance Fabric, though BaaS Fabric provides program data). This fabric manages the partner relationship and API access layer, not the banking products or customer accounts.

---

## Source of Truth

- **Entities owned:** BaaS partner record, partner program, API credential, API rate limit, usage meter, program configuration, partner webhook subscription, sandbox environment, program fee schedule, partner compliance attestation, API version assignment
- **Key invariants:** API credentials are partner-specific and independently revocable; rate limits are enforced in real-time; usage metering is accurate for billing and audit; program configurations cannot violate bank policy or regulatory requirements; sandbox environments are isolated from production; every API call is logged with partner attribution
- **Configurable vs. compliance floor:** API rate limits, feature enablement per partner, program branding, fee structures, and webhook configurations are configurable per partner agreement. Compliance floor: OCC/Fed third-party risk management requirements, partner due diligence documentation, program-level BSA/AML controls, and consumer protection disclosures for embedded finance

---

## Scope Highlights

- Partner lifecycle management: onboarding, due diligence, contracting, go-live, and offboarding
- API access governance: credential issuance, rate limiting, versioning, and deprecation management
- Program configuration: product enablement, limit setting, branding parameters, and fee schedules
- Usage metering and billing: tracking API calls, transaction volumes, and account counts for billing
- Sandbox and testing: isolated environments for partner development and certification

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Partner Onboarding and Due Diligence
2. API Credential and Access Management
3. Program Configuration and Governance
4. Usage Metering and Billing
5. Sandbox and Developer Experience
6. Partner Compliance and Monitoring

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| All Banking Fabrics | Banking Fabrics provide capabilities; BaaS Fabric governs partner access to those capabilities |
| Trust Fabric | Trust Fabric handles identity; BaaS Fabric manages partner-level API authentication and may delegate customer identity |
| Product Fabric | Product Fabric defines products; BaaS Fabric configures which products are available per partner program |
| Regulatory Compliance Fabric | Regulatory Fabric handles filings; BaaS Fabric provides program-level data for third-party risk reporting |
| Customer Record Fabric | Customer Fabric holds customer data; BaaS Fabric governs partner access to customer operations |

---

## References

_To be added._
