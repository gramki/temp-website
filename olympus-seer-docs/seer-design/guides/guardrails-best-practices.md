# Guardrails Best Practices Guide

> **Audience**: Agent Developers, Domain Stewards, Tenant Admins  
> **Last Updated**: 2026-01-08

---

## Overview

This guide helps you design, implement, and manage guardrails effectively. Guardrails are powerful but can impact performance, cost, and user experience if misused.

**Key Principle**: Guardrails are a **shared responsibility** between platform, tenant admins, and developers.

---

## Responsibility Matrix

| Role | Responsibilities |
|------|------------------|
| **Platform Team** | Provide platform guardrails, maintain guardrail framework, set defaults |
| **Tenant Admin** | Approve tenant guardrails, set workbench policies, monitor costs |
| **Domain Steward** | Define domain-appropriate guardrails, review Training Specs |
| **Agent Developer** | Select guardrails, configure appropriately, test thoroughly |

---

## For Agent Developers

### Rule 1: Don't Rely Solely on Behavioral Guidelines

❌ **Wrong:**
```yaml
behavioralGuidelines:
  - name: pii-protection
    guideline: "Never include PII in responses"
# No enforcement — LLM can ignore this
```

✅ **Right:**
```yaml
behavioralGuidelines:
  - name: pii-protection
    guideline: "Never include PII in responses"

sidecarGuardrails:
  after:
    - ref: pii-detector
      config:
        mode: redact  # Enforces the guideline
```

**Why**: Behavioral guidelines are advisory. LLMs can ignore them, especially with adversarial prompts. Always pair critical guidelines with sidecar enforcement.

---

### Rule 2: Start with Platform Guardrails

Before creating custom guardrails, check what's already available:

```bash
# List available platform guardrails
seer guardrails list --scope platform

# Common platform guardrails:
# - pii-detector          (privacy)
# - prompt-injection      (security)
# - toxicity-filter       (safety)
# - hallucination-check   (accuracy)
# - scope-validator       (authorization)
```

**Why**: Platform guardrails are tested, optimized, and maintained by the platform team. Custom guardrails add maintenance burden.

---

### Rule 3: Minimize Guardrail Count

❌ **Wrong:**
```yaml
before:
  - ref: pii-detector
  - ref: prompt-injection
  - ref: scope-validator
  - ref: input-sanitizer
  - ref: rate-limiter
  - ref: content-classifier
  - ref: language-detector
  - ref: custom-check-1
  - ref: custom-check-2
# 9 guardrails = 9x latency overhead
```

✅ **Right:**
```yaml
before:
  - ref: pii-detector
  - ref: prompt-injection
  - ref: scope-validator
# Only critical guardrails
```

**Why**: Each guardrail adds latency. A pipeline with 10 guardrails at 50ms each adds 500ms+ to every request.

**Guideline**: Aim for 3-5 guardrails per phase (before/after).

---

### Rule 4: Use Parallel Execution

When guardrails are independent, run them in parallel:

```yaml
before:
  - ref: pii-detector
    parallel: true
  - ref: prompt-injection
    parallel: true
  - ref: toxicity-filter
    parallel: true
  # All three run simultaneously
```

**When NOT to parallelize:**
```yaml
before:
  - ref: input-sanitizer
    id: sanitizer
  - ref: pii-detector
    dependsOn: [sanitizer]  # Must wait for sanitized input
```

---

### Rule 5: Choose the Right Guardrail Type

| Need | Use |
|------|-----|
| Fast, deterministic checks | Rule-based guardrails |
| Pattern matching (PII, etc.) | Regex-based guardrails |
| Nuanced judgment | LLM-based guardrails (sparingly) |
| Complex validation | Custom Python guardrails |

**LLM Guardrails — Use Sparingly:**
```yaml
# LLM guardrails are:
# - Slow (100-500ms+ per call)
# - Expensive (additional token cost)
# - Non-deterministic (may give different results)

# Only use when rule-based approaches can't work
after:
  - ref: toxicity-filter
    config:
      model: gpt-4o-mini      # Use smallest capable model
      cacheIdenticalInputs: true  # Cache results
```

---

### Rule 6: Configure Sensitivity Appropriately

❌ **Wrong:**
```yaml
- ref: pii-detector
  config:
    sensitivity: high  # Everything in Training Spec
```

✅ **Right:**
```yaml
# Training Spec — Set reasonable defaults
- ref: pii-detector
  config:
    sensitivity: medium

# Employment Spec — Adjust for specific use case
- ref: pii-detector
  config:
    sensitivity: high  # Stricter for healthcare scenario
```

**Why**: Over-sensitive guardrails cause false positives, frustrating users and reducing agent effectiveness.

---

### Rule 7: Test Your Guardrail Pipeline

```python
# test_guardrails.py
from seer_guardrails.testing import PipelineTestHarness

class TestFraudAnalystGuardrails:
    
    def setup(self):
        self.pipeline = PipelineTestHarness.from_training_spec(
            "fraud-analyst-v2"
        )
    
    def test_blocks_pii_in_request(self):
        result = self.pipeline.test_before({
            "content": "Check account for John Smith, SSN 123-45-6789"
        })
        assert result.action == "reject"
    
    def test_allows_clean_request(self):
        result = self.pipeline.test_before({
            "content": "Check account [CUSTOMER_ID] for fraud indicators"
        })
        assert result.action == "pass"
    
    def test_redacts_pii_in_response(self):
        result = self.pipeline.test_after({
            "response": "Customer email is john@example.com"
        })
        assert result.action == "transform"
        assert "john@example.com" not in result.payload["response"]
    
    def test_latency_acceptable(self):
        # Ensure guardrails don't add excessive latency
        result = self.pipeline.test_before(
            {"content": "Normal request"},
            measure_latency=True
        )
        assert result.latency_ms < 100  # Max 100ms for before phase
```

---

### Rule 8: Handle Failures Gracefully

```yaml
# For critical security guardrails
- ref: pii-detector
  config:
    failurePolicy: deny  # Block if guardrail fails
    
# For non-critical logging/metrics guardrails
- ref: usage-logger
  config:
    failurePolicy: allow  # Don't block on logging failure
    failurePolicyJustification: "Logging only, not security-critical"
```

**Document your failure policies:**
| Guardrail | Failure Policy | Justification |
|-----------|----------------|---------------|
| pii-detector | deny | Security-critical |
| toxicity-filter | deny | Safety-critical |
| usage-logger | allow | Observability only |

---

## For Domain Stewards

### Rule 1: Define Domain-Appropriate Guardrails

Different domains have different requirements:

| Domain | Critical Guardrails |
|--------|---------------------|
| **Healthcare** | PII (HIPAA), PHI protection, medical advice disclaimers |
| **Finance** | PII, regulatory compliance, investment disclaimers |
| **Customer Service** | Toxicity, scope boundaries, escalation triggers |
| **Legal** | Privilege protection, jurisdiction awareness |

```yaml
# Healthcare domain example
guardrails:
  before:
    - ref: hipaa-compliance
    - ref: phi-detector
  after:
    - ref: medical-disclaimer-injector
    - ref: phi-redactor
```

---

### Rule 2: Review Training Specs Before Publication

Checklist for Training Spec review:

- [ ] All behavioral guidelines have sidecar enforcement
- [ ] Guardrail count is reasonable (3-5 per phase)
- [ ] LLM guardrails are justified and configured with small models
- [ ] Failure policies are appropriate (deny for security, allow only with justification)
- [ ] Parallel execution is used where possible
- [ ] Test coverage exists for guardrail pipeline

---

### Rule 3: Monitor Guardrail Effectiveness

Track these metrics:

| Metric | Target | Action if Exceeded |
|--------|--------|---------------------|
| **False Positive Rate** | < 5% | Reduce sensitivity |
| **False Negative Rate** | < 1% | Increase sensitivity or add guardrails |
| **Latency (before phase)** | < 100ms | Parallelize or reduce count |
| **Latency (after phase)** | < 150ms | Parallelize or reduce count |
| **LLM Guardrail Cost** | < 20% of agent cost | Use smaller models, add caching |

---

### Rule 4: Establish Guardrail Governance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      GUARDRAIL GOVERNANCE FLOW                               │
│                                                                               │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│   │ Developer   │────►│ Steward     │────►│ Publication │                   │
│   │ Proposes    │     │ Reviews     │     │             │                   │
│   └─────────────┘     └─────────────┘     └─────────────┘                   │
│                              │                                               │
│                              ▼                                               │
│                       ┌─────────────┐                                        │
│                       │ Checklist   │                                        │
│                       │ • Coverage  │                                        │
│                       │ • Latency   │                                        │
│                       │ • Cost      │                                        │
│                       │ • Testing   │                                        │
│                       └─────────────┘                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## For Tenant Admins

### Rule 1: Set Workbench-Level Policies

```yaml
# Workbench specification
spec:
  guardrailPolicies:
    # Minimum required guardrails for all agents
    required:
      - ref: pii-detector
      - ref: scope-validator
    
    # Banned guardrails (e.g., expensive LLM guardrails)
    prohibited:
      - ref: custom-llm-guardrail  # Too expensive
    
    # Cost limits
    maxLLMGuardrails: 2
    maxTotalGuardrails: 8
    
    # Latency budgets
    maxBeforeLatencyMs: 150
    maxAfterLatencyMs: 200
```

---

### Rule 2: Approve Custom Guardrails Carefully

Before approving a tenant custom guardrail:

- [ ] Is there a platform guardrail that does the same thing?
- [ ] Is the guardrail stateless and side-effect free?
- [ ] Has it been tested thoroughly?
- [ ] What's the performance impact?
- [ ] Who maintains it long-term?

```yaml
# Custom guardrail approval
apiVersion: seer.olympus.io/v1
kind: GuardrailApproval
metadata:
  name: approve-acme-compliance
spec:
  guardrail:
    name: acme-compliance-check
    namespace: acme-disputes
  approvedBy: tenant-admin@acme.com
  approvalDate: "2026-01-08"
  reviewDate: "2026-07-08"  # 6-month review
  conditions:
    - "Must not use LLM calls"
    - "Must complete in < 50ms"
```

---

### Rule 3: Monitor Costs

Guardrails can silently increase costs:

```
Monthly Cost Breakdown:
├── Agent LLM calls:           $10,000
├── Guardrail LLM calls:       $3,500  ← 35% overhead!
│   ├── toxicity-filter:       $2,000
│   └── hallucination-check:   $1,500
└── Total:                     $13,500
```

**Cost Optimization Actions:**
1. Replace LLM guardrails with rule-based where possible
2. Enable caching for LLM guardrails
3. Use smaller models (gpt-4o-mini vs gpt-4o)
4. Reduce sensitivity to lower invocation count

---

### Rule 4: Regular Audits

Quarterly guardrail audit:

| Check | Action |
|-------|--------|
| Guardrails with > 10% false positive rate | Tune or replace |
| Guardrails with > 100ms latency | Optimize or remove |
| LLM guardrails without caching | Enable caching |
| Custom guardrails without recent updates | Review necessity |
| Fail-open guardrails | Review justification |

---

## Quick Reference

### Optimal Configuration Checklist

```yaml
# ✅ Well-configured guardrail pipeline
spec:
  guardrails:
    behavioralGuidelines:
      - name: pii-protection
        guideline: "..."  # Advisory
    
    before:
      - ref: pii-detector        # Platform guardrail
        parallel: true
        config:
          sensitivity: medium
          failurePolicy: deny
      
      - ref: prompt-injection    # Platform guardrail
        parallel: true
        config:
          failurePolicy: deny
    
    after:
      - ref: pii-redactor        # Enforce guideline
        parallel: true
        config:
          mode: redact
          failurePolicy: deny
      
      - ref: usage-logger        # Non-critical
        parallel: true
        config:
          failurePolicy: allow
          failurePolicyJustification: "Logging only"
```

### Latency Budget

| Phase | Budget | Recommendation |
|-------|--------|----------------|
| Before | 100-150ms | 2-3 parallel guardrails |
| After | 150-200ms | 2-4 parallel guardrails |
| Total | 250-350ms | 5-7 guardrails maximum |

### Cost Comparison

| Guardrail Type | Cost per 1000 calls |
|----------------|---------------------|
| Rule-based | ~$0 |
| Regex-based | ~$0 |
| LLM (gpt-4o-mini) | ~$0.15-0.50 |
| LLM (gpt-4o) | ~$1.50-5.00 |
| Custom Python | ~$0 (compute only) |

---

## Related Documentation

- [Guardrails Subsystem](../subsystems/guardrails.md) — Technical specification
- [Training Spec CRD](../hub-integration/training-spec-crd.md) — Guardrail configuration
- [Employment Spec CRD](../hub-integration/employment-spec-crd.md) — Additional guardrails

---

*Effective guardrails balance safety with performance. Follow these guidelines to protect your agents without degrading user experience.*

