# Chapter 03.02.13: Commercial Card Issuance Fabric — Product Note

**The system of record for corporate and commercial card programs — managing purchasing cards, travel cards, fleet cards, and virtual card numbers with the hierarchical controls, approval workflows, and expense management integration that enterprise buyers require.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Commercial Card Issuance Fabric owns the identity, hierarchy, and lifecycle of cards issued to businesses rather than consumers. This includes corporate cards (individually liable and company liable), purchasing cards (P-cards), fleet cards, single-use virtual card numbers (VCNs), and ghost cards for recurring vendor payments. The fabric governs corporate program setup, card hierarchy (company → cost center → cardholder), spending controls (MCC restrictions, transaction limits, velocity limits), and the data enrichment required for expense management and ERP integration. It does not govern the credit facility underwriting (Underwriting Fabric), the underlying line of credit (Line and Limits Fabric), or transaction authorization logic (Card Issuer Transaction Processing Fabric).

---

## Source of Truth

- **Entities owned:** Commercial Card Program, Corporate Hierarchy Node, Commercial Card, Virtual Card Number, Spending Control Profile, MCC Restriction Set, Approval Workflow, Card-to-Cost-Center Mapping, Program Administrator Role
- **Key invariants:**
  - Every commercial card belongs to exactly one program and one hierarchy node
  - Spending controls at parent nodes cascade to children unless explicitly overridden
  - Virtual card numbers have defined validity windows and usage limits (single-use, merchant-locked, amount-capped)
  - MCC restrictions are enforced atomically — a card cannot transact at a blocked merchant category
  - Program-level credit exposure cannot exceed the approved facility limit
- **Configurable vs. compliance floor:**
  - *Configurable:* Hierarchy depth, control inheritance rules, approval thresholds, MCC allow/block lists, VCN generation rules, expense category mappings, ERP export formats
  - *Compliance floor:* PCI DSS for card data; segregation of duties between program administrators and cardholders; audit trail for control changes; real-time propagation of card blocks; merchant category accuracy per network standards

---

## Scope Highlights

- Corporate program setup — program terms, billing cycles, liability models (corporate vs. individual), rebate structures
- Hierarchy management — modeling organizational structures (company, division, department, cost center, project) with control inheritance
- Card issuance workflows — bulk issuance, self-service requests, manager approvals, instant virtual cards
- Spending control configuration — per-card, per-hierarchy-node, or program-wide limits, MCC rules, time-of-day restrictions
- Virtual card number generation — on-demand VCNs for AP automation, travel booking, subscription management
- Expense data enrichment — Level II/III data capture, merchant name cleansing, category tagging for downstream reconciliation

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Commercial Program Management
2. Corporate Hierarchy and Cost Center Modeling
3. Spending Control Engine
4. Virtual Card Number Generation
5. Card Lifecycle (Commercial)
6. Expense Data Enrichment and ERP Integration
7. Program Administrator Self-Service

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Line and Limits Fabric | Line and Limits owns the corporate credit facility; Commercial Card Issuance allocates and tracks utilization against that facility |
| Underwriting Fabric | Underwriting approves the corporate program and facility; Commercial Card Issuance operationalizes it |
| Card Issuer Transaction Processing Fabric | Commercial Card Issuance provides card and control data; Transaction Processing executes authorization with MCC/limit checks |
| Issuer Tokenization Fabric | Commercial Card Issuance owns PANs; Tokenization owns token provisioning for commercial card tokens |
| Accounting Fabric | Commercial Card Issuance provides transaction and hierarchy data; Accounting posts to GL per program terms |
| Product Fabric | Product Fabric defines commercial card products; Commercial Card Issuance instantiates programs against those products |

---

## References

_To be added._
