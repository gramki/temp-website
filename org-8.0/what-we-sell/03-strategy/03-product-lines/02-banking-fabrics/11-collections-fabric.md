# Chapter 03.02.11: Collections Fabric — Product Note

**The authoritative system of record for delinquency management and recovery — tracking past-due accounts, managing NPA classification, orchestrating collection strategies, restructuring debt, and processing write-offs.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Collections Fabric owns the delinquency and recovery lifecycle — from the moment an account becomes past due through resolution (cure, restructure, charge-off, or recovery). This includes delinquency tracking, non-performing asset (NPA) classification, collection strategy execution, debt restructuring, and write-off processing.

In scope: delinquency identification and aging, NPA classification per regulatory rules, collection queue management, collection strategy assignment, customer contact orchestration (calls, letters, SMS), payment arrangement negotiation, debt restructuring and forbearance, charge-off processing, post-charge-off recovery tracking, agency placement management. Out of scope: the loan or credit account itself (domain fabrics), credit decisioning for restructured terms (Underwriting Fabric), and legal proceedings (external counsel management).

---

## Source of Truth

- **Entities owned:** Delinquency records, collection cases, NPA classifications, collection activities (contact attempts, promises to pay), payment arrangements, restructuring agreements, charge-off records, recovery records, agency placement records
- **Key invariants:** Delinquency aging is calculated consistently across all products. NPA classification follows regulatory rules without exception. Charge-off timing complies with regulatory requirements. Recovery amounts are tracked against charge-off amounts for accurate loss reporting.
- **Configurable vs. compliance floor:** Collection strategies, contact frequency, restructuring terms, and charge-off timing (within regulatory bounds) are configurable. NPA classification rules (per jurisdiction), fair debt collection practices (FDCPA, equivalent), and loss recognition accuracy are the compliance floor.

---

## Scope Highlights

- Identifies and tracks delinquent accounts across all credit products (cards, loans, mortgages)
- Calculates delinquency aging (30/60/90 DPD) and days past due metrics
- Classifies accounts as non-performing per regulatory definitions (NPA, NPL, substandard, doubtful, loss)
- Assigns and executes collection strategies based on risk segmentation and account characteristics
- Manages customer contact: call campaigns, collection letters, SMS, email, portal-based self-cure
- Negotiates and tracks payment arrangements: promise to pay, payment plans, hardship programs

---

## Capability Domains

_To be expanded._ Candidate domains:

1. **Delinquency Tracking** — Past-due identification, aging calculation, delinquency bucket management, cure tracking
2. **NPA Classification** — Regulatory classification rules, classification triggers, upgrade/downgrade processing
3. **Collection Strategy** — Strategy assignment, segmentation, treatment paths, escalation rules, strategy effectiveness tracking
4. **Contact Management** — Contact orchestration, attempt tracking, right-party contact, regulatory contact limits
5. **Arrangement Management** — Promise to pay, payment plans, forbearance, hardship programs, arrangement compliance
6. **Charge-off and Recovery** — Charge-off processing, provision triggers, recovery tracking, agency placement, recovery allocation

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Revolving Credit Fabric | Delinquent credit card accounts are identified by Revolving Credit; Collections manages the collection case |
| Term Loans Fabric | Delinquent loans are identified by Term Loans; Collections manages recovery |
| Mortgage Fabric | Delinquent mortgages are identified by Mortgage Fabric; Collections manages pre-foreclosure and loss mitigation |
| Demand Deposit Fabric | Overdrawn accounts may be referred to Collections; Collections manages recovery |
| Underwriting Fabric | Restructuring terms may require credit re-evaluation; Underwriting assesses modified terms |
| Accounting Fabric | Charge-offs and provisions trigger accounting entries; Collections provides the charge-off data |
| Customer Record Fabric | Collection cases are linked to customers; contact information comes from Customer Record |
| Credit Bureau Fabric | Delinquency and charge-off status is reported to bureaus through Credit Bureau Fabric |
| Statement Fabric | Collection notices and payoff statements are generated; Statement Fabric may handle delivery |

---

## References

_To be added._
