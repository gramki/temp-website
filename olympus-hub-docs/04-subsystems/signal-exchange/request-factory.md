# Request Factory

> **Status:** 🟡 Draft — Under active development

The Request Factory creates new Requests or updates existing Requests based on **Request Mutation DTOs** produced by Triggers.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Create and update Requests from Request Mutation DTOs |
| **Input** | Request Mutation DTOs from Trigger Evaluator |
| **Output** | Requests dispatched to Application Router |
| **State** | Interacts with Request Management for persistence |

---

## Request Mutation DTO

The **Request Mutation DTO** is the standard input format for the Request Factory. Triggers transform Normalized Signal DTOs into Request Mutation DTOs.

| Mutation Type | Description |
|---------------|-------------|
| **INITIATION** | Create a new Request |
| **UPDATE** | Update an existing Request |

See [Signal Provider Interactions](./signal-provider-interactions.md#request-mutation-dto) for the full DTO schema.

---

## Responsibilities

| Function | Description |
|----------|-------------|
| **Request Creation** | Create new Request instances from INITIATION mutations |
| **Request Updates** | Update existing Requests from UPDATE mutations |
| **Observer Registration** | Auto-register originating Signal Provider as observer |
| **Session Binding** | Bind Request to Application session |
| **Idempotency** | Prevent duplicate Request creation via idempotency keys |
| **Request Typing** | Apply correct Request type (Service/Business/System) |
| **Delegation Context Init** | Initialize delegation context from Channel-attached certificates |

---

## Create vs Update Logic

```
Based on trigger configuration (create_or_update):

create_new:
  → Always create a new Request

update_existing:
  → Find existing Request by correlation key
  → If found → update
  → If not found → error or create (configurable)

create_or_update:
  → Find existing Request by correlation key
  → If found → update
  → If not found → create new
```

---

## Request Correlation

Requests can be correlated by:
- **Explicit correlation ID** in signal
- **Business entity ID** (e.g., customer_id, transaction_id)
- **Session ID** from I/O Gateway
- **Idempotency key** from trigger definition

---

## Request-Application Session

A Request represents a session with a Hub Application:

| Aspect | Description |
|--------|-------------|
| **Lifecycle** | Request lives as long as Application processes it |
| **Updates** | Subsequent signals can update the same Request |
| **State** | Request state reflects Application processing state |

---

---

## Delegation Context Initialization

When creating a Request, the Request Factory initializes the delegation context:

### From Channel-Attached Certificates

If the initiating Channel attaches a Delegation Certificate (proactive delegation):

```python
def initialize_delegation_context(
    request: Request,
    initiation_dto: RequestMutationDTO
) -> None:
    """Initialize delegation context for new request."""
    
    if initiation_dto.delegation_certificates:
        for cert_ref in initiation_dto.delegation_certificates:
            request.delegations.certificates.append(
                DelegationCertificateRef(
                    id=cert_ref.certificate_id,
                    template=cert_ref.template,
                    delegator=cert_ref.delegator,
                    attached_at=datetime.now(),
                    expires_at=cert_ref.expires_at,
                    attachment_type="proactive"
                )
            )
```

### From Parent Request (Child Creation)

When creating a child request, inheritable delegations flow down:

```python
def inherit_delegation_context(
    child_request: Request,
    parent_request: Request
) -> None:
    """Inherit delegation context from parent."""
    
    for cert in parent_request.delegations.certificates:
        template = get_template(cert.template)
        
        if template.constraints.chainingAllowed:
            child_request.delegations.certificates.append(
                DelegationCertificateRef(
                    id=cert.id,
                    template=cert.template,
                    delegator=cert.delegator,
                    attached_at=datetime.now(),
                    expires_at=cert.expires_at,
                    attachment_type="inherited",
                    source_request_id=parent_request.id
                )
            )
```

→ See [Delegation Context](../request-management/delegation-context.md) for details.

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Trigger Evaluator](./trigger-evaluator.md)
- [Application Router](./application-router.md)
- [Request Management](../request-management/README.md)
- [Delegation Context](../request-management/delegation-context.md)
- [Delegation Handling](./delegation-handling.md)

---

*TODO: Detailed design — correlation strategies, session management, error handling*

