# Delegation Service

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-17  
> **Design Level**: C2 (Container)  
> **Related**: [Request-Scoped Delegation](../../implementation-concepts/request-scoped-delegation.md)

---

## Overview

The Delegation Service handles request-scoped authority delegation within the Seer Sidecar. It provides:
1. **Pre-guardrail delegation check** — Verify agent has required authority before action
2. **Authority request initiation** — Post AUTHORITY_REQUEST when authority is missing
3. **Token injection** — Place delegation tokens in action context
4. **Chaining support** — Delegate authority to child agents

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DELEGATION SERVICE IN SEER SIDECAR                        │
│                                                                              │
│   Agent Action Request                                                       │
│        │                                                                     │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │              PRE-GUARDRAIL DELEGATION CHECK                          │   │
│   │                                                                       │   │
│   │   1. Check if action requires delegation                             │   │
│   │   2. Look up tokens in request context (environment.auth.delegations)│   │
│   │   3. Validate token for this agent                                   │   │
│   │   4. If missing/invalid → initiate Authority Request                 │   │
│   └─────────────────────────┬───────────────────────────────────────────┘   │
│                            │                                                 │
│                   ┌────────┴────────┐                                        │
│                   ▼                 ▼                                        │
│           [Has Token]        [No Token]                                      │
│               │                   │                                          │
│               ▼                   ▼                                          │
│   ┌─────────────────┐   ┌─────────────────────────────────────────┐         │
│   │  TOKEN INJECTION │   │    AUTHORITY REQUEST INITIATION         │         │
│   │                  │   │                                         │         │
│   │  Add token to    │   │  1. Build AUTHORITY_REQUEST             │         │
│   │  action context  │   │  2. Post to Signal Exchange             │         │
│   │                  │   │  3. Wait for AUTHORITY_GRANTED/DENIED   │         │
│   └────────┬─────────┘   │  4. Inject token or return denial       │         │
│            │             └─────────────────────────────────────────┘         │
│            ▼                                                                 │
│   Continue to Guardrails                                                     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Pre-Guardrail Delegation Check

### When Check Occurs

The delegation check runs **before** guardrail execution on outbound calls:

| Traffic Type | Delegation Check |
|--------------|------------------|
| Tool calls requiring user authority | ✅ Yes |
| Hub API calls (request updates) | ❌ No (uses agent authority) |
| Model Gateway calls | ❌ No (uses agent authority) |
| Tool calls with only agent authority | ❌ No |

### Check Algorithm

```python
class DelegationChecker:
    """Pre-guardrail delegation check."""
    
    async def check_delegation_before_action(
        self,
        action: AgentAction,
        request_context: RequestContext
    ) -> DelegationCheckResult:
        """Check if agent has required delegation for action."""
        
        # Step 1: Get delegation requirements for this action
        required_templates = self._get_required_templates(action)
        
        if not required_templates:
            # Action doesn't require delegation
            return DelegationCheckResult.not_required()
        
        # Step 2: Get available delegations from context
        available = request_context.environment.auth.delegations or []
        
        # Step 3: Check each required template
        for template in required_templates:
            matching = [d for d in available if d.template == template]
            
            if not matching:
                # Need to request authority
                return DelegationCheckResult.authority_needed(
                    template=template,
                    reason=f"Action requires {template} delegation"
                )
            
            # Step 4: Validate the token
            token = matching[0].token
            validation = await self._validate_token(
                token=token,
                expected_agent=request_context.agent_spiffe_id,
                action=action
            )
            
            if not validation.valid:
                return DelegationCheckResult.invalid_delegation(
                    reason=validation.reason
                )
        
        return DelegationCheckResult.authorized(
            tokens=[d.token for d in available if d.template in required_templates]
        )
    
    def _get_required_templates(self, action: AgentAction) -> List[str]:
        """Determine which delegation templates an action requires."""
        
        # From tool manifest
        if action.tool_id:
            tool = self.tool_registry.get(action.tool_id)
            return tool.delegation_requirements.templates
        
        return []
    
    async def _validate_token(
        self,
        token: str,
        expected_agent: str,
        action: AgentAction
    ) -> TokenValidation:
        """Validate delegation token (local verification)."""
        
        try:
            claims = jwt.decode(token, self.public_key, algorithms=["RS256"])
        except jwt.InvalidTokenError as e:
            return TokenValidation.invalid(str(e))
        
        # Check expiry
        if claims["exp"] < datetime.now().timestamp():
            return TokenValidation.expired()
        
        # Check audience binding
        if claims["aud"] != expected_agent:
            return TokenValidation.invalid("Token not bound to this agent")
        
        # Check template constraints
        constraints = claims["delegation"]["constraints"]
        if not self._constraints_satisfied(constraints, action):
            return TokenValidation.denied("Constraints not satisfied")
        
        return TokenValidation.valid()
```

---

## Authority Request Initiation

### Posting Authority Request

When delegation is missing, the sidecar posts an AUTHORITY_REQUEST:

```python
class AuthorityRequestInitiator:
    """Initiates authority requests when delegation is missing."""
    
    async def request_authority(
        self,
        template: str,
        reason: str,
        request_context: RequestContext,
        timeout: timedelta = timedelta(minutes=5)
    ) -> AuthorityRequestResult:
        """Post AUTHORITY_REQUEST and wait for response."""
        
        # Build authority request payload
        authority_request = AuthorityRequest(
            request_id=generate_id(),
            template=template,
            agent_id=request_context.agent_spiffe_id,
            agent_role=request_context.agent_role,
            reason=reason,
            timeout=timeout.isoformat()
        )
        
        # Post as REQUEST_UPDATE
        update = RequestUpdate(
            update_type="AUTHORITY_REQUEST",
            payload={"authority_request": authority_request.to_dict()}
        )
        
        await self.signal_exchange.post_update(
            request_id=request_context.request_id,
            update=update
        )
        
        # Wait for response (AUTHORITY_GRANTED or AUTHORITY_DENIED)
        response = await self._wait_for_authority_response(
            request_id=request_context.request_id,
            auth_request_id=authority_request.request_id,
            timeout=timeout
        )
        
        return response
    
    async def _wait_for_authority_response(
        self,
        request_id: str,
        auth_request_id: str,
        timeout: timedelta
    ) -> AuthorityRequestResult:
        """Wait for authority grant or denial."""
        
        start = datetime.now()
        
        while datetime.now() - start < timeout:
            # Check for response in request updates
            response = await self._check_for_response(
                request_id, 
                auth_request_id
            )
            
            if response:
                if response.update_type == "AUTHORITY_GRANTED":
                    return AuthorityRequestResult.granted(
                        certificate_id=response.payload.certificate_id,
                        token=response.environment.auth.delegations[0].token
                    )
                elif response.update_type == "AUTHORITY_DENIED":
                    return AuthorityRequestResult.denied(
                        reason=response.payload.reason
                    )
            
            await asyncio.sleep(0.5)
        
        return AuthorityRequestResult.timeout()
```

---

## Token Injection

### Injecting Token into Action Context

When delegation is authorized, the token is injected:

```python
def inject_delegation_token(
    action: AgentAction,
    token: str,
    template: str
) -> AgentAction:
    """Inject delegation token into action context."""
    
    action.context.delegation = DelegationContext(
        token=token,
        template=template,
        header_name="X-Delegation-Token"
    )
    
    return action
```

### Token Propagation to Tool Gateway

The token is passed to Tool Gateway in the request:

```yaml
# Request to Tool Gateway
headers:
  Authorization: "Bearer {agent_token}"
  X-Delegation-Token: "eyJ..."  # Delegation Access Token

body:
  tool_id: "payment-initiate"
  parameters:
    amount: 450
    recipient: "user-12345"
```

Tool Gateway validates both tokens and enforces both authority sets.

---

## Chaining Support

### Agent-to-Agent Delegation

When an agent needs to delegate authority to a child agent:

```python
class DelegationChainer:
    """Handles delegation chaining to child agents."""
    
    async def delegate_to_child(
        self,
        child_agent_id: str,
        template: str,
        parent_token: str,
        request_context: RequestContext
    ) -> DelegationAccessToken:
        """Create chained delegation for child agent."""
        
        # Validate parent token allows chaining
        parent_claims = jwt.decode(parent_token, self.public_key)
        
        if not parent_claims.get("delegation", {}).get("chainingAllowed"):
            raise ChainingNotAllowedError("Parent token does not allow chaining")
        
        # Request chained token from Cipher
        chained_token = await self.cipher_client.create_chained_token(
            parent_token=parent_token,
            child_agent_id=child_agent_id,
            template=template,
            request_id=request_context.request_id
        )
        
        return chained_token
```

---

## Configuration

### Sidecar Configuration

```yaml
sidecar:
  delegation:
    enabled: true
    
    # Pre-guardrail check
    pre_guardrail_check:
      enabled: true
      fail_on_missing: false  # If false, continue with degraded capability
    
    # Token validation
    token_validation:
      public_key_source: "cipher"
      revocation_check: true
      revocation_cache_ttl: "1m"
    
    # Authority request
    authority_request:
      default_timeout: "5m"
      max_timeout: "30m"
      retry_on_failure: true
    
    # Chaining
    chaining:
      enabled: true
      max_chain_depth: 3
```

---

## Metrics

```prometheus
# Delegation checks
seer_sidecar_delegation_checks_total{result="authorized"} 5678
seer_sidecar_delegation_checks_total{result="authority_needed"} 234
seer_sidecar_delegation_checks_total{result="denied"} 12

# Authority requests
seer_sidecar_authority_requests_total{outcome="granted"} 200
seer_sidecar_authority_requests_total{outcome="denied"} 30
seer_sidecar_authority_requests_total{outcome="timeout"} 4

# Token validation
seer_sidecar_token_validation_total{result="valid"} 5678
seer_sidecar_token_validation_total{result="expired"} 23
seer_sidecar_token_validation_total{result="revoked"} 5
```

---

## Related Documentation

- [Authority Enforcement Service](./authority-enforcement-service.md) — Authority ceiling enforcement
- [Policy Enforcement Service](./policy-enforcement-service.md) — OPA policy evaluation
- [Request-Scoped Delegation](../../implementation-concepts/request-scoped-delegation.md) — Comprehensive design
- [Delegation Handling (Hub)](../../../../olympus-hub-docs/04-subsystems/signal-exchange/delegation-handling.md) — Signal Exchange processing

---

*Delegation Service provides pre-guardrail authority checks, request initiation, and token injection for request-scoped delegation.*
