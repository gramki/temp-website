# Request-Scoped Delegation (Hub Perspective)

> **Category:** Agent Delegation  
> **Status:** 🟢 Design Complete  
> **Last Updated:** 2026-01-21  
> **Authoritative Source:** [Request-Scoped Delegation (Seer)](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)

---

## Overview

Request-Scoped Delegation enables Employed Agents to act on behalf of **business users** (customers, external employees) with **temporary, task-bounded authority**. Authority is granted per-request when a user consents via a Channel.

This document describes the Hub-side components and patterns; for the complete design, see the authoritative Seer documentation linked above.

---

## Purpose

| Need | How Request-Scoped Addresses It |
|------|--------------------------------|
| **Temporary authority** | Authority expires when request completes; no lingering permissions |
| **User consent** | Business user explicitly grants permission per-task |
| **Task isolation** | Authority scoped to specific request; doesn't affect other work |
| **Customer trust** | Users control what agents can do on their behalf |

**Primary Use Cases:**
- Personal finance AI paying bills for a customer
- Family banking assistant transferring money
- Expense approval bot acting on behalf of employees
- Any customer-facing agent requiring explicit consent

---

## Contrast with Other Delegation Types

| Aspect | Request-Scoped | Scenario-Scoped | Enterprise (User/Role/Bot) |
|--------|----------------|-----------------|---------------------------|
| **Purpose** | Temporary, user-initiated tasks | Long-lived operational agents | Internal operator delegation |
| **Authority Source** | Business User consent | Scenario Identity Profile | Enterprise IAM |
| **Certificate Timing** | Per-request | At deployment | N/A (direct inheritance) |
| **Token Timing** | Per-request | Per-request | N/A |
| **Authority Sync** | Eventual consistency | Eventual consistency | Real-time |
| **Accountability** | Layered: Business User + Enterprise | Layered: Scenario Profile + Enterprise | Designated accountable human |
| **User Interaction** | Consent via Channel | None required | None required |
| **Typical Agent** | Customer-facing assistant | Enterprise automation | Employee assistant |

**Note on Layered Accountability:** The business user (delegator) is accountable for actions they authorized, while the enterprise (via designated accountable human) remains accountable for the agent's behavior itself.

---

## Hub Components Involved

| Component | Role in Delegation |
|-----------|-------------------|
| **Channel** | Orchestrates consent flow, requests certificates/tokens from Cipher, handles AUTHORITY_REQUEST |
| **Signal Exchange** | Routes AUTHORITY_REQUEST/GRANTED, refreshes tokens on delivery |
| **Request Lifecycle Manager** | Stores delegation context per request |
| **Observer Modules** | Channels receive REQUEST_UPDATEs as observers |

---

## Signal Provider vs Channel: Critical Distinction

A key architectural boundary for delegation:

| Aspect | Signal Provider (I/O Gateway) | Channel |
|--------|-------------------------------|---------|
| **Purpose** | Signal ingestion (events, files, API calls) | User interaction interface |
| **Direction** | Primarily inbound; may send responses | Fully bidirectional |
| **User Presence** | No user context; machine-to-machine | User is present and can interact |
| **Delegation Role** | **Cannot delegate** — just forwards signals | **Can facilitate delegation** — captures consent, presents UI |
| **Examples** | Atropos (events), Dia (files), Kale (scheduler), Cronus | Web Console, MS Teams, MCP, REST API |

### Why This Matters

1. **Signal Providers have no user identity context** — they normalize and forward signals but cannot grant authority
2. **Channels interact with authenticated users** — users can grant or deny delegation
3. **Only Channels can**:
   - Present consent UI for AUTHORITY_REQUEST
   - Attach Delegation Certificates to Requests
   - Implicitly fulfill from existing certificates

---

## REQUEST_UPDATE Sub-Types for Delegation

Two new sub-types extend the REQUEST_UPDATE mechanism:

### AUTHORITY_REQUEST

Sent by agent (via sidecar) when it needs authority:

```json
{
  "update": {
    "update_type": "AUTHORITY_REQUEST",
    "sequence": 5
  },
  "payload": {
    "authority_request": {
      "request_id": "auth-req-67890",
      "template": "personal-finance-assistant",
      "agent_id": "spiffe://seer/agents/my-assistant",
      "reason": "Need to initiate payment on user's behalf",
      "timeout": "PT5M"
    }
  }
}
```

### AUTHORITY_GRANTED

Sent by Channel after obtaining consent:

```json
{
  "update": {
    "update_type": "AUTHORITY_GRANTED",
    "sequence": 6
  },
  "payload": {
    "authority_granted": {
      "request_id": "auth-req-67890",
      "certificate_id": "cert-11111",
      "template": "personal-finance-assistant",
      "delegator": "user-67890",
      "expires_at": "2026-01-17T22:00:00Z"
    }
  }
}
```

### AUTHORITY_DENIED

Sent by Channel when delegation is denied or times out:

```json
{
  "update": {
    "update_type": "AUTHORITY_DENIED",
    "sequence": 6
  },
  "payload": {
    "authority_denied": {
      "request_id": "auth-req-67890",
      "template": "personal-finance-assistant",
      "reason": "user_denied"
    }
  }
}
```

---

## environment.auth.delegations

Signal Exchange places delegation tokens in the message envelope:

```yaml
environment:
  auth:
    identity:
      spiffeId: "spiffe://seer/agents/my-agent"
      delegationMode: "deferred"
    
    delegations:
      - token: "eyJ..."
        template: "personal-finance-assistant"
        delegator: "user-67890"
        expiresAt: "2026-01-17T22:00:00Z"
```

### Token Refresh Behavior

Signal Exchange **refreshes** tokens on every REQUEST_UPDATE delivery to an agent:

1. Get certificates from Request delegation context
2. Filter revoked/expired certificates
3. Issue fresh Delegation Access Token per agent
4. Place in `environment.auth.delegations`

---

## Channel Responsibilities

Channels (as observer modules) handle delegation flows:

### Proactive Delegation

User grants before agent needs:
1. User initiates via Channel UI
2. Channel obtains Delegation Certificate from Cipher
3. Channel attaches Certificate to Request context

### Reactive Delegation

Agent requests mid-execution:
1. Agent posts AUTHORITY_REQUEST (via sidecar)
2. Signal Exchange routes to observers
3. Channel receives, checks for existing certificate
4. If found: implicit fulfillment → AUTHORITY_GRANTED
5. If not found: prompt user → consent or deny

### Implicit Fulfillment

```python
async def handle_authority_request(notification: ObserverNotification):
    """Channel handling AUTHORITY_REQUEST."""
    
    auth_request = notification.payload.authority_request
    
    # Check for existing valid certificate
    existing_cert = await find_matching_certificate(
        user_id=notification.request.subject.id,
        template=auth_request.template,
        delegate_pattern=auth_request.agent_role
    )
    
    if existing_cert:
        # Implicit fulfillment - no user prompt needed
        await post_authority_granted(
            request_id=notification.request.id,
            certificate_id=existing_cert.id
        )
    else:
        # Need user consent
        await prompt_user_for_consent(notification)
```

---

## Cascading via Request Hierarchy

When a child request needs authority and no user is present at the child Channel, the authority request can cascade to the parent:

```
Parent Request (user present at Channel)
    │
    ├── Child Request (agent-to-agent, no user)
    │       │
    │       └── AUTHORITY_REQUEST ──▶ No user present
    │                                      │
    │       ◀── CASCADE TO PARENT ─────────┘
    │
    └── Channel prompts user
            │
            └── AUTHORITY_GRANTED cascades down
```

This follows the same pattern as lifecycle cascade in Request Hierarchy.

---

## Integration Points

| Hub Component | Integration |
|---------------|-------------|
| [Signal Exchange](../../04-subsystems/signal-exchange/delegation-handling.md) | Token refresh, update routing |
| [Request Management](../../04-subsystems/request-management/delegation-context.md) | Context storage |
| [Channels](./channel.md) | Consent capture, fulfillment |
| [Observer Pattern](./observer-pattern.md) | Channels as delegation observers |

---

## Related Documentation

### Mode Comparison

| Concept | Description |
|---------|-------------|
| [Agent Delegation](./agent-delegation.md) | Umbrella concept; unified model overview |
| [Scenario-Scoped Delegation](./scenario-scoped-delegation.md) | Alternative mode with deployment-time authority |

### Authoritative Source

- [Request-Scoped Delegation (Seer)](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md) — Complete design

### Hub Integration

| Concept | Description |
|---------|-------------|
| [Delegation Handling](../../04-subsystems/signal-exchange/delegation-handling.md) | Signal Exchange processing |
| [Delegation Context](../../04-subsystems/request-management/delegation-context.md) | Request-level storage |
| [Channel](./channel.md) | Channel delegation responsibilities |
| [Observer Pattern](./observer-pattern.md) | Channels as delegation observers |

### Decision Records

| ADR | Decision |
|-----|----------|
| [ADR-0127](../../decision-logs/0127-request-scoped-authority-delegation.md) | Request-Scoped Authority Delegation |
| [ADR-0130](../../decision-logs/0130-unified-delegation-model.md) | Unified Delegation Model |

---

*This document provides the Hub perspective on request-scoped delegation. For the complete design including Cipher, Agent SDK, and Seer Sidecar, see the authoritative Seer documentation.*
