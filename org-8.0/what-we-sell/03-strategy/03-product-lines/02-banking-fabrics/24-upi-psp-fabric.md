# Chapter 03.02.24: UPI PSP Fabric — Product Note

**The system of record for UPI payment service provider operations — owning VPA lifecycle, mandate management, and merchant/customer UPI transaction orchestration from the PSP perspective.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

UPI PSP Fabric is the authoritative system for UPI PSP-side operations: Virtual Payment Address (VPA) creation and lifecycle, mandate (recurring payment authorization) management, collect/pay request orchestration, and merchant integration for UPI acceptance. It governs the PSP's responsibilities under NPCI's UPI ecosystem — acting as the interface between end-users/merchants and the UPI switch, distinct from the issuing bank's transaction processing.

Out of scope: issuer-side UPI transaction processing (UPI Issuer Transaction Processing Fabric), card-based payment gateway operations (Card PSP Fabric), and inter-bank settlement (handled by NPCI/RBI infrastructure). This fabric owns the PSP layer, not the remitting/beneficiary bank layer.

---

## Source of Truth

- **Entities owned:** VPA (Virtual Payment Address), VPA-to-account mapping, UPI mandate (autopay authorization), mandate revocation record, collect request, PSP merchant, UPI transaction reference (PSP-level), dispute/complaint record (PSP-initiated), device binding record
- **Key invariants:** Each VPA maps to exactly one bank account at any time; mandates cannot exceed customer-authorized limits (amount, frequency); collect requests expire within NPCI-defined windows; device binding follows NPCI's device fingerprinting requirements; every transaction has an end-to-end traceable reference (UPI transaction ID)
- **Configurable vs. compliance floor:** VPA naming conventions, mandate default limits, merchant callback URLs, and transaction velocity limits are configurable. Compliance floor: NPCI circular compliance (transaction limits, mandate rules, dispute timelines), device binding requirements, and two-factor authentication for high-value transactions

---

## Scope Highlights

- VPA lifecycle: creation, modification, deactivation, and multi-account linking
- Mandate management: creation, amendment, pause/resume, revocation, and execution tracking
- Collect/pay orchestration: request initiation, status tracking, callback delivery, and timeout handling
- Merchant UPI integration: QR code generation, deep-link support, and intent-based payment flows
- Dispute handling: complaint registration, status tracking, and resolution workflow (PSP leg)

---

## Capability Domains

_To be expanded._ Candidate domains:

1. VPA Lifecycle Management
2. Mandate and Recurring Payment Management
3. Collect and Pay Request Processing
4. Merchant Integration and QR Management
5. Device Binding and Security
6. Dispute and Complaint Handling

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| UPI Issuer Transaction Processing Fabric | Issuer Fabric handles remitting/beneficiary bank processing; PSP Fabric handles VPA and mandate layer |
| Card PSP Fabric | Separate fabric for card payment gateway; UPI PSP Fabric is UPI-specific |
| Customer Record Fabric | Customer Fabric provides KYC and identity; UPI PSP Fabric links VPAs to verified customers |
| Demand Deposit Fabric | Deposit Fabric holds account balances; UPI PSP Fabric maps VPAs to these accounts |
| Acquirer Fraud and Risk Fabric | Fraud Fabric provides risk signals for UPI transactions; PSP Fabric can apply velocity controls |

---

## References

_To be added._
