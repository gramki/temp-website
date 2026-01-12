# Cipher IAM Extensions - Scope and Design Status

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Scope

The **Cipher IAM Extensions** subsystem extends Hub Cipher IAM to support agent-specific identity and authority management. It is responsible for:

1. **Agent Profiles** — Raw, Trained, and Employed agent identity types
2. **Authority Delegation** — Delegation from users/roles with inheritance
3. **Human Accountability** — Mandatory accountable human for every agent
4. **Per-PEP Policies** — Policy configuration per Policy Enforcement Point
5. **Credential Management** — Virtual keys, tokens, and SVID issuance

---

## Intended Depth

This design documentation is at **C2 (Container) level** with **C3 (Component) detail** for critical mechanisms:

| Aspect | Coverage |
|--------|----------|
| **Functional Scope** | Complete — what each component does |
| **Integration Points** | Complete — hand-offs between containers |
| **Conceptual Models** | Complete — illustrated with examples |
| **C3 Detail Areas** | Complete — API, delegation algorithms, policy evaluation |
| **Data Models** | Conceptual only — no detailed schemas |
| **API Specifications** | Conceptual with examples — not formal OpenAPI |

### C3 Detail Areas

The following areas are documented at C3 (Component) level:

| Area | Document | Details |
|------|----------|---------|
| **Agent Profile API** | agent-profile-api.md | Endpoints, schemas, error handling |
| **Authority Inheritance** | authority-delegation.md | Role/group inheritance algorithms |
| **Policy Evaluation** | policy-enforcement-points.md | PEP evaluation flow, precedence |

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [README.md](./README.md) | Overview, architecture, design summary | ✅ Complete |
| [architecture.md](./architecture.md) | Hub Cipher IAM relationship, SPIFFE | ✅ Complete |
| [agent-profile-api.md](./agent-profile-api.md) | API specification (C3) | ✅ Complete |
| [authority-delegation.md](./authority-delegation.md) | Delegation model, algorithms (C3) | ✅ Complete |
| [profile-tags.md](./profile-tags.md) | Profile tag structure | ✅ Complete |
| [human-accountability.md](./human-accountability.md) | Accountability requirements | ✅ Complete |
| [policy-enforcement-points.md](./policy-enforcement-points.md) | PEP registration, evaluation (C3) | ✅ Complete |
| [credential-management.md](./credential-management.md) | Credential lifecycle | ✅ Complete |
| [internal-implementation.md](./internal-implementation.md) | Storage, policy attachment | ✅ Complete |
| [integration-patterns.md](./integration-patterns.md) | Seer component integration | ✅ Complete |

---

## Coverage Summary

### ✅ Architecture (architecture.md)
- Extension model (extends, not replaces)
- Three agent identity types
- SPIFFE integration and SVID issuance
- Division of responsibilities with Hub Cipher IAM

### ✅ Agent Profile API (agent-profile-api.md)
- **C3**: Endpoint specifications
- **C3**: Request/response schemas
- **C3**: Error handling and validation flow

### ✅ Authority Delegation (authority-delegation.md)
- Delegation types (user, role, bot)
- Delegation chain structure
- **C3**: Role inheritance algorithm
- **C3**: Group inheritance algorithm
- **C3**: Wildcard and CSV handling

### ✅ Profile Tags (profile-tags.md)
- Raw Agent tags
- Trained Agent tags
- Employed Agent tags
- Tag lifecycle

### ✅ Human Accountability (human-accountability.md)
- Mandatory accountable human
- Accountability chain
- Manager relationship
- Audit trail requirements

### ✅ Policy Enforcement Points (policy-enforcement-points.md)
- Registered PEPs
- Policy attachment per agent
- Unknown PEP handling
- **C3**: Policy evaluation flow
- **C3**: Policy precedence

### ✅ Credential Management (credential-management.md)
- Credential types
- Virtual key lifecycle
- Credential injection
- Rotation and revocation

### ✅ Internal Implementation (internal-implementation.md)
- Profile storage (PostgreSQL + Redis)
- Delegation chain storage
- Policy attachment mechanisms
- Core IAM integration

### ✅ Integration Patterns (integration-patterns.md)
- Seer Operator integration
- Agent Runtime integration
- PEP integration patterns
- Error handling patterns

---

## Key Design Decisions

1. **Extensions to Hub Cipher IAM** — Not a replacement, but extensions with agent-specific semantics
2. **Three Agent Identity Types** — Raw, Trained, Employed with increasing authority
3. **Mandatory Human Accountability** — Every agent must have an accountable human
4. **Per-PEP Policies** — Policies are configured per Policy Enforcement Point
5. **Unknown PEP Handling** — Unknown PEPs are ignored with warnings (graceful degradation)

---

## Implementation Details Deferred

The following implementation details are deferred to the detailed implementation stage:

| Area | Deferred Details |
|------|------------------|
| **Database Schema** | Exact column types, indexes, constraints |
| **Cache TTLs** | Specific cache duration values |
| **SPIRE Configuration** | Detailed SPIRE agent configuration |

These will be addressed during implementation with common defaults applied.

---

## Related Subsystems

- **[Agent Runtime](../agent-runtime/README.md)** — Credential injection, runtime authentication
- **[Model Gateway](../model-gateway/README.md)** — Virtual key consumption, policy enforcement
- **[Agent Ingress Gateway](../agent-ingress-gateway/README.md)** — sx-observer authentication
- **[Seer Operator](../seer-operator/README.md)** — Profile provisioning

---

## Related Documentation

- [Hub Cipher IAM](../../../../olympus-hub-docs/04-subsystems/cipher-iam/README.md) — Core Cipher IAM
- [Agent Lifecycle](../../implementation-concepts/agent-lifecycle.md) — Lifecycle integration
- [Authority Enforcement](../../implementation-concepts/authority-enforcement.md) — Enforcement concepts

---

*This scope document reflects the completed detailed design of the Cipher IAM Extensions subsystem.*
