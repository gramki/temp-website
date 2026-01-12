# ADR-0106: Cipher IAM Extensions Agent Profile Architecture

**Status**: Accepted  
**Date**: 2026-01-12  
**Authors**: Architecture Team

---

## Context

Seer agents require identity and authority management that integrates with Hub's existing Cipher IAM system. Key requirements:

1. Agents need unique identities with SPIFFE integration
2. Authority must be delegated from humans or roles
3. Every agent must have an accountable human
4. Policies must be enforced per Policy Enforcement Point
5. Credentials must be securely issued and managed

Two approaches were considered:

1. **Separate IAM System**: Build a standalone agent identity system
2. **Cipher IAM Extensions**: Extend Hub Cipher IAM with agent-specific semantics

---

## Decision

**Agent identity is managed through Cipher IAM Extensions, which extends Hub Cipher IAM with agent-specific semantics.**

### Key Design Elements

1. **Three Agent Identity Types**: Raw, Trained, Employed
2. **Authority Delegation**: User delegation, role delegation, or bot mode
3. **Mandatory Accountability**: Every agent has an accountable human
4. **Per-PEP Policies**: Policies configured per Policy Enforcement Point
5. **Credential Management**: Virtual keys, tokens, and SVIDs

---

## Rationale

### Benefits of Extension Approach

| Benefit | Description |
|---------|-------------|
| **Unified IAM** | Single identity system for users and agents |
| **Leverage Infrastructure** | Reuse SPIFFE, OPA, credential management |
| **Consistent Governance** | Same policy model across Hub |
| **Audit Integration** | Unified audit trail in CAF |

### Division of Responsibilities

| Responsibility | Owner |
|----------------|-------|
| Agent-specific semantics (profiles, delegation) | Seer (Cipher IAM Extensions) |
| Identity infrastructure (SPIFFE, OPA) | Hub Cipher IAM |
| API surface for agent profiles | Cipher IAM Extensions |
| Core credential issuance | Hub Cipher IAM |

---

## Consequences

### Positive

- Unified identity management
- Reuse of proven IAM infrastructure
- Consistent security model
- Integrated audit trail

### Negative

- Dependency on Hub Cipher IAM
- Extensions must be coordinated with Core IAM team

### Neutral

- Agent profiles stored in Cipher IAM database
- Seer Operator is primary API client

---

## Implementation Details

### Profile Lifecycle

```
EmploymentSpec Created
        │
        ▼
Seer Operator calls Cipher IAM Extensions API
        │
        ▼
Create Agent Profile with:
  - SPIFFE identity
  - Delegation chain
  - Inherited roles/groups
  - Per-PEP policies
  - Virtual key
        │
        ▼
Agent pods deployed with credentials
```

### Authority Inheritance Algorithm

1. If roles/groups = `*`, inherit all from delegator
2. If CSV, compute intersection with delegator's roles/groups
3. Unavailable items generate warnings (not errors)
4. Profile still created with available subset

### Unknown PEP Handling

- Unknown PEPs in policy configuration are **ignored**
- Warning is logged, profile creation continues
- Graceful degradation ensures forward compatibility

---

## Related Documentation

- [Cipher IAM Extensions Design](../../olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/README.md)
- [Hub Cipher IAM](../04-subsystems/cipher-iam/README.md)
- [Authority Enforcement Concepts](../../olympus-seer-docs/seer-design/implementation-concepts/authority-enforcement.md)
