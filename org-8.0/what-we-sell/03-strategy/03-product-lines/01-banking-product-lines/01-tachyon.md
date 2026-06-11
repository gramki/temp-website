# Chapter 03.01.01: Tachyon — Account Products

**Product lines for account origination, lifecycle, and management — covering deposits, credit, lending, and customer lifecycle across retail and business banking.**

---

## Product Family

Tachyon is Zeta's account products family. It provides the core account infrastructure that banks need to originate, manage, and service financial accounts across segments and product types.

### Product Lines

| Product Line | Domain | Description | Production Status |
|---|---|---|---|
| **Tachyon Kernel** | Core account infrastructure | Shared account ledger, limit management, and product configuration engine underlying all Tachyon product lines. | In production (powers all Tachyon deployments) |
| **Tachyon DDA** | Demand deposit accounts | Demand deposit account origination, lifecycle, and servicing — supporting purpose-specific account programs (health benefits, loyalty and rewards). | In production — multiple US programs including health benefits (Optum) and loyalty/rewards programs |
| **Tachyon Credit Cards** | Credit card issuance and management | Credit card account origination, lifecycle management, billing, statement generation, and card-level controls. | In production — three credit card programs in the USA |
| **Tachyon CLM** | Customer lifecycle management | *(To be expanded)* | |
| **Tachyon Loans** | Lending products | *(To be expanded)* | |

### Production Footprint

Tachyon is in production in the United States across two product lines:

- **Tachyon Credit Cards** powers three credit card programs in the USA. All three programs use Photon for payment rail processing (authorization, clearing, settlement).
- **Tachyon DDA** powers multiple demand deposit account programs in the USA, including health benefits accounts (Optum) and loyalty/rewards programs. All programs use Photon for payment processing.

Tachyon Credit Cards and Tachyon DDA represent Zeta's core account platform in production at scale in the US market. Tachyon CLM and Tachyon Loans remain in earlier stages of development.

---

## Relationship to Fabrics

| Fabric | How Tachyon Uses It |
|---|---|
| **Evolution Fabric** | Tachyon product lines register as Machines in domain Hubs — declaring their capabilities as Tools (commands, predictions, decisions) that Scenarios invoke. Account operations modeled as Streams and Loops within Evolution Fabric's domain model |
| **Trust Fabric** | Customer identity, authentication, consent, and privacy for account holders |
| **Truth Fabric** | Semantic definitions for account entities — balances, limits, statuses, product terms — with authority-aware reconciliation |
| **Cognitive Audit Fabric** | Auditability for account decisions — credit approvals, limit changes, fee assessments, risk classifications |
| **Cloud Fabric** | Infrastructure management, observability, and operational reliability for Tachyon deployments |

---

## Relationship to Other Product Families

| Family | Relationship |
|---|---|
| **Photon** | Tachyon accounts are the ledger endpoints for Photon payment flows — debits, credits, holds, and settlements |
| **Electron** | Electron commercial card programs are built on Tachyon account infrastructure |
| **Neutrino** | Neutrino channels provide the customer-facing experiences for Tachyon account products |
| **Quark** | Quark domain hubs consume Tachyon product lines as Machines — invoking account capabilities through declared tool contracts |

---

*Tachyon Credit Cards and Tachyon DDA are production-validated. Tachyon CLM and Tachyon Loans product line details to be expanded in subsequent sessions.*
