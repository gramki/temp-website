# Chapter 03.02.14: Issuer Tokenization Fabric — Product Note

**The system of record for issuer-side payment token lifecycle — managing the provisioning, suspension, and deletion of tokens that represent card credentials in mobile wallets, e-commerce vaults, and IoT devices while preserving the issuer's control over when and where a card can transact.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Issuer Tokenization Fabric owns the token lifecycle from the issuing bank's perspective. When a cardholder provisions their card into Apple Pay, Google Pay, a merchant's card-on-file vault, or a connected device, this fabric manages the token request approval, token-to-PAN mapping, token status synchronization, and lifecycle events (suspend, resume, delete). It coordinates with Token Service Providers (TSPs) operated by card networks (Visa VTS, Mastercard MDES) and maintains the issuer's authoritative view of which tokens exist for each card. The fabric does not own the card itself (Card Issuance Fabric) or transaction authorization (Card Issuer Transaction Processing Fabric), but provides the token context required for authorization decisions.

---

## Source of Truth

- **Entities owned:** Token, Token-to-PAN Mapping, Token Requestor Registration, Device Binding, Token Status, Provisioning Request, Token Lifecycle Event
- **Key invariants:**
  - Every token maps to exactly one PAN, and that mapping is immutable for the token's lifetime
  - Token status (active, suspended, deleted) is always synchronized with the TSP within SLA bounds
  - A suspended or deleted token cannot authorize transactions — this state is available to authorization in real time
  - Provisioning decisions respect card status — tokens cannot be provisioned for blocked, expired, or closed cards
  - Token requestor identity is verified and recorded for every provisioning event
- **Configurable vs. compliance floor:**
  - *Configurable:* Wallet and token requestor allow/deny lists, step-up authentication requirements per requestor risk tier, automatic provisioning rules, token display preferences (last-four digits, card art)
  - *Compliance floor:* EMVCo tokenization standards compliance; PCI DSS for token-to-PAN mapping storage; real-time token status synchronization with networks; cardholder consent and authentication for provisioning; audit trail for all lifecycle events

---

## Scope Highlights

- Token provisioning approval — evaluating provisioning requests, applying risk rules, triggering step-up authentication (ID&V)
- TSP integration — bidirectional communication with Visa VTS, Mastercard MDES, and private-label TSPs
- Token-to-PAN mapping — maintaining the authoritative issuer-side record linking tokens to underlying cards
- Token lifecycle management — suspend, resume, delete in response to card events (lost/stolen, reissue) or cardholder requests
- Device and wallet binding — tracking which tokens are bound to which devices, wallets, or merchant vaults
- Token context for authorization — providing token metadata to Transaction Processing Fabric for authorization decisions

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Token Provisioning and ID&V
2. TSP Integration (VTS, MDES, Private-Label)
3. Token-to-PAN Mapping Registry
4. Token Lifecycle Management
5. Device and Wallet Binding
6. Token Requestor Management
7. Card Event Propagation to Tokens

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Card Issuance Fabric | Card Issuance owns the PAN and card status; Tokenization Fabric provisions tokens against that PAN and propagates card status changes to tokens |
| Card Issuer Transaction Processing Fabric | Tokenization Fabric provides token-to-PAN resolution and token status; Transaction Processing uses this for authorization |
| Card Authentication Fabric | Authentication Fabric may trigger step-up during provisioning; Tokenization Fabric consumes authentication results |
| Issuer Fraud and Risk Fabric | Fraud Fabric provides risk signals for provisioning decisions; Tokenization Fabric may suspend tokens based on fraud alerts |
| Commercial Card Issuance Fabric | For commercial cards, Commercial Card Issuance owns the card; Tokenization Fabric provisions tokens similarly |

---

## References

_To be added._
