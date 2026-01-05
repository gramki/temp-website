# Hub Native Utilities

> **Status:** 🔴 Stub — Placeholder for expansion

Hub Native Utilities are **built-in capabilities** that Hub provides for use by Hub Applications and agents. These utilities are available to any Hub Application running on any Automation Runtime (Atlantis, Perseus, Rhea, ChronoShift, Seer).

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Provide reusable, Hub-managed capabilities for applications and agents |
| **Consumers** | Hub Applications, AI Agents, Human Agents |
| **Scope** | Platform-provided + Tenant-developed utilities |
| **Hosting** | Atlantis (Hub's container runtime) |

---

## Utility Categories

Hub Native Utilities include different types of capabilities:

### Decision & Prediction Tools (Stateless)

**Decision Tools** and **Prediction Tools** are specifically designed as **stateless, pure-function** utilities:

- **Stateless** — Output determined solely by input context (no hidden state)
- **Reproducible** — Same inputs always produce same outputs
- **CAF-Compliant** — Automatic audit capture for every invocation
- **Externalized** — Business logic separated from application code

This statelessness is a deliberate design choice for decisions and predictions to ensure:
- Auditability (all context is explicit)
- Testability (no side effects)
- Explainability (inputs fully capture decision basis)

### Other Native Utilities

Not all Hub utilities are stateless. Other utilities (to be detailed) may maintain state as required by their function:

- **Checklist Service** — Manages checklist instances and completion tracking (stateful)
- *Additional utilities to be defined*

---

## Why Decision & Prediction as Native Utilities?

Hub Applications often need to make decisions or predictions as part of their processing. By providing these as **native utilities**, Hub ensures:

1. **CAF Compliance** — Every invocation automatically:
   - Records the decision/prediction context
   - Captures the inputs and outputs
   - Links to the Request for audit trail
   - Produces explanation artifacts

2. **Reusability** — Decision logic is:
   - Defined once, invoked from any automation
   - Version-controlled and governed
   - Shared across Workbenches (with access control)

3. **Separation of Concerns** — Business logic is externalized:
   - Applications focus on orchestration
   - Decision rules managed by business analysts
   - Models managed by data scientists

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                   HUB NATIVE UTILITIES                           │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │         STATELESS TOOLS (Decision & Prediction)            ││
│  │                                                             ││
│  │  ┌─────────────────────────┐  ┌─────────────────────────┐  ││
│  │  │     DECISION TOOLS      │  │    PREDICTION TOOLS     │  ││
│  │  │                         │  │                         │  ││
│  │  │  • Drools Rule Engine   │  │  • ML Models (Elara)    │  ││
│  │  │  • DMN Decision Tables  │  │  • Scikit-learn         │  ││
│  │  │  • JS Pure Functions    │  │  • TensorFlow/PyTorch   │  ││
│  │  │                         │  │  • XGBoost/LightGBM     │  ││
│  │  └─────────────────────────┘  └─────────────────────────┘  ││
│  │                                                             ││
│  │  Characteristics: Stateless, CAF-compliant, Pure functions  ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │              OTHER UTILITIES (Stateful)                     ││
│  │                                                             ││
│  │  ┌─────────────────────────┐  ┌─────────────────────────┐  ││
│  │  │   Checklist Service     │  │    (Future Utilities)   │  ││
│  │  │   (TBD)                 │  │                         │  ││
│  │  └─────────────────────────┘  └─────────────────────────┘  ││
│  │                                                             ││
│  │  Characteristics: May maintain state as required            ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │              COMMON INFRASTRUCTURE                          ││
│  │                                                             ││
│  │  • Tool Registry Integration (discovery, access control)    ││
│  │  • Invocation Gateway (routing, auth)                       ││
│  │  • Versioning & Deployment (blue-green, canary)             ││
│  │  • CAF Integration (for Decision & Prediction tools)        ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

---

## Native Utility Inventory

### Stateless Tools (Decision & Prediction)

| Utility | Description | Status |
|---------|-------------|--------|
| [Decision Tools](./decision-tools.md) | Drools, DMN, JS pure-functions — stateless, CAF-compliant | 🔴 Stub |
| [Prediction Tools](./prediction-tools.md) | ML Models via Elara/Kserve — stateless, CAF-compliant | 🔴 Stub |
| [CAF Integration](./caf-integration.md) | Automatic cognitive audit for Decision & Prediction tools | 🔴 Stub |

### Other Utilities (Stateful)

| Utility | Description | Status |
|---------|-------------|--------|
| [Checklist Service](./checklist-service.md) | Workbench-scoped scheduled multi-operation governance | 🔴 Stub |
| [Routine Service](./routine-service.md) | Agent-scoped scheduled operations (personal or assigned) | 🔴 Stub |
| [Manual Task Application](./manual-task-application.md) | Pass-through app for manual tasks (1:1 Request-Task wiring) | 🔴 Stub |
| [HTTP Tool Calling Application](./http-tool-calling-application.md) | Simplified app for HTTP tool invocations with JS transformations | 🟡 Draft |
| *(Additional utilities to be defined)* | | |

---

## Decision & Prediction Tool Invocation

Decision and Prediction tools follow a consistent invocation pattern with automatic CAF integration:

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

## CAF-Aware Outputs (Decision & Prediction Tools)

Every Decision and Prediction tool invocation automatically produces CAF-compliant output:

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

