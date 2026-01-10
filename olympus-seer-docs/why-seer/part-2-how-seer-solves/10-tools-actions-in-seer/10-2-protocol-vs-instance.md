# 10.2 Protocol vs. Instance

The Tool Registry distinguishes between abstract Tool Protocols and concrete Tool Instances. This separation enables reusable definitions, environment-specific bindings, and clean governance.

## The Distinction

| Aspect | Tool Protocol | Tool Instance |
|--------|---------------|---------------|
| **What** | Abstract capability | Concrete binding |
| **Contains** | Schema, description | Endpoint, credentials |
| **Scope** | Shared across environments | Per environment |
| **Ownership** | Platform/shared | Workbench/tenant |
| **Changes** | Versioned, approved | Deployment-specific |

## Why This Matters

### Reusability

One protocol, many instances:

```yaml
protocol: get-transaction-details
  │
  ├── instance: dev-transaction-service
  │   └── endpoint: https://dev.internal/txn
  │
  ├── instance: staging-transaction-service
  │   └── endpoint: https://staging.internal/txn
  │
  └── instance: prod-transaction-service
      └── endpoint: https://prod.internal/txn
```

### Environment Isolation

Agents use the same tool "name" but get environment-appropriate binding:

```python
# Agent code (same in all environments)
result = await tools.invoke("get-transaction-details", {
    "transaction_id": txn_id
})

# In dev: calls dev-transaction-service
# In prod: calls prod-transaction-service
```

### Credential Separation

Credentials are instance-specific:

```yaml
dev_instance:
  credentials_ref: dev-service-account
  
prod_instance:
  credentials_ref: prod-service-account (more restricted)
```

## Protocol Definition

```yaml
# Protocol defines WHAT the tool does
protocol:
  name: approve-refund
  
  description: "Approve a refund for a disputed transaction"
  
  input:
    type: object
    required: [case_id, amount]
    properties:
      case_id:
        type: string
      amount:
        type: number
        minimum: 0
        maximum: 10000
      reason:
        type: string
        
  output:
    type: object
    properties:
      refund_id:
        type: string
      status:
        type: string
        enum: [approved, pending, failed]
        
  side_effects:
    - "Creates refund transaction"
    - "Updates case status"
    - "Sends customer notification"
    
  risk_level: high
```

## Instance Definition

```yaml
# Instance defines HOW to call it
instance:
  name: acme-refund-api
  protocol: approve-refund
  
  binding:
    type: http
    endpoint: https://refunds.acme.internal/v1/refunds
    method: POST
    
    request_mapping:
      case_id: $.body.case_id
      amount: $.body.amount
      reason: $.body.reason
      
    response_mapping:
      refund_id: $.response.id
      status: $.response.status
      
  authentication:
    type: mtls
    certificate_ref: acme-refund-mtls-cert
    
  timeout: 30s
  retry:
    max_attempts: 2
    backoff: exponential
    
  circuit_breaker:
    failure_threshold: 5
    recovery_time: 30s
```

## Resolution Process

When agent invokes a tool:

```
Agent calls: invoke("approve-refund", params)
    │
    ▼
Registry resolves:
    │
    ├── Find protocol: approve-refund
    ├── Find instance for workbench: acme-refund-api
    ├── Verify agent access policy
    └── Return instance with binding
    │
    ▼
Tool Executor:
    │
    ├── Apply request mapping
    ├── Authenticate with credentials
    ├── Call endpoint
    ├── Apply response mapping
    └── Return normalized result
```

## Versioning

Protocols are versioned:

```yaml
protocol:
  name: approve-refund
  version: 2.0.0
  
  # Breaking change from v1
  input:
    required: [case_id, amount, justification]  # New required field
```

Instances specify protocol version:

```yaml
instance:
  protocol: approve-refund
  protocol_version: ">=2.0.0"  # Requires v2+
```

---

**References:**
*   `olympus-hub-docs/04-subsystems/registry-services/tool-registry.md`
*   `olympus-seer-docs/seer-design/hub-integration/tool-binding-crd.md`

