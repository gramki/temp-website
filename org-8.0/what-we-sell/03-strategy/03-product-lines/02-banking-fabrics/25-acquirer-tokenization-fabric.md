# Chapter 03.02.25: Acquirer Tokenization Fabric — Product Note

**The system of record for acquirer-side and token-requestor tokenization — owning card-on-file token lifecycle, HCE provisioning, and the merchant/acquirer's interface to network token services.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Acquirer Tokenization Fabric is the authoritative system for token requestor scenarios: requesting network tokens on behalf of merchants for card-on-file (CoF) storage, managing token lifecycle (provisioning, updates, suspensions), and supporting Host Card Emulation (HCE) for mobile wallet provisioning on the acquirer/merchant side. It governs the acquirer's or PSP's relationship with Token Service Providers (TSPs) — Visa VTS, Mastercard MDES, and network-agnostic solutions.

Out of scope: issuer-side token provisioning and lifecycle (Issuer Tokenization Fabric), which handles the issuing bank's TSP integration. This fabric focuses on the merchant/acquirer as token requestor, not the issuer as token provider.

---

## Source of Truth

- **Entities owned:** Token requestor ID, network token (acquirer-held), token-to-PAN mapping reference, token status, CoF token profile, HCE provisioning record, cryptogram generation request, token update notification, merchant token vault
- **Key invariants:** PANs are never stored post-tokenization (only tokens); token status reflects network source of truth (active, suspended, deleted); cryptograms are single-use and time-bound; token updates (e.g., new expiry from issuer) propagate to stored credentials within SLA; each token maps to exactly one funding PAN at the network level
- **Configurable vs. compliance floor:** Token requestor enrollment per network, merchant token vault partitioning, cryptogram validity windows, and automatic retry policies are configurable. Compliance floor: PCI DSS token storage requirements, network brand rules for token requestor certification, and EMVCo standards for HCE cryptogram generation

---

## Scope Highlights

- Token requestor enrollment: certification and onboarding with Visa VTS, Mastercard MDES, and other TSPs
- Card-on-file tokenization: PAN-to-token conversion at checkout, token storage, and transaction submission with tokens
- Token lifecycle management: handling issuer-initiated updates (new expiry, account changes), suspensions, and deletions
- HCE provisioning: mobile wallet token provisioning for merchant apps, cryptogram generation, and device binding
- Token vault operations: secure storage, retrieval, and rotation of merchant-held tokens

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Token Requestor Enrollment and Certification
2. Card-on-File Token Lifecycle
3. HCE Provisioning and Cryptogram Management
4. Token Vault and Secure Storage
5. Network Token Update Processing
6. Multi-Network Token Orchestration

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Issuer Tokenization Fabric | Issuer Fabric handles token provisioning from issuer side; Acquirer Fabric handles token requestor side |
| Card PSP Fabric | PSP Fabric stores tokens for recurring/saved card payments; Tokenization Fabric manages the token lifecycle |
| Payment Acquiring Fabric | Acquiring Fabric submits tokenized transactions to networks; Tokenization Fabric provides valid tokens and cryptograms |
| Card Authentication Fabric | Authentication Fabric may require token-based authentication data; Tokenization Fabric supplies token metadata |

---

## References

_To be added._
