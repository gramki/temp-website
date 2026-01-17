# Delegation Handling

> **Status:** 🟢 Design Complete  
> **Last Updated:** 2026-01-17  
> **Related:** [Request-Scoped Delegation](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)

---

## Overview

Signal Exchange handles request-scoped delegation by:
1. Routing `AUTHORITY_REQUEST` updates to observer modules (specifically Channels)
2. Processing `AUTHORITY_GRANTED` updates from Channels
3. Refreshing Delegation Access Tokens in `environment.auth.delegations` on each update delivery
4. Managing delegation context within the Request lifecycle

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DELEGATION HANDLING IN SIGNAL EXCHANGE                    │
│                                                                              │
│   ┌───────────────────────────────────────────────────────────────────────┐ │
│   │                      AUTHORITY REQUEST FLOW                            │ │
│   │                                                                        │ │
│   │   Agent (via Sidecar) ──▶ AUTHORITY_REQUEST ──▶ Signal Exchange       │ │
│   │                                                       │                │ │
│   │                                                       ▼                │ │
│   │                                          Observer Notification        │ │
│   │                                                       │                │ │
│   │                                                       ▼                │ │
│   │                                    Channel (handles consent/fulfillment)│ │
│   └───────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│   ┌───────────────────────────────────────────────────────────────────────┐ │
│   │                      AUTHORITY GRANTED FLOW                            │ │
│   │                                                                        │ │
│   │   Channel ──▶ (requests cert+token from Cipher) ──▶ AUTHORITY_GRANTED │ │
│   │                                                            │           │ │
│   │                                                            ▼           │ │
│   │                                       Signal Exchange receives update  │ │
│   │                                                            │           │ │
│   │                                                            ▼           │ │
│   │                               Store certificate + token in context     │ │
│   │                                                            │           │ │
│   │                                                            ▼           │ │
│   │                               Notify Agent (token in env.auth)         │ │
│   └───────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│   ┌───────────────────────────────────────────────────────────────────────┐ │
│   │                      TOKEN REFRESH ON UPDATE                           │ │
│   │                                                                        │ │
│   │   Every REQUEST_UPDATE delivery to Agent:                              │ │
│   │   1. Get certificates from Request context                             │ │
│   │   2. Issue/refresh tokens for target agent                             │ │
│   │   3. Place in environment.auth.delegations                             │ │
│   │   4. Deliver updated envelope                                          │ │
│   └───────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## AUTHORITY_REQUEST Routing

### Request Update Sub-Type

`AUTHORITY_REQUEST` is a sub-type of `REQUEST_UPDATE` from Hub Applications (or agents via sidecar):

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_UPDATE",
    "message_id": "uuid",
    "timestamp": "2026-01-17T14:30:00Z",
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001"
  },
  
  "request": {
    "workbench_id": "retail-banking",
    "scenario_id": "personal-finance-assistant",
    "id": "req-12345"
  },
  
  "update": {
    "update_type": "AUTHORITY_REQUEST",
    "sequence": 5
  },
  
  "payload": {
    "authority_request": {
      "request_id": "auth-req-67890",
      "template": "personal-finance-assistant",
      "agent_role": "personal-assistant-agent",
      "agent_id": "spiffe://seer/agents/my-assistant",
      "reason": "Need to initiate payment on user's behalf",
      "timeout": "PT5M"
    }
  }
}
```

### Routing Behavior

Signal Exchange routes `AUTHORITY_REQUEST` updates to **all registered observer modules** for the request, following the standard observer notification pattern:

1. **No special routing** — follows same path as any REQUEST_UPDATE
2. **Channels receive it** — as observer modules subscribed to the workbench
3. **Channels handle it** — determine if they can fulfill (certificate exists) or need user consent

```python
async def handle_authority_request_update(
    update: RequestUpdate
) -> None:
    """Handle AUTHORITY_REQUEST update - standard observer routing."""
    
    # Standard observer notification
    # Signal Exchange does NOT know which Channel should handle it
    # All observers receive it; Channel(s) determine action
    await dispatch_to_observers(update)
```

---

## AUTHORITY_GRANTED Processing

### Request Update Sub-Type

`AUTHORITY_GRANTED` is sent by Channels after obtaining user consent (or implicit fulfillment). The Channel orchestrates the flow: it requests the Certificate from Cipher, then requests the Token for the target agent:

```json
{
  "envelope": {
    "version": "1.0",
    "message_type": "REQUEST_UPDATE",
    "message_id": "uuid",
    "timestamp": "2026-01-17T14:31:00Z",
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001"
  },
  
  "request": {
    "workbench_id": "retail-banking",
    "scenario_id": "personal-finance-assistant",
    "id": "req-12345"
  },
  
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
      "expires_at": "2026-01-17T22:00:00Z",
      "fulfillment_type": "user_consent",  // "user_consent" | "implicit_certificate"
      "token": "eyJhbGciOiJSUzI1NiIs..."  // Token obtained from Cipher for target agent
    }
  }
}
```

### Processing Behavior

```python
async def handle_authority_granted_update(
    update: RequestUpdate
) -> None:
    """Handle AUTHORITY_GRANTED update from Channel."""
    
    authority_granted = update.payload.authority_granted
    
    # Step 1: Store certificate reference in request context
    await request_context_store.add_delegation(
        request_id=update.request.id,
        certificate_id=authority_granted.certificate_id,
        template=authority_granted.template,
        delegator=authority_granted.delegator,
        expires_at=authority_granted.expires_at
    )
    
    # Step 2: Store initial token (Channel already obtained from Cipher)
    await request_context_store.set_initial_token(
        request_id=update.request.id,
        agent_id=authority_granted.target_agent,
        token=authority_granted.token
    )
    
    # Step 3: Notify observers (agent receives token immediately)
    await dispatch_to_observers(update)
```

---

## Token Refresh on Update Delivery

### Core Mechanism

Every time Signal Exchange delivers a `REQUEST_UPDATE` to an agent, it **refreshes** the delegation tokens in `environment.auth.delegations`:

```python
async def prepare_update_for_agent_delivery(
    update: RequestUpdate,
    target_agent: str
) -> MessageEnvelope:
    """Prepare update envelope with fresh delegation tokens."""
    
    # Get current delegation context for this request
    delegations = await request_context_store.get_delegations(
        request_id=update.request.id
    )
    
    # Issue/refresh tokens for the target agent
    agent_delegations = []
    for delegation in delegations:
        # Check certificate is still valid
        if not await is_certificate_valid(delegation.certificate_id):
            continue
        
        # Issue token for this agent
        token = await cipher_client.issue_delegation_token(
            certificate_id=delegation.certificate_id,
            agent_id=target_agent,
            request_id=update.request.id
        )
        
        agent_delegations.append({
            "token": token.value,
            "template": delegation.template,
            "delegator": delegation.delegator,
            "expiresAt": token.expires_at.isoformat()
        })
    
    # Build envelope with fresh tokens
    return MessageEnvelope(
        header=update.header,
        payload=update.payload,
        environment={
            **update.environment,
            "auth": {
                **update.environment.get("auth", {}),
                "delegations": agent_delegations
            }
        }
    )
```

### Why Refresh on Every Update?

The **initial token** is obtained by the Channel from Cipher and included in the Request or AUTHORITY_GRANTED. Signal Exchange **refreshes** tokens on subsequent updates:

1. **Token Freshness** — Tokens have limited validity; refreshing ensures agent always has valid token
2. **Revocation Check** — Revoked certificates are filtered out on each delivery
3. **Multiple Agents** — Each agent gets its own token (bound to their SPIFFE ID)
4. **New Delegations** — Mid-request delegation grants are immediately available

---

## AUTHORITY_DENIED Handling

When user denies delegation or request times out:

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
      "reason": "user_denied",  // "user_denied" | "timeout" | "not_available"
      "user_message": "User declined the permission request"
    }
  }
}
```

Processing:
```python
async def handle_authority_denied_update(
    update: RequestUpdate
) -> None:
    """Handle AUTHORITY_DENIED update from Channel."""
    
    # No certificate stored; just notify observers
    await dispatch_to_observers(update)
    
    # Agent receives the denial and must handle gracefully
    # Default behavior: continue with degraded capability
```

---

## Cascading Authority Requests

### Up the Request Hierarchy

When a child request needs authority and the initiating Channel doesn't have a user present, the authority request can **cascade** up the request hierarchy:

```python
async def handle_authority_request_with_cascade(
    update: RequestUpdate
) -> None:
    """Handle authority request with possible cascade to parent."""
    
    # First, dispatch to observers at this request level
    await dispatch_to_observers(update)
    
    # If no observer can fulfill (determined asynchronously),
    # the Channel may cascade to parent request
    # This is handled by the Channel, not Signal Exchange
```

### Channel-Driven Cascade

The Channel (as observer) determines if cascade is needed:

```python
# In Channel observer module
async def handle_authority_request_notification(
    notification: ObserverNotification
) -> None:
    """Channel handles authority request."""
    
    authority_request = notification.update.payload.authority_request
    
    # Try implicit fulfillment
    existing_cert = await find_matching_certificate(
        user_id=notification.request.subject.id,
        template=authority_request.template
    )
    
    if existing_cert:
        # Implicit fulfillment
        await post_authority_granted(
            request_id=notification.request.id,
            certificate_id=existing_cert.id
        )
        return
    
    # Check if user is present
    if await is_user_present(notification.request.id):
        # Prompt user for consent
        await prompt_user_consent(notification)
        return
    
    # No user present - cascade to parent if hierarchy exists
    if notification.request.parent_request_id:
        await cascade_authority_request_to_parent(
            parent_request_id=notification.request.parent_request_id,
            authority_request=authority_request
        )
    else:
        # No cascade possible - deny
        await post_authority_denied(
            request_id=notification.request.id,
            reason="not_available"
        )
```

---

## Delegation Context in Request Storage

### Schema

```yaml
request:
  id: "req-12345"
  workbench_id: "retail-banking"
  scenario_id: "personal-finance-assistant"
  
  delegations:
    certificates:
      - certificate_id: "cert-11111"
        template: "personal-finance-assistant"
        delegator: "user-67890"
        issued_at: "2026-01-17T14:31:00Z"
        expires_at: "2026-01-17T22:00:00Z"
        fulfillment_type: "user_consent"
    
    pending_requests:
      - request_id: "auth-req-67890"
        template: "personal-finance-assistant"
        requested_at: "2026-01-17T14:30:00Z"
        timeout_at: "2026-01-17T14:35:00Z"
        status: "pending"  # "pending" | "granted" | "denied" | "timeout"
```

---

## Signal Provider vs Channel

A critical distinction for delegation handling:

| Aspect | Signal Provider | Channel |
|--------|-----------------|---------|
| **Delegation Role** | Cannot delegate | Can facilitate delegation |
| **User Context** | No user presence | User is present |
| **AUTHORITY_REQUEST** | Ignores | Handles (consent or implicit) |
| **AUTHORITY_GRANTED** | N/A | Posts when consent obtained |

Only **Channels** can:
- Present consent UI to users
- Attach Delegation Certificates to Requests
- Handle AUTHORITY_REQUEST updates
- Implicitly fulfill from existing certificates

Signal Providers just forward signals; they have no user identity context.

---

## Metrics

```prometheus
# Authority requests
seer_authority_requests_total{workbench="retail-banking", outcome="granted"} 1234
seer_authority_requests_total{workbench="retail-banking", outcome="denied"} 56
seer_authority_requests_total{workbench="retail-banking", outcome="timeout"} 12

# Token refresh
seer_delegation_token_refresh_total{workbench="retail-banking"} 5678
seer_delegation_token_refresh_errors_total{reason="cert_revoked"} 23

# Cascade
seer_authority_cascade_total{direction="to_parent"} 89
```

---

## Related Documentation

- [Message Envelope](./message-envelope.md) — `environment.auth.delegations` schema
- [Observer Notifications](./observer-notifications.md) — Observer dispatch
- [Request-Scoped Delegation](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md) — Comprehensive design
- [Delegation Context](../request-management/delegation-context.md) — Request-level delegation storage

---

*Delegation Handling provides token refresh, authority request routing, and cascading for request-scoped delegation.*
