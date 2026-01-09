# Direct Tool Dispatcher

> **Status:** 🟡 Draft — Architecture defined

The Direct Tool Dispatcher is a **platform utility** that enables direct invocation of tools within a workbench, bypassing Signal Exchange and Request lifecycle. It acts as a proxy between callers (Hub Applications, I/O Gateways) and the machines hosting tools.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Enable direct, low-overhead tool invocation within a workbench |
| **Deployment** | Platform utility executing in (subscription, workbench) context |
| **Consumers** | Hub Applications, I/O Gateways, External Clients |
| **Bypass** | Signal Exchange, Request lifecycle |

---

## Why Direct Tool Dispatcher?

### The Problem

Not all tool invocations need the full Signal Exchange → Request → Application flow:

| SX/Request Flow | Direct Tool Invocation |
|-----------------|------------------------|
| Creates/updates a Request | No Request involved |
| Trigger evaluation overhead | Direct routing |
| Full observability/lifecycle | Lightweight observability |
| Audit as Request updates | Tool-level audit |
| Best for: operational scenarios | Best for: function calls, API-like operations |

### The Solution

The Direct Tool Dispatcher provides:

1. **Optimal Path** — Direct routing to tool without SX overhead
2. **Credential Management** — Configurable credential handling (pass-through or escalation)
3. **Access Control** — Enforcement at dispatcher level
4. **Observability** — Integrated with Olympus Watch
5. **Retry Logic** — Configurable retry with tool-defined policies

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        DIRECT TOOL DISPATCHER                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                       INVOCATION SOURCES                             │   │
│   │                                                                      │   │
│   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │   │
│   │  │ Hub Apps    │  │ I/O Gateway │  │ External    │                  │   │
│   │  │ (Internal)  │  │ (Heracles)  │  │ Clients     │                  │   │
│   │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘                  │   │
│   │         │                │                │                          │   │
│   └─────────┼────────────────┼────────────────┼──────────────────────────┘   │
│             │                │                │                              │
│             └────────────────┼────────────────┘                              │
│                              │                                               │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    DIRECT TOOL DISPATCHER                            │   │
│   │                                                                      │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                  Access Control Layer                        │   │   │
│   │   │  • Validate caller identity                                  │   │   │
│   │   │  • Check tool access permissions                             │   │   │
│   │   │  • Enforce OPA policies (if configured)                      │   │   │
│   │   └────────────────────────┬────────────────────────────────────┘   │   │
│   │                            │                                        │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                  Credential Resolver                         │   │   │
│   │   │  • Pass-through: Forward caller credentials                  │   │   │
│   │   │  • Configured: Use workbench-configured credentials          │   │   │
│   │   │  • Escalation: Use elevated credentials for target tool      │   │   │
│   │   └────────────────────────┬────────────────────────────────────┘   │   │
│   │                            │                                        │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                  Tool Router                                 │   │   │
│   │   │  • Resolve tool from Tool Registry                          │   │   │
│   │   │  • Determine target machine                                  │   │   │
│   │   │  • Apply retry configuration                                 │   │   │
│   │   └────────────────────────┬────────────────────────────────────┘   │   │
│   │                            │                                        │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                  Observability                               │   │   │
│   │   │  • Log invocation to Olympus Watch                          │   │   │
│   │   │  • Trace propagation                                         │   │   │
│   │   │  • Metrics collection                                        │   │   │
│   │   └────────────────────────┬────────────────────────────────────┘   │   │
│   │                            │                                        │   │
│   └────────────────────────────┼────────────────────────────────────────┘   │
│                                │                                             │
│                                ▼                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                         TARGET TOOLS                                 │   │
│   │                                                                      │   │
│   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │   │
│   │  │ Standalone  │  │ Machine     │  │ Decision/   │                  │   │
│   │  │ Tools       │  │ Tools       │  │ Prediction  │                  │   │
│   │  │ (WB-hosted) │  │ (External)  │  │ Tools       │                  │   │
│   │  └─────────────┘  └─────────────┘  └─────────────┘                  │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Capabilities

### 1. Credential Management

The dispatcher supports multiple credential handling modes:

| Mode | Description | Use Case |
|------|-------------|----------|
| **pass-through** | Forward caller's credentials to target tool | When tool should act on behalf of original caller |
| **configured** | Use workbench-configured credentials for the tool | When tool requires specific service account |
| **escalation** | Use elevated credentials for privileged operations | Controlled privilege escalation |

```yaml
# Credential configuration in Tool Definition
credential_mode: configured  # pass-through | configured | escalation

# For configured/escalation modes
credentials:
  type: oauth2_client_credentials
  client_id_env: TOOL_CLIENT_ID      # Environment variable name
  client_secret_env: TOOL_CLIENT_SECRET
```

### 2. Access Control

Access control is enforced at the dispatcher level:

| Source | Access Control |
|--------|----------------|
| **I/O Gateway** | Gateway-level controls already applied; dispatcher performs additional checks |
| **Hub Applications** | Dispatcher validates application's permission to invoke the tool |
| **External Clients** | Full access control at dispatcher (identity, role, OPA policy) |

```yaml
# Access control in Tool Definition
access_control:
  # Identity-based
  allowed_applications:
    - app-id-1
    - app-id-2
  
  # Role-based
  allowed_roles:
    - developer
    - service-operator
  
  # OPA policy (for complex rules)
  opa_policy_ref: policies/tool-access-policy
```

### 3. Retry Configuration

Retry behavior is defined in the Tool Definition but can be overridden by caller:

```yaml
# In Tool Definition
retry:
  enabled: true
  max_attempts: 3
  backoff:
    type: exponential  # constant | linear | exponential
    initial_delay_ms: 100
    max_delay_ms: 5000
    multiplier: 2
  retryable_status_codes:
    - 500
    - 502
    - 503
    - 504
  retryable_exceptions:
    - ConnectionTimeout
    - ServiceUnavailable
```

### 4. Observability Integration

All invocations are logged to Olympus Watch:

```yaml
# Automatic observability
observability:
  logging:
    level: info
    include_request: true
    include_response: false  # For PII protection
    
  metrics:
    - invocation_count
    - latency_p50
    - latency_p95
    - latency_p99
    - error_rate
    
  tracing:
    enabled: true
    propagate_context: true
```

---

## Invocation Flow

### Internal Invocation (Hub Application → Tool)

```
Hub Application                 Direct Tool Dispatcher              Target Tool
       │                               │                               │
       │ ── invoke tool ─────────────> │                               │
       │    (tool_id, params,          │                               │
       │     caller_context)           │                               │
       │                               │                               │
       │                               │ ── Resolve tool ────────────> │
       │                               │    from Tool Registry         │
       │                               │                               │
       │                               │ ── Validate access ─────────> │
       │                               │    (caller permitted?)        │
       │                               │                               │
       │                               │ ── Resolve credentials ─────> │
       │                               │    (pass-through or config)   │
       │                               │                               │
       │                               │ ── Invoke tool ─────────────> │
       │                               │    with resolved credentials  │
       │                               │                               │
       │                               │ <── Tool response ──────────  │
       │                               │                               │
       │                               │ ── Log to Olympus Watch ────> │
       │                               │                               │
       │ <── Tool response ─────────── │                               │
       │                               │                               │
```

### External Invocation (I/O Gateway → Tool)

When a workbench is exposed as a Machine (via Workbench-as-Machine pattern), external clients invoke tools through the I/O Gateway:

```
External Client       I/O Gateway (Heracles)     Direct Tool Dispatcher     Target Tool
       │                     │                          │                      │
       │ ── HTTP request ──> │                          │                      │
       │                     │ ── Authenticate ───────> │                      │
       │                     │    Route to tool         │                      │
       │                     │                          │                      │
       │                     │                          │ ── Access check ───> │
       │                     │                          │                      │
       │                     │                          │ ── Invoke tool ────> │
       │                     │                          │                      │
       │                     │ <── Response ─────────── │ <── Response ──────  │
       │ <── HTTP response ─ │                          │                      │
```

---

## Configuration

### Workbench-Level Configuration

```yaml
# In WorkbenchDeploymentSpec
direct_tool_dispatcher:
  enabled: true
  
  # Default credential mode for all tools
  default_credential_mode: pass-through
  
  # Default retry configuration
  default_retry:
    max_attempts: 3
    backoff:
      type: exponential
      initial_delay_ms: 100
      max_delay_ms: 5000
  
  # Observability
  observability:
    log_level: info
    metrics_enabled: true
    tracing_enabled: true
```

### Tool-Level Configuration

Each tool can override dispatcher behavior:

```yaml
# In ToolInstance or StandaloneToolSpec
dispatcher_config:
  # Credential handling
  credential_mode: configured
  credentials:
    type: oauth2_client_credentials
    client_id_env: CORE_BANKING_CLIENT_ID
    client_secret_env: CORE_BANKING_CLIENT_SECRET
  
  # Access control
  access_control:
    allowed_applications:
      - dispute-resolution-app
      - fraud-detection-app
    allowed_roles:
      - service-operator
  
  # Retry
  retry:
    max_attempts: 5
    backoff:
      type: exponential
      initial_delay_ms: 500
  
  # Timeout
  timeout_ms: 30000
```

---

## Use Cases

### 1. Hub Application Calling External Machine Tool

A Hub Application needs to call a core banking tool:

```python
# In Hub Application
async def check_account_balance(customer_id: str):
    # Direct tool invocation (no Request/SX involved)
    result = await tools.invoke(
        tool_id="core-banking/get-account-balance",
        params={"customer_id": customer_id}
    )
    return result["balance"]
```

### 2. Hub Application Calling Another Hub Application (Standalone Tool)

A fraud detection app is registered as a standalone tool and invoked directly:

```python
# In calling Hub Application
async def analyze_transaction(transaction: dict):
    # Direct invocation of fraud detection app as tool
    result = await tools.invoke(
        tool_id="fraud-detection-tool",
        params={"transaction": transaction}
    )
    return result["risk_score"]
```

### 3. External Client Calling Workbench Tool

When workbench is exposed as a machine, external clients call tools through Heracles:

```bash
curl -X POST https://heracles.hub.acme.com/tools/dispute-ops/create-dispute \
  -H "Authorization: Bearer ${CLIENT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"customer_id": "C123", "transaction_id": "T456", "amount": 100.00}'
```

---

## Security Considerations

### Credential Isolation

- Credentials are stored in environment variables, not in specs
- Environment variables are populated at deployment time from secure vault
- Credentials are never logged or exposed in responses

### Privilege Escalation Control

When using `escalation` credential mode:

1. Must be explicitly enabled per tool
2. Requires additional approval role
3. All escalated invocations are audited
4. OPA policy can enforce additional constraints

```yaml
# Controlled privilege escalation
credential_mode: escalation
escalation_control:
  requires_approval: true
  approval_role: security-officer
  audit_all: true
  opa_policy_ref: policies/escalation-policy
```

### Access Audit

All invocations are logged with:
- Caller identity
- Target tool
- Credential mode used
- Success/failure
- Duration

---

## Error Handling

### Error Response Format

```json
{
  "error": {
    "code": "TOOL_INVOCATION_FAILED",
    "message": "Failed to invoke tool after 3 attempts",
    "details": {
      "tool_id": "core-banking/get-account-balance",
      "last_error": "Connection timeout",
      "attempts": 3
    }
  },
  "trace_id": "abc123..."
}
```

### Error Codes

| Code | Description |
|------|-------------|
| `TOOL_NOT_FOUND` | Tool not registered in Tool Registry |
| `ACCESS_DENIED` | Caller not authorized to invoke tool |
| `CREDENTIAL_ERROR` | Failed to resolve/validate credentials |
| `TOOL_INVOCATION_FAILED` | Tool returned error or timed out |
| `RETRY_EXHAUSTED` | All retry attempts failed |

---

## Related Documentation

- [Tool Registry](../registry-services/tool-registry.md) — Tool registration and discovery
- [Hub Application as Standalone Tool](../../09-composite-systems-and-patterns/hub-application-as-standalone-tool.md) — Pattern for standalone tools
- [Workbench as a Machine](../../09-composite-systems-and-patterns/workbench-as-a-machine.md) — Pattern for exposing workbenches

---

*Direct Tool Dispatcher provides the optimal path for tool invocations that don't require Request lifecycle, enabling efficient machine-to-machine and application-to-tool communication within Hub.*

