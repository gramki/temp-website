# ADR-0025: Decision and Prediction Tools as Stateless Utilities

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub Applications frequently need to:
- Make business decisions (eligibility checks, risk assessments, approval logic)
- Generate predictions (fraud probability, customer churn, credit risk)

These operations are critical for business outcomes and require:
- **Auditability**: Full record of inputs, outputs, and rationale
- **Explainability**: Why a decision was made or prediction generated
- **Reproducibility**: Same inputs produce same outputs
- **Testability**: Easy to test without side effects

Traditional approaches embed decision/prediction logic in application code, making these requirements difficult to achieve.

## Decision

**Decision Tools** and **Prediction Tools** are designed as **stateless, pure-function** Hub Native Utilities:

1. **Stateless**: Output determined solely by input context—no hidden state

2. **Pure Functions**: No side effects, deterministic, reproducible

3. **CAF-Compliant**: Every invocation automatically captured in Cognitive Audit Fabric:
   - Input context
   - Output/decision
   - Explanation artifacts
   - Link to originating Request

4. **Externalized Logic**: Business logic separated from application code:
   - Applications focus on orchestration
   - Decision rules managed by business analysts
   - ML models managed by data scientists

### Implementation Technologies

| Tool Type | Technologies |
|-----------|--------------|
| **Decision Tools** | Drools Rule Engine, DMN Decision Tables, JavaScript Pure Functions |
| **Prediction Tools** | ML Models via Elara/Kserve, Scikit-learn, TensorFlow, XGBoost |

### Invocation Flow

```
Hub Application
       │
       │ invoke: "credit-risk-decision"
       ▼
┌─────────────────────────────────────────┐
│         Tool Registry                    │
│  (resolve, check access, get spec)       │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│       Native Utility Gateway            │
│  (route to appropriate engine)          │
└────────────────┬────────────────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
┌───────────────┐  ┌───────────────┐
│ Decision      │  │ Prediction    │
│ Engine        │  │ Engine        │
│ (Drools/DMN)  │  │ (Elara)       │
└───────┬───────┘  └───────┬───────┘
        │                  │
        └────────┬─────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│       CAF Integration Layer             │
│  (capture context, inputs, outputs,     │
│   generate explanation, link to request)│
└────────────────────────────────────────┘
```

## Alternatives Considered

### Alternative 1: Embed Logic in Application Code
Decision/prediction logic written directly in Hub Applications.

- **Pros**: Simpler development, no external tools
- **Cons**: Hard to audit, not reproducible, logic scattered across applications, difficult to test

### Alternative 2: External Decision Services (Stateful)
Call external decision services that may maintain state.

- **Pros**: Flexibility, existing services
- **Cons**: State complicates auditing, reproducibility issues, harder to explain

### Alternative 3: Database-Driven Rules (Stateful)
Store rules in database, evaluate at runtime.

- **Pros**: Dynamic rule updates
- **Cons**: Database state affects outcomes, harder to version, audit complexity

## Consequences

### Positive
- **Auditability**: Every decision/prediction automatically recorded with full context
- **Reproducibility**: Same inputs always produce same outputs (no hidden state)
- **Testability**: Pure functions easy to test in isolation
- **Explainability**: CAF integration provides explanation artifacts
- **Separation of Concerns**: Business logic externalized from application code
- **Reusability**: Decision/prediction tools shared across applications

### Negative
- **Statelessness Constraint**: Cannot consider historical patterns without explicit input
- **Learning Curve**: Teams must learn Drools/DMN/ML frameworks
- **Performance Overhead**: CAF logging adds some latency

### Neutral
- Tools hosted on Atlantis (Hub's container runtime)
- Tenants can develop and deploy their own decision/prediction tools
- Standard Tool Registry access control applies

## CAF-Aware Output

Every invocation produces CAF-compliant output:

```yaml
response:
  result: object              # The decision/prediction outcome
  
  caf_audit:
    invocation_id: string     # Unique invocation ID
    request_id: string        # Link to originating Request
    timestamp: datetime
    
    context:
      inputs: object          # All inputs provided
      context_sources: array  # Where context came from
    
    explanation:
      type: rule_trace | feature_importance | decision_path
      details: object         # Engine-specific explanation
    
    confidence: number        # 0.0 - 1.0 (for predictions)
    audit_ref: string         # Reference to stored audit record
```

## Why Statelessness Matters

| Concern | Stateful Approach | Stateless Approach |
|---------|-------------------|-------------------|
| **Audit Trail** | What state was active? | All context in inputs |
| **Reproducibility** | Depends on state at time of call | Always reproducible |
| **Testing** | Must mock state | Pure function testing |
| **Debugging** | "What state caused this?" | "What inputs caused this?" |
| **Explainability** | State may be hidden factor | All factors explicit |

## Related Decisions

- [ADR-0023: HTTP Tool Calling Application](./0023-http-tool-calling-application.md)
- [ADR-0024: JavaScript Transformation Functions](./0024-javascript-transformation-functions.md)

