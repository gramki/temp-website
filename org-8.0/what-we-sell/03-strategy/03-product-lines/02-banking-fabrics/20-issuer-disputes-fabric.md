# Chapter 03.02.20: Issuer Disputes Fabric — Product Note

**The system of record for cardholder disputes from the issuing bank's perspective — managing dispute intake, chargeback filing, representment defense, arbitration, and regulatory compliance while protecting cardholder rights and managing financial exposure.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Issuer Disputes Fabric owns the lifecycle of transaction disputes where the bank is the card issuer acting on behalf of its cardholder. This includes dispute intake (cardholder claims of fraud, non-receipt, not-as-described, duplicate charge), investigation and evidence gathering, chargeback filing with networks, processing merchant representments, escalation to arbitration or compliance when necessary, and provisional/final credit management. The fabric enforces network timelines (Visa, Mastercard dispute rules), manages reason code accuracy, and maintains the documentation required for regulatory examination. It does not own the original transaction (Card Issuer Transaction Processing Fabric), fraud detection (Issuer Fraud and Risk Fabric), or account posting (Revolving Credit or Demand Deposit Fabrics), but coordinates with each.

---

## Source of Truth

- **Entities owned:** Dispute Case, Cardholder Claim, Chargeback Record, Representment Record, Arbitration Filing, Provisional Credit, Final Resolution, Evidence Package, Reason Code Assignment
- **Key invariants:**
  - Every dispute has exactly one active status and follows a defined state machine (intake → investigation → chargeback → [representment → rebuttal →] resolution)
  - Network filing deadlines are never missed — disputes are filed within mandated timeframes or escalated for exception handling
  - Provisional credits are posted within Regulation E/Z timeframes and reversed only on substantiated merchant win
  - Reason codes accurately reflect the dispute basis — misclassification creates network compliance and arbitration risk
  - Resolution (cardholder win or merchant win) is final within the case — reopen requires new case with new evidence
- **Configurable vs. compliance floor:**
  - *Configurable:* Auto-chargeback thresholds, provisional credit policies, documentation requirements by dispute type, escalation workflows, SLA targets
  - *Compliance floor:* Regulation E (debit) and Regulation Z (credit) consumer protections; Visa/Mastercard operating regulation timelines; accurate reason code assignment; audit trail for every dispute action; cardholder notification requirements

---

## Scope Highlights

- Dispute intake — capturing cardholder claims via call center, digital channels, or branch with required documentation
- Investigation — gathering transaction data, authentication results, merchant information, and prior cardholder history
- Chargeback filing — submitting chargebacks to networks with accurate reason codes and supporting documentation within deadlines
- Representment handling — receiving and evaluating merchant representments, deciding acceptance or rebuttal
- Provisional and final credit — posting conditional credits during investigation, finalizing on resolution
- Arbitration and compliance — escalating to network arbitration when needed, managing pre-arbitration and compliance filings

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Dispute Intake and Triage
2. Investigation and Evidence Management
3. Chargeback Filing Engine
4. Representment Processing
5. Provisional Credit Management
6. Arbitration and Compliance Filing
7. Network Connectivity (VROL, Mastercom)
8. Deadline and SLA Management
9. Cardholder Communication

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Card Issuer Transaction Processing Fabric | Transaction Processing provides original transaction data; Disputes Fabric uses it for investigation and chargeback basis |
| Issuer Fraud and Risk Fabric | Fraud Fabric provides fraud indicators and prior fraud history; Disputes Fabric uses them for investigation and reason code selection |
| Revolving Credit Fabric | For credit card disputes, Revolving Credit owns the account; Disputes Fabric coordinates provisional and final credit posting |
| Demand Deposit Fabric | For debit card disputes, Demand Deposit owns the account; Disputes Fabric coordinates provisional and final credit posting |
| Card Authentication Fabric | Authentication Fabric provides 3DS authentication results; Disputes Fabric uses them for liability shift determination |
| Accounting Fabric | Disputes Fabric provides dispute financial impacts; Accounting posts to GL and manages dispute reserves |

---

## References

_To be added._
