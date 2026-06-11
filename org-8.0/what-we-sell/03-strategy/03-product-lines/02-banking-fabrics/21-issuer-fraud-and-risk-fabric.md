# Chapter 03.02.21: Issuer Fraud and Risk Fabric — Product Note

**The system of record for transaction-level fraud detection and risk management from the issuing bank's perspective — providing real-time risk scores, fraud rules execution, alert management, and case investigation while balancing fraud loss reduction against customer friction.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Issuer Fraud and Risk Fabric owns the detection, scoring, and management of fraud risk for transactions where the bank is the issuer. This includes real-time transaction risk scoring (during authorization), fraud rule execution, alert generation and triage, case investigation workflows, and feedback loops to improve detection models. The fabric provides risk signals consumed by Card Issuer Transaction Processing, Card Authentication, and other fabrics for decisioning. It also manages post-transaction fraud detection, account-level risk assessment, and fraud operations workflows. It does not own the transaction authorization decision (Card Issuer Transaction Processing Fabric), dispute handling (Issuer Disputes Fabric), or the underlying accounts, but provides the fraud intelligence that informs those systems.

---

## Source of Truth

- **Entities owned:** Risk Score, Fraud Rule, Alert, Fraud Case, Investigation Record, Fraud Pattern, Customer Risk Profile, Device Trust Record, Merchant Risk Profile, Model Performance Metrics
- **Key invariants:**
  - Every scored transaction has a traceable risk score with the contributing factors documented for explainability
  - Real-time scoring completes within authorization latency budgets (typically <100ms incremental latency)
  - Alerts are triaged within SLA — aging alerts are escalated, not silently ignored
  - Confirmed fraud cases feed back to models and rules — the system learns from outcomes
  - False positive rates are monitored and managed — excessive friction triggers review
- **Configurable vs. compliance floor:**
  - *Configurable:* Risk thresholds for decline vs. step-up vs. approve, rule weights, alert prioritization, investigation workflows, model retraining frequency, customer friction tolerance
  - *Compliance floor:* BSA/AML suspicious activity detection and reporting; fair lending compliance in risk scoring; audit trail for every risk decision; model governance per SR 11-7; timely fraud loss reporting per network requirements

---

## Scope Highlights

- Real-time transaction scoring — evaluating transaction, cardholder, device, and merchant signals to produce risk scores within latency budget
- Fraud rule execution — applying velocity rules, pattern rules, geographic rules, and behavioral rules alongside model scores
- Alert generation and triage — creating alerts from high-risk transactions, prioritizing by severity, routing to appropriate queues
- Case investigation — providing investigators with transaction context, history, related alerts, and decision support tools
- Feedback and model improvement — capturing confirmed fraud and false positive outcomes, retraining models, tuning rules
- Account-level risk management — maintaining customer and account risk profiles, detecting account takeover patterns, coordinating card blocks

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Real-Time Risk Scoring Engine
2. Fraud Rule Management
3. Alert Generation and Prioritization
4. Case Management and Investigation
5. Customer Risk Profiling
6. Device Intelligence
7. Merchant Risk Assessment
8. Model Training and Governance
9. Feedback Loop Management
10. Fraud Operations Workflow

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Card Issuer Transaction Processing Fabric | Fraud Fabric provides risk scores; Transaction Processing incorporates them in authorization decisions |
| Card Authentication Fabric | Fraud Fabric provides risk signals; Authentication Fabric uses them for RBA decisions on frictionless vs. challenge |
| Issuer Disputes Fabric | Fraud Fabric provides fraud indicators; Disputes Fabric uses them for investigation and reason code selection |
| Card Issuance Fabric | Fraud Fabric may trigger card blocks; Card Issuance executes status changes and reissuance |
| Issuer Tokenization Fabric | Fraud Fabric may flag high-risk provisioning; Tokenization Fabric uses signals for provisioning decisions |
| UPI Issuer Transaction Processing Fabric | Fraud Fabric provides risk scores for UPI transactions; UPI Processing uses them for transaction decisions |
| Transfers Fabric | Fraud Fabric provides risk signals for transfers; Transfers Fabric may hold or block suspicious transfers |
| Collections Fabric | Fraud Fabric identifies first-party fraud patterns; Collections coordinates with fraud on recovery strategies |

---

## References

_To be added._
