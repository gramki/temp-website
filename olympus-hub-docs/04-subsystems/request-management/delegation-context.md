# Delegation Context

> **Status:** 🟢 Design Complete  
> **Last Updated:** 2026-01-17  
> **Related:** [Request-Scoped Delegation](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)

---

## Overview

**Delegation Context** is the request-level storage for delegation certificates and tokens that enable agents to act on behalf of business users. The Request Lifecycle Manager maintains this context as part of the Request's runtime state.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Delegation Context** | Collection of active delegations for a Request |
| **Certificate Reference** | Pointer to Delegation Certificate stored in Cipher |
| **Token Cache** | Per-agent tokens issued from certificates |
| **Authority Requests** | Pending requests for additional authority |

---

## Schema

### Delegation Context Structure

```yaml
delegations:
  # Active certificates for this request
  certificates:
    - id: "cert-11111"
      template: "personal-finance-assistant"
      delegator:
        id: "user-67890"
        type: "business-user"
      attached_at: "2026-01-17T10:00:00Z"
      expires_at: "2026-01-17T22:00:00Z"
      attachment_type: "proactive"  # "proactive" | "reactive" | "inherited"
      source_request_id: null  # For inherited: the request that obtained it
    
    - id: "cert-22222"
      template: "view-investments"
      delegator:
        id: "user-67890"
        type: "business-user"
      attached_at: "2026-01-17T10:05:00Z"
      expires_at: "2026-01-18T10:05:00Z"
      attachment_type: "reactive"
      source_request_id: null

  # Pending authority requests (not yet resolved)
  pending_requests:
    - request_id: "auth-req-33333"
      template: "initiate-large-payments"
      requested_by: "spiffe://seer/agents/my-assistant"
      requested_at: "2026-01-17T14:30:00Z"
      timeout_at: "2026-01-17T14:35:00Z"
      reason: "Need to initiate payment over $500"
      status: "pending"
  
  # Token cache (ephemeral, per-delivery)
  # Not stored; computed on each REQUEST_UPDATE delivery
```

---

## Delegation Context API

### Get Delegations for Request

```python
async def get_delegations(
    request_id: str
) -> DelegationContext:
    """Get all active delegations for a request."""
    
    context = await request_store.get_delegation_context(request_id)
    
    # Filter out expired certificates
    active = [
        cert for cert in context.certificates
        if cert.expires_at > datetime.now()
    ]
    
    return DelegationContext(
        certificates=active,
        pending_requests=context.pending_requests
    )
```

### Add Delegation to Request

```python
async def add_delegation(
    request_id: str,
    certificate_id: str,
    template: str,
    delegator: DelegatorRef,
    expires_at: datetime,
    attachment_type: str = "reactive"
) -> None:
    """Add a delegation certificate to a request."""
    
    context = await request_store.get_delegation_context(request_id)
    
    # Check for duplicates
    existing = next(
        (c for c in context.certificates if c.id == certificate_id),
        None
    )
    if existing:
        return  # Already attached
    
    # Add certificate reference
    context.certificates.append(DelegationCertificateRef(
        id=certificate_id,
        template=template,
        delegator=delegator,
        attached_at=datetime.now(),
        expires_at=expires_at,
        attachment_type=attachment_type
    ))
    
    await request_store.update_delegation_context(request_id, context)
```

### Check Delegation Availability

```python
async def has_delegation(
    request_id: str,
    template: str,
    agent_id: str = None
) -> bool:
    """Check if request has a valid delegation for the given template."""
    
    context = await get_delegations(request_id)
    
    for cert in context.certificates:
        if cert.template != template:
            continue
        if cert.expires_at <= datetime.now():
            continue
        
        # If agent_id specified, verify eligibility
        if agent_id:
            full_cert = await cipher_client.get_certificate(cert.id)
            if not matches_delegate_pattern(agent_id, full_cert.delegate):
                continue
        
        return True
    
    return False
```

### Register Authority Request

```python
async def register_authority_request(
    request_id: str,
    auth_request: AuthorityRequest
) -> str:
    """Register a pending authority request."""
    
    context = await request_store.get_delegation_context(request_id)
    
    pending = PendingAuthorityRequest(
        request_id=generate_id(),
        template=auth_request.template,
        requested_by=auth_request.agent_id,
        requested_at=datetime.now(),
        timeout_at=datetime.now() + auth_request.timeout,
        reason=auth_request.reason,
        status="pending"
    )
    
    context.pending_requests.append(pending)
    await request_store.update_delegation_context(request_id, context)
    
    return pending.request_id
```

### Resolve Authority Request

```python
async def resolve_authority_request(
    request_id: str,
    auth_request_id: str,
    outcome: str,  # "granted" | "denied" | "timeout"
    certificate_id: str = None
) -> None:
    """Resolve a pending authority request."""
    
    context = await request_store.get_delegation_context(request_id)
    
    pending = next(
        (p for p in context.pending_requests if p.request_id == auth_request_id),
        None
    )
    
    if not pending:
        raise NotFoundError(f"Authority request {auth_request_id} not found")
    
    pending.status = outcome
    pending.resolved_at = datetime.now()
    
    if outcome == "granted" and certificate_id:
        # Add the granted certificate
        cert = await cipher_client.get_certificate(certificate_id)
        await add_delegation(
            request_id=request_id,
            certificate_id=certificate_id,
            template=cert.template.name,
            delegator=DelegatorRef(
                id=cert.delegator.id,
                type=cert.delegator.type
            ),
            expires_at=cert.constraints.expiry,
            attachment_type="reactive"
        )
    
    await request_store.update_delegation_context(request_id, context)
```

---

## Context Inheritance (Child Requests)

### Inheritance Rules

When a child request is created, delegation context can be inherited from the parent:

| Inheritance Type | Behavior |
|------------------|----------|
| **Automatic** | Certificates flow to child if template allows |
| **On-Demand** | Child requests authority, cascades to parent |
| **None** | Child must obtain its own delegations |

### Inheritance Algorithm

```python
async def initialize_child_delegation_context(
    child_request_id: str,
    parent_request_id: str,
    scenario_config: ScenarioConfig
) -> None:
    """Initialize delegation context for a child request."""
    
    parent_context = await get_delegations(parent_request_id)
    child_context = DelegationContext(certificates=[], pending_requests=[])
    
    for cert in parent_context.certificates:
        # Check if template allows inheritance
        template = await get_template(cert.template)
        
        if template.constraints.chainingAllowed:
            # Reference parent's certificate (not copy)
            child_context.certificates.append(DelegationCertificateRef(
                id=cert.id,
                template=cert.template,
                delegator=cert.delegator,
                attached_at=datetime.now(),
                expires_at=cert.expires_at,
                attachment_type="inherited",
                source_request_id=parent_request_id
            ))
    
    await request_store.update_delegation_context(
        child_request_id, 
        child_context
    )
```

---

## Cleanup on Request Completion

When a request reaches a terminal state, delegation context is cleaned up:

```python
async def cleanup_delegation_context(request_id: str) -> None:
    """Clean up delegation context when request completes."""
    
    context = await get_delegations(request_id)
    
    # Cancel pending authority requests
    for pending in context.pending_requests:
        if pending.status == "pending":
            pending.status = "cancelled"
            pending.resolved_at = datetime.now()
    
    # Note: Certificate references are kept for audit
    # Actual certificates in Cipher have their own lifecycle
    
    await request_store.update_delegation_context(request_id, context)
```

---

## Storage

Delegation context is stored as part of the Request document:

```json
{
  "request_id": "req-12345",
  "workbench_id": "retail-banking",
  "scenario_id": "personal-finance-assistant",
  "status": "ACTIVE",
  
  "delegations": {
    "certificates": [...],
    "pending_requests": [...]
  },
  
  "subject": {...},
  "payload": {...}
}
```

Storage characteristics:
- **Transactional** — Updates are atomic with request state
- **Queryable** — Can query requests by delegation template or delegator
- **Retention** — Follows request retention policy

---

## Related Documentation

- [Request Storage](./request-storage.md) — Request document structure
- [Request Hierarchy](./request-hierarchy.md) — Parent-child inheritance
- [Delegation Handling (SX)](../signal-exchange/delegation-handling.md) — Signal Exchange processing
- [Request-Scoped Delegation](../../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md) — Comprehensive design

---

*Delegation Context provides request-level storage and APIs for managing delegation certificates and authority requests.*
