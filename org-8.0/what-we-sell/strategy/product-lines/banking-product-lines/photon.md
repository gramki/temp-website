# Photon — Payments and Money Movement

**Product lines for payment processing, orchestration, acquiring, and money movement — covering payment rails, card management, merchant acquiring, tokenization, and private-labeled payment networks.**

---

## Product Family

Photon is Zeta's payments and money movement family. It provides the full infrastructure for processing, routing, acquiring, and settling payments — from payment rail orchestration through merchant management to private-labeled payment networks.

### Product Lines

| Product Line | Domain | Description |
|---|---|---|
| **Photon Payments Hub** | Payment orchestration across rails | Orchestration and routing across domestic and cross-border payment rails — UPI, IMPS, NEFT, RTGS, ACH, SWIFT, card networks. *(To be expanded)* |
| **Photon Acquiring** | Merchant acquiring and acceptance | Merchant onboarding, management, payment terminals, POS acquiring, QR acquiring, online acquiring, and checkout interfaces. *(To be expanded)* |
| **Photon Card Management** | Card lifecycle and operations | Card issuance, lifecycle management, replacement, reissuance, PIN management, and card-level controls. *(To be expanded)* |
| **Photon Tokenization** | Token lifecycle and credential management | Tokenized credentials, token provisioning, lifecycle management, and de-tokenization services across networks and form factors. *(To be expanded)* |
| **Photon Payment Network** | Private-labeled payment instruments and networks | Private-labeled instruments, proprietary rails, clearing, settlement, and dispute management for closed-loop and hybrid payment networks. *(To be expanded)* |
| **Photon Payment Aggregator Services** | Payment aggregation and facilitation | Payment aggregation, sub-merchant management, and payment facilitation services. *(To be expanded)* |

---

## Relationship to Fabrics

| Fabric | How Photon Uses It |
|---|---|
| **Evolution Fabric** | Photon product lines register as Machines in payment domain Hubs — declaring payment capabilities (authorize, settle, reverse, route) as Tools. Payment flows modeled as Streams; reconciliation, fraud detection, and settlement cycles modeled as Loops |
| **Trust Fabric** | Transaction authentication, merchant identity, payment consent, and regulatory compliance for payment participants |
| **Truth Fabric** | Semantic definitions for payment entities — transaction states, settlement statuses, interchange categories, fee structures — with authority-aware reconciliation across rails |
| **Cognitive Audit Fabric** | Auditability for payment decisions — routing choices, fraud assessments, exception handling, dispute adjudication |
| **Cloud Fabric** | Infrastructure management, observability, and operational reliability for Photon deployments |

---

## Relationship to Other Product Families

| Family | Relationship |
|---|---|
| **Tachyon** | Photon payment flows debit and credit Tachyon accounts — the account ledger is the endpoint for every payment |
| **Electron** | Electron card transactions flow through Photon for authorization, clearing, and settlement |
| **Neutrino** | Neutrino channels provide payment initiation surfaces — mobile payments, merchant portals, API integrations |
| **Quark** | Quark payment domain hubs consume Photon as a Machine — invoking payment capabilities through declared tool contracts within payment Streams and Loops |

---

*This is a placeholder brief. Individual product line details to be expanded in subsequent sessions.*
