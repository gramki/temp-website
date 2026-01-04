# Decision Tools

> **Status:** 🔴 Stub — Placeholder for expansion

Decision Tools are **stateless, pure-function decision services** that Hub provides as native capabilities. They externalize decision logic from Hub Applications, ensuring decisions are auditable, reproducible, and CAF-compliant.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Provide stateless, auditable decision capabilities |
| **Nature** | Pure functions — output determined solely by input context |
| **CAF Integration** | Automatic — all invocations produce audit artifacts |
| **Invocation** | Via Tool Registry, like any other Tool |
| **Hosting** | Atlantis (Hub's container runtime) |

---

## Why External Decision Tools?

Externalizing decisions from application logic provides:

| Benefit | Description |
|---------|-------------|
| **Auditability** | Every decision automatically captured with full context |
| **Reproducibility** | Same inputs → same outputs (no hidden state) |
| **Testability** | Decision logic tested independently of application |
| **Governance** | Decision rules managed by business analysts, not developers |
| **Reusability** | Same decision invoked from multiple applications |
| **Explainability** | Decision engines provide built-in explanation capabilities |

---

## Supported Decision Technologies

### Drools (Rule Engine)

| Aspect | Details |
|--------|---------|
| **Technology** | Drools (BRMS), JVM-based |
| **Format** | DRL (Drools Rule Language), Spreadsheet Decision Tables |
| **Use Cases** | Complex rule sets, business rules with many conditions |
| **Explanation** | Rule activation trace, agenda audit |

**Example Use Cases:**
- Transaction fraud scoring rules
- Loan eligibility determination
- Account status determination
- Regulatory threshold evaluation

### DMN (Decision Model and Notation)

| Aspect | Details |
|--------|---------|
| **Technology** | Kogito/Drools DMN Engine |
| **Format** | DMN 1.3 (XML), visual decision tables |
| **Use Cases** | Decision tables, structured decision logic |
| **Explanation** | Decision table trace, FEEL expression evaluation |

**Example Use Cases:**
- Credit scoring decision tables
- Pricing tier determination
- Risk classification
- Customer segment assignment

### JavaScript Pure Functions

| Aspect | Details |
|--------|---------|
| **Technology** | V8 (Node.js) or QuickJS (embedded) |
| **Format** | JavaScript/TypeScript functions |
| **Use Cases** | Custom logic, calculations, transformations |
| **Explanation** | Function execution trace (if instrumented) |

**Example Use Cases:**
- Custom calculation formulas
- Data transformation logic
- Validation rules
- Business-specific algorithms

---

## Decision Tool Registration

Decision tools are registered in the Tool Registry with additional metadata:

```yaml
tool:
  id: "credit-risk-decision"
  name: "Credit Risk Decision"
  namespace: "risk-management"
  
  # Tool type marker
  type: decision_tool
  
  # Decision engine
  decision_engine:
    type: enum          # drools | dmn | javascript
    version: string     # Engine version
    artifact_ref: string # Reference to deployed artifact
  
  # Input/Output
  input_schema:
    type: object
    properties:
      customer_id: { type: string }
      loan_amount: { type: number }
      income: { type: number }
      credit_history: { type: array }
  
  output_schema:
    type: object
    properties:
      decision: { type: string, enum: [approve, decline, refer] }
      risk_score: { type: number }
      factors: { type: array }
  
  # CAF configuration
  caf_config:
    explanation_level: enum   # minimal | standard | detailed
    context_capture: enum     # inputs_only | inputs_and_sources | full
    retention_policy: string  # Reference to retention policy
  
  # Access control (standard)
  access_control:
    discoverability: { ... }
    invocation: { ... }
```

---

## Invocation Pattern

```
Hub Application
        │
        │ POST /tools/credit-risk-decision/invoke
        │ {
        │   "context": {
        │     "customer_id": "CUST-123",
        │     "loan_amount": 50000,
        │     "income": 75000,
        │     "credit_history": [...]
        │   },
        │   "request_id": "REQ-456"  // For CAF linking
        │ }
        │
        ▼
┌─────────────────────────────────────────┐
│       Native Utility Gateway            │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│       Decision Engine (Drools)          │
│                                         │
│  1. Load rules                          │
│  2. Insert facts (input context)        │
│  3. Fire rules                          │
│  4. Capture explanation trace           │
│  5. Return result                       │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│       CAF Integration Layer             │
│                                         │
│  1. Record invocation                   │
│  2. Capture context snapshot            │
│  3. Store explanation                   │
│  4. Link to Request                     │
│  5. Generate audit reference            │
└────────────────┬────────────────────────┘
                 │
                 ▼
Response:
{
  "result": {
    "decision": "approve",
    "risk_score": 0.23,
    "factors": ["stable_income", "good_history"]
  },
  "caf_audit": {
    "invocation_id": "INV-789",
    "request_id": "REQ-456",
    "explanation": {
      "type": "rule_trace",
      "activated_rules": [
        "income-to-loan-ratio",
        "credit-history-check",
        "final-decision"
      ]
    },
    "audit_ref": "caf://decisions/INV-789"
  }
}
```

---

## Explanation Types

Each decision engine provides different explanation capabilities:

### Drools Explanation

```yaml
explanation:
  type: rule_trace
  activated_rules:
    - name: "income-ratio-check"
      condition: "income / loanAmount > 0.3"
      matched: true
    - name: "credit-history-positive"
      condition: "creditScore > 650"
      matched: true
  agenda_sequence:
    - "income-ratio-check" (priority: 100)
    - "credit-history-positive" (priority: 90)
    - "final-decision" (priority: 10)
```

### DMN Explanation

```yaml
explanation:
  type: decision_table_trace
  decision_table: "CreditDecision"
  input_entries:
    - input: "Income Range"
      value: "$50K-$100K"
      column: 2
    - input: "Credit Score"
      value: ">700"
      column: 3
  matched_rule: 5
  output: "Approve"
```

### JavaScript Explanation

```yaml
explanation:
  type: function_result
  function: "calculateRiskScore"
  # Note: JS functions require explicit instrumentation for detailed explanations
  result_breakdown:
    base_score: 0.5
    income_adjustment: -0.15
    history_adjustment: -0.12
    final_score: 0.23
```

---

## Development Workflow

### 1. Develop Decision Logic

```
Developer / Business Analyst
        │
        ├── Drools: Create .drl files or decision spreadsheets
        ├── DMN: Design decision tables in DMN modeler
        └── JavaScript: Write pure functions
```

### 2. Package Artifact

```yaml
# decision-artifact.yaml
artifact:
  id: "credit-risk-decision"
  version: "1.2.0"
  engine: drools
  
  # Drools-specific
  drools:
    kmodule: kmodule.xml
    rules:
      - rules/credit-scoring.drl
      - rules/final-decision.drl
    resources:
      - decision-tables/thresholds.xlsx
```

### 3. Deploy to Atlantis

```
Hub Console → Native Utilities → Decision Tools → Deploy
├── Select Artifact: [Upload or from artifact repository]
├── Version: 1.2.0
├── Environment: Production
└── Deployment Strategy: [Blue-Green / Canary / Rolling]
```

### 4. Register as Tool

Automatically registered upon successful deployment, or manually configure access control.

---

## Versioning

Decision tools support versioning for governance:

| Feature | Description |
|---------|-------------|
| **Semantic Versioning** | Major.Minor.Patch |
| **Multiple Active Versions** | Run old and new versions simultaneously |
| **Version Pinning** | Workbenches can pin to specific versions |
| **Deprecation** | Warn on deprecated version usage |
| **Audit Trail** | Which version was used for each decision |

---

## Related Documentation

- [Hub Native Utilities](./README.md) — Overview
- [Prediction Tools](./prediction-tools.md) — ML model serving
- [CAF Integration](./caf-integration.md) — Audit requirements
- [Tool Registry](../registry-services/tool-registry.md) — Registration

---

*TODO: Detailed design — Drools configuration, DMN modeling guidelines, JS sandbox restrictions*

