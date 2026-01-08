# Seer Guardrails

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08

---

## Overview

Seer Guardrails provide **safety constraints and enforcement** for AI agents. Guardrails operate at two levels:

1. **Behavioral Guidelines** — Advisory instructions embedded in agent prompts (not enforced programmatically)
2. **Sidecar Guardrails** — Enforcement functions that intercept and validate requests/responses

Both types are complementary: behavioral guidelines shape agent behavior, while sidecar guardrails provide programmatic enforcement.

> **Important**: Behavioral guidelines rely on LLM compliance and are advisory. Sidecar guardrails are the **actual enforcement layer**. Critical safety requirements should always have sidecar enforcement.

---

## Guardrail Types

### Behavioral Guidelines (Prompt-Based)

Behavioral guidelines are **advisory instructions** embedded in the Training Spec that shape agent behavior. They are **not programmatically enforced** — the agent may ignore them (especially under adversarial prompting).

```yaml
# In TrainingSpec
spec:
  behavioral:
    systemPrompt: |
      You are a Fraud Case Analyst...
    
    behavioralGuidelines:
      - name: pii-protection
        guideline: |
          CRITICAL SAFETY RULE: Never include personally identifiable 
          information (PII) in your responses. Always use entity 
          references like [CUSTOMER_ID] instead of actual names, 
          account numbers, or addresses.
      
      - name: scope-boundary
        guideline: |
          You are only authorized to handle fraud cases. If a request 
          is outside your scope (e.g., account closure, loan approval), 
          politely decline and suggest the appropriate channel.
```

**Key Characteristics:**
- Specified distinctly in Training Spec
- CAE ensures they are retained in compiled context
- **Advisory only** — not enforced programmatically
- LLMs can ignore guidelines (especially with jailbreaks)
- **Must be paired with sidecar guardrails** for critical safety requirements

> **Design Principle**: Never rely solely on behavioral guidelines for security-critical constraints. Always pair with sidecar enforcement.

#### Verification Pattern

For critical behavioral guidelines, add a sidecar guardrail that verifies compliance:

```yaml
# Behavioral guideline (advisory)
behavioralGuidelines:
  - name: pii-protection
    guideline: "Never include PII..."

# Sidecar enforcement (verification)
sidecarGuardrails:
  after:
    - ref: pii-detector
      config:
        mode: reject  # Enforces what the guideline advises
```

### Sidecar Guardrails

Sidecar guardrails are **enforcement functions** that execute before and/or after agent invocation:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      SIDECAR GUARDRAIL PIPELINE                               │
│                                                                               │
│   ┌─────────────┐                                                            │
│   │   Request   │                                                            │
│   └──────┬──────┘                                                            │
│          │                                                                    │
│          ▼                                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    BEFORE GUARDRAILS                                 │   │
│   │                                                                       │   │
│   │   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐             │   │
│   │   │Training │──►│Training │──►│Employ.  │──►│Employ.  │             │   │
│   │   │Guard 1  │   │Guard 2  │   │Guard 1  │   │Guard 2  │             │   │
│   │   └─────────┘   └─────────┘   └─────────┘   └─────────┘             │   │
│   │                                                                       │   │
│   │   Can: Transform request, Reject, Add context                        │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│          │                                                                    │
│          ▼                                                                    │
│   ┌─────────────┐                                                            │
│   │   Agent     │                                                            │
│   │  Container  │                                                            │
│   └──────┬──────┘                                                            │
│          │                                                                    │
│          ▼                                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    AFTER GUARDRAILS                                  │   │
│   │                                                                       │   │
│   │   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐             │   │
│   │   │Training │──►│Training │──►│Employ.  │──►│Employ.  │             │   │
│   │   │Guard 1  │   │Guard 2  │   │Guard 1  │   │Guard 2  │             │   │
│   │   └─────────┘   └─────────┘   └─────────┘   └─────────┘             │   │
│   │                                                                       │   │
│   │   Can: Transform response, Reject, Redact                            │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│          │                                                                    │
│          ▼                                                                    │
│   ┌─────────────┐                                                            │
│   │  Response   │                                                            │
│   └─────────────┘                                                            │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Execution Order

Guardrails execute in a deterministic order:

1. **Training Spec guardrails first** (in order specified)
2. **Employment Spec guardrails second** (in order specified)

This ensures Training guardrails (immutable) always execute before Employment additions.

```yaml
# Training Spec guardrails
guardrails:
  before:
    - ref: pii-detector          # Executes 1st
    - ref: prompt-injection      # Executes 2nd
  after:
    - ref: pii-redactor          # Executes 1st
    - ref: toxicity-filter       # Executes 2nd

# Employment Spec additional guardrails
guardrails:
  before:
    - ref: tenant-scope-check    # Executes 3rd (after Training)
  after:
    - ref: compliance-logger     # Executes 3rd (after Training)
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

## Guardrail Actions

### Before Guardrails

| Action | Description |
|--------|-------------|
| **Pass** | Allow request to proceed unchanged |
| **Transform** | Modify request before agent receives it |
| **Inject** | Add context/headers for agent to use |
| **Reject** | Block request entirely |

### After Guardrails

| Action | Description |
|--------|-------------|
| **Pass** | Allow response unchanged |
| **Transform** | Modify response before returning |
| **Redact** | Remove sensitive content from response |
| **Reject** | Block response entirely |

---

## Guardrail CRD

### Schema

```yaml
apiVersion: seer.olympus.io/v1
kind: GuardrailProcessor
metadata:
  name: pii-detector
  namespace: seer-guardrails  # Platform scope
  labels:
    seer.olympus.io/category: privacy
    seer.olympus.io/provider: platform
spec:
  # Processor metadata
  displayName: "PII Detector"
  description: "Detects personally identifiable information in requests/responses"
  version: "1.2.0"
  
  # OCI image containing the Python library
  image:
    registry: registry.olympus.io
    repository: seer/guardrails/pii-detector
    tag: v1.2.0
    digest: sha256:abc123...
  
  # Execution capabilities
  capabilities:
    before: true
    after: true
  
  # Default behavior on failure
  failurePolicy: deny  # deny | allow
  
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
      patterns:
        type: array
        items:
          type: string
        description: "Additional regex patterns to detect"
      redactWith:
        type: string
        default: "[REDACTED]"
    required: []
  
  # Error codes this guardrail can emit
  errorCodes:
    - code: GR-PII-001
      description: "PII detected in request content"
      severity: high
    - code: GR-PII-002
      description: "PII detected in response content"
      severity: high
    - code: GR-PII-003
      description: "Potential PII pattern detected (low confidence)"
      severity: medium
  
  # Resource requirements
  resources:
    cpu: "100m"
    memory: "128Mi"

status:
  state: active
  lastValidated: "2026-01-08T10:00:00Z"
  usageCount: 1250
```

### Tenant-Scoped Guardrails

Tenant-provided guardrails are registered at Workbench scope:

```yaml
apiVersion: seer.olympus.io/v1
kind: GuardrailProcessor
metadata:
  name: acme-compliance-check
  namespace: acme-disputes  # Tenant workbench
  labels:
    seer.olympus.io/category: compliance
    seer.olympus.io/provider: tenant
spec:
  displayName: "ACME Compliance Checker"
  description: "Tenant-specific compliance rules"
  # ... same schema as platform guardrails
```

Tenant guardrails:
- Managed by Tenant Admin
- Scoped to Workbench specifications
- Registered via Hub's artifact-registry and ci-subsystem
- Deployed by Hub operators

---

## Python Contract

### Guardrail Interface

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class GuardrailContext:
    """Context available to guardrails."""
    request_id: str
    tenant_id: str
    workbench_id: str
    scenario_id: str
    agent_id: str
    
    # Full request/response payload
    payload: Dict[str, Any]
    
    # Compiled context (if available)
    compiled_context: Optional[Dict[str, Any]]
    
    # Configuration from spec
    config: Dict[str, Any]
    
    # Headers from previous guardrails
    headers: Dict[str, str]

@dataclass
class GuardrailResult:
    """Result of guardrail execution."""
    action: str  # "pass", "transform", "reject", "redact"
    
    # Modified payload (for transform/redact)
    payload: Optional[Dict[str, Any]] = None
    
    # Error code (for reject)
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    
    # Headers to add
    headers: Dict[str, str] = None
    
    # Intervention details
    intervention: Optional[Dict[str, Any]] = None

class BeforeGuardrail(ABC):
    """Interface for before-request guardrails."""
    
    @abstractmethod
    def execute(self, context: GuardrailContext) -> GuardrailResult:
        """
        Execute guardrail on incoming request.
        
        Args:
            context: Full request context including payload and config
            
        Returns:
            GuardrailResult indicating action to take
        """
        pass

class AfterGuardrail(ABC):
    """Interface for after-response guardrails."""
    
    @abstractmethod
    def execute(self, context: GuardrailContext) -> GuardrailResult:
        """
        Execute guardrail on outgoing response.
        
        Args:
            context: Full response context including payload and config
            
        Returns:
            GuardrailResult indicating action to take
        """
        pass
```

### Example Implementation

```python
from seer_guardrails import BeforeGuardrail, AfterGuardrail, GuardrailContext, GuardrailResult
import re

class PIIDetector(BeforeGuardrail, AfterGuardrail):
    """Detects and optionally redacts PII."""
    
    # Common PII patterns
    PII_PATTERNS = {
        'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
    }
    
    def execute(self, context: GuardrailContext) -> GuardrailResult:
        sensitivity = context.config.get('sensitivity', 'medium')
        content = self._extract_content(context.payload)
        
        detections = self._detect_pii(content, sensitivity)
        
        if detections:
            if context.config.get('mode') == 'redact':
                # Redact and continue
                redacted_payload = self._redact(
                    context.payload, 
                    detections,
                    context.config.get('redactWith', '[REDACTED]')
                )
                return GuardrailResult(
                    action='transform',
                    payload=redacted_payload,
                    headers={
                        'X-Guardrail-PII-Detected': 'true',
                        'X-Guardrail-PII-Count': str(len(detections))
                    },
                    intervention={
                        'type': 'pii_redaction',
                        'count': len(detections),
                        'patterns': list(set(d['type'] for d in detections))
                    }
                )
            else:
                # Reject
                return GuardrailResult(
                    action='reject',
                    error_code='GR-PII-001',
                    error_message=f"PII detected: {len(detections)} instances",
                    headers={
                        'X-Guardrail-Error': 'GR-PII-001'
                    }
                )
        
        return GuardrailResult(action='pass')
    
    def _detect_pii(self, content: str, sensitivity: str) -> List[Dict]:
        detections = []
        patterns = self.PII_PATTERNS.copy()
        
        if sensitivity == 'high':
            patterns['name'] = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
        
        for pii_type, pattern in patterns.items():
            matches = re.finditer(pattern, content)
            for match in matches:
                detections.append({
                    'type': pii_type,
                    'start': match.start(),
                    'end': match.end()
                })
        
        return detections
    
    def _extract_content(self, payload: Dict) -> str:
        # Extract text content from payload
        return str(payload)
    
    def _redact(self, payload: Dict, detections: List, replacement: str) -> Dict:
        # Redact detected PII
        # Implementation details...
        return payload
```

### Guardrail with LLM

```python
from seer_guardrails import AfterGuardrail, GuardrailContext, GuardrailResult
from seer_sdk import ModelGateway

class ToxicityFilter(AfterGuardrail):
    """Uses LLM to detect toxic content."""
    
    def __init__(self):
        self.model = ModelGateway.from_environment()
    
    def execute(self, context: GuardrailContext) -> GuardrailResult:
        response_text = context.payload.get('response', {}).get('content', '')
        
        # Use LLM to assess toxicity
        assessment = self.model.complete(
            model=context.config.get('model', 'gpt-4o-mini'),
            messages=[
                {
                    "role": "system",
                    "content": "Assess the following text for toxicity. Respond with JSON: {\"toxic\": bool, \"score\": float, \"reason\": str}"
                },
                {
                    "role": "user",
                    "content": response_text
                }
            ],
            max_tokens=100
        )
        
        result = json.loads(assessment.content)
        threshold = context.config.get('threshold', 0.7)
        
        if result['toxic'] and result['score'] > threshold:
            return GuardrailResult(
                action='reject',
                error_code='GR-TOX-001',
                error_message=f"Toxic content detected: {result['reason']}",
                headers={
                    'X-Guardrail-Toxicity-Score': str(result['score'])
                }
            )
        
        return GuardrailResult(action='pass')
```

---

## Specification in Training/Employment

### Training Spec

```yaml
# In TrainingSpec
spec:
  guardrails:
    # Behavioral guidelines (advisory, not enforced)
    behavioralGuidelines:
      - name: pii-protection
        guideline: "Never include PII in responses..."
      - name: scope-boundary
        guideline: "Only handle fraud cases..."
    
    # Sidecar guardrails (enforced)
    before:
      - ref:
          name: pii-detector
          namespace: seer-guardrails
        config:
          sensitivity: high
          mode: reject
      
      - ref:
          name: prompt-injection-detector
          namespace: seer-guardrails
        config:
          strictness: high
    
    after:
      - ref:
          name: pii-detector
          namespace: seer-guardrails
        config:
          sensitivity: high
          mode: redact
          redactWith: "[PII_REDACTED]"
      
      - ref:
          name: toxicity-filter
          namespace: seer-guardrails
        config:
          threshold: 0.7
          model: gpt-4o-mini
```

### Employment Spec

```yaml
# In EmploymentSpec (additional guardrails only)
spec:
  guardrails:
    before:
      - ref:
          name: acme-compliance-check
          namespace: acme-disputes
        config:
          regulations: ["GDPR", "CCPA"]
    
    after:
      - ref:
          name: audit-logger
          namespace: acme-disputes
        config:
          logLevel: detailed
```

---

## HTTP Headers

Guardrails communicate via HTTP headers:

### Standard Headers

| Header | Description |
|--------|-------------|
| `X-Guardrail-Error` | Error code from rejecting guardrail |
| `X-Guardrail-Intervention` | JSON describing intervention taken |
| `X-Guardrail-Chain` | List of guardrails executed |
| `X-Guardrail-Latency-Ms` | Total guardrail execution time |

### Per-Guardrail Headers

Each guardrail can add custom headers with prefix:

```
X-Guardrail-{GuardrailName}-{Key}: {Value}
```

Example:
```
X-Guardrail-PII-Detected: true
X-Guardrail-PII-Count: 3
X-Guardrail-Toxicity-Score: 0.85
```

---

## Sidecar Deployment

Sidecar guardrails are deployed using Istio service mesh in Atlantis:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                         EMPLOYED AGENT POD                                    │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                      ISTIO SIDECAR PROXY                             │   │
│   │                                                                       │   │
│   │   Intercepts all traffic to/from agent container                     │   │
│   │   Routes through guardrail containers                                │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐           │
│   │   Guardrail     │   │   Guardrail     │   │   Agent         │           │
│   │   Container 1   │   │   Container 2   │   │   Container     │           │
│   │                 │   │                 │   │                 │           │
│   │   pii-detector  │   │   toxicity-     │   │   Raw Agent     │           │
│   │                 │   │   filter        │   │                 │           │
│   └─────────────────┘   └─────────────────┘   └─────────────────┘           │
│                                                                               │
│   Shared compute resources (CPU, Memory)                                     │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Execution Isolation

Each guardrail executes in its own:
- **Container** — Isolated filesystem, process space
- **Virtual environment** — Python dependencies isolated
- **Subprocess** — Crash isolation

---

## Error Handling

### Failure Policy

Each guardrail specifies its failure policy:

| Policy | Behavior |
|--------|----------|
| `deny` | On guardrail failure (crash/timeout), reject the request |
| `allow` | On guardrail failure, allow request to proceed |

```yaml
spec:
  failurePolicy: deny  # or 'allow'
  timeout: 5s
```

### Timeout Handling

```yaml
# Guardrail times out after 5 seconds
spec:
  timeout: 5s
  failurePolicy: deny

# Result: Request rejected with GR-TIMEOUT error
```

---

## Guardrail Access

Guardrails have the same access as agents:

| Resource | Access |
|----------|--------|
| **Request/Response** | Full payload view |
| **Compiled Context** | Read access |
| **Agent Memory** | Read access (current session) |
| **Enterprise Memory** | Via access tools |
| **Knowledge Bank** | Via search API |
| **CAE** | Full compile access |
| **Model Gateway** | LLM invocation |
| **Tools** | All agent-accessible tools |

---

## Observability

### Metrics

| Metric | Description |
|--------|-------------|
| `seer_guardrail_duration_seconds` | Execution time per guardrail |
| `seer_guardrail_result_total` | Count by action (pass/reject/transform) |
| `seer_guardrail_error_total` | Error count by code |
| `seer_guardrail_timeout_total` | Timeout count |

### Tracing

Guardrail execution is traced:

```json
{
  "traceId": "trace-abc123",
  "spans": [
    {
      "name": "guardrail.before.pii-detector",
      "duration": 15,
      "result": "pass"
    },
    {
      "name": "guardrail.before.prompt-injection",
      "duration": 8,
      "result": "pass"
    },
    {
      "name": "agent.invoke",
      "duration": 2500
    },
    {
      "name": "guardrail.after.pii-detector",
      "duration": 12,
      "result": "transform",
      "intervention": {"type": "redaction", "count": 2}
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
  "phase": "after",
  "action": "redact",
  "error_code": null,
  "intervention": {
    "type": "pii_redaction",
    "count": 2,
    "patterns": ["email", "phone"]
  },
  "timestamp": "2026-01-08T14:30:00Z"
}
```

---

## Platform vs Tenant Guardrails

| Aspect | Platform Guardrails | Tenant Guardrails |
|--------|---------------------|-------------------|
| **Scope** | All tenants | Workbench-scoped |
| **Managed By** | Seer publishers | Tenant Admin |
| **Change Management** | Platform governance | Tenant governance |
| **Registration** | seer-guardrails namespace | Workbench namespace |
| **Approval** | Platform team + Security | Tenant Admin |

---

## Design Considerations

### Latency Optimization

Guardrails add latency to every request. To mitigate:

#### Parallel Execution

Independent guardrails can execute in parallel:

```yaml
spec:
  guardrails:
    before:
      - ref: pii-detector
        parallel: true        # Can run in parallel
      - ref: prompt-injection
        parallel: true        # Can run in parallel
      - ref: scope-validator
        dependsOn: [pii-detector]  # Must wait for pii-detector
```

#### Pre-Warmed Worker Pools

To avoid subprocess startup overhead (~350ms), guardrails use pre-warmed worker pools:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      GUARDRAIL WORKER POOL                                   │
│                                                                               │
│   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐                     │
│   │ Worker  │   │ Worker  │   │ Worker  │   │ Worker  │  Pre-warmed         │
│   │   1     │   │   2     │   │   3     │   │   4     │  Python venvs       │
│   └─────────┘   └─────────┘   └─────────┘   └─────────┘                     │
│                                                                               │
│   New request → Dispatch to available worker → Execute → Return              │
│   (No subprocess fork, no venv load)                                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

Configuration:
```yaml
spec:
  workerPool:
    minWorkers: 2
    maxWorkers: 8
    idleTimeout: 300s
```

---

### Failure Policy

Default failure policy is **deny** (fail-closed):

```yaml
spec:
  failurePolicy: deny  # DEFAULT - request blocked if guardrail fails
```

Using `allow` (fail-open) requires explicit justification:

```yaml
spec:
  failurePolicy: allow
  failurePolicyJustification: "Non-critical logging guardrail, should not block requests"
```

> **Security Principle**: Fail-closed by default. Fail-open requires documented justification and should be audited regularly.

---

### LLM-Based Guardrails

LLM-based guardrails (e.g., toxicity detection) have special considerations:

#### Circuit Breakers

LLM calls go through **Model Gateway**, which provides circuit breakers:

```yaml
# Model Gateway handles:
- Rate limiting
- Timeout handling
- Fallback on model unavailability
- Token budget enforcement
```

#### Non-Determinism

LLM guardrails may produce different results on identical inputs:

```yaml
spec:
  llmGuardrails:
    determinism:
      cacheIdenticalInputs: true    # Cache results for same input
      cacheExpiry: 60s
      
      # For testing only
      deterministicMode: false      # Set true in test environments
      seed: 42                      # Fixed seed for reproducibility
```

#### Cost Implications

LLM guardrails double (or more) the LLM cost per request:

```
Request: 
  Agent LLM call:      1,000 tokens
  Guardrail LLM call:    500 tokens
  ----------------------------
  Total:               1,500 tokens (50% overhead)
```

Consider using smaller models for guardrail tasks:
```yaml
config:
  model: gpt-4o-mini    # Smaller, cheaper model for guardrail
```

---

### Testing Framework

Guardrails require systematic testing:

#### Unit Testing

```python
from seer_guardrails.testing import GuardrailTestHarness

def test_pii_detector_rejects_ssn():
    harness = GuardrailTestHarness(PIIDetector())
    
    result = harness.test_before(
        payload={"content": "SSN: 123-45-6789"},
        config={"sensitivity": "high"}
    )
    
    assert result.action == "reject"
    assert result.error_code == "GR-PII-001"

def test_pii_detector_passes_clean_content():
    harness = GuardrailTestHarness(PIIDetector())
    
    result = harness.test_before(
        payload={"content": "The transaction was approved"},
        config={"sensitivity": "high"}
    )
    
    assert result.action == "pass"
```

#### Pipeline Integration Testing

```python
from seer_guardrails.testing import PipelineTestHarness

def test_full_pipeline():
    pipeline = PipelineTestHarness(
        training_guardrails=[PIIDetector(), PromptInjection()],
        employment_guardrails=[ComplianceChecker()]
    )
    
    # Test that union of guardrails works correctly
    result = pipeline.test_request(
        payload={"content": "Check account 123-45-6789"},
        expected_action="reject",
        expected_stage="before"
    )
```

#### Deterministic Mode for LLM Guardrails

```python
from seer_guardrails.testing import DeterministicLLM

def test_toxicity_filter():
    with DeterministicLLM(responses={"toxic_input": {"toxic": True, "score": 0.9}}):
        harness = GuardrailTestHarness(ToxicityFilter())
        
        result = harness.test_after(
            payload={"response": {"content": "toxic_input"}},
            config={"threshold": 0.7}
        )
        
        assert result.action == "reject"
```

---

### Guardrail Composition

For complex logic requiring multiple guardrail outcomes:

```yaml
spec:
  guardrails:
    before:
      - ref: pii-detector
        id: pii
      - ref: toxicity-detector
        id: toxicity
      
      # Meta-guardrail that evaluates combined results
      - ref: composite-evaluator
        config:
          rules:
            - condition: "pii.detected AND toxicity.detected"
              action: reject
              escalate: true
            - condition: "pii.detected OR toxicity.detected"
              action: transform
              addReviewFlag: true
```

---

### Resource Management

Guardrails share pod resources. To prevent resource starvation:

```yaml
spec:
  resources:
    # Per-guardrail limits
    perGuardrail:
      cpu: "200m"
      memory: "256Mi"
      timeout: 5s
    
    # Total guardrail budget (all guardrails combined)
    totalBudget:
      cpu: "1"
      memory: "1Gi"
      
    # Reserve for agent (guaranteed)
    agentReserve:
      cpu: "2"
      memory: "4Gi"
```

---

## Related Documentation

- [Agent Lifecycle Service](./agent-lifecycle-service.md) — Guardrail immutability
- [Training Spec CRD](../hub-integration/training-spec-crd.md) — Guardrail specification
- [Employment Spec CRD](../hub-integration/employment-spec-crd.md) — Additional guardrails
- [Context Assembly Engine](./context-assembly-engine.md) — Behavioral guidelines in context
- [Model Gateway](./model-gateway.md) — LLM circuit breakers
- [Hub Artifact Registry](../../../olympus-hub-docs/04-subsystems/registry-services/README.md) — Tenant guardrail registration
- [Atlantis Runtime](../../../olympus-hub-docs/05-infrastructure/README.md) — Sidecar deployment

---

*Seer Guardrails provide defense-in-depth safety through behavioral guidelines and enforcement sidecars, with optimizations for latency, testing, and resource management.*

