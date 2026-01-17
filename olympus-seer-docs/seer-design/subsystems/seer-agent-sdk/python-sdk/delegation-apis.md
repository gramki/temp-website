# Delegation APIs (Python)

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-17  
> **Related**: [Request-Scoped Delegation](../../../implementation-concepts/request-scoped-delegation.md)

---

## Overview

The Delegation APIs enable agents to work with request-scoped authority delegation. These APIs allow agents to:
1. **Request authority** — Ask for delegation when needed
2. **Get delegation tokens** — Access available tokens for actions
3. **Delegate to children** — Pass authority to child agents
4. **Handle denial** — Gracefully handle denied requests

---

## Core APIs

### HubClient Delegation Methods

```python
from seer_sdk.hub import HubClient
from seer_sdk.delegation import (
    DelegationToken,
    AuthorityRequest,
    AuthorityResponse,
    DelegationError,
    AuthorityDeniedError,
    AuthorityTimeoutError
)

class HubClient:
    """Hub integration client with delegation support."""
    
    async def request_authority(
        self,
        template_id: str,
        reason: str,
        timeout: timedelta = timedelta(minutes=5)
    ) -> DelegationToken:
        """
        Request delegation authority from the user.
        
        This posts an AUTHORITY_REQUEST and waits for the response.
        The Channel will prompt the user (or auto-fulfill from existing
        certificates).
        
        Args:
            template_id: ID of the Delegation Template to request
            reason: Human-readable reason for the request
            timeout: How long to wait for user response
            
        Returns:
            DelegationToken if granted
            
        Raises:
            AuthorityDeniedError: User denied the request
            AuthorityTimeoutError: Request timed out
            DelegationError: Other delegation errors
        """
        ...
    
    def get_delegation_token(
        self,
        template_id: str
    ) -> Optional[DelegationToken]:
        """
        Get an available delegation token for the specified template.
        
        Returns None if no token is available. Call request_authority()
        to obtain a token if needed.
        
        Args:
            template_id: ID of the Delegation Template
            
        Returns:
            DelegationToken if available, None otherwise
        """
        ...
    
    def get_all_delegation_tokens(self) -> List[DelegationToken]:
        """
        Get all available delegation tokens for this request.
        
        Returns:
            List of all DelegationToken objects in the current context
        """
        ...
    
    def has_delegation(self, template_id: str) -> bool:
        """
        Check if agent has delegation for the specified template.
        
        Args:
            template_id: ID of the Delegation Template
            
        Returns:
            True if delegation is available
        """
        ...
    
    async def delegate_to_child(
        self,
        child_agent_id: str,
        template_id: str
    ) -> DelegationToken:
        """
        Delegate authority to a child agent.
        
        Requires that the current token allows chaining.
        
        Args:
            child_agent_id: SPIFFE ID of the child agent
            template_id: Template to delegate (must be <= current scope)
            
        Returns:
            DelegationToken for the child agent
            
        Raises:
            ChainingNotAllowedError: Token doesn't allow chaining
            DelegationError: Other delegation errors
        """
        ...
    
    def can_delegate_to_child(self, template_id: str = None) -> bool:
        """
        Check if current token allows chaining to child agents.
        
        Args:
            template_id: Optional template ID to check specific token
            
        Returns:
            True if chaining is allowed
        """
        ...
```

---

## Data Classes

### DelegationToken

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

@dataclass
class DelegationToken:
    """Represents a Delegation Access Token."""
    
    token: str
    """The JWT token string."""
    
    template_id: str
    """The Delegation Template ID."""
    
    delegator_id: str
    """ID of the business user who delegated."""
    
    expires_at: datetime
    """When the token expires."""
    
    permissions: List[str]
    """List of permissions granted."""
    
    constraints: Dict
    """Constraints on the delegation (e.g., maxAmount)."""
    
    chaining_allowed: bool
    """Whether this token can be delegated to child agents."""
    
    def is_expired(self) -> bool:
        """Check if token is expired."""
        return datetime.now() > self.expires_at
    
    def to_header(self) -> Dict[str, str]:
        """Get header dict for API calls."""
        return {"X-Delegation-Token": self.token}
```

### AuthorityRequest

```python
@dataclass
class AuthorityRequest:
    """Request for delegation authority."""
    
    template_id: str
    """Template to request."""
    
    reason: str
    """Why the agent needs this authority."""
    
    timeout: timedelta = timedelta(minutes=5)
    """How long to wait."""
```

### AuthorityResponse

```python
@dataclass
class AuthorityResponse:
    """Response to an authority request."""
    
    granted: bool
    """Whether authority was granted."""
    
    token: Optional[DelegationToken]
    """Token if granted."""
    
    denial_reason: Optional[str]
    """Reason if denied."""
```

---

## Usage Examples

### Basic Authority Request

```python
from seer_sdk.hub import HubClient
from seer_sdk.delegation import AuthorityDeniedError

hub_client = HubClient()

async def process_payment():
    # Check if we already have authority
    if not hub_client.has_delegation("personal-finance-assistant"):
        try:
            # Request authority from user
            token = await hub_client.request_authority(
                template_id="personal-finance-assistant",
                reason="Need to initiate payment on your behalf"
            )
            print(f"Authority granted, expires: {token.expires_at}")
        except AuthorityDeniedError as e:
            print(f"User denied: {e.reason}")
            # Continue with degraded capability
            return await handle_no_authority()
    
    # Use delegation for payment
    token = hub_client.get_delegation_token("personal-finance-assistant")
    await initiate_payment(amount=450, delegation_token=token)
```

### Using Token with Tool Calls

```python
from seer_sdk.tools import ToolClient

async def call_payment_tool():
    tool_client = ToolClient()
    
    # Get delegation token
    token = hub_client.get_delegation_token("personal-finance-assistant")
    
    if not token:
        raise DelegationError("No delegation available for payment")
    
    # Token is automatically included when calling tools
    result = await tool_client.call(
        tool_id="payment-initiate",
        params={"amount": 450, "recipient": "user-12345"},
        delegation_token=token  # Passed to Tool Gateway
    )
    
    return result
```

### Chaining to Child Agent

```python
async def delegate_to_child():
    # Check if we can chain
    if not hub_client.can_delegate_to_child("personal-finance-assistant"):
        raise ChainingNotAllowedError("Cannot delegate to child")
    
    # Create token for child agent
    child_token = await hub_client.delegate_to_child(
        child_agent_id="spiffe://seer/agents/child-payment-processor",
        template_id="personal-finance-assistant"
    )
    
    # Pass to child via scenario invocation
    await invoke_child_scenario(
        scenario_id="payment-processing",
        delegation_tokens=[child_token]
    )
```

### Graceful Degradation

```python
async def process_with_optional_delegation():
    """Process with delegation if available, otherwise degrade."""
    
    token = hub_client.get_delegation_token("view-investments")
    
    if token:
        # Full capability - can show real portfolio
        portfolio = await fetch_user_portfolio(delegation_token=token)
        return format_portfolio(portfolio)
    else:
        # Degraded - show educational content instead
        return get_educational_content("investment-basics")
```

---

## Error Handling

### Exception Classes

```python
class DelegationError(Exception):
    """Base class for delegation errors."""
    pass

class AuthorityDeniedError(DelegationError):
    """User denied the authority request."""
    
    def __init__(self, reason: str):
        self.reason = reason
        super().__init__(f"Authority denied: {reason}")

class AuthorityTimeoutError(DelegationError):
    """Authority request timed out."""
    pass

class ChainingNotAllowedError(DelegationError):
    """Token does not allow chaining to child agents."""
    pass

class TokenExpiredError(DelegationError):
    """Delegation token has expired."""
    pass

class TokenRevokedError(DelegationError):
    """Delegation token has been revoked."""
    pass
```

### Best Practices

```python
from seer_sdk.delegation import (
    DelegationError,
    AuthorityDeniedError,
    AuthorityTimeoutError
)

async def robust_delegation_handling():
    try:
        token = await hub_client.request_authority(
            template_id="personal-finance-assistant",
            reason="Need to check your account balance"
        )
        return await perform_action_with_delegation(token)
        
    except AuthorityDeniedError:
        # User explicitly denied - respect their decision
        return await perform_degraded_action()
        
    except AuthorityTimeoutError:
        # User didn't respond - continue with degraded capability
        return await perform_degraded_action()
        
    except DelegationError as e:
        # Other errors - log and degrade
        logger.warning(f"Delegation error: {e}")
        return await perform_degraded_action()
```

---

## Related Documentation

- [Hub Integration APIs](./hub-integration-apis.md) — Other Hub APIs
- [Java Delegation APIs](../java-sdk/delegation-apis.md) — Java equivalent
- [Request-Scoped Delegation](../../../implementation-concepts/request-scoped-delegation.md) — Comprehensive design

---

*Delegation APIs provide Python interfaces for request-scoped authority delegation.*
