# Chapter 03.02.23: Card PSP Fabric — Product Note

**The payer-facing credential and wallet infrastructure — owning stored payment credentials, payer authentication, and the resolution of funding instruments for card-based payments.**

> **Status: Placeholder.** Scope and intent captured. Capability domains and references to be expanded.

---

## What It Governs

Card PSP Fabric is the authoritative system for payer wallets and stored credentials: digital wallet provisioning (Apple Wallet, Samsung Pay, Google Pay, proprietary wallets), credential storage, payer authentication, and the resolution of funding instruments when a payer initiates payment. It operates across channels — ecommerce checkout flows and physical POS (tap-to-pay, NFC) — providing the payer-facing layer that authenticates the payer, captures their funding choice, and delivers a usable credential to the merchant or acquirer.

Out of scope: merchant onboarding and integration (Payment Acquiring Fabric), network routing and settlement (Payment Acquiring Fabric), and issuer-side transaction processing. This fabric focuses on the payer's wallet and credential resolution, not the merchant acceptance or network connectivity layers.

---

## Source of Truth

- **Entities owned:** Payer wallet, stored credential (card-on-file, tokenized card), wallet provisioning request, credential lifecycle state, payer authentication event, funding source preference, device binding, pass/credential in wallet apps
- **Key invariants:** A credential is never returned without successful payer authentication; credential lifecycle state (active, suspended, expired, revoked) is always current; a single credential maps to exactly one funding source; authentication events are immutably logged; expired or revoked credentials are never resolvable
- **Configurable vs. compliance floor:** Supported wallet platforms, authentication methods (biometric, PIN, passkey), credential display preferences, and default funding source are configurable per payer. Compliance floor: PCI DSS for credential storage, EMVCo tokenization standards, strong customer authentication (SCA) where mandated, and credential lifecycle synchronization with issuers

---

## Scope Highlights

- Wallet provisioning: onboarding credentials to Apple Wallet, Samsung Pay, Google Pay, and proprietary wallet apps
- Credential storage: secure storage of card-on-file tokens and wallet-bound credentials
- Payer authentication: biometric, PIN, passkey, or device-based authentication before credential release
- Credential resolution: translating a wallet tap or checkout selection into a usable funding credential for the acquirer
- Lifecycle management: provisioning, updates (expiry refresh, re-tokenization), suspension, and revocation of stored credentials

---

## Capability Domains

_To be expanded._ Candidate domains:

1. Wallet Provisioning and Device Binding
2. Credential Storage and Tokenization
3. Payer Authentication
4. Credential Resolution and Handoff
5. Lifecycle Management (Updates, Suspension, Revocation)
6. Multi-Wallet Orchestration

---

## Responsibility Division: PSP vs. Acquiring

The Card PSP Fabric and Payment Acquiring Fabric have a clear handoff:

| Responsibility | Card PSP Fabric | Payment Acquiring Fabric |
|---|---|---|
| Payer wallet and stored credentials | ✓ Owns | — |
| Payer authentication | ✓ Owns | — |
| Credential resolution | ✓ Owns | — |
| Merchant onboarding and integration | — | ✓ Owns |
| Checkout button/flow (e.g., "Pay with Apple") | — | ✓ Owns (merchant-facing) |
| Network routing and authorization | — | ✓ Owns |
| Settlement to merchants | — | ✓ Owns |

**Dependency flow:** When a merchant-initiated payment shifts to the payer domain (e.g., payer selects Apple Pay at checkout), Acquiring Fabric invokes PSP Fabric to authenticate the payer and resolve the credential. PSP returns the credential; Acquiring presents it to the network.

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| Payment Acquiring Fabric | Acquiring invokes PSP for wallet-based payments; PSP returns resolved credentials; Acquiring routes to networks and settles |
| Acquirer Tokenization Fabric | Tokenization Fabric manages CoF token lifecycle; PSP Fabric consumes tokens for credential storage and resolution |
| Issuer Tokenization Fabric | Issuer-side tokens (e.g., MDES/VTS provisioning) flow into PSP wallets; PSP manages the payer-facing lifecycle |
| Card Authentication Fabric | Authentication Fabric may provide 3DS signals; PSP Fabric performs payer authentication for wallet-initiated flows |
| UPI PSP Fabric | Separate fabric for UPI-specific payer wallet and VPA operations; Card PSP focuses on card rails |

---

## References

_To be added._
