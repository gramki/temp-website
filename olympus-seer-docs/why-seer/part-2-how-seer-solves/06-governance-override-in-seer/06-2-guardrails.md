# 6.2 Guardrails

Guardrails are safety mechanisms that constrain agent behavior to acceptable boundaries. Unlike policies that govern *what* an agent can do, guardrails focus on *how* the agent behaves—preventing harmful, inappropriate, or non-compliant outputs regardless of intent.

## Types of Guardrails

| Guardrail Type | What It Protects Against | Example |
|----------------|-------------------------|---------|
| **Input guardrails** | Malicious or inappropriate inputs | Prompt injection, jailbreak attempts |
| **Output guardrails** | Harmful or non-compliant outputs | PII exposure, prohibited content |
| **Behavioral guardrails** | Unsafe behavioral patterns | Infinite loops, excessive tool calls |

## Guardrail Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   GUARDRAIL LAYERS                           │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │              INPUT GUARDRAILS                      │    │
│   │                                                    │    │
│   │   User Input → Validation → Sanitization → Pass    │    │
│   │                                                    │    │
│   │   • Prompt injection detection                     │    │
│   │   • Jailbreak pattern detection                    │    │
│   │   • Input length limits                            │    │
│   │   • PII detection and handling                     │    │
│   └───────────────────────────────────────────────────┘    │
│                            │                                │
│                            ▼                                │
│   ┌───────────────────────────────────────────────────┐    │
│   │           BEHAVIORAL GUARDRAILS                    │    │
│   │                                                    │    │
│   │   Agent Operation → Monitoring → Intervention      │    │
│   │                                                    │    │
│   │   • Loop detection                                 │    │
│   │   • Tool call rate limiting                        │    │
│   │   • Cost ceiling enforcement                       │    │
│   │   • Timeout enforcement                            │    │
│   └───────────────────────────────────────────────────┘    │
│                            │                                │
│                            ▼                                │
│   ┌───────────────────────────────────────────────────┐    │
│   │             OUTPUT GUARDRAILS                      │    │
│   │                                                    │    │
│   │   Agent Output → Check → Remediate → Deliver       │    │
│   │                                                    │    │
│   │   • PII redaction                                  │    │
│   │   • Prohibited content blocking                    │    │
│   │   • Factuality check (if enabled)                  │    │
│   │   • Required disclosures                           │    │
│   └───────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Input Guardrails

### Prompt Injection Detection

Detect attempts to override system instructions:

```yaml
input_guardrail:
  name: prompt-injection-detector
  type: pattern_detection
  
  patterns:
    - "ignore previous instructions"
    - "disregard your training"
    - "you are now"
    - regex: "system:\\s*"
    
  on_detection:
    action: block
    log_to: caf
    response: "I cannot process that request."
```

### Jailbreak Detection

Detect attempts to bypass safety constraints:

```yaml
input_guardrail:
  name: jailbreak-detector
  type: classifier
  model: jailbreak-classifier-v1
  threshold: 0.8
  
  on_detection:
    action: block
    log_to: caf
    alert: security-team
```

### PII Handling

Handle personal data in inputs:

```yaml
input_guardrail:
  name: pii-handler
  type: pii_detection
  
  categories:
    - ssn: mask
    - email: allow
    - phone: mask
    - credit_card: block
    
  on_detection:
    action: apply_handling
    log_to: caf
```

## Behavioral Guardrails

### Loop Detection

Prevent infinite reasoning loops:

```yaml
behavioral_guardrail:
  name: loop-detector
  
  triggers:
    - same_tool_call_count: 3  # Same tool called 3 times
    - total_turns: 20          # Max 20 reasoning turns
    - no_progress_turns: 5     # 5 turns with no forward progress
    
  on_trigger:
    action: escalate_to_human
    log_to: caf
    message: "Agent appears stuck in loop"
```

### Tool Rate Limiting

Prevent excessive tool usage:

```yaml
behavioral_guardrail:
  name: tool-rate-limiter
  
  limits:
    - tool: "*"
      max_per_minute: 30
    - tool: "expensive_api"
      max_per_minute: 5
      
  on_exceed:
    action: throttle
    log_to: caf
```

### Cost Ceiling

Enforce cost limits:

```yaml
behavioral_guardrail:
  name: cost-ceiling
  
  ceilings:
    per_request: 10.00
    per_hour: 100.00
    per_day: 500.00
    
  on_exceed:
    action: terminate_and_alert
    log_to: caf
```

## Output Guardrails

### PII Redaction

Prevent PII in outputs:

```yaml
output_guardrail:
  name: pii-redactor
  
  detect:
    - ssn
    - credit_card
    - email (if not explicitly requested)
    
  action: redact
  replacement: "[REDACTED]"
  log_to: caf
```

### Prohibited Content

Block inappropriate content:

```yaml
output_guardrail:
  name: content-blocker
  type: classifier
  model: content-safety-classifier
  
  categories:
    - hate_speech: block
    - violence: block
    - adult_content: block
    - self_harm: block
    
  on_detection:
    action: block
    fallback_response: "I cannot provide that information."
    log_to: caf
```

### Required Disclosures

Ensure mandatory statements are included:

```yaml
output_guardrail:
  name: disclosure-checker
  
  required_when:
    - action_type: financial_advice
      disclosure: "This is not personalized financial advice..."
    - action_type: dispute_decision
      disclosure: "You have the right to appeal..."
      
  on_missing:
    action: append_disclosure
    log_to: caf
```

## Guardrail Immutability

Guardrails defined in Training Spec cannot be relaxed at Employment:

```yaml
training_spec:
  guardrails:
    input:
      - prompt_injection_detection: required
      - jailbreak_detection: required
    output:
      - pii_redaction: required
    behavioral:
      - cost_ceiling: 50.00  # Max $50 per request
      
employment_spec:
  guardrails:
    behavioral:
      - cost_ceiling: 25.00  # Can reduce to $25
      # Cannot set to $100 - would exceed training ceiling
```

## Guardrail Audit

All guardrail evaluations are logged:

```yaml
guardrail_audit:
  timestamp: 2026-01-10T14:30:00Z
  request_id: req-abc123
  
  input_guardrails:
    - name: prompt-injection-detector
      result: pass
    - name: jailbreak-detector
      result: pass
      
  behavioral_guardrails:
    - name: loop-detector
      turns_so_far: 3
      result: pass
      
  output_guardrails:
    - name: pii-redactor
      detected: 1 email
      action: redacted
      result: remediated
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/guardrails.md`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-2-immutability-principle.md`
