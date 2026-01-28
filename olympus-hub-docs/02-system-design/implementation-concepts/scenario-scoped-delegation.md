# Scenario-Scoped Delegation (Hub Perspective)

> **Category:** Agent Delegation  
> **Status:** 🟢 Design Complete  
> **Last Updated:** 2026-01-21  
> **Authoritative Source:** [Scenario-Scoped Delegation (Seer)](../../../olympus-seer-docs/seer-design/implementation-concepts/scenario-scoped-delegation.md)

---

## Overview

Scenario-Scoped Delegation enables Employed Agents to act with **stable, enterprise-granted authority** derived from a Scenario Identity Profile. Authority is established at deployment time and remains valid for the employment lifetime.

This document describes the Hub-side components and patterns; for the complete design, see the authoritative Seer documentation linked above.

---

## Purpose

| Need | How Scenario-Scoped Addresses It |
|------|----------------------------------|
| **Operational continuity** | Authority persists across requests; no per-request consent |
| **Enterprise processes** | Authority from Scenario Identity Profile, not individual users |
| **Consistent behavior** | Same authority for all requests handled by the agent |
| **Audit traceability** | Actions attributed to Scenario Identity Profile |

**Typical Use Cases:**
- Dispute resolution agents
- Fraud detection and monitoring
- Document processing workflows
- Any enterprise automation with stable authority

---

## Contrast with Other Delegation Types

| Aspect | Scenario-Scoped | Request-Scoped | Enterprise (User/Role/Bot) |
|--------|-----------------|----------------|---------------------------|
| **Purpose** | Long-lived operational agents | Temporary, user-initiated tasks | Internal operator delegation |
| **Authority Source** | Scenario Identity Profile | Business User consent | Enterprise IAM |
| **Certificate Timing** | At deployment | Per-request | N/A (direct inheritance) |
| **Token Timing** | Per-request | Per-request | N/A |
| **Authority Sync** | Eventual consistency | Eventual consistency | Real-time |
| **Accountability** | Layered: Scenario Profile + Enterprise | Layered: Business User + Enterprise | Designated accountable human |
| **User Interaction** | None required | Consent via Channel | None required |
| **Typical Agent** | Enterprise automation | Customer-facing assistant | Employee assistant |

**Note on Layered Accountability:** The Scenario Identity Profile is accountable for actions authorized under the delegation, while the enterprise (via designated accountable human) remains accountable for the agent's behavior itself.

---

## Hub Components Involved

| Component | Role in Scenario-Scoped Delegation |
|-----------|-----------------------------------|
| **Signal Exchange** | Fetches certificate from deployment context; issues fresh tokens per REQUEST_UPDATE |
| **Request Lifecycle Manager** | Stores deployment delegation context |
| **Scenario Registry** | Provides Identity Profile reference for the Scenario |
| **ScenarioDeploymentSpec** | References delegation configuration from EmploymentSpec |

---

## How It Works

### Certificate Lifecycle

```
Deployment Time (One-Time):
┌─────────────────────────────────────────────────────────────────────┐
│  1. Scenario deployed with Identity Profile                         │
│  2. EmploymentSpec specifies mode: "scenario-scoped"                │
│  3. Cipher creates Delegation Certificate from Scenario Profile     │
│  4. Certificate stored, referenced in deployment context            │
└─────────────────────────────────────────────────────────────────────┘

Per-Request (Every REQUEST_UPDATE):
┌─────────────────────────────────────────────────────────────────────┐
│  1. Signal Exchange receives REQUEST_UPDATE for agent               │
│  2. Fetches Certificate from deployment context                     │
│  3. Requests fresh Delegation Access Token from Cipher              │
│  4. Places token in environment.auth.delegations                    │
│  5. Delivers REQUEST_UPDATE with refreshed token                    │
└─────────────────────────────────────────────────────────────────────┘
```

### Token Refresh Behavior

Signal Exchange refreshes tokens on **every** REQUEST_UPDATE delivery:

1. Get Certificate from deployment delegation context
2. Verify Certificate not revoked/expired
3. Issue fresh Delegation Access Token from Certificate
4. Place in `environment.auth.delegations`

This ensures:
- Short-lived tokens (security)
- Certificate revocations reflected immediately
- No stale authority persists

---

## Token Placement

Tokens appear in the message envelope:

```yaml
environment:
  auth:
    identity:
      spiffeId: "spiffe://seer/agents/dispute-resolver"
      delegationMode: "scenario-scoped"
    
    delegations:
      - token: "eyJ..."
        template: "analyze-disputes"
        delegator: "dispute-resolution-profile"
        expiresAt: "2026-01-21T23:00:00Z"
```

| Field | Description |
|-------|-------------|
| `delegationMode` | Indicates scenario-scoped (vs request-scoped) |
| `delegations` | Array of active delegation tokens |
| `delegator` | Scenario Identity Profile (not a business user) |

---

## ScenarioDeploymentSpec Integration

The deployment spec references delegation configuration:

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioDeploymentSpec
metadata:
  name: dispute-resolution-prod
spec:
  scenarioRef:
    name: dispute-resolution
    
  # Employment reference (includes delegation config)
  employmentRef:
    name: dispute-resolver-employment
    
  # Delegation mode inherited from EmploymentSpec
  # mode: scenario-scoped
  # allowedTemplates: [analyze-disputes, ...]
```

---

## No Channel Involvement

Unlike request-scoped delegation, scenario-scoped delegation **does not involve Channels**:

| Aspect | Scenario-Scoped | Request-Scoped |
|--------|-----------------|----------------|
| **Consent Capture** | Not needed (enterprise grants at deployment) | Required (user grants via Channel) |
| **AUTHORITY_REQUEST** | Not used | Used when agent needs authority mid-execution |
| **AUTHORITY_GRANTED** | Not used | Channel sends after user consent |
| **Channel as Observer** | Not relevant | Critical for delegation flow |

Scenario-scoped delegation is **proactive only** — authority is granted before any request arrives.

---

## Integration Points

| Hub Component | Integration |
|---------------|-------------|
| [Signal Exchange](../../04-subsystems/signal-exchange/delegation-handling.md) | Token refresh on delivery |
| [Request Management](../../04-subsystems/request-management/delegation-context.md) | Context storage |
| [Scenario Registry](../../04-subsystems/workbench-management/scenario-definitions.md) | Identity Profile reference |
| [Agent Delegation](./agent-delegation.md) | Umbrella concept |

---

## Related Documentation

### Mode Comparison

| Concept | Description |
|---------|-------------|
| [Agent Delegation](./agent-delegation.md) | Umbrella concept; unified model overview |
| [Request-Scoped Delegation](./request-scoped-delegation.md) | Alternative mode with per-request user consent |

### Authoritative Source

- [Scenario-Scoped Delegation (Seer)](../../../olympus-seer-docs/seer-design/implementation-concepts/scenario-scoped-delegation.md) — Complete design

### Decision Records

| ADR | Decision |
|-----|----------|
| [ADR-0130](../../decision-logs/0130-unified-delegation-model.md) | Unified Delegation Model |
| [ADR-0129](../../decision-logs/0129-agent-identity-model.md) | Agent Identity Model |

---

*This document provides the Hub perspective on scenario-scoped delegation. For the complete design including Cipher, Employment Spec, and Seer components, see the authoritative Seer documentation.*
