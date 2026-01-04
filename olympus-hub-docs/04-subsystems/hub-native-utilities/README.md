# Hub Native Utilities

> **Status:** 🔴 Stub — Placeholder for expansion

Hub Native Utilities are **stateless, context-only tools** that Hub provides as built-in capabilities. These tools can be invoked by any Hub Application running on any Automation Runtime (Atlantis, Perseus, Rhea, ChronoShift, Seer).

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Provide reusable, CAF-aware decision and prediction capabilities |
| **Nature** | Stateless pure functions — all context passed as input |
| **Consumers** | Any Hub Application, regardless of Automation Runtime |
| **CAF Integration** | Automatic — all invocations produce CAF-compliant outputs |
| **Registration** | Registered as Tools in the Tool Registry |

---

## Why Native Utilities?

Hub Applications often need to make decisions or predictions as part of their processing. By providing these as **native utilities**, Hub ensures:

1. **Statelessness** — Decisions are pure functions, making them:
   - Reproducible (same input → same output)
   - Testable (no hidden state)
   - Auditable (all context is explicit)

2. **CAF Compliance** — Every invocation automatically:
   - Records the decision/prediction context
   - Captures the inputs and outputs
   - Links to the Request for audit trail
   - Produces explanation artifacts

3. **Reusability** — Decision logic is:
   - Defined once, invoked from any automation
   - Version-controlled and governed
   - Shared across Workbenches (with access control)

4. **Separation of Concerns** — Business logic is externalized:
   - Applications focus on orchestration
   - Decision rules managed by business analysts
   - Models managed by data scientists

---

## Utility Categories

```
┌─────────────────────────────────────────────────────────────────┐
│                   HUB NATIVE UTILITIES                           │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                  DECISION TOOLS                             ││
│  │                                                             ││
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐││
│  │  │   Drools     │ │     DMN      │ │  JS Pure Functions   │││
│  │  │  Rule Engine │ │ Decision     │ │  (V8/QuickJS)        │││
│  │  │              │ │ Model        │ │                      │││
│  │  └──────────────┘ └──────────────┘ └──────────────────────┘││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                 PREDICTION TOOLS                            ││
│  │                                                             ││
│  │  ┌──────────────────────────────────────────────────────┐  ││
│  │  │   ML Models (via Elara/Kserve on Atlantis)           │  ││
│  │  │                                                      │  ││
│  │  │   • Scikit-learn  • TensorFlow  • PyTorch           │  ││
│  │  │   • XGBoost       • LightGBM    • Custom Models     │  ││
│  │  └──────────────────────────────────────────────────────┘  ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │              COMMON INFRASTRUCTURE                          ││
│  │                                                             ││
│  │  • CAF Integration Layer (automatic audit capture)          ││
│  │  • Tool Registry Integration (discovery, access control)    ││
│  │  • Invocation Gateway (unified invoke pattern)              ││
│  │  • Versioning & Deployment (blue-green, canary)             ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

---

## Native Utility Inventory

| Utility | Description | Status |
|---------|-------------|--------|
| [Decision Tools](./decision-tools.md) | Drools, DMN, JS pure-functions | 🔴 Stub |
| [Prediction Tools](./prediction-tools.md) | ML Models via Elara/Kserve | 🔴 Stub |
| [CAF Integration](./caf-integration.md) | Automatic cognitive audit for all utilities | 🔴 Stub |

---

## Invocation Pattern

All native utilities follow a consistent invocation pattern:

```
Hub Application (any Runtime)
        │
        │ invoke tool: "credit-risk-decision"
        ▼
┌─────────────────────────────────────────┐
│         Tool Registry                    │
│  (resolve tool, check access, get spec)  │
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
└────────────────┬────────────────────────┘
                 │
                 ▼
        Response to Hub Application
        (result + CAF audit reference)
```

---

## CAF-Aware Outputs

Every native utility invocation produces CAF-compliant output:

```yaml
response:
  # Result
  result: object              # The decision/prediction outcome
  
  # CAF Audit Artifacts (automatically generated)
  caf_audit:
    invocation_id: string     # Unique invocation ID
    request_id: string        # Link to originating Request
    timestamp: datetime
    
    # Context snapshot
    context:
      inputs: object          # All inputs provided
      context_sources: array  # Where context came from (memory, knowledge, etc.)
    
    # Explanation
    explanation:
      type: enum              # rule_trace | feature_importance | decision_path
      details: object         # Engine-specific explanation
    
    # Confidence (for predictions)
    confidence: number        # 0.0 - 1.0 (if applicable)
    
    # Audit storage reference
    audit_ref: string         # Reference to stored audit record
```

---

## Hosting Infrastructure

Native utilities are hosted on **Atlantis** (Hub's container runtime):

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Decision Engines** | Drools (JVM), Kogito (DMN), V8/QuickJS (JS) | Execute decision logic |
| **Prediction Engines** | Elara (Kserve) | Serve ML models |
| **Gateway** | Hub Native Utility Gateway | Unified routing, CAF integration |
| **Registry** | Tool Registry | Discovery, access control, versioning |

---

## Tenant Development

Tenants can create and deploy their own Decision and Prediction tools:

1. **Develop** — Create decision rules (Drools/DMN) or train ML model
2. **Package** — Package as Hub-compatible artifact
3. **Register** — Register as Tool in Tool Registry
4. **Deploy** — Deploy to Atlantis (via Hub deployment pipeline)
5. **Invoke** — Available for any Hub Application to invoke

See [Decision Tools](./decision-tools.md) and [Prediction Tools](./prediction-tools.md) for detailed development guides.

---

## Access Control

Native utilities follow standard Tool Registry access control:

| Scope | Control |
|-------|---------|
| **Discoverability** | Which workbenches/roles can see the tool |
| **Invocation** | Which workbenches/roles can invoke the tool |
| **Deployment** | Who can deploy/update the tool (typically Developers, Process Architects) |

---

## Related Documentation

- [Tool Registry](../registry-services/tool-registry.md) — Tool registration and discovery
- [Cognitive Audit Fabric](../cognitive-audit-fabric/README.md) — CAF requirements
- [Atlantis Runtime](../automation-runtimes/atlantis-runtime.md) — Hosting infrastructure
- [Hub Applications](../../01-concepts/hub-applications.md) — Application concepts

---

*TODO: Detailed design — engine configurations, deployment pipeline, versioning strategy*

