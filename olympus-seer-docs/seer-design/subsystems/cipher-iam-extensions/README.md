# Cipher IAM Extensions

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

## Overview

Cipher IAM Extensions extends the Hub Cipher IAM system to support agent-specific identity and authority management. It provides the IAM foundation for agent identity, authority delegation, and policy enforcement.

**Key Characteristics:**
- Extensions to Hub Cipher IAM (not replacement)
- Supports Raw, Trained, and Employed Agent identity types
- Authority delegation with human accountability
- Per-PEP policy enforcement

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     CIPHER IAM EXTENSIONS ARCHITECTURE                       │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                        SEER COMPONENTS                               │   │
│   │                                                                       │   │
│   │   ┌───────────┐   ┌───────────┐   ┌───────────┐                     │   │
│   │   │   Seer    │   │  Agent    │   │   PEPs    │                     │   │
│   │   │ Operator  │   │  Runtime  │   │ (Gateway) │                     │   │
│   │   └─────┬─────┘   └─────┬─────┘   └─────┬─────┘                     │   │
│   │         │               │               │                            │   │
│   └─────────┼───────────────┼───────────────┼────────────────────────────┘   │
│             │               │               │                                │
│             │ Profile API   │ Credential    │ Policy                        │
│             │               │ Injection     │ Evaluation                    │
│             ▼               ▼               ▼                                │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                 CIPHER IAM EXTENSIONS                                │   │
│   │                                                                       │   │
│   │   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │   │
│   │   │  Agent Profile  │  │    Authority    │  │      Policy     │     │   │
│   │   │      API        │  │    Delegation   │  │   Enforcement   │     │   │
│   │   └─────────────────┘  └─────────────────┘  └─────────────────┘     │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│             │                                                                │
│             │ Extends                                                        │
│             ▼                                                                │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                     HUB CIPHER IAM (Core)                            │   │
│   │                                                                       │   │
│   │   • Identity Management    • Role/Group Management                   │   │
│   │   • SPIFFE Integration     • OPA Policy Engine                       │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Architecture](./architecture.md) | Hub Cipher IAM relationship, agent identity types, SPIFFE | ✅ Complete |
| [Agent Profile API](./agent-profile-api.md) | API specification, endpoints, schemas (C3) | ✅ Complete |
| [Authority Delegation](./authority-delegation.md) | Delegation model, inheritance algorithms (C3) | ✅ Complete |
| [Profile Tags](./profile-tags.md) | Raw/Trained/Employed agent profile tags | ✅ Complete |
| [Human Accountability](./human-accountability.md) | Accountable human assignment, audit trail | ✅ Complete |
| [Policy Enforcement Points](./policy-enforcement-points.md) | PEP registration, policy evaluation (C3) | ✅ Complete |
| [Credential Management](./credential-management.md) | Credential issuance, injection, virtual keys | ✅ Complete |
| [Internal Implementation](./internal-implementation.md) | Profile storage, policy attachment | ✅ Complete |
| [Integration Patterns](./integration-patterns.md) | Seer Operator, Agent Runtime integration | ✅ Complete |
| [SCOPE.md](./SCOPE.md) | Coverage summary, design status | ✅ Complete |

---

## Key Design Decisions

### Extensions to Hub Cipher IAM
- Cipher IAM Extensions **extends** Hub Cipher IAM, not replaces
- Seer defines agent-specific semantics; Cipher provides infrastructure
- Leverages existing IAM capabilities (SPIFFE, OPA, etc.)

### Agent Profile Types
- **Raw Agent Profile** — Base capabilities, no delegation
- **Trained Agent Profile** — Trained capabilities, potential delegation constraints
- **Employed Agent Profile** — Full identity with delegation chain and policies

### Authority Delegation Model
- **User Delegation** — Agent acts on behalf of a specific user
- **Role Delegation** — Agent inherits from a role
- **Bot Mode** — Agent has base identity only, no delegation

### Policies Per PEP
- Policies are **per Policy Enforcement Point** (not global)
- Unknown PEPs are **ignored** (graceful degradation)
- Policies are **referenced files** (not inline)

---

## Related Subsystems

| Subsystem | Relationship |
|-----------|-------------|
| [Agent Runtime](../agent-runtime/README.md) | Credential injection, profile consumption |
| [Model Gateway](../model-gateway/README.md) | Virtual key management, policy enforcement |
| [Agent Ingress Gateway](../agent-ingress-gateway/README.md) | sx-observer authentication |
| [Seer Operator](../seer-operator/README.md) | Profile provisioning API calls |

---

## Related Documentation

- [Hub Cipher IAM](../../../../olympus-hub-docs/04-subsystems/cipher-iam/README.md) — Core Cipher IAM
- [Agent Lifecycle](../../implementation-concepts/agent-lifecycle.md) — Lifecycle integration
- [Authority Enforcement](../../implementation-concepts/authority-enforcement.md) — Enforcement concepts
- [Delegation Chains](../../why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-2-delegation-chains.md) — Delegation model

---

*Cipher IAM Extensions provides comprehensive identity and authority management for Seer agents, extending Hub Cipher IAM with agent-specific semantics.*
