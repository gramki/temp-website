# Chapter 03.02.26: Acquirer Disputes Fabric — Product Note

**The system of record for acquirer-side dispute management — owning retrieval request response, chargeback defense, representment, and the merchant's dispute lifecycle.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Acquirer Disputes Fabric is the authoritative system for managing disputes from the acquirer and merchant perspective: receiving retrieval requests and chargebacks from networks, coordinating merchant response and evidence collection, submitting representments, and tracking dispute outcomes through arbitration if necessary. It governs the merchant's defense against cardholder disputes, distinct from issuer-side dispute initiation.

Out of scope: issuer-side chargeback initiation and cardholder dispute intake (Issuer Disputes Fabric), transaction authorization and clearing (Payment Acquiring Fabric), and fraud detection (Acquirer Fraud and Risk Fabric). This fabric manages the dispute workflow, not the underlying transaction processing or fraud decision.

---

## Source of Truth

- **Entities owned:** Chargeback case (acquirer view), retrieval request, representment submission, dispute evidence package, pre-arbitration case, arbitration filing, dispute outcome, merchant dispute history, reason code classification, dispute fee record
- **Key invariants:** Response deadlines are enforced per network rules (Visa 30 days, Mastercard 45 days, etc.); representment evidence packages are immutable once submitted; dispute outcomes update merchant settlement and reserve positions; each dispute maps to exactly one original transaction; reason code determines valid defense types
- **Configurable vs. compliance floor:** Auto-accept thresholds (disputes below $X), merchant notification preferences, evidence template selection, and representment automation rules are configurable. Compliance floor: network brand dispute rules (Visa VCR, Mastercard Dispute Resolution), response deadline enforcement, and audit trail retention for regulatory examination

---

## Scope Highlights

- Retrieval request processing: receiving requests, notifying merchants, collecting transaction documentation, and responding within deadlines
- Chargeback defense: reason code analysis, evidence gathering (receipts, delivery proof, communication logs), and representment submission
- Merchant communication: dispute alerts, evidence requests, outcome notifications, and dispute analytics
- Pre-arbitration and arbitration: escalation handling, filing preparation, and outcome tracking
- Financial impact management: chargeback debits, representment credits, and reserve adjustments

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Retrieval Request Management
2. Chargeback Intake and Classification
3. Evidence Collection and Representment
4. Pre-Arbitration and Arbitration
5. Merchant Dispute Portal and Communication
6. Dispute Analytics and Prevention Insights

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Issuer Disputes Fabric | Issuer Fabric initiates chargebacks on cardholder behalf; Acquirer Fabric defends on merchant behalf |
| Payment Acquiring Fabric | Acquiring Fabric provides original transaction data; Disputes Fabric manages the dispute case |
| Acquirer Fraud and Risk Fabric | Fraud Fabric identifies transactions with high dispute risk; Disputes Fabric handles actual disputes |
| Card PSP Fabric | PSP Fabric may surface dispute notifications to merchants; Disputes Fabric owns the dispute record |
| Accounting Fabric | Accounting Fabric records chargeback debits and representment credits |

---

## References

_To be added._
