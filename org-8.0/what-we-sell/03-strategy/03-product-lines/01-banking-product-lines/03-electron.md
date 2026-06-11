# Chapter 03.01.03: Electron — Commercial Cards and Payment Products

**Product lines for commercial card programs — covering benefits cards, expense management, purchase cards, and corporate payment products.**

---

## Product Family

Electron is Zeta's commercial cards and payment products family. It provides the infrastructure for issuing, managing, and governing commercial card programs across corporate, SME, and institutional segments.

### Product Lines

| Product Line | Domain | Description |
|---|---|---|
| **Electron Benefits** | Benefits card programs | *(To be expanded)* |
| **Electron Expense Cards** | Corporate expense management | *(To be expanded)* |
| **Electron Purchase Cards** | Procurement and purchase card programs | *(To be expanded)* |

---

## Relationship to Fabrics

| Fabric | How Electron Uses It |
|---|---|
| **Evolution Fabric** | Electron product lines register as Machines in commercial card domain Hubs — declaring card program capabilities (issue, load, authorize, report, reconcile) as Tools. Card program operations modeled as Streams; expense policy enforcement, reconciliation, and reporting cycles modeled as Loops |
| **Trust Fabric** | Cardholder and program administrator identity, authentication, authorization policies, and corporate hierarchy-based consent |
| **Truth Fabric** | Semantic definitions for commercial card entities — expense categories, policy limits, merchant categories, allocation codes — with authority-aware reconciliation across corporate hierarchies |
| **Cognitive Audit Fabric** | Auditability for commercial card decisions — policy exceptions, spending approvals, expense categorizations, fraud determinations |
| **Cloud Fabric** | Infrastructure management, observability, and operational reliability for Electron deployments |

---

## Relationship to Other Product Families

| Family | Relationship |
|---|---|
| **Tachyon** | Electron commercial card programs are built on Tachyon account infrastructure — card accounts, ledgers, and limit management |
| **Photon** | Electron card transactions flow through Photon for authorization, clearing, and settlement across payment networks |
| **Neutrino** | Neutrino channels provide cardholder and administrator experiences — mobile apps, expense portals, reporting dashboards |
| **Quark** | Quark commercial card domain hubs consume Electron as a Machine — invoking card program capabilities through declared tool contracts within program Streams and Loops |

---

*This is a placeholder brief. Individual product line details to be expanded in subsequent sessions.*
