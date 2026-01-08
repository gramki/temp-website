# Agent Identity & Authority Framework

> **Status**: ⬜ Placeholder — Depends on Cipher IAM design  
> **Last Updated**: 2026-01-08

## Overview

The Agent Identity & Authority Framework provides **verifiable identity** and **explicit authority** for agents, integrating with Cipher for identity management.

## Scope

| Capability | Description |
|------------|-------------|
| **Agent Identity** | Unique, cryptographically verifiable agent identifiers |
| **Identity Lifecycle** | Create, rotate, revoke agent credentials |
| **Authority Definition** | Explicit statement of what agent can do |
| **Delegation Chain** | Who delegated authority to this agent? |
| **Ceiling Enforcement** | Hard limits on agent actions |
| **Authority Audit** | Immutable log of all delegation changes |

## Key Principles

- Agents have distinct identity from users and systems
- Authority is explicitly delegated, never assumed
- Delegated authority ≤ delegator's current authority (real-time)
- A human must always be Accountable (AOSM RASCI)

## Cipher Integration

- Seer defines the framework; Cipher provides identity infrastructure
- Raw Agents: Infrastructure identity (SPIFFE)
- Trained Agents: Application identity
- Employed Agents: Workforce/Customer IAM identity

## Related

- [Introduction](../introduction.md)
- [Raw, Trained, Employed Agents](../../../aosm-meta-model/raw-trained-employed-agents.md)

---

*TODO: Detailed design*

