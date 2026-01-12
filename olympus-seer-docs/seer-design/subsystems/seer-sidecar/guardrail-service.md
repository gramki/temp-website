# Guardrail Service

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12  
> **Design Level**: C2 (Container)

---

## Overview

The Guardrail Service provides runtime enforcement for agent interactions through intercepting and validating traffic. Unlike the behavioral guidelines (prompt-based, advisory), the Guardrail Service provides **programmatic enforcement** that cannot be bypassed by the agent.

The service operates at two interception points:

1. **Inbound Guardrails** — Execute on `/dispatch` requests coming into the agent
2. **Outbound Guardrails** — Execute on every outbound Hub API call from the agent

---

## Guardrail Execution Model

### Inbound Guardrails

Inbound guardrails intercept requests on the `/dispatch` endpoint before they reach the agent container.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      INBOUND GUARDRAIL PIPELINE                              │
│                                                                              │
│   ┌─────────────┐                                                           │
│   │  Dispatch   │                                                           │
│   │  Request    │                                                           │
│   └──────┬──────┘                                                           │
│          │                                                                   │
│          ▼                                                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                    INBOUND GUARDRAILS                               │  │
│   │                                                                      │  │
│   │   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐            │  │
│   │   │Training │──►│Training │──►│Employ.  │──►│Employ.  │            │  │
│   │   │Guard 1  │   │Guard 2  │   │Guard 1  │   │Guard 2  │            │  │
│   │   └─────────┘   └─────────┘   └─────────┘   └─────────┘            │  │
│   │                                                                      │  │
│   │   Returns: Allow, Alert, Deny, Transform, Inject                    │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│          │                                                                   │
│          ▼                                                                   │
│   ┌─────────────┐                                                           │
│   │   Agent     │                                                           │
│   │  Container  │                                                           │
│   └─────────────┘                                                           │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Inbound Guardrail Actions:**

| Action | Description |
|--------|-------------|
| **Allow** | Request proceeds unchanged |
| **Alert** | Request proceeds, notification sent to observers |
| **Deny** | Request blocked with error response |
| **Transform** | Request modified before agent receives it |
| **Inject** | Context/headers added for agent to use |

### Outbound Guardrails

Outbound guardrails intercept every HTTP call from the agent container to Hub APIs. This includes:

- Request updates (`/api/agent/v1/requests/*/updates`)
- Decision submissions (`/api/agent/v1/decisions`)
- Task completions (`/api/agent/v1/tasks/*/complete`)
- Memory service calls
- Any other Hub API calls

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      OUTBOUND GUARDRAIL PIPELINE                             │
│                                                                              │
│   ┌─────────────┐                                                           │
│   │   Agent     │                                                           │
│   │  Container  │                                                           │
│   └──────┬──────┘                                                           │
│          │                                                                   │
│          │  POST /api/agent/v1/requests/{id}/updates                        │
│          │  POST /api/agent/v1/decisions                                    │
│          │  POST /api/agent/v1/tasks/{id}/complete                          │
│          │  ...                                                              │
│          ▼                                                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                    OUTBOUND GUARDRAILS                              │  │
│   │                                                                      │  │
│   │   Pattern Matching: /api/agent/v1/requests/*/updates                │  │
│   │                                                                      │  │
│   │   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐            │  │
│   │   │Training │──►│Training │──►│Employ.  │──►│Employ.  │            │  │
│   │   │Guard 1  │   │Guard 2  │   │Guard 1  │   │Guard 2  │            │  │
│   │   └─────────┘   └─────────┘   └─────────┘   └─────────┘            │  │
│   │                                                                      │  │
│   │   Returns: Allow, Alert, Deny, Transform, Redact                    │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│          │                                                                   │
│          ▼                                                                   │
│   ┌─────────────┐                                                           │
│   │  Hub API    │                                                           │
│   └─────────────┘                                                           │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Outbound Guardrail Actions:**

| Action | Description |
|--------|-------------|
| **Allow** | Call proceeds unchanged |
| **Alert** | Call proceeds, notification sent to observers |
| **Deny** | Call blocked with error response |
| **Transform** | Call payload modified before reaching Hub API |
| **Redact** | Sensitive content removed from payload |

---

## Guardrail Response Model

Each guardrail processor returns a **response** (the enforcement decision) along with optional **payload modifications**:

### Response Types

| Response | Behavior | Use Case |
|----------|----------|----------|
| **Allow** | Proceed with the operation | Content passes validation |
| **Alert** | Proceed but notify observers | Borderline content, requires monitoring |
| **Deny** | Block the operation | Policy violation detected |

### Payload Modifications

In addition to the response, guardrails can modify the payload:

| Modification | Applies To | Description |
|--------------|------------|-------------|
| **Transform** | Inbound/Outbound | Modify payload content |
| **Inject** | Inbound | Add context/headers for agent |
| **Redact** | Outbound | Remove sensitive content |

The response is determined by the guardrail's configuration schema. Each guardrail processor defines its own schema that influences when to return Allow, Alert, or Deny.

> **Terminology Note**: Guardrails use "Deny" for blocking operations. OPA policies (in Policy Enforcement Service) use "REJECT" for the same concept. Both result in blocking the operation.

```yaml
# Example: PII Detector configuration schema
config:
  sensitivity: high    # low, medium, high
  mode: deny           # deny, alert, redact
  # Based on sensitivity and mode, the guardrail returns:
  # - sensitivity: high + mode: deny → Deny on any PII detection
  # - sensitivity: low + mode: alert → Alert on confirmed PII only
```

---

## API Pattern Matching

Outbound guardrails can be configured for specific API endpoints using pattern matching with wildcard support:

| Pattern | Matches |
|---------|---------|
| `/api/agent/v1/decisions` | Exact match for decision submissions |
| `/api/agent/v1/requests/*/updates` | All request update endpoints |
| `/api/agent/v1/tasks/*/complete` | All task completion endpoints |
| `*` | All outbound API calls |

Pattern matching is evaluated in order of specificity:
1. Exact matches first
2. Wildcard patterns next
3. Catch-all (`*`) last

---

## Guardrail Configuration

### Training Spec Configuration

```yaml
# In TrainingSpec
spec:
  guardrails:
    # Inbound guardrails (on /dispatch requests)
    inbound:
      - ref:
          name: pii-detector
          namespace: seer-guardrails
        config:
          sensitivity: high
          mode: deny
      
      - ref:
          name: prompt-injection-detector
          namespace: seer-guardrails
        config:
          strictness: high
    
    # Outbound guardrails (on Hub API calls)
    outbound:
      # Default for all outbound APIs
      default:
        - ref:
            name: pii-redactor
            namespace: seer-guardrails
          config:
            sensitivity: medium
            mode: redact
      
      # Per-API guardrails
      apis:
        - pattern: "/api/agent/v1/decisions"
          guardrails:
            - ref:
                name: decision-validator
                namespace: seer-guardrails
              config:
                strict_mode: true
                on_violation: deny
        
        - pattern: "/api/agent/v1/requests/*/updates"
          guardrails:
            - ref:
                name: request-update-validator
                namespace: seer-guardrails
              config:
                on_violation: alert
        
        - pattern: "/api/agent/v1/tasks/*/complete"
          guardrails:
            - ref:
                name: task-completion-validator
                namespace: seer-guardrails
              config:
                on_violation: deny
```

### Employment Spec Configuration (Additions Only)

```yaml
# In EmploymentSpec (additional guardrails only)
spec:
  guardrails:
    inbound:
      - ref:
          name: acme-compliance-check
          namespace: acme-disputes
        config:
          regulations: ["GDPR", "CCPA"]
    
    outbound:
      apis:
        - pattern: "/api/agent/v1/decisions"
          guardrails:
            - ref:
                name: acme-decision-audit
                namespace: acme-disputes
              config:
                logLevel: detailed
```

---

## Execution Order

Guardrails execute in a deterministic order:

1. **Training Spec guardrails first** (in order specified)
2. **Employment Spec guardrails second** (in order specified)

This ensures Training guardrails (immutable) always execute before Employment additions.

```
Training Guard 1 → Training Guard 2 → Employment Guard 1 → Employment Guard 2
```

---

## Guardrail Immutability

| Action | Training Spec | Employment Spec |
|--------|---------------|-----------------|
| Define guardrails | ✅ Yes | ✅ Yes (additional only) |
| Remove guardrails | ❌ No (once published) | ❌ No (cannot remove Training) |
| Modify guardrail config | ❌ No (once published) | ❌ No (cannot modify Training) |
| Add new guardrails | N/A | ✅ Yes |

> **Key Principle**: Union of Training and Employment guardrails can only result in **stricter** enforcement.

---

## Failure Policy

Guardrail failure (crash, timeout, or error) defaults to **Deny** (fail-closed):

```yaml
spec:
  failurePolicy: deny  # DEFAULT - operation blocked if guardrail fails
  timeout: 5s
```

This ensures that enforcement is never bypassed due to guardrail failures.

---

## Guardrail Processor CRD

```yaml
apiVersion: seer.olympus.io/v1
kind: GuardrailProcessor
metadata:
  name: pii-detector
  namespace: seer-guardrails
  labels:
    seer.olympus.io/category: privacy
    seer.olympus.io/provider: platform
spec:
  displayName: "PII Detector"
  description: "Detects personally identifiable information"
  version: "1.2.0"
  
  # OCI image containing the Python library
  image:
    registry: registry.olympus.io
    repository: seer/guardrails/pii-detector
    tag: v1.2.0
    digest: sha256:abc123...
  
  # Execution capabilities
  capabilities:
    inbound: true
    outbound: true
  
  # Default failure policy
  failurePolicy: deny
  
  # Timeout
  timeout: 5s
  
  # Configuration schema (JSON Schema)
  configSchema:
    type: object
    properties:
      sensitivity:
        type: string
        enum: [low, medium, high]
        default: medium
      mode:
        type: string
        enum: [allow, alert, deny, redact]
        default: deny
      patterns:
        type: array
        items:
          type: string
    required: []
  
  # Error codes this guardrail can emit
  errorCodes:
    - code: GR-PII-001
      description: "PII detected in content"
      severity: high
    - code: GR-PII-002
      description: "Potential PII pattern detected"
      severity: medium
  
  # Resource requirements
  resources:
    cpu: "100m"
    memory: "128Mi"
```

---

## Guardrail Processor Interface

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Dict, Any, Literal

@dataclass
class GuardrailContext:
    """Context available to guardrails."""
    request_id: str
    tenant_id: str
    workbench_id: str
    scenario_id: str
    agent_id: str
    
    # Request/response payload
    payload: Dict[str, Any]
    
    # For outbound guardrails: API endpoint being called
    api_endpoint: Optional[str] = None
    api_method: Optional[str] = None
    
    # Configuration from spec
    config: Dict[str, Any] = None
    
    # Headers from previous guardrails
    headers: Dict[str, str] = None

@dataclass
class GuardrailResult:
    """Result of guardrail execution."""
    response: Literal["allow", "alert", "deny"]
    
    # Modified payload (for transform/redact)
    payload: Optional[Dict[str, Any]] = None
    
    # Error details (for deny)
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    
    # Headers to add
    headers: Dict[str, str] = None
    
    # Alert details (for alert)
    alert_details: Optional[Dict[str, Any]] = None

class InboundGuardrail(ABC):
    """Interface for inbound guardrails (on /dispatch requests)."""
    
    @abstractmethod
    def execute(self, context: GuardrailContext) -> GuardrailResult:
        """Execute guardrail on inbound dispatch request."""
        pass

class OutboundGuardrail(ABC):
    """Interface for outbound guardrails (on Hub API calls)."""
    
    @abstractmethod
    def execute(self, context: GuardrailContext) -> GuardrailResult:
        """Execute guardrail on outbound Hub API call."""
        pass
```

---

## Sidecar Deployment

The Guardrail Service is deployed as part of the Istio service mesh in Atlantis:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                         EMPLOYED AGENT POD                                   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                      ISTIO SIDECAR PROXY                            │  │
│   │                                                                      │  │
│   │   Intercepts all traffic to/from agent container                    │  │
│   │   Routes inbound /dispatch through guardrail containers             │  │
│   │   Routes outbound Hub API calls through guardrail containers        │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐          │
│   │   Guardrail     │   │   Guardrail     │   │   Agent         │          │
│   │   Container 1   │   │   Container 2   │   │   Container     │          │
│   │                 │   │                 │   │                 │          │
│   │   pii-detector  │   │   decision-     │   │   Raw Agent     │          │
│   │                 │   │   validator     │   │                 │          │
│   └─────────────────┘   └─────────────────┘   └─────────────────┘          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Integration Points

### Agent Runtime
- Guardrail configuration from Employment Spec → Sidecar deployment
- Pod composition includes guardrail containers

### Training Management
- Training Spec guardrails → Immutable guardrail configuration
- Guardrail processor references validated at training time

### Agent Lifecycle Manager
- Employment Spec guardrails → Additional guardrail configuration
- Guardrail changes trigger hot-reload

### Hot-reload Service
- Guardrail configuration updates → Runtime guardrail reload
- No pod restart required for configuration changes

### Istio Service Mesh
- Inbound request interception via Istio ingress
- Outbound call interception via Istio egress
- Pattern-based routing to appropriate guardrails

### Observability
- Metrics: `seer_guardrail_duration_seconds`, `seer_guardrail_result_total`
- Tracing: Guardrail spans in distributed traces
- Audit: Guardrail interventions logged to CAF

---

## Observability

### Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_guardrail_duration_seconds` | Execution time per guardrail | `guardrail`, `phase`, `api_pattern` |
| `seer_guardrail_result_total` | Count by response | `guardrail`, `phase`, `response` |
| `seer_guardrail_error_total` | Error count | `guardrail`, `error_code` |
| `seer_guardrail_timeout_total` | Timeout count | `guardrail`, `phase` |

### Tracing

```json
{
  "traceId": "trace-abc123",
  "spans": [
    {
      "name": "guardrail.inbound.pii-detector",
      "duration": 15,
      "response": "allow"
    },
    {
      "name": "agent.invoke",
      "duration": 2500
    },
    {
      "name": "guardrail.outbound.decision-validator",
      "duration": 12,
      "response": "allow",
      "tags": {
        "api_pattern": "/api/agent/v1/decisions"
      }
    }
  ]
}
```

### Audit

Guardrail interventions are logged to CAF:

```json
{
  "record_type": "guardrail_intervention",
  "request_id": "req-abc123",
  "guardrail": "pii-detector",
  "phase": "outbound",
  "api_pattern": "/api/agent/v1/requests/*/updates",
  "response": "deny",
  "error_code": "GR-PII-001",
  "timestamp": "2026-01-12T14:30:00Z"
}
```

---

## Related Documentation

- [Guardrails Concepts](../../implementation-concepts/guardrails.md) — Two-layer model, behavioral guidelines
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) — Guardrail configuration in Employment Spec
- [Training Spec CRD](../../hub-integration/training-spec-crd.md) — Guardrail specification
- [Employment Spec CRD](../../hub-integration/employment-spec-crd.md) — Additional guardrails
- [Hot-reload Service](./guardrail-hot-reload-service.md) — Configuration updates without restart
- [ADR-0072: Guardrails Two-Layer Model](../../../../olympus-hub-docs/decision-logs/0072-seer-guardrails-two-layer-model.md)

---

*Guardrail Service provides programmatic enforcement for agent interactions through inbound guardrails on dispatch requests and outbound guardrails on Hub API calls, with per-API configuration and Allow/Alert/Deny response model.*
