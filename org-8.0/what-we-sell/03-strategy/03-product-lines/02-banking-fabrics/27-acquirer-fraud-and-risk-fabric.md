# Chapter 03.02.27: Acquirer Fraud and Risk Fabric — Product Note

**The system of record for acquirer-side fraud prevention and merchant risk management — owning transaction screening, merchant risk scoring, and fraud prevention controls from the acquiring perspective.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Acquirer Fraud and Risk Fabric is the authoritative system for fraud detection and risk management on the acquirer side: real-time transaction screening before authorization, merchant risk assessment and monitoring, velocity controls, and fraud pattern detection across the merchant portfolio. It governs the acquirer's and PSP's responsibility to prevent fraudulent transactions and manage merchant risk — distinct from issuer-side fraud detection which protects cardholders.

Out of scope: issuer-side fraud detection and cardholder protection (Issuer Fraud and Risk Fabric), dispute management (Acquirer Disputes Fabric), and merchant onboarding decisions (Payment Acquiring Fabric, though this fabric provides risk signals). This fabric focuses on transaction-level and merchant-level fraud/risk assessment, not the dispute remediation process.

---

## Source of Truth

- **Entities owned:** Transaction risk score (acquirer-calculated), merchant risk profile, fraud rule, velocity limit, block list entry, suspicious activity report (acquirer-filed), fraud case, risk alert, device fingerprint (acquirer-collected), merchant monitoring status
- **Key invariants:** Every transaction receives a risk assessment before authorization decision; block lists are applied in real-time with zero false-negative tolerance for confirmed fraud indicators; merchant risk scores update based on actual fraud/chargeback rates; SAR filing deadlines are enforced; velocity limits are atomic and cannot be circumvented by transaction splitting
- **Configurable vs. compliance floor:** Risk score thresholds, velocity limit parameters, rule weights, merchant review triggers, and alert routing are configurable per merchant segment. Compliance floor: BSA/AML SAR filing requirements, PCI DSS fraud monitoring requirements, and network brand rules for merchant monitoring programs (Visa VFMP, Mastercard MATCH)

---

## Scope Highlights

- Real-time transaction screening: risk scoring, rule evaluation, and decline/flag decisions before authorization submission
- Merchant risk monitoring: ongoing assessment of fraud rates, chargeback ratios, and suspicious patterns
- Velocity and limit controls: transaction frequency, amount, and pattern limits to prevent fraud bursts
- Block list management: maintaining and applying lists of known fraudulent cards, devices, and identities
- Fraud case management: investigation workflows, evidence collection, and resolution tracking

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Real-Time Transaction Risk Scoring
2. Merchant Risk Assessment and Monitoring
3. Velocity Controls and Limit Management
4. Block List and Watchlist Management
5. Fraud Investigation and Case Management
6. Regulatory Reporting (SAR/STR Filing)

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Issuer Fraud and Risk Fabric | Issuer Fabric protects cardholders; Acquirer Fabric protects merchants and the acquirer from fraud losses |
| Payment Acquiring Fabric | Acquiring Fabric consumes risk decisions for authorization; Fraud Fabric provides the risk assessment |
| Card PSP Fabric | PSP Fabric may apply fraud rules at gateway level; Fraud Fabric provides the rule engine and risk scores |
| Acquirer Disputes Fabric | Disputes Fabric handles post-transaction chargebacks; Fraud Fabric aims to prevent fraud pre-authorization |
| Underwriting Fabric | Underwriting provides merchant onboarding risk assessment; Fraud Fabric provides ongoing transaction monitoring |

---

## References

_To be added._
