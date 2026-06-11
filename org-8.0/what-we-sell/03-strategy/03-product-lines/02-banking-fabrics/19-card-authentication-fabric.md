# Chapter 03.02.19: Card Authentication Fabric — Product Note

**The system of record for cardholder authentication in e-commerce and digital transactions — managing 3D Secure challenges, Strong Customer Authentication (SCA) orchestration, and risk-based authentication decisions from the issuer's perspective.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Card Authentication Fabric owns the issuer-side orchestration of cardholder authentication for card-not-present (CNP) transactions. This includes processing 3D Secure (3DS) authentication requests per EMVCo specifications (3DS 2.x), executing Strong Customer Authentication (SCA) as required by PSD2 and equivalent regulations, making risk-based authentication (RBA) decisions to determine frictionless vs. challenge flows, and managing authentication methods (OTP, biometrics, app-based approval). The fabric receives authentication requests from the Directory Server, evaluates transaction and cardholder risk, selects authentication methods, and returns authentication results. It does not own the transaction authorization (Card Issuer Transaction Processing Fabric), cardholder contact data (Customer Record Fabric), or fraud models (Issuer Fraud and Risk Fabric), but coordinates with each.

---

## Source of Truth

- **Entities owned:** Authentication Request, Authentication Response, Challenge Record, Authentication Method Preference, RBA Decision, Authentication Result, SCA Exemption Claim, Device Fingerprint Record
- **Key invariants:**
  - Every authentication request receives a response within protocol timeframes (typically <10 seconds for frictionless, longer for challenge)
  - SCA is applied when required by regulation — exemptions are claimed only when legally permitted and risk-justified
  - Challenge completion status is final — a passed challenge cannot be retroactively failed, and vice versa
  - Authentication results are cryptographically signed and tamper-evident for liability shift purposes
  - Cardholder authentication method preferences are respected within risk tolerance bounds
- **Configurable vs. compliance floor:**
  - *Configurable:* RBA thresholds for frictionless approval, preferred authentication methods, challenge UX flows, exemption request policies, device trust rules
  - *Compliance floor:* EMVCo 3DS protocol compliance; PSD2 SCA requirements and exemption rules; cryptographic signing of authentication results; audit trail for every authentication decision; timely response per protocol SLAs

---

## Scope Highlights

- 3DS authentication request processing — receiving AReq from Directory Server, gathering cardholder and transaction context, initiating RBA
- Risk-based authentication (RBA) — evaluating transaction risk signals, device trust, behavioral patterns to determine frictionless vs. challenge
- Challenge orchestration — selecting authentication method, delivering challenge (OTP, push notification, biometric), validating response
- SCA exemption handling — evaluating and claiming exemptions (low-value, trusted beneficiary, TRA) per regulatory rules
- Authentication result generation — producing cryptographically signed ARes with authentication outcome and liability shift indicators
- Method management — maintaining cardholder authentication preferences, enrolled methods, and fallback options

---

## Capability Domains

_To be expanded._ Candidate domains:

1. 3DS Protocol Handling (ACS)
2. Risk-Based Authentication Engine
3. Challenge Orchestration
4. Authentication Method Management
5. SCA Exemption Engine
6. Device Trust and Fingerprinting
7. Cryptographic Signing and Verification
8. Directory Server Integration

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Card Issuer Transaction Processing Fabric | Authentication occurs before or during authorization; Transaction Processing receives authentication results for authorization decisions and liability shift |
| Issuer Fraud and Risk Fabric | Fraud Fabric provides risk signals; Authentication Fabric incorporates them in RBA decisions |
| Card Issuance Fabric | Card Issuance provides card and cardholder data; Authentication Fabric uses it for validation and challenge delivery |
| Customer Record Fabric | Customer Record provides contact data (phone, email); Authentication Fabric uses it for OTP and notification delivery |
| Issuer Tokenization Fabric | For tokenized transactions, Tokenization provides token context; Authentication Fabric may use it for device binding decisions |

---

## References

_To be added._
