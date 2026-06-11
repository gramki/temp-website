# Chapter 03.02.35: Sourcing Fabric — Product Note

**The system of record for customer acquisition and application intake — owning lead management, application processing, channel attribution, and the origination funnel that feeds product onboarding.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Sourcing Fabric is the authoritative system for customer acquisition and origination: capturing leads from marketing channels, managing applications through intake and initial verification, attributing conversions to channels/campaigns, and routing qualified applications to product-specific onboarding. It governs the top of the customer funnel — the systems that capture interest and convert it to applications, distinct from the underwriting decisions or account creation that follow.

Out of scope: credit decisioning (Underwriting Fabric), account opening and product setup (Product Fabric), customer identity verification (Trust Fabric), and marketing campaign execution (external marketing systems). This fabric manages the lead-to-application journey, not the credit decision or account activation.

---

## Source of Truth

- **Entities owned:** Lead record, application record (pre-decision), channel source, campaign attribution, referral record, application status, document collection request, pre-qualification result, abandonment record, conversion event
- **Key invariants:** Every application traces to a source channel with attribution preserved; lead deduplication prevents double-counting; application status reflects actual processing state; pre-qualification results are advisory only (not credit decisions); document requests track completion status; abandonment points are captured for funnel analysis
- **Configurable vs. compliance floor:** Channel definitions, attribution models (first-touch, last-touch, multi-touch), application workflows, and document requirements are configurable per product and channel. Compliance floor: TCPA consent for marketing contacts, fair lending requirements for application acceptance, adverse action notices for declined pre-qualifications, and data retention limits for abandoned applications

---

## Scope Highlights

- Lead capture: ingesting leads from digital channels, branches, partners, and marketing campaigns
- Application intake: collecting application data, document requests, and initial verification
- Channel attribution: tracking source, campaign, and referral data through conversion
- Pre-qualification: soft-pull eligibility checks before full application (advisory, not decisioning)
- Funnel analytics: conversion rates, abandonment analysis, and channel performance

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Lead Capture and Management
2. Application Intake and Processing
3. Channel and Campaign Attribution
4. Pre-Qualification and Eligibility
5. Document Collection
6. Funnel Analytics and Reporting

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Underwriting Fabric | Underwriting receives applications for credit decision; Sourcing Fabric manages pre-decision intake |
| Product Fabric | Product Fabric handles account creation; Sourcing Fabric routes approved applications for onboarding |
| Trust Fabric | Trust Fabric handles identity verification; Sourcing Fabric captures initial identity data |
| Customer Record Fabric | Customer Fabric is authoritative for customer data; Sourcing Fabric creates initial records that migrate on approval |
| Credit Bureau Fabric | Bureau Fabric provides soft-pull reports; Sourcing Fabric uses them for pre-qualification |
| BaaS Fabric | BaaS Fabric governs partner programs; Sourcing Fabric may capture partner-sourced applications |

---

## References

_To be added._
