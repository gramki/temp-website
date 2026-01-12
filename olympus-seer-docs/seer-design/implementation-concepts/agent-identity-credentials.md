# Agent Identity & Credentials

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

Agent Identity & Credentials extends Hub Cipher IAM to support **agent-specific identity and authority management**. It provides the IAM foundation for agent identity, authority delegation, and policy enforcement.

**Key Characteristics:**
- Extensions to Hub Cipher IAM (not replacement)
- Supports Raw, Trained, and Employed Agent identity types
- Authority delegation with human accountability
- Per-PEP policy enforcement

---

## Architecture

Cipher IAM Extensions extends Hub Cipher IAM:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 CIPHER IAM EXTENSIONS ARCHITECTURE                          │
│                                                                              │
│   Seer Components → Cipher IAM Extensions → Hub Cipher IAM (Core)          │
│                                                                              │
│   • Agent Profile API                                                       │
│   • Authority Delegation                                                    │
│   • Policy Enforcement                                                       │
│   • Credential Management                                                   │
│                                                                              │
│   Extends:                                                                   │
│   • Identity Management                                                      │
│   • SPIFFE Integration                                                       │
│   • OPA Policy Engine                                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Extensions to Hub Cipher IAM** — Extends Hub Cipher IAM, not replaces
- **Agent Profile Types** — Raw, Trained, and Employed Agent profiles
- **Authority Delegation Model** — User delegation, role delegation, bot mode
- **Policies Per PEP** — Policies are per Policy Enforcement Point (not global)
- **SPIFFE Integration** — Leverages SPIFFE for cryptographic identity

---

## Agent Profile Types

### Raw Agent Profile

| Aspect | Description |
|--------|-------------|
| **Tag** | `raw-agent` |
| **Capabilities** | Base capabilities, no delegation |
| **Credentials** | No runtime credentials (not yet employed) |
| **Purpose** | Declares supported models, tools, and capabilities |

### Trained Agent Profile

| Aspect | Description |
|--------|-------------|
| **Tag** | `trained-agent` |
| **Capabilities** | Trained capabilities, potential delegation constraints |
| **Credentials** | No runtime credentials (not yet employed) |
| **Purpose** | Inherits from Raw Agent, adds allowed models |

### Employed Agent Profile

| Aspect | Description |
|--------|-------------|
| **Tag** | `employed-agent` |
| **Capabilities** | Full identity with delegation chain and policies |
| **Credentials** | Full credential set (SPIFFE, virtual key, zone-vault reference) |
| **Purpose** | Runtime identity with authority and accountability |

---

## Authority Delegation Model

Three delegation models:

| Model | Description |
|-------|-------------|
| **User Delegation** | Agent acts on behalf of a specific user |
| **Role Delegation** | Agent inherits from a role |
| **Bot Mode** | Agent has base identity only, no delegation |

---

## Credential Management

Credential lifecycle for Employed Agents:

| Credential Type | Provisioned By | Purpose | Rotation |
|-----------------|----------------|---------|----------|
| **SPIFFE Certificate** | SPIRE Agent | mTLS identity, service mesh auth | Automatic (hourly) |
| **Virtual Key** | Seer Operator | Model Gateway access, budget tracking | On employment or rotation request |
| **Zone-Vault Reference** | Seer Operator | Tool credential injection | On demand |

---

## SPIFFE Identity

Employed Agents receive **SPIFFE identities**:

| Aspect | Description |
|--------|-------------|
| **Format** | `spiffe://hub.olympus.io/seer/tenant/{tenant_id}/workbench/{workbench_id}/agent/{agent_id}` |
| **Purpose** | Cryptographic identity for mTLS and service mesh authentication |
| **Rotation** | Automatic rotation (hourly) |
| **Revocation** | Revoked on employment revocation |

---

## Policy Enforcement Points (PEPs)

Policies are **per Policy Enforcement Point**:

| Aspect | Description |
|--------|-------------|
| **PEP-Specific** | Policies are per PEP (not global) |
| **Unknown PEPs** | Unknown PEPs are ignored (graceful degradation) |
| **Policy References** | Policies are referenced files (not inline) |
| **PEP Types** | Tool Gateway, Model Gateway, Signal Exchange, Seer Sidecar |

---

## Human Accountability

All Employed Agents have **accountable humans**:

| Aspect | Description |
|--------|-------------|
| **Accountable Human** | Reference to the Supervisor who delegated authority |
| **Audit Trail** | Full audit trail of delegation and accountability |
| **Delegation Chain** | Full delegation chain traceable to humans |

---

## Related

### Cipher IAM Extensions Subsystem
- [Cipher IAM Extensions README](../subsystems/cipher-iam-extensions/README.md) — Subsystem overview
- [Architecture](../subsystems/cipher-iam-extensions/architecture.md) — Hub Cipher IAM relationship, agent identity types
- [Agent Profile API](../subsystems/cipher-iam-extensions/agent-profile-api.md) — API specification, endpoints
- [Authority Delegation](../subsystems/cipher-iam-extensions/authority-delegation.md) — Delegation model, inheritance algorithms
- [Profile Tags](../subsystems/cipher-iam-extensions/profile-tags.md) — Raw/Trained/Employed agent profile tags
- [Credential Management](../subsystems/cipher-iam-extensions/credential-management.md) — Credential issuance, injection, virtual keys
- [Policy Enforcement Points](../subsystems/cipher-iam-extensions/policy-enforcement-points.md) — PEP registration, policy evaluation

### Related Systems
- [Agent Lifecycle](../implementation-concepts/agent-lifecycle.md) — Lifecycle integration
- [Authority Enforcement](../implementation-concepts/authority-enforcement.md) — Enforcement concepts
- [Hub Cipher IAM](../../../olympus-hub-docs/04-subsystems/cipher-iam/README.md) — Core Cipher IAM
- [ADR-0106: Cipher IAM Extensions for Agent Profiles](../../../olympus-hub-docs/decision-logs/0106-seer-cipher-iam-extensions-agent-profiles.md) — Architecture decision

---

*For detailed implementation, see [Cipher IAM Extensions README](../subsystems/cipher-iam-extensions/README.md).*
