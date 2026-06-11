# Chapter 03.02.22: Payment Acquiring Fabric — Product Note

**The merchant-facing system for payment acceptance and the network-routing engine for authorization and settlement — owning merchant onboarding, checkout integration, transaction routing, and settlement disbursement.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Payment Acquiring Fabric is the authoritative system for merchant relationships, checkout integration, authorization routing, and settlement. It governs the full merchant lifecycle: application and underwriting, terminal/integration provisioning, checkout experience (including wallet payment buttons like "Pay with Apple" or "Stripe Link"), authorization routing to card networks, and settlement disbursement to merchants.

When a payer selects a wallet-based payment at checkout, this fabric hands off to Card PSP Fabric for payer authentication and credential resolution, then receives the resolved credential and routes the transaction to networks.

Out of scope: payer wallet and credential storage (Card PSP Fabric), payer authentication (Card PSP Fabric), issuer-side transaction processing (Card Issuer Transaction Processing Fabric), and fraud detection logic (Acquirer Fraud and Risk Fabric) — though this fabric consumes outputs from each.

---

## Source of Truth

- **Entities owned:** Merchant account, merchant hierarchy (chain/store/terminal), acquiring BIN, interchange qualification, fee schedule, settlement instruction, authorization routing rule, merchant category code assignment, reserve account, checkout configuration, payment method enablement
- **Key invariants:** Every authorization request routes to exactly one network endpoint per attempt; settlement amounts always reconcile to cleared transactions minus fees, chargebacks, and reserves; merchant reserves are held and released according to contracted schedules; interchange qualification is determined at transaction time and is immutable post-settlement
- **Configurable vs. compliance floor:** Fee structures, reserve percentages, settlement frequency (next-day, T+2, weekly), routing preferences, and enabled payment methods (card, wallet buttons) are configurable per merchant or portfolio. Compliance floor: PCI DSS controls on cardholder data in transit, network brand rules on authorization/clearing windows, and anti-money-laundering controls on merchant onboarding (beneficial ownership, sanctions screening)

---

## Scope Highlights

- Merchant onboarding: application intake, underwriting decision, boarding to networks, terminal/integration provisioning
- Checkout integration: payment button rendering ("Pay with Apple", "Google Pay", "Stripe Link"), method selection, and checkout orchestration
- Authorization routing: intelligent routing across networks (Visa, Mastercard, local schemes) based on cost, approval rates, and merchant preference
- Settlement processing: daily/periodic calculation of merchant payouts net of interchange, fees, chargebacks, and reserve holds
- Reserve management: holds, releases, and application of reserves to cover chargebacks or merchant default

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Merchant Lifecycle Management
2. Checkout Integration and Payment Method Enablement
3. Authorization Routing and Network Connectivity
4. Clearing and Settlement Processing
5. Interchange and Fee Management
6. Reserve and Risk Mitigation
7. Merchant Hierarchy and Reporting

---

## Responsibility Division: Acquiring vs. PSP

Payment Acquiring Fabric and Card PSP Fabric collaborate on wallet-based payments:

| Responsibility | Payment Acquiring Fabric | Card PSP Fabric |
|---|---|---|
| Merchant onboarding and account management | ✓ Owns | — |
| Checkout integration ("Pay with Apple" button) | ✓ Owns | — |
| Network routing and authorization | ✓ Owns | — |
| Settlement to merchants | ✓ Owns | — |
| Payer wallet and stored credentials | — | ✓ Owns |
| Payer authentication | — | ✓ Owns |
| Credential resolution | — | ✓ Owns |

**Dependency flow:** Merchant-initiated payment → payer selects wallet → Acquiring invokes PSP → PSP authenticates payer and resolves credential → PSP returns credential to Acquiring → Acquiring routes to network → authorization response → settlement.

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Card PSP Fabric | Acquiring invokes PSP for wallet-based payments; PSP authenticates payer and returns resolved credential; Acquiring routes to networks |
| Acquirer Fraud and Risk Fabric | Fraud Fabric provides risk signals and decline recommendations; Acquiring Fabric executes authorization decisions |
| Acquirer Disputes Fabric | Disputes Fabric manages chargeback lifecycle; Acquiring Fabric applies financial adjustments to settlement |
| Acquirer Tokenization Fabric | Tokenization Fabric manages CoF tokens for token-requestor scenarios; Acquiring routes tokenized transactions |
| Accounting Fabric | Settlement entries post to Accounting Fabric for GL reconciliation |

---

## References

_To be added._
