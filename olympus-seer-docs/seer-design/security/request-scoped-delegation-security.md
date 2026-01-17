# Request-Scoped Delegation: Security Considerations

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-17  
> **Related**: [Request-Scoped Authority Delegation](../implementation-concepts/request-scoped-delegation.md)

---

## Overview

This document outlines security considerations, threat models, and mitigations for Request-Scoped Authority Delegation. The system enables business users to delegate authority to agents, introducing new attack surfaces that must be addressed.

---

## 1. Threat Model

### 1.1 Actors

| Actor | Description | Trust Level |
|-------|-------------|-------------|
| Business User | End-user delegating authority | Authenticated, trusted |
| Employed Agent | Agent receiving delegation | Partially trusted (constrained) |
| Malicious Agent | Compromised or rogue agent | Untrusted |
| External Attacker | Network-based attacker | Untrusted |
| Insider Threat | Malicious bank employee | Partially trusted |

### 1.2 Assets

| Asset | Sensitivity | Impact of Compromise |
|-------|-------------|----------------------|
| Delegation Access Token | High | Unauthorized actions on behalf of user |
| Delegation Certificate | High | Long-term authority grant |
| Business User Profile | Medium | PII exposure |
| Delegation Template | Low | Scope definition (not secret) |

### 1.3 Threat Categories

#### T1: Token Theft and Misuse
- **Threat**: Attacker steals Delegation Access Token and uses it from different context
- **Likelihood**: Medium
- **Impact**: High
- **Mitigation**: 
  - Token bound to specific agent SPIFFE ID
  - Short-lived tokens (5-15 minute expiry)
  - Token validation at every PEP
  - Revocation propagation on compromise detection

#### T2: Consent Manipulation
- **Threat**: User tricked into granting excessive delegation
- **Likelihood**: Medium
- **Impact**: High
- **Mitigation**:
  - Clear, human-readable Delegation Template descriptions
  - Mandatory consent UI with explicit approve/deny
  - Audit trail of all consent decisions
  - Template review by tenant admins

#### T3: Privilege Escalation via Chaining
- **Threat**: Agent chains delegation to grant more authority than it received
- **Likelihood**: Low
- **Impact**: High
- **Mitigation**:
  - Chaining only allowed if `chainingAllowed: true` in Certificate
  - Child scope must be strict subset of parent scope
  - Cipher IAM validates scope narrowing on chain creation

#### T4: Authority Request Flooding
- **Threat**: Agent floods user with Authority Requests to exhaust attention
- **Likelihood**: Medium
- **Impact**: Medium
- **Mitigation**:
  - Rate limiting on Authority Requests per agent/user/session
  - Timeout for unresponded requests
  - User can block agent from further requests

#### T5: Certificate Revocation Bypass
- **Threat**: Revoked certificate continues to be used
- **Likelihood**: Low
- **Impact**: High
- **Mitigation**:
  - Real-time revocation propagation to all PEPs
  - Short token lifetime limits exposure window
  - Token refresh checks certificate status

#### T6: Business User Identity Spoofing
- **Threat**: Attacker impersonates business user to grant delegation
- **Likelihood**: Low
- **Impact**: Critical
- **Mitigation**:
  - Federation with trusted external IdPs
  - MFA enforcement during delegation consent
  - Session binding for certificates
  - Anomaly detection on delegation patterns

---

## 2. Security Controls

### 2.1 Token Security

| Control | Implementation |
|---------|----------------|
| **Token Binding** | Each token bound to single agent SPIFFE ID |
| **Short Lifetime** | Default 5-15 minutes; max 1 hour |
| **Token Refresh** | Signal Exchange refreshes tokens before expiry |
| **JWT Signature** | RS256 with Cipher IAM key rotation |
| **No Token Storage** | Tokens not persisted; derived from Certificates on demand |

### 2.2 Certificate Security

| Control | Implementation |
|---------|----------------|
| **Immutability** | Certificate core properties immutable after issuance |
| **Scope Narrowing** | User can narrow but not expand template constraints |
| **Revocation** | Immediate revocation with propagation to all PEPs |
| **Expiry** | Configurable expiry, max from template's `maxValidityDuration` |
| **Session Binding** | Optional `sessionScoped: true` ties to user session |

### 2.3 Consent Security

| Control | Implementation |
|---------|----------------|
| **Explicit Consent** | All delegations require explicit user action |
| **Informed Consent** | Template `displayName` and `description` shown to user |
| **MFA Option** | `requiresMFAAtDelegation: true` enforces MFA |
| **Audit Trail** | All consent decisions logged to CAF |
| **Revocation UI** | Users can view and revoke active delegations |

### 2.4 Policy Enforcement

| Control | Implementation |
|---------|----------------|
| **Composition** | All policies (Training, Employment, Template) must ALLOW |
| **PEP Validation** | Every PEP validates token before action |
| **Early Rejection** | Sidecar rejects unauthorized actions before downstream call |
| **OPA Policies** | Fine-grained policies embedded in templates |

---

## 3. Audit and Compliance

### 3.1 Audit Events

All delegation-related events are logged to Central Audit Fabric (CAF):

| Event Type | Data Captured |
|------------|---------------|
| `DELEGATION_TEMPLATE_CREATED` | Template ID, creator, permissions |
| `DELEGATION_CERTIFICATE_ISSUED` | Certificate ID, delegator, delegate, template, expiry |
| `DELEGATION_CERTIFICATE_REVOKED` | Certificate ID, revoker, reason |
| `DELEGATION_TOKEN_ISSUED` | Token ID, certificate, agent, expiry |
| `AUTHORITY_REQUEST_SENT` | Request ID, agent, template, reason |
| `AUTHORITY_REQUEST_GRANTED` | Request ID, user, certificate |
| `AUTHORITY_REQUEST_DENIED` | Request ID, user, reason |
| `DELEGATION_ACTION_PERFORMED` | Token ID, action, resource, outcome |
| `DELEGATION_ACTION_BLOCKED` | Token ID, action, policy violation |

### 3.2 Compliance Considerations

| Regulation | Requirement | How Addressed |
|------------|-------------|---------------|
| **GDPR** | Explicit consent, right to withdraw | Consent UI, revocation, data minimization |
| **PCI-DSS** | Access control, audit trails | Token scoping, PEP enforcement, CAF logging |
| **SOC 2** | Security, availability, confidentiality | Encryption, redundancy, access controls |
| **FFIEC** | Third-party risk, customer auth | MFA, identity federation, policy enforcement |

---

## 4. Incident Response

### 4.1 Token Compromise

**Detection**: Anomalous token usage patterns, geographic anomalies, rate anomalies

**Response**:
1. Revoke associated Delegation Certificate immediately
2. Invalidate all derived tokens
3. Notify affected business user
4. Review agent behavior for other compromises
5. Generate incident report

### 4.2 Mass Certificate Revocation

**Trigger**: Security incident requiring bulk revocation

**Process**:
1. Identify affected certificates by template, delegate, or delegator
2. Execute bulk revocation via Cipher IAM API
3. Propagate revocation to all PEPs
4. Notify affected users and agents
5. Audit downstream impacts

### 4.3 Template Vulnerability

**Detection**: Template allows unintended authority

**Response**:
1. Deprecate vulnerable template
2. Revoke certificates issued against template
3. Issue new corrected template
4. Re-consent affected users
5. Review template approval process

---

## 5. Security Testing Requirements

| Test Category | Scope |
|---------------|-------|
| **Token Validation** | Verify tokens rejected when expired, wrong agent, revoked |
| **Scope Enforcement** | Verify actions outside scope are blocked |
| **Chaining Validation** | Verify chaining only allowed when permitted |
| **Revocation Propagation** | Verify revocation reaches all PEPs within SLA |
| **Consent Flow** | Verify consent cannot be bypassed |
| **Rate Limiting** | Verify Authority Request rate limits work |
| **Penetration Testing** | Token theft, privilege escalation, consent manipulation |

---

## Related Documentation

- [Request-Scoped Authority Delegation](../implementation-concepts/request-scoped-delegation.md)
- [Cipher IAM Extensions](../subsystems/cipher-iam-extensions/README.md)
- [Policy Enforcement Points](../subsystems/cipher-iam-extensions/policy-enforcement-points.md)
- [Central Audit Fabric](../../olympus-hub-docs/04-subsystems/central-audit-fabric/README.md)
