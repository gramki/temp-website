# Subscription Policies

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Overview

Agent Ingress Gateway supports subscription-scoped policies that control request routing and access. This document describes policy configuration and provides C3-level detail on policy evaluation.

---

## Subscription-Scoped Policy Configuration

### Policy Types

| Policy Type | Scope | Purpose |
|-------------|-------|---------|
| **Rate Limiting** | Per agent | Limit requests per time window |
| **Authorization** | Per request | Validate request is allowed |
| **Routing Rules** | Per scenario | Custom routing logic |

### Policy Configuration

```yaml
apiVersion: seer.olympus.io/v1
kind: SubscriptionPolicy
metadata:
  name: fraud-analyst-policy
  namespace: acme-disputes
spec:
  agentRef:
    name: fraud-analyst-acme-retail
  
  rateLimit:
    requestsPerMinute: 100
    burstLimit: 20
    action: throttle  # or: reject
  
  authorization:
    requireScenarioMatch: true
    allowedUpdateTypes:
      - new_request
      - status_change
      - data_update
  
  routing:
    priority: 10
    conditions:
      - field: "payload.priority"
        operator: "equals"
        value: "high"
```

---

## Policy Enforcement Points

### Enforcement Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    POLICY ENFORCEMENT POINTS                                 │
│                                                                              │
│   sx-observer                                                                │
│        │                                                                     │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  PEP 1: REQUEST FILTERING                                           │   │
│   │  • Authorization check                                               │   │
│   │  • Update type validation                                            │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│        │                                                                     │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  PEP 2: RATE LIMITING                                                │   │
│   │  • Request rate check                                                │   │
│   │  • Burst limit check                                                 │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│        │                                                                     │
│        ▼                                                                     │
│   Agent Ingress Gateway (Heracles)                                          │
│        │                                                                     │
│        ▼                                                                     │
│   Agent Pod                                                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Policy Evaluation Flow (C3 Detail)

### Evaluation Pipeline

```python
class PolicyEvaluator:
    """Evaluates subscription policies for request dispatch."""
    
    def __init__(self, policy_store):
        self.policies = policy_store
    
    async def evaluate(
        self, 
        agent_id: str, 
        update: RequestUpdate
    ) -> PolicyDecision:
        """
        Evaluate all policies for a request dispatch.
        
        Args:
            agent_id: Target agent ID
            update: Request update to dispatch
        
        Returns:
            PolicyDecision with allow/deny and metadata
        """
        policy = await self.policies.get(agent_id)
        if not policy:
            return PolicyDecision(allowed=True)  # No policy = allow
        
        # Evaluate authorization
        auth_result = self._evaluate_authorization(policy, update)
        if not auth_result.allowed:
            return auth_result
        
        # Evaluate rate limit
        rate_result = await self._evaluate_rate_limit(policy, agent_id)
        if not rate_result.allowed:
            return rate_result
        
        # Evaluate routing conditions
        routing_result = self._evaluate_routing(policy, update)
        if not routing_result.allowed:
            return routing_result
        
        return PolicyDecision(allowed=True)
    
    def _evaluate_authorization(
        self, 
        policy: SubscriptionPolicy, 
        update: RequestUpdate
    ) -> PolicyDecision:
        """Evaluate authorization policy."""
        auth = policy.authorization
        
        # Check update type
        if auth.allowed_update_types:
            if update.update_type not in auth.allowed_update_types:
                return PolicyDecision(
                    allowed=False,
                    reason=f"Update type '{update.update_type}' not allowed"
                )
        
        # Check scenario match
        if auth.require_scenario_match:
            if update.scenario not in policy.subscribed_scenarios:
                return PolicyDecision(
                    allowed=False,
                    reason=f"Scenario '{update.scenario}' not in subscription"
                )
        
        return PolicyDecision(allowed=True)
    
    async def _evaluate_rate_limit(
        self, 
        policy: SubscriptionPolicy, 
        agent_id: str
    ) -> PolicyDecision:
        """Evaluate rate limit policy."""
        rate_config = policy.rate_limit
        if not rate_config:
            return PolicyDecision(allowed=True)
        
        # Get current rate
        current_rate = await self._get_current_rate(agent_id)
        
        # Check rate limit
        if current_rate >= rate_config.requests_per_minute:
            if rate_config.action == "reject":
                return PolicyDecision(
                    allowed=False,
                    reason="Rate limit exceeded",
                    retry_after=60
                )
            else:  # throttle
                return PolicyDecision(
                    allowed=True,
                    throttle=True,
                    delay_ms=self._calculate_delay(current_rate, rate_config)
                )
        
        # Check burst limit
        if await self._is_burst_exceeded(agent_id, rate_config.burst_limit):
            return PolicyDecision(
                allowed=True,
                throttle=True,
                delay_ms=100  # Brief delay for burst smoothing
            )
        
        return PolicyDecision(allowed=True)
```

### Policy Decision Structure

```python
@dataclass
class PolicyDecision:
    allowed: bool
    reason: Optional[str] = None
    throttle: bool = False
    delay_ms: int = 0
    retry_after: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
```

---

## Policy Precedence (C3 Detail)

### Precedence Order

When multiple policies apply, precedence is:

1. **Agent-specific policy** (highest)
2. **Workbench-level policy**
3. **Subscription-level default policy**
4. **Platform default** (lowest)

### Precedence Algorithm

```python
class PolicyResolver:
    """Resolves which policy applies to an agent."""
    
    def resolve(self, agent_id: str, workbench: str) -> SubscriptionPolicy:
        """
        Resolve the effective policy for an agent.
        
        Precedence (highest to lowest):
        1. Agent-specific policy
        2. Workbench-level policy
        3. Subscription-level default
        4. Platform default
        """
        # Try agent-specific
        policy = self.store.get_agent_policy(agent_id)
        if policy:
            return policy
        
        # Try workbench-level
        policy = self.store.get_workbench_policy(workbench)
        if policy:
            return policy
        
        # Try subscription-level
        subscription = self.store.get_subscription(agent_id)
        policy = self.store.get_subscription_policy(subscription.id)
        if policy:
            return policy
        
        # Platform default
        return self.store.get_platform_default_policy()
```

### Policy Merging

When a lower-precedence policy exists, fields are merged:

```yaml
# Workbench policy
rateLimit:
  requestsPerMinute: 100

# Agent-specific policy (overrides)
rateLimit:
  requestsPerMinute: 200  # Override
  burstLimit: 30          # Add

# Effective policy
rateLimit:
  requestsPerMinute: 200  # From agent policy
  burstLimit: 30          # From agent policy
```

---

## Violation Handling (C3 Detail)

### Violation Types

| Violation | Action | Logging |
|-----------|--------|---------|
| **Authorization failure** | Reject request | Log to DLQ |
| **Rate limit exceeded (reject)** | Reject with 429 | Log warning |
| **Rate limit exceeded (throttle)** | Delay dispatch | Log info |

### Violation Response

```json
{
  "violation": {
    "type": "rate_limit_exceeded",
    "policy": "fraud-analyst-policy",
    "agent_id": "fraud-analyst-acme-retail",
    "current_rate": 105,
    "limit": 100,
    "action": "throttle",
    "delay_ms": 500
  },
  "request_id": "req-12345",
  "timestamp": "2026-01-12T14:30:00Z"
}
```

### DLQ for Violations

Rejected requests are moved to Dead Letter Queue:

```yaml
# DLQ message
topic: sx.dlq.fraud-analyst-acme-retail
message:
  original_request:
    request_id: "req-12345"
    scenario: "fraud-investigation"
  violation:
    type: "authorization_failure"
    reason: "Update type 'delete' not allowed"
  timestamp: "2026-01-12T14:30:00Z"
  retries: 0
```

---

## Integration with Cipher IAM

### Authorization via Cipher IAM

For authorization policies, Cipher IAM can be consulted:

```python
async def _evaluate_authorization(self, policy, update):
    # Check if Cipher IAM authorization is required
    if policy.authorization.use_cipher_iam:
        iam_result = await self.cipher_iam.check_authorization(
            principal=update.source_principal,
            resource=f"agent/{policy.agent_id}",
            action="dispatch"
        )
        if not iam_result.allowed:
            return PolicyDecision(allowed=False, reason=iam_result.reason)
    
    # ... rest of authorization checks
```

---

## Related Documentation

- [Architecture](./architecture.md) — Overall architecture
- [Request Routing](./request-routing.md) — Routing algorithms
- [Cipher IAM Extensions](../cipher-iam-extensions/README.md) — IAM integration

---

*Subscription Policies provide flexible access control and rate limiting for request dispatch.*
